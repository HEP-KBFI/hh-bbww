#include "FWCore/ParameterSet/interface/ParameterSet.h" // edm::ParameterSet
#include "FWCore/Utilities/interface/Exception.h" // cms::Exception
#include "PhysicsTools/FWLite/interface/TFileService.h" // fwlite::TFileService
#include "DataFormats/FWLite/interface/InputSource.h" // fwlite::InputSource
#include "DataFormats/FWLite/interface/OutputFiles.h" // fwlite::OutputFiles
#include "DataFormats/Math/interface/LorentzVector.h" // math::PtEtaPhiMLorentzVector, math::XYZTLorentzVectorD
#include "DataFormats/Math/interface/deltaR.h" // deltaR
#include "DataFormats/Math/interface/deltaPhi.h" // deltaPhi

#if __has_include (<FWCore/ParameterSetReader/interface/ParameterSetReader.h>)
#  include <FWCore/ParameterSetReader/interface/ParameterSetReader.h> // edm::readPSetsFrom()
#else
#  include <FWCore/PythonParameterSet/interface/MakeParameterSets.h> // edm::readPSetsFrom()
#endif

#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h" // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/RecoJet.h" // RecoJet
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEt.h" // RecoMEt
#include "tthAnalysis/HiggsToTauTau/interface/GenLepton.h" // GenLepton
#include "tthAnalysis/HiggsToTauTau/interface/GenJet.h" // GenJet
#include "tthAnalysis/HiggsToTauTau/interface/GenHadTau.h" // GenHadTau
#include "tthAnalysis/HiggsToTauTau/interface/ObjectMultiplicity.h" // ObjectMultiplicity
#include "tthAnalysis/HiggsToTauTau/interface/mvaAuxFunctions.h" // check_mvaInputs, get_mvaInputVariables
#include "tthAnalysis/HiggsToTauTau/interface/mvaInputVariables.h" // auxiliary functions for computing input variables of the MVA used for signal extraction
#include "tthAnalysis/HiggsToTauTau/interface/LeptonFakeRateInterface.h" // LeptonFakeRateInterface
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronReader.h" // RecoElectronReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonReader.h" // RecoMuonReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTauReader.h" // RecoHadTauReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetReader.h" // RecoJetReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetReaderAK8.h" // RecoJetReaderAK8
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEtReader.h" // RecoMEtReader
#include "tthAnalysis/HiggsToTauTau/interface/MEtFilterReader.h" // MEtFilterReader
#include "tthAnalysis/HiggsToTauTau/interface/GenLeptonReader.h" // GenLeptonReader
#include "tthAnalysis/HiggsToTauTau/interface/GenParticleReader.h" // GenParticleReader
#include "tthAnalysis/HiggsToTauTau/interface/GenHadTauReader.h" // GenHadTauReader
#include "tthAnalysis/HiggsToTauTau/interface/GenPhotonReader.h" // GenPhotonReader
#include "tthAnalysis/HiggsToTauTau/interface/GenJetReader.h" // GenJetReader
#include "tthAnalysis/HiggsToTauTau/interface/LHEInfoReader.h" // LHEInfoReader
#include "tthAnalysis/HiggsToTauTau/interface/PSWeightReader.h" // PSWeightReader
#include "tthAnalysis/HiggsToTauTau/interface/ObjectMultiplicityReader.h" // ObjectMultiplicityReader
#include "tthAnalysis/HiggsToTauTau/interface/convert_to_ptrs.h" // convert_to_ptrs
#include "tthAnalysis/HiggsToTauTau/interface/EventInfo.h" // EventInfo
#include "tthAnalysis/HiggsToTauTau/interface/EventInfoReader.h" // EventInfoReader
#include "tthAnalysis/HiggsToTauTau/interface/ParticleCollectionCleaner.h" // RecoElectronCollectionCleaner, RecoMuonCollectionCleaner, RecoJetCollectionCleaner
#include "tthAnalysis/HiggsToTauTau/interface/ParticleCollectionGenMatcher.h" // RecoElectronCollectionGenMatcher, RecoMuonCollectionGenMatcher, RecoJetCollectionGenMatcher
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronCollectionSelectorLoose.h" // RecoElectronCollectionSelectorLoose
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronCollectionSelectorFakeable.h" // RecoElectronCollectionSelectorFakeable
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronCollectionSelectorTight.h" // RecoElectronCollectionSelectorTight
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonCollectionSelectorLoose.h" // RecoMuonCollectionSelectorLoose
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonCollectionSelectorFakeable.h" // RecoMuonCollectionSelectorFakeable
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonCollectionSelectorTight.h" // RecoMuonCollectionSelectorTight
#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTauCollectionSelectorTight.h" // RecoHadTauCollectionSelectorTight
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetCollectionSelector.h" // RecoJetCollectionSelector
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetCollectionSelectorBtag.h" // RecoJetCollectionSelectorBtagLoose, RecoJetCollectionSelectorBtagMedium
#include "tthAnalysis/HiggsToTauTau/interface/RunLumiEventSelector.h" // RunLumiEventSelector
#include "tthAnalysis/HiggsToTauTau/interface/MEtFilterSelector.h" // MEtFilterSelector
#include "tthAnalysis/HiggsToTauTau/interface/ElectronHistManager.h" // ElectronHistManager
#include "tthAnalysis/HiggsToTauTau/interface/MuonHistManager.h" // MuonHistManager
#include "tthAnalysis/HiggsToTauTau/interface/JetHistManager.h" // JetHistManager
#include "tthAnalysis/HiggsToTauTau/interface/JetHistManagerAK8.h" // JetHistManagerAK8
#include "tthAnalysis/HiggsToTauTau/interface/MEtHistManager.h" // MEtHistManager
#include "tthAnalysis/HiggsToTauTau/interface/MEtFilterHistManager.h" // MEtFilterHistManager
#include "tthAnalysis/HiggsToTauTau/interface/EvtYieldHistManager.h" // EvtYieldHistManager
#include "tthAnalysis/HiggsToTauTau/interface/CutFlowTableHistManager.h" // CutFlowTableHistManager
#include "tthAnalysis/HiggsToTauTau/interface/WeightHistManager.h" // WeightHistManager
#include "tthAnalysis/HiggsToTauTau/interface/GenEvtHistManager.h" // GenEvtHistManager
#include "tthAnalysis/HiggsToTauTau/interface/LHEInfoHistManager.h" // LHEInfoHistManager
#include "tthAnalysis/HiggsToTauTau/interface/leptonTypes.h" // getLeptonType, kElectron, kMuon
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // getBTagWeight_option, getHadTau_genPdgId, isHigherPt, isMatched
#include "tthAnalysis/HiggsToTauTau/interface/leptonGenMatchingAuxFunctions.h" // getLeptonGenMatch_definitions_1lepton, getLeptonGenMatch_string, getLeptonGenMatch_int
#include "tthAnalysis/HiggsToTauTau/interface/GenMatchInterface.h" // GenMatchInterface
#include "tthAnalysis/HiggsToTauTau/interface/fakeBackgroundAuxFunctions.h"
#include "tthAnalysis/HiggsToTauTau/interface/generalAuxFunctions.h" // format_vstring
#include "tthAnalysis/HiggsToTauTau/interface/mvaInputVariables.h" // comp_lep1_conePt, comp_lep2_conePt
#include "tthAnalysis/HiggsToTauTau/interface/hltPath.h" // hltPath, create_hltPaths, hltPaths_isTriggered, hltPaths_delete
#include "tthAnalysis/HiggsToTauTau/interface/hltPathReader.h" // hltPathReader
#include "tthAnalysis/HiggsToTauTau/interface/Data_to_MC_CorrectionInterface_2016.h"
#include "tthAnalysis/HiggsToTauTau/interface/Data_to_MC_CorrectionInterface_2017.h"
#include "tthAnalysis/HiggsToTauTau/interface/Data_to_MC_CorrectionInterface_2018.h"
#include "tthAnalysis/HiggsToTauTau/interface/lutAuxFunctions.h" // loadTH2, get_sf_from_TH2
#include "tthAnalysis/HiggsToTauTau/interface/L1PreFiringWeightReader.h" // L1PreFiringWeightReader
#include "tthAnalysis/HiggsToTauTau/interface/cutFlowTable.h" // cutFlowTableType
#include "tthAnalysis/HiggsToTauTau/interface/NtupleFillerBDT.h" // NtupleFillerBDT
#include "tthAnalysis/HiggsToTauTau/interface/TTreeWrapper.h" // TTreeWrapper
#include "tthAnalysis/HiggsToTauTau/interface/hltFilter.h" // hltFilter()
#include "tthAnalysis/HiggsToTauTau/interface/EvtWeightManager.h" // EvtWeightManager
#include "tthAnalysis/HiggsToTauTau/interface/mT2_2particle.h" // mT2_2particle::comp_mT
#include "tthAnalysis/HiggsToTauTau/interface/mT2_3particle.h" // mT2_3particle::comp_mT
#include "tthAnalysis/HiggsToTauTau/interface/XGBInterface.h" // XGBInterface
#include "tthAnalysis/HiggsToTauTau/interface/TensorFlowInterface.h"
#include "tthAnalysis/HiggsToTauTau/interface/MVAInputVarHistManager.h" // MVAInputVarHistManager
#include "tthAnalysis/HiggsToTauTau/interface/HHWeightInterface.h" // HHWeightInterface
#include "tthAnalysis/HiggsToTauTau/interface/BtagSFRatioFacility.h" // BtagSFRatioFacility

#include "hhAnalysis/multilepton/interface/RecoJetCollectionSelectorAK8_hh_Wjj.h" // RecoJetSelectorAK8_hh_Wjj
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetCollectionSelectorAK8.h" // RecoJetSelectorAK8_hh_Wjj
#include "hhAnalysis/multilepton/interface/EvtWeightRecorderHH.h" // EvtWeightRecorderHH

#include "hhAnalysis/bbww/interface/EvtHistManager_hh_bb1l.h" // EvtHistManager_hh_bb1l
#include "hhAnalysis/bbww/interface/RecoJetCollectionSelectorAK8_hh_bbWW_Hbb.h" // RecoJetSelectorAK8_hh_bbWW_Hbb
#include "hhAnalysis/bbww/interface/MEMOutput_hh_bb1l.h" // MEMOutput_hh_bb1l
#include "hhAnalysis/bbww/interface/MEMOutputReader_hh_bb1l.h" // MEMOutputReader_hh_bb1l
#include "hhAnalysis/bbww/interface/JetPair.h" // initialize_mva_Wjj
#include "hhAnalysis/bbww/interface/jetSelectionAuxFunctions.h" // selectJets_Hbb, countBJetsJets_Hbb, selectJets_Wjj
#include "hhAnalysis/bbww/interface/SyncNtupleManager_bbww.h" // SyncNtupleManager_bbww
#include "hhAnalysis/bbww/interface/comp_metP4_B2G_18_008.h" // comp_metP4_B2G_18_008
#include "hhAnalysis/bbww/interface/BM_list.h" // BMS

#include <TBenchmark.h> // TBenchmark
#include <TString.h> // TString, Form
#include <TError.h> // gErrorAbortLevel, kError
#include <TRandom3.h> // TRandom3
#include <TROOT.h> // TROOT

#include <boost/algorithm/string/predicate.hpp> // boost::starts_with()
#include <boost/math/special_functions/sign.hpp> // boost::math::sign()
#include <boost/algorithm/string/replace.hpp> // boost::replace_all_copy()

#include <iostream> // std::cerr, std::fixed
#include <iomanip> // std::setprecision(), std::setw()
#include <string> // std::string
#include <vector> // std::vector<>
#include <cstdlib> // EXIT_SUCCESS, EXIT_FAILURE
#include <fstream> // std::ofstream
#include <assert.h> // assert

typedef math::PtEtaPhiMLorentzVector LV;
typedef std::vector<std::string> vstring;
typedef std::vector<double> vdouble;

enum { kFR_disabled, kFR_enabled };

const int hadTauSelection_veto_antiElectron = -1; // not applied
const int hadTauSelection_veto_antiMuon = -1; // not applied

const double higgsBosonMass = 125.;

enum { kHbb_undefined, kHbb_resolved, kHbb_boosted };
enum { kWjj_undefined, kWjj_resolved, kWjj_boosted_lowPurity, kWjj_boosted_highPurity };
enum { kVBF_undefined, kVBF_nottagged, kVBF_tagged };

struct categoryEntryType
{
  categoryEntryType(int numElectrons, int numMuons, int numBJets_medium, int numBJets_loose, int type_Hbb, int type_Wjj, int type_vbf)
    : numElectrons_(numElectrons)
    , numMuons_(numMuons)
    , numBJets_medium_(numBJets_medium)
    , numBJets_loose_(numBJets_loose)
    , type_Hbb_(type_Hbb)
    , type_Wjj_(type_Wjj)
    , type_vbf_(type_vbf)
  {
    name_ = "hh_";
    if      ( numBJets_medium_ >= 2                         ) name_ += "2bM";
    else if ( numBJets_medium_ >= 1 && numBJets_loose_ >= 2 ) name_ += "1bM1bL";
    else if ( numBJets_medium_ >= 1                         ) name_ += "1bM";
    else name_ += "bb";
    if      ( numElectrons_ >= 1 ) name_ += "1e";
    else if ( numMuons_     >= 1 ) name_ += "1mu";
    else name_ += "1l";
    if      ( type_Hbb_ == kHbb_resolved           ) name_ += "_resolvedHbb";
    else if ( type_Hbb_ == kHbb_boosted            ) name_ += "_boostedHbb";
    if      ( type_Wjj_ == kWjj_resolved           ) name_ += "_resolvedWjj";
    else if ( type_Wjj_ == kWjj_boosted_lowPurity  ) name_ += "_boostedWjj_lowPurity";
    else if ( type_Wjj_ == kWjj_boosted_highPurity ) name_ += "_boostedWjj_highPurity";
    if      ( type_vbf_ == kVBF_tagged             ) name_ += "_vbf";
    else if ( type_vbf_ == kVBF_nottagged          ) name_ += "_nonvbf";
  }
  ~categoryEntryType() {}
  std::string name_;
  int numElectrons_;
  int numMuons_;
  int numBJets_medium_;
  int numBJets_loose_;
  int type_Hbb_; // 0 = either resolved or boosted, 1 = resolved, 2 = boosted
  int type_Wjj_; // 0 = either resolved or boosted (any purity); 1 = resolved; 2 = boosted, low purity; 3 = boosted, high purity
  int type_vbf_; // 0 = either tagged or not tagged, 1 = not tagged; 2 = tagged
};

/*void addCategory_conditionally(std::vector<categoryEntryType>& categories_evt, const categoryEntryType& category, const std::vector<std::string>& evtCategories)
{
  if ( contains(evtCategories, category.name_) ) {
    categories_evt.push_back(category);
  }
}*/



void dumpGenParticles(const std::string& label, const std::vector<GenParticle>& particles)
{
  for ( size_t idxParticle = 0; idxParticle < particles.size(); ++idxParticle ) {
    std::cout << label << " #" << idxParticle << ":" << " ";
    std::cout << particles[idxParticle];
    std::cout << std::endl;
  }
}

void printHbb(const std::vector<const RecoJetAK8*>& jets_ak8, const RecoJetCollectionSelectorAK8_hh_bbWW_Hbb& jetSelectorAK8_Hbb,
	      const std::vector<GenParticle>& genBJets)
{
  std::cout << "<printHbb>:" << std::endl;
  std::cout << "#genBJets = " << genBJets.size() << std::endl;
  for ( size_t idxBJet = 0; idxBJet < genBJets.size(); ++idxBJet ) {
    const GenParticle& genBJet = genBJets[idxBJet];
    std::cout << " genBJet #" << idxBJet << ": pT = " << genBJet.pt() << ", eta = " << genBJet.eta() << ", phi = " << genBJet.phi() << std::endl;
  }
  if ( genBJets.size() == 2 ) {
    bool isMatched = false;
    Particle::LorentzVector genHbbP4 = genBJets[0].p4() + genBJets[1].p4();
    std::cout << "genHbb: pT = " << genHbbP4.pt() << ", eta = " << genHbbP4.eta() << ", phi = " << genHbbP4.phi() << std::endl;
    for ( std::vector<const RecoJetAK8*>::const_iterator jet_ak8 = jets_ak8.begin();
	  jet_ak8 != jets_ak8.end(); ++jet_ak8 ) {
      double dR = deltaR(genHbbP4, (*jet_ak8)->p4());
      if ( dR < 0.8 ) {
	std::cout << "matches reconstructed AK8 jet: pT = " << (*jet_ak8)->pt() << ", eta = " << (*jet_ak8)->eta() << ", phi = " << (*jet_ak8)->phi() << ", which ";
	if ( jetSelectorAK8_Hbb.getSelector()(**jet_ak8) ) {
	  std::cout << "PASSES";
	  isMatched = true;
	} else {
	  std::cout << "FAILS";
	}
	std::cout << " the H->bb jet selection." << std::endl;
      }
    }
    if ( genHbbP4.pt() > 100. && !isMatched ) std::cout << "--> DEBUG (Hbb) !!" << std::endl;
  }
}

void printWjj(const std::vector<const RecoJetAK8*>& jets_ak8, const RecoJetCollectionSelectorAK8_hh_Wjj& jetSelectorAK8_Wjj,
	      const std::vector<GenParticle>& genWBosons, const std::vector<GenParticle>& genWJets)
{
  std::cout << "<printWjj>:" << std::endl;
  std::cout << "#genWBosons = " << genWBosons.size() << std::endl;
  for ( size_t idxWBoson = 0; idxWBoson < genWBosons.size(); ++idxWBoson ) {
    const GenParticle& genWBoson = genWBosons[idxWBoson];
    std::cout << " genWBoson #" << idxWBoson << ": pT = " << genWBoson.pt() << ", eta = " << genWBoson.eta() << ", phi = " << genWBoson.phi() << std::endl;
  }
  std::cout << "#genWJets = " << genWJets.size() << std::endl;
  for ( size_t idxWJet = 0; idxWJet < genWJets.size(); ++idxWJet ) {
    const GenParticle& genWJet = genWJets[idxWJet];
    std::cout << " genWJet #" << idxWJet << ": pT = " << genWJet.pt() << ", eta = " << genWJet.eta() << ", phi = " << genWJet.phi() << std::endl;
  }
  if ( genWBosons.size() == 1 ) {
    bool isMatched = false;
    Particle::LorentzVector genWjjP4 = genWBosons[0].p4();
    std::cout << "genWjj: pT = " << genWjjP4.pt() << ", eta = " << genWjjP4.eta() << ", phi = " << genWjjP4.phi() << std::endl;
    for ( std::vector<const RecoJetAK8*>::const_iterator jet_ak8 = jets_ak8.begin();
	  jet_ak8 != jets_ak8.end(); ++jet_ak8 ) {
      double dR = deltaR(genWjjP4, (*jet_ak8)->p4());
      if ( dR < 0.8 ) {
	std::cout << "matches reconstructed AK8 jet: pT = " << (*jet_ak8)->pt() << ", eta = " << (*jet_ak8)->eta() << ", phi = " << (*jet_ak8)->phi() << ","
		  << " msoftdrop = " << (*jet_ak8)->msoftdrop() << ", tau21 = " << (*jet_ak8)->tau2()/(*jet_ak8)->tau1() << ", which ";
	if ( jetSelectorAK8_Wjj.getSelector()(**jet_ak8) ) {
	  std::cout << "PASSES";
	  isMatched = true;
	} else {
	  std::cout << "FAILS";
	}
	std::cout << " the W->jj jet selection." << std::endl;
	std::cout << "generator-level subjets:" << std::endl;
	for ( std::vector<GenParticle>::const_iterator genWJet1 = genWJets.begin();
	      genWJet1 != genWJets.end(); ++genWJet1 ) {
	  for ( std::vector<GenParticle>::const_iterator genWJet2 = genWJet1 + 1;
		genWJet2 != genWJets.end(); ++genWJet2 ) {
	    if ( deltaR(genWJet1->p4() + genWJet2->p4(), genWjjP4) < 1.e-1 && std::fabs((genWJet1->p4() + genWJet2->p4()).mass() - genWjjP4.mass()) < 1.e+1 ) {
	      std::cout << " genWJet #1: pT = " << genWJet1->pt() << ", eta = " << genWJet1->eta() << ", phi = " << genWJet1->phi() << std::endl;
	      std::cout << " genWJet #2: pT = " << genWJet2->pt() << ", eta = " << genWJet2->eta() << ", phi = " << genWJet2->phi() << std::endl;
	    }
	  }
	}
	std::cout << "reconstructed subjets:" << std::endl;
	const RecoSubjetAK8* subjet1 = (*jet_ak8)->subJet1();
	if ( subjet1 ) std::cout << " subjet #1: pT = " << subjet1->pt() << ", eta = " << subjet1->eta() << ", phi = " << subjet1->phi() << std::endl;
	const RecoSubjetAK8* subjet2 = (*jet_ak8)->subJet2();
	if ( subjet2 ) std::cout << " subjet #2: pT = " << subjet2->pt() << ", eta = " << subjet2->eta() << ", phi = " << subjet2->phi() << std::endl;
      }
    }
    if ( genWjjP4.pt() > 100. && !isMatched ) std::cout << "--> DEBUG (Wjj) !!" << std::endl;
  }
}

enum { kSignal, kBackground };

double
comp_mem_sumWeights(const std::vector<MEMOutput_hh_bb1l>& memOutputs_hh_bb1l, int signal_or_background)
{
  double weightSum = 0.;
  int numWeights = 0;
  for ( std::vector<MEMOutput_hh_bb1l>::const_iterator memOutput = memOutputs_hh_bb1l.begin();
  	memOutput != memOutputs_hh_bb1l.end(); ++memOutput ) {
    if ( memOutput->isValid() )
    {
      if      ( signal_or_background == kSignal     ) weightSum += memOutput->weight_signal();
      else if ( signal_or_background == kBackground ) weightSum += memOutput->weight_background();
      else assert(0);
      ++numWeights;
    }
  }
  if ( numWeights == 0 ) weightSum = -1.;
  return weightSum;
}

double
comp_mem_avWeight(const std::vector<MEMOutput_hh_bb1l>& memOutputs_hh_bb1l, int signal_or_background)
{
  double weightSum = comp_mem_sumWeights(memOutputs_hh_bb1l, signal_or_background);
  int numWeights = 0;
  for ( std::vector<MEMOutput_hh_bb1l>::const_iterator memOutput = memOutputs_hh_bb1l.begin();
  	memOutput != memOutputs_hh_bb1l.end(); ++memOutput ) {
    if ( memOutput->isValid() ) ++numWeights;
  }
  double avWeight = ( numWeights > 0 ) ? weightSum/numWeights : -1.;
  return avWeight;
}

double
comp_mem_avLR(const std::vector<MEMOutput_hh_bb1l>& memOutputs_hh_bb1l)
{
  double weightSum_signal = 0.;
  double weightSum_background = 0.;
  int numWeights = 0;
  for ( std::vector<MEMOutput_hh_bb1l>::const_iterator memOutput = memOutputs_hh_bb1l.begin();
  	memOutput != memOutputs_hh_bb1l.end(); ++memOutput ) {
    if ( memOutput->isValid() )
    {
      weightSum_signal += memOutput->weight_signal();
      weightSum_background += memOutput->weight_background();
      ++numWeights;
    }
  }
  double memLR = -1.;
  if ( numWeights > 0 )
  {
    if ( (weightSum_signal + weightSum_background) > 0. )
    {
      memLR = weightSum_signal/(weightSum_signal + weightSum_background);
    }
    else
    {
      memLR = 0.;
    }
  }
  return memLR;
}

double
comp_mem_maxWeight(const std::vector<MEMOutput_hh_bb1l>& memOutputs_hh_bb1l, int signal_or_background)
{
  double maxWeight = -1.;
  for ( std::vector<MEMOutput_hh_bb1l>::const_iterator memOutput = memOutputs_hh_bb1l.begin();
  	memOutput != memOutputs_hh_bb1l.end(); ++memOutput ) {
    if ( memOutput->isValid() )
    {
      double weight = 0.;
      if      ( signal_or_background == kSignal     ) weight = memOutput->weight_signal();
      else if ( signal_or_background == kBackground ) weight = memOutput->weight_background();
      else assert(0);
      if ( weight > maxWeight )
      {
        maxWeight = weight;
      }
    }
  }
  return maxWeight;
}

double
comp_mem_minLR(const std::vector<MEMOutput_hh_bb1l>& memOutputs_hh_bb1l)
{
  double minLR = -1.;
  bool isFirst = true;
  for ( std::vector<MEMOutput_hh_bb1l>::const_iterator memOutput = memOutputs_hh_bb1l.begin();
  	memOutput != memOutputs_hh_bb1l.end(); ++memOutput ) {
    if ( memOutput->isValid() )
    {
      if ( memOutput->LR() < minLR || isFirst )
      {
        minLR = memOutput->LR();
        isFirst = false;
      }
    }
  }
  return minLR;
}

