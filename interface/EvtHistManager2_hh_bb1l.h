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
  EvtHistManager2_hh_bb1l(const edm::ParameterSet & cfg, const bool plot_DNN_correlation);
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
                 double m_HH_B2G_18_008, double m_HH_analytic, double m_HH_vis, double m_HH, double pT_HH, double dPhi_HHvis, double pT_HHvis,
                 double mT_W, double mT_top_2particle, double mT_top_3particle,
                 double vbf_m_jj, double vbf_dEta_jj, double vbf_lhe_m_jj, double vbf_lhe_dEta_jj,
                 double bjet1_btagCSV, double bjet2_btagCSV, double wjet1_btagCSV,  double wjet2_btagCSV,
                 double mindr_lep1_jet, double avg_dr_jet_central,
                 double lepPairType_loose, double selLepton_type,
                 double mbb_medium,
                 double dR_b1lep, double dR_b2lep,
                 double mjj_highestpt,
                 double numJetsForward, double tau21_Hbb, const RecoJetAK8* selJetAK8_Hbb,
                 double lep_eta, double lep_phi, double lep_e,
                 double Hbb_lead_pt, double Hbb_lead_eta, double Hbb_lead_phi, double Hbb_lead_m,
                 double Hbb_sublead_pt, double Hbb_sublead_eta, double Hbb_sublead_phi, double Hbb_sublead_m,
                 double Wjj_lead_pt, double Wjj_lead_eta, double Wjj_lead_phi, double Wjj_lead_m,
                 double Wjj_sublead_pt, double Wjj_sublead_eta, double Wjj_sublead_phi, double Wjj_sublead_m,
                 double jet1_pt, double jet1_eta, double jet1_phi,
                 double jet2_pt, double jet2_eta, double jet2_phi,
                 double m_Hww, double m_HH_bbregCorr, double dPhi_met_lep, double dR_lep_Wjj,
                 double dR_lep_Hbb, double pT_wlep, double dPhi_met_Hbb, double dPhi_met_Wjj,
                 double met_phi, double lepPairCharge_loose, double m_wlep,
                 std::map<std::string, std::map<std::string, double>>& lbnOutputs_resonant_spin0,
                 std::map<std::string, std::map<std::string, double>>& lbnOutputs_resonant_spin2,
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
  TH1 * histogram_met_phi_;
  TH1* histogram_m_wlep_;
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
  TH1* histogram_m_HH_analytic_;
  TH1* histogram_m_HH_;
  TH1* histogram_m_HH_vis_;
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

  TH1 * histogram_lep_eta_;
  TH1 * histogram_lep_phi_;
  TH1 * histogram_lep_e_;

  TH1 * histogram_Hbb_lead_pt_;
  TH1 * histogram_Hbb_lead_eta_;
  TH1 * histogram_Hbb_lead_phi_;
  TH1 * histogram_Hbb_lead_m_;

  TH1 * histogram_Hbb_sublead_pt_;
  TH1 * histogram_Hbb_sublead_eta_;
  TH1 * histogram_Hbb_sublead_phi_;
  TH1 * histogram_Hbb_sublead_m_;

  TH1 * histogram_Wjj_lead_pt_;
  TH1 * histogram_Wjj_lead_eta_;
  TH1 * histogram_Wjj_lead_phi_;
  TH1 * histogram_Wjj_lead_m_;

  TH1 * histogram_Wjj_sublead_pt_;
  TH1 * histogram_Wjj_sublead_eta_;
  TH1 * histogram_Wjj_sublead_phi_;
  TH1 * histogram_Wjj_sublead_m_;

  TH1 * histogram_jet1_pt_;
  TH1 * histogram_jet1_eta_;
  TH1 * histogram_jet1_phi_;

  TH1 * histogram_jet2_pt_;
  TH1 * histogram_jet2_eta_;
  TH1 * histogram_jet2_phi_;

  TH1 * histogram_evtCategory_; // event category on datacard level
  
  TH1* histogram_m_Hww_;
  TH1* histogram_m_HH_bbregCorr_;
  TH1* histogram_dPhi_met_lep_;
  TH1* histogram_dR_lep_Wjj_;
  TH1* histogram_dR_lep_Hbb_;
  TH1* histogram_pT_wlep_;
  TH1* histogram_dPhi_met_Hbb_;
  TH1* histogram_dPhi_met_Wjj_;
  TH1* histogram_lepPairCharge_loose_;
  TH2* histogram_TT_resolved_270_300_spin2_;
  TH2* histogram_TT_resolved_300_400_spin2_;
  TH2* histogram_W_270_300_spin2_;
  TH2* histogram_W_300_400_spin2_;
  TH2* histogram_TT_boosted_270_300_spin2_;
  TH2* histogram_TT_boosted_300_400_spin2_;
  TH2* histogram_Other_270_300_spin2_;
  TH2* histogram_Other_300_400_spin2_;
  TH2* histogram_HH_resolved_2b_270_300_spin2_;
  TH2* histogram_HH_resolved_2b_300_400_spin2_;
  TH2* histogram_HH_resolved_1b_270_300_spin2_;
  TH2* histogram_HH_resolved_1b_300_400_spin2_;
  TH2* histogram_HH_boosted_270_300_spin2_;
  TH2* histogram_HH_boosted_300_400_spin2_;
  TH2* histogram_TT_resolved_270_300_spin0_;
  TH2* histogram_TT_resolved_300_400_spin0_;
  TH2* histogram_W_270_300_spin0_;
  TH2* histogram_W_300_400_spin0_;
  TH2* histogram_TT_boosted_270_300_spin0_;
  TH2* histogram_TT_boosted_300_400_spin0_;
  TH2* histogram_Other_270_300_spin0_;
  TH2* histogram_Other_300_400_spin0_;
  TH2* histogram_HH_resolved_2b_270_300_spin0_;
  TH2* histogram_HH_resolved_2b_300_400_spin0_;
  TH2* histogram_HH_resolved_1b_270_300_spin0_;
  TH2* histogram_HH_resolved_1b_300_400_spin0_;
  TH2* histogram_HH_boosted_270_300_spin0_;
  TH2* histogram_HH_boosted_300_400_spin0_;
  TH1 * histogram_EventCounter_;
  float TT_270_spin2;
  float TT_300_spin2;
  float TT_400_spin2;
  float W_270_spin2;
  float W_300_spin2;
  float W_400_spin2;
  float Other_270_spin2;
  float Other_300_spin2;
  float Other_400_spin2;
  float HH_270_spin2;
  float HH_300_spin2;
  float HH_400_spin2;
  float TT_270_spin0;
  float TT_300_spin0;
  float TT_400_spin0;
  float W_270_spin0;
  float W_300_spin0;
  float W_400_spin0;
  float Other_270_spin0;
  float Other_300_spin0;
  float Other_400_spin0;
  float HH_270_spin0;
  float HH_300_spin0;
  float HH_400_spin0;
  bool plot_DNN_correlation_;
};

#endif
