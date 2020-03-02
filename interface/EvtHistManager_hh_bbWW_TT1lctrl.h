#ifndef hhAnalysis_bbww_EvtHistManager_hh_bbWW_TT1lctrl_h
#define hhAnalysis_bbww_EvtHistManager_hh_bbWW_TT1lctrl_h

/** \class EvtHistManager_hh_bbWW_TT1lctrl
 *
 * Book and fill histograms for event-level quantities in the Drell-Yan (DY) control region 
 * of the HH->bbWW analysis
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h" // HistManagerBase
#include "tthAnalysis/HiggsToTauTau/interface/Particle.h"        // Particle::LorentzVector

class EvtHistManager_hh_bbWW_TT1lctrl
  : public HistManagerBase
{
public:
  EvtHistManager_hh_bbWW_TT1lctrl(const edm::ParameterSet & cfg);
  ~EvtHistManager_hh_bbWW_TT1lctrl() {}

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
  TH1 * histogram_numJetsAK8_Wjj_;

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

  TH1 * histogram_genHadTop_pt_;
  TH1 * histogram_genHadTop_eta_;
  TH1 * histogram_genHadTop_phi_;
  TH1 * histogram_hadTop_pt_;
  TH1 * histogram_hadTop_eta_;
  TH1 * histogram_hadTop_phi_;
  TH1 * histogram_deltaHadTop_pt_;
  TH2 * histogram_deltaHadTop_pt_vs_genHadTop_pt_;
  TH1 * histogram_deltaHadTop_parl_;
  TH2 * histogram_deltaHadTop_parl_vs_genHadTop_pt_;
  TH1 * histogram_deltaHadTop_perp_;
  TH2 * histogram_deltaHadTop_perp_vs_genHadTop_pt_;
  TH1 * histogram_deltaHadTop_eta_;
  TH1 * histogram_deltaHadTop_phi_;

  TH1 * histogram_genLepTop_pt_;
  TH1 * histogram_genLepTop_eta_;
  TH1 * histogram_genLepTop_phi_;
  TH1 * histogram_lepTop_pt_;
  TH1 * histogram_lepTop_eta_;
  TH1 * histogram_lepTop_phi_;
  TH1 * histogram_deltaLepTop_pt_;
  TH2 * histogram_deltaLepTop_pt_vs_genLepTop_pt_;
  TH1 * histogram_deltaLepTop_parl_;
  TH2 * histogram_deltaLepTop_parl_vs_genLepTop_pt_;
  TH1 * histogram_deltaLepTop_perp_;
  TH2 * histogram_deltaLepTop_perp_vs_genLepTop_pt_;
  TH1 * histogram_deltaLepTop_eta_;
  TH1 * histogram_deltaLepTop_phi_;

  TH1 * histogram_genMtt_;
  TH1 * histogram_mtt_;
  TH2 * histogram_deltaMtt_vs_genMtt_;

  TH1 * histogram_mT_;
  TH1 * histogram_m_lnu_;
  TH1 * histogram_dPhi_lnu_;
  TH1 * histogram_pT_lnu_;

  TH1 * histogram_m_HH_hme_;

  TH1 * histogram_jetAK8_Wjj_dR_lepton_;

  TH1 * histogram_vbf_m_jj_;
  TH1 * histogram_vbf_dEta_jj_;

  TH1 * histogram_EventCounter_;
};

#endif
