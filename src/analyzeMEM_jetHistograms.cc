#include "hhAnalysis/bbww/interface/analyzeMEM_jetHistograms.h"

#include "tthAnalysis/HiggsToTauTau/interface/RecoJet.h"       // RecoJet
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetAK8.h"    // RecoJetAK8
#include "tthAnalysis/HiggsToTauTau/interface/RecoSubjetAK8.h" // RecoSubjetAK8

jetHistograms::jetHistograms(const std::string& label)
  : label_(label)
  , histogram_pt_(nullptr)
  , histogram_btagCSV_(nullptr)
{}

jetHistograms::~jetHistograms() {}

void 
jetHistograms::bookHistograms(fwlite::TFileService& fs)
{
  std::string histogramName_pt = Form("%s_pt", label_.data());
  histogram_pt_ = fs.make<TH1D>(histogramName_pt.data(), histogramName_pt.data(), 50, 0., 250.);
  std::string histogramName_absEta = Form("%s_absEta", label_.data());
  histogram_absEta_ = fs.make<TH1D>(histogramName_absEta.data(), histogramName_absEta.data(), 50, 0., 5.0);
  std::string histogramName_btagCSV = Form("%s_btagCSV", label_.data());
  histogram_btagCSV_ = fs.make<TH1D>(histogramName_btagCSV.data(), histogramName_btagCSV.data(), 50, 0., 1.);
}
  
void 
jetHistograms::fillHistograms(const RecoJetBase* jet, double evtWeight)
{
  fillWithOverFlow(histogram_pt_, jet->pt(), evtWeight); 
  fillWithOverFlow(histogram_absEta_, jet->absEta(), evtWeight); 
  if ( dynamic_cast<const RecoJet*>(jet) ) 
  {
    fillWithOverFlow(histogram_btagCSV_, (dynamic_cast<const RecoJet*>(jet))->BtagCSV(), evtWeight);
  }    
  else if ( dynamic_cast<const RecoSubjetAK8*>(jet) ) 
  {
    fillWithOverFlow(histogram_btagCSV_, (dynamic_cast<const RecoSubjetAK8*>(jet))->BtagCSV(), evtWeight);
  } else assert(0);
}
