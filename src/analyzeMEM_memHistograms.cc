#include "hhAnalysis/bbww/interface/analyzeMEM_memHistograms.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow
#include "hhAnalysis/bbww/interface/genMatchingAuxFunctions.h"         // isGenMatchedT

memHistograms::memHistograms(const std::string& label, int numUnmatchedLeptons, int numUnmatchedBJets, int numUnmatchedWJets)
  : label_(label)
  , numUnmatchedLeptons_(numUnmatchedLeptons)
  , numUnmatchedBJets_(numUnmatchedBJets)
  , numUnmatchedWJets_(numUnmatchedWJets)
  , histogram_LR_(nullptr)
  , histogram_weightS_(nullptr)
  , histogram_weightB_(nullptr)
  , histogram_isValid_(nullptr) 
{}

memHistograms::~memHistograms() 
{}
  
void 
memHistograms::bookHistograms(fwlite::TFileService& fs)
{
  std::string histogramName_prefix = "mem";
  if ( label_ != "" ) histogramName_prefix.append("_").append(label_);
  std::string histogramName_suffix;
  if ( numUnmatchedLeptons_ == 0 && numUnmatchedBJets_ == 0 && numUnmatchedWJets_ == 0 ) 
  {
    histogramName_suffix = "fullyMatched";
  }
  else if ( numUnmatchedLeptons_ >= 1 && numUnmatchedBJets_ == 0 && numUnmatchedWJets_ == 0 ) 
  {
    histogramName_suffix = "unmatchedLepton";
  }
  else if ( numUnmatchedLeptons_ == 0 && numUnmatchedBJets_ >= 1 && numUnmatchedWJets_ == 0 ) 
  {
    histogramName_suffix = "unmatchedBJet";
  }
  else if ( numUnmatchedLeptons_ == 0 && numUnmatchedBJets_ == 0 && numUnmatchedWJets_ >= 1 ) 
  {
    histogramName_suffix = "unmatchedWJet";
  }
  else assert(0);
  std::string histogramName_LR = Form("%s_LR_%s", histogramName_prefix.data(), histogramName_suffix.data());
  histogram_LR_ = fs.make<TH1D>(histogramName_LR.data(), histogramName_LR.data(), 500, -40., +10.);
  std::string histogramName_weightS = Form("%s_weightS_%s", histogramName_prefix.data(), histogramName_suffix.data());
  histogram_weightS_ = fs.make<TH1D>(histogramName_weightS.data(), histogramName_weightS.data(), 500, -40., +10.);
  std::string histogramName_weightB = Form("%s_weightB_%s", histogramName_prefix.data(), histogramName_suffix.data());
  histogram_weightB_ = fs.make<TH1D>(histogramName_weightB.data(), histogramName_weightB.data(), 500, -40., +10.);
  std::string histogramName_isValid = Form("%s_isValid_%s", histogramName_prefix.data(), histogramName_suffix.data());
  histogram_isValid_ = fs.make<TH1D>(histogramName_isValid.data(), histogramName_isValid.data(), 2, -0.5, +1.5);
}

