#include "hhAnalysis/bbww/interface/EvtHistManager_hh_bbWW_DYctrl.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), fillWithOverFlow2d()

#include <TMath.h> // TMath::Pi() 

EvtHistManager_hh_bbWW_DYctrl::EvtHistManager_hh_bbWW_DYctrl(const edm::ParameterSet & cfg)
  : HistManagerBase(cfg)
{
  central_or_shiftOptions_["numElectrons"] = { "central" };
  central_or_shiftOptions_["numMuons"] = { "central" };
  central_or_shiftOptions_["numJets"] = { "central" };
  central_or_shiftOptions_["numBJets_loose"] = { "central" };
  central_or_shiftOptions_["numBJets_medium"] = { "central" };
  central_or_shiftOptions_["HT"] = { "central" };
  central_or_shiftOptions_["STMET"] = { "central" };
  central_or_shiftOptions_["m_bb"] = { "central" };
  central_or_shiftOptions_["dR_bb"] = { "central" };
  central_or_shiftOptions_["dPhi_bb"] = { "central" };
  central_or_shiftOptions_["pT_bb"] = { "central" };
  central_or_shiftOptions_["m_ll"] = { "central" };
  central_or_shiftOptions_["dR_ll"] = { "central" };
  central_or_shiftOptions_["dPhi_ll"] = { "central" };
  central_or_shiftOptions_["pT_ll"] = { "central" };
  central_or_shiftOptions_["m_bbll"] = { "central" };
  central_or_shiftOptions_["dPhi_bbll"] = { "central" };
  central_or_shiftOptions_["pT_bbll"] = { "central" };
  central_or_shiftOptions_["m_bbllMEt"] = { "central" };
  central_or_shiftOptions_["m_HH_hme"] = { "central" };
  central_or_shiftOptions_["dPhi_bbllMEt"] = { "central" };
  central_or_shiftOptions_["pT_bbllMEt"] = { "central" };
  central_or_shiftOptions_["Smin_bbllMEt"] = { "central" };
  central_or_shiftOptions_["vbf_m_jj"] = { "central" };
  central_or_shiftOptions_["vbf_dEta_jj"] = { "central" };
  central_or_shiftOptions_["EventCounter"] = { "*" };
}

const TH1 *
EvtHistManager_hh_bbWW_DYctrl::getHistogram_EventCounter() const
{
  return histogram_EventCounter_;
}

