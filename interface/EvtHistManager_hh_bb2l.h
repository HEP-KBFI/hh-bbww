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
		 double m_bb, double dR_bb, double m_ll, double dR_ll,
		 double mT_llMEt,
		 double pT_bbllMEt, double dPhi_bbllMEt,
		 double mT2_W, int mT2_W_step, double mT2_top_2particle, int mT2_top_2particle_step, double mT2_top_3particle, int mT2_top_3particle_step, 
		 double logHiggsness, double logTopness,
		 double m_bbll, double m_bbllMEt, double hmeMass, 
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

  TH1 * histogram_m_ll_;
  TH1 * histogram_dR_ll_;

  TH1 * histogram_mT_llMEt_;

  TH1 * histogram_pT_bbllMEt_;
  TH1 * histogram_dPhi_bbllMEt_;

  TH1 * histogram_mT2_W_;
  TH1 * histogram_mT2_W_step_;
  TH1 * histogram_mT2_top_2particle_;
  TH1 * histogram_mT2_top_2particle_step_;
  TH1 * histogram_mT2_top_3particle_;
  TH1 * histogram_mT2_top_3particle_step_;
 
  TH1 * histogram_logHiggsness_;
  TH1 * histogram_logTopness_;
  TH2 * histogram_logTopness_vs_logHiggsness_;

  TH1 * histogram_m_bbll_;
  TH1 * histogram_m_bbllMEt_;
  TH1 * histogram_hmeMass_;
      
  TH1 * histogram_EventCounter_;
};

#endif
