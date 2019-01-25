#include "hhAnalysis/bbww/interface/EvtHistManager_hh_bb2l.h"

#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h" // cmsException()
#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), fillWithOverFlow2d()

#include <TMath.h> // TMath::Pi(), TMath::Log, TMath::Max

EvtHistManager_hh_bb2l::EvtHistManager_hh_bb2l(const edm::ParameterSet & cfg)
  : HistManagerBase(cfg)
  , option_(kOption_undefined)
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
  central_or_shiftOptions_["m_ll"] = { "central" };
  central_or_shiftOptions_["dR_ll"] = { "central" };
  central_or_shiftOptions_["dPhi_ll"] = { "central" };
  central_or_shiftOptions_["pT_ll"] = { "central" };
  central_or_shiftOptions_["m_Hww"] = { "central" };
  central_or_shiftOptions_["pT_Hww"] = { "central" };
  central_or_shiftOptions_["Smin_Hww"] = { "central" };
  central_or_shiftOptions_["m_HHvis"] = { "*" };
  central_or_shiftOptions_["m_HH"] = { "central" };
  central_or_shiftOptions_["m_HH_hme"] = { "central" }; // CV: to be replaced by "*" once HME is implemented !!
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
}

const TH1 *
EvtHistManager_hh_bb2l::getHistogram_EventCounter() const
{
  return histogram_EventCounter_;
}

void
EvtHistManager_hh_bb2l::bookHistograms(TFileDirectory & dir)
{
  histogram_numElectrons_                            = book1D(dir, "numElectrons",                            5,   -0.5,  +4.5);
  histogram_numMuons_                                = book1D(dir, "numMuons",                                5,   -0.5,  +4.5);
  histogram_numJets_                                 = book1D(dir, "numJets",                                20,   -0.5, +19.5);
  histogram_numBJets_loose_                          = book1D(dir, "numBJets_loose",                         10,   -0.5,  +9.5);
  histogram_numBJets_medium_                         = book1D(dir, "numBJets_medium",                        10,   -0.5,  +9.5);

  histogram_HT_                                      = book1D(dir, "HT",                                    150,    0., 1500.);
  histogram_STMET_                                   = book1D(dir, "STMET",                                 150,    0., 1500.);

  histogram_m_Hbb_                                   = book1D(dir, "m_Hbb",                                  40,    0.,  200.); 
  histogram_dR_Hbb_                                  = book1D(dir, "dR_Hbb",                                100,    0.,    5.);
  histogram_dPhi_Hbb_                                = book1D(dir, "dPhi_Hbb",                               36,    0, TMath::Pi());
  histogram_pT_Hbb_                                  = book1D(dir, "pT_Hbb",                                100,    0.,  500.); 

  histogram_m_ll_                                    = book1D(dir, "m_ll",                                   40,    0.,  200.); 
  histogram_dR_ll_                                   = book1D(dir, "dR_ll",                                 100,    0.,    5.);
  histogram_dPhi_ll_                                 = book1D(dir, "dPhi_ll",                                36,    0, TMath::Pi());
  histogram_pT_ll_                                   = book1D(dir, "pT_ll",                                 100,    0.,  500.); 

  histogram_m_Hww_                                   = book1D(dir, "m_Hww",                                  40,    0.,  200.); 
  histogram_pT_Hww_                                  = book1D(dir, "pT_Hww",                                100,    0.,  500.);  
  histogram_Smin_Hww_                                = book1D(dir, "Smin_Hww",                              100,    0.,  500.);  

  histogram_m_HHvis_                                 = book1D(dir, "m_HHvis",                               100,    0., 1000.);  
  histogram_m_HH_                                    = book1D(dir, "m_HH",                                  150,    0., 1500.);
  histogram_m_HH_hme_                                = book1D(dir, "m_HH_hme",                              150,    0., 1500.);
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
  
  if ( option_ == kOption_memEnabled ) {
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
  }

  histogram_MVAOutput300_                            = book1D(dir, "MVAOutput_300",                         360,    0.,    1.);
  histogram_MVAOutput400_                            = book1D(dir, "MVAOutput_400",                         360,    0.,    1.);
  histogram_MVAOutput750_                            = book1D(dir, "MVAOutput_750",                         360,    0.,    1.);
  histogram_MVAOutputnohiggnessnotopness300_         = book1D(dir, "MVAOutputnohiggnessnotopness_300",      360,    0.,    1.);
  histogram_MVAOutputnohiggnessnotopness400_         = book1D(dir, "MVAOutputnohiggnessnotopness_400",      360,    0.,    1.);
  histogram_MVAOutputnohiggnessnotopness750_         = book1D(dir, "MVAOutputnohiggnessnotopness_750",      360,    0.,    1.);

  histogram_EventCounter_                            = book1D(dir, "EventCounter",                            1,   -0.5,  +0.5);
}

