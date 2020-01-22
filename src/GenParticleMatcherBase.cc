#include "hhAnalysis/bbww/interface/GenParticleMatcherBase.h"

GenParticleMatcherBase::GenParticleMatcherBase()
 : genMEtPt_(0.)
 , genMEtPhi_(0)
{}

GenParticleMatcherBase::~GenParticleMatcherBase()
{}

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
  met_ptr->set_genPt(genMEtPt_);
  met_ptr->set_genPhi(genMEtPhi_);
}
