#include "hhAnalysis/bbww/interface/JetPair.h"

#include "hhAnalysis/bbww/interface/genMatchingAuxFunctions.h" // isGenMatched

#include <algorithm> // std::sort

//---------------------------------------------------------------------------------------------------
// common code, shared between H->bb and W->jj decays
bool
isHigherRankedByMass(const JetPairBase& pair1, const JetPairBase& pair2)
{
  double deltaMass1 = std::fabs(pair1.p4_.mass() - mem::wBosonMass);
  double deltaMass2 = std::fabs(pair2.p4_.mass() - mem::wBosonMass);
  return ( deltaMass1 < deltaMass2 );
}

bool
isHigherRankedByDeltaR(const JetPairBase& pair1, const JetPairBase& pair2)
{
  double deltaR1 = deltaR(pair1.jet1_->p4(), pair1.jet2_->p4());
  double deltaR2 = deltaR(pair2.jet1_->p4(), pair2.jet2_->p4());
  return ( deltaR1 < deltaR2 );
}

bool
isHigherRankedByPt(const JetPairBase& pair1, const JetPairBase& pair2)
{
  double pt1 = pair1.p4_.pt();
  double pt2 = pair2.p4_.pt();
  return ( pt1 > pt2 );
}

bool
isHigherRankedByScalarPt(const JetPairBase& pair1, const JetPairBase& pair2)
{
  double sumPt1 = pair1.jet1_->pt() + pair1.jet2_->pt();
  double sumPt2 = pair2.jet1_->pt() + pair2.jet2_->pt();
  return ( sumPt1 > sumPt2 );
}

template <typename T>
std::vector<T> 
makeJetPairsT(const std::vector<const RecoJet*>& selJetsAK4, const std::vector<const GenJet*>* genWJets)
{
  std::vector<T> jetPairs;
  for ( std::vector<const RecoJet*>::const_iterator selJet1 = selJetsAK4.begin(); selJet1 != selJetsAK4.end(); ++selJet1 ) 
  {
    for ( std::vector<const RecoJet*>::const_iterator selJet2 = selJet1 + 1; selJet2 != selJetsAK4.end(); ++selJet2 ) 
    {
      bool selJet1_isGenMatched = ( genWJets ) ? isGenMatchedT<GenJet>((*selJet1)->eta(), (*selJet1)->phi(), *genWJets) : false;
      bool selJet2_isGenMatched = ( genWJets ) ? isGenMatchedT<GenJet>((*selJet2)->eta(), (*selJet2)->phi(), *genWJets) : false;
      T jetPair(*selJet1, selJet1_isGenMatched, *selJet2, selJet2_isGenMatched);
      jetPairs.push_back(jetPair); 
    }
  }
  return jetPairs;
}
//---------------------------------------------------------------------------------------------------

//---------------------------------------------------------------------------------------------------
// code specific to H->bb decay
bool
isHigherRankedByCSV(const JetPair_Hbb& pair1, const JetPair_Hbb& pair2)
{
  double sumCSV1 = pair1.jet1_btagCSV_ + pair1.jet2_btagCSV_;
  double sumCSV2 = pair2.jet1_btagCSV_ + pair2.jet2_btagCSV_;
  return ( sumCSV1 > sumCSV2 );
}

std::vector<JetPair_Hbb> 
makeJetPairs_Hbb(const std::vector<const RecoJet*>& selJetsAK4_Hbb, const std::vector<const GenJet*>* genWJets)
{
  return makeJetPairsT<JetPair_Hbb>(selJetsAK4_Hbb, genWJets);
}

void
rankJetPairs_Hbb(std::vector<JetPair_Hbb>& jetPairs_Hbb)
{
  std::sort(jetPairs_Hbb.begin(), jetPairs_Hbb.end(), isHigherRankedByCSV);
}
//---------------------------------------------------------------------------------------------------

//---------------------------------------------------------------------------------------------------
// code specific to W->jj decay
bool
isHigherRankedByBDT(const JetPair_Wjj& pair1, const JetPair_Wjj& pair2)
{
  double bdtScore1 = pair1.bdtScore_;
  double bdtScore2 = pair2.bdtScore_;
  return ( bdtScore1 > bdtScore2 );
}

std::vector<JetPair_Wjj> 
makeJetPairs_Wjj(const std::vector<const RecoJet*>& selJetsAK4_Wjj, const std::vector<const GenJet*>* genWJets)
{
  return makeJetPairsT<JetPair_Wjj>(selJetsAK4_Wjj, genWJets);
}

