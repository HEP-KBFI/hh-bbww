
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
#include <fstream>


TH1* loadHistogram(TFile* inputFile, const std::string& histogramName)
{
  //  std::cout << "************" << histogramName << std::endl;
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

std::string 
find_MVAtype(std::string inputfile) {
  std::string MVAtype = "";
  if ( inputfile.find("BDT") != std::string::npos ) {
    return "BDT";
  }
  else if ( inputfile.find("LBN") != std::string::npos ) {
      return "LBN";
  }
  return "";
}


void dumpEventYields_1(int era, std::string category, std::string inputfile)
{
  std::string MVAtype = find_MVAtype(inputfile); //hadd_stage1_5_BDT_resolved_2b_nonvbf_Tight.root
  std::vector<std::string> evtcats;
  if ( MVAtype == "BDT" ) {
    evtcats.push_back("resolved_2b_nonvbf");
    evtcats.push_back("resolved_2b_vbf");
    evtcats.push_back("resolved_1b");
    evtcats.push_back("boosted");
  }
  else if ( MVAtype == "LBN" ) {
    evtcats.push_back("HH_resolved_2b_nonvbf");
    evtcats.push_back("HH_resolved_2b_vbf");
    evtcats.push_back("HH_resolved_1b");
    evtcats.push_back("HH_boosted");
    evtcats.push_back("TT_resolved");
    evtcats.push_back("TT_boosted");
    evtcats.push_back("W_resolved");
    evtcats.push_back("W_boosted");
    evtcats.push_back("DY_resolved");
    evtcats.push_back("DY_boosted");
    evtcats.push_back("ST_resolved");
    evtcats.push_back("ST_boosted");
    evtcats.push_back("Other");
  }
  
  //  std::cout << BDT_evtcat << std::endl;
  ofstream myfile (Form("eventYield_%d.txt", era));
  if ( !myfile.is_open() ) {
    std::cerr << "output file couldn't be opened !!" << std::endl;
    assert(0);
  }
  gROOT->SetBatch(true);

  TH1::AddDirectory(false);
  std::vector<TH1*> hists;
  typedef std::vector<std::string> vstring;

  vstring histograms;
  histograms.push_back("MVAOutput_SM");
  vstring inclusive_signal_processes; // key = channel
  vstring signal_processes; 
  inclusive_signal_processes.push_back("signal_ggf_nonresonant_cHHH1_hh");                                                                                                     
  inclusive_signal_processes.push_back("signal_ggf_nonresonant_cHHH5_hh");
  inclusive_signal_processes.push_back("signal_ggf_nonresonant_cHHH2p45_hh");
  inclusive_signal_processes.push_back("signal_ggf_nonresonant_cHHH0_hh");
  inclusive_signal_processes.push_back("signal_vbf_nonresonant_1_1_2_hh");
  inclusive_signal_processes.push_back("signal_vbf_nonresonant_1_0_1_hh");
  inclusive_signal_processes.push_back("signal_vbf_nonresonant_1_2_1_hh");
  inclusive_signal_processes.push_back("signal_vbf_nonresonant_1_1_1_hh");
  inclusive_signal_processes.push_back("signal_vbf_nonresonant_0p5_1_1_hh");
  inclusive_signal_processes.push_back("signal_vbf_nonresonant_1_1_0_hh");
  inclusive_signal_processes.push_back("signal_vbf_nonresonant_1p5_1_1_hh");
  
  std::vector<std::string> signal_process_parts;
  signal_process_parts.push_back("");
  vstring hhbrs;
  hhbrs.push_back("bbww");
  hhbrs.push_back("bbzz");
  hhbrs.push_back("bbtt");
  for (auto inclusive_proc: inclusive_signal_processes) {
    signal_processes.push_back(Form("%s_Convs", inclusive_proc.data()));
    signal_processes.push_back(Form("%s_fake", inclusive_proc.data()));
    for ( auto br: hhbrs ) {
      signal_processes.push_back(Form("%s_%s", inclusive_proc.data(), br.data()));
    }
  }

  vstring background_processes; // key = channel
  background_processes.push_back("TT");
  background_processes.push_back("ST");
  background_processes.push_back("W");
  background_processes.push_back("DY");
  background_processes.push_back("data_fakes");
  background_processes.push_back("TTZ");
  background_processes.push_back("TTH");
  background_processes.push_back("TTW");
  background_processes.push_back("ZZ");
  background_processes.push_back("TTWW");
  background_processes.push_back("WZ");
  background_processes.push_back("Convs");
  background_processes.push_back("Other");
  background_processes.push_back("qqZZ");
  background_processes.push_back("ggZZ");
  background_processes.push_back("WW");
  vstring inclusive_procss;
  inclusive_procss.push_back("TH");
  inclusive_procss.push_back("TW");
  inclusive_procss.push_back("ggH");
  inclusive_procss.push_back("qqH");
  inclusive_procss.push_back("ZH");
  inclusive_procss.push_back("WH");
  vstring brs;
  brs.push_back("hww");
  brs.push_back("hbb");
  brs.push_back("hzz");
  brs.push_back("htt");
  for (auto inclusive_proc: inclusive_procss) {
    background_processes.push_back(Form("%s_fake", inclusive_proc.data()));
    background_processes.push_back(Form("%s_Convs", inclusive_proc.data()));
    for ( auto br: brs ) {
      background_processes.push_back(Form("%s_%s", inclusive_proc.data(), br.data()));
    }
  }
  std::vector<std::string> background_process_parts;
  background_process_parts.push_back("");
  background_process_parts.push_back("_Convs");
  background_process_parts.push_back("_fake");
  TString inputFileName_full = inputfile.data();
  TFile* inputFile;
  std::size_t pos = inputfile.rfind(MVAtype);
  for (auto evtcat: evtcats) {
    Double_t total_bkg(0);
    Double_t total_sig(0);
    inputfile = inputfile.replace( inputfile.begin()+pos+MVAtype.length(), inputfile.end(), "_"+evtcat+"_OS_Tight.root");
    myfile << "evtcat: " << evtcat  << std::endl;
    inputFile = new TFile(inputfile.data());
    if ( !inputFile ) {
      std::cerr << "Failed to open input file = " << inputfile << " !!" << std::endl;
      assert(0);
    }
  for ( auto histogram: histograms) {
    for ( auto signal_process: signal_processes) {
      std::map<std::string, double> integral_parts;
      std::map<std::string, double> integralErr_parts;
      double integral_sum = 0.;
      double integralErr2_sum = 0.;
      for ( auto signal_process_part: signal_process_parts) {
          std::string histogramName = Form("%s/sel/datacard/%s/%s/%s%s/%s", 
              category.data(), MVAtype.data(), evtcat.data(), signal_process.data(), signal_process_part.data(), histogram.data());
        TH1* histogram = loadHistogram(inputFile, histogramName);
        if ( histogram ) {
          double integral = compIntegral(histogram);
          integral_parts[signal_process_part] = integral;
          integral_sum += integral;
          double integralErr = compIntegralErr(histogram);
          integralErr_parts[signal_process_part] = integralErr;
          integralErr2_sum += square(integralErr); 
          total_sig +=integral;
        }
      }
      double integralErr_sum = TMath::Sqrt(integralErr2_sum);
      myfile << signal_process << ": " << integral_sum << " +/- " << integralErr_sum << std::endl;
      if ( integral_parts.size() > 1 ) {
        myfile << " (non-fake = " << integral_parts[""] << " +/- " << integralErr_parts[""] << ","
               << " fake = " << integral_parts["_fake"] << " +/- " << integralErr_parts["_fake"] << ","
               << " conversion = " << integral_parts["_Convs"] << " +/- " << integralErr_parts["_Convs"] << ")" << std::endl;
      }
    }
    double integral_THsum = 0.;
    double integralErr2_THsum = 0.;
    double integral_WHsum = 0.;
    double integralErr2_WHsum = 0.;
    double integral_ZHsum = 0.;
    double integralErr2_ZHsum = 0.;
    double integral_TWsum = 0.;
    double integralErr2_TWsum = 0.;
    double integral_qqHsum = 0.;
    double integralErr2_qqHsum = 0.;
    double integral_ggHsum = 0.;
    double integralErr2_ggHsum = 0.;
    for ( auto background_process: background_processes) {
      std::map<std::string, double> integral_parts;
      std::map<std::string, double> integralErr_parts;
      double integral_sum = 0.;
      double integralErr2_sum = 0.;
      for ( auto background_process_part: background_process_parts) {
        std::string histogramName = Form("%s/sel/datacard/%s/%s/%s%s/%s",
          category.data(), MVAtype.data(), evtcat.data(), background_process.data(), background_process_part.data(), histogram.data());
        TH1* histogram = loadHistogram(inputFile, histogramName);
        if ( histogram ) {
          if ( histogramName.find("TH") != std::string::npos ) {
            integral_THsum += compIntegral(histogram);
            integralErr2_THsum += compIntegralErr(histogram);
            total_bkg +=integral_THsum;
          }
          else if ( histogramName.find("WH") != std::string::npos ) {
            integral_WHsum += compIntegral(histogram);
            integralErr2_WHsum += compIntegralErr(histogram);
            total_bkg +=integral_WHsum;
          }
          else if ( histogramName.find("ZH") != std::string::npos ) {
            integral_ZHsum += compIntegral(histogram);
            integralErr2_ZHsum += compIntegralErr(histogram);
            total_bkg +=integral_ZHsum;
          }
          else if ( histogramName.find("TW") != std::string::npos ) {
            integral_TWsum += compIntegral(histogram);
            integralErr2_TWsum += compIntegralErr(histogram);
            total_bkg +=integral_TWsum;
          }
          else if ( histogramName.find("qqH") != std::string::npos ) {
            integral_qqHsum += compIntegral(histogram);
            integralErr2_qqHsum += compIntegralErr(histogram);
            total_bkg +=integral_qqHsum;
          }
          else if ( histogramName.find("ggH") != std::string::npos ) {
            integral_ggHsum += compIntegral(histogram);
            integralErr2_ggHsum += compIntegralErr(histogram);
            total_bkg +=integral_ggHsum;
          }
          else {
            double integral = compIntegral(histogram);
            integral_parts[background_process_part] = integral;
            integral_sum += integral;
            double integralErr = compIntegralErr(histogram);
            integralErr_parts[background_process_part] = integralErr;
            integralErr2_sum += square(integralErr);
            total_bkg +=integral;
          }
        }
      }
      double integralErr_sum = TMath::Sqrt(integralErr2_sum);
      if ( (background_process.find("TH") == std::string::npos) && (background_process.find("WH") == std::string::npos) &&
           (background_process.find("ZH") == std::string::npos) && (background_process.find("TW") == std::string::npos) &&
           (background_process.find("qqH") == std::string::npos) && (background_process.find("ggH") == std::string::npos) ) 
        {
          myfile << background_process << ": " << integral_sum << " +/- " << integralErr_sum << std::endl;
          if ( integral_parts.size() > 1 ) {
            myfile << " (non-fake = " << integral_parts[""] << " +/- " << integralErr_parts[""] << ","
                   << " fake = " << integral_parts["_fake"] << " +/- " << integralErr_parts["_fake"] << ","
                   << " conversion = " << integral_parts["_Convs"] << " +/- " << integralErr_parts["_Convs"] << ")" << std::endl;
          }
        }
    }
    myfile << "TH: " <<  integral_THsum << "+/- " << integralErr2_THsum  << std::endl;
    myfile << "WH: " <<  integral_WHsum << "+/- " << integralErr2_WHsum  << std::endl;
    myfile << "ZH: " <<  integral_ZHsum << "+/- " << integralErr2_ZHsum  << std::endl;
    myfile << "TW: " <<  integral_TWsum << "+/- " << integralErr2_TWsum  << std::endl;
    myfile << "qqH: " <<  integral_qqHsum << "+/- " << integralErr2_qqHsum  << std::endl;
    myfile << "ggH: " <<  integral_ggHsum << "+/- " << integralErr2_ggHsum  << std::endl;
    std::string histogramName = Form("%s/sel/datacard/%s/%s/%s/%s",
               category.data(), MVAtype.data(), evtcat.data(), "data_obs", histogram.data());
    TH1* histogram_ = loadHistogram(inputFile, histogramName);
    if ( histogram_ ) {
      double integral = compIntegral(histogram_);
      myfile << "data_obs: " << integral << std::endl;
      std::cout << "data_obs: " << integral << std::endl;
    }
    myfile << std::endl;
    myfile << "sig: " << total_sig << std::endl;
    myfile << "bkg: " << total_bkg << std::endl <<std::endl;
    std::cout << "evtcat: " << evtcat << std::endl;
    std::cout << "sig: " << total_sig << std::endl;
    std::cout << "bkg: " << total_bkg << std::endl <<std::endl;
  }
  delete inputFile;
  }
}
    
