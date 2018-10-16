
#include <TFile.h>
#include <TString.h>
#include <TH1.h>
#include <TMath.h>
#include <TROOT.h>
#include <TStyle.h>

#include <string>
#include <vector>
#include <map>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <assert.h>

TH1* 
loadHistogram(TFile* inputFile, const std::string& histogramName)
{
  //std::cout << " loading histogram = '" << histogramName << "'" << std::endl;
  TH1* histogram = dynamic_cast<TH1*>(inputFile->Get(histogramName.data()));
  if ( !histogram ) {
    //std::cerr << "Failed to load histogram = " << histogramName << " from file = " << inputFile->GetName() << " !!" << std::endl;
    //assert(0);
    return 0;
  }
  if ( !histogram->GetSumw2N() ) histogram->Sumw2();
  return histogram;
}

double
compIntegral(const TH1 * histogram,
             bool includeUnderflowBin = false,
             bool includeOverflowBin = false)
{  
  if ( histogram ) {
    const int numBins  = histogram->GetNbinsX();
    const int firstBin = includeUnderflowBin ? 0           : 1;
    const int lastBin  = includeOverflowBin  ? numBins + 1 : numBins;
    double sumBinContent = 0.;
    for(int iBin = firstBin; iBin <= lastBin; ++iBin)
    {
      sumBinContent += histogram->GetBinContent(iBin);
    }
    return sumBinContent;
  } else {
    return -1.;
  }
}

double 
square(double x)
{
  return x*x;
}

double
compIntegralErr(const TH1 * histogram,
		bool includeUnderflowBin = false,
		bool includeOverflowBin = false)
{
  if ( histogram ) {
    const int numBins  = histogram->GetNbinsX();
    const int firstBin = includeUnderflowBin ? 0           : 1;
    const int lastBin  = includeOverflowBin  ? numBins + 1 : numBins;
    double sumBinErr2 = 0.;
    for(int iBin = firstBin; iBin <= lastBin; ++iBin)
    {
      sumBinErr2 += square(histogram->GetBinError(iBin));
    }
    return std::sqrt(sumBinErr2);
  } else {
    return -1.;
  }
}

enum { kHbb_undefined, kHbb_resolved, kHbb_boosted };
enum { kVBF_undefined, kVBF_nottagged, kVBF_tagged };
enum { kDilepton, kDielectron, kDimuon };

struct categoryEntryType
{
  categoryEntryType(int numElectrons, int numMuons, int numBJets_medium, int numBJets_loose, int minNumJets, int maxNumJets, int type_Hbb, int type_vbf)
    : numElectrons_(numElectrons)
    , numMuons_(numMuons)
    , minNumJets_(minNumJets)
    , maxNumJets_(maxNumJets)
    , numBJets_medium_(numBJets_medium)
    , numBJets_loose_(numBJets_loose)
    , type_Hbb_(type_Hbb)
    , type_vbf_(type_vbf)
  {
    name_  = "hh_bbWW_";
    label_ = "";
    if      ( numBJets_medium_ >= 2                         ) { name_ += "2bM";    label_ += "2bM";    }
    else if ( numBJets_medium_ >= 1 && numBJets_loose_ >= 1 ) { name_ += "1bM1bL"; label_ += "1bM1bL"; }
    else if ( numBJets_medium_ >= 1                         ) { name_ += "1bM";    label_ += "1bM";    }
    else if (                          numBJets_loose_ >= 2 ) { name_ += "2bL";    label_ += "2bL";    }
    else if (                          numBJets_loose_ >= 1 ) { name_ += "1bL";    label_ += "1bL";    }
    if      ( minNumJets == -1 && maxNumJets == -1          ) (void)0; // CV: do nothing ("no operation")
    else if ( minNumJets == maxNumJets                      ) { name_ += Form("%ij", minNumJets);                 label_ += Form(", %i jets", minNumJets);                 }
    else if ( minNumJets == -1                              ) { name_ += Form("le%ij", maxNumJets);               label_ += Form(", <= %i jets", maxNumJets);               }
    else if ( maxNumJets == -1                              ) { name_ += Form("ge%ij", minNumJets);               label_ += Form(", >= %i jets", minNumJets);               }
    else if ( maxNumJets >  minNumJets                      ) { name_ += Form("%ito%ij", minNumJets, maxNumJets); label_ += Form(", %i to %i jets", minNumJets, maxNumJets); }
    else assert(0);
    if      ( numElectrons_ >= 2                            ) { name_ += "2e";  label_ += ", 2e";  }
    else if ( numMuons_ >= 2                                ) { name_ += "2mu"; label_ += ", 2mu"; }
    else                                                      { name_ += "2l";  label_ += ", 2l";  }
    name_ += "_DYctrl";
    if      ( type_Hbb_ == kHbb_resolved                    ) { name_ += "_resolvedHbb"; label_ += "";            }
    else if ( type_Hbb_ == kHbb_boosted                     ) { name_ += "_boostedHbb";  label_ += "_boostedHbb"; }
    if      ( type_vbf_ == kVBF_tagged                      ) { name_ += "_vbf";         label_ += "_vbf";        }
    else if ( type_vbf_ == kVBF_nottagged                   ) { name_ += "_nonvbf";      label_ += "";            }
    name_ += "_OS_Tight";
  }
  ~categoryEntryType() {}
  std::string name_;
  std::string label_;
  int numElectrons_;
  int numMuons_;
  int minNumJets_;
  int maxNumJets_;
  int numBJets_medium_;
  int numBJets_loose_;
  int type_Hbb_; // 0 = either resolved or boosted, 1 = resolved, 2 = boosted
  int type_vbf_; // 0 = either tagged or not tagged, 1 = not tagged; 2 = tagged 
};

