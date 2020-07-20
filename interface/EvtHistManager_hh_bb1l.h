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

#include "hhAnalysis/bbwwMEM/interface/MEMResult.h" // MEMbbwwResultSingleLepton

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
		 double m_Wjj, double dR_Wjj, double dPhi_Wjj, double pT_Wjj,
		 double dR_Hww, double dPhi_Hww, double pT_Hww, double Smin_Hww,
		 double m_HHvis, double m_HH, double m_HH_B2G_18_008, double m_HH_hme, double dR_HH, double dPhi_HH, double pT_HH, double Smin_HH,
		 double mT_W, double mT_top_2particle, double mT_top_3particle,
		 double mvaOutput_Hj_tagger, double mvaOutput_Hjj_tagger,
		 double vbf_jet1_pt, double vbf_jet1_eta, double vbf_jet2_pt, double vbf_jet2_eta, double vbf_m_jj, double vbf_dEta_jj,
		 const MEMbbwwResultSingleLepton* memResult, double memCpuTime,
		 double mvaoutput350, double mvaoutput400, double mvaoutput750,
     std::string category_SM_jets,
     std::string  category_mount,
     const std::map<std::string, double> categories_map_MVAs,
     double selLepton_lead_pt, double selLepton_lead_eta,
     double selJetsAK4_0_pt,
     double selJetsAK4_1_pt,
     double selJetsAK4_0_eta,
     double selJetsAK4_1_eta,
     bool doDataMCPlots,
                 double evtWeight);

  const TH1 *
  getHistogram_EventCounter() const;

  void
  bookCategories(TFileDirectory & dir,
      const std::map<std::string, std::vector<double>> & categories_SM_jets,
      const std::map<std::string, std::vector<double>> & categories_list_bins,
      const std::vector<std::string> for_categories_map,
      bool doDataMCPlots
  );

  /// flag to enable/disable booking & filling of MEM histograms
  enum { kOption_undefined, kOption_memDisabled, kOption_memEnabled };

 private:
  TH1 * histogram_numElectrons_;
  TH1 * histogram_numMuons_;
  TH1 * histogram_numJets_;
  TH1 * histogram_numBJets_loose_;
  TH1 * histogram_numBJets_medium_;

  TH1 * histogram_HT_;
  TH1 * histogram_STMET_;

  TH1 * histogram_m_Hbb_;
  TH1 * histogram_dR_Hbb_;
  TH1 * histogram_dPhi_Hbb_;
  TH1 * histogram_pT_Hbb_;

  TH1 * histogram_m_Wjj_;
  TH1 * histogram_dR_Wjj_;
  TH1 * histogram_dPhi_Wjj_;
  TH1 * histogram_pT_Wjj_;

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

  TH1 * histogram_vbf_jet1_pt_;
  TH1 * histogram_vbf_jet1_eta_;
  TH1 * histogram_vbf_jet2_pt_;
  TH1 * histogram_vbf_jet2_eta_;
  TH1 * histogram_vbf_m_jj_;
  TH1 * histogram_vbf_dEta_jj_;

  TH1 * histogram_log_memProb_signal_;
  TH1 * histogram_log_memProbErr_signal_;
  TH1 * histogram_log_memProb_background_;
  TH1 * histogram_log_memProbErr_background_;
  TH1 * histogram_memLR_;
  TH1 * histogram_log_memLR_div_Err_;
  TH1 * histogram_memScore_;
  TH1 * histogram_memCpuTime_;

  TH1 * histogram_MVAOutput350_;
  TH1 * histogram_MVAOutput400_;
  TH1 * histogram_MVAOutput750_;

  TH1 * histogram_EventCounter_;

  std::map<std::string, TH1 *> histograms_by_category_SM_plainVars_noHH_;
  std::map<std::string, TH1 *> histograms_by_category_types_;

  std::map<std::string, TH1 *> histograms_by_category_check_jet1_pt_;
  std::map<std::string, TH1 *> histograms_by_category_check_jet1_eta_;
  std::map<std::string, TH1 *> histograms_by_category_check_lep1_pt_;
  std::map<std::string, TH1 *> histograms_by_category_check_lep1_eta_;
  std::map<std::string, TH1 *> histograms_by_category_check_jet2_pt_;
  std::map<std::string, TH1 *> histograms_by_category_check_jet2_eta_;

  int option_; // flag to enable/disable booking & filling of MEM histograms
};

#endif
