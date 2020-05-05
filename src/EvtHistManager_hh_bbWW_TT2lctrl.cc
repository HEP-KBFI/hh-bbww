#include "hhAnalysis/bbww/interface/EvtHistManager_hh_bbWW_TT2lctrl.h"

#include "DataFormats/Math/interface/deltaR.h"   // deltaR
#include "DataFormats/Math/interface/deltaPhi.h" // deltaPhi

#include <TMath.h> // TMath::Abs, TMath::Log, TMath::Min, TMath::Pi, TMath::Sqrt
#include <TH2.h>   // TH2->Fill

EvtHistManager_hh_bbWW_TT2lctrl::EvtHistManager_hh_bbWW_TT2lctrl(const edm::ParameterSet & cfg)
  : HistManagerBase(cfg)
  , associations_({ "all", "correctAssoc", "incorrectAssoc", })
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
  central_or_shiftOptions_["genAntiTop_pt"] = { "central" };
  central_or_shiftOptions_["genAntiTop_eta"] = { "central" };
  central_or_shiftOptions_["genAntiTop_phi"] = { "central" };
  central_or_shiftOptions_["genTopPair_mass"] = { "central" };
  central_or_shiftOptions_["genTopPair_pt"] = { "central" };
  central_or_shiftOptions_["isValid_topKinReco"] = { "central" };
  central_or_shiftOptions_["numSolutions_topKinReco"] = { "central" };
  for ( const std::string& association : associations_ )
  {
    histograms_top_and_antiTop_[association] = new histogramEntryType(association, central_or_shiftOptions_);    
  }
  central_or_shiftOptions_["topPair_pt_incorrectAssoc_vs_topPair_pt_correctAssoc"] = { "central" };
  central_or_shiftOptions_["logWeight_incorrectAssoc_vs_logWeight_correctAssoc"] = { "central" };
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
  histogram_numElectrons_            = book1D(dir, "numElectrons",            "numElectrons",             5,   -0.5,  +4.5);
  histogram_numMuons_                = book1D(dir, "numMuons",                "numMuons",                 5,   -0.5,  +4.5);
  histogram_numJets_                 = book1D(dir, "numJets",                 "numJets",                 20,   -0.5, +19.5);
  histogram_numBJets_loose_          = book1D(dir, "numBJets_loose",          "numBJets_loose",          10,   -0.5,  +9.5);
  histogram_numBJets_medium_         = book1D(dir, "numBJets_medium",         "numBJets_medium",         10,   -0.5,  +9.5);
  histogram_numJetsAK8_Hbb_          = book1D(dir, "numJetsAK8_Hbb",          "numJetsAK8_Hbb",           4,   -0.5,  +3.5);
 
  histogram_HT_                      = book1D(dir, "HT",                      "HT",                     150,    0., 1500.);
  histogram_STMET_                   = book1D(dir, "STMET",                   "STMET",                  150,    0., 1500.);

  histogram_genMEt_pt_               = book1D(dir, "genMEt_pt",               "genMEt_pt",              100,    0.,  500.);
  histogram_genMEt_eta_              = book1D(dir, "genMEt_eta",              "genMEt_eta",             100,   -5.,   +5.);
  histogram_genMEt_phi_              = book1D(dir, "genMEt_phi",              "genMEt_phi",              36, -TMath::Pi(), +TMath::Pi());
  histogram_recMEt_pt_               = book1D(dir, "met_pt",                  "met_pt",                 100,    0.,  500.);
  histogram_recMEt_eta_              = book1D(dir, "met_eta",                 "met_eta",                100,   -5.,   +5.);
  histogram_recMEt_phi_              = book1D(dir, "met_phi",                 "met_phi",                 36, -TMath::Pi(), +TMath::Pi());
  histogram_deltaMEt_eta_            = book1D(dir, "deltaMEt_eta",            "deltaMEt_eta",           100,   -5.,   +5.);
  histogram_deltaMEt_px_             = book1D(dir, "deltaMEt_px",             "deltaMEt_px",             40, -100., +100.);
  histogram_deltaMEt_py_             = book1D(dir, "deltaMEt_py",             "deltaMEt_py",             40, -100., +100.);

  histogram_genTop_pt_               = book1D(dir, "genTop_pt",               "genTop_pt",              100,    0.,  500.);
  histogram_genTop_eta_              = book1D(dir, "genTop_eta",              "genTop_eta",             100,   -5.,   +5.);
  histogram_genTop_phi_              = book1D(dir, "genTop_phi",              "genTop_phi",              36, -TMath::Pi(), +TMath::Pi());

  histogram_genAntiTop_pt_           = book1D(dir, "genAntiTop_pt",           "genAntiTop_pt",          100,    0.,  500.);
  histogram_genAntiTop_eta_          = book1D(dir, "genAntiTop_eta",          "genAntiTop_eta",         100,   -5.,   +5.);
  histogram_genAntiTop_phi_          = book1D(dir, "genAntiTop_phi",          "genAntiTop_phi",          36, -TMath::Pi(), +TMath::Pi());

  histogram_genTopPair_mass_         = book1D(dir, "genTopPair_mass",         "genTopPair_mass",        100,    0., 1000.);
  histogram_genTopPair_pt_           = book1D(dir, "genTopPair_pt",           "genTopPair_pt",          100,    0., 1000.);

  histogram_isValid_topKinReco_      = book1D(dir, "isValid_topKinReco",      "isValid_topKinReco",       2,   -0.5,  +1.5);
  histogram_numSolutions_topKinReco_ = book1D(dir, "numSolutions_topKinReco", "numSolutions_topKinReco", 10,   -0.5,  +9.5);

  for ( std::vector<std::string>::const_iterator association = associations_.begin();
        association != associations_.end(); ++association ) {
    assert(histograms_top_and_antiTop_[*association]);
    histograms_top_and_antiTop_[*association]->bookHistograms(dir, this);
  }

  histogram_topPair_pt_incorrectAssoc_vs_topPair_pt_correctAssoc_ = book2D(dir, "topPair_pt_incorrectAssoc_vs_topPair_pt_correctAssoc", 10, 0., 500., 10, 0., 500.);
  histogram_logWeight_incorrectAssoc_vs_logWeight_correctAssoc_   = book2D(dir, "logWeight_incorrectAssoc_vs_logWeight_correctAssoc",   30, 0.,  15., 30, 0.,  15.);

  histogram_m_ll_                    = book1D(dir, "m_ll",                    "m_ll",                    40,    0.,  200.);
  histogram_dR_ll_                   = book1D(dir, "dR_ll",                   "dR_ll",                  100,    0.,    5.);
  histogram_dPhi_ll_                 = book1D(dir, "dPhi_ll",                 "dPhi_ll",                 36,    0, TMath::Pi());
  histogram_dEta_ll_                 = book1D(dir, "dEta_ll",                 "dEta_ll",                 50,    0,     5.);
  histogram_pT_ll_                   = book1D(dir, "pT_ll",                   "pT_ll",                  100,    0.,  500.);

  histogram_m_HH_hme_                = book1D(dir, "m_HH_hme",                "m_HH_hme",               150,    0., 1500.);

  histogram_vbf_m_jj_                = book1D(dir, "vbf_m_jj",                "vbf_m_jj",               150,    0., 1500.);
  histogram_vbf_dEta_jj_             = book1D(dir, "vbf_dEta_jj",             "vbf_dEta_jj",            100,    0.,   10.);

  histogram_EventCounter_            = book1D(dir, "EventCounter",            "EventCounter",             1,   -0.5,  +0.5);
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
                                                const Particle::LorentzVector& genMEtP4, const Particle::LorentzVector& metP4,
                                                bool isValid_topKinReco, int numSolutions_topKinReco, double weight_topKinReco_assoc1, double weight_topKinReco_assoc2,
                                                const Particle::LorentzVector& genTopQuarkP4_top, 
                                                bool isGenMatched_top_assoc1, const Particle::LorentzVector& topQuarkP4_top_assoc1,
                                                bool isGenMatched_top_assoc2, const Particle::LorentzVector& topQuarkP4_top_assoc2,
                                                const Particle::LorentzVector& genTopQuarkP4_antitop, 
                                                bool isGenMatched_antitop_assoc1, const Particle::LorentzVector& topQuarkP4_antitop_assoc1,
                                                bool isGenMatched_antitop_assoc2, const Particle::LorentzVector& topQuarkP4_antitop_assoc2,
		                                const Particle::LorentzVector& selLeptonP4_lead, const Particle::LorentzVector& selLeptonP4_sublead,
                                                double m_HH_hme,
					        double vbf_m_jj, double vbf_dEta_jj,
					        double evtWeight)
{
  const double evtWeightErr = 0.;

  fillWithOverFlow(histogram_numElectrons_,            numElectrons,                 evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numMuons_,                numMuons,                     evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJets_,                 numJets,                      evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_loose_,          numBJets_loose,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_medium_,         numBJets_medium,              evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJetsAK8_Hbb_,          numJetsAK8_Hbb,               evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_HT_,                      HT,                           evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_STMET_,                   STMET,                        evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_genMEt_pt_,               genMEtP4.pt(),                evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_genMEt_eta_,              genMEtP4.eta(),               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_genMEt_phi_,              genMEtP4.phi(),               evtWeight, evtWeightErr);
  if ( isValid_topKinReco ) 
  {
    fillWithOverFlow(histogram_recMEt_pt_,             metP4.pt(),                   evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_recMEt_eta_,            metP4.eta(),                  evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_recMEt_phi_,            metP4.phi(),                  evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_deltaMEt_eta_,          metP4.eta() - genMEtP4.eta(), evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_deltaMEt_px_,           metP4.px() - genMEtP4.px(),   evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_deltaMEt_py_,           metP4.py() - genMEtP4.py(),   evtWeight, evtWeightErr);
  }

  fillWithOverFlow(histogram_genTop_pt_,               genTopQuarkP4_top.pt(),       evtWeight, evtWeightErr);   
  fillWithOverFlow(histogram_genTop_eta_,              genTopQuarkP4_top.eta(),      evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_genTop_phi_,              genTopQuarkP4_top.phi(),      evtWeight, evtWeightErr);        
  
  fillWithOverFlow(histogram_genAntiTop_pt_,           genTopQuarkP4_antitop.pt(),   evtWeight, evtWeightErr);   
  fillWithOverFlow(histogram_genAntiTop_eta_,          genTopQuarkP4_antitop.eta(),  evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_genAntiTop_phi_,          genTopQuarkP4_antitop.phi(),  evtWeight, evtWeightErr);        

  Particle::LorentzVector genTopPairP4 = genTopQuarkP4_top + genTopQuarkP4_antitop;
  fillWithOverFlow(histogram_genTopPair_mass_,         genTopPairP4.mass(),          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_genTopPair_pt_,           genTopPairP4.pt(),            evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_isValid_topKinReco_,      isValid_topKinReco,           evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numSolutions_topKinReco_, numSolutions_topKinReco,      evtWeight, evtWeightErr);

  for ( const std::string& association : associations_ )
  {
    histograms_top_and_antiTop_[association]->fillHistograms(
      isValid_topKinReco, numSolutions_topKinReco, weight_topKinReco_assoc1, weight_topKinReco_assoc2,
      genTopQuarkP4_top, isGenMatched_top_assoc1, topQuarkP4_top_assoc1, isGenMatched_top_assoc2, topQuarkP4_top_assoc2,
      genTopQuarkP4_antitop, isGenMatched_antitop_assoc1, topQuarkP4_antitop_assoc1, isGenMatched_antitop_assoc2, topQuarkP4_antitop_assoc2,
      evtWeight);
  }

  if ( isValid_topKinReco && ((isGenMatched_top_assoc1 && isGenMatched_antitop_assoc1) || (isGenMatched_top_assoc2 && isGenMatched_antitop_assoc2)) )
  {
    Particle::LorentzVector topPairP4_correctAssoc;
    double weight_correctAssoc = -1.;
    Particle::LorentzVector topPairP4_incorrectAssoc;
    double weight_incorrectAssoc = -1.;
    if ( isGenMatched_top_assoc1 && isGenMatched_antitop_assoc1 )
    {
      topPairP4_correctAssoc = topQuarkP4_top_assoc1 + topQuarkP4_antitop_assoc1;
      weight_correctAssoc = weight_topKinReco_assoc1;
      topPairP4_incorrectAssoc = topQuarkP4_top_assoc2 + topQuarkP4_antitop_assoc2;
      weight_incorrectAssoc = weight_topKinReco_assoc2;
    }
    else if ( isGenMatched_top_assoc2 && isGenMatched_antitop_assoc2 )
    {
      topPairP4_correctAssoc = topQuarkP4_top_assoc2 + topQuarkP4_antitop_assoc2;
      weight_correctAssoc = weight_topKinReco_assoc2;
      topPairP4_incorrectAssoc = topQuarkP4_top_assoc1 + topQuarkP4_antitop_assoc1;
      weight_incorrectAssoc = weight_topKinReco_assoc1;
    }
    else assert(0);
    if(histogram_topPair_pt_incorrectAssoc_vs_topPair_pt_correctAssoc_)fillWithOverFlow2d(histogram_topPair_pt_incorrectAssoc_vs_topPair_pt_correctAssoc_, topPairP4_correctAssoc.pt(), topPairP4_incorrectAssoc.pt(), evtWeight, evtWeightErr); 
    double logWeight_correctAssoc = TMath::Log(TMath::Min(1.e-10, weight_correctAssoc));
    double logWeight_incorrectAssoc = TMath::Log(TMath::Min(1.e-10, weight_incorrectAssoc));
    if(histogram_logWeight_incorrectAssoc_vs_logWeight_correctAssoc_)fillWithOverFlow2d(histogram_logWeight_incorrectAssoc_vs_logWeight_correctAssoc_, logWeight_correctAssoc, logWeight_incorrectAssoc, evtWeight, evtWeightErr);
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
