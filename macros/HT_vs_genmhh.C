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
#include <TTree.h>
#include <TPaveStats.h>
#include <string>
#include <vector>
#include <map>
#include <iostream>
void var(std::string var) {
  TCanvas* canvas = new TCanvas("canvas", "canvas", 800, 800);
  std::string hist_dir = "hh_bb1l_Tight/sel/evtntuple";
  TLegend* l = new TLegend(0.30, 0.80, 0.60, 0.90);
  std::vector<TH1F*> hists;
  std::string samples_name[] = {"signal_ggf_spin0_260_hh", "signal_ggf_spin0_300_hh", "signal_ggf_spin0_400_hh", "signal_ggf_spin0_500_hh", "TTToSemiLeptonic", "W2JetsToLNu"};
  std::string inputPaths = "/hdfs/local/snandan/hhAnalysis/2016/bdt_bb1l_with_additional_jets/histograms/hh_bb1l/Tight";
  int color[] = {1,2,3,4,6,7,8,9,10,11,12,13};
  float ymax = 0;
  float dy1 = 0.15;
  float dy = 0.1;
  for(int sample_name=0; sample_name<=5; sample_name++) {
    TH1D* h = new TH1D("","", 15, 50, 1000);
    TPaveStats* stat;
    std::string filename  = (sample_name<4) ? Form("%s/%s_2b2v_sl/analyze_%s_2b2v_sl_Tight_central_1.root", inputPaths.data(), samples_name[sample_name].data(), samples_name[sample_name].data()) : ((sample_name==4) ? Form("%s/TTToSemiLeptonic/analyze_TTToSemiLeptonic_Tight_central_1.root", inputPaths.data()) : Form("%s/W2JetsToLNu/analyze_W2JetsToLNu_Tight_central_1.root", inputPaths.data()));
    TFile* f = new TFile(filename.c_str(), "r");
    TTree* t = (sample_name<4) ? (TTree*) f->Get(Form("%s/%s/evtTree", hist_dir.data(), samples_name[sample_name].data())) :
      ((sample_name==4) ? (TTree*) f->Get(Form("%s/TT/evtTree", hist_dir.data())) : (TTree*) f->Get(Form("%s/W/evtTree", hist_dir.data())));
    float mhh;
    t->SetBranchAddress(var.c_str(),&mhh);
    for (Int_t i=0; i<t->GetEntries(); i++) {
      t->GetEntry(i);
      h->Fill(mhh);
    }
    h->Scale(1/h->Integral());
    h->GetYaxis()->SetRangeUser(0,0.4);
    h->SetLineColor(color[sample_name]);
    if(sample_name ==0)  h->Draw("hist");
    else h->Draw("hist sames");
    l->AddEntry(h, samples_name[sample_name].c_str(), "l");
    gPad->Update();
    stat = (TPaveStats*)h->GetListOfFunctions()->FindObject("stats");
    stat->SetX1NDC(0.8);
    stat->SetX2NDC(1.0);
    stat->SetY1NDC(dy1);
    stat->SetY2NDC(dy1+dy);
    stat->SetTextColor(color[sample_name]);
    stat->Draw("same");
    dy1 += dy;
  }
  l->Draw("same");
  canvas->Update();
  canvas->SaveAs(Form("%s.png", var.data()));
}