void
EvtHistManager_hh_bbWW_DYctrl::bookHistograms(TFileDirectory & dir)
{
  histogram_numElectrons_           = book1D(dir, "numElectrons",           "numElectrons",             5, -0.5,  +4.5);
  histogram_numMuons_               = book1D(dir, "numMuons",               "numMuons",                 5, -0.5,  +4.5);
  histogram_numJets_                = book1D(dir, "numJets",                "numJets",                 20, -0.5, +19.5);
  histogram_numBJets_loose_         = book1D(dir, "numBJets_loose",         "numBJets_loose",          10, -0.5,  +9.5);
  histogram_numBJets_medium_        = book1D(dir, "numBJets_medium",        "numBJets_medium",         10, -0.5,  +9.5);

  histogram_HT_                     = book1D(dir, "HT",                     "HT",                     150,  0., 1500.);
  histogram_STMET_                  = book1D(dir, "STMET",                  "STMET",                  150,  0., 1500.);
 
  histogram_m_bb_                   = book1D(dir, "m_bb",                   "m_bb",                    40,  0.,  200.); 
  histogram_dR_bb_                  = book1D(dir, "dR_bb",                  "dR_bb",                  100,  0.,    5.);
  histogram_dPhi_bb_                = book1D(dir, "dPhi_bb",                "dPhi_bb",                 36, -TMath::Pi(), +TMath::Pi());
  histogram_pT_bb_                  = book1D(dir, "pT_bb",                  "pT_bb",                  100,  0.,  500.); 

  histogram_m_ll_                   = book1D(dir, "m_ll",                   "m_ll",                    30,  60., 120.); 
  histogram_dR_ll_                  = book1D(dir, "dR_ll",                  "dR_ll",                  100,  0.,    5.);
  histogram_dPhi_ll_                = book1D(dir, "dPhi_ll",                "dPhi_ll",                 36, -TMath::Pi(), +TMath::Pi());
  histogram_pT_ll_                  = book1D(dir, "pT_ll",                  "pT_ll",                  100,  0.,  500.); 

  histogram_m_bbll_                 = book1D(dir, "m_bbll",                 "m_bbll",                 100,  0., 1000.);  
  histogram_dPhi_bbll_              = book1D(dir, "dPhi_bbll",              "dPhi_bbll",               36, -TMath::Pi(), +TMath::Pi());
  histogram_pT_bbll_                = book1D(dir, "pT_bbll",                "pT_bbll",                100,  0.,  500.);  

  histogram_m_bbllMEt_              = book1D(dir, "m_bbllMEt",              "m_bbllMEt",              150,  0., 1500.);
  histogram_m_HH_hme_               = book1D(dir, "m_HH_hme",               "m_HH_hme",               150,  0., 1500.);
  histogram_dPhi_bbllMEt_           = book1D(dir, "dPhi_bbllMEt",           "dPhi_bbllMEt",            36, -TMath::Pi(), +TMath::Pi());
  histogram_pT_bbllMEt_             = book1D(dir, "pT_bbllMEt",             "pT_bbllMEt",             100,  0.,  500.);  
  histogram_Smin_bbllMEt_           = book1D(dir, "Smin_bbllMEt",           "Smin_bbllMEt",           100,  0., 1000.); 

  histogram_vbf_m_jj_               = book1D(dir, "vbf_m_jj",               "vbf_m_jj",               150,  0., 1500.);
  histogram_vbf_dEta_jj_            = book1D(dir, "vbf_dEta_jj",            "vbf_dEta_jj",            100,  0.,   10.);

  histogram_EventCounter_           = book1D(dir, "EventCounter",           "EventCounter",             1, -0.5,  +0.5);
}

void
EvtHistManager_hh_bbWW_DYctrl::fillHistograms(int numElectrons,
					      int numMuons,
					      int numJets,
					      int numBJets_loose,
					      int numBJets_medium,
					      double HT,
					      double STMET,
					      double m_bb, double dR_bb, double dPhi_bb, double pT_bb, 
					      double m_ll, double dR_ll, double dPhi_ll, double pT_ll,
					      double m_bbll, double dPhi_bbll, double pT_bbll, 
					      double m_bbllMEt, double m_HH_hme, double dPhi_bbllMEt, double pT_bbllMEt, double Smin_bbllMEt,
					      double vbf_m_jj, double vbf_dEta_jj,
					      double evtWeight)
{
  const double evtWeightErr = 0.;

  fillWithOverFlow(histogram_numElectrons_,           numElectrons,           evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numMuons_,               numMuons,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJets_,                numJets,                evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_loose_,         numBJets_loose,         evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_medium_,        numBJets_medium,        evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_HT_,                     HT,                     evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_STMET_,                  STMET,                  evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_m_bb_,                   m_bb,                   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dR_bb_,                  dR_bb,                  evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_bb_,                dPhi_bb,                evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_bb_,                  pT_bb,                  evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_m_ll_,                   m_ll,                   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dR_ll_,                  dR_ll,                  evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_ll_,                dPhi_ll,                evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_ll_,                  pT_ll,                  evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_m_bbll_,                 m_bbll,                 evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_bbll_,              dPhi_bbll,              evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_bbll_,                pT_bbll,                evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_m_bbllMEt_,              m_bbllMEt,              evtWeight, evtWeightErr);
  if ( m_HH_hme > 0. ) {
    fillWithOverFlow(histogram_m_HH_hme_,             m_HH_hme,               evtWeight, evtWeightErr);    
  }
  fillWithOverFlow(histogram_dPhi_bbllMEt_,           dPhi_bbllMEt,           evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_bbllMEt_,             pT_bbllMEt,             evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_Smin_bbllMEt_,           Smin_bbllMEt,           evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_vbf_m_jj_,               vbf_m_jj,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_vbf_dEta_jj_,            vbf_dEta_jj,            evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_EventCounter_,           0.,                     evtWeight, evtWeightErr);
}
