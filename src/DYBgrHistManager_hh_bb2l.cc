#include "hhAnalysis/bbww/interface/DYBgrHistManager_hh_bb2l.h"

#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h" // cmsException()
#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), fillWithOverFlow2d()

#include <TMath.h> // TMath::Pi(), TMath::Log, TMath::Max

DYBgrHistManager_hh_bb2l::DYBgrHistManager_hh_bb2l(const edm::ParameterSet & cfg)
  : HistManagerBase(cfg)
{
  central_or_shiftOptions_["resolved_2b_HT"]         = { "*" };
  central_or_shiftOptions_["resolved_1b_HT"]         = { "*" };
  central_or_shiftOptions_["resolved_0b_HT"]         = { "*" };
  central_or_shiftOptions_["boosted_ge1b_msoftdrop"] = { "*" };
  central_or_shiftOptions_["boosted_0b_msoftdrop"]   = { "*" };
}

void
DYBgrHistManager_hh_bb2l::bookHistograms(TFileDirectory & dir)
{
  // CV: binning in HT and msoftdrop taken from Section 9.2 of AN-2020/119 v6.
  int numBins_HT = 36;
  float binning_HT[numBins_HT + 1] = { 
    50., 55., 60., 65., 70., 75., 80., 85., 90., 95., 
    100., 110., 120., 130., 140., 150., 160., 170., 180., 190., 
    200., 220., 240., 260., 280., 300., 325., 350., 375., 
    400., 450., 500., 550., 600., 700., 800., 1000.
  };

  histogram_resolved_2b_HT_ = book1D(dir, "resolved_2b_HT", "resolved_2b_HT", numBins_HT, binning_HT);
  histogram_resolved_1b_HT_ = book1D(dir, "resolved_1b_HT", "resolved_1b_HT", numBins_HT, binning_HT);
  histogram_resolved_0b_HT_ = book1D(dir, "resolved_0b_HT", "resolved_0b_HT", numBins_HT, binning_HT);
   
  int numBins_msoftdrop = 5;
  float binning_msoftdrop[numBins_HT + 1] = { 
    30., 50., 70., 100., 150., 210.
  };
  
  histogram_boosted_ge1b_msoftdrop_ = book1D(dir, "boosted_ge1b_msoftdrop", "boosted_ge1b_msoftdrop", numBins_msoftdrop, binning_msoftdrop);
  histogram_boosted_0b_msoftdrop_   = book1D(dir, "boosted_0b_msoftdrop",   "boosted_0b_msoftdrop",   numBins_msoftdrop, binning_msoftdrop);
}

void
DYBgrHistManager_hh_bb2l::fillHistograms(double HT, double selJetAK8_Hbb_msoftdrop, bool isBoosted, int numBJets_medium, double evtWeight)
{
  const double evtWeightErr = 0.;

  if ( isBoosted )
  {
    TH1 * histogram_msoftdrop = nullptr;
    if ( numBJets_medium >= 1 ) histogram_msoftdrop = histogram_boosted_ge1b_msoftdrop_;
    else                        histogram_msoftdrop = histogram_boosted_0b_msoftdrop_;
    fillWithOverFlow(histogram_msoftdrop, selJetAK8_Hbb_msoftdrop, evtWeight, evtWeightErr);
  }
  else
  {
    TH1 * histogram_HT = nullptr;
    if      ( numBJets_medium >= 2 ) histogram_HT = histogram_resolved_2b_HT_;
    else if ( numBJets_medium == 1 ) histogram_HT = histogram_resolved_1b_HT_;
    else                             histogram_HT = histogram_resolved_0b_HT_;
    fillWithOverFlow(histogram_HT, HT, evtWeight, evtWeightErr);
  }
}
