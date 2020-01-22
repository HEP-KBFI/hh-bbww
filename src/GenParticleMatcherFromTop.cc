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

std::vector<GenJet> 
getGenWJetsForMatching(const std::vector<GenParticle>& genLightQuarksFromTop)
{
  std::vector<GenJet> genWJets;
  for ( auto genLightQuark : genLightQuarksFromTop )
  {
    genWJets.push_back(GenJet(genLightQuark.pt(), genLightQuark.eta(), genLightQuark.phi(), genLightQuark.mass(), genLightQuark.pdgId()));
  }
  std::sort(genWJets.begin(), genWJets.end(), isHigherPtT<GenJet>);
  return genWJets;
}

std::vector<GenJet> 
getGenBJetsForMatching(const std::vector<GenParticle>& genBQuarksFromTop)
{
  std::vector<GenJet> genBJets;
  for ( auto genBQuark : genBQuarksFromTop )
  {
    genBJets.push_back(GenJet(genBQuark.pt(), genBQuark.eta(), genBQuark.phi(), mem::bottomQuarkMass, genBQuark.pdgId()));
  }
  std::sort(genBJets.begin(), genBJets.end(), isHigherPtT<GenJet>);
  return genBJets;
}
//---------------------------------------------------------------------------------------------------

GenParticleMatcherFromTop::GenParticleMatcherFromTop()
{}

GenParticleMatcherFromTop::~GenParticleMatcherFromTop()
{}

void 
GenParticleMatcherFromTop::operator()(const std::vector<const RecoLepton*>& selLeptons, 
                                      const std::vector<const RecoJetBase*>& selJets_Hbb, 
                                      const std::vector<const RecoJetBase*>& selJets_Wjj, 
                                      const RecoMEt& met,
                                      const std::vector<GenLepton>& genLeptonsFromTop, 
	                              const std::vector<GenParticle>& genNeutrinosFromTop,
                                      const std::vector<GenParticle>& genLightQuarksFromTop, 
                                      const std::vector<GenParticle>& genBQuarksFromTop)
{
  genLeptonsForMatching_ = getGenLeptonsForMatching(genLeptonsFromTop);
  genWJetsForMatching_ = getGenWJetsForMatching(genLightQuarksFromTop);
  genBJetsForMatching_ = getGenBJetsForMatching(genBQuarksFromTop);
  getGenMEt(genNeutrinosFromTop, genMEtPt_, genMEtPhi_);
  GenParticleMatcherBase::operator()(selLeptons, selJets_Hbb, selJets_Wjj, met);
}
