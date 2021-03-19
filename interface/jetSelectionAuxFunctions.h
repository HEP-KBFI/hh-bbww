#ifndef hhAnalysis_bbww_jetSelectionAuxFunctions_h
#define hhAnalysis_bbww_jetSelectionAuxFunctions_h

#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h" // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/RecoJet.h" // RecoJet
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetAK8.h" // RecoJetAK8
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetBase.h" // RecoJetBase
#include "tthAnalysis/HiggsToTauTau/interface/EventInfo.h" // EventInfo
#include "tthAnalysis/HiggsToTauTau/interface/TMVAInterface.h" // TMVAInterface
#include "tthAnalysis/HiggsToTauTau/interface/ParticleCollectionCleaner.h" // RecoJetCollectionCleaner, RecoJetCollectionCleanerAK8
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetCollectionSelector.h" // RecoJetCollectionSelector
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetCollectionSelectorBtag.h" // RecoJetCollectionSelectorBtagLoose, RecoJetCollectionSelectorBtagMedium
#include "hhAnalysis/multilepton/interface/RecoJetCollectionSelectorAK8_hh_Wjj.h" // RecoJetSelectorAK8_hh_Wjj
#include "hhAnalysis/bbww/interface/RecoJetCollectionSelectorAK8_hh_bbWW_Hbb.h" // RecoJetSelectorAK8_hh_bbWW_Hbb

#include <vector> // std::vector<>

struct selJetsType_Hbb
{
  selJetsType_Hbb()
    : fatjet_(nullptr)
    , jet_or_subjet1_(nullptr)
    , jet_or_subjet2_(nullptr)
    , numBJets_loose_(0)
    , numBJets_medium_(0)
  {}
  ~selJetsType_Hbb() {}
  const RecoJetAK8* fatjet_;
  const RecoJetBase* jet_or_subjet1_;
  const RecoJetBase* jet_or_subjet2_;
  int numBJets_loose_;
  int numBJets_medium_;
};

std::vector<selJetsType_Hbb>
selectJets_Hbb(const std::vector<const RecoJetAK8*>& selJetsAK8_Hbb,
               const std::vector<const RecoJet*> selJetsAK4_Hbb,
               const RecoLepton* selLepton_lead = nullptr,
	       const RecoLepton* selLepton_sublead = nullptr,
               int maxJetPairs = 1,
               bool isDEBUG = false);

void
countBJets_Hbb(const selJetsType_Hbb& selJets_Hbb,
               const RecoJetCollectionSelectorAK8_hh_bbWW_Hbb& jetSelectorAK8_Hbb,
               const RecoJetCollectionSelectorBtagLoose& jetSelectorAK4_bTagLoose,
               const RecoJetCollectionSelectorBtagMedium& jetSelectorAK4_bTagMedium,
               int& numBJets_loose,
               int& numBJets_medium);

void
countBJets_jpa(const RecoJetAK8* selJetAK8_Hbb, const RecoJetBase* selJet1_Hbb, const RecoJetBase* selJet2_Hbb, 
               const RecoJetCollectionSelectorAK8_hh_bbWW_Hbb& jetSelectorAK8_Hbb,
               const RecoJetCollectionSelectorBtagLoose& jetSelectorAK4_bTagLoose,
               const RecoJetCollectionSelectorBtagMedium& jetSelectorAK4_bTagMedium,
               int& numBJets_jpa_loose,
               int& numBJets_jpa_medium);

struct selJetsType_Wjj
{
  selJetsType_Wjj()
    : fatjet_(nullptr)
    , jet_or_subjet1_(nullptr)
    , jet_or_subjet2_(nullptr)
  {}
  ~selJetsType_Wjj() {}
  const RecoJetAK8* fatjet_;
  const RecoJetBase* jet_or_subjet1_;
  const RecoJetBase* jet_or_subjet2_;
};

std::vector<selJetsType_Wjj>
selectJets_Wjj(const std::vector<const RecoJetAK8*>& jet_ptrs_ak8LS,
               const RecoJetCollectionCleanerAK8& jetCleanerAK8_dR12,
               const RecoJetCollectionCleanerAK8& jetCleanerAK8_dR16,
               const RecoJetCollectionSelectorAK8_hh_Wjj& jetSelectorAK8LS_Wjj,
               const std::vector<const RecoJet*>& cleanedJetsAK4_wrtLeptons,
               const RecoJetCollectionCleaner& jetCleanerAK4_dR08,
               const RecoJetCollectionCleaner& jetCleanerAK4_dR12,
               const RecoJetCollectionSelector& jetSelectorAK4,
               const selJetsType_Hbb& selJets_Hbb,
               const RecoLepton* selLepton,
               const std::vector<const RecoJet*>& selBJetsAK4_medium,
               const TMVAInterface& mva_Wjj,
               const EventInfo& eventInfo,
               const std::vector<const GenJet*>* genWJets = nullptr,
               int maxJetPairs = 1,
	       bool isDEBUG = false);

std::vector<selJetsType_Wjj>
selectJets_Wjj_resolved(
              //const std::vector<const RecoJet*>& cleanedJetsAK4_wrtLeptons,
              const std::vector<const RecoJet*>& cleanedJetsAK4_wrtHbb,
              const RecoLepton* selLepton,
              const RecoJetCollectionCleaner& jetCleanerAK4_dR08,
              const RecoJetCollectionCleaner& jetCleanerAK4_dR12,
              const RecoJetCollectionSelector& jetSelectorAK4,
              const std::vector<const RecoJet*>& selBJetsAK4_medium,
              const TMVAInterface& mva_Wjj,
              const EventInfo& eventInfo,
	            bool isDEBUG);

std::pair< const RecoJetBase*, const RecoJetBase* >
selectJets_Wjj_forrestOfcat(const std::vector<const RecoJet*>& cleanedJetsAK4_wrtHbb,
			    const Particle::LorentzVector metP4,
			    const RecoLepton* selLepton,
			    const RecoJetBase* selJet1_Hbb, const RecoJetBase* selJet2_Hbb);
std::vector<const RecoJet*>
jetSelectorAK4_wpt50(const std::vector<const RecoJet*>& jet);

double
mjj_closeToHiggs(const std::vector<const RecoJet*>& jet);
double
mjj_closeToHiggs(const std::vector<const RecoJetAK8*>& jet);
#endif // jetSelectionAuxFunctions_h
