#ifndef hhAnalysis_bbww_JetPair_h
#define hhAnalysis_bbww_JetPair_h

#include "tthAnalysis/HiggsToTauTau/interface/RecoJet.h" // RecoJet
#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h" // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/Particle.h" // Particle::LorentzVector
#include "tthAnalysis/HiggsToTauTau/interface/TMVAInterface.h" // TMVAInterface
#include "tthAnalysis/HiggsToTauTau/interface/EventInfo.h" // EventInfo
#include "hhAnalysis/bbwwMEM/interface/memAuxFunctions.h" // wBosonMass
#include "DataFormats/Math/interface/deltaR.h" // deltaR

#include <vector> // std::vector<>
#include <cmath> // std::fabs

struct JetPairBase
{
  JetPairBase(const RecoJet* jet1, bool jet1_isGenMatched, const RecoJet* jet2, bool jet2_isGenMatched)
    : jet1_(jet1)
    , jet1_isGenMatched_(jet1_isGenMatched)
    , jet2_(jet2)
    , jet2_isGenMatched_(jet2_isGenMatched)
  {
    assert(jet1 && jet2);
    p4_ = jet1->p4() + jet2->p4();
  }
  ~JetPairBase() {}
  Particle::LorentzVector p4_;
  const RecoJet* jet1_;
  bool jet1_isGenMatched_;
  const RecoJet* jet2_;
  bool jet2_isGenMatched_;
};

bool isHigherRankedByMass(const JetPairBase& pair1, const JetPairBase& pair2);
bool isHigherRankedByDeltaR(const JetPairBase& pair1, const JetPairBase& pair2);
bool isHigherRankedByPt(const JetPairBase& pair1, const JetPairBase& pair2);
bool isHigherRankedByScalarPt(const JetPairBase& pair1, const JetPairBase& pair2);

struct JetPair_Hbb : public JetPairBase
{
  JetPair_Hbb(const RecoJet* jet1, bool jet1_isGenMatched, const RecoJet* jet2, bool jet2_isGenMatched, double bdtScore = -1.)
    : JetPairBase(jet1, jet1_isGenMatched, jet2, jet2_isGenMatched)
    , jet1_btagCSV_(jet1->BtagCSV())
    , jet2_btagCSV_(jet2->BtagCSV()) 
  {}
  ~JetPair_Hbb() {}
  double jet1_btagCSV_;
  double jet2_btagCSV_;
};

bool isHigherRankedByCSV(const JetPair_Hbb& pair1, const JetPair_Hbb& pair2);

std::vector<JetPair_Hbb> 
makeJetPairs_Hbb(const std::vector<const RecoJet*>& selJetsAK4_Hbb, const std::vector<const GenJet*>* genWJets = nullptr);

void
rankJetPairs_Hbb(std::vector<JetPair_Hbb>& jetPairs_Hbb);

struct JetPair_Wjj : public JetPairBase
{
  JetPair_Wjj(const RecoJet* jet1, bool jet1_isGenMatched, const RecoJet* jet2, bool jet2_isGenMatched, double bdtScore = -1.)
    : JetPairBase(jet1, jet1_isGenMatched, jet2, jet2_isGenMatched)
    , bdtScore_(bdtScore)
  {}
  ~JetPair_Wjj() {}
  double bdtScore_;
};

bool
isHigherRankedByBDT(const JetPair_Wjj& pair1, const JetPair_Wjj& pair2);

std::vector<JetPair_Wjj> 
makeJetPairs_Wjj(const std::vector<const RecoJet*>& selJetsAK4_Wjj, const std::vector<const GenJet*>* genWJets = nullptr);

TMVAInterface initialize_mva_Wjj();

void
rankJetPairs_Wjj(std::vector<JetPair_Wjj>& jetPairs_Wjj, 
	         const std::vector<const RecoJet*>& selJetsAK4_Wjj, const RecoLepton& selLepton, int nBJetMedium, 
                 const TMVAInterface& mva_Wjj, const EventInfo& eventInfo);

template<typename T>
int
getIndex_isGenMatched(const std::vector<T>& pairs)
{
  size_t numPairs = pairs.size();
  for ( size_t idx = 0; idx < numPairs; ++idx ) 
  {
    const T& pair = pairs[idx];
    if ( pair.jet1_isGenMatched_ && pair.jet2_isGenMatched_ )
    {
      return idx;
    }
  }
  return -1;
}

#endif // JetPair_h
