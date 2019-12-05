#ifndef hhAnalysis_bbww_MEMInterface_hh_bb1l_h
#define hhAnalysis_bbww_MEMInterface_hh_bb1l_h

#include "hhAnalysis/bbww/interface/MEMOutput_hh_bb1l.h" // MEMOutput_hh_bb1l
#include "hhAnalysis/bbwwMEM/interface/MEMbbwwAlgoSingleLepton.h"
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEt.h" // RecoMEt

// forward declarations
class RecoLepton;
class RecoJetBase;

class TBenchmark;

class MEMInterface_hh_bb1l
{
public:
  MEMInterface_hh_bb1l();
  ~MEMInterface_hh_bb1l();

  /**
   * @brief Calculates output of MEM integration.
   * @param pointers to lepton, leading and subleading jet from W->jj decay, leading and subleading b-tagged jet from H->bb decay, MET and
   *        MET covariance matrix
   * @return object with         MVA output
   */
  MEMOutput_hh_bb1l
  operator()(const RecoLepton * selLepton,
             const RecoJetBase * selJet_Wjj_lead,
	     const RecoJetBase * selJet_Wjj_sublead,
             const RecoJetBase * selJet_Hbb_lead,
	     const RecoJetBase * selJet_Hbb_sublead,
             const RecoMEt & met) const;

 private:
  MEMbbwwAlgoSingleLepton * memAlgo_;

  TBenchmark * clock_;
};

#endif // MEMInterface_hh_bb1l_h
