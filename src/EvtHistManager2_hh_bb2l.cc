#include "hhAnalysis/bbww/interface/EvtHistManager2_hh_bb2l.h"

#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h" // cmsException()
#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), fillWithOverFlow2d()

#include <TMath.h> // TMath::Pi(), TMath::Log, TMath::Max

EvtHistManager2_hh_bb2l::EvtHistManager2_hh_bb2l(const edm::ParameterSet & cfg)
  : HistManagerBase(cfg)
{
  central_or_shiftOptions_["numElectrons"] = { "central" };
  central_or_shiftOptions_["numMuons"] = { "central" };
  central_or_shiftOptions_["numJets"] = { "central" };
  central_or_shiftOptions_["numBJets_loose"] = { "central" };
  central_or_shiftOptions_["numBJets_medium"] = { "central" };
  central_or_shiftOptions_["HT"] = { "central" };
  central_or_shiftOptions_["STMET"] = { "central" };  
  central_or_shiftOptions_["m_Hbb"] = { "central" };
  central_or_shiftOptions_["dR_Hbb"] = { "central" };
  central_or_shiftOptions_["dPhi_Hbb"] = { "central" };
  central_or_shiftOptions_["pT_Hbb"] = { "central" };
  central_or_shiftOptions_["m_ll"] = { "central" };
  central_or_shiftOptions_["dR_ll"] = { "central" };
  central_or_shiftOptions_["dPhi_ll"] = { "central" };
  central_or_shiftOptions_["pT_ll"] = { "central" };
  central_or_shiftOptions_["m_HHvis"] = { "central" };
  central_or_shiftOptions_["m_HH"] = { "central" };
  central_or_shiftOptions_["m_HH_hme"] = { "central" };
  central_or_shiftOptions_["hmeCpuTime"] = { "central" };
  central_or_shiftOptions_["vbf_jet1_pt"] = { "central" };
  central_or_shiftOptions_["vbf_jet1_eta"] = { "central" };
  central_or_shiftOptions_["vbf_jet2_pt"] = { "central" };
  central_or_shiftOptions_["vbf_jet2_eta"] = { "central" };
  central_or_shiftOptions_["vbf_m_jj"] = { "central" };
  central_or_shiftOptions_["vbf_dEta_jj"] = { "central" };
  central_or_shiftOptions_["EventCounter"] = { "*" };
  central_or_shiftOptions_["leadlepton_cone_pt"] = { "central" };
  central_or_shiftOptions_["subleadlepton_cone_pt"] = { "central" };
}

const TH1 *
EvtHistManager2_hh_bb2l::getHistogram_EventCounter() const
{
  return histogram_EventCounter_;
}

