
#include <TCanvas.h>
#include <TH1.h>
#include <TAxis.h>
#include <TF1.h>
#include <TLegend.h>
#include <TMath.h>
#include <TROOT.h>

#include <string>
#include <iostream>
#include <iomanip>
#include <assert.h>

void plotWBosonDecayAngle()
{
//--- stop ROOT from keeping references to all histograms
  TH1::AddDirectory(false);

//--- suppress the output canvas 
  gROOT->SetBatch(true);

  TCanvas* canvas = new TCanvas("canvas", "canvas", 1150, 850);
  canvas->SetFillColor(10);
  canvas->SetBorderSize(2);

  canvas->SetLeftMargin(0.14);
  canvas->SetBottomMargin(0.12);

  TF1* fWPlus  = new TF1("fWPlus",  "TMath::Power(1 - TMath::Cos(x), 2.)", 0., TMath::Pi());
  TF1* fWMinus = new TF1("fWMinus", "TMath::Power(1 + TMath::Cos(x), 2.)", 0., TMath::Pi());
  
  TH1* dummyHistogram = new TH1D("dummyHistogram", "dummyHistogram", 100, 0., TMath::Pi());
  dummyHistogram->SetTitle("");
  dummyHistogram->SetStats(false);
  dummyHistogram->SetMinimum(-0.5);
  dummyHistogram->SetMaximum(+4.5);

  TAxis* xAxis = dummyHistogram->GetXaxis();
  xAxis->SetTitle("#theta");
  xAxis->SetTitleSize(0.050);
  xAxis->SetTitleOffset(1.2);

  TAxis* yAxis = dummyHistogram->GetYaxis();
  yAxis->SetTitle("#frac{dN}{d#theta}");
  yAxis->SetTitleSize(0.050);
  yAxis->SetTitleOffset(1.3);

  dummyHistogram->Draw("axis");

  fWPlus->SetLineColor(1);
  fWPlus->SetLineWidth(1);
  fWPlus->SetLineStyle(7);
  fWPlus->Draw("same");

  fWMinus->SetLineColor(2);
  fWMinus->SetLineWidth(2);
  fWMinus->SetLineStyle(1);
  fWMinus->Draw("same");

  TLegend* legend = new TLegend(0.34, 0.73, 0.78, 0.89, "", "brNDC"); 
  legend->SetBorderSize(0);
  legend->SetFillColor(0);
  legend->SetTextSize(0.050);
  legend->AddEntry(fWPlus,  "(1 - cos #theta)^{2}", "L");
  legend->AddEntry(fWMinus, "(1 + cos #theta)^{2}", "L");
  legend->Draw();

  canvas->Print("plotWBosonDecayAngle.png");
  canvas->Print("plotWBosonDecayAngle.pdf");

  delete dummyHistogram;
  delete fWPlus;
  delete fWMinus;
  delete canvas;
}
