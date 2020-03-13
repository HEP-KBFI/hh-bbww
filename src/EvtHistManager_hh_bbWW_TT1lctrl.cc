#include "hhAnalysis/bbww/interface/EvtHistManager_hh_bbWW_TT1lctrl.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), fillWithOverFlow2d()

#include <TMath.h> // TMath::Pi(), TMath::Sqrt
#include <TH2.h>   // TH2->Fill

EvtHistManager_hh_bbWW_TT1lctrl::EvtHistManager_hh_bbWW_TT1lctrl(const edm::ParameterSet & cfg)
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
  central_or_shiftOptions_["genMEt_pt"] = { "central" };
  central_or_shiftOptions_["genMEt_eta"] = { "central" };
  central_or_shiftOptions_["genMEt_phi"] = { "central" };
  central_or_shiftOptions_["met_pt"] = { "central" };
  central_or_shiftOptions_["met_eta"] = { "central" };
  central_or_shiftOptions_["met_phi"] = { "central" };
  central_or_shiftOptions_["deltaMEt_eta"] = { "central" };
  central_or_shiftOptions_["deltaMEt_px"] = { "central" };
  central_or_shiftOptions_["deltaMEt_py"] = { "central" };
  central_or_shiftOptions_["genHadTop_pt"] = { "central" };
  central_or_shiftOptions_["genHadTop_eta"] = { "central" };
  central_or_shiftOptions_["genHadTop_phi"] = { "central" };
  central_or_shiftOptions_["hadTop_pt"] = { "*" };
  central_or_shiftOptions_["hadTop_eta"] = { "central" };
  central_or_shiftOptions_["hadTop_phi"] = { "central" };
  central_or_shiftOptions_["genHadTop_pt_vs_hadTop_pt"] = { "central" };
  central_or_shiftOptions_["deltaHadTop_pt"] = { "central" };
  central_or_shiftOptions_["deltaHadTop_pt_vs_genHadTop_pt"] = { "central" };
  central_or_shiftOptions_["deltaHadTop_parl"] = { "central" };
  central_or_shiftOptions_["deltaHadTop_parl_vs_genHadTop_pt"] = { "central" };
  central_or_shiftOptions_["deltaHadTop_perp"] = { "central" };
  central_or_shiftOptions_["deltaHadTop_perp_vs_genHadTop_pt"] = { "central" };
  central_or_shiftOptions_["deltaHadTop_eta"] = { "central" };
  central_or_shiftOptions_["deltaHadTop_phi"] = { "central" };
  central_or_shiftOptions_["genLepTop_pt"] = { "central" };
  central_or_shiftOptions_["genLepTop_eta"] = { "central" };
  central_or_shiftOptions_["genLepTop_phi"] = { "central" };
  central_or_shiftOptions_["lepTop_pt"] = { "*" };
  central_or_shiftOptions_["lepTop_eta"] = { "central" };
  central_or_shiftOptions_["lepTop_phi"] = { "central" };
  central_or_shiftOptions_["genLepTop_pt_vs_lepTop_pt"] = { "central" };
  central_or_shiftOptions_["deltaLepTop_pt"] = { "central" };
  central_or_shiftOptions_["deltaLepTop_pt_vs_genLepTop_pt"] = { "central" };
  central_or_shiftOptions_["deltaLepTop_parl"] = { "central" };
  central_or_shiftOptions_["deltaLepTop_parl_vs_genLepTop_pt"] = { "central" };
  central_or_shiftOptions_["deltaLepTop_perp"] = { "central" };
  central_or_shiftOptions_["deltaLepTop_perp_vs_genLepTop_pt"] = { "central" };
  central_or_shiftOptions_["deltaLepTop_eta"] = { "central" };
  central_or_shiftOptions_["deltaLepTop_phi"] = { "central" };
  central_or_shiftOptions_["genTopPair_mass"] = { "central" };
  central_or_shiftOptions_["topPair_mass"] = { "central" };
  central_or_shiftOptions_["deltaTopPair_mass_vs_genTopPair_mass"] = { "central" };
  central_or_shiftOptions_["genTopPair_pt"] = { "central" };
  central_or_shiftOptions_["topPair_pt"] = { "central" };
  central_or_shiftOptions_["deltaTopPair_pt_vs_genTopPair_pt"] = { "central" };
  central_or_shiftOptions_["mT"] = { "*" };
  central_or_shiftOptions_["m_lnu"] = { "central" };
  central_or_shiftOptions_["dPhi_lnu"] = { "central" };
  central_or_shiftOptions_["pT_lnu"] = { "*" };
  central_or_shiftOptions_["m_HH_hme"] = { "central" };
  central_or_shiftOptions_["jetAK8_Wjj_dR_lepton"] = { "central" };
  central_or_shiftOptions_["vbf_m_jj"] = { "central" };
  central_or_shiftOptions_["vbf_dEta_jj"] = { "central" };
  central_or_shiftOptions_["EventCounter"] = { "*" };
}

