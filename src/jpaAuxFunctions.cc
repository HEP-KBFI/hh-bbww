#include "hhAnalysis/bbww/interface/jpaAuxFunctions.h"

#include "DataFormats/Math/interface/deltaR.h" // deltaR

JPAJet 
convert_to_JPAJet(const RecoJet* ak4Jet)
{
  JPAJet ak4Jet_jpa(ak4Jet->p4(), ak4Jet->p4_bRegCorr(), ak4Jet->BtagCSV(), ak4Jet->QGDiscr());
  return ak4Jet_jpa;
}

std::pair<JPAJet, JPAJet> 
convert_to_JPAJets(const RecoJetAK8* ak8Jet)
{
  assert(ak8Jet->subJet1() && ak8Jet->subJet2());

  const RecoSubjetAK8* ak8jet_subjet1 = ak8Jet->subJet1();
  double ak8jet_subjet1_QGDiscr = 1.; // CV: treat jets for which quark/gluon discriminator is not available as quark jets
  JPAJet ak8jet_subjet1_jpa(ak8jet_subjet1->p4(), ak8jet_subjet1->p4(), ak8jet_subjet1->BtagCSV(), ak8jet_subjet1_QGDiscr);

  const RecoSubjetAK8* ak8jet_subjet2 = ak8Jet->subJet2();
  double ak8jet_subjet2_QGDiscr = 1.; // CV: treat jets for which quark/gluon discriminator is not available as quark jets
  JPAJet ak8jet_subjet2_jpa(ak8jet_subjet2->p4(), ak8jet_subjet2->p4(), ak8jet_subjet2->BtagCSV(), ak8jet_subjet2_QGDiscr);

  return std::pair<JPAJet, JPAJet>(ak8jet_subjet1_jpa, ak8jet_subjet2_jpa);
}

const RecoJetBase*
convert_to_RecoJet(const JPAJet* ak4Jet_jpa, const std::vector<const RecoJet*>& ak4Jets)
{
  const RecoJetBase* ak4Jet_matched = nullptr;
  if ( ak4Jet_jpa )
  {
    double dRmatch = 1.e+3;
    for ( std::vector<const RecoJet*>::const_iterator ak4Jet = ak4Jets.begin();
          ak4Jet != ak4Jets.end(); ++ak4Jet ) {
      double dR = deltaR(ak4Jet_jpa->p4(), (*ak4Jet)->p4());
      if ( dR < 1.e-1 && dR < dRmatch )
      {
        ak4Jet_matched = *ak4Jet;
        dRmatch = dR;
      }
    }
    assert(ak4Jet_matched);
  }
  return ak4Jet_matched;
}
