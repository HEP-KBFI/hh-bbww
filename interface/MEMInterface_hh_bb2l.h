#ifndef hhAnalysis_bbww_MEMInterface_hh_bb2l_h
#define hhAnalysis_bbww_MEMInterface_hh_bb2l_h

#include "hhAnalysis/bbww/interface/MEMOutput_hh_bb2l.h" // MEMOutput_hh_bb2l
#include "hhAnalysis/bbwwMEM/interface/MEMbbwwAlgoDilepton.h"
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEt.h" // RecoMEt

// forward declarations
class RecoLepton;
class RecoJetBase;

class TBenchmark;

class MEMInterface_hh_bb2l
{
public:
  MEMInterface_hh_bb2l();
  ~MEMInterface_hh_bb2l();

  /**
   * @brief Calculates output of MEM integration.
   * @param pointers to leading and subleading lepton, leading and subleading b-tagged jet from H->bb decay, MET and
   *        MET covariance matrix
   * @return object with         MVA output
   */
  MEMOutput_hh_bb2l
  operator()(const RecoLepton * selLepton_lead,
             const RecoLepton * selLepton_sublead,
             const RecoJetBase * selJet_Hbb_lead,
	           const RecoJetBase * selJet_Hbb_sublead,
             const RecoMEt & met,
             std::string BM = "SM",
	     bool switchToGen = false,
       bool isDebug = false) const;

 private:
  map<std::string, MEMbbwwAlgoDilepton *> memAlgo_;

  TBenchmark * clock_;
};

#endif // MEMInterface_hh_bb2l_h
