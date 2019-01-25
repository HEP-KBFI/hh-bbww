
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
  if ( histogram->GetNbinsX() > 100 ) histogram->Rebin(10);
  return histogram;
}

void showHistograms(double canvasSizeX, double canvasSizeY,
		    TH1* histogram1, const std::string& legendEntry1,
		    TH1* histogram2, const std::string& legendEntry2,
		    TH1* histogram3, const std::string& legendEntry3,
		    TH1* histogram4, const std::string& legendEntry4,
		    TH1* histogram5, const std::string& legendEntry5,
		    TH1* histogram6, const std::string& legendEntry6,
		    int colors[], int markerStyles[], 
		    double legendTextSize, double legendPosX, double legendPosY, double legendSizeX, double legendSizeY, 
		    std::vector<std::string>& labelTextLines, double labelTextSize,
		    double labelPosX, double labelPosY, double labelSizeX, double labelSizeY,
		    const std::string& xAxisTitle, double xAxisOffset,
		    bool useLogScale, double yMin, double yMax, const std::string& yAxisTitle, double yAxisOffset,
		    const std::string& outputFileName)
{
  TCanvas* canvas = new TCanvas("canvas", "canvas", canvasSizeX, canvasSizeY);
  canvas->SetFillColor(10);
  canvas->SetBorderSize(2);
  
  canvas->SetLeftMargin(0.14);
  canvas->SetBottomMargin(0.12);

  canvas->SetLogy(useLogScale);

  histogram1->SetTitle("");
  histogram1->SetStats(false);
  histogram1->SetMinimum(yMin);
  histogram1->SetMaximum(yMax);

  TAxis* xAxis = histogram1->GetXaxis();
  xAxis->SetTitle(xAxisTitle.data());
  xAxis->SetTitleSize(0.045);
  xAxis->SetTitleOffset(xAxisOffset);

  TAxis* yAxis = histogram1->GetYaxis();
  yAxis->SetTitle(yAxisTitle.data());
  yAxis->SetTitleSize(0.045);
  yAxis->SetTitleOffset(yAxisOffset);

  histogram1->SetLineColor(colors[0]);
  histogram1->SetLineWidth(2);
  histogram1->SetMarkerColor(colors[0]);
  histogram1->SetMarkerStyle(markerStyles[0]);
  histogram1->SetMarkerSize(1);
  histogram1->Draw("hist");

  if ( histogram2 ) {
    histogram2->SetLineColor(colors[1]);
    histogram2->SetLineWidth(2);
    histogram2->SetMarkerColor(colors[1]);
    histogram2->SetMarkerStyle(markerStyles[1]);
    histogram2->SetMarkerSize(1);
    histogram2->Draw("histsame");
  }
  
  if ( histogram3 ) {
    histogram3->SetLineColor(colors[2]);
    histogram3->SetLineWidth(2);
    histogram3->SetMarkerColor(colors[2]);
    histogram3->SetMarkerStyle(markerStyles[2]);
    histogram3->SetMarkerSize(1);
    histogram3->Draw("histsame");
  }

  if ( histogram4 ) {
    histogram4->SetLineColor(colors[3]);
    histogram4->SetLineWidth(2);
    histogram4->SetMarkerColor(colors[3]);
    histogram4->SetMarkerStyle(markerStyles[3]);
    histogram4->SetMarkerSize(1);
    histogram4->Draw("histsame");
  }

  if ( histogram5 ) {
    histogram5->SetLineColor(colors[4]);
    histogram5->SetLineWidth(2);
    histogram5->SetMarkerColor(colors[4]);
    histogram5->SetMarkerStyle(markerStyles[4]);
    histogram5->SetMarkerSize(1);
    histogram5->Draw("histsame");
  }

  if ( histogram6 ) {
    histogram6->SetLineColor(colors[5]);
    histogram6->SetLineWidth(2);
    histogram6->SetMarkerColor(colors[5]);
    histogram6->SetMarkerStyle(markerStyles[5]);
    histogram6->SetMarkerSize(1);
    histogram6->Draw("histsame");
  }
  
  TLegend* legend = new TLegend(legendPosX, legendPosY, legendPosX + legendSizeX, legendPosY + legendSizeY, "", "brNDC"); 
  legend->SetBorderSize(0);
  legend->SetFillColor(0);
  legend->SetTextSize(legendTextSize);
  legend->AddEntry(histogram1, legendEntry1.data(), "l");
  if ( histogram2 ) legend->AddEntry(histogram2, legendEntry2.data(), "l");
  if ( histogram3 ) legend->AddEntry(histogram3, legendEntry3.data(), "l");
  if ( histogram4 ) legend->AddEntry(histogram4, legendEntry4.data(), "l");
  if ( histogram5 ) legend->AddEntry(histogram5, legendEntry5.data(), "l");
  if ( histogram6 ) legend->AddEntry(histogram6, legendEntry6.data(), "l");
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
}

