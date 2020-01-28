#ifndef hhAnalysis_bbww_analyzeMEM_memHistograms_h
#define hhAnalysis_bbww_analyzeMEM_memHistograms_h

#include "PhysicsTools/FWLite/interface/TFileService.h"    // fwlite::TFileService

#include "tthAnalysis/HiggsToTauTau/interface/GenLepton.h" // GenLepton
#include "tthAnalysis/HiggsToTauTau/interface/GenJet.h"    // GenJet
#include "hhAnalysis/bbww/interface/MEMOutput_hh_bb1l.h"   // MEMOutput_hh_bb1l
#include "hhAnalysis/bbww/interface/MEMOutput_hh_bb2l.h"   // MEMOutput_hh_bb2l

#include <TH1.h>   // TH1
#include <TMath.h> // TMath:Log10, TMath::Max

#include <string> // std::string

struct memHistograms
{ 
  memHistograms(const std::string& label, int numUnmatchedLeptons, int numUnmatchedBJets, int numUnmatchedWJets);
  ~memHistograms();
  void bookHistograms(fwlite::TFileService& fs);
  template<typename T>
  void fillHistograms(const T& memOutput, double evtWeight)
  {
    if ( memOutput.isValid() )
    { 
      fillWithOverFlow(histogram_LR_, TMath::Log10(TMath::Max(1.e-37, 1. - memOutput.LR())), evtWeight);
      fillWithOverFlow(histogram_weightS_, TMath::Log10(TMath::Max((Float_t)1.e-37, memOutput.weight_signal())), evtWeight);
      fillWithOverFlow(histogram_weightB_, TMath::Log10(TMath::Max((Float_t)1.e-37, memOutput.weight_background())), evtWeight);
    }
    fillWithOverFlow(histogram_isValid_, memOutput.isValid(), evtWeight);
  }
  std::string label_;
  int numUnmatchedLeptons_;
  int numUnmatchedBJets_;
  int numUnmatchedWJets_;
  TH1* histogram_LR_;
  TH1* histogram_weightS_;
  TH1* histogram_weightB_;
  TH1* histogram_isValid_; 
};

void 
fillHistograms_mem(const MEMOutput_hh_bb1l& memOutput, 
		   const std::vector<const GenLepton*>& genLeptons, 
		   const std::vector<const GenJet*>& genBJets, 
		   const std::vector<const GenJet*>& genWJets, 
		   memHistograms& histograms_fullyMatched, 
		   memHistograms& histograms_unmatchedLepton, 
		   memHistograms& histograms_unmatchedBJet, 
		   memHistograms& histograms_unmatchedWJet, double evtWeight);

void 
fillHistograms_mem(const MEMOutput_hh_bb2l& memOutput, 
		   const std::vector<const GenLepton*>& genLeptons, 
		   const std::vector<const GenJet*>& genBJets, 
		   memHistograms& histograms_fullyMatched, 
		   memHistograms& histograms_unmatchedLepton, 
		   memHistograms& histograms_unmatchedBJet, double evtWeight);

#endif // analyzeMEM_memHistograms_h
