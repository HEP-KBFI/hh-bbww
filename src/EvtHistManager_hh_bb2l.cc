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

  histogram_m_Hbb_                  = book1D(dir, "m_Hbb",                  "m_Hbb",                   40,  0.,  200.); 
  histogram_dR_Hbb_                 = book1D(dir, "dR_Hbb",                 "dR_Hbb",                 100,  0.,    5.);
  histogram_dPhi_Hbb_               = book1D(dir, "dPhi_Hbb",               "dPhi_Hbb",                36, -TMath::Pi(), +TMath::Pi());
  histogram_pT_Hbb_                 = book1D(dir, "pT_Hbb",                 "pT_Hbb",                 100,  0.,  500.); 

  histogram_m_ll_                   = book1D(dir, "m_ll",                   "m_ll",                    40,  0.,  200.); 
  histogram_dR_ll_                  = book1D(dir, "dR_ll",                  "dR_ll",                  100,  0.,    5.);
  histogram_dPhi_ll_                = book1D(dir, "dPhi_ll",                "dPhi_ll",                 36, -TMath::Pi(), +TMath::Pi());
  histogram_pT_ll_                  = book1D(dir, "pT_ll",                  "pT_ll",                  100,  0.,  500.); 

  histogram_m_Hww_                  = book1D(dir, "m_Hww",                  "m_Hww",                   40,  0.,  200.); 
  histogram_pT_Hww_                 = book1D(dir, "pT_Hwww",                "pT_Hww",                 100,  0.,  500.);  
  histogram_Smin_Hww_               = book1D(dir, "Smin_Hww",               "Smin_Hww",               100,  0.,  500.);  

  histogram_m_HHvis_                = book1D(dir, "m_HHvis",                "m_HHvis",                100,  0., 1000.);  
  histogram_m_HH_                   = book1D(dir, "m_HH",                   "m_HH",                   150,  0., 1500.);
  histogram_m_HH_hme_               = book1D(dir, "m_HH_hme",               "m_HH_hme",               150,  0., 1500.);
  histogram_dR_HH_                  = book1D(dir, "dR_HH",                  "dR_HH",                  100,  0.,    5.);
  histogram_dPhi_HH_                = book1D(dir, "dPhi_HH",                "dPhi_HH",                 36, -TMath::Pi(), +TMath::Pi());
  histogram_pT_HH_                  = book1D(dir, "pT_HH",                  "pT_HH",                  100,  0.,  500.);  
  histogram_Smin_HH_                = book1D(dir, "Smin_HH",                "Smin_HH",                100,  0., 1000.); 

  histogram_mT2_W_                  = book1D(dir, "mT2_W",                  "mT2_W",                   40,  0.,  200.); 
  histogram_mT2_W_step_             = book1D(dir, "mT2_W_step",             "mT2_W_step",             103, -1.5, 101.5); 
  histogram_mT2_top_2particle_      = book1D(dir, "mT2_top_2particle",      "mT2_top_2particle",      100,  0.,  500.);
  histogram_mT2_top_2particle_step_ = book1D(dir, "mT2_top_2particle_step", "mT2_top_2particle_step", 103, -1.5, 101.5); 
  histogram_mT2_top_3particle_      = book1D(dir, "mT2_top_3particle",      "mT2_top_3particle",      100,  0.,  500.);
  histogram_mT2_top_3particle_step_ = book1D(dir, "mT2_top_3particle_step", "mT2_top_3particle_step", 103, -1.5, 101.5); 

  histogram_logHiggsness_           = book1D(dir, "logHiggsness",           "logHiggsness",            60, -15., +15.);  
  histogram_logTopness_             = book1D(dir, "logTopness",             "logTopness",              60, -15., +15.);  
  histogram_logTopness_vs_logHiggsness_ = book2D(dir, "logTopness_vs_logHiggsness", "logTopness_vs_logHiggsness", 60, -15., +15., 60, -15., +15.);

  histogram_vbf_m_jj_               = book1D(dir, "vbf_m_jj",               "vbf_m_jj",               150,  0., 1500.);
  histogram_vbf_dEta_jj_            = book1D(dir, "vbf_dEta_jj",            "vbf_dEta_jj",            100,  0.,   10.);

  histogram_EventCounter_           = book1D(dir, "EventCounter",           "EventCounter",             1, -0.5,  +0.5);
  histogram_MVAOutput300_           = book1D(dir, "MVAOutput_300",           "MVAOutput_300",             100, 0.,  1.);
  histogram_MVAOutput400_           = book1D(dir, "MVAOutput_400",           "MVAOutput_400",             100, 0.,  1.);
  histogram_MVAOutput750_           = book1D(dir, "MVAOutput_750",           "MVAOutput_750",             100, 0.,  1.);
}

