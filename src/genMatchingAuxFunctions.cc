#include "hhAnalysis/bbww/interface/genMatchingAuxFunctions.h"

#include "DataFormats/Math/interface/deltaR.h" // deltaR

bool 
isGenMatched(double eta, double phi, const std::vector<GenParticle>& genParticles, 
	     const std::vector<int>* pdgIds, double dRmax)
{
  bool isMatched = false;
  for ( std::vector<GenParticle>::const_iterator genParticle = genParticles.begin();
	genParticle != genParticles.end(); ++genParticle ) {
    bool isSelected = false;
    if ( pdgIds )
    {
      int genParticle_pdgId = genParticle->pdgId();
      for ( std::vector<int>::const_iterator pdgId = pdgIds->begin();
	    pdgId != pdgIds->end(); ++pdgId ) {
	if ( genParticle_pdgId == (*pdgId) ) isSelected = true;
      }
    }
    if ( pdgIds && !isSelected ) continue;
    double dR = deltaR(eta, phi, genParticle->eta(), genParticle->phi());
    if ( dR < dRmax ) isMatched = true;
  }
  return isMatched;
}
