#include "hhAnalysis/bbww/interface/testMEMauxFunctions.h"

#include "tthAnalysis/HiggsToTauTau/interface/RecoJet.h" // RecoJet
#include "tthAnalysis/HiggsToTauTau/interface/RecoSubjetAK8.h" // RecoJet
#include "hhAnalysis/bbwwMEM/interface/memAuxFunctions.h" // mem::higgsBosonMass

#include <iostream>
#include <iomanip>

std::pair<const GenLepton*, const GenParticle*> 
findGenLepton_and_NeutrinoFromWBoson(const GenParticle* genWBoson, const std::vector<GenLepton>& genLeptons, const std::vector<GenParticle>& genNeutrinos)
{
  const GenLepton* genLeptonFromWBoson = nullptr;
  const GenParticle* genNeutrinoFromWBoson = nullptr;
  double minDeltaMass = 1.e+3;
  for ( std::vector<GenLepton>::const_iterator genLepton = genLeptons.begin();
	genLepton != genLeptons.end(); ++genLepton ) {
    for ( std::vector<GenParticle>::const_iterator genNeutrino = genNeutrinos.begin();
	  genNeutrino != genNeutrinos.end(); ++genNeutrino ) {
      Particle::LorentzVector genLepton_and_NeutrinoP4 = genLepton->p4() + genNeutrino->p4();
      double deltaMass = TMath::Abs(genLepton_and_NeutrinoP4.mass() - genWBoson->mass());
      double dR = deltaR(genLepton_and_NeutrinoP4, genWBoson->p4());
      if ( deltaMass < 5. && deltaMass < minDeltaMass && dR < 1. ) {
	genLeptonFromWBoson = &(*genLepton);
	genNeutrinoFromWBoson = &(*genNeutrino);
	minDeltaMass = deltaMass;
      }
    }
  }
  return std::pair<const GenLepton*, const GenParticle*>(genLeptonFromWBoson, genNeutrinoFromWBoson);
}

bool
isHigherPt_GenLepton(const GenLepton& lepton1, const GenLepton& lepton2)
{
  return lepton1.pt() > lepton2.pt();
}

bool
isHigherPt_GenLepton_ptr(const GenLepton* lepton1, const GenLepton* lepton2)
{
  return lepton1->pt() > lepton2->pt();
}

bool
isHigherPt_GenJet(const GenJet& jet1, const GenJet& jet2)
{
  return jet1.pt() > jet2.pt();
}

bool
isHigherPt_GenJet_ptr(const GenJet* jet1, const GenJet* jet2)
{
  return jet1->pt() > jet2->pt();
}

TH1*
bookHistogram1d(fwlite::TFileService& fs, const std::string& histogramName, int numBinsX, double xMin, double xMax)
{
  return fs.make<TH1D>(histogramName.data(), histogramName.data(), numBinsX, xMin, xMax);
}

void 
printBJet(const std::string& label, const RecoJetBase* jet) 
{
  std::cout << label << ": pT = " << jet->pt() << ", eta = " << jet->eta() << ", phi = " << jet->phi();
  if ( dynamic_cast<const RecoJet*>(jet) ) {
    std::cout << " (btagCSV = " << (dynamic_cast<const RecoJet*>(jet))->BtagCSV() << ")";
  } else if ( dynamic_cast<const RecoSubjetAK8*>(jet) ) {
    std::cout << " (btagCSV = " << (dynamic_cast<const RecoSubjetAK8*>(jet))->BtagCSV() << ")";
  } 
  std::cout << std::endl;
}

std::pair<const RecoJet*, const RecoJet*> 
selectBJetsFromHbb(const std::vector<const RecoJet*>& selJetsAK4, 
		   const RecoJetCollectionSelectorBtagLoose& jetSelectorAK4_bTagLoose, int minNumBJets_loose, 
		   const RecoJetCollectionSelectorBtagMedium& jetSelectorAK4_bTagMedium, int minNumBJets_medium)
{
  const RecoJet* selJet1_Hbb = nullptr;
  const RecoJet* selJet2_Hbb = nullptr;
  double minDeltaMass = 1.e+3;
  for ( std::vector<const RecoJet*>::const_iterator selJet1 = selJetsAK4.begin();
	selJet1 != selJetsAK4.end(); ++selJet1 ) {
    for ( std::vector<const RecoJet*>::const_iterator selJet2 = selJet1 + 1;
	  selJet2 != selJetsAK4.end(); ++selJet2 ) {
      int numBJets_loose = 0;
      if ( jetSelectorAK4_bTagLoose.getSelector()(**selJet1) ) ++numBJets_loose;
      if ( jetSelectorAK4_bTagLoose.getSelector()(**selJet2) ) ++numBJets_loose;
      int numBJets_medium = 0;
      if ( jetSelectorAK4_bTagMedium.getSelector()(**selJet1) ) ++numBJets_medium;
      if ( jetSelectorAK4_bTagMedium.getSelector()(**selJet2) ) ++numBJets_medium;
      if ( numBJets_loose >= minNumBJets_loose || numBJets_medium >= minNumBJets_medium ) {
	double deltaMass = TMath::Abs(((*selJet1)->p4() + (*selJet2)->p4()).mass() - mem::higgsBosonMass);
	if ( deltaMass < minDeltaMass ) {
	  selJet1_Hbb = (*selJet1);
	  selJet2_Hbb = (*selJet2);
	  minDeltaMass = deltaMass;
	}
      }
    }
  }
  return std::pair<const RecoJet*, const RecoJet*>(selJet1_Hbb, selJet2_Hbb);
}

namespace
{

bool isMatched(const RecoJet& selJet, const std::vector<GenJet>& genBJetsForMatching, double dRmax)
{
  for ( std::vector<GenJet>::const_iterator genBJet = genBJetsForMatching.begin();
	genBJet != genBJetsForMatching.end(); ++genBJet ) {
    double dR = deltaR(selJet.p4(), genBJet->p4());
    if ( dR < dRmax ) return true;
  }
  return false;
}

}

int
countGenMatchedBJets(const std::pair<const RecoJet*, const RecoJet*>& selBJets, const std::vector<GenJet>& genBJetsForMatching, double dRmax)
{
  int numGenMatchedBJets = 0;
  if ( selBJets.first  && isMatched(*selBJets.first,  genBJetsForMatching, dRmax) ) ++numGenMatchedBJets;
  if ( selBJets.second && isMatched(*selBJets.second, genBJetsForMatching, dRmax) ) ++numGenMatchedBJets;
  return numGenMatchedBJets;
}
