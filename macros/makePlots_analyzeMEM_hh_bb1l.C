
#include <TAxis.h>
#include <TCanvas.h>
#include <TFile.h>
#include <TGraph.h>
#include <TH1.h>
#include <TH2.h>
#include <TLegend.h>
#include <TMath.h>
#include <TPaveText.h>
#include <TROOT.h>
#include <TString.h>
#include <TSystem.h>

#include <string>
#include <vector>
#include <map>
#include <iostream>
#include <iomanip>
#include <assert.h>
#include <math.h>
#include <limits>

TFile* openFile(const std::string& inputFilePath, const std::string& inputFileName)
{
  std::string inputFileName_full = inputFilePath;
  if ( inputFileName_full.find_last_of("/") != (inputFileName_full.size() - 1) ) inputFileName_full.append("/");
  inputFileName_full.append(inputFileName);
  TFile* inputFile = new TFile(inputFileName_full.data());
  if ( !inputFile ) {
    std::cerr << "Failed to open input file = '" << inputFileName_full << "' !!" << std::endl;
    assert(0);
  }
  return inputFile;
}

TH1* loadHistogram1d(TFile* inputFile, const std::string& histogramName)
{
  TH1* histogram = dynamic_cast<TH1*>(inputFile->Get(histogramName.data()));
  if ( !histogram ) {
    std::cerr << "Failed to load histogram = " << histogramName << " from file = " << inputFile->GetName() << " !!" << std::endl;
    assert(0);
  }
  if ( !histogram->GetSumw2N() ) histogram->Sumw2();
  return histogram;
}

TH2* loadHistogram2d(TFile* inputFile, const std::string& histogramName)
{
  TH1* histogram1d = loadHistogram1d(inputFile, histogramName);
  TH2* histogram2d = dynamic_cast<TH2*>(histogram1d);
  if ( !histogram2d ) {
    std::cerr << "Failed to load histogram = " << histogramName << ", because it is not of type TH2 !!" << std::endl;
    assert(0);
  }
  return histogram2d;
}

TH1* rebinHistogram(const TH1* histogram, unsigned numBinsMin_rebinned, double xMin, double xMax)
{
  TH1* histogram_rebinned = 0;

  if ( histogram ) {
    histogram_rebinned = (TH1*)histogram->Clone(std::string(histogram->GetName()).append("_rebinned").data());
    if ( !histogram_rebinned->GetSumw2N() ) histogram_rebinned->Sumw2();
/*    
    if ( xMin == xMax ) {
      const TAxis* xAxis = histogram->GetXaxis();
      xMin = xAxis->GetXmin();
      xMax = xAxis->GetXmax();
    }

    unsigned numBins = histogram->GetNbinsX();
    unsigned numBins_withinRange = 0;
    for ( unsigned idxBin = 1; idxBin <= numBins; ++idxBin ) {
      double binCenter = histogram->GetBinCenter(idxBin);
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
 */
  }
  
  return histogram_rebinned;
}

double compIntegral1d(TH1* histogram, unsigned idxFirstBin, unsigned idxLastBin)
{
  double integral = 0.;
  for ( unsigned idxBin = idxFirstBin; idxBin <= idxLastBin; ++idxBin ) {
    integral += histogram->GetBinContent(idxBin);
  }
  return integral;
}

void normalizeHistogram1d(TH1* histogram)
{
  if ( histogram ) {
    double integral = compIntegral1d(histogram, 1, histogram->GetNbinsX());
    if ( integral > 0. ) histogram->Scale(1./integral);
  }
}

