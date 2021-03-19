
#include <TFile.h>
#include <TString.h>
#include <TH1.h>
#include <TH2.h>
#include <TGraph.h>
#include <TAxis.h>
#include <TCanvas.h>
#include <TLegend.h>
#include <TMath.h>
#include <TROOT.h>
#include <TStyle.h>

#include <string>
#include <vector>
#include <map>
#include <iostream>
#include <iomanip>
#include <assert.h>

enum { kUndefined, kAbsolute, kRelative };

TH1* loadHistogram(TFile* inputFile, const std::string& histogramName)
{
  TH1* histogram = dynamic_cast<TH1*>(inputFile->Get(histogramName.data()));
  if ( !histogram ) {
    std::cerr << "Failed to load histogram = " << histogramName << " from file = " << inputFile->GetName() << " !!" << std::endl;
    assert(0);
  }
  if ( !histogram->GetSumw2N() ) histogram->Sumw2();
  return histogram;
}

double compIntegral(const TH1* histogram)
{
  if ( !histogram ) return -1.;
  double integral = 0.;
  int numBins = histogram->GetNbinsX();
  for ( int iBin = 1; iBin <= numBins; ++iBin ) {
    double binContent = histogram->GetBinContent(iBin);
    integral += binContent;
  }
  return integral;
}

TH1* compRatioHistogram(const std::string& ratioHistogramName, const TH1* numerator, const TH1* denominator)
{
  TH1* histogramRatio = 0;
  
  if ( numerator->GetDimension() == denominator->GetDimension() &&
       numerator->GetNbinsX() == denominator->GetNbinsX() ) {
    histogramRatio = (TH1*)numerator->Clone(ratioHistogramName.data());
    histogramRatio->Divide(denominator);
    
    int nBins = histogramRatio->GetNbinsX();
    for ( int iBin = 1; iBin <= nBins; ++iBin ){
      double binContent = histogramRatio->GetBinContent(iBin);
      histogramRatio->SetBinContent(iBin, binContent - 1.);
    }
    
    histogramRatio->SetLineColor(numerator->GetLineColor());
    histogramRatio->SetLineWidth(numerator->GetLineWidth());
    histogramRatio->SetMarkerColor(numerator->GetMarkerColor());
    histogramRatio->SetMarkerStyle(numerator->GetMarkerStyle());
    histogramRatio->SetMarkerSize(numerator->GetMarkerSize());
  }

  return histogramRatio;
}

