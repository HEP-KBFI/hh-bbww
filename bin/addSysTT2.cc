
/** \executable addSysTT
 *
 * Compute systematic uncertainty on TT background.
 *
 * \author Saswati Nandan, Tallinn
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

namespace
{
  bool sortbyfirstmax(const std::pair<float,float> &a,
                      const std::pair<float,float> &b)
  {
    return (a.first > b.first);
  }

  float sqr(float x) 
  {
    return x*x;
  }

  float funcvalue(float bincenter, float xmin, float xmax) 
  {
    float funcvalue_ = (bincenter - 0.5*(xmin+xmax))*2/(xmax-xmin);
    return funcvalue_;
  }

  void setHistName(TH1* hist) 
  {
    TString histName = hist->GetName();
    TString histNameReplace;
    if ( histName.Contains("mtop173p5") ) 
    {
      histNameReplace = histName.ReplaceAll("mtop173p5", "CMS_HHbbww_TT_mtopUp");
    }
    else if ( histName.Contains("mtop171p5") ) 
    {
      histNameReplace = histName.ReplaceAll("mtop171p5", "CMS_HHbbww_TT_mtopDown");
    }
    else if ( !histName.Contains("CMS") ) 
    {
      histNameReplace = histName.Insert(0,"CMS_HHbbww_TT_");
    }
    else if ( histName.Contains("CMS_ttHl") ) 
    {
      histNameReplace = histName.ReplaceAll("CMS_ttHl", "CMS_HHbbww");
    }
    hist->SetName(histNameReplace);
  }

  std::pair<TH1*, TH1*> add_syshist(TH1* hist_central, TH1* hist_up, TH1* hist_dn) 
  {
    std::string histname = hist_central->GetName();
    for ( int i = 0; i < hist_central->GetNbinsX(); ++i ) 
    {
      float bincont = hist_central->GetBinContent(i+1);
      float bincontErr = hist_central->GetBinError(i+1);
      float bincontup = hist_up->GetBinContent(i+1);
      float bincontupErr = hist_up->GetBinError(i+1);
      float bincontdn = hist_dn->GetBinContent(i+1);
      float bincontdnErr = hist_dn->GetBinError(i+1);
      float bincontnew = bincont + 0.5*(bincontup-bincontdn);
      float bincontnewErr = std::sqrt(sqr(bincontErr) + sqr(0.5) * ( sqr(bincontupErr) + sqr(bincontdnErr)));
      hist_up->SetBinContent(i+1,bincontnew);
      hist_up->SetBinError(i+1,bincontnewErr);
      bincontnew = bincont - 0.5*(bincontup-bincontdn);
      bincontnewErr = std::sqrt(sqr(bincontErr) + sqr(0.5) * ( sqr(bincontupErr) + sqr(bincontdnErr)));
      hist_dn->SetBinContent(i+1, bincontnew);
      hist_dn->SetBinError(i+1, bincontnewErr);
    }
    setHistName(hist_up);
    setHistName(hist_dn);
    return std::make_pair(hist_up,hist_dn);
  }

  void add_sysCR(TH1* hist_central, const std::vector<std::string>& histNames, const TDirectory* dir, const std::string& process_input) 
  {
    std::vector<TH1*> hists_cr;

    for ( unsigned int ihistName = 0; ihistName < histNames.size(); ++ihistName ) 
    {
      TString histName = hist_central->GetName();
      histName.Insert(0,histNames[ihistName]+"_");
      TH1* hist_cr = getHistogram(dir, process_input, histName.Data(), "", true);
      assert(hist_cr);
      hist_cr->Scale(hist_central->Integral()/hist_cr->Integral());
      hists_cr.push_back(hist_cr);
    }

    std::string histNameUp = "CMS_HHbbww_TT_crUp_";
    histNameUp += hist_central->GetName();
    std::string histNameDown = "CMS_HHbbww_TT_crDown_";
    histNameDown += hist_central->GetName();
    TH1* hist_up = (TH1*) hist_central->Clone(histNameUp.data());
    TH1* hist_dn = (TH1*) hist_central->Clone(histNameDown.data());

    float xmin = hist_central->GetBinLowEdge(1);
    float xmax = hist_central->GetBinLowEdge(hist_central->GetNbinsX()) + hist_central->GetBinWidth(hist_central->GetNbinsX());

    std::vector<std::pair<float, float> > hist_diff;
    for ( int i = 0; i < hist_central->GetNbinsX(); ++i ) 
    {
      float bincont = hist_central->GetBinContent(i+1);
      float bincontErr = hist_central->GetBinError(i+1);
      hist_diff.clear();
      for ( size_t hist_cr = 0; hist_cr < hists_cr.size(); ++hist_cr ) 
      {
        float bincont_shift = hists_cr[hist_cr]->GetBinContent(i+1);
        float bincont_shiftErr = hists_cr[hist_cr]->GetBinError(i+1);
        float bin_diff = fabs(bincont-bincont_shift);
        float bin_diffErr = std::sqrt( sqr(bincontErr) + sqr(bincont_shiftErr));
        hist_diff.push_back(std::make_pair(bin_diff, bin_diffErr));
      }
      sort(hist_diff.begin(), hist_diff.end(), sortbyfirstmax);
      float bincenter = hist_central->GetXaxis()->GetBinCenter(i+1);
      float funcvalue_ = funcvalue(bincenter, xmin, xmax);
      float maxdiff = hist_diff[0].first;
      float maxdiffErr = hist_diff[0].second;
      float bincontnew = bincont + maxdiff*funcvalue_;
      float bincontnewErr = std::sqrt( sqr(bincontErr) + sqr(funcvalue_) * sqr(maxdiffErr) );
      hist_up->SetBinContent(i+1, bincontnew);
      hist_up->SetBinError(i+1, bincontnewErr);
      bincontnew = bincont - maxdiff*funcvalue_;
      bincontnewErr = std::sqrt( sqr(bincontErr) + sqr(funcvalue_) * sqr(maxdiffErr) );
      hist_dn->SetBinContent(i+1, bincontnew);
      hist_dn->SetBinError(i+1, bincontnewErr);
    }
  }

  void processSubdirectory_recursively(TFileDirectory& fs, 
                                       const TDirectory* dir, const std::string& dirName, 
                                       const vstring& processes_input, const std::string& process_output, 
                                       const vstring& central_or_shifts,
                                       bool isDEBUG = false)
  {
    if ( isDEBUG )
    {
      std::cout << "<processSubdirectory_recursively>:" << std::endl;
      std::cout << " dir = '" << dirName << "'" << std::endl;
    }

    // check if directory given as function argument contains subdirectories for input processes
    bool allProcessesExist = true;
    for ( auto process_input: processes_input )
    {
      const TDirectory* subdir_input = dynamic_cast<TDirectory*>((const_cast<TDirectory*>(dir))->Get(process_input.data()));
      if ( !subdir_input ) 
      {
        allProcessesExist = false;
      }
    }
    if ( allProcessesExist ) 
    {
      if ( isDEBUG )
      {
        std::cout << "processing directory = " << dirName << std::endl;
      }

      // get list of histograms to be added
      std::string the_process_input = "TT";
      const TDirectory* the_subdir_input = dynamic_cast<TDirectory*>((const_cast<TDirectory*>(dir))->Get(the_process_input.data()));      
      assert(the_subdir_input);
      //the_subdir_input->ls();
      
      TList* list = the_subdir_input->GetListOfKeys();
      bool addedCR = false;
      for ( auto central_or_shift: central_or_shifts ) 
      {
	std::string find_histogramUp; 
        std::string find_histogramDown;
        if ( central_or_shift == "mtop" ) 
        {
          find_histogramUp = "mtop173p5_";
          find_histogramDown = "mtop171p5_";
        }
        else 
        {
          find_histogramUp = central_or_shift + "Up_";
          find_histogramDown = central_or_shift + "Down_";
	}
        std::set<std::string> histogramNames;
        TIter next(list);
        TKey* key = 0;
	while ( (key = dynamic_cast<TKey*>(next())) ) 
        {
          TObject* object = key->ReadObj();
          TH1* histogram = dynamic_cast<TH1*>(object);
          if ( !histogram ) continue;
          std::string histogramName = histogram->GetName();
          if ( histogramName.find(find_histogramUp) != std::string::npos ) 
          {
            histogramNames.insert(histogramName);
          }
	} //while

        std::pair<TH1*, TH1*> hists_updn;

        for ( auto process_input: processes_input )
        {
          std::string subdirName_output = Form("%s/%s", dirName.data(), process_input.data());
          if ( isDEBUG )
          {
            std::cout << "creating subdirectory = '" << subdirName_output << "'" << std::endl;
          }
          TDirectory* subdir_output = createSubdirectory_recursively(fs, subdirName_output);
          subdir_output->cd();

          for ( auto histogramName: histogramNames )
          {
            std::string histogramName_up = histogramName;
            TH1* histogram_up = getHistogram(dir, process_input, histogramName_up, "", true);
            assert(histogram_up);
            std::string histogramName_dn = TString(histogramName_up.data()).ReplaceAll(find_histogramUp.data(), find_histogramDown.data()).Data();
            TH1* histogram_dn = getHistogram(dir, process_input, histogramName_dn, "", true);
            assert(histogram_dn);
            std::string histogramName_central = TString(histogramName_up.data()).ReplaceAll(find_histogramUp.data(), "").Data();
            TH1* histogram_central = getHistogram(dir, process_input, histogramName_central, "", true);
            assert(histogram_central);
            hists_updn = add_syshist(histogram_central, histogram_up, histogram_dn);
            if ( !addedCR )
            {
              add_sysCR(histogram_central, { "QCDbased", "GluonMove", "erdON" }, dir, process_input);
            }
            hists_updn.first->Write();
            hists_updn.second->Write();
          } //histogramName
        } // process_input
        addedCR = true;
      } // central_or_shift
    }

    // recursively process all subdirectories
    std::vector<const TDirectory*> subdirs = getSubdirectories(dir);
    for ( std::vector<const TDirectory*>::iterator subdir = subdirs.begin();
          subdir != subdirs.end(); ++subdir ) {
      processSubdirectory_recursively(fs, *subdir, dirName + "/" + (*subdir)->GetName(), processes_input, process_output, central_or_shifts, isDEBUG);
    }
    for ( const TDirectory* subdir: subdirs )
    {
      delete subdir;
      subdir = nullptr;
    }
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

  std::cout << "<addSysTT2>:\n";

//--- keep track of time it takes the macro to execute
  TBenchmark clock;
  clock.Start("addSysTT2");

//--- read python configuration parameters
  if ( !edm::readPSetsFrom(argv[1])->existsAs<edm::ParameterSet>("process") )
    throw cmsException(__func__, __LINE__)
      << "No ParameterSet 'process' found in configuration file = " << argv[1];

  edm::ParameterSet cfg = edm::readPSetsFrom(argv[1])->getParameter<edm::ParameterSet>("process");

  edm::ParameterSet cfg_addSysTT = cfg.getParameter<edm::ParameterSet>("addSysTT");

  vstring categories = cfg_addSysTT.getParameter<vstring>("categories");

  vstring central_or_shifts = cfg_addSysTT.getParameter<vstring>("sysShifts");

  vstring processes_input = cfg_addSysTT.getParameter<vstring>("processes_input");
  std::string process_output = cfg_addSysTT.getParameter<std::string>("process_output");

  bool isDEBUG = cfg_addSysTT.exists("isDEBUG") ? cfg_addSysTT.getParameter<bool>("isDEBUG") : false;
  //bool isDEBUG = cfg_addSysTT.getParameter<bool>("isDEBUG");

  fwlite::InputSource inputFiles(cfg);
  if ( !(inputFiles.files().size() == 1) )
    throw cmsException(__func__, __LINE__) << "Exactly one input file expected";
  TFile* inputFile = new TFile(inputFiles.files().front().data());

  fwlite::OutputFiles outputFile(cfg);
  fwlite::TFileService fs = fwlite::TFileService(outputFile.file().data());

  if ( categories.size() == 0 ) 
  {
    categories = getSubdirectoryNames(inputFile);
  }

  for ( const std::string & category: categories )
  {
    std::cout << "processing category = " << category << std::endl;

    TDirectory* dir = getDirectory(inputFile, category, true);
    assert(dir);

    processSubdirectory_recursively(fs, dir, category, processes_input, process_output, central_or_shifts, isDEBUG);
  } // categories

  //---------------------------------------------------------------------------------------------------
  // CV: Add (dummy) histograms for number of analyzed and processed events
  //     This is needed to avoid run-time errors/warnings when executing python/commands/get_events_count.py (called by python/sbatch-node.template.hadd.sh)
  fs.make<TH1D>("analyzedEntries", "analyzedEntries", 1, -0.5, +0.5);
  fs.make<TH1D>("selectedEntries", "selectedEntries", 1, -0.5, +0.5);
  //---------------------------------------------------------------------------------------------------

  delete inputFile;

  clock.Show("addSysTT2");

  std::cout << "returning exit code = " << EXIT_SUCCESS << " (EXIT_SUCCESS)." << std::endl;
  return EXIT_SUCCESS;
}
