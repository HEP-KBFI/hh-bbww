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
std::cout << "genLepton1: pT = " << genLepton1->pt() << ", eta = " << genLepton1->eta() << ", phi = " << genLepton1->phi() << std::endl;
      genLeptonsFromHiggs.push_back(*genLepton1);
    }
    std::pair<const GenLepton*, const GenParticle*> genLepton_and_Neutrino2 =
      findGenLepton_and_NeutrinoFromWBoson(genWBosons[1], genLeptons, genNeutrinos);
    if ( genLepton_and_Neutrino2.first && genLepton_and_Neutrino2.second )
    {
      const GenParticle* genLepton2 = genLepton_and_Neutrino2.first;
std::cout << "genLepton2: pT = " << genLepton2->pt() << ", eta = " << genLepton2->eta() << ", phi = " << genLepton2->phi() << std::endl;
      genLeptonsFromHiggs.push_back(*genLepton2);
    }
  }
  std::sort(genLeptonsFromHiggs.begin(), genLeptonsFromHiggs.end(), isHigherPtT<GenLepton>);
  return genLeptonsFromHiggs;
}

void
getGenMEt(const std::vector<GenParticle>& genParticlesFromHiggs, 
          const std::vector<GenLepton>& genLeptons, 
          const std::vector<GenParticle>& genNeutrinos, 
	  double& genMEtPt, double& genMEtPhi)
{
  double genMEtPx = 0.;
  double genMEtPy = 0.;
  std::vector<GenParticle> genWBosons = getGenWBosonsFromHiggs(genParticlesFromHiggs);
  if ( genWBosons.size() == 2 ) 
  {
    std::pair<const GenLepton*, const GenParticle*> genLepton_and_Neutrino1 =
      findGenLepton_and_NeutrinoFromWBoson(genWBosons[0], genLeptons, genNeutrinos);
    if ( genLepton_and_Neutrino1.first && genLepton_and_Neutrino1.second )
    {
      const GenParticle* genNeutrino1 = genLepton_and_Neutrino1.second;
std::cout << "genNeutrino1: pT = " << genNeutrino1->pt() << ", eta = " << genNeutrino1->eta() << ", phi = " << genNeutrino1->phi() << std::endl;
      genMEtPx += genNeutrino1->p4().px();
      genMEtPy += genNeutrino1->p4().py();
    }
    std::pair<const GenLepton*, const GenParticle*> genLepton_and_Neutrino2 =
      findGenLepton_and_NeutrinoFromWBoson(genWBosons[1], genLeptons, genNeutrinos);
    if ( genLepton_and_Neutrino2.first && genLepton_and_Neutrino2.second )
    {
      const GenParticle* genNeutrino2 = genLepton_and_Neutrino2.second;
std::cout << "genNeutrino2: pT = " << genNeutrino2->pt() << ", eta = " << genNeutrino2->eta() << ", phi = " << genNeutrino2->phi() << std::endl;
      genMEtPx += genNeutrino2->p4().px();
      genMEtPy += genNeutrino2->p4().py();
    }
  }
  genMEtPt = TMath::Sqrt(genMEtPx*genMEtPx + genMEtPy*genMEtPy);
  genMEtPhi = TMath::ATan2(genMEtPy, genMEtPx);
}

