#ifndef hhAnalysis_bbww_GenParticleMatcherFromHiggs_h
#define hhAnalysis_bbww_GenParticleMatcherFromHiggs_h

#include "hhAnalysis/bbww/interface/GenParticleMatcherBase.h" // GenParticleMatcherBase
#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h" // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetBase.h" // RecoJetBase
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEt.h" // RecoMEt
#include "tthAnalysis/HiggsToTauTau/interface/GenParticle.h" // GenParticle
#include "tthAnalysis/HiggsToTauTau/interface/GenLepton.h" // GenLepton

#include <vector> // std::vector<>

class GenParticleMatcherFromHiggs : public GenParticleMatcherBase
{
 public:
  GenParticleMatcherFromHiggs();
  ~GenParticleMatcherFromHiggs();

  void 
  operator()(const std::vector<const RecoLepton*>& selLeptons, 
             const std::vector<const RecoJetBase*>& selJets_Hbb, 
             const std::vector<const RecoJetBase*>& selJets_Wjj, 
             const RecoMEt& met,
             const std::vector<GenParticle>& genParticlesFromHiggs, 
             const std::vector<GenLepton>& genLeptons, 
             const std::vector<GenParticle>& genNeutrinos);   
};

#endif // GenParticleMatcherFromHiggs_h