void
EvtHistManager_hh_bb2l::fillHistograms(int numElectrons,
				       int numMuons,
				       int numJets,
				       int numBJets_loose,
				       int numBJets_medium,
				       double HT,
				       double STMET,
				       double m_Hbb, double dR_Hbb, double dPhi_Hbb, double pT_Hbb, 
				       double m_ll, double dR_ll, double dPhi_ll, double pT_ll,
				       double m_Hww, double pT_Hww, double Smin_Hww,
				       double m_HHvis, double m_HH, double m_HH_hme, double dR_HH, double dPhi_HH, double pT_HH, double Smin_HH,
				       double mT2_W, int mT2_W_step, double mT2_top_2particle, int mT2_top_2particle_step, double mT2_top_3particle, int mT2_top_3particle_step,
				       double logHiggsness, double logTopness,
				       double vbf_m_jj, double vbf_dEta_jj, double mvaoutput_bb2l300, double mvaoutput_bb2l400, double mvaoutput_bb2l750,
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

  fillWithOverFlow(histogram_m_Hbb_,                  m_Hbb,                  evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dR_Hbb_,                 dR_Hbb,                 evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_Hbb_,               dPhi_Hbb,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_Hbb_,                 pT_Hbb,                 evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_m_ll_,                   m_ll,                   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dR_ll_,                  dR_ll,                  evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_ll_,                dPhi_ll,                evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_ll_,                  pT_ll,                  evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_m_Hww_,                  m_Hww,                  evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_Hww_,                 pT_Hww,                 evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_Smin_Hww_,               Smin_Hww,               evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_m_HHvis_,                m_HHvis,                evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_m_HH_,                   m_HH,                   evtWeight, evtWeightErr);
  if ( m_HH_hme > 0. ) {
    fillWithOverFlow(histogram_m_HH_hme_,             m_HH_hme,               evtWeight, evtWeightErr);    
  }
  fillWithOverFlow(histogram_dR_HH_,                  dR_HH,                  evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_HH_,                dPhi_HH,                evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_HH_,                  pT_HH,                  evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_Smin_HH_,                Smin_HH,                evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_mT2_W_,                  mT2_W,                  evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT2_W_step_,             mT2_W_step,             evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT2_top_2particle_,      mT2_top_2particle,      evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT2_top_2particle_step_, mT2_top_2particle_step, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT2_top_3particle_,      mT2_top_3particle,      evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT2_top_3particle_step_, mT2_top_3particle_step, evtWeight, evtWeightErr);
 
  fillWithOverFlow(histogram_logHiggsness_,           logHiggsness,           evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_logTopness_,             logTopness,             evtWeight, evtWeightErr);

  fillWithOverFlow2d(histogram_logTopness_vs_logHiggsness_, logHiggsness, logTopness, evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_vbf_m_jj_,               vbf_m_jj,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_vbf_dEta_jj_,            vbf_dEta_jj,            evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_MVAOutput300_,           mvaoutput_bb2l300,                     evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_MVAOutput400_,           mvaoutput_bb2l400,                     evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_MVAOutput750_,           mvaoutput_bb2l750,                     evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_EventCounter_,           0.,                     evtWeight, evtWeightErr);
}
