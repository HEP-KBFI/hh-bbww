#include "hhAnalysis/bbww/interface/EvtHistManager_hh_bb1l1tau.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), fillWithOverFlow2d()

#include <TMath.h> // TMath::Pi() 

EvtHistManager_hh_bb1l1tau::EvtHistManager_hh_bb1l1tau(const edm::ParameterSet & cfg)
  : HistManagerBase(cfg)
{
  central_or_shiftOptions_["numElectrons"] = { "central" };
  central_or_shiftOptions_["numMuons"] = { "central" };
  central_or_shiftOptions_["numHadTaus"] = { "central" };
  central_or_shiftOptions_["numJets"] = { "central" };
  central_or_shiftOptions_["numBJets_loose"] = { "central" };
  central_or_shiftOptions_["numBJets_medium"] = { "central" };
  central_or_shiftOptions_["HT"] = { "central" };
  central_or_shiftOptions_["STMET"] = { "central" };
  central_or_shiftOptions_["m_Hbb"] = { "central" };
  central_or_shiftOptions_["dR_Hbb"] = { "central" };
  central_or_shiftOptions_["dPhi_Hbb"] = { "central" };
  central_or_shiftOptions_["pT_Hbb"] = { "central" };
  central_or_shiftOptions_["m_ltau"] = { "central" };
  central_or_shiftOptions_["dR_ltau"] = { "central" };
  central_or_shiftOptions_["dPhi_ltau"] = { "central" };
  central_or_shiftOptions_["pT_ltau"] = { "central" };
  central_or_shiftOptions_["m_Hww"] = { "central" };
  central_or_shiftOptions_["pT_Hww"] = { "central" };
  central_or_shiftOptions_["m_HHvis"] = { "*" };
  central_or_shiftOptions_["m_HH"] = { "central" };
  central_or_shiftOptions_["dPhi_HH"] = { "central" };
  central_or_shiftOptions_["pT_HH"] = { "central" };
  central_or_shiftOptions_["mT2_W"] = { "central" };
  central_or_shiftOptions_["mT2_W_step"] = { "central" };
  central_or_shiftOptions_["mT2_top_2particle"] = { "central" };
  central_or_shiftOptions_["mT2_top_2particle_step"] = { "central" };
  central_or_shiftOptions_["mT2_top_3particle"] = { "central" };
  central_or_shiftOptions_["mT2_top_3particle_step"] = { "central" };
  central_or_shiftOptions_["vbf_jet1_pt"] = { "central" };
  central_or_shiftOptions_["vbf_jet1_eta"] = { "central" };
  central_or_shiftOptions_["vbf_jet2_pt"] = { "central" };
  central_or_shiftOptions_["vbf_jet2_eta"] = { "central" };
  central_or_shiftOptions_["vbf_m_jj"] = { "central" };
  central_or_shiftOptions_["vbf_dEta_jj"] = { "central" };
  central_or_shiftOptions_["EventCounter"] = { "*" };
}

const TH1 *
EvtHistManager_hh_bb1l1tau::getHistogram_EventCounter() const
{
  return histogram_EventCounter_;
}

void
EvtHistManager_hh_bb1l1tau::bookHistograms(TFileDirectory & dir)
{
  histogram_numElectrons_           = book1D(dir, "numElectrons",           "numElectrons",             5, -0.5,  +4.5);
  histogram_numMuons_               = book1D(dir, "numMuons",               "numMuons",                 5, -0.5,  +4.5);
  histogram_numHadTaus_             = book1D(dir, "numHadTaus",             "numHadTaus",               5, -0.5,  +4.5);
  histogram_numJets_                = book1D(dir, "numJets",                "numJets",                 20, -0.5, +19.5);
  histogram_numBJets_loose_         = book1D(dir, "numBJets_loose",         "numBJets_loose",          10, -0.5,  +9.5);
  histogram_numBJets_medium_        = book1D(dir, "numBJets_medium",        "numBJets_medium",         10, -0.5,  +9.5);

  histogram_HT_                     = book1D(dir, "HT",                     "HT",                     150,  0., 1500.);
  histogram_STMET_                  = book1D(dir, "STMET",                  "STMET",                  150,  0., 1500.);

  histogram_m_Hbb_                  = book1D(dir, "m_Hbb",                  "m_Hbb",                   40,  0.,  200.); 
  histogram_dR_Hbb_                 = book1D(dir, "dR_Hbb",                 "dR_Hbb",                 100,  0.,    5.);
  histogram_dPhi_Hbb_               = book1D(dir, "dPhi_Hbb",               "dPhi_Hbb",                36,  0, TMath::Pi());
  histogram_pT_Hbb_                 = book1D(dir, "pT_Hbb",                 "pT_Hbb",                 100,  0.,  500.); 

  histogram_m_ltau_                 = book1D(dir, "m_ltau",                 "m_ltau",                  40,  0.,  200.); 
  histogram_dR_ltau_                = book1D(dir, "dR_ltau",                "dR_ltau",                100,  0.,    5.);
  histogram_dPhi_ltau_              = book1D(dir, "dPhi_ltau",              "dPhi_ltau",               36,  0, TMath::Pi());
  histogram_pT_ltau_                = book1D(dir, "pT_ltau",                "pT_ltau",                100,  0.,  500.); 

  histogram_m_Hww_                  = book1D(dir, "m_Hww",                  "m_Hww",                   40,  0.,  200.); 
  histogram_pT_Hww_                 = book1D(dir, "pT_Hww",                 "pT_Hww",                 100,  0.,  500.);  

  histogram_m_HHvis_                = book1D(dir, "m_HHvis",                "m_HHvis",                100,  0., 1000.);  
  histogram_m_HH_                   = book1D(dir, "m_HH",                   "m_HH",                   150,  0., 1500.);
  histogram_dPhi_HH_                = book1D(dir, "dPhi_HH",                "dPhi_HH",                 36,  0., TMath::Pi());
  histogram_pT_HH_                  = book1D(dir, "pT_HH",                  "pT_HH",                  100,  0.,  500.);  

  histogram_mT2_W_                  = book1D(dir, "mT2_W",                  "mT2_W",                   40,  0.,  200.); 
  histogram_mT2_W_step_             = book1D(dir, "mT2_W_step",             "mT2_W_step",             103, -1.5, 101.5); 
  histogram_mT2_top_2particle_      = book1D(dir, "mT2_top_2particle",      "mT2_top_2particle",      100,  0.,  500.);
  histogram_mT2_top_2particle_step_ = book1D(dir, "mT2_top_2particle_step", "mT2_top_2particle_step", 103, -1.5, 101.5); 
  histogram_mT2_top_3particle_      = book1D(dir, "mT2_top_3particle",      "mT2_top_3particle",      100,  0.,  500.);
  histogram_mT2_top_3particle_step_ = book1D(dir, "mT2_top_3particle_step", "mT2_top_3particle_step", 103, -1.5, 101.5); 

  histogram_vbf_jet1_pt_            = book1D(dir, "vbf_jet1_pt",            "vbf_jet1_pt",             40,  0.,  200.);  
  histogram_vbf_jet1_eta_           = book1D(dir, "vbf_jet1_eta",           "vbf_jet1_eta",           100, -5.0,  +5.0);
  histogram_vbf_jet2_pt_            = book1D(dir, "vbf_jet2_pt",            "vbf_jet2_pt",             40,  0.,  200.);  
  histogram_vbf_jet2_eta_           = book1D(dir, "vbf_jet2_eta",           "vbf_jet2_eta",           100, -5.0,  +5.0);
  histogram_vbf_m_jj_               = book1D(dir, "vbf_m_jj",               "vbf_m_jj",               150,  0., 1500.);
  histogram_vbf_dEta_jj_            = book1D(dir, "vbf_dEta_jj",            "vbf_dEta_jj",            100,  0.,   10.);
  
  histogram_EventCounter_           = book1D(dir, "EventCounter",           "EventCounter",             1, -0.5,  +0.5);
}

