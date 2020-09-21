#ifndef hhAnalysis_bbww_JetQuad_h
#define hhAnalysis_bbww_JetQuad_h

#include "tthAnalysis/HiggsToTauTau/interface/RecoJet.h" // RecoJet
#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h" // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/Particle.h" // Particle::LorentzVector
#include "tthAnalysis/HiggsToTauTau/interface/EventInfo.h" // EventInfo
#include "tthAnalysis/HiggsToTauTau/interface/TMVAInterface.h" // TMVAInterface

#include "hhAnalysis/bbwwMEM/interface/memAuxFunctions.h" // wBosonMass
#include "DataFormats/Math/interface/deltaR.h" // deltaR

#include <vector> // std::vector<>
#include <cmath> // std::fabs

struct JetQuad
{
JetQuad(const RecoJet* BJet1, bool BJet1_isGenMatched, const RecoJet* BJet2, bool BJet2_isGenMatched,
	    const RecoJet* WJet1, bool WJet1_isGenMatched, const RecoJet* WJet2, bool WJet2_isGenMatched, double bdtScore = -1.)
    : BJet1_(BJet1)
    , BJet1_isGenMatched_(BJet1_isGenMatched)
    , BJet2_(BJet2)
    , BJet2_isGenMatched_(BJet2_isGenMatched)
    , WJet1_(WJet1)
    , WJet1_isGenMatched_(WJet1_isGenMatched)
    , WJet2_(WJet2)
    , WJet2_isGenMatched_(WJet2_isGenMatched)
    , bdtScore_(bdtScore)
  {
    assert(BJet1 && BJet2 && WJet1 && WJet2);
  }
  ~JetQuad() {}
  const RecoJet* BJet1_;
  bool BJet1_isGenMatched_;
  const RecoJet* BJet2_;
  bool BJet2_isGenMatched_;
  const RecoJet* WJet1_;
  bool WJet1_isGenMatched_;
  const RecoJet* WJet2_;
  bool WJet2_isGenMatched_;
  double bdtScore_;
};

bool
isHigherRankedByBDT(const JetQuad& quad1, const JetQuad& quad2);
TMVAInterface initialize_mva_jpa();
void
rankJetQuads(std::vector<JetQuad>& jetQuads, const RecoLepton& selLepton, int nBJetMedium, const TMVAInterface& mva_jpa, const EventInfo& eventInfo);

std::vector<const RecoJet*> 
selectJet_Quad(const std::vector<const RecoJet*> selJetsAK4, const RecoLepton selLepton, 
	       int nBJetMedium, const std::vector<const GenJet*>& genBJets_ptrs, const std::vector<const GenJet*>& genWJets_ptrs,
	       const TMVAInterface& mva_jpa, const EventInfo& eventInfo);

std::vector<JetQuad> 
makeJetQuads(const std::vector<const RecoJet*>& selJetsAK4, const std::vector<const GenJet*>& genBJets, const std::vector<const GenJet*>& genWJets);
#endif // hhAnalysis_bbww_JetQuad_h
