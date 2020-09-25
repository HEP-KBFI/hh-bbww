#ifndef hhAnalysis_bbww_JetQuad_h
#define hhAnalysis_bbww_JetQuad_h

#include "tthAnalysis/HiggsToTauTau/interface/RecoJet.h" // RecoJet
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetAK8.h" // RecoJetAK8
#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h" // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/Particle.h" // Particle::LorentzVector
#include "tthAnalysis/HiggsToTauTau/interface/EventInfo.h" // EventInfo
#include "tthAnalysis/HiggsToTauTau/interface/TMVAInterface.h" // TMVAInterface
#include "tthAnalysis/HiggsToTauTau/interface/XGBInterface.h" // TMVAInterface
#include "hhAnalysis/bbwwMEM/interface/memAuxFunctions.h" // wBosonMass
#include "DataFormats/Math/interface/deltaR.h" // deltaR

#include <vector> // std::vector<>
#include <cmath> // std::fabs

struct JetQuadBase
{
JetQuadBase(const RecoJetBase* BJet1=nullptr, bool BJet1_isGenMatched=false, const RecoJetBase* BJet2=nullptr, bool BJet2_isGenMatched=false,
	    const RecoJetBase* WJet1=nullptr, bool WJet1_isGenMatched=false, const RecoJetBase* WJet2=nullptr, bool WJet2_isGenMatched=false, double bdtScore = -1.)
    : BJet1_(BJet1)
    , BJet1_isGenMatched_(BJet1_isGenMatched)
    , BJet2_(BJet2)
    , BJet2_isGenMatched_(BJet2_isGenMatched)
    , WJet1_(WJet1)
    , WJet1_isGenMatched_(WJet1_isGenMatched)
    , WJet2_(WJet2)
    , WJet2_isGenMatched_(WJet2_isGenMatched)
    , bdtScore_(bdtScore)
  {}
  ~JetQuadBase() {}
  const RecoJetBase* BJet1_;
  bool BJet1_isGenMatched_;
  const RecoJetBase* BJet2_;
  bool BJet2_isGenMatched_;
  const RecoJetBase* WJet1_;
  bool WJet1_isGenMatched_;
  const RecoJetBase* WJet2_;
  bool WJet2_isGenMatched_;
  double bdtScore_;
};

struct JetQuad : public JetQuadBase
{
 JetQuad(const RecoJet* BJet1, bool BJet1_isGenMatched, const RecoJet* BJet2, bool BJet2_isGenMatched,
			const RecoJet* WJet1, bool WJet1_isGenMatched, const RecoJet* WJet2, bool WJet2_isGenMatched, double bdtScore = -1.)
    : JetQuadBase(BJet1, BJet1_isGenMatched, BJet2, BJet2_isGenMatched, WJet1, WJet1_isGenMatched, WJet2, WJet2_isGenMatched, bdtScore)
    {
      assert(BJet1 && BJet2 && WJet1 && WJet2);
    }
  ~JetQuad() {}
};

struct JetTripletMissingBJet : public JetQuadBase
{
  JetTripletMissingBJet(const RecoJet* BJet1, bool BJet1_isGenMatched,
	  const RecoJet* WJet1, bool WJet1_isGenMatched, const RecoJet* WJet2, bool WJet2_isGenMatched, double bdtScore = -1.)
  : JetQuadBase(BJet1, BJet1_isGenMatched, nullptr, false, WJet1, WJet1_isGenMatched, WJet2, WJet2_isGenMatched, bdtScore)
  {
    assert(BJet1 && WJet1 && WJet2);
  }
  ~JetTripletMissingBJet() {}
};

struct JetTripletMissingWJet : public JetQuadBase
{
JetTripletMissingWJet(const RecoJet* BJet1, bool BJet1_isGenMatched, const RecoJet* BJet2, bool BJet2_isGenMatched,
			const RecoJet* WJet1, bool WJet1_isGenMatched, double bdtScore = -1.)
  : JetQuadBase(BJet1, BJet1_isGenMatched, BJet2, BJet2_isGenMatched, WJet1, WJet1_isGenMatched, nullptr, false, bdtScore)
  {
    assert(BJet1 && BJet2 && WJet1);
  }
  ~JetTripletMissingWJet() {}
};

