#include "hhAnalysis/bbww/interface/GenParticleMatcherBase.h"

GenParticleMatcherBase::GenParticleMatcherBase()
{}

GenParticleMatcherBase::~GenParticleMatcherBase()
{}

const std::vector<GenLepton>& 
GenParticleMatcherBase::getLeptons() const
{
  return genLeptonsForMatching_;
}

const std::vector<GenParticle>& 
GenParticleMatcherBase::getWQuarks() const
{
  return genWQuarksForMatching_;
}

const std::vector<GenJet>& 
GenParticleMatcherBase::getWJets() const
{
  return genWJetsForMatching_;
}

const std::vector<GenParticle>& 
GenParticleMatcherBase::getBQuarks() const
{
  return genBQuarksForMatching_;
}

const std::vector<GenJet>& 
GenParticleMatcherBase::getBJets() const
{
  return genBJetsForMatching_;
}

const Particle::LorentzVector&
GenParticleMatcherBase::getMEt() const
{
  return genMEtP4_;
}

std::vector<GenJet> 
GenParticleMatcherBase::convert_genQuarks_to_genJets(const std::vector<GenParticle>& genQuarks, double mass)
{
  std::vector<GenJet> genJets;
  for ( std::vector<GenParticle>::const_iterator genQuark = genQuarks.begin(); genQuark != genQuarks.end(); ++genQuark )
  {
    double genJet_mass = ( mass >= 0. ) ? mass : genQuark->mass();
    genJets.push_back(GenJet(genQuark->pt(), genQuark->eta(), genQuark->phi(), genJet_mass, genQuark->pdgId()));
  }
  return genJets;
}

void 
GenParticleMatcherBase::operator()(const std::vector<const RecoLepton*>& selLeptons, 
                                   const std::vector<const RecoJetBase*>& selJets_Hbb, 
                                   const std::vector<const RecoJetBase*>& selJets_Wjj, 
                                   const RecoMEt& met)
{
  leptonGenMatcher_.addGenLeptonMatch(selLeptons, genLeptonsForMatching_, 0.2);
  jet_or_subjetGenMatcher_.addGenJetMatch(selJets_Hbb, genBJetsForMatching_, 0.2);
  jet_or_subjetGenMatcher_.addGenJetMatch(selJets_Wjj, genWJetsForMatching_, 0.2);
  RecoMEt* met_ptr = const_cast<RecoMEt*>(&met);
  met_ptr->set_genPt(genMEtP4_.pt());
  met_ptr->set_genPhi(genMEtP4_.phi());
}
