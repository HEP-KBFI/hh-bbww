#ifndef hhAnalysis_bbww_EvtHistManager_hh_bb2l_h
#define hhAnalysis_bbww_EvtHistManager_hh_bb2l_h

/** \class EvtHistManager_hh_bb2l
 *
 * Book and fill histograms for event-level quantities in the dilepton category 
 * of the HH->bbWW analysis
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h" // HistManagerBase

class EvtHistManager_hh_bb2l
  : public HistManagerBase
{
public:
  EvtHistManager_hh_bb2l(const edm::ParameterSet & cfg);
  ~EvtHistManager_hh_bb2l() {}

  /// book and fill histograms
  void
  bookHistograms(TFileDirectory & dir) override;

  void
  fillHistograms(int numElectrons,
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
                 double vbf_m_jj, double vbf_dEta_jj, double mvaoutput300, double mvaoutput400, double mvaoutput750,
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

  TH1 * histogram_m_ll_;
  TH1 * histogram_dR_ll_;
  TH1 * histogram_dPhi_ll_;
  TH1 * histogram_pT_ll_;

  TH1 * histogram_m_Hww_;
  TH1 * histogram_pT_Hww_;
  TH1 * histogram_Smin_Hww_;

  TH1 * histogram_m_HHvis_;
  TH1 * histogram_m_HH_;
  TH1 * histogram_m_HH_hme_;
  TH1 * histogram_dR_HH_;
  TH1 * histogram_dPhi_HH_;
  TH1 * histogram_pT_HH_;
  TH1 * histogram_Smin_HH_;

  TH1 * histogram_mT2_W_;
  TH1 * histogram_mT2_W_step_;
  TH1 * histogram_mT2_top_2particle_;
  TH1 * histogram_mT2_top_2particle_step_;
  TH1 * histogram_mT2_top_3particle_;
  TH1 * histogram_mT2_top_3particle_step_;
 
  TH1 * histogram_logHiggsness_;
  TH1 * histogram_logTopness_;
  TH2 * histogram_logTopness_vs_logHiggsness_;

  TH1 * histogram_vbf_m_jj_;
  TH1 * histogram_vbf_dEta_jj_;

  TH1 * histogram_EventCounter_;
  TH1 * histogram_MVAOutput300_;
  TH1 * histogram_MVAOutput400_;
  TH1 * histogram_MVAOutput750_;
};

#endif
