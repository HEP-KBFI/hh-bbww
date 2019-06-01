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
				       const MEMbbwwResultDilepton* memResult, double memCpuTime,
				       const MEMbbwwResultDilepton* memResult_missingBJet, double memCpuTime_missingBJet,
				       double mvaoutput_bb2l300, double mvaoutput_bb2l400, double mvaoutput_bb2l750,
				       double mvaoutputnohiggnessnotopness_bb2l300, double mvaoutputnohiggnessnotopness_bb2l400, double mvaoutputnohiggnessnotopness_bb2l750,
				       double mvaoutput_bb2l_node3, double mvaoutput_bb2l_node7, double mvaoutput_bb2l_sm,
				       double evtWeight)
{
  const double evtWeightErr = 0.;

  fillWithOverFlow(histogram_numElectrons_,                                 numElectrons,                                   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numMuons_,                                     numMuons,                                       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJets_,                                      numJets,                                        evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_loose_,                               numBJets_loose,                                 evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_medium_,                              numBJets_medium,                                evtWeight, evtWeightErr);

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
}
