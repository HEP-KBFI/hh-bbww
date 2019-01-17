 
#include "TFile.h"
#include "TDirectory.h"
#include "TH1.h"
#include "TH2.h"
#include "TGraphErrors.h"
#include "TCanvas.h"
#include "TLegend.h"
#include "TPaveText.h"
#include "TMath.h"
#include "TString.h"

#include <string>
#include <vector>
#include <iostream>
#include <iomanip>
#include <assert.h>

TH1* loadHistogram1d(TFile* inputFile, const std::string& directory, const std::string& histogramName)
{  
  TString histogram1dName_full = Form("%s", directory.data());
  if ( !histogram1dName_full.EndsWith("/") ) histogram1dName_full.Append("/");
  histogram1dName_full.Append(histogramName.data());

  TH1* histogram1d = (TH1*)inputFile->Get(histogram1dName_full.Data());
  //std::cout << "histogram1d = " << histogram1d << std::endl;

  if ( histogram1d && !histogram1d->GetSumw2N() ) histogram1d->Sumw2();
  else if ( !histogram1d ) 
    std::cerr << "Failed to load histogram = " << histogram1dName_full << " from file = " << inputFile->GetName() << " !!" << std::endl;

  return histogram1d;
}

TH2* loadHistogram2d(TFile* inputFile, const std::string& directory, const std::string& histogramName)
{
  TH1* histogram1d = loadHistogram1d(inputFile, directory, histogramName);
  //std::cout << "histogram1d = " << histogram1d << std::endl;
  
  TH2* histogram2d = dynamic_cast<TH2*>(histogram1d);
  //std::cout << "histogram2d = " << histogram2d << std::endl;
  if ( !histogram2d ) 
    std::cerr << "Histogram = " << histogramName << " loaded from file = " << inputFile->GetName() << " is not of type TH2 !!" << std::endl;

  return histogram2d;
}

TH1* compHistogramResponse(const std::string& histogram1dName, TH2* histogram2d, double minOfflineTauPt)
{
  //std::cout << "<compHistogramResponse>:" << std::endl;
  TAxis* xAxis = histogram2d->GetXaxis();
  int numBinsX = xAxis->GetNbins();
  TAxis* yAxis = histogram2d->GetYaxis();
  int numBinsY = yAxis->GetNbins();
  //TArrayF histogram1dBinning(numBinsX + 1);
  //for ( int iBinX = 1; iBinX <= numBinsX; ++iBinX ) {
  //  histogram1dBinning[iBinX - 1] = xAxis->GetBinLowEdge(iBinX);
  //  histogram1dBinning[iBinX] = xAxis->GetBinUpEdge(iBinX);
  //}
  //TH1* histogram1d = new TH1D(histogram1dName.data(), histogram1dName.data(), numBinsX, histogram1dBinning.GetArray());
  TH1* histogram1d = new TH1D(histogram1dName.data(), histogram1dName.data(), 300, 0., 3.);
  for ( int iBinX = 1; iBinX <= numBinsX; ++iBinX ) {
    double binCenterX = xAxis->GetBinCenter(iBinX);    
    if ( !(binCenterX > minOfflineTauPt) ) continue;
    for ( int iBinY = 1; iBinY <= numBinsY; ++iBinY ) {
      double binCenterY = yAxis->GetBinCenter(iBinY);
      if ( binCenterY < 1. ) continue; // CV: skip events for which there is no L1Tau object
      double binContent = histogram2d->GetBinContent(iBinX, iBinY);
      double binErr = histogram2d->GetBinError(iBinX, iBinY);
      int iBin1d = histogram1d->FindBin(binCenterY/binCenterX);
      double binContent1d = histogram1d->GetBinContent(iBin1d);
      double binErr1d = histogram1d->GetBinError(iBin1d);
      histogram1d->SetBinContent(iBin1d, binContent + binContent1d);
      histogram1d->SetBinError(iBin1d, TMath::Sqrt(binErr*binErr + binErr1d*binErr1d));
    }
  }
  //for ( int iBin1d = 1; iBin1d <= 300; ++iBin1d ) {
  //  double binCenter1d = histogram1d->GetBinCenter(iBin1d);
  //  double binContent1d = histogram1d->GetBinContent(iBin1d);
  //  double binErr1d = histogram1d->GetBinError(iBin1d);
  //  std::cout << "bin #" << iBin1d << " (binCenter = " << binCenter1d << "): " << binContent1d << " +/- " << binErr1d << std::endl;
  //}
  //std::cout << "mean = " << histogram1d->GetMean() << " +/- " << histogram1d->GetMeanError() << std::endl;
  //assert(0);
  return histogram1d;
} 

TGraph* compGraphRateVsL1TauPt(const std::string& graphName, const TH1* histogram1d, double averageL1TauResponse = 1.0);

TGraph* compGraphEfficiencyVsL1TauPt(const std::string& graphName, const TH2* histogram2d, double minOfflineTauPt, double averageL1TauResponse = 1.0)
{
  TAxis* xAxis = histogram2d->GetXaxis();
  int numBinsX = xAxis->GetNbins();
  int firstBinX = -1;
  for ( int iBinX = 1; iBinX <= numBinsX; ++iBinX ) {
    double binCenter = xAxis->GetBinCenter(iBinX);
    if ( binCenter > minOfflineTauPt ) {
      firstBinX = iBinX;
      break;
    }
  }
  assert(firstBinX >= 1 && firstBinX <= numBinsX);
  int lastBinX = numBinsX;
  std::string histogramNameProjectionY = Form("histogramProjectionY_%s", graphName.data());
  TH1* histogramProjectionY = histogram2d->ProjectionY(histogramNameProjectionY.data(), firstBinX, lastBinX);
  TGraph* graphEfficiency = compGraphRateVsL1TauPt(graphName, histogramProjectionY, averageL1TauResponse);
  delete histogramProjectionY;
  return graphEfficiency;
} 

