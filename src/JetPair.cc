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
    "HadW_mass",
    "jet1_btagCSV",
    "dr_HadW_lep",
    "dR_jj",
    "jet1_pt",
    "jet1_qgDiscr",
    "jet2_pt",
    "jet2_qgDiscr",
    "nBJetMedium",
    "nJet"
  };
  TMVAInterface mva_Wjj(mvaFileName_Wjj_odd, mvaFileName_Wjj_even, mvaInputVariables_Wjj);
  mva_Wjj.enableBDTTransform();
  return mva_Wjj;
}

void
rankJetPairs_Wjj(std::vector<JetPair_Wjj>& jetPairs_Wjj, 
                 const std::vector<const RecoJet*>& selJetsAK4_Wjj, const RecoLepton& selLepton, int nBJetMedium, 
                 const TMVAInterface& mva_Wjj, const EventInfo& eventInfo)
{
  for ( std::vector<JetPair_Wjj>::iterator jetPair = jetPairs_Wjj.begin(); jetPair != jetPairs_Wjj.end(); ++jetPair )
  {
    const RecoJet* selJet1 = jetPair->jet1_;
    assert(selJet1);
    Particle::LorentzVector selJet1P4 = selJet1->p4();
    const RecoJet* selJet2 = jetPair->jet2_;
    assert(selJet2);
    Particle::LorentzVector selJet2P4 = selJet2->p4();
    Particle::LorentzVector jetPairP4 = selJet1P4 + selJet2P4; 
    std::map<std::string, double> mvaInputVariables_Wjj = {
      { "HadW_mass",    jetPairP4.mass()                  },
      { "jet1_btagCSV", selJet1->BtagCSV()                },
      { "dr_HadW_lep",  deltaR(jetPairP4, selLepton.p4()) },
      { "dR_jj",        deltaR(selJet1P4, selJet2P4)      },
      { "jet1_pt",      selJet1P4.pt()                    },
      { "jet1_qgDiscr", selJet1->QGDiscr()                },
      { "jet2_pt",      selJet2P4.pt()                    },
      { "jet2_qgDiscr", selJet2->QGDiscr()                },
      { "nBJetMedium",  nBJetMedium                       },
      { "nJet",         selJetsAK4_Wjj.size()             }
    };
    double bdtScore = mva_Wjj(mvaInputVariables_Wjj, eventInfo.event);
    jetPair->bdtScore_ = bdtScore;
  }
  std::sort(jetPairs_Wjj.begin(), jetPairs_Wjj.end(), isHigherRankedByBDT);
}
//---------------------------------------------------------------------------------------------------