namespace
{
  void fillWithOverFlow_logx(TH1* histogram, double x, double evtWeight, double evtWeightErr = 0.)
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
				       double HT,
				       double STMET,
				       double m_Hbb, double dR_Hbb, double dPhi_Hbb, double pT_Hbb, 
				       double m_ll, double dR_ll, double dPhi_ll, double pT_ll,
				       double m_Hww, double pT_Hww, double Smin_Hww,
				       double m_HHvis, double m_HH, double m_HH_hme, double dR_HH, double dPhi_HH, double pT_HH, double Smin_HH,
				       double mT2_W, int mT2_W_step, double mT2_top_2particle, int mT2_top_2particle_step, double mT2_top_3particle, int mT2_top_3particle_step,
				       double logHiggsness, double logTopness,
				       double vbf_jet1_pt, double vbf_jet1_eta, double vbf_jet2_pt, double vbf_jet2_eta, double vbf_m_jj, double vbf_dEta_jj,
				       const MEMbbwwResultDilepton* memResult, double memCpuTime,
				       const MEMbbwwResultDilepton* memResult_missingBJet, double memCpuTime_missingBJet,
				       double mvaoutput_bb2l300, double mvaoutput_bb2l400, double mvaoutput_bb2l750,
				       double mvaoutputnohiggnessnotopness_bb2l300, double mvaoutputnohiggnessnotopness_bb2l400, double mvaoutputnohiggnessnotopness_bb2l750,
				       double evtWeight)
{
  const double evtWeightErr = 0.;

  fillWithOverFlow(histogram_numElectrons_,                                 numElectrons,                                   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numMuons_,                                     numMuons,                                       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJets_,                                      numJets,                                        evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_loose_,                               numBJets_loose,                                 evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_medium_,                              numBJets_medium,                                evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_HT_,                                           HT,                                             evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_STMET_,                                        STMET,                                          evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_m_Hbb_,                                        m_Hbb,                                          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dR_Hbb_,                                       dR_Hbb,                                         evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_Hbb_,                                     dPhi_Hbb,                                       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_Hbb_,                                       pT_Hbb,                                         evtWeight, evtWeightErr);
 
  fillWithOverFlow(histogram_m_ll_,                                         m_ll,                                           evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dR_ll_,                                        dR_ll,                                          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_ll_,                                      dPhi_ll,                                        evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_ll_,                                        pT_ll,                                          evtWeight, evtWeightErr);
  
  fillWithOverFlow(histogram_m_Hww_,                                        m_Hww,                                          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_Hww_,                                       pT_Hww,                                         evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_Smin_Hww_,                                     Smin_Hww,                                       evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_m_HHvis_,                                      m_HHvis,                                        evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_m_HH_,                                         m_HH,                                           evtWeight, evtWeightErr);
  if ( m_HH_hme > 0. ) {
    fillWithOverFlow(histogram_m_HH_hme_,                                   m_HH_hme,                                       evtWeight, evtWeightErr);    
  }
  fillWithOverFlow(histogram_dR_HH_,                                        dR_HH,                                          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_HH_,                                      dPhi_HH,                                        evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_HH_,                                        pT_HH,                                          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_Smin_HH_,                                      Smin_HH,                                        evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_mT2_W_,                                        mT2_W,                                          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT2_W_step_,                                   mT2_W_step,                                     evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT2_top_2particle_,                            mT2_top_2particle,                              evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT2_top_2particle_step_,                       mT2_top_2particle_step,                         evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT2_top_3particle_,                            mT2_top_3particle,                              evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT2_top_3particle_step_,                       mT2_top_3particle_step,                         evtWeight, evtWeightErr);
 
  fillWithOverFlow(histogram_logHiggsness_,                                 logHiggsness,                                   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_logTopness_,                                   logTopness,                                     evtWeight, evtWeightErr);

  //fillWithOverFlow2d(histogram_logTopness_vs_logHiggsness_, logHiggsness, logTopness, evtWeight, evtWeightErr);

  if ( vbf_jet1_pt > 0. ) {
    fillWithOverFlow(histogram_vbf_jet1_pt_,                                vbf_jet1_pt,                                    evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_vbf_jet1_eta_,                               vbf_jet1_eta,                                   evtWeight, evtWeightErr);
  }
  if ( vbf_jet2_pt > 0. ) {
    fillWithOverFlow(histogram_vbf_jet2_pt_,                                vbf_jet2_pt,                                    evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_vbf_jet2_eta_,                               vbf_jet2_eta,                                   evtWeight, evtWeightErr);
  }
  fillWithOverFlow(histogram_vbf_m_jj_,                                     vbf_m_jj,                                       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_vbf_dEta_jj_,                                  vbf_dEta_jj,                                    evtWeight, evtWeightErr);

  if ( option_ == kOption_memEnabled ) {
    assert(memResult);    
    fillWithOverFlow_logx(histogram_log_memProb_signal_,                    memResult->getProb_signal(),                    evtWeight, evtWeightErr);            
    fillWithOverFlow_logx(histogram_log_memProbErr_signal_,                 memResult->getProbErr_signal(),                 evtWeight, evtWeightErr);    
    fillWithOverFlow_logx(histogram_log_memProb_background_,                memResult->getProb_background(),                evtWeight, evtWeightErr);    
    fillWithOverFlow_logx(histogram_log_memProbErr_background_,             memResult->getProbErr_background(),             evtWeight, evtWeightErr);    
    fillWithOverFlow(histogram_memLR_,                                      memResult->getLikelihoodRatio(),                evtWeight, evtWeightErr);           
    if ( memResult->getLikelihoodRatioErr() > 0. ) {
      double memLR_div_Err = memResult->getLikelihoodRatio()/memResult->getLikelihoodRatioErr();
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
    if ( memResult_missingBJet->getLikelihoodRatioErr() > 0. ) {
      double memLR_div_Err_missingBJet = memResult_missingBJet->getLikelihoodRatio()/memResult_missingBJet->getLikelihoodRatioErr();
      fillWithOverFlow_logx(histogram_log_memLR_div_Err_missingBJet_,       memLR_div_Err_missingBJet,                      evtWeight, evtWeightErr);  
    }
    fillWithOverFlow(histogram_memScore_missingBJet_,                       memResult_missingBJet->getScore(),              evtWeight, evtWeightErr);  
    fillWithOverFlow(histogram_memCpuTime_missingBJet_,                     memCpuTime_missingBJet,                         evtWeight, evtWeightErr);   
  }

  fillWithOverFlow(histogram_MVAOutput300_,                                 mvaoutput_bb2l300,                              evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_MVAOutput400_,                                 mvaoutput_bb2l400,                              evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_MVAOutput750_,                                 mvaoutput_bb2l750,                              evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_MVAOutputnohiggnessnotopness300_,              mvaoutputnohiggnessnotopness_bb2l300,           evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_MVAOutputnohiggnessnotopness400_,              mvaoutputnohiggnessnotopness_bb2l400,           evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_MVAOutputnohiggnessnotopness750_,              mvaoutputnohiggnessnotopness_bb2l750,           evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_EventCounter_,                                 0.,                                             evtWeight, evtWeightErr);
}
