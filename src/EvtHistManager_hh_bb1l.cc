#include "hhAnalysis/bbww/interface/EvtHistManager_hh_bb1l.h"

#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h" // cmsException()
#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), fillWithOverFlow2d()

#include <TMath.h> // TMath::Pi()

EvtHistManager_hh_bb1l::EvtHistManager_hh_bb1l(const edm::ParameterSet & cfg)
  : HistManagerBase(cfg)
{
  std::string option_string = cfg.getParameter<std::string>("option");
  if ( option_string == "memDisabled" ) {
    option_ = kOption_memDisabled;
  } else if ( option_string == "memEnabled" ) {
    option_ = kOption_memEnabled;
  } else {
    throw cmsException(__func__) << "Invalid Configuration parameter 'option' = " << option_string << " !!";
  }

  central_or_shiftOptions_["numElectrons"] = { "central" };
  central_or_shiftOptions_["numMuons"] = { "central" };
  central_or_shiftOptions_["numJets"] = { "central" };
  central_or_shiftOptions_["numBJets_loose"] = { "central" };
  central_or_shiftOptions_["numBJets_medium"] = { "central" };
  central_or_shiftOptions_["HT"] = { "central" };
  central_or_shiftOptions_["STMET"] = { "central" };
  central_or_shiftOptions_["m_Hbb"] = { "central" };
  central_or_shiftOptions_["dR_Hbb"] = { "central" };
  central_or_shiftOptions_["dPhi_Hbb"] = { "central" };
  central_or_shiftOptions_["pT_Hbb"] = { "central" };
  central_or_shiftOptions_["m_Wjj"] = { "central" };
  central_or_shiftOptions_["dR_Wjj"] = { "central" };
  central_or_shiftOptions_["dPhi_Wjj"] = { "central" };
  central_or_shiftOptions_["pT_Wjj"] = { "central" };
  central_or_shiftOptions_["dR_Hww"] = { "central" };
  central_or_shiftOptions_["dPhi_Hww"] = { "central" };
  central_or_shiftOptions_["pT_Hww"] = { "central" };
  central_or_shiftOptions_["Smin_Hww"] = { "central" };
  central_or_shiftOptions_["m_HHvis"] = { "*" };
  central_or_shiftOptions_["m_HH"] = { "central" };
  central_or_shiftOptions_["m_HH_B2G_18_008"] = { "*" };
  central_or_shiftOptions_["m_HH_hme"] = { "central" }; // CV: to be replaced by "*" once HME is implemented !!
  central_or_shiftOptions_["dR_HH"] = { "central" };
  central_or_shiftOptions_["dPhi_HH"] = { "central" };
  central_or_shiftOptions_["pT_HH"] = { "central" };
  central_or_shiftOptions_["Smin_HH"] = { "central" };
  central_or_shiftOptions_["mT_W"] = { "central" };
  central_or_shiftOptions_["mT_top_2particle"] = { "central" };
  central_or_shiftOptions_["mT_top_3particle"] = { "central" };
  central_or_shiftOptions_["mvaOutput_Hj_tagger"] = { "central" };
  central_or_shiftOptions_["mvaOutput_Hjj_tagger"] = { "central" };
  central_or_shiftOptions_["vbf_jet1_pt"] = { "central" };
  central_or_shiftOptions_["vbf_jet1_eta"] = { "central" };
  central_or_shiftOptions_["vbf_jet2_pt"] = { "central" };
  central_or_shiftOptions_["vbf_jet2_eta"] = { "central" };
  central_or_shiftOptions_["vbf_m_jj"] = { "central" };
  central_or_shiftOptions_["vbf_dEta_jj"] = { "central" };
  central_or_shiftOptions_["log_memProb_signal"] = { "central" };
  central_or_shiftOptions_["log_memProbErr_signal"] = { "central" };
  central_or_shiftOptions_["log_memProb_background"] = { "central" };
  central_or_shiftOptions_["log_memProbErr_background"] = { "central" };
  central_or_shiftOptions_["memLR"] = { "*" };
  central_or_shiftOptions_["log_memLR_div_Err"] = { "central" };
  central_or_shiftOptions_["memScore"] = { "*" };
  central_or_shiftOptions_["memCpuTime"] = { "central" };
  central_or_shiftOptions_["EventCounter"] = { "*" };
}

