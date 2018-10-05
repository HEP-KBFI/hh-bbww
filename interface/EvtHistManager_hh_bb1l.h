#ifndef hhAnalysis_bbww_EvtHistManager_hh_bb1l_h
#define hhAnalysis_bbww_EvtHistManager_hh_bb1l_h

/** \class EvtHistManager_hh_bb1l
 *
 * Book and fill histograms for event-level quantities in the dilepton category 
 * of the HH->bbWW analysis
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h" // HistManagerBase

class EvtHistManager_hh_bb1l
  : public HistManagerBase
{
public:
  EvtHistManager_hh_bb1l(const edm::ParameterSet & cfg);
  ~EvtHistManager_hh_bb1l() {}

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
		 double m_bb, double dR_bb, double dR_jjlMEt, double dPhi_jjlMEt, 
		 double pT_jjlMEt, double Smin_jjlMEt, 
		 double pT_bbjjlMEt, double Smin_bbjjlMEt, double dPhi_bbjjlMEt,
		 double mT_W, double mT_top_2particle, double mT_top_3particle,
		 double m_bbjjl, double m_bbjjlMEt, double m_bbjjlMEt_B2G_18_008, double hmeMass, 
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

  TH1 * histogram_dR_jjlMEt_;
  TH1 * histogram_dPhi_jjlMEt_;

  TH1 * histogram_pT_jjlMEt_;
  TH1 * histogram_Smin_jjlMEt_;

  TH1 * histogram_pT_bbjjlMEt_;
  TH1 * histogram_Smin_bbjjlMEt_;
  TH1 * histogram_dPhi_bbjjlMEt_;

  TH1 * histogram_mT_W_;
  TH1 * histogram_mT_top_2particle_;
  TH1 * histogram_mT_top_3particle_;

  TH1 * histogram_m_bbjjl_;
  TH1 * histogram_m_bbjjlMEt_;
  TH1 * histogram_m_bbjjlMEt_B2G_18_008_;
  TH1 * histogram_hmeMass_;
      
  TH1 * histogram_EventCounter_;
};

#endif
