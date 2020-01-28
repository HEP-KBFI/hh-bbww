#ifndef hhAnalysis_bbww_analyzeMEM_jetHistograms_h
#define hhAnalysis_bbww_analyzeMEM_jetHistograms_h

#include "PhysicsTools/FWLite/interface/TFileService.h"                // fwlite::TFileService

#include "tthAnalysis/HiggsToTauTau/interface/RecoJetBase.h"           // RecoJetBase
#include "tthAnalysis/HiggsToTauTau/interface/GenJet.h"                // GenJet
#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow
#include "hhAnalysis/bbww/interface/genMatchingAuxFunctions.h"         // isGenMatchedT

#include <TH1.h> // TH1

#include <string> // std::string

struct jetHistograms
{
  jetHistograms(const std::string& label);
  ~jetHistograms();
  void bookHistograms(fwlite::TFileService& fs);
  void fillHistograms(const RecoJetBase* jet, double evtWeight);
  std::string label_;
  TH1* histogram_pt_;
  TH1* histogram_absEta_;
  TH1* histogram_btagCSV_;
};

template<typename T>
void 
fillHistograms_jets(const std::vector<const T*>& jets, 
		    const std::vector<const GenJet*>& genJets, 
		    jetHistograms& histograms_jet1, TH1* histogram_idx1, 
		    jetHistograms& histograms_jet2, TH1* histogram_idx2, TH1* histogram_numIndices, TH1* histogram_mjj, double evtWeight)
{
  std::vector<int> indices;
  size_t numJets = jets.size();
  for ( size_t idxJet = 0; idxJet < numJets; ++idxJet )
  {
    const T* jet = jets[idxJet];
    bool isMatched = isGenMatchedT<GenJet>(jet->eta(), jet->phi(), genJets);
    if ( isMatched ) indices.push_back(idxJet);
  }
  const T* jet1 = nullptr;
  if ( indices.size() >= 1 ) 
  {
    size_t idx1 = indices[0];
    jet1 = jets[idx1];
    histograms_jet1.fillHistograms(jet1, evtWeight);
    fillWithOverFlow(histogram_idx1, idx1, evtWeight);
  }
  const T* jet2 = nullptr;
  if ( indices.size() >= 2 ) 
  {
    size_t idx2 = indices[1];
    jet2 = jets[idx2];
    histograms_jet2.fillHistograms(jet2, evtWeight);
    fillWithOverFlow(histogram_idx2, idx2, evtWeight);
  }
  fillWithOverFlow(histogram_numIndices, indices.size(), evtWeight);
  if ( jet1 && jet2 ) 
  {
    fillWithOverFlow(histogram_mjj, (jet1->p4() + jet2->p4()).mass(), evtWeight); 
  }
}

#endif // analyzeMEM_jetHistograms_h
