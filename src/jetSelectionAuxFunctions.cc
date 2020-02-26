#include "hhAnalysis/bbww/interface/jetSelectionAuxFunctions.h"

#include "DataFormats/Math/interface/deltaR.h" // deltaR()

#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // pickFirstNobjects
#include "hhAnalysis/bbww/interface/JetPair.h" // JetPair_Hbb, makeJetPairs_Hbb, rankJetPairs_Hbb, JetPair_Wjj, makeJetPairs_Wjj, rankJetPairs_Wjj
#include "hhAnalysis/bbww/interface/genMatchingAuxFunctions.h" // isGenMatchedT

#include <string>   // std::string
#include <iostream> // std::cout, std::endl

void 
printJet(const std::string& label, const RecoJetBase* jet, const RecoLepton* selLepton_lead = nullptr, const RecoLepton* selLepton_sublead = nullptr)
{
  std::cout << label << ":";
  if ( jet ) 
  {
    std::cout << " pT = " << jet->pt() << ", eta = " << jet->eta() << ", phi = " << jet->phi();
    if ( selLepton_lead    ) std::cout << ", dR(selLepton_lead) = " << deltaR(jet->p4(), selLepton_lead->p4());
    if ( selLepton_sublead ) std::cout << ", dR(selLepton_sublead) = " << deltaR(jet->p4(), selLepton_lead->p4());
  }
  else
  {
    std::cout << " N/A";
  }
  std::cout << std::endl;
}

std::vector<selJetsType_Hbb>
selectJets_Hbb(const std::vector<const RecoJetAK8*>& selJetsAK8_Hbb, 
               const std::vector<const RecoJet*> selJetsAK4_Hbb,
               const RecoLepton* selLepton_lead,
	       const RecoLepton* selLepton_sublead,
               int maxJetPairs,
               bool isDEBUG)
{
//--- select jets from H->bb decay

  std::vector<selJetsType_Hbb> retVal;

  size_t numJetPairs_boosted = selJetsAK8_Hbb.size();
  if ( maxJetPairs >= 0 ) numJetPairs_boosted = std::min((int)numJetPairs_boosted, maxJetPairs);
  for ( size_t idx = 0; idx < numJetPairs_boosted; ++idx )
  {
    selJetsType_Hbb selJets_Hbb;
    selJets_Hbb.fatjet_ = selJetsAK8_Hbb[idx];
    assert(selJets_Hbb.fatjet_->subJet1() && selJets_Hbb.fatjet_->subJet2());
    if ( selJets_Hbb.fatjet_->subJet1()->BtagCSV() > selJets_Hbb.fatjet_->subJet2()->BtagCSV() )
    {
      selJets_Hbb.jet_or_subjet1_ = selJets_Hbb.fatjet_->subJet1();
      selJets_Hbb.jet_or_subjet2_ = selJets_Hbb.fatjet_->subJet2();
    }
    else
    {
      selJets_Hbb.jet_or_subjet1_ = selJets_Hbb.fatjet_->subJet2();
      selJets_Hbb.jet_or_subjet2_ = selJets_Hbb.fatjet_->subJet1();
    }
    if ( isDEBUG ) {
      std::cout << "found boosted H->bb decay:" << std::endl;
      printJet("AK8 jet", selJets_Hbb.fatjet_, selLepton_lead, selLepton_sublead);
      printJet(" subjet #1", selJets_Hbb.jet_or_subjet1_, selLepton_lead, selLepton_sublead);
      printJet(" subjet #2", selJets_Hbb.jet_or_subjet2_, selLepton_lead, selLepton_sublead);
    }
    retVal.push_back(selJets_Hbb);
  } 

  if ( (int)retVal.size() < maxJetPairs || maxJetPairs == -1 )
  {
    if ( selJetsAK4_Hbb.size() >= 2 )
    {
      std::vector<JetPair_Hbb> jetsPairsAK4_Hbb = makeJetPairs_Hbb(selJetsAK4_Hbb);
      rankJetPairs_Hbb(jetsPairsAK4_Hbb);

      size_t numJetPairs_resolved = jetsPairsAK4_Hbb.size();
      if ( maxJetPairs >= 0 ) numJetPairs_resolved = std::min((int)numJetPairs_resolved, std::max(0, maxJetPairs - (int)retVal.size()));
      for ( size_t idx = 0; idx < numJetPairs_resolved; ++idx )
      {
        selJetsType_Hbb selJets_Hbb;
        const JetPair_Hbb& jetPair = jetsPairsAK4_Hbb[idx];
        assert(jetPair.jet1_ && jetPair.jet2_);
        selJets_Hbb.jet_or_subjet1_ = jetPair.jet1_;
        selJets_Hbb.jet_or_subjet2_ = jetPair.jet2_;
        if ( isDEBUG ) {
          std::cout << "found resolved H->bb decay:" << std::endl;
          printJet("AK4 jet #1", selJets_Hbb.jet_or_subjet1_);
          printJet("AK4 jet #2", selJets_Hbb.jet_or_subjet2_);
        }
        retVal.push_back(selJets_Hbb);
      }
    }
    else
    {
      selJetsType_Hbb selJets_Hbb;
      if ( selJetsAK4_Hbb.size() >= 1 ) selJets_Hbb.jet_or_subjet1_ = selJetsAK4_Hbb[0];
      if ( selJetsAK4_Hbb.size() >= 2 ) selJets_Hbb.jet_or_subjet2_ = selJetsAK4_Hbb[1];
      retVal.push_back(selJets_Hbb);
    }
  }

  return retVal;
}

