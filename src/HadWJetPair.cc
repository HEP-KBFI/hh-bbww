#include "hhAnalysis/bbww/interface/HadWJetPair.h"

#include "hhAnalysis/bbww/interface/genMatchingAuxFunctions.h" // isGenMatched

#include <algorithm> // std::sort

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

std::vector<HadWJetPair> 
makeHadWJetPairs(const std::vector<const RecoJet*>& selJetsAK4_Wjj, const std::vector<GenParticle>* genWJets)
{
  std::vector<HadWJetPair> hadWJetPairs;
  for ( std::vector<const RecoJet*>::const_iterator selJet1 = selJetsAK4_Wjj.begin();
	selJet1 != selJetsAK4_Wjj.end(); ++selJet1 ) {
    for ( std::vector<const RecoJet*>::const_iterator selJet2 = selJet1 + 1;
	  selJet2 != selJetsAK4_Wjj.end(); ++selJet2 ) {
      bool selJet1_isGenMatched = ( genWJets ) ? isGenMatched((*selJet1)->eta(), (*selJet1)->phi(), *genWJets) : false;
      bool selJet2_isGenMatched = ( genWJets ) ? isGenMatched((*selJet2)->eta(), (*selJet2)->phi(), *genWJets) : false;
      HadWJetPair hadWJetPair(*selJet1, selJet1_isGenMatched, *selJet2, selJet2_isGenMatched);
      hadWJetPairs.push_back(hadWJetPair); 
    }
  }
  return hadWJetPairs;
}

void
rankHadWJetPairs(std::vector<HadWJetPair>& hadWJetPairs, 
                 const std::vector<const RecoJet*>& selJetsAK4_Wjj, const RecoLepton& selLepton, int nBJetMedium, 
                 const TMVAInterface& mva_Wjj, const EventInfo& eventInfo)
{
  for ( std::vector<HadWJetPair>::iterator hadWJetPair = hadWJetPairs.begin();
        hadWJetPair != hadWJetPairs.end(); ++hadWJetPair ) { 
    const RecoJet* selJet1 = hadWJetPair->jet1_;
    assert(selJet1);
    Particle::LorentzVector selJet1P4 = selJet1->p4();
    const RecoJet* selJet2 = hadWJetPair->jet2_;
    assert(selJet2);
    Particle::LorentzVector selJet2P4 = selJet2->p4();
    Particle::LorentzVector hadWP4 = selJet1P4 + selJet2P4; 
    std::map<std::string, double> mvaInputVariables_Wjj = {
      { "HadW_mass",    hadWP4.mass()                  },
      { "jet1_btagCSV", selJet1->BtagCSV()             },
      { "dr_HadW_lep",  deltaR(hadWP4, selLepton.p4()) },
      { "dR_jj",        deltaR(selJet1P4, selJet2P4)   },
      { "jet1_pt",      selJet1P4.pt()                 },
      { "jet1_qgDiscr", selJet1->QGDiscr()             },
      { "jet2_pt",      selJet2P4.pt()                 },
      { "jet2_qgDiscr", selJet2->QGDiscr()             },
      { "nBJetMedium",  nBJetMedium                    },
      { "nJet",         selJetsAK4_Wjj.size()          }
    };
    double bdtScore = mva_Wjj(mvaInputVariables_Wjj, eventInfo.event);
    hadWJetPair->bdtScore_ = bdtScore;
  }
  std::sort(hadWJetPairs.begin(), hadWJetPairs.end(), sortHadWJetPairsByBDT());
}

