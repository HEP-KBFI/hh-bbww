#include "hhAnalysis/bbww/interface/EvtHistManager2_hh_bb1l.h"

#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h"          // cmsException()
#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), fillWithOverFlow2d()
#include "hhAnalysis/bbww/interface/JPAInterface.h"                    // get_jpaCategory_string, JPA::Category_resolved, JPA::Category_boosted

#include <TAxis.h> // TAxis
#include <TMath.h> // TMath::Pi()

EvtHistManager2_hh_bb1l::EvtHistManager2_hh_bb1l(const edm::ParameterSet & cfg)
  : HistManagerBase(cfg)
{
  central_or_shiftOptions_["numJets"] = { "central" };
  central_or_shiftOptions_["numBJets_loose"] = { "central" };
  central_or_shiftOptions_["numBJets_medium"] = { "central" };
  central_or_shiftOptions_["HT"] = { "*" };
  central_or_shiftOptions_["met"] = { "*" };
  central_or_shiftOptions_["met_LD"] = { "*" };
  central_or_shiftOptions_["lep_pt"] = { "central" };
  central_or_shiftOptions_["mll_loose"] = { "central" };
  central_or_shiftOptions_["m_Hbb"] = { "*" };
  central_or_shiftOptions_["pT_Hbb"] = { "*" };
  central_or_shiftOptions_["dR_Hbb"] = { "central" };
  central_or_shiftOptions_["m_Hbb_regCorr"] = { "*" };
  central_or_shiftOptions_["dPhi_Hww"] = { "central" };
  central_or_shiftOptions_["pT_Hww"] = { "*" };
  central_or_shiftOptions_["m_HH_B2G_18_008"] = { "*" };
  central_or_shiftOptions_["pT_HH"] = { "*" };
  central_or_shiftOptions_["dPhi_HHvis"] = { "central" };
  central_or_shiftOptions_["pT_HHvis"] = { "*" };
  central_or_shiftOptions_["mT_W"] = { "*" };
  central_or_shiftOptions_["mT_top_2particle"] = { "*" };
  central_or_shiftOptions_["mT_top_3particle"] = { "*" };
  central_or_shiftOptions_["vbf_m_jj"] = { "central" };
  central_or_shiftOptions_["vbf_dEta_jj"] = { "central" };
  central_or_shiftOptions_["vbf_lhe_m_jj"] = { "central" };
  central_or_shiftOptions_["vbf_lhe_dEta_jj"] = { "central" };
  central_or_shiftOptions_["bjet1_btagCSV"] = { "*" };
  central_or_shiftOptions_["bjet2_btagCSV"] = { "*" };
  central_or_shiftOptions_["wjet1_btagCSV"] = { "*" };
  central_or_shiftOptions_["wjet2_btagCSV"] = { "*" };
  central_or_shiftOptions_["mindr_lep1_jet"] = { "central" };
  central_or_shiftOptions_["avg_dr_jet_central"] = { "central" };
  central_or_shiftOptions_["lepPairType_loose"] = { "central" };
  central_or_shiftOptions_["selLepton_type"] = { "central" };
  central_or_shiftOptions_["mbb_medium"] = { "*" };
  central_or_shiftOptions_["dR_b1lep"] = { "central" };
  central_or_shiftOptions_["dR_b2lep"] = { "central" };
  central_or_shiftOptions_["mjj_highestpt"] = { "*" };
  central_or_shiftOptions_["numJetsForward"] = { "central" };
  central_or_shiftOptions_["tau21_Hbb"] = { "central" };
  central_or_shiftOptions_["lep_px"] = { "central" };
  central_or_shiftOptions_["lep_py"] = { "central" };
  central_or_shiftOptions_["lep_pz"] = { "central" };
  central_or_shiftOptions_["lep_e"] = { "central" };
  central_or_shiftOptions_["Hbb_lead_px"] = { "central" };
  central_or_shiftOptions_["Hbb_lead_py"] = { "central" };
  central_or_shiftOptions_["Hbb_lead_pz"] = { "central" };
  central_or_shiftOptions_["Hbb_lead_e"] = { "central" };
  central_or_shiftOptions_["Hbb_sublead_px"] = { "central" };
  central_or_shiftOptions_["Hbb_sublead_py"] = { "central" };
  central_or_shiftOptions_["Hbb_sublead_pz"] = { "central" };
  central_or_shiftOptions_["Hbb_sublead_e"] = { "central" };
  central_or_shiftOptions_["Wjj_lead_px"] = { "central" };
  central_or_shiftOptions_["Wjj_lead_py"] = { "central" };
  central_or_shiftOptions_["Wjj_lead_pz"] = { "central" };
  central_or_shiftOptions_["Wjj_lead_e"] = { "central" };
  central_or_shiftOptions_["Wjj_sublead_px"] = { "central" };
  central_or_shiftOptions_["Wjj_sublead_py"] = { "central" };
  central_or_shiftOptions_["Wjj_sublead_pz"] = { "central" };
  central_or_shiftOptions_["Wjj_sublead_e"] = { "central" };
  central_or_shiftOptions_["evtCategory"] = { "central" };
  central_or_shiftOptions_["EventCounter"] = { "*" };
}

