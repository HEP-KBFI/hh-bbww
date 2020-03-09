#ifndef hhAnalysis_bbww_EvtHistManager_hh_bbWW_TT2lctrl_h
#define hhAnalysis_bbww_EvtHistManager_hh_bbWW_TT2lctrl_h

/** \class EvtHistManager_hh_bbWW_TT2lctrl
 *
 * Book and fill histograms for event-level quantities in the tt+jets (TT) dilepton control region 
 * of the HH->bbWW analysis
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h" // HistManagerBase
#include "tthAnalysis/HiggsToTauTau/interface/Particle.h"        // Particle::LorentzVector

class EvtHistManager_hh_bbWW_TT2lctrl
  : public HistManagerBase
{
public:
  EvtHistManager_hh_bbWW_TT2lctrl(const edm::ParameterSet & cfg);
  ~EvtHistManager_hh_bbWW_TT2lctrl() {}

  /// book and fill histograms
  void
  bookHistograms(TFileDirectory & dir) override;

  void
  fillHistograms(int numElectrons,
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
		 double evtWeight);

  const TH1 *
  getHistogram_EventCounter() const;

 private:
  TH1 * histogram_numElectrons_;
  TH1 * histogram_numMuons_;
  TH1 * histogram_numHadTaus_;
  TH1 * histogram_numJets_;
  TH1 * histogram_numBJets_loose_;
  TH1 * histogram_numBJets_medium_;
  TH1 * histogram_numJetsAK8_Hbb_; 

  TH1 * histogram_HT_;
  TH1 * histogram_STMET_;

  TH1 * histogram_genMEt_pt_;
  TH1 * histogram_genMEt_eta_;
  TH1 * histogram_genMEt_phi_;
  TH1 * histogram_recMEt_pt_;
  TH1 * histogram_recMEt_eta_;
  TH1 * histogram_recMEt_phi_;
  TH1 * histogram_deltaMEt_eta_;
  TH1 * histogram_deltaMEt_px_;
  TH1 * histogram_deltaMEt_py_;

  TH1 * histogram_genTop_pt_;
  TH1 * histogram_genTop_eta_;
  TH1 * histogram_genTop_phi_;
  TH1 * histogram_top_pt_;
  TH1 * histogram_top_eta_;
  TH1 * histogram_top_phi_;
  TH2 * histogram_genTop_pt_vs_top_pt_;
  TH1 * histogram_deltaTop_pt_;
  TH2 * histogram_deltaTop_pt_vs_genTop_pt_;
  TH1 * histogram_deltaTop_parl_;
  TH2 * histogram_deltaTop_parl_vs_genTop_pt_;
  TH1 * histogram_deltaTop_perp_;
  TH2 * histogram_deltaTop_perp_vs_genTop_pt_;
  TH1 * histogram_deltaTop_eta_;
  TH1 * histogram_deltaTop_phi_;

  TH1 * histogram_genAntiTop_pt_;
  TH1 * histogram_genAntiTop_eta_;
  TH1 * histogram_genAntiTop_phi_;
  TH1 * histogram_antiTop_pt_;
  TH1 * histogram_antiTop_eta_;
  TH1 * histogram_antiTop_phi_;
  TH2 * histogram_genAntiTop_pt_vs_antiTop_pt_;
  TH1 * histogram_deltaAntiTop_pt_;
  TH2 * histogram_deltaAntiTop_pt_vs_genAntiTop_pt_;
  TH1 * histogram_deltaAntiTop_parl_;
  TH2 * histogram_deltaAntiTop_parl_vs_genAntiTop_pt_;
  TH1 * histogram_deltaAntiTop_perp_;
  TH2 * histogram_deltaAntiTop_perp_vs_genAntiTop_pt_;
  TH1 * histogram_deltaAntiTop_eta_;
  TH1 * histogram_deltaAntiTop_phi_;

  TH1 * histogram_genMtt_;
  TH1 * histogram_mtt_;
  TH2 * histogram_deltaMtt_vs_genMtt_;

  TH1 * histogram_m_ll_;
  TH1 * histogram_dR_ll_;
  TH1 * histogram_dPhi_ll_;
  TH1 * histogram_dEta_ll_;
  TH1 * histogram_pT_ll_;

  TH1 * histogram_m_HH_hme_;

  TH1 * histogram_vbf_m_jj_;
  TH1 * histogram_vbf_dEta_jj_;

  TH1 * histogram_EventCounter_;
};

#endif
