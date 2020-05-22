
/** \executable addBackgrounds
 *
 * Add "background" contributions of different MC samples.
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/PythonParameterSet/interface/MakeParameterSets.h"

#include "FWCore/Utilities/interface/Exception.h"

#include "PhysicsTools/FWLite/interface/TFileService.h"
#include "DataFormats/FWLite/interface/InputSource.h"
#include "DataFormats/FWLite/interface/OutputFiles.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h"
#include "tthAnalysis/HiggsToTauTau/interface/addBackgroundsAuxFunctions.h" // getSubdirectories, getSubdirectoryNames
#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h" // cmsException()

#include <TFile.h>
#include <TH1.h>
#include <TBenchmark.h>
#include <TMath.h>
#include <TError.h> // gErrorAbortLevel, kError
#include "TPRegexp.h"
#include "TDirectory.h"
#include "TList.h"
#include "TKey.h"
#include "TObject.h"

#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <cstdlib> // EXIT_SUCCESS, EXIT_FAILURE
#include <assert.h>

typedef std::vector<std::string> vstring;

bool sortbymax(const float &a,
		  const float &b)
{
  return (a > b);
}

float funcvalue(float bincenter, float xmin, float xmax) {
  float funcvalue_ = (bincenter - 0.5*(xmin+xmax))*2/(xmax-xmin);
  return funcvalue_;
}

void setHistName(TH1* hist) {

  TString histName = hist->GetName();
  TString histNameReplace;
  if(histName.Contains("mtop173p5")) {
    histNameReplace = histName.ReplaceAll("mtop173p5", "CMS_HHbbww_TT_mtopUp");
  }
  else if(histName.Contains("mtop171p5")) {
    histNameReplace = histName.ReplaceAll("mtop171p5", "CMS_HHbbww_TT_mtopDown");
  }
  else if( ! histName.Contains("CMS")) {
    histNameReplace = histName.Insert(0,"CMS_HHbbww_TT_");
  }
  else if( histName.Contains("CMS_ttHl")) {
    histNameReplace = histName.ReplaceAll("CMS_ttHl", "CMS_HHbbww");
  }
  
  hist->SetName(histNameReplace);

}

std::pair<TH1*, TH1*> add_syshist(TH1* hist_central, TH1* hist_up, TH1* hist_dn) {

  std::string histname = hist_central->GetName();
  for(int i=0; i<hist_central->GetNbinsX(); i++) {
    float bincont = hist_central->GetBinContent(i+1);
    float bincontup = hist_up->GetBinContent(i+1);
    float bincontdn = hist_dn->GetBinContent(i+1);
    float bincontnew = bincont + 0.5*(bincontup-bincontdn);
    hist_up->SetBinContent(i+1,bincontnew);
    bincontnew = bincont - 0.5*(bincontup-bincontdn);
    hist_dn->SetBinContent(i+1, bincontnew);
  }
  setHistName(hist_up);
  setHistName(hist_dn);
  return std::make_pair(hist_up,hist_dn);
}

void add_sysCR(TH1* hist_central, std::vector<std::string> histNames, const TDirectory* dir, std::string process_input) {

  std::vector<TH1*> hists_cr;

  for(unsigned int ihistName=0; ihistName<histNames.size(); ihistName++) {
    TString histName = hist_central->GetName();
    histName.Insert(0,histNames[ihistName]+"_");
    TH1* hist_cr = getHistogram(dir, process_input, histName.Data(), "", true);
    assert(hist_cr);
    hist_cr->Scale(hist_central->Integral()/hist_cr->Integral());
    hists_cr.push_back(hist_cr);
  }

  float xmin = hist_central->GetBinLowEdge(1);
  float xmax = hist_central->GetBinLowEdge(hist_central->GetNbinsX()) + hist_central->GetBinWidth(hist_central->GetNbinsX());

  std::string histNameUp = "CMS_HHbbww_TT_crUp_";
  histNameUp += hist_central->GetName();
  std::string histNameDown = "CMS_HHbbww_TT_crDown_";
  histNameDown += hist_central->GetName();
  TH1* hist_up = (TH1*) hist_central->Clone(histNameUp.data());
  TH1* hist_dn = (TH1*) hist_central->Clone(histNameDown.data());

  std::vector<float> hist_diff;
  for(int i=0; i<hist_central->GetNbinsX(); i++) {
    float bincont = hist_central->GetBinContent(i+1);
    hist_diff.clear();
    for(unsigned int hist_cr=0; hist_cr<hists_cr.size(); hist_cr++) {
      float bincont_shift = hists_cr[hist_cr]->GetBinContent(i+1);
      float bin_diff = fabs(bincont-bincont_shift);
      hist_diff.push_back(bin_diff);
    }
    sort(hist_diff.begin(), hist_diff.end(), sortbymax);
    float bincenter = hist_central->GetXaxis()->GetBinCenter(i+1);
    float funcvalue_ = funcvalue(bincenter, xmin, xmax);
    float maxdiff = hist_diff[0];
    float bincontnew = bincont + maxdiff*funcvalue_;
    hist_up->SetBinContent(i+1, bincontnew);
    bincontnew = bincont - maxdiff*funcvalue_;
    hist_dn->SetBinContent(i+1, bincontnew);
  }
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

  std::cout << "<addSysTT>:\n";

//--- keep track of time it takes the macro to execute
  TBenchmark clock;
  clock.Start("addBackgrounds");

//--- read python configuration parameters
  if ( !edm::readPSetsFrom(argv[1])->existsAs<edm::ParameterSet>("process") )
    throw cmsException(__func__, __LINE__)
      << "No ParameterSet 'process' found in configuration file = " << argv[1];

  edm::ParameterSet cfg = edm::readPSetsFrom(argv[1])->getParameter<edm::ParameterSet>("process");

  edm::ParameterSet cfgAddSysTT = cfg.getParameter<edm::ParameterSet>("addSysTT");

  vstring categories = cfgAddSysTT.getParameter<vstring>("categories");

  vstring central_or_shifts = cfgAddSysTT.getParameter<vstring>("sysShifts");

  vstring processes_input = cfgAddSysTT.getParameter<vstring>("processes_input");
  std::string process_output = cfgAddSysTT.getParameter<std::string>("process_output");

  fwlite::InputSource inputFiles(cfg);
  if ( !(inputFiles.files().size() == 1) )
    throw cmsException(__func__, __LINE__) << "Exactly one input file expected";
  TFile* inputFile = new TFile(inputFiles.files().front().data());

  fwlite::OutputFiles outputFile(cfg);
  fwlite::TFileService fs = fwlite::TFileService(outputFile.file().data());

  if ( categories.size() == 0 ) categories = getSubdirectoryNames(inputFile);

  for(const std::string & category: categories)
  {
    std::cout << "processing category = " << category << '\n';
    TDirectory* dir = getDirectory(inputFile, category, true);
    assert(dir);
    std::vector<const TDirectory*> subdirs_level1 = getSubdirectories(dir);

    for(const TDirectory * subdir_level1: subdirs_level1)
      {  
	if(std::string(subdir_level1->GetName()).find("unbiased") != std::string::npos) continue;

	std::vector<const TDirectory*> subdirs_level2 = getSubdirectories(subdir_level1);
	for(const TDirectory * subdir_level2: subdirs_level2)
	  {
	    if(std::string(subdir_level2->GetName()).find("cutFlow") != std::string::npos) continue;
	    std::cout << " processing directory = " << Form("%s/%s", subdir_level1->GetName(), subdir_level2->GetName()) << '\n';

	    std::string the_process_input = "TT";
	    TDirectory * dir_input = dynamic_cast<TDirectory *>((const_cast<TDirectory *>(subdir_level2))->Get(the_process_input.data()));
	    assert(dir_input);
	    TList* list = dir_input->GetListOfKeys();
	    bool addedCR(false);
	    for(std::string central_or_shift: central_or_shifts) {
	      std::set<TString> histograms;
	      TIter next(list);
	      TKey* key = 0;
	      std::string find_histogramUp; std::string find_histogramDown;
	      if(central_or_shift == "mtop") {
		find_histogramUp = "mtop173p5_";
		find_histogramDown = "mtop171p5_";
	      }
	      else {
		find_histogramUp = central_or_shift + "Up_";
		find_histogramDown = central_or_shift + "Down_";
	      }
	      while ( (key = dynamic_cast<TKey*>(next())) ) {
		TObject* object = key->ReadObj();
		TH1* histogram = dynamic_cast<TH1*>(object);
		if ( !histogram ) continue;
		std::string histogramName = histogram->GetName();
		if(histogramName.find(find_histogramUp.data()) != std::string::npos) {
		  histograms.insert((TString)histogramName);
		}
	      }//while
	      
	      std::pair<TH1*, TH1*> hists_updn;
	      
	      for(const std::string & process_input: processes_input)
		{
		  std::string subdirName_output = Form(
		      "%s/%s/%s/%s", category.data(), subdir_level1->GetName(), subdir_level2->GetName(), process_input.data()
		    );
		  TDirectory * subdir_output = createSubdirectory_recursively(fs, subdirName_output);
		  subdir_output->cd();

		  for(TString  histogram: histograms)
		    {
		      std::string histogramName =  histogram.Data();
		      TH1 * histogram_up = getHistogram(subdir_level2, process_input, histogramName, "", true);
		      assert(histogram_up);
		      histogramName = histogram.ReplaceAll(Form("%s",find_histogramUp.data()), Form("%s", find_histogramDown.data())).Data();
		      TH1 * histogram_dn = getHistogram(subdir_level2, process_input, histogramName, "", true);
		      assert(histogram_dn);
		      histogramName = histogram.ReplaceAll(Form("%s",find_histogramDown.data()), "").Data();
		      TH1* histogram_central = getHistogram(subdir_level2, process_input, histogramName, "", true);
		      assert(histogram_central);
		      hists_updn = add_syshist(histogram_central, histogram_up, histogram_dn);
		      if(! addedCR) add_sysCR(histogram_central, {"QCDbased","GluonMove", "erdON"}, subdir_level2, process_input.data());
		      hists_updn.first->Write();
		      hists_updn.second->Write();
		    }//histogramName
		}// process_input
	      addedCR = true;
	    }//isys
	  }//subdir_level2
      }//subdir_level1
  }//categories

  //---------------------------------------------------------------------------------------------------
  // CV: Add (dummy) histograms for number of analyzed and processed events
  //     This is needed to avoid run-time errors/warnings when executing python/commands/get_events_count.py (called by python/sbatch-node.template.hadd.sh)
  fs.make<TH1D>("analyzedEntries", "analyzedEntries", 1, -0.5, +0.5);
  fs.make<TH1D>("selectedEntries", "selectedEntries", 1, -0.5, +0.5);
  //---------------------------------------------------------------------------------------------------

  delete inputFile;

  clock.Show("addSysTT");

  std::cout << "returning exit code = " << EXIT_SUCCESS << " (EXIT_SUCCESS)." << std::endl;
  return EXIT_SUCCESS;
}
