 
#include "TFile.h"
#include "TDirectory.h"
#include "TH1.h"
#include "TGraph.h"
#include "TCanvas.h"
#include "TLegend.h"
#include "TPaveText.h"
#include "TMath.h"
#include "TString.h"
#include <TROOT.h>
#include <TStyle.h>

#include <string>
#include <vector>
#include <iostream>
#include <iomanip>
#include <assert.h>

TFile* openFile(const std::string& inputFilePath, const std::string& inputFileName)
{
  TString inputFileName_full = inputFilePath.data();
  if ( !inputFileName_full.EndsWith("/") ) inputFileName_full.Append("/");
  inputFileName_full.Append(inputFileName.data());
  TFile* inputFile = new TFile(inputFileName_full.Data());
  if ( !inputFile ) {
    std::cerr << "Failed to open input file = " << inputFileName_full.Data() << " !!" << std::endl;
    assert(0);
  }
  return inputFile;
}
  
TH1* loadHistogram(TFile* inputFile, const std::string& histogramName)
{  
  TH1* histogram = (TH1*)inputFile->Get(histogramName.data());
  if ( !histogram ) {
    std::cerr << "Failed to load histogram = " << histogramName << " from file = " << inputFile->GetName() << " !!" << std::endl;
    assert(0);
  }
  if ( !histogram->GetSumw2N() ) histogram->Sumw2();
  return histogram;
}

enum { kUndefined, kLeftToRight, kRightToLeft };

TGraph* compGraphEfficiency(const std::string& graphName, const TH1* histogram, int mode)
{
  const TAxis* xAxis = histogram->GetXaxis();
  int numPoints = xAxis->GetNbins();
  TGraph* graphEfficiency = new TGraph(numPoints + 2);
  graphEfficiency->SetName(graphName.data());
  graphEfficiency->SetPoint(0, xAxis->GetXmin(), 1.0);
  double integral = histogram->Integral(1, histogram->GetNbinsX());
  double sum = 0.;
  for ( int idxPoint = 1; idxPoint <= numPoints; ++idxPoint ) {
    int idxBin = -1;
    if ( mode == kLeftToRight ) {
      idxBin = idxPoint;
    } else if ( mode == kRightToLeft ) {
      idxBin = histogram->GetNbinsX() - (idxPoint - 1);
    } else assert(0);
    double binCenter = xAxis->GetBinCenter(idxBin);
    double binContent = histogram->GetBinContent(idxBin);
    sum += binContent;
    graphEfficiency->SetPoint(idxPoint, binCenter, 1.0 - (sum/integral));
  }
  graphEfficiency->SetPoint(numPoints + 1, xAxis->GetXmax(), 0.0);
  return graphEfficiency;
} 

