#include "hhAnalysis/bbww/interface/EvtHistManager2_hh_bb1l.h"

#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h"          // cmsException()
#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), fillWithOverFlow2d()
#include "hhAnalysis/bbww/interface/JPAInterface.h"                    // get_jpaCategory_string, JPA::Category_resolved, JPA::Category_boosted

#include <TAxis.h> // TAxis
#include <TMath.h> // TMath::Pi()

EvtHistManager2_hh_bb1l::EvtHistManager2_hh_bb1l(const edm::ParameterSet & cfg, const bool plot_DNN_correlation)
  : HistManagerBase(cfg)
  , plot_DNN_correlation_(plot_DNN_correlation)
{
  central_or_shiftOptions_["numJets"] = { "central" };
  central_or_shiftOptions_["numBJets_loose"] = { "central" };
  central_or_shiftOptions_["numBJets_medium"] = { "central" };
  central_or_shiftOptions_["HT"] = { "*" };
  central_or_shiftOptions_["met"] = { "*" };
  central_or_shiftOptions_["met_phi"] = { "central" };
  central_or_shiftOptions_["lepPairCharge_loose"] = { "central" };
  central_or_shiftOptions_["m_wlep"] = { "central" };
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
  central_or_shiftOptions_["m_HH_analytic"] = { "*" };
  central_or_shiftOptions_["m_HH"] = { "*" };
  central_or_shiftOptions_["m_HH_vis"] = { "*" };
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
  central_or_shiftOptions_["lep_eta"] = { "central" };
  central_or_shiftOptions_["lep_phi"] = { "central" };
  central_or_shiftOptions_["lep_e"] = { "central" };
  central_or_shiftOptions_["Hbb_lead_pt"] = { "central" };
  central_or_shiftOptions_["Hbb_lead_eta"] = { "central" };
  central_or_shiftOptions_["Hbb_lead_phi"] = { "central" };
  central_or_shiftOptions_["Hbb_lead_m"] = { "central" };
  central_or_shiftOptions_["Hbb_sublead_pt"] = { "central" };
  central_or_shiftOptions_["Hbb_sublead_eta"] = { "central" };
  central_or_shiftOptions_["Hbb_sublead_phi"] = { "central" };
  central_or_shiftOptions_["Hbb_sublead_m"] = { "central" };
  central_or_shiftOptions_["Wjj_lead_pt"] = { "central" };
  central_or_shiftOptions_["Wjj_lead_eta"] = { "central" };
  central_or_shiftOptions_["Wjj_lead_phi"] = { "central" };
  central_or_shiftOptions_["Wjj_lead_m"] = { "central" };
  central_or_shiftOptions_["Wjj_sublead_pt"] = { "central" };
  central_or_shiftOptions_["Wjj_sublead_eta"] = { "central" };
  central_or_shiftOptions_["Wjj_sublead_phi"] = { "central" };
  central_or_shiftOptions_["Wjj_sublead_m"] = { "central" };
  central_or_shiftOptions_["jet1_pt"] = { "central" };
  central_or_shiftOptions_["jet1_eta"] = { "central" };
  central_or_shiftOptions_["jet1_phi"] = { "central" };
  central_or_shiftOptions_["jet2_pt"] = { "central" };
  central_or_shiftOptions_["jet2_eta"] = { "central" };
  central_or_shiftOptions_["jet2_phi"] = { "central" };
  central_or_shiftOptions_["evtCategory"] = { "central" };
  central_or_shiftOptions_["TT_resolved_270_300_spin0"] = { "central" };
  central_or_shiftOptions_["TT_resolved_300_400_spin0"] = { "central" };
  central_or_shiftOptions_["TT_boosted_270_300_spin0"] = { "central" };
  central_or_shiftOptions_["TT_boosted_300_400_spin0"] = { "central" };
  central_or_shiftOptions_["W_270_300_spin0"] = { "central" };
  central_or_shiftOptions_["W_300_400_spin0"] = { "central" };
  central_or_shiftOptions_["Other_270_300_spin0"] = { "central" };
  central_or_shiftOptions_["Other_300_400_spin0"] = { "central" };
  central_or_shiftOptions_["HH_boosted_270_300_spin0"] = { "central" };
  central_or_shiftOptions_["HH_boosted_300_400_spin0"] = { "central" };
  central_or_shiftOptions_["HH_resolved_2b_270_300_spin0"] = { "central" };
  central_or_shiftOptions_["HH_resolved_2b_300_400_spin0"] = { "central" };
  central_or_shiftOptions_["HH_resolved_1b_270_300_spin0"] = { "central" };
  central_or_shiftOptions_["HH_resolved_1b_300_400_spin0"] = { "central" };
  central_or_shiftOptions_["TT_resolved_270_300_spin2"] = { "central" };
  central_or_shiftOptions_["TT_resolved_300_400_spin2"] = { "central" };
  central_or_shiftOptions_["TT_boosted_270_300_spin2"] = { "central" };
  central_or_shiftOptions_["TT_boosted_300_400_spin2"] = { "central" };
  central_or_shiftOptions_["W_270_300_spin2"] = { "central" };
  central_or_shiftOptions_["W_300_400_spin2"] = { "central" };
  central_or_shiftOptions_["Other_270_300_spin2"] = { "central" };
  central_or_shiftOptions_["Other_300_400_spin2"] = { "central" };
  central_or_shiftOptions_["HH_boosted_270_300_spin2"] = { "central" };
  central_or_shiftOptions_["HH_boosted_300_400_spin2"] = { "central" };
  central_or_shiftOptions_["HH_resolved_2b_270_300_spin2"] = { "central" };
  central_or_shiftOptions_["HH_resolved_2b_300_400_spin2"] = { "central" };
  central_or_shiftOptions_["HH_resolved_1b_270_300_spin2"] = { "central" };
  central_or_shiftOptions_["HH_resolved_1b_300_400_spin2"] = { "central" };
  central_or_shiftOptions_["m_Hww"] = { "central" };
  central_or_shiftOptions_["m_HH_bbregCorr"] = { "central" };
  central_or_shiftOptions_["dPhi_met_lep"] = { "central" };
  central_or_shiftOptions_["dR_lep_Wjj"] = { "central" };
  central_or_shiftOptions_["dR_lep_Hbb"] = { "central" };
  central_or_shiftOptions_["pT_wlep"] = { "central" };
  central_or_shiftOptions_["dPhi_met_Hbb"] = { "central" };
  central_or_shiftOptions_["dPhi_met_Wjj"] = { "central" };
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
  histogram_met_              = book1D(dir, "met",              100,  0., 1000.);
  histogram_met_phi_          = book1D(dir, "met_phi",          36,  0., TMath::Pi());
  histogram_lepPairCharge_loose_        = book1D(dir, "lepPairCharge_loose",          5,  -2.5, 2.5);
  histogram_m_wlep_           = book1D(dir, "m_wlep",             50,  0.,  200.);
  histogram_met_LD_            = book1D(dir, "met_LD",              100,  0., 1000.);

  histogram_mll_loose_           = book1D(dir, "mll_loose",          10,  0.,    50.);

  histogram_m_Hbb_            = book1D(dir, "m_Hbb",             40,  0.,  200.);
  histogram_dR_Hbb_           = book1D(dir, "dR_Hbb",           100,  0.,    5.);
  histogram_m_Hww_            = book1D(dir, "m_Hww",             100,  0.,  400.);
  histogram_m_HH_bbregCorr_   = book1D(dir, "m_HH_bbregCorr",    120,  0.,  1200.);
  histogram_dPhi_met_lep_     = book1D(dir, "dPhi_met_lep",      36,  0.,  TMath::Pi());
  histogram_dR_lep_Wjj_       = book1D(dir, "dR_lep_Wjj",        100,  0.,  5.);
  histogram_dR_lep_Hbb_       = book1D(dir, "dR_lep_Hbb",        100,  0.,  5.);
  histogram_pT_wlep_          = book1D(dir, "pT_wlep",           100,  0.,  500.);
  histogram_dPhi_met_Hbb_     = book1D(dir, "dPhi_met_Hbb",      36,  0.,  TMath::Pi());
  histogram_dPhi_met_Wjj_     = book1D(dir, "dPhi_met_Wjj",      36,  0.,  TMath::Pi());
  histogram_pT_Hbb_           = book1D(dir, "pT_Hbb",           100,  0.,  500.);
  histogram_m_Hbb_regCorr_            = book1D(dir, "m_Hbb_regCorr",    40,  0.,  200.);

  histogram_dPhi_Hww_         = book1D(dir, "dPhi_Hww",          36,  0., TMath::Pi());
  histogram_pT_Hww_           = book1D(dir, "pT_Hww",           100,  0.,  500.);

  histogram_m_HH_B2G_18_008_  = book1D(dir, "m_HH_B2G_18_008",  150,  0., 1500.);
  histogram_m_HH_analytic_  = book1D(dir, "m_HH_analytic",  150,  0., 1500.);
  histogram_m_HH_  = book1D(dir, "m_HH",  150,  0., 1500.);
  histogram_m_HH_vis_  = book1D(dir, "m_HH_vis",  150,  0., 1500.);
  histogram_dPhi_HHvis_          = book1D(dir, "dPhi_HHvis",           36,  0., TMath::Pi());
  histogram_pT_HH_            = book1D(dir, "pT_HH",            100,  0.,  500.);
  histogram_pT_HHvis_          = book1D(dir, "pT_HHvis",          100,  0., 500.);

  histogram_mT_W_             = book1D(dir, "mT_W",              40,  0.,  200.);
  histogram_mT_top_2particle_ = book1D(dir, "mT_top_2particle", 100,  0.,  400.);
  histogram_mT_top_3particle_ = book1D(dir, "mT_top_3particle", 100,  0.,  400.);

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
  histogram_tau21_Hbb_         = book1D(dir, "tau21_Hbb",         50,  0., 1.);

  histogram_lep_pt_         = book1D(dir, "lep_pt",         40,  0., 200.);
  histogram_lep_eta_         = book1D(dir, "lep_eta",         40,  0., 2.5);
  histogram_lep_phi_         = book1D(dir, "lep_phi",         36,  0., TMath::Pi());
  histogram_lep_e_         = book1D(dir, "lep_e",         50,  0., 500.);

  histogram_Hbb_lead_pt_         = book1D(dir, "Hbb_lead_pt",         100,  0., 500.);
  histogram_Hbb_lead_eta_     = book1D(dir, "Hbb_lead_eta",         40,  0., 2.5);
  histogram_Hbb_lead_phi_         = book1D(dir, "Hbb_lead_phi",      36,  0, TMath::Pi());
  histogram_Hbb_lead_m_         = book1D(dir, "Hbb_lead_m",         50,  0, 20.);

  histogram_Hbb_sublead_pt_         = book1D(dir, "Hbb_sublead_pt",         100,  0., 500.);
  histogram_Hbb_sublead_eta_     = book1D(dir, "Hbb_sublead_eta",         40,  0., 2.5);
  histogram_Hbb_sublead_phi_         = book1D(dir, "Hbb_sublead_phi",         36,  0, TMath::Pi());
  histogram_Hbb_sublead_m_         = book1D(dir, "Hbb_sublead_m",         50,  0., 20);

  histogram_Wjj_lead_pt_         = book1D(dir, "Wjj_lead_pt",         100,  0., 500.);
  histogram_Wjj_lead_eta_     = book1D(dir, "Wjj_lead_eta",         40,  0., 2.5);
  histogram_Wjj_lead_phi_         = book1D(dir, "Wjj_lead_phi",         36,  0., TMath::Pi());
  histogram_Wjj_lead_m_         = book1D(dir, "Wjj_lead_m",         50,  0, 20);

  histogram_Wjj_sublead_pt_         = book1D(dir, "Wjj_sublead_pt",         100,  0., 500.);
  histogram_Wjj_sublead_eta_     = book1D(dir, "Wjj_sublead_eta",         40,  0., 2.5);
  histogram_Wjj_sublead_phi_         = book1D(dir, "Wjj_sublead_phi",         36,  0., TMath::Pi());
  histogram_Wjj_sublead_m_         = book1D(dir, "Wjj_sublead_m",         50,  0., 20.);
  
  histogram_jet1_pt_         = book1D(dir, "jet1_pt",         100,  0., 500.);
  histogram_jet1_eta_     = book1D(dir, "jet1_eta",         40,  0., 2.5);
  histogram_jet1_phi_         = book1D(dir, "jet1_phi",         36,  0., TMath::Pi());

  histogram_jet2_pt_         = book1D(dir, "jet2_pt",         100,  0., 500.);
  histogram_jet2_eta_     = book1D(dir, "jet2_eta",         40,  0., 2.5);
  histogram_jet2_phi_         = book1D(dir, "jet2_phi",         36,  0., TMath::Pi());

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
  if ( plot_DNN_correlation_ ) {
    histogram_TT_resolved_270_300_spin2_ = book2D(dir, "TT_resolved_270_300_spin2",       10, 0,  1., 10, 0., 1.);
    histogram_TT_resolved_300_400_spin2_ = book2D(dir, "TT_resolved_300_400_spin2",       10, 0,  1., 10, 0., 1.);
    histogram_TT_boosted_270_300_spin2_ = book2D(dir, "TT_boosted_270_300_spin2",       10, 0,  1., 10, 0., 1.);
    histogram_TT_boosted_300_400_spin2_ = book2D(dir, "TT_boosted_300_400_spin2",       10, 0,  1., 10, 0., 1.);
    histogram_W_270_300_spin2_ = book2D(dir, "W_270_300_spin2",       10, 0,  1., 10, 0., 1.);
    histogram_W_300_400_spin2_ = book2D(dir, "W_300_400_spin2",       10, 0,  1., 10, 0., 1.);
    histogram_Other_270_300_spin2_ = book2D(dir, "Other_270_300_spin2",       10, 0,  1., 10, 0., 1.);
    histogram_Other_300_400_spin2_ = book2D(dir, "Other_300_400_spin2",       10, 0,  1., 10, 0., 1.);
    histogram_HH_resolved_2b_270_300_spin2_ = book2D(dir, "HH_resolved_2b_270_300_spin2",       10, 0,  1., 10, 0., 1.);
    histogram_HH_resolved_2b_300_400_spin2_ = book2D(dir, "HH_resolved_2b_300_400_spin2",       10, 0,  1., 10, 0., 1.);
    histogram_HH_resolved_1b_270_300_spin2_ = book2D(dir, "HH_resolved_1b_270_300_spin2",       10, 0,  1., 10, 0., 1.);
    histogram_HH_resolved_1b_300_400_spin2_ = book2D(dir, "HH_resolved_1b_300_400_spin2",       10, 0,  1., 10, 0., 1.);
    histogram_HH_boosted_270_300_spin2_ = book2D(dir, "HH_boosted_270_300_spin2",       10, 0,  1., 10, 0., 1.);
    histogram_HH_boosted_300_400_spin2_ = book2D(dir, "HH_boosted_300_400_spin2",       10, 0,  1., 10, 0., 1.);
    //spin0
    histogram_TT_resolved_270_300_spin0_ = book2D(dir, "TT_resolved_270_300_spin0",       10, 0,  1., 10, 0., 1.);
    histogram_TT_resolved_300_400_spin0_ = book2D(dir, "TT_resolved_300_400_spin0",       10, 0,  1., 10, 0., 1.);
    histogram_TT_boosted_270_300_spin0_ = book2D(dir, "TT_boosted_270_300_spin0",       10, 0,  1., 10, 0., 1.);
    histogram_TT_boosted_300_400_spin0_ = book2D(dir, "TT_boosted_300_400_spin0",       10, 0,  1., 10, 0., 1.);
    histogram_W_270_300_spin0_ = book2D(dir, "W_270_300_spin0",       10, 0,  1., 10, 0., 1.);
    histogram_W_300_400_spin0_ = book2D(dir, "W_300_400_spin0",       10, 0,  1., 10, 0., 1.);
    histogram_Other_270_300_spin0_ = book2D(dir, "Other_270_300_spin0",       10, 0,  1., 10, 0., 1.);
    histogram_Other_300_400_spin0_ = book2D(dir, "Other_300_400_spin0",       10, 0,  1., 10, 0., 1.);
    histogram_HH_resolved_2b_270_300_spin0_ = book2D(dir, "HH_resolved_2b_270_300_spin0",       10, 0,  1., 10, 0., 1.);
    histogram_HH_resolved_2b_300_400_spin0_ = book2D(dir, "HH_resolved_2b_300_400_spin0",       10, 0,  1., 10, 0., 1.);
    histogram_HH_resolved_1b_270_300_spin0_ = book2D(dir, "HH_resolved_1b_270_300_spin0",       10, 0,  1., 10, 0., 1.);
    histogram_HH_resolved_1b_300_400_spin0_ = book2D(dir, "HH_resolved_1b_300_400_spin0",       10, 0,  1., 10, 0., 1.);
    histogram_HH_boosted_270_300_spin0_ = book2D(dir, "HH_boosted_270_300_spin0",       10, 0,  1., 10, 0., 1.);
    histogram_HH_boosted_300_400_spin0_ = book2D(dir, "HH_boosted_300_400_spin0",       10, 0,  1., 10, 0., 1.);
  }
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
                                        double evtWeight)
{
  const double evtWeightErr = 0.;

  fillWithOverFlow(histogram_numJets_,          numJets,           evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_loose_,   numBJets_loose,    evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_medium_,  numBJets_medium,   evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_HT_,               HT,                evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_met_,              met,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_met_phi_,              met_phi,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lepPairCharge_loose_,              lepPairCharge_loose,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_m_wlep_,              m_wlep,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_met_LD_,              met_LD,               evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_lep_pt_,              lep_pt,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mll_loose_,            mll_loose,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_m_Hww_,            m_Hww,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_m_HH_bbregCorr_,   m_HH_bbregCorr,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_met_lep_,   dPhi_met_lep,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dR_lep_Wjj_,   dR_lep_Wjj,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dR_lep_Hbb_,   dR_lep_Hbb,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_wlep_,   pT_wlep,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_met_Hbb_,   dPhi_met_Hbb,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_met_Wjj_,   dPhi_met_Wjj,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_m_Hbb_,            m_Hbb,             evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_Hbb_,           pT_Hbb,            evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dR_Hbb_,         dR_Hbb,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_m_Hbb_regCorr_,           m_Hbb_regCorr,            evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_dPhi_Hww_,           dPhi_Hww,            evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_Hww_,         pT_Hww,          evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_m_HH_B2G_18_008_,  m_HH_B2G_18_008,   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_m_HH_analytic_,  m_HH_analytic,   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_m_HH_vis_,  m_HH_vis,   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_m_HH_,  m_HH,   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_HH_,          pT_HH,           evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_HHvis_,            dPhi_HHvis,             evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_HHvis_,          pT_HHvis,           evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_mT_W_,             std::sqrt(mT_W),              evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT_top_2particle_, std::sqrt(mT_top_2particle),  evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT_top_3particle_, std::sqrt(mT_top_3particle),  evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_vbf_m_jj_,         vbf_m_jj,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_vbf_dEta_jj_,      vbf_dEta_jj,       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_vbf_lhe_m_jj_,         vbf_lhe_m_jj,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_vbf_lhe_dEta_jj_,      vbf_lhe_dEta_jj,       evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_bjet1_btagCSV_,         bjet1_btagCSV,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_bjet2_btagCSV_,      bjet2_btagCSV,       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_wjet1_btagCSV_,         wjet1_btagCSV,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_wjet2_btagCSV_,      wjet2_btagCSV,       evtWeight, evtWeightErr);

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

  fillWithOverFlow(histogram_lep_eta_,         lep_eta,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep_phi_,      lep_phi,       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep_e_,      lep_e,       evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_Hbb_lead_pt_,     Hbb_lead_pt,       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_Hbb_lead_eta_,         Hbb_lead_eta,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_Hbb_lead_phi_,      Hbb_lead_phi,       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_Hbb_lead_m_,      Hbb_lead_m,       evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_Hbb_sublead_pt_,     Hbb_sublead_pt,       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_Hbb_sublead_eta_,         Hbb_sublead_eta,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_Hbb_sublead_phi_,      Hbb_sublead_phi,       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_Hbb_sublead_m_,      Hbb_sublead_m,       evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_Wjj_lead_pt_,     Wjj_lead_pt,       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_Wjj_lead_eta_,         Wjj_lead_eta,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_Wjj_lead_phi_,      Wjj_lead_phi,       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_Wjj_lead_m_,      Wjj_lead_m,       evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_Wjj_sublead_pt_,     Wjj_sublead_pt,       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_Wjj_sublead_eta_,         Wjj_sublead_eta,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_Wjj_sublead_phi_,      Wjj_sublead_phi,       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_Wjj_sublead_m_,      Wjj_sublead_m,       evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_jet1_pt_,     jet1_pt,       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_jet1_eta_,         jet1_eta,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_jet1_phi_,      jet1_phi,       evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_jet2_pt_,     jet2_pt,       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_jet2_eta_,      jet2_eta,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_jet2_phi_,      jet2_phi,       evtWeight, evtWeightErr);


  //  fillWithOverFlow(histogram_jpaCategory_,      jpa.jpaCategory(), evtWeight, evtWeightErr);
  
  int evtCategory = 0;
  if      ( selJetAK8_Hbb        ) evtCategory = 3;
  else if ( numBJets_medium >= 2 ) evtCategory = 2;
  else if ( numBJets_medium >= 1 ) evtCategory = 1;
  fillWithOverFlow(histogram_evtCategory_,      evtCategory,       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_EventCounter_,     0.,                evtWeight, evtWeightErr);

  if ( plot_DNN_correlation_ ) {
    for ( std::map<std::string, std::map<std::string, double>>::const_iterator gen_mHH_or_bmName = lbnOutputs_resonant_spin2.begin();
          gen_mHH_or_bmName != lbnOutputs_resonant_spin2.end(); ++gen_mHH_or_bmName ) {
      if ( (gen_mHH_or_bmName->first == "270_spin2" || gen_mHH_or_bmName->first == "300_spin2" || gen_mHH_or_bmName->first == "400_spin2") ) {
        for ( std::map<std::string, double>::const_iterator classIter = gen_mHH_or_bmName->second.begin();
              classIter != gen_mHH_or_bmName->second.end(); ++classIter ) {
          //std::cout << classIter->first << "\t" << classIter->second << std::endl;
          if ( gen_mHH_or_bmName->first == "270_spin2" ) {
            if ( classIter->first == "TT" || classIter->first == "ST" ) {
              TT_270_spin2 = classIter->second;
            }else if ( classIter->first == "W") {
              W_270_spin2 = classIter->second;
            }else if ( classIter->first == "Other" || classIter->first == "H" ) {
              Other_270_spin2 = classIter->second;
            }else if ( classIter->first == "HH" ) {
              HH_270_spin2 = classIter->second;
            }
          }
          else if ( gen_mHH_or_bmName->first == "300_spin2" ) {
            if ( classIter->first == "TT" || classIter->first == "ST" ) {
              TT_300_spin2 = classIter->second;
            }else if ( classIter->first == "W") {
              W_300_spin2 = classIter->second;
            }else if ( classIter->first == "Other" || classIter->first == "H" ) {
              Other_300_spin2 = classIter->second;
            }else if ( classIter->first == "HH" ) {
              HH_300_spin2 = classIter->second;
            }
          }
          else if ( gen_mHH_or_bmName->first == "400_spin2" ) {
            if ( classIter->first == "TT" || classIter->first == "ST" ) {
              TT_400_spin2 = classIter->second;
            }else if ( classIter->first == "W") {
              W_400_spin2 = classIter->second;
            }else if ( classIter->first == "Other" || classIter->first == "H" ) {
              Other_400_spin2 = classIter->second;
            }else if ( classIter->first == "HH" ) {
              HH_400_spin2 = classIter->second;
            }
          }
        }
      }
    }
    for ( std::map<std::string, std::map<std::string, double>>::const_iterator gen_mHH_or_bmName = lbnOutputs_resonant_spin0.begin();
          gen_mHH_or_bmName != lbnOutputs_resonant_spin0.end(); ++gen_mHH_or_bmName ) {
      if ( (gen_mHH_or_bmName->first == "270_spin0" || gen_mHH_or_bmName->first == "300_spin0" || gen_mHH_or_bmName->first == "400_spin0") ) {
        for ( std::map<std::string, double>::const_iterator classIter = gen_mHH_or_bmName->second.begin();
              classIter != gen_mHH_or_bmName->second.end(); ++classIter ) {
          if ( gen_mHH_or_bmName->first == "270_spin0" ) {
            if ( classIter->first == "TT" || classIter->first == "ST" ) {
              TT_270_spin0 = classIter->second;
            }else if ( classIter->first == "W") {
              W_270_spin0 = classIter->second;
            }else if ( classIter->first == "Other" || classIter->first == "H" ) {
              Other_270_spin0 = classIter->second;
            }else if ( classIter->first == "HH" ) {
              HH_270_spin0 = classIter->second;
            }
          }
          else if ( gen_mHH_or_bmName->first == "300_spin0" ) {
            if ( classIter->first == "TT" || classIter->first == "ST" ) {
              TT_300_spin0 = classIter->second;
            }else if ( classIter->first == "W") {
              W_300_spin0 = classIter->second;
            }else if ( classIter->first == "Other" || classIter->first == "H" ) {
              Other_300_spin0 = classIter->second;
            }else if ( classIter->first == "HH" ) {
              HH_300_spin0 = classIter->second;
            }
          }
          else if ( gen_mHH_or_bmName->first == "400_spin0" ) {
            if ( classIter->first == "TT" || classIter->first == "ST" ) {
              TT_400_spin0 = classIter->second;
            }else if ( classIter->first == "W") {
              W_400_spin0 = classIter->second;
            }else if ( classIter->first == "Other" || classIter->first == "H" ) {
              Other_400_spin0 = classIter->second;
            }else if ( classIter->first == "HH" ) {
              HH_400_spin0 = classIter->second;
            }
          }
        }
      }
    }
    if ( selJetAK8_Hbb ) {
      fillWithOverFlow2d(histogram_TT_boosted_270_300_spin2_, TT_270_spin2, TT_300_spin2, evtWeight, evtWeightErr);
      fillWithOverFlow2d(histogram_TT_boosted_300_400_spin2_, TT_300_spin2, TT_400_spin2, evtWeight, evtWeightErr);
      fillWithOverFlow2d(histogram_HH_boosted_270_300_spin2_, HH_270_spin2, HH_300_spin2, evtWeight, evtWeightErr);
      fillWithOverFlow2d(histogram_HH_boosted_300_400_spin2_, HH_300_spin2, HH_400_spin2, evtWeight, evtWeightErr);
      fillWithOverFlow2d(histogram_TT_boosted_270_300_spin0_, TT_270_spin0, TT_300_spin0, evtWeight, evtWeightErr);
      fillWithOverFlow2d(histogram_TT_boosted_300_400_spin0_, TT_300_spin0, TT_400_spin0, evtWeight, evtWeightErr);
      fillWithOverFlow2d(histogram_HH_boosted_270_300_spin0_, HH_270_spin0, HH_300_spin0, evtWeight, evtWeightErr);
      fillWithOverFlow2d(histogram_HH_boosted_300_400_spin0_, HH_300_spin0, HH_400_spin0, evtWeight, evtWeightErr);
    }
    else {
      fillWithOverFlow2d(histogram_TT_resolved_270_300_spin2_, TT_270_spin2, TT_300_spin2, evtWeight, evtWeightErr);
      fillWithOverFlow2d(histogram_TT_resolved_300_400_spin2_, TT_300_spin2, TT_400_spin2, evtWeight, evtWeightErr);
      fillWithOverFlow2d(histogram_W_270_300_spin2_, W_270_spin2, W_300_spin2, evtWeight, evtWeightErr);
      fillWithOverFlow2d(histogram_W_300_400_spin2_, W_300_spin2, W_400_spin2, evtWeight, evtWeightErr);
      fillWithOverFlow2d(histogram_Other_270_300_spin2_, Other_270_spin2, Other_300_spin2, evtWeight, evtWeightErr);
      fillWithOverFlow2d(histogram_Other_300_400_spin2_, Other_300_spin2, Other_400_spin2, evtWeight, evtWeightErr);
      fillWithOverFlow2d(histogram_TT_resolved_270_300_spin0_, TT_270_spin0, TT_300_spin0, evtWeight, evtWeightErr);
      fillWithOverFlow2d(histogram_TT_resolved_300_400_spin0_, TT_300_spin0, TT_400_spin0, evtWeight, evtWeightErr);
      fillWithOverFlow2d(histogram_W_270_300_spin0_, W_270_spin0, W_300_spin0, evtWeight, evtWeightErr);
      fillWithOverFlow2d(histogram_W_300_400_spin0_, W_300_spin0, W_400_spin0, evtWeight, evtWeightErr);
      fillWithOverFlow2d(histogram_Other_270_300_spin0_, Other_270_spin0, Other_300_spin0, evtWeight, evtWeightErr);
      fillWithOverFlow2d(histogram_Other_300_400_spin0_, Other_300_spin0, Other_400_spin0, evtWeight, evtWeightErr);
      if ( numBJets_medium == 2 ) {
        fillWithOverFlow2d(histogram_HH_resolved_2b_270_300_spin2_, HH_270_spin2, HH_300_spin2, evtWeight, evtWeightErr);
        fillWithOverFlow2d(histogram_HH_resolved_2b_300_400_spin2_, HH_300_spin2, HH_400_spin2, evtWeight, evtWeightErr);
        fillWithOverFlow2d(histogram_HH_resolved_2b_270_300_spin0_, HH_270_spin0, HH_300_spin0, evtWeight, evtWeightErr);
        fillWithOverFlow2d(histogram_HH_resolved_2b_300_400_spin0_, HH_300_spin0, HH_400_spin0, evtWeight, evtWeightErr);
      }
      else if ( numBJets_medium ==1) {
        fillWithOverFlow2d(histogram_HH_resolved_1b_270_300_spin2_, HH_270_spin2, HH_300_spin2, evtWeight, evtWeightErr);
        fillWithOverFlow2d(histogram_HH_resolved_1b_300_400_spin2_, HH_300_spin2, HH_400_spin2, evtWeight, evtWeightErr);
        fillWithOverFlow2d(histogram_HH_resolved_1b_270_300_spin0_, HH_270_spin0, HH_300_spin0, evtWeight, evtWeightErr);
        fillWithOverFlow2d(histogram_HH_resolved_1b_300_400_spin0_, HH_300_spin0, HH_400_spin0, evtWeight, evtWeightErr);
      }
    }
  }
}