bool
isHigherPriority(const categoryEntryType& category1,
		 const categoryEntryType& category2)
{
  if ( category1.numBJets_medium_ > category2.numBJets_medium_ ) return true;
  if ( category1.numBJets_medium_ < category2.numBJets_medium_ ) return false;
  if ( category1.numBJets_loose_  > category2.numBJets_loose_  ) return true;
  if ( category1.numBJets_loose_  < category2.numBJets_loose_  ) return false;
  if ( category1.maxNumJets_      > category2.maxNumJets_      ) return true;
  if ( category1.maxNumJets_      < category2.maxNumJets_      ) return false;
  if ( category1.minNumJets_      > category2.minNumJets_      ) return true;
  if ( category1.minNumJets_      < category2.minNumJets_      ) return false;
  if ( category1.type_Hbb_        > category2.type_Hbb_        ) return true;
  if ( category1.type_Hbb_        < category2.type_Hbb_        ) return false;
  if ( category1.type_vbf_        > category2.type_vbf_        ) return true;
  if ( category1.type_vbf_        < category2.type_vbf_        ) return false;
  if ( category1.numMuons_        > category2.numMuons_        ) return true;
  if ( category1.numMuons_        < category2.numMuons_        ) return false;
  if ( category1.numElectrons_    > category2.numElectrons_    ) return true;
  if ( category1.numElectrons_    < category2.numElectrons_    ) return false;
  assert(0);
}

