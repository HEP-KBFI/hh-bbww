#ifndef hhAnalysis_bbww_EvtHistManager_hh_bb1l1tau_h
#define hhAnalysis_bbww_EvtHistManager_hh_bb1l1tau_h

/** \class EvtHistManager_hh_bb1l1tau
 *
 * Book and fill histograms for event-level quantities in the lepton+tau category 
 * of the HH->bbWW analysis
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h" // HistManagerBase

class EvtHistManager_hh_bb1l1tau
  : public HistManagerBase
{
public:
  EvtHistManager_hh_bb1l1tau(const edm::ParameterSet & cfg);
  ~EvtHistManager_hh_bb1l1tau() {}

  /// book and fill histograms
  void
  bookHistograms(TFileDirectory & dir) override;

  void
  fillHistograms(int numElectrons,
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

  TH1 * histogram_HT_;
  TH1 * histogram_STMET_;

  TH1 * histogram_m_Hbb_;
  TH1 * histogram_dR_Hbb_;
  TH1 * histogram_dPhi_Hbb_;
  TH1 * histogram_pT_Hbb_;

  TH1 * histogram_m_ltau_;
  TH1 * histogram_dR_ltau_;
  TH1 * histogram_dPhi_ltau_;
  TH1 * histogram_pT_ltau_;

  TH1 * histogram_m_Hww_;
  TH1 * histogram_pT_Hww_;

  TH1 * histogram_m_HHvis_;
  TH1 * histogram_m_HH_;
  TH1 * histogram_dPhi_HH_;
  TH1 * histogram_pT_HH_;

  TH1 * histogram_mT2_W_;
  TH1 * histogram_mT2_W_step_;
  TH1 * histogram_mT2_top_2particle_;
  TH1 * histogram_mT2_top_2particle_step_;
  TH1 * histogram_mT2_top_3particle_;
  TH1 * histogram_mT2_top_3particle_step_;
 
  TH1 * histogram_vbf_jet1_pt_;
  TH1 * histogram_vbf_jet1_eta_;
  TH1 * histogram_vbf_jet2_pt_;
  TH1 * histogram_vbf_jet2_eta_;
  TH1 * histogram_vbf_m_jj_;
  TH1 * histogram_vbf_dEta_jj_;

  TH1 * histogram_EventCounter_;
};

#endif