const TH1 *
EvtHistManager_hh_bb1l::getHistogram_EventCounter() const
{
  return histogram_EventCounter_;
}

void
EvtHistManager_hh_bb1l::bookCategories(TFileDirectory & dir,
    const std::map<std::string, std::vector<double>> & categories_list_bins,
    const std::vector<std::string> for_categories_map,
    bool doDataMCPlots
  )
{
    for(auto typeMVA: for_categories_map)
    {
      for(auto category: categories_list_bins)
      {
        std::string name_test = typeMVA + category.first;
        //std::cout<< "Booked histo: " << name_test <<"\n";
        if(! category.second.empty())
        {
          const int npoints = category.second.size();
          Float_t binsx[npoints];
          std::copy(category.second.begin(), category.second.end(), binsx);
          histograms_by_category_types_[name_test] = book1D(dir, name_test, category.first, npoints - 1, binsx);
        }
        else
        {
          histograms_by_category_types_[name_test] = book1D(dir, name_test, category.first, 400,  0., +1.);
	  /*histograms_by_category_types_[name_test+"_leppt"] = book1D(dir, name_test+"_leppt", category.first+"_leppt", 50,  0., 200.);
	  histograms_by_category_types_[name_test+"_bjet1pt"] = book1D(dir, name_test+"_bjet1pt", category.first+"_bjet1pt", 50,  0., 400.);
	  histograms_by_category_types_[name_test+"_mht"] = book1D(dir, name_test+"_mht", category.first+"_mht", 50,  0., 200.);
	  histograms_by_category_types_[name_test+"_m_Hbb_regCorr"] = book1D(dir, name_test+"_m_Hbb_regCorr", category.first+"_m_Hbb_regCorr", 50,  0., 200.);
	  histograms_by_category_types_[name_test+"_m_Wjj"] = book1D(dir, name_test+"_m_Wjj", category.first+"_mWjj", 50,  0., 200.);
	  histograms_by_category_types_[name_test+"_pT_Wjj"] = book1D(dir, name_test+"_pT_Wjj", category.first+"_ptWjj", 50,  0., 400.);
	  histograms_by_category_types_[name_test+"_dR_Hww"] = book1D(dir, name_test+"_dR_Hww", category.first+"_drHww", 50,  0.,10.);
	  histograms_by_category_types_[name_test+"_Smin_Hww"] = book1D(dir, name_test+"_SminHww", category.first+"_SminHww", 50,  0., 400.);
	  histograms_by_category_types_[name_test+"_dR_b1lep"] = book1D(dir, name_test+"_dR_b1lep", category.first+"_dR_b1lep", 50,  0., 10.);
	  histograms_by_category_types_[name_test+"_dR_b2lep"] = book1D(dir, name_test+"_dR_b2lep", category.first+"_dR_b2lep", 50,  0., 10.);
	  histograms_by_category_types_[name_test+"_pT_HH"] = book1D(dir, name_test+"_pT_HH", category.first+"_pTHH", 50,  0., 400.);
	  histograms_by_category_types_[name_test+"_mTW"] = book1D(dir, name_test+"_mTW", category.first+"_mTW", 100,  0., 50000.);
	  histograms_by_category_types_[name_test+"_mT_top_3particle"] = book1D(dir, name_test+"_mT_top_3particle", category.first+"_mTtop3part", 100,  0., 50000.);
	  histograms_by_category_types_[name_test+"_mindr_lep1_jet"] = book1D(dir, name_test+"_mindr_lep1_jet", category.first+"_mindrlepjet", 50,  0., 10.);
	  histograms_by_category_types_[name_test+"_avg_dr_jet_central"] = book1D(dir, name_test+"_avg_dr_jetcentral", category.first+"_avgdrjetcentral", 50,  0., 10.);
	  histograms_by_category_types_[name_test+"_mbb_loose"] = book1D(dir, name_test+"_mbb_loose", category.first+"_mbb_loose", 50,  0., 400.);
	  histograms_by_category_types_[name_test+"_mbb_medium"] = book1D(dir, name_test+"_mbb_medium", category.first+"_mbb_medium", 50,  0., 400.);
	  histograms_by_category_types_[name_test+"_cosThetaS_Hbb_reg"] = book1D(dir, name_test+"_costhetaS_Hbb_reg", category.first+"_costhetaS_Hbb_reg", 20,  0., 1.);
	  histograms_by_category_types_[name_test+"_cosThetaS_HH"] = book1D(dir, name_test+"_costhetaS_HH", category.first+"_costhetasS_HH", 50,  0., 1.);*/
        }
        central_or_shiftOptions_[name_test] = { "*" };
      }
    }
    ///////////////////////////////
    if ( doDataMCPlots )
    {
      for(auto category: categories_list_bins)
      {
        histograms_by_category_check_jet1_pt_[category.first] = book1D(dir, "jet1_pt" + category.first, category.first, 40,  0., 200.);
        histograms_by_category_check_jet1_eta_[category.first] = book1D(dir, "jet1_eta" + category.first, category.first, 22,  -3., +3.);
        histograms_by_category_check_lep1_pt_[category.first] = book1D(dir, "lep1_pt" + category.first, category.first, 60,  0., +300.);
        histograms_by_category_check_lep1_eta_[category.first] = book1D(dir, "lep1_eta" + category.first, category.first, 22,  -3., +3.);
        histograms_by_category_check_jet2_pt_[category.first] = book1D(dir, "jet2_pt" + category.first, category.first, 40,  0., 200.);
        histograms_by_category_check_jet2_eta_[category.first] = book1D(dir, "jet2_eta" + category.first, category.first, 22,  -3., +3.);
        central_or_shiftOptions_[category.first] = { "*" };
    }
    }
}


