#ifndef hhAnalysis_bbww_testMEMauxFunctions_h
#define hhAnalysis_bbww_testMEMauxFunctions_h

#include "PhysicsTools/FWLite/interface/TFileService.h" // fwlite::TFileService
#include "DataFormats/Math/interface/deltaR.h" // deltaR

#include "tthAnalysis/HiggsToTauTau/interface/GenParticle.h" // GenParticle
#include "tthAnalysis/HiggsToTauTau/interface/GenLepton.h" // GenLepton
#include "tthAnalysis/HiggsToTauTau/interface/GenJet.h" // GenJet
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetBase.h" // RecoJetBase
#include "tthAnalysis/HiggsToTauTau/interface/RecoJet.h" // RecoJet
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetCollectionSelectorBtag.h" // RecoJetCollectionSelectorBtagLoose, RecoJetCollectionSelectorBtagMedium

#include <TMath.h> // TMath
#include <TH1.h> // TH1

#include <string> // std::string
#include <vector> // std::vector<>

std::pair<const GenLepton*, const GenParticle*> 
findGenLepton_and_NeutrinoFromWBoson(const GenParticle* genWBoson, const std::vector<GenLepton>& genLeptons, const std::vector<GenParticle>& genNeutrinos);

template<typename T>
bool 
isGenMatched(const GenParticle* genParticle, const std::vector<const T*>& recParticles, double dRmax)
{
  for ( typename std::vector<const T*>::const_iterator recParticle = recParticles.begin();
	recParticle != recParticles.end(); ++recParticle ) {
    double dR = deltaR((*recParticle)->p4(), genParticle->p4());
    if ( dR < dRmax ) return true;
  }
  return false;
}

template<typename T1, typename T2>
int 
compGenMatchType(const GenParticle* genParticle, 
		 const std::vector<const T1*>& selParticles, const std::vector<const T2*>& looseParticles, const std::vector<const T2*>& tightParticles,
		 double dRmax = 0.2)
{
  if      ( isGenMatched(genParticle, selParticles,   dRmax) ) return 1;
  else if ( isGenMatched(genParticle, tightParticles, dRmax) ) return 2;
  else if ( isGenMatched(genParticle, looseParticles, dRmax) ) return 3;
  else                                                         return 4;
}

bool 
isHigherPt_GenLepton(const GenLepton& lepton1, const GenLepton& lepton2);

bool 
isHigherPt_GenLepton_ptr(const GenLepton* lepton1, const GenLepton* lepton2);

bool 
isHigherPt_GenJet(const GenJet& jet1, const GenJet& jet2);

bool 
isHigherPt_GenJet_ptr(const GenJet* jet1, const GenJet* jet2);

TH1* 
bookHistogram1d(fwlite::TFileService& fs, const std::string& histogramName, int numBinsX, double xMin, double xMax);

void 
printBJet(const std::string& label, const RecoJetBase* jet);

std::pair<const RecoJet*, const RecoJet*> 
selectBJetsFromHbb(const std::vector<const RecoJet*>& selJetsAK4, 
		   const RecoJetCollectionSelectorBtagLoose& jetSelectorAK4_bTagLoose, int minNumBJets_loose, 
		   const RecoJetCollectionSelectorBtagMedium& jetSelectorAK4_bTagMedium, int minNumBJets_medium);

int
countGenMatchedBJets(const std::pair<const RecoJet*, const RecoJet*>& selBJets, const std::vector<GenJet>& genBJetsForMatching, double dRmax);

#endif
