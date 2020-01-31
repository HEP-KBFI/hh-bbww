#ifndef hhAnalysis_bbww_genBoostedAuxFunctions_h
#define hhAnalysis_bbww_genBoostedAuxFunctions_h

#include "tthAnalysis/HiggsToTauTau/interface/GenLepton.h" // GenLepton
#include "tthAnalysis/HiggsToTauTau/interface/GenJet.h"    // GenJet
#include "tthAnalysis/HiggsToTauTau/interface/Particle.h"  // Particle::LorentzVector

#include <vector> // std::vector<>

template<typename T>
Particle::LorentzVector
compSumP4(const std::vector<const T*>& particles)
{
  Particle::LorentzVector sumP4;
  for ( const T* particle : particles )
  {
    sumP4 += particle->p4();
  }
  return sumP4;
}

bool isBoosted_genHbb(const std::vector<const GenJet*>& genBJets, double dRmax_fatjet = 0.8);

bool isBoosted_genWjj(const std::vector<const GenJet*>& genWJets, const std::vector<const GenLepton*>& genLeptons, double dRmax_fatjet = 0.8, double dRmax_lepton = 1.2);

#endif // genBoostedAuxFunctions_h
