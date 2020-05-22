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
  central_or_shiftOptions_["SM_plainVars_noHH_withbb_nocat"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_nocat"] = { "central" };
  ///////////
  central_or_shiftOptions_["SM_plainVars_Xness_ee"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_Xness_em"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_Xness_mm"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_HME_ee"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_HME_em"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_HME_mm"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_Xness_HME_ee"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_Xness_HME_em"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_Xness_HME_mm"] = { "central" };
  /*central_or_shiftOptions_["SM_plainVars_nobb_noHME_ee_lowMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_nobb_noHME_ee_medMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_nobb_noHME_ee_highMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_nobb_noHME_em_lowMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_nobb_noHME_em_medMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_nobb_noHME_em_highMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_nobb_noHME_mm_lowMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_nobb_noHME_mm_medMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_nobb_noHME_mm_highMbb"] = { "central" };*/
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
  central_or_shiftOptions_["SM_plainVars_noHH_ee_MHH1_lowMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_em_MHH1_lowMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_mm_MHH1_lowMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_ee_MHH2_lowMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_em_MHH2_lowMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_mm_MHH2_lowMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_ee_MHH3_lowMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_em_MHH3_lowMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_mm_MHH3_lowMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_ee_MHH4_lowMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_em_MHH4_lowMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_mm_MHH4_lowMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_ee_MHH5_lowMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_em_MHH5_lowMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_mm_MHH5_lowMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_ee_MHH1_medMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_em_MHH1_medMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_mm_MHH1_medMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_ee_MHH2_medMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_em_MHH2_medMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_mm_MHH2_medMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_ee_MHH3_medMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_em_MHH3_medMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_mm_MHH3_medMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_ee_MHH4_medMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_em_MHH4_medMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_mm_MHH4_medMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_ee_MHH5_medMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_em_MHH5_medMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_mm_MHH5_medMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_ee_MHH1_highMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_em_MHH1_highMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_mm_MHH1_highMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_ee_MHH2_highMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_em_MHH2_highMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_mm_MHH2_highMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_ee_MHH3_highMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_em_MHH3_highMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_mm_MHH3_highMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_ee_MHH4_highMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_em_MHH4_highMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_mm_MHH4_highMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_ee_MHH5_highMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_em_MHH5_highMbb"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_mm_MHH5_highMbb"] = { "central" };
  //
  central_or_shiftOptions_["SM_plainVars_noHH_withbb_ee_MHH1"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_withbb_em_MHH1"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_withbb_mm_MHH1"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_withbb_ee_MHH2"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_withbb_em_MHH2"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_withbb_mm_MHH2"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_withbb_ee_MHH3"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_withbb_em_MHH3"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_withbb_mm_MHH3"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_withbb_ee_MHH4"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_withbb_em_MHH4"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_withbb_mm_MHH4"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_withbb_ee_MHH5"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_withbb_em_MHH5"] = { "central" };
  central_or_shiftOptions_["SM_plainVars_noHH_withbb_mm_MHH5"] = { "central" };
}

const TH1 *
EvtHistManager_hh_bb2l::getHistogram_EventCounter() const
{
  return histogram_EventCounter_;
}

void
EvtHistManager_hh_bb2l::bookCategories(TFileDirectory & dir,
    const std::map<std::string, std::vector<double>> & categories_SM_plainVars_Xness,
    //const std::map<std::string, std::vector<double>> & categories_SM_plainVars_HME,
    //const std::map<std::string, std::vector<double>> & categories_SM_plainVars_Xness_HME,
    //const std::map<std::string, std::vector<double>> & categories_SM_plainVars_nobb_noHME,
    //const std::map<std::string, std::vector<double>> & categories_SM_plainVars_Xness_nnoMbb_noHME,
    //const std::map<std::string, std::vector<double>> & categories_SM_plainVars_Xness_nobb_noHME,
    const std::map<std::string, std::vector<double>> & categories_SM_plainVars,
    const std::map<std::string, std::vector<double>> & categories_SM_plainVars_noHH_withbb,
    const std::map<std::string, std::vector<double>> & categories_SM_plainVars_noHH
  )
{
  // X: not the smartest way, but we will detele most and keep one in the end, so it is ok
  // I would not waste time trying to do a dict of  histograms_by_category_
  //for(auto categoryType: {categories_SM_plainVars_Xness, categories_SM_plainVars_HME, categories_SM_plainVars_Xness_HME})
  //{
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
    /*/////
    for(auto category: categories_SM_plainVars_HME)
    {
      //std::cout<< "Booked histo: " << category.first <<"\n";
      if(! category.second.empty())
      {
        const int npoints = category.second.size();
        Float_t binsx[npoints];
        std::copy(category.second.begin(), category.second.end(), binsx);
        histograms_by_category_SM_plainVars_HME_[category.first] = book1D(dir, category.first, category.first, npoints - 1, binsx);
      }
      else
      {
        histograms_by_category_SM_plainVars_HME_[category.first] = book1D(dir, category.first, category.first, 100,  0., +1.);
      }
      central_or_shiftOptions_[category.first] = { "*" };
    }*/
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
    for(auto category: categories_SM_plainVars_noHH_withbb)
    {
      //std::cout<< "Booked histo: " << category.first <<"\n";
      if(! category.second.empty())
      {
        const int npoints = category.second.size();
        Float_t binsx[npoints];
        std::copy(category.second.begin(), category.second.end(), binsx);
        histograms_by_category_SM_plainVars_noHH_withbb_[category.first] = book1D(dir, category.first, category.first, npoints - 1, binsx);
      }
      else
      {
        histograms_by_category_SM_plainVars_noHH_withbb_[category.first] = book1D(dir, category.first, category.first, 100,  0., +1.);
      }
      central_or_shiftOptions_[category.first] = { "*" };
    }
    /////
    for(auto category: categories_SM_plainVars_noHH)
    {
      //std::cout<< "Booked histo: " << category.first <<"\n";
      if(! category.second.empty())
      {
        const int npoints = category.second.size();
        Float_t binsx[npoints];
        std::copy(category.second.begin(), category.second.end(), binsx);
        histograms_by_category_SM_plainVars_noHH_[category.first] = book1D(dir, category.first, category.first, npoints - 1, binsx);
      }
      else
      {
        histograms_by_category_SM_plainVars_noHH_[category.first] = book1D(dir, category.first, category.first, 100,  0., +1.);
      }
      central_or_shiftOptions_[category.first] = { "*" };
    }
    /*////
    for(auto category: categories_SM_plainVars_Xness_HME)
    {
      //std::cout<< "Booked histo: " << category.first <<"\n";
      if(! category.second.empty())
      {
        const int npoints = category.second.size();
        Float_t binsx[npoints];
        std::copy(category.second.begin(), category.second.end(), binsx);
        histograms_by_category_SM_plainVars_Xness_HME_[category.first] = book1D(dir, category.first, category.first, npoints - 1, binsx);
      }
      else
      {
        histograms_by_category_SM_plainVars_Xness_HME_[category.first] = book1D(dir, category.first, category.first, 100,  0., +1.);
      }
      central_or_shiftOptions_[category.first] = { "*" };
    }
  //}
  ////////////////////////////
  //for(auto categoryType: {categories_SM_plainVars_nobb_noHME, categories_SM_plainVars_Xness_nnoMbb_noHME, categories_SM_plainVars_Xness_nobb_noHME})
  //{*/
    /*for(auto category: categories_SM_plainVars_nobb_noHME)
    {
      //std::cout<< "Booked histo: " << category.first <<"\n";
      histograms_by_category_SM_plainVars_nobb_noHME_[category.first] = book2D(dir, category.first, category.first, 50,  0., +1., 100,  0., +1000.);
      central_or_shiftOptions_[category.first] = { "*" };
    }
    ///////////////
    for(auto category: categories_SM_plainVars_Xness_nnoMbb_noHME)
    {
      //std::cout<< "Booked histo: " << category.first <<"\n";
      histograms_by_category_SM_plainVars_Xness_nnoMbb_noHME_[category.first] = book2D(dir, category.first, category.first, 50,  0., +1., 100,  0., +1000.);
      central_or_shiftOptions_[category.first] = { "*" };
    }
    ////////////////
    for(auto category: categories_SM_plainVars_Xness_nobb_noHME)
    {
      //std::cout<< "Booked histo: " << category.first <<"\n";
      histograms_by_category_SM_plainVars_Xness_nobb_noHME_[category.first] = book2D(dir, category.first, category.first, 50,  0., +1., 100,  0., +1000.);
      central_or_shiftOptions_[category.first] = { "*" };
    }
  //}*/


}

void
EvtHistManager_hh_bb2l::bookHistograms(TFileDirectory & dir)
{
  histogram_numElectrons_                            = book1D(dir, "numElectrons",                            5,   -0.5,  +4.5);
  histogram_numMuons_                                = book1D(dir, "numMuons",                                5,   -0.5,  +4.5);
  histogram_numJets_                                 = book1D(dir, "numJets",                                20,   -0.5, +19.5);
  histogram_numBJets_loose_                          = book1D(dir, "numBJets_loose",                         10,   -0.5,  +9.5);
  histogram_numBJets_medium_                         = book1D(dir, "numBJets_medium",                        10,   -0.5,  +9.5);

  /*histogram_HT_                                      = book1D(dir, "HT",                                    150,    0., 1500.);
  histogram_STMET_                                   = book1D(dir, "STMET",                                 150,    0., 1500.);

  histogram_m_Hbb_                                   = book1D(dir, "m_Hbb",                                  40,    0.,  200.);
  histogram_dR_Hbb_                                  = book1D(dir, "dR_Hbb",                                100,    0.,    5.);
  histogram_dPhi_Hbb_                                = book1D(dir, "dPhi_Hbb",                               36,    0, TMath::Pi());
  histogram_pT_Hbb_                                  = book1D(dir, "pT_Hbb",                                100,    0.,  500.);

  histogram_m_ll_                                    = book1D(dir, "m_ll",                                   40,    0.,  200.);
  histogram_dR_ll_                                   = book1D(dir, "dR_ll",                                 100,    0.,    5.);
  histogram_dPhi_ll_                                 = book1D(dir, "dPhi_ll",                                36,    0, TMath::Pi());
  histogram_dEta_ll_                                 = book1D(dir, "dEta_ll",                                50,    0,     5.);
  histogram_pT_ll_                                   = book1D(dir, "pT_ll",                                 100,    0.,  500.);

  histogram_m_Hww_                                   = book1D(dir, "m_Hww",                                  40,    0.,  200.);
  histogram_mT_Hww_                                  = book1D(dir, "mT_Hww",                                 40,    0.,  200.);
  histogram_pT_Hww_                                  = book1D(dir, "pT_Hww",                                100,    0.,  500.);
  histogram_Smin_Hww_                                = book1D(dir, "Smin_Hww",                              100,    0.,  500.);

  histogram_met_pt_proj_                             = book1D(dir, "met_pt_proj",                            40,    0.,  200.);

  histogram_hmeCpuTime_                              = book1D(dir, "hmeCpuTime",                            200,    0.,   20.);
  histogram_dR_HH_                                   = book1D(dir, "dR_HH",                                 100,    0.,    5.);
  histogram_dPhi_HH_                                 = book1D(dir, "dPhi_HH",                                36,    0., TMath::Pi());
  histogram_pT_HH_                                   = book1D(dir, "pT_HH",                                 100,    0.,  500.);
  histogram_Smin_HH_                                 = book1D(dir, "Smin_HH",                               100,    0., 1000.);

  histogram_mT2_W_                                   = book1D(dir, "mT2_W",                                  40,    0.,  200.);
  histogram_mT2_W_step_                              = book1D(dir, "mT2_W_step",                            103,   -1.5, 101.5);
  histogram_mT2_top_2particle_                       = book1D(dir, "mT2_top_2particle",                     100,    0.,  500.);
  histogram_mT2_top_2particle_step_                  = book1D(dir, "mT2_top_2particle_step",                103,   -1.5, 101.5);
  histogram_mT2_top_3particle_                       = book1D(dir, "mT2_top_3particle",                     100,    0.,  500.);
  histogram_mT2_top_3particle_step_                  = book1D(dir, "mT2_top_3particle_step",                103,   -1.5, 101.5);

  histogram_logHiggsness_                            = book1D(dir, "logHiggsness",                           60,  -15., +15.);
  histogram_logTopness_                              = book1D(dir, "logTopness",                             60,  -15., +15.);
  //histogram_logTopness_vs_logHiggsness_ = book2D(dir, "logTopness_vs_logHiggsness", 60, -15., +15., 60, -15., +15.);

  histogram_vbf_jet1_pt_                             = book1D(dir, "vbf_jet1_pt",                            40,    0.,  200.);
  histogram_vbf_jet1_eta_                            = book1D(dir, "vbf_jet1_eta",                          100,   -5.0,  +5.0);
  histogram_vbf_jet2_pt_                             = book1D(dir, "vbf_jet2_pt",                            40,    0.,  200.);
  histogram_vbf_jet2_eta_                            = book1D(dir, "vbf_jet2_eta",                          100,   -5.0,  +5.0);
  histogram_vbf_m_jj_                                = book1D(dir, "vbf_m_jj",                              150,    0., 1500.);
  histogram_vbf_dEta_jj_                             = book1D(dir, "vbf_dEta_jj",                           100,    0.,   10.);

  if(option_ == kOption_memEnabled)
  {
    histogram_log_memProb_signal_                    = book1D(dir, "log_memProb_signal",                    200, -100., +100.);
    histogram_log_memProbErr_signal_                 = book1D(dir, "log_memProbErr_signal",                 200, -100., +100.);
    histogram_log_memProb_background_                = book1D(dir, "log_memProb_background",                200, -100., +100.);
    histogram_log_memProbErr_background_             = book1D(dir, "log_memProbErr_background",             200, -100., +100.);
    histogram_memLR_                                 = book1D(dir, "memLR",                                 360,    0.,    1.);
    histogram_log_memLR_div_Err_                     = book1D(dir, "log_memLR_div_Err",                     200,  -10.,  +10.);
    histogram_memScore_                              = book1D(dir, "memScore",                              360,  -18.,  +18.);
    histogram_memCpuTime_                            = book1D(dir, "memCpuTime",                            100,    0., 1000.);

    histogram_log_memProb_signal_missingBJet_        = book1D(dir, "log_memProb_signal_missingBJet",        200, -100., +100.);
    histogram_log_memProbErr_signal_missingBJet_     = book1D(dir, "log_memProbErr_signal_missingBJet",     200, -100., +100.);
    histogram_log_memProb_background_missingBJet_    = book1D(dir, "log_memProb_background_missingBJet",    200, -100., +100.);
    histogram_log_memProbErr_background_missingBJet_ = book1D(dir, "log_memProbErr_background_missingBJet", 200, -100., +100.);
    histogram_memLR_missingBJet_                     = book1D(dir, "memLR_missingBJet",                     360,    0.,    1.);
    histogram_log_memLR_div_Err_missingBJet_         = book1D(dir, "log_memLR_div_Err_missingBJet",         200,  -10.,  +10.);
    histogram_memScore_missingBJet_                  = book1D(dir, "memScore_missingBJet",                  360,  -18.,  +18.);
    histogram_memCpuTime_missingBJet_                = book1D(dir, "memCpuTime_missingBJet",                100,    0., 1000.);
  }*/

  histogram_m_HHvis_                                 = book1D(dir, "m_HHvis",                               100,    0., 1000.);
  histogram_m_HH_                                    = book1D(dir, "m_HH",                                  150,    0., 1500.);
  histogram_m_HH_hme_                                = book1D(dir, "m_HH_hme",                              150,    0., 1500.);

  histograms_SM_plainVars_Xness_nocat_       = book1D(dir, "SM_plainVars_Xness_nocat",                               100,    0., 1.);
  histograms_SM_plainVars_nocat_             = book1D(dir, "SM_plainVars_nocat",                               100,    0., 1.);
  histograms_SM_plainVars_noHH_withbb_nocat_ = book1D(dir, "SM_plainVars_noHH_withbb_nocat",                               100,    0., 1.);
  histograms_SM_plainVars_noHH_nocat_        = book1D(dir, "SM_plainVars_noHH_noca",                               100,    0., 1.);


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
                                       //std::string category_SM_plainVars_HME,
                                       //std::string category_SM_plainVars_Xness_HME,
                                       //std::string category_SM_plainVars_nobb_noHME,
                                       //std::string category_SM_plainVars_Xness_nnoMbb_noHME,
                                       //std::string category_SM_plainVars_Xness_nobb_noHME,
                                       std::string category_SM_plainVars,
                                       std::string category_SM_plainVars_noHH_withbb,
                                       std::string category_SM_plainVars_noHH,
                                       double mva_SM_plainVars_Xness,
                                       //double mva_SM_plainVars_HME,
                                       //double mva_SM_plainVars_Xness_HME,
                                       //double mva_SM_plainVars_nobb_noHME,
                                       //double mva_SM_plainVars_Xness_nnoMbb_noHME,
                                       //double mva_SM_plainVars_Xness_nobb_noHME,
                                       double mva_SM_plainVars,
                                       double mva_SM_plainVars_noHH_withbb,
                                       double mva_SM_plainVars_noHH,
                                       double m_HH_hme,
                                       double m_HH,
                                       double m_HHvis,
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
  fillWithOverFlow(histograms_SM_plainVars_noHH_withbb_nocat_,      mva_SM_plainVars_noHH_withbb,                    evtWeight, evtWeightErr);
  fillWithOverFlow(histograms_SM_plainVars_noHH_nocat_,             mva_SM_plainVars_noHH,                                   evtWeight, evtWeightErr);


  ////
  // X: not the smartest way, but we will detele most and keep one in the end, so it is ok
  // I would not waste time trying to do a dict of  histograms_by_category_
  /////
  if(! histograms_by_category_SM_plainVars_Xness_.count(category_SM_plainVars_Xness))
  {
    throw cmsException(this, __func__, __LINE__) << "Histogram of the name '" << category_SM_plainVars_Xness << "' was never booked";
  }
  fillWithOverFlow(histograms_by_category_SM_plainVars_Xness_[category_SM_plainVars_Xness], mva_SM_plainVars_Xness, evtWeight, evtWeightErr);
  /////
  /*if(! histograms_by_category_SM_plainVars_HME_.count(category_SM_plainVars_HME))
  {
    throw cmsException(this, __func__, __LINE__) << "Histogram of the name '" << category_SM_plainVars_HME << "' was never booked";
  }
  fillWithOverFlow(histograms_by_category_SM_plainVars_HME_[category_SM_plainVars_HME], mva_SM_plainVars_HME, evtWeight, evtWeightErr);*/
  /////
  /*if(! histograms_by_category_SM_plainVars_Xness_HME_.count(category_SM_plainVars_Xness_HME))
  {
    throw cmsException(this, __func__, __LINE__) << "Histogram of the name '" << category_SM_plainVars_Xness_HME << "' was never booked";
  }
  fillWithOverFlow(histograms_by_category_SM_plainVars_Xness_HME_[category_SM_plainVars_Xness_HME], mva_SM_plainVars_Xness_HME, evtWeight, evtWeightErr);*/
  //////
  if(! histograms_by_category_SM_plainVars_.count(category_SM_plainVars))
  {
    throw cmsException(this, __func__, __LINE__) << "Histogram of the name '" << category_SM_plainVars << "' was never booked";
  }
  fillWithOverFlow(histograms_by_category_SM_plainVars_[category_SM_plainVars], mva_SM_plainVars, evtWeight, evtWeightErr);
  /////
  if(! histograms_by_category_SM_plainVars_noHH_withbb_.count(category_SM_plainVars_noHH_withbb))
  {
    throw cmsException(this, __func__, __LINE__) << "Histogram of the name '" << category_SM_plainVars_noHH_withbb << "' was never booked";
  }
  fillWithOverFlow(histograms_by_category_SM_plainVars_noHH_withbb_[category_SM_plainVars_noHH_withbb], mva_SM_plainVars_noHH_withbb, evtWeight, evtWeightErr);
  /////
  if(! histograms_by_category_SM_plainVars_noHH_.count(category_SM_plainVars_noHH))
  {
    throw cmsException(this, __func__, __LINE__) << "Histogram of the name '" << category_SM_plainVars_noHH << "' was never booked";
  }
  fillWithOverFlow(histograms_by_category_SM_plainVars_noHH_[category_SM_plainVars_noHH], mva_SM_plainVars_noHH, evtWeight, evtWeightErr);
  /////
  //////////////////////// the 2D are with HH mass in y-axis
  /////
  /*if(! histograms_by_category_SM_plainVars_nobb_noHME_.count(category_SM_plainVars_nobb_noHME))
  {
    throw cmsException(this, __func__, __LINE__) << "Histogram of the name '" << category_SM_plainVars_nobb_noHME << "' was never booked";
  }
  fillWithOverFlow2d(histograms_by_category_SM_plainVars_nobb_noHME_[category_SM_plainVars_nobb_noHME], mva_SM_plainVars_nobb_noHME, m_HH, evtWeight, evtWeightErr);*/
  /////
  /*if(! histograms_by_category_SM_plainVars_Xness_nnoMbb_noHME_.count(category_SM_plainVars_Xness_nnoMbb_noHME))
  {
    throw cmsException(this, __func__, __LINE__) << "Histogram of the name '" << category_SM_plainVars_Xness_nnoMbb_noHME << "' was never booked";
  }
  fillWithOverFlow2d(histograms_by_category_SM_plainVars_Xness_nnoMbb_noHME_[category_SM_plainVars_Xness_nnoMbb_noHME], mva_SM_plainVars_Xness_nnoMbb_noHME, m_HH_hme, evtWeight, evtWeightErr);
  /////
  if(! histograms_by_category_SM_plainVars_Xness_nobb_noHME_.count(category_SM_plainVars_Xness_nobb_noHME))
  {
    throw cmsException(this, __func__, __LINE__) << "Histogram of the name '" << category_SM_plainVars_Xness_nobb_noHME << "' was never booked";
  }
  fillWithOverFlow2d(histograms_by_category_SM_plainVars_Xness_nobb_noHME_[category_SM_plainVars_Xness_nobb_noHME], mva_SM_plainVars_Xness_nobb_noHME, m_HH_hme, evtWeight, evtWeightErr);*/


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

//    assert(memResult_missingBJet);
//    fillWithOverFlow_logx(histogram_log_memProb_signal_missingBJet_,        memResult_missingBJet->weight_signal(),        evtWeight, evtWeightErr);
//    fillWithOverFlow_logx(histogram_log_memProbErr_signal_missingBJet_,     memResult_missingBJet->weightErr_signal(),     evtWeight, evtWeightErr);
//    fillWithOverFlow_logx(histogram_log_memProb_background_missingBJet_,    memResult_missingBJet->weight_background(),    evtWeight, evtWeightErr);
//    fillWithOverFlow_logx(histogram_log_memProbErr_background_missingBJet_, memResult_missingBJet->weightErr_background(), evtWeight, evtWeightErr);
//    fillWithOverFlow(histogram_memLR_missingBJet_,                          memResult_missingBJet->LR(),                   evtWeight, evtWeightErr);

//    if(memResult_missingBJet->LRErr() > 0.)
//    {
//      const double memLR_div_Err_missingBJet = memResult_missingBJet->LR() / memResult_missingBJet->LRErr();
//      fillWithOverFlow_logx(histogram_log_memLR_div_Err_missingBJet_,       memLR_div_Err_missingBJet,                     evtWeight, evtWeightErr);
//    }
//    fillWithOverFlow(histogram_memScore_missingBJet_,                       memResult_missingBJet->Score(),                evtWeight, evtWeightErr);
//    fillWithOverFlow(histogram_memCpuTime_missingBJet_,                     memResult_missingBJet->cpuTime(),              evtWeight, evtWeightErr);
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