void showHistograms1d(double canvasSizeX, double canvasSizeY,
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

  normalizeHistogram1d(histogram1_rebinned);
  normalizeHistogram1d(histogram2_rebinned);
  normalizeHistogram1d(histogram3_rebinned);
  normalizeHistogram1d(histogram4_rebinned);
  normalizeHistogram1d(histogram5_rebinned);
  normalizeHistogram1d(histogram6_rebinned);

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

  TLegend* legend = 0;
  if ( legendEntry1 != "" ) {
    legend = new TLegend(legendPosX, legendPosY, legendPosX + legendSizeX, legendPosY + legendSizeY, "", "brNDC"); 
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
  }

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

void showHistograms2d(double canvasSizeX, double canvasSizeY,
                      TH2* histogram,
                      double xMin, double xMax, const std::string& xAxisTitle, double xAxisOffset,
                      double yMin, double yMax, const std::string& yAxisTitle, double yAxisOffset,
                      const std::string& drawOption,
                      const std::string& outputFileName)
{
  TCanvas* canvas = new TCanvas("canvas", "canvas", canvasSizeX, canvasSizeY);
  canvas->SetFillColor(10);
  canvas->SetBorderSize(2);
  
  canvas->SetLeftMargin(0.14);
  canvas->SetBottomMargin(0.12);

  canvas->SetLogy(false);
  
  histogram->SetTitle("");
  histogram->SetStats(false);

  TAxis* xAxis = histogram->GetXaxis();
  xAxis->SetTitle(xAxisTitle.data());
  xAxis->SetTitleSize(0.045);
  xAxis->SetTitleOffset(xAxisOffset);  
  if ( xMax > xMin ) {
    std::cout << "limiting x-axis range to " << xMin << ".." << xMax << std::endl;
    xAxis->SetRangeUser(xMin, xMax);
  }

  TAxis* yAxis = histogram->GetYaxis();
  yAxis->SetTitle(yAxisTitle.data());
  yAxis->SetTitleSize(0.045);
  yAxis->SetTitleOffset(yAxisOffset);
  if ( yMax > yMin ) {
    std::cout << "limiting y-axis range to " << yMin << ".." << yMax << std::endl;
    yAxis->SetRangeUser(yMin, yMax);
  }

  histogram->Draw(drawOption.data());

  canvas->Update();
  std::string outputFileName_plot = "plots/";
  size_t idx = outputFileName.find_last_of('.');
  outputFileName_plot.append(std::string(outputFileName, 0, idx));
  if ( idx != std::string::npos ) canvas->Print(std::string(outputFileName_plot).append(std::string(outputFileName, idx)).data());
  canvas->Print(std::string(outputFileName_plot).append(".png").data());
  canvas->Print(std::string(outputFileName_plot).append(".pdf").data());
  
  delete canvas;  
}
  
TGraph* compGraph_Efficiency(TH1* histogram)
{
  TAxis* xAxis = histogram->GetXaxis();
  int numPoints = xAxis->GetNbins() + 1;
  TGraph* graph_Efficiency = new TGraph(numPoints);
  graph_Efficiency->SetPoint(0, 0., 1.0);
  double integral = histogram->Integral(1, histogram->GetNbinsX());
  double sum = 0.;
  for ( int idxPoint = 0; idxPoint <= numPoints; ++idxPoint ) {
    double binCenter = 0.;
    if ( idxPoint >= 1 ) {      
      int idxBin = idxPoint;
      binCenter = xAxis->GetBinCenter(idxBin);
      double binContent = histogram->GetBinContent(idxBin);
      sum += binContent;
    }
    std::string histogramName = histogram->GetName();
    if ( histogramName.find("nllKinFit") != std::string::npos ) graph_Efficiency->SetPoint(idxPoint, binCenter, sum/integral);
    else graph_Efficiency->SetPoint(idxPoint, binCenter, 1.0 - (sum/integral));
  }
  return graph_Efficiency;
}

TGraph* compGraph_ROCcurve_fromHistogram1d(TH1* histogram_signal, TH1* histogram_background)
{
  TGraph* graph_signal = compGraph_Efficiency(histogram_signal);
  TGraph* graph_background = compGraph_Efficiency(histogram_background);
  int numPoints = graph_signal->GetN();
  assert(graph_background->GetN() == numPoints);
  TGraph* graph_ROCcurve = new TGraph(numPoints);
  for ( int idxPoint = 0; idxPoint < numPoints; ++idxPoint ) {
    double x_signal, y_signal;
    graph_signal->GetPoint(idxPoint, x_signal, y_signal);
    //double y_background = graph_background->Eval(x_signal);
    double x_background, y_background;
    graph_background->GetPoint(idxPoint, x_background, y_background);
    assert(TMath::Abs(x_signal - x_background) < 1.e-4);
    double x_ROCcurve = y_signal;
    //double y_ROCcurve = 1.0 - y_background;
    double y_ROCcurve = y_background;
    graph_ROCcurve->SetPoint(idxPoint, x_ROCcurve, y_ROCcurve);
  }
  return graph_ROCcurve;
}

double compIntegral2d(TH2* histogram, int idxFirstBinX, int idxLastBinX, int idxFirstBinY, int idxLastBinY)
{
  double integral = 0;
  for ( int idxBinX = idxFirstBinX; idxBinX <= idxLastBinX; ++idxBinX ) {
    for ( int idxBinY = idxFirstBinY; idxBinY <= idxLastBinY; ++idxBinY ) {
      integral += histogram->GetBinContent(idxBinX, idxBinY);
    }
  }
  return integral;
}

TGraph* compGraph_ROCcurve_fromHistogram2d(TH2* histogram_signal, TH2* histogram_background)
{
  std::cout << "<compGraph_ROCcurve_fromHistogram2d>: processing histogram = '" << histogram_signal->GetName() << "'" << std::endl;
 
  struct cutEntryType
  {
    double xCut_;
    double yCut_;
    double probS_;
    double probB_;
  };
  std::map<int, cutEntryType> cuts;
  for ( int idx = 0; idx <= 100; ++idx ) {
    cutEntryType cut;
    cut.xCut_  = -1.;
    cut.yCut_  = -1.;
    cut.probS_ = -1.;
    cut.probB_ = -1.;
    cuts[idx] = cut;
  }

  TAxis* xAxis = histogram_signal->GetXaxis();
  int numBinsX = xAxis->GetNbins();
  TAxis* yAxis = histogram_signal->GetYaxis();
  int numBinsY = yAxis->GetNbins();
  double integralS = compIntegral2d(histogram_signal, 1, numBinsX, 1, numBinsY);
  double integralB = compIntegral2d(histogram_background, 1, numBinsX, 1, numBinsY);
  //std::cout << "integral: S = " << integralS << ", B = " << integralB << std::endl;
  for ( int idxBinX = 1; idxBinX <= numBinsX; ++idxBinX ) {
    for ( int idxBinY = 1; idxBinY <= numBinsY; ++idxBinY ) {
      double probS, probB;
      std::string histogramName = histogram_signal->GetName();
      if ( histogramName.find("nllKinFit") != std::string::npos ) {
	probS = compIntegral2d(histogram_signal, idxBinX, numBinsX, 1, idxBinY)/integralS;
	probB = compIntegral2d(histogram_background, idxBinX, numBinsX, 1, idxBinY)/integralB;
      } else {
	probS = compIntegral2d(histogram_signal, idxBinX, numBinsX, idxBinY, numBinsY)/integralS;
	probB = compIntegral2d(histogram_background, idxBinX, numBinsX, idxBinY, numBinsY)/integralB;
      }
      //std::cout << "prob: S = " << probS << ", B = " << probB << std::endl;
      int idx = TMath::Nint(100.*probS);
      //std::cout << "idx = " << idx << std::endl;
      if ( idx >= 0 && idx <= 100 ) {
	cutEntryType& cut = cuts[idx];
	if ( cut.probB_ == -1. || cut.probB_ > probB ) {
	  cut.xCut_  = xAxis->GetBinCenter(idxBinX);
	  cut.yCut_  = yAxis->GetBinCenter(idxBinY);
	  cut.probS_ = probS;
	  cut.probB_ = probB;
	}
      }
    }
  }

  std::vector<double> xPoints;
  std::vector<double> yPoints;
  for ( int idx = 0; idx <= 100; ++idx ) {
    cutEntryType& cut = cuts[idx];
    if ( cut.probS_ == -1. || cut.probB_ == -1. ) continue;
    double x = cut.probS_;
    double y = cut.probB_;
    //std::cout << "cut: x = " << cut.xCut_ << ", y = " << cut.yCut_ << " --> prob: S = " << cut.probS_ << ", B = " << cut.probB_ << std::endl;
    xPoints.push_back(x);
    yPoints.push_back(y);
  }  
  assert(xPoints.size() == yPoints.size());
  int numPoints = xPoints.size();
  assert(numPoints > 0);
  TGraph* graph = new TGraph(numPoints);
  for ( int idxPoint = 0; idxPoint < numPoints; ++idxPoint ) {
    graph->SetPoint(idxPoint, xPoints[idxPoint], yPoints[idxPoint]);
  }

  return graph;
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

  TGraph* graph_line = 0;
  if ( !useLogScale ) {
    graph_line = new TGraph(2);
    graph_line->SetPoint(0, 1., 1.);
    graph_line->SetPoint(1, 0., 0.);
    graph_line->SetLineColor(8);
    graph_line->SetLineWidth(1);
    graph_line->Draw("L");
  }

  graph1->SetLineColor(colors[0]);
  graph1->SetLineWidth(2);
  graph1->SetMarkerColor(colors[0]);
  graph1->SetMarkerStyle(markerStyles[0]);
  graph1->SetMarkerSize(1);
  graph1->Draw("pL");

  if ( graph2 ) {
    graph2->SetLineColor(colors[1]);
    graph2->SetLineWidth(2);
    graph2->SetMarkerColor(colors[1]);
    graph2->SetMarkerStyle(markerStyles[1]);
    graph2->SetMarkerSize(1);
    graph2->Draw("pL");
  }
  
  if ( graph3 ) {
    graph3->SetLineColor(colors[2]);
    graph3->SetLineWidth(2);
    graph3->SetMarkerColor(colors[2]);
    graph3->SetMarkerStyle(markerStyles[2]);
    graph3->SetMarkerSize(1);
    graph3->Draw("pL");
  }

  if ( graph4 ) {
    graph4->SetLineColor(colors[3]);
    graph4->SetLineWidth(2);
    graph4->SetMarkerColor(colors[3]);
    graph4->SetMarkerStyle(markerStyles[3]);
    graph4->SetMarkerSize(1);
    graph4->Draw("pL");
  }

  if ( graph5 ) {
    graph5->SetLineColor(colors[4]);
    graph5->SetLineWidth(2);
    graph5->SetMarkerColor(colors[4]);
    graph5->SetMarkerStyle(markerStyles[4]);
    graph5->SetMarkerSize(1);
    graph5->Draw("pL");
  }

  if ( graph6 ) {
    graph6->SetLineColor(colors[5]);
    graph6->SetLineWidth(2);
    graph6->SetMarkerColor(colors[5]);
    graph6->SetMarkerStyle(markerStyles[5]);
    graph6->SetMarkerSize(1);
    graph6->Draw("pL");
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

void makePlots_analyzeMEM_hh_bb1l()
{
//--- stop ROOT from keeping references to all histograms
  TH1::AddDirectory(false);

//--- suppress the output canvas 
  gROOT->SetBatch(true);

  std::string inputFilePath = "/home/veelken/CMSSW_10_2_10_centOS/CMSSW_10_2_10/src/hhAnalysis/bbww/test/templates";
  std::string inputFileName_signal = "analyzeMEM_hh_bb1l_signal_absEtaLt2p4.root";
  TFile* inputFile_signal = openFile(inputFilePath, inputFileName_signal);
  std::string inputFileName_background = "analyzeMEM_hh_bb1l_background_absEtaLt2p4.root";
  TFile* inputFile_background = openFile(inputFilePath, inputFileName_background);

  std::vector<std::string> labelTextLines;

  int colors[6] = { 1, 2, 8, 4, 6, 7 };
  int lineStyles[6] = { 1, 1, 1, 1, 1, 1 };
  int markerStyles[6] = { 22, 32, 20, 24, 21, 25 };

  std::vector<std::string> histograms1d;
genLepton_pt
genLepton_absEta
", "genLepton_pt", 70, 0., 350.);
  TH1* histogram_genLepton_absEta = fs.make<TH1D>("genLepton_absEta
  histograms1d.push_back("genWJet1_pt");
  histograms1d.push_back("genWJet1_absEta");
  histograms1d.push_back("genWJet2_pt");
  histograms1d.push_back("genWJet2_absEta");
  histograms1d.push_back("dR_genWJets");
  histograms1d.push_back("dRmin_genWJets_to_genLepton");
  histograms1d.push_back("dRmax_genWJets_to_genLepton");
  histograms1d.push_back("genBJet1_pt");
  histograms1d.push_back("genBJet1_absEta");
  histograms1d.push_back("genBJet2_pt");
  histograms1d.push_back("genBJet2_absEta");
  //histograms1d.push_back("dR_genBJets");
  
  std::map<std::string, std::string> xAxisTitles1d; // key = histograms1d
  xAxisTitles1d["genWJet1_pt"]                 = "p_{T} [GeV]";
  xAxisTitles1d["genWJet1_absEta"]             = "#eta";
  xAxisTitles1d["genWJet2_pt"]                 = "p_{T} [GeV]";
  xAxisTitles1d["genWJet2_absEta"]             = "#eta";
  xAxisTitles1d["dR_genWJets"]                 = "#Delta R";
  xAxisTitles1d["dRmin_genWJets_to_genLepton"] = "min #Delta R";
  xAxisTitles1d["dRmax_genWJets_to_genLepton"] = "max #Delta R";
  xAxisTitles1d["genBJet1_pt"]                 = "p_{T} [GeV]";
  xAxisTitles1d["genBJet1_absEta"]             = "#eta";
  xAxisTitles1d["genBJet2_pt"]                 = "p_{T} [GeV]";
  xAxisTitles1d["genBJet2_absEta"]             = "#eta";
  xAxisTitles1d["dR_genBJets"]                 = "#Delta R";
  
  for ( std::vector<std::string>::const_iterator histogramName = histograms1d.begin();
	histogramName != histograms1d.end(); ++histogramName ) {
    TH1* histogram_signal = loadHistogram1d(inputFile_signal, *histogramName);
    TH1* histogram_background = loadHistogram1d(inputFile_background, *histogramName);

    std::string outputFileName = Form("makePlots_analyzeMEM_hh_bb1l_%s.png", histogramName->data());
    showHistograms1d(1150, 800,
	             histogram_signal,     "HH->bbWW",
  	             histogram_background, "t#bar{t}",
  		     0, "",
		     0, "",
		     0, "",
		     0, "",
		     colors, lineStyles, 
		     0.050, 0.63, 0.72, 0.26, 0.17, 
		     labelTextLines, 0.050,
		     0.63, 0.65, 0.26, 0.07, 
		     -1., -1., xAxisTitles1d[*histogramName], 1.2, 
		     true, 1.e-4, 1.e0, "Events", 1.2, 
		     outputFileName);
  }
	
  std::vector<std::string> histograms2d;
  histograms2d.push_back("selJetCorrelation");
  histograms2d.push_back("dRmax_vs_dRmin_genWJets_to_genLepton");

  std::map<std::string, std::string> xAxisTitles2d; // key = histograms2d
  xAxisTitles2d["selJetCorrelation"]                    = "H->bb";
  xAxisTitles2d["dRmax_vs_dRmin_genWJets_to_genLepton"] = "min #Delta R";
  
  std::map<std::string, std::string> yAxisTitles2d; // key = histograms2d
  yAxisTitles2d["selJetCorrelation"]                    = "W->jj";
  yAxisTitles2d["dRmax_vs_dRmin_genWJets_to_genLepton"] = "max #Delta R";

  std::map<std::string, std::string> drawOptions; // key = histograms2d
  drawOptions["selJetCorrelation"]                    = "TEXT";
  drawOptions["dRmax_vs_dRmin_genWJets_to_genLepton"] = "BOX";

  for ( std::vector<std::string>::const_iterator histogramName = histograms2d.begin();
	histogramName != histograms2d.end(); ++histogramName ) {
    TH2* histogram_signal = loadHistogram2d(inputFile_signal, *histogramName);
    TH2* histogram_background = loadHistogram2d(inputFile_background, *histogramName);

    std::string outputFileName_signal = Form("makePlots_analyzeMEM_hh_bb1l_%s_signal.png", histogramName->data());
    showHistograms2d(900, 900,
	             histogram_signal,
		     -1., -1., xAxisTitles2d[*histogramName], 1.2, 
		     -1., -1., yAxisTitles2d[*histogramName], 1.2, 
                     drawOptions[*histogramName],
		     outputFileName_signal);

    std::string outputFileName_background = Form("makePlots_analyzeMEM_hh_bb1l_%s_background.png", histogramName->data());
    showHistograms2d(900, 900,
	             histogram_background,
		     -1., -1., xAxisTitles2d[*histogramName], 1.2, 
		     -1., -1., yAxisTitles2d[*histogramName], 1.2, 
                     drawOptions[*histogramName],
		     outputFileName_background);
  }

  delete inputFile_signal;
  delete inputFile_background;
}

