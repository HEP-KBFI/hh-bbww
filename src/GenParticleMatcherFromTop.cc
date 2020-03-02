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

Particle::LorentzVector
getGenMEt(const std::vector<GenParticle>& genNeutrinosFromTop)
{
  Particle::LorentzVector genMEtP4;
  for ( auto genNeutrino : genNeutrinosFromTop )
  {
    genMEtP4 += genNeutrino.p4();
  }
  return genMEtP4;
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
  genMEtP4_ = getGenMEt(genNeutrinosFromTop);
}

//---------------------------------------------------------------------------------------------------
const GenLepton* 
getLeptonFromTop(const std::vector<GenLepton>& genLeptons)
{
  const GenLepton* genLeptonFromTop = nullptr;
  for ( std::vector<GenLepton>::const_iterator genLepton = genLeptons.begin(); 
        genLepton != genLeptons.end(); ++genLepton ) {
    if ( genLepton->charge() > 0. ) 
    {
      genLeptonFromTop = &(*genLepton);
      break;
    }
  }
  return genLeptonFromTop;
}

const GenLepton* 
getLeptonFromAntiTop(const std::vector<GenLepton>& genLeptons)
{
  const GenLepton* genLeptonFromAntiTop = nullptr;
  for ( std::vector<GenLepton>::const_iterator genLepton = genLeptons.begin(); 
        genLepton != genLeptons.end(); ++genLepton ) {
    if ( genLepton->charge() < 0. ) 
    {
      genLeptonFromAntiTop = &(*genLepton);
      break;
    }
  }
  return genLeptonFromAntiTop;
}

const GenParticle* 
getBQuarkFromTop(const std::vector<GenParticle>& genBQuarks)
{
  const GenParticle* genBQuarkFromTop = nullptr;
  for ( std::vector<GenParticle>::const_iterator genBQuark = genBQuarks.begin(); 
        genBQuark != genBQuarks.end(); ++genBQuark ) {
    if ( genBQuark->pdgId() == +5 )
    {
      genBQuarkFromTop = &(*genBQuark);
      break;
    }
  }
  return genBQuarkFromTop;
}

const GenParticle* 
getBQuarkFromAntiTop(const std::vector<GenParticle>& genBQuarks)
{
  const GenParticle* genBQuarkFromAntiTop = nullptr;
  for ( std::vector<GenParticle>::const_iterator genBQuark = genBQuarks.begin(); 
        genBQuark != genBQuarks.end(); ++genBQuark ) {
    if ( genBQuark->pdgId() == -5 )
    {
      genBQuarkFromAntiTop = &(*genBQuark);
      break;
    }
  }
  return genBQuarkFromAntiTop;
}
//---------------------------------------------------------------------------------------------------