TGraph* compGraphRateVsL1TauPt(const std::string& graphName, const TH1* histogram1d, double averageL1TauResponse)
{
  TAxis* xAxis = histogram1d->GetXaxis();
  int numPoints = xAxis->GetNbins();
  TGraph* graphRate = new TGraph(numPoints);
  graphRate->SetName(graphName.data());
  graphRate->SetPoint(0, 0., 1.0);
  double integral = histogram1d->Integral(1, histogram1d->GetNbinsX());
  double sum = 0.;
  for ( int iPoint = 0; iPoint < numPoints; ++iPoint ) {
    double binCenter = 0.;
    if ( iPoint >= 1 ) {      
      int iBin = iPoint;
      binCenter = xAxis->GetBinCenter(iBin);
      double binContent = histogram1d->GetBinContent(iBin);
      sum += binContent;
    }
    graphRate->SetPoint(iPoint, binCenter/averageL1TauResponse, 1.0 - (sum/integral));
  }
  return graphRate;
} 

TGraph* compGraphEfficiencyVsOfflineTauPt(const std::string& graphName, const TH2* histogram2d, double minL1TauPt)
{
  TAxis* xAxis = histogram2d->GetXaxis();
  int numBinsX = xAxis->GetNbins();
  TAxis* yAxis = histogram2d->GetYaxis();
  int numBinsY = yAxis->GetNbins();
  int numPoints = numBinsX;
  TGraph* graphEfficiency = new TGraph(numPoints);
  graphEfficiency->SetName(graphName.data());
  for ( int iBinX = 1; iBinX <= numBinsX; ++iBinX ) {
    double binCenterX = xAxis->GetBinCenter(iBinX);
    double integral = 0.;
    double sum = 0.;
    for ( int iBinY = 1; iBinY <= numBinsY; ++iBinY ) {
      double binCenterY = yAxis->GetBinCenter(iBinY);
      double binContent = histogram2d->GetBinContent(iBinX, iBinY);
      if ( binCenterY > minL1TauPt ) sum += binContent;
      integral += binContent;
    }
    int iPoint = iBinX - 1;
    graphEfficiency->SetPoint(iPoint, binCenterX, sum/integral);
  }
  return graphEfficiency;
} 

TGraph* compGraphROCcurve(const std::string& graphName, const TGraph* graph_efficiency, const TGraph* graph_rate)
{
  int numPoints = graph_efficiency->GetN();
  TGraph* graphROCcurve = new TGraph(numPoints);
  graphROCcurve->SetName(graphName.data());
  for ( int iPoint = 0; iPoint < numPoints; ++iPoint ) {
    double l1TauPt, efficiency;
    graph_efficiency->GetPoint(iPoint, l1TauPt, efficiency);
    double rate = graph_rate->Eval(l1TauPt);
    double xROCcurve = efficiency;
    double yROCcurve = 1.0 - rate;
    graphROCcurve->SetPoint(iPoint, xROCcurve, yROCcurve);
  }
  return graphROCcurve;
}

TH1* rebinHistogram(const TH1* histogram, unsigned numBinsMin_rebinned, double xMin, double xMax)
{
  TH1* histogram_rebinned = 0;

  if ( histogram ) {
    histogram_rebinned = (TH1*)histogram->Clone(std::string(histogram->GetName()).append("_rebinned").data());
    if ( !histogram_rebinned->GetSumw2N() ) histogram_rebinned->Sumw2();
    
    unsigned numBins = histogram->GetNbinsX();
    unsigned numBins_withinRange = 0;
    for ( unsigned iBin = 1; iBin <= numBins; ++iBin ) {
      double binCenter = histogram->GetBinCenter(iBin);
      if ( binCenter >= xMin && binCenter <= xMax ) ++numBins_withinRange;
    }
    
    assert(histogram_rebinned->GetNbinsX() == (int)numBins);

    std::cout << "histogram = " << histogram->GetName() << ":" 
	      << " numBins(" << xMin << ".." << "xMax) = " << numBins_withinRange << std::endl;

    for ( int combineNumBins = 5; combineNumBins >= 2; --combineNumBins ) {
      if ( numBins_withinRange > (combineNumBins*numBinsMin_rebinned) && (numBins % combineNumBins) == 0 ) {
	histogram_rebinned->Rebin(combineNumBins);
	numBins /= combineNumBins;
	numBins_withinRange /= combineNumBins;
      }
    }

    std::cout << "histogram(rebinned) = " << histogram_rebinned->GetName() << ":" 
	      << " numBins = " << histogram_rebinned->GetNbinsX() << std::endl;
  }

  return histogram_rebinned;
}