TGraph* compGraphROC(const std::string& graphName, const TGraph* graphEfficiency_signal, const TGraph* graphEfficiency_background, bool useLogScale)
{
  //std::cout << "<compGraphROC>:" << std::endl;
  //std::cout << " graphName = " << graphName << std::endl;
  assert(graphEfficiency_signal->GetN() == graphEfficiency_background->GetN());
  int numPoints = graphEfficiency_signal->GetN();
  TGraph* graphROC = new TGraph(numPoints);
  graphROC->SetName(graphName.data());
  for ( int idxPoint = 0; idxPoint < numPoints; ++idxPoint ) {
    double x, efficiency_signal;
    graphEfficiency_signal->GetPoint(idxPoint, x, efficiency_signal);
    double efficiency_background = graphEfficiency_background->Eval(x);
    double xROC = efficiency_signal;
    double yROC;
    if ( useLogScale ) yROC = efficiency_background;
    else yROC = 1.0 - efficiency_background;
    //std::cout << "point #" << idxPoint << ": x = " << xROC << ", y = " << yROC << std::endl;
    graphROC->SetPoint(idxPoint, xROC, yROC);
  }
  return graphROC;
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

void makeROCforMEM()
{
  gROOT->SetBatch(true);

  TH1::AddDirectory(false);
  
  std::vector<std::string> channels;
  //channels.push_back("hh_bb2l");
  channels.push_back("hh_bb1l");

  std::map<std::string, std::vector<std::string>> categories; // key = channel
  //categories["hh_bb2l"].push_back(""); // fully reconstructed case
  //categories["hh_bb2l"].push_back("missingBJet");
  categories["hh_bb1l"].push_back(""); // fully reconstructed case
  categories["hh_bb1l"].push_back("missingBJet");
  categories["hh_bb1l"].push_back("missingHadWJet");

  std::map<std::string, std::string> inputFilePaths; // key = channel
  //inputFilePaths["hh_bb2l"] = "";
  inputFilePaths["hh_bb1l"] = "/home/veelken/CMSSW_10_2_10_centOS/CMSSW_10_2_10/src/hhAnalysis/bbww/test/templates/";

  std::map<std::string, std::string> inputFileNames_signal; // key = channel
  inputFileNames_signal["hh_bb2l"] = "";
  inputFileNames_signal["hh_bb1l"] = "analyzeMEM_hh_bb1l_signal.root";

  std::map<std::string, std::string> inputFileNames_background; // key = channel
  inputFileNames_background["hh_bb2l"] = "";
  inputFileNames_background["hh_bb1l"] = "analyzeMEM_hh_bb1l_background.root";

  std::map<std::string, std::vector<std::string>> plotNames; // key = channel
  //plotNames["hh_bb2l"].push_back("");
  //plotNames["hh_bb2l"].push_back("");
  //plotNames["hh_bb2l"].push_back("");
  plotNames["hh_bb1l"].push_back("LR");
  plotNames["hh_bb1l"].push_back("weightS");
  plotNames["hh_bb1l"].push_back("weightB");

  std::map<std::string, std::map<std::string, std::map<std::string, std::string>>> histogramNames_signal; // key = channel, category, plotName
  //histogramNames_signal["hh_bb2l"][""][""]                      = "";
  //histogramNames_signal["hh_bb2l"][""][""]                      = "";
  //histogramNames_signal["hh_bb2l"][""][""]                      = "";
  histogramNames_signal["hh_bb1l"][""]["LR"]                    = "mem_LR_fullyMatched";
  histogramNames_signal["hh_bb1l"][""]["weightS"]               = "mem_weightS_fullyMatched";
  histogramNames_signal["hh_bb1l"][""]["weightB"]               = "mem_weightB_fullyMatched";
  histogramNames_signal["hh_bb1l"]["missingBJet"]["LR"]         = "mem_missingBJet_LR_fullyMatched";
  histogramNames_signal["hh_bb1l"]["missingBJet"]["weightS"]    = "mem_missingBJet_weightS_fullyMatched";
  histogramNames_signal["hh_bb1l"]["missingBJet"]["weightB"]    = "mem_missingBJet_weightB_fullyMatched";
  histogramNames_signal["hh_bb1l"]["missingHadWJet"]["LR"]      = "mem_missingHadWJet_LR_fullyMatched";
  histogramNames_signal["hh_bb1l"]["missingHadWJet"]["weightS"] = "mem_missingHadWJet_weightS_fullyMatched";
  histogramNames_signal["hh_bb1l"]["missingHadWJet"]["weightB"] = "mem_missingHadWJet_weightB_fullyMatched";
  
  std::map<std::string, std::map<std::string, std::map<std::string, std::string>>> histogramNames_background; // key = channel, category, plotName
  histogramNames_background = histogramNames_signal;

  std::map<std::string, std::map<std::string, int>> mode; // key = channel, plotName
  //mode["hh_bb2l"][""]        = kUndefined;
  //mode["hh_bb2l"][""]        = kUndefined;
  //mode["hh_bb2l"][""]        = kUndefined;
  mode["hh_bb1l"]["LR"]      = kRightToLeft;
  mode["hh_bb1l"]["weightS"] = kLeftToRight;
  mode["hh_bb1l"]["weightB"] = kRightToLeft;

  std::map<std::string, std::map<std::string, std::string>> legendEntries; // key = channel, plotName
  //legendEntries["hh_bb2l"][""]        = "";
  //legendEntries["hh_bb2l"][""]        = "";
  //legendEntries["hh_bb2l"][""]        = "";
  legendEntries["hh_bb1l"]["LR"]      = "w_{S}/(w_{S} + w_{B})";
  legendEntries["hh_bb1l"]["weightS"] = "w_{S}";
  legendEntries["hh_bb1l"]["weightB"] = "w_{B}";

  for ( std::vector<std::string>::const_iterator channel = channels.begin();
	channel != channels.end(); ++channel ) {
    TFile* inputFile_signal = openFile(inputFilePaths[*channel], inputFileNames_signal[*channel]);
    TFile* inputFile_background = nullptr;
    if ( inputFileNames_background[*channel] != inputFileNames_signal[*channel] ) {
      inputFile_background = openFile(inputFilePaths[*channel], inputFileNames_background[*channel]);
    } else {
      inputFile_background = inputFile_signal; 
    }

    for ( std::vector<std::string>::const_iterator category = categories[*channel].begin();
	  category != categories[*channel].end(); ++category ) {

      enum { kStyle_linear, kStyle_log };
      for ( int iStyle = kStyle_linear; iStyle <= kStyle_log; ++iStyle ) {
        bool useLogScale;
        if      ( iStyle == kStyle_linear ) useLogScale = false;
        else if ( iStyle == kStyle_log    ) useLogScale = true;
        else assert(0);
      
        std::map<std::string, TGraph*> graphs_roc; // key = plotName
        for ( std::vector<std::string>::const_iterator plotName = plotNames[*channel].begin();
	      plotName != plotNames[*channel].end(); ++plotName ) {
  	  TH1* histogram_signal = loadHistogram(inputFile_signal, histogramNames_signal[*channel][*category][*plotName]);
          std::string graphName_signal = Form("graph_%s_%s_signal_%s", channel->data(), category->data(), plotName->data());
 	  TGraph* graph_signal = compGraphEfficiency(graphName_signal.data(), histogram_signal, mode[*channel][*plotName]);
	  TH1* histogram_background = loadHistogram(inputFile_background, histogramNames_background[*channel][*category][*plotName]);
          std::string graphName_background = Form("graph_%s_%s_background_%s", channel->data(), category->data(), plotName->data());
	  TGraph* graph_background = compGraphEfficiency(graphName_background.data(), histogram_background, mode[*channel][*plotName]);
          std::string graphName_roc = Form("graphROC_%s_%s_%s", channel->data(), category->data(), plotName->data());
	  graphs_roc[*plotName] = compGraphROC(graphName_roc.data(), graph_signal, graph_background, useLogScale);
  	  delete graph_signal;
	  delete graph_background;
        }
      
        int colors[6] = { 1, 2, 8, 4, 6, 7 };
        int markerStyles[6] = { 22, 32, 20, 24, 21, 25 };
        double legendPosX, legendPosY;
        std::vector<std::string> labelTextLines;
        double yMin, yMax;
        std::string yAxisTitle;
        std::string outputFileName;
        if ( useLogScale ) {
  	  legendPosX = 0.16;
	  legendPosY = 0.64;
  	  yMin = 4.e-4;
	  yMax = 1.5e0;
	  yAxisTitle = "Background Rate";
	  outputFileName = Form("makeROCforMEM_%s_%s_log.pdf", channel->data(), category->data());
        } else {
  	  legendPosX = 0.16;
	  legendPosY = 0.17;
	  yMin = 0.;
 	  yMax = 1.01;
	  yAxisTitle = "Background Suppression";
	  outputFileName = Form("makeROCforMEM_%s_%s_linear.pdf", channel->data(), category->data());
        }
        TGraph* graph1_roc = nullptr;
        std::string legendEntry1;
        TGraph* graph2_roc = nullptr;
        std::string legendEntry2;
        TGraph* graph3_roc = nullptr;
        std::string legendEntry3;
        TGraph* graph4_roc = nullptr;
        std::string legendEntry4;
        TGraph* graph5_roc = nullptr;
        std::string legendEntry5;
        TGraph* graph6_roc = nullptr;
        std::string legendEntry6;
        double legendSizeX = 0.23;
	double legendSizeY = 0.23;
        if ( (*channel) == "hh_bb2l" ) {

        } else if ( (*channel) == "hh_bb1l" ) {
          graph1_roc = graphs_roc["LR"];
	  legendEntry1 = legendEntries[*channel]["LR"];
          graph2_roc = graphs_roc["weightS"];
	  legendEntry2 = legendEntries[*channel]["weightS"];
          graph3_roc = graphs_roc["weightB"];
	  legendEntry3 = legendEntries[*channel]["weightB"];
        } else assert(0);
        showGraphs(
          800, 600,
	  graph1_roc, legendEntry1,
	  graph2_roc, legendEntry2,
  	  graph3_roc, legendEntry3,
	  graph4_roc, legendEntry4,
	  graph5_roc, legendEntry5,
	  graph6_roc, legendEntry6,
	  colors, markerStyles,
	  0.045, legendPosX, legendPosY, legendSizeX, legendSizeY,
	  labelTextLines, 0.045, 
	  0.18, 0.64, 0.31, 0.05, 
	  0., 1.01, "Signal Efficiency", 1.2,
	  useLogScale, yMin, yMax, yAxisTitle, 1.2,
	  outputFileName);
    
        for ( std::map<std::string, TGraph*>::iterator it = graphs_roc.begin();
	      it != graphs_roc.end(); ++it ) {
	  delete it->second;
        }
      }
    }

    delete inputFile_signal;
    if ( inputFile_background != inputFile_signal ) delete inputFile_background;
  }
}