const TH1 *
EvtHistManager_hh_bbWW_TT1lctrl::getHistogram_EventCounter() const
{
  return histogram_EventCounter_;
}

void
EvtHistManager_hh_bbWW_TT1lctrl::bookHistograms(TFileDirectory & dir)
{
  histogram_numElectrons_         = book1D(dir, "numElectrons",         "numElectrons",             5,   -0.5,  +4.5);
  histogram_numMuons_             = book1D(dir, "numMuons",             "numMuons",                 5,   -0.5,  +4.5);
  histogram_numJets_              = book1D(dir, "numJets",              "numJets",                 20,   -0.5, +19.5);
  histogram_numBJets_loose_       = book1D(dir, "numBJets_loose",       "numBJets_loose",          10,   -0.5,  +9.5);
  histogram_numBJets_medium_      = book1D(dir, "numBJets_medium",      "numBJets_medium",         10,   -0.5,  +9.5);
  histogram_numJetsAK8_Hbb_       = book1D(dir, "numJetsAK8_Hbb",       "numJetsAK8_Hbb",           4,   -0.5,  +3.5);
  histogram_numJetsAK8_Wjj_       = book1D(dir, "numJetsAK8_Wjj",       "numJetsAK8_Wjj",           4,   -0.5,  +3.5);
 
  histogram_HT_                   = book1D(dir, "HT",                   "HT",                     150,    0., 1500.);
  histogram_STMET_                = book1D(dir, "STMET",                "STMET",                  150,    0., 1500.);

  histogram_genMEt_pt_            = book1D(dir, "genMEt_pt",            "genMEt_pt",              100,    0.,  500.);
  histogram_genMEt_eta_           = book1D(dir, "genMEt_eta",           "genMEt_eta",             100,   -5.,   +5.);
  histogram_genMEt_phi_           = book1D(dir, "genMEt_phi",           "genMEt_phi",              36, -TMath::Pi(), +TMath::Pi());
  histogram_recMEt_pt_            = book1D(dir, "met_pt",               "met_pt",                 100,    0.,  500.);
  histogram_recMEt_eta_           = book1D(dir, "met_eta",              "met_eta",                100,   -5.,   +5.);
  histogram_recMEt_phi_           = book1D(dir, "met_phi",              "met_phi",                 36, -TMath::Pi(), +TMath::Pi());
  histogram_deltaMEt_eta_         = book1D(dir, "deltaMEt_eta",         "deltaMEt_eta",           100,   -5.,   +5.);
  histogram_deltaMEt_px_          = book1D(dir, "deltaMEt_px",          "deltaMEt_px",             40, -100., +100.);
  histogram_deltaMEt_py_          = book1D(dir, "deltaMEt_py",          "deltaMEt_py",             40, -100., +100.);

  // CV: binning in top quark pT taken from AN-2015/309 (TOP-16-001)
  int numBins_pt = 6;
  float binning_pt[numBins_pt + 1] = { 0., 65., 125., 200., 290., 400., 550. } ;

  histogram_genHadTop_pt_         = book1D(dir, "genHadTop_pt",         "genHadTop_pt",           100,    0.,  500.);
  histogram_genHadTop_eta_        = book1D(dir, "genHadTop_eta",        "genHadTop_eta",          100,   -5.,   +5.);
  histogram_genHadTop_phi_        = book1D(dir, "genHadTop_phi",        "genHadTop_phi",           36, -TMath::Pi(), +TMath::Pi());
  histogram_hadTop_pt_            = book1D(dir, "hadTop_pt",            "hadTop_pt",              100,    0.,  500.);
  histogram_hadTop_eta_           = book1D(dir, "hadTop_eta",           "hadTop_eta",             100,   -5.,   +5.);
  histogram_hadTop_phi_           = book1D(dir, "hadTop_phi",           "hadTop_phi",              36, -TMath::Pi(), +TMath::Pi());
  histogram_genHadTop_pt_vs_hadTop_pt_        = book2D(dir, "genHadTop_pt_vs_hadTop_pt",        "genHadTop_pt_vs_hadTop_pt", numBins_pt, binning_pt, numBins_pt, binning_pt);
  histogram_deltaHadTop_pt_       = book1D(dir, "deltaHadTop_pt",       "deltaHadTop_pt",          40, -100., +100.);
  histogram_deltaHadTop_pt_vs_genHadTop_pt_   = book2D(dir, "deltaHadTop_pt_vs_genHadTop_pt",   "deltaHadTop_pt_vs_genHadTop_pt",   10, 0., 250., 30, -75., +75.);
  histogram_deltaHadTop_parl_     = book1D(dir, "deltaHadTop_parl",     "deltaHadTop_parl",        40, -100., +100.);
  histogram_deltaHadTop_parl_vs_genHadTop_pt_ = book2D(dir, "deltaHadTop_parl_vs_genHadTop_pt", "deltaHadTop_parl_vs_genHadTop_pt", 10, 0., 250., 30, -75., +75.);
  histogram_deltaHadTop_perp_     = book1D(dir, "deltaHadTop_perp",     "deltaHadTop_perp",        40, -100., +100.);
  histogram_deltaHadTop_perp_vs_genHadTop_pt_ = book2D(dir, "deltaHadTop_perp_vs_genHadTop_pt", "deltaHadTop_perp_vs_genHadTop_pt", 10, 0., 250., 30, -75., +75.);
  histogram_deltaHadTop_eta_      = book1D(dir, "deltaHadTop_eta",      "deltaHadTop_eta",        100,   -5.,   +5.);
  histogram_deltaHadTop_phi_      = book1D(dir, "deltaHadTop_phi",      "deltaHadTop_phi",         36,    0., 0.2*TMath::Pi());

  histogram_genLepTop_pt_         = book1D(dir, "genLepTop_pt",         "genLepTop_pt",           100,    0.,  500.);
  histogram_genLepTop_eta_        = book1D(dir, "genLepTop_eta",        "genLepTop_eta",          100,   -5.,   +5.);
  histogram_genLepTop_phi_        = book1D(dir, "genLepTop_phi",        "genLepTop_phi",           36, -TMath::Pi(), +TMath::Pi());
  histogram_lepTop_pt_            = book1D(dir, "lepTop_pt",            "lepTop_pt",              100,    0.,  500.);
  histogram_lepTop_eta_           = book1D(dir, "lepTop_eta",           "lepTop_eta",             100,   -5.,   +5.);
  histogram_lepTop_phi_           = book1D(dir, "lepTop_phi",           "lepTop_phi",              36, -TMath::Pi(), +TMath::Pi());
  histogram_genLepTop_pt_vs_lepTop_pt_        = book2D(dir, "genLepTop_pt_vs_lepTop_pt",        "genLepTop_pt_vs_lepTop_pt", numBins_pt, binning_pt, numBins_pt, binning_pt);
  histogram_deltaLepTop_pt_       = book1D(dir, "deltaLepTop_pt",       "deltaLepTop_pt",          40, -100., +100.);
  histogram_deltaLepTop_pt_vs_genLepTop_pt_   = book2D(dir, "deltaLepTop_pt_vs_genLepTop_pt",   "deltaLepTop_pt_vs_genLepTop_pt",   10, 0., 250., 30, -75., +75.);
  histogram_deltaLepTop_parl_     = book1D(dir, "deltaLepTop_parl",     "deltaLepTop_parl",        40, -100., +100.);
  histogram_deltaLepTop_parl_vs_genLepTop_pt_ = book2D(dir, "deltaLepTop_parl_vs_genLepTop_pt", "deltaLepTop_parl_vs_genLepTop_pt", 10, 0., 250., 30, -75., +75.);
  histogram_deltaLepTop_perp_     = book1D(dir, "deltaLepTop_perp",     "deltaLepTop_perp",        40, -100., +100.);
  histogram_deltaLepTop_perp_vs_genLepTop_pt_ = book2D(dir, "deltaLepTop_perp_vs_genLepTop_pt", "deltaLepTop_perp_vs_genLepTop_pt", 10, 0., 250., 30, -75., +75.);
  histogram_deltaLepTop_eta_      = book1D(dir, "deltaLepTop_eta",      "deltaLepTop_eta",        100,   -5.,   +5.);
  histogram_deltaLepTop_phi_      = book1D(dir, "deltaLepTop_phi",      "deltaLepTop_phi",         36,    0., 0.2*TMath::Pi());

  histogram_genTopPair_mass_      = book1D(dir, "genTopPair_mass",      "genTopPair_mass",        100,    0., 1000.);
  histogram_topPair_mass_         = book1D(dir, "topPair_mass",         "topPair_mass",           100,    0., 1000.);
  histogram_deltaTopPair_mass_vs_genTopPair_mass_ = book2D(dir, "deltaTopPair_mass_vs_genTopPair_mass", "deltaTopPair_mass_vs_genTopPair_mass", 10, 0., 500., 30, -150, +150.);
  histogram_genTopPair_pt_        = book1D(dir, "genTopPair_pt",        "genTopPair_pt",          100,    0., 1000.);
  histogram_topPair_pt_           = book1D(dir, "topPair_pt",           "topPair_pt",             100,    0., 1000.);
  histogram_deltaTopPair_pt_vs_genTopPair_pt_ = book2D(dir, "deltaTopPair_pt_vs_genTopPair_pt", "deltaTopPair_pt_vs_genTopPair_pt", 10, 0., 500., 30, -150, +150.);

  histogram_mT_                   = book1D(dir, "mT",                   "mT",                      30,  0.,  150.); 
  histogram_m_lnu_                = book1D(dir, "m_lnu",                "m_lnu",                   50,  0.,  250.); 
  histogram_dPhi_lnu_             = book1D(dir, "dPhi_lnu",             "dPhi_lnu",                36, -TMath::Pi(), +TMath::Pi());
  histogram_pT_lnu_               = book1D(dir, "pT_lnu",               "pT_lnu",                 100,  0.,  500.); 

  histogram_m_HH_hme_             = book1D(dir, "m_HH_hme",             "m_HH_hme",               150,  0., 1500.);

  histogram_jetAK8_Wjj_dR_lepton_ = book1D(dir, "jetAK8_Wjj_dR_lepton", "jetAK8_Wjj_dR_lepton",    50., 0.,    5.);

  histogram_vbf_m_jj_             = book1D(dir, "vbf_m_jj",             "vbf_m_jj",               150,  0., 1500.);
  histogram_vbf_dEta_jj_          = book1D(dir, "vbf_dEta_jj",          "vbf_dEta_jj",            100,  0.,   10.);

  histogram_EventCounter_         = book1D(dir, "EventCounter",         "EventCounter",             1, -0.5,  +0.5);
}

