#include "hhAnalysis/bbww/interface/EvtHistManager_hh_bb1l.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), fillWithOverFlow2d()

#include <TMath.h> // TMath::Pi() 

EvtHistManager_hh_bb1l::EvtHistManager_hh_bb1l(const edm::ParameterSet & cfg)
  : HistManagerBase(cfg)
{}

const TH1 *
EvtHistManager_hh_bb1l::getHistogram_EventCounter() const
{
  return histogram_EventCounter_;
}

void
EvtHistManager_hh_bb1l::bookHistograms(TFileDirectory & dir)
{
  histogram_numElectrons_          = book1D(dir, "numElectrons",          "numElectrons",            5, -0.5,  +4.5);
  histogram_numMuons_              = book1D(dir, "numMuons",              "numMuons",                5, -0.5,  +4.5);
  histogram_numJets_               = book1D(dir, "numJets",               "numJets",                20, -0.5, +19.5);
  histogram_numBJets_loose_        = book1D(dir, "numBJets_loose",        "numBJets_loose",         10, -0.5,  +9.5);
  histogram_numBJets_medium_       = book1D(dir, "numBJets_medium",       "numBJets_medium",        10, -0.5,  +9.5);

  histogram_HT_                    = book1D(dir, "HT",                    "HT",                    150,  0., 1500.);
  histogram_STMET_                 = book1D(dir, "STMET",                 "STMET",                 150,  0., 1500.);

  histogram_m_bb_                  = book1D(dir, "m_bb",                  "m_bb",                   40,  0.,  200.); 
  histogram_dR_bb_                 = book1D(dir, "dR_bb",                 "dR_bb",                 100,  0.,    5.);

  histogram_dR_jjlMEt_             = book1D(dir, "dR_jjlMEt",             "dR_jjlMEt",             100,  0.,    5.);
  histogram_dPhi_jjlMEt_           = book1D(dir, "dPhi_jjlMEt",           "dPhi_jjlMEt",            36, -TMath::Pi(), +TMath::Pi());

  histogram_pT_jjlMEt_             = book1D(dir, "pT_jjlMEt",             "pT_jjlMEt",             100,  0.,  500.);  
  histogram_Smin_jjlMEt_           = book1D(dir, "Smin_jjlMEt",           "Smin_jjlMEt",           100,  0.,  500.);  

  histogram_pT_bbjjlMEt_           = book1D(dir, "pT_bbjjlMEt",           "pT_bbjjlMEt",           100,  0.,  500.);  
  histogram_Smin_bbjjlMEt_         = book1D(dir, "Smin_bbjjlMEt",         "Smin_bbjjlMEt",         100,  0., 1000.); 
  histogram_dPhi_bbjjlMEt_         = book1D(dir, "dPhi_bbjjlMEt",         "dPhi_bbjjlMEt",          36,  0., TMath::Pi());
  
  histogram_mT_W_                  = book1D(dir, "mT_W",                  "mT_W",                   40,  0.,  200.); 
  histogram_mT_top_2particle_      = book1D(dir, "mT_top_2particle",      "mT_top_2particle",      100,  0.,  500.);
  histogram_mT_top_3particle_      = book1D(dir, "mT_top_3particle",      "mT_top_3particle",      100,  0.,  500.);
 
  histogram_m_bbjjl_               = book1D(dir, "m_bbjjl",               "m_bbjjl",               100,  0., 1000.);  
  histogram_m_bbjjlMEt_            = book1D(dir, "m_bbjjlMEt",            "m_bbjjlMEt",            100,  0., 1000.);
  histogram_m_bbjjlMEt_B2G_18_008_ = book1D(dir, "m_bbjjlMEt_B2G_18_008", "m_bbjjlMEt_B2G_18_008", 100,  0., 1000.); 
  histogram_hmeMass_               = book1D(dir, "hmeMass",               "hmeMass",               150,  0., 1500.);

  histogram_EventCounter_          = book1D(dir, "EventCounter",          "EventCounter",            1, -0.5,  +0.5);
}

void
EvtHistManager_hh_bb1l::fillHistograms(int numElectrons,
				       int numMuons,
				       int numJets,
				       int numBJets_loose,
				       int numBJets_medium,
				       double HT,
				       double STMET,
				       double m_bb, double dR_bb, double dR_jjlMEt, double dPhi_jjlMEt, 
				       double pT_jjlMEt, double Smin_jjlMEt, 
				       double pT_bbjjlMEt, double Smin_bbjjlMEt, double dPhi_bbjjlMEt,
				       double mT_W, double mT_top_2particle, double mT_top_3particle,
				       double m_bbjjl, double m_bbjjlMEt, double m_bbjjlMEt_B2G_18_008, double hmeMass, 
				       double evtWeight)
{
  const double evtWeightErr = 0.;

  fillWithOverFlow(histogram_numElectrons_,          numElectrons,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numMuons_,              numMuons,              evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJets_,               numJets,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_loose_,        numBJets_loose,        evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_medium_,       numBJets_medium,       evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_HT_,                    HT,                    evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_STMET_,                 STMET,                 evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_m_bb_,                  m_bb,                  evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dR_bb_,                 dR_bb,                 evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_dR_jjlMEt_,             dR_jjlMEt,             evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_jjlMEt_,           dPhi_jjlMEt,           evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_pT_jjlMEt_,             pT_jjlMEt,             evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_Smin_jjlMEt_,           Smin_jjlMEt,           evtWeight, evtWeightErr);
 
  fillWithOverFlow(histogram_pT_bbjjlMEt_,           pT_bbjjlMEt,           evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_Smin_bbjjlMEt_,         Smin_bbjjlMEt,         evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_bbjjlMEt_,         dPhi_bbjjlMEt,         evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_mT_W_,                  mT_W,                  evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT_top_2particle_,      mT_top_2particle,      evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT_top_3particle_,      mT_top_3particle,      evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_m_bbjjl_,               m_bbjjl,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_m_bbjjlMEt_,            m_bbjjlMEt,            evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_m_bbjjlMEt_B2G_18_008_, m_bbjjlMEt_B2G_18_008, evtWeight, evtWeightErr);

  if ( hmeMass > 0. ) {
    fillWithOverFlow(histogram_hmeMass_,             hmeMass,               evtWeight, evtWeightErr);    
  }
  
  fillWithOverFlow(histogram_EventCounter_,             0.,                     evtWeight, evtWeightErr);
}
