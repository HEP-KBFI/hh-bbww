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
#include "hhAnalysis/bbww/interface/genMatchingAuxFunctions.h" // isGenMatched

#include <TMath.h> // TMath
#include <TH1.h> // TH1

#include <string> // std::string
#include <vector> // std::vector<>

template<typename T1, typename T2>
int 
compGenMatchType(const GenParticle* genParticle, 
		 const std::vector<const T1*>& selParticles, const std::vector<const T2*>& looseParticles, const std::vector<const T2*>& tightParticles,
		 double dRmax = 0.2)
{
  if      ( isGenMatched(genParticle->eta(), genParticle->phi(), selParticles,   dRmax) ) return 1;
  else if ( isGenMatched(genParticle->eta(), genParticle->phi(), tightParticles, dRmax) ) return 2;
  else if ( isGenMatched(genParticle->eta(), genParticle->phi(), looseParticles, dRmax) ) return 3;
  else                                                                                    return 4;
}

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