void 
fillHistograms_mem(const MEMOutput_hh_bb1l& memOutput, 
		   const std::vector<const GenLepton*>& genLeptons, 
		   const std::vector<const GenJet*>& genBJets, 
		   const std::vector<const GenJet*>& genWJets, 
		   memHistograms& histograms_fullyMatched, 
		   memHistograms& histograms_unmatchedLepton, 
		   memHistograms& histograms_unmatchedBJet, 
		   memHistograms& histograms_unmatchedWJet, double evtWeight)
{
  int numUnmatchedLeptons = 0;
  if ( !isGenMatchedT<GenLepton>(memOutput.lepton_eta_, memOutput.lepton_phi_, genLeptons) ) 
  {
    ++numUnmatchedLeptons;
  }
  int numUnmatchedBJets = 0;
  if ( memOutput.bjet1_isReconstructed_ && !isGenMatchedT<GenJet>(memOutput.bjet1_eta_, memOutput.bjet1_phi_, genBJets) )
  { 
    ++numUnmatchedBJets;
  }
  if ( memOutput.bjet2_isReconstructed_ && !isGenMatchedT<GenJet>(memOutput.bjet2_eta_, memOutput.bjet2_phi_, genBJets) )
  { 
    ++numUnmatchedBJets;
  }
  int numUnmatchedWJets = 0;
  if ( memOutput.wjet1_isReconstructed_ && !isGenMatchedT<GenJet>(memOutput.wjet1_eta_, memOutput.wjet1_phi_, genWJets) )
  { 
    ++numUnmatchedWJets;
  }
  if ( memOutput.wjet2_isReconstructed_ && !isGenMatchedT<GenJet>(memOutput.wjet2_eta_, memOutput.wjet2_phi_, genWJets) )
  { 
    ++numUnmatchedWJets;
  }
  if      ( numUnmatchedLeptons == 0 && numUnmatchedBJets == 0 && numUnmatchedWJets == 0 ) 
  {
    histograms_fullyMatched.fillHistograms(memOutput, evtWeight);
  }
  else if ( numUnmatchedLeptons >= 1 && numUnmatchedBJets == 0 && numUnmatchedWJets == 0 ) 
  {
    histograms_unmatchedLepton.fillHistograms(memOutput, evtWeight);
  }
  else if ( numUnmatchedLeptons == 0 && numUnmatchedBJets >= 1 && numUnmatchedWJets == 0 ) 
  {
    histograms_unmatchedBJet.fillHistograms(memOutput, evtWeight);
  }
  else if ( numUnmatchedLeptons == 0 && numUnmatchedBJets == 0 && numUnmatchedWJets >= 1 ) 
  {
    histograms_unmatchedWJet.fillHistograms(memOutput, evtWeight);
  }
}

void 
fillHistograms_mem(const MEMOutput_hh_bb2l& memOutput, 
		   const std::vector<const GenLepton*>& genLeptons, 
		   const std::vector<const GenJet*>& genBJets, 
		   memHistograms& histograms_fullyMatched, 
		   memHistograms& histograms_unmatchedLepton, 
		   memHistograms& histograms_unmatchedBJet, double evtWeight)
{
  int numUnmatchedLeptons = 0;
  if ( !(isGenMatchedT<GenLepton>(memOutput.leadLepton_eta_,    memOutput.leadLepton_phi_,    genLeptons) &&  
         isGenMatchedT<GenLepton>(memOutput.subleadLepton_eta_, memOutput.subleadLepton_phi_, genLeptons)) )
  {
    ++numUnmatchedLeptons;
  }
  int numUnmatchedBJets = 0;
  if ( memOutput.bjet1_isReconstructed_ && !isGenMatchedT<GenJet>(memOutput.bjet1_eta_, memOutput.bjet1_phi_, genBJets) )
  { 
    ++numUnmatchedBJets;
  }
  if ( memOutput.bjet2_isReconstructed_ && !isGenMatchedT<GenJet>(memOutput.bjet2_eta_, memOutput.bjet2_phi_, genBJets) )
  { 
    ++numUnmatchedBJets;
  }
  if      ( numUnmatchedLeptons == 0 && numUnmatchedBJets == 0 ) 
  {
    histograms_fullyMatched.fillHistograms(memOutput, evtWeight);
  }
  else if ( numUnmatchedLeptons >= 1 && numUnmatchedBJets == 0 ) 
  {
    histograms_unmatchedLepton.fillHistograms(memOutput, evtWeight);
  }
  else if ( numUnmatchedLeptons == 0 && numUnmatchedBJets >= 1 ) 
  {
    histograms_unmatchedBJet.fillHistograms(memOutput, evtWeight);
  }
}