void
EvtHistManager2_hh_bb2l::bookHistograms(TFileDirectory & dir)
{
  histogram_numElectrons_     = book1D(dir, "numElectrons",       5, -0.5,  +4.5);
  histogram_numMuons_         = book1D(dir, "numMuons",           5, -0.5,  +4.5);
  histogram_numJets_          = book1D(dir, "numJets",           20, -0.5, +19.5);
  histogram_numBJets_loose_   = book1D(dir, "numBJets_loose",    10, -0.5,  +9.5);
  histogram_numBJets_medium_  = book1D(dir, "numBJets_medium",   10, -0.5,  +9.5);

  histogram_HT_               = book1D(dir, "HT",               150,  0., 1500.);
  histogram_STMET_            = book1D(dir, "STMET",            150,  0., 1500.);

  histogram_m_Hbb_            = book1D(dir, "m_Hbb",             40,  0.,  200.);
  histogram_dR_Hbb_           = book1D(dir, "dR_Hbb",           100,  0.,    5.);
  histogram_dPhi_Hbb_         = book1D(dir, "dPhi_Hbb",          36,  0., TMath::Pi());
  histogram_pT_Hbb_           = book1D(dir, "pT_Hbb",           100,  0.,  500.);

  histogram_m_ll_             = book1D(dir, "m_ll",              40,  0.,  200.); 
  histogram_dR_ll_            = book1D(dir, "dR_ll",            100,  0.,    5.);
  histogram_dPhi_ll_          = book1D(dir, "dPhi_ll",           36,  0, TMath::Pi());
  histogram_pT_ll_            = book1D(dir, "pT_ll",            100,  0.,  500.); 

  histogram_m_HHvis_          = book1D(dir, "m_HHvis",          100,  0., 1000.);
  histogram_m_HH_             = book1D(dir, "m_HH",             150,  0., 1500.);
  histogram_m_HH_hme_         = book1D(dir, "m_HH_hme",         150,  0., 1500.);
  histogram_hmeCpuTime_       = book1D(dir, "hmeCpuTime",       200,  0.,   20.);

  histogram_vbf_jet1_pt_      = book1D(dir, "vbf_jet1_pt",       40,  0.,  200.);
  histogram_vbf_jet1_eta_     = book1D(dir, "vbf_jet1_eta",     100, -5.0,  +5.0);
  histogram_vbf_jet2_pt_      = book1D(dir, "vbf_jet2_pt",       40,  0.,  200.);
  histogram_vbf_jet2_eta_     = book1D(dir, "vbf_jet2_eta",     100, -5.0,  +5.0);
  histogram_vbf_m_jj_         = book1D(dir, "vbf_m_jj",         150,  0., 1500.);
  histogram_vbf_dEta_jj_      = book1D(dir, "vbf_dEta_jj",      100,  0.,   10.);

  histogram_EventCounter_     = book1D(dir, "EventCounter",       1, -0.5,  +0.5);
  histogram_leadconept_     = book1D(dir, "leadlepton_cone_pt",       100, 25.,  200.);
  histogram_subleadconept_     = book1D(dir, "subleadlepton_cone_pt",   100, 15., 200.);
}

void
EvtHistManager2_hh_bb2l::fillHistograms(int numElectrons,
                                        int numMuons,
                                        int numJets,
                                        int numBJets_loose,
                                        int numBJets_medium,
                                        double HT,
		                        double STMET,            
                                        double m_Hbb, double dR_Hbb, double dPhi_Hbb, double pT_Hbb,
                                        double m_ll, double dR_ll, double dPhi_ll, double pT_ll,
                                        double m_HHvis, double m_HH, 
                                        double m_HH_hme, double hmeCpuTime,
                                        double vbf_jet1_pt, double vbf_jet1_eta, double vbf_jet2_pt, double vbf_jet2_eta, double vbf_m_jj, double vbf_dEta_jj,
                                        double lead_conept, double sublead_conept,
                                        double evtWeight)
{
  const double evtWeightErr = 0.;

  fillWithOverFlow(histogram_numElectrons_,     numElectrons,      evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_leadconept_,     lead_conept,      evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_subleadconept_,     sublead_conept,      evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numMuons_,         numMuons,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJets_,          numJets,           evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_loose_,   numBJets_loose,    evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_medium_,  numBJets_medium,   evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_HT_,               HT,                evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_STMET_,            STMET,             evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_m_Hbb_,            m_Hbb,             evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dR_Hbb_,           dR_Hbb,            evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_Hbb_,         dPhi_Hbb,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_Hbb_,           pT_Hbb,            evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_m_ll_,             m_ll,              evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dR_ll_,            dR_ll,             evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_ll_,          dPhi_ll,           evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_ll_,            pT_ll,             evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_m_HHvis_,          m_HHvis,           evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_m_HH_,             m_HH,              evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_m_HH_hme_,         m_HH_hme,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_hmeCpuTime_,       hmeCpuTime,        evtWeight, evtWeightErr);

  if ( vbf_jet1_pt > 0. ) {
    fillWithOverFlow(histogram_vbf_jet1_pt_,    vbf_jet1_pt,       evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_vbf_jet1_eta_,   vbf_jet1_eta,      evtWeight, evtWeightErr);
  }
  if ( vbf_jet2_pt > 0. ) {
    fillWithOverFlow(histogram_vbf_jet2_pt_,    vbf_jet2_pt,       evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_vbf_jet2_eta_,   vbf_jet2_eta,      evtWeight, evtWeightErr);
  }
  fillWithOverFlow(histogram_vbf_m_jj_,         vbf_m_jj,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_vbf_dEta_jj_,      vbf_dEta_jj,       evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_EventCounter_,     0.,                evtWeight, evtWeightErr);
}