void
EvtHistManager_hh_bb1l1tau::fillHistograms(int numElectrons,
					   int numMuons,
					   int numHadTaus,
					   int numJets,
					   int numBJets_loose,
					   int numBJets_medium,
					   double HT,
					   double STMET,
					   double m_Hbb, double dR_Hbb, double dPhi_Hbb, double pT_Hbb, 
					   double m_ltau, double dR_ltau, double dPhi_ltau, double pT_ltau,
					   double m_Hww, double pT_Hww, 
					   double m_HHvis, double m_HH, double dPhi_HH, double pT_HH, 
					   double mT2_W, int mT2_W_step, double mT2_top_2particle, int mT2_top_2particle_step, double mT2_top_3particle, int mT2_top_3particle_step, 
					   double vbf_jet1_pt, double vbf_jet1_eta, double vbf_jet2_pt, double vbf_jet2_eta, double vbf_m_jj, double vbf_dEta_jj,
					   double evtWeight)
{
  const double evtWeightErr = 0.;

  fillWithOverFlow(histogram_numElectrons_,           numElectrons,           evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numMuons_,               numMuons,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numHadTaus_,             numHadTaus,             evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJets_,                numJets,                evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_loose_,         numBJets_loose,         evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_medium_,        numBJets_medium,        evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_HT_,                     HT,                     evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_STMET_,                  STMET,                  evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_m_Hbb_,                  m_Hbb,                  evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dR_Hbb_,                 dR_Hbb,                 evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_Hbb_,               dPhi_Hbb,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_Hbb_,                 pT_Hbb,                 evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_m_ltau_,                 m_ltau,                 evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dR_ltau_,                dR_ltau,                evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_ltau_,              dPhi_ltau,              evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_ltau_,                pT_ltau,                evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_m_Hww_,                  m_Hww,                  evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_Hww_,                 pT_Hww,                 evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_m_HHvis_,                m_HHvis,                evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_m_HH_,                   m_HH,                   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_HH_,                dPhi_HH,                evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_HH_,                  pT_HH,                  evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_mT2_W_,                  mT2_W,                  evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT2_W_step_,             mT2_W_step,             evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT2_top_2particle_,      mT2_top_2particle,      evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT2_top_2particle_step_, mT2_top_2particle_step, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT2_top_3particle_,      mT2_top_3particle,      evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT2_top_3particle_step_, mT2_top_3particle_step, evtWeight, evtWeightErr);

  if ( vbf_jet1_pt > 0. ) {
    fillWithOverFlow(histogram_vbf_jet1_pt_,          vbf_jet1_pt,            evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_vbf_jet1_eta_,         vbf_jet1_eta,           evtWeight, evtWeightErr);
  }
  if ( vbf_jet2_pt > 0. ) {
    fillWithOverFlow(histogram_vbf_jet2_pt_,          vbf_jet2_pt,            evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_vbf_jet2_eta_,         vbf_jet2_eta,           evtWeight, evtWeightErr);
  }
  fillWithOverFlow(histogram_vbf_m_jj_,               vbf_m_jj,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_vbf_dEta_jj_,            vbf_dEta_jj,            evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_EventCounter_,           0.,                     evtWeight, evtWeightErr);
}
