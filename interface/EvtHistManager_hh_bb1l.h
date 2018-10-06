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
		 double m_Hbb, double dR_Hbb, double dPhi_Hbb, double pT_Hbb, 
		 double dR_Hww, double dPhi_Hww, double pT_Hww, double Smin_Hww,
		 double m_HHvis, double m_HH, double m_HH_B2G_18_008, double m_HH_hme, double dR_HH, double dPhi_HH, double pT_HH, double Smin_HH,
		 double mT_W, double mT_top_2particle, double mT_top_3particle,
		 double mvaOutput_Hj_tagger, double mvaOutput_Hjj_tagger,
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

  TH1 * histogram_m_Hbb_;
  TH1 * histogram_dR_Hbb_;
  TH1 * histogram_dPhi_Hbb_;
  TH1 * histogram_pT_Hbb_;

  TH1 * histogram_dR_Hww_;
  TH1 * histogram_dPhi_Hww_;
  TH1 * histogram_pT_Hww_;  
  TH1 * histogram_Smin_Hww_;

  TH1 * histogram_m_HHvis_;
  TH1 * histogram_m_HH_;
  TH1 * histogram_m_HH_B2G_18_008_;
  TH1 * histogram_m_HH_hme_;
  TH1 * histogram_dR_HH_;
  TH1 * histogram_dPhi_HH_;
  TH1 * histogram_pT_HH_;
  TH1 * histogram_Smin_HH_;

  TH1 * histogram_mT_W_;
  TH1 * histogram_mT_top_2particle_;
  TH1 * histogram_mT_top_3particle_;

  TH1 * histogram_mvaOutput_Hj_tagger_;
  TH1 * histogram_mvaOutput_Hjj_tagger_;

  TH1 * histogram_vbf_m_jj_;
  TH1 * histogram_vbf_dEta_jj_;
      
  TH1 * histogram_EventCounter_;
};

#endif
