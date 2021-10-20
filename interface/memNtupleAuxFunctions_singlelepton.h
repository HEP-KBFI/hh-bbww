#ifndef hhAnalysis_bbww_memNtupleAuxFunctions_singlelepton_h
#define hhAnalysis_bbww_memNtupleAuxFunctions_singlelepton_h

#include "tthAnalysis/HiggsToTauTau/interface/RecoJet.h"    // RecoJet
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetAK8.h" // RecoJetAK8
#include "tthAnalysis/HiggsToTauTau/interface/GenJet.h"     // GenJet
#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h" // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/GenLepton.h"  // GenLepton

#include "hhAnalysis/bbwwMEM/interface/MeasuredParticle.h"  // MeasuredParticle
#include "hhAnalysis/bbwwMEM/interface/MEMResult.h"         // MEMResultBase

#include <TMatrixD.h>                                       // TMatrixD

struct MEMEvent_singlelepton
{
  MEMEvent_singlelepton(const mem::MeasuredParticle* measuredBJet1, const mem::MeasuredParticle* measuredBJet2,
                        const mem::MeasuredParticle* measuredWJet1, const mem::MeasuredParticle* measuredWJet2,
                        const mem::MeasuredParticle* measuredLepton,
                        double measuredMEtPx, double measuredMEtPy, const TMatrixD& measuredMEtCov)
    : measuredBJet1_(measuredBJet1)
    , genBJet1_(nullptr)
    , measuredBJet2_(measuredBJet2)
    , genBJet2_(nullptr)
    , isBoosted_Hbb_(false)
    , measuredWJet1_(measuredWJet1)
    , genWJet1_(nullptr)
    , measuredWJet2_(measuredWJet2)
    , genWJet2_(nullptr)
    , isBoosted_Wjj_(false)
    , measuredLepton_(measuredLepton)
    , genLepton_(nullptr)
    , measuredMEtPx_(measuredMEtPx)
    , genMEtPx_(0.)
    , measuredMEtPy_(measuredMEtPy)
    , genMEtPy_(0.)
    , measuredMEtCov_(measuredMEtCov)
    , memCpuTime_(-1.)
    , key_(-1)
  {}
  ~MEMEvent_singlelepton()
  {}
  const mem::MeasuredParticle* measuredBJet1_;
  const GenJet* genBJet1_;
  const mem::MeasuredParticle* measuredBJet2_;
  const GenJet* genBJet2_;
  bool isBoosted_Hbb_;
  const mem::MeasuredParticle* measuredWJet1_;
  const GenJet* genWJet1_;
  const mem::MeasuredParticle* measuredWJet2_;
  const GenJet* genWJet2_;
  bool isBoosted_Wjj_;
  const mem::MeasuredParticle* measuredLepton_;
  const GenLepton* genLepton_; 
  double measuredMEtPx_;
  double genMEtPx_;
  double measuredMEtPy_;
  double genMEtPy_;
  TMatrixD measuredMEtCov_;
  MEMResultBase memResult_;
  double memCpuTime_;
  mutable int key_;
};

std::vector<MEMEvent_singlelepton>
buildMEMEvents_singlelepton_boosted(const std::vector<const std::pair<mem::MeasuredParticle, mem::MeasuredParticle>*>& measuredJetsAK8_Hbb,
                                    const std::vector<const std::pair<mem::MeasuredParticle, mem::MeasuredParticle>*>& measuredJetsAK8_Wjj,
                                    const std::vector<const mem::MeasuredParticle*>& measuredLeptons,
                                    double measuredMEtPx, double measuredMEtPy, const TMatrixD& measuredMEtCov);

std::vector<MEMEvent_singlelepton>
buildMEMEvents_singlelepton_semiboosted(const std::vector<const std::pair<mem::MeasuredParticle, mem::MeasuredParticle>*>& measuredJetsAK8_Hbb,
                                        const std::vector<const mem::MeasuredParticle*>& measuredJetsAK4_Wjj, int numWJets,
                                        const std::vector<const mem::MeasuredParticle*>& measuredLeptons,
                                        double measuredMEtPx, double measuredMEtPy, const TMatrixD& measuredMEtCov);

std::vector<MEMEvent_singlelepton>
buildMEMEvents_singlelepton_resolved(const std::vector<const mem::MeasuredParticle*>& measuredJetsAK4_Hbb, int numBJets, 
                                     const std::vector<const mem::MeasuredParticle*>& measuredJetsAK4_Wjj, int numWJets,
                                     const std::vector<const mem::MeasuredParticle*>& measuredLeptons,
                                     double measuredMEtPx, double measuredMEtPy, const TMatrixD& measuredMEtCov);

void
addGenMatches_singlelepton(std::vector<MEMEvent_singlelepton>& memEvents,
              const std::vector<const GenJet*>& genBJets,
              const std::vector<const GenJet*>& genWJets,
              const std::vector<const GenLepton*>& genLeptons,
              double genMEtPx, double genMEtPy);

std::map<int, std::vector<const MEMEvent_singlelepton*>>
buildMEMEventMap_singlelepton(const std::vector<MEMEvent_singlelepton>& memEvents);

#endif