void showHistograms(double canvasSizeX, double canvasSizeY,
		    TH1* histogram1, const std::string& legendEntry1,
		    TH1* histogram2, const std::string& legendEntry2,
		    TH1* histogram3, const std::string& legendEntry3,
		    TH1* histogram4, const std::string& legendEntry4,
		    TH1* histogram5, const std::string& legendEntry5,
		    TH1* histogram6, const std::string& legendEntry6,
		    int colors[], int lineStyles[], 
		    double legendTextSize, double legendPosX, double legendPosY, double legendSizeX, double legendSizeY, 
		    std::vector<std::string>& labelTextLines, double labelTextSize,
		    double labelPosX, double labelPosY, double labelSizeX, double labelSizeY,
		    double xMin, double xMax, const std::string& xAxisTitle, double xAxisOffset,
		    bool useLogScale, double yMin, double yMax, const std::string& yAxisTitle, double yAxisOffset,
		    const std::string& outputFileName)
{
  unsigned numBinsMin_rebinned = 20;
  TH1* histogram1_rebinned = rebinHistogram(histogram1, numBinsMin_rebinned, xMin, xMax);
  TH1* histogram2_rebinned = rebinHistogram(histogram2, numBinsMin_rebinned, xMin, xMax);
  TH1* histogram3_rebinned = rebinHistogram(histogram3, numBinsMin_rebinned, xMin, xMax);
  TH1* histogram4_rebinned = rebinHistogram(histogram4, numBinsMin_rebinned, xMin, xMax);
  TH1* histogram5_rebinned = rebinHistogram(histogram5, numBinsMin_rebinned, xMin, xMax);
  TH1* histogram6_rebinned = rebinHistogram(histogram6, numBinsMin_rebinned, xMin, xMax);

  TCanvas* canvas = new TCanvas("canvas", "canvas", canvasSizeX, canvasSizeY);
  canvas->SetFillColor(10);
  canvas->SetBorderSize(2);
  
  canvas->SetLeftMargin(0.14);
  canvas->SetBottomMargin(0.12);

  canvas->SetLogy(useLogScale);
  
  if ( !histogram1 ) {
    std::cerr << "<showHistograms>: histogram1 = NULL --> skipping !!" << std::endl;
    return;
  }

  histogram1_rebinned->SetTitle("");
  histogram1_rebinned->SetStats(false);
  histogram1_rebinned->SetMinimum(yMin);
  histogram1_rebinned->SetMaximum(yMax);

  TAxis* xAxis = histogram1_rebinned->GetXaxis();
  xAxis->SetTitle(xAxisTitle.data());
  xAxis->SetTitleSize(0.045);
  xAxis->SetTitleOffset(xAxisOffset);  
  if ( xMax > xMin ) {
    std::cout << "limiting x-axis range to " << xMin << ".." << xMax << std::endl;
    xAxis->SetRangeUser(xMin, xMax);
  }

  TAxis* yAxis = histogram1_rebinned->GetYaxis();
  yAxis->SetTitle(yAxisTitle.data());
  yAxis->SetTitleSize(0.045);
  yAxis->SetTitleOffset(yAxisOffset);

  histogram1_rebinned->SetLineColor(colors[0]);
  histogram1_rebinned->SetLineWidth(2);
  histogram1_rebinned->SetLineStyle(lineStyles[0]);
  histogram1_rebinned->Draw("hist");

  if ( histogram2_rebinned ) {
    histogram2_rebinned->SetLineColor(colors[1]);
    histogram2_rebinned->SetLineWidth(2);
    histogram2_rebinned->SetLineStyle(lineStyles[1]);
    histogram2_rebinned->Draw("histsame");
  }

  if ( histogram3_rebinned ) {
    histogram3_rebinned->SetLineColor(colors[2]);
    histogram3_rebinned->SetLineWidth(2);
    histogram3_rebinned->SetLineStyle(lineStyles[2]);
    histogram3_rebinned->Draw("histsame");
  }

  if ( histogram4_rebinned ) {
    histogram4_rebinned->SetLineColor(colors[3]);
    histogram4_rebinned->SetLineWidth(2);
    histogram4_rebinned->SetLineStyle(lineStyles[3]);
    histogram4_rebinned->Draw("histsame");
  }

  if ( histogram5_rebinned ) {
    histogram5_rebinned->SetLineColor(colors[4]);
    histogram5_rebinned->SetLineWidth(2);
    histogram5_rebinned->SetLineStyle(lineStyles[4]);
    histogram5_rebinned->Draw("histsame");
  }

  if ( histogram6_rebinned ) {
    histogram6_rebinned->SetLineColor(colors[5]);
    histogram6_rebinned->SetLineWidth(2);
    histogram6_rebinned->SetLineStyle(lineStyles[5]);
    histogram6_rebinned->Draw("histsame");
  }

  TLegend* legend = new TLegend(legendPosX, legendPosY, legendPosX + legendSizeX, legendPosY + legendSizeY, "", "brNDC"); 
  legend->SetBorderSize(0);
  legend->SetFillColor(0);
  legend->SetTextSize(legendTextSize);
  legend->AddEntry(histogram1_rebinned, legendEntry1.data(), "l");
  if ( histogram2_rebinned ) legend->AddEntry(histogram2_rebinned, legendEntry2.data(), "l");
  if ( histogram3_rebinned ) legend->AddEntry(histogram3_rebinned, legendEntry3.data(), "l");
  if ( histogram4_rebinned ) legend->AddEntry(histogram4_rebinned, legendEntry4.data(), "l");
  if ( histogram5_rebinned ) legend->AddEntry(histogram5_rebinned, legendEntry5.data(), "l");
  if ( histogram6_rebinned ) legend->AddEntry(histogram6_rebinned, legendEntry6.data(), "l");
  legend->Draw();

  TPaveText* label = 0;
  if ( labelTextLines.size() > 0 ) {
    label = new TPaveText(labelPosX, labelPosY, labelPosX + labelSizeX, labelPosY + labelSizeY, "brNDC");
    for ( std::vector<std::string>::const_iterator labelTextLine = labelTextLines.begin();
	  labelTextLine != labelTextLines.end(); ++labelTextLine ) {
      label->AddText(labelTextLine->data());
    }
    label->SetFillColor(10);
    label->SetBorderSize(0);
    label->SetTextColor(1);
    label->SetTextAlign(12);
    label->SetTextSize(labelTextSize);
    label->Draw();
  }

  canvas->Update();
  std::string outputFileName_plot = "plots/";
  size_t idx = outputFileName.find_last_of('.');
  outputFileName_plot.append(std::string(outputFileName, 0, idx));
  if ( idx != std::string::npos ) canvas->Print(std::string(outputFileName_plot).append(std::string(outputFileName, idx)).data());
  canvas->Print(std::string(outputFileName_plot).append(".png").data());
  canvas->Print(std::string(outputFileName_plot).append(".pdf").data());
  
  delete label;
  delete legend;
  delete canvas;  

  delete histogram1_rebinned;
  delete histogram2_rebinned;
  delete histogram3_rebinned;
  delete histogram4_rebinned;
  delete histogram5_rebinned;
  delete histogram6_rebinned;
}

