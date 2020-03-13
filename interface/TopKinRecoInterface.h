#ifndef hhAnalysis_bbww_TopKinRecoInterface_h
#define hhAnalysis_bbww_TopKinRecoInterface_h

#include "tthAnalysis/HiggsToTauTau/interface/Particle.h" // Particle::LorentzVector
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEt.h"  // RecoMEt

#include "TopAnalysis/KinematicReconstruction/interface/KinematicReconstruction.h" // KinematicReconstruction

#include <TBenchmark.h> // TBenchmark

// forward declarations
class RecoLepton;
class RecoJetBase;

class TopKinRecoInterface
{
public:
  TopKinRecoInterface(double btag_wp, bool considerOnlyBJets);
  ~TopKinRecoInterface();

  void
  setInputs(const RecoLepton * selLepton_lead,
            const RecoLepton * selLepton_sublead,
            const RecoJetBase * selBJet_lead,
	    const RecoJetBase * selBJet_sublead,
            const RecoMEt & met, 
            bool switchToGen = false);

  bool
  isValid() const;

  const Particle::LorentzVector&
  getLeptonP4_top(int idx = -1) const;

  const Particle::LorentzVector&
  getBJetP4_top(int idx = -1) const;

  const Particle::LorentzVector&
  getTopQuarkP4_top(int idx = -1) const;

  const Particle::LorentzVector&
  getLeptonP4_antitop(int idx = -1) const;

  const Particle::LorentzVector&
  getBJetP4_antitop(int idx = -1) const;

  const Particle::LorentzVector&
  getTopQuarkP4_antitop(int idx = -1) const;

  const Particle::LorentzVector&
  getMEtP4(int idx = -1) const;

 private:
  KinematicReconstruction * algo_;

  bool isValid_;

  std::vector<Particle::LorentzVector> leptonP4_top_;
  std::vector<Particle::LorentzVector> neutrinoP4_top_;
  std::vector<Particle::LorentzVector> bJetP4_top_;
  std::vector<Particle::LorentzVector> topQuarkP4_top_;

  std::vector<Particle::LorentzVector> leptonP4_antitop_;
  std::vector<Particle::LorentzVector> neutrinoP4_antitop_;
  std::vector<Particle::LorentzVector> bJetP4_antitop_;
  std::vector<Particle::LorentzVector> topQuarkP4_antitop_;

  std::vector<Particle::LorentzVector> sumNeutrinoP4_;

  Particle::LorentzVector leptonP4_top_maxWeight_;
  Particle::LorentzVector neutrinoP4_top_maxWeight_;
  Particle::LorentzVector bJetP4_top_maxWeight_;
  Particle::LorentzVector topQuarkP4_top_maxWeight_;

  Particle::LorentzVector leptonP4_antitop_maxWeight_;
  Particle::LorentzVector neutrinoP4_antitop_maxWeight_;
  Particle::LorentzVector bJetP4_antitop_maxWeight_;
  Particle::LorentzVector topQuarkP4_antitop_maxWeight_;

  Particle::LorentzVector sumNeutrinoP4_maxWeight_;

  TBenchmark * clock_;
  double cpuTime_;
  double realTime_;
};

#endif // TopKinRecoInterface_h
