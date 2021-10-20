#ifndef hhAnalysis_bbww_memNtupleAuxFunctions_dilepton_h
#define hhAnalysis_bbww_memNtupleAuxFunctions_dilepton_h

#include "tthAnalysis/HiggsToTauTau/interface/RecoJet.h"    // RecoJet
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetAK8.h" // RecoJetAK8
#include "tthAnalysis/HiggsToTauTau/interface/GenJet.h"     // GenJet
#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h" // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/GenLepton.h"  // GenLepton

#include "hhAnalysis/bbwwMEM/interface/MeasuredParticle.h"  // MeasuredParticle
#include "hhAnalysis/bbwwMEM/interface/MEMResult.h"         // MEMResultBase

#include <TMatrixD.h>                                       // TMatrixD

struct MEMEvent_dilepton
{
  MEMEvent_dilepton(const mem::MeasuredParticle* measuredBJet1, const mem::MeasuredParticle* measuredBJet2, 
                    const mem::MeasuredParticle* measuredLepton1, const mem::MeasuredParticle* measuredLepton2, 
                    double measuredMEtPx, double measuredMEtPy, const TMatrixD& measuredMEtCov)
    : measuredBJet1_(measuredBJet1)
    , genBJet1_(nullptr)
    , measuredBJet2_(measuredBJet2)
    , genBJet2_(nullptr)
    , isBoosted_Hbb_(false)
    , measuredLepton1_(measuredLepton1)
    , genLepton1_(nullptr)
    , measuredLepton2_(measuredLepton2)
    , genLepton2_(nullptr)
    , measuredMEtPx_(measuredMEtPx)
    , genMEtPx_(0.)
    , measuredMEtPy_(measuredMEtPy)
    , genMEtPy_(0.)
    , measuredMEtCov_(measuredMEtCov)
    , memCpuTime_(-1.)
    , key_(-1)
  {}
  ~MEMEvent_dilepton()
  {}
  const mem::MeasuredParticle* measuredBJet1_;
  const GenJet* genBJet1_;
  const mem::MeasuredParticle* measuredBJet2_;
  const GenJet* genBJet2_;
  bool isBoosted_Hbb_;
  const mem::MeasuredParticle* measuredLepton1_;
  const GenLepton* genLepton1_;
  const mem::MeasuredParticle* measuredLepton2_;
  const GenLepton* genLepton2_; 
  double measuredMEtPx_;
  double genMEtPx_;
  double measuredMEtPy_;
  double genMEtPy_;
  TMatrixD measuredMEtCov_;
  MEMResultBase memResult_;
  double memCpuTime_;
  mutable int key_;
};

std::vector<MEMEvent_dilepton>
buildMEMEvents_dilepton_boosted(const std::vector<const std::pair<mem::MeasuredParticle, mem::MeasuredParticle>*>& measuredJetsAK8_Hbb,
                                const std::vector<const mem::MeasuredParticle*>& measuredLeptons,
                                double measuredMEtPx, double measuredMEtPy, const TMatrixD& measuredMEtCov);

std::vector<MEMEvent_dilepton>
buildMEMEvents_dilepton_resolved(const std::vector<const mem::MeasuredParticle*>& measuredJetsAK4, int numBJets,
                                 const std::vector<const mem::MeasuredParticle*>& measuredLeptons,
                                 double measuredMEtPx, double measuredMEtPy, const TMatrixD& measuredMEtCov);

void
addGenMatches_dilepton(std::vector<MEMEvent_dilepton>& memEvents,
                       const std::vector<const GenJet*>& genBJets,
                       const std::vector<const GenLepton*>& genLeptons,
                       double genMEtPx, double genMEtPy);

std::map<int, std::vector<const MEMEvent_dilepton*>>
buildMEMEventMap_dilepton(const std::vector<MEMEvent_dilepton>& memEvents);

#endif