void compDYSF()
{
  gROOT->SetBatch(true);

  TH1::AddDirectory(false);

  std::string inputFilePath = "/hdfs/local/veelken/hhAnalysis/2017/2018Oct13_DYctrl/histograms/hh_bbWW_DYctrl/";
  std::string inputFileName = "histograms_harvested_stage2_hh_bbWW_DYctrl_OS_Tight.root";

  std::vector<categoryEntryType> categories;
  for ( int type_lepton = kDielectron; type_lepton <= kDimuon; ++type_lepton ) {
    int numElectrons = ( type_lepton == kDielectron ) ? 2 : -1;
    int numMuons     = ( type_lepton == kDimuon     ) ? 2 : -1;
    // CV: add categories for "resolved" b-jets without VBF jet selection
    //categories.push_back(categoryEntryType(numElectrons, numMuons,  2, -1, -1, -1, kHbb_resolved, kVBF_undefined)); // hh_bbWW_2bM2e_DYctrl,        hh_bbWW_2bM2mu_DYctrl
    categories.push_back(categoryEntryType(numElectrons, numMuons,  2, -1,  2,  2, kHbb_resolved, kVBF_undefined)); // hh_bbWW_2bM2j2e_DYctrl,      hh_bbWW_2bM2j2mu_DYctrl 
    categories.push_back(categoryEntryType(numElectrons, numMuons,  2, -1,  3,  3, kHbb_resolved, kVBF_undefined)); // hh_bbWW_2bM3j2e_DYctrl,      hh_bbWW_2bM3j2mu_DYctrl
    categories.push_back(categoryEntryType(numElectrons, numMuons,  2, -1,  4, -1, kHbb_resolved, kVBF_undefined)); // hh_bbWW_2bMge4j2e_DYctrl,    hh_bbWW_2bMge4j2mu_DYctrl
    //categories.push_back(categoryEntryType(numElectrons, numMuons,  1,  1, -1, -1, kHbb_resolved, kVBF_undefined)); // hh_bbWW_1bM1bL2e_DYctrl,     hh_bbWW_1bM1bL2mu_DYctrl
    categories.push_back(categoryEntryType(numElectrons, numMuons,  1,  1,  2,  2, kHbb_resolved, kVBF_undefined)); // hh_bbWW_1bM1bL2j2e_DYctrl,   hh_bbWW_1bM1bL2j2mu_DYctrl
    categories.push_back(categoryEntryType(numElectrons, numMuons,  1,  1,  3,  3, kHbb_resolved, kVBF_undefined)); // hh_bbWW_1bM1bL3j2e_DYctrl,   hh_bbWW_1bM1bL3j2mu_DYctrl
    categories.push_back(categoryEntryType(numElectrons, numMuons,  1,  1,  4, -1, kHbb_resolved, kVBF_undefined)); // hh_bbWW_1bM1bLge4j2e_DYctrl, hh_bbWW_1bM1bLge4j2mu_DYctrl
    //categories.push_back(categoryEntryType(numElectrons, numMuons,  1, -1, -1, -1, kHbb_resolved, kVBF_undefined)); // hh_bbWW_1bM2e_DYctrl,        hh_bbWW_1bM2mu_DYctrl
    categories.push_back(categoryEntryType(numElectrons, numMuons,  1, -1,  2,  2, kHbb_resolved, kVBF_undefined)); // hh_bbWW_1bM2j2e_DYctrl,      hh_bbWW_1bM2j2mu_DYctrl 
    categories.push_back(categoryEntryType(numElectrons, numMuons,  1, -1,  3,  3, kHbb_resolved, kVBF_undefined)); // hh_bbWW_1bM3j2e_DYctrl,      hh_bbWW_1bM3j2mu_DYctrl
    categories.push_back(categoryEntryType(numElectrons, numMuons,  1, -1,  4, -1, kHbb_resolved, kVBF_undefined)); // hh_bbWW_1bMge4j2e_DYctrl,    hh_bbWW_1bMge4j2mu_DYctrl
    //categories.push_back(categoryEntryType(numElectrons, numMuons, -1,  2, -1, -1, kHbb_resolved, kVBF_undefined)); // hh_bbWW_2bL2e_DYctrl,        hh_bbWW_2bL2mu_DYctrl
    categories.push_back(categoryEntryType(numElectrons, numMuons, -1,  2,  2,  2, kHbb_resolved, kVBF_undefined)); // hh_bbWW_2bL2j2e_DYctrl,      hh_bbWW_2bL2j2mu_DYctrl 
    categories.push_back(categoryEntryType(numElectrons, numMuons, -1,  2,  3,  3, kHbb_resolved, kVBF_undefined)); // hh_bbWW_2bL3j2e_DYctrl,      hh_bbWW_2bL3j2mu_DYctrl
    categories.push_back(categoryEntryType(numElectrons, numMuons, -1,  2,  4, -1, kHbb_resolved, kVBF_undefined)); // hh_bbWW_2bLge4j2e_DYctrl,    hh_bbWW_2bLge4j2mu_DYctrl
    // CV: add categories for "resolved" b-jets with VBF jet selection
    //categories.push_back(categoryEntryType(numElectrons, numMuons,  2, -1, -1, -1, kHbb_resolved, kVBF_tagged));    // hh_bbWW_2bM2e_DYctrl,        hh_bbWW_2bM2mu_DYctrl
    //categories.push_back(categoryEntryType(numElectrons, numMuons,  1,  1, -1, -1, kHbb_resolved, kVBF_tagged));    // hh_bbWW_1bM1bL2e_DYctrl,     hh_bbWW_1bM1bL2mu_DYctrl
    //categories.push_back(categoryEntryType(numElectrons, numMuons,  1, -1, -1, -1, kHbb_resolved, kVBF_tagged));    // hh_bbWW_1bM2e_DYctrl,        hh_bbWW_1bM2mu_DYctrl
    //categories.push_back(categoryEntryType(numElectrons, numMuons, -1,  2, -1, -1, kHbb_resolved, kVBF_tagged));    // hh_bbWW_2bL2e_DYctrl,        hh_bbWW_2bL2mu_DYctrl
    // CV: add categories for "boosted" b-jets (no VBF jet selection)
    //categories.push_back(categoryEntryType(numElectrons, numMuons,  2, -1, -1, -1, kHbb_boosted,  kVBF_undefined)); // hh_bbWW_2bM2e_DYctrl,        hh_bbWW_2bM2mu_DYctrl
    //categories.push_back(categoryEntryType(numElectrons, numMuons,  1,  1, -1, -1, kHbb_boosted,  kVBF_undefined)); // hh_bbWW_1bM1bL2e_DYctrl,     hh_bbWW_1bM1bL2mu_DYctrl
    //categories.push_back(categoryEntryType(numElectrons, numMuons,  1, -1, -1, -1, kHbb_boosted,  kVBF_undefined)); // hh_bbWW_1bM2e_DYctrl,        hh_bbWW_1bM2mu_DYctrl
  }
  std::sort(categories.begin(), categories.end(), isHigherPriority);
    
  std::vector<std::string> signal_processes;
  signal_processes.push_back("DY");
  signal_processes.push_back("DY_conversion");
  signal_processes.push_back("DY_fake");

  std::vector<std::string> background_processes;
  background_processes.push_back("TT");
  background_processes.push_back("TTW");
  background_processes.push_back("TTWW");
  background_processes.push_back("TTZ");
  background_processes.push_back("TH");
  background_processes.push_back("TTH");
  background_processes.push_back("WZ");
  background_processes.push_back("ZZ");
  background_processes.push_back("W");
  //background_processes.push_back("conversions");
  //background_processes.push_back("fakes_data");
  //background_processes.push_back("fakes_mc");
  background_processes.push_back("VH");
  
  TString inputFileName_full = inputFilePath.data();
  if ( !inputFileName_full.EndsWith("/") ) inputFileName_full.Append("/");
  inputFileName_full.Append(inputFileName.data());
  TFile* inputFile = new TFile(inputFileName_full.Data());
  if ( !inputFile ) {
    std::cerr << "Failed to open input file = " << inputFileName_full.Data() << " !!" << std::endl;
    assert(0);
  }
  //std::cout << "opened input file = '" << inputFileName_full.Data() << "'" << std::endl;
  
  for ( std::vector<categoryEntryType>::const_iterator category = categories.begin();
	category != categories.end(); ++category ) {
    std::cout << "category = " << category->label_ << std::endl;

    // process DY signal contributions
    double numEvents_signalSum = 0.;
    double numEventsErr2_signalSum = 0.;
    for ( std::vector<std::string>::const_iterator signal_process = signal_processes.begin();
	  signal_process != signal_processes.end(); ++signal_process ) {
      std::string histogramName = Form("%s/sel/evt/%s/EventCounter", 
	category->name_.data(), signal_process->data());
      TH1* histogram = loadHistogram(inputFile, histogramName);
      assert(histogram);
      double integral = compIntegral(histogram);
      numEvents_signalSum += integral;
      double integralErr = compIntegralErr(histogram);
      numEventsErr2_signalSum += square(integralErr); 
    }
    double numEventsErr_signalSum = TMath::Sqrt(numEventsErr2_signalSum);

    // process background contributions
    double numEvents_backgroundSum = 0.;
    double numEventsErr2_backgroundSum = 0.;
    for ( std::vector<std::string>::const_iterator background_process = background_processes.begin();
	  background_process != background_processes.end(); ++background_process ) {
      std::string histogramName = Form("%s/sel/evt/%s/EventCounter", 
	category->name_.data(), background_process->data());
      TH1* histogram = loadHistogram(inputFile, histogramName);
      assert(histogram);
      double integral = compIntegral(histogram);
      numEvents_backgroundSum += integral;
      double integralErr = compIntegralErr(histogram);
      numEventsErr2_backgroundSum += square(integralErr); 
    }
    double numEventsErr_backgroundSum = TMath::Sqrt(numEventsErr2_backgroundSum);

    // process data
    std::string histogramName = Form("%s/sel/evt/%s/EventCounter", 
      category->name_.data(), "data_obs");
    TH1* histogram = loadHistogram(inputFile, histogramName);
    assert(histogram);
    double numEvents_data = compIntegral(histogram);
    double numEventsErr_data = compIntegralErr(histogram);

    double numEvents_data_minus_background = numEvents_data - numEvents_backgroundSum;
    double numEventsErr_data_minus_background = TMath::Sqrt(square(numEventsErr_data) + square(numEventsErr_backgroundSum));

    double sf = numEvents_data_minus_background/numEvents_signalSum;
    double sfErr = sf*TMath::Sqrt(square(numEventsErr_data_minus_background/numEvents_data_minus_background) + square(numEventsErr_signalSum/numEvents_signalSum));

    std::cout << " DY = " << numEvents_signalSum << " +/- " << numEventsErr_signalSum << ","
	      << " data - background = " << numEvents_data_minus_background << " +/- " << numEventsErr_data_minus_background
	      << " --> SF = " << sf << " +/- " << sfErr << std::endl;
  }

  delete inputFile;
}
