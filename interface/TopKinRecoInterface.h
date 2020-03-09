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
  TopKinRecoInterface(double btag_wp);
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
  getLeptonP4_top() const;

  const Particle::LorentzVector&
  getBJetP4_top() const;

  const Particle::LorentzVector&
  getTopQuarkP4_top() const;

  const Particle::LorentzVector&
  getLeptonP4_antitop() const;

  const Particle::LorentzVector&
  getBJetP4_antitop() const;

  const Particle::LorentzVector&
  getTopQuarkP4_antitop() const;

  const Particle::LorentzVector&
  getMEtP4() const;

 private:
  KinematicReconstruction * algo_;

  bool isValid_;

  Particle::LorentzVector leptonP4_top_;
  Particle::LorentzVector neutrinoP4_top_;
  Particle::LorentzVector bJetP4_top_;
  Particle::LorentzVector topQuarkP4_top_;

  Particle::LorentzVector leptonP4_antitop_;
  Particle::LorentzVector neutrinoP4_antitop_;
  Particle::LorentzVector bJetP4_antitop_;
  Particle::LorentzVector topQuarkP4_antitop_;

  Particle::LorentzVector metP4_;

  TBenchmark * clock_;
  double cpuTime_;
  double realTime_;
};

#endif // TopKinRecoInterface_h
