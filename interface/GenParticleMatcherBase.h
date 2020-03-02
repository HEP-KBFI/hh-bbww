#ifndef hhAnalysis_bbww_GenParticleMatcherBase_h
#define hhAnalysis_bbww_GenParticleMatcherBase_h

#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h" // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetBase.h" // RecoJetBase
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEt.h" // RecoMEt
#include "tthAnalysis/HiggsToTauTau/interface/Particle.h" // Particle::LorentzVector
#include "tthAnalysis/HiggsToTauTau/interface/ParticleCollectionGenMatcher.h" // RecoLeptonCollectionGenMatcher, RecoJetBaseCollectionGenMatcher
#include "tthAnalysis/HiggsToTauTau/interface/GenLepton.h" // GenLepton
#include "tthAnalysis/HiggsToTauTau/interface/GenJet.h" // GenJet

#include <vector> // std::vector<>

class GenParticleMatcherBase
{
 public:
  GenParticleMatcherBase();
  ~GenParticleMatcherBase();

  const std::vector<GenLepton>& getLeptons() const;
  const std::vector<GenParticle>& getWQuarks() const;
  const std::vector<GenJet>& getWJets() const;
  const std::vector<GenParticle>& getBQuarks() const;
  const std::vector<GenJet>& getBJets() const;
  const Particle::LorentzVector& getMEt() const;

  void 
  operator()(const std::vector<const RecoLepton*>& selLeptons, 
             const std::vector<const RecoJetBase*>& selJets_Hbb, 
             const std::vector<const RecoJetBase*>& selJets_Wjj, 
             const RecoMEt& met);

 protected:
  std::vector<GenJet> convert_genQuarks_to_genJets(const std::vector<GenParticle>& genQuarks, double mass = -1.);

  std::vector<GenLepton> genLeptonsForMatching_;
  std::vector<GenParticle> genWQuarksForMatching_;
  std::vector<GenJet> genWJetsForMatching_;
  std::vector<GenParticle> genBQuarksForMatching_;
  std::vector<GenJet> genBJetsForMatching_;
  Particle::LorentzVector genMEtP4_;

 private:
  RecoLeptonCollectionGenMatcher leptonGenMatcher_;
  RecoJetBaseCollectionGenMatcher jet_or_subjetGenMatcher_;
};

#endif // GenParticleMatcherBase_h