void makePlotsForMEM()
{
  gROOT->SetBatch(true);

  TH1::AddDirectory(false);
  
  std::vector<std::string> channels;
  channels.push_back("hh_bb2l");
  //channels.push_back("hh_bb1l");

  std::map<std::string, std::string> inputFilePaths; // key = channel
  inputFilePaths["hh_bb2l"] = "/home/veelken/CMSSW_9_4_6_patch1/src/hhAnalysis/bbww/test/";
  inputFilePaths["hh_bb1l"] = "/home/veelken/CMSSW_9_4_6_patch1/src/hhAnalysis/bbww/test/";

  std::map<std::string, std::string> inputFileNames_signal; // key = channel
  inputFileNames_signal["hh_bb2l"] = "testMEM_hh_bb2l_signal_genMatchOpt3.root";
  inputFileNames_signal["hh_bb1l"] = "";

  std::map<std::string, std::string> inputFileNames_background; // key = channel
  inputFileNames_background["hh_bb2l"] = "testMEM_hh_bb2l_background_genMatchOpt3.root";
  inputFileNames_background["hh_bb1l"] = "";

  std::map<std::string, std::vector<std::string>> plotNames; // key = channel
  plotNames["hh_bb2l"].push_back("memLR");
  plotNames["hh_bb2l"].push_back("memLR_missingBJet");
  plotNames["hh_bb2l"].push_back("badMEM_genLepton_lead_matchType");
  plotNames["hh_bb2l"].push_back("badMEM_genLepton_sublead_matchType");
  plotNames["hh_bb2l"].push_back("badMEM_genJet_Hbb_lead_matchType");
  plotNames["hh_bb2l"].push_back("badMEM_genJet_Hbb_sublead_matchType");
  plotNames["hh_bb2l"].push_back("badMEM_numBJets_loose");
  plotNames["hh_bb2l"].push_back("badMEM_numBJets_medium");
  plotNames["hh_bb2l"].push_back("badMEM_memLR_missingBJet");

  std::map<std::string, std::map<std::string, std::string>> histogramNames_signal; // key = channel, plotName
  histogramNames_signal["hh_bb2l"]["memLR"] = "signal_genMatchOpt3/sel/evt/signal/memLR";
  histogramNames_signal["hh_bb2l"]["memLR_missingBJet"] = "signal_genMatchOpt3/sel/evt/signal/memLR_missingBJet";
  histogramNames_signal["hh_bb2l"]["badMEM_genLepton_lead_matchType"] = "badMEM_genLepton_lead_matchType";
  histogramNames_signal["hh_bb2l"]["badMEM_genLepton_sublead_matchType"] = "badMEM_genLepton_sublead_matchType";
  histogramNames_signal["hh_bb2l"]["badMEM_genJet_Hbb_lead_matchType"] = "badMEM_genJet_Hbb_lead_matchType";
  histogramNames_signal["hh_bb2l"]["badMEM_genJet_Hbb_sublead_matchType"] = "badMEM_genJet_Hbb_sublead_matchType";
  histogramNames_signal["hh_bb2l"]["badMEM_numBJets_loose"] = "badMEM_numBJets_loose";
  histogramNames_signal["hh_bb2l"]["badMEM_numBJets_medium"] = "badMEM_numBJets_medium";
  histogramNames_signal["hh_bb2l"]["badMEM_memLR_missingBJet"] = "badMEM_memLR_missingBJet";

  std::map<std::string, std::map<std::string, std::string>> histogramNames_background; // key = channel, plotName
  histogramNames_background["hh_bb2l"]["memLR"] = "background_genMatchOpt3/sel/evt/background/memLR";
  histogramNames_background["hh_bb2l"]["memLR_missingBJet"] = "background_genMatchOpt3/sel/evt/background/memLR_missingBJet";
  histogramNames_background["hh_bb2l"]["badMEM_genLepton_lead_matchType"] = "badMEM_genLepton_lead_matchType";
  histogramNames_background["hh_bb2l"]["badMEM_genLepton_sublead_matchType"] = "badMEM_genLepton_sublead_matchType";
  histogramNames_background["hh_bb2l"]["badMEM_genJet_Hbb_lead_matchType"] = "badMEM_genJet_Hbb_lead_matchType";
  histogramNames_background["hh_bb2l"]["badMEM_genJet_Hbb_sublead_matchType"] = "badMEM_genJet_Hbb_sublead_matchType";
  histogramNames_background["hh_bb2l"]["badMEM_numBJets_loose"] = "badMEM_numBJets_loose";
  histogramNames_background["hh_bb2l"]["badMEM_numBJets_medium"] = "badMEM_numBJets_medium";
  histogramNames_background["hh_bb2l"]["badMEM_memLR_missingBJet"] = "badMEM_memLR_missingBJet";
  
  std::map<std::string, std::map<std::string, std::string>> xAxisTitles; // key = channel, plotName
  xAxisTitles["hh_bb2l"]["memLR"] = "MEM LR opt3";
  xAxisTitles["hh_bb2l"]["memLR_missingBJet"] = "MEM LR (missing b-jet) opt3";
  xAxisTitles["hh_bb2l"]["badMEM_genLepton_lead_matchType"] = "leading Lepton gen. match";
  xAxisTitles["hh_bb2l"]["badMEM_genLepton_sublead_matchType"] = "subleading Lepton gen. match";
  xAxisTitles["hh_bb2l"]["badMEM_genJet_Hbb_lead_matchType"] = "leading b-jet gen. match";
  xAxisTitles["hh_bb2l"]["badMEM_genJet_Hbb_sublead_matchType"] = "subleading b-jet gen. match";
  xAxisTitles["hh_bb2l"]["badMEM_numBJets_loose"] = "Number of loose b-jets";
  xAxisTitles["hh_bb2l"]["badMEM_numBJets_medium"] = "Number of medium b-jets";
  xAxisTitles["hh_bb2l"]["badMEM_memLR_missingBJet"] = "MEM LR (missing b-jet) opt3";

  for ( std::vector<std::string>::const_iterator channel = channels.begin();
	channel != channels.end(); ++channel ) {
    TFile* inputFile_signal = openFile(inputFilePaths[*channel], inputFileNames_signal[*channel]);

    TFile* inputFile_background = openFile(inputFilePaths[*channel], inputFileNames_background[*channel]);
        
    for ( std::vector<std::string>::const_iterator plotName = plotNames[*channel].begin();
	  plotName != plotNames[*channel].end(); ++plotName ) {
      TH1* histogram_signal = loadHistogram(inputFile_signal, histogramNames_signal[*channel][*plotName]);

      TH1* histogram_background = loadHistogram(inputFile_background, histogramNames_background[*channel][*plotName]);
      
      enum { kStyle_linear, kStyle_log };
      for ( int iStyle = kStyle_linear; iStyle <= kStyle_log; ++iStyle ) {
	bool useLogScale;
	if      ( iStyle == kStyle_linear ) useLogScale = false;
	else if ( iStyle == kStyle_log    ) useLogScale = true;
	else assert(0);
	
	int colors[6] = { 1, 2, 8, 4, 6, 7 };
	int markerStyles[6] = { 22, 32, 20, 24, 21, 25 };
	double legendPosX, legendPosY;
	std::vector<std::string> labelTextLines;
	double yMin, yMax;
	std::string yAxisTitle;
	std::string outputFileName;
	if ( useLogScale ) {
	  legendPosX = 0.57;
	  legendPosY = 0.76;
	  yMin = 1.e-3;
	  yMax = 1.e+3;
	  outputFileName = Form("makePlotsForMEM_%s_%s_log.pdf", channel->data(), plotName->data());
	} else {
	  legendPosX = 0.57;
	  legendPosY = 0.76;
	  yMin = 0.;
	  yMax = 1.2*TMath::Max(histogram_signal->GetMaximum(), histogram_background->GetMaximum());
	  outputFileName = Form("makePlotsForMEM_%s_%s_linear.pdf", channel->data(), plotName->data());
	}
        showHistograms(
          800, 600,
	  histogram_signal, "HH Signal",
	  histogram_background, "t#bar{t} Background ",
	  nullptr, "",
	  nullptr, "",
	  nullptr, "",
	  nullptr, "",
	  colors, markerStyles,
	  0.045, legendPosX, legendPosY, 0.30, 0.11,
	  labelTextLines, 0.045, 
	  0.18, 0.64, 0.31, 0.05, 
	  xAxisTitles[*channel][*plotName], 1.2,
	  useLogScale, yMin, yMax, "Events", 1.2,
	  outputFileName);
      }
    }

    delete inputFile_signal;
    delete inputFile_background;
  }
}
