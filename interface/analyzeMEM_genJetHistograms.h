#ifndef hhAnalysis_bbww_analyzeMEM_genJetHistograms_h
#define hhAnalysis_bbww_analyzeMEM_genJetHistograms_h

#include "PhysicsTools/FWLite/interface/TFileService.h"                   // fwlite::TFileService

#include "tthAnalysis/HiggsToTauTau/interface/GenJet.h"                   // GenJet
#include "tthAnalysis/HiggsToTauTau/interface/GenJetCollectionSelector.h" // GenJetCollectionSelector

#include <TH1.h> // TH1

#include <string> // std::string

struct genJetHistograms
{
  genJetHistograms(const std::string& label);
  ~genJetHistograms();
  void bookHistograms(fwlite::TFileService& fs);
  void fillHistograms(const GenJet* genJet_lead, const GenJet* genJet_sublead, double min_pt, double max_absEta, double evtWeight);
  std::string label_;
  TH1* histogram_genJet1_pt_;
  TH1* histogram_genJet1_absEta_;
  TH1* histogram_genJet2_pt_;
  TH1* histogram_genJet2_absEta_;
};

void 
fillHistograms_genJets(const std::vector<const GenJet*>& genJets, const GenJetCollectionSelector& genJetSelector,
                       genJetHistograms& histograms, double evtWeight);

#endif // analyzeMEM_genJetHistograms_h
