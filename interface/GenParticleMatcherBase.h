#ifndef hhAnalysis_bbww_GenParticleMatcherBase_h
#define hhAnalysis_bbww_GenParticleMatcherBase_h

#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h" // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetBase.h" // RecoJetBase
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEt.h" // RecoMEt
#include "tthAnalysis/HiggsToTauTau/interface/ParticleCollectionGenMatcher.h" // RecoLeptonCollectionGenMatcher, RecoJetBaseCollectionGenMatcher
#include "tthAnalysis/HiggsToTauTau/interface/GenLepton.h" // GenLepton
#include "tthAnalysis/HiggsToTauTau/interface/GenJet.h" // GenJet

#include <vector> // std::vector<>

class GenParticleMatcherBase
{
 public:
  GenParticleMatcherBase();
  ~GenParticleMatcherBase();

  void 
  operator()(const std::vector<const RecoLepton*>& selLeptons, 
             const std::vector<const RecoJetBase*>& selJets_Hbb, 
             const std::vector<const RecoJetBase*>& selJets_Wjj, 
             const RecoMEt& met);

 protected:
  std::vector<GenLepton> genLeptonsForMatching_;
  std::vector<GenJet> genWJetsForMatching_;
  std::vector<GenJet> genBJetsForMatching_;
  double genMEtPt_;
  double genMEtPhi_;

 private:
  RecoLeptonCollectionGenMatcher leptonGenMatcher_;
  RecoJetBaseCollectionGenMatcher jet_or_subjetGenMatcher_;
};

#endif // GenParticleMatcherBase_h
