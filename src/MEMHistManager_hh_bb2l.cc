#include "hhAnalysis/bbww/interface/MEMHistManager_hh_bb2l.h"

#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h" // cmsException()
#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), fillWithOverFlow2d()

#include "hhAnalysis/bbww/interface/MEMOutput_hh_bb2l.h" // MEMOutput_hh_bb2l

#include <TMath.h> // TMath::Pi(), TMath::Log, TMath::Max

MEMHistManager_hh_bb2l::MEMHistManager_hh_bb2l(const edm::ParameterSet & cfg)
  : HistManagerBase(cfg)
{
  central_or_shiftOptions_["log_memProb_signal"] = { "central" };
  central_or_shiftOptions_["log_memProbErr_signal"] = { "central" };
  central_or_shiftOptions_["log_memProb_background"] = { "central" };
  central_or_shiftOptions_["log_memProbErr_background"] = { "central" };
  central_or_shiftOptions_["memLR"] = { "central" };
  central_or_shiftOptions_["log_memLR_div_Err"] = { "central" };
  central_or_shiftOptions_["memScore"] = { "central" };
  central_or_shiftOptions_["memCpuTime"] = { "central" };
  central_or_shiftOptions_["log_memProb_signal_missingBJet"] = { "central" };
  central_or_shiftOptions_["log_memProbErr_signal_missingBJet"] = { "central" };
  central_or_shiftOptions_["log_memProb_background_missingBJet"] = { "central" };
  central_or_shiftOptions_["log_memProbErr_background_missingBJet"] = { "central" };
  central_or_shiftOptions_["memLR_missingBJet"] = { "central" };
  central_or_shiftOptions_["log_memLR_div_Err_missingBJet"] = { "central" };
  central_or_shiftOptions_["memScore_missingBJet"] = { "central" };
  central_or_shiftOptions_["memCpuTime_missingBJet"] = { "central" };
}

void
MEMHistManager_hh_bb2l::bookHistograms(TFileDirectory & dir)
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
MEMHistManager_hh_bb2l::fillHistograms(const MEMOutput_hh_bb2l * const memResult,
                                       //const MEMOutput_hh_bb2l * const memResult_missingBJet,
                                       double evtWeight)
{
  const double evtWeightErr = 0.;

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

void
MEMHistManager_hh_bb2l::fillHistograms(const MEMbbwwResultDilepton * const memResult,
                                       double memCpuTime,
                                       //const MEMbbwwResultDilepton * const memResult_missingBJet,
                                       //double memCpuTime_missingBJet,
                                       double evtWeight)
{
  const double evtWeightErr = 0.;

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

  //assert(memResult_missingBJet);
  //fillWithOverFlow_logx(histogram_log_memProb_signal_missingBJet_,        memResult_missingBJet->getProb_signal(),        evtWeight, evtWeightErr);
  //fillWithOverFlow_logx(histogram_log_memProbErr_signal_missingBJet_,     memResult_missingBJet->getProbErr_signal(),     evtWeight, evtWeightErr);
  //fillWithOverFlow_logx(histogram_log_memProb_background_missingBJet_,    memResult_missingBJet->getProb_background(),    evtWeight, evtWeightErr);
  //fillWithOverFlow_logx(histogram_log_memProbErr_background_missingBJet_, memResult_missingBJet->getProbErr_background(), evtWeight, evtWeightErr);
  //fillWithOverFlow(histogram_memLR_missingBJet_,                          memResult_missingBJet->getLikelihoodRatio(),    evtWeight, evtWeightErr);
  //if(memResult_missingBJet->getLikelihoodRatioErr() > 0.)
  //{
  //  const double memLR_div_Err_missingBJet = memResult_missingBJet->getLikelihoodRatio()/memResult_missingBJet->getLikelihoodRatioErr();
  //  fillWithOverFlow_logx(histogram_log_memLR_div_Err_missingBJet_,       memLR_div_Err_missingBJet,                      evtWeight, evtWeightErr);
  //}
  //fillWithOverFlow(histogram_memScore_missingBJet_,                       memResult_missingBJet->getScore(),              evtWeight, evtWeightErr);
  //fillWithOverFlow(histogram_memCpuTime_missingBJet_,                     memCpuTime_missingBJet,                         evtWeight, evtWeightErr);
}
