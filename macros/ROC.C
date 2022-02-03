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

typedef std::vector<std::string> vstring;

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
  TLegend* legend = new TLegend(legendPosX, legendPosY, legendPosX + legendSizeX, legendPosY + legendSizeY, "", "brNDC"); 
  legend->SetBorderSize(0);
  legend->SetFillColor(0);
  legend->SetTextSize(legendTextSize);
  legend->AddEntry(graph1, legendEntry1.data(), "p");
  if ( graph2 ) legend->AddEntry(graph2, legendEntry2.data(), "p");
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
TH1* loadHistogram(TFile* inputFile, const std::string& histogramName)
{
  TH1* histogram = dynamic_cast<TH1*>(inputFile->Get(Form("HH_1l_0tau/%s", histogramName.data())));
  //TH1* histogram = dynamic_cast<TH1*>(inputFile->Get(Form("%s", histogramName.data())));
  if ( !histogram ) {
    std::cout << "Failed to load histogram = " << histogramName << " from file = " << inputFile->GetName() << " !!" << std::endl;
    //assert(0);
  }
  if ( histogram && !histogram->GetSumw2N() ) histogram->Sumw2();
  return histogram;
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
    //double x_ROCcurve = y_signal;
    //double y_ROCcurve = 1.0 - y_background;
    //double y_ROCcurve = y_background;
    double x_ROCcurve = y_background;
    double y_ROCcurve = y_signal;
    graph_ROCcurve->SetPoint(idxPoint, x_ROCcurve, y_ROCcurve);
  }
  graph_ROCcurve->SetPoint(numPoints+1, 1, 0);
  return graph_ROCcurve;
}