namespace
{
  // compute projection of (metPx, metPy) in direction parallel to vector q in transverse plane,
  // cf. Eq. (4) in CMS AN-2011/459 v7
  double comp_metParl(double qX, double qY, double metPx, double metPy)
  {
    double metParl = 0.;
    double qT = TMath::Sqrt(qX*qX + qY*qY);
    if ( qT > 0. )
    {
      metParl = (qX*metPx + qX*metPy)/qT;
    }
    return metParl;
  }

  // compute projection of (metPx, metPy) in direction perpendicular to vector q in transverse plane,
  // cf. Eq. (5) in CMS AN-2011/459 v7
  double comp_metPerp(double qX, double qY, double metPx, double metPy)
  {
    double metPerp = 0.;
    double qT = TMath::Sqrt(qX*qX + qY*qY);
    if ( qT > 0. )
    {
      metPerp = (qX*metPy - qY*metPx)/qT;
    }
    return metPerp;
  }
}

void
EvtHistManager_hh_bbWW_TT1lctrl::fillHistograms(int numElectrons,
				  	        int numMuons,
					        int numJets,
					        int numBJets_loose,
					        int numBJets_medium,
                                                int numJetsAK8_Hbb, 
                                                int numJetsAK8_Wjj, 
					        double HT,
					        double STMET,
                                                const Particle::LorentzVector& genMEtP4, const Particle::LorentzVector& metP4,
                                                const Particle::LorentzVector& genTopQuarkP4_hadTop, bool isGenMatched_hadTop, const Particle::LorentzVector& topQuarkP4_hadTop,
                                                const Particle::LorentzVector& genTopQuarkP4_lepTop, bool isGenMatched_lepTop, const Particle::LorentzVector& topQuarkP4_lepTop,
		                                double mT, double m_lnu, double dPhi_lnu, double pT_lnu,
                                                double m_HH_hme,
                                                double jetAK8_Wjj_dR_lepton, 
					        double vbf_m_jj, double vbf_dEta_jj,
					        double evtWeight)
{
  const double evtWeightErr = 0.;

  fillWithOverFlow(histogram_numElectrons_,           numElectrons,                 evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numMuons_,               numMuons,                     evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJets_,                numJets,                      evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_loose_,         numBJets_loose,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_medium_,        numBJets_medium,              evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJetsAK8_Hbb_,         numJetsAK8_Hbb,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJetsAK8_Wjj_,         numJetsAK8_Wjj,               evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_HT_,                     HT,                           evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_STMET_,                  STMET,                        evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_genMEt_pt_,              genMEtP4.pt(),                evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_genMEt_eta_,             genMEtP4.eta(),               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_genMEt_phi_,             genMEtP4.phi(),               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_recMEt_pt_,              metP4.pt(),                   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_recMEt_eta_,             metP4.eta(),                  evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_recMEt_phi_,             metP4.phi(),                  evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_deltaMEt_eta_,           metP4.eta() - genMEtP4.eta(), evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_deltaMEt_px_,            metP4.px() - genMEtP4.px(),   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_deltaMEt_py_,            metP4.py() - genMEtP4.py(),   evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_genHadTop_pt_,           genTopQuarkP4_hadTop.pt(),    evtWeight, evtWeightErr);   
  fillWithOverFlow(histogram_genHadTop_eta_,          genTopQuarkP4_hadTop.eta(),   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_genHadTop_phi_,          genTopQuarkP4_hadTop.phi(),   evtWeight, evtWeightErr);        
  fillWithOverFlow(histogram_hadTop_pt_,              topQuarkP4_hadTop.pt(),       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_hadTop_eta_,             topQuarkP4_hadTop.eta(),      evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_hadTop_phi_,             topQuarkP4_hadTop.phi(),      evtWeight, evtWeightErr);  
  if ( isGenMatched_hadTop )
  {
    histogram_genHadTop_pt_vs_hadTop_pt_->Fill(topQuarkP4_hadTop.pt(), genTopQuarkP4_hadTop.pt(), evtWeight);
    double deltaHadTop_pt = topQuarkP4_hadTop.pt() - genTopQuarkP4_hadTop.pt();
    fillWithOverFlow(histogram_deltaHadTop_pt_, deltaHadTop_pt, evtWeight, evtWeightErr);
    fillWithOverFlow2d(histogram_deltaHadTop_pt_vs_genHadTop_pt_, genTopQuarkP4_hadTop.pt(), deltaHadTop_pt, evtWeight, evtWeightErr);
    double deltaHadTop_px = topQuarkP4_hadTop.px() - genTopQuarkP4_hadTop.px();
    double deltaHadTop_py = topQuarkP4_hadTop.py() - genTopQuarkP4_hadTop.py();
    double deltaHadTop_parl = comp_metParl(genTopQuarkP4_hadTop.px(), genTopQuarkP4_hadTop.py(), deltaHadTop_px, deltaHadTop_py);
    fillWithOverFlow(histogram_deltaHadTop_parl_, deltaHadTop_parl, evtWeight, evtWeightErr);  
    fillWithOverFlow2d(histogram_deltaHadTop_parl_vs_genHadTop_pt_, genTopQuarkP4_hadTop.pt(), deltaHadTop_parl, evtWeight, evtWeightErr);
    double deltaHadTop_perp = comp_metPerp(genTopQuarkP4_hadTop.px(), genTopQuarkP4_hadTop.py(), deltaHadTop_px, deltaHadTop_py);
    fillWithOverFlow(histogram_deltaHadTop_perp_, deltaHadTop_perp, evtWeight, evtWeightErr);  
    fillWithOverFlow2d(histogram_deltaHadTop_perp_vs_genHadTop_pt_, genTopQuarkP4_hadTop.pt(), deltaHadTop_perp, evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_deltaHadTop_eta_, topQuarkP4_hadTop.eta() - genTopQuarkP4_hadTop.eta(), evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_deltaHadTop_phi_, topQuarkP4_hadTop.phi() - genTopQuarkP4_hadTop.phi(), evtWeight, evtWeightErr);
  }

  fillWithOverFlow(histogram_genLepTop_pt_,           genTopQuarkP4_lepTop.pt(),    evtWeight, evtWeightErr);   
  fillWithOverFlow(histogram_genLepTop_eta_,          genTopQuarkP4_lepTop.eta(),   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_genLepTop_phi_,          genTopQuarkP4_lepTop.phi(),   evtWeight, evtWeightErr);        
  fillWithOverFlow(histogram_lepTop_pt_,              topQuarkP4_lepTop.pt(),       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lepTop_eta_,             topQuarkP4_lepTop.eta(),      evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lepTop_phi_,             topQuarkP4_lepTop.phi(),      evtWeight, evtWeightErr);
  if ( isGenMatched_lepTop )
  {
    histogram_genLepTop_pt_vs_lepTop_pt_->Fill(topQuarkP4_lepTop.pt(), genTopQuarkP4_lepTop.pt(), evtWeight);
    double deltaLepTop_pt = topQuarkP4_lepTop.pt() - genTopQuarkP4_lepTop.pt();
    fillWithOverFlow(histogram_deltaLepTop_pt_,       deltaLepTop_pt,               evtWeight, evtWeightErr);
    fillWithOverFlow2d(histogram_deltaLepTop_pt_vs_genLepTop_pt_, genTopQuarkP4_lepTop.pt(), deltaLepTop_pt, evtWeight, evtWeightErr);
    double deltaLepTop_px = topQuarkP4_lepTop.px() - genTopQuarkP4_lepTop.px();
    double deltaLepTop_py = topQuarkP4_lepTop.py() - genTopQuarkP4_lepTop.py();
    double deltaLepTop_parl = comp_metParl(genTopQuarkP4_lepTop.px(), genTopQuarkP4_lepTop.py(), deltaLepTop_px, deltaLepTop_py);
    fillWithOverFlow(histogram_deltaLepTop_parl_,     deltaLepTop_parl,             evtWeight, evtWeightErr);  
    fillWithOverFlow2d(histogram_deltaLepTop_parl_vs_genLepTop_pt_, genTopQuarkP4_lepTop.pt(), deltaLepTop_parl, evtWeight, evtWeightErr);
    double deltaLepTop_perp = comp_metPerp(genTopQuarkP4_lepTop.px(), genTopQuarkP4_lepTop.py(), deltaLepTop_px, deltaLepTop_py);
    fillWithOverFlow(histogram_deltaLepTop_perp_,     deltaLepTop_perp,             evtWeight, evtWeightErr);  
    fillWithOverFlow2d(histogram_deltaLepTop_perp_vs_genLepTop_pt_, genTopQuarkP4_lepTop.pt(), deltaLepTop_perp, evtWeight, evtWeightErr);
    double deltaLepTop_eta = topQuarkP4_lepTop.eta() - genTopQuarkP4_lepTop.eta();
    fillWithOverFlow(histogram_deltaLepTop_eta_,      deltaLepTop_eta,              evtWeight, evtWeightErr);
    double deltaLepTop_phi = topQuarkP4_lepTop.phi() - genTopQuarkP4_lepTop.phi();
    fillWithOverFlow(histogram_deltaLepTop_phi_,      deltaLepTop_phi,              evtWeight, evtWeightErr);
  }

  Particle::LorentzVector genTopPairP4 = genTopQuarkP4_hadTop + genTopQuarkP4_lepTop;
  Particle::LorentzVector topPairP4 = topQuarkP4_hadTop + topQuarkP4_lepTop;
  fillWithOverFlow(histogram_genTopPair_mass_,        genTopPairP4.mass(),          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_topPair_mass_,           topPairP4.mass(),             evtWeight, evtWeightErr);
  fillWithOverFlow2d(histogram_deltaTopPair_mass_vs_genTopPair_mass_, genTopPairP4.mass(), topPairP4.mass() - genTopPairP4.mass(), evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_genTopPair_pt_,          genTopPairP4.pt(),            evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_topPair_pt_,             topPairP4.pt(),               evtWeight, evtWeightErr);
  fillWithOverFlow2d(histogram_deltaTopPair_pt_vs_genTopPair_pt_, genTopPairP4.pt(), topPairP4.pt() - genTopPairP4.pt(), evtWeight, evtWeightErr);
  
  fillWithOverFlow(histogram_mT_,                     mT,                           evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_m_lnu_,                  m_lnu,                        evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_lnu_,               dPhi_lnu,                     evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_lnu_,                 pT_lnu,                       evtWeight, evtWeightErr);

  if ( m_HH_hme > 0. ) {
    fillWithOverFlow(histogram_m_HH_hme_,             m_HH_hme,                     evtWeight, evtWeightErr);    
  }

  if ( jetAK8_Wjj_dR_lepton >= 0. ) {
    fillWithOverFlow(histogram_jetAK8_Wjj_dR_lepton_, jetAK8_Wjj_dR_lepton,         evtWeight, evtWeightErr);    
  }

  fillWithOverFlow(histogram_vbf_m_jj_,               vbf_m_jj,                     evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_vbf_dEta_jj_,            vbf_dEta_jj,                  evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_EventCounter_,           0.,                           evtWeight, evtWeightErr);
}
