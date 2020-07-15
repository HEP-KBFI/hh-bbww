#include "hhAnalysis/bbww/interface/EvtHistManager_hh_bb2l.h"

#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h" // cmsException()
#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), fillWithOverFlow2d()

#include "hhAnalysis/bbww/interface/MEMOutput_hh_bb2l.h" // MEMOutput_hh_bb2l

#include <TMath.h> // TMath::Pi(), TMath::Log, TMath::Max

EvtHistManager_hh_bb2l::EvtHistManager_hh_bb2l(const edm::ParameterSet & cfg)
  : HistManagerBase(cfg)
  , option_(kOption_undefined)
{
  std::string option_string = cfg.getParameter<std::string>("option");
  if(option_string == "memDisabled")
  {
    option_ = kOption_memDisabled;
  }
  else if( option_string == "memEnabled")
  {
    option_ = kOption_memEnabled;
  } else
  {
    throw cmsException(this, __func__, __LINE__) << "Invalid Configuration parameter 'option' = " << option_string << " !!";
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
  central_or_shiftOptions_["m_ll"] = { "central" };
  central_or_shiftOptions_["dR_ll"] = { "central" };
  central_or_shiftOptions_["dPhi_ll"] = { "central" };
  central_or_shiftOptions_["dEta_ll"] = { "central" };
  central_or_shiftOptions_["pT_ll"] = { "central" };
  central_or_shiftOptions_["m_Hww"] = { "central" };
  central_or_shiftOptions_["mT_Hww"] = { "central" };
  central_or_shiftOptions_["pT_Hww"] = { "central" };
  central_or_shiftOptions_["Smin_Hww"] = { "central" };
  central_or_shiftOptions_["met_pt_proj"] = { "central" };
  central_or_shiftOptions_["m_HHvis"] = { "*" };
  central_or_shiftOptions_["m_HH"] = { "central" };
  central_or_shiftOptions_["m_HH_hme"] = { "central" }; // CV: to be replaced by "*" once HME is implemented !!
  central_or_shiftOptions_["hmeCpuTime"] = { "central" };
  central_or_shiftOptions_["dR_HH"] = { "central" };
  central_or_shiftOptions_["dPhi_HH"] = { "central" };
  central_or_shiftOptions_["pT_HH"] = { "central" };
  central_or_shiftOptions_["Smin_HH"] = { "central" };
  central_or_shiftOptions_["mT2_W"] = { "central" };
  central_or_shiftOptions_["mT2_W_step"] = { "central" };
  central_or_shiftOptions_["mT2_top_2particle"] = { "central" };
  central_or_shiftOptions_["mT2_top_2particle_step"] = { "central" };
  central_or_shiftOptions_["mT2_top_3particle"] = { "central" };
  central_or_shiftOptions_["mT2_top_3particle_step"] = { "central" };
  central_or_shiftOptions_["logHiggsness"] = { "central" };
  central_or_shiftOptions_["logTopness"] = { "central" };
  central_or_shiftOptions_["logTopness_vs_logHiggsness"] = { "central" };
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
  central_or_shiftOptions_["log_memProb_signal_missingBJet"] = { "central" };
  central_or_shiftOptions_["log_memProbErr_signal_missingBJet"] = { "central" };
  central_or_shiftOptions_["log_memProb_background_missingBJet"] = { "central" };
  central_or_shiftOptions_["log_memProbErr_background_missingBJet"] = { "central" };
  central_or_shiftOptions_["memLR_missingBJet"] = { "*" };
  central_or_shiftOptions_["log_memLR_div_Err_missingBJet"] = { "central" };
  central_or_shiftOptions_["memScore_missingBJet"] = { "*" };
  central_or_shiftOptions_["memCpuTime_missingBJet"] = { "central" };
  central_or_shiftOptions_["MVAOutput_300"] = { "*" };
  central_or_shiftOptions_["MVAOutput_400"] = { "*" };
  central_or_shiftOptions_["MVAOutput_750"] = { "*" };
  central_or_shiftOptions_["MVAOutputnohiggnessnotopness_300"] = { "*" };
  central_or_shiftOptions_["MVAOutputnohiggnessnotopness_400"] = { "*" };
  central_or_shiftOptions_["MVAOutputnohiggnessnotopness_750"] = { "*" };
  central_or_shiftOptions_["EventCounter"] = { "*" };
  /////////
  central_or_shiftOptions_["SM_plainVars_Xness_nocat"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_nocat"] = { "central" };
  ///////////
  central_or_shiftOptions_["SM_plainVars_Xness_ee"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_Xness_em"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_Xness_mm"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_HME_ee"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_HME_em"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_HME_mm"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_ee"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_em"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_mm"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_Xness_HME_ee"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_Xness_HME_em"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_Xness_HME_mm"] = { "central" };
  /////
  central_or_shiftOptions_["SM_plainVars_ee_Hbb_resolved"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_em_Hbb_resolved"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_mm_Hbb_resolved"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_ee_Hbb_boosted"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_em_Hbb_boosted"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_mm_Hbb_boosted"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_Hbb_resolved"]   = { "central" };
  central_or_shiftOptions_["SM_plainVars_Hbb_boosted"]    = { "central" };
  /////
  central_or_shiftOptions_["SM_plainVars_Xness_nnoMbb_noHME_ee_lowMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_Xness_nnoMbb_noHME_ee_medMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_Xness_nnoMbb_noHME_ee_highMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_Xness_nnoMbb_noHME_em_lowMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_Xness_nnoMbb_noHME_em_medMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_Xness_nnoMbb_noHME_em_highMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_Xness_nnoMbb_noHME_mm_lowMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_Xness_nnoMbb_noHME_mm_medMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_Xness_nnoMbb_noHME_mm_highMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_Xness_nobb_noHME_ee_lowMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_Xness_nobb_noHME_ee_medMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_Xness_nobb_noHME_ee_highMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_Xness_nobb_noHME_em_lowMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_Xness_nobb_noHME_em_medMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_Xness_nobb_noHME_em_highMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_Xness_nobb_noHME_mm_lowMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_Xness_nobb_noHME_mm_medMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_Xness_nobb_noHME_mm_highMbb"] = { "central" };
  /////////
}

const TH1 *
EvtHistManager_hh_bb2l::getHistogram_EventCounter() const
{
  return histogram_EventCounter_;
}

void
EvtHistManager_hh_bb2l::bookCategories(TFileDirectory & dir,
    const std::map<std::string, std::vector<double>> & categories_SM_plainVars_Xness,
    const std::map<std::string, std::vector<double>> & categories_SM_plainVars,
    const std::map<std::string, std::vector<double>> & categories_SM_plainVars_flavour_boosted,
    const std::map<std::string, std::vector<double>> & categories_SM_plainVars_boosted,
    const std::map<std::string, std::vector<double>> & categories_check
  )
{
  // X: not the smartest way, but we will detele most and keep one in the end, so it is ok
  // I would not waste time trying to do a dict of  histograms_by_category_
  //for(auto categoryType: {categories_SM_plainVars_Xness, categories_SM_plainVars_HME, categories_SM_plainVars_Xness_HME})
    for(auto category: categories_SM_plainVars_Xness)
    {
      //std::cout<< "Booked histo: " << category.first <<"\n";
      if(! category.second.empty())
      {
        const int npoints = category.second.size();
        Float_t binsx[npoints];
        std::copy(category.second.begin(), category.second.end(), binsx);
        histograms_by_category_SM_plainVars_Xness_[category.first] = book1D(dir, category.first, category.first, npoints - 1, binsx);
      }
      else
      {
        histograms_by_category_SM_plainVars_Xness_[category.first] = book1D(dir, category.first, category.first, 100,  0., +1.);
      }
      central_or_shiftOptions_[category.first] = { "*" };
    }
    /////
    for(auto category: categories_SM_plainVars_flavour_boosted)
    {
      //std::cout<< "Booked histo: " << category.first <<"\n";
      if(! category.second.empty())
      {
        const int npoints = category.second.size();
        Float_t binsx[npoints];
        std::copy(category.second.begin(), category.second.end(), binsx);
        histograms_by_category_SM_plainVars_flavour_boosted_[category.first] = book1D(dir, category.first, category.first, npoints - 1, binsx);
      }
      else
      {
        histograms_by_category_SM_plainVars_flavour_boosted_[category.first] = book1D(dir, category.first, category.first, 100,  0., +1.);
      }
      central_or_shiftOptions_[category.first] = { "*" };
    }
    /////
    for(auto category: categories_SM_plainVars)
    {
      //std::cout<< "Booked histo: " << category.first <<"\n";
      if(! category.second.empty())
      {
        const int npoints = category.second.size();
        Float_t binsx[npoints];
        std::copy(category.second.begin(), category.second.end(), binsx);
        histograms_by_category_SM_plainVars_[category.first] = book1D(dir, category.first, category.first, npoints - 1, binsx);
      }
      else
      {
        histograms_by_category_SM_plainVars_[category.first] = book1D(dir, category.first, category.first, 100,  0., +1.);
      }
      central_or_shiftOptions_[category.first] = { "*" };
    }
    /////
    for(auto category: categories_SM_plainVars_boosted)
    {
      //std::cout<< "Booked histo: " << category.first <<"\n";
      if(! category.second.empty())
      {
        const int npoints = category.second.size();
        Float_t binsx[npoints];
        std::copy(category.second.begin(), category.second.end(), binsx);
        histograms_by_category_SM_plainVars_boosted_[category.first] = book1D(dir, category.first, category.first, npoints - 1, binsx);
      }
      else
      {
        histograms_by_category_SM_plainVars_boosted_[category.first] = book1D(dir, category.first, category.first, 100,  0., +1.);
      }
      central_or_shiftOptions_[category.first] = { "*" };
    }
    /////
    for(auto category: categories_check)
    {
      histograms_by_category_check_jet1_pt_[category.first] = book1D(dir, category.first + "_jet1_pt", category.first, 40,  0., 200.);
      histograms_by_category_check_jet1_eta_[category.first] = book1D(dir, category.first + "_jet1_eta", category.first, 22,  -3., +3.);
      histograms_by_category_check_lep1_pt_[category.first] = book1D(dir, category.first + "_lep1_pt", category.first, 60,  0., +300.);
      histograms_by_category_check_lep1_eta_[category.first] = book1D(dir, category.first + "_lep1_eta", category.first, 22,  -3., +3.);
      histograms_by_category_check_jet2_pt_[category.first] = book1D(dir, category.first + "_jet2_pt", category.first, 30,  0., 150.);
      histograms_by_category_check_jet2_eta_[category.first] = book1D(dir, category.first + "_jet2_eta", category.first, 22,  -3., +3.);
      histograms_by_category_check_lep2_pt_[category.first] = book1D(dir, category.first + "_lep2_pt", category.first, 40,  0., +200.);
      histograms_by_category_check_lep2_eta_[category.first] = book1D(dir, category.first + "_lep2_eta", category.first, 22,  -3., +3.);
      central_or_shiftOptions_[category.first] = { "*" };
    }
    //
}

void
EvtHistManager_hh_bb2l::bookHistograms(TFileDirectory & dir)
{
  histogram_numElectrons_                            = book1D(dir, "numElectrons",                            5,   -0.5,  +4.5);
  histogram_numMuons_                                = book1D(dir, "numMuons",                                5,   -0.5,  +4.5);
  histogram_numJets_                                 = book1D(dir, "numJets",                                20,   -0.5, +19.5);
  histogram_numBJets_loose_                          = book1D(dir, "numBJets_loose",                         10,   -0.5,  +9.5);
  histogram_numBJets_medium_                         = book1D(dir, "numBJets_medium",                        10,   -0.5,  +9.5);

  histogram_m_HHvis_                                 = book1D(dir, "m_HHvis",                               100,    0., 1000.);
  histogram_m_HH_                                    = book1D(dir, "m_HH",                                  150,    0., 1500.);
  histogram_m_HH_hme_                                = book1D(dir, "m_HH_hme",                              150,    0., 1500.);

  histograms_SM_plainVars_Xness_nocat_       = book1D(dir, "SM_plainVars_Xness_nocat",                               100,    0., 1.);
  histograms_SM_plainVars_nocat_             = book1D(dir, "SM_plainVars_nocat",                               100,    0., 1.);

  histogram_MVAOutput300_                    = book1D(dir, "MVAOutput_300",                    "MVAOutput_300",                    360,   0.,    1.);
  histogram_MVAOutput400_                    = book1D(dir, "MVAOutput_400",                    "MVAOutput_400",                    360,   0.,    1.);
  histogram_MVAOutput750_                    = book1D(dir, "MVAOutput_750",                    "MVAOutput_750",                    360,   0.,    1.);
  histogram_MVAOutputnohiggnessnotopness300_ = book1D(dir, "MVAOutputnohiggnessnotopness_300", "MVAOutputnohiggnessnotopness_300", 360,   0.,    1.);
  histogram_MVAOutputnohiggnessnotopness400_ = book1D(dir, "MVAOutputnohiggnessnotopness_400", "MVAOutputnohiggnessnotopness_400", 360,   0.,    1.);
  histogram_MVAOutputnohiggnessnotopness750_ = book1D(dir, "MVAOutputnohiggnessnotopness_750", "MVAOutputnohiggnessnotopness_750", 360,   0.,    1.);
  histogram_MVAOutputnode3_                  = book1D(dir, "MVAOutput_node3",                  "MVAOutput_node3",                  360,   0.,    1.);
  histogram_MVAOutputnode7_                  = book1D(dir, "MVAOutput_node7",                  "MVAOutput_node7",                  360,   0.,    1.);
  histogram_MVAOutputsm_                     = book1D(dir, "MVAOutput_sm",                     "MVAOutput_sm",                     360,   0.,    1.);
  histogram_EventCounter_                    = book1D(dir, "EventCounter",                     "EventCounter",                       1,  -0.5,  +0.5);
}

namespace
{
  void fillWithOverFlow_logx(TH1* histogram,
                             double x,
                             double evtWeight,
                             double evtWeightErr = 0.)
  {
    const double nonzero = 1.e-30;
    fillWithOverFlow(histogram, TMath::Log(TMath::Max(nonzero, x)), evtWeight, evtWeightErr);
  }
}

void
EvtHistManager_hh_bb2l::fillHistograms(int numElectrons,
                                       int numMuons,
                                       int numJets,
                                       int numBJets_loose,
                                       int numBJets_medium,
                                       double mvaoutput_bb2l300,
                                       double mvaoutput_bb2l400,
                                       double mvaoutput_bb2l750,
                                       double mvaoutputnohiggnessnotopness_bb2l300,
                                       double mvaoutputnohiggnessnotopness_bb2l400,
                                       double mvaoutputnohiggnessnotopness_bb2l750,
                                       double mvaoutput_bb2l_node3,
                                       double mvaoutput_bb2l_node7,
                                       double mvaoutput_bb2l_sm,
                                       ///
                                       std::string category_SM_plainVars_Xness,
                                       std::string category_SM_plainVars,
                                       std::string category_SM_plainVars_flavour_boosted,
                                       std::string category_SM_plainVars_boosted,
                                       std::string category_check,
                                       double mva_SM_plainVars_Xness,
                                       double mva_SM_plainVars,
                                       double m_HH_hme,
                                       double m_HH,
                                       double m_HHvis,
                                       double selLepton_lead_pt, double selLepton_lead_eta,
                                       double selLepton_sublead_pt, double selLepton_sublead_eta,
                                       double selJetsAK4_0_pt,
                                       double selJetsAK4_1_pt,
                                       double selJetsAK4_0_eta,
                                       double selJetsAK4_1_eta,
                                       ///
                                       double evtWeight)
{
  const double evtWeightErr = 0.;

  fillWithOverFlow(histogram_numElectrons_,                    numElectrons,                         evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numMuons_,                        numMuons,                             evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJets_,                         numJets,                              evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_loose_,                  numBJets_loose,                       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_medium_,                 numBJets_medium,                      evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_MVAOutput300_,                    mvaoutput_bb2l300,                    evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_MVAOutput400_,                    mvaoutput_bb2l400,                    evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_MVAOutput750_,                    mvaoutput_bb2l750,                    evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_MVAOutputnohiggnessnotopness300_, mvaoutputnohiggnessnotopness_bb2l300, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_MVAOutputnohiggnessnotopness400_, mvaoutputnohiggnessnotopness_bb2l400, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_MVAOutputnohiggnessnotopness750_, mvaoutputnohiggnessnotopness_bb2l750, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_MVAOutputnode3_,                  mvaoutput_bb2l_node3,                 evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_MVAOutputnode7_,                  mvaoutput_bb2l_node7,                 evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_MVAOutputsm_,                     mvaoutput_bb2l_sm,                    evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_EventCounter_,                    0.,                                   evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_m_HH_hme_,                        m_HH_hme,                    evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_m_HH_,                            m_HH,                    evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_m_HHvis_,                         m_HHvis,                    evtWeight, evtWeightErr);

  fillWithOverFlow(histograms_SM_plainVars_Xness_nocat_ ,           mva_SM_plainVars_Xness,                 evtWeight, evtWeightErr);
  fillWithOverFlow(histograms_SM_plainVars_nocat_,                  mva_SM_plainVars,                 evtWeight, evtWeightErr);

  ////
  // X: not the smartest way, but we will detele most and keep one in the end, so it is ok
  // I would not waste time trying to do a dict of  histograms_by_category_
  /////
  if(! histograms_by_category_SM_plainVars_Xness_.count(category_SM_plainVars_Xness))
  {
    throw cmsException(this, __func__, __LINE__) << "Histogram of the name '" << category_SM_plainVars_Xness << "' was never booked";
  }
  fillWithOverFlow(histograms_by_category_SM_plainVars_Xness_[category_SM_plainVars_Xness], mva_SM_plainVars_Xness, evtWeight, evtWeightErr);
  //////
  if(! histograms_by_category_SM_plainVars_.count(category_SM_plainVars))
  {
    throw cmsException(this, __func__, __LINE__) << "Histogram of the name '" << category_SM_plainVars << "' was never booked";
  }
  fillWithOverFlow(histograms_by_category_SM_plainVars_[category_SM_plainVars], mva_SM_plainVars, evtWeight, evtWeightErr);
  /////
  if(! histograms_by_category_SM_plainVars_flavour_boosted_.count(category_SM_plainVars_flavour_boosted))
  {
    throw cmsException(this, __func__, __LINE__) << "Histogram of the name (flavour_boosted) '" << category_SM_plainVars_flavour_boosted << "' was never booked";
  }
  fillWithOverFlow(histograms_by_category_SM_plainVars_flavour_boosted_[category_SM_plainVars_flavour_boosted], mva_SM_plainVars, evtWeight, evtWeightErr);
  /////
  if(! histograms_by_category_SM_plainVars_boosted_.count(category_SM_plainVars_boosted))
  {
    throw cmsException(this, __func__, __LINE__) << "Histogram of the name (boosted) '" << category_SM_plainVars_boosted << "' was never booked";
  }
  fillWithOverFlow(histograms_by_category_SM_plainVars_boosted_[category_SM_plainVars_boosted], mva_SM_plainVars, evtWeight, evtWeightErr);
  /////
  if(! histograms_by_category_check_jet1_pt_.count(category_check))
  {
    throw cmsException(this, __func__, __LINE__) << "Histogram of the name '" << category_check << "' was never booked";
  }
  fillWithOverFlow(histograms_by_category_check_jet1_pt_[category_check], selJetsAK4_0_pt, evtWeight, evtWeightErr);
  fillWithOverFlow(histograms_by_category_check_jet1_eta_[category_check], selJetsAK4_0_eta, evtWeight, evtWeightErr);
  fillWithOverFlow(histograms_by_category_check_lep1_pt_[category_check], selLepton_lead_pt, evtWeight, evtWeightErr);
  fillWithOverFlow(histograms_by_category_check_lep1_eta_[category_check], selLepton_lead_eta, evtWeight, evtWeightErr);
  fillWithOverFlow(histograms_by_category_check_jet2_pt_[category_check], selJetsAK4_1_pt, evtWeight, evtWeightErr);
  fillWithOverFlow(histograms_by_category_check_jet2_eta_[category_check], selJetsAK4_1_eta, evtWeight, evtWeightErr);
  fillWithOverFlow(histograms_by_category_check_lep2_pt_[category_check], selLepton_sublead_pt, evtWeight, evtWeightErr);
  fillWithOverFlow(histograms_by_category_check_lep2_eta_[category_check], selLepton_sublead_eta, evtWeight, evtWeightErr);
}

void
EvtHistManager_hh_bb2l::fillHistograms(const MEMOutput_hh_bb2l * const memResult,
                                       //const MEMOutput_hh_bb2l * const memResult_missingBJet,
                                       double evtWeight)
{
  const double evtWeightErr = 0.;

  if(option_ == kOption_memEnabled)
  {
    assert(memResult);
    fillWithOverFlow_logx(histogram_log_memProb_signal_,                    memResult->weight_signal(),                    evtWeight, evtWeightErr);
    fillWithOverFlow_logx(histogram_log_memProbErr_signal_,                 memResult->weightErr_signal(),                 evtWeight, evtWeightErr);
    fillWithOverFlow_logx(histogram_log_memProb_background_,                memResult->weight_background(),                evtWeight, evtWeightErr);
    fillWithOverFlow_logx(histogram_log_memProbErr_background_,             memResult->weightErr_background(),             evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_memLR_,                                      memResult->LR(),                               evtWeight, evtWeightErr);
    if(memResult->LR() > 0.)
    {
      const double memLR_div_Err = memResult->LR() / memResult->LRErr();
      fillWithOverFlow_logx(histogram_log_memLR_div_Err_,                   memLR_div_Err,                                 evtWeight, evtWeightErr);
    }
    fillWithOverFlow(histogram_memScore_,                                   memResult->Score(),                            evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_memCpuTime_,                                 memResult->cpuTime(),                          evtWeight, evtWeightErr);
  }
}

void
EvtHistManager_hh_bb2l::fillHistograms(const MEMbbwwResultDilepton * const memResult,
                                       double memCpuTime,
                                       const MEMbbwwResultDilepton * const memResult_missingBJet,
                                       double memCpuTime_missingBJet,
                                       double evtWeight)
{
  const double evtWeightErr = 0.;

  if(option_ == kOption_memEnabled)
  {
    assert(memResult);
    fillWithOverFlow_logx(histogram_log_memProb_signal_,                    memResult->getProb_signal(),                    evtWeight, evtWeightErr);
    fillWithOverFlow_logx(histogram_log_memProbErr_signal_,                 memResult->getProbErr_signal(),                 evtWeight, evtWeightErr);
    fillWithOverFlow_logx(histogram_log_memProb_background_,                memResult->getProb_background(),                evtWeight, evtWeightErr);
    fillWithOverFlow_logx(histogram_log_memProbErr_background_,             memResult->getProbErr_background(),             evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_memLR_,                                      memResult->getLikelihoodRatio(),                evtWeight, evtWeightErr);
    if(memResult->getLikelihoodRatioErr() > 0.)
    {
      const double memLR_div_Err = memResult->getLikelihoodRatio()/memResult->getLikelihoodRatioErr();
      fillWithOverFlow_logx(histogram_log_memLR_div_Err_,                   memLR_div_Err,                                  evtWeight, evtWeightErr);
    }
    fillWithOverFlow(histogram_memScore_,                                   memResult->getScore(),                          evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_memCpuTime_,                                 memCpuTime,                                     evtWeight, evtWeightErr);

    assert(memResult_missingBJet);
    fillWithOverFlow_logx(histogram_log_memProb_signal_missingBJet_,        memResult_missingBJet->getProb_signal(),        evtWeight, evtWeightErr);
    fillWithOverFlow_logx(histogram_log_memProbErr_signal_missingBJet_,     memResult_missingBJet->getProbErr_signal(),     evtWeight, evtWeightErr);
    fillWithOverFlow_logx(histogram_log_memProb_background_missingBJet_,    memResult_missingBJet->getProb_background(),    evtWeight, evtWeightErr);
    fillWithOverFlow_logx(histogram_log_memProbErr_background_missingBJet_, memResult_missingBJet->getProbErr_background(), evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_memLR_missingBJet_,                          memResult_missingBJet->getLikelihoodRatio(),    evtWeight, evtWeightErr);
    if(memResult_missingBJet->getLikelihoodRatioErr() > 0.)
    {
      const double memLR_div_Err_missingBJet = memResult_missingBJet->getLikelihoodRatio()/memResult_missingBJet->getLikelihoodRatioErr();
      fillWithOverFlow_logx(histogram_log_memLR_div_Err_missingBJet_,       memLR_div_Err_missingBJet,                      evtWeight, evtWeightErr);
    }
    fillWithOverFlow(histogram_memScore_missingBJet_,                       memResult_missingBJet->getScore(),              evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_memCpuTime_missingBJet_,                     memCpuTime_missingBJet,                         evtWeight, evtWeightErr);
  }
}