struct JetDoubletMissingAllWJet : public JetQuadBase
{
 JetDoubletMissingAllWJet(const RecoJet* BJet1, bool BJet1_isGenMatched, const RecoJet* BJet2, bool BJet2_isGenMatched,
		       double bdtScore = -1.)
    : JetQuadBase(BJet1, BJet1_isGenMatched, BJet2, BJet2_isGenMatched, nullptr, false, nullptr, false, bdtScore)
    {
      assert(BJet1 && BJet2);
    }
  ~JetDoubletMissingAllWJet() {}
};

struct JetSingletMissingBJetMissingAllWJet : public JetQuadBase
{
 JetSingletMissingBJetMissingAllWJet(const RecoJet* BJet1, bool BJet1_isGenMatched,
                        double bdtScore = -1.)
   : JetQuadBase(BJet1, BJet1_isGenMatched, nullptr, false, nullptr, false, nullptr, false, bdtScore)
    {
      assert(BJet1);
    }
  ~JetSingletMissingBJetMissingAllWJet() {}
};

struct JetDoubletMissingBJetMissingWJet : public JetQuadBase
{
  JetDoubletMissingBJetMissingWJet(const RecoJet* BJet1, bool BJet1_isGenMatched, 
				   const RecoJet* WJet1, bool WJet1_isGenMatched, double bdtScore = -1.)
    : JetQuadBase(BJet1, BJet1_isGenMatched, nullptr, false, WJet1, WJet1_isGenMatched, nullptr, false, bdtScore)
    {
      assert(BJet1 && WJet1);
    }
  ~JetDoubletMissingBJetMissingWJet() {}
};

bool isHigherRankedByBDT(const JetQuadBase& quad1, const JetQuadBase& quad2);

TMVAInterface initialize_mva_jpa_4jet(bool Hbb_isBoosted = false);
TMVAInterface initialize_mva_jpa_missingWJet(bool Hbb_isBoosted = false);
TMVAInterface initialize_mva_jpa_missingBJet();
TMVAInterface initialize_mva_jpa_missingBJetmissingWJet();
TMVAInterface initialize_mva_jpa_missingAllWJet();
TMVAInterface initialize_mva_jpa_missingBJetmissingAllWJet();
TMVAInterface initialize_mva_evt_category(bool Hbb_isBoosted = false);

int evt_category(const TMVAInterface& mva, double bdtScore_jpa_4jet, double bdtScore_jpa_missingWJet, double bdtScore_jpa_missingBJet, 
		 double bdtScore_jpa_missingAllWJet, double bdtScore_jpa_missingBJet_missingWJet, double bdtScore_jpa_missingBJet_missingAllWJet,
		 EventInfo eventInfo, RecoJetAK8* selJetAK8_Hbb = nullptr );

void
rankJetQuads(std::vector<JetQuadBase>& jetQuads, const RecoLepton& selLepton, 
	     int nBJetMedium, 
	     const Particle::LorentzVector& metP4,
	     const TMVAInterface& mva, const EventInfo& eventInfo, const RecoJetAK8* selJetAK8_Hbb = nullptr);
void rankJetTripletsMissingBJet(std::vector<JetQuadBase>& jetTriplets, const RecoLepton& selLepton, int nJet, int nBJetMedium, const TMVAInterface& mva, const EventInfo& eventInfo);
void rankJetTripletsMissingWJet(std::vector<JetQuadBase>& jetTriplets, const RecoLepton& selLepton, 
				int nJet, int nBJetLoose, int nBJetMedium, 
				const TMVAInterface& mva, const EventInfo& eventInfo, const RecoJetAK8* selJetAK8_Hbb = nullptr);
void rankJetDoubletsMissingBJetMissingWJet(std::vector<JetQuadBase>& jetDoublets, const RecoLepton& selLepton, 
					   int nJet, int nBJetLoose, int nBJetMedium, int nLep, const TMVAInterface& mva, const EventInfo& eventInfo);
void rankJetDoubletsMissingAllWJet(std::vector<JetQuadBase>& jetDoublets, const RecoLepton& selLepton,
                                           int nJet, int nBJetMedium, const TMVAInterface& mva, const EventInfo& eventInfo);
