#include "hhAnalysis/bbww/interface/GenParticleMatcherFromHiggs.h"

#include "tthAnalysis/HiggsToTauTau/interface/GenLepton.h" // GenLepton
#include "tthAnalysis/HiggsToTauTau/interface/GenJet.h" // GenJet
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // isHigherPt, findGenJetsFromWBoson
#include "hhAnalysis/bbww/interface/genMatchingAuxFunctions.h" // findGenLepton_and_NeutrinoFromWBoson
#include "hhAnalysis/bbwwMEM/interface/memAuxFunctions.h" // mem::bottomQuarkMass

#include <TMath.h> // TMath::ATan2, TMath::Sqrt

#include <algorithm> // std::sort

//---------------------------------------------------------------------------------------------------
// gen-matching functions specific to HH->bbWW signal events

std::vector<GenParticle> 
getGenWBosonsFromHiggs(const std::vector<GenParticle>& genParticlesFromHiggs)
{
  std::vector<GenParticle> genWBosons;
  const GenParticle* genWBosonPlus  = nullptr;
  const GenParticle* genWBosonMinus = nullptr;
  for ( std::vector<GenParticle>::const_iterator genParticle = genParticlesFromHiggs.begin(); genParticle != genParticlesFromHiggs.end(); ++genParticle )
  {
    if      ( genParticle->pdgId() == +24 ) genWBosonPlus  = &(*genParticle);
    else if ( genParticle->pdgId() == -24 ) genWBosonMinus = &(*genParticle);
  }
  if ( genWBosonPlus && genWBosonMinus ) 
  {
    genWBosons.push_back(*genWBosonPlus);
    genWBosons.push_back(*genWBosonMinus);
  }
  std::sort(genWBosons.begin(), genWBosons.end(), isHigherPtT<GenParticle>);
  return genWBosons;
}

std::vector<GenLepton> 
getGenLeptonsForMatching(const std::vector<GenParticle>& genParticlesFromHiggs, 
                         const std::vector<GenLepton>& genLeptons, 
                         const std::vector<GenParticle>& genNeutrinos)
{
  std::vector<GenLepton> genLeptonsFromHiggs;
  std::vector<GenParticle> genWBosons = getGenWBosonsFromHiggs(genParticlesFromHiggs);
  if ( genWBosons.size() == 2 ) 
  {
    std::pair<const GenLepton*, const GenParticle*> genLepton_and_Neutrino1 =
      findGenLepton_and_NeutrinoFromWBoson(genWBosons[0], genLeptons, genNeutrinos);      
    if ( genLepton_and_Neutrino1.first && genLepton_and_Neutrino1.second )
    {
      const GenParticle* genLepton1 = genLepton_and_Neutrino1.first;
      genLeptonsFromHiggs.push_back(*genLepton1);
    }
    std::pair<const GenLepton*, const GenParticle*> genLepton_and_Neutrino2 =
      findGenLepton_and_NeutrinoFromWBoson(genWBosons[1], genLeptons, genNeutrinos);
    if ( genLepton_and_Neutrino2.first && genLepton_and_Neutrino2.second )
    {
      const GenParticle* genLepton2 = genLepton_and_Neutrino2.first;
      genLeptonsFromHiggs.push_back(*genLepton2);
    }
  }
  std::sort(genLeptonsFromHiggs.begin(), genLeptonsFromHiggs.end(), isHigherPtT<GenLepton>);
  return genLeptonsFromHiggs;
}

Particle::LorentzVector
getGenMEt(const std::vector<GenParticle>& genParticlesFromHiggs, 
          const std::vector<GenLepton>& genLeptons, 
          const std::vector<GenParticle>& genNeutrinos)
{
  Particle::LorentzVector genMEtP4;
  std::vector<GenParticle> genWBosons = getGenWBosonsFromHiggs(genParticlesFromHiggs);
  if ( genWBosons.size() == 2 ) 
  {
    std::pair<const GenLepton*, const GenParticle*> genLepton_and_Neutrino1 =
      findGenLepton_and_NeutrinoFromWBoson(genWBosons[0], genLeptons, genNeutrinos);
    if ( genLepton_and_Neutrino1.first && genLepton_and_Neutrino1.second )
    {
      const GenParticle* genNeutrino1 = genLepton_and_Neutrino1.second;
      genMEtP4 += genNeutrino1->p4();
    }
    std::pair<const GenLepton*, const GenParticle*> genLepton_and_Neutrino2 =
      findGenLepton_and_NeutrinoFromWBoson(genWBosons[1], genLeptons, genNeutrinos);
    if ( genLepton_and_Neutrino2.first && genLepton_and_Neutrino2.second )
    {
      const GenParticle* genNeutrino2 = genLepton_and_Neutrino2.second;
      genMEtP4 += genNeutrino2->p4();
    }
  }
  return genMEtP4;
}