//void makeHadTopTaggerPlots(std::string cat, int bins)
void makeHadTopTaggerPlots(std::string era, std::string cat, std::string bins)
{
  //--- stop ROOT from keeping references to all histograms
  TH1::AddDirectory(false);
  
  //--- suppress the output canvas 
  gROOT->SetBatch(true);
  
  //std::string inputFilePath = "/home/snandan/hhAnalysis/2016/final_bb1l_LBN_sigweight1_23June/datacards/hh_bb1l/addSystFakeRates/";
  //std::string inputFilePath = Form("/home/snandan//cmssw10/CMSSW_10_2_13/src/CombineHarvester/ttH_htt/datacard_wconept/%s/res/spin2/datacards_rebined/", era.data());
  std::string inputFilePath = Form("/home/snandan//cmssw10/CMSSW_10_2_13/src/CombineHarvester/ttH_htt/datacard_SM/%s/nonresNLO/datacards_rebined/", era.data());
  std::string inputFileName = Form("datacard_hh_bb1l_LBN_%s_MVAOutput_SM_%sbins_quantiles_nonresNLO_%s.root", cat.data(), bins.data(), era.data());
  //std::string inputFilePath = "/home/snandan/hh_Analysis/CMSSW_11_1_2/src/hhAnalysis/bbww/florian";
  //std::string inputFileName = Form("HH_900_%s_%s.root", cat.data(), era.data());
  //std::string inputFileName = Form("datacard_hh_bb1l_LBN_%s_MVAOutput_450_spin2_%sbins_quantiles_res_%s.root", cat.data(), bins.data(), era.data());
  std::string inputFileName_full = inputFilePath;
  if ( inputFileName_full.find_last_of("/") != (inputFileName_full.size() - 1) ) inputFileName_full.append("/");
  inputFileName_full.append(inputFileName);
  TFile* inputFile = new TFile(inputFileName_full.data());
  if ( !inputFile ) {
    std::cerr << "Failed to open input file = '" << inputFileName_full << "' !!" << std::endl;
    assert(0);
  }
  std::vector<std::string> signals;
  signals.push_back("ggHH_kl_1_kt_1_hbbhww");
  signals.push_back("ggHH_kl_5_kt_1_hbbhww");
  signals.push_back("ggHH_kl_2p45_kt_1_hbbhww");
  signals.push_back("ggHH_kl_0_kt_1_hbbhww");
  signals.push_back("qqHH_CV_1_C2V_1_kl_2_hbbhww");
  signals.push_back("qqHH_CV_1_C2V_0_kl_1_hbbhww");
  signals.push_back("qqHH_CV_1_C2V_2_kl_1_hbbhww");
  signals.push_back("qqHH_CV_1_C2V_1_kl_1_hbbhww");
  signals.push_back("qqHH_CV_0p5_C2V_1_kl_1_hbbhww");
  signals.push_back("qqHH_CV_1_C2V_1_kl_0_hbbhww");
  signals.push_back("qqHH_CV_1p5_C2V_1_kl_1_hbbhww");
  signals.push_back("ggHH_kl_1_kt_1_hbbhtt");
  signals.push_back("ggHH_kl_5_kt_1_hbbhtt");
  signals.push_back("ggHH_kl_2p45_kt_1_hbbhtt");
  signals.push_back("ggHH_kl_0_kt_1_hbbhtt");
  signals.push_back("qqHH_CV_1_C2V_1_kl_2_hbbhtt");
  signals.push_back("qqHH_CV_1_C2V_0_kl_1_hbbhtt");
  signals.push_back("qqHH_CV_1_C2V_2_kl_1_hbbhtt");
  signals.push_back("qqHH_CV_1_C2V_1_kl_1_hbbhtt");
  signals.push_back("qqHH_CV_0p5_C2V_1_kl_1_hbbhtt");
  signals.push_back("qqHH_CV_1_C2V_1_kl_0_hbbhtt");
  signals.push_back("qqHH_CV_1p5_C2V_1_kl_1_hbbhtt");
  /*signals.push_back("signal_ggf_spin2_450_hbbhww");
  signals.push_back("signal_ggf_spin2_450_hbbhzz");
  signals.push_back("signal_ggf_spin2_450_hbbhtt");*/
  //signals.push_back("ggHH_M_900_hbbhwwdl");
  //signals.push_back("ggHH_M_900_hbbhtt");
  //signals.push_back("ggHH_kl_1_kt_1_hbbhww");
  //signals.push_back("ggHH_kl_1_kt_1_hbbhtt");
  std::vector<std::string> background_processes;
  background_processes.push_back("TT");
  background_processes.push_back("ST");
  background_processes.push_back("WJets");
  background_processes.push_back("DY");
  background_processes.push_back("Fakes");
  //background_processes.push_back("ttZ");
  //background_processes.push_back("ttW");
  //background_processes.push_back("ttWW");
  background_processes.push_back("VV");
  background_processes.push_back("VVV");
  //background_processes.push_back("Convs");
  background_processes.push_back("Other_bbWW");
  vstring inclusive_procss;
  //inclusive_procss.push_back("ggH");
  //inclusive_procss.push_back("qqH");
  /*inclusive_procss.push_back("ZH");
  inclusive_procss.push_back("WH");
  inclusive_procss.push_back("tHq");
  inclusive_procss.push_back("tHW");
  inclusive_procss.push_back("ttH");
  vstring brs;
  brs.push_back("hww");
  brs.push_back("hbb");
  brs.push_back("hzz");
  brs.push_back("htt");
  for (auto inclusive_proc: inclusive_procss) {
    for ( auto br: brs ) {
      background_processes.push_back(Form("%s_%s", inclusive_proc.data(), br.data()));
    }
    }*/
  int colors[6] = { 1, 2, 8, 4, 6, 7 };
  int lineStyles[6] = { 1, 1, 1, 1, 1, 1 };
  int markerStyles[6] = { 22, 32, 20, 24, 21, 25 };

  bool firstHist(true);
  TH1* histogram_S;
  for ( std::vector<std::string>::const_iterator signal = signals.begin();
        signal != signals.end(); ++signal ) {
    std::string histogramName_S_full = Form("%s", signal->data());
    if ( firstHist ) {
      histogram_S = loadHistogram(inputFile, histogramName_S_full);
      if(histogram_S) firstHist = false;
    }
    else {
      TH1* h = loadHistogram(inputFile, histogramName_S_full);
      if (h) histogram_S->Add(h);
    }
  }
  firstHist = true;
  TH1* histogram_B;
  for ( std::vector<std::string>::const_iterator bkg = background_processes.begin();
        bkg != background_processes.end(); ++bkg ) {
    std::string histogramName_B_full = Form("%s", bkg->data());
    if ( firstHist ) {
      histogram_B = loadHistogram(inputFile, histogramName_B_full);
      if (histogram_B) firstHist = false;
    }
    else {
      TH1* h = loadHistogram(inputFile, histogramName_B_full);
      if (h) histogram_B->Add(h);
    }
  }
  TGraph* graphs_ROC = compGraph_ROCcurve_fromHistogram1d(histogram_S, histogram_B);
  std::vector<std::string> labelTextLines;
  labelTextLines.push_back(Form("auc: %0.3f", graphs_ROC->Integral()));
  labelTextLines.push_back("\n\n\n");
  /*labelTextLines.push_back(Form("Signal: %0.3f", histogram_S->Integral()));
  labelTextLines.push_back("\n\n\n");
  labelTextLines.push_back(Form("Background: %0.3f", histogram_B->Integral()));
  labelTextLines.push_back("\n\n\n");*/
  labelTextLines.push_back(Form("S/sqrt(B): %0.3f", histogram_S->Integral()/TMath::Sqrt(histogram_B->Integral())));
  showGraphs(1150, 800,
             graphs_ROC, cat.data(),
             0, "",
             0, "",
             0, "",
             0, "",
             0, "",
             colors, markerStyles, 
             0.050, 0.63, 0.23, 0.26, 0.30, 
             labelTextLines, 0.050,
             0.63, 0.65, 0.26, 0.07, 
             0., 1., "P(Background)", 1.2, 
             false, 1.e-3, 1.e0, "P(Signal)", 1.2, 
             Form("%s_MVAOutput_SM", cat.data()));

  std::cout << histogram_B->Integral() << "\t" << histogram_S->Integral() << std::endl;
}
