
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
#include <assert.h>

TH1* loadHistogram(TFile* inputFile, const std::string& histogramName)
{
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
  const int numBins  = histogram->GetNbinsX();
  const int firstBin = includeUnderflowBin ? 0           : 1;
  const int lastBin  = includeOverflowBin  ? numBins + 1 : numBins;

  double sumBinContent = 0.;
  for(int iBin = firstBin; iBin <= lastBin; ++iBin)
  {
    sumBinContent += histogram->GetBinContent(iBin);
  }
  return sumBinContent;
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
  const int numBins  = histogram->GetNbinsX();
  const int firstBin = includeUnderflowBin ? 0           : 1;
  const int lastBin  = includeOverflowBin  ? numBins + 1 : numBins;

  double sumBinErr2 = 0.;
  for(int iBin = firstBin; iBin <= lastBin; ++iBin)
  {
    sumBinErr2 += square(histogram->GetBinError(iBin));
  }
  return std::sqrt(sumBinErr2);
}

void dumpEventYields()
{
  gROOT->SetBatch(true);

  TH1::AddDirectory(false);

  typedef std::vector<std::string> vstring;
  vstring channels;
  channels.push_back("hh_bb1l");
  //channels.push_back("hh_bb2l");
  //channels.push_back("hh_bb1l1tau");

  std::map<std::string, std::string> inputFilePaths; // key = channel
  inputFilePaths["hh_bb1l"] = "/hdfs/local/veelken/hhAnalysis/2017/2018Nov01/histograms/hh_bb1l/";
  inputFilePaths["hh_bb2l"] = "/hdfs/local/veelken/hhAnalysis/2017/2018Oct18/histograms/hh_bb2l/";
  inputFilePaths["hh_bb1l1tau"] = "/hdfs/local/veelken/hhAnalysis/2017/2018Nov12/histograms/hh_bb1l1tau/";

  std::map<std::string, std::string> inputFileNames; // key = channel
  inputFileNames["hh_bb1l"] = "histograms_harvested_stage2_hh_bb1l_Tight.root";
  inputFileNames["hh_bb2l"] = "histograms_harvested_stage2_hh_bb2l_OS_Tight.root";
  inputFileNames["hh_bb1l1tau"] = "histograms_harvested_stage2_hh_bb1l1tau_OS_Tight.root";

  std::map<std::string, vstring> categories; // key = channel
  categories["hh_bb1l"].push_back("hh_bb1l_Tight");
  //categories["hh_bb1l"].push_back("hh_bb1e_Tight");
  //categories["hh_bb1l"].push_back("hh_bb1mu_Tight");
  categories["hh_bb1l"].push_back("hh_bb1l_resolvedHbb_resolvedWjj_Tight");
  //categories["hh_bb1l"].push_back("hh_bb1l_resolvedHbb_resolvedWjj_vbf_Tight");
  //categories["hh_bb1l"].push_back("hh_bb1l_resolvedHbb_resolvedWjj_nonvbf_Tight");
  //categories["hh_bb1l"].push_back("hh_bb1l_resolvedHbb_boostedWjj_highPurity_Tight");
  //categories["hh_bb1l"].push_back("hh_bb1l_resolvedHbb_boostedWjj_lowPurity_Tight");
  categories["hh_bb1l"].push_back("hh_bb1l_boostedHbb_resolvedWjj_Tight");
  categories["hh_bb1l"].push_back("hh_bb1l_boostedHbb_boostedWjj_highPurity_Tight");
  categories["hh_bb1l"].push_back("hh_bb1l_boostedHbb_boostedWjj_lowPurity_Tight");
  //categories["hh_bb1l"].push_back("hh_bb1l_vbf");
  categories["hh_bb2l"].push_back("hh_bb2l_OS_Tight");
  //categories["hh_bb2l"].push_back("hh_bb2l_resolvedHbb_vbf_OS_Tight");
  //categories["hh_bb2l"].push_back("hh_bb2l_resolvedHbb_nonvbf_OS_Tight");
  categories["hh_bb2l"].push_back("hh_bb2l_resolvedHbb_OS_Tight");
  categories["hh_bb2l"].push_back("hh_bb2l_boostedHbb_OS_Tight");
/*
  categories["hh_bb2l"].push_back("hh_bb2e_OS_Tight");
  categories["hh_bb2l"].push_back("hh_bb2e_resolvedHbb_vbf_OS_Tight");
  categories["hh_bb2l"].push_back("hh_bb2e_resolvedHbb_nonvbf_OS_Tight");
  categories["hh_bb2l"].push_back("hh_bb2e_boostedHbb_OS_Tight");
  categories["hh_bb2l"].push_back("hh_bb1e1mu_OS_Tight");
  categories["hh_bb2l"].push_back("hh_bb1e1mu_resolvedHbb_vbf_OS_Tight");
  categories["hh_bb2l"].push_back("hh_bb1e1mu_resolvedHbb_nonvbf_OS_Tight");
  categories["hh_bb2l"].push_back("hh_bb1e1mu_boostedHbb_OS_Tight");
  categories["hh_bb2l"].push_back("hh_bb2mu_OS_Tight");
  categories["hh_bb2l"].push_back("hh_bb2mu_resolvedHbb_vbf_OS_Tight");
  categories["hh_bb2l"].push_back("hh_bb2mu_resolvedHbb_nonvbf_OS_Tight");
  categories["hh_bb2l"].push_back("hh_bb2mu_boostedHbb_OS_Tight");
 */
/*  
  categories["hh_bb2l"].push_back("hh_2l_OS");
  categories["hh_bb2l"].push_back("hh_2l_vbf_OS");
  categories["hh_bb2l"].push_back("hh_2e_OS");
  categories["hh_bb2l"].push_back("hh_2e_vbf_OS");
  categories["hh_bb2l"].push_back("hh_2mu_OS");
  categories["hh_bb2l"].push_back("hh_2mu_vbf_OS");
  categories["hh_bb2l"].push_back("hh_1e1mu_OS");
  categories["hh_bb2l"].push_back("hh_1e1mu_vbf_OS");
 */
  categories["hh_bb1l1tau"].push_back("hh_bb1l1tau_OS_Tight");
  categories["hh_bb1l1tau"].push_back("hh_bb1l1tau_resolvedHbb_vbf_OS_Tight");
  categories["hh_bb1l1tau"].push_back("hh_bb1l1tau_resolvedHbb_nonvbf_OS_Tight");
  categories["hh_bb1l1tau"].push_back("hh_bb1l1tau_boostedHbb_OS_Tight");
  categories["hh_bb1l1tau"].push_back("hh_bb1e1tau_OS_Tight");
  //categories["hh_bb1l1tau"].push_back("hh_bb1e1tau_resolvedHbb_vbf_OS_Tight");
  //categories["hh_bb1l1tau"].push_back("hh_bb1e1tau_resolvedHbb_nonvbf_OS_Tight");
  //categories["hh_bb1l1tau"].push_back("hh_bb1e1tau_boostedHbb_OS_Tight");
  categories["hh_bb1l1tau"].push_back("hh_bb1mu1tau_OS_Tight");
  //categories["hh_bb1l1tau"].push_back("hh_bb1mu1tau_resolvedHbb_vbf_OS_Tight");
  //categories["hh_bb1l1tau"].push_back("hh_bb1mu1tau_resolvedHbb_nonvbf_OS_Tight");
  //categories["hh_bb1l1tau"].push_back("hh_bb1mu1tau_boostedHbb_OS_Tight");

  std::map<std::string, std::string> directories; // key = channel
  directories["hh_bb1l"] = "sel/evt";
  directories["hh_bb2l"] = "sel/evt";
  directories["hh_bb1l1tau"] = "sel/evt";

  std::map<std::string, vstring> signal_processes; // key = channel
  //signal_processes["hh_bb1l"].push_back("signal_ggf_spin0_400_hh_bbvv");
  //signal_processes["hh_bb1l"].push_back("signal_ggf_spin0_700_hh_bbvv");
  //signal_processes["hh_bb1l"].push_back("signal_ggf_spin0_400_hh_bbtt");
  //signal_processes["hh_bb1l"].push_back("signal_ggf_spin0_700_hh_bbtt");
  signal_processes["hh_bb1l"].push_back("signal_vbf_spin0_300_hh_bbvv");
  signal_processes["hh_bb1l"].push_back("signal_vbf_spin0_400_hh_bbvv");
  signal_processes["hh_bb1l"].push_back("signal_vbf_spin0_750_hh_bbvv");
  //signal_processes["hh_bb1l"].push_back("signal_vbf_spin0_400_hh_bbtt");
  //signal_processes["hh_bb1l"].push_back("signal_vbf_spin0_700_hh_bbtt");
  //signal_processes["hh_bb2l"].push_back("signal_ggf_spin0_400_hh_bbvv");
  //signal_processes["hh_bb2l"].push_back("signal_ggf_spin0_700_hh_bbvv");
  //signal_processes["hh_bb2l"].push_back("signal_ggf_spin0_400_hh_bbtt");
  //signal_processes["hh_bb2l"].push_back("signal_ggf_spin0_700_hh_bbtt");
  signal_processes["hh_bb2l"].push_back("signal_vbf_spin0_300_hh_bbvv");
  signal_processes["hh_bb2l"].push_back("signal_vbf_spin0_400_hh_bbvv");
  signal_processes["hh_bb2l"].push_back("signal_vbf_spin0_750_hh_bbvv");
  //signal_processes["hh_bb2l"].push_back("signal_vbf_spin0_400_hh_bbtt");
  //signal_processes["hh_bb2l"].push_back("signal_vbf_spin0_700_hh_bbtt");
  signal_processes["hh_bb1l1tau"].push_back("signal_vbf_spin0_300_hh_bbvv");
  signal_processes["hh_bb1l1tau"].push_back("signal_vbf_spin0_400_hh_bbvv");
  signal_processes["hh_bb1l1tau"].push_back("signal_vbf_spin0_750_hh_bbvv");

  std::vector<std::string> signal_process_parts;
  signal_process_parts.push_back("");
  signal_process_parts.push_back("_Convs");
  signal_process_parts.push_back("_fake");
  
  std::map<std::string, vstring> background_processes; // key = channel
  background_processes["hh_bb1l"].push_back("TT");
  background_processes["hh_bb1l"].push_back("TTW");
  background_processes["hh_bb1l"].push_back("TTWW");
  background_processes["hh_bb1l"].push_back("TTZ");
  background_processes["hh_bb1l"].push_back("TH");
  background_processes["hh_bb1l"].push_back("TTH");
  background_processes["hh_bb1l"].push_back("WZ");
  background_processes["hh_bb1l"].push_back("ZZ");
  background_processes["hh_bb1l"].push_back("DY");
  background_processes["hh_bb1l"].push_back("W");
  background_processes["hh_bb1l"].push_back("Convs");
  background_processes["hh_bb1l"].push_back("data_fakes");
  background_processes["hh_bb1l"].push_back("fakes_mc");
  background_processes["hh_bb1l"].push_back("VH");
  background_processes["hh_bb2l"].push_back("TT");
  background_processes["hh_bb2l"].push_back("TTW");
  background_processes["hh_bb2l"].push_back("TTWW");
  background_processes["hh_bb2l"].push_back("TTZ");
  background_processes["hh_bb2l"].push_back("TH");
  background_processes["hh_bb2l"].push_back("TTH");
  background_processes["hh_bb2l"].push_back("WZ");
  background_processes["hh_bb2l"].push_back("ZZ");
  background_processes["hh_bb2l"].push_back("DY");
  background_processes["hh_bb2l"].push_back("W");
  background_processes["hh_bb2l"].push_back("Convs");
  background_processes["hh_bb2l"].push_back("data_fakes");
  background_processes["hh_bb2l"].push_back("fakes_mc");
  background_processes["hh_bb2l"].push_back("VH");
  background_processes["hh_bb1l1tau"].push_back("TT");
  background_processes["hh_bb1l1tau"].push_back("TTW");
  background_processes["hh_bb1l1tau"].push_back("TTWW");
  background_processes["hh_bb1l1tau"].push_back("TTZ");
  background_processes["hh_bb1l1tau"].push_back("TH");
  background_processes["hh_bb1l1tau"].push_back("TTH");
  background_processes["hh_bb1l1tau"].push_back("WZ");
  background_processes["hh_bb1l1tau"].push_back("ZZ");
  background_processes["hh_bb1l1tau"].push_back("DY");
  background_processes["hh_bb1l1tau"].push_back("W");
  background_processes["hh_bb1l1tau"].push_back("Convs");
  background_processes["hh_bb1l1tau"].push_back("data_fakes");
  background_processes["hh_bb1l1tau"].push_back("fakes_mc");
  background_processes["hh_bb1l1tau"].push_back("VH");
  
  std::vector<std::string> background_process_parts;
  background_process_parts.push_back("");
  background_process_parts.push_back("_Convs");
  background_process_parts.push_back("_fake");

  double lumi_datacard = 41.5;
  double lumi_projection = 41.5;
  double lumi_SF = lumi_projection/lumi_datacard;
  std::cout << "scaling signal and background yields to L=" << lumi_projection << "fb^-1 @ 13 TeV." << std::endl;

  for ( vstring::const_iterator channel = channels.begin();
	channel != channels.end(); ++channel ) {

    TString inputFileName_full = inputFilePaths[*channel].data();
    if ( !inputFileName_full.EndsWith("/") ) inputFileName_full.Append("/");
    inputFileName_full.Append(inputFileNames[*channel].data());
    std::cout << "channel = " << inputFileName_full.Data() << std::endl;
    TFile* inputFile = new TFile(inputFileName_full.Data());
    if ( !inputFile ) {
      std::cerr << "Failed to open input file = " << inputFileName_full.Data() << " !!" << std::endl;
      assert(0);
    }
    
    for ( vstring::const_iterator category = categories[*channel].begin();
	  category != categories[*channel].end(); ++category ) {
      std::cout << "channel = " << (*channel) << ": category = " << (*category) << std::endl;

      for ( vstring::const_iterator signal_process = signal_processes[*channel].begin();
	    signal_process != signal_processes[*channel].end(); ++signal_process ) {
	std::map<std::string, double> integral_parts;
	std::map<std::string, double> integralErr_parts;
	double integral_sum = 0.;
	double integralErr2_sum = 0.;
	for ( std::vector<std::string>::const_iterator signal_process_part = signal_process_parts.begin();
	      signal_process_part != signal_process_parts.end(); ++signal_process_part ) {
	  std::string histogramName = Form("%s/%s/%s%s/EventCounter", 
	    category->data(), directories[*channel].data(), signal_process->data(), signal_process_part->data());
	  TH1* histogram = loadHistogram(inputFile, histogramName);
	  if ( histogram ) {
	    histogram->Scale(lumi_SF);
	    double integral = compIntegral(histogram);
	    integral_parts[*signal_process_part] = integral;
	    integral_sum += integral;
	    double integralErr = compIntegralErr(histogram);
	    integralErr_parts[*signal_process_part] = integralErr;
	    integralErr2_sum += square(integralErr); 
	  }
	}
	double integralErr_sum = TMath::Sqrt(integralErr2_sum);
	std::cout << (*signal_process) << ": " << integral_sum << " +/- " << integralErr_sum << std::endl;
	if ( integral_parts.size() > 1 ) {
	  std::cout << " (non-fake = " << integral_parts[""] << " +/- " << integralErr_parts[""] << ","
		    << " fake = " << integral_parts["_fake"] << " +/- " << integralErr_parts["_fake"] << ","
		    << " conversion = " << integral_parts["_Convs"] << " +/- " << integralErr_parts["_Convs"] << ")" << std::endl;
	}
      }
      for ( vstring::const_iterator background_process = background_processes[*channel].begin();
	    background_process != background_processes[*channel].end(); ++background_process ) {
	std::map<std::string, double> integral_parts;
	std::map<std::string, double> integralErr_parts;
	double integral_sum = 0.;
	double integralErr2_sum = 0.;
	for ( std::vector<std::string>::const_iterator background_process_part = background_process_parts.begin();
	      background_process_part != background_process_parts.end(); ++background_process_part ) {
	  std::string histogramName = Form("%s/%s/%s%s/EventCounter", 
	    category->data(), directories[*channel].data(), background_process->data(), background_process_part->data());
	  TH1* histogram = loadHistogram(inputFile, histogramName);
	  if ( histogram ) {
	    histogram->Scale(lumi_SF);
	    double integral = compIntegral(histogram);
	    integral_parts[*background_process_part] = integral;
	    integral_sum += integral;
	    double integralErr = compIntegralErr(histogram);
	    integralErr_parts[*background_process_part] = integralErr;
	    integralErr2_sum += square(integralErr); 
	  }
	}
	double integralErr_sum = TMath::Sqrt(integralErr2_sum);
	std::cout << (*background_process) << ": " << integral_sum << " +/- " << integralErr_sum << std::endl;
	if ( integral_parts.size() > 1 ) {
	  std::cout << " (non-fake = " << integral_parts[""] << " +/- " << integralErr_parts[""] << ","
		    << " fake = " << integral_parts["_fake"] << " +/- " << integralErr_parts["_fake"] << ","
		    << " conversion = " << integral_parts["_Convs"] << " +/- " << integralErr_parts["_Convs"] << ")" << std::endl;
	}
      }

      std::string histogramName = Form("%s/%s/%s/EventCounter", 
        category->data(), directories[*channel].data(), "data_obs");
      TH1* histogram = loadHistogram(inputFile, histogramName);
      if ( histogram ) {
	histogram->Scale(lumi_SF);
	double integral = compIntegral(histogram);
	std::cout << "data_obs: " << integral << std::endl;
      }
      std::cout << std::endl;
    }

    delete inputFile;
  }
}
