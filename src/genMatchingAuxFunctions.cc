#include "hhAnalysis/bbww/interface/genMatchingAuxFunctions.h"

#include "DataFormats/Math/interface/deltaR.h" // deltaR

#include <TMath.h> // TMath::Abs

std::pair<const GenLepton*, const GenParticle*> 
findGenLepton_and_NeutrinoFromWBoson(const GenParticle& genWBoson, const std::vector<GenLepton>& genLeptons, const std::vector<GenParticle>& genNeutrinos)
{
  const GenLepton* genLeptonFromWBoson = nullptr;
  const GenParticle* genNeutrinoFromWBoson = nullptr;
  double minDeltaMass = 1.e+3;
  for ( std::vector<GenLepton>::const_iterator genLepton = genLeptons.begin();
	genLepton != genLeptons.end(); ++genLepton ) {
    for ( std::vector<GenParticle>::const_iterator genNeutrino = genNeutrinos.begin();
	  genNeutrino != genNeutrinos.end(); ++genNeutrino ) {
      Particle::LorentzVector genLepton_and_NeutrinoP4 = genLepton->p4() + genNeutrino->p4();
      double deltaMass = TMath::Abs(genLepton_and_NeutrinoP4.mass() - genWBoson.mass());
      double dR = deltaR(genLepton_and_NeutrinoP4, genWBoson.p4());
      if ( deltaMass < 5. && deltaMass < minDeltaMass && dR < 1.e-1 ) {
	genLeptonFromWBoson = &(*genLepton);
	genNeutrinoFromWBoson = &(*genNeutrino);
	minDeltaMass = deltaMass;
      }
    }
  }
  return std::pair<const GenLepton*, const GenParticle*>(genLeptonFromWBoson, genNeutrinoFromWBoson);
}

bool 
isGenMatched(double eta, double phi, 
             const std::vector<const GenJet*>& genJets,
	     double dRmax)
{
  bool isMatched = false;
  for ( const GenJet* genJet : genJets )
  {
    double dR = deltaR(eta, phi, genJet->eta(), genJet->phi());
    if ( dR < dRmax ) isMatched = true;
  }
  return isMatched;
}
