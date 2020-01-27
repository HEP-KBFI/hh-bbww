#ifndef hhAnalysis_bbww_genMatchingAuxFunctions_h
#define hhAnalysis_bbww_genMatchingAuxFunctions_h

#include "tthAnalysis/HiggsToTauTau/interface/GenLepton.h" // GenLepton
#include "tthAnalysis/HiggsToTauTau/interface/GenJet.h" // GenJet
#include "tthAnalysis/HiggsToTauTau/interface/GenParticle.h" // GenParticle

#include <string> // std::string
#include <vector> // std::vector<>

std::pair<const GenLepton*, const GenParticle*> 
findGenLepton_and_NeutrinoFromWBoson(const GenParticle& genWBoson, const std::vector<GenLepton>& genLeptons, const std::vector<GenParticle>& genNeutrinos);

template<typename T>
bool 
isGenMatchedT(double eta, double phi, 
              const std::vector<const T*>& genParticles, const std::vector<int>* pdgIds = nullptr, 
	      double dRmax = 0.3)
{
  bool isMatched = false;
  for ( const T* genParticle : genParticles )
  {
    bool isSelected = false;
    if ( pdgIds )
    {
      int genParticle_pdgId = genParticle->pdgId();
      for ( int pdgId : *pdgIds )
      {
	if ( genParticle_pdgId == pdgId ) isSelected = true;
      }
    }
    if ( pdgIds && !isSelected ) continue;
    double dR = deltaR(eta, phi, genParticle->eta(), genParticle->phi());
    if ( dR < dRmax ) isMatched = true;
  }
  return isMatched;
}

bool 
isGenMatched(double eta, double phi, 
             const std::vector<const GenJet*>& genJets,
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

template<typename Trec, typename Tgen>
std::vector<const Trec*>
selectGenMatchedParticles(const std::vector<const Trec*>& recParticles, const std::vector<const Tgen*>& genParticles, const std::vector<int>* pdgIds = nullptr, double dRmax = 0.3)
{
  std::vector<const Trec*> selParticles;
  for ( const Trec* recParticle : recParticles )
  {
    if ( isGenMatchedT<Tgen>(recParticle->eta(), recParticle->phi(), genParticles, pdgIds, dRmax) ) selParticles.push_back(recParticle);
  }
  return selParticles;
}

template<typename T>
std::vector<const T*>
selectGenMatchedParticles(const std::vector<const T*>& recParticles, const std::vector<const GenJet*>& genJets, double dRmax = 0.3)
{
  std::vector<const T*> selParticles;
  for ( const T* recParticle : recParticles )
  {
    if ( isGenMatched(recParticle->eta(), recParticle->phi(), genJets, dRmax) ) selParticles.push_back(recParticle);
  }
  return selParticles;
}

#endif // genMatchingAuxFunctions_h
