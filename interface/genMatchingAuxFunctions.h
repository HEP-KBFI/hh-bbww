#ifndef hhAnalysis_bbww_genMatchingAuxFunctions_h
#define hhAnalysis_bbww_genMatchingAuxFunctions_h

#include "tthAnalysis/HiggsToTauTau/interface/GenLepton.h" // GenLepton
#include "tthAnalysis/HiggsToTauTau/interface/GenParticle.h" // GenParticle

#include <string> // std::string
#include <vector> // std::vector<>

std::pair<const GenLepton*, const GenParticle*> 
findGenLepton_and_NeutrinoFromWBoson(const GenParticle& genWBoson, const std::vector<GenLepton>& genLeptons, const std::vector<GenParticle>& genNeutrinos);

bool 
isGenMatched(double eta, double phi, 
             const std::vector<GenParticle>& genParticles, const std::vector<int>* pdgIds = nullptr, 
	     double dRmax = 0.3);

template<typename T>
bool 
isGenMatched(double eta, double phi, 
             const std::vector<const T*>& recParticles, 
             double dRmax = 0.3)
{
  for ( const T* recParticle : recParticles )
  {
    double dR = deltaR(eta, phi, recParticle->eta(), recParticle->phi());
    if ( dR < dRmax ) return true;
  }
  return false;
}

#endif // genMatchingAuxFunctions_h