void showGraphs(double canvasSizeX, double canvasSizeY,
		TGraph* graph1, const std::string& legendEntry1,
		TGraph* graph2, const std::string& legendEntry2,
		TGraph* graph3, const std::string& legendEntry3,
		TGraph* graph4, const std::string& legendEntry4,
		TGraph* graph5, const std::string& legendEntry5,
		TGraph* graph6, const std::string& legendEntry6,
		int colors[], int markerStyles[], 
		double legendTextSize, double legendPosX, double legendPosY, double legendSizeX, double legendSizeY, 
		std::vector<std::string>& labelTextLines, double labelTextSize,
		double labelPosX, double labelPosY, double labelSizeX, double labelSizeY,
		double xMin, double xMax, const std::string& xAxisTitle, double xAxisOffset,
		bool useLogScale, double yMin, double yMax, const std::string& yAxisTitle, double yAxisOffset,
		const std::string& outputFileName)
{
  TCanvas* canvas = new TCanvas("canvas", "canvas", canvasSizeX, canvasSizeY);
  canvas->SetFillColor(10);
  canvas->SetBorderSize(2);
  
  canvas->SetLeftMargin(0.14);
  canvas->SetBottomMargin(0.12);

  canvas->SetLogy(useLogScale);

  TH1* dummyHistogram = new TH1D("dummyHistogram", "dummyHistogram", 100, xMin, xMax);
  dummyHistogram->SetTitle("");
  dummyHistogram->SetStats(false);
  dummyHistogram->SetMinimum(yMin);
  dummyHistogram->SetMaximum(yMax);

  TAxis* xAxis = dummyHistogram->GetXaxis();
  xAxis->SetTitle(xAxisTitle.data());
  xAxis->SetTitleSize(0.045);
  xAxis->SetTitleOffset(xAxisOffset);

  TAxis* yAxis = dummyHistogram->GetYaxis();
  yAxis->SetTitle(yAxisTitle.data());
  yAxis->SetTitleSize(0.045);
  yAxis->SetTitleOffset(yAxisOffset);

  dummyHistogram->Draw("axis");

  graph1->SetLineColor(colors[0]);
  graph1->SetLineWidth(2);
  graph1->SetMarkerColor(colors[0]);
  graph1->SetMarkerStyle(markerStyles[0]);
  graph1->SetMarkerSize(1);
  graph1->Draw("p");

  if ( graph2 ) {
    graph2->SetLineColor(colors[1]);
    graph2->SetLineWidth(2);
    graph2->SetMarkerColor(colors[1]);
    graph2->SetMarkerStyle(markerStyles[1]);
    graph2->SetMarkerSize(1);
    graph2->Draw("p");
  }
  
  if ( graph3 ) {
    graph3->SetLineColor(colors[2]);
    graph3->SetLineWidth(2);
    graph3->SetMarkerColor(colors[2]);
    graph3->SetMarkerStyle(markerStyles[2]);
    graph3->SetMarkerSize(1);
    graph3->Draw("p");
  }

  if ( graph4 ) {
    graph4->SetLineColor(colors[3]);
    graph4->SetLineWidth(2);
    graph4->SetMarkerColor(colors[3]);
    graph4->SetMarkerStyle(markerStyles[3]);
    graph4->SetMarkerSize(1);
    graph4->Draw("p");
  }

  if ( graph5 ) {
    graph5->SetLineColor(colors[4]);
    graph5->SetLineWidth(2);
    graph5->SetMarkerColor(colors[4]);
    graph5->SetMarkerStyle(markerStyles[4]);
    graph5->SetMarkerSize(1);
    graph5->Draw("p");
  }

  if ( graph6 ) {
    graph6->SetLineColor(colors[5]);
    graph6->SetLineWidth(2);
    graph6->SetMarkerColor(colors[5]);
    graph6->SetMarkerStyle(markerStyles[5]);
    graph6->SetMarkerSize(1);
    graph6->Draw("p");
  }
  
  TLegend* legend = new TLegend(legendPosX, legendPosY, legendPosX + legendSizeX, legendPosY + legendSizeY, "", "brNDC"); 
  legend->SetBorderSize(0);
  legend->SetFillColor(0);
  legend->SetTextSize(legendTextSize);
  legend->AddEntry(graph1, legendEntry1.data(), "p");
  if ( graph2 ) legend->AddEntry(graph2, legendEntry2.data(), "p");
  if ( graph3 ) legend->AddEntry(graph3, legendEntry3.data(), "p");
  if ( graph4 ) legend->AddEntry(graph4, legendEntry4.data(), "p");
  if ( graph5 ) legend->AddEntry(graph5, legendEntry5.data(), "p");
  if ( graph6 ) legend->AddEntry(graph6, legendEntry6.data(), "p");
  legend->Draw();

  TPaveText* label = 0;
  if ( labelTextLines.size() > 0 ) {
    label = new TPaveText(labelPosX, labelPosY, labelPosX + labelSizeX, labelPosY + labelSizeY, "brNDC");
    for ( std::vector<std::string>::const_iterator labelTextLine = labelTextLines.begin();
	  labelTextLine != labelTextLines.end(); ++labelTextLine ) {
      label->AddText(labelTextLine->data());
    }
    label->SetFillColor(10);
    label->SetBorderSize(0);
    label->SetTextColor(1);
    label->SetTextAlign(12);
    label->SetTextSize(labelTextSize);
    label->Draw();
  }

  canvas->Update();
  std::string outputFileName_plot = "plots/";
  size_t idx = outputFileName.find_last_of('.');
  outputFileName_plot.append(std::string(outputFileName, 0, idx));
  if ( idx != std::string::npos ) canvas->Print(std::string(outputFileName_plot).append(std::string(outputFileName, idx)).data());
  canvas->Print(std::string(outputFileName_plot).append(".png").data());
  canvas->Print(std::string(outputFileName_plot).append(".pdf").data());
  
  delete dummyHistogram;
  delete label;
  delete legend;
  delete canvas;  
}