void
EvtHistManager_hh_bb1l::bookHistograms(TFileDirectory & dir)
{
  histogram_numElectrons_                = book1D(dir, "numElectrons",                5,   -0.5,  +4.5);
  histogram_numMuons_                    = book1D(dir, "numMuons",                    5,   -0.5,  +4.5);
  histogram_numJets_                     = book1D(dir, "numJets",                    20,   -0.5, +19.5);
  histogram_numBJets_loose_              = book1D(dir, "numBJets_loose",             10,   -0.5,  +9.5);
  histogram_numBJets_medium_             = book1D(dir, "numBJets_medium",            10,   -0.5,  +9.5);

  histogram_HT_                          = book1D(dir, "HT",                        150,    0., 1500.);
  histogram_STMET_                       = book1D(dir, "STMET",                     150,    0., 1500.);

  histogram_m_Hbb_                       = book1D(dir, "m_Hbb",                      40,    0.,  200.);
  histogram_dR_Hbb_                      = book1D(dir, "dR_Hbb",                    100,    0.,    5.);
  histogram_dPhi_Hbb_                    = book1D(dir, "dPhi_Hbb",                   36,    0., TMath::Pi());
  histogram_pT_Hbb_                      = book1D(dir, "pT_Hbb",                    100,    0.,  500.);

  histogram_m_Wjj_                       = book1D(dir, "m_Wjj",                      40,    0.,  200.);
  histogram_dR_Wjj_                      = book1D(dir, "dR_Wjj",                    100,    0.,    5.);
  histogram_dPhi_Wjj_                    = book1D(dir, "dPhi_Wjj",                   36,    0., TMath::Pi());
  histogram_pT_Wjj_                      = book1D(dir, "pT_Wjj",                    100,    0.,  500.);

  histogram_dR_Hww_                      = book1D(dir, "dR_Hww",                    100,    0.,    5.);
  histogram_dPhi_Hww_                    = book1D(dir, "dPhi_Hww",                   36,    0., TMath::Pi());
  histogram_pT_Hww_                      = book1D(dir, "pT_Hww",                    100,    0.,  500.);
  histogram_Smin_Hww_                    = book1D(dir, "Smin_Hww",                  100,    0.,  500.);

  histogram_m_HHvis_                     = book1D(dir, "m_HHvis",                   100,    0., 1000.);
  histogram_m_HH_                        = book1D(dir, "m_HH",                      150,    0., 1500.);
  histogram_m_HH_B2G_18_008_             = book1D(dir, "m_HH_B2G_18_008",           150,    0., 1500.);
  histogram_m_HH_hme_                    = book1D(dir, "m_HH_hme",                  150,    0., 1500.);
  histogram_dR_HH_                       = book1D(dir, "dR_HH",                     100,    0.,    5.);
  histogram_dPhi_HH_                     = book1D(dir, "dPhi_HH",                    36,    0., TMath::Pi());
  histogram_pT_HH_                       = book1D(dir, "pT_HH",                     100,    0.,  500.);
  histogram_Smin_HH_                     = book1D(dir, "Smin_HH",                   100,    0., 1000.);

  histogram_mT_W_                        = book1D(dir, "mT_W",                       40,    0.,  200.);
  histogram_mT_top_2particle_            = book1D(dir, "mT_top_2particle",          100,    0.,  500.);
  histogram_mT_top_3particle_            = book1D(dir, "mT_top_3particle",          100,    0.,  500.);

  histogram_mvaOutput_Hj_tagger_         = book1D(dir, "mvaOutput_Hj_tagger",        40,   -1.,   +1.);
  histogram_mvaOutput_Hjj_tagger_        = book1D(dir, "mvaOutput_Hjj_tagger",       40,   -1.,   +1.);

  histogram_vbf_jet1_pt_                 = book1D(dir, "vbf_jet1_pt",                40,    0.,  200.);
  histogram_vbf_jet1_eta_                = book1D(dir, "vbf_jet1_eta",              100,   -5.0,  +5.0);
  histogram_vbf_jet2_pt_                 = book1D(dir, "vbf_jet2_pt",                40,    0.,  200.);
  histogram_vbf_jet2_eta_                = book1D(dir, "vbf_jet2_eta",              100,   -5.0,  +5.0);
  histogram_vbf_m_jj_                    = book1D(dir, "vbf_m_jj",                  150,    0., 1500.);
  histogram_vbf_dEta_jj_                 = book1D(dir, "vbf_dEta_jj",               100,    0.,   10.);

  if ( option_ == kOption_memEnabled ) {
    histogram_log_memProb_signal_        = book1D(dir, "log_memProb_signal",        200, -200.,   0.);
    histogram_log_memProbErr_signal_     = book1D(dir, "log_memProbErr_signal",     200, -200.,    0.);
    histogram_log_memProb_background_    = book1D(dir, "log_memProb_background",    200, -200.,    0.);
    histogram_log_memProbErr_background_ = book1D(dir, "log_memProbErr_background", 200, -200.,    0.);
    histogram_memLR_                     = book1D(dir, "memLR",                     360,    0.,    1.);
    histogram_log_memLR_div_Err_         = book1D(dir, "log_memLR_div_Err",         200,  -10.,  +10.);
    histogram_memScore_                  = book1D(dir, "memScore",                  360,  -18.,  +18.);
    histogram_memCpuTime_                = book1D(dir, "memCpuTime",                100,    0., 1000.);
  }

  histogram_EventCounter_                = book1D(dir, "EventCounter",                1,   -0.5,  +0.5);
}

