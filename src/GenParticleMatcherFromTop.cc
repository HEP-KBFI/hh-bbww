#include "hhAnalysis/bbww/interface/GenParticleMatcherFromTop.h"

#include "tthAnalysis/HiggsToTauTau/interface/GenLepton.h" // GenLepton
#include "tthAnalysis/HiggsToTauTau/interface/GenJet.h" // GenJet
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // isHigherPt
#include "hhAnalysis/bbwwMEM/interface/memAuxFunctions.h" // mem::bottomQuarkMass

#include <TMath.h> // TMath::ATan2, TMath::Sqrt

#include <algorithm> // std::sort

//---------------------------------------------------------------------------------------------------
// gen-matching functions specific to tt+jets background events

std::vector<GenLepton> 
getGenLeptonsForMatching(const std::vector<GenLepton>& genLeptonsFromTop)
{
  std::vector<GenLepton> genLeptons = genLeptonsFromTop;
  std::sort(genLeptons.begin(), genLeptons.end(), isHigherPtT<GenLepton>);
  return genLeptons;
}

void
getGenMEt(const std::vector<GenParticle>& genNeutrinosFromTop, 
	  double& genMEtPt, double& genMEtPhi)
{
  double genMEtPx = 0.;
  double genMEtPy = 0.;
  for ( auto genNeutrino : genNeutrinosFromTop )
  {
    genMEtPx += genNeutrino.p4().px();
    genMEtPy += genNeutrino.p4().py();
  }
  genMEtPt = TMath::Sqrt(genMEtPx*genMEtPx + genMEtPy*genMEtPy);
  genMEtPhi = TMath::ATan2(genMEtPy, genMEtPx);
}

std::vector<GenParticle> 
getGenWQuarksForMatching(const std::vector<GenParticle>& genLightQuarksFromTop)
{
  std::vector<GenParticle> genWQuarks = genLightQuarksFromTop;
  std::sort(genWQuarks.begin(), genWQuarks.end(), isHigherPtT<GenParticle>);
  return genWQuarks;
}

std::vector<GenParticle> 
getGenBQuarksForMatching(const std::vector<GenParticle>& genBQuarksFromTop)
{
  std::vector<GenParticle> genBQuarks = genBQuarksFromTop;
  std::sort(genBQuarks.begin(), genBQuarks.end(), isHigherPtT<GenParticle>);
  return genBQuarks;
}
//---------------------------------------------------------------------------------------------------

GenParticleMatcherFromTop::GenParticleMatcherFromTop()
{}

GenParticleMatcherFromTop::~GenParticleMatcherFromTop()
{}

void 
GenParticleMatcherFromTop::setGenParticles(const std::vector<GenLepton>& genLeptonsFromTop, 
	                                   const std::vector<GenParticle>& genNeutrinosFromTop,
                                           const std::vector<GenParticle>& genLightQuarksFromTop, 
                                           const std::vector<GenParticle>& genBQuarksFromTop)
{
  genLeptonsForMatching_ = getGenLeptonsForMatching(genLeptonsFromTop);
  genWQuarksForMatching_ = getGenWQuarksForMatching(genLightQuarksFromTop);
  genWJetsForMatching_ = convert_genQuarks_to_genJets(genWQuarksForMatching_);
  genBQuarksForMatching_ = getGenBQuarksForMatching(genBQuarksFromTop);
  genBJetsForMatching_ = convert_genQuarks_to_genJets(genBQuarksForMatching_, mem::bottomQuarkMass);
  getGenMEt(genNeutrinosFromTop, genMEtPt_, genMEtPhi_);
}