void showHistograms(double canvasSizeX, double canvasSizeY,
		    TH1* histogram_ref, const std::string& legendEntry_ref, double integral_ref,
		    TH1* histogram2, const std::string& legendEntry2, double integral2,
		    TH1* histogram3, const std::string& legendEntry3, double integral3,
		    TH1* histogram4, const std::string& legendEntry4, double integral4,
		    TH1* histogram5, const std::string& legendEntry5, double integral5,
		    TH1* histogram6, const std::string& legendEntry6, double integral6,
		    const std::string& xAxisTitle, double xAxisOffset,
		    bool useLogScale, double yMin, double yMax, const std::string& yAxisTitle, double yAxisOffset,
		    double legendX0, double legendY0, 
		    const std::string& outputFileName)
{
  if ( !(histogram_ref && histogram2) ) return;

  TCanvas* canvas = new TCanvas("canvas", "canvas", canvasSizeX, canvasSizeY);
  canvas->SetFillColor(10);
  canvas->SetBorderSize(2);
  canvas->SetLeftMargin(0.12);
  canvas->SetBottomMargin(0.12);

  TPad* topPad = new TPad("topPad", "topPad", 0.00, 0.35, 1.00, 1.00);
  topPad->SetFillColor(10);
  topPad->SetTopMargin(0.04);
  topPad->SetLeftMargin(0.15);
  topPad->SetBottomMargin(0.03);
  topPad->SetRightMargin(0.05);
  topPad->SetLogy(useLogScale);

  TPad* bottomPad = new TPad("bottomPad", "bottomPad", 0.00, 0.00, 1.00, 0.35);
  bottomPad->SetFillColor(10);
  bottomPad->SetTopMargin(0.02);
  bottomPad->SetLeftMargin(0.15);
  bottomPad->SetBottomMargin(0.24);
  bottomPad->SetRightMargin(0.05);
  bottomPad->SetLogy(false);

  canvas->cd();
  topPad->Draw();
  topPad->cd();

  //int colors[6] = { kBlack, kGreen - 6, kBlue - 7,  kMagenta - 7, kCyan - 6, kRed - 6 };
  int colors[6] = { kBlack, kRed, kBlue - 7,  kMagenta - 7, kCyan - 6, kRed - 6 };
  int markerStyles[6] = { 24, 25, 20, 21, 22, 23 };
  int markerSizes[6] = { 1, 1, 1, 1, 1, 1 };

  TLegend* legend = new TLegend(legendX0, legendY0, legendX0 + 0.61, legendY0 + 0.21, "", "brNDC"); 
  legend->SetBorderSize(0);
  legend->SetFillColor(0);

  histogram_ref->SetTitle("");
  histogram_ref->SetStats(false);
  histogram_ref->SetMinimum(yMin);
  histogram_ref->SetMaximum(yMax);
  histogram_ref->SetLineColor(colors[0]);
  histogram_ref->SetLineWidth(2);
  histogram_ref->SetMarkerColor(colors[0]);
  histogram_ref->SetMarkerStyle(markerStyles[0]);
  histogram_ref->SetMarkerSize(markerSizes[0]);
  histogram_ref->Draw("e1p");
  //if ( integral_ref >= 0. ) legend->AddEntry(histogram_ref, Form("%s: %1.2f", legendEntry_ref.data(), integral_ref), "p");
  //else legend->AddEntry(histogram_ref, legendEntry_ref.data(), "p");
  legend->AddEntry(histogram_ref, Form("%s: %1.2f", legendEntry_ref.data(), integral_ref), "p");

  TAxis* xAxis_top = histogram_ref->GetXaxis();
  xAxis_top->SetTitle(xAxisTitle.data());
  xAxis_top->SetTitleOffset(xAxisOffset);
  xAxis_top->SetLabelColor(10);
  xAxis_top->SetTitleColor(10);

  TAxis* yAxis_top = histogram_ref->GetYaxis();
  yAxis_top->SetTitle(yAxisTitle.data());
  yAxis_top->SetTitleOffset(yAxisOffset);

  if ( histogram2 ) {
    histogram2->SetLineColor(colors[1]);
    histogram2->SetLineWidth(2);
    histogram2->SetMarkerColor(colors[1]);
    histogram2->SetMarkerStyle(markerStyles[1]);
    histogram2->SetMarkerSize(markerSizes[1]);
    histogram2->Draw("e1psame");
    //if ( integral2 >= 0. ) legend->AddEntry(histogram2, Form("%s: %1.2f", legendEntry2.data(), integral2), "p");
    //else legend->AddEntry(histogram2, legendEntry2.data(), "p");
    legend->AddEntry(histogram2, Form("%s: %1.2f", legendEntry2.data(), integral2), "p");
  }

  if ( histogram3 ) {
    histogram3->SetLineColor(colors[2]);
    histogram3->SetLineWidth(2);
    histogram3->SetMarkerColor(colors[2]);
    histogram3->SetMarkerStyle(markerStyles[2]);
    histogram3->SetMarkerSize(markerSizes[2]);
    histogram3->Draw("e1psame");
    //if ( integral3 >= 0. ) legend->AddEntry(histogram3, Form("%s: %1.2f", legendEntry3.data(), integral3), "p");
    //else legend->AddEntry(histogram3, legendEntry3.data(), "p");
    legend->AddEntry(histogram3, Form("%s: %1.2f", legendEntry3.data(), integral3), "p");
  }

  if ( histogram4 ) {
    histogram4->SetLineColor(colors[3]);
    histogram4->SetLineWidth(2);
    histogram4->SetMarkerColor(colors[3]);
    histogram4->SetMarkerStyle(markerStyles[3]);
    histogram4->SetMarkerSize(markerSizes[3]);
    histogram4->Draw("e1psame");
    if ( integral4 >= 0. ) legend->AddEntry(histogram4, Form("%s: %1.2f", legendEntry4.data(), integral4), "p");
    else legend->AddEntry(histogram4, legendEntry4.data(), "p");
  }

  if ( histogram5 ) {
    histogram5->SetLineColor(colors[4]);
    histogram5->SetLineWidth(2);
    histogram5->SetMarkerColor(colors[4]);
    histogram5->SetMarkerStyle(markerStyles[4]);
    histogram5->SetMarkerSize(markerSizes[4]);
    histogram5->Draw("e1psame");
    if ( integral5 >= 0. ) legend->AddEntry(histogram5, Form("%s: %1.2f", legendEntry5.data(), integral5), "p");
    else legend->AddEntry(histogram5, legendEntry5.data(), "p");
  }

  if ( histogram6 ) {
    histogram6->SetLineColor(colors[5]);
    histogram6->SetLineWidth(2);
    histogram6->SetMarkerColor(colors[5]);
    histogram6->SetMarkerStyle(markerStyles[5]);
    histogram6->SetMarkerSize(markerSizes[5]);
    histogram6->Draw("e1psame");
    if ( integral6 >= 0. ) legend->AddEntry(histogram6, Form("%s: %1.2f", legendEntry6.data(), integral6), "p");
    else legend->AddEntry(histogram6, legendEntry6.data(), "p");
  }

  legend->Draw();

  canvas->cd();
  bottomPad->Draw();
  bottomPad->cd();

  TH1* histogram2_div_ref = 0;
  if ( histogram2 ) {
    std::string histogramName2_div_ref = std::string(histogram2->GetName()).append("_div_").append(histogram_ref->GetName());
    histogram2_div_ref = compRatioHistogram(histogramName2_div_ref, histogram2, histogram_ref);
    if ( histogram2_div_ref ) {
      histogram2_div_ref->SetTitle("");
      histogram2_div_ref->SetStats(false);
      histogram2_div_ref->SetMinimum(-1.00);
      histogram2_div_ref->SetMaximum(+1.00);
      
      TAxis* xAxis_bottom = histogram2_div_ref->GetXaxis();
      xAxis_bottom->SetTitle(xAxis_top->GetTitle());
      xAxis_bottom->SetLabelColor(1);
      xAxis_bottom->SetTitleColor(1);
      xAxis_bottom->SetTitleOffset(1.20);
      xAxis_bottom->SetTitleSize(0.08);
      xAxis_bottom->SetLabelOffset(0.02);
      xAxis_bottom->SetLabelSize(0.08);
      xAxis_bottom->SetTickLength(0.055);
      
      TAxis* yAxis_bottom = histogram2_div_ref->GetYaxis();
      yAxis_bottom->SetTitle(Form("#frac{%s - %s}{%s}", legendEntry2.data(), legendEntry_ref.data(), legendEntry_ref.data()));
      yAxis_bottom->SetTitleOffset(0.85);
      yAxis_bottom->SetNdivisions(505);
      yAxis_bottom->CenterTitle();
      yAxis_bottom->SetTitleSize(0.08);
      yAxis_bottom->SetLabelSize(0.08);
      yAxis_bottom->SetTickLength(0.04);  
      
      histogram2_div_ref->Draw("e1p");
    }
  }

  TH1* histogram3_div_ref = 0;
  if ( histogram3 ) {
    std::string histogramName3_div_ref = std::string(histogram3->GetName()).append("_div_").append(histogram_ref->GetName());
    histogram3_div_ref = compRatioHistogram(histogramName3_div_ref, histogram3, histogram_ref);
    if ( histogram3_div_ref ) {
      histogram3_div_ref->SetTitle("");
      histogram3_div_ref->SetStats(false);
      histogram3_div_ref->SetMinimum(-0.50);
      histogram3_div_ref->SetMaximum(+0.50);
      
      TAxis* xAxis_bottom = histogram3_div_ref->GetXaxis();
      xAxis_bottom->SetTitle(xAxis_top->GetTitle());
      xAxis_bottom->SetLabelColor(1);
      xAxis_bottom->SetTitleColor(1);
      xAxis_bottom->SetTitleOffset(1.20);
      xAxis_bottom->SetTitleSize(0.08);
      xAxis_bottom->SetLabelOffset(0.02);
      xAxis_bottom->SetLabelSize(0.08);
      xAxis_bottom->SetTickLength(0.055);
      
      TAxis* yAxis_bottom = histogram3_div_ref->GetYaxis();
      yAxis_bottom->SetTitle(Form("#frac{%s - %s}{%s}", legendEntry3.data(), legendEntry_ref.data(), legendEntry_ref.data()));
      yAxis_bottom->SetTitleOffset(0.85);
      yAxis_bottom->SetNdivisions(505);
      yAxis_bottom->CenterTitle();
      yAxis_bottom->SetTitleSize(0.08);
      yAxis_bottom->SetLabelSize(0.08);
      yAxis_bottom->SetTickLength(0.04);  
      
      if ( histogram2 ) histogram3_div_ref->Draw("e1psame");
      else histogram3_div_ref->Draw("e1p");
    }
  }

  TGraph* graph_line = new TGraph(2);
  graph_line->SetPoint(0, xAxis_top->GetXmin(), 0.);
  graph_line->SetPoint(1, xAxis_top->GetXmax(), 0.);
  graph_line->SetLineColor(8);
  graph_line->SetLineWidth(1);
  graph_line->Draw("L");

  if ( histogram2_div_ref ) histogram2_div_ref->Draw("e1psame");
  if ( histogram3_div_ref ) histogram3_div_ref->Draw("e1psame");

  TH1* histogram4_div_ref = 0;
  if ( histogram4 ) {
    std::string histogramName4_div_ref = std::string(histogram4->GetName()).append("_div_").append(histogram_ref->GetName());
    histogram4_div_ref = compRatioHistogram(histogramName4_div_ref, histogram4, histogram_ref);
    if ( histogram4_div_ref ) {
      histogram4_div_ref->Draw("e1psame");
    }
  }

  TH1* histogram5_div_ref = 0;
  if ( histogram5 ) {
    std::string histogramName5_div_ref = std::string(histogram5->GetName()).append("_div_").append(histogram_ref->GetName());
    histogram5_div_ref = compRatioHistogram(histogramName5_div_ref, histogram5, histogram_ref);
    if ( histogram5_div_ref ) {
      histogram5_div_ref->Draw("e1psame");
    }
  }

  TH1* histogram6_div_ref = 0;
  if ( histogram6 ) {
    std::string histogramName6_div_ref = std::string(histogram6->GetName()).append("_div_").append(histogram_ref->GetName());
    histogram6_div_ref = compRatioHistogram(histogramName6_div_ref, histogram6, histogram_ref);
    if ( histogram6_div_ref ) {
      histogram6_div_ref->Draw("e1psame");
    }
  }
  
  canvas->Update();
  size_t idx = outputFileName.find_last_of('.');
  std::string outputFileName_plot = std::string(outputFileName, 0, idx);
  if ( useLogScale ) outputFileName_plot.append("_log");
  else outputFileName_plot.append("_linear");
  if ( idx != std::string::npos ) canvas->Print(std::string(outputFileName_plot).append(std::string(outputFileName, idx)).data());
  canvas->Print(std::string(outputFileName_plot).append(".png").data());
  //canvas->Print(std::string(outputFileName_plot).append(".pdf").data());
  //canvas->Print(std::string(outputFileName_plot).append(".root").data());
  
  delete legend;
  delete histogram2_div_ref;
  delete histogram3_div_ref;
  delete histogram4_div_ref;
  delete histogram5_div_ref;
  delete histogram6_div_ref;
  delete topPad;
  delete bottomPad;
  delete canvas;  
}