void
countBJetsJets_Hbb(const selJetsType_Hbb& selJets_Hbb,
                   const RecoJetCollectionSelectorAK8_hh_bbWW_Hbb& jetSelectorAK8_Hbb,
                   const RecoJetCollectionSelectorBtagLoose& jetSelectorAK4_bTagLoose,
                   const RecoJetCollectionSelectorBtagMedium& jetSelectorAK4_bTagMedium,
                   int& numBJets_loose,
                   int& numBJets_medium)
{
//--- count jets from H->bb decay that pass Loose and Medium b-tagging discriminators

  if ( selJets_Hbb.fatjet_ )
  {
    numBJets_loose = 0;
    double min_BtagCSV_loose = jetSelectorAK8_Hbb.getSelector().get_min_BtagCSV_loose();
    if ( selJets_Hbb.fatjet_->subJet1()->BtagCSV() >= min_BtagCSV_loose  ) ++numBJets_loose;
    if ( selJets_Hbb.fatjet_->subJet2()->BtagCSV() >= min_BtagCSV_loose  ) ++numBJets_loose;
    numBJets_medium = 0;
    double min_BtagCSV_medium = jetSelectorAK8_Hbb.getSelector().get_min_BtagCSV_medium();
    if ( selJets_Hbb.fatjet_->subJet1()->BtagCSV() >= min_BtagCSV_medium ) ++numBJets_medium;
    if ( selJets_Hbb.fatjet_->subJet2()->BtagCSV() >= min_BtagCSV_medium ) ++numBJets_medium;
  }
  else
  {
    std::vector<const RecoJet*> jets;
    if ( dynamic_cast<const RecoJet*>(selJets_Hbb.jet_or_subjet1_) ) jets.push_back(dynamic_cast<const RecoJet*>(selJets_Hbb.jet_or_subjet1_));
    if ( dynamic_cast<const RecoJet*>(selJets_Hbb.jet_or_subjet2_) ) jets.push_back(dynamic_cast<const RecoJet*>(selJets_Hbb.jet_or_subjet2_));
    numBJets_loose = jetSelectorAK4_bTagLoose(jets, isHigherPt).size();
    numBJets_medium = jetSelectorAK4_bTagMedium(jets, isHigherPt).size();
  }
}

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
               const std::vector<const GenJet*>* genWJets,
               int maxJetPairs,
	       bool isDEBUG)
{
//--- select jets from W->jj decay

  std::vector<selJetsType_Wjj> retVal;

  std::vector<const RecoJetAK8*> cleanedJetsAK8LS_wrtHbb;
  std::vector<const RecoJetAK8*> cleanedJetsAK8_wrtHbb;
  std::vector<const RecoJet*>    cleanedJetsAK4_wrtHbb;
  if ( selJets_Hbb.fatjet_ ) {
    const std::vector<const RecoJetAK8*> overlaps = { selJets_Hbb.fatjet_ };
    cleanedJetsAK8LS_wrtHbb = jetCleanerAK8_dR16(jet_ptrs_ak8LS, overlaps); // CV: do *not* clean W->jj "fat" jet collection with respect to leptons!
    cleanedJetsAK4_wrtHbb   = jetCleanerAK4_dR12(cleanedJetsAK4_wrtLeptons, overlaps);
  } else {
    std::vector<const RecoJetBase*> overlaps;
    if ( selJets_Hbb.jet_or_subjet1_ ) overlaps.push_back(selJets_Hbb.jet_or_subjet1_);
    if ( selJets_Hbb.jet_or_subjet2_ ) overlaps.push_back(selJets_Hbb.jet_or_subjet2_);
    cleanedJetsAK8LS_wrtHbb = jetCleanerAK8_dR12(jet_ptrs_ak8LS, overlaps);
    cleanedJetsAK4_wrtHbb   = jetCleanerAK4_dR08(cleanedJetsAK4_wrtLeptons, overlaps);
  }
  std::vector<const RecoJetAK8*> selJetsAK8LS_Wjj;
  if ( selLepton ) 
  { 
    jetSelectorAK8LS_Wjj.getSelector().set_lepton(selLepton);
    selJetsAK8LS_Wjj = jetSelectorAK8LS_Wjj(cleanedJetsAK8LS_wrtHbb, isHigherPt);
  } 
  else 
  { 
    if ( isDEBUG ) 
    {
      std::cerr << "Warning in <selectJets_Wjj>: Cannot select AK8LS jets, as there is no lepton in the event !!" << std::endl;
    }
    return retVal;
  }
  // CV: only consider the first ten jets, in order to avoid too large combinatorics in building W->jj pairs,
  //     which would require many time-consuming MEM computations
  const std::vector<const RecoJet*> selJetsFullAK4_Wjj = jetSelectorAK4(cleanedJetsAK4_wrtHbb, isHigherPt);
  const std::vector<const RecoJet*> selJetsAK4_Wjj = pickFirstNobjects(selJetsFullAK4_Wjj, 10);

  size_t numJetPairs_boosted = selJetsAK8LS_Wjj.size();
  if ( maxJetPairs >= 0 ) numJetPairs_boosted = std::min((int)numJetPairs_boosted, maxJetPairs);
  for ( size_t idx = 0; idx < numJetPairs_boosted; ++idx )
  {
    selJetsType_Wjj selJets_Wjj;
    selJets_Wjj.fatjet_ = selJetsAK8LS_Wjj[idx];
    assert(selJets_Wjj.fatjet_->subJet1() && selJets_Wjj.fatjet_->subJet2());
    selJets_Wjj.jet_or_subjet1_ = selJets_Wjj.fatjet_->subJet1();
    selJets_Wjj.jet_or_subjet2_ = selJets_Wjj.fatjet_->subJet2();
    if ( isDEBUG ) {
      std::cout << "found boosted AK8LS W->jj decay:" << std::endl;
      printJet("AK8LS jet", selJets_Wjj.fatjet_, selLepton);
      printJet(" subjet #1", selJets_Wjj.jet_or_subjet1_, selLepton);
      printJet(" subjet #2", selJets_Wjj.jet_or_subjet2_, selLepton);
    }
    retVal.push_back(selJets_Wjj);
  }

  if ( (int)retVal.size() < maxJetPairs || maxJetPairs == -1 )
  {
    if ( selJetsAK4_Wjj.size() >= 2 ) 
    { 
      std::vector<JetPair_Wjj> jetsPairsAK4_Wjj = makeJetPairs_Wjj(selJetsAK4_Wjj);
      assert(selLepton);
      rankJetPairs_Wjj(jetsPairsAK4_Wjj, selJetsAK4_Wjj, *selLepton, selBJetsAK4_medium.size(), mva_Wjj, eventInfo);
      assert(jetsPairsAK4_Wjj.size() >= 1);

      size_t numJetPairs_resolved = jetsPairsAK4_Wjj.size();
      if ( maxJetPairs >= 0 ) numJetPairs_resolved = std::min((int)numJetPairs_resolved, std::max(0, maxJetPairs - (int)retVal.size()));
      for ( size_t idx = 0; idx < numJetPairs_resolved; ++idx )
      {
        selJetsType_Wjj selJets_Wjj;
        const JetPair_Wjj& jetPair = jetsPairsAK4_Wjj[idx];
        assert(jetPair.jet1_ && jetPair.jet2_);
        selJets_Wjj.jet_or_subjet1_ = jetPair.jet1_;
        selJets_Wjj.jet_or_subjet2_ = jetPair.jet2_; 
        if ( isDEBUG ) 
        {
          std::cout << "found resolved AK4 W->jj decay:" << std::endl;
          printJet("AK4 jet #1", selJets_Wjj.jet_or_subjet1_);
          printJet("AK4 jet #2", selJets_Wjj.jet_or_subjet2_);
        }
        retVal.push_back(selJets_Wjj);
      }
    } 
    else 
    {
      selJetsType_Wjj selJets_Wjj;
      if ( selJetsAK4_Wjj.size() >= 1 ) selJets_Wjj.jet_or_subjet1_ = selJetsAK4_Wjj[0];
      if ( selJetsAK4_Wjj.size() >= 2 ) selJets_Wjj.jet_or_subjet2_ = selJetsAK4_Wjj[1];
      retVal.push_back(selJets_Wjj);
    }
  }

  return retVal;
}
