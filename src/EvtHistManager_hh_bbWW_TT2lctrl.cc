#include "hhAnalysis/bbww/interface/EvtHistManager_hh_bbWW_TT2lctrl.h"

#include "DataFormats/Math/interface/deltaR.h"   // deltaR
#include "DataFormats/Math/interface/deltaPhi.h" // deltaPhi

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), fillWithOverFlow2d()

#include <TMath.h> // TMath::Pi(), TMath::Sqrt, TMath::Abs
#include <TH2.h>   // TH2->Fill

EvtHistManager_hh_bbWW_TT2lctrl::EvtHistManager_hh_bbWW_TT2lctrl(const edm::ParameterSet & cfg)
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
  central_or_shiftOptions_["genTop_pt"] = { "central" };
  central_or_shiftOptions_["genTop_eta"] = { "central" };
  central_or_shiftOptions_["genTop_phi"] = { "central" };
  central_or_shiftOptions_["top_pt"] = { "*" };
  central_or_shiftOptions_["top_eta"] = { "central" };
  central_or_shiftOptions_["top_phi"] = { "central" };
  central_or_shiftOptions_["genTop_pt_vs_top_pt"] = { "central" };
  central_or_shiftOptions_["deltaTop_pt"] = { "central" };
  central_or_shiftOptions_["deltaTop_pt_vs_genTop_pt"] = { "central" };
  central_or_shiftOptions_["deltaTop_parl"] = { "central" };
  central_or_shiftOptions_["deltaTop_parl_vs_genTop_pt"] = { "central" };
  central_or_shiftOptions_["deltaTop_perp"] = { "central" };
  central_or_shiftOptions_["deltaTop_perp_vs_genTop_pt"] = { "central" };
  central_or_shiftOptions_["deltaTop_eta"] = { "central" };
  central_or_shiftOptions_["deltaTop_phi"] = { "central" };
  central_or_shiftOptions_["genAntiTop_pt"] = { "central" };
  central_or_shiftOptions_["genAntiTop_eta"] = { "central" };
  central_or_shiftOptions_["genAntiTop_phi"] = { "central" };
  central_or_shiftOptions_["antiTop_pt"] = { "*" };
  central_or_shiftOptions_["antiTop_eta"] = { "central" };
  central_or_shiftOptions_["antiTop_phi"] = { "central" };
  central_or_shiftOptions_["genAntiTop_pt_vs_antiTop_pt"] = { "central" };
  central_or_shiftOptions_["deltaAntiTop_pt"] = { "central" };
  central_or_shiftOptions_["deltaAntiTop_pt_vs_genAntiTop_pt"] = { "central" };
  central_or_shiftOptions_["deltaAntiTop_parl"] = { "central" };
  central_or_shiftOptions_["deltaAntiTop_parl_vs_genAntiTop_pt"] = { "central" };
  central_or_shiftOptions_["deltaAntiTop_perp"] = { "central" };
  central_or_shiftOptions_["deltaAntiTop_perp_vs_genAntiTop_pt"] = { "central" };
  central_or_shiftOptions_["deltaAntiTop_eta"] = { "central" };
  central_or_shiftOptions_["deltaAntiTop_phi"] = { "central" };
  central_or_shiftOptions_["genMtt"] = { "central" };
  central_or_shiftOptions_["mtt"] = { "central" };
  central_or_shiftOptions_["deltaMtt_vs_genMtt"] = { "central" };
  central_or_shiftOptions_["m_ll"] = { "central" };
  central_or_shiftOptions_["dR_ll"] = { "central" };
  central_or_shiftOptions_["dPhi_ll"] = { "central" };
  central_or_shiftOptions_["dEta_ll"] = { "central" };
  central_or_shiftOptions_["pT_ll"] = { "central" };
  central_or_shiftOptions_["m_HH_hme"] = { "central" };
  central_or_shiftOptions_["vbf_m_jj"] = { "central" };
  central_or_shiftOptions_["vbf_dEta_jj"] = { "central" };
  central_or_shiftOptions_["EventCounter"] = { "*" };
}

const TH1 *
EvtHistManager_hh_bbWW_TT2lctrl::getHistogram_EventCounter() const
{
  return histogram_EventCounter_;
}

