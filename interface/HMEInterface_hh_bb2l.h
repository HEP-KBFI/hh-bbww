#ifndef hhAnalysis_bbww_HMEInterface_hh_bb2l_h
#define hhAnalysis_bbww_HMEInterface_hh_bb2l_h

#include "hhAnalysis/bbww/interface/HMEOutput_hh_bb2l.h" // HMEOutput_hh_bb2l
#include "hhAnalysis/Heavymassestimator/interface/heavyMassEstimator.h" // heavyMassEstimator (HME) algorithm for computation of HH mass
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEt.h" // RecoMEt
#include "tthAnalysis/HiggsToTauTau/interface/LocalFileInPath.h" // LocalFileInPath 

// forward declarations
class RecoLepton;
class RecoJetBase;

class TBenchmark;

class HMEInterface_hh_bb2l
{
public:
  HMEInterface_hh_bb2l();
  ~HMEInterface_hh_bb2l();

  /**
   * @brief Calculates output of HME integration.
   * @param pointers to leading and subleading lepton, leading and subleading b-tagged jet from H->bb decay, MET and
   *        MET covariance matrix
   * @return object with         MVA output
   */
  HMEOutput_hh_bb2l
  operator()(const RecoLepton * selLepton_lead,
             const RecoLepton * selLepton_sublead,
             const RecoJetBase * selJet_Hbb_lead,
	     const RecoJetBase * selJet_Hbb_sublead,
             const RecoMEt & met,
	     const int & ievent) const;

 private:
  //heavyMassEstimator * hmeAlgo_;
  const bool PUSample;
  const int iterations;
  const int bjetrescaleAlgo;
  const int metcorrection;
  const bool weightfromonshellnupt_func;
  const bool weightfromonshellnupt_hist;
  const bool weightfromonoffshellWmass_hist;
  const bool useMET;
  LocalFileInPath RefPDFfile;
  
  TBenchmark * clock_;
};

#endif // HMEInterface_hh_bb2l_h
