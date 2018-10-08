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

  histogram_m_Wjj_                  = book1D(dir, "m_Wjj",                  "m_Wjj",                   40,  0.,  200.); 
  histogram_dR_Wjj_                 = book1D(dir, "dR_Wjj",                 "dR_Wjj",                 100,  0.,    5.);
  histogram_dPhi_Wjj_               = book1D(dir, "dPhi_Wjj",               "dPhi_Wjj",                36, -TMath::Pi(), +TMath::Pi());
  histogram_pT_Wjj_                 = book1D(dir, "pT_Wjj",                 "pT_Wjj",                 100,  0.,  500.); 

  histogram_dR_Hww_                 = book1D(dir, "dR_Hww",                 "dR_Hww",                 100,  0.,    5.);
  histogram_dPhi_Hww_               = book1D(dir, "dPhi_Hww",               "dPhi_Hww",                36, -TMath::Pi(), +TMath::Pi());
  histogram_pT_Hww_                 = book1D(dir, "pT_Hwww",                "pT_Hww",                 100,  0.,  500.);  
  histogram_Smin_Hww_               = book1D(dir, "Smin_Hww",               "Smin_Hww",               100,  0.,  500.);  

  histogram_m_HHvis_                = book1D(dir, "m_HHvis",                "m_HHvis",                100,  0., 1000.);  
  histogram_m_HH_                   = book1D(dir, "m_HH",                   "m_HH",                   150,  0., 1500.);
  histogram_m_HH_B2G_18_008_        = book1D(dir, "m_HH_B2G_18_008",        "m_HH_B2G_18_008",        150,  0., 1500.);
  histogram_m_HH_hme_               = book1D(dir, "m_HH_hme",               "m_HH_hme",               150,  0., 1500.);
  histogram_dR_HH_                  = book1D(dir, "dR_HH",                  "dR_HH",                  100,  0.,    5.);
  histogram_dPhi_HH_                = book1D(dir, "dPhi_HH",                "dPhi_HH",                 36, -TMath::Pi(), +TMath::Pi());
  histogram_pT_HH_                  = book1D(dir, "pT_HH",                  "pT_HH",                  100,  0.,  500.);  
  histogram_Smin_HH_                = book1D(dir, "Smin_HH",                "Smin_HH",                100,  0., 1000.); 
  
  histogram_mT_W_                   = book1D(dir, "mT_W",                   "mT_W",                    40,  0.,  200.); 
  histogram_mT_top_2particle_       = book1D(dir, "mT_top_2particle",       "mT_top_2particle",       100,  0.,  500.);
  histogram_mT_top_3particle_       = book1D(dir, "mT_top_3particle",       "mT_top_3particle",       100,  0.,  500.);
  
  histogram_mvaOutput_Hj_tagger_    = book1D(dir, "mvaOutput_Hj_tagger",    "mvaOutput_Hj_tagger",     40, -1.,  +1.);
  histogram_mvaOutput_Hjj_tagger_   = book1D(dir, "mvaOutput_Hjj_tagger",   "mvaOutput_Hjj_tagger",    40, -1.,  +1.);

  histogram_vbf_m_jj_               = book1D(dir, "vbf_m_jj",               "vbf_m_jj",               150,  0., 1500.);
  histogram_vbf_dEta_jj_            = book1D(dir, "vbf_dEta_jj",            "vbf_dEta_jj",            100,  0.,   10.);

  histogram_EventCounter_           = book1D(dir, "EventCounter",           "EventCounter",             1, -0.5,  +0.5);
}

void
EvtHistManager_hh_bb1l::fillHistograms(int numElectrons,
				       int numMuons,
				       int numJets,
				       int numBJets_loose,
				       int numBJets_medium,
				       double HT,
				       double STMET,
				       double m_Hbb, double dR_Hbb, double dPhi_Hbb, double pT_Hbb, 
				       double m_Wjj, double dR_Wjj, double dPhi_Wjj, double pT_Wjj, 
				       double dR_Hww, double dPhi_Hww, double pT_Hww, double Smin_Hww,
				       double m_HHvis, double m_HH, double m_HH_B2G_18_008, double m_HH_hme, double dR_HH, double dPhi_HH, double pT_HH, double Smin_HH,
				       double mT_W, double mT_top_2particle, double mT_top_3particle,
				       double mvaOutput_Hj_tagger, double mvaOutput_Hjj_tagger,
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

  fillWithOverFlow(histogram_m_Hbb_,                  m_Hbb,                  evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dR_Hbb_,                 dR_Hbb,                 evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_Hbb_,               dPhi_Hbb,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_Hbb_,                 pT_Hbb,                 evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_m_Wjj_,                  m_Wjj,                  evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dR_Wjj_,                 dR_Wjj,                 evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_Wjj_,               dPhi_Wjj,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_Wjj_,                 pT_Wjj,                 evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_dR_Hww_,                 dR_Hww,                 evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_Hww_,               dPhi_Hww,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_Hww_,                 pT_Hww,                 evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_Smin_Hww_,               Smin_Hww,               evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_m_HHvis_,                m_HHvis,                evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_m_HH_,                   m_HH,                   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_m_HH_B2G_18_008_,        m_HH_B2G_18_008,        evtWeight, evtWeightErr);
  if ( m_HH_hme > 0. ) {
    fillWithOverFlow(histogram_m_HH_hme_,             m_HH_hme,               evtWeight, evtWeightErr);    
  }
  fillWithOverFlow(histogram_dR_HH_,                  dR_HH,                  evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_HH_,                dPhi_HH,                evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_HH_,                  pT_HH,                  evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_Smin_HH_,                Smin_HH,                evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_mT_W_,                   mT_W,                   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT_top_2particle_,       mT_top_2particle,       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT_top_3particle_,       mT_top_3particle,       evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_mvaOutput_Hj_tagger_,    mvaOutput_Hj_tagger,    evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mvaOutput_Hjj_tagger_,   mvaOutput_Hjj_tagger,   evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_vbf_m_jj_,               vbf_m_jj,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_vbf_dEta_jj_,            vbf_dEta_jj,            evtWeight, evtWeightErr);
  
  fillWithOverFlow(histogram_EventCounter_,           0.,                     evtWeight, evtWeightErr);
}