void
EvtHistManager_hh_bbWW_TT2lctrl::bookHistograms(TFileDirectory & dir)
{
  histogram_numElectrons_         = book1D(dir, "numElectrons",         "numElectrons",             5,   -0.5,  +4.5);
  histogram_numMuons_             = book1D(dir, "numMuons",             "numMuons",                 5,   -0.5,  +4.5);
  histogram_numJets_              = book1D(dir, "numJets",              "numJets",                 20,   -0.5, +19.5);
  histogram_numBJets_loose_       = book1D(dir, "numBJets_loose",       "numBJets_loose",          10,   -0.5,  +9.5);
  histogram_numBJets_medium_      = book1D(dir, "numBJets_medium",      "numBJets_medium",         10,   -0.5,  +9.5);
  histogram_numJetsAK8_Hbb_       = book1D(dir, "numJetsAK8_Hbb",       "numJetsAK8_Hbb",           4,   -0.5,  +3.5);
 
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

  histogram_genTop_pt_            = book1D(dir, "genTop_pt",            "genTop_pt",              100,    0.,  500.);
  histogram_genTop_eta_           = book1D(dir, "genTop_eta",           "genTop_eta",             100,   -5.,   +5.);
  histogram_genTop_phi_           = book1D(dir, "genTop_phi",           "genTop_phi",              36, -TMath::Pi(), +TMath::Pi());
  histogram_top_pt_               = book1D(dir, "top_pt",               "top_pt",                 100,    0.,  500.);
  histogram_top_eta_              = book1D(dir, "top_eta",              "top_eta",                100,   -5.,   +5.);
  histogram_top_phi_              = book1D(dir, "top_phi",              "top_phi",                 36, -TMath::Pi(), +TMath::Pi());
  histogram_genTop_pt_vs_top_pt_        = book2D(dir, "genTop_pt_vs_top_pt",        "genTop_pt_vs_top_pt", numBins_pt, binning_pt, numBins_pt, binning_pt);
  histogram_deltaTop_pt_          = book1D(dir, "deltaTop_pt",          "deltaTop_pt",             40, -100., +100.);
  histogram_deltaTop_pt_vs_genTop_pt_   = book2D(dir, "deltaTop_pt_vs_genTop_pt",   "deltaTop_pt_vs_genTop_pt",   10, 0., 250., 30, -75., +75.);
  histogram_deltaTop_parl_        = book1D(dir, "deltaTop_parl",        "deltaTop_parl",           40, -100., +100.);
  histogram_deltaTop_parl_vs_genTop_pt_ = book2D(dir, "deltaTop_parl_vs_genTop_pt", "deltaTop_parl_vs_genTop_pt", 10, 0., 250., 30, -75., +75.);
  histogram_deltaTop_perp_        = book1D(dir, "deltaTop_perp",        "deltaTop_perp",           40, -100., +100.);
  histogram_deltaTop_perp_vs_genTop_pt_ = book2D(dir, "deltaTop_perp_vs_genTop_pt", "deltaTop_perp_vs_genTop_pt", 10, 0., 250., 30, -75., +75.);
  histogram_deltaTop_eta_         = book1D(dir, "deltaTop_eta",         "deltaTop_eta",           100,   -5.,   +5.);
  histogram_deltaTop_phi_         = book1D(dir, "deltaTop_phi",         "deltaTop_phi",            36,    0., 0.2*TMath::Pi());

  histogram_genAntiTop_pt_        = book1D(dir, "genAntiTop_pt",        "genAntiTop_pt",          100,    0.,  500.);
  histogram_genAntiTop_eta_       = book1D(dir, "genAntiTop_eta",       "genAntiTop_eta",         100,   -5.,   +5.);
  histogram_genAntiTop_phi_       = book1D(dir, "genAntiTop_phi",       "genAntiTop_phi",          36, -TMath::Pi(), +TMath::Pi());
  histogram_antiTop_pt_           = book1D(dir, "antiTop_pt",           "antiTop_pt",             100,    0.,  500.);
  histogram_antiTop_eta_          = book1D(dir, "antiTop_eta",          "antiTop_eta",            100,   -5.,   +5.);
  histogram_antiTop_phi_          = book1D(dir, "antiTop_phi",          "antiTop_phi",             36, -TMath::Pi(), +TMath::Pi());
  histogram_genAntiTop_pt_vs_antiTop_pt_        = book2D(dir, "genAntiTop_pt_vs_antiTop_pt",        "genAntiTop_pt_vs_antiTop_pt", numBins_pt, binning_pt, numBins_pt, binning_pt);
  histogram_deltaAntiTop_pt_      = book1D(dir, "deltaAntiTop_pt",      "deltaAntiTop_pt",         40, -100., +100.);
  histogram_deltaAntiTop_pt_vs_genAntiTop_pt_   = book2D(dir, "deltaAntiTop_pt_vs_genAntiTop_pt",   "deltaAntiTop_pt_vs_genAntiTop_pt",   10, 0., 250., 30, -75., +75.);
  histogram_deltaAntiTop_parl_    = book1D(dir, "deltaAntiTop_parl",    "deltaAntiTop_parl",       40, -100., +100.);
  histogram_deltaAntiTop_parl_vs_genAntiTop_pt_ = book2D(dir, "deltaAntiTop_parl_vs_genAntiTop_pt", "deltaAntiTop_parl_vs_genAntiTop_pt", 10, 0., 250., 30, -75., +75.);
  histogram_deltaAntiTop_perp_    = book1D(dir, "deltaAntiTop_perp",    "deltaAntiTop_perp",       40, -100., +100.);
  histogram_deltaAntiTop_perp_vs_genAntiTop_pt_ = book2D(dir, "deltaAntiTop_perp_vs_genAntiTop_pt", "deltaAntiTop_perp_vs_genAntiTop_pt", 10, 0., 250., 30, -75., +75.);
  histogram_deltaAntiTop_eta_     = book1D(dir, "deltaAntiTop_eta",     "deltaAntiTop_eta",       100,   -5.,   +5.);
  histogram_deltaAntiTop_phi_     = book1D(dir, "deltaAntiTop_phi",     "deltaAntiTop_phi",        36,    0., 0.2*TMath::Pi());

  histogram_genMtt_               = book1D(dir, "genMtt",               "genMtt",                 100,    0., 1000.);
  histogram_mtt_                  = book1D(dir, "mtt",                  "mtt",                    100,    0., 1000.);
  histogram_deltaMtt_vs_genMtt_   = book2D(dir, "deltaMtt_vs_genMtt", "deltaMtt_vs_genMtt", 10, 0., 500., 30, -150, +150.);

  histogram_m_ll_                 = book1D(dir, "m_ll",                 "m_ll",                    40,    0.,  200.);
  histogram_dR_ll_                = book1D(dir, "dR_ll",                "dR_ll",                  100,    0.,    5.);
  histogram_dPhi_ll_              = book1D(dir, "dPhi_ll",              "dPhi_ll",                 36,    0, TMath::Pi());
  histogram_dEta_ll_              = book1D(dir, "dEta_ll",              "dEta_ll",                 50,    0,     5.);
  histogram_pT_ll_                = book1D(dir, "pT_ll",                "pT_ll",                  100,    0.,  500.);

  histogram_m_HH_hme_             = book1D(dir, "m_HH_hme",             "m_HH_hme",               150,    0., 1500.);

  histogram_vbf_m_jj_             = book1D(dir, "vbf_m_jj",             "vbf_m_jj",               150,    0., 1500.);
  histogram_vbf_dEta_jj_          = book1D(dir, "vbf_dEta_jj",          "vbf_dEta_jj",            100,    0.,   10.);

  histogram_EventCounter_         = book1D(dir, "EventCounter",         "EventCounter",             1,   -0.5,  +0.5);
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
EvtHistManager_hh_bbWW_TT2lctrl::fillHistograms(int numElectrons,
				  	        int numMuons,
					        int numJets,
					        int numBJets_loose,
					        int numBJets_medium,
                                                int numJetsAK8_Hbb, 
					        double HT,
					        double STMET,
                                                bool isValid_topKinReco, 
                                                const Particle::LorentzVector& genMEtP4, const Particle::LorentzVector& metP4,
                                                const Particle::LorentzVector& genTopQuarkP4_top, bool isGenMatched_top, const Particle::LorentzVector& topQuarkP4_top,
                                                const Particle::LorentzVector& genTopQuarkP4_antitop, bool isGenMatched_antitop, const Particle::LorentzVector& topQuarkP4_antitop,
		                                const Particle::LorentzVector& selLeptonP4_lead, const Particle::LorentzVector& selLeptonP4_sublead,
                                                double m_HH_hme,
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

  fillWithOverFlow(histogram_HT_,                     HT,                           evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_STMET_,                  STMET,                        evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_genMEt_pt_,              genMEtP4.pt(),                evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_genMEt_eta_,             genMEtP4.eta(),               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_genMEt_phi_,             genMEtP4.phi(),               evtWeight, evtWeightErr);
  if ( isValid_topKinReco ) 
  {
    fillWithOverFlow(histogram_recMEt_pt_,            metP4.pt(),                   evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_recMEt_eta_,           metP4.eta(),                  evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_recMEt_phi_,           metP4.phi(),                  evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_deltaMEt_eta_,         metP4.eta() - genMEtP4.eta(), evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_deltaMEt_px_,          metP4.px() - genMEtP4.px(),   evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_deltaMEt_py_,          metP4.py() - genMEtP4.py(),   evtWeight, evtWeightErr);
  }

  fillWithOverFlow(histogram_genTop_pt_,              genTopQuarkP4_top.pt(),       evtWeight, evtWeightErr);   
  fillWithOverFlow(histogram_genTop_eta_,             genTopQuarkP4_top.eta(),      evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_genTop_phi_,             genTopQuarkP4_top.phi(),      evtWeight, evtWeightErr);        
  if ( isValid_topKinReco )
  {
    fillWithOverFlow(histogram_top_pt_,               topQuarkP4_top.pt(),          evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_top_eta_,              topQuarkP4_top.eta(),         evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_top_phi_,              topQuarkP4_top.phi(),         evtWeight, evtWeightErr);
    if ( isGenMatched_top )
    {
      histogram_genTop_pt_vs_top_pt_->Fill(topQuarkP4_top.pt(), genTopQuarkP4_top.pt(), evtWeight);
      double deltaTop_pt = topQuarkP4_top.pt() - genTopQuarkP4_top.pt();
      fillWithOverFlow(histogram_deltaTop_pt_,        deltaTop_pt,                  evtWeight, evtWeightErr);
      fillWithOverFlow2d(histogram_deltaTop_pt_vs_genTop_pt_, genTopQuarkP4_top.pt(), deltaTop_pt, evtWeight, evtWeightErr);
      double deltaTop_px = topQuarkP4_top.px() - genTopQuarkP4_top.px();
      double deltaTop_py = topQuarkP4_top.py() - genTopQuarkP4_top.py();
      double deltaTop_parl = comp_metParl(genTopQuarkP4_top.px(), genTopQuarkP4_top.py(), deltaTop_px, deltaTop_py);
      fillWithOverFlow(histogram_deltaTop_parl_,      deltaTop_parl,                evtWeight, evtWeightErr);  
      fillWithOverFlow2d(histogram_deltaTop_parl_vs_genTop_pt_, genTopQuarkP4_top.pt(), deltaTop_parl, evtWeight, evtWeightErr);
      double deltaTop_perp = comp_metPerp(genTopQuarkP4_top.px(), genTopQuarkP4_top.py(), deltaTop_px, deltaTop_py);
      fillWithOverFlow(histogram_deltaTop_perp_,      deltaTop_perp,                evtWeight, evtWeightErr);  
      fillWithOverFlow2d(histogram_deltaTop_perp_vs_genTop_pt_, genTopQuarkP4_top.pt(), deltaTop_perp, evtWeight, evtWeightErr);
      double deltaTop_eta = topQuarkP4_top.eta() - genTopQuarkP4_top.eta();
      fillWithOverFlow(histogram_deltaTop_eta_,       deltaTop_eta,                 evtWeight, evtWeightErr);
      double deltaTop_phi = topQuarkP4_top.phi() - genTopQuarkP4_top.phi();
      fillWithOverFlow(histogram_deltaTop_phi_,       deltaTop_phi,                 evtWeight, evtWeightErr);
    }
  }

  fillWithOverFlow(histogram_genAntiTop_pt_,          genTopQuarkP4_antitop.pt(),   evtWeight, evtWeightErr);   
  fillWithOverFlow(histogram_genAntiTop_eta_,         genTopQuarkP4_antitop.eta(),  evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_genAntiTop_phi_,         genTopQuarkP4_antitop.phi(),  evtWeight, evtWeightErr);        
  if ( isValid_topKinReco )
  {
    fillWithOverFlow(histogram_antiTop_pt_,           topQuarkP4_antitop.pt(),      evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_antiTop_eta_,          topQuarkP4_antitop.eta(),     evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_antiTop_phi_,          topQuarkP4_antitop.phi(),     evtWeight, evtWeightErr);
    if ( isGenMatched_antitop )
    {
      histogram_genAntiTop_pt_vs_antiTop_pt_->Fill(topQuarkP4_antitop.pt(), genTopQuarkP4_antitop.pt(), evtWeight);
      double deltaAntiTop_pt = topQuarkP4_antitop.pt() - genTopQuarkP4_antitop.pt();
      fillWithOverFlow(histogram_deltaAntiTop_pt_,    deltaAntiTop_pt,              evtWeight, evtWeightErr);
      fillWithOverFlow2d(histogram_deltaAntiTop_pt_vs_genAntiTop_pt_, genTopQuarkP4_antitop.pt(), deltaAntiTop_pt, evtWeight, evtWeightErr);
      double deltaAntiTop_px = topQuarkP4_antitop.px() - genTopQuarkP4_antitop.px();
      double deltaAntiTop_py = topQuarkP4_antitop.py() - genTopQuarkP4_antitop.py();
      double deltaAntiTop_parl = comp_metParl(genTopQuarkP4_antitop.px(), genTopQuarkP4_antitop.py(), deltaAntiTop_px, deltaAntiTop_py);
      fillWithOverFlow(histogram_deltaAntiTop_parl_,  deltaAntiTop_parl,            evtWeight, evtWeightErr);  
      fillWithOverFlow2d(histogram_deltaAntiTop_parl_vs_genAntiTop_pt_, genTopQuarkP4_antitop.pt(), deltaAntiTop_parl, evtWeight, evtWeightErr);
      double deltaAntiTop_perp = comp_metPerp(genTopQuarkP4_antitop.px(), genTopQuarkP4_antitop.py(), deltaAntiTop_px, deltaAntiTop_py);
      fillWithOverFlow(histogram_deltaAntiTop_perp_,  deltaAntiTop_perp,            evtWeight, evtWeightErr);  
      fillWithOverFlow2d(histogram_deltaAntiTop_perp_vs_genAntiTop_pt_, genTopQuarkP4_antitop.pt(), deltaAntiTop_perp, evtWeight, evtWeightErr);
      double deltaAntiTop_eta = topQuarkP4_antitop.eta() - genTopQuarkP4_antitop.eta();
      fillWithOverFlow(histogram_deltaAntiTop_eta_,   deltaAntiTop_eta,             evtWeight, evtWeightErr);
      double deltaAntiTop_phi = topQuarkP4_antitop.phi() - genTopQuarkP4_antitop.phi();
      fillWithOverFlow(histogram_deltaAntiTop_phi_,   deltaAntiTop_phi,             evtWeight, evtWeightErr);
    }
  }

  double genMtt = (genTopQuarkP4_top + genTopQuarkP4_antitop).mass();
  fillWithOverFlow(histogram_genMtt_,                 genMtt,                       evtWeight, evtWeightErr);
  if ( isValid_topKinReco )
  {
    double mtt = (topQuarkP4_top + topQuarkP4_antitop).mass();
    fillWithOverFlow(histogram_mtt_,                  mtt,                          evtWeight, evtWeightErr);
    fillWithOverFlow2d(histogram_deltaMtt_vs_genMtt_, genMtt, mtt - genMtt, evtWeight, evtWeightErr);
  }

  const Particle::LorentzVector& dileptonP4 = selLeptonP4_lead + selLeptonP4_sublead;
  fillWithOverFlow(histogram_m_ll_,                   dileptonP4.mass(),            evtWeight, evtWeightErr);
  double dR_ll = deltaR(selLeptonP4_lead, selLeptonP4_sublead);
  fillWithOverFlow(histogram_dR_ll_,                  dR_ll,                        evtWeight, evtWeightErr);
  double dPhi_ll = deltaPhi(selLeptonP4_lead.phi(), selLeptonP4_sublead.phi());
  fillWithOverFlow(histogram_dPhi_ll_,                dPhi_ll,                      evtWeight, evtWeightErr);
  double dEta_ll = TMath::Abs(selLeptonP4_lead.eta() - selLeptonP4_sublead.eta());
  fillWithOverFlow(histogram_dEta_ll_,                dEta_ll,                      evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_ll_,                  dileptonP4.pt(),              evtWeight, evtWeightErr);

  if ( m_HH_hme > 0. ) {
    fillWithOverFlow(histogram_m_HH_hme_,             m_HH_hme,                     evtWeight, evtWeightErr);    
  }

  fillWithOverFlow(histogram_vbf_m_jj_,               vbf_m_jj,                     evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_vbf_dEta_jj_,            vbf_dEta_jj,                  evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_EventCounter_,           0.,                           evtWeight, evtWeightErr);
}