void rankJetSingletsMissingBJetMissingAllWJet(std::vector<JetQuadBase>& jetDoublets, const RecoLepton& selLepton,
				   int nJet, int nBJetLoose, int nBJetMedium, const TMVAInterface& mva, const EventInfo& eventInfo);
JetQuadBase
selectJet_Quad(const std::vector<const RecoJet*> selJetsAK4, const RecoLepton selLepton,
	       int nBJetMedium, const Particle::LorentzVector& metP4,
	       const std::vector<const GenJet*>& genBJets_ptrs, const std::vector<const GenJet*>& genWJets_ptrs,
	       const TMVAInterface& mva, const EventInfo& eventInfo, const RecoJetAK8* selJetAK8_Hbb = nullptr);

JetQuadBase
selectJet_TripletMissingBJet(const std::vector<const RecoJet*> selJetsAK4, const RecoLepton selLepton,
			     int nJet, int nBJetMedium, const std::vector<const GenJet*>& genBJets_ptrs, const std::vector<const GenJet*>& genWJets_ptrs,
			     const TMVAInterface& mva, const EventInfo& eventInfo);
JetQuadBase
selectJet_TripletMissingWJet(const std::vector<const RecoJet*> selJetsAK4, const RecoLepton selLepton,
			     int nJet, int nBJetLoose, int nBJetMedium,
			     const std::vector<const GenJet*>& genBJets_ptrs, const std::vector<const GenJet*>& genWJets_ptrs,
			     const TMVAInterface& mva, const EventInfo& eventInfo, const RecoJetAK8* selJetAK8_Hbb = nullptr);

JetQuadBase
selectJet_DoubletMissingBJetMissingWJet(const std::vector<const RecoJet*> selJetsAK4, const RecoLepton selLepton,
					int nJet, int nBJetLoose, int nBJetMedium, int nLep, const std::vector<const GenJet*>& genBJets_ptrs, const std::vector<const GenJet*>& genWJets_ptrs,
					const TMVAInterface& mva, const EventInfo& eventInfo);
JetQuadBase
selectJet_DoubletMissingAllWJet(const std::vector<const RecoJet*> selJetsAK4, const RecoLepton selLepton,
				int nJet, int nBJetMedium, const std::vector<const GenJet*>& genBJets_ptrs, const std::vector<const GenJet*>& genWJets_ptrs,
				const TMVAInterface& mva, const EventInfo& eventInfo);

JetQuadBase 
selectJet_SingletMissingBJetMissingAllWJet(const std::vector<const RecoJet*> cleanedJetsAK4_wrtLeptons, const RecoLepton selLepton,
					   int nJet, int nBJetLoose, int nBJetMedium,
					   const std::vector<const GenJet*>& genBJets_ptrs, const std::vector<const GenJet*>& genWJets_ptrs,
					   const TMVAInterface& mva, const EventInfo& eventInfo);

std::vector<JetQuadBase> 
makeJetQuads(const std::vector<const RecoJet*>& selJetsAK4, const std::vector<const GenJet*>& genBJets, const std::vector<const GenJet*>& genWJets, const RecoJetAK8* selJetAK8_Hbb = nullptr);
std::vector<JetQuadBase>
makeJetTripletsMissingBJet(const std::vector<const RecoJet*>& selJetsAK4, const std::vector<const GenJet*>& genBJets, const std::vector<const GenJet*>& genWJets);
std::vector<JetQuadBase>
makeJetTripletsMissingWJet(const std::vector<const RecoJet*>& selJetsAK4, const std::vector<const GenJet*>& genBJets, const std::vector<const GenJet*>& genWJets);
std::vector<JetQuadBase>
makeJetDoubletsMissingBJetMissingWJet(const std::vector<const RecoJet*>& selJetsAK4, const std::vector<const GenJet*>& genBJets, const std::vector<const GenJet*>& genWJets);
std::vector<JetQuadBase>
makeJetDoubletsMissingAllWJet(const std::vector<const RecoJet*>& selJetsAK4, const std::vector<const GenJet*>& genBJets, const std::vector<const GenJet*>& genWJets);
std::vector<JetQuadBase>
makeJetSingletsMissingBJetMissingAllWJet(const std::vector<const RecoJet*>& selJetsAK4, const std::vector<const GenJet*>& genBJets);
#endif // hhAnalysis_bbww_JetQuad_h
