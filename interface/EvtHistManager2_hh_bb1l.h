#ifndef hhAnalysis_bbww_EvtHistManager2_hh_bb1l_h
#define hhAnalysis_bbww_EvtHistManager2_hh_bb1l_h

/** \class EvtHistManager2_hh_bb1l
 *
 * Book and fill histograms for event-level quantities in the dilepton category
 * of the HH->bbWW analysis
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h" // HistManagerBase
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetAK8.h"      // RecoJetAK8

#include "hhAnalysis/bbwwMEM/interface/MEMResult.h"              // MEMbbwwResultSingleLepton
#include "hhAnalysis/bbww/interface/JPAInterface.h"              // JPA

class EvtHistManager2_hh_bb1l
  : public HistManagerBase
{
public:
  EvtHistManager2_hh_bb1l(const edm::ParameterSet & cfg);
  ~EvtHistManager2_hh_bb1l() {}

  /// book and fill histograms
  void
  bookHistograms(TFileDirectory & dir) override;

  void
  fillHistograms(int numJets,
                 int numBJets_loose,
                 int numBJets_medium,
                 double HT,
                 double met, double met_LD,
                 double lep_pt, double mll_loose,
                 double m_Hbb, double pT_Hbb, double dR_Hbb, double m_Hbb_regCorr,
                 double dPhi_Hww, double pT_Hww,
                 double m_HH_B2G_18_008, double pT_HH, double dPhi_HHvis, double pT_HHvis,
                 double mT_W, double mT_top_2particle, double mT_top_3particle,
                 double vbf_m_jj, double vbf_dEta_jj, double vbf_lhe_m_jj, double vbf_lhe_dEta_jj,
                 double bjet1_btagCSV, double bjet2_btagCSV, double wjet1_btagCSV,  double wjet2_btagCSV,
                 double mindr_lep1_jet, double avg_dr_jet_central,
                 double lepPairType_loose, double selLepton_type,
                 double mbb_medium,
                 double dR_b1lep, double dR_b2lep,
                 double mjj_highestpt,
                 double numJetsForward, double tau21_Hbb, const RecoJetAK8* selJetAK8_Hbb,
                 double lep_px, double lep_py, double lep_pz, double lep_e,
                 double Hbb_lead_px, double Hbb_lead_py, double Hbb_lead_pz, double Hbb_lead_e,
                 double Hbb_sublead_px, double Hbb_sublead_py, double Hbb_sublead_pz, double Hbb_sublead_e,
                 double Wjj_lead_px, double Wjj_lead_py, double Wjj_lead_pz, double Wjj_lead_e,
                 double Wjj_sublead_px, double Wjj_sublead_py, double Wjj_sublead_pz, double Wjj_sublead_e,
                 double evtWeight);

  const TH1 *
  getHistogram_EventCounter() const;

  /// flag to enable/disable booking & filling of MEM histograms
  enum { kOption_undefined, kOption_memDisabled, kOption_memEnabled };

 private:
  TH1 * histogram_numJets_;
  TH1 * histogram_numBJets_loose_;
  TH1 * histogram_numBJets_medium_;

  TH1 * histogram_HT_;
  TH1 * histogram_met_;
  TH1 * histogram_met_LD_;

  TH1 * histogram_lep_pt_;
  TH1 * histogram_mll_loose_;

  TH1 * histogram_m_Hbb_;
  TH1 * histogram_dR_Hbb_;
  TH1 * histogram_pT_Hbb_;
  TH1 * histogram_m_Hbb_regCorr_;

  TH1 * histogram_dPhi_Hww_;
  TH1 * histogram_pT_Hww_;

  TH1 * histogram_m_HH_B2G_18_008_;
  TH1 * histogram_dPhi_HHvis_;
  TH1 * histogram_pT_HH_;
  TH1 * histogram_pT_HHvis_;

  TH1 * histogram_mT_W_;
  TH1 * histogram_mT_top_2particle_;
  TH1 * histogram_mT_top_3particle_;

  TH1 * histogram_vbf_m_jj_;
  TH1 * histogram_vbf_dEta_jj_;
  TH1 * histogram_vbf_lhe_m_jj_;
  TH1 * histogram_vbf_lhe_dEta_jj_;

  //  TH1 * histogram_jpaCategory_; // event category on JPA level
  TH1 * histogram_bjet1_btagCSV_;
  TH1 * histogram_bjet2_btagCSV_;
  TH1 * histogram_wjet1_btagCSV_;
  TH1 * histogram_wjet2_btagCSV_;

  TH1 * histogram_mindr_lep1_jet_;
  TH1 * histogram_avg_dr_jet_central_;

  TH1 * histogram_lepPairType_loose_;
  TH1 * histogram_selLepton_type_;

  TH1 * histogram_mbb_medium_;
  TH1 * histogram_dR_b1lep_;
  TH1 * histogram_dR_b2lep_;

  TH1 * histogram_mjj_highestpt_;
  TH1 * histogram_numJetsForward_;
  TH1 * histogram_tau21_Hbb_;

  TH1 * histogram_lep_px_;
  TH1 * histogram_lep_py_;
  TH1 * histogram_lep_pz_;
  TH1 * histogram_lep_e_;

  TH1 * histogram_Hbb_lead_px_;
  TH1 * histogram_Hbb_lead_py_;
  TH1 * histogram_Hbb_lead_pz_;
  TH1 * histogram_Hbb_lead_e_;

  TH1 * histogram_Hbb_sublead_px_;
  TH1 * histogram_Hbb_sublead_py_;
  TH1 * histogram_Hbb_sublead_pz_;
  TH1 * histogram_Hbb_sublead_e_;

  TH1 * histogram_Wjj_lead_px_;
  TH1 * histogram_Wjj_lead_py_;
  TH1 * histogram_Wjj_lead_pz_;
  TH1 * histogram_Wjj_lead_e_;

  TH1 * histogram_Wjj_sublead_px_;
  TH1 * histogram_Wjj_sublead_py_;
  TH1 * histogram_Wjj_sublead_pz_;
  TH1 * histogram_Wjj_sublead_e_;

  TH1 * histogram_evtCategory_; // event category on datacard level

  TH1 * histogram_EventCounter_;
};

#endif
