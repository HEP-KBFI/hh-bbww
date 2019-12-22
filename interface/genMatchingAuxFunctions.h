#ifndef hhAnalysis_bbww_genMatchingAuxFunctions_h
#define hhAnalysis_bbww_genMatchingAuxFunctions_h

#include "tthAnalysis/HiggsToTauTau/interface/GenParticle.h" // GenParticle

#include <vector> // std::vector<>

bool 
isGenMatched(double eta, double phi, const std::vector<GenParticle>& genParticles, 
	     const std::vector<int>* pdgIds = nullptr, double dRmax = 0.3);

#endif // genMatchingAuxFunctions_h