TMVAInterface initialize_mva_Wjj()
{
  std::string mvaFileName_Wjj_even = "hhAnalysis/bbww/data/bb1l_HH_XGB_Wjj_10Var_even.xml";
  std::string mvaFileName_Wjj_odd  = "hhAnalysis/bbww/data/bb1l_HH_XGB_Wjj_10Var_odd.xml";
  std::vector<std::string> mvaInputVariables_Wjj = {
    "wjet1_pt",
    "wjet1_btagCSV",
    "wjet1_qgDiscr",
    "wjet2_pt",
    "wjet2_qgDiscr",
    "dR_HadW_lep", 
    "dR_wjet1wjet2",
    "HadW_mass",
    "nBJetMedium",
    "nJet"
  };
  TMVAInterface mva_Wjj(mvaFileName_Wjj_odd, mvaFileName_Wjj_even, mvaInputVariables_Wjj);
  mva_Wjj.enableBDTTransform();
  return mva_Wjj;
}

const RecoJet* getSelJetAK4(const RecoJetBase* jet_or_subjet, const std::vector<const RecoJet*>& selJetsAK4)
{
  const RecoJet* jet = nullptr;
  if ( dynamic_cast<const RecoJet*>(jet_or_subjet) )
  {
    jet = dynamic_cast<const RecoJet*>(jet_or_subjet);
  } 
  else 
  {
    double dRmin = 1.e+3;
    for ( const RecoJet* selJetAK4 : selJetsAK4 )
    {
      double dR = deltaR(jet_or_subjet->p4(), selJetAK4->p4());
      if ( dR < 0.2 && dR < dRmin )
      {
        jet = selJetAK4;
        dRmin = dR;
      }
    }
  }
  return jet;
}

void
rankJetPairs_Wjj(std::vector<JetPair_Wjj>& jetPairs_Wjj, 
                 const std::vector<const RecoJet*>& selJetsAK4_Wjj, const RecoLepton& selLepton, int nBJetMedium, 
                 const TMVAInterface& mva_Wjj, const EventInfo& eventInfo)
{
  for ( std::vector<JetPair_Wjj>::iterator jetPair = jetPairs_Wjj.begin(); jetPair != jetPairs_Wjj.end(); ++jetPair )
  {
    assert(jetPair->jet1_ && jetPair->jet2_);
    double selJet1_BtagCSV = 0.; // CV: treat jets for which b-tagging discriminator is not available as light-quark jets
    double selJet1_QGDiscr = 1.; // CV: treat jets for which quark/gluon discriminator is not available as quark jets
    const RecoJet* selJet1 = getSelJetAK4(jetPair->jet1_, selJetsAK4_Wjj);
    if ( selJet1 )
    {
      selJet1_BtagCSV = selJet1->BtagCSV();
      selJet1_QGDiscr = selJet1->QGDiscr();
    }
    Particle::LorentzVector selJet1P4 = jetPair->jet1_->p4();
    double selJet2_QGDiscr = 1.; // CV: treat jets for which quark/gluon discriminator is not available as quark jets
    const RecoJet* selJet2 = getSelJetAK4(jetPair->jet2_, selJetsAK4_Wjj);
    if ( selJet2 )
    {
      selJet2_QGDiscr = selJet2->QGDiscr();
    }
    Particle::LorentzVector selJet2P4 = jetPair->jet2_->p4();
    Particle::LorentzVector jetPairP4 = selJet1P4 + selJet2P4; 
    std::map<std::string, double> mvaInputVariables_Wjj = {
      { "wjet1_pt",             selJet1P4.pt()                    },
      { "wjet1_btagCSV",        selJet1_BtagCSV                   },
      { "wjet1_qgDiscr",        selJet1_QGDiscr                   },
      { "wjet2_pt",             selJet2P4.pt()                    },
      { "wjet2_qgDiscr",        selJet2_QGDiscr                   },
      { "dR_HadW_lep",          deltaR(jetPairP4, selLepton.p4()) },
      { "dR_wjet1wjet2",        deltaR(selJet1P4, selJet2P4)      },
      { "HadW_mass",            jetPairP4.mass()                  },
      { "nBJetMedium",          nBJetMedium                       },
      { "nJet",                 selJetsAK4_Wjj.size()             }
    };
    double bdtScore = mva_Wjj(mvaInputVariables_Wjj, eventInfo.event);
    jetPair->bdtScore_ = bdtScore;
  }
  std::sort(jetPairs_Wjj.begin(), jetPairs_Wjj.end(), isHigherRankedByBDT);
}
//---------------------------------------------------------------------------------------------------
