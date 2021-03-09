
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
  if ( inputfile.find("BDT") != std::string::npos ) {
    return "BDT";
  }
  else if ( inputfile.find("LBN") != std::string::npos ) {
      return "LBN";
  }
  return "";
}

bool cmp(pair<std::string, pair<double,double>>& a,
         pair<std::string, pair<double,double>>& b)
{
  return a.second.first > b.second.first;
}

void dumpEventYields_1(std::string era, std::string category, std::string inputfile)
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
    evtcats.push_back("HH_resolved_1b_vbf");
    evtcats.push_back("HH_resolved_1b_nonvbf");
    /*evtcats.push_back("GGF_HH_resolved_2b");
    evtcats.push_back("VBF_HH_resolved_2b");
    evtcats.push_back("GGF_HH_resolved_1b");
    evtcats.push_back("VBF_HH_resolved_1b");*/
    evtcats.push_back("HH_boosted");
    evtcats.push_back("TT_resolved");
    evtcats.push_back("TT_boosted");
    evtcats.push_back("W_resolved");
    evtcats.push_back("W_boosted");
    evtcats.push_back("DY_resolved");
    evtcats.push_back("DY_boosted");
    evtcats.push_back("SingleTop_resolved");
    evtcats.push_back("SingleTop_boosted");
    evtcats.push_back("Other");
  }
  
  //  std::cout << BDT_evtcat << std::endl;
  ofstream myfile (Form("eventYield_%s.txt", era.c_str()));
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
    //signal_processes.push_back(Form("%s_Convs", inclusive_proc.data()));
    //signal_processes.push_back(Form("%s_fake", inclusive_proc.data()));
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
  background_processes.push_back("TTW");
  background_processes.push_back("TTWW");
  background_processes.push_back("VV");
  background_processes.push_back("VVV");
  background_processes.push_back("Convs");
  background_processes.push_back("Other");
  background_processes.push_back("WZ");
  background_processes.push_back("WW");
  background_processes.push_back("qqZZ");
  background_processes.push_back("ggZZ");
  vstring inclusive_procss;
  inclusive_procss.push_back("TH");
  inclusive_procss.push_back("ggH");
  inclusive_procss.push_back("qqH");
  inclusive_procss.push_back("ZH");
  inclusive_procss.push_back("WH");
  inclusive_procss.push_back("tHq");
  inclusive_procss.push_back("tHW");
  inclusive_procss.push_back("TTH");
  vstring brs;
  brs.push_back("hww");
  brs.push_back("hbb");
  brs.push_back("hzz");
  brs.push_back("htt");
  for (auto inclusive_proc: inclusive_procss) {
    for ( auto br: brs ) {
      background_processes.push_back(Form("%s_%s", inclusive_proc.data(), br.data()));
    }
  }
  std::vector<std::string> background_process_parts;
  background_process_parts.push_back("");
  //background_process_parts.push_back("_Convs");
  //background_process_parts.push_back("_fake");
  TString inputFileName_full = inputfile.data();
  TFile* inputFile;
  std::size_t pos = inputfile.rfind(MVAtype);
  double totSig(0.);
  double totBkg(0.);
  double totTT(0.);
  double totST(0.);
  double totW(0.);
  double totDY(0.);
  double totfake(0);
  double totSingleH(0.);
  double totData(0.);
  for (auto evtcat: evtcats) {
    Double_t total_bkg(0);
    Double_t total_sig(0);
    Double_t total_sig_conv(0.);
    std::vector<std::pair<string, std::pair<double, double>> > cat_yield;
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
          if ( histogramName.find("Convs") != std::string::npos ) {
            total_sig_conv +=integral;
          }
          else {
            total_sig +=integral;
          }
        }
      }
      double integralErr_sum = TMath::Sqrt(integralErr2_sum);
      myfile << signal_process << ": " << integral_sum << " +/- " << integralErr_sum << std::endl;
      if ( integral_parts.size() > 1 ) {
        myfile << " (non-fake = " << integral_parts[""] << " +/- " << integralErr_parts[""] << ","
          //<< " fake = " << integral_parts["_fake"] << " +/- " << integralErr_parts["_fake"] << ","
               << " conversion = " << integral_parts["_Convs"] << " +/- " << integralErr_parts["_Convs"] << ")" << std::endl;
      }
    }
    double integral_SingleHsum = 0.;
    double integralErr2_SingleHsum = 0;
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
          if ( histogramName.find("TH") != std::string::npos ||
               histogramName.find("TTH") != std::string::npos ||
               histogramName.find("WH") != std::string::npos ||
               histogramName.find("ZH") != std::string::npos ||
               histogramName.find("qqH") != std::string::npos ||
               histogramName.find("ggH") != std::string::npos ||
               histogramName.find("tHq") != std::string::npos ||
               histogramName.find("tHW") != std::string::npos )
            {
            double integral = compIntegral(histogram);
            integral_SingleHsum += integral;
            double integral_Err = compIntegralErr(histogram);
            integralErr2_SingleHsum += square(integral_Err);
            total_bkg +=integral;
            totSingleH += integral;
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
           (background_process.find("ZH") == std::string::npos) &&
           (background_process.find("qqH") == std::string::npos) && (background_process.find("ggH") == std::string::npos) &&
           (background_process.find("tHW") == std::string::npos) && (background_process.find("tHq") == std::string::npos) ) 
        {
          if (background_process == "TT") totTT += integral_parts[""];
          if (background_process == "W")  totW += integral_parts[""];
          if (background_process == "ST") totST += integral_parts[""];
          if (background_process == "DY") totDY += integral_parts[""];
          if (background_process == "data_fakes") totfake += integral_parts[""];
          cat_yield.push_back(std::pair<std::string, std::pair<double,double>> (background_process, std::pair<double,double>(integral_parts[""],integralErr_parts[""])));
          //myfile << background_process << ": " << integral_sum << " +/- " << integralErr_sum << std::endl;
          //if ( integral_parts.size() > 1 ) {
          //myfile << " (non-fake = " << integral_parts[""] << " +/- " << integralErr_parts[""] << ","
          //       << " fake = " << integral_parts["_fake"] << " +/- " << integralErr_parts["_fake"] << ","
          //       << " conversion = " << integral_parts["_Convs"] << " +/- " << integralErr_parts["_Convs"] << ")" << std::endl;
          //}
        }
    }  
    cat_yield.push_back(std::pair<std::string, std::pair<double,double>> ("SingleH", std::pair<double,double>(integral_SingleHsum, TMath::Sqrt(integralErr2_SingleHsum))));
    sort(cat_yield.begin(), cat_yield.end(), cmp);
    //myfile << "SingleH: " <<  integral_SingleHsum << "+/- " << integralErr2_SingleHsum  << std::endl;
    //myfile << "TW: " <<  integral_TWsum << "+/- " << integralErr2_TWsum  << std::endl;
    for (auto& it : cat_yield) {
      if (it.second.first !=0) {
        myfile << it.first << " "
               << it.second.first << " +/ " << it.second.second  << endl;
      } 
    }
    std::string histogramName = Form("%s/sel/datacard/%s/%s/%s/%s",
            category.data(), MVAtype.data(), evtcat.data(), "data_obs", histogram.data());
    TH1* histogram_ = loadHistogram(inputFile, histogramName);
    double integral(0.);
    if ( histogram_ ) {
      integral = compIntegral(histogram_);
      totData += integral;
      myfile << "data_obs: " << integral << std::endl;
      std::cout << "data_obs: " << integral << std::endl;
    }
    totSig += total_sig;
    totBkg += total_bkg; 
    myfile << "sig: " << total_sig << std::endl;
    myfile << "bkg: " << total_bkg << "\t s/sqrt(B): " << total_sig/TMath::Sqrt(total_bkg) << std::endl <<std::endl;
    myfile << "disagreement in data-mc: " << std::abs(integral-total_bkg)/integral << std::endl;
    std::cout << "evtcat: " << evtcat << std::endl;
    std::cout << "sig: " << total_sig << "\t" << "sig conv: " << total_sig_conv << std::endl;
    std::cout << "bkg: " << total_bkg << std::endl <<std::endl;
  }
  delete inputFile;
  }
  myfile << "totsig: " << totSig << "\t" << "totBkg: " << totBkg << std::endl;
  myfile << "totTT: " << totTT << std::endl;
  myfile << "totST: " << totST << std::endl;
  myfile << "totDY: " << totDY << std::endl;
  myfile << "totW: " << totW << std::endl;
  myfile << "totSingleH: " << totSingleH << std::endl;
  myfile << "totData: " << totData << std::endl;
  myfile << "totfake: " << totfake << std::endl;
}
    
