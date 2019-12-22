#ifndef hhAnalysis_bbww_HadWJetPair_h
#define hhAnalysis_bbww_HadWJetPair_h

#include "tthAnalysis/HiggsToTauTau/interface/RecoJet.h" // RecoJet
#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h" // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/Particle.h" // Particle::LorentzVector
#include "tthAnalysis/HiggsToTauTau/interface/TMVAInterface.h" // TMVAInterface
#include "tthAnalysis/HiggsToTauTau/interface/EventInfo.h" // EventInfo
#include "hhAnalysis/bbwwMEM/interface/memAuxFunctions.h" // wBosonMass
#include "DataFormats/Math/interface/deltaR.h" // deltaR

#include <vector> // std::vector<>
#include <cmath> // std::fabs

struct HadWJetPair
{
  HadWJetPair(const RecoJet* jet1, bool jet1_isGenMatched, const RecoJet* jet2, bool jet2_isGenMatched, double bdtScore = -1.)
    : jet1_(jet1)
    , jet1_isGenMatched_(jet1_isGenMatched)
    , jet2_(jet2)
    , jet2_isGenMatched_(jet2_isGenMatched)
    , bdtScore_(bdtScore)
  {
    assert(jet1 && jet2);
    p4_ = jet1->p4() + jet2->p4();
  }
  ~HadWJetPair() {}
  Particle::LorentzVector p4_;
  const RecoJet* jet1_;
  bool jet1_isGenMatched_;
  const RecoJet* jet2_;
  bool jet2_isGenMatched_;
  double bdtScore_;
};

struct sortHadWJetPairsByMass
{
  bool operator() (const HadWJetPair& pair1, const HadWJetPair& pair2)
  {
    double deltaMass1 = std::fabs(pair1.p4_.mass() - mem::wBosonMass);
    double deltaMass2 = std::fabs(pair2.p4_.mass() - mem::wBosonMass);
    return ( deltaMass1 < deltaMass2 );
  }
};
struct sortHadWJetPairsByDeltaR
{
  bool operator() (const HadWJetPair& pair1, const HadWJetPair& pair2)
  {
    double deltaR1 = deltaR(pair1.jet1_->p4(), pair1.jet2_->p4());
    double deltaR2 = deltaR(pair2.jet1_->p4(), pair2.jet2_->p4());
    return ( deltaR1 < deltaR2 );
  }
};
struct sortHadWJetPairsByPt
{
  bool operator() (const HadWJetPair& pair1, const HadWJetPair& pair2)
  {
    double pt1 = pair1.p4_.pt();
    double pt2 = pair2.p4_.pt();
    return ( pt1 > pt2 );
  }
};
struct sortHadWJetPairsByScalarPt
{
  bool operator() (const HadWJetPair& pair1, const HadWJetPair& pair2)
  {
    double sumPt1 = pair1.jet1_->pt() + pair1.jet2_->pt();
    double sumPt2 = pair2.jet1_->pt() + pair2.jet2_->pt();
    return ( sumPt1 > sumPt2 );
  }
};
struct sortHadWJetPairsByBDT
{
  bool operator() (const HadWJetPair& pair1, const HadWJetPair& pair2)
  {
    double bdtScore1 = pair1.bdtScore_;
    double bdtScore2 = pair2.bdtScore_;
    return ( bdtScore1 > bdtScore2 );
  }
};

TMVAInterface initialize_mva_Wjj();

std::vector<HadWJetPair> 
makeHadWJetPairs(const std::vector<const RecoJet*>& selJetsAK4_Wjj, const std::vector<GenParticle>* genWJets = nullptr);

void
rankHadWJetPairs(std::vector<HadWJetPair>& hadWJetPairs, 
	         const std::vector<const RecoJet*>& selJetsAK4_Wjj, const RecoLepton& selLepton, int nBJetMedium, 
                 const TMVAInterface& mva_Wjj, const EventInfo& eventInfo);

#endif // HadWJetPair_h
