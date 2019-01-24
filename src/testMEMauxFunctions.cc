#include "hhAnalysis/bbww/interface/testMEMauxFunctions.h"

#include "tthAnalysis/HiggsToTauTau/interface/RecoJet.h" // RecoJet
#include "tthAnalysis/HiggsToTauTau/interface/RecoSubjetAK8.h" // RecoJet

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
isHigherPt_GenJet(const GenJet& jet1, const GenJet& jet2)
{
  return jet1.pt() > jet2.pt();
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
