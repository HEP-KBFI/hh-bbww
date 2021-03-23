
#include <TFile.h>
#include <TString.h>
#include <TH1.h>
#include <TH2.h>
#include <TProfile.h>
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

int colors[7] = { kBlack, kRed, kBlue - 7,  kMagenta - 7, kCyan - 6, kRed - 6, 3 };
int markerStyles[7] = { 24, 25, 20, 21, 22, 23, 20 };
int markerSizes[7] = { 1, 1, 1, 1, 1, 1, 1 };

void divideByBinWidth(TH1* histogram)
{
  if(! (histogram && histogram->GetDimension() == 1))
  {
    return;
  }
  const TAxis * const xAxis = histogram->GetXaxis();
  const int numBins = xAxis->GetNbins();
  for(int idxBin = 1; idxBin <= numBins; ++idxBin)
  {
    const double binContent = histogram->GetBinContent(idxBin);
    const double binError = histogram->GetBinError(idxBin);
    const double binWidth = xAxis->GetBinWidth(idxBin);
    histogram->SetBinContent(idxBin, binContent/binWidth);
    histogram->SetBinError(idxBin, binError/binWidth);
  }
}

TH1* loadHistogram(TFile* inputFile, const std::string& dirName, const std::string& subdirName, const std::string& histogramName)
{
  TString histogramName_full = dirName.data();
  if ( !histogramName_full.EndsWith("/") ) histogramName_full.Append("/");
  histogramName_full.Append(subdirName.data());
  if ( !histogramName_full.EndsWith("/") ) histogramName_full.Append("/");
  histogramName_full.Append(histogramName.data());
  TH1* histogram = dynamic_cast<TH1*>(inputFile->Get(histogramName_full.Data()));
  if ( !histogram ) {
    std::cerr << "Failed to load histogram = " << histogramName_full.Data() << " from file = " << inputFile->GetName() << " !!" << std::endl;
    assert(0);
  }
  if ( !histogram->GetSumw2N() ) histogram->Sumw2();
  histogram->Scale(1./histogram->Integral());
  divideByBinWidth(histogram);
  return histogram;
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

void showHistograms_wRatio(double canvasSizeX, double canvasSizeY,
		           TH1* histogram_ref, const std::string& legendEntry_ref,
		           TH1* histogram2, const std::string& legendEntry2,
		           TH1* histogram3, const std::string& legendEntry3,
		           TH1* histogram4, const std::string& legendEntry4,
		           TH1* histogram5, const std::string& legendEntry5,
		           TH1* histogram6, const std::string& legendEntry6,
                           TH1* histogram7, const std::string& legendEntry7,
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

  TLegend* legend = new TLegend(legendX0, legendY0, legendX0 + 0.38, legendY0 + 0.24, "", "brNDC"); 
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
  legend->AddEntry(histogram_ref, legendEntry_ref.data(), "p");

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
    legend->AddEntry(histogram2, legendEntry2.data(), "p");
  }

  if ( histogram3 ) {
    histogram3->SetLineColor(colors[2]);
    histogram3->SetLineWidth(2);
    histogram3->SetMarkerColor(colors[2]);
    histogram3->SetMarkerStyle(markerStyles[2]);
    histogram3->SetMarkerSize(markerSizes[2]);
    histogram3->Draw("e1psame");
    legend->AddEntry(histogram3, legendEntry3.data(), "p");
  }

  if ( histogram4 ) {
    histogram4->SetLineColor(colors[3]);
    histogram4->SetLineWidth(2);
    histogram4->SetMarkerColor(colors[3]);
    histogram4->SetMarkerStyle(markerStyles[3]);
    histogram4->SetMarkerSize(markerSizes[3]);
    histogram4->Draw("e1psame");
    legend->AddEntry(histogram4, legendEntry4.data(), "p");
  }

  if ( histogram5 ) {
    histogram5->SetLineColor(colors[4]);
    histogram5->SetLineWidth(2);
    histogram5->SetMarkerColor(colors[4]);
    histogram5->SetMarkerStyle(markerStyles[4]);
    histogram5->SetMarkerSize(markerSizes[4]);
    histogram5->Draw("e1psame");
    legend->AddEntry(histogram5, legendEntry5.data(), "p");
  }

  if ( histogram6 ) {
    histogram6->SetLineColor(colors[5]);
    histogram6->SetLineWidth(2);
    histogram6->SetMarkerColor(colors[5]);
    histogram6->SetMarkerStyle(markerStyles[5]);
    histogram6->SetMarkerSize(markerSizes[5]);
    histogram6->Draw("e1psame");
    legend->AddEntry(histogram6, legendEntry6.data(), "p");
  }

  if ( histogram7 ) {
    histogram7->SetLineColor(colors[6]);
    histogram7->SetLineWidth(2);
    histogram7->SetMarkerColor(colors[6]);
    histogram7->SetMarkerStyle(markerStyles[6]);
    histogram7->SetMarkerSize(markerSizes[6]);
    histogram7->Draw("e1psame");
    legend->AddEntry(histogram7, legendEntry7.data(), "p");
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

  TH1* histogram7_div_ref = 0;
  if ( histogram7 ) {
    std::string histogramName7_div_ref = std::string(histogram7->GetName()).append("_div_").append(histogram_ref->GetName());
    histogram7_div_ref = compRatioHistogram(histogramName7_div_ref, histogram7, histogram_ref);
    if ( histogram7_div_ref ) {
      histogram7_div_ref->Draw("e1psame");
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
  delete histogram7_div_ref;
  delete topPad;
  delete bottomPad;
  delete canvas;  
}

void compareGenKinematics_HH_forSiddhesh()
{
  gROOT->SetBatch(true);

  TH1::AddDirectory(false);

  std::string inputFilePath = "/hdfs/local/veelken/hhAnalysis/2016/2021Mar23v3/histograms/hh_HHatLOvsNLO/hadd/";
  std::string inputFileName = "hadd_stage2.root";
  TString inputFileName_full = inputFilePath.data();
  if ( !inputFileName_full.EndsWith("/") ) inputFileName_full.Append("/");
  inputFileName_full.Append(inputFileName.data());
  TFile* inputFile = new TFile(inputFileName_full.Data());
  if ( !inputFile ) {
    std::cerr << "Failed to open input file = " << inputFileName_full.Data() << " !!" << std::endl;
    assert(0);
  }

  std::string dirName = "analyze_HHatLOvsNLO/sel/";

  std::string histogramName = "genHH_mass";

  std::vector<std::string> nodeNames = { "sm", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12" }; 
  for ( std::vector<std::string>::const_iterator nodeName = nodeNames.begin();
        nodeName != nodeNames.end(); ++nodeName ) {
    std::string bmName;
    if ( (*nodeName) == "sm" )
    {
      bmName = "SM";
    }
    else
    {
      bmName = Form("BM%s", nodeName->data());
    }

    std::string subdirName_NLO, legendEntry_NLO;
    if ( (*nodeName) == "sm" )
    {
      subdirName_NLO = "hh_woLOWeights_woLOtoNLOWeights/signal_ggf_nonresonant_cHHH1_hh";
      legendEntry_NLO = "NLO SM";
    }
    else
    {
      subdirName_NLO = Form("hh_%s_wNLOtoNLOWeights_V2/signal_ggf_nonresonant_cHHH1_hh", bmName.data());
      legendEntry_NLO = "NLO SM rew.";
    }
    TH1* histogram_NLO = loadHistogram(inputFile, dirName, subdirName_NLO, histogramName);

    std::string subdirName_LO = Form("hh_woLOWeights_woLOtoNLOWeights/signal_ggf_nonresonant_hh_node_%s", nodeName->data());
    TH1* histogram_LO = loadHistogram(inputFile, dirName, subdirName_LO, histogramName);

    std::string subdirName_sumLO = Form("hh_%s_wLOWeights_woLOtoNLOWeights/signal_ggf_nonresonant_hh", bmName.data());
    TH1* histogram_sumLO = loadHistogram(inputFile, dirName, subdirName_sumLO, histogramName);

    std::string subdirName_LOtoNLO = Form("hh_%s_woLOWeights_wLOtoNLOWeights_V2/signal_ggf_nonresonant_hh_node_%s", bmName.data(), nodeName->data());
    TH1* histogram_LOtoNLO = loadHistogram(inputFile, dirName, subdirName_LOtoNLO, histogramName);

    std::string subdirName_sumLOtoNLO = Form("hh_%s_wLOWeights_wLOtoNLOWeights_V2/signal_ggf_nonresonant_hh", bmName.data());
    TH1* histogram_sumLOtoNLO = loadHistogram(inputFile, dirName, subdirName_sumLOtoNLO, histogramName);

    std::string outputFileName_gen_mHH = Form("plots/compareGenKinematics_HH_forSiddhesh_%s_%s.png", histogramName.data(), bmName.data());
    showHistograms_wRatio(1050, 1050,
                          histogram_NLO, legendEntry_NLO.data(), 
                          histogram_LO, "LO",
                          histogram_sumLO, "#Sigma LO",
                          histogram_LOtoNLO, "LO #Rightarrow NLO",
                          histogram_sumLOtoNLO, "#Sigma LO #Rightarrow NLO",
                          nullptr, "",
                          nullptr, "",
                          "gen. m_{HH} [GeV]", 1.2,
                          true, 1.e-7, 1.e-2, "dN/dm_{HH} [1/GeV]", 1.2,
                          0.61, 0.69,
                          outputFileName_gen_mHH);
  }

  delete inputFile;
}


