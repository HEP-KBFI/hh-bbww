/** \executable compDBBgrWeights
 *
 * Compute weights for the data-driven Drell-Yan background estimation,
 * cf. Section 9.2 of AN-2020/119 v6.
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#if __has_include (<FWCore/ParameterSetReader/interface/ParameterSetReader.h>)
#  include <FWCore/ParameterSetReader/interface/ParameterSetReader.h> // edm::readPSetsFrom()
#else
#  include <FWCore/PythonParameterSet/interface/MakeParameterSets.h> // edm::readPSetsFrom()
#endif

#include "FWCore/Utilities/interface/Exception.h"

#include "PhysicsTools/FWLite/interface/TFileService.h"
#include "DataFormats/FWLite/interface/InputSource.h"
#include "DataFormats/FWLite/interface/OutputFiles.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // checkCompatibleBinning, subtractHistograms

#include <TFile.h>
#include <TH1.h>
#include <TBenchmark.h>
#include <TMath.h>
#include <TString.h> // Form
#include <TError.h>  // gErrorAbortLevel, kError

#include <iostream>
#include <string>
#include <vector>
#include <assert.h>

typedef std::vector<std::string> vstring;

TFile* 
createOutputFile(const std::string& outputFilePath, const std::string& outputFileName)
{
  std::string outputFileName_full = outputFilePath;
  if ( outputFileName_full.find_last_of("/") != (outputFileName_full.size() - 1) ) outputFileName_full.append("/");
  outputFileName_full.append(outputFileName);
  TFile* outputFile = new TFile(outputFileName_full.data(), "RECREATE");
  return outputFile;
}

TH1* loadHistogram(TFile* inputFile, const std::string& histogramName, const std::string& process)
{
  std::string histogramName_process = Form(histogramName.data(), process.data());
  TH1* histogram = dynamic_cast<TH1*>(inputFile->Get(histogramName_process.data()));
  if ( !histogram )
    throw cms::Exception("comp_jetToTauFakeRate") 
      << "Failed to load histogram '" << histogramName << "' from file = " << inputFile->GetName() << " !!\n";
  return histogram;
}

TH1* 
compWeightHistogram(TFile* inputFile,
                    const std::string& processData_or_mc, const vstring& processesToSubtract,
                    const std::string& histogramName_numerator, const std::string& histogramName_denominator, const std::string& histogramName_weight)
{
  

  TH1* histogramData_or_mc_numerator = loadHistogram(inputFile, histogramName_numerator, processData_or_mc);
  std::vector<TH1*> histogramsToSubtract_numerator;
  for ( auto processToSubtract : processesToSubtract )
  {
    TH1* histogramToSubtract_numerator = loadHistogram(inputFile, histogramName_numerator, processToSubtract);
    histogramsToSubtract_numerator.push_back(histogramToSubtract_numerator);
  }
  TH1* histogram_numerator = subtractHistograms("numerator", histogramData_or_mc_numerator, histogramsToSubtract_numerator);

  TH1* histogramData_or_mc_denominator = loadHistogram(inputFile, histogramName_denominator, processData_or_mc);
  std::vector<TH1*> histogramsToSubtract_denominator;
  for ( auto processToSubtract : processesToSubtract )
  {
    TH1* histogramToSubtract_denominator = loadHistogram(inputFile, histogramName_denominator, processToSubtract);
    histogramsToSubtract_denominator.push_back(histogramToSubtract_denominator);
  }
  TH1* histogram_denominator = subtractHistograms("denominator", histogramData_or_mc_denominator, histogramsToSubtract_denominator);

  checkCompatibleBinning(histogram_numerator, histogram_denominator);

  TH1* histogram_weight = (TH1*)histogram_numerator->Clone(histogramName_weight.data());
  if ( !histogram_weight->GetSumw2N() ) histogram_weight->Sumw2();
  histogram_weight->Divide(histogram_denominator);

  delete histogram_numerator;
  delete histogram_denominator;

  return histogram_weight;
}

int main(int argc, char* argv[]) 
{
//--- throw an exception in case ROOT encounters an error
  gErrorAbortLevel = kError;

//--- parse command-line arguments
  if ( argc < 2 ) {
    std::cout << "Usage: " << argv[0] << " [parameters.py]" << std::endl;
    return EXIT_FAILURE;
  }

  std::cout << "<compDYBgrWeights>:" << std::endl;

//--- keep track of time it takes the macro to execute
  TBenchmark clock;
  clock.Start("compDYBgrWeights");

//--- read python configuration parameters
  if ( !edm::readPSetsFrom(argv[1])->existsAs<edm::ParameterSet>("process") ) 
    throw cms::Exception("comp_jetToTauFakeRate") 
      << "No ParameterSet 'process' found in configuration file = " << argv[1] << " !!\n";

  edm::ParameterSet cfg = edm::readPSetsFrom(argv[1])->getParameter<edm::ParameterSet>("process");

  edm::ParameterSet cfg_comp = cfg.getParameter<edm::ParameterSet>("compDYBgrWeights");
  
  std::string era = cfg_comp.getParameter<std::string>("era");

  bool isMC = cfg_comp.getParameter<bool>("isMC");

  std::string processData_or_mc;
  vstring processesToSubtract;
  if ( isMC )
  {
    processData_or_mc = cfg_comp.getParameter<std::string>("processMC");
  }
  else
  {
    processData_or_mc = cfg_comp.getParameter<std::string>("processData");
    processesToSubtract = cfg_comp.getParameter<vstring>("processesToSubtract");
  }

  std::string outputFilePath = cfg_comp.getParameter<std::string>("outputFilePath");

  fwlite::InputSource inputFiles(cfg); 
  if ( !(inputFiles.files().size() == 1) )
    throw cms::Exception("comp_jetToTauFakeRate") 
      << "Exactly one input file expected !!\n";
  TFile* inputFile = new TFile(inputFiles.files().front().data());
  if ( !inputFile ) throw cms::Exception("comp_jetToTauFakeRate") 
    << "Failed to open input file = '" << inputFiles.files().front() << "' !!\n";

  edm::VParameterSet cfg_categories = cfg_comp.getParameter<edm::VParameterSet>("categories");
  for ( edm::VParameterSet::const_iterator cfg_category = cfg_categories.begin();
        cfg_category != cfg_categories.end(); ++cfg_category ) {
    std::string histogramName1_numerator = cfg_category->getParameter<std::string>("numerator1");
    std::string histogramName1_denominator = cfg_category->getParameter<std::string>("denominator1");
    std::string histogramName1_weight = cfg_category->getParameter<std::string>("weight1");
    TH1* histogram1_weight = nullptr;
    if ( histogramName1_numerator != "" && histogramName1_denominator != "" && histogramName1_weight != "" )
    {
      histogram1_weight = compWeightHistogram(
        inputFile,
        processData_or_mc, processesToSubtract,
        histogramName1_numerator, histogramName1_denominator, histogramName1_weight
      );
    }

    std::string histogramName2_numerator = cfg_category->getParameter<std::string>("numerator2");
    std::string histogramName2_denominator = cfg_category->getParameter<std::string>("denominator2");
    std::string histogramName2_weight = cfg_category->getParameter<std::string>("weight2");
    TH1* histogram2_weight = nullptr;
    if ( histogramName2_numerator != "" && histogramName2_denominator != "" && histogramName2_weight != "" )
    {
      histogram2_weight = compWeightHistogram(
        inputFile,
        processData_or_mc, processesToSubtract,
        histogramName2_numerator, histogramName2_denominator, histogramName2_weight
      );
    }

    std::string outputFileName = cfg_category->getParameter<std::string>("outputFileName");
    std::string data_or_mc = ( isMC ) ? "mc" : "data";
    outputFileName = Form(outputFileName.data(), data_or_mc.data(), era.data());
    TFile* outputFile = createOutputFile(outputFilePath, outputFileName);
    outputFile->cd();
    if ( histogram1_weight ) histogram1_weight->Write();
    if ( histogram2_weight ) histogram2_weight->Write();
    delete outputFile;
    delete histogram1_weight;
    delete histogram2_weight;
  }

  delete inputFile;

  clock.Show("compDYBgrWeights");

  return 0;
}