std::vector<GenParticle> 
getGenWQuarksFromHiggs(const std::vector<GenParticle>& genParticlesFromHiggs, 
                     const std::vector<GenLepton>& genLeptons, 
                     const std::vector<GenParticle>& genNeutrinos, 
                     const std::vector<GenParticle>& genWJets)
{  
  std::vector<GenParticle> genWQuarksFromHiggs;

  std::vector<GenParticle> genWBosons = getGenWBosonsFromHiggs(genParticlesFromHiggs);
  if ( genWBosons.size() == 2 ) 
  {
    std::pair<const GenLepton*, const GenParticle*> genLepton_and_Neutrino1 =
      findGenLepton_and_NeutrinoFromWBoson(genWBosons[0], genLeptons, genNeutrinos);
    if ( !(genLepton_and_Neutrino1.first && genLepton_and_Neutrino1.second) )
    {
      std::vector<const GenParticle*> genJetsFromWBoson1 =
        findGenJetsFromWBoson(genWBosons[0], genWJets);
      for ( std::vector<const GenParticle*>::const_iterator genJetFromWBoson1 = genJetsFromWBoson1.begin();
            genJetFromWBoson1 != genJetsFromWBoson1.end(); ++genJetFromWBoson1 ) {
        genWQuarksFromHiggs.push_back(**genJetFromWBoson1);
      }
    }
    std::pair<const GenLepton*, const GenParticle*> genLepton_and_Neutrino2 =
      findGenLepton_and_NeutrinoFromWBoson(genWBosons[1], genLeptons, genNeutrinos);
    if ( !(genLepton_and_Neutrino2.first && genLepton_and_Neutrino2.second) )
    {
      std::vector<const GenParticle*> genJetsFromWBoson2 =
        findGenJetsFromWBoson(genWBosons[1], genWJets);
      for ( std::vector<const GenParticle*>::const_iterator genJetFromWBoson2 = genJetsFromWBoson2.begin();
            genJetFromWBoson2 != genJetsFromWBoson2.end(); ++genJetFromWBoson2 ) {
        genWQuarksFromHiggs.push_back(**genJetFromWBoson2);
      }
    }
  }
  std::sort(genWQuarksFromHiggs.begin(), genWQuarksFromHiggs.end(), isHigherPtT<GenParticle>);
  return genWQuarksFromHiggs;
}

std::vector<GenParticle> 
getGenBQuarksFromHiggs(const std::vector<GenParticle>& genParticlesFromHiggs)
{
  std::vector<GenParticle> genBQuarksFromHiggs;
  const GenParticle* genBQuark     = nullptr;
  const GenParticle* genAntiBQuark = nullptr;
  for ( std::vector<GenParticle>::const_iterator genParticle = genParticlesFromHiggs.begin(); genParticle != genParticlesFromHiggs.end(); ++genParticle )
  {
    if      ( genParticle->pdgId() == +5 ) genBQuark     = &(*genParticle);
    else if ( genParticle->pdgId() == -5 ) genAntiBQuark = &(*genParticle);
  }
  if ( genBQuark && genAntiBQuark ) 
  { 
    genBQuarksFromHiggs.push_back(*genBQuark);
    genBQuarksFromHiggs.push_back(*genAntiBQuark);
    
  }
  std::sort(genBQuarksFromHiggs.begin(), genBQuarksFromHiggs.end(), isHigherPtT<GenParticle>);
  return genBQuarksFromHiggs;
}
//---------------------------------------------------------------------------------------------------

GenParticleMatcherFromHiggs::GenParticleMatcherFromHiggs()
{}

GenParticleMatcherFromHiggs::~GenParticleMatcherFromHiggs()
{}

void 
GenParticleMatcherFromHiggs::setGenParticles(const std::vector<GenParticle>& genParticlesFromHiggs, 
                                             const std::vector<GenLepton>& genLeptons, 
                                             const std::vector<GenParticle>& genNeutrinos,
                                             const std::vector<GenParticle>& genWJets)
{
  genLeptonsForMatching_ = getGenLeptonsForMatching(genParticlesFromHiggs, genLeptons, genNeutrinos);
  genWQuarksForMatching_ = getGenWQuarksFromHiggs(genParticlesFromHiggs, genLeptons, genNeutrinos, genWJets);
  genWJetsForMatching_ = convert_genQuarks_to_genJets(genWQuarksForMatching_);
  genBQuarksForMatching_ = getGenBQuarksFromHiggs(genParticlesFromHiggs);
  genBJetsForMatching_ = convert_genQuarks_to_genJets(genBQuarksForMatching_, mem::bottomQuarkMass);
  genMEtP4_ = getGenMEt(genParticlesFromHiggs, genLeptons, genNeutrinos);
}
