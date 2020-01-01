#ifndef hhAnalysis_bbww_EvtHistManager_hh_bbWW_DYctrl_h
#define hhAnalysis_bbww_EvtHistManager_hh_bb2l_DYctrl_h

/** \class EvtHistManager_hh_bb2l
 *
 * Book and fill histograms for event-level quantities in the Drell-Yan (DY) control region 
 * of the HH->bbWW analysis
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h" // HistManagerBase

class EvtHistManager_hh_bbWW_DYctrl
  : public HistManagerBase
{
public:
  EvtHistManager_hh_bbWW_DYctrl(const edm::ParameterSet & cfg);
  ~EvtHistManager_hh_bbWW_DYctrl() {}

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
		 double m_bb, double dR_bb, double dPhi_bb, double pT_bb, 
		 double m_ll, double dR_ll, double dPhi_ll, double pT_ll,
		 double m_bbll, double dPhi_bbll, double pT_bbll, 
		 double m_bbllMEt, double m_HH_hme, double dPhi_bbllMEt, double pT_bbllMEt, double Smin_bbllMEt,
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

  TH1 * histogram_HT_;
  TH1 * histogram_STMET_;

  TH1 * histogram_m_bb_;
  TH1 * histogram_dR_bb_;
  TH1 * histogram_dPhi_bb_;
  TH1 * histogram_pT_bb_;

  TH1 * histogram_m_ll_;
  TH1 * histogram_m_ll_high_;
  TH1 * histogram_dR_ll_;
  TH1 * histogram_dPhi_ll_;
  TH1 * histogram_pT_ll_;

  TH1 * histogram_m_bbll_;
  TH1 * histogram_dPhi_bbll_;
  TH1 * histogram_pT_bbll_;

  TH1 * histogram_m_bbllMEt_;
  TH1 * histogram_m_HH_hme_;
  TH1 * histogram_dPhi_bbllMEt_;
  TH1 * histogram_pT_bbllMEt_;
  TH1 * histogram_Smin_bbllMEt_;

  TH1 * histogram_vbf_m_jj_;
  TH1 * histogram_vbf_dEta_jj_;

  TH1 * histogram_EventCounter_;
};

#endif