double
comp_mem_maxLR(const std::vector<MEMOutput_hh_bb1l>& memOutputs_hh_bb1l)
{
  double maxLR = -1.;
  for ( std::vector<MEMOutput_hh_bb1l>::const_iterator memOutput = memOutputs_hh_bb1l.begin();
  	memOutput != memOutputs_hh_bb1l.end(); ++memOutput ) {
    if ( memOutput->isValid() )
    {
      if ( memOutput->LR() > maxLR )
      {
        maxLR = memOutput->LR();
      }
    }
  }
  return maxLR;
}

/**
 * @brief Produce datacard and control plots for dilepton category of the HH->bbWW analysis.
 */
int main(int argc, char* argv[])
{
//--- throw an exception in case ROOT encounters an error
  gErrorAbortLevel = kError;

//--- stop ROOT from keeping track of all histograms
  TH1::AddDirectory(false);

//--- parse command-line arguments
  if ( argc < 2 ) {
    std::cout << "Usage: " << argv[0] << " [parameters.py]" << std::endl;
    return EXIT_FAILURE;
  }

  std::cout << "<analyze_hh_bb1l>:" << std::endl;

//--- keep track of time it takes the macro to execute
  TBenchmark clock;
  clock.Start("analyze_hh_bb1l");

//--- read python configuration parameters
  if ( !edm::readPSetsFrom(argv[1])->existsAs<edm::ParameterSet>("process") )
    throw cms::Exception("analyze_hh_bb1l")
      << "No ParameterSet 'process' found in configuration file = " << argv[1] << " !!\n";

  edm::ParameterSet cfg = edm::readPSetsFrom(argv[1])->getParameter<edm::ParameterSet>("process");

  edm::ParameterSet cfg_analyze = cfg.getParameter<edm::ParameterSet>("analyze_hh_bb1l");

  std::string treeName = cfg_analyze.getParameter<std::string>("treeName");

  std::string process_string = cfg_analyze.getParameter<std::string>("process");
  const bool isMC_tH = process_string == "TH";
  const bool isMC_ttH = process_string == "TTH";
  const bool isMC_EWK = process_string == "WZ" || process_string == "ZZ";

  const bool take_Wjj_boosted_from_AK8_LS = false;
  const bool take_Wjj_boosted_with_B2G_sel = false;
  const bool ignore_Wjj_boosted = true; // this to be false will make Wjj_boosted be empty, but not innesistent
  const bool doDataMCPlots      = false;

  std::string histogramDir = cfg_analyze.getParameter<std::string>("histogramDir");
  bool isMCClosure_e = histogramDir.find("mcClosure_e") != std::string::npos;
  bool isMCClosure_m = histogramDir.find("mcClosure_m") != std::string::npos;

  std::string era_string = cfg_analyze.getParameter<std::string>("era");
  const Era era = get_era(era_string);

  vstring triggerNames_1e = cfg_analyze.getParameter<vstring>("triggers_1e");
  std::vector<hltPath*> triggers_1e = create_hltPaths(triggerNames_1e);
  bool use_triggers_1e = cfg_analyze.getParameter<bool>("use_triggers_1e");
  vstring triggerNames_1mu = cfg_analyze.getParameter<vstring>("triggers_1mu");
  std::vector<hltPath*> triggers_1mu = create_hltPaths(triggerNames_1mu);
  bool use_triggers_1mu = cfg_analyze.getParameter<bool>("use_triggers_1mu");

  bool apply_offline_e_trigger_cuts_1e = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_1e");
  bool apply_offline_e_trigger_cuts_1mu = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_1mu");

  const std::string electronSelection_string = cfg_analyze.getParameter<std::string>("electronSelection");
  const std::string muonSelection_string     = cfg_analyze.getParameter<std::string>("muonSelection");
  std::cout << "electronSelection_string = " << electronSelection_string << "\n"
               "muonSelection_string     = " << muonSelection_string     << '\n'
  ;
  const int electronSelection = get_selection(electronSelection_string);
  const int muonSelection     = get_selection(muonSelection_string);

  bool apply_leptonGenMatching = cfg_analyze.getParameter<bool>("apply_leptonGenMatching");
  std::vector<leptonGenMatchEntry> leptonGenMatch_definitions = getLeptonGenMatch_definitions_1lepton(true);
  std::cout << "leptonGenMatch_definitions:" << std::endl;
  std::cout << leptonGenMatch_definitions;

  GenMatchInterface genMatchInterface(1, apply_leptonGenMatching, false);

  bool apply_hadTauVeto = cfg_analyze.getParameter<bool>("apply_hadTauVeto");
  const std::string hadTauSelection_veto = cfg_analyze.getParameter<std::string>("hadTauSelection_veto");

  vstring evtCategoryNames = cfg_analyze.getParameter<vstring>("evtCategories");
  std::cout << "evtCategories = " << format_vstring(evtCategoryNames) << std::endl;

  bool isMC = cfg_analyze.getParameter<bool>("isMC");
  bool isSignal = boost::starts_with(process_string, "signal_") && process_string.find("_hh_") != std::string::npos;
  bool isHH_rwgt_allowed = boost::starts_with(process_string, "signal_ggf_nonresonant_") && process_string.find("cHHH") == std::string::npos;
  bool hasLHE = cfg_analyze.getParameter<bool>("hasLHE");
  bool hasPS = cfg_analyze.getParameter<bool>("hasPS");
  bool useAssocJetBtag = cfg_analyze.getParameter<bool>("useAssocJetBtag");
  bool apply_LHE_nom = cfg_analyze.getParameter<bool>("apply_LHE_nom");
  bool useObjectMultiplicity = cfg_analyze.getParameter<bool>("useObjectMultiplicity");
  std::string central_or_shift_main = cfg_analyze.getParameter<std::string>("central_or_shift");
  std::vector<std::string> central_or_shifts_local = cfg_analyze.getParameter<std::vector<std::string>>("central_or_shifts_local");
  edm::VParameterSet lumiScale = cfg_analyze.getParameter<edm::VParameterSet>("lumiScale");
  bool apply_genWeight = cfg_analyze.getParameter<bool>("apply_genWeight");
  bool apply_l1PreFireWeight = cfg_analyze.getParameter<bool>("apply_l1PreFireWeight");
  bool apply_btagSFRatio = cfg_analyze.getParameter<bool>("applyBtagSFRatio");
  std::string apply_topPtReweighting_str = cfg_analyze.getParameter<std::string>("apply_topPtReweighting");
  bool apply_topPtReweighting = ! apply_topPtReweighting_str.empty();
  bool apply_hlt_filter = cfg_analyze.getParameter<bool>("apply_hlt_filter");
  bool apply_met_filters = cfg_analyze.getParameter<bool>("apply_met_filters");
  edm::ParameterSet cfgMEtFilter = cfg_analyze.getParameter<edm::ParameterSet>("cfgMEtFilter");
  MEtFilterSelector metFilterSelector(cfgMEtFilter, isMC);
  const bool useNonNominal = cfg_analyze.getParameter<bool>("useNonNominal");
  const bool useNonNominal_jetmet = useNonNominal || ! isMC;

  if(! central_or_shifts_local.empty())
  {
    assert(central_or_shift_main == "central");
    assert(std::find(central_or_shifts_local.cbegin(), central_or_shifts_local.cend(), "central") != central_or_shifts_local.cend());
  }
  else
  {
    central_or_shifts_local = { central_or_shift_main };
  }

  edm::ParameterSet triggerWhiteList;
  if(! isMC)
  {
    triggerWhiteList = cfg_analyze.getParameter<edm::ParameterSet>("triggerWhiteList");
  }

  const edm::ParameterSet syncNtuple_cfg = cfg_analyze.getParameter<edm::ParameterSet>("syncNtuple");
  const std::string syncNtuple_tree = syncNtuple_cfg.getParameter<std::string>("tree");
  const std::string syncNtuple_output = syncNtuple_cfg.getParameter<std::string>("output");
  const bool do_sync = ! syncNtuple_tree.empty() && ! syncNtuple_output.empty();

  const edm::ParameterSet additionalEvtWeight = cfg_analyze.getParameter<edm::ParameterSet>("evtWeight");
  const bool applyAdditionalEvtWeight = additionalEvtWeight.getParameter<bool>("apply");
  EvtWeightManager * eventWeightManager = nullptr;
  if(applyAdditionalEvtWeight)
  {
    eventWeightManager = new EvtWeightManager(additionalEvtWeight);
    eventWeightManager->set_central_or_shift(central_or_shift_main);
  }

  bool isDEBUG = cfg_analyze.getParameter<bool>("isDEBUG");
  if ( isDEBUG ) std::cout << "Warning: DEBUG mode enabled -> trigger selection will not be applied for data !!" << std::endl;

  checkOptionValidity(central_or_shift_main, isMC);
  const int met_option      = useNonNominal_jetmet ? kJetMET_central_nonNominal : getMET_option(central_or_shift_main, isMC);
  const int jetPt_option    = useNonNominal_jetmet ? kJetMET_central_nonNominal : getJet_option(central_or_shift_main, isMC);
  const int fatJetPt_option = useNonNominal_jetmet ? kFatJet_central_nonNominal : getFatJet_option(central_or_shift_main, isMC);
  const int hadTauPt_option = useNonNominal_jetmet ? kHadTauPt_uncorrected      : getHadTauPt_option(central_or_shift_main);

  std::cout
    << "central_or_shift = "    << central_or_shift_main << "\n"
       " -> hadTauPt_option = " << hadTauPt_option       << "\n"
       " -> jetPt_option    = " << jetPt_option          << "\n"
       "--> fatJetPt_option = " << fatJetPt_option       << '\n'
  ;

  edm::ParameterSet cfg_dataToMCcorrectionInterface;
  cfg_dataToMCcorrectionInterface.addParameter<std::string>("era", era_string);
  cfg_dataToMCcorrectionInterface.addParameter<std::string>("hadTauSelection", "disabled"); // CV: dummy value (no taus used in HH->bbWW channel)
  cfg_dataToMCcorrectionInterface.addParameter<int>("hadTauSelection_antiElectron", -1);
  cfg_dataToMCcorrectionInterface.addParameter<int>("hadTauSelection_antiMuon", -1);
  cfg_dataToMCcorrectionInterface.addParameter<bool>("isDEBUG", isDEBUG);
  Data_to_MC_CorrectionInterface_Base * dataToMCcorrectionInterface = nullptr;
  switch(era)
  {
    case Era::k2016: dataToMCcorrectionInterface = new Data_to_MC_CorrectionInterface_2016(cfg_dataToMCcorrectionInterface); break;
    case Era::k2017: dataToMCcorrectionInterface = new Data_to_MC_CorrectionInterface_2017(cfg_dataToMCcorrectionInterface); break;
    case Era::k2018: dataToMCcorrectionInterface = new Data_to_MC_CorrectionInterface_2018(cfg_dataToMCcorrectionInterface); break;
    default: throw cmsException("analyze_hh_bb1l", __LINE__) << "Invalid era = " << static_cast<int>(era);
  }

  std::string applyFakeRateWeights_string = cfg_analyze.getParameter<std::string>("applyFakeRateWeights");
  int applyFakeRateWeights = -1;
  if      ( applyFakeRateWeights_string == "disabled" ) applyFakeRateWeights = kFR_disabled;
  else if ( applyFakeRateWeights_string == "enabled"  ) applyFakeRateWeights = kFR_enabled;
  else throw cms::Exception("analyze_hh_bb1l")
    << "Invalid Configuration parameter 'applyFakeRateWeights' = " << applyFakeRateWeights_string << " !!\n";

  LeptonFakeRateInterface* leptonFakeRateInterface = 0;
  if ( applyFakeRateWeights == kFR_enabled ) {
    edm::ParameterSet cfg_leptonFakeRateWeight = cfg_analyze.getParameter<edm::ParameterSet>("leptonFakeRateWeight");
    cfg_leptonFakeRateWeight.addParameter<std::string>("era", era_string);
    leptonFakeRateInterface = new LeptonFakeRateInterface(cfg_leptonFakeRateWeight);
  }

  bool fillGenEvtHistograms = cfg_analyze.getParameter<bool>("fillGenEvtHistograms");
  edm::ParameterSet cfg_EvtYieldHistManager = cfg_analyze.getParameter<edm::ParameterSet>("cfgEvtYieldHistManager");

  std::string branchName_electrons = cfg_analyze.getParameter<std::string>("branchName_electrons");
  std::string branchName_muons = cfg_analyze.getParameter<std::string>("branchName_muons");
  std::string branchName_hadTaus = cfg_analyze.getParameter<std::string>("branchName_hadTaus");
  std::string branchName_jets_ak4 = cfg_analyze.getParameter<std::string>("branchName_jets_ak4");
  std::string branchName_jets_ak8 = cfg_analyze.getParameter<std::string>("branchName_jets_ak8");
  std::string branchName_subjets_ak8 = cfg_analyze.getParameter<std::string>("branchName_subjets_ak8");
  std::string branchName_jets_ak8LS = cfg_analyze.getParameter<std::string>("branchName_jets_ak8LS");
  std::string branchName_subjets_ak8LS = cfg_analyze.getParameter<std::string>("branchName_subjets_ak8LS");
  std::string branchName_met = cfg_analyze.getParameter<std::string>("branchName_met");

  std::string branchName_memOutput = cfg_analyze.getParameter<std::string>("branchName_memOutput");
  std::string branchName_memOutput_missingBJet = cfg_analyze.getParameter<std::string>("branchName_memOutput_missingBJet");
  std::string branchName_memOutput_missingHadWJet = cfg_analyze.getParameter<std::string>("branchName_memOutput_missingHadWJet");

  std::string branchName_genLeptons = cfg_analyze.getParameter<std::string>("branchName_genLeptons");
  std::string branchName_genHadTaus = cfg_analyze.getParameter<std::string>("branchName_genHadTaus");
  std::string branchName_genPhotons = cfg_analyze.getParameter<std::string>("branchName_genPhotons");
  std::string branchName_genJets = cfg_analyze.getParameter<std::string>("branchName_genJets");

  std::string branchName_muonGenMatch     = cfg_analyze.getParameter<std::string>("branchName_muonGenMatch");
  std::string branchName_electronGenMatch = cfg_analyze.getParameter<std::string>("branchName_electronGenMatch");
  std::string branchName_hadTauGenMatch   = cfg_analyze.getParameter<std::string>("branchName_hadTauGenMatch");
  std::string branchName_jetGenMatch      = cfg_analyze.getParameter<std::string>("branchName_jetGenMatch");

  bool redoGenMatching = cfg_analyze.getParameter<bool>("redoGenMatching");
  bool jetCleaningByIndex = cfg_analyze.getParameter<bool>("jetCleaningByIndex");
  bool genMatchingByIndex = cfg_analyze.getParameter<bool>("genMatchingByIndex");

  std::string branchName_genBJets = cfg_analyze.getParameter<std::string>("branchName_genBJets");
  std::string branchName_genWBosons = cfg_analyze.getParameter<std::string>("branchName_genWBosons");
  std::string branchName_genWJets = cfg_analyze.getParameter<std::string>("branchName_genWJets");

  bool selectBDT = ( cfg_analyze.exists("selectBDT") ) ? cfg_analyze.getParameter<bool>("selectBDT") : false;

  std::string selEventsFileName_input = cfg_analyze.getParameter<std::string>("selEventsFileName_input");
  std::cout << "selEventsFileName_input = " << selEventsFileName_input << std::endl;
  RunLumiEventSelector* run_lumi_eventSelector = 0;
  if ( selEventsFileName_input != "" ) {
    edm::ParameterSet cfg_runLumiEventSelector;
    cfg_runLumiEventSelector.addParameter<std::string>("inputFileName", selEventsFileName_input);
    cfg_runLumiEventSelector.addParameter<std::string>("separator", ":");
    run_lumi_eventSelector = new RunLumiEventSelector(cfg_runLumiEventSelector);
  }

  std::string selEventsFileName_output = cfg_analyze.getParameter<std::string>("selEventsFileName_output");
  std::cout << "selEventsFileName_output = " << selEventsFileName_output << std::endl;

  fwlite::InputSource inputFiles(cfg);
  int maxEvents = inputFiles.maxEvents();
  std::cout << " maxEvents = " << maxEvents << std::endl;
  unsigned reportEvery = inputFiles.reportAfter();

  fwlite::OutputFiles outputFile(cfg);
  fwlite::TFileService fs = fwlite::TFileService(outputFile.file().data());

  TTreeWrapper* inputTree = new TTreeWrapper(treeName.data(), inputFiles.files(), maxEvents);
  std::cout << "Loaded " << inputTree->getFileCount() << " file(s)\n";

//--- prepare sync Ntuple
  SyncNtupleManager_bbww * snm = nullptr;
  if(do_sync)
  {
    snm = new SyncNtupleManager_bbww(syncNtuple_output, syncNtuple_tree);
    snm->initializeBranches();
    snm->initializeHLTBranches({ triggers_1e, triggers_1mu });
  }

//--- declare event-level variables
  EventInfo eventInfo(isMC, isSignal, isHH_rwgt_allowed, apply_topPtReweighting);
  const std::string default_cat_str = "default";
  std::vector<std::string> evt_cat_strs = { default_cat_str };

//--- HH scan
  const edm::ParameterSet hhWeight_cfg = cfg_analyze.getParameterSet("hhWeight_cfg");
  const bool apply_HH_rwgt = eventInfo.is_hh_nonresonant() && hhWeight_cfg.getParameter<bool>("apply_rwgt");
  const HHWeightInterface * HHWeight_calc = nullptr;
  if(apply_HH_rwgt)
  {
    HHWeight_calc = new HHWeightInterface(hhWeight_cfg);
    evt_cat_strs = HHWeight_calc->get_scan_strs();
  }
  const size_t Nscan = evt_cat_strs.size();
  if (apply_HH_rwgt)
  {
    std::cout << "Number of points being scanned = " << Nscan << '\n';
    for (const std::string catcat : evt_cat_strs) {
      std::cout << catcat << '\n';
    }
    for (const std::string catcat : BMS) {
      std::cout << catcat << '\n';
    }
  }

  const std::vector<edm::ParameterSet> tHweights = cfg_analyze.getParameterSetVector("tHweights");
  if((isMC_tH || isMC_ttH) && ! tHweights.empty())
  {
    eventInfo.loadWeight_tH(tHweights);
  }
  EventInfoReader eventInfoReader(&eventInfo);
  if(apply_topPtReweighting)
  {
    eventInfoReader.setTopPtRwgtBranchName(apply_topPtReweighting_str);
  }
  inputTree->registerReader(&eventInfoReader);

  ObjectMultiplicity objectMultiplicity;
  ObjectMultiplicityReader objectMultiplicityReader(&objectMultiplicity);
  if(useObjectMultiplicity)
  {
    inputTree -> registerReader(&objectMultiplicityReader);
  }
  const int minLeptonSelection = std::min(electronSelection, muonSelection);

  hltPathReader hltPathReader_instance({ triggers_1e, triggers_1mu });
  inputTree->registerReader(&hltPathReader_instance);

  if(eventWeightManager)
  {
    inputTree->registerReader(eventWeightManager);
  }

  L1PreFiringWeightReader * l1PreFiringWeightReader = nullptr;
  if(apply_l1PreFireWeight)
  {
    l1PreFiringWeightReader = new L1PreFiringWeightReader(era);
    inputTree->registerReader(l1PreFiringWeightReader);
  }

  BtagSFRatioFacility * btagSFRatioFacility = nullptr;
  if(apply_btagSFRatio)
  {
    const edm::ParameterSet btagSFRatio = cfg_analyze.getParameterSet("btagSFRatio");
    btagSFRatioFacility = new BtagSFRatioFacility(btagSFRatio);
  }

//--- declare particle collections
  const bool readGenObjects = isMC && !redoGenMatching;
  RecoMuonReader* muonReader = new RecoMuonReader(era, branchName_muons, isMC, readGenObjects);
  inputTree->registerReader(muonReader);
  RecoMuonCollectionGenMatcher muonGenMatcher;
  RecoMuonCollectionSelectorLoose preselMuonSelector(era, -1, isDEBUG);
  RecoMuonCollectionSelectorFakeable fakeableMuonSelector(era, -1, isDEBUG);
  RecoMuonCollectionSelectorTight tightMuonSelector(era, -1, isDEBUG);
  fakeableMuonSelector.getSelector().set_assocJetBtag(useAssocJetBtag);
  tightMuonSelector.getSelector().set_assocJetBtag(useAssocJetBtag);

  RecoElectronReader* electronReader = new RecoElectronReader(era, branchName_electrons, isMC, readGenObjects);
  inputTree->registerReader(electronReader);
  RecoElectronCollectionGenMatcher electronGenMatcher;
  RecoElectronCollectionCleaner electronCleaner(0.3, isDEBUG);
  RecoElectronCollectionSelectorLoose preselElectronSelector(era, -1, isDEBUG);
  RecoElectronCollectionSelectorFakeable fakeableElectronSelector(era, -1, isDEBUG);
  RecoElectronCollectionSelectorTight tightElectronSelector(era, -1, isDEBUG);
  fakeableElectronSelector.getSelector().set_assocJetBtag(useAssocJetBtag);
  tightElectronSelector.getSelector().set_assocJetBtag(useAssocJetBtag);

  RecoHadTauReader* hadTauReader = new RecoHadTauReader(era, branchName_hadTaus, isMC, readGenObjects);
  hadTauReader->setHadTauPt_central_or_shift(hadTauPt_option);
  inputTree->registerReader(hadTauReader);
  RecoHadTauCollectionGenMatcher hadTauGenMatcher;
  RecoHadTauCollectionCleaner hadTauCleaner(0.3, isDEBUG);
  // CV: veto events containing one or more taus, to avoid overlap with HH->bbWW single lepton channel
  RecoHadTauCollectionSelectorTight vetoHadTauSelector(era, -1, isDEBUG);
  vetoHadTauSelector.set(hadTauSelection_veto);
  vetoHadTauSelector.set_min_antiElectron(hadTauSelection_veto_antiElectron);
  vetoHadTauSelector.set_min_antiMuon(hadTauSelection_veto_antiMuon);

  RecoJetReader* jetReaderAK4 = new RecoJetReader(era, isMC, branchName_jets_ak4, readGenObjects);
  jetReaderAK4->setPtMass_central_or_shift(jetPt_option);
  jetReaderAK4->read_btag_systematics((central_or_shifts_local.size() > 1 || central_or_shift_main != "central") && isMC);
  inputTree->registerReader(jetReaderAK4);
  RecoJetCollectionGenMatcher jetGenMatcherAK4;
  RecoJetCollectionCleaner jetCleanerAK4_dR04(0.4, isDEBUG);
  RecoJetCollectionCleanerByIndex jetCleanerAK4_byIndex(isDEBUG);
  RecoJetCollectionCleaner jetCleanerAK4_dR08(0.8, isDEBUG);
  RecoJetCollectionCleaner jetCleanerAK4_dR12(1.2, isDEBUG);
  RecoJetCollectionSelector jetSelectorAK4(era, -1, isDEBUG);
  RecoJetCollectionSelector jetSelectorAK4_vbf(era, -1, isDEBUG);
  //jetSelectorAK4_vbf.getSelector().set_min_pt(30.);
  jetSelectorAK4_vbf.getSelector().set_max_absEta(4.7);
  RecoJetCollectionSelectorBtagLoose jetSelectorAK4_bTagLoose(era, -1, isDEBUG);
  RecoJetCollectionSelectorBtagMedium jetSelectorAK4_bTagMedium(era, -1, isDEBUG);

  RecoJetReaderAK8* jetReaderAK8 = new RecoJetReaderAK8(era, isMC, branchName_jets_ak8, branchName_subjets_ak8);
  jetReaderAK8->set_central_or_shift(fatJetPt_option);
  RecoJetReaderAK8* jetReaderAK8LS = nullptr;
  if ( branchName_jets_ak8LS != branchName_jets_ak8 ) {
    jetReaderAK8LS = new RecoJetReaderAK8(era, isMC, branchName_jets_ak8LS, branchName_subjets_ak8LS);
    jetReaderAK8LS->set_central_or_shift(fatJetPt_option);
  } else {
    jetReaderAK8LS = jetReaderAK8;
  }
  inputTree->registerReader(jetReaderAK8);
  inputTree->registerReader(jetReaderAK8LS);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR08(0.8, isDEBUG);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR12(1.2, isDEBUG);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR16(1.6, isDEBUG);
  RecoJetCollectionSelectorAK8_hh_bbWW_Hbb jetSelectorAK8_Hbb(era, -1, isDEBUG);
  RecoJetCollectionSelectorAK8_hh_Wjj jetSelectorAK8_Wjj(era, -1, isDEBUG);
  RecoJetCollectionSelectorAK8 jetSelectorAK8(era);

  MEMOutputReader_hh_bb1l* memReader = nullptr;
  if ( !branchName_memOutput.empty() )
  {
    memReader = new MEMOutputReader_hh_bb1l(
      Form("n%s", branchName_memOutput.data()), branchName_memOutput);
    inputTree->registerReader(memReader);
  }
  MEMOutputReader_hh_bb1l* memReader_missingBJet = nullptr;
  if ( !branchName_memOutput_missingBJet.empty() )
  {
    memReader_missingBJet = new MEMOutputReader_hh_bb1l(
      Form("n%s", branchName_memOutput_missingBJet.data()), branchName_memOutput_missingBJet);
    inputTree->registerReader(memReader_missingBJet);
  }
  MEMOutputReader_hh_bb1l* memReader_missingHadWJet = nullptr;
  if ( !branchName_memOutput_missingHadWJet.empty() )
  {
    memReader_missingHadWJet = new MEMOutputReader_hh_bb1l(
      Form("n%s", branchName_memOutput_missingHadWJet.data()), branchName_memOutput_missingHadWJet);
    inputTree->registerReader(memReader_missingHadWJet);
  }

  GenParticleReader* genBJetReader = nullptr;
  GenParticleReader* genWBosonReader = nullptr;
  GenParticleReader* genWJetReader = nullptr;
  if ( isMC ) {
    genBJetReader = new GenParticleReader(branchName_genBJets);
    inputTree->registerReader(genBJetReader);
    genWBosonReader = new GenParticleReader(branchName_genWBosons);
    inputTree->registerReader(genWBosonReader);
    genWJetReader = new GenParticleReader(branchName_genWJets);
    inputTree->registerReader(genWJetReader);
  }

//--- declare missing transverse energy
  RecoMEtReader* metReader = new RecoMEtReader(era, isMC, branchName_met);
  metReader->setMEt_central_or_shift(met_option);
  inputTree->registerReader(metReader);

  MEtFilter metFilters;
  MEtFilterReader* metFilterReader = new MEtFilterReader(&metFilters, era);
  inputTree->registerReader(metFilterReader);

//--- declare generator level information
  GenLeptonReader * genLeptonReader = nullptr;
  GenHadTauReader * genHadTauReader = nullptr;
  GenPhotonReader * genPhotonReader = nullptr;
  GenJetReader * genJetReader = nullptr;
  LHEInfoReader * lheInfoReader = nullptr;
  PSWeightReader * psWeightReader = nullptr;

  GenParticleReader * genMatchToMuonReader     = nullptr;
  GenParticleReader * genMatchToElectronReader = nullptr;
  GenParticleReader * genMatchToHadTauReader   = nullptr;
  GenParticleReader * genMatchToJetReader      = nullptr;

  if(isMC)
  {
    if(! readGenObjects)
    {
      genLeptonReader = new GenLeptonReader(branchName_genLeptons);
      inputTree->registerReader(genLeptonReader);
      genHadTauReader = new GenHadTauReader(branchName_genHadTaus);
      inputTree->registerReader(genHadTauReader);
      genJetReader = new GenJetReader(branchName_genJets);
      inputTree->registerReader(genJetReader);

      if(genMatchingByIndex)
      {
        genMatchToMuonReader = new GenParticleReader(branchName_muonGenMatch);
        genMatchToMuonReader -> readGenPartFlav(true);
        inputTree -> registerReader(genMatchToMuonReader);

        genMatchToElectronReader = new GenParticleReader(branchName_electronGenMatch);
        genMatchToElectronReader -> readGenPartFlav(true);
        inputTree -> registerReader(genMatchToElectronReader);

        genMatchToHadTauReader = new GenParticleReader(branchName_hadTauGenMatch);
        genMatchToHadTauReader -> readGenPartFlav(true);
        inputTree -> registerReader(genMatchToHadTauReader);

        genMatchToJetReader = new GenParticleReader(branchName_jetGenMatch);
        genMatchToJetReader -> readGenPartFlav(true);
        inputTree -> registerReader(genMatchToJetReader);
      }
      else
      {
        genPhotonReader = new GenPhotonReader(branchName_genPhotons);
        inputTree -> registerReader(genPhotonReader);
      }
    }
    lheInfoReader = new LHEInfoReader(hasLHE);
    inputTree->registerReader(lheInfoReader);
    psWeightReader = new PSWeightReader(hasPS, apply_LHE_nom);
    inputTree -> registerReader(psWeightReader);
  }

//--- initialize BDT for ranking of W->jj decays
  TMVAInterface mva_Wjj = initialize_mva_Wjj();

//--- open output file containing run:lumi:event numbers of events passing final event selection criteria
  std::ostream* selEventsFile = ( selEventsFileName_output != "" ) ? new std::ofstream(selEventsFileName_output.data(), std::ios::out) : 0;
  std::cout << "selEventsFileName_output = " << selEventsFileName_output << std::endl;

//--- declare histograms
  std::vector<std::string> xgbInputVariables_bb1l_X900GeV_Wjj_simple = {
    "mindr_lep1_jet", "m_Hbb_regCorr", "mHH_simple_met", "mWlep_met_simple", "mWW_simple_met", "mWjj_simple", "cosThetaS_Hbb", "cosThetaS_Wjj_simple", "cosThetaS_WW_simple_met", "cosThetaS_HH_simple_met", "nJet", "nBJetMedium", "dR_b1lep", "dR_b2lep", "dr_Wj1_lep_simple", "dr_Wj2_lep_simple", "lep_conePt", "met_LD", "HT", "mT_top_3particle", "mT_W"
  };
  // baselines == trained for 2016 era only
  // for the all reco category with simple Wjj reconstruction
  std::string xgbFileName_bb1l_X900GeV_Wjj_simple_full_reco_only_even = "hhAnalysis/bbww/data/BDT_hh_bb1l/hh_bb1l_X900GeV_Wjj_simple_full_reco_even.xml";
  std::string xgbFileName_bb1l_X900GeV_Wjj_simple_full_reco_only_odd  = "hhAnalysis/bbww/data/BDT_hh_bb1l/hh_bb1l_X900GeV_Wjj_simple_full_reco_odd.xml";
  TMVAInterface mva_xgb_bb1l_X900GeV_Wjj_simple_full_reco_only( xgbFileName_bb1l_X900GeV_Wjj_simple_full_reco_only_odd, xgbFileName_bb1l_X900GeV_Wjj_simple_full_reco_only_even, xgbInputVariables_bb1l_X900GeV_Wjj_simple);
  mva_xgb_bb1l_X900GeV_Wjj_simple_full_reco_only.enableBDTTransform();
  std::vector<std::string> xgbInputVariables_bb1l_SM_Wjj_simple = {
    "mindr_lep1_jet", "m_Hbb_regCorr", "mHH_simple_met", "mWlep_met_simple", "mWW_simple_met", "mWjj_simple", "cosThetaS_Hbb", "cosThetaS_Wjj_simple", "cosThetaS_WW_simple_met", "cosThetaS_HH_simple_met", "nJet", "nBJetMedium", "dR_b1lep", "dR_b2lep", "lep_conePt", "selJet1_Hbb_pT", "selJet2_Hbb_pT", "met_LD", "HT", "mT_top_3particle", "mT_W"
  };
  std::string xgbFileName_bb1l_SM_Wjj_simple_full_reco_only_even = "hhAnalysis/bbww/data/BDT_hh_bb1l/hh_bb1l_SM_Wjj_simple_full_reco_only_noIndPt_even.xml";
  std::string xgbFileName_bb1l_SM_Wjj_simple_full_reco_only_odd  = "hhAnalysis/bbww/data/BDT_hh_bb1l/hh_bb1l_SM_Wjj_simple_full_reco_only_noIndPt_odd.xml";
  TMVAInterface mva_xgb_bb1l_SM_Wjj_simple_full_reco_only(      xgbFileName_bb1l_SM_Wjj_simple_full_reco_only_odd, xgbFileName_bb1l_SM_Wjj_simple_full_reco_only_even, xgbInputVariables_bb1l_SM_Wjj_simple);
  mva_xgb_bb1l_SM_Wjj_simple_full_reco_only.enableBDTTransform();

  // for the missingJet category
  std::vector<std::string> xgbInputVariables_bb1l_X900GeV_Wj1 = {
    "mT_top_3particle", "mT_W", "mindr_lep1_jet", "dR_b1lep", "dR_b2lep", "m_Hbb_regCorr", "selJet1_Hbb_pT", "selJet2_Hbb_pT", "dr_Wj1_lep_simple", "nBJetMedium", "lep_conePt", "met_LD", "HT"
  };
  std::string xgbFileName_bb1l_X900GeV_Wj1_even                       = "hhAnalysis/bbww/data/BDT_hh_bb1l/hh_bb1l_X900GeV_Wj1_even.xml";
  std::string xgbFileName_bb1l_X900GeV_Wj1_odd                        = "hhAnalysis/bbww/data/BDT_hh_bb1l/hh_bb1l_X900GeV_Wj1_odd.xml";
  TMVAInterface mva_xgb_bb1l_X900GeV_Wj1(                       xgbFileName_bb1l_X900GeV_Wj1_odd,                       xgbFileName_bb1l_X900GeV_Wj1_even,                       xgbInputVariables_bb1l_X900GeV_Wj1);
  std::vector<std::string> xgbInputVariables_bb1l_SM_Wj1 = {
    "mT_top_3particle", "mT_W", "mindr_lep1_jet", "dR_b1lep", "dR_b2lep", "m_Hbb_regCorr", "selJet1_Hbb_pT", "selJet2_Hbb_pT", "dr_Wj1_lep_simple", "nBJetMedium", "lep_conePt", "met_LD", "HT"
  };
  mva_xgb_bb1l_X900GeV_Wj1.enableBDTTransform();
  std::string xgbFileName_bb1l_SM_Wj1_even                       = "hhAnalysis/bbww/data/BDT_hh_bb1l/hh_bb1l_SM_Wj1_even.xml";
  std::string xgbFileName_bb1l_SM_Wj1_odd                        = "hhAnalysis/bbww/data/BDT_hh_bb1l/hh_bb1l_SM_Wj1_odd.xml";
  TMVAInterface mva_xgb_bb1l_SM_Wj1(                            xgbFileName_bb1l_SM_Wj1_odd,                       xgbFileName_bb1l_SM_Wj1_even,                       xgbInputVariables_bb1l_SM_Wj1);

  // for the all reco category with MVA Wjj
  /*
  std::vector<std::string> xgbInputVariables_4jet_assigment = {};
  std::string xgbFileName_4jet_assigment_even    = "";
  std::string xgbFileName_4jet_assigment_odd     = "";
  XGBInterface xgbFileName_4jet_assigment(    xgbFileName_4jet_assigment_odd,    xgbFileName_4jet_assigment_even,    xgbInputVariables_4jet_assigment);
  //xgbFileName_4jet_assigment.enableBDTTransform();

  // --> event level BDTs trained with the 4 jets selected as result of the 4jet_assigment above
  std::vector<std::string> xgbInputVariables_bb1l_X900GeV_Wjj_BDT = {};
  std::string xgbFileName_bb1l_X900GeV_Wjj_BDT_full_reco_only_even    = "";
  std::string xgbFileName_bb1l_X900GeV_Wjj_BDT_full_reco_only_odd     = "";
  TMVAInterface mva_xgb_bb1l_X900GeV_Wjj_BDT_full_reco_only(    xgbFileName_bb1l_X900GeV_Wjj_BDT_full_reco_only_odd,    xgbFileName_bb1l_X900GeV_Wjj_BDT_full_reco_only_even,    xgbInputVariables_bb1l_X900GeV_Wjj_BDT);
  mva_xgb_bb1l_X900GeV_Wjj_BDT_full_reco_only.enableBDTTransform();
  mva_xgb_bb1l_SM_Wj1.enableBDTTransform();
  std::vector<std::string> xgbInputVariables_bb1l_SM_Wjj_BDT = {
    "mindr_lep1_jet", "m_Hbb_regCorr", "m_HH", "mWlep_met_simple", "dR_Hww", "m_Wjj", "cosThetaS_Hbb", "cosThetaS_Wjj", "cosThetaS_WW", "cosThetaS_HH", "nJet", "nBJetMedium", "dR_b1lep", "dR_b2lep", "selJet1_Hbb_pT", "selJet2_Hbb_pT", "lep_conePt", "met_LD", "mT_W", "mT_top_3particle", "HT"
  };
  std::string xgbFileName_bb1l_SM_Wjj_BDT_full_reco_only_even    = "hhAnalysis/bbww/data/BDT_hh_bb1l/hh_bb1l_SM_Wjj_BDT_full_reco_only_even.xml";
  std::string xgbFileName_bb1l_SM_Wjj_BDT_full_reco_only_odd     = "hhAnalysis/bbww/data/BDT_hh_bb1l/hh_bb1l_SM_Wjj_BDT_full_reco_only_odd.xml";
  TMVAInterface mva_xgb_bb1l_SM_Wjj_BDT_full_reco_only(         xgbFileName_bb1l_SM_Wjj_BDT_full_reco_only_odd,    xgbFileName_bb1l_SM_Wjj_BDT_full_reco_only_even,    xgbInputVariables_bb1l_SM_Wjj_BDT); // ,
  mva_xgb_bb1l_SM_Wjj_BDT_full_reco_only.enableBDTTransform();
  */

  // example of loading pb
  /*
  std::string jet_assignment_LBN = "hhAnalysis/bbww/data/jet_assignment_MVAs/my_model_even.pb";
  std::vector<std::string> mvaInputVariables_LBN = {
    "bjet1_btagCSV", "bjet2_ptReg", "bjet2_btagCSV", "bjet2_qgDiscr", "wjet2_ptReg", "wjet2_qgDiscr", "HadW_mass", "dR_HadW_lep", "max_dR_HadW_bjet", "dR_wjet1wjet2", "mTop1"
  };
  TensorFlowInterface mva_LBN(jet_assignment_LBN, mvaInputVariables_LBN, {}, "", "");
  */

  ////
  // _HbbFat_WjjFat_HP
  // _HbbFat_WjjFat_LP
  // _HbbFat_WjjRes_allReco
  // _HbbFat_WjjRes_MissWJet
  // _WjjFat_HP
  // _WjjFat_LP
  // _Res_allReco
  // _Res_MissWJet
  // _Res_MissBJet
  std::map<std::string, std::vector<double>> categories_list_bins = {
     // category name          binning (if empty is 400 bins from 0-1)
     {"_HbbFat_WjjRes_allReco_e", {}},
     {"_Res_allReco_1b_e",        {}},
     {"_Res_allReco_2b_e",        {}},
     //
     {"_HbbFat_WjjRes_allReco_m", {}},
     {"_Res_allReco_1b_m",        {}},
     {"_Res_allReco_2b_m",        {}},
     //
     {"_HbbFat_WjjRes_MissWJet_e", {}},
     {"_Res_MissWJet_1b_e",       {}},
     {"_Res_MissWJet_2b_e",       {}},
     //
     {"_HbbFat_WjjRes_MissWJet_m", {}},
     {"_Res_MissWJet_1b_m",       {}},
     {"_Res_MissWJet_2b_m",       {}}
  };
  if ( ! ignore_Wjj_boosted )
  {
      categories_list_bins["_HbbFat_WjjFat_HP_e"] =      {};
      categories_list_bins["_WjjFat_HP_e"] =             {};
      categories_list_bins["_HbbFat_WjjFat_LP_e"] =      {};
      categories_list_bins["_WjjFat_LP_e"] =             {};
      //
      categories_list_bins["_HbbFat_WjjFat_HP_m"] =      {};
      categories_list_bins["_WjjFat_HP_m"] =             {};
      categories_list_bins["_HbbFat_WjjFat_LP_m"] =      {};
      categories_list_bins["_WjjFat_LP_m"] =             {};
      //
      categories_list_bins["_Res_MissBJet_m"] =          {};
      categories_list_bins["_Res_MissBJet_e"] =          {};
  }
  const std::vector<std::string> for_categories_map =
  {
    "cat_jet_2BDT_Wjj_BDT_SM",
    "cat_jet_2BDT_Wjj_simple_SM",
    "cat_jet_2BDT_Wjj_BDT_X900GeV",
    "cat_jet_2BDT_Wjj_simple_X900GeV"
  };
  // X: I will assume that the binning by subcategory is fixed independent of the BDT
  // that may end up not being true. In that case, there is some logic to work out again
  // one idea of solution if the different binning schemes to resonant and non-resonant is to make
  // a  categories_list_bins_res / for_categories_map_res / categories_map_MVA_res and a categories_list_bins_nonres / for_categories_map_nonres / categories_map_MVA_nonres

  struct selHistManagerType
  {
    ElectronHistManager* electrons_;
    MuonHistManager* muons_;
    JetHistManager* jetsAK4_;
    JetHistManager* leadJetAK4_;
    JetHistManager* subleadJetAK4_;
    JetHistManagerAK8* jetsAK8_Hbb_;
    JetHistManagerAK8* jetsAK8_Wjj_;
    JetHistManager* BJetsAK4_loose_;
    JetHistManager* leadBJetAK4_loose_;
    JetHistManager* subleadBJetAK4_loose_;
    JetHistManager* BJetsAK4_medium_;
    MEtHistManager* met_;
    MEtFilterHistManager* metFilters_;
    std::map<std::string, EvtHistManager_hh_bb1l*> evt_;
    std::map<std::string, std::map<std::string, EvtHistManager_hh_bb1l*>> evt_in_categories_;
    GenEvtHistManager* genEvtHistManager_afterCuts_;
    LHEInfoHistManager* lheInfoHistManager_afterCuts_;
    std::map<std::string, LHEInfoHistManager*> lheInfoHistManager_afterCuts_in_categories_;
    EvtYieldHistManager* evtYield_;
    WeightHistManager* weights_;
  };

  std::map<std::string, GenEvtHistManager*> genEvtHistManager_beforeCuts;
  std::map<std::string, LHEInfoHistManager*> lheInfoHistManager_beforeCuts;
  std::map<std::string, std::map<int, selHistManagerType*>> selHistManagers;
  for(const std::string & central_or_shift: central_or_shifts_local)
  {
    const bool skipBooking = central_or_shift != central_or_shift_main;
    std::vector<const GenMatchEntry*> genMatchDefinitions = genMatchInterface.getGenMatchDefinitions();
    for (const GenMatchEntry * genMatchDefinition : genMatchDefinitions)
    {
      std::string process_and_genMatch = process_string;
      process_and_genMatch += genMatchDefinition->getName();

      int idxLepton = genMatchDefinition->getIdx();

      selHistManagerType* selHistManager = new selHistManagerType();
      if(! skipBooking)
      {
        selHistManager->electrons_ = new ElectronHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/electrons", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
        selHistManager->electrons_->bookHistograms(fs);
        selHistManager->muons_ = new MuonHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/muons", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
        selHistManager->muons_->bookHistograms(fs);
        selHistManager->jetsAK4_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/jetsAK4", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
        selHistManager->jetsAK4_->bookHistograms(fs);
        selHistManager->leadJetAK4_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/leadJetAK4", histogramDir.data()), era_string, central_or_shift, "minimalHistograms", 0));
        selHistManager->leadJetAK4_->bookHistograms(fs);
        selHistManager->subleadJetAK4_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/subleadJetAK4", histogramDir.data()), era_string, central_or_shift, "minimalHistograms", 1));
        selHistManager->subleadJetAK4_->bookHistograms(fs);
        selHistManager->jetsAK8_Hbb_ = new JetHistManagerAK8(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/jetsAK8_Hbb", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
        selHistManager->jetsAK8_Hbb_->bookHistograms(fs);
        selHistManager->jetsAK8_Wjj_ = new JetHistManagerAK8(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/jetsAK8_Wjj", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
        selHistManager->jetsAK8_Wjj_->bookHistograms(fs);
        selHistManager->BJetsAK4_loose_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/BJetsAK4_loose", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
        selHistManager->BJetsAK4_loose_->bookHistograms(fs);
        selHistManager->leadBJetAK4_loose_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/leadBJetAK4_loose", histogramDir.data()), era_string, central_or_shift, "minimalHistograms", 0));
        selHistManager->leadBJetAK4_loose_->bookHistograms(fs);
        selHistManager->subleadBJetAK4_loose_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/subleadBJetAK4_loose", histogramDir.data()), era_string, central_or_shift, "minimalHistograms", 1));
        selHistManager->subleadBJetAK4_loose_->bookHistograms(fs);
        selHistManager->BJetsAK4_medium_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/BJetsAK4_medium", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
        selHistManager->BJetsAK4_medium_->bookHistograms(fs);
        selHistManager->met_ = new MEtHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/met", histogramDir.data()), era_string, central_or_shift));
        selHistManager->met_->bookHistograms(fs);
        selHistManager->metFilters_ = new MEtFilterHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/metFilters", histogramDir.data()), era_string, central_or_shift));
        selHistManager->metFilters_->bookHistograms(fs);
      }

      for(const std::string & evt_cat_str: evt_cat_strs)
      {
        if(skipBooking && evt_cat_str != default_cat_str)
        {
          continue;
        }
        const std::string process_string_new = evt_cat_str == default_cat_str ?
          process_string  :
          process_string + evt_cat_str
        ;

        const std::string process_and_genMatchName = boost::replace_all_copy(
          process_and_genMatch, process_string, process_string_new
        );
        selHistManager->evt_[evt_cat_str] = new EvtHistManager_hh_bb1l(makeHistManager_cfg(process_and_genMatchName,
          Form("%s/sel/evt", histogramDir.data()), era_string, central_or_shift, "memDisabled"));
        selHistManager->evt_[evt_cat_str]->bookHistograms(fs);
        //
        selHistManager->evt_[evt_cat_str]->bookCategories(fs, categories_list_bins, for_categories_map, doDataMCPlots);
      }

      if(isMC && ! skipBooking)
      {
        selHistManager->genEvtHistManager_afterCuts_ = new GenEvtHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/genEvt", histogramDir.data()), era_string, central_or_shift));
        selHistManager->genEvtHistManager_afterCuts_->bookHistograms(fs);
        selHistManager->lheInfoHistManager_afterCuts_ = new LHEInfoHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/lheInfo", histogramDir.data()), era_string, central_or_shift));
        selHistManager->lheInfoHistManager_afterCuts_->bookHistograms(fs);

        if(eventWeightManager)
        {
          selHistManager->genEvtHistManager_afterCuts_->bookHistograms(fs, eventWeightManager);
        }
      }

      if(! skipBooking)
      {
        edm::ParameterSet cfg_EvtYieldHistManager_sel = makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/evtYield", histogramDir.data()), era_string, central_or_shift);
        cfg_EvtYieldHistManager_sel.addParameter<edm::ParameterSet>("runPeriods", cfg_EvtYieldHistManager);
        cfg_EvtYieldHistManager_sel.addParameter<bool>("isMC", isMC);
        selHistManager->evtYield_ = new EvtYieldHistManager(cfg_EvtYieldHistManager_sel);
        selHistManager->evtYield_->bookHistograms(fs);
        selHistManager->weights_ = new WeightHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/weights", histogramDir.data()), era_string, central_or_shift));
        selHistManager->weights_->bookHistograms(fs, { "genWeight", "pileupWeight", "triggerWeight", "data_to_MC_correction", "fakeRate" });
      }
      selHistManagers[central_or_shift][idxLepton] = selHistManager;
    }

    if(isMC && ! skipBooking)
    {
      genEvtHistManager_beforeCuts[central_or_shift] = new GenEvtHistManager(makeHistManager_cfg(process_string,
        Form("%s/unbiased/genEvt", histogramDir.data()), era_string, central_or_shift));
      genEvtHistManager_beforeCuts[central_or_shift]->bookHistograms(fs);
      lheInfoHistManager_beforeCuts[central_or_shift] = new LHEInfoHistManager(makeHistManager_cfg(process_string,
        Form("%s/unbiased/lheInfo", histogramDir.data()), era_string, central_or_shift));
      lheInfoHistManager_beforeCuts[central_or_shift]->bookHistograms(fs);

      if(eventWeightManager)
      {
        genEvtHistManager_beforeCuts[central_or_shift]->bookHistograms(fs, eventWeightManager);
      }
    }
  }

  std::cout << "Book BDT filling" << std::endl;
  NtupleFillerBDT<float, int>* bdt_filler = nullptr;
  typedef std::remove_pointer<decltype(bdt_filler)>::type::float_type float_type;
  typedef std::remove_pointer<decltype(bdt_filler)>::type::int_type int_type;

  if ( selectBDT ) {
    bdt_filler = new std::remove_pointer<decltype(bdt_filler)>::type(
      makeHistManager_cfg(process_string, Form("%s/sel/evtntuple", histogramDir.data()), era_string, central_or_shift_main)
    );
    for(const std::string & evt_cat_str: evt_cat_strs)
    {
      //Book Weight_klScan
      bdt_filler->register_variable<float_type>(Form("weight_%s", evt_cat_str.c_str()) );
    }
    for(const std::string & evt_cat_str: BMS)
    {
      bdt_filler->register_variable<float_type>( Form("weight_%s", evt_cat_str.c_str()) );
    }
    bdt_filler->register_variable<float_type>(
      "lep_pt", "lep_conePt", "lep_eta",
      "bjet1_pt", "bjet1_eta",
      "bjet2_pt", "bjet2_eta",
      "met", "mht", "met_LD",
      "HT", "STMET",
      "m_Hbb", "m_Hbb_regCorr", "m_Hbb_regRes", "dR_Hbb", "dPhi_Hbb", "pT_Hbb", "eta_Hbb",
      //
      "m_Wjj", "dR_Wjj", "dPhi_Wjj", "pT_Wjj", "tau21_Wjj",
      "dR_Hww", "dPhi_Hww", "pT_Hww", "Smin_Hww",
      "dR_b1lep", "dR_b2lep",
      "m_HHvis", "pT_HHvis", "dPhi_HHvis",
      "m_HH", "m_HH_B2G_18_008", "pT_HH", "dPhi_HH", "Smin_HH",
      "mT_W", "mT_top_2particle", "mT_top_3particle",
      "m_HH_hme",
      "vbf_jet1_pt", "vbf_jet1_eta", "vbf_jet2_pt", "vbf_jet2_eta", "vbf_m_jj", "vbf_dEta_jj",
      "mem_maxWeight_signal", "mem_sumWeights_signal", "mem_avWeight_signal",
      "mem_maxWeight_background", "mem_sumWeights_background", "mem_avWeight_background",
      "mem_minLR", "mem_maxLR", "mem_avLR",
      "mem_maxWeight_signal_missingBJet", "mem_sumWeights_signal_missingBJet", "mem_avWeight_signal_missingBJet",
      "mem_maxWeight_background_missingBJet", "mem_sumWeights_background_missingBJet", "mem_avWeight_background_missingBJet",
      "mem_minLR_missingBJet", "mem_maxLR_missingBJet", "mem_avLR_missingBJet",
      "mem_maxWeight_signal_missingHadWJet", "mem_sumWeights_signal_missingHadWJet", "mem_avWeight_signal_missingHadWJet",
      "mem_maxWeight_background_missingHadWJet", "mem_sumWeights_background_missingHadWJet", "mem_avWeight_background_missingHadWJet",
      "mem_minLR_missingHadWJet", "mem_maxLR_missingHadWJet", "mem_avLR_missingHadWJet",
      "genWeight", "evtWeight",
      "mhh_gen", "costS_gen",
      "mindr_lep1_jet", "avg_dr_jet_central", "mbb_loose", "mbb_medium",
      "dR_HH", "mass_dist_HWW_Hbb",
      //
      "mWlep_simple",
      "pt_Wlep_simple",
      "eta_Wlep_simple",
      "dr_Wlep_lep_simple",
      //
      "mWjj_simple",
      "pt_Wjj_simple",
      "eta_Wjj_simple",
      "dr_Wj1_Wj2j_simple",
      //
      "mWW_simple",
      "pt_WW_simple",
      "eta_WW_simple",
      "dr_WW_simple",
      //
      "mHH_simple",
      "pt_HH_simple",
      "eta_HH_simple",
      "dr_HH_simple",
      "dr_HH_vis_simple",
      "mHH_vis_simple",
      //
      "dr_Wj1_b1_simple",
      "dr_Wj2_b1_simple",
      "dr_Wj1_b2_simple",
      "dr_Wj2_b2_simple",
      "dr_Wj1_lep_simple",
      "dr_Wj2_lep_simple",
      //
      "tau21_Hbb",
      "tau21_Wjj_simple",
      "mWW_vis_simple", "dr_Wjj_lep_simple",
      "m_Hbb_SF", "m_Wjj_SF_simple",
      "genDR_Wjj",  "genDR_Wlep", "gendr_Wj1_Wj2j_simple",  "genDR_Wlep_simple",
      //
      "mWlep_met_simple",
      "pt_Wlep_met_simple",
      "eta_Wlep_met_simple",
      "dr_Wlep_met_lep_simple",
      //
      "mWW_simple_met",
      "pt_WW_simple_met",
      "eta_WW_simple_met",
      "dr_WW_simple_met",
      //
      "cosThetaS_Hbb", "cosThetaS_Hbb_reg",
      "selJet1_Hbb_pT",  "selJet2_Hbb_pT", "selJet1_Hbb_eta", "selJet2_Hbb_eta",
      "cosThetaS_Wjj_simple", "cosThetaS_WW_simple", "cosThetaS_HH_simple", "cosThetaS_WW_simple_met",
      "cosThetaS_Wjj", "cosThetaS_WW", "cosThetaS_HH",
      "mHH_simple_met", "pt_HH_simple_met", "eta_HH_simple_met", "dr_HH_simple_met", "cosThetaS_HH_simple_met",
      "pt_Wj1_simple",  "pt_Wj2_simple",  "eta_Wj1_simple",  "eta_Wj2_simple"
    );
    bdt_filler->register_variable<int_type>(
      "lep_charge", "nElectron", "new_had_cut", "new_had_cut_fullreco", "original_jet_cut", "nJet_that_not_bb",
      "nJet", "nBJetLoose", "nBJetMedium", "numBJets_loose", "numBJets_medium",
      "isHbb_boosted", "isWjj_boosted", "isWjj_boosted_highPurity",
      "isWjj_boosted_simple", "isWjj_boosted_highPurity_simple",
      "nJet_vbf", "isVBF", "WjjWasFat",
      "nMEMOutputs", "nMEMOutputs_missingBJet", "nMEMOutputs_missingHadWJet",
      "isMatched_Wjj_simple", "isMatched_Wjj_fat_simple", "isMatched_Wlep_simple", "isMatched_Wjj", "isMatched_Wjj_fat", "isMatched_Wlep"
    );
    bdt_filler->bookTree(fs);
  }

  int analyzedEntries = 0;
  int selectedEntries = 0;
  double selectedEntries_weighted = 0.;
  std::map<std::string, int> selectedEntries_byGenMatchType; // key = process_and_genMatch
  std::map<std::string, std::map<std::string, double>> selectedEntries_weighted_byGenMatchType; // key = central_or_shift, process_and_genMatch
  TH1* histogram_analyzedEntries = fs.make<TH1D>("analyzedEntries", "analyzedEntries", 1, -0.5, +0.5);
  TH1* histogram_selectedEntries = fs.make<TH1D>("selectedEntries", "selectedEntries", 1, -0.5, +0.5);
  cutFlowTableType cutFlowTable;
  const edm::ParameterSet cutFlowTableCfg = makeHistManager_cfg(
    process_string, Form("%s/sel/cutFlow", histogramDir.data()), era_string, central_or_shift_main
  );
  //bool isDEBUG_TF = true;
  const std::vector<std::string> cuts = {
    "run:ls:event selection",
    "object multiplicity",
    "trigger",
    ">= 1 presel leptons",
    ">= 1 sel leptons",
    "electron pT > 32 GeV / muon pT > 25 GeV",
    "<= 1 tight leptons",
    "fakeable lepton trigger match",
    "HLT filter matching",
    "#jets to make Hbb and Wjj",
    ">= 2 jets from H->bb",
    ">= 1 medium b-jet",
    ">= 1 jets from W->jj",
    "tau veto",
    "m(ll) > 12 GeV",
    "Z-boson mass veto",
    "boosted W->jj: mD < 125 GeV",
    "boosted W->jj: pT_HWW/mHH > 0.3",
    "MEt filters",
    "signal region veto"
  };
  CutFlowTableHistManager * cutFlowHistManager = new CutFlowTableHistManager(cutFlowTableCfg, cuts);
  cutFlowHistManager->bookHistograms(fs);
  while ( inputTree->hasNextEvent() && (! run_lumi_eventSelector || (run_lumi_eventSelector && ! run_lumi_eventSelector -> areWeDone())) ) {
    if ( inputTree -> canReport(reportEvery) ) {
      std::cout << "processing Entry " << inputTree -> getCurrentMaxEventIdx()
                << " or " << inputTree -> getCurrentEventIdx() << " entry in #"
                << (inputTree -> getProcessedFileCount() - 1)
                << " (" << eventInfo
                << ") file (" << selectedEntries << " Entries selected)\n";
    }
    ++analyzedEntries;
    //if ( analyzedEntries > 1000) break;
    histogram_analyzedEntries->Fill(0.);

    if ( isDEBUG ) {
      std::cout << "event #" << inputTree -> getCurrentMaxEventIdx() << ' ' << eventInfo << '\n';
    }

    if ( run_lumi_eventSelector && !(*run_lumi_eventSelector)(eventInfo) ) continue;
    EvtWeightRecorderHH evtWeightRecorder(central_or_shifts_local, central_or_shift_main, isMC);
    cutFlowTable.update("run:ls:event selection", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("run:ls:event selection", evtWeightRecorder.get(central_or_shift_main));

    if ( run_lumi_eventSelector ) {
      std::cout << "processing Entry #" << inputTree->getCumulativeMaxEventCount() << ": " << eventInfo << std::endl;
      if ( inputTree -> isOpen() ) {
        std::cout << "input File = " << inputTree->getCurrentFileName() << std::endl;
      }
    }

    if(useObjectMultiplicity)
    {
      if(objectMultiplicity.getNRecoLepton(minLeptonSelection) < 1 ||
         objectMultiplicity.getNRecoLepton(kTight)             > 1  )
      {
        if(isDEBUG || run_lumi_eventSelector)
        {
          std::cout << "event " << eventInfo.str() << " FAILS preliminary object multiplicity cuts\n";
        }
        continue;
      }
    }
    cutFlowTable.update("object multiplicity", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("object multiplicity", evtWeightRecorder.get(central_or_shift_main));

//--- build collections of generator level particles (before any cuts are applied, to check distributions in unbiased event samples)
    std::vector<GenLepton> genLeptons;
    std::vector<GenLepton> genElectrons;
    std::vector<GenLepton> genMuons;
    std::vector<GenHadTau> genHadTaus;
    std::vector<GenPhoton> genPhotons;
    std::vector<GenJet> genJets;

    std::vector<GenParticle> muonGenMatch;
    std::vector<GenParticle> electronGenMatch;
    std::vector<GenParticle> hadTauGenMatch;
    std::vector<GenParticle> jetGenMatch;
    if(isMC && fillGenEvtHistograms)
    {
      if(genLeptonReader)
      {
        genLeptons = genLeptonReader->read();
        for(const GenLepton & genLepton: genLeptons)
        {
          const int abs_pdgId = std::abs(genLepton.pdgId());
          switch(abs_pdgId)
          {
            case 11: genElectrons.push_back(genLepton); break;
            case 13: genMuons.push_back(genLepton);     break;
            default: assert(0);
          }
        }
      }
      if(genHadTauReader) genHadTaus = genHadTauReader->read();
      if(genPhotonReader) genPhotons = genPhotonReader->read();
      if(genJetReader)    genJets = genJetReader->read();

      if(genMatchToMuonReader)     muonGenMatch = genMatchToMuonReader->read();
      if(genMatchToElectronReader) electronGenMatch = genMatchToElectronReader->read();
      if(genMatchToHadTauReader)   hadTauGenMatch = genMatchToHadTauReader->read();
      if(genMatchToJetReader)      jetGenMatch = genMatchToJetReader->read();

      if(isDEBUG)
      {
        printCollection("genLeptons", genLeptons);
        printCollection("genHadTaus", genHadTaus);
        printCollection("genJets", genJets);
      }
    }

    std::vector<GenParticle> genBJets;
    std::vector<GenParticle> genWBosons;
    std::vector<GenParticle> genWJets;
    if ( isMC ) {
      genBJets = genBJetReader->read();
      genWBosons = genWBosonReader->read();
      genWJets = genWJetReader->read();
    }

    if ( isDEBUG ) {
      dumpGenParticles("genBJet", genBJets);
      dumpGenParticles("genWBoson", genWBosons);
      dumpGenParticles("genWJet", genWJets);
    }

    if(isMC)
    {
      if(apply_genWeight)         evtWeightRecorder.record_genWeight(boost::math::sign(eventInfo.genWeight));
      if(eventWeightManager)      evtWeightRecorder.record_auxWeight(eventWeightManager);
      if(l1PreFiringWeightReader) evtWeightRecorder.record_l1PrefireWeight(l1PreFiringWeightReader);
      if(apply_topPtReweighting)  evtWeightRecorder.record_toppt_rwgt(eventInfo.topPtRwgtSF);
      lheInfoReader->read();
      psWeightReader->read();
      evtWeightRecorder.record_lheScaleWeight(lheInfoReader);
      evtWeightRecorder.record_psWeight(psWeightReader);
      evtWeightRecorder.record_puWeight(&eventInfo);
      evtWeightRecorder.record_nom_tH_weight(&eventInfo);
      evtWeightRecorder.record_lumiScale(lumiScale);
      for(const std::string & central_or_shift: central_or_shifts_local)
      {
        if(central_or_shift != central_or_shift_main)
        {
          continue;
        }
        genEvtHistManager_beforeCuts[central_or_shift]->fillHistograms(
          genElectrons, genMuons, genHadTaus, genPhotons, genJets, evtWeightRecorder.get_inclusive(central_or_shift)
        );
        if(eventWeightManager)
        {
          genEvtHistManager_beforeCuts[central_or_shift]->fillHistograms(
            eventWeightManager, evtWeightRecorder.get_inclusive(central_or_shift)
          );
        }
      }
    }

    bool isTriggered_1e = hltPaths_isTriggered(triggers_1e, triggerWhiteList, eventInfo, isMC);
    bool isTriggered_1mu = hltPaths_isTriggered(triggers_1mu, triggerWhiteList, eventInfo, isMC);

    bool selTrigger_1e = use_triggers_1e && isTriggered_1e;
    bool selTrigger_1mu = use_triggers_1mu && isTriggered_1mu;
    if ( !(selTrigger_1e || selTrigger_1mu) ) {
      if ( run_lumi_eventSelector ) {
	std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
        std::cout << " (selTrigger_1e = " << selTrigger_1e
                  << ", selTrigger_1mu = " << selTrigger_1mu << ")" << std::endl;
      }
      continue;
    }

//--- rank triggers by priority and ignore triggers of lower priority if a trigger of higher priority has fired for given event;
//    the ranking of the triggers is as follows: 1mu, 1e
// CV: this logic is necessary to avoid that the same event is selected multiple times when processing different primary datasets
    if ( !isMC && !isDEBUG ) {
      if ( selTrigger_1e && isTriggered_1mu ) {
        if ( run_lumi_eventSelector ) {
	  std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
          std::cout << " (selTrigger_1e = " << selTrigger_1e
                    << ", isTriggered_1mu = " << isTriggered_1mu << ")" << std::endl;
        }
        continue;
      }
    }
    cutFlowTable.update("trigger", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("trigger", evtWeightRecorder.get(central_or_shift_main));

    if ( (selTrigger_1e  && !apply_offline_e_trigger_cuts_1e)  ||
         (selTrigger_1mu && !apply_offline_e_trigger_cuts_1mu) ) {
      fakeableElectronSelector.disable_offline_e_trigger_cuts();
      tightElectronSelector.disable_offline_e_trigger_cuts();
    } else {
      tightElectronSelector.enable_offline_e_trigger_cuts();
      fakeableElectronSelector.enable_offline_e_trigger_cuts();
    }

//--- build collections of electrons, muons and hadronic taus;
//    resolve overlaps in order of priority: muon, electron,
    const std::vector<RecoMuon> muons = muonReader->read();
    const std::vector<const RecoMuon*> muon_ptrs = convert_to_ptrs(muons);
    const std::vector<const RecoMuon*> cleanedMuons = muon_ptrs; // CV: no cleaning needed for muons, as they have the highest priority in the overlap removal
    const std::vector<const RecoMuon*> preselMuons = preselMuonSelector(cleanedMuons, isHigherConePt);
    const std::vector<const RecoMuon*> fakeableMuons = fakeableMuonSelector(preselMuons, isHigherConePt);
    const std::vector<const RecoMuon*> tightMuons = tightMuonSelector(fakeableMuons, isHigherConePt);
    if ( isDEBUG || run_lumi_eventSelector ) {
      printCollection("preselMuons",   preselMuons);
      printCollection("fakeableMuons", fakeableMuons);
      printCollection("tightMuons",    tightMuons);
    }

    const std::vector<RecoElectron> electrons = electronReader->read();
    const std::vector<const RecoElectron*> electron_ptrs = convert_to_ptrs(electrons);
    const std::vector<const RecoElectron*> cleanedElectrons = electronCleaner(electron_ptrs, preselMuons);
    const std::vector<const RecoElectron*> preselElectrons = preselElectronSelector(cleanedElectrons, isHigherConePt);
    const std::vector<const RecoElectron*> preselElectronsUncleaned = preselElectronSelector(electron_ptrs, isHigherConePt);
    const std::vector<const RecoElectron*> fakeableElectrons = fakeableElectronSelector(preselElectrons, isHigherConePt);
    const std::vector<const RecoElectron*> tightElectrons = tightElectronSelector(fakeableElectrons, isHigherConePt);
    if ( isDEBUG || run_lumi_eventSelector ) {
      printCollection("preselElectrons",   preselElectrons);
      printCollection("preselElectronsUncleaned", preselElectronsUncleaned);
      printCollection("fakeableElectrons", fakeableElectrons);
      printCollection("tightElectrons",    tightElectrons);
    }

    const std::vector<const RecoLepton*> preselLeptonsFull = mergeLeptonCollections(preselElectrons, preselMuons, isHigherConePt);
    const std::vector<const RecoLepton*> preselLeptonsFullUncleaned = mergeLeptonCollections(preselElectronsUncleaned, preselMuons, isHigherConePt);
    const std::vector<const RecoLepton*> fakeableLeptonsFull = mergeLeptonCollections(fakeableElectrons, fakeableMuons, isHigherConePt);
    const std::vector<const RecoLepton*> tightLeptonsFull = mergeLeptonCollections(tightElectrons, tightMuons, isHigherConePt);

    const std::vector<const RecoLepton*> preselLeptons = pickFirstNobjects(preselLeptonsFull, 1);
    const std::vector<const RecoLepton*> fakeableLeptons = pickFirstNobjects(fakeableLeptonsFull, 1);
    const std::vector<const RecoLepton*> tightLeptons = getIntersection(fakeableLeptons, tightLeptonsFull, isHigherConePt);

    std::vector<const RecoLepton*> selLeptons;
    std::vector<const RecoMuon*> selMuons;
    std::vector<const RecoElectron*> selElectrons;
    if ( electronSelection == muonSelection ) {
      // for SR, flip region and fake CR
      // doesn't matter if we supply electronSelection or muonSelection here
      selLeptons = selectObjects(muonSelection, preselLeptons, fakeableLeptons, tightLeptons);
      selMuons = getIntersection(preselMuons, selLeptons, isHigherConePt);
      selElectrons = getIntersection(preselElectrons, selLeptons, isHigherConePt);
    } else {
      // for MC closure
      // make sure that neither electron nor muon selections are loose
      assert(electronSelection != kLoose && muonSelection != kLoose);
      selMuons = selectObjects(muonSelection, preselMuons, fakeableMuons, tightMuons);
      selElectrons = selectObjects(electronSelection, preselElectrons, fakeableElectrons, tightElectrons);
      const std::vector<const RecoLepton*> selLeptons_full = mergeLeptonCollections(selElectrons, selMuons, isHigherConePt);
      selLeptons = getIntersection(fakeableLeptons, selLeptons_full, isHigherConePt);
    }

    if ( isDEBUG || run_lumi_eventSelector ) {
      printCollection("selMuons", selMuons);
      printCollection("selElectrons", selElectrons);
      printCollection("selLeptons", selLeptons);
    }

    const std::vector<RecoHadTau> hadTaus = hadTauReader->read();
    const std::vector<const RecoHadTau*> hadTau_ptrs = convert_to_ptrs(hadTaus);
    const std::vector<const RecoHadTau*> cleanedHadTaus = hadTauCleaner(hadTau_ptrs, fakeableMuons, fakeableElectrons);
    // CV: veto events containing one or more taus, to avoid overlap with HH->bbWW single lepton channel
    const std::vector<const RecoHadTau*> vetoHadTaus = vetoHadTauSelector(cleanedHadTaus, isHigherPt);

//--- build collections of jets and select subset of jets passing b-tagging criteria
    const std::vector<RecoJet> jets_ak4 = jetReaderAK4->read();
    const std::vector<const RecoJet*> jet_ptrs_ak4 = convert_to_ptrs(jets_ak4);
    const std::vector<const RecoJet*> cleanedJetsAK4_wrtLeptons = jetCleaningByIndex ?
      jetCleanerAK4_byIndex(jet_ptrs_ak4, fakeableLeptons) :
      jetCleanerAK4_dR04   (jet_ptrs_ak4, fakeableLeptons)
    ;
    const std::vector<const RecoJet*> selJetsAK4 = jetSelectorAK4(cleanedJetsAK4_wrtLeptons, isHigherPt);
    const std::vector<const RecoJet*> selBJetsAK4_loose = jetSelectorAK4_bTagLoose(cleanedJetsAK4_wrtLeptons, isHigherPt);
    const std::vector<const RecoJet*> selBJetsAK4_medium = jetSelectorAK4_bTagMedium(cleanedJetsAK4_wrtLeptons, isHigherPt);

    if ( isDEBUG || run_lumi_eventSelector ) {
      printCollection("uncleaned AK4 jets", jet_ptrs_ak4);
      printCollection("cleaned AK4 jets(wrtLeptons)", cleanedJetsAK4_wrtLeptons);
      printCollection("selected AK4 jets", selJetsAK4);
    }

//--- build collections of generator level particles (after some cuts are applied, to save computing time)
    if(isMC && redoGenMatching && ! fillGenEvtHistograms)
    {
      if(genLeptonReader)
      {
        genLeptons = genLeptonReader->read();
        for(const GenLepton & genLepton: genLeptons)
        {
          const int abs_pdgId = std::abs(genLepton.pdgId());
          switch(abs_pdgId)
          {
            case 11: genElectrons.push_back(genLepton); break;
            case 13: genMuons.push_back(genLepton);     break;
            default: assert(0);
          }
        }
      }
      if(genHadTauReader) genHadTaus = genHadTauReader->read();
      if(genPhotonReader) genPhotons = genPhotonReader->read();
      if(genJetReader)    genJets = genJetReader->read();

      if(genMatchToMuonReader)     muonGenMatch = genMatchToMuonReader->read();
      if(genMatchToElectronReader) electronGenMatch = genMatchToElectronReader->read();
      if(genMatchToHadTauReader)   hadTauGenMatch = genMatchToHadTauReader->read();
      if(genMatchToJetReader)      jetGenMatch = genMatchToJetReader->read();
    }

//--- match reconstructed to generator level particles
    if(isMC && redoGenMatching)
    {
      if(genMatchingByIndex)
      {
        muonGenMatcher.addGenLeptonMatchByIndex(preselMuons, muonGenMatch, GenParticleType::kGenMuon);
        muonGenMatcher.addGenHadTauMatch       (preselMuons, genHadTaus);
        muonGenMatcher.addGenJetMatch          (preselMuons, genJets);

        electronGenMatcher.addGenLeptonMatchByIndex(preselElectrons, electronGenMatch, GenParticleType::kGenElectron);
        electronGenMatcher.addGenPhotonMatchByIndex(preselElectrons, electronGenMatch);
        electronGenMatcher.addGenHadTauMatch       (preselElectrons, genHadTaus);
        electronGenMatcher.addGenJetMatch          (preselElectrons, genJets);

        hadTauGenMatcher.addGenLeptonMatchByIndex(cleanedHadTaus, hadTauGenMatch, GenParticleType::kGenAnyLepton);
        hadTauGenMatcher.addGenHadTauMatch       (cleanedHadTaus, genHadTaus);
        hadTauGenMatcher.addGenJetMatch          (cleanedHadTaus, genJets);

        jetGenMatcherAK4.addGenLeptonMatch    (cleanedJetsAK4_wrtLeptons, genLeptons);
        jetGenMatcherAK4.addGenHadTauMatch    (cleanedJetsAK4_wrtLeptons, genHadTaus);
        jetGenMatcherAK4.addGenJetMatchByIndex(cleanedJetsAK4_wrtLeptons, jetGenMatch);
      }
      else
      {
        muonGenMatcher.addGenLeptonMatch(preselMuons, genMuons);
        muonGenMatcher.addGenHadTauMatch(preselMuons, genHadTaus);
        muonGenMatcher.addGenJetMatch   (preselMuons, genJets);

        electronGenMatcher.addGenLeptonMatch(preselElectrons, genElectrons);
        electronGenMatcher.addGenPhotonMatch(preselElectrons, genPhotons);
        electronGenMatcher.addGenHadTauMatch(preselElectrons, genHadTaus);
        electronGenMatcher.addGenJetMatch   (preselElectrons, genJets);

        hadTauGenMatcher.addGenLeptonMatch(cleanedHadTaus, genLeptons);
        hadTauGenMatcher.addGenHadTauMatch(cleanedHadTaus, genHadTaus);
        hadTauGenMatcher.addGenJetMatch   (cleanedHadTaus, genJets);

        jetGenMatcherAK4.addGenLeptonMatch(cleanedJetsAK4_wrtLeptons, genLeptons);
        jetGenMatcherAK4.addGenHadTauMatch(cleanedJetsAK4_wrtLeptons, genHadTaus);
        jetGenMatcherAK4.addGenJetMatch   (cleanedJetsAK4_wrtLeptons, genJets);
      }
    }

    // require at least one lepton passing loose preselection criteria
    if ( !(preselLeptonsFull.size() >= 1) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS preselLeptons selection." << std::endl;
        printCollection("preselLeptons", preselLeptonsFull);
      }
      continue;
    }
    cutFlowTable.update(">= 1 presel leptons", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(">= 1 presel leptons", evtWeightRecorder.get(central_or_shift_main));

    // require at least one lepton passing fakeable or tight selection criteria
    // (fakeable lepton selection applied in fake background control region,
    //  tight lepton selection applied in signal region)
    if ( !(selLeptons.size() >= 1) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS selLeptons selection." << std::endl;
        printCollection("selLeptons", selLeptons);
      }
      continue;
    }
    cutFlowTable.update(">= 1 sel leptons", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(">= 1 sel leptons", evtWeightRecorder.get(central_or_shift_main));
    const RecoLepton* selLepton = selLeptons[0];
    const Particle::LorentzVector& selLeptonP4 = selLepton->p4();
    int selLepton_type = getLeptonType(selLepton->pdgId());
    const leptonGenMatchEntry& selLepton_genMatch = getLeptonGenMatch(leptonGenMatch_definitions, selLepton);

    const double minPt_electron = 32.;
    const double minPt_muon = 25.;
    if ( !((selLepton->is_electron() && selLepton->cone_pt() > minPt_electron) || (selLepton->is_muon() && selLepton->cone_pt() > minPt_muon)) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS lepton pT selection." << std::endl;
        if      ( selLepton->is_electron() ) std::cout << " (selElectron pT = " << selLepton->pt() << ", minPt_electron = " << minPt_electron << ")" << std::endl;
        else if ( selLepton->is_muon()     ) std::cout << " (selMuon pT = " << selLepton->pt() << ", minPt_muon = " << minPt_muon << ")" << std::endl;
        else assert(0);
      }
      continue;
    }
    cutFlowTable.update(Form("electron pT > %f0.0 GeV / muon pT > %f0.0 GeV", minPt_electron, minPt_muon), evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("electron pT > 32 GeV / muon pT > 25 GeV", evtWeightRecorder.get(central_or_shift_main));

    // require exactly one lepton passing tight selection criteria, to avoid overlap with other channels
    if ( !(tightLeptonsFull.size() <= 1) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS tightLeptons selection." << std::endl;
        printCollection("tightLeptonsFull", tightLeptonsFull);
      }
      continue;
    }
    cutFlowTable.update("<= 1 tight leptons", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("<= 1 tight leptons", evtWeightRecorder.get(central_or_shift_main));

    // require that trigger paths match event category (with event category based on fakeableLeptons)
    if ( !((fakeableElectrons.size() >= 1 && selTrigger_1e) ||
           (fakeableMuons.size()     >= 1 && selTrigger_1mu)) ) {
      if ( run_lumi_eventSelector ) {
	std::cout << "event " << eventInfo.str() << " FAILS trigger selection for given fakeableLepton multiplicity." << std::endl;
        std::cout << " (#fakeableElectrons = " << fakeableElectrons.size()
                  << ", #fakeableMuons = " << fakeableMuons.size()
                  << ", selTrigger_1mu = " << selTrigger_1mu
                  << ", selTrigger_1e = " << selTrigger_1e << ")" << std::endl;
      }
      continue;
    }
    cutFlowTable.update("fakeable lepton trigger match", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("fakeable lepton trigger match", evtWeightRecorder.get(central_or_shift_main));

//--- apply HLT filter
    if ( apply_hlt_filter ) {
      const std::map<hltPathsE, bool> trigger_bits = {
        { hltPathsE::trigger_1e,  selTrigger_1e  },
        { hltPathsE::trigger_1mu, selTrigger_1mu },
      };
      if ( !hltFilter(trigger_bits, fakeableLeptons, {}) ) {
        if ( run_lumi_eventSelector || isDEBUG ) {
          std::cout << "event " << eventInfo.str() << " FAILS HLT filter matching\n";
        }
        continue;
      }
    }
    cutFlowTable.update("HLT filter matching", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("HLT filter matching", evtWeightRecorder.get(central_or_shift_main));

    if(isMC)
    {
//--- compute event-level weight for data/MC correction of b-tagging efficiency and mistag rate
//   (using the method "Event reweighting using scale factors calculated with a tag and probe method",
//    described on the BTV POG twiki https://twiki.cern.ch/twiki/bin/view/CMS/BTagShapeCalibration )
      evtWeightRecorder.record_btagWeight(selJetsAK4);
      if(btagSFRatioFacility)
      {
        evtWeightRecorder.record_btagSFRatio(btagSFRatioFacility, selJetsAK4.size());
      }

      if(isMC_EWK)
      {
        evtWeightRecorder.record_ewk_jet(selJetsAK4);
        evtWeightRecorder.record_ewk_bjet(selBJetsAK4_medium);
      }

      dataToMCcorrectionInterface->setLeptons(selLepton_type, selLepton->pt(), selLepton->cone_pt(), selLepton->eta());

//--- apply data/MC corrections for trigger efficiency
      evtWeightRecorder.record_leptonTriggerEff(dataToMCcorrectionInterface);

//--- apply data/MC corrections for efficiencies for lepton to pass loose identification and isolation criteria
      evtWeightRecorder.record_leptonIDSF_recoToLoose(dataToMCcorrectionInterface);

//--- apply data/MC corrections for efficiencies of leptons passing the loose identification and isolation criteria
//    to also pass the tight identification and isolation criteria
      if(electronSelection == kFakeable && muonSelection == kFakeable)
      {
        evtWeightRecorder.record_leptonSF(dataToMCcorrectionInterface->getSF_leptonID_and_Iso_fakeable_to_loose());
      }
      else if( electronSelection >= kFakeable && muonSelection >= kFakeable)
      {
        // apply loose-to-tight lepton ID SFs if either of the following is true:
        // 1) both electron and muon selections are tight -> corresponds to SR
        // 2) electron selection is relaxed to fakeable and muon selection is kept as tight -> corresponds to MC closure w/ relaxed e selection
        // 3) muon selection is relaxed to fakeable and electron selection is kept as tight -> corresponds to MC closure w/ relaxed mu selection
        // we allow (2) and (3) so that the MC closure regions would more compatible w/ the SR (1) in comparison
        evtWeightRecorder.record_leptonIDSF_looseToTight(dataToMCcorrectionInterface);
      }
    }

    bool passesTight_lepton = isMatched(*selLepton, tightElectrons) || isMatched(*selLepton, tightMuons);

    if ( leptonFakeRateInterface )
    {
      evtWeightRecorder.record_jetToLepton_FR_lead(leptonFakeRateInterface, selLepton);
    }

    if(applyFakeRateWeights == kFR_enabled)
    {
      evtWeightRecorder.compute_FR_1l(passesTight_lepton);
    }

    const std::vector<RecoJetAK8> jets_ak8 = jetReaderAK8->read();
    const std::vector<const RecoJetAK8*> jet_ptrs_ak8 = convert_to_ptrs(jets_ak8);
    const std::vector<RecoJetAK8> jets_ak8LS = jetReaderAK8LS->read();
    const std::vector<const RecoJetAK8*> jet_ptrs_ak8LS = convert_to_ptrs(jets_ak8LS);

    if ( isDEBUG || run_lumi_eventSelector ) {
      printCollection("uncleaned AK8 jets (Hbb)", jet_ptrs_ak8);
      printHbb(jet_ptrs_ak8, jetSelectorAK8_Hbb, genBJets);
      printCollection("uncleaned AK8LS jets (Wjj)", jet_ptrs_ak8LS);
      printWjj(jet_ptrs_ak8LS, jetSelectorAK8_Wjj, genWBosons, genWJets);
    }
    // make the AK8_LS collection here -- outside the Wjjreco function

    // select jets from H->bb decay
    const std::vector<const RecoJetAK8*> cleanedJetsAK8_wrtLeptons = jetCleanerAK8_dR08(jet_ptrs_ak8, fakeableLeptons);
    const std::vector<const RecoJetAK8*> selJetsAK8_Hbb = jetSelectorAK8_Hbb(cleanedJetsAK8_wrtLeptons, isHigherCSV_ak8);
    const std::vector<const RecoJetAK8*> selJetsAK8 = jetSelectorAK8(cleanedJetsAK8_wrtLeptons, isHigherPt);
    const std::vector<const RecoJet*> selJetsAK4_Hbb = jetSelectorAK4(cleanedJetsAK4_wrtLeptons, isHigherCSV);

    if ( !(selBJetsAK4_medium.size() >= 1 || selJetsAK8_Hbb.size() >=1 ) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS >= 1 medium b-jet selection\n";
      }
      continue;
    }
    cutFlowTable.update(">= 1 medium b-jet", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(">= 1 medium b-jet", evtWeightRecorder.get(central_or_shift_main));

    // preliminary jet selection to make Hbb possible
    if ( !((selJetsAK4.size() >= 2) || (selJetsAK8_Hbb.size() > 0))  ) {
      continue;
    }

    std::vector<selJetsType_Hbb> selJetsT_Hbb = selectJets_Hbb(selJetsAK8_Hbb, selJetsAK4_Hbb);
    const selJetsType_Hbb* selJetT_Hbb = nullptr;
    const RecoJetAK8* selJetAK8_Hbb = nullptr;
    const RecoJetBase* selJet1_Hbb = nullptr;
    const RecoJetBase* selJet2_Hbb = nullptr;
    double tau21_Hbb = -1.;
    double m_Hbb_SF = -1.;
    if ( selJetsT_Hbb.size() >= 1 )
    {
      selJetT_Hbb = &selJetsT_Hbb[0];
      selJetAK8_Hbb = selJetT_Hbb->fatjet_;
      selJet1_Hbb = selJetT_Hbb->jet_or_subjet1_;
      selJet2_Hbb = selJetT_Hbb->jet_or_subjet2_;
      if ( selJetAK8_Hbb )
      {
        tau21_Hbb = selJetAK8_Hbb->tau2()/selJetAK8_Hbb->tau1();
        m_Hbb_SF = selJetAK8_Hbb->msoftdrop();
      }
    }
    bool original_jet_cut = true;
    ///*
    // X: this should not be a cut -- there should be only a jet multiplicity cut
    if ( !(selJet1_Hbb && selJet2_Hbb) ) {
      std::cout << "event " << eventInfo.str() << " FAILS >= 2 jets from H->bb selection\n";
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS >= 2 jets from H->bb selection\n";
      }
      original_jet_cut = false;
    }
    cutFlowTable.update(">= 2 jets from H->bb", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(">= 2 jets from H->bb", evtWeightRecorder.get(central_or_shift_main));

    const double selJet1_Hbb_pT = selJet1_Hbb->pt();
    const double selJet2_Hbb_pT = selJet2_Hbb->pt();
    const double selJet1_Hbb_eta = selJet1_Hbb->eta();
    const double selJet2_Hbb_eta = selJet2_Hbb->eta();
    const double cosThetaS_Hbb = comp_cosThetaStar(selJet1_Hbb->p4(), selJet2_Hbb->p4());
    Particle::LorentzVector HbbP4 = selJet1_Hbb->p4() + selJet2_Hbb->p4();

    std::vector<const RecoJetBase*> selJets_Hbb = { selJet1_Hbb, selJet2_Hbb };
    std::sort(selJets_Hbb.begin(), selJets_Hbb.end(), isHigherPt);
    const RecoJetBase* selJet_Hbb_lead = selJets_Hbb[0];
    const Particle::LorentzVector& selJetP4_Hbb_lead = selJet_Hbb_lead->p4();
    const RecoJetBase* selJet_Hbb_sublead = selJets_Hbb[1];
    const Particle::LorentzVector& selJetP4_Hbb_sublead = selJet_Hbb_sublead->p4();

    int numBJets_loose, numBJets_medium;
    countBJetsJets_Hbb(*selJetT_Hbb, jetSelectorAK8_Hbb, jetSelectorAK4_bTagLoose, jetSelectorAK4_bTagMedium, numBJets_loose, numBJets_medium);

    double m_Hbb    = HbbP4.mass();
    double m_Hbb_regCorr = 0.;
    double m_Hbb_regRes  = 0.;
    double cosThetaS_Hbb_reg = -0.01;
    Particle::LorentzVector HbbP4_reg;
    if ( dynamic_cast<const RecoJet*>(selJet_Hbb_lead) && dynamic_cast<const RecoJet*>(selJet_Hbb_sublead) )
    {
      const RecoJet* selJetAK4_Hbb_lead    = dynamic_cast<const RecoJet*>(selJet_Hbb_lead);
      const RecoJet* selJetAK4_Hbb_sublead = dynamic_cast<const RecoJet*>(selJet_Hbb_sublead);
      HbbP4_reg = selJetAK4_Hbb_lead->p4()*selJetAK4_Hbb_lead->bRegCorr() + selJetAK4_Hbb_sublead->p4()*selJetAK4_Hbb_sublead->bRegCorr();
      cosThetaS_Hbb_reg = comp_cosThetaStar(selJetAK4_Hbb_lead->p4()*selJetAK4_Hbb_lead->bRegCorr(), selJetAK4_Hbb_sublead->p4()*selJetAK4_Hbb_sublead->bRegCorr());
      m_Hbb_regCorr = HbbP4_reg.mass();
      m_Hbb_regRes  = m_Hbb_regCorr*TMath::Sqrt(
         mem::square(selJetAK4_Hbb_lead->bRegRes()/selJetAK4_Hbb_lead->bRegCorr())
       + mem::square(selJetAK4_Hbb_sublead->bRegRes()/selJetAK4_Hbb_sublead->bRegCorr()));
    } else {
      HbbP4_reg = HbbP4;
      m_Hbb_regCorr = HbbP4.mass();
    }
    /////////////
    // X: have a minimal amount of jets to make Wjj
    std::vector<const RecoJet*> cleanedJetsAK4_wrtHbb;
    if ( selJetsAK8_Hbb.size() > 0 )
    {
      const RecoJetAK8 * jetFat = selJetsAK8_Hbb[0];
      cleanedJetsAK4_wrtHbb   = jetCleanerAK4_dR08(selJetsAK4, std::vector<const RecoJetBase*>({ jetFat }));
    } else {
      //cleanedJetsAK4_wrtHbb   = jetCleanerAK4_dR04(selJetsAK4, std::vector<const RecoJetBase*>({ selJet1_Hbb, selJet2_Hbb }));
      // the above was not effective in extremelly rare cases in if the initial selection is done only in jet multiplicity
      // I will assume that the selJetsAK4 objects are all isolated among them
      // and just make sure that I remove the AK4 that is the same in pt and eta
      for(auto jet1_it = selJetsAK4.begin(); jet1_it != selJetsAK4.end(); ++jet1_it)
      {
        const RecoJet * jet1 = *jet1_it;
        if ( !( (jet1->pt() == selJet1_Hbb->pt() && jet1->eta() == selJet1_Hbb->eta()) || (jet1->pt() == selJet2_Hbb->pt() && jet1->eta() == selJet2_Hbb->eta()) ) )
        {
          cleanedJetsAK4_wrtHbb.push_back( jet1 );
        }
      }
    }
    int nJet_that_not_bb = cleanedJetsAK4_wrtHbb.size();

    std::vector<const RecoJetAK8*> selJets_Wjj_boosted;
    if ( take_Wjj_boosted_from_AK8_LS || ! ignore_Wjj_boosted )
    {
      std::vector<const RecoJetAK8*> cleanedJetsAK8LS_wrtHbb;
      if ( jet_ptrs_ak8LS.size() > 0 )
      {
        if ( selJetAK8_Hbb ) {
          const std::vector<const RecoJetAK8*> overlaps = { selJetAK8_Hbb };
          cleanedJetsAK8LS_wrtHbb = jetCleanerAK8_dR16(jet_ptrs_ak8LS, overlaps); // CV: do *not* clean W->jj "fat" jet collection with respect to leptons!
        } else {
          cleanedJetsAK8LS_wrtHbb = jetCleanerAK8_dR12(jet_ptrs_ak8LS, std::vector<const RecoJetBase*>({ selJet1_Hbb, selJet2_Hbb }));
        }
        if ( selLepton )
        {
          jetSelectorAK8_Wjj.getSelector().set_lepton(selLepton);
          selJets_Wjj_boosted = jetSelectorAK8_Wjj(cleanedJetsAK8LS_wrtHbb, isHigherPt);
        }
        else
        {
          if ( isDEBUG )
          {
            std::cerr << "Warning in <selectJets_Wjj>: Cannot select AK8LS jets, as there is no lepton in the event !!" << std::endl;
          }
        }
      }
    } else if ( ! ignore_Wjj_boosted ) {
      // if AK8 to Wjj
      if ( selJetAK8_Hbb ) {
        // the bellow assures that is not the same object
        for(auto jet1_it = selJetsAK8.begin(); jet1_it != selJetsAK8.end(); ++jet1_it)
        {
          const RecoJetAK8 * jet1 = *jet1_it;
          if ( !( jet1->pt() == selJetAK8_Hbb->pt() && jet1->eta() == selJetAK8_Hbb->eta() ) )
          {
            selJets_Wjj_boosted.push_back( jet1 );
          }
        }
      } else {
        selJets_Wjj_boosted = jetCleanerAK8_dR08(selJetsAK8, std::vector<const RecoJetBase*>({ selJet1_Hbb, selJet2_Hbb }));
      }
    }

    bool new_had_cut = true;
    if ( !(
      ( selJetsAK8_Hbb.size() == 0   && selJets_Wjj_boosted.size() == 0 && selJetsAK4.size() >= 3 ) ||
      ( selJetsAK8_Hbb.size() >= 1   && selJets_Wjj_boosted.size() == 0 && nJet_that_not_bb >= 1 ) ||
      ( selJets_Wjj_boosted.size() >= 1 )
    )
    )
    {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS >= #jets to make Hbb and Wjj\n";
      }
      continue;
      new_had_cut = false;
    }

    bool new_had_cut_fullreco = true;
    if ( !(
      ( selJetsAK8_Hbb.size() == 0   && selJets_Wjj_boosted.size() == 0 && selJetsAK4.size() >= 4 ) ||
      ( selJetsAK8_Hbb.size() >= 1   && selJets_Wjj_boosted.size() == 0 && nJet_that_not_bb >= 2 ) ||
      ( selJets_Wjj_boosted.size() >= 1  )
    ))
    {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS >= #jets to make Hbb and Wjj\n";
      }
      new_had_cut_fullreco = false;
    }
    if ( isDEBUG )
    {
      std::cout << "event " << eventInfo.str() << " PASSES >= #jets to make Hbb and Wjj\n";
      std::cout << "selJetsAK4.size() " << selJetsAK4.size() << " \n";
      std::cout << "selJetsAK8_Hbb.size() " << selJetsAK8_Hbb.size() << " \n";
      std::cout << "nJet_that_not_bb " << nJet_that_not_bb << " \n";
      std::cout << "cleanedJetsAK4_wrtHbb.size() " << cleanedJetsAK4_wrtHbb.size() << " \n";
      std::cout << "selJets_Wjj_boosted.size() " << selJets_Wjj_boosted.size() << " \n";
    }

    cutFlowTable.update("#jets to make Hbb and Wjj", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("#jets to make Hbb and Wjj", evtWeightRecorder.get(central_or_shift_main));

    // select jets from W->jj decay
    const RecoJetAK8* selJetAK8_Wjj = nullptr;
    const RecoJetBase* selJet1_Wjj = nullptr; // to use with the evt-level BDT with reco Wjj-BDT method
    const RecoJetBase* selJet2_Wjj = nullptr; // to use with the evt-level BDT with reco Wjj-BDT method
    const RecoJetBase* selJet1_Hbb_4jet_assigment = nullptr; // to use with the evt-level BDT with reco Wjj-BDT method
    const RecoJetBase* selJet2_Hbb_4jet_assigment = nullptr; // to use with the evt-level BDT with reco Wjj-BDT method

    double tau21_Wjj_simple = -1.;
    double m_Wjj_SF_simple = -1.;
    const RecoJetBase* selJet1_Wjj_simple = nullptr; // to use with the evt-level BDT with reco Wjj-simple method
    const RecoJetBase* selJet2_Wjj_simple = nullptr; // to use with the evt-level BDT with reco Wjj-simple method
    double mass_dist_Wjj = 1000.;
    bool WjjWasFat = false;

    const RecoMEt met_uncorr = metReader->read();
    const RecoMEt met = recompute_met(met_uncorr, jets_ak4, met_option, isDEBUG);
    const Particle::LorentzVector& metP4 = met.p4();

    Particle::LorentzVector neutrinoP4_B2G_18_008;
    Particle::LorentzVector WlnuP4 = selLeptonP4 + neutrinoP4_B2G_18_008;
    // if AK8_LS to Wjj
    if ( selJets_Wjj_boosted.size() >= 1 )
    {
      selJetAK8_Wjj = selJets_Wjj_boosted[0];
      selJet1_Wjj = selJetAK8_Wjj->subJet1();
      selJet2_Wjj = selJetAK8_Wjj->subJet2();
      // to feed the evt-level BDT where the Wjj-resolved is done by a BDT

      tau21_Wjj_simple = selJetAK8_Wjj->tau2()/selJetAK8_Wjj->tau1();
      m_Wjj_SF_simple = selJetAK8_Wjj->msoftdrop();
      selJet1_Wjj_simple = selJetAK8_Wjj->subJet1();
      selJet2_Wjj_simple = selJetAK8_Wjj->subJet2();
      // to feed the evt-level BDT where the Wjj-resolved is done by a simple loop
      mass_dist_Wjj = std::abs((selJetAK8_Wjj->p4() + selLeptonP4 + metP4).mass() - m_Hbb_regCorr);

      neutrinoP4_B2G_18_008 = comp_metP4_B2G_18_008(selLeptonP4 + selJet1_Wjj->p4() + selJet2_Wjj->p4(), metP4.px(), metP4.py(), higgsBosonMass);
      WlnuP4 = selLeptonP4 + neutrinoP4_B2G_18_008;

      WjjWasFat = true;
    }

    // !fails_mD_cut && !fails_centrality_cut &&
    // compute cut on mD variable, defined by Eq.(3) in AN-2018/058 (v4) to define HP/LP
    bool fails_mD_cut = false;
    if ( selJetAK8_Wjj ) {
      Particle::LorentzVector WjjP4 = selJetAK8_Wjj->p4();
      double mD = deltaR(WjjP4, WlnuP4)*0.5*(WjjP4 + WlnuP4).pt();
      if ( !(mD <= higgsBosonMass) ) {
      	if ( run_lumi_eventSelector ) {
      	  std::cout << "event " << eventInfo.str() << " FAILS mD < 125 GeV selection\n";
      	}
      	fails_mD_cut = true;
      }
    }
    cutFlowTable.update("boosted W->jj: mD < 125 GeV selection", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("boosted W->jj: mD < 125 GeV selection", evtWeightRecorder.get(central_or_shift_main));

    // apply cut on event centrality variable, defined in Table 9 of AN-2018/058 (v4)
    bool fails_centrality_cut = false;
    if ( selJetAK8_Wjj ) {
      double pT_HWW = (selJetAK8_Wjj->p4() + selLepton->p4() + neutrinoP4_B2G_18_008).pt();
      double mHH = (selJetP4_Hbb_lead + selJetP4_Hbb_sublead + selJetAK8_Wjj->p4() + selLepton->p4() + neutrinoP4_B2G_18_008).mass();
      if ( !((pT_HWW/mHH) >= 0.3) ) {
      	if ( run_lumi_eventSelector ) {
      	  std::cout << "event " << eventInfo.str() << " FAILS pT_HWW/mHH > 0.3 selection\n";
      	}
      	fails_centrality_cut = true;
      }
    }
    cutFlowTable.update("boosted W->jj: pT_HWW/mHH > 0.3", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("boosted W->jj: pT_HWW/mHH > 0.3", evtWeightRecorder.get(central_or_shift_main));

    if ( fails_mD_cut || fails_centrality_cut )
    {
      WjjWasFat = false;
    }
    // up to here you defined if you have boosted or semi-boosted scenarios or resolved

    ///////////
    // put your other favourite method to reconstruct HERE

    ////////
    // take the resolved jets by the BDT
    if ( ! WjjWasFat )
    {
      // implement the 4-jet loop here
      if ( selJetsAK4.size() >= 4 && selJetsAK8_Hbb.size() == 0 ) // if resolved with 4 jets
      {
        double max_mvaOutput_4jet_assigment = -9.;
        bool   max_truth_4jet_assigment     = false;
        bool hadtruth = false;
        for ( std::vector<const RecoJet*>::const_iterator selBJet1 = selJetsAK4.begin(); selBJet1 != selJetsAK4.end(); ++selBJet1 ) {
          for ( std::vector<const RecoJet*>::const_iterator selBJet2 = selJetsAK4.begin(); selBJet2 != selJetsAK4.end(); ++selBJet2 ) {
            if ( &(*selBJet2) == &(*selBJet1) ) continue;
            for ( std::vector<const RecoJet*>::const_iterator selWJet1 = selJetsAK4.begin(); selWJet1 != selJetsAK4.end(); ++selWJet1 ) {
              if ( &(*selWJet1) == &(*selBJet1) ) continue;
              if ( &(*selWJet1) == &(*selBJet2) ) continue;
              for ( std::vector<const RecoJet*>::const_iterator selWJet2 = selJetsAK4.begin(); selWJet2 != selJetsAK4.end(); ++selWJet2 ) {
                if ( &(*selWJet2) == &(*selBJet1) ) continue;
                if ( &(*selWJet2) == &(*selBJet2) ) continue;
                if ( &(*selWJet2) == &(*selWJet1) ) continue;
                bool isGenMatched = false;
                /*std::map<std::string, double> mvaInputVariables_list_4jet_assigment = {
                  {"bjet1_btagCSV",    0.5}
                  {"bjet2_ptReg",      100.}
                  {"bjet2_btagCSV",    0.5}
                  {"bjet2_qgDiscr",    0.5}
                  {"wjet2_ptReg",      100.}
                  {"wjet2_qgDiscr",    0.5}
                  {"HadW_mass",        90.}
                  {"dR_HadW_lep",      0.6}
                  {"max_dR_HadW_bjet", 1.4}
                  {"dR_wjet1wjet2",    1.4}
                  {"mTop1",            180.}
                };*/
                const double bdtResult = 1.0; // xgbFileName_4jet_assigment(mvaInputVariables_list_4jet_assigment);
                isGenMatched = false; // test gen-matching in some way
                // check if there was an correct choice to chose
                if ( isGenMatched ) hadtruth = true;
                // save genpt of all options
                if ( bdtResult > max_mvaOutput_4jet_assigment ) {
                  // check if the correct choice was made
                  max_truth_4jet_assigment     = isGenMatched;
                  max_mvaOutput_4jet_assigment = bdtResult;

                  selJet1_Wjj = (*selWJet1);
                  selJet2_Wjj = (*selWJet1);
                  selJet1_Hbb_4jet_assigment = (*selBJet1);
                  selJet2_Hbb_4jet_assigment = (*selBJet2);

                }
              }
            }
          }
        }

        neutrinoP4_B2G_18_008 = comp_metP4_B2G_18_008(selLeptonP4 + selJet1_Wjj->p4() + selJet2_Wjj->p4(), metP4.px(), metP4.py(), higgsBosonMass);
      } else if ( selJetsAK8_Hbb.size() == 0 ) // if not Hbb boosted and missing jet
      {
        // put here the MVA for the 3-jet assigment, with similar loop
        // now it is just assuming that the Hbb jets are the Hbb as we defined and the thrird jet the Wj1
        selJet1_Hbb_4jet_assigment = selJet_Hbb_lead;
        selJet2_Hbb_4jet_assigment = selJet_Hbb_sublead;
        selJet1_Wjj = cleanedJetsAK4_wrtHbb[0];
        neutrinoP4_B2G_18_008 = comp_metP4_B2G_18_008(selLeptonP4 + selJet1_Wjj->p4(), metP4.px(), metP4.py(), higgsBosonMass);
        // just for the subsequent variables do not crash
        // one should not use the variables that use neutrinoP4_B2G_18_008 too be contructed on the missing jet case
      }
    }
    WlnuP4 = selLeptonP4 + neutrinoP4_B2G_18_008;

    // the bellow is just because we want the jwts on Wjj to be ordered by pT and the ones of selJets_Hbb_4jet_assigment by btag score
    std::vector<const RecoJetBase*> selJets_Wjj;
    if ( selJet1_Wjj ) selJets_Wjj.push_back(selJet1_Wjj);
    if ( selJet2_Wjj ) selJets_Wjj.push_back(selJet2_Wjj);
    std::sort(selJets_Wjj.begin(), selJets_Wjj.end(), isHigherPt);

    std::vector<const RecoJetBase*> selJets_Hbb_4jet_assigment;
    if ( selJet1_Hbb_4jet_assigment ) selJets_Hbb_4jet_assigment.push_back(selJet1_Hbb_4jet_assigment);
    if ( selJet2_Hbb_4jet_assigment ) selJets_Hbb_4jet_assigment.push_back(selJet2_Hbb_4jet_assigment);
    //std::sort(selJets_Hbb_4jet_assigment.begin(), selJets_Hbb_4jet_assigment.end(), isHigherCSV);

    const RecoJetBase* selJet_Wjj_lead = nullptr;
    Particle::LorentzVector selJetP4_Wjj_lead;
    const RecoJetBase* selJet_Wjj_sublead = nullptr;
    Particle::LorentzVector selJetP4_Wjj_sublead;
    if ( selJets_Wjj.size() >= 1 )
    {
      selJet_Wjj_lead = selJets_Wjj[0];
      selJetP4_Wjj_lead = selJet_Wjj_lead->p4();
      if ( selJets_Wjj.size() >= 2 ) {
        selJet_Wjj_sublead = selJets_Wjj[1];
        selJetP4_Wjj_sublead = selJet_Wjj_sublead->p4();
      }
    }

    const RecoJetBase* selJet_Hbb_4jet_assigment_lead = nullptr;
    Particle::LorentzVector selJetP4_Hbb_4jet_assigment_lead;
    const RecoJetBase* selJet_Hbb_4jet_assigment_sublead = nullptr;
    Particle::LorentzVector selJetP4_Hbb_4jet_assigment_sublead;
    if ( selJets_Hbb_4jet_assigment.size() >= 1 )
    {
      selJet_Hbb_4jet_assigment_lead = selJets_Hbb_4jet_assigment[0];
      selJetP4_Hbb_4jet_assigment_lead = selJet_Hbb_4jet_assigment_lead->p4();
      if ( selJets_Hbb_4jet_assigment.size() >= 2 ) {
        selJet_Hbb_4jet_assigment_sublead = selJets_Hbb_4jet_assigment[1];
        selJetP4_Hbb_4jet_assigment_sublead = selJet_Hbb_4jet_assigment_sublead->p4();
      }
    }

    // Using the result of the LBN instead
    // Here is a dumb filling to test the loading of the pb file to test it
    /*std::map<std::string, double> mvaInputVariables_list_LBN = {
      {"bjet1_btagCSV",    0.5}
      {"bjet2_ptReg",      100.}
      {"bjet2_btagCSV",    0.5}
      {"bjet2_qgDiscr",    0.5}
      {"wjet2_ptReg",      100.}
      {"wjet2_qgDiscr",    0.5}
      {"HadW_mass",        90.}
      {"dR_HadW_lep",      0.6}
      {"max_dR_HadW_bjet", 1.4}
      {"dR_wjet1wjet2",    1.4}
      {"mTop1",            180.}
    };
    std::map<std::string, double> mvaOutput_LBN = mva_LBN(mvaInputVariables_list_LBN);
   if ( isDEBUG_TF ) {
     std::cout << "event " << eventInfo.str() << "\n";
     std::cout << "Variables :\n";
     for(auto elem : vaInputVariables_list_LBN) std::cout << elem.first << " " << elem.second << "\n";
     std::cout << "\n";
     std::cout << "result :";
     for(auto elem : mvaOutput_LBN) std::cout << elem.first << " " << elem.second << " ";
     std::cout << "\n";
   }*/


    ///////////////////////////
    // take the resolved jets by the simple reco
    // simpler to compare -- it is just a simple loop
    // if there is a fat jet and it is not already tagged as Hbb
    // chose the two jets (ordered by pT, that are not the Hbb ones) with closest mass of the Hbb as the Wjj
    if ( ! WjjWasFat )
    {
      if ( ! new_had_cut_fullreco )
      {
        selJet1_Wjj_simple = cleanedJetsAK4_wrtHbb[0];
      } else {
        for(auto jet1_it = cleanedJetsAK4_wrtHbb.begin(); jet1_it != cleanedJetsAK4_wrtHbb.end(); ++jet1_it)
        {
          const RecoJetBase * jet1 = *jet1_it;
          if (mass_dist_Wjj == 1000.) selJet1_Wjj_simple = jet1;

          for(auto jet2_it = jet1_it + 1; jet2_it != cleanedJetsAK4_wrtHbb.end(); ++jet2_it)
          {
            const RecoJetBase * jet2 = *jet2_it;

            const double massdiff = std::abs((jet1->p4() + jet2->p4() + selLeptonP4 + metP4).mass() - m_Hbb_regCorr);

            if( massdiff < mass_dist_Wjj )
            {
              mass_dist_Wjj = massdiff;
              selJet1_Wjj_simple = jet1;
              selJet2_Wjj_simple = jet2;
            }
          }
        }
      }
    }
    //////////////
    // take_Wjj_boosted_with_B2G_sel
    /*
    if ( WjjWasFat && selJetAK8_Wjj )
    {
      // HT >= 400 GeV
      // veto events with medium btags outside the Hbb
      // tau21 <= 0.75
      // HWW statistic Dlvqq <= 11 -- check what it is and if that is possible
    }
    */

    // select VBF jet candidates
    //const std::vector<const RecoJet*> cleanedJetsAK4_wrtHbb = jetCleanerAK4_dR04(cleanedJetsAK4_wrtLeptons, std::vector<const RecoJetBase*>({ selJet1_Hbb, selJet2_Hbb }));
    std::vector<const RecoJet*> cleanedJetsAK4_vbf;
    if ( selJetAK8_Wjj ) {
      std::vector<const RecoJetAK8*> overlaps = { selJetAK8_Wjj };
      cleanedJetsAK4_vbf = jetCleanerAK4_dR12(cleanedJetsAK4_wrtHbb, overlaps);
    } else {
      cleanedJetsAK4_vbf = jetCleanerAK4_dR08(cleanedJetsAK4_wrtHbb, selJets_Wjj);
    }
    const std::vector<const RecoJet*> selJetsAK4_vbf = jetSelectorAK4_vbf(cleanedJetsAK4_vbf, isHigherPt);

    // CV: veto events containing one or more taus, to avoid overlap with HH->bbWW lepton+tau channel
    if ( apply_hadTauVeto ) {
      if ( vetoHadTaus.size() > 0 ) {
	if ( run_lumi_eventSelector ) {
	  std::cout << "event " << eventInfo.str() << " FAILS vetoHadTaus selection." << std::endl;
	  printCollection("vetoHadTaus", vetoHadTaus);
	}
	continue;
      }
    }
    cutFlowTable.update("tau veto", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("tau veto", evtWeightRecorder.get(central_or_shift_main));

    const bool failsLowMassVeto = isfailsLowMassVeto(preselLeptonsFullUncleaned);
    if ( failsLowMassVeto ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS low mass lepton pair veto." << std::endl;
      }
      continue;
    }
    cutFlowTable.update("m(ll) > 12 GeV", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("m(ll) > 12 GeV", evtWeightRecorder.get(central_or_shift_main));

    const bool failsZbosonMassVeto = isfailsZbosonMassVeto(preselLeptonsFull);
    if ( failsZbosonMassVeto ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS Z-boson veto." << std::endl;
      }
      continue;
    }
    cutFlowTable.update("Z-boson mass veto", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("Z-boson mass veto", evtWeightRecorder.get(central_or_shift_main));

//--- compute MHT and linear MET discriminant (met_LD)

    const std::vector<const RecoJet*> selJetsAK4_mht = jetSelectorAK4(cleanedJetsAK4_wrtLeptons, isHigherPt);
    Particle::LorentzVector mhtP4 = compMHT(fakeableLeptons, {}, selJetsAK4_mht);
    double met_LD = compMEt_LD(metP4, mhtP4);


    // compute HT and STMET variables used for signal extraction in EXO analyses
    std::vector<const RecoJetBase*> selJets_HT_and_STMET;
    selJets_HT_and_STMET.insert(selJets_HT_and_STMET.end(), selJets_Hbb.begin(), selJets_Hbb.end());
    selJets_HT_and_STMET.insert(selJets_HT_and_STMET.end(), selJets_Wjj.begin(), selJets_Wjj.end());
    double HT = compHT(fakeableLeptons, {}, selJets_HT_and_STMET);
    double STMET = compSTMEt(fakeableLeptons, {}, selJets_HT_and_STMET, met.p4());

    if ( apply_met_filters ) {
      if ( !metFilterSelector(metFilters) ) {
        if ( run_lumi_eventSelector ) {
	  std::cout << "event " << eventInfo.str() << " FAILS MEt filters." << std::endl;
        }
        continue;
      }
    }
    cutFlowTable.update("MEt filters", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("MEt filters", evtWeightRecorder.get(central_or_shift_main));

    bool failsSignalRegionVeto = false;
    if ( isMCClosure_e || isMCClosure_m ) {
      bool applySignalRegionVeto = (isMCClosure_e && countFakeElectrons(selLeptons) >= 1) || (isMCClosure_m && countFakeMuons(selLeptons) >= 1);
      if ( applySignalRegionVeto && tightLeptons.size() >= 1 ) failsSignalRegionVeto = true;
    } else if ( electronSelection == kFakeable || muonSelection == kFakeable ) {
      if ( tightLeptons.size() >= 1 ) failsSignalRegionVeto = true;
    }
    if ( failsSignalRegionVeto ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS overlap w/ the SR: "
	  "# tight leptons = " << tightLeptons.size() << " >= 2\n"
	;
        printCollection("tightLeptons", tightLeptons);
      }
      continue; // CV: avoid overlap with signal region
    }
    cutFlowTable.update("signal region veto", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("signal region veto", evtWeightRecorder.get(central_or_shift_main));

    std::vector<double> WeightBM; // weights to do histograms for BMs
    std::map<std::string, double> Weight_ktScan; // weights to do histograms

    std::map<std::string, double> WeightBM_toBDT; // weights to do histograms for BMs
    std::map<std::string, double> Weight_ktScan_toBDT; // weights to do histograms

    double HHWeight = 1.0; // X: for the SM point -- the point explicited on this code

    if(apply_HH_rwgt)
    {
      assert(HHWeight_calc);
      WeightBM = HHWeight_calc->getJHEPWeight(eventInfo.gen_mHH, eventInfo.gen_cosThetaStar, isDEBUG);
      Weight_ktScan = HHWeight_calc->getScanWeight(eventInfo.gen_mHH, eventInfo.gen_cosThetaStar, isDEBUG);
      HHWeight = WeightBM[0];
      evtWeightRecorder.record_bm(HHWeight); // SM by default

      for(std::size_t bm_list = 0; bm_list < WeightBM.size() ; ++bm_list)
      {
        std::string bench;
        if (bm_list == 0) bench = "SM";
        else {
          bench = Form("BM%s", std::to_string(bm_list).data() );
        }
        std::string name_BM = Form("weight_%s", bench.data() );
        WeightBM_toBDT[name_BM] =  WeightBM[bm_list];
        if (isDEBUG) std::cout << "line = " << name_BM << "; Weight = " << WeightBM[bm_list] << '\n';
      }
      for(std::size_t bm_list = 0; bm_list < evt_cat_strs.size() ; ++bm_list)
      {
        std::string bench = evt_cat_strs[bm_list].data();
        std::string name_BM = Form("weight_%s", bench.data() );
        Weight_ktScan_toBDT[name_BM] =  Weight_ktScan[bench];
        if (isDEBUG) std::cout << "line = " << name_BM << "; Weight = " << Weight_ktScan_toBDT[name_BM] << '\n';
      }

      if(isDEBUG)
      {
        std::cout << "mhh = " << eventInfo.gen_mHH          << " : "
          "cost "             << eventInfo.gen_cosThetaStar << " : "
          "weight = "         << HHWeight                   << '\n'
          ;
        std::cout << "Calculated " << Weight_ktScan.size() << " scan weights\n";
        for(std::size_t bm_list = 0; bm_list < Weight_ktScan.size(); ++bm_list)
        {
          std::cout << "line = " << bm_list << " " << evt_cat_strs[bm_list] << "; Weight = " <<  Weight_ktScan[evt_cat_strs[bm_list]] << '\n';
        }
        std::cout << '\n';
      }
    } else {
      for(std::size_t bm_list = 0; bm_list < BMS.size() ; ++bm_list)
      {
        std::string bench;
        if (bm_list == 0) bench = "SM";
        else {
          bench = Form("BM%s", std::to_string(bm_list).data() );
        }
        std::string name_BM = Form("weight_%s", bench.data() );
        WeightBM_toBDT[name_BM] =  1.0;
      }
      ////
      for(std::size_t bm_list = 0; bm_list < evt_cat_strs.size() ; ++bm_list)
      {
        std::string name_BM = Form("weight_%s", evt_cat_strs[bm_list].data() );
        Weight_ktScan_toBDT[name_BM] =  1.0;
      }
    }

    double dR_b1lep = deltaR(selJetP4_Hbb_lead, selLeptonP4);
    double dR_b2lep = deltaR(selJetP4_Hbb_sublead, selLeptonP4);

    ///////////////////////////////
    // compute signal extraction observables with BDT-Wjj based objects
    Particle::LorentzVector HbbP4_4jet_assigment = (selJetP4_Hbb_4jet_assigment_lead + selJetP4_Hbb_4jet_assigment_sublead);
    double dR_Hbb   = deltaR(selJetP4_Hbb_4jet_assigment_lead, selJetP4_Hbb_4jet_assigment_sublead);
    double dPhi_Hbb = TMath::Abs(deltaPhi(selJetP4_Hbb_4jet_assigment_lead.phi(), selJetP4_Hbb_4jet_assigment_sublead.phi())); // CV: map dPhi into interval [0..pi]
    double pT_Hbb   = HbbP4_4jet_assigment.pt();
    double eta_Hbb  = HbbP4_4jet_assigment.eta();
    Particle::LorentzVector WjjP4 = selJetP4_Wjj_lead + selJetP4_Wjj_sublead;
    double m_Wjj    = -1.;
    double dR_Wjj   = -1.;
    double dPhi_Wjj = -1.;
    double pT_Wjj   = -1.;
    double cosThetaS_Wjj = -0.01;
    if ( selJet_Wjj_lead && selJet_Wjj_sublead ) {
      cosThetaS_Wjj = comp_cosThetaStar(selJetP4_Wjj_lead, selJetP4_Wjj_sublead);
      m_Wjj    = WjjP4.mass();
      dR_Wjj   = deltaR(selJetP4_Wjj_lead, selJetP4_Wjj_sublead);
      dPhi_Wjj = TMath::Abs(deltaPhi(selJetP4_Wjj_lead.phi(), selJetP4_Wjj_sublead.phi()));
      pT_Wjj   = WjjP4.pt();
    }
    double tau21_Wjj = ( selJetAK8_Wjj ) ? selJetAK8_Wjj->tau2()/selJetAK8_Wjj->tau1() : -1.;
    double dR_Hww = deltaR(WjjP4, WlnuP4);
    double dPhi_Hww = TMath::Abs(deltaPhi(WjjP4.phi(), WlnuP4.phi()));
    double cosThetaS_WW = comp_cosThetaStar(WjjP4, WlnuP4);

    Particle::LorentzVector HwwP4 = WjjP4 + WlnuP4;
    double pT_Hww = HwwP4.pt();
    double Smin_Hww = comp_Smin(WjjP4 + selLeptonP4, metP4.px(), metP4.py());

    Particle::LorentzVector HHvisP4 = HbbP4_4jet_assigment + WjjP4 + selLeptonP4;
    double m_HHvis  = HHvisP4.mass();
    double pT_HHvis = HHvisP4.pt();
    double dPhi_HHvis = TMath::Abs(deltaPhi(HbbP4_4jet_assigment.phi(), (WjjP4 + selLeptonP4).phi()));
    Particle::LorentzVector HHP4_B2G_18_008 = HbbP4_4jet_assigment + WjjP4 + selLeptonP4 + neutrinoP4_B2G_18_008;
    Particle::LorentzVector HHP4 = HbbP4_4jet_assigment + WjjP4 + selLeptonP4 + metP4;
    double m_HH = HHP4.mass();
    double m_HH_B2G_18_008 = HHP4_B2G_18_008.mass();
    double pT_HH = HHP4.pt();
    double Smin_HH = comp_Smin(HHvisP4, metP4.px(), metP4.py());
    double dR_HH = deltaR(HbbP4_4jet_assigment, WjjP4 + selLeptonP4 + neutrinoP4_B2G_18_008);
    double dPhi_HH = TMath::Abs(deltaPhi(HbbP4_4jet_assigment.phi(), (WjjP4 + selLeptonP4 + metP4).phi()));
    double cosThetaS_HH = comp_cosThetaStar(HbbP4_4jet_assigment, WjjP4 + selLeptonP4 + metP4);

    // check gen-matching with 4jet_assigment reco based objects
    // add the chack for the Hbb_4jet_assigment part
    bool isMatched_Wjj = false;
    bool isMatched_Wjj_fat = false;
    bool isMatched_Wlep = false;
    double genDR_Wjj = 1000.;
    double genDR_Wlep = 1000.;
    for(auto jet1_it = genWBosons.begin(); jet1_it != genWBosons.end(); ++jet1_it)
    {
      const Particle::LorentzVector jet1 = jet1_it->p4();
      Particle::LorentzVector Wjj = selJetP4_Wjj_lead + selJetP4_Wjj_sublead;
      double DRgenWjj = deltaR(Wjj, jet1);
      double DRgenWlep = 1000.;
      if ( DRgenWjj < 0.8 ) isMatched_Wjj_fat = true;
      if ( DRgenWjj < 0.4 ) isMatched_Wjj = true;
      if ( DRgenWlep < 0.4 ) isMatched_Wlep = true;

      if ( DRgenWjj < genDR_Wjj ) genDR_Wjj = DRgenWjj;
      if ( DRgenWlep < genDR_Wlep ) genDR_Wlep = DRgenWlep;
    }

    ///////////////////////////////
    // compute signal extraction observables with simple-Wjj reco based objects
    Particle::LorentzVector Wjj_simple;
    double mWjj_simple = -1.;
    double pt_Wjj_simple = -1.;
    double pt_Wj1_simple = -1.;
    double pt_Wj2_simple = -1.;
    double eta_Wjj_simple = -100.;
    double eta_Wj1_simple = -100.;
    double eta_Wj2_simple = -100.;

    double dr_Wj1_b1_simple = -1.;
    double dr_Wj2_b1_simple = -1.;
    double dr_Wj1_b2_simple = -1.;
    double dr_Wj2_b2_simple = -1.;
    double dr_Wj1_lep_simple = -1.;
    double dr_Wj2_lep_simple = -1.;
    double dr_Wj1_Wj2j_simple  = -1.;
    if ( (selJet1_Wjj_simple && selJet2_Wjj_simple) )
    {
      Wjj_simple = selJet1_Wjj_simple->p4() + selJet2_Wjj_simple->p4();
      mWjj_simple = Wjj_simple.mass();
      pt_Wjj_simple = Wjj_simple.pt();
      eta_Wjj_simple = Wjj_simple.eta();
      dr_Wj1_Wj2j_simple = deltaR(selJet1_Wjj_simple->p4(), selJet2_Wjj_simple->p4());
      pt_Wj1_simple = selJet1_Wjj_simple->pt();
      pt_Wj2_simple = selJet2_Wjj_simple->pt();
      eta_Wj1_simple = selJet1_Wjj_simple->eta();
      eta_Wj2_simple =  selJet2_Wjj_simple->eta();
      //
      dr_Wj1_b1_simple = deltaR(selJet1_Wjj_simple->p4(), selJetP4_Hbb_lead);
      dr_Wj2_b1_simple = deltaR(selJet2_Wjj_simple->p4(), selJetP4_Hbb_lead);
      dr_Wj1_b2_simple = deltaR(selJet1_Wjj_simple->p4(), selJetP4_Hbb_sublead);
      dr_Wj2_b2_simple = deltaR(selJet2_Wjj_simple->p4(), selJetP4_Hbb_sublead);
      dr_Wj1_lep_simple = deltaR(selJet1_Wjj_simple->p4(), selLeptonP4);
      dr_Wj2_lep_simple = deltaR(selJet2_Wjj_simple->p4(), selLeptonP4);
    } else if ( selJet1_Wjj_simple )
    {
      pt_Wj1_simple = selJet1_Wjj_simple->pt();
      eta_Wj1_simple = selJet1_Wjj_simple->eta();
      //
      dr_Wj1_b1_simple = deltaR(selJet1_Wjj_simple->p4(), selJetP4_Hbb_lead);
      dr_Wj1_b2_simple = deltaR(selJet1_Wjj_simple->p4(), selJetP4_Hbb_sublead);
      dr_Wj1_lep_simple = deltaR(selJet1_Wjj_simple->p4(), selLeptonP4);
    }

    double mWlep_simple = -1.;
    double pt_Wlep_simple = -1.;
    double eta_Wlep_simple = -100.;
    double dr_Wlep_lep_simple = -100.;
    //
    double mWW_simple = -1.;
    double pt_WW_simple = -1.;
    double eta_WW_simple = -100.;
    double dr_WW_simple = -100.;
    double mWW_vis_simple = -1;
    double dr_Wjj_lep_simple = -100.;
    //
    double mHH_simple = -1.;
    double pt_HH_simple = -1.;
    double eta_HH_simple = -100;
    double dr_HH_simple = -100.;
    double dr_HH_vis_simple = -100.;
    double mHH_vis_simple = -1.;
    //
    double mHH_simple_met  = -1.;
    double pt_HH_simple_met  = -1.;
    double eta_HH_simple_met  = -100.;
    double dr_HH_simple_met  = -100.;
    double cosThetaS_HH_simple_met  = -0.01;
    //
    bool isMatched_Wjj_simple = false;
    bool isMatched_Wjj_fat_simple = false;
    bool isMatched_Wlep_simple = false;
    double gendr_Wj1_Wj2j_simple = 1000.;
    double genDR_Wlep_simple = 1000.;

    double mWlep_met_simple = -1.;
    double pt_Wlep_met_simple = -1.;
    double eta_Wlep_met_simple = -100.;
    double dr_Wlep_met_lep_simple;
    //
    double mWW_simple_met = -1.;
    double pt_WW_simple_met = -1.;
    double eta_WW_simple_met = -100.;
    double dr_WW_simple_met = -1.;

    double cosThetaS_Wjj_simple = -0.01;
    double cosThetaS_WW_simple  = -0.01;
    double cosThetaS_WW_simple_met = -0.01;
    double cosThetaS_HH_simple  = -0.01;

    Particle::LorentzVector neutrinoP4_B2G_18_008_simple = comp_metP4_B2G_18_008(selLeptonP4 + Wjj_simple, metP4.px(), metP4.py(), higgsBosonMass);
    Particle::LorentzVector Wlep_simple = selLeptonP4 + neutrinoP4_B2G_18_008_simple;
    mWlep_simple = Wlep_simple.mass();
    pt_Wlep_simple = Wlep_simple.pt();
    eta_Wlep_simple = Wlep_simple.eta();
    dr_Wlep_lep_simple = deltaR(Wlep_simple, selLeptonP4);
    //
    Particle::LorentzVector HWW_simple = Wjj_simple + Wlep_simple;
    mWW_simple = HWW_simple.mass();
    pt_WW_simple = HWW_simple.pt();
    eta_WW_simple = HWW_simple.eta();
    dr_WW_simple = deltaR(Wjj_simple, Wlep_simple);
    if ( selJet1_Wjj_simple && selJet2_Wjj_simple )
    {
      mWW_vis_simple = (Wjj_simple + selLeptonP4).mass();
      dr_Wjj_lep_simple = deltaR(selJet1_Wjj_simple->p4() + selJet2_Wjj_simple->p4(), selLeptonP4);
      cosThetaS_Wjj_simple = comp_cosThetaStar(selJet1_Wjj_simple->p4(), selJet2_Wjj_simple->p4());
      cosThetaS_WW_simple = comp_cosThetaStar(Wjj_simple, Wlep_simple);
      cosThetaS_WW_simple_met = comp_cosThetaStar(Wjj_simple, selLeptonP4 + metP4);
    } else if ( selJet1_Wjj_simple )
    {
      mWW_vis_simple = (selJet1_Wjj_simple->p4() + selLeptonP4).mass();
    }
    //
    Particle::LorentzVector HH_simple = HWW_simple + HbbP4_reg;
    mHH_simple = HH_simple.mass();
    pt_HH_simple = HH_simple.pt();
    eta_HH_simple = HH_simple.eta();
    dr_HH_simple = deltaR(HWW_simple, HbbP4_reg);
    if ( selJet1_Wjj_simple && selJet2_Wjj_simple )
    {
      mHH_vis_simple = (HbbP4_reg + Wjj_simple + selLeptonP4).mass();
      dr_HH_vis_simple = deltaR(Wjj_simple + selLeptonP4, HbbP4_reg);
    } else if (selJet1_Wjj_simple) {
      mHH_vis_simple = (HbbP4_reg + selJet1_Wjj_simple->p4() + selLeptonP4).mass();
      dr_HH_vis_simple = deltaR(selJet1_Wjj_simple->p4() + selLeptonP4, HbbP4_reg);
    }
    cosThetaS_HH_simple = comp_cosThetaStar(HWW_simple, HbbP4_reg);
    //
    // constructing stuff with MET instead
    Particle::LorentzVector Wlep_met_simple = selLeptonP4 + metP4;
    mWlep_met_simple = Wlep_simple.mass();
    pt_Wlep_met_simple = Wlep_simple.pt();
    eta_Wlep_met_simple = Wlep_simple.eta();
    dr_Wlep_met_lep_simple = deltaR(Wlep_met_simple, selLeptonP4);
    //
    Particle::LorentzVector HWW_met_simple = Wjj_simple + Wlep_met_simple;
    mWW_simple_met = HWW_met_simple.mass();
    pt_WW_simple_met = HWW_met_simple.pt();
    eta_WW_simple_met = HWW_met_simple.eta();
    dr_WW_simple_met = deltaR(Wjj_simple, Wlep_met_simple);
    //
    Particle::LorentzVector HHP4_simple_met = HbbP4_reg + Wjj_simple + Wlep_met_simple;
    mHH_simple_met = HHP4_simple_met.mass();
    pt_HH_simple_met = HHP4_simple_met.pt();
    eta_HH_simple_met = HHP4_simple_met.eta();
    dr_HH_simple_met = deltaR(HbbP4_reg, Wjj_simple + selLeptonP4 + metP4);
    cosThetaS_HH_simple_met = comp_cosThetaStar(HbbP4_reg, Wjj_simple + selLeptonP4 + metP4);
    // check gen-matching with simple-Wjj reco based objects
    for(auto jet1_it = genWBosons.begin(); jet1_it != genWBosons.end(); ++jet1_it)
    {
      const Particle::LorentzVector jet1 = jet1_it->p4();
      double DRgenWjj = deltaR(Wjj_simple, jet1);
      double DRgenWlep = deltaR(Wlep_simple, jet1);
      if ( DRgenWjj < 0.8 ) isMatched_Wjj_fat_simple = true;
      if ( DRgenWjj < 0.4 ) isMatched_Wjj_simple = true;
      if ( DRgenWlep < 0.4 ) isMatched_Wlep_simple = true;

      if ( DRgenWjj < gendr_Wj1_Wj2j_simple ) gendr_Wj1_Wj2j_simple = DRgenWjj;
      if ( DRgenWlep < genDR_Wlep_simple ) genDR_Wlep_simple = DRgenWlep;

    }

    // compute signal extraction observables that do nnot depend on Wjj reco
    //
    double mT_W = mT2_2particle::comp_mT(selLeptonP4.px(), selLeptonP4.py(), selLeptonP4.mass(), metP4.px(), metP4.py(), 0.);
    double mT_top_2particle_permutation1 = mT2_2particle::comp_mT(
      selJetP4_Hbb_lead.px(), selJetP4_Hbb_lead.py(), selJetP4_Hbb_lead.mass(),
      selLeptonP4.px() + metP4.px(), selLeptonP4.py() + metP4.py(), wBosonMass);
    double mT_top_2particle_permutation2 = mT2_2particle::comp_mT(
      selJetP4_Hbb_sublead.px(), selJetP4_Hbb_sublead.py(), selJetP4_Hbb_sublead.mass(),
      selLeptonP4.px() + metP4.px(), selLeptonP4.py() + metP4.py(), wBosonMass);
    //
    double mT_top_2particle = TMath::Min(mT_top_2particle_permutation1, mT_top_2particle_permutation2);
    double mT_top_3particle_permutation1 = mT2_3particle::comp_mT(
      selJetP4_Hbb_lead.px(), selJetP4_Hbb_lead.py(), selJetP4_Hbb_lead.mass(),
      selLeptonP4.px(), selLeptonP4.py(), selLeptonP4.mass(), metP4.px(), metP4.py(), 0.);
    double mT_top_3particle_permutation2 = mT2_3particle::comp_mT(
      selJetP4_Hbb_sublead.px(), selJetP4_Hbb_sublead.py(), selJetP4_Hbb_sublead.mass(),
      selLeptonP4.px(), selLeptonP4.py(), selLeptonP4.mass(), metP4.px(), metP4.py(), 0.);
    double mT_top_3particle = TMath::Min(mT_top_3particle_permutation1, mT_top_3particle_permutation2);

    double m_HH_hme = -1.; // CV: not implemented yet

    const RecoJet* selJet_vbf_lead = nullptr;
    const RecoJet* selJet_vbf_sublead = nullptr;
    double vbf_dEta_jj = -1.;
    double vbf_m_jj = -1.;
    bool isVBF = false;
    for ( std::vector<const RecoJet*>::const_iterator selJet1_vbf = selJetsAK4_vbf.begin();
          selJet1_vbf != selJetsAK4_vbf.end(); ++selJet1_vbf ) {
      for ( std::vector<const RecoJet*>::const_iterator selJet2_vbf = selJet1_vbf + 1;
	    selJet2_vbf != selJetsAK4_vbf.end(); ++selJet2_vbf ) {
	double dEta_jj = TMath::Abs((*selJet1_vbf)->eta() - (*selJet2_vbf)->eta());
	double m_jj = ((*selJet1_vbf)->p4() + (*selJet2_vbf)->p4()).mass();
	if ( dEta_jj > 4. && m_jj > 500. ) {
	  if ( m_jj > vbf_m_jj ) { // CV: in case of ambiguity, take the jet pair of highest mass
	    selJet_vbf_lead = (*selJet1_vbf);
	    selJet_vbf_sublead = (*selJet2_vbf);
	    vbf_dEta_jj = dEta_jj;
	    vbf_m_jj = m_jj;
	  }
	  isVBF = true;
	}
      }
    }
    double vbf_jet1_pt = -1.;
    double vbf_jet1_eta = 0.;
    if ( selJet_vbf_lead ) {
      vbf_jet1_pt = selJet_vbf_lead->pt();
      vbf_jet1_eta = selJet_vbf_lead->eta();
    }
    double vbf_jet2_pt = -1.;
    double vbf_jet2_eta = 0.;
    if ( selJet_vbf_sublead ) {
      vbf_jet2_pt = selJet_vbf_sublead->pt();
      vbf_jet2_eta = selJet_vbf_sublead->eta();
    }

    // computing event level BDTs
    double mindr_lep1_jet = comp_mindr_jet(*selLepton, selJetsAK4);
    std::map<std::string, double> mvaInputVariables_list = {
      {"nJet",                    selJetsAK4.size()},
      {"mindr_lep1_jet",          mindr_lep1_jet},
      {"m_Hbb_regCorr",           m_Hbb_regCorr},
      {"m_HH",                    m_HH},
      {"mWlep_met_simple",        mWlep_met_simple},
      {"dR_Hww",                  dR_Hww},
      {"m_Wjj",                   m_Wjj},
      {"cosThetaS_Hbb",           cosThetaS_Hbb},
      {"cosThetaS_Wjj",           cosThetaS_Wjj},
      {"cosThetaS_WW",            cosThetaS_WW},
      {"cosThetaS_HH",            cosThetaS_HH},
      {"nBJetMedium",             selBJetsAK4_medium.size()},
      {"dR_b1lep",                dR_b1lep},
      {"dR_b2lep",                dR_b2lep},
      {"lep_conePt",              comp_lep_conePt(*selLepton)},
      {"selJet1_Hbb_pT",          selJet1_Hbb_pT},
      {"selJet2_Hbb_pT",          selJet2_Hbb_pT},
      {"met_LD",                  met_LD},
      {"mT_W",                    mT_W},
      {"mT_top_3particle",        mT_top_3particle},
      {"HT",                      HT},
      {"mHH_simple_met",          mHH_simple_met},
      {"mWlep_met_simple",        mWlep_met_simple},
      {"mWW_simple_met",          mWW_simple_met},
      {"mWjj_simple",             mWjj_simple},
      {"cosThetaS_Wjj_simple",    cosThetaS_Wjj_simple},
      {"cosThetaS_WW_simple_met", cosThetaS_WW_simple_met},
      {"cosThetaS_HH_simple_met", cosThetaS_HH_simple_met},
      {"dr_Wj1_lep_simple",       dr_Wj1_lep_simple},
      {"dr_Wj2_lep_simple",       dr_Wj2_lep_simple}
    };
    //////
    double mvaoutput_bb1l_SM_Wj1                            = mva_xgb_bb1l_SM_Wj1(mvaInputVariables_list, eventInfo.event);
    double mvaoutput_bb1l_X900GeV_Wj1                       = mva_xgb_bb1l_X900GeV_Wj1(mvaInputVariables_list, eventInfo.event);

    double mvaoutput_bb1l_SM_Wjj_BDT_full_reco_only         = 1.0; //mva_xgb_bb1l_SM_Wjj_BDT_full_reco_only(mvaInputVariables_list, eventInfo.event);
    double mvaoutput_bb1l_X900GeV_Wjj_BDT_full_reco_only    = 1.0; //mva_xgb_bb1l_X900GeV_Wjj_BDT_full_reco_only(mvaInputVariables_list, eventInfo.event);

    double mvaoutput_bb1l_SM_Wjj_simple_full_reco_only      = mva_xgb_bb1l_SM_Wjj_simple_full_reco_only(mvaInputVariables_list, eventInfo.event);
    double mvaoutput_bb1l_X900GeV_Wjj_simple_full_reco_only = mva_xgb_bb1l_X900GeV_Wjj_simple_full_reco_only(mvaInputVariables_list, eventInfo.event);

    if (isDEBUG )  std::cout << "BDT outputs \n" <<
    "mvaoutput_bb1l_SM_Wj1 = " << mvaoutput_bb1l_SM_Wj1 << "; \n" <<
    "mvaoutput_bb1l_SM_Wjj_BDT_full_reco_only = " << mvaoutput_bb1l_SM_Wjj_BDT_full_reco_only << "; \n" <<
    "mvaoutput_bb1l_SM_Wjj_simple_full_reco_only = " << mvaoutput_bb1l_SM_Wjj_simple_full_reco_only << "; \n" <<
    "mvaoutput_bb1l_X900GeV_Wj1 = " << mvaoutput_bb1l_X900GeV_Wj1 << "; \n" <<
    "mvaoutput_bb1l_X900GeV_Wjj_BDT_full_reco_only = " << mvaoutput_bb1l_X900GeV_Wjj_BDT_full_reco_only << "; \n";

    // determining default value for BDT for cases that assume a different BDT for the missing jet case
    double output_SM_cat_jet_2BDT_Wjj_simple      = mvaoutput_bb1l_SM_Wjj_simple_full_reco_only;
    double output_X900GeV_cat_jet_2BDT_Wjj_simple = mvaoutput_bb1l_X900GeV_Wjj_simple_full_reco_only;

    double output_SM_cat_jet_2BDT_Wjj_BDT         = mvaoutput_bb1l_SM_Wjj_BDT_full_reco_only;
    double output_X900GeV_cat_jet_2BDT_Wjj_BDT    = mvaoutput_bb1l_X900GeV_Wjj_BDT_full_reco_only;

    ///////
    /// making the subcategories following Christian's fluxogram
    // _HbbFat_WjjFat_HP
    // _HbbFat_WjjFat_LP
    // _HbbFat_WjjRes_allReco
    // _HbbFat_WjjRes_MissWJet
    // _WjjFat_HP
    // _WjjFat_LP
    // _Res_allReco
    // _Res_MissWJet
    // _Res_MissBJet
    std::string category_mount    = "";
    if ( selJetAK8_Hbb )
    {
      category_mount       += "_HbbFat";
      if ( WjjWasFat && ! ignore_Wjj_boosted )
      {
        category_mount       += "_WjjFat";
        if ( !fails_mD_cut && !fails_centrality_cut && tau21_Wjj_simple < 0.55 )
        {
          category_mount += "_HP";
        } else {
          category_mount += "_LP";
        }
      } else {
        category_mount       += "_WjjRes";
        if ( selJet1_Wjj_simple && selJet2_Wjj_simple )
        {
          category_mount       += "_allReco";
        } else {
          category_mount       += "_MissWJet";
          // in the case of the missing W jet use the BDT made for this phase space
          output_SM_cat_jet_2BDT_Wjj_BDT         = mvaoutput_bb1l_SM_Wj1;
          output_SM_cat_jet_2BDT_Wjj_simple      = mvaoutput_bb1l_SM_Wj1;
          output_X900GeV_cat_jet_2BDT_Wjj_BDT    = mvaoutput_bb1l_X900GeV_Wj1;
          output_X900GeV_cat_jet_2BDT_Wjj_simple = mvaoutput_bb1l_X900GeV_Wj1;
        }
      }
    } else {
      if ( WjjWasFat && ! ignore_Wjj_boosted )
      {
        category_mount       += "_WjjFat";
        if ( !fails_mD_cut && !fails_centrality_cut && tau21_Wjj_simple < 0.55 )
        {
          category_mount += "_HP";
        } else {
          category_mount += "_LP";
        }
      } else {
        category_mount       += "_Res";
        // here I added the missing b-jet when the case -- now that will be empty
        if ( selJet1_Wjj_simple && selJet2_Wjj_simple && selJet1_Hbb && selJet2_Hbb)
        {
          category_mount       += "_allReco";
          if ( selBJetsAK4_medium.size() >= 2 )
          {
            category_mount       += "_2b";
          } else {
            category_mount       += "_1b";
          }
        } else if ( ! ( selJet1_Wjj_simple && selJet2_Wjj_simple ) )
        {
          category_mount       += "_MissWJet";
          if ( selBJetsAK4_medium.size() >= 1 )
          {
            category_mount       += "_2b";
          } else {
            category_mount       += "_1b";
          }
          // in the case of the missing W jet use the BDT made fpr this phase space
          output_SM_cat_jet_2BDT_Wjj_BDT         = mvaoutput_bb1l_SM_Wj1;
          output_SM_cat_jet_2BDT_Wjj_simple      = mvaoutput_bb1l_SM_Wj1;
          output_X900GeV_cat_jet_2BDT_Wjj_BDT    = mvaoutput_bb1l_X900GeV_Wj1;
          output_X900GeV_cat_jet_2BDT_Wjj_simple = mvaoutput_bb1l_X900GeV_Wj1;
        } else
        {
          // by now that will be always empty by deffition
          category_mount       += "_MissBJet";
        }
      }
    }
    //////////
    if ( selLepton_type == kElectron )
    {
      category_mount    += "_e";
    } else {
      category_mount    += "_m";
    }
    if ( isDEBUG ) std::cout << "category_mount = " << category_mount << std::endl;
    ////
    // Map  for variables to fill and naming conventions
    // the keys should coincide with for_categories_map (keys used for histogram booking)
    // -- like this for a resonant case or BM's case that can be added as a loop
    const std::map<std::string, double> categories_map_MVAs =
    {
      {"cat_jet_2BDT_Wjj_BDT_SM",         output_SM_cat_jet_2BDT_Wjj_BDT},
      {"cat_jet_2BDT_Wjj_simple_SM",      output_SM_cat_jet_2BDT_Wjj_simple},
      {"cat_jet_2BDT_Wjj_BDT_X900GeV",    output_X900GeV_cat_jet_2BDT_Wjj_BDT},
      {"cat_jet_2BDT_Wjj_simple_X900GeV", output_X900GeV_cat_jet_2BDT_Wjj_simple}
    };

    int numElectrons = ( selLepton_type == kElectron ) ?            1 : 0;
    int numMuons     = ( selLepton_type == kMuon     ) ?            1 : 0;
    int type_Hbb     = ( selJetAK8_Hbb               ) ? kHbb_boosted : kHbb_resolved;
    if ( isDEBUG ) {
      std::cout << "type_Hbb = " << type_Hbb << std::endl;
    }
    //////////////////////////////// !fails_mD_cut && !fails_centrality_cut && tau21_Wjj_simple < 0.55
    int type_Wjj     = kWjj_resolved;
    if ( selJetAK8_Wjj && !fails_mD_cut && !fails_centrality_cut ) {
      if ( (selJetAK8_Wjj->tau2()/selJetAK8_Wjj->tau1()) < 0.55 ) type_Wjj = kWjj_boosted_highPurity;
      else type_Wjj = kWjj_boosted_lowPurity;
    }
    if ( isDEBUG ) {
      std::cout << "type_Wjj = " << type_Wjj << std::endl;
      if ( selJetAK8_Wjj ) {
        std::cout << " (fails_mD_cut = " << fails_mD_cut << ","
                  << " fails_centrality_cut = " << fails_centrality_cut << ","
                  << " tau21 = " << selJetAK8_Wjj->tau2()/selJetAK8_Wjj->tau1() << ")" << std::endl;
      }
    }
    ////////////////////////////
    int type_Wjj_simple     = kWjj_resolved;
    if ( WjjWasFat && !fails_mD_cut && !fails_centrality_cut ) {
      if ( tau21_Wjj_simple < 0.55 ) type_Wjj_simple = kWjj_boosted_highPurity;
      else type_Wjj_simple = kWjj_boosted_lowPurity;
    }
    ///////////////////////////
    int type_vbf     = ( isVBF                       ) ?  kVBF_tagged : kVBF_nottagged;

    std::vector<MEMOutput_hh_bb1l> memOutputs_hh_bb1l;
    if ( memReader )
    {
      memOutputs_hh_bb1l = memReader->read();
    }
    std::vector<MEMOutput_hh_bb1l> memOutputs_hh_bb1l_missingBJet;
    if ( memReader_missingBJet )
    {
      memOutputs_hh_bb1l_missingBJet = memReader_missingBJet->read();
    }
    std::vector<MEMOutput_hh_bb1l> memOutputs_hh_bb1l_missingHadWJet;
    if ( memReader_missingHadWJet )
    {
      memOutputs_hh_bb1l_missingHadWJet = memReader_missingHadWJet->read();
    }

//--- retrieve gen-matching flags
    std::vector<const GenMatchEntry*> genMatches = genMatchInterface.getGenMatch(selLeptons);

//--- fill histograms with events passing final selection
    for(const std::string & central_or_shift: central_or_shifts_local)
    {
      const double evtWeight = evtWeightRecorder.get(central_or_shift);

      const bool skipFilling = central_or_shift != central_or_shift_main;
      std::map<std::string, double> rwgt_map;
      for(const std::string & evt_cat_str: evt_cat_strs)
      {
        if(skipFilling && evt_cat_str != default_cat_str)
        {
          continue;
        }
        if(apply_HH_rwgt)
        {
          rwgt_map[evt_cat_str] = evtWeight * Weight_ktScan[evt_cat_str] / HHWeight;
        }
        else
        {
          rwgt_map[evt_cat_str] = evtWeight;
        }
      }
      /*if(apply_HH_rwgt) {
        for(std::size_t bm_list = 0; bm_list < WeightBM.size() ; ++bm_list)
        {
          std::string bench;
          if (bm_list == 0) bench = "SM";
          else {
            bench = Form("BM%s", std::to_string(bm_list).data() );
          }
          rwgt_map[bench] = evtWeight * WeightBM[bm_list] / HHWeight;
        }
      }*/

      for (const GenMatchEntry* genMatch : genMatches)
      {
        selHistManagerType* selHistManager = selHistManagers[central_or_shift][genMatch->getIdx()];
        assert(selHistManager);
        if(! skipFilling)
        {
          selHistManager->electrons_->fillHistograms(selElectrons, evtWeight);
          selHistManager->muons_->fillHistograms(selMuons, evtWeight);
          selHistManager->jetsAK4_->fillHistograms(selJetsAK4, evtWeight);
          selHistManager->leadJetAK4_->fillHistograms(selJetsAK4, evtWeight);
          selHistManager->subleadJetAK4_->fillHistograms(selJetsAK4, evtWeight);
          if ( selJetAK8_Hbb ) {
            selHistManager->jetsAK8_Hbb_->fillHistograms({ selJetAK8_Hbb }, evtWeight);
          }
          if ( selJetAK8_Wjj ) {
            selHistManager->jetsAK8_Wjj_->fillHistograms({ selJetAK8_Wjj }, evtWeight);
          }
          selHistManager->BJetsAK4_loose_->fillHistograms(selBJetsAK4_loose, evtWeight);
          selHistManager->leadBJetAK4_loose_->fillHistograms(selBJetsAK4_loose, evtWeight);
          selHistManager->subleadBJetAK4_loose_->fillHistograms(selBJetsAK4_loose, evtWeight);
          selHistManager->BJetsAK4_medium_->fillHistograms(selBJetsAK4_medium, evtWeight);
          selHistManager->met_->fillHistograms(met, mhtP4, met_LD, evtWeight);
          selHistManager->metFilters_->fillHistograms(metFilters, evtWeight);
        }
        for(const auto & kv: rwgt_map)
        {
          selHistManager->evt_[kv.first]->fillHistograms(
            selElectrons.size(),
            selMuons.size(),
            selJetsAK4.size(),
            selBJetsAK4_loose.size(),
            selBJetsAK4_medium.size(),
            HT,
            STMET,
            m_Hbb, dR_Hbb, dPhi_Hbb, pT_Hbb,
            m_Wjj, dR_Wjj, dPhi_Wjj, pT_Wjj,
            dR_Hww, dPhi_Hww, pT_Hww, Smin_Hww,
            m_HHvis, m_HH, m_HH_B2G_18_008, m_HH_hme, dR_HH, dPhi_HH, pT_HH, Smin_HH,
            mT_W, mT_top_2particle, mT_top_3particle,
            vbf_jet1_pt, vbf_jet1_eta, vbf_jet2_pt, vbf_jet2_eta, vbf_m_jj, vbf_dEta_jj,
            nullptr, -1.,
            category_mount,
            categories_map_MVAs,
            selLepton->pt(), selLepton->eta(),
            selJetsAK4.size() > 0  ? selJetsAK4[0]->pt() : 0.,
            selJetsAK4.size() > 1  ? selJetsAK4[1]->pt() : 0.,
            selJetsAK4.size() > 0  ? selJetsAK4[0]->eta() : -10.,
            selJetsAK4.size() > 1  ? selJetsAK4[1]->eta() : -10.,
            doDataMCPlots,
            kv.second
          );
        }

        if(isMC && ! skipFilling)
        {
          selHistManager->genEvtHistManager_afterCuts_->fillHistograms(
            genElectrons, genMuons, genHadTaus, genPhotons, genJets, evtWeightRecorder.get_inclusive(central_or_shift)
          );
          selHistManager->lheInfoHistManager_afterCuts_->fillHistograms(*lheInfoReader, evtWeight);

          if(eventWeightManager)
          {
            selHistManager->genEvtHistManager_afterCuts_->fillHistograms(
              eventWeightManager, evtWeightRecorder.get_inclusive(central_or_shift)
            );
          }
        }
        if(! skipFilling)
        {
          selHistManager->evtYield_->fillHistograms(eventInfo, evtWeight);
          selHistManager->weights_->fillHistograms("genWeight", eventInfo.genWeight);
          selHistManager->weights_->fillHistograms("pileupWeight", evtWeightRecorder.get_puWeight(central_or_shift));
          selHistManager->weights_->fillHistograms("triggerWeight", evtWeightRecorder.get_sf_triggerEff(central_or_shift));
          selHistManager->weights_->fillHistograms("data_to_MC_correction", evtWeightRecorder.get_data_to_MC_correction(central_or_shift));
          selHistManager->weights_->fillHistograms("fakeRate", evtWeightRecorder.get_FR(central_or_shift));
        }

      }
    }

    if ( selEventsFile ) {
      (*selEventsFile) << eventInfo.run << ':' << eventInfo.lumi << ':' << eventInfo.event << '\n';
    }

    bool isGenMatched = false;
    if(isMC)
    {
      for (const GenMatchEntry * genMatch : genMatches)
      {
        if(genMatch->getName().empty())
        {
          isGenMatched = true; // non-fake
          break;
        }
      }
    }

    if ( bdt_filler ) {

      bdt_filler -> operator()({ eventInfo.run, eventInfo.lumi, eventInfo.event })
          ("lep_pt",                                   selLepton->pt())
          ("lep_conePt",                               comp_lep_conePt(*selLepton))
          ("lep_eta",                                  selLepton->eta())
          ("lep_charge",                               selLepton->charge())
          ("bjet1_pt",                                 selJetP4_Hbb_lead.pt())
          ("bjet1_eta",                                selJetP4_Hbb_lead.eta())
          ("bjet2_pt",                                 selJetP4_Hbb_sublead.pt())
          ("bjet2_eta",                                selJetP4_Hbb_sublead.eta())
          ("met",                                      metP4.pt())
          ("mht",                                      mhtP4.pt())
          ("met_LD",                                   met_LD)
          ("HT",                                       HT)
          ("STMET",                                    STMET)
          ("m_Hbb",                                    m_Hbb)
          ("m_Hbb_regCorr",                            m_Hbb_regCorr)
          ("m_Hbb_regRes",                             m_Hbb_regRes)
          ("dR_Hbb",                                   dR_Hbb)
          ("dPhi_Hbb",                                 dPhi_Hbb)
          ("pT_Hbb",                                   pT_Hbb)
          ("eta_Hbb",                                  eta_Hbb)
          ("m_Hbb_SF",                                 m_Hbb_SF)
          ("tau21_Hbb",                                tau21_Hbb)
          ("cosThetaS_Hbb",                            cosThetaS_Hbb)
          ("cosThetaS_Hbb_reg",                        cosThetaS_Hbb_reg)
          ("selJet1_Hbb_pT",                           selJet1_Hbb_pT)
          ("selJet2_Hbb_pT",                           selJet2_Hbb_pT)
          ("selJet1_Hbb_eta",                          selJet1_Hbb_eta)
          ("selJet2_Hbb_eta",                          selJet2_Hbb_eta)
          // done with BDT to reco Wjj
          ("m_Wjj",                                    m_Wjj)
          ("dR_Wjj",                                   dR_Wjj)
          ("dPhi_Wjj",                                 dPhi_Wjj)
          ("pT_Wjj",                                   pT_Wjj)
	        ("tau21_Wjj",                                tau21_Wjj)
          ("dR_Hww",                                   dR_Hww)
          ("dPhi_Hww",                                 dPhi_Hww)
          ("Smin_Hww",                                 Smin_Hww)
          ("pT_Hww",                                   pT_Hww)
          ("m_HHvis",                                  m_HHvis)
          ("pT_HHvis",                                 pT_HHvis)
          ("dPhi_HHvis",                               dPhi_HHvis)
          ("m_HH",                                     m_HH)
          ("m_HH_B2G_18_008",                          m_HH_B2G_18_008)
          ("pT_HH",                                    pT_HH)
          ("dPhi_HH",                                  dPhi_HH)
  	      ("Smin_HH",                                  Smin_HH)
          ("dR_HH",                                    dR_HH)
          ("isWjj_boosted",                            type_Wjj == kWjj_boosted_lowPurity || type_Wjj == kWjj_boosted_highPurity)
          ("isWjj_boosted_highPurity",                 type_Wjj == kWjj_boosted_highPurity)
          ("isMatched_Wjj",                            isMatched_Wjj)
          ("isMatched_Wjj_fat",                        isMatched_Wjj_fat)
          ("isMatched_Wlep",                           isMatched_Wlep)
          ("genDR_Wjj",                                genDR_Wjj)
          ("genDR_Wlep",                               genDR_Wlep)
          ("cosThetaS_Wjj",          cosThetaS_Wjj)
          ("cosThetaS_WW",           cosThetaS_WW)
          ("cosThetaS_HH",           cosThetaS_HH)
          // done with simple method
          ("mass_dist_HWW_Hbb",                        mass_dist_Wjj)
          //
          ("mWlep_simple",                             mWlep_simple)
          ("pt_Wlep_simple",                           pt_Wlep_simple)
          ("eta_Wlep_simple",                          eta_Wlep_simple)
          ("dr_Wlep_lep_simple",                       dr_Wlep_lep_simple)
          //
          ("mWjj_simple",                              mWjj_simple)
          ("pt_Wjj_simple",                            pt_Wjj_simple)
          ("eta_Wjj_simple",                           eta_Wjj_simple)
          ("dr_Wj1_Wj2j_simple",                       dr_Wj1_Wj2j_simple)
          ("pt_Wj1_simple",                            pt_Wj1_simple)
          ("pt_Wj2_simple",                            pt_Wj2_simple)
          ("eta_Wj1_simple",                           eta_Wj1_simple)
          ("eta_Wj2_simple",                           eta_Wj2_simple)
          //
          ("mWW_simple",                               mWW_simple)
          ("pt_WW_simple",                             pt_WW_simple)
          ("eta_WW_simple",                            eta_WW_simple)
          ("dr_WW_simple",                             dr_WW_simple)
          ("mWW_vis_simple",                           mWW_vis_simple)
          ("dr_Wjj_lep_simple",                        dr_Wjj_lep_simple)
          ("m_Wjj_SF_simple",                          m_Wjj_SF_simple)
          //
          ("mHH_simple",                               mHH_simple)
          ("pt_HH_simple",                             pt_HH_simple)
          ("eta_HH_simple",                            eta_HH_simple)
          ("dr_HH_simple",                             dr_HH_simple)
          ("dr_HH_vis_simple",                         dr_HH_vis_simple)
          ("mHH_vis_simple",                           mHH_vis_simple)
          //
          ("cosThetaS_Wjj_simple",   cosThetaS_Wjj_simple)
          ("cosThetaS_WW_simple",    cosThetaS_WW_simple)
          ("cosThetaS_WW_simple_met", cosThetaS_WW_simple_met)
          ("cosThetaS_HH_simple",    cosThetaS_HH_simple)
          ("mHH_simple_met",         mHH_simple_met)
          ("pt_HH_simple_met",       pt_HH_simple_met)
          ("eta_HH_simple_met",      eta_HH_simple_met)
          ("dr_HH_simple_met",       dr_HH_simple_met)
          ("cosThetaS_HH_simple_met", cosThetaS_HH_simple_met)
          //
          ("WjjWasFat",                                WjjWasFat)
          ("tau21_Wjj_simple",                         tau21_Wjj_simple)
          ("isWjj_boosted_simple",                     type_Wjj_simple == kWjj_boosted_lowPurity || type_Wjj_simple == kWjj_boosted_highPurity)
          ("isWjj_boosted_highPurity_simple",          type_Wjj_simple == kWjj_boosted_highPurity)
          ("isMatched_Wjj_simple",                     isMatched_Wjj_simple)
          ("isMatched_Wjj_fat_simple",                 isMatched_Wjj_fat_simple)
          ("isMatched_Wlep_simple",                    isMatched_Wlep_simple)
          ("gendr_Wj1_Wj2j_simple",                    gendr_Wj1_Wj2j_simple)
          ("genDR_Wlep_simple",                        genDR_Wlep_simple)
          //
          ("mWlep_met_simple",                          mWlep_met_simple)
          ("pt_Wlep_met_simple",                        pt_Wlep_met_simple)
          ("eta_Wlep_met_simple",                       eta_Wlep_met_simple)
          ("dr_Wlep_met_lep_simple",                    dr_Wlep_met_lep_simple)
          //
          ("mWW_simple_met",                            mWW_simple_met)
          ("pt_WW_simple_met",                          pt_WW_simple_met)
          ("eta_WW_simple_met",                         eta_WW_simple_met)
          ("dr_WW_simple_met",                          dr_WW_simple_met)
          //
          ("dr_Wj1_b1_simple",                          dr_Wj1_b1_simple)
          ("dr_Wj2_b1_simple",                          dr_Wj2_b1_simple)
          ("dr_Wj1_b2_simple",                          dr_Wj1_b2_simple)
          ("dr_Wj2_b2_simple",                          dr_Wj2_b2_simple)
          ("dr_Wj1_lep_simple",                         dr_Wj1_lep_simple)
          ("dr_Wj2_lep_simple",                         dr_Wj2_lep_simple)
          //
          ("dR_b1lep",                                 dR_b1lep)
          ("dR_b2lep",                                 dR_b2lep)
          //
          ("mT_W",                                     mT_W)
          ("mT_top_2particle",                         mT_top_2particle)
          ("mT_top_3particle",                         mT_top_3particle)
          ("m_HH_hme",                                 m_HH_hme)
      	  ("vbf_jet1_pt",                              vbf_jet1_pt)
          ("vbf_jet1_eta",                             vbf_jet1_eta)
          ("vbf_jet2_pt",                              vbf_jet2_pt)
	        ("vbf_jet2_eta",                             vbf_jet2_eta)
          ("vbf_dEta_jj",                              vbf_dEta_jj)
          ("vbf_m_jj",                                 vbf_m_jj)
          ("mem_maxWeight_signal",                     comp_mem_maxWeight(memOutputs_hh_bb1l, kSignal))
          ("mem_sumWeights_signal",                    comp_mem_sumWeights(memOutputs_hh_bb1l, kSignal))
          ("mem_avWeight_signal",                      comp_mem_avWeight(memOutputs_hh_bb1l, kSignal))
          ("mem_maxWeight_background",                 comp_mem_maxWeight(memOutputs_hh_bb1l, kBackground))
          ("mem_sumWeights_background",                comp_mem_sumWeights(memOutputs_hh_bb1l, kBackground))
          ("mem_avWeight_background",                  comp_mem_avWeight(memOutputs_hh_bb1l, kBackground))
          ("mem_minLR",                                comp_mem_minLR(memOutputs_hh_bb1l))
          ("mem_maxLR",                                comp_mem_maxLR(memOutputs_hh_bb1l))
          ("mem_avLR",                                 comp_mem_avLR(memOutputs_hh_bb1l))
          ("mem_maxWeight_signal_missingBJet",         comp_mem_maxWeight(memOutputs_hh_bb1l_missingBJet, kSignal))
          ("mem_sumWeights_signal_missingBJet",        comp_mem_sumWeights(memOutputs_hh_bb1l_missingBJet, kSignal))
          ("mem_avWeight_signal_missingBJet",          comp_mem_avWeight(memOutputs_hh_bb1l_missingBJet, kSignal))
          ("mem_maxWeight_background_missingBJet",     comp_mem_maxWeight(memOutputs_hh_bb1l_missingBJet, kBackground))
          ("mem_sumWeights_background_missingBJet",    comp_mem_sumWeights(memOutputs_hh_bb1l_missingBJet, kBackground))
          ("mem_avWeight_background_missingBJet",      comp_mem_avWeight(memOutputs_hh_bb1l_missingBJet, kBackground))
          ("mem_minLR_missingBJet",                    comp_mem_minLR(memOutputs_hh_bb1l_missingBJet))
          ("mem_maxLR_missingBJet",                    comp_mem_maxLR(memOutputs_hh_bb1l_missingBJet))
          ("mem_avLR_missingBJet",                     comp_mem_avLR(memOutputs_hh_bb1l_missingBJet))
          ("mem_maxWeight_signal_missingHadWJet",      comp_mem_maxWeight(memOutputs_hh_bb1l_missingHadWJet, kSignal))
          ("mem_sumWeights_signal_missingHadWJet",     comp_mem_sumWeights(memOutputs_hh_bb1l_missingHadWJet, kSignal))
          ("mem_avWeight_signal_missingHadWJet",       comp_mem_avWeight(memOutputs_hh_bb1l_missingHadWJet, kSignal))
          ("mem_maxWeight_background_missingHadWJet",  comp_mem_maxWeight(memOutputs_hh_bb1l_missingHadWJet, kBackground))
          ("mem_sumWeights_background_missingHadWJet", comp_mem_sumWeights(memOutputs_hh_bb1l_missingHadWJet, kBackground))
          ("mem_avWeight_background_missingHadWJet",   comp_mem_avWeight(memOutputs_hh_bb1l_missingHadWJet, kBackground))
          ("mem_minLR_missingHadWJet",                 comp_mem_minLR(memOutputs_hh_bb1l_missingHadWJet))
          ("mem_maxLR_missingHadWJet",                 comp_mem_maxLR(memOutputs_hh_bb1l_missingHadWJet))
          ("mem_avLR_missingHadWJet",                  comp_mem_avLR(memOutputs_hh_bb1l_missingHadWJet))
          ("genWeight",                                eventInfo.genWeight)
          ("evtWeight",                                evtWeightRecorder.get(central_or_shift_main))
          ("nJet",                                     comp_n_jet25_recl(selJetsAK4))
          ("nBJetLoose",                               selBJetsAK4_loose.size())
          ("nBJetMedium",                              selBJetsAK4_medium.size())
          ("nJet_vbf",                                 selJetsAK4_vbf.size())
          ("nJet_that_not_bb",                         nJet_that_not_bb)
	        ("isHbb_boosted",                            type_Hbb == kHbb_boosted)
          ("isVBF",                                    isVBF)
          ("nMEMOutputs",                              memOutputs_hh_bb1l.size())
          ("nMEMOutputs_missingBJet",                  memOutputs_hh_bb1l_missingBJet.size())
          ("nMEMOutputs_missingHadWJet",               memOutputs_hh_bb1l_missingHadWJet.size())
          ("mhh_gen",                                  eventInfo.gen_mHH)
          ("costS_gen",                                eventInfo.gen_cosThetaStar)
          /////
          ("mindr_lep1_jet",         mindr_lep1_jet )
          ("avg_dr_jet_central",     comp_avg_dr_jet(selJetsAK4))
          ("mbb_loose",              selBJetsAK4_loose.size()>1  ? (selBJetsAK4_loose[0]->p4()+selBJetsAK4_loose[1]->p4()).mass() : 0  )
          ("mbb_medium",             selBJetsAK4_medium.size()>1 ? (selBJetsAK4_medium[0]->p4()+selBJetsAK4_medium[1]->p4()).mass() : 0 )
          ("nElectron",              selElectrons.size())
          ("new_had_cut",             new_had_cut)
          ("new_had_cut_fullreco",    new_had_cut_fullreco)
          ("original_jet_cut",        original_jet_cut)
          ("numBJets_loose",          numBJets_loose)
          ("numBJets_medium",         numBJets_medium)
          //
          (WeightBM_toBDT)
          (Weight_ktScan_toBDT)
        .fill()
      ;
    }

    if(snm)
    {
      snm->read(eventInfo);
      snm->read({ triggers_1e, triggers_1mu });

      snm->read(preselMuons, fakeableMuons, tightMuons);
      snm->read(preselElectrons, fakeableElectrons, tightElectrons);
      //snm->read(selJetsAK4);
      std::vector<const RecoJetAK8*> tmpJetsAK8_Hbb;
      if ( selJetAK8_Hbb ) tmpJetsAK8_Hbb.push_back(selJetAK8_Hbb);
      snm->read(tmpJetsAK8_Hbb, false);
      std::vector<const RecoJetAK8*> tmpJetsAK8_Wjj;
      if ( selJetAK8_Wjj ) tmpJetsAK8_Wjj.push_back(selJetAK8_Wjj);
      snm->read(tmpJetsAK8_Wjj, true);

      const bool is_boosted = type_Hbb == kHbb_boosted && (type_Wjj == kWjj_resolved || type_Wjj == kWjj_boosted_highPurity);
      const bool is_semiboosted = type_Hbb == kHbb_boosted && type_Wjj == kWjj_resolved;
      const bool is_resolved = type_Hbb == kHbb_resolved && type_Wjj == kWjj_resolved;
      snm->read(is_boosted, is_semiboosted, is_resolved);

      const double leptonSF = evtWeightRecorder.get_leptonIDSF("central");
      const double triggerSF = evtWeightRecorder.get_sf_triggerEff("central");
      const double btagSF = evtWeightRecorder.get_btag("central");
      const double topPtWeight = evtWeightRecorder.get_toppt_rwgt("central");
      const double fakeRate = evtWeightRecorder.get_FR("central");
      const double l1Prefire = evtWeightRecorder.get_l1PreFiringWeight("central");
      const double leptonSF_recoToLoose = evtWeightRecorder.get_leptonIDSF_recoToLoose("central");
      const double leptonSF_looseToTight = evtWeightRecorder.get_leptonIDSF_looseToTight("central");

      snm->read(triggerSF,                              FloatVariableType_bbww::trigger_SF);
      snm->read(fakeRate,                               FloatVariableType_bbww::fakeRate);
      snm->read(leptonSF,                               FloatVariableType_bbww::lepton_IDSF);
      snm->read(btagSF,                                 FloatVariableType_bbww::btag_SF);
      snm->read(topPtWeight,                            FloatVariableType_bbww::topPt_wgt);
      snm->read(l1Prefire,                              FloatVariableType_bbww::L1prefire);
      snm->read(leptonSF_recoToLoose,                   FloatVariableType_bbww::lepton_IDSF_recoToLoose);
      snm->read(leptonSF_looseToTight,                  FloatVariableType_bbww::lepton_IDSF_looseToTight);
      snm->read(m_HH_hme,                               FloatVariableType_bbww::HME);
      snm->read(eventInfo.pileupWeight,                 FloatVariableType_bbww::PU_weight);
      snm->read(boost::math::sign(eventInfo.genWeight), FloatVariableType_bbww::MC_weight);
      snm->read(met.pt(),                               FloatVariableType_bbww::PFMET);
      snm->read(met.phi(),                              FloatVariableType_bbww::PFMETphi);

      if(isGenMatched)
      {
        snm->fill();
      }
      else
      {
        snm->resetBranches();
      }
    }

    ++selectedEntries;
    selectedEntries_weighted += evtWeightRecorder.get(central_or_shift_main);
    std::string process_and_genMatch = process_string;
    process_and_genMatch += selLepton_genMatch.name_;
    ++selectedEntries_byGenMatchType[process_and_genMatch];
    for(const std::string & central_or_shift: central_or_shifts_local)
    {
      selectedEntries_weighted_byGenMatchType[central_or_shift][process_and_genMatch] += evtWeightRecorder.get(central_or_shift);
    }
    histogram_selectedEntries->Fill(0.);
  }

  if(snm)
  {
    snm->write();
  }

  std::cout << "max num. Entries = " << inputTree -> getCumulativeMaxEventCount()
            << " (limited by " << maxEvents << ") processed in "
            << inputTree -> getProcessedFileCount() << " file(s) (out of "
            << inputTree -> getFileCount() << ")\n"
            << " analyzed = " << analyzedEntries << '\n'
            << " selected = " << selectedEntries << " (weighted = " << selectedEntries_weighted << ")\n\n"
            << "cut-flow table" << std::endl;
  cutFlowTable.print(std::cout);
  std::cout << std::endl;

  std::cout << "sel. Entries by gen. matching:" << std::endl;
  for(const std::string & central_or_shift: central_or_shifts_local)
  {
    std::cout << "central_or_shift = " << central_or_shift << '\n';
    for(const leptonGenMatchEntry & leptonGenMatch_definition: leptonGenMatch_definitions)
    {
      std::string process_and_genMatch = process_string;
      process_and_genMatch += leptonGenMatch_definition.name_;
      std::cout << " " << process_and_genMatch << " = " << selectedEntries_byGenMatchType[process_and_genMatch]
                << " (weighted = " << selectedEntries_weighted_byGenMatchType[central_or_shift][process_and_genMatch] << ")\n";
    }
  }
  std::cout << std::endl;

//--- manually write histograms to output file
  fs.file().cd();
  //histogram_analyzedEntries->Write();
  //histogram_selectedEntries->Write();
  HistManagerBase::writeHistograms();

//--- memory clean-up
  delete dataToMCcorrectionInterface;

  delete leptonFakeRateInterface;

  delete run_lumi_eventSelector;

  delete selEventsFile;

  delete muonReader;
  delete electronReader;
  delete jetReaderAK4;
  delete jetReaderAK8;
  if ( jetReaderAK8LS != jetReaderAK8 ) {
    delete jetReaderAK8LS;
  }
  delete metReader;
  delete metFilterReader;
  delete genLeptonReader;
  delete genHadTauReader;
  delete genPhotonReader;
  delete genJetReader;
  delete lheInfoReader;
  delete psWeightReader;

  for(auto & kv: genEvtHistManager_beforeCuts)
  {
    delete kv.second;
  }
  delete eventWeightManager;

  hltPaths_delete(triggers_1e);
  hltPaths_delete(triggers_1mu);

  delete inputTree;
  delete snm;

  clock.Show("analyze_hh_bb1l");

  return EXIT_SUCCESS;
}
