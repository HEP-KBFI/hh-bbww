#ifndef hhAnalysis_bbww_EvtHistManager_hh_bbWW_Wctrl_h
#define hhAnalysis_bbww_EvtHistManager_hh_bbWW_Wctrl_h

/** \class EvtHistManager_hh_bbWW_Wctrl
 *
 * Book and fill histograms for event-level quantities in the Drell-Yan (DY) control region 
 * of the HH->bbWW analysis
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h" // HistManagerBase

class EvtHistManager_hh_bbWW_Wctrl
  : public HistManagerBase
{
public:
  EvtHistManager_hh_bbWW_Wctrl(const edm::ParameterSet & cfg);
  ~EvtHistManager_hh_bbWW_Wctrl() {}

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
		 double mT, double dPhi_lnu, double pT_lnu,
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

  TH1 * histogram_mT_;
  TH1 * histogram_dPhi_lnu_;
  TH1 * histogram_pT_lnu_;

  TH1 * histogram_m_HH_hme_;

  TH1 * histogram_jetAK8_Wjj_dR_lepton_;

  TH1 * histogram_vbf_m_jj_;
  TH1 * histogram_vbf_dEta_jj_;

  TH1 * histogram_EventCounter_;
};

#endif
