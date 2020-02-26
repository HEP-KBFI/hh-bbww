#include "hhAnalysis/bbww/interface/EvtHistManager_hh_bbWW_Wctrl.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), fillWithOverFlow2d()

#include <TMath.h> // TMath::Pi() 

EvtHistManager_hh_bbWW_Wctrl::EvtHistManager_hh_bbWW_Wctrl(const edm::ParameterSet & cfg)
  : HistManagerBase(cfg)
{
  central_or_shiftOptions_["numElectrons"] = { "central" };
  central_or_shiftOptions_["numMuons"] = { "central" };
  central_or_shiftOptions_["numJets"] = { "*" };
  central_or_shiftOptions_["numBJets_loose"] = { "*" };
  central_or_shiftOptions_["numBJets_medium"] = { "*" };
  central_or_shiftOptions_["numJetsAK8_Hbb"] = { "*" };
  central_or_shiftOptions_["numJetsAK8_Wjj"] = { "*" };
  central_or_shiftOptions_["HT"] = { "central" };
  central_or_shiftOptions_["STMET"] = { "central" };
  central_or_shiftOptions_["mT"] = { "*" };
  central_or_shiftOptions_["dPhi_lnu"] = { "central" };
  central_or_shiftOptions_["pT_lnu"] = { "*" };
  central_or_shiftOptions_["m_HH_hme"] = { "central" };
  central_or_shiftOptions_["jetAK8_Wjj_dR_lepton"] = { "central" };
  central_or_shiftOptions_["vbf_m_jj"] = { "central" };
  central_or_shiftOptions_["vbf_dEta_jj"] = { "central" };
  central_or_shiftOptions_["EventCounter"] = { "*" };
}

const TH1 *
EvtHistManager_hh_bbWW_Wctrl::getHistogram_EventCounter() const
{
  return histogram_EventCounter_;
}

void
EvtHistManager_hh_bbWW_Wctrl::bookHistograms(TFileDirectory & dir)
{
  histogram_numElectrons_           = book1D(dir, "numElectrons",           "numElectrons",             5, -0.5,  +4.5);
  histogram_numMuons_               = book1D(dir, "numMuons",               "numMuons",                 5, -0.5,  +4.5);
  histogram_numJets_                = book1D(dir, "numJets",                "numJets",                 20, -0.5, +19.5);
  histogram_numBJets_loose_         = book1D(dir, "numBJets_loose",         "numBJets_loose",          10, -0.5,  +9.5);
  histogram_numBJets_medium_        = book1D(dir, "numBJets_medium",        "numBJets_medium",         10, -0.5,  +9.5);
  histogram_numJetsAK8_Hbb_         = book1D(dir, "numJetsAK8_Hbb",         "numJetsAK8_Hbb",           4, -0.5,  +3.5);
  histogram_numJetsAK8_Wjj_         = book1D(dir, "numJetsAK8_Wjj",         "numJetsAK8_Wjj",           4, -0.5,  +3.5);
 
  histogram_HT_                     = book1D(dir, "HT",                     "HT",                     150,  0., 1500.);
  histogram_STMET_                  = book1D(dir, "STMET",                  "STMET",                  150,  0., 1500.);

  histogram_mT_                     = book1D(dir, "mT",                     "mT",                      30,  0.,  150.); 
  histogram_dPhi_lnu_               = book1D(dir, "dPhi_lnu",               "dPhi_lnu",                36, -TMath::Pi(), +TMath::Pi());
  histogram_pT_lnu_                 = book1D(dir, "pT_lnu",                 "pT_lnu",                 100,  0.,  500.); 

  histogram_m_HH_hme_               = book1D(dir, "m_HH_hme",               "m_HH_hme",               150,  0., 1500.);

  histogram_jetAK8_Wjj_dR_lepton_   = book1D(dir, "jetAK8_Wjj_dR_lepton",   "jetAK8_Wjj_dR_lepton",    50., 0.,    5.);

  histogram_vbf_m_jj_               = book1D(dir, "vbf_m_jj",               "vbf_m_jj",               150,  0., 1500.);
  histogram_vbf_dEta_jj_            = book1D(dir, "vbf_dEta_jj",            "vbf_dEta_jj",            100,  0.,   10.);

  histogram_EventCounter_           = book1D(dir, "EventCounter",           "EventCounter",             1, -0.5,  +0.5);
}

void
EvtHistManager_hh_bbWW_Wctrl::fillHistograms(int numElectrons,
					     int numMuons,
					     int numJets,
					     int numBJets_loose,
					     int numBJets_medium,
                                             int numJetsAK8_Hbb, 
                                             int numJetsAK8_Wjj, 
					     double HT,
					     double STMET,
		                             double mT, double dPhi_lnu, double pT_lnu,
                                             double m_HH_hme,
                                             double jetAK8_Wjj_dR_lepton, 
					     double vbf_m_jj, double vbf_dEta_jj,
					     double evtWeight)
{
  const double evtWeightErr = 0.;

  fillWithOverFlow(histogram_numElectrons_,           numElectrons,           evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numMuons_,               numMuons,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJets_,                numJets,                evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_loose_,         numBJets_loose,         evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_medium_,        numBJets_medium,        evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJetsAK8_Hbb_,         numJetsAK8_Hbb,         evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJetsAK8_Wjj_,         numJetsAK8_Wjj,         evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_HT_,                     HT,                     evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_STMET_,                  STMET,                  evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_mT_,                     mT,                     evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_lnu_,               dPhi_lnu,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_lnu_,                 pT_lnu,                 evtWeight, evtWeightErr);

  if ( m_HH_hme > 0. ) {
    fillWithOverFlow(histogram_m_HH_hme_,             m_HH_hme,               evtWeight, evtWeightErr);    
  }

  if ( jetAK8_Wjj_dR_lepton >= 0. ) {
    fillWithOverFlow(histogram_jetAK8_Wjj_dR_lepton_, jetAK8_Wjj_dR_lepton,   evtWeight, evtWeightErr);    
  }

  fillWithOverFlow(histogram_vbf_m_jj_,               vbf_m_jj,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_vbf_dEta_jj_,            vbf_dEta_jj,            evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_EventCounter_,           0.,                     evtWeight, evtWeightErr);
}