const TH1 *
EvtHistManager2_hh_bb1l::getHistogram_EventCounter() const
{
  return histogram_EventCounter_;
}

void
EvtHistManager2_hh_bb1l::bookHistograms(TFileDirectory & dir)
{
  histogram_numJets_          = book1D(dir, "numJets",           20, -0.5, +19.5);
  histogram_numBJets_loose_   = book1D(dir, "numBJets_loose",    10, -0.5,  +9.5);
  histogram_numBJets_medium_  = book1D(dir, "numBJets_medium",   10, -0.5,  +9.5);

  histogram_HT_               = book1D(dir, "HT",               150,  0., 1500.);
  histogram_met_            = book1D(dir, "met",              100,  0., 1000.);
  histogram_met_LD_            = book1D(dir, "met_LD",              100,  0., 1000.);

  histogram_lep_pt_            = book1D(dir, "lep_pt",             100,  20.,  400.);
  histogram_mll_loose_           = book1D(dir, "mll_loose",          10,  0.,    50.);

  histogram_m_Hbb_            = book1D(dir, "m_Hbb",             40,  0.,  200.);
  histogram_dR_Hbb_           = book1D(dir, "dR_Hbb",           100,  0.,    5.);
  histogram_pT_Hbb_           = book1D(dir, "pT_Hbb",           100,  0.,  500.);
  histogram_m_Hbb_regCorr_            = book1D(dir, "m_Hbb_regCorr",    40,  0.,  200.);

  histogram_dPhi_Hww_         = book1D(dir, "dPhi_Hww",          36,  0., TMath::Pi());
  histogram_pT_Hww_           = book1D(dir, "pT_Hww",           100,  0.,  500.);

  histogram_m_HH_B2G_18_008_  = book1D(dir, "m_HH_B2G_18_008",  150,  0., 1500.);
  histogram_dPhi_HHvis_          = book1D(dir, "dPhi_HHvis",           36,  0., TMath::Pi());
  histogram_pT_HH_            = book1D(dir, "pT_HH",            100,  0.,  500.);
  histogram_pT_HHvis_          = book1D(dir, "pT_HHvis",          100,  0., 500.);

  histogram_mT_W_             = book1D(dir, "mT_W",              50,  100.,  50000.);
  histogram_mT_top_2particle_ = book1D(dir, "mT_top_2particle", 100,  100.,  100000.);
  histogram_mT_top_3particle_ = book1D(dir, "mT_top_3particle", 100,  100.,  20000.);

  histogram_vbf_m_jj_         = book1D(dir, "vbf_m_jj",         150,  0., 1500.);
  histogram_vbf_dEta_jj_      = book1D(dir, "vbf_dEta_jj",      100,  0.,   10.);
  histogram_vbf_lhe_m_jj_         = book1D(dir, "vbf_lhe_m_jj",         150,  0., 1500.);
  histogram_vbf_lhe_dEta_jj_      = book1D(dir, "vbf_lhe_dEta_jj",      100,  0.,   10.);

  histogram_bjet1_btagCSV_         = book1D(dir, "bjet1_btagCSV",         50,  0., 1.);
  histogram_bjet2_btagCSV_         = book1D(dir, "bjet2_btagCSV",         50,  0., 1.);
  histogram_wjet1_btagCSV_         = book1D(dir, "wjet1_btagCSV",         50,  0., 1.);
  histogram_wjet2_btagCSV_         = book1D(dir, "wjet2_btagCSV",         50,  0., 1.);

  histogram_mindr_lep1_jet_         = book1D(dir, "mindr_lep1_jet",         50,  0., 5.);
  histogram_avg_dr_jet_central_     = book1D(dir, "avg_dr_jet_central",         50,  0., 5.);

  histogram_lepPairType_loose_         = book1D(dir, "lepPairType_loose",         2,  0.5, 999.5);
  histogram_selLepton_type_         = book1D(dir, "selLepton_type",         2,  -0.5, 1.5);

  histogram_mbb_medium_         = book1D(dir, "mbb_medium",         40,  0., 200.);

  histogram_dR_b1lep_         = book1D(dir, "dR_b1lep",         50,  0., 5.);
  histogram_dR_b2lep_         = book1D(dir, "dR_b2lep",         50,  0., 5.);
  
  histogram_mjj_highestpt_         = book1D(dir, "mjj_highestpt",         100,  0., 1000.);

  histogram_numJetsForward_         = book1D(dir, "numJetsForward",         10,  -0.5, 10.5);
  histogram_tau21_Hbb_         = book1D(dir, "tau21_Hbb",         10,  0., 1.);

  histogram_lep_px_         = book1D(dir, "lep_px",         40,  -200., 200.);
  histogram_lep_py_         = book1D(dir, "lep_py",         40,  -200., 200.);
  histogram_lep_pz_         = book1D(dir, "lep_pz",         100,  -500., 500.);
  histogram_lep_e_         = book1D(dir, "lep_e",         50,  0., 500.);

  histogram_Hbb_lead_px_         = book1D(dir, "Hbb_lead_px",         100,  -500., 500.);
  histogram_Hbb_lead_py_     = book1D(dir, "Hbb_lead_py",         100,  -500., 500.);
  histogram_Hbb_lead_pz_         = book1D(dir, "Hbb_lead_pz",      200   ,  -1000, 1000);
  histogram_Hbb_lead_e_         = book1D(dir, "Hbb_lead_e",         150,  0, 1500);

  histogram_Hbb_sublead_px_         = book1D(dir, "Hbb_sublead_px",         100,  -500., 500.);
  histogram_Hbb_sublead_py_     = book1D(dir, "Hbb_sublead_py",         100,  -500., 500.);
  histogram_Hbb_sublead_pz_         = book1D(dir, "Hbb_sublead_pz",         200,  -1000, 1000);
  histogram_Hbb_sublead_e_         = book1D(dir, "Hbb_sublead_e",         150,  0., 1500);

  histogram_Wjj_lead_px_         = book1D(dir, "Wjj_lead_px",         100,  -500., 500.);
  histogram_Wjj_lead_py_     = book1D(dir, "Wjj_lead_py",         100,  -500., 500.);
  histogram_Wjj_lead_pz_         = book1D(dir, "Wjj_lead_pz",         200,  -1000., 1000.);
  histogram_Wjj_lead_e_         = book1D(dir, "Wjj_lead_e",         150,  0, 1500);

  histogram_Wjj_sublead_px_         = book1D(dir, "Wjj_sublead_px",         100,  -500., 500.);
  histogram_Wjj_sublead_py_     = book1D(dir, "Wjj_sublead_py",         100,  -500., 500.);
  histogram_Wjj_sublead_pz_         = book1D(dir, "Wjj_sublead_pz",         200,  -1000., 1000.);
  histogram_Wjj_sublead_e_         = book1D(dir, "Wjj_sublead_e",         150,  0., 1500.);

  /*  histogram_jpaCategory_      = book1D(dir, "jpaCategory",       15, -0.5, +14.5);
  if ( histogram_jpaCategory_ ) {
    TAxis* xAxis_jpaCategory = histogram_jpaCategory_->GetXaxis();
    for ( int jpaCategory = (int)JPA::Category_resolved::k2b2W; jpaCategory <= (int)JPA::Category_resolved::k0b; ++jpaCategory )
    {
      int idxBin = xAxis_jpaCategory->FindBin(jpaCategory);
      xAxis_jpaCategory->SetBinLabel(idxBin, get_jpaCategory_string(jpaCategory).data());
    }
    for ( int jpaCategory = (int)JPA::Category_boosted::k2b2W; jpaCategory <= (int)JPA::Category_boosted::k2b0W; ++jpaCategory )
    {
      int idxBin = xAxis_jpaCategory->FindBin(jpaCategory);
      xAxis_jpaCategory->SetBinLabel(idxBin, get_jpaCategory_string(jpaCategory).data());
    }
    }*/

  histogram_evtCategory_      = book1D(dir, "evtCategory",        4, -0.5,  +3.5);
  if ( histogram_evtCategory_ )
  {
    TAxis* xAxis_evtCategory = histogram_evtCategory_->GetXaxis();
    xAxis_evtCategory->SetBinLabel(1, "Undefined");
    xAxis_evtCategory->SetBinLabel(2, "Resolved 2b");
    xAxis_evtCategory->SetBinLabel(3, "Resolved 1b");
    xAxis_evtCategory->SetBinLabel(4, "Boosted");
  }
  histogram_EventCounter_     = book1D(dir, "EventCounter",       1, -0.5,  +0.5);
}