/*namespace
{
  void fillWithOverFlow_logx(TH1* histogram, double x, double evtWeight, double evtWeightErr = 0.)
  {
    const double nonzero = 1.e-30;
    fillWithOverFlow(histogram, TMath::Log(TMath::Max(nonzero, x)), evtWeight, evtWeightErr);
  }
}*/

void
EvtHistManager_hh_bb1l::fillHistograms(int numElectrons,
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
				       double vbf_jet1_pt, double vbf_jet1_eta, double vbf_jet2_pt, double vbf_jet2_eta, double vbf_m_jj, double vbf_dEta_jj,
				       const MEMbbwwResultSingleLepton* memResult, double memCpuTime,
               std::string  category_mount,
               const std::map<std::string, double> categories_map_MVAs,
               double selLepton_lead_pt, double selLepton_lead_eta,
               double selJetsAK4_0_pt,
               double selJetsAK4_1_pt,
               double selJetsAK4_0_eta,
               double selJetsAK4_1_eta, 
	       double mht, double m_Hbb_regCorr, double dR_b1lep, double dR_b2lep,
				       double mindr_lep1_jet, double avg_dr_jet_central, double mbb_loose, double mbb_medium, double cosThetaS_Hbb_reg, double cosThetaS_HH,
               bool doDataMCPlots,
				       double evtWeight)
{
  const double evtWeightErr = 0.;

  for(auto typeMVA: categories_map_MVAs)
  {
    std::string name_test = typeMVA.first + category_mount;
    if(! histograms_by_category_types_.count( name_test ))
    {
      throw cmsException(this, __func__, __LINE__) << "Histogram of the name '" << name_test << "' was never booked";
    }
    fillWithOverFlow(histograms_by_category_types_[name_test],  typeMVA.second, evtWeight, evtWeightErr);
    /*    fillWithOverFlow(histograms_by_category_types_[name_test+"_leppt"],  selLepton_lead_pt, evtWeight, evtWeightErr);
    fillWithOverFlow(histograms_by_category_types_[name_test+"_bjet1pt"],  selJetsAK4_0_pt, evtWeight, evtWeightErr);
    fillWithOverFlow(histograms_by_category_types_[name_test+"_mht"],  mht, evtWeight, evtWeightErr);
    fillWithOverFlow(histograms_by_category_types_[name_test+"_m_Hbb_regCorr"],  m_Hbb_regCorr, evtWeight, evtWeightErr);
    fillWithOverFlow(histograms_by_category_types_[name_test+"_m_Wjj"],  m_Wjj, evtWeight, evtWeightErr);
    fillWithOverFlow(histograms_by_category_types_[name_test+"_pT_Wjj"],  pT_Wjj, evtWeight, evtWeightErr);
    fillWithOverFlow(histograms_by_category_types_[name_test+"_dR_Hww"],  dR_Hww, evtWeight, evtWeightErr);
    fillWithOverFlow(histograms_by_category_types_[name_test+"_Smin_Hww"],  Smin_Hww, evtWeight, evtWeightErr);
    fillWithOverFlow(histograms_by_category_types_[name_test+"_dR_b1lep"],  dR_b1lep, evtWeight, evtWeightErr);
    fillWithOverFlow(histograms_by_category_types_[name_test+"_dR_b2lep"],  dR_b2lep, evtWeight, evtWeightErr);
    fillWithOverFlow(histograms_by_category_types_[name_test+"_pT_HH"],  pT_HH, evtWeight, evtWeightErr);
    fillWithOverFlow(histograms_by_category_types_[name_test+"_mTW"],  mT_W, evtWeight, evtWeightErr);
    fillWithOverFlow(histograms_by_category_types_[name_test+"_mT_top_3particle"],  mT_top_3particle, evtWeight, evtWeightErr);
    fillWithOverFlow(histograms_by_category_types_[name_test+"_mindr_lep1_jet"],  mindr_lep1_jet, evtWeight, evtWeightErr);
    fillWithOverFlow(histograms_by_category_types_[name_test+"_avg_dr_jet_central"],  avg_dr_jet_central, evtWeight, evtWeightErr);
    fillWithOverFlow(histograms_by_category_types_[name_test+"_mbb_loose"],  mbb_loose, evtWeight, evtWeightErr);
    fillWithOverFlow(histograms_by_category_types_[name_test+"_mbb_medium"],  mbb_medium, evtWeight, evtWeightErr);
    fillWithOverFlow(histograms_by_category_types_[name_test+"_cosThetaS_Hbb_reg"],  cosThetaS_Hbb_reg, evtWeight, evtWeightErr);
    fillWithOverFlow(histograms_by_category_types_[name_test+"_cosThetaS_HH"],  cosThetaS_HH, evtWeight, evtWeightErr);*/
  }
  //
  fillWithOverFlow(histogram_numElectrons_,                     numElectrons,                       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numMuons_,                         numMuons,                           evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJets_,                          numJets,                            evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_loose_,                   numBJets_loose,                     evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_medium_,                  numBJets_medium,                    evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_HT_,                               HT,                                 evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_STMET_,                            STMET,                              evtWeight, evtWeightErr);
  /////
  if ( doDataMCPlots )
  {
    if(! histograms_by_category_check_jet1_pt_.count(category_mount))
    {
      throw cmsException(this, __func__, __LINE__) << "Histogram of the name '" << category_mount << "' was never booked";
    }
    fillWithOverFlow(histograms_by_category_check_jet1_pt_[category_mount], selJetsAK4_0_pt, evtWeight, evtWeightErr);
    fillWithOverFlow(histograms_by_category_check_jet1_eta_[category_mount], selJetsAK4_0_eta, evtWeight, evtWeightErr);
    fillWithOverFlow(histograms_by_category_check_lep1_pt_[category_mount], selLepton_lead_pt, evtWeight, evtWeightErr);
    fillWithOverFlow(histograms_by_category_check_lep1_eta_[category_mount], selLepton_lead_eta, evtWeight, evtWeightErr);
    fillWithOverFlow(histograms_by_category_check_jet2_pt_[category_mount], selJetsAK4_1_pt, evtWeight, evtWeightErr);
    fillWithOverFlow(histograms_by_category_check_jet2_eta_[category_mount], selJetsAK4_1_eta, evtWeight, evtWeightErr);
  }
  /*fillWithOverFlow(histogram_m_Hbb_,                            m_Hbb,                              evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dR_Hbb_,                           dR_Hbb,                             evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_Hbb_,                         dPhi_Hbb,                           evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_Hbb_,                           pT_Hbb,                             evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_m_Wjj_,                            m_Wjj,                              evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dR_Wjj_,                           dR_Wjj,                             evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_Wjj_,                         dPhi_Wjj,                           evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_Wjj_,                           pT_Wjj,                             evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_dR_Hww_,                           dR_Hww,                             evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_Hww_,                         dPhi_Hww,                           evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_Hww_,                           pT_Hww,                             evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_Smin_Hww_,                         Smin_Hww,                           evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_m_HHvis_,                          m_HHvis,                            evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_m_HH_,                             m_HH,                               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_m_HH_B2G_18_008_,                  m_HH_B2G_18_008,                    evtWeight, evtWeightErr);
  if ( m_HH_hme > 0. ) {
    fillWithOverFlow(histogram_m_HH_hme_,                       m_HH_hme,                           evtWeight, evtWeightErr);
  }
  fillWithOverFlow(histogram_dR_HH_,                            dR_HH,                              evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_HH_,                          dPhi_HH,                            evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_HH_,                            pT_HH,                              evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_Smin_HH_,                          Smin_HH,                            evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_mT_W_,                             mT_W,                               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT_top_2particle_,                 mT_top_2particle,                   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT_top_3particle_,                 mT_top_3particle,                   evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_mvaOutput_Hj_tagger_,              mvaOutput_Hj_tagger,                evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mvaOutput_Hjj_tagger_,             mvaOutput_Hjj_tagger,               evtWeight, evtWeightErr);

  if ( vbf_jet1_pt > 0. ) {
    fillWithOverFlow(histogram_vbf_jet1_pt_,                    vbf_jet1_pt,                        evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_vbf_jet1_eta_,                   vbf_jet1_eta,                       evtWeight, evtWeightErr);
  }
  if ( vbf_jet2_pt > 0. ) {
    fillWithOverFlow(histogram_vbf_jet2_pt_,                    vbf_jet2_pt,                        evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_vbf_jet2_eta_,                   vbf_jet2_eta,                       evtWeight, evtWeightErr);
  }
  fillWithOverFlow(histogram_vbf_m_jj_,                         vbf_m_jj,                           evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_vbf_dEta_jj_,                      vbf_dEta_jj,                        evtWeight, evtWeightErr);

  if ( option_ == kOption_memEnabled ) {
    assert(memResult);
    fillWithOverFlow_logx(histogram_log_memProb_signal_,        memResult->getProb_signal(),        evtWeight, evtWeightErr);
    fillWithOverFlow_logx(histogram_log_memProbErr_signal_,     memResult->getProbErr_signal(),     evtWeight, evtWeightErr);
    fillWithOverFlow_logx(histogram_log_memProb_background_,    memResult->getProb_background(),    evtWeight, evtWeightErr);
    fillWithOverFlow_logx(histogram_log_memProbErr_background_, memResult->getProbErr_background(), evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_memLR_,                          memResult->getLikelihoodRatio(),    evtWeight, evtWeightErr);
    if ( memResult->getLikelihoodRatioErr() > 0. ) {
      double memLR_div_Err = memResult->getLikelihoodRatio()/memResult->getLikelihoodRatioErr();
      fillWithOverFlow_logx(histogram_log_memLR_div_Err_,       memLR_div_Err,                      evtWeight, evtWeightErr);
    }
    fillWithOverFlow(histogram_memScore_,                       memResult->getScore(),              evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_memCpuTime_,                     memCpuTime,                         evtWeight, evtWeightErr);
  }
  */

  fillWithOverFlow(histogram_EventCounter_,                     0.,                                 evtWeight, evtWeightErr);
}