std::vector<GenJet> 
getGenWJetsFromHiggs(const std::vector<GenParticle>& genParticlesFromHiggs, 
                     const std::vector<GenLepton>& genLeptons, 
                     const std::vector<GenParticle>& genNeutrinos, 
                     const std::vector<GenParticle>& genWJets)
{  
  std::vector<GenJet> genWJetsFromHiggs;
std::cout << "break-point A.1 reached" << std::endl;

  std::vector<GenParticle> genWBosons = getGenWBosonsFromHiggs(genParticlesFromHiggs);
std::cout << "break-point A.2 reached" << std::endl;
  if ( genWBosons.size() == 2 ) 
  {
std::cout << "break-point A.3 reached" << std::endl;
    std::pair<const GenLepton*, const GenParticle*> genLepton_and_Neutrino1 =
      findGenLepton_and_NeutrinoFromWBoson(genWBosons[0], genLeptons, genNeutrinos);
std::cout << "break-point A.4 reached" << std::endl;
std::cout << "genWBosons[0]: pT = " << genWBosons[0].pt() << ", eta = " << genWBosons[0].eta() << ", phi = " << genWBosons[0].phi() << std::endl;
    if ( !(genLepton_and_Neutrino1.first && genLepton_and_Neutrino1.second) )
    {
std::cout << "break-point A.5 reached" << std::endl;
      std::pair<const GenParticle*, const GenParticle*> genJetsFromWBoson1 =
        findGenJetsFromWBoson(genWBosons[0], genWJets);
std::cout << "break-point A.6 reached" << std::endl;
      if ( genJetsFromWBoson1.first && genJetsFromWBoson1.second )
      {
        const GenParticle* genJet1_Wjj = genJetsFromWBoson1.first;
std::cout << "genJet1_Wjj: pT = " << genJet1_Wjj->pt() << ", eta = " << genJet1_Wjj->eta() << ", phi = " << genJet1_Wjj->phi() << std::endl;
        genWJetsFromHiggs.push_back(GenJet(genJet1_Wjj->pt(), genJet1_Wjj->eta(), genJet1_Wjj->phi(), genJet1_Wjj->mass(), genJet1_Wjj->pdgId()));
        const GenParticle* genJet2_Wjj = genJetsFromWBoson1.second;
std::cout << "genJet2_Wjj: pT = " << genJet2_Wjj->pt() << ", eta = " << genJet2_Wjj->eta() << ", phi = " << genJet2_Wjj->phi() << std::endl;
        genWJetsFromHiggs.push_back(GenJet(genJet2_Wjj->pt(), genJet2_Wjj->eta(), genJet2_Wjj->phi(), genJet2_Wjj->mass(), genJet2_Wjj->pdgId()));
      }
    }
std::cout << "genWBosons[1]: pT = " << genWBosons[1].pt() << ", eta = " << genWBosons[1].eta() << ", phi = " << genWBosons[1].phi() << std::endl;
    std::pair<const GenLepton*, const GenParticle*> genLepton_and_Neutrino2 =
      findGenLepton_and_NeutrinoFromWBoson(genWBosons[1], genLeptons, genNeutrinos);
    if ( !(genLepton_and_Neutrino2.first && genLepton_and_Neutrino2.second) )
    {
      std::pair<const GenParticle*, const GenParticle*> genJetsFromWBoson2 =
        findGenJetsFromWBoson(genWBosons[1], genWJets);
      if ( genJetsFromWBoson2.first && genJetsFromWBoson2.second )
      {
        const GenParticle* genJet1_Wjj = genJetsFromWBoson2.first;
std::cout << "genJet1_Wjj: pT = " << genJet1_Wjj->pt() << ", eta = " << genJet1_Wjj->eta() << ", phi = " << genJet1_Wjj->phi() << std::endl;
        genWJetsFromHiggs.push_back(GenJet(genJet1_Wjj->pt(), genJet1_Wjj->eta(), genJet1_Wjj->phi(), genJet1_Wjj->mass(), genJet1_Wjj->pdgId()));
        const GenParticle* genJet2_Wjj = genJetsFromWBoson2.second;
std::cout << "genJet2_Wjj: pT = " << genJet2_Wjj->pt() << ", eta = " << genJet2_Wjj->eta() << ", phi = " << genJet2_Wjj->phi() << std::endl;
        genWJetsFromHiggs.push_back(GenJet(genJet2_Wjj->pt(), genJet2_Wjj->eta(), genJet2_Wjj->phi(), genJet2_Wjj->mass(), genJet2_Wjj->pdgId()));
      }
    }
  }
  std::sort(genWJetsFromHiggs.begin(), genWJetsFromHiggs.end(), isHigherPtT<GenJet>);
  return genWJetsFromHiggs;
}

std::vector<GenJet> 
getGenBJetsFromHiggs(const std::vector<GenParticle>& genParticlesFromHiggs)
{
  std::vector<GenJet> genBJetsFromHiggs;
  const GenParticle* genBQuark     = nullptr;
  const GenParticle* genAntiBQuark = nullptr;
  for ( std::vector<GenParticle>::const_iterator genParticle = genParticlesFromHiggs.begin(); genParticle != genParticlesFromHiggs.end(); ++genParticle )
  {
    if      ( genParticle->pdgId() == +5 ) genBQuark     = &(*genParticle);
    else if ( genParticle->pdgId() == -5 ) genAntiBQuark = &(*genParticle);
  }
  if ( genBQuark && genAntiBQuark ) 
  { 
    genBJetsFromHiggs.push_back(GenJet(genBQuark->pt(), genBQuark->eta(), genBQuark->phi(), mem::bottomQuarkMass, genBQuark->pdgId()));
    genBJetsFromHiggs.push_back(GenJet(genAntiBQuark->pt(), genAntiBQuark->eta(), genAntiBQuark->phi(), mem::bottomQuarkMass, genAntiBQuark->pdgId()));
  }
  std::sort(genBJetsFromHiggs.begin(), genBJetsFromHiggs.end(), isHigherPtT<GenJet>);
  return genBJetsFromHiggs;
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
std::cout << "break-point 1 reached" << std::endl;
  genLeptonsForMatching_ = getGenLeptonsForMatching(genParticlesFromHiggs, genLeptons, genNeutrinos);
std::cout << "break-point 2 reached" << std::endl;
  genWJetsForMatching_ = getGenWJetsFromHiggs(genParticlesFromHiggs, genLeptons, genNeutrinos, genWJets);
std::cout << "break-point 3 reached" << std::endl;
  genBJetsForMatching_ = getGenBJetsFromHiggs(genParticlesFromHiggs);
std::cout << "break-point 4 reached" << std::endl;
  getGenMEt(genParticlesFromHiggs, genLeptons, genNeutrinos, genMEtPt_, genMEtPhi_);
std::cout << "break-point 5 reached" << std::endl;
std::cout << "genMEtPt = " << genMEtPt_ << std::endl;
std::cout << "genMEtPhi = " << genMEtPhi_ << std::endl;
}
