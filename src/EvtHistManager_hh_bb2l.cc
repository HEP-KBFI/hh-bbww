#include "hhAnalysis/bbww/interface/EvtHistManager_hh_bb2l.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), fillWithOverFlow2d()

#include <TMath.h> // TMath::Pi() 

EvtHistManager_hh_bb2l::EvtHistManager_hh_bb2l(const edm::ParameterSet & cfg)
  : HistManagerBase(cfg)
{}

const TH1 *
EvtHistManager_hh_bb2l::getHistogram_EventCounter() const
{
  return histogram_EventCounter_;
}

void
EvtHistManager_hh_bb2l::bookHistograms(TFileDirectory & dir)
{
  histogram_numElectrons_           = book1D(dir, "numElectrons",           "numElectrons",             5, -0.5,  +4.5);
  histogram_numMuons_               = book1D(dir, "numMuons",               "numMuons",                 5, -0.5,  +4.5);
  histogram_numJets_                = book1D(dir, "numJets",                "numJets",                 20, -0.5, +19.5);
  histogram_numBJets_loose_         = book1D(dir, "numBJets_loose",         "numBJets_loose",          10, -0.5,  +9.5);
  histogram_numBJets_medium_        = book1D(dir, "numBJets_medium",        "numBJets_medium",         10, -0.5,  +9.5);

  histogram_HT_                     = book1D(dir, "HT",                     "HT",                     150,  0., 1500.);
  histogram_STMET_                  = book1D(dir, "STMET",                  "STMET",                  150,  0., 1500.);

  histogram_m_bb_                   = book1D(dir, "m_bb",                   "m_bb",                    40,  0.,  200.); 
  histogram_dR_bb_                  = book1D(dir, "dR_bb",                  "dR_bb",              100,  0.,    5.);

  histogram_m_ll_                   = book1D(dir, "m_ll",                   "m_ll",                    40,  0.,  200.); 
  histogram_dR_ll_                  = book1D(dir, "dR_ll",                  "dR_ll",              100,  0.,    5.);

  histogram_mT_llMEt_               = book1D(dir, "mT_llMEt",               "mT_llMEt",               100,  0.,  500.);  

  histogram_pT_bbllMEt_             = book1D(dir, "pT_bbllMEt",             "pT_bbllMEt",             100,  0.,  500.);  
  histogram_dPhi_bbllMEt_           = book1D(dir, "dPhi_bbllMEt",           "dPhi_bbllMEt",        36,  0., TMath::Pi());

  histogram_mT2_W_                  = book1D(dir, "mT2_W",                  "mT2_W",                   40,  0.,  200.); 
  histogram_mT2_W_step_             = book1D(dir, "mT2_W",                  "mT2_W",                  103, -1.5, 101.5); 
  histogram_mT2_top_2particle_      = book1D(dir, "mT2_top_2particle",      "mT2_top_2particle",      100,  0.,  500.);
  histogram_mT2_top_2particle_step_ = book1D(dir, "mT2_top_2particle_step", "mT2_top_2particle_step", 103, -1.5, 101.5); 
  histogram_mT2_top_3particle_      = book1D(dir, "mT2_top_3particle",      "mT2_top_3particle",      100,  0.,  500.);
  histogram_mT2_top_3particle_step_ = book1D(dir, "mT2_top_3particle_step", "mT2_top_3particle_step", 103, -1.5, 101.5); 
 
  histogram_logHiggsness_           = book1D(dir, "logHiggsness",           "logHiggsness",            60, -15., +15.);  
  histogram_logTopness_             = book1D(dir, "logTopness",             "logTopness",              60, -15., +15.);  
  histogram_logTopness_vs_logHiggsness_ = book2D(dir, "logTopness_vs_logHiggsness", "logTopness_vs_logHiggsness", 60, -15., +15., 60, -15., +15.);

  histogram_m_bbll_                 = book1D(dir, "m_bbll",                 "m_bbll",                 100,  0., 1000.);  
  histogram_m_bbllMEt_              = book1D(dir, "m_bbllMEt",              "m_bbllMEt",              100,  0., 1000.);
  histogram_hmeMass_                = book1D(dir, "hmeMass",                "hmeMass",                150,  0., 1500.);

  histogram_EventCounter_           = book1D(dir, "EventCounter",           "EventCounter",             1, -0.5,  +0.5);
}

void
EvtHistManager_hh_bb2l::fillHistograms(int numElectrons,
				       int numMuons,
				       int numJets,
				       int numBJets_loose,
				       int numBJets_medium,
				       double HT,
				       double STMET,
				       double m_bb, double dR_bb, double m_ll, double dR_ll,
				       double mT_llMEt,
				       double pT_bbllMEt, double dPhi_bbllMEt,
				       double mT2_W, int mT2_W_step, double mT2_top_2particle, int mT2_top_2particle_step, double mT2_top_3particle, int mT2_top_3particle_step,
				       double logHiggsness, double logTopness,
				       double m_bbll, double m_bbllMEt, double hmeMass, 
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

  fillWithOverFlow(histogram_m_ll_,                   m_ll,                   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dR_ll_,                  dR_ll,                  evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_mT_llMEt_,               mT_llMEt,               evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_pT_bbllMEt_,             pT_bbllMEt,             evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_bbllMEt_,           dPhi_bbllMEt,           evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_mT2_W_,                  mT2_W,                  evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT2_W_step_,             mT2_W_step,             evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT2_top_2particle_,      mT2_top_2particle,      evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT2_top_2particle_step_, mT2_top_2particle_step, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT2_top_3particle_,      mT2_top_3particle,      evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT2_top_3particle_step_, mT2_top_3particle_step, evtWeight, evtWeightErr);
 
  fillWithOverFlow(histogram_logHiggsness_,           logHiggsness,           evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_logTopness_,             logTopness,             evtWeight, evtWeightErr);

  fillWithOverFlow2d(histogram_logTopness_vs_logHiggsness_, logHiggsness, logTopness, evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_m_bbll_,                 m_bbll,                 evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_m_bbllMEt_,              m_bbllMEt,              evtWeight, evtWeightErr);

  if ( hmeMass > 0. ) {
    fillWithOverFlow(histogram_hmeMass_,              hmeMass,                evtWeight, evtWeightErr);    
  }
  
  fillWithOverFlow(histogram_EventCounter_,           0.,                     evtWeight, evtWeightErr);
}