void compMuTauL1Thresholds()
{
  std::string inputFileName_efficiency = "/data1/veelken/tmp/CMSSW_5_3_14_patch2_trg_2014Jan30/src/TauAnalysis/Test/test/analyzeMuTau_efficiency_2014Feb13.root";
  std::string directory_efficiency = "DQMData/muTauTriggerAnalyzer";
  TFile* inputFile_efficiency = new TFile(inputFileName_efficiency.data());

  //std::string inputFileName_rate = "/data1/veelken/tmp/CMSSW_5_3_14_patch2_trg_2014Jan30/src/TauAnalysis/Test/test/analyzeMuTau_rateL1Muon_2014Feb13.root";
  std::string inputFileName_rate = "/data1/veelken/tmp/CMSSW_5_3_14_patch2_trg_2014Jan30/src/TauAnalysis/Test/test/analyzeMuTau_rate_2014Feb17.root";
  std::string directory_rate = "DQMData/muTauTriggerAnalyzer";
  TFile* inputFile_rate = new TFile(inputFileName_rate.data());

  bool correctForResponse = false;
  //bool correctForResponse = true;
  
  std::vector<std::string> l1TauAlgorithms;
  l1TauAlgorithms.push_back("L1Tau");
  l1TauAlgorithms.push_back("L1UpgradeTau");
  l1TauAlgorithms.push_back("L1UpgradeIsoTau");
  l1TauAlgorithms.push_back("max4CaloTowersDR015");

  l1TauAlgorithms.push_back("max4CaloTowersDR015_HLTTauPathPassed");

  std::vector<double> offlineTauPtThresholds;
  offlineTauPtThresholds.push_back(20.);
  offlineTauPtThresholds.push_back(30.);
  offlineTauPtThresholds.push_back(40.);
  
  std::vector<double> l1TauPtThresholds;
  l1TauPtThresholds.push_back(10.);
  l1TauPtThresholds.push_back(15.);
  l1TauPtThresholds.push_back(20.);
  l1TauPtThresholds.push_back(25.);
  l1TauPtThresholds.push_back(30.);
  
  std::map<std::string, std::string> histogramNames_efficiency; // key = l1TauAlgorithm
  histogramNames_efficiency["L1Tau"] = "maxL1TauPtVsHightestPtOfflineTau";
  histogramNames_efficiency["L1UpgradeTau"] = "maxL1UpgradeTauPtVsHightestPtOfflineTau";
  histogramNames_efficiency["L1UpgradeIsoTau"] = "maxL1UpgradeIsoTauPtVsHightestPtOfflineTau";
  histogramNames_efficiency["max4CaloTowersDR015"] = "hltCaloTowerPt4VsOfflineTauPtDR015Seed40";
  //histogramNames_efficiency["max4CaloTowersDR015"] = "maxHLTCaloTowerPt4DR015Seed40";

  histogramNames_efficiency["max4CaloTowersDR015_HLTTauPathPassed"] = histogramNames_efficiency["max4CaloTowersDR015"];

  std::map<std::string, std::string> histogramNames_rate; // key = l1TauAlgorithm
  histogramNames_rate["L1Tau"] = "maxL1TauPt";
  histogramNames_rate["L1UpgradeTau"] = "maxL1UpgradeTauPt";
  histogramNames_rate["L1UpgradeIsoTau"] = "maxL1UpgradeIsoTauPt";
  histogramNames_rate["max4CaloTowersDR015"] = "maxHLTCaloTowerPt4DR015Seed40";

  histogramNames_rate["max4CaloTowersDR015_HLTTauPathPassed"] = "HLTTauPathPassed/maxHLTCaloTowerPt4DR015Seed40";
  
  std::map<std::string, std::map<double, TGraph*> > graphsTurnOnVsL1TauPt_efficiency; // key = l1TauAlgorithm, offlineTauPtThreshold
  std::map<std::string, std::map<double, TGraph*> > graphsTurnOnVsL1TauPt_rate;       // key = l1TauAlgorithm, offlineTauPtThreshold
  
  std::map<std::string, std::map<double, TGraph*> > graphsTurnOnVsOfflineTauPt_efficiency; // key = l1TauAlgorithm, l1TauPtThreshold
  std::map<std::string, std::map<double, TGraph*> > graphsTurnOnVsOfflineTauPt_rate;       // key = l1TauAlgorithm, l1TauPtThreshold

  std::map<std::string, std::map<double, TH1*> > histogramsResponse; // key = l1TauAlgorithm, l1TauPtThreshold

  std::map<std::string, std::map<double, TGraph*> > graphsROCcurve; // key = l1TauAlgorithm, offlineTauPtThreshold

  for ( std::vector<std::string>::const_iterator l1TauAlgorithm = l1TauAlgorithms.begin();
	l1TauAlgorithm != l1TauAlgorithms.end(); ++l1TauAlgorithm ) {
    const std::string& histogramName_efficiency = histogramNames_efficiency[*l1TauAlgorithm];
    TH1* histogram_efficiency1d = loadHistogram1d(inputFile_efficiency, directory_efficiency, histogramName_efficiency);
    assert(histogram_efficiency1d);
    TH2* histogram_efficiency2d = dynamic_cast<TH2*>(histogram_efficiency1d);

    const std::string& histogramName_rate = histogramNames_rate[*l1TauAlgorithm];
    TH1* histogram_rate = loadHistogram1d(inputFile_rate, directory_rate, histogramName_rate);
    assert(histogram_rate);
    
    if ( histogram_efficiency2d ) {
      for ( std::vector<double>::const_iterator offlineTauPtThreshold = offlineTauPtThresholds.begin();
	    offlineTauPtThreshold != offlineTauPtThresholds.end(); ++offlineTauPtThreshold ) {
	std::string histogramName_response = Form("response_%s_offlineTauPtGt%1.0f", l1TauAlgorithm->data(), *offlineTauPtThreshold);
	TH1* histogram_response = compHistogramResponse(histogramName_response, histogram_efficiency2d, *offlineTauPtThreshold);
	histogramsResponse[*l1TauAlgorithm][*offlineTauPtThreshold] = histogram_response;
      }
    }

    for ( std::vector<double>::const_iterator offlineTauPtThreshold = offlineTauPtThresholds.begin();
	  offlineTauPtThreshold != offlineTauPtThresholds.end(); ++offlineTauPtThreshold ) {
      double averageL1TauResponse = 1.0;
      if ( correctForResponse ) {
	TH1* histogram_response = histogramsResponse[*l1TauAlgorithm][*offlineTauPtThreshold];
	assert(histogram_response);
	averageL1TauResponse = histogram_response->GetMean();
	std::cout << "algorithm = " << (*l1TauAlgorithm) << ", offline tau Pt threshold = " << (*offlineTauPtThreshold) << ":" 
		  << " <response> = " << averageL1TauResponse << ", rms/<response> = " << histogram_response->GetRMS()/averageL1TauResponse << std::endl;
      }

      std::string graphNameTurnOnVsL1TauPt_efficiency = Form("graphTurnOnVsL1TauPt_%s_offlineTauPtGt%1.0f_efficiency", l1TauAlgorithm->data(), *offlineTauPtThreshold);
      TGraph* graphTurnOnVsL1TauPt_efficiency = 0;
      if ( histogram_efficiency2d ) {
	graphTurnOnVsL1TauPt_efficiency = compGraphEfficiencyVsL1TauPt(graphNameTurnOnVsL1TauPt_efficiency, histogram_efficiency2d, *offlineTauPtThreshold, averageL1TauResponse);
      } else {
	graphTurnOnVsL1TauPt_efficiency = compGraphRateVsL1TauPt(graphNameTurnOnVsL1TauPt_efficiency, histogram_efficiency1d, averageL1TauResponse);
      }
      graphsTurnOnVsL1TauPt_efficiency[*l1TauAlgorithm][*offlineTauPtThreshold] = graphTurnOnVsL1TauPt_efficiency;

      std::string graphNameTurnOnVsL1TauPt_rate = Form("graphTurnOnVsL1TauPt_%s_offlineTauPtGt%1.0f_rate", l1TauAlgorithm->data(), *offlineTauPtThreshold);
      TGraph* graphTurnOnVsL1TauPt_rate = compGraphRateVsL1TauPt(graphNameTurnOnVsL1TauPt_rate, histogram_rate, averageL1TauResponse);
      graphsTurnOnVsL1TauPt_rate[*l1TauAlgorithm][*offlineTauPtThreshold] = graphTurnOnVsL1TauPt_rate;

      std::string graphNameROCcurve = Form("graphROCcurve_%s_offlineTauPtGt%1.0f_rate", l1TauAlgorithm->data(), *offlineTauPtThreshold);
      TGraph* graphROCcurve = compGraphROCcurve(graphNameROCcurve, graphTurnOnVsL1TauPt_efficiency, graphTurnOnVsL1TauPt_rate);
      graphsROCcurve[*l1TauAlgorithm][*offlineTauPtThreshold] = graphROCcurve;
    }

    if ( histogram_efficiency2d ) {
      for ( std::vector<double>::const_iterator l1TauPtThreshold = l1TauPtThresholds.begin();
	    l1TauPtThreshold != l1TauPtThresholds.end(); ++l1TauPtThreshold ) {
	TH1* histogram_response = histogramsResponse[*l1TauAlgorithm][20.];
	assert(histogram_response);
	double averageL1TauResponse = 1.0;
	if ( correctForResponse ) {
	  averageL1TauResponse = histogram_response->GetMean();
	}
	std::string graphNameTurnOnVsOfflineTauPt_efficiency = Form("graphNameTurnOnVsOfflineTauPt_%s_offlineTauPtGt%1.0f_efficiency", l1TauAlgorithm->data(), *l1TauPtThreshold);
	TGraph* graphTurnOnVsOfflineTauPt_efficiency = compGraphEfficiencyVsOfflineTauPt(graphNameTurnOnVsOfflineTauPt_efficiency, histogram_efficiency2d, (*l1TauPtThreshold)*averageL1TauResponse);
	graphsTurnOnVsOfflineTauPt_efficiency[*l1TauAlgorithm][*l1TauPtThreshold] = graphTurnOnVsOfflineTauPt_efficiency;
      }
    }
  }

  std::vector<std::string> labelTextLines;

  int colors[6] = { 1, 2, 8, 4, 6, 7 };
  int lineStyles[6] = { 1, 1, 1, 1, 1, 1 };
  int markerStyles[6] = { 22, 32, 20, 24, 21, 25 };

  for ( std::vector<std::string>::const_iterator l1TauAlgorithm = l1TauAlgorithms.begin();
	l1TauAlgorithm != l1TauAlgorithms.end(); ++l1TauAlgorithm ) {
    TH1* histogramResponse_offlineTauPtGt20 = histogramsResponse[*l1TauAlgorithm][20.];
    if ( histogramResponse_offlineTauPtGt20 ) histogramResponse_offlineTauPtGt20->Scale(1./histogramResponse_offlineTauPtGt20->Integral());
    TH1* histogramResponse_offlineTauPtGt30 = histogramsResponse[*l1TauAlgorithm][30.];
    if ( histogramResponse_offlineTauPtGt30 ) histogramResponse_offlineTauPtGt30->Scale(1./histogramResponse_offlineTauPtGt30->Integral());
    TH1* histogramResponse_offlineTauPtGt40 = histogramsResponse[*l1TauAlgorithm][40.];
    if ( histogramResponse_offlineTauPtGt40 ) histogramResponse_offlineTauPtGt40->Scale(1./histogramResponse_offlineTauPtGt40->Integral());
    std::string outputFileName = Form("compMuTauL1Thresholds_%s_response.pdf", l1TauAlgorithm->data());
    showHistograms(800, 600,
		   histogramResponse_offlineTauPtGt20, "P_{T}^{off} > 20 GeV",
		   histogramResponse_offlineTauPtGt30, "P_{T}^{off} > 30 GeV",
		   histogramResponse_offlineTauPtGt40, "P_{T}^{off} > 40 GeV",
		   0, "",
		   0, "",
		   0, "",
		   colors, lineStyles,
		   0.045, 0.18, 0.71, 0.31, 0.18,
		   labelTextLines, 0.045, 
		   0.18, 0.64, 0.31, 0.05, 
		   0., 3., "P_{T}^{L1}/P_{T}^{off}", 1.2,
		   true, 1.e-3, 1.e+1, "#Events", 1.2,
		   outputFileName);
  }

  for ( std::vector<double>::const_iterator offlineTauPtThreshold = offlineTauPtThresholds.begin();
	offlineTauPtThreshold != offlineTauPtThresholds.end(); ++offlineTauPtThreshold ) {
    TH1* histogramResponse_L1Tau = histogramsResponse["L1Tau"][*offlineTauPtThreshold];
    if ( histogramResponse_L1Tau ) histogramResponse_L1Tau->Scale(1./histogramResponse_L1Tau->Integral());
    TH1* histogramResponse_L1UpgradeTau = histogramsResponse["L1UpgradeTau"][*offlineTauPtThreshold];
    if ( histogramResponse_L1UpgradeTau ) histogramResponse_L1UpgradeTau->Scale(1./histogramResponse_L1UpgradeTau->Integral());
    TH1* histogramResponse_L1UpgradeIsoTau = histogramsResponse["L1UpgradeIsoTau"][*offlineTauPtThreshold];
    if ( histogramResponse_L1UpgradeIsoTau ) histogramResponse_L1UpgradeIsoTau->Scale(1./histogramResponse_L1UpgradeIsoTau->Integral());
    TH1* histogramResponse_max4CaloTowersDR015 = histogramsResponse["max4CaloTowersDR015"][*offlineTauPtThreshold];
    if ( histogramResponse_max4CaloTowersDR015 ) histogramResponse_max4CaloTowersDR015->Scale(1./histogramResponse_max4CaloTowersDR015->Integral());
    std::string outputFileName = Form("compMuTauL1Thresholds_offlineTauPtGt%1.0f_response.pdf", *offlineTauPtThreshold);
    showHistograms(800, 600,
		   histogramResponse_L1Tau, "L1Tau",
		   histogramResponse_L1UpgradeTau, "L1UpgradeTau",
		   histogramResponse_L1UpgradeIsoTau, "L1UpgradeIsoTau",
		   histogramResponse_max4CaloTowersDR015, "max4CaloTowersDR015",
		   0, "",
		   0, "",
		   colors, lineStyles,
		   0.045, 0.18, 0.71, 0.31, 0.18,
		   labelTextLines, 0.045, 
		   0.18, 0.64, 0.31, 0.05, 
		   0., 3., "P_{T}^{L1}/P_{T}^{off}", 1.2,
		   true, 1.e-3, 1.e+1, "#Events", 1.2,
		   outputFileName);
  }

  for ( std::vector<double>::const_iterator l1TauPtThreshold = l1TauPtThresholds.begin();
	l1TauPtThreshold != l1TauPtThresholds.end(); ++l1TauPtThreshold ) {
    TGraph* graphTurnOnVsOfflineTauPt_L1Tau = graphsTurnOnVsOfflineTauPt_efficiency["L1Tau"][*l1TauPtThreshold];
    TGraph* graphTurnOnVsOfflineTauPt_L1UpgradeTau = graphsTurnOnVsOfflineTauPt_efficiency["L1UpgradeTau"][*l1TauPtThreshold];
    TGraph* graphTurnOnVsOfflineTauPt_L1UpgradeIsoTau = graphsTurnOnVsOfflineTauPt_efficiency["L1UpgradeIsoTau"][*l1TauPtThreshold];
    TGraph* graphTurnOnVsOfflineTauPt_max4CaloTowersDR015 = graphsTurnOnVsOfflineTauPt_efficiency["max4CaloTowersDR015"][*l1TauPtThreshold];
    std::string outputFileName = Form("compMuTauL1Thresholds_l1TauPtDivResponseGt%1.0f_efficiencyVsOfflineTauPt.pdf", *l1TauPtThreshold);
    showGraphs(800, 600,
	       graphTurnOnVsOfflineTauPt_L1Tau, "L1Tau",
	       graphTurnOnVsOfflineTauPt_L1UpgradeTau, "L1UpgradeTau",
	       graphTurnOnVsOfflineTauPt_L1UpgradeIsoTau, "L1UpgradeIsoTau",
	       graphTurnOnVsOfflineTauPt_max4CaloTowersDR015, "max4CaloTowersDR015",
	       0, "",
	       0, "",
	       colors, markerStyles,
	       0.045, 0.43, 0.71, 0.46, 0.18,
	       labelTextLines, 0.045, 
	       0.18, 0.64, 0.31, 0.05, 
	       0., 100., "P_{T}^{off} [GeV]", 1.2,
	       false, 0., 1.4, "Efficiency", 1.2,
	       outputFileName);
  }

  for ( std::vector<std::string>::const_iterator l1TauAlgorithm = l1TauAlgorithms.begin();
	l1TauAlgorithm != l1TauAlgorithms.end(); ++l1TauAlgorithm ) {
    TGraph* graphTurnOnVsOfflineTauPt_l1TauPtDivResponseGt10 = graphsTurnOnVsOfflineTauPt_efficiency[*l1TauAlgorithm][10.];
    TGraph* graphTurnOnVsOfflineTauPt_l1TauPtDivResponseGt15 = graphsTurnOnVsOfflineTauPt_efficiency[*l1TauAlgorithm][15.];
    TGraph* graphTurnOnVsOfflineTauPt_l1TauPtDivResponseGt20 = graphsTurnOnVsOfflineTauPt_efficiency[*l1TauAlgorithm][20.];
    std::string outputFileName = Form("compMuTauL1Thresholds_%s_efficiencyVsOfflineTauPt.pdf", l1TauAlgorithm->data());
    showGraphs(800, 600,
	       graphTurnOnVsOfflineTauPt_l1TauPtDivResponseGt10, "L1 Threshold = 10 GeV",
	       graphTurnOnVsOfflineTauPt_l1TauPtDivResponseGt15, "L1 Threshold = 15 GeV",
	       graphTurnOnVsOfflineTauPt_l1TauPtDivResponseGt20, "L1 Threshold = 20 GeV",
	       0, "",
	       0, "",
	       0, "",
	       colors, markerStyles,
	       0.045, 0.43, 0.71, 0.46, 0.18,
	       labelTextLines, 0.045, 
	       0.18, 0.64, 0.31, 0.05, 
	       0., 100., "P_{T}^{off} [GeV]", 1.2,
	       false, 0., 1.4, "Efficiency", 1.2,
	       outputFileName);
  }

  for ( std::vector<double>::const_iterator offlineTauPtThreshold = offlineTauPtThresholds.begin();
	offlineTauPtThreshold != offlineTauPtThresholds.end(); ++offlineTauPtThreshold ) {
    TGraph* graphTurnOnVsL1TauPt_L1Tau = graphsTurnOnVsL1TauPt_efficiency["L1Tau"][*offlineTauPtThreshold];
    TGraph* graphTurnOnVsL1TauPt_L1UpgradeTau = graphsTurnOnVsL1TauPt_efficiency["L1UpgradeTau"][*offlineTauPtThreshold];
    TGraph* graphTurnOnVsL1TauPt_L1UpgradeIsoTau = graphsTurnOnVsL1TauPt_efficiency["L1UpgradeIsoTau"][*offlineTauPtThreshold];
    TGraph* graphTurnOnVsL1TauPt_max4CaloTowersDR015 = graphsTurnOnVsL1TauPt_efficiency["max4CaloTowersDR015"][*offlineTauPtThreshold];
    std::string outputFileName = Form("compMuTauL1Thresholds_offlineTauPtGt%1.0f_efficiencyVsL1TauPt.pdf", *offlineTauPtThreshold);
    showGraphs(800, 600,
	       graphTurnOnVsL1TauPt_L1Tau, "L1Tau",
	       graphTurnOnVsL1TauPt_L1UpgradeTau, "L1UpgradeTau",
	       graphTurnOnVsL1TauPt_L1UpgradeIsoTau, "L1UpgradeIsoTau",
	       graphTurnOnVsL1TauPt_max4CaloTowersDR015, "max4CaloTowersDR015",
	       0, "",
	       0, "",
	       colors, markerStyles,
	       0.045, 0.43, 0.71, 0.46, 0.18,
	       labelTextLines, 0.045, 
	       0.18, 0.64, 0.31, 0.05, 
	       0., 100., "L1 Threshold [GeV]", 1.2,
	       false, 0., 1.05, "Efficiency", 1.2,
	       outputFileName);
  }

  for ( std::vector<double>::const_iterator offlineTauPtThreshold = offlineTauPtThresholds.begin();
	offlineTauPtThreshold != offlineTauPtThresholds.end(); ++offlineTauPtThreshold ) {
    TGraph* graphTurnOnVsL1TauPt_L1Tau = graphsTurnOnVsL1TauPt_rate["L1Tau"][*offlineTauPtThreshold];
    TGraph* graphTurnOnVsL1TauPt_L1UpgradeTau = graphsTurnOnVsL1TauPt_rate["L1UpgradeTau"][*offlineTauPtThreshold];
    TGraph* graphTurnOnVsL1TauPt_L1UpgradeIsoTau = graphsTurnOnVsL1TauPt_rate["L1UpgradeIsoTau"][*offlineTauPtThreshold];
    TGraph* graphTurnOnVsL1TauPt_max4CaloTowersDR015 = graphsTurnOnVsL1TauPt_rate["max4CaloTowersDR015"][*offlineTauPtThreshold];
    std::string outputFileName = Form("compMuTauL1Thresholds_offlineTauPtGt%1.0f_rateVsL1TauPt.pdf", *offlineTauPtThreshold);
    showGraphs(800, 600,
	       graphTurnOnVsL1TauPt_L1Tau, "L1Tau",
	       graphTurnOnVsL1TauPt_L1UpgradeTau, "L1UpgradeTau",
	       graphTurnOnVsL1TauPt_L1UpgradeIsoTau, "L1UpgradeIsoTau",
	       graphTurnOnVsL1TauPt_max4CaloTowersDR015, "max4CaloTowersDR015",
	       0, "",
	       0, "",
	       colors, markerStyles,
	       0.045, 0.43, 0.71, 0.46, 0.18,
	       labelTextLines, 0.045, 
	       0.18, 0.64, 0.31, 0.05, 
	       0., 100., "L1 Threshold [GeV]", 1.2,
	       true, 1.e-3, 1.5, "Rate", 1.2,
	       outputFileName);
  }
  
  for ( std::vector<double>::const_iterator offlineTauPtThreshold = offlineTauPtThresholds.begin();
	offlineTauPtThreshold != offlineTauPtThresholds.end(); ++offlineTauPtThreshold ) {
    TGraph* graphROCcurve_L1Tau = graphsROCcurve["L1Tau"][*offlineTauPtThreshold];
    TGraph* graphROCcurve_L1UpgradeTau = graphsROCcurve["L1UpgradeTau"][*offlineTauPtThreshold];
    TGraph* graphROCcurve_L1UpgradeIsoTau = graphsROCcurve["L1UpgradeIsoTau"][*offlineTauPtThreshold];
    TGraph* graphROCcurve_max4CaloTowersDR015 = graphsROCcurve["max4CaloTowersDR015"][*offlineTauPtThreshold];
    std::string outputFileName = Form("compMuTauL1Thresholds_offlineTauPtGt%1.0f_triggerEfficiencyVsRate.pdf", *offlineTauPtThreshold);
    showGraphs(800, 600,
	       graphROCcurve_L1Tau, "L1Tau",
	       graphROCcurve_L1UpgradeTau, "L1UpgradeTau",
	       graphROCcurve_L1UpgradeIsoTau, "L1UpgradeIsoTau",
	       graphROCcurve_max4CaloTowersDR015, "max4CaloTowersDR015",
	       0, "",
	       0, "",
	       colors, markerStyles,
	       0.045, 0.15, 0.17, 0.31, 0.18,
	       labelTextLines, 0.045, 
	       0.18, 0.64, 0.31, 0.05, 
	       0., 1.05, "Efficiency", 1.2,
	       false, 0., 1.05, "1 - Rate", 1.2,
	       outputFileName);

    TGraph* graphROCcurve_max4CaloTowersDR015_HLTTauPathPassed = graphsROCcurve["max4CaloTowersDR015_HLTTauPathPassed"][*offlineTauPtThreshold];
    std::string outputFileName_HLTTauPathPassed = Form("compMuTauL1Thresholds_offlineTauPtGt%1.0f_hltRateReduction.pdf", *offlineTauPtThreshold);
    showGraphs(800, 600,
	       graphROCcurve_max4CaloTowersDR015_HLTTauPathPassed, "max4CaloTowersDR015",
	       0, "",
	       0, "",
	       0, "",
	       0, "",
	       0, "",
	       colors, markerStyles,
	       0.045, 0.15, 0.17, 0.31, 0.18,
	       labelTextLines, 0.045, 
	       0.18, 0.64, 0.31, 0.05, 
	       0., 1.05, "Efficiency", 1.2,
	       false, 0., 1.05, "1 - Rate", 1.2,
	       outputFileName_HLTTauPathPassed);
  }

  delete inputFile_efficiency;
  delete inputFile_rate;
}