void compareHHatLOvsNLO()
{
  gROOT->SetBatch(true);

  TH1::AddDirectory(false);

  std::vector<std::string> periods;
  //periods.push_back("2016");
  //periods.push_back("2017");
  periods.push_back("2018");

  std::map<std::string, std::string> inputFilePaths; // key = data-taking period
  inputFilePaths["2016"] = "/hdfs/local/veelken/hhAnalysis/2016/2020Nov31/histograms/hh_bb1l/Tight/";
  inputFilePaths["2017"] = "/hdfs/local/veelken/hhAnalysis/2017/2020Dec22/histograms/hh_bb1l/Tight/";
  inputFilePaths["2018"] = "/hdfs/local/veelken/hhAnalysis/2018/2021Feb22/histograms/hh_bb1l/Tight/";

  std::string inputFileName_LO_woHHReweighting = "signal_ggf_nonresonant_node_sm_hh_2b2v_sl/analyze_signal_ggf_nonresonant_node_sm_hh_2b2v_sl_Tight_central_1_woHHReweighting.root";
  //std::string inputFileName_LO_wHHReweighting = "hadd/hadd_signal_ggf_nonresonant_allNodes_hh_2b2v_sl_Tight_central.root";
  std::string inputFileName_NLO = "signal_ggf_nonresonant_cHHH1_hh_2b2v_sl/analyze_signal_ggf_nonresonant_cHHH1_hh_2b2v_sl_Tight_central_1.root";

  std::vector<std::string> categories;
  categories.push_back("BDT_resolved_2b_nonvbf");
  categories.push_back("BDT_resolved_2b_vbf");
  categories.push_back("BDT_resolved_1b");
  categories.push_back("BDT_boosted");

  std::map<std::string, std::string> directoryNames; // key = category
  directoryNames["BDT_resolved_2b_nonvbf"] = "hh_bb1l_Tight/sel/datacard/BDT/resolved_2b_nonvbf";
  directoryNames["BDT_resolved_2b_vbf"]    = "hh_bb1l_Tight/sel/datacard/BDT/resolved_2b_vbf";
  directoryNames["BDT_resolved_1b"]        = "hh_bb1l_Tight/sel/datacard/BDT/resolved_1b";
  directoryNames["BDT_boosted"]            = "hh_bb1l_Tight/sel/datacard/BDT/boosted";

  std::string subdirectoryName_LO_woHHReweighting = "signal_ggf_nonresonant_hh";
  //std::string subdirectoryName_LO_wHHReweighting = "signal_ggf_nonresonant_hh";
  std::string subdirectoryName_NLO = "signal_ggf_nonresonant_cHHH1_hh";

  std::string histogramName = "MVAOutput_SM";

  double sf_LO_woHHReweighting = 1.00;
  //double sf_LO_wHHReweighting = 1.00;
  double sf_NLO = 33.50;

  for ( std::vector<std::string>::const_iterator period = periods.begin();
        period != periods.end(); ++period ) {
    TString inputFileName_LO_woHHReweighting_full = inputFilePaths[*period].data();
    if ( !inputFileName_LO_woHHReweighting_full.EndsWith("/") ) inputFileName_LO_woHHReweighting_full.Append("/");
    inputFileName_LO_woHHReweighting_full.Append(inputFileName_LO_woHHReweighting.data());
    TFile* inputFile_LO_woHHReweighting = new TFile(inputFileName_LO_woHHReweighting_full.Data());
    if ( !inputFile_LO_woHHReweighting ) {
      std::cerr << "Failed to open input file = " << inputFileName_LO_woHHReweighting_full.Data() << " !!" << std::endl;
      assert(0);
    }
  
    //TString inputFileName_LO_wHHReweighting_full = inputFilePaths[*period].data();
    //if ( !inputFileName_LO_wHHReweighting_full.EndsWith("/") ) inputFileName_LO_wHHReweighting_full.Append("/");
    //inputFileName_LO_wHHReweighting_full.Append(inputFileName_LO_wHHReweighting.data());
    //TFile* inputFile_LO_wHHReweighting = new TFile(inputFileName_LO_wHHReweighting_full.Data());
    //if ( !inputFile_LO_wHHReweighting ) {
    //  std::cerr << "Failed to open input file = " << inputFileName_LO_wHHReweighting_full.Data() << " !!" << std::endl;
    //  assert(0);
    //}

    TString inputFileName_NLO_full = inputFilePaths[*period].data();
    if ( !inputFileName_NLO_full.EndsWith("/") ) inputFileName_NLO_full.Append("/");
    inputFileName_NLO_full.Append(inputFileName_NLO.data());
    TFile* inputFile_NLO = new TFile(inputFileName_NLO_full.Data());
    if ( !inputFile_NLO ) {
      std::cerr << "Failed to open input file = " << inputFileName_NLO_full.Data() << " !!" << std::endl;
      assert(0);
    }

    for ( std::vector<std::string>::const_iterator category = categories.begin();
          category != categories.end(); ++category ) {
      std::string histogramName_LO_woHHReweighting_full = Form("%s/%s/%s", directoryNames[*category].data(), subdirectoryName_LO_woHHReweighting.data(), histogramName.data());
      TH1* histogram_LO_woHHReweighting = loadHistogram(inputFile_LO_woHHReweighting, histogramName_LO_woHHReweighting_full);
      histogram_LO_woHHReweighting->Scale(sf_LO_woHHReweighting);
      double integral_LO_woHHReweighting = compIntegral(histogram_LO_woHHReweighting);

      //std::string histogramName_LO_wHHReweighting_full = Form("%s/%s/%s", directoryNames[*category].data(), subdirectoryName_LO_wHHReweighting.data(), histogramName.data());
      //TH1* histogram_LO_wHHReweighting = loadHistogram(inputFile_LO_wHHReweighting, histogramName_LO_wHHReweighting_full);
      //histogram_LO_wHHReweighting->Scale(sf_LO_woHHReweighting);
      //double integral_LO_wHHReweighting = compIntegral(histogram_LO_wHHReweighting);

      std::string histogramName_NLO_full = Form("%s/%s/%s", directoryNames[*category].data(), subdirectoryName_NLO.data(), histogramName.data());
      TH1* histogram_NLO = loadHistogram(inputFile_NLO, histogramName_NLO_full);
      histogram_NLO->Scale(sf_NLO);
      double integral_NLO = compIntegral(histogram_NLO);

      histogram_LO_woHHReweighting->Scale(integral_NLO/integral_LO_woHHReweighting);
      integral_LO_woHHReweighting = compIntegral(histogram_LO_woHHReweighting);

      std::string outputFileName = Form("plots/compareHHatLOvsNLO_%s_%s.png", category->data(), period->data());
      showHistograms(800, 1050,
                     histogram_NLO, "NLO", integral_NLO,
                     histogram_LO_woHHReweighting, "LO (woHHRew)", integral_LO_woHHReweighting,
                     //histogram_LO_wHHReweighting, "LO (wHHRew)", integral_LO_wHHReweighting,
                     nullptr, "", -1.,
                     nullptr, "", -1.,
                     nullptr, "", -1.,
                     nullptr, "", -1.,
                     "MVA Output", 1.2,
                     true, 1.e-2, 1.e+3, "Events", 1.2,
                     0.22, 0.74,
                     outputFileName);
    }

    delete inputFile_LO_woHHReweighting;
    //delete inputFile_LO_wHHReweighting;
    delete inputFile_NLO;
  }
}


