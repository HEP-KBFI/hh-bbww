#include "hhAnalysis/bbww/interface/measuredParticleAuxFunctions.h"

#include "hhAnalysis/bbwwMEM/interface/memAuxFunctions.h" // mem::electronMass, mem::muonMass, mem::bottomQuarkMass

mem::MeasuredParticle
convert_to_MeasuredParticle(const RecoLepton& lepton)
{
  int type = mem::MeasuredParticle::kUndefinedType;
  double mass = 0.;
  if ( lepton.is_electron() ) 
  {
    mass = mem::electronMass;
    type = mem::MeasuredParticle::kElectron;
  }
  else if ( lepton.is_muon() ) 
  {
    mass = mem::muonMass;
    type = mem::MeasuredParticle::kMuon;
  }
  else assert(0);
  return mem::MeasuredParticle(type, lepton.pt(), lepton.eta(), lepton.phi(), mass, lepton.charge());
}

std::vector<mem::MeasuredParticle>
convert_to_MeasuredParticles(const std::vector<const RecoLepton*>& leptons)
{
  std::vector<mem::MeasuredParticle> retVal;
  for ( std::vector<const RecoLepton*>::const_iterator lepton = leptons.begin();
        lepton != leptons.end(); ++lepton ) {
    retVal.push_back(convert_to_MeasuredParticle(**lepton));
  }
  return retVal;
}

mem::MeasuredParticle
convert_to_MeasuredParticle(const RecoSubjetAK8& subJet, bool isBJet)
{
  int type = ( isBJet ) ? mem::MeasuredParticle::kBJet : mem::MeasuredParticle::kHadWJet;
  double mass = ( isBJet ) ? mem::bottomQuarkMass : subJet.mass();
  return mem::MeasuredParticle(type, subJet.pt(), subJet.eta(), subJet.phi(), mass);
}

std::pair<mem::MeasuredParticle, mem::MeasuredParticle>
convert_to_MeasuredParticle(const RecoJetAK8& jet, bool isHbb)
{
  assert(jet.subJet1() && jet.subJet2());
  mem::MeasuredParticle subJet1 = convert_to_MeasuredParticle(*jet.subJet1(), isHbb);
  mem::MeasuredParticle subJet2 = convert_to_MeasuredParticle(*jet.subJet2(), isHbb);
  return std::make_pair(subJet1, subJet2);
}

std::vector<std::pair<mem::MeasuredParticle, mem::MeasuredParticle>>
convert_to_MeasuredParticles(const std::vector<const RecoJetAK8*> jets, bool isHbb)
{
  std::vector<std::pair<mem::MeasuredParticle, mem::MeasuredParticle>> retVal;
  for ( std::vector<const RecoJetAK8*>::const_iterator jet = jets.begin();
        jet != jets.end(); ++jet ) {
    retVal.push_back(convert_to_MeasuredParticle(**jet, isHbb));
  }
  return retVal;
}

mem::MeasuredParticle
convert_to_MeasuredParticle(const RecoJet& jet, bool isBJet)
{
  int type = ( isBJet ) ? mem::MeasuredParticle::kBJet : mem::MeasuredParticle::kHadWJet;
  double mass = ( isBJet ) ? mem::bottomQuarkMass : jet.mass();
  return mem::MeasuredParticle(type, jet.pt(), jet.eta(), jet.phi(), mass);
}

std::vector<mem::MeasuredParticle>
convert_to_MeasuredParticles(const std::vector<const RecoJet*>& jets, bool isBJet)
{
  std::vector<mem::MeasuredParticle> retVal;
  for ( std::vector<const RecoJet*>::const_iterator jet = jets.begin();
        jet != jets.end(); ++jet ) {
    retVal.push_back(convert_to_MeasuredParticle(**jet, isBJet));
  }
  return retVal;
}
