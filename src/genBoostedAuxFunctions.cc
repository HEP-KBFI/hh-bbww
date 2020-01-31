#include "hhAnalysis/bbww/interface/genBoostedAuxFunctions.h"

#include "DataFormats/Math/interface/deltaR.h" // deltaR

#include <TMath.h> // TMath::Abs

bool isBoosted_genHbb(const std::vector<const GenJet*>& genBJets, double dRmax_fatjet)
{
  if ( !(genBJets.size() >= 2) ) return false;
  Particle::LorentzVector fatjetP4 = compSumP4(genBJets);
  bool isBoosted = true;
  int numSubJets_lo = 0;
  int numSubJets_hi = 0;	
  for ( const GenJet* genBJet : genBJets )
  {
    if ( genBJet->pt() > 20. && genBJet->absEta() < 2.4 ) ++numSubJets_lo;
    if ( genBJet->pt() > 30. && genBJet->absEta() < 2.4 ) ++numSubJets_hi;
    double dR = deltaR(genBJet->p4(), fatjetP4);
    if ( dR > dRmax_fatjet ) 
    { 
      isBoosted = false;
      break;
    }
  }
  if ( fatjetP4.pt() > 200. && TMath::Abs(fatjetP4.eta()) < 2.4 && numSubJets_lo >= 2 && numSubJets_hi >= 1 && isBoosted ) return true;
  else return false;
}

bool isBoosted_genWjj(const std::vector<const GenJet*>& genWJets, const std::vector<const GenLepton*>& genLeptons, double dRmax_fatjet, double dRmax_lepton)
{
  if ( !(genWJets.size() >= 2 && genLeptons.size() >= 1) ) return false;
  Particle::LorentzVector fatjetP4 = compSumP4(genWJets);
  bool isBoosted = true;
  int numSubJets = 0;
  for ( const GenJet* genWJet : genWJets )
  {
    if ( genWJet->pt() > 20. && genWJet->absEta() < 2.4 ) ++numSubJets;
    double dR = deltaR(genWJet->p4(), fatjetP4);
    if ( dR > dRmax_fatjet ) 
    { 
      isBoosted = false;
      break;
    }
  }
  int numLeptons_withinFatjet = 0;
  for ( const GenLepton* genLepton : genLeptons )
  {
    double dR = deltaR(genLepton->p4(), fatjetP4);
    if ( dR < dRmax_lepton ) 
    { 
      ++numLeptons_withinFatjet;
    } 
  }
  if ( fatjetP4.pt() > 100. && TMath::Abs(fatjetP4.eta()) < 2.4 && numSubJets >= 2 && isBoosted && numLeptons_withinFatjet >= 1 ) return true;
  else return false;
}