void
EvtHistManager2_hh_bb1l::fillHistograms(int numJets,
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
                                        double evtWeight)
{
  const double evtWeightErr = 0.;

  fillWithOverFlow(histogram_numJets_,          numJets,           evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_loose_,   numBJets_loose,    evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_medium_,  numBJets_medium,   evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_HT_,               HT,                evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_met_,              met,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_met_LD_,              met_LD,               evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_lep_pt_,              lep_pt,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mll_loose_,            mll_loose,               evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_m_Hbb_,            m_Hbb,             evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_Hbb_,           pT_Hbb,            evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dR_Hbb_,         dR_Hbb,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_m_Hbb_regCorr_,           m_Hbb_regCorr,            evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_dPhi_Hww_,           dPhi_Hww,            evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_Hww_,         pT_Hww,          evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_m_HH_B2G_18_008_,  m_HH_B2G_18_008,   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_HH_,          pT_HH,           evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_HHvis_,            dPhi_HHvis,             evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_HHvis_,          pT_HHvis,           evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_mT_W_,             mT_W,              evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT_top_2particle_, mT_top_2particle,  evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT_top_3particle_, mT_top_3particle,  evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_vbf_m_jj_,         vbf_m_jj,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_vbf_dEta_jj_,      vbf_dEta_jj,       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_vbf_lhe_m_jj_,         vbf_lhe_m_jj,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_vbf_lhe_dEta_jj_,      vbf_lhe_dEta_jj,       evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_bjet1_btagCSV_,         bjet1_btagCSV,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_bjet2_btagCSV_,      bjet2_btagCSV,       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_wjet1_btagCSV_,         wjet1_btagCSV,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_wjet2_btagCSV_,      bjet1_btagCSV,       evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_mindr_lep1_jet_,         mindr_lep1_jet,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_avg_dr_jet_central_,     avg_dr_jet_central,       evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_lepPairType_loose_,         lepPairType_loose,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_selLepton_type_,      selLepton_type,       evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_mbb_medium_,         mbb_medium,          evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_dR_b1lep_,     dR_b1lep,       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dR_b2lep_,     dR_b2lep,       evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_mjj_highestpt_,         mjj_highestpt,          evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_numJetsForward_,      numJetsForward,       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_tau21_Hbb_,      tau21_Hbb,       evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_lep_px_,     lep_px,       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep_py_,         lep_py,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep_pz_,      lep_pz,       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep_e_,      lep_e,       evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_Hbb_lead_px_,     Hbb_lead_px,       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_Hbb_lead_py_,         Hbb_lead_py,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_Hbb_lead_pz_,      Hbb_lead_pz,       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_Hbb_lead_e_,      Hbb_lead_e,       evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_Hbb_sublead_px_,     Hbb_sublead_px,       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_Hbb_sublead_py_,         Hbb_sublead_py,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_Hbb_sublead_pz_,      Hbb_sublead_pz,       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_Hbb_sublead_e_,      Hbb_sublead_e,       evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_Wjj_lead_px_,     Wjj_lead_px,       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_Wjj_lead_py_,         Wjj_lead_py,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_Wjj_lead_pz_,      Wjj_lead_pz,       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_Wjj_lead_e_,      Wjj_lead_e,       evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_Wjj_sublead_px_,     Wjj_sublead_px,       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_Wjj_sublead_py_,         Wjj_sublead_py,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_Wjj_sublead_pz_,      Wjj_sublead_pz,       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_Wjj_sublead_e_,      Wjj_sublead_e,       evtWeight, evtWeightErr);


  //  fillWithOverFlow(histogram_jpaCategory_,      jpa.jpaCategory(), evtWeight, evtWeightErr);
  
  int evtCategory = 0;
  if      ( selJetAK8_Hbb        ) evtCategory = 3;
  else if ( numBJets_medium >= 2 ) evtCategory = 2;
  else if ( numBJets_medium >= 1 ) evtCategory = 1;
  fillWithOverFlow(histogram_evtCategory_,      evtCategory,       evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_EventCounter_,     0.,                evtWeight, evtWeightErr);
}
