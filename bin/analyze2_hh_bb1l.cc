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
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetAK8.h" // RecoJetAK8
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
#include "tthAnalysis/HiggsToTauTau/interface/LHEParticleReader.h" // LHEParticleReader
#include "tthAnalysis/HiggsToTauTau/interface/LHEParticle.h" // LHEParticle
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
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetCollectionSelectorForward.h" // RecoJetSelectorForward
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
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // getBTagWeight_option, getHadTau_genPdgId, isHigherPt, isMatched, pileupJetID
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
#include "tthAnalysis/HiggsToTauTau/interface/DYMCReweighting.h" // DYMCReweighting
#include "tthAnalysis/HiggsToTauTau/interface/L1PreFiringWeightReader.h" // L1PreFiringWeightReader
#include "tthAnalysis/HiggsToTauTau/interface/cutFlowTable.h" // cutFlowTableType
#include "tthAnalysis/HiggsToTauTau/interface/NtupleFillerBDT.h" // NtupleFillerBDT
#include "tthAnalysis/HiggsToTauTau/interface/TTreeWrapper.h" // TTreeWrapper
#include "tthAnalysis/HiggsToTauTau/interface/hltFilter.h" // hltFilter()
#include "tthAnalysis/HiggsToTauTau/interface/EvtWeightManager.h" // EvtWeightManager
#include "tthAnalysis/HiggsToTauTau/interface/mT2_2particle.h" // mT2_2particle::comp_mT
#include "tthAnalysis/HiggsToTauTau/interface/mT2_3particle.h" // mT2_3particle::comp_mT
#include "tthAnalysis/HiggsToTauTau/interface/TMVAInterface.h" // TMVAInterface
#include "tthAnalysis/HiggsToTauTau/interface/TensorFlowInterfaceLBN.h" // TensorFlowInterfaceLBN
#include "tthAnalysis/HiggsToTauTau/interface/MVAInputVarHistManager.h" // MVAInputVarHistManager
#include "tthAnalysis/HiggsToTauTau/interface/HHWeightInterface2.h" // HHWeightInterface2
#include "tthAnalysis/HiggsToTauTau/interface/HHWeightInterfaceLOtoNLO.h" // HHWeightInterfaceLOtoNLO
#include "tthAnalysis/HiggsToTauTau/interface/DYMCNormScaleFactors.h" // DYMCNormScaleFactors 
#include "tthAnalysis/HiggsToTauTau/interface/BtagSFRatioFacility.h" // BtagSFRatioFacility
#include "tthAnalysis/HiggsToTauTau/interface/LHEParticle.h" // LHEParticle
#include "tthAnalysis/HiggsToTauTau/interface/RecoVertex.h" // RecoVertex
#include "tthAnalysis/HiggsToTauTau/interface/RecoVertexReader.h" // RecoVertexReader

#include "hhAnalysis/multilepton/interface/RecoJetCollectionSelectorAK8_hh_Wjj.h" // RecoJetSelectorAK8_hh_Wjj
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetCollectionSelectorAK8.h" // RecoJetSelectorAK8
#include "hhAnalysis/multilepton/interface/EvtWeightRecorderHH.h" // EvtWeightRecorderHH
#include "hhAnalysis/multilepton/interface/AnalysisConfig_hh.h" // AnalysisConfig_hh
#include "hhAnalysis/multilepton/interface/DatacardHistManager_hh.h" // DatacardHistManager_hh
#include "hhAnalysis/multilepton/interface/DatacardHistManager_hh_multiclass.h" // DatacardHistManager_hh_multiclass
#include "hhAnalysis/multilepton/interface/RecoElectronCollectionSelectorFakeable_hh_multilepton.h" // RecoElectronCollectionSelectorFakeable_hh_multilepton
#include "hhAnalysis/multilepton/interface/RecoMuonCollectionSelectorFakeable_hh_multilepton.h" // RecoMuonCollectionSelectorFakeable_hh_multilepton
#include "hhAnalysis/multilepton/interface/HHGenKinematicsHistManager.h"

#include "hhAnalysis/bbww/interface/EvtHistManager2_hh_bb1l.h" // EvtHistManager2_hh_bb1l
#include "hhAnalysis/bbww/interface/RecoJetCollectionSelectorAK8_hh_bbWW_Hbb.h" // RecoJetSelectorAK8_hh_bbWW_Hbb
#include "hhAnalysis/bbww/interface/MEMOutput_hh_bb1l.h" // MEMOutput_hh_bb1l
#include "hhAnalysis/bbww/interface/MEMOutputReader_hh_bb1l.h" // MEMOutputReader_hh_bb1l
#include "hhAnalysis/bbww/interface/JetPair.h" // initialize_mva_Wjj
#include "hhAnalysis/bbww/interface/jetSelectionAuxFunctions.h" // selectJets_Hbb, countBJetsJets_Hbb, selectJets_Wjj
#include "hhAnalysis/bbww/interface/SyncNtupleManager_bbww.h" // SyncNtupleManager_bbww
#include "hhAnalysis/bbww/interface/comp_metP4_B2G_18_008.h" // comp_metP4_B2G_18_008
#include "hhAnalysis/bbww/interface/BM_list.h" // BMS
#include "hhAnalysis/bbww/interface/GenParticleMatcherFromHiggs.h" // GenParticleMatcherFromHiggs
#include "hhAnalysis/bbww/interface/GenParticleMatcherFromTop.h" // GenParticleMatcherFromTop
#include "hhAnalysis/bbww/interface/genMatchingAuxFunctions.h" // isGenMatched 
#include "hhAnalysis/bbww/interface/JPAInterface.h" // JPA, JPAJet, JPAInterface
#include "hhAnalysis/bbww/interface/jpaAuxFunctions.h" // convert_to_JPAJet, convert_to_JPAJets, convert_to_RecoJet
#include "hhAnalysis/bbww/interface/EventCategory_hh_bb1l_BDT.h" // EventCategory_hh_bb1l_BDT
#include "hhAnalysis/bbww/interface/EventCategory_hh_bb1l_LBN.h" // EventCategory_hh_bb1l_LBN
#include "hhAnalysis/bbww/interface/analysisAuxFunctions_hh_bbWW.h" // makeTMVAInterface, makeTensorFlowInterfaceLBN, printHbb, printWjj
#include "hhAnalysis/bbww/interface/dumpGenParticles.h" // dumpGenParticles

#include <TBenchmark.h> // TBenchmark
#include <TString.h> // TString, Form
#include <TError.h> // gErrorAbortLevel, kError
#include <TRandom3.h> // TRandom3
#include <TROOT.h> // TROOT
#include <TH1.h>
#include <TH2.h>
#include <TProfile.h>
#include <boost/algorithm/string/predicate.hpp> // boost::starts_with()

#include <iostream> // std::cerr, std::fixed
#include <iomanip> // std::setprecision(), std::setw()
#include <string> // std::string
#include <vector> // std::vector<>
#include <cstdlib> // EXIT_SUCCESS, EXIT_FAILURE
#include <fstream> // std::ofstream
#include <assert.h> // assert
/*TH2D* h_genmatch = new TH2D("genmatch", "" , 7, 0.5,7.5, 7, 0.5, 7.5);
  TH2D* h_genmatchBoosted = new TH2D("genmatch_boosted", "" , 3, 0.5,3.5, 3, 0.5, 3.5);*/
typedef math::PtEtaPhiMLorentzVector LV;
typedef std::vector<std::string> vstring;
typedef std::vector<double> vdouble;

enum { kFR_disabled, kFR_enabled };

const int hadTauSelection_veto_antiElectron = -1; // not applied
const int hadTauSelection_veto_antiMuon = -1; // not applied

const double higgsBosonMass = 125.;

// CV: limit number of jets considered for building JPAs to avoid that a single noisy event can increase the number of JPAs by a lot
//    (for resolved events, the numbers of JPAs scales like numJets**4, while for boosted events, the number of JPA scales like numJets**2)
const int max_numJets = 50;

enum { kjpa_HbbBoosted_undefined, kjpa_HbbBoosted_2jet, kjpa_HbbBoosted_missingWJet, kjpa_HbbBoosted_restOfcat };
enum { kjpa_HbbResolved_undefined, kjpa_HbbResolved_4jet, kjpa_HbbResolved_missingWJet, kjpa_HbbResolved_missingBJet, kjpa_HbbResolved_missingAllWJet, 
       kjpa_HbbResolved_missingBJet_missingWJet, kjpa_HbbResolved_missingBJet_missingAllWJet, kjpa_HbbResolved_restOfcat };

std::pair<int, int> 
getMatchedJets(const std::vector<const RecoJet*>& cleanedJetsAK4_wrtLeptons, 
               const std::vector<const GenJet*>& genBJets_ptrs, 
               const std::vector<const GenJet*>& genWJets_ptrs,
	       bool Hbb_isBoosted = false) 
{
  int matchedBJet(0);
  int matchedWJet(0);
  for ( std::vector<const RecoJet*>::const_iterator selJet1 = cleanedJetsAK4_wrtLeptons.begin();
        selJet1 != cleanedJetsAK4_wrtLeptons.end(); ++selJet1 ) {
    if ( !Hbb_isBoosted && isGenMatched((*selJet1)->eta(), (*selJet1)->phi(), genBJets_ptrs) ) 
    {
      ++matchedBJet;
    }
    else if ( isGenMatched((*selJet1)->eta(), (*selJet1)->phi(), genWJets_ptrs) )
    {
      ++matchedWJet;
    }
  }
  return std::pair<int, int>(matchedBJet, matchedWJet);
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
  AnalysisConfig_hh analysisConfig("HH->bbWW", cfg_analyze);

  std::string treeName = cfg_analyze.getParameter<std::string>("treeName");

  std::string process_string = cfg_analyze.getParameter<std::string>("process");
  std::string process_string_hh = ( process_string.find("signal_") != std::string::npos ) ? cfg_analyze.getParameter<std::string>("process_hh") : "";
  bool isMC = cfg_analyze.getParameter<bool>("isMC");
  bool isSignal = analysisConfig.isMC_HH();
  bool isMC_tH  = analysisConfig.isMC_tH();
  bool isMC_ttH = analysisConfig.isMC_ttH();
  bool isMC_TT  = isMC && process_string.find("TT") != std::string::npos;

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

  const std::string apply_pileupJetID_string = cfg_analyze.getParameter<std::string>("apply_pileupJetID");
  const pileupJetID apply_pileupJetID = get_pileupJetID(apply_pileupJetID_string);

  vstring evtCategoryNames = cfg_analyze.getParameter<vstring>("evtCategories");
  std::cout << "evtCategories = " << format_vstring(evtCategoryNames) << std::endl;

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
  bool apply_DYMCReweighting = cfg_analyze.getParameter<bool>("apply_DYMCReweighting");
  bool apply_DYMCNormScaleFactors = cfg_analyze.getParameter<bool>("apply_DYMCNormScaleFactors");
  std::string apply_topPtReweighting_str = cfg_analyze.getParameter<std::string>("apply_topPtReweighting");
  bool apply_topPtReweighting = ! apply_topPtReweighting_str.empty();
  bool apply_hlt_filter = cfg_analyze.getParameter<bool>("apply_hlt_filter");
  bool apply_met_filters = cfg_analyze.getParameter<bool>("apply_met_filters");
  edm::ParameterSet cfgMEtFilter = cfg_analyze.getParameter<edm::ParameterSet>("cfgMEtFilter");
  MEtFilterSelector metFilterSelector(cfgMEtFilter, isMC);
  const bool useNonNominal = cfg_analyze.getParameter<bool>("useNonNominal");
  const bool useNonNominal_jetmet = useNonNominal || ! isMC;

  const double lep_mva_cut_mu = cfg_analyze.getParameter<double>("lep_mva_cut_mu");
  const double lep_mva_cut_e  = cfg_analyze.getParameter<double>("lep_mva_cut_e");
  const std::string lep_mva_wp = cfg_analyze.getParameter<std::string>("lep_mva_wp");

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

  DYMCReweighting* dyReweighting = nullptr;
  if(apply_DYMCReweighting)
  {
    dyReweighting = new DYMCReweighting(era);
  }
  DYMCNormScaleFactors * dyNormScaleFactors = nullptr;
  if(apply_DYMCNormScaleFactors)
  {
    dyNormScaleFactors = new DYMCNormScaleFactors(era);
  }
  edm::ParameterSet cfg_dataToMCcorrectionInterface;
  cfg_dataToMCcorrectionInterface.addParameter<std::string>("era", era_string);
  cfg_dataToMCcorrectionInterface.addParameter<std::string>("hadTauSelection", "disabled"); // CV: dummy value (no taus used in HH->bbWW channel)
  cfg_dataToMCcorrectionInterface.addParameter<int>("hadTauSelection_antiElectron", -1);
  cfg_dataToMCcorrectionInterface.addParameter<int>("hadTauSelection_antiMuon", -1);
  cfg_dataToMCcorrectionInterface.addParameter<std::string>("pileupJetID", apply_pileupJetID_string);
  cfg_dataToMCcorrectionInterface.addParameter<bool>("isDEBUG", isDEBUG);
  cfg_dataToMCcorrectionInterface.addParameter<std::string>("lep_mva_wp", lep_mva_wp);
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
    cfg_leptonFakeRateWeight.addParameter<bool>("debug", isDEBUG);
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
  std::string branchName_vertex = cfg_analyze.getParameter<std::string>("branchName_vertex");

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
  std::string branchName_genParticlesFromHiggs = cfg_analyze.getParameter<std::string>("branchName_genParticlesFromHiggs");
  std::string branchName_genWBosons = cfg_analyze.getParameter<std::string>("branchName_genWBosons");
  std::string branchName_genWJets = cfg_analyze.getParameter<std::string>("branchName_genWJets");
  std::string branchName_genWJetsFromTop = cfg_analyze.getParameter<std::string>("branchName_genWJetsFromTop");
  std::string branchName_genBJetsFromTop = cfg_analyze.getParameter<std::string>("branchName_genBJetsFromTop");

  bool selectBDT = ( cfg_analyze.exists("selectBDT") ) ? cfg_analyze.getParameter<bool>("selectBDT") : false;
  bool second_bdt = ( cfg_analyze.exists("secondBDT") ) ? cfg_analyze.getParameter<bool>("secondBDT") : false;

  std::vector<double> gen_mHH = analysisConfig.get_HH_resonant_mass_points();
  std::vector<double> nonRes_BMs = cfg_analyze.getParameter<std::vector<double>>("nonRes_BMs");

  bool fillHistograms_nonresonant = cfg_analyze.getParameter<bool>("fillHistograms_nonresonant");
  bool fillHistograms_resonant_spin0 = cfg_analyze.getParameter<bool>("fillHistograms_resonant_spin0");
  bool fillHistograms_resonant_spin2 = cfg_analyze.getParameter<bool>("fillHistograms_resonant_spin2");

  // initialize BDT-based signal extraction for resonant and non-resonant HH signal
  bool fillHistograms_BDT = cfg_analyze.getParameter<bool>("fillHistograms_BDT");
  std::vector<TMVAInterface *> BDT_resonant_spin2_boosted;//  = nullptr;
  std::vector<TMVAInterface *> BDT_resonant_spin2_resolved;// = nullptr;
  std::vector<TMVAInterface *> BDT_resonant_spin0_boosted;//  = nullptr;
  std::vector<TMVAInterface *> BDT_resonant_spin0_resolved;// = nullptr;
  std::vector<TMVAInterface *> BDT_nonresonant_boosted;//     = nullptr;
  std::vector<TMVAInterface *> BDT_nonresonant_resolved;//    = nullptr;
  if ( fillHistograms_BDT )
  {
    edm::ParameterSet cfg_BDT = cfg_analyze.getParameter<edm::ParameterSet>("BDT");

    edm::ParameterSet cfg_BDT_resonant_spin2_boosted = cfg_BDT.getParameter<edm::ParameterSet>("resonant_spin2_boosted");
    BDT_resonant_spin2_boosted = makeTMVAInterface(cfg_BDT_resonant_spin2_boosted, era_string, false);
    edm::ParameterSet cfg_BDT_resonant_spin2_resolved = cfg_BDT.getParameter<edm::ParameterSet>("resonant_spin2_resolved");
    BDT_resonant_spin2_resolved = makeTMVAInterface(cfg_BDT_resonant_spin2_resolved, era_string, false);

    edm::ParameterSet cfg_BDT_resonant_spin0_boosted = cfg_BDT.getParameter<edm::ParameterSet>("resonant_spin0_boosted");
    BDT_resonant_spin0_boosted = makeTMVAInterface(cfg_BDT_resonant_spin0_boosted, era_string, false);
    edm::ParameterSet cfg_BDT_resonant_spin0_resolved = cfg_BDT.getParameter<edm::ParameterSet>("resonant_spin0_resolved");
    BDT_resonant_spin0_resolved = makeTMVAInterface(cfg_BDT_resonant_spin0_resolved, era_string, false);

    edm::ParameterSet cfg_BDT_nonresonant_boosted = cfg_BDT.getParameter<edm::ParameterSet>("nonresonant_boosted");
    BDT_nonresonant_boosted = makeTMVAInterface(cfg_BDT_nonresonant_boosted, era_string, true);
    edm::ParameterSet cfg_BDT_nonresonant_resolved = cfg_BDT.getParameter<edm::ParameterSet>("nonresonant_resolved");
    BDT_nonresonant_resolved = makeTMVAInterface(cfg_BDT_nonresonant_resolved, era_string, true);
  }

  // initialize LBN-based signal extraction for resonant and non-resonant HH signal
  bool fillHistograms_LBN = cfg_analyze.getParameter<bool>("fillHistograms_LBN");
  std::vector<TensorFlowInterfaceLBN *> LBN_resonant_spin2_boosted;
  std::vector<TensorFlowInterfaceLBN *> LBN_resonant_spin2_resolved;
  std::vector<TensorFlowInterfaceLBN *> LBN_resonant_spin0_boosted;
  std::vector<TensorFlowInterfaceLBN *> LBN_resonant_spin0_resolved;
  std::vector<TensorFlowInterfaceLBN *> LBN_nonresonant_boosted;
  std::vector<TensorFlowInterfaceLBN *> LBN_nonresonant_resolved;
  if ( fillHistograms_LBN )
  {
    edm::ParameterSet cfg_LBN = cfg_analyze.getParameter<edm::ParameterSet>("LBN");

    edm::ParameterSet cfg_LBN_resonant_spin2_boosted = cfg_LBN.getParameter<edm::ParameterSet>("resonant_spin2_boosted");
    LBN_resonant_spin2_boosted = makeTensorFlowInterfaceLBN(cfg_LBN_resonant_spin2_boosted, era_string);
    edm::ParameterSet cfg_LBN_resonant_spin2_resolved = cfg_LBN.getParameter<edm::ParameterSet>("resonant_spin2_resolved");
    LBN_resonant_spin2_resolved = makeTensorFlowInterfaceLBN(cfg_LBN_resonant_spin2_resolved, era_string);

    edm::ParameterSet cfg_LBN_resonant_spin0_boosted = cfg_LBN.getParameter<edm::ParameterSet>("resonant_spin0_boosted");
    LBN_resonant_spin0_boosted = makeTensorFlowInterfaceLBN(cfg_LBN_resonant_spin0_boosted, era_string);
    edm::ParameterSet cfg_LBN_resonant_spin0_resolved = cfg_LBN.getParameter<edm::ParameterSet>("resonant_spin0_resolved");
    LBN_resonant_spin0_resolved = makeTensorFlowInterfaceLBN(cfg_LBN_resonant_spin0_resolved, era_string);

    edm::ParameterSet cfg_LBN_nonresonant_boosted = cfg_LBN.getParameter<edm::ParameterSet>("nonresonant_boosted");
    LBN_nonresonant_boosted = makeTensorFlowInterfaceLBN(cfg_LBN_nonresonant_boosted, era_string);
    edm::ParameterSet cfg_LBN_nonresonant_resolved = cfg_LBN.getParameter<edm::ParameterSet>("nonresonant_resolved");
    LBN_nonresonant_resolved = makeTensorFlowInterfaceLBN(cfg_LBN_nonresonant_resolved, era_string);
  }  

  std::string selEventsFileName_input = cfg_analyze.getParameter<std::string>("selEventsFileName_input");
  std::cout << "selEventsFileName_input = " << selEventsFileName_input << std::endl;
  GenParticleMatcherFromHiggs genParticleMatcherFromHiggs;
  GenParticleMatcherFromTop genParticleMatcherFromTop;

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
  EventInfo eventInfo(analysisConfig);
  if(isMC)
  {
    const double ref_genWeight = cfg_analyze.getParameter<double>("ref_genWeight");
    eventInfo.set_refGetWeight(ref_genWeight);
  }

//--- HH coupling scan
  std::vector<std::string> HHWeightNames;
  std::vector<std::string> HHBMNames;
  const edm::ParameterSet hhWeight_cfg = cfg_analyze.getParameterSet("hhWeight_cfg");
  const bool apply_HH_rwgt = analysisConfig.isHH_rwgt_allowed() && hhWeight_cfg.getParameter<bool>("apply_rwgt");
  const HHWeightInterface2* HHWeight_calc = nullptr;
  if(apply_HH_rwgt)
  {
    HHWeight_calc = new HHWeightInterface2(hhWeight_cfg);
    HHWeightNames = HHWeight_calc->get_weight_names();
    HHBMNames = HHWeight_calc->get_bm_names();
  }
  const bool apply_HH_rwgt_LOtoNLO = analysisConfig.isHH_rwgt_allowed() && hhWeight_cfg.getParameter<bool>("apply_rwgt_LOtoNLO");
  const HHWeightInterfaceLOtoNLO* HHWeight_calc_LOtoNLO = nullptr;
  if(apply_HH_rwgt_LOtoNLO)
  {
    HHWeight_calc_LOtoNLO = new HHWeightInterfaceLOtoNLO(10., isDEBUG);
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

  RecoVertex vertex;
  RecoVertexReader vertexReader(&vertex, branchName_vertex);
  inputTree -> registerReader(&vertexReader);

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
  LHEParticleReader* lheparticleReader = new LHEParticleReader();
  inputTree->registerReader(lheparticleReader);
  RecoMuonReader* muonReader = new RecoMuonReader(era, branchName_muons, isMC, readGenObjects);
  inputTree->registerReader(muonReader);
  RecoMuonCollectionGenMatcher muonGenMatcher;
  RecoMuonCollectionSelectorLoose preselMuonSelector(era, -1, isDEBUG);
  RecoMuonCollectionSelectorFakeable fakeableMuonSelector_default(era, -1, isDEBUG);
  RecoMuonCollectionSelectorFakeable_hh_multilepton fakeableMuonSelector_hh_multilepton(era, -1, isDEBUG);
  RecoMuonCollectionSelectorTight tightMuonSelector(era, -1, isDEBUG);
  fakeableMuonSelector_default.getSelector().set_assocJetBtag(useAssocJetBtag);
  fakeableMuonSelector_hh_multilepton.getSelector().set_assocJetBtag(useAssocJetBtag);
  tightMuonSelector.getSelector().set_assocJetBtag(useAssocJetBtag);
  muonReader->set_mvaTTH_wp(lep_mva_cut_mu);

  RecoElectronReader* electronReader = new RecoElectronReader(era, branchName_electrons, isMC, readGenObjects);
  inputTree->registerReader(electronReader);
  RecoElectronCollectionGenMatcher electronGenMatcher;
  RecoElectronCollectionCleaner electronCleaner(0.3, isDEBUG);
  RecoElectronCollectionSelectorLoose preselElectronSelector(era, -1, isDEBUG);
  RecoElectronCollectionSelectorFakeable fakeableElectronSelector_default(era, -1, isDEBUG);
  RecoElectronCollectionSelectorFakeable_hh_multilepton fakeableElectronSelector_hh_multilepton(era, -1, isDEBUG);
  RecoElectronCollectionSelectorTight tightElectronSelector(era, -1, isDEBUG);
  fakeableElectronSelector_default.getSelector().set_assocJetBtag(useAssocJetBtag);
  fakeableElectronSelector_hh_multilepton.getSelector().set_assocJetBtag(useAssocJetBtag);
  tightElectronSelector.getSelector().set_assocJetBtag(useAssocJetBtag);
  electronReader->set_mvaTTH_wp(lep_mva_cut_e);

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
  RecoJetCollectionSelector jetSelectorAK4_wPileupJetId(era, -1, isDEBUG);
  jetSelectorAK4_wPileupJetId.getSelector().set_pileupJetId(apply_pileupJetID);
  RecoJetCollectionSelector jetSelectorAK4_woPileupJetId(era, -1, isDEBUG);
  jetSelectorAK4_woPileupJetId.getSelector().set_pileupJetId(kPileupJetID_disabled);
  RecoJetCollectionSelector jetSelectorAK4_vbf(era, -1, isDEBUG);
  jetSelectorAK4_vbf.getSelector().set_min_pt(30.);
  jetSelectorAK4_vbf.getSelector().set_max_absEta(4.7);
  jetSelectorAK4_vbf.getSelector().set_pileupJetId(apply_pileupJetID);
  RecoJetCollectionSelector jetSelectorAK4_vbf_woPileupJetId(era, -1, isDEBUG);
  jetSelectorAK4_vbf_woPileupJetId.getSelector().set_min_pt(30.);
  jetSelectorAK4_vbf_woPileupJetId.getSelector().set_max_absEta(4.7);
  jetSelectorAK4_vbf_woPileupJetId.getSelector().set_pileupJetId(kPileupJetID_disabled);
  RecoJetCollectionSelectorBtagLoose jetSelectorAK4_bTagLoose(era, -1, isDEBUG);
  jetSelectorAK4_bTagLoose.getSelector().set_pileupJetId(apply_pileupJetID);
  RecoJetCollectionSelectorBtagMedium jetSelectorAK4_bTagMedium(era, -1, isDEBUG);
  jetSelectorAK4_bTagMedium.getSelector().set_pileupJetId(apply_pileupJetID);
  RecoJetCollectionSelectorForward jetSelectorForward(era, -1, isDEBUG);
  jetSelectorForward.getSelector().set_pileupJetId(apply_pileupJetID);

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

  GenParticleReader* genBJetReader = nullptr;
  GenParticleReader* genWBosonReader = nullptr;
  GenParticleReader* genWJetReader = nullptr;
  GenParticleReader* genParticleFromHiggsReader = nullptr;
  GenParticleReader* genBJetFromTopReader = nullptr;
  GenParticleReader* genWJetFromTopReader = nullptr;

  if ( isMC ) {
    genBJetReader = new GenParticleReader(branchName_genBJets);
    inputTree->registerReader(genBJetReader);
    genWBosonReader = new GenParticleReader(branchName_genWBosons);
    inputTree->registerReader(genWBosonReader);
    genWJetReader = new GenParticleReader(branchName_genWJets);
    inputTree->registerReader(genWJetReader);
  }

  if ( isSignal )
  {
    genParticleFromHiggsReader = new GenParticleReader(branchName_genParticlesFromHiggs);
    inputTree->registerReader(genParticleFromHiggsReader);
  }
  else if ( isMC_TT )
  {
    genBJetFromTopReader = new GenParticleReader(branchName_genBJetsFromTop);
    inputTree->registerReader(genBJetFromTopReader);
    genWJetFromTopReader = new GenParticleReader(branchName_genWJetsFromTop);
    inputTree->registerReader(genWJetFromTopReader);
  }

//--- declare missing transverse energy
  RecoMEtReader* metReader = new RecoMEtReader(era, isMC, branchName_met);
  metReader->setMEt_central_or_shift(met_option);
  metReader->set_phiModulationCorrDetails(&eventInfo, &vertex);
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

  if ( isMC )
  {
    if ( !readGenObjects )
    {
      genLeptonReader = new GenLeptonReader(branchName_genLeptons);
      inputTree->registerReader(genLeptonReader);
      genHadTauReader = new GenHadTauReader(branchName_genHadTaus);
      inputTree->registerReader(genHadTauReader);
      genJetReader = new GenJetReader(branchName_genJets);
      inputTree->registerReader(genJetReader);

      if ( genMatchingByIndex )
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

  JPAInterface jpaInterface("hhAnalysis/bbww/data/BDT_hh_bb1l", era_string);

//--- open output file containing run:lumi:event numbers of events passing final event selection criteria
  std::ostream* selEventsFile = ( selEventsFileName_output != "" ) ? new std::ofstream(selEventsFileName_output.data(), std::ios::out) : 0;
  std::cout << "selEventsFileName_output = " << selEventsFileName_output << std::endl;

//--- declare histograms
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
    EvtHistManager2_hh_bb1l* evt_;
    HHGenKinematicsHistManager* genKinematics_HH_;
    DatacardHistManager_hh* datacard_BDT_;
    DatacardHistManager_hh_multiclass* datacard_LBN_;
    EvtYieldHistManager* evtYield_;
    WeightHistManager* weights_;
  };

  EventCategory_hh_bb1l_BDT eventCategory_BDT;
  EventCategory_hh_bb1l_LBN eventCategory_LBN;

  std::map<std::string, GenEvtHistManager*> genEvtHistManager_beforeCuts;
  std::map<std::string, GenEvtHistManager*> genEvtHistManager_afterCuts;
  std::map<std::string, LHEInfoHistManager*> lheInfoHistManager;
  std::map<std::string, std::map<int, selHistManagerType*>> selHistManagers;
  for ( const std::string & central_or_shift: central_or_shifts_local )
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
        selHistManager->evt_ = new EvtHistManager2_hh_bb1l(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/evt", histogramDir.data()), era_string, central_or_shift));
        selHistManager->evt_->bookHistograms(fs);
        selHistManager->genKinematics_HH_ = new HHGenKinematicsHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/genKinematics_HH", histogramDir.data()), era_string, central_or_shift),
          analysisConfig, eventInfo, HHWeight_calc, HHWeight_calc_LOtoNLO);
        selHistManager->genKinematics_HH_->bookHistograms(fs);
      }

      if ( fillHistograms_BDT )
      {
        selHistManager->datacard_BDT_ = new DatacardHistManager_hh(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/datacard/BDT", histogramDir.data()), era_string, central_or_shift),
          analysisConfig, eventInfo, HHWeight_calc, HHWeight_calc_LOtoNLO, &eventCategory_BDT,
          isDEBUG, 
          fillHistograms_nonresonant, fillHistograms_resonant_spin0, fillHistograms_resonant_spin2);
        selHistManager->datacard_BDT_->bookHistograms(fs);
      }
      if ( fillHistograms_LBN )
      {
        selHistManager->datacard_LBN_ = new DatacardHistManager_hh_multiclass(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/datacard/LBN", histogramDir.data()), era_string, central_or_shift),
          analysisConfig, eventInfo, HHWeight_calc, HHWeight_calc_LOtoNLO, &eventCategory_LBN,
          isDEBUG, 
          fillHistograms_nonresonant, fillHistograms_resonant_spin0, fillHistograms_resonant_spin2);
        selHistManager->datacard_LBN_->bookHistograms(fs);
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
        selHistManager->weights_->bookHistograms(fs, { "genWeight", "pileupWeight", "triggerWeight", "btagWeight", "data_to_MC_correction", "fakeRate" });
      }
      selHistManagers[central_or_shift][idxLepton] = selHistManager;
    }

    if ( isMC && !skipBooking )
    {
      genEvtHistManager_beforeCuts[central_or_shift] = new GenEvtHistManager(makeHistManager_cfg(process_string,
        Form("%s/unbiased/genEvt", histogramDir.data()), era_string, central_or_shift));
      genEvtHistManager_beforeCuts[central_or_shift]->bookHistograms(fs);
      genEvtHistManager_afterCuts[central_or_shift] = new GenEvtHistManager(makeHistManager_cfg(process_string,
        Form("%s/sel/genEvt", histogramDir.data()), era_string, central_or_shift));
      genEvtHistManager_afterCuts[central_or_shift]->bookHistograms(fs);
      lheInfoHistManager[central_or_shift] = new LHEInfoHistManager(makeHistManager_cfg(process_string,
        Form("%s/sel/lheInfo", histogramDir.data()), era_string, central_or_shift));
      lheInfoHistManager[central_or_shift]->bookHistograms(fs);

      if(eventWeightManager)
      {
        genEvtHistManager_beforeCuts[central_or_shift]->bookHistograms(fs, eventWeightManager);
        genEvtHistManager_afterCuts[central_or_shift]->bookHistograms(fs, eventWeightManager);
      }
    }
  }

  NtupleFillerBDT<float, int>* bdt_filler = nullptr;
  typedef std::remove_pointer<decltype(bdt_filler)>::type::float_type float_type;
  typedef std::remove_pointer<decltype(bdt_filler)>::type::int_type int_type;

  NtupleFillerBDT<float, int>* second_bdt_filler = nullptr;
  typedef std::remove_pointer<decltype(second_bdt_filler)>::type::float_type float_type;
  typedef std::remove_pointer<decltype(second_bdt_filler)>::type::int_type int_type;

  if ( selectBDT ) {
    if ( second_bdt ) {
      second_bdt_filler = new std::remove_pointer<decltype(bdt_filler)>::type(
         makeHistManager_cfg(process_string, Form("%s/sel/evtntuple", histogramDir.data()), era_string, central_or_shift_main)
      );
      second_bdt_filler->register_variable<float_type>(
        "jpaScore_2b2W_resolved", "jpaScore_2b1W_resolved", "jpaScore_2b0W_resolved", "jpaScore_1b2W_resolved", "jpaScore_1b1W_resolved", "jpaScore_1b0W_resolved",
        "jpaScore_2b2W_boosted", "jpaScore_2b1W_boosted",
	"evtWeight"
      );
      second_bdt_filler->register_variable<int_type>(
        "Hbb_isBoosted", 
        "target"
      );
      second_bdt_filler->bookTree(fs);
    }
    else 
    {
      bdt_filler = new std::remove_pointer<decltype(bdt_filler)>::type(
         makeHistManager_cfg(process_string, Form("%s/sel/evtntuple", histogramDir.data()), era_string, central_or_shift_main)
      );
      for ( const std::string & evt_cat_str: HHWeightNames )
      {
        if (!apply_HH_rwgt) continue;
        bdt_filler->register_variable<float_type>(Form(evt_cat_str.c_str()));
      }
      bdt_filler->register_variable<float_type>(
        "lep_pt", "lep_conePt", "lep_eta", "lep_phi", "lep_mass",
        "lep_e", "lep_px", "lep_py", "lep_pz",
        "lep_frWeight",
        "bjet1_pt", "bjet1_eta", "bjet1_phi", "bjet1_mass",
        "bjet1_e", "bjet1_px", "bjet1_py", "bjet1_pz",
        "bjet2_pt", "bjet2_eta", "bjet2_phi", "bjet2_mass",
        "bjet2_e", "bjet2_px", "bjet2_py", "bjet2_pz",
        "wjet1_pt", "wjet1_eta", "wjet1_phi", "wjet1_mass",
        "wjet1_e", "wjet1_px", "wjet1_py", "wjet1_pz",
        "wjet2_pt", "wjet2_eta", "wjet2_phi", "wjet2_mass",
        "wjet2_e", "wjet2_px", "wjet2_py", "wjet2_pz",
        "bjet1_btagCSV", "bjet2_btagCSV", "wjet1_btagCSV", "wjet2_btagCSV",
        "met", "mht", "met_LD",
        "HT", "STMET",
        "m_Hbb", "m_Hbb_regCorr", "m_Hbb_regRes", "dR_Hbb", "dPhi_Hbb", "pT_Hbb", "eta_Hbb", "jpaScore",
        "m_Wjj", "dR_Wjj", "dPhi_Wjj", "pT_Wjj", "tau21_Wjj",
        "dR_Hww", "dPhi_Hww", "pT_Hww", "Smin_Hww",
        "dR_b1lep", "dR_b2lep",
        "m_HHvis", "pT_HHvis", "eta_HHvis", "dPhi_HHvis",
        "m_HH", "m_HH_B2G_18_008", "pT_HH", "dPhi_HH", "Smin_HH",
        "mT_W", "mT_top_2particle", "mT_top_3particle",
        "vbf_jet1_pt", "vbf_jet1_eta", "vbf_jet2_pt", "vbf_jet2_eta", "vbf_m_jj", "vbf_dEta_jj",
        "genWeight", "evtWeight",
        "mhh_gen", "costS_gen",
        "mindr_lep1_jet", "avg_dr_jet_central", "mbb_loose", "mbb_medium",
        "dR_HH",
        "tau21_Hbb",
        "cosThetaS_Hbb", "cosThetaS_Hbb_reg",
        "cosThetaS_Wjj", "cosThetaS_WW", "cosThetaS_HH", "mll_loose",
        "mostFwdJet_eta", "mostFwdJet_pt", "mostFwdJet_phi", "mostFwdJet_E",
        "leadFwdJet_eta", "leadFwdJet_pt", "leadFwdJet_phi", "leadFwdJet_E"
      );
      bdt_filler->register_variable<int_type>(
        "lep_charge", "numElectrons",
        "numJets", "numBJets_loose", "numBJets_medium", 
        "numBJets_jpa_loose", "numBJets_jpa_medium", "numBJets_jpa", "numWJets_jpa",
        "isHbb_boosted", "isWjj_boosted",
        "numJets_vbf", "isVBF",
        "numElectrons", "numLeptons_loose", "numJetsForward", "lepPairCharge_loose", "lepPairType_loose",
        "selLepton_charge", "selLepton_type"
      );
      bdt_filler->bookTree(fs);
    }
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
  const std::vector<std::string> cuts = {
    "run:ls:event selection",
    "object multiplicity",
    "trigger",
    ">= 1 presel leptons",
    ">= 1 sel leptons",
    "electron pT > 32 GeV / muon pT > 25 GeV",
    "<= 1 tight leptons",
    "trigger & fakeable lepton flavor matching",
    "trigger & dataset matching",
    "HLT filter matching",
    "tau veto",
    "m(ll) > 12 GeV",
    "Z-boson mass veto",
    ">= 2 jets from H->bb",
    ">= 1 medium b-jet",
    ">= 1 jets from W->jj",
    "MEt filters",
    "signal region veto"
  };
  CutFlowTableHistManager * cutFlowHistManager = new CutFlowTableHistManager(cutFlowTableCfg, cuts);
  cutFlowHistManager->bookHistograms(fs);
  while ( inputTree->hasNextEvent() && (! run_lumi_eventSelector || (run_lumi_eventSelector && ! run_lumi_eventSelector -> areWeDone())) ) 
  {
    if ( inputTree -> canReport(reportEvery) ) 
    {
      std::cout << "processing Entry " << inputTree -> getCurrentMaxEventIdx()
                << " or " << inputTree -> getCurrentEventIdx() << " entry in #"
                << (inputTree -> getProcessedFileCount() - 1)
                << " (" << eventInfo
                << ") file (" << selectedEntries << " Entries selected)\n";
    }
    ++analyzedEntries;
    histogram_analyzedEntries->Fill(0.);

    if ( isDEBUG ) 
    {
      std::cout << "event #" << inputTree -> getCurrentMaxEventIdx() << ' ' << eventInfo << '\n';
    }

    if ( run_lumi_eventSelector && !(*run_lumi_eventSelector)(eventInfo) ) continue;
    EvtWeightRecorderHH evtWeightRecorder(central_or_shifts_local, central_or_shift_main, isMC);
    cutFlowTable.update("run:ls:event selection", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("run:ls:event selection", evtWeightRecorder.get(central_or_shift_main));

    if ( run_lumi_eventSelector ) 
    {
      std::cout << "processing Entry #" << inputTree->getCumulativeMaxEventCount() << ": " << eventInfo << std::endl;
      if ( inputTree -> isOpen() ) 
      {
        std::cout << "input File = " << inputTree->getCurrentFileName() << std::endl;
      }
    }

    if(useObjectMultiplicity)
    {
      if ( objectMultiplicity.getNRecoLepton(minLeptonSelection) < 1 ||
           objectMultiplicity.getNRecoLepton(kTight)             > 1 )
      {
        if ( isDEBUG || run_lumi_eventSelector )
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
    if ( isMC && fillGenEvtHistograms )
    {
      if ( genLeptonReader )
      {
        genLeptons = genLeptonReader->read();
        for ( const GenLepton & genLepton: genLeptons )
        {
          const int abs_pdgId = std::abs(genLepton.pdgId());
          switch ( abs_pdgId )
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

      if ( isDEBUG )
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

    eventInfo.reset_productionMode();
    if ( isMC ) {
      if(analysisConfig.isMC_VH())
      {
        eventInfo.set_productionMode(get_VH_productionMode(genWBosons));
      }
    }

    std::vector<GenParticle> genLeptonsDY;
    if ( isMC )
    {
      for ( const GenParticle & genLepton : genLeptons )
      {
	genLeptonsDY.push_back(genLepton);
      }
      if(apply_genWeight)         evtWeightRecorder.record_genWeight(eventInfo);
      if(apply_DYMCReweighting)   evtWeightRecorder.record_dy_rwgt(dyReweighting, genLeptonsDY);
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
      for ( const std::string & central_or_shift: central_or_shifts_local )
      {
        if ( central_or_shift != central_or_shift_main )
        {
          continue;
        }
        genEvtHistManager_beforeCuts[central_or_shift]->fillHistograms(
          genElectrons, genMuons, genHadTaus, genPhotons, genJets, evtWeightRecorder.get_inclusive(central_or_shift)
        );
        if ( eventWeightManager )
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
    if ( !(selTrigger_1e || selTrigger_1mu) ) 
    {
      if ( run_lumi_eventSelector ) 
      {
	std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
        std::cout << " (selTrigger_1e = " << selTrigger_1e
                  << ", selTrigger_1mu = " << selTrigger_1mu << ")" << std::endl;
      }
      continue;
    }
    cutFlowTable.update("trigger", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("trigger", evtWeightRecorder.get(central_or_shift_main));

    if ( (selTrigger_1e  && !apply_offline_e_trigger_cuts_1e)  ||
         (selTrigger_1mu && !apply_offline_e_trigger_cuts_1mu) ) 
    {
      fakeableElectronSelector_default.disable_offline_e_trigger_cuts();
      tightElectronSelector.disable_offline_e_trigger_cuts();
    } 
    else 
    {
      tightElectronSelector.enable_offline_e_trigger_cuts();
      fakeableElectronSelector_default.enable_offline_e_trigger_cuts();
    }

    double vbf_lhe_m_jj(-1.);
    double vbf_lhe_dEta_jj(-1.);
    if ( isMC && process_string_hh.find("vbf") != std::string::npos )
    {
      const std::vector<LHEParticle> lheparticles = lheparticleReader->read();
      std::vector<Particle::LorentzVector> vbf_lhe_p4;
      for (const auto & particle: lheparticles) {
        if ( particle.pdgId() !=25 ) vbf_lhe_p4.push_back(Particle::LorentzVector(particle.pt(), particle.eta(), particle.phi(), particle.mass()));
      }
    assert( vbf_lhe_p4.size() ==2 );
    vbf_lhe_m_jj = (vbf_lhe_p4[0] + vbf_lhe_p4[1]).mass();
    vbf_lhe_dEta_jj = TMath::Abs((vbf_lhe_p4[0].eta() - vbf_lhe_p4[1].eta()));
    }
//--- build collections of electrons, muons and hadronic taus;
//    resolve overlaps in order of priority: muon, electron,
    const std::vector<RecoMuon> muons = muonReader->read();
    const std::vector<const RecoMuon*> muon_ptrs = convert_to_ptrs(muons);
    const std::vector<const RecoMuon*> cleanedMuons = muon_ptrs; // CV: no cleaning needed for muons, as they have the highest priority in the overlap removal
    const std::vector<const RecoMuon*> preselMuons = preselMuonSelector(cleanedMuons, isHigherConePt);
    const std::vector<const RecoMuon*> fakeableMuons = lep_mva_wp == "hh_multilepton" ?
      fakeableMuonSelector_hh_multilepton(preselMuons, isHigherConePt) :
      fakeableMuonSelector_default(preselMuons, isHigherConePt)
    ;
    const std::vector<const RecoMuon*> tightMuons = tightMuonSelector(fakeableMuons, isHigherConePt);
    if ( isDEBUG || run_lumi_eventSelector ) 
    {
      printCollection("preselMuons",   preselMuons);
      printCollection("fakeableMuons", fakeableMuons);
      printCollection("tightMuons",    tightMuons);
    }

    const std::vector<RecoElectron> electrons = electronReader->read();
    const std::vector<const RecoElectron*> electron_ptrs = convert_to_ptrs(electrons);
    const std::vector<const RecoElectron*> cleanedElectrons = electronCleaner(electron_ptrs, preselMuons);
    const std::vector<const RecoElectron*> preselElectrons = preselElectronSelector(cleanedElectrons, isHigherConePt);
    const std::vector<const RecoElectron*> preselElectronsUncleaned = preselElectronSelector(electron_ptrs, isHigherConePt);
    const std::vector<const RecoElectron*> fakeableElectrons = lep_mva_wp == "hh_multilepton" ?
      fakeableElectronSelector_hh_multilepton(preselElectrons, isHigherConePt) :
      fakeableElectronSelector_default(preselElectrons, isHigherConePt)
    ;
    const std::vector<const RecoElectron*> tightElectrons = tightElectronSelector(fakeableElectrons, isHigherConePt);
    if ( isDEBUG || run_lumi_eventSelector ) 
    {
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
    const std::vector<const RecoLepton*> vetoLeptons = tightLeptonsFull;

    std::vector<const RecoLepton*> selLeptons;
    std::vector<const RecoMuon*> selMuons;
    std::vector<const RecoElectron*> selElectrons;
    if ( electronSelection == muonSelection ) 
    {
      // for SR, flip region and fake CR
      // doesn't matter if we supply electronSelection or muonSelection here
      selLeptons = selectObjects(muonSelection, preselLeptons, fakeableLeptons, tightLeptons);
      selMuons = getIntersection(preselMuons, selLeptons, isHigherConePt);
      selElectrons = getIntersection(preselElectrons, selLeptons, isHigherConePt);
    } 
    else 
    {
      // for MC closure
      // make sure that neither electron nor muon selections are loose
      assert(electronSelection != kLoose && muonSelection != kLoose);
      selMuons = selectObjects(muonSelection, preselMuons, fakeableMuons, tightMuons);
      selElectrons = selectObjects(electronSelection, preselElectrons, fakeableElectrons, tightElectrons);
      const std::vector<const RecoLepton*> selLeptons_full = mergeLeptonCollections(selElectrons, selMuons, isHigherConePt);
      selLeptons = getIntersection(fakeableLeptons, selLeptons_full, isHigherConePt);
    }

    if ( isDEBUG || run_lumi_eventSelector ) 
    {
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
    const std::vector<const RecoJet*> tmpJetsAK4 = jetCleaningByIndex ?
      jetCleanerAK4_byIndex(jet_ptrs_ak4, fakeableLeptons) :
      jetCleanerAK4_dR04   (jet_ptrs_ak4, fakeableLeptons)
    ;
    std::vector<const RecoJet*> cleanedJetsAK4_wrtLeptons = pickFirstNobjects(tmpJetsAK4, max_numJets);
    const std::vector<const RecoJet*> selJetsAK4_vbf_beforeCleaning = jetSelectorAK4_vbf(jet_ptrs_ak4, isHigherPt);
    const std::vector<const RecoJet*> selJetsAK4_vbf_postLeptonCleaning = jetCleaningByIndex ?
      jetCleanerAK4_byIndex(selJetsAK4_vbf_beforeCleaning, fakeableLeptons) :
      jetCleanerAK4_dR04   (selJetsAK4_vbf_beforeCleaning, fakeableLeptons)
    ;
    const std::vector<const RecoJet*> selJetsAK4 = jetSelectorAK4_wPileupJetId(cleanedJetsAK4_wrtLeptons, isHigherPt);
    const std::vector<const RecoJet*> selBJetsAK4_loose = jetSelectorAK4_bTagLoose(cleanedJetsAK4_wrtLeptons, isHigherPt);
    const std::vector<const RecoJet*> selBJetsAK4_medium = jetSelectorAK4_bTagMedium(cleanedJetsAK4_wrtLeptons, isHigherPt);
    const std::vector<const RecoJet *> selJetsForward = jetSelectorForward(cleanedJetsAK4_wrtLeptons, isHigherPt);

    if ( isDEBUG || run_lumi_eventSelector ) 
    {
      printCollection("hadTau_ptrs", hadTau_ptrs);
      printCollection("cleanedHadTaus", cleanedHadTaus);
      printCollection("vetoHadTaus", vetoHadTaus);
      printCollection("uncleaned AK4 jets", jet_ptrs_ak4);
      printCollection("cleaned AK4 jets(wrtLeptons)", cleanedJetsAK4_wrtLeptons);
      printCollection("selected AK4 jets", selJetsAK4);
      printCollection("selJetsForward", selJetsForward);
    }

    const RecoMEt met = metReader->read();
    const Particle::LorentzVector& metP4 = met.p4();

//--- build collections of generator level particles (after some cuts are applied, to save computing time)
    if ( isMC && redoGenMatching && !fillGenEvtHistograms )
    {
      if ( genLeptonReader )
      {
        genLeptons = genLeptonReader->read();
        for ( const GenLepton & genLepton: genLeptons )
        {
          const int abs_pdgId = std::abs(genLepton.pdgId());
          switch ( abs_pdgId )
          {
            case 11: genElectrons.push_back(genLepton); break;
            case 13: genMuons.push_back(genLepton);     break;
            default: assert(0);
          }
        }
      }
      if ( genHadTauReader ) genHadTaus = genHadTauReader->read();
      if ( genPhotonReader ) genPhotons = genPhotonReader->read();
      if ( genJetReader ) genJets = genJetReader->read();

      if ( genMatchToMuonReader ) muonGenMatch = genMatchToMuonReader->read();
      if ( genMatchToElectronReader ) electronGenMatch = genMatchToElectronReader->read();
      if ( genMatchToHadTauReader ) hadTauGenMatch = genMatchToHadTauReader->read();
      if ( genMatchToJetReader ) jetGenMatch = genMatchToJetReader->read();
    }

//--- match reconstructed to generator level particles
    if ( isMC && redoGenMatching )
    {
      if ( genMatchingByIndex )
      {
        muonGenMatcher.addGenLeptonMatchByIndex(preselMuons, muonGenMatch, GenParticleType::kGenMuon);
        muonGenMatcher.addGenHadTauMatch(preselMuons, genHadTaus);
        muonGenMatcher.addGenJetMatch(preselMuons, genJets);

        electronGenMatcher.addGenLeptonMatchByIndex(preselElectrons, electronGenMatch, GenParticleType::kGenElectron);
        electronGenMatcher.addGenPhotonMatchByIndex(preselElectrons, electronGenMatch);
        electronGenMatcher.addGenHadTauMatch(preselElectrons, genHadTaus);
        electronGenMatcher.addGenJetMatch(preselElectrons, genJets);

        hadTauGenMatcher.addGenLeptonMatchByIndex(cleanedHadTaus, hadTauGenMatch, GenParticleType::kGenAnyLepton);
        hadTauGenMatcher.addGenHadTauMatch(cleanedHadTaus, genHadTaus);
        hadTauGenMatcher.addGenJetMatch(cleanedHadTaus, genJets);

        jetGenMatcherAK4.addGenLeptonMatch(jet_ptrs_ak4, genLeptons);
        jetGenMatcherAK4.addGenHadTauMatch(jet_ptrs_ak4, genHadTaus);
        jetGenMatcherAK4.addGenJetMatchByIndex(jet_ptrs_ak4, jetGenMatch);
      }
      else
      {
        muonGenMatcher.addGenLeptonMatch(preselMuons, genMuons);
        muonGenMatcher.addGenHadTauMatch(preselMuons, genHadTaus);
        muonGenMatcher.addGenJetMatch(preselMuons, genJets);

        electronGenMatcher.addGenLeptonMatch(preselElectrons, genElectrons);
        electronGenMatcher.addGenPhotonMatch(preselElectrons, genPhotons);
        electronGenMatcher.addGenHadTauMatch(preselElectrons, genHadTaus);
        electronGenMatcher.addGenJetMatch(preselElectrons, genJets);

        hadTauGenMatcher.addGenLeptonMatch(cleanedHadTaus, genLeptons);
        hadTauGenMatcher.addGenHadTauMatch(cleanedHadTaus, genHadTaus);
        hadTauGenMatcher.addGenJetMatch(cleanedHadTaus, genJets);

        jetGenMatcherAK4.addGenLeptonMatch(jet_ptrs_ak4, genLeptons);
        jetGenMatcherAK4.addGenHadTauMatch(jet_ptrs_ak4, genHadTaus);
        jetGenMatcherAK4.addGenJetMatch(jet_ptrs_ak4, genJets);
      }
    }
    GenParticleMatcherBase* genParticleMatcher = nullptr;
    if ( isSignal )
    {
      std::vector<GenParticle> genNeutrinos;
      std::vector<GenParticle> genParticlesFromHiggs = genParticleFromHiggsReader->read();
      genWJets = genWJetReader->read();
      genParticleMatcherFromHiggs.setGenParticles(genParticlesFromHiggs, genLeptons, genNeutrinos, genWJets);
      genParticleMatcher = &genParticleMatcherFromHiggs;
    }
    else if ( isMC_TT )
    {
      std::vector<GenLepton> genLeptonsFromTop;
      std::vector<GenParticle> genNeutrinosFromTop;
      std::vector<GenParticle> genBJetsFromTop = genBJetFromTopReader->read();
      std::vector<GenParticle> genWJetsFromTop = genWJetFromTopReader->read();
      genParticleMatcherFromTop.setGenParticles(genLeptonsFromTop, genNeutrinosFromTop, genWJetsFromTop, genBJetsFromTop);
      genParticleMatcher = &genParticleMatcherFromTop;
    }
    std::vector<const GenJet*> genBJets_ptrs;
    std::vector<const GenJet*> genWJets_ptrs;
    std::vector<GenJet> genBJets_;
    std::vector<GenJet> genWJets_;
    if ( genParticleMatcher ) 
    {
      genBJets_ = genParticleMatcher->getBJets();
      genBJets_ptrs = convert_to_ptrs(genBJets_);
      genWJets_ = genParticleMatcher->getWJets();
      genWJets_ptrs = convert_to_ptrs(genWJets_);
    }

    // require at least one lepton passing loose preselection criteria
    if ( !(preselLeptonsFull.size() >= 1) ) 
    {
      if ( run_lumi_eventSelector ) 
      {
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
    if ( !(selLeptons.size() >= 1) ) 
    {
      if ( run_lumi_eventSelector ) 
      {
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
    if ( !((selLepton->is_electron() && selLepton->cone_pt() > minPt_electron) || (selLepton->is_muon() && selLepton->cone_pt() > minPt_muon)) ) 
    {
      if ( run_lumi_eventSelector ) 
      {
        std::cout << "event " << eventInfo.str() << " FAILS lepton pT selection." << std::endl;
        if      ( selLepton->is_electron() ) std::cout << " (selElectron pT = " << selLepton->pt() << ", minPt_electron = " << minPt_electron << ")" << std::endl;
        else if ( selLepton->is_muon()     ) std::cout << " (selMuon pT = " << selLepton->pt() << ", minPt_muon = " << minPt_muon << ")" << std::endl;
        else assert(0);
      }
      continue;
    }
    cutFlowTable.update(Form("electron pT > %0.0f GeV / muon pT > %0.0f GeV", minPt_electron, minPt_muon), evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("electron pT > 32 GeV / muon pT > 25 GeV", evtWeightRecorder.get(central_or_shift_main));

    // require exactly one lepton passing tight selection criteria, to avoid overlap with other channels
    if ( !(vetoLeptons.size() <= 1) ) 
    {
      if ( run_lumi_eventSelector ) 
      {
        std::cout << "event " << eventInfo.str() << " FAILS tightLeptons selection." << std::endl;
        printCollection("vetoLeptons", vetoLeptons);
      }
      continue;
    }
    cutFlowTable.update("<= 1 tight leptons", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("<= 1 tight leptons", evtWeightRecorder.get(central_or_shift_main));

    // require that trigger paths match lepton flavor (for fakeable leptons)
    if ( !((selElectrons.size() >= 1 && selTrigger_1e) ||
           (selMuons.size()     >= 1 && selTrigger_1mu)) ) 
    {
      if ( run_lumi_eventSelector ) 
      {
	std::cout << "event " << eventInfo.str() << " FAILS trigger selection for given selLepton multiplicity." << std::endl;
        std::cout << " (#selElectrons = " << selElectrons.size()
                  << ", #selMuons = " << selMuons.size()
                  << ", selTrigger_1mu = " << selTrigger_1mu
                  << ", selTrigger_1e = " << selTrigger_1e << ")" << std::endl;
      }
      continue;
    }
    cutFlowTable.update("trigger & fakeable lepton flavor matching", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("trigger & fakeable lepton flavor matching", evtWeightRecorder.get(central_or_shift_main));

    // Require that trigger paths match primary datasets,
    // to avoid that the same event is selected multiple times when processing different primary datasets (PD).
    // In case the same event passes the triggers paths for more than one primary datasets,
    // the event is selected in the PD of highest priority only. 
    // The ranking of the PDs is as follows: SingleMuon, SingleElectron.
    if ( !isMC && !isDEBUG ) 
    {
      //bool isTriggered_SingleElectron = isTriggered_1e && fakeableElectrons.size() >= 1;
      bool isTriggered_SingleMuon = isTriggered_1mu && fakeableMuons.size() >= 1;

      bool selTrigger_SingleElectron = selTrigger_1e;
      //bool selTrigger_SingleMuon = selTrigger_1mu;

      if ( selTrigger_SingleElectron && isTriggered_SingleMuon ) 
      {
        if ( run_lumi_eventSelector ) 
        {
          std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
          std::cout << " (selTrigger_SingleElectron = " << selTrigger_SingleElectron
                    << ", isTriggered_SingleMuon = " << isTriggered_SingleMuon << ")" << std::endl;
        }
        continue;
      }
    }
    cutFlowTable.update("trigger & dataset matching", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("trigger & dataset matching", evtWeightRecorder.get(central_or_shift_main));

//--- apply HLT filter
    if ( apply_hlt_filter ) 
    {
      const std::map<hltPathsE, bool> trigger_bits = {
        { hltPathsE::trigger_1e,  selTrigger_1e  },
        { hltPathsE::trigger_1mu, selTrigger_1mu },
      };
      if ( !hltFilter(trigger_bits, fakeableLeptons, {}) ) 
      {
        if ( run_lumi_eventSelector || isDEBUG ) 
        {
          std::cout << "event " << eventInfo.str() << " FAILS HLT filter matching\n";
        }
        continue;
      }
    }
    cutFlowTable.update("HLT filter matching", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("HLT filter matching", evtWeightRecorder.get(central_or_shift_main));

    if ( apply_hadTauVeto ) 
    {
      if ( vetoHadTaus.size() > 0 ) 
      {
        if ( run_lumi_eventSelector ) 
        {
	  std::cout << "event " << eventInfo.str() << " FAILS vetoHadTaus selection." << std::endl;
          printCollection("vetoHadTaus", vetoHadTaus);
        }
        continue;
      }
    }
    cutFlowTable.update("tau veto", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("tau veto", evtWeightRecorder.get(central_or_shift_main));

    const bool failsLowMassVeto = isfailsLowMassVeto(preselLeptonsFullUncleaned);
    if ( failsLowMassVeto ) 
    {
      if ( run_lumi_eventSelector ) 
      {
	std::cout << "event " << eventInfo.str() << " FAILS low mass lepton pair veto." << std::endl;
      }
      continue;
    }
    cutFlowTable.update("m(ll) > 12 GeV", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("m(ll) > 12 GeV", evtWeightRecorder.get(central_or_shift_main));

    const bool failsZbosonMassVeto = isfailsZbosonMassVeto(preselLeptonsFull);
    if ( failsZbosonMassVeto ) 
    {
      if ( run_lumi_eventSelector ) 
      {
	std::cout << "event " << eventInfo.str() << " FAILS Z-boson veto." << std::endl;
      }
      continue;
    }
    cutFlowTable.update("Z-boson mass veto", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("Z-boson mass veto", evtWeightRecorder.get(central_or_shift_main));

    if ( isMC )
    {
      if ( apply_DYMCNormScaleFactors )
      {
	evtWeightRecorder.record_dy_norm(
          dyNormScaleFactors, genLeptonsDY, selJetsAK4.size(), selBJetsAK4_loose.size(), selBJetsAK4_medium.size());
      }
//--- compute event-level weight for data/MC correction of b-tagging efficiency and mistag rate
//   (using the method "Event reweighting using scale factors calculated with a tag and probe method",
//    described on the BTV POG twiki https://twiki.cern.ch/twiki/bin/view/CMS/BTagShapeCalibration )
      evtWeightRecorder.record_btagWeight(selJetsAK4);
      if ( btagSFRatioFacility )
      {
        evtWeightRecorder.record_btagSFRatio(btagSFRatioFacility, selJetsAK4.size());
      }

      dataToMCcorrectionInterface->setLeptons({ selLepton });

      if ( apply_pileupJetID != kPileupJetID_disabled )
      {
        const std::vector<const RecoJet*> selJetsAK4_woPileupJetId = jetSelectorAK4_woPileupJetId(cleanedJetsAK4_wrtLeptons, isHigherPt);
        const std::vector<const RecoJet*> selJetsAK4_vbf_woPileupJetId = jetSelectorAK4_vbf_woPileupJetId(cleanedJetsAK4_wrtLeptons, isHigherPt);
        const std::vector<const RecoJet*> selJetsAK4_forPUjetIDSF = mergeCollections(selJetsAK4_woPileupJetId, selJetsAK4_vbf_woPileupJetId, isHigherPt);
        if(isDEBUG)
        {
          printCollection("selJetsAK4_woPileupJetId", selJetsAK4_woPileupJetId);
          printCollection("selJetsAK4_vbf_woPileupJetId", selJetsAK4_vbf_woPileupJetId);
          printCollection("selJetsAK4_forPUjetIDSF", selJetsAK4_forPUjetIDSF);
        }
        dataToMCcorrectionInterface->setJets(selJetsAK4_forPUjetIDSF);
        evtWeightRecorder.record_pileupJetIDSF(dataToMCcorrectionInterface);
      }

//--- apply data/MC corrections for trigger efficiency
      evtWeightRecorder.record_leptonTriggerEff(dataToMCcorrectionInterface);

//--- apply data/MC corrections for efficiencies for lepton to pass loose identification and isolation criteria
      evtWeightRecorder.record_leptonIDSF_recoToLoose(dataToMCcorrectionInterface);

//--- apply data/MC corrections for efficiencies of leptons passing the loose identification and isolation criteria
//    to also pass the tight identification and isolation criteria
      if ( electronSelection >= kFakeable && muonSelection >= kFakeable )
      {
        // apply looseToTight SF to leptons matched to generator-level prompt leptons and passing Tight selection conditions
        evtWeightRecorder.record_leptonIDSF_looseToTight(dataToMCcorrectionInterface);
      }
    }

    bool passesTight_lepton = isMatched(*selLepton, tightElectrons) || isMatched(*selLepton, tightMuons);

    if ( leptonFakeRateInterface )
    {
      evtWeightRecorder.record_jetToLepton_FR_lead(leptonFakeRateInterface, selLepton);
    }

    if ( !selectBDT )
    {
      if(applyFakeRateWeights == kFR_enabled)
      {
	evtWeightRecorder.compute_FR_1l(passesTight_lepton);
      }
    }

    const std::vector<RecoJetAK8> jets_ak8 = jetReaderAK8->read();
    const std::vector<const RecoJetAK8*> jet_ptrs_ak8 = convert_to_ptrs(jets_ak8);
    const std::vector<RecoJetAK8> jets_ak8LS = jetReaderAK8LS->read();
    const std::vector<const RecoJetAK8*> jet_ptrs_ak8LS = convert_to_ptrs(jets_ak8LS);

    if ( isDEBUG || run_lumi_eventSelector ) 
    {
      printCollection("uncleaned AK8 jets (Hbb)", jet_ptrs_ak8);
      printHbb(jet_ptrs_ak8, jetSelectorAK8_Hbb, genBJets);
      printCollection("uncleaned AK8LS jets (Wjj)", jet_ptrs_ak8LS);
      printWjj(jet_ptrs_ak8LS, jetSelectorAK8_Wjj, genWBosons, genWJets);
    }

    // select jets from H->bb decay
    const std::vector<const RecoJetAK8*> cleanedJetsAK8_wrtLeptons = jetCleanerAK8_dR08(jet_ptrs_ak8, fakeableLeptons);
    const std::vector<const RecoJetAK8*> selJetsAK8_Hbb = jetSelectorAK8_Hbb(cleanedJetsAK8_wrtLeptons, isHigherCSV_ak8);
    const std::vector<const RecoJetAK8*> selJetsAK8 = jetSelectorAK8(cleanedJetsAK8_wrtLeptons, isHigherPt);
    const std::vector<const RecoJet*> selJetsAK4_Hbb = jetSelectorAK4_wPileupJetId(cleanedJetsAK4_wrtLeptons, isHigherCSV);

    std::vector<selJetsType_Hbb> selJetsT_Hbb = selectJets_Hbb(selJetsAK8_Hbb, selJetsAK4_Hbb);
    selJetsType_Hbb* selJetT_Hbb = nullptr;
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
    std::vector<const RecoJet*> cleanedJetsAK4_wrtHbb;
    std::vector<const RecoJet*> cleanedJetsAK4_vbf_wrtHbb;
    if ( selJetAK8_Hbb )
    {
      cleanedJetsAK4_wrtHbb = jetCleanerAK4_dR12(selJetsAK4, std::vector<const RecoJetBase*>({ selJetAK8_Hbb }));
      cleanedJetsAK4_vbf_wrtHbb = jetCleanerAK4_dR12(selJetsAK4_vbf_postLeptonCleaning, std::vector<const RecoJetBase*>({ selJetAK8_Hbb }));
    } 
    else 
    {
      std::vector<const RecoJetBase*> overlaps;
      if ( selJet1_Hbb ) { overlaps.push_back(selJet1_Hbb); }
      if ( selJet2_Hbb ) { overlaps.push_back(selJet2_Hbb); }
      cleanedJetsAK4_wrtHbb = jetCleanerAK4_dR04(selJetsAK4, overlaps);
      cleanedJetsAK4_vbf_wrtHbb = jetCleanerAK4_dR04(selJetsAK4_vbf_postLeptonCleaning, overlaps);
    }
    if ( !(selJet1_Hbb && selJet2_Hbb) ) 
    {
      if ( run_lumi_eventSelector ) 
      {
	std::cout << "event " << eventInfo.str() << " FAILS >= 2 jets from H->bb selection\n";
      }
      continue;
    }
    cutFlowTable.update(">= 2 jets from H->bb", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(">= 2 jets from H->bb", evtWeightRecorder.get(central_or_shift_main));

    if ( !(selJetAK8_Hbb || selBJetsAK4_medium.size() >= 1) )
    {
      if ( run_lumi_eventSelector ) 
      {
	std::cout << "event " << eventInfo.str() << " FAILS >= 1 medium b-jet selection\n";
      }
      continue;
    }
    cutFlowTable.update(">= 1 medium b-jet", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(">= 1 medium b-jet", evtWeightRecorder.get(central_or_shift_main));

    if ( !((selJetAK8_Hbb && cleanedJetsAK4_wrtHbb.size() >=1) || (!selJetAK8_Hbb && selJetsAK4.size() >=3)) ) 
    {
      if ( run_lumi_eventSelector ) 
      {
	std::cout << "event " << eventInfo.str() << " FAILS >= 1 jets from W->jj selection\n";
      }
      continue;
    }
    cutFlowTable.update(">= 1 jets from W->jj", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(">= 1 jets from W->jj", evtWeightRecorder.get(central_or_shift_main));

    if ( apply_met_filters ) 
    {
      if ( !metFilterSelector(metFilters) ) 
      {
        if ( run_lumi_eventSelector ) 
        {
	  std::cout << "event " << eventInfo.str() << " FAILS MEt filters." << std::endl;
        }
        continue;
      }
    }
    cutFlowTable.update("MEt filters", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("MEt filters", evtWeightRecorder.get(central_or_shift_main));

    bool failsSignalRegionVeto = false;
    if ( isMCClosure_e || isMCClosure_m ) 
    {
      bool applySignalRegionVeto = (isMCClosure_e && countFakeElectrons(selLeptons) >= 1) || (isMCClosure_m && countFakeMuons(selLeptons) >= 1);
      if ( applySignalRegionVeto && tightLeptons.size() >= 1 ) failsSignalRegionVeto = true;
    } 
    else if ( electronSelection == kFakeable || muonSelection == kFakeable ) 
    {
      if ( tightLeptons.size() >= 1 ) failsSignalRegionVeto = true;
    }
    if ( failsSignalRegionVeto ) 
    {
      if ( run_lumi_eventSelector ) 
      {
	std::cout << "event " << eventInfo.str() << " FAILS overlap w/ the SR: "
          "# tight leptons = " << tightLeptons.size() << " >= 2\n"
	  ;
        printCollection("tightLeptons", tightLeptons);
      }
      continue; // CV: avoid overlap with signal region
    }
    cutFlowTable.update("signal region veto", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("signal region veto", evtWeightRecorder.get(central_or_shift_main));

    std::vector<const RecoJetAK8*> selJetsAK8_Wjj;
    if ( jet_ptrs_ak8LS.size() > 0 )
    {
      std::vector<const RecoJetAK8*> cleanedJetsAK8LS_wrtHbb;
      if ( selJetAK8_Hbb ) 
      {
        const std::vector<const RecoJetAK8*> overlaps = { selJetAK8_Hbb };
        cleanedJetsAK8LS_wrtHbb = jetCleanerAK8_dR16(jet_ptrs_ak8LS, overlaps); // CV: do *not* clean W->jj "fat" jet collection with respect to leptons!
      }
      else 
      {
        const std::vector<const RecoJetBase*> overlaps = { selJet1_Hbb, selJet2_Hbb };
        cleanedJetsAK8LS_wrtHbb = jetCleanerAK8_dR12(jet_ptrs_ak8LS, overlaps);
      }
      if ( selLepton && selJet1_Hbb && selJet2_Hbb )
      {
        jetSelectorAK8_Wjj.getSelector().set_lepton(selLepton);
        std::vector<const RecoJetAK8*> preselJetsAK8_Wjj = jetSelectorAK8_Wjj(cleanedJetsAK8LS_wrtHbb, isHigherPt);
        for ( const RecoJetAK8* preselJetAK8_Wjj: preselJetsAK8_Wjj )
        {
          const RecoJetBase* subJet1_Wjj = preselJetAK8_Wjj->subJet1();
          const RecoJetBase* subJet2_Wjj = preselJetAK8_Wjj->subJet2();
          if ( !(subJet1_Wjj && subJet2_Wjj) ) continue;

          Particle::LorentzVector neutrinoP4_B2G_18_008 = comp_metP4_B2G_18_008(selLeptonP4 + subJet1_Wjj->p4() + subJet2_Wjj->p4(), metP4.px(), metP4.py(), higgsBosonMass);
          Particle::LorentzVector WjjP4 = subJet1_Wjj->p4() + subJet2_Wjj->p4();
          Particle::LorentzVector WlnuP4 = selLeptonP4 + neutrinoP4_B2G_18_008;

          // apply cut on mD variable, defined by Eq.(3) in AN-2018/058 (v4)
          double mD = deltaR(WjjP4, WlnuP4)*0.5*(WjjP4 + WlnuP4).pt();
          if ( !(mD <= higgsBosonMass) ) continue;

          // apply cut on event centrality variable, defined in Table 9 of AN-2018/058 (v4)
          double pT_HWW = (WjjP4 + WlnuP4).pt();
          double mHH = (selJet1_Hbb->p4() + selJet2_Hbb->p4() + WjjP4 + WlnuP4).mass();
          if ( !((pT_HWW/mHH) >= 0.3) ) continue;

          selJetsAK8_Wjj.push_back(preselJetAK8_Wjj);
        }
      }
      else
      {
        if ( isDEBUG )
        {
          std::cerr << "Warning in <selectJets_Wjj>: Cannot select AK8LS jets, as there is no lepton in the event !!" << std::endl;
        }
      }
    }
    std::sort(selJetsAK8_Wjj.begin(), selJetsAK8_Wjj.end(), isHigherPt);
    const RecoJetAK8* selJetAK8_Wjj = ( selJetsAK8_Wjj.size() >= 1 ) ? selJetsAK8_Wjj[0] : nullptr;
    
    // select jets from H->bb and W->jj decay using jet-parton assignment (JPA) method
    JPA jpa;
    if ( selJetAK8_Hbb ) 
    {
      std::vector<JPAJet> ak4Jets_jpa;
      for ( const RecoJet* ak4Jet: cleanedJetsAK4_wrtHbb )
      {
        ak4Jets_jpa.push_back(convert_to_JPAJet(ak4Jet));
      }
      //std::cout << "#ak4Jets_jpa (boosted) = " << ak4Jets_jpa.size() << std::endl;
      std::pair<JPAJet, JPAJet> ak8jet_subjet1_and_2_jpa = convert_to_JPAJets(selJetAK8_Hbb);
      jpa = jpaInterface(
        ak4Jets_jpa, ak8jet_subjet1_and_2_jpa.first, ak8jet_subjet1_and_2_jpa.second, 
        selLepton->p4(), preselLeptons.size(), selJetsAK4.size(), selBJetsAK4_loose.size(), selBJetsAK4_medium.size(), metP4.px(), metP4.py(), 
        eventInfo.event);
      //std::cout << "JPA (boosted):" << std::endl;
      //std::cout << jpa;
    }
    else
    {
      std::vector<JPAJet> ak4Jets_jpa;
      for ( const RecoJet* ak4Jet: selJetsAK4 )
      {
        ak4Jets_jpa.push_back(convert_to_JPAJet(ak4Jet));
      }
      //std::cout << "#ak4Jets_jpa (resolved) = " << ak4Jets_jpa.size() << std::endl;
      jpa = jpaInterface(
        ak4Jets_jpa,
        selLepton->p4(), preselLeptons.size(), selJetsAK4.size(), selBJetsAK4_loose.size(), selBJetsAK4_medium.size(), metP4.px(), metP4.py(), 
        eventInfo.event);
      //std::cout << "JPA (resolved):" << std::endl;
      //std::cout << jpa;
    }   

    if ( second_bdt ) 
    {
      std::pair<int, int> matchedJets;
      if ( selJetAK8_Hbb ) matchedJets = getMatchedJets(cleanedJetsAK4_wrtHbb, genBJets_ptrs, genWJets_ptrs, true);
      else matchedJets = getMatchedJets(selJetsAK4, genBJets_ptrs, genWJets_ptrs);
      int gen_jpaCategory = -1;
      if ( selJetAK8_Hbb ) 
      {
        if      ( matchedJets.second == 2 ) gen_jpaCategory = kjpa_HbbBoosted_2jet;
	else if ( matchedJets.second == 1 ) gen_jpaCategory = kjpa_HbbBoosted_missingWJet;
        else                                gen_jpaCategory = kjpa_HbbBoosted_restOfcat;
      }
      else
      {
        if      ( matchedJets.first == 2 && matchedJets.second == 2 ) gen_jpaCategory = kjpa_HbbResolved_4jet;
        else if ( matchedJets.first == 2 && matchedJets.second == 1 ) gen_jpaCategory = kjpa_HbbResolved_missingWJet;
        else if ( matchedJets.first == 1 && matchedJets.second == 2 ) gen_jpaCategory = kjpa_HbbResolved_missingBJet;
	else if ( matchedJets.first == 2 && matchedJets.second == 0 ) gen_jpaCategory = kjpa_HbbResolved_missingAllWJet;
        else if ( matchedJets.first == 1 && matchedJets.second == 1 ) gen_jpaCategory = kjpa_HbbResolved_missingBJet_missingWJet;
        else if ( matchedJets.first == 1 && matchedJets.second == 0 ) gen_jpaCategory = kjpa_HbbResolved_missingBJet_missingAllWJet;
        else                                                          gen_jpaCategory = kjpa_HbbResolved_restOfcat;
      }
      second_bdt_filler -> operator()({ eventInfo.run, eventInfo.lumi, eventInfo.event })
        ("jpaScore_2b2W_resolved", jpaInterface.mvaOutput_1stLayer((int)JPA::Category_resolved::k2b2W))
        ("jpaScore_2b1W_resolved", jpaInterface.mvaOutput_1stLayer((int)JPA::Category_resolved::k2b1W))
        ("jpaScore_2b0W_resolved", jpaInterface.mvaOutput_1stLayer((int)JPA::Category_resolved::k2b0W))
        ("jpaScore_1b2W_resolved", jpaInterface.mvaOutput_1stLayer((int)JPA::Category_resolved::k1b2W))
        ("jpaScore_1b1W_resolved", jpaInterface.mvaOutput_1stLayer((int)JPA::Category_resolved::k1b1W))
        ("jpaScore_1b0W_resolved", jpaInterface.mvaOutput_1stLayer((int)JPA::Category_resolved::k1b0W))
        ("jpaScore_2b2W_boosted",  jpaInterface.mvaOutput_1stLayer((int)JPA::Category_boosted::k2b2W))
        ("jpaScore_2b1W_boosted",  jpaInterface.mvaOutput_1stLayer((int)JPA::Category_boosted::k2b1W))
        ("Hbb_isBoosted",          (selJetAK8_Hbb) ? true : false)
        ("target",                 gen_jpaCategory)
        ("evtWeight",              evtWeightRecorder.get(central_or_shift_main))
        .fill()
      ;
      /*if(!selJetAK8_Hbb) {
	h_genmatch->Fill(gen_jpaCategory, jpaInterface.getevtCat());
      }
      else {
	h_genmatchBoosted->Fill(gen_jpaCategory, jpaInterface.getevtCat());
	}*/
      continue;
    }

    const RecoJetBase* selJet1_Wjj = nullptr;
    const RecoJetBase* selJet2_Wjj = nullptr;
    if ( selJetAK8_Hbb ) 
    {
      selJet1_Wjj = convert_to_RecoJet(jpa.wjet1(), cleanedJetsAK4_wrtHbb);
      selJet2_Wjj = convert_to_RecoJet(jpa.wjet2(), cleanedJetsAK4_wrtHbb);
    } 
    else
    {
      selJet1_Hbb = convert_to_RecoJet(jpa.bjet1(), selJetsAK4);
      selJet2_Hbb = convert_to_RecoJet(jpa.bjet2(), selJetsAK4);
      selJet1_Wjj = convert_to_RecoJet(jpa.wjet1(), selJetsAK4);
      selJet2_Wjj = convert_to_RecoJet(jpa.wjet2(), selJetsAK4);
    }
    double jpaScore = jpa.jpaScore();

    std::vector<const RecoJetBase*> selJets_Hbb;
    if ( selJet1_Hbb ) selJets_Hbb.push_back(selJet1_Hbb);
    if ( selJet2_Hbb ) selJets_Hbb.push_back(selJet2_Hbb);
    std::sort(selJets_Hbb.begin(), selJets_Hbb.end(), isHigherPt);
    const RecoJetBase* selJet_Hbb_lead = ( selJets_Hbb.size() >= 1 ) ? selJets_Hbb[0] : nullptr;
    Particle::LorentzVector selJetP4_Hbb_lead;
    if ( selJet_Hbb_lead ) selJetP4_Hbb_lead = selJet_Hbb_lead->p4();
    const RecoJetBase* selJet_Hbb_sublead = ( selJets_Hbb.size() >= 2 ) ? selJets_Hbb[1] : nullptr;
    Particle::LorentzVector selJetP4_Hbb_sublead;
    if ( selJet_Hbb_sublead ) selJetP4_Hbb_sublead = selJet_Hbb_sublead->p4();

    std::vector<const RecoJetBase*> selJets_Wjj;
    if ( selJet1_Wjj ) selJets_Wjj.push_back(selJet1_Wjj);
    if ( selJet2_Wjj ) selJets_Wjj.push_back(selJet2_Wjj);
    std::sort(selJets_Wjj.begin(), selJets_Wjj.end(), isHigherPt);
    const RecoJetBase* selJet_Wjj_lead = ( selJets_Wjj.size() >= 1 ) ? selJets_Wjj[0] : nullptr;
    Particle::LorentzVector selJetP4_Wjj_lead;
    if ( selJet_Wjj_lead ) selJetP4_Wjj_lead = selJet_Wjj_lead->p4();
    const RecoJetBase* selJet_Wjj_sublead = ( selJets_Wjj.size() >= 2 ) ? selJets_Wjj[1] : nullptr;
    Particle::LorentzVector selJetP4_Wjj_sublead;
    if ( selJet_Wjj_sublead ) selJetP4_Wjj_sublead = selJet_Wjj_sublead->p4();

    // select VBF jet candidates
    std::vector<const RecoJet*> selJetsAK4_vbf;
    if ( selJetAK8_Hbb ) {
      std::vector<const RecoJetBase*> overlaps;
      if ( selJet1_Wjj ) overlaps.push_back(selJet1_Wjj);
      if ( selJet2_Wjj ) overlaps.push_back(selJet2_Wjj);
      selJetsAK4_vbf = jetCleanerAK4_dR08(cleanedJetsAK4_vbf_wrtHbb, overlaps);
    } else {
      std::vector<const RecoJetBase*> overlaps;
      if ( selJet1_Hbb ) overlaps.push_back(selJet1_Hbb);
      if ( selJet2_Hbb ) overlaps.push_back(selJet2_Hbb);
      if ( selJet1_Wjj ) overlaps.push_back(selJet1_Wjj);
      if ( selJet2_Wjj ) overlaps.push_back(selJet2_Wjj);
      selJetsAK4_vbf = jetCleanerAK4_dR08(selJetsAK4_vbf_postLeptonCleaning, overlaps);
    }
    if(isDEBUG)
    {
      printCollection("selJetsAK4_vbf", selJetsAK4_vbf);
    }

//--- compute MHT and linear MET discriminant (met_LD)
    const std::vector<const RecoJet*> selJetsAK4_mht = jetSelectorAK4_wPileupJetId(cleanedJetsAK4_wrtLeptons, isHigherPt);
    Particle::LorentzVector mhtP4 = compMHT(fakeableLeptons, {}, selJetsAK4_mht);
    double met_LD = compMEt_LD(metP4, mhtP4);

    // compute HT and STMET variables used for signal extraction in EXO analyses
    std::vector<const RecoJetBase*> selJets_HT_and_STMET;
    selJets_HT_and_STMET.insert(selJets_HT_and_STMET.end(), selJets_Hbb.begin(), selJets_Hbb.end());
    selJets_HT_and_STMET.insert(selJets_HT_and_STMET.end(), selJets_Wjj.begin(), selJets_Wjj.end());
    double HT = compHT(fakeableLeptons, {}, selJets_HT_and_STMET);
    double STMET = compSTMEt(fakeableLeptons, {}, selJets_HT_and_STMET, met.p4());

    Particle::LorentzVector HbbP4;
    Particle::LorentzVector HbbP4_reg;
    double m_Hbb = -1.;
    double m_Hbb_regCorr = -1.;
    double m_Hbb_regRes = -1.;
    double dR_Hbb = -1.;
    double dPhi_Hbb = -1.;
    double pT_Hbb = -1.;
    double eta_Hbb = -10.;
    double cosThetaS_Hbb = -10.;
    double cosThetaS_Hbb_reg = -10.;
    if ( selJet_Hbb_lead && selJet_Hbb_sublead ) {
      cosThetaS_Hbb = comp_cosThetaStar(selJetP4_Hbb_lead, selJetP4_Hbb_sublead);
      HbbP4 = selJetP4_Hbb_lead + selJetP4_Hbb_sublead;
      m_Hbb = HbbP4.mass();
      if ( dynamic_cast<const RecoJet*>(selJet_Hbb_lead) && dynamic_cast<const RecoJet*>(selJet_Hbb_sublead) )
      {
        const RecoJet* selJetAK4_Hbb_lead    = dynamic_cast<const RecoJet*>(selJet_Hbb_lead);
        const RecoJet* selJetAK4_Hbb_sublead = dynamic_cast<const RecoJet*>(selJet_Hbb_sublead);
        cosThetaS_Hbb_reg = comp_cosThetaStar(selJetAK4_Hbb_lead->p4_bRegCorr(), selJetAK4_Hbb_sublead->p4_bRegCorr());
        HbbP4_reg = selJetAK4_Hbb_lead->p4_bRegCorr() + selJetAK4_Hbb_sublead->p4_bRegCorr(); 
        m_Hbb_regCorr = HbbP4_reg.mass();
        m_Hbb_regRes  = m_Hbb_regCorr*TMath::Sqrt(
         mem::square(selJetAK4_Hbb_lead->bRegRes()/selJetAK4_Hbb_lead->bRegCorr())
       + mem::square(selJetAK4_Hbb_sublead->bRegRes()/selJetAK4_Hbb_sublead->bRegCorr()));
      }
      dR_Hbb = deltaR(selJetP4_Hbb_lead, selJetP4_Hbb_sublead);
      dPhi_Hbb = TMath::Abs(deltaPhi(selJetP4_Hbb_lead.phi(), selJetP4_Hbb_sublead.phi())); // CV: map dPhi into interval [0..pi]
      pT_Hbb = HbbP4.pt();
      eta_Hbb = HbbP4.eta();
    }
    Particle::LorentzVector WjjP4 = selJetP4_Wjj_lead + selJetP4_Wjj_sublead;
    Particle::LorentzVector neutrinoP4_B2G_18_008;
    if ( selJet1_Wjj && selJet2_Wjj )
    {
      neutrinoP4_B2G_18_008 = comp_metP4_B2G_18_008(selLeptonP4 + selJet1_Wjj->p4() + selJet2_Wjj->p4(), metP4.px(), metP4.py(), higgsBosonMass);
    }
    else
    {
      neutrinoP4_B2G_18_008 = metP4;
    }
    Particle::LorentzVector WlnuP4 = selLeptonP4 + neutrinoP4_B2G_18_008;
    Particle::LorentzVector HwwP4 = WjjP4 + WlnuP4;
    Particle::LorentzVector HHP4 = HbbP4 + HwwP4;
    double m_Wjj = -1.;
    double dR_Wjj = -1.;
    double dPhi_Wjj = -1.;
    double pT_Wjj = -1.;
    double cosThetaS_Wjj = -10.;
    if ( selJet_Wjj_lead && selJet_Wjj_sublead ) 
    {
      cosThetaS_Wjj = comp_cosThetaStar(selJetP4_Wjj_lead, selJetP4_Wjj_sublead);
      m_Wjj = WjjP4.mass();
      dR_Wjj = deltaR(selJetP4_Wjj_lead, selJetP4_Wjj_sublead);
      dPhi_Wjj = TMath::Abs(deltaPhi(selJetP4_Wjj_lead.phi(), selJetP4_Wjj_sublead.phi()));
      pT_Wjj = WjjP4.pt();
    }
    double tau21_Wjj = ( selJetAK8_Wjj ) ? selJetAK8_Wjj->tau2()/selJetAK8_Wjj->tau1() : -1.;
    double dR_Hww = -1.;
    double dPhi_Hww = -1.;
    double cosThetaS_WW = -10.;
    double pT_Hww = -1.;
    double Smin_Hww = -1.;
    if ( selJet_Wjj_lead && selJet_Wjj_sublead ) 
    {
      dR_Hww = deltaR(WjjP4, WlnuP4);
      dPhi_Hww = TMath::Abs(deltaPhi(WjjP4.phi(), WlnuP4.phi()));
      cosThetaS_WW = comp_cosThetaStar(WjjP4, WlnuP4);
      pT_Hww = HwwP4.pt();
      Smin_Hww = comp_Smin(WjjP4 + selLeptonP4, metP4.px(), metP4.py());
    }

    double dR_b1lep = ( selJet_Hbb_lead ) ? deltaR(selJetP4_Hbb_lead, selLeptonP4) : -1;
    double dR_b2lep = ( selJet_Hbb_sublead ) ? deltaR(selJetP4_Hbb_sublead, selLeptonP4) : -1;
    Particle::LorentzVector HHvisP4 = HbbP4 + WjjP4 + selLeptonP4;
    double m_HHvis = HHvisP4.mass();
    double pT_HHvis = HHvisP4.pt();
    double eta_HHvis = HHvisP4.eta();
    double dPhi_HHvis = TMath::Abs(deltaPhi(HbbP4.phi(), (WjjP4 + selLeptonP4).phi()));
    double Smin_HH = comp_Smin(HHvisP4, metP4.px(), metP4.py());
    double m_HH = (HbbP4 + WjjP4 + selLeptonP4 + metP4).mass();
    double m_HH_B2G_18_008 = HHP4.mass();
    double pT_HH = (HbbP4 + WjjP4 + selLeptonP4 + metP4).pt();
    double dPhi_HH = TMath::Abs(deltaPhi(HbbP4.phi(), (WjjP4 + selLeptonP4 + metP4).phi()));
    double dR_HH = deltaR(HbbP4, WjjP4 + selLeptonP4 + metP4);
    double cosThetaS_HH = comp_cosThetaStar(HbbP4, WjjP4 + selLeptonP4 + metP4);

    double mT_W = mT2_2particle::comp_mT(selLeptonP4.px(), selLeptonP4.py(), selLeptonP4.mass(), metP4.px(), metP4.py(), 0.);
    double mT_top_2particle_permutation1 = ( selJets_Hbb.size() ) ? 
      mT2_2particle::comp_mT(
	selJetP4_Hbb_lead.px(), selJetP4_Hbb_lead.py(), selJetP4_Hbb_lead.mass(),
	selLeptonP4.px() + metP4.px(), selLeptonP4.py() + metP4.py(), wBosonMass) 
      : 1000;
    double mT_top_2particle_permutation2 = ( selJets_Hbb.size() >1 ) ?
      mT2_2particle::comp_mT(
        selJetP4_Hbb_sublead.px(), selJetP4_Hbb_sublead.py(), selJetP4_Hbb_sublead.mass(),
        selLeptonP4.px() + metP4.px(), selLeptonP4.py() + metP4.py(), wBosonMass)
      : 1000;
    double mT_top_2particle = TMath::Min(mT_top_2particle_permutation1, mT_top_2particle_permutation2);
    double mT_top_3particle_permutation1 = ( selJets_Hbb.size() ) ?
      mT2_3particle::comp_mT(
        selJetP4_Hbb_lead.px(), selJetP4_Hbb_lead.py(), selJetP4_Hbb_lead.mass(),
        selLeptonP4.px(), selLeptonP4.py(), selLeptonP4.mass(), metP4.px(), metP4.py(), 0.) 
      : 1000.;
    double mT_top_3particle_permutation2 = ( selJets_Hbb.size() >1 ) ?
      mT2_3particle::comp_mT(
        selJetP4_Hbb_sublead.px(), selJetP4_Hbb_sublead.py(), selJetP4_Hbb_sublead.mass(),
        selLeptonP4.px(), selLeptonP4.py(), selLeptonP4.mass(), metP4.px(), metP4.py(), 0.)
      : 1000.;
    double mT_top_3particle = TMath::Min(mT_top_3particle_permutation1, mT_top_3particle_permutation2);

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
	if ( dEta_jj > 3.0 && m_jj > 500. ) 
        {
	  if ( m_jj > vbf_m_jj ) // CV: in case of ambiguity, take the jet pair of highest mass
          {
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

    double mindr_lep1_jet = comp_mindr_jet(*selLepton, selJetsAK4);
    double min_Deta_mostfwdJet_jet = 0;
    double min_Deta_leadfwdJet_jet = 0;
    // take the highest eta selJetsForward
    Particle::LorentzVector mostFwdJet = HighestEtaFwdJet(selJetsForward);
    if ( selJetsForward.size() >= 1 && selJetsAK4.size() >= 1 )
    {
      min_Deta_mostfwdJet_jet = min_Deta_fwdJet_jet(mostFwdJet, selJetsAK4);
      Particle::LorentzVector leadFwdJet = selJetsForward[0]-> p4();
      min_Deta_leadfwdJet_jet = min_Deta_fwdJet_jet(leadFwdJet, selJetsAK4);
    }

    const std::map<std::string, Particle> ll_inputs = {
      { "bjet1",  Particle(selJetP4_Hbb_lead)    },
      { "bjet2",  Particle(selJetP4_Hbb_sublead) },
      { "wjet1",  Particle(selJetP4_Wjj_lead)    },
      { "wjet2",  Particle(selJetP4_Wjj_sublead) },
      { "lep",    Particle(selLepton->p4())      }
    };
    std::map<std::string, const Particle *> ll_inputs_ptr;
    for( const auto & kv: ll_inputs )
    {
      ll_inputs_ptr[kv.first] = &kv.second;
    }

    double bjet1_btagCSV = ( selJetAK8_Hbb ) ? selJetAK8_Hbb->subJet1()->BtagCSV() : ( (selJet1_Hbb) ? dynamic_cast<const RecoJet*>(selJet1_Hbb)->BtagCSV() : -1 );
    double bjet2_btagCSV = ( selJetAK8_Hbb ) ? selJetAK8_Hbb->subJet2()->BtagCSV() : ( (selJet2_Hbb) ? dynamic_cast<const RecoJet*>(selJet2_Hbb)->BtagCSV() : -1 );
    double wjet1_btagCSV = (selJet1_Wjj) ? dynamic_cast<const RecoJet*>(selJet1_Wjj)->BtagCSV() : -1;
    double wjet2_btagCSV = (selJet2_Wjj) ? dynamic_cast<const RecoJet*>(selJet2_Wjj)->BtagCSV() : -1;

    int numBJets_jpa_loose, numBJets_jpa_medium;
    countBJets_jpa(selJetAK8_Hbb, selJet1_Hbb, selJet2_Hbb, jetSelectorAK8_Hbb, jetSelectorAK4_bTagLoose, jetSelectorAK4_bTagMedium, numBJets_jpa_loose, numBJets_jpa_medium);
    int numWJets_jpa = 0;
    if ( selJet1_Wjj ) ++numWJets_jpa;
    if ( selJet2_Wjj ) ++numWJets_jpa;
    int numBJets_jpa = 0;
    if ( selJet1_Hbb ) ++numBJets_jpa;
    if ( selJet2_Hbb ) ++numBJets_jpa;

    std::map<std::string, double> mvaInputVariables_list = {
      {"numBJets_jpa_medium",     numBJets_jpa_medium},
      {"lep_pt",                  selLepton->pt()},
      {"lep_conePt",              comp_lep_conePt(*selLepton)},
      {"lep_eta",                 selLepton->eta()},
      {"lep_e",                 selLepton->p4().energy()},
      {"lep_phi",                 selLepton->phi()},
      {"lep_mass",                selLepton->mass()},
      {"bjet1_e",                selJetP4_Hbb_lead.e()},
      {"bjet1_pt",                selJetP4_Hbb_lead.pt()},
      {"bjet1_eta",               selJetP4_Hbb_lead.eta()},
      {"bjet1_phi",               selJetP4_Hbb_lead.phi()},
      {"bjet1_mass",              selJetP4_Hbb_lead.mass()},
      {"bjet1_btagCSV",           bjet1_btagCSV},
      {"bjet2_pt",                selJetP4_Hbb_sublead.pt()},
      {"bjet2_eta",               selJetP4_Hbb_sublead.eta()},
      {"bjet2_phi",               selJetP4_Hbb_sublead.phi()},
      {"bjet2_mass",              selJetP4_Hbb_sublead.mass()},
      {"bjet2_btagCSV",           bjet2_btagCSV},
      {"wjet1_pt",                selJetP4_Wjj_lead.pt()},
      {"wjet1_eta",               selJetP4_Wjj_lead.eta()},
      {"wjet1_phi",               selJetP4_Wjj_lead.phi()},
      {"wjet1_e",               selJetP4_Wjj_lead.e()},
      {"wjet1_mass",              selJetP4_Wjj_lead.mass()},
      {"wjet1_btagCSV",           wjet1_btagCSV},
      {"wjet2_pt",                selJetP4_Wjj_sublead.pt()},
      {"wjet2_eta",               selJetP4_Wjj_sublead.eta()},
      {"wjet2_phi",               selJetP4_Wjj_sublead.phi()},
      {"wjet2_mass",              selJetP4_Wjj_sublead.mass()},
      {"wjet2_btagCSV",           wjet2_btagCSV},
      {"jpaScore",                jpaScore},
      {"mht",                     mhtP4.pt()},
      {"pT_Wjj",                  pT_Wjj},
      {"m_Hbb",                   m_Hbb},
      {"Smin_Hww",                Smin_Hww},
      {"tau21_Hbb",               tau21_Hbb},
      {"numBJets_loose",          selBJetsAK4_loose.size()},
      {"dR_Hbb",                  dR_Hbb},
      {"met",                     metP4.pt()},
      {"cosThetaS_Hbb_reg",       cosThetaS_Hbb_reg},
      {"pT_Hbb",                  pT_Hbb},
      {"dR_HH",                   dR_HH},
      {"dR_Wjj",                  dR_Wjj},
      {"pT_Hww",                  pT_Hww},
      {"m_HHvis",                 m_HHvis},
      {"dPhi_HHvis",              dPhi_HHvis},
      {"pT_HH",                   pT_HH},
      {"pT_HHvis",                pT_HHvis},
      {"avg_dr_jet_central",      comp_avg_dr_jet(selJetsAK4)},
      {"mbb_loose",               selBJetsAK4_loose.size() >= 2 ? (selBJetsAK4_loose[0]->p4() + selBJetsAK4_loose[1]->p4()).mass() : 0.},
      {"mbb_medium",              selBJetsAK4_medium.size() >= 2 ? (selBJetsAK4_medium[0]->p4() + selBJetsAK4_medium[1]->p4()).mass() : 0.},
      {"numJets",                 selJetsAK4.size()},
      {"mindr_lep1_jet",          mindr_lep1_jet},
      {"m_Hbb_regCorr",           m_Hbb_regCorr},
      {"m_HH",                    m_HH},
      {"m_HH_B2G_18_008",         m_HH_B2G_18_008},
      {"dR_Hww",                  dR_Hww},
      {"m_Wjj",                   m_Wjj},
      {"cosThetaS_Hbb",           cosThetaS_Hbb},
      {"cosThetaS_Wjj",           cosThetaS_Wjj},
      {"cosThetaS_WW",            cosThetaS_WW},
      {"cosThetaS_HH",            cosThetaS_HH},
      {"numBJets_medium",         selBJetsAK4_medium.size()},
      {"dR_b1lep",                dR_b1lep},
      {"dR_b2lep",                dR_b2lep},
      {"met_LD",                  met_LD},
      {"mT_W",                    mT_W},
      {"mT_top_3particle",        mT_top_3particle},
      {"mT_top_2particle",        mT_top_2particle},
      {"HT",                      HT},
      {"eta_Hbb",                 eta_Hbb},
      {"leadFwdJet_pt",           selJetsForward.size() >= 1 ? selJetsForward[0]->pt() : -1000.},
      {"mll_loose",               preselLeptonsFull.size() >= 2 ? (preselLeptonsFull[0]->p4() + preselLeptonsFull[1]->p4()).mass() : 0.},
      {"numLeptons",              preselLeptonsFull.size()},
      {"STMET",                   STMET},
      {"Smin_HH",                 Smin_HH},
      {"vbf_dEta_jj",             vbf_dEta_jj},
      {"vbf_m_jj",                vbf_m_jj},
      {"selLepton_type",          selLepton_type},
      {"dPhi_Hbb",                dPhi_Hbb},
      {"dPhi_HH",                 dPhi_HH}
    };

    if ( bdt_filler ) {

      double lep_frWeight = ( selLepton->genLepton() ) ? 1. : evtWeightRecorder.get_jetToLepton_FR_lead(central_or_shift_main);

      std::map<std::string, double> weightMapHH;
      if ( apply_HH_rwgt || apply_HH_rwgt_LOtoNLO )
      {
        for ( unsigned int i = 0; i < HHWeightNames.size(); i++ )
        {
          double HHReweight = 1.;
          if ( apply_HH_rwgt )
          {
            assert(HHWeight_calc);
            HHReweight = HHWeight_calc->getWeight(HHBMNames[i], eventInfo.gen_mHH, eventInfo.gen_cosThetaStar, isDEBUG);
          }
          if ( apply_HH_rwgt_LOtoNLO )
          {
            assert(HHWeight_calc_LOtoNLO);
            HHReweight *= HHWeight_calc_LOtoNLO->getReWeight(HHBMNames[i], eventInfo.gen_mHH, eventInfo.gen_cosThetaStar, isDEBUG);
          }
          weightMapHH[HHWeightNames[i]] = HHReweight;
        }
      }

      bdt_filler -> operator()({ eventInfo.run, eventInfo.lumi, eventInfo.event })
	("jpaScore",             jpaScore)
	("bjet1_btagCSV",        bjet1_btagCSV)
	("bjet2_btagCSV",        bjet2_btagCSV)
	("wjet1_btagCSV",        wjet1_btagCSV)
        ("wjet2_btagCSV",        wjet2_btagCSV)
	("lep_pt",               selLepton->pt())
	("lep_conePt",           comp_lep_conePt(*selLepton))
	("lep_eta",              selLepton->eta())
	("lep_phi",              selLepton->phi())
	("lep_mass",             selLepton->mass())
	("lep_charge",           selLepton->charge())
	("lep_e",                selLepton->p4().e())
        ("lep_px",               selLepton->p4().px())
        ("lep_py",               selLepton->p4().py())
        ("lep_pz",               selLepton->p4().pz())
        ("lep_frWeight",         lep_frWeight)
	("bjet1_pt",             selJetP4_Hbb_lead.pt())
	("bjet1_eta",            selJetP4_Hbb_lead.eta())
	("bjet1_phi",            selJetP4_Hbb_lead.phi())
	("bjet1_mass",           selJetP4_Hbb_lead.mass())
	("bjet1_e", selJetP4_Hbb_lead.energy())
	("bjet1_px",             selJetP4_Hbb_lead.px())
        ("bjet1_py",             selJetP4_Hbb_lead.py())
        ("bjet1_pz",             selJetP4_Hbb_lead.pz())
	("wjet1_pt",             selJetP4_Wjj_lead.pt())
	("wjet1_eta",            selJetP4_Wjj_lead.eta())
        ("wjet1_phi",            selJetP4_Wjj_lead.phi())
        ("wjet1_mass",           selJetP4_Wjj_lead.mass())
	("wjet1_e",              selJetP4_Wjj_lead.energy())
        ("wjet1_px",             selJetP4_Wjj_lead.px())
	("wjet1_py",             selJetP4_Wjj_lead.py())
	("wjet1_pz",             selJetP4_Wjj_lead.pz())
	("bjet2_pt",             selJetP4_Hbb_sublead.pt())
	("bjet2_eta",            selJetP4_Hbb_sublead.eta())
	("bjet2_phi",            selJetP4_Hbb_sublead.phi())
	("bjet2_mass",           selJetP4_Hbb_sublead.mass())
	("bjet2_e",              selJetP4_Hbb_sublead.energy())
        ("bjet2_px",             selJetP4_Hbb_sublead.px())
        ("bjet2_py",             selJetP4_Hbb_sublead.py())
        ("bjet2_pz",             selJetP4_Hbb_sublead.pz())
	("wjet2_pt",             selJetP4_Wjj_sublead.pt())
	("wjet2_eta",            selJetP4_Wjj_sublead.eta())
        ("wjet2_phi",            selJetP4_Wjj_sublead.phi())
        ("wjet2_mass",           selJetP4_Wjj_sublead.mass())
	("wjet2_e",              selJetP4_Wjj_sublead.energy())
        ("wjet2_px",             selJetP4_Wjj_sublead.px())
        ("wjet2_py",             selJetP4_Wjj_sublead.py())
        ("wjet2_pz",             selJetP4_Wjj_sublead.pz())
	("met",                  metP4.pt())
	("mht",                  mhtP4.pt())
	("met_LD",               met_LD)
	("HT",                   HT)
	("STMET",                STMET)
	("m_Hbb",                m_Hbb)
	("m_Hbb_regCorr",        m_Hbb_regCorr)
	("m_Hbb_regRes",         m_Hbb_regRes)
	("dR_Hbb",               dR_Hbb)
	("dPhi_Hbb",             dPhi_Hbb)
	("pT_Hbb",               pT_Hbb)
	("eta_Hbb",              eta_Hbb)
	("tau21_Hbb",            tau21_Hbb)
	("cosThetaS_Hbb",        cosThetaS_Hbb)
	("cosThetaS_Hbb_reg",    cosThetaS_Hbb_reg)
	("m_Wjj",                m_Wjj)
	("dR_Wjj",               dR_Wjj)
	("dPhi_Wjj",             dPhi_Wjj)
	("pT_Wjj",               pT_Wjj)
	("tau21_Wjj",            tau21_Wjj)
	("dR_Hww",               dR_Hww)
	("dPhi_Hww",             dPhi_Hww)
	("Smin_Hww",             Smin_Hww)
	("pT_Hww",               pT_Hww)
	("m_HHvis",              m_HHvis)
	("pT_HHvis",             pT_HHvis)
        ("eta_HHvis",            eta_HHvis)
	("dPhi_HHvis",           dPhi_HHvis)
	("m_HH",                 m_HH)
        ("m_HH_B2G_18_008",      m_HH_B2G_18_008)
	("pT_HH",                pT_HH)
	("dPhi_HH",              dPhi_HH)
	("Smin_HH",              Smin_HH)
	("dR_HH",                dR_HH)
	("cosThetaS_Wjj",        cosThetaS_Wjj)
	("cosThetaS_WW",         cosThetaS_WW)
	("cosThetaS_HH",         cosThetaS_HH)
	("dR_b1lep",             dR_b1lep)
	("dR_b2lep",             dR_b2lep)
	("mT_W",                 mT_W)
	("mT_top_2particle",     mT_top_2particle)
	("mT_top_3particle",     mT_top_3particle)
	("vbf_jet1_pt",          vbf_jet1_pt)
	("vbf_jet1_eta",         vbf_jet1_eta)
	("vbf_jet2_pt",          vbf_jet2_pt)
	("vbf_jet2_eta",         vbf_jet2_eta)
	("vbf_dEta_jj",          vbf_dEta_jj)
	("vbf_m_jj",             vbf_m_jj)
	("genWeight",            eventInfo.genWeight)
	("evtWeight",            evtWeightRecorder.get(central_or_shift_main))
	("numJets",              comp_n_jet25_recl(selJetsAK4))
	("isHbb_boosted",        selJetAK8_Hbb ? true : false)
        ("isWjj_boosted",        selJetsAK8_Wjj.size() >= 1 ? true : false)
	("isVBF",                isVBF)
	("mhh_gen",              eventInfo.gen_mHH)
	("costS_gen",            eventInfo.gen_cosThetaStar)
	("mindr_lep1_jet",       mindr_lep1_jet )
	("avg_dr_jet_central",   comp_avg_dr_jet(selJetsAK4))
	("mbb_loose",            selBJetsAK4_loose.size() >= 2 ? (selBJetsAK4_loose[0]->p4() + selBJetsAK4_loose[1]->p4()).mass() : 0)
	("mbb_medium",           selBJetsAK4_medium.size() >= 2 ? (selBJetsAK4_medium[0]->p4() + selBJetsAK4_medium[1]->p4()).mass() : 0)
	("mll_loose",            preselLeptonsFull.size() >= 2 ? (preselLeptonsFull[0]->p4() + preselLeptonsFull[1]->p4()).mass() : 0)
	("numLeptons_loose",     preselLeptonsFull.size())
	("lepPairCharge_loose",  preselLeptonsFull.size() >= 2 ? preselLeptonsFull[0]->charge() + preselLeptonsFull[1]->charge() : 999)
	("selLepton_charge",     preselLeptonsFull[0]->charge())
	("selLepton_type",       selLepton_type)
	("lepPairType_loose",    preselLeptonsFull.size() >= 2 ? fabs(preselLeptonsFull[0]->pdgId()) == fabs(preselLeptonsFull[1]->pdgId()) : 999)
	("numElectrons",         selElectrons.size())
	("numBJets_loose",       selBJetsAK4_loose.size())
	("numBJets_medium",      selBJetsAK4_medium.size())
        ("numBJets_jpa_loose",   numBJets_jpa_loose)
        ("numBJets_jpa_medium",  numBJets_jpa_medium)
	("numBJets_jpa",         numBJets_jpa)
	("numWJets_jpa",         numWJets_jpa)
        ("numJets_vbf",          selJetsAK4_vbf.size())
	("mostFwdJet_eta",       selJetsForward.size() >= 1 ? std::abs(mostFwdJet.Eta()) : -1000)
	("mostFwdJet_pt",        selJetsForward.size() >= 1 ? mostFwdJet.pt() : -1000)
	("mostFwdJet_phi",       selJetsForward.size() >= 1 ? mostFwdJet.phi() : -1000)
	("mostFwdJet_E",         selJetsForward.size() >= 1 ? mostFwdJet.energy() : -1000)
	("leadFwdJet_eta",       selJetsForward.size() >= 1 ? selJetsForward[0] -> absEta() : -1000)
	("leadFwdJet_pt",        selJetsForward.size() >= 1 ? selJetsForward[0] -> pt() : -1000)
	("leadFwdJet_phi",       selJetsForward.size() >= 1 ? selJetsForward[0] -> phi() : -1000)
	("leadFwdJet_E",         selJetsForward.size() >= 1 ? selJetsForward[0] -> p4().energy() : -1000)
	("numJetsForward",       selJetsForward.size())
	(weightMapHH)
        .fill()
	;
      continue;
    }

//--- compute event-level BDT outputs
    std::map<std::string, double> bdtOutputs_resonant_spin2;
    std::map<std::string, double> bdtOutputs_resonant_spin0;
    std::map<std::string, double> bdtOutputs_nonresonant;
    double bdtOutputs_nonresonant_all(-1.);
    if ( fillHistograms_BDT )
    {
      if ( selJetAK8_Hbb )
      {
        std::map<std::string, double> bdtInputs_resonant_spin2 = InitializeInputVarMap(mvaInputVariables_list, BDT_resonant_spin2_boosted[0]->mvaInputVariables(), true); // FIXME: set to false
        bdtOutputs_resonant_spin2 = CreateBDTOutputMap(gen_mHH, BDT_resonant_spin2_boosted, bdtInputs_resonant_spin2, eventInfo.event, false, "_spin2");
        std::map<std::string, double> bdtInputs_resonant_spin0 = InitializeInputVarMap(mvaInputVariables_list, BDT_resonant_spin0_boosted[0]->mvaInputVariables(), true); // FIXME: set to false
        bdtOutputs_resonant_spin0 = CreateBDTOutputMap(gen_mHH, BDT_resonant_spin0_boosted, bdtInputs_resonant_spin0, eventInfo.event, false, "_spin0");

        std::map<std::string, double> bdtInputs_nonresonant = InitializeInputVarMap(mvaInputVariables_list, BDT_nonresonant_boosted[0]->mvaInputVariables());
        bdtOutputs_nonresonant = CreateBDTOutputMap(nonRes_BMs, BDT_nonresonant_boosted, bdtInputs_nonresonant, eventInfo.event, true, "");
        bdtOutputs_nonresonant_all = (*BDT_nonresonant_boosted[BDT_nonresonant_boosted.size()-1])(bdtInputs_nonresonant, eventInfo.event);
      }
      else
      {
        std::map<std::string, double> bdtInputs_resonant_spin2 = InitializeInputVarMap(mvaInputVariables_list, BDT_resonant_spin2_resolved[0]->mvaInputVariables(), true); // FIXME: set to false
        bdtOutputs_resonant_spin2 = CreateBDTOutputMap(gen_mHH, BDT_resonant_spin2_resolved, bdtInputs_resonant_spin2, eventInfo.event, false, "_spin2");
        std::map<std::string, double> bdtInputs_resonant_spin0 = InitializeInputVarMap(mvaInputVariables_list, BDT_resonant_spin0_resolved[0]->mvaInputVariables(), true); // FIXME: set to false
        bdtOutputs_resonant_spin0 = CreateBDTOutputMap(gen_mHH, BDT_resonant_spin0_resolved, bdtInputs_resonant_spin0, eventInfo.event, false, "_spin0");

        std::map<std::string, double> bdtInputs_nonresonant = InitializeInputVarMap(mvaInputVariables_list, BDT_nonresonant_resolved[0]->mvaInputVariables());
        bdtOutputs_nonresonant = CreateBDTOutputMap(nonRes_BMs, BDT_nonresonant_resolved, bdtInputs_nonresonant, eventInfo.event, true, "");
        bdtOutputs_nonresonant_all = (*BDT_nonresonant_resolved[BDT_nonresonant_resolved.size()-1])(bdtInputs_nonresonant, eventInfo.event);
        //assert(0);
      }
    }

//--- compute event-level LBN outputs
    std::map<std::string, std::map<std::string, double>> lbnOutputs_resonant_spin2;
    std::map<std::string, std::map<std::string, double>> lbnOutputs_resonant_spin0;
    std::map<std::string, std::map<std::string, double>> lbnOutputs_nonresonant;
    std::map<std::string, double> lbnOutputs_nonresonant_all;
    if ( fillHistograms_LBN )
    {
      if ( selJetAK8_Hbb )
      {
        std::map<std::string, double> hl_inputs_resonant_spin2 = InitializeInputVarMap(mvaInputVariables_list, LBN_resonant_spin2_boosted[0]->hl_mvaInputVariables(), true); // FIXME: set to false
        lbnOutputs_resonant_spin2 = CreateLBNOutputMap(gen_mHH, LBN_resonant_spin2_boosted, ll_inputs_ptr, hl_inputs_resonant_spin2, eventInfo.event, false, "_spin2");
        std::map<std::string, double> hl_inputs_resonant_spin0 = InitializeInputVarMap(mvaInputVariables_list, LBN_resonant_spin0_boosted[0]->hl_mvaInputVariables(), true); // FIXME: set to false
        lbnOutputs_resonant_spin0 = CreateLBNOutputMap(gen_mHH, LBN_resonant_spin0_boosted, ll_inputs_ptr, hl_inputs_resonant_spin0, eventInfo.event, false, "_spin0");

        std::map<std::string, double> hl_inputs_nonresonant = InitializeInputVarMap(mvaInputVariables_list, LBN_nonresonant_boosted[0]->hl_mvaInputVariables());
        lbnOutputs_nonresonant = CreateLBNOutputMap(nonRes_BMs, LBN_nonresonant_boosted, ll_inputs_ptr, hl_inputs_nonresonant, eventInfo.event, true, "");
        lbnOutputs_nonresonant_all = (*LBN_nonresonant_boosted[LBN_nonresonant_boosted.size()-1])(ll_inputs_ptr, hl_inputs_nonresonant, eventInfo.event);
      }
      else
      {
        std::map<std::string, double> hl_inputs_resonant_spin2 = InitializeInputVarMap(mvaInputVariables_list, LBN_resonant_spin2_resolved[0]->hl_mvaInputVariables(), true); // FIXME: set to false
        lbnOutputs_resonant_spin2 = CreateLBNOutputMap(gen_mHH, LBN_resonant_spin2_resolved, ll_inputs_ptr, hl_inputs_resonant_spin2, eventInfo.event, false, "_spin2");
        std::map<std::string, double> hl_inputs_resonant_spin0 = InitializeInputVarMap(mvaInputVariables_list, LBN_resonant_spin0_resolved[0]->hl_mvaInputVariables(), true); // FIXME: set to false
        lbnOutputs_resonant_spin0 = CreateLBNOutputMap(gen_mHH, LBN_resonant_spin0_resolved, ll_inputs_ptr, hl_inputs_resonant_spin0, eventInfo.event, false, "_spin0");

        std::map<std::string, double> hl_inputs_nonresonant = InitializeInputVarMap(mvaInputVariables_list, LBN_nonresonant_resolved[0]->hl_mvaInputVariables());
        lbnOutputs_nonresonant = CreateLBNOutputMap(nonRes_BMs, LBN_nonresonant_resolved, ll_inputs_ptr, hl_inputs_nonresonant, eventInfo.event, true, "");
        lbnOutputs_nonresonant_all = (*LBN_nonresonant_resolved[LBN_nonresonant_resolved.size()-1])(ll_inputs_ptr, hl_inputs_nonresonant, eventInfo.event);
        //        assert(0);
      }
    }

//--- retrieve gen-matching flags
    std::vector<const GenMatchEntry*> genMatches = genMatchInterface.getGenMatch(selLeptons);

//--- fill histograms with events passing final selection
    for(const std::string & central_or_shift: central_or_shifts_local)
    {
      const double evtWeight = evtWeightRecorder.get(central_or_shift);
      const bool skipFilling = central_or_shift != central_or_shift_main;
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
          selHistManager->evt_->fillHistograms(
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
            m_HHvis, m_HH, m_HH_B2G_18_008, dR_HH, dPhi_HH, pT_HH, Smin_HH,
            mT_W, mT_top_2particle, mT_top_3particle,
            vbf_jet1_pt, vbf_jet1_eta, vbf_jet2_pt, vbf_jet2_eta, vbf_m_jj, vbf_dEta_jj, vbf_lhe_m_jj, vbf_lhe_dEta_jj,
            jpa, selJetAK8_Hbb,
            evtWeight
          );
          if ( isSignal )
          {
            selHistManager->genKinematics_HH_->fillHistograms(evtWeight);
          }
        }

        if ( fillHistograms_BDT )
        {
          eventCategory_BDT.set(selJetAK8_Hbb != nullptr, selBJetsAK4_medium.size(), isVBF);
          selHistManager->datacard_BDT_->fillHistograms(
            bdtOutputs_resonant_spin2,
            bdtOutputs_resonant_spin0,
            bdtOutputs_nonresonant,
            bdtOutputs_nonresonant_all, // CV: bdtOutput for nonresonant_allBMs case not implemented yet !!
            evtWeight
          );
        }
        if ( fillHistograms_LBN )
        {
          eventCategory_LBN.set(selJetAK8_Hbb != nullptr, selBJetsAK4_medium.size(), isVBF);
          selHistManager->datacard_LBN_->fillHistograms(
            lbnOutputs_resonant_spin2,
            lbnOutputs_resonant_spin0,
            lbnOutputs_nonresonant,
            lbnOutputs_nonresonant_all, // CV: lbnOutput for nonresonant_allBMs case not implemented yet !!
            evtWeight
          );
        }

        if(! skipFilling)
        {
          selHistManager->evtYield_->fillHistograms(eventInfo, evtWeight);
          selHistManager->weights_->fillHistograms("genWeight", eventInfo.genWeight);
          selHistManager->weights_->fillHistograms("pileupWeight", evtWeightRecorder.get_puWeight(central_or_shift));
          selHistManager->weights_->fillHistograms("triggerWeight", evtWeightRecorder.get_sf_triggerEff(central_or_shift));
          selHistManager->weights_->fillHistograms("btagWeight", evtWeightRecorder.get_btag(central_or_shift)*evtWeightRecorder.get_btagSFRatio(central_or_shift));
          selHistManager->weights_->fillHistograms("data_to_MC_correction", evtWeightRecorder.get_data_to_MC_correction(central_or_shift));
          selHistManager->weights_->fillHistograms("fakeRate", evtWeightRecorder.get_FR(central_or_shift));
        }
      }

      if(isMC && ! skipFilling)
      {
        genEvtHistManager_afterCuts[central_or_shift]->fillHistograms(
          genElectrons, genMuons, genHadTaus, genPhotons, genJets, evtWeightRecorder.get_inclusive(central_or_shift)
        );
        lheInfoHistManager[central_or_shift]->fillHistograms(*lheInfoReader, evtWeight);
        if(eventWeightManager)
        {
          genEvtHistManager_afterCuts[central_or_shift]->fillHistograms(
            eventWeightManager, evtWeightRecorder.get_inclusive(central_or_shift)
          );
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
    /*if ( bdt_filler ) {

      double lep_frWeight = ( selLepton->genLepton() ) ? 1. : evtWeightRecorder.get_jetToLepton_FR_lead(central_or_shift_main);

      std::map<std::string, double> weightMapHH;
      if(apply_HH_rwgt)
      {
        assert(HHWeight_calc);
        for(unsigned int i =0; i < HHWeightNames.size();i++)
        {
          weightMapHH[HHWeightNames[i]] = HHWeight_calc->getWeight(HHBMNames[i], eventInfo.gen_mHH, eventInfo.gen_cosThetaStar, isDEBUG);
        }
      }

      bdt_filler -> operator()({ eventInfo.run, eventInfo.lumi, eventInfo.event })
	("jpaScore",             jpaScore)
	("bjet1_btagCSV",        bjet1_btagCSV)
	("bjet2_btagCSV",        bjet2_btagCSV)
	("wjet1_btagCSV",        wjet1_btagCSV)
        ("wjet2_btagCSV",        wjet2_btagCSV)
	("lep_pt",               selLepton->pt())
	("lep_conePt",           comp_lep_conePt(*selLepton))
	("lep_eta",              selLepton->eta())
	("lep_phi",              selLepton->phi())
	("lep_mass",             selLepton->mass())
	("lep_charge",           selLepton->charge())
	("lep_e",                selLepton->p4().e())
        ("lep_px",               selLepton->p4().px())
        ("lep_py",               selLepton->p4().py())
        ("lep_pz",               selLepton->p4().pz())
        ("lep_frWeight",         lep_frWeight)      
	("bjet1_pt",             selJetP4_Hbb_lead.pt())
	("bjet1_eta",            selJetP4_Hbb_lead.eta())
	("bjet1_phi",            selJetP4_Hbb_lead.phi())
	("bjet1_mass",           selJetP4_Hbb_lead.mass())
	("bjet1_e",              selJetP4_Hbb_lead.energy())
        ("bjet1_px",             selJetP4_Hbb_lead.px())
        ("bjet1_py",             selJetP4_Hbb_lead.py())
        ("bjet1_pz",             selJetP4_Hbb_lead.pz())
	("wjet1_pt",             selJetP4_Wjj_lead.pt())
	("wjet1_eta",            selJetP4_Wjj_lead.eta())
        ("wjet1_phi",            selJetP4_Wjj_lead.phi())
        ("wjet1_mass",           selJetP4_Wjj_lead.mass())
	("wjet1_e",              selJetP4_Wjj_lead.energy())
        ("wjet1_px",             selJetP4_Wjj_lead.px())
        ("wjet1_py",             selJetP4_Wjj_lead.py())
        ("wjet1_pz",             selJetP4_Wjj_lead.pz())
	("bjet2_pt",             selJetP4_Hbb_sublead.pt())
	("bjet2_eta",            selJetP4_Hbb_sublead.eta())
	("bjet2_phi",            selJetP4_Hbb_sublead.phi())
	("bjet2_mass",           selJetP4_Hbb_sublead.mass())
	("bjet2_e",              selJetP4_Hbb_sublead.energy())
        ("bjet2_px",             selJetP4_Hbb_sublead.px())
        ("bjet2_py",             selJetP4_Hbb_sublead.py())
        ("bjet2_pz",             selJetP4_Hbb_sublead.pz())
	("wjet2_pt",             selJetP4_Wjj_sublead.pt())
	("wjet2_eta",            selJetP4_Wjj_sublead.eta())
        ("wjet2_phi",            selJetP4_Wjj_sublead.phi())
        ("wjet2_mass",           selJetP4_Wjj_sublead.mass())
	("wjet2_e",              selJetP4_Wjj_sublead.energy())
        ("wjet2_px",             selJetP4_Wjj_sublead.px())
        ("wjet2_py",             selJetP4_Wjj_sublead.py())
        ("wjet2_pz",             selJetP4_Wjj_sublead.pz())
	("met",                  metP4.pt())
	("mht",                  mhtP4.pt())
	("met_LD",               met_LD)
	("HT",                   HT)
	("STMET",                STMET)
	("m_Hbb",                m_Hbb)
	("m_Hbb_regCorr",        m_Hbb_regCorr)
	("m_Hbb_regRes",         m_Hbb_regRes)
	("dR_Hbb",               dR_Hbb)
	("dPhi_Hbb",             dPhi_Hbb)
	("pT_Hbb",               pT_Hbb)
	("eta_Hbb",              eta_Hbb)
	("tau21_Hbb",            tau21_Hbb)
	("cosThetaS_Hbb",        cosThetaS_Hbb)
	("cosThetaS_Hbb_reg",    cosThetaS_Hbb_reg)
	("m_Wjj",                m_Wjj)
	("dR_Wjj",               dR_Wjj)
	("dPhi_Wjj",             dPhi_Wjj)
	("pT_Wjj",               pT_Wjj)
	("tau21_Wjj",            tau21_Wjj)
	("dR_Hww",               dR_Hww)
	("dPhi_Hww",             dPhi_Hww)
	("Smin_Hww",             Smin_Hww)
	("pT_Hww",               pT_Hww)
	("m_HHvis",              m_HHvis)
	("pT_HHvis",             pT_HHvis)
        ("eta_HHvis",            eta_HHvis)
	("dPhi_HHvis",           dPhi_HHvis)
	("m_HH",                 m_HH)
        ("m_HH_B2G_18_008",      m_HH_B2G_18_008)
	("pT_HH",                pT_HH)
	("dPhi_HH",              dPhi_HH)
	("Smin_HH",              Smin_HH)
	("dR_HH",                dR_HH)
	("cosThetaS_Wjj",        cosThetaS_Wjj)
	("cosThetaS_WW",         cosThetaS_WW)
	("cosThetaS_HH",         cosThetaS_HH)
	("dR_b1lep",             dR_b1lep)
	("dR_b2lep",             dR_b2lep)
	("mT_W",                 mT_W)
	("mT_top_2particle",     mT_top_2particle)
	("mT_top_3particle",     mT_top_3particle)
	("vbf_jet1_pt",          vbf_jet1_pt)
	("vbf_jet1_eta",         vbf_jet1_eta)
	("vbf_jet2_pt",          vbf_jet2_pt)
	("vbf_jet2_eta",         vbf_jet2_eta)
	("vbf_dEta_jj",          vbf_dEta_jj)
	("vbf_m_jj",             vbf_m_jj)
	("genWeight",            eventInfo.genWeight)
	("evtWeight",            evtWeightRecorder.get(central_or_shift_main))
	("numJets",              comp_n_jet25_recl(selJetsAK4))
	("isHbb_boosted",        selJetAK8_Hbb ? true : false)
        ("isWjj_boosted",        selJetsAK8_Wjj.size() >= 1 ? true : false)
	("isVBF",                isVBF)
	("mhh_gen",              eventInfo.gen_mHH)
	("costS_gen",            eventInfo.gen_cosThetaStar)
	("mindr_lep1_jet",       mindr_lep1_jet )
	("avg_dr_jet_central",   comp_avg_dr_jet(selJetsAK4))
	("mbb_loose",            selBJetsAK4_loose.size() >= 2 ? (selBJetsAK4_loose[0]->p4() + selBJetsAK4_loose[1]->p4()).mass() : 0)
	("mbb_medium",           selBJetsAK4_medium.size() >= 2 ? (selBJetsAK4_medium[0]->p4() + selBJetsAK4_medium[1]->p4()).mass() : 0)
	("mll_loose",            preselLeptonsFull.size() >= 2 ? (preselLeptonsFull[0]->p4() + preselLeptonsFull[1]->p4()).mass() : 0)
	("numLeptons_loose",     preselLeptonsFull.size())
	("lepPairCharge_loose",  preselLeptonsFull.size() >= 2 ? preselLeptonsFull[0]->charge() + preselLeptonsFull[1]->charge() : 999)
	("selLepton_charge",     preselLeptonsFull[0]->charge())
	("selLepton_type",       selLepton_type)
	("lepPairType_loose",    preselLeptonsFull.size() >= 2 ? fabs(preselLeptonsFull[0]->pdgId()) == fabs(preselLeptonsFull[1]->pdgId()) : 999)
	("numElectrons",         selElectrons.size())
	("numBJets_loose",       selBJetsAK4_loose.size())
	("numBJets_medium",      selBJetsAK4_medium.size())
        ("numBJets_jpa_loose",   numBJets_jpa_loose)
        ("numBJets_jpa_medium",  numBJets_jpa_medium)
	("numBJets_jpa",         numBJets_jpa)
	("numWJets_jpa",         numWJets_jpa)
        ("numJets_vbf",          selJetsAK4_vbf.size())
	("mostFwdJet_eta",       selJetsForward.size() >= 1 ? std::abs(mostFwdJet.Eta()) : -1000)
	("mostFwdJet_pt",        selJetsForward.size() >= 1 ? mostFwdJet.pt() : -1000)
	("mostFwdJet_phi",       selJetsForward.size() >= 1 ? mostFwdJet.phi() : -1000)
	("mostFwdJet_E",         selJetsForward.size() >= 1 ? mostFwdJet.energy() : -1000)
	("leadFwdJet_eta",       selJetsForward.size() >= 1 ? selJetsForward[0] -> absEta() : -1000)
	("leadFwdJet_pt",        selJetsForward.size() >= 1 ? selJetsForward[0] -> pt() : -1000)
	("leadFwdJet_phi",       selJetsForward.size() >= 1 ? selJetsForward[0] -> phi() : -1000)
	("leadFwdJet_E",         selJetsForward.size() >= 1 ? selJetsForward[0] -> p4().energy() : -1000)
	("numJetsForward",       selJetsForward.size())
	(weightMapHH)
        .fill()
	;
	}*/
    if (snm )
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

      std::vector<const RecoJet*> tmpJets_vbf;
      if(selJet_vbf_lead)    { tmpJets_vbf.push_back(selJet_vbf_lead);    }
      if(selJet_vbf_sublead) { tmpJets_vbf.push_back(selJet_vbf_sublead); }
      snm->read(
        selJetsAK4_vbf_beforeCleaning,
        tmpJets_vbf,
        selJetsAK4_vbf_postLeptonCleaning.size(),
        selJetsAK4_vbf.size()
      );
      if ( isVBF )
      {
        snm->read(vbf_m_jj,    FloatVariableType_bbww::vbf_m_jj);
        snm->read(vbf_dEta_jj, FloatVariableType_bbww::vbf_dEta_jj);
      }

      const bool is_boosted = selJetAK8_Hbb && selJetAK8_Wjj;
      const bool is_semiboosted = selJetAK8_Hbb && !is_boosted;
      const bool is_resolved = !(is_boosted || is_semiboosted);
      snm->read(is_boosted, is_semiboosted, is_resolved);

      const double leptonSF = evtWeightRecorder.get_leptonIDSF("central");
      const double triggerSF = evtWeightRecorder.get_sf_triggerEff("central");
      const double btagSF = evtWeightRecorder.get_btag("central");
      const double topPtWeight = evtWeightRecorder.get_toppt_rwgt("central");
      const double fakeRate = evtWeightRecorder.get_FR("central");
      const double l1Prefire = evtWeightRecorder.get_l1PreFiringWeight("central");
      const double leptonSF_recoToLoose = evtWeightRecorder.get_leptonIDSF_recoToLoose("central");
      const double leptonSF_looseToTight = evtWeightRecorder.get_leptonIDSF_looseToTight("central");
      const double pileupJetIDSF = evtWeightRecorder.get_pileupJetIDSF("central");

      snm->read(triggerSF,                              FloatVariableType_bbww::trigger_SF);
      snm->read(fakeRate,                               FloatVariableType_bbww::fakeRate);
      snm->read(leptonSF,                               FloatVariableType_bbww::lepton_IDSF);
      snm->read(btagSF,                                 FloatVariableType_bbww::btag_SF);
      snm->read(topPtWeight,                            FloatVariableType_bbww::topPt_wgt);
      snm->read(l1Prefire,                              FloatVariableType_bbww::L1prefire);
      snm->read(leptonSF_recoToLoose,                   FloatVariableType_bbww::lepton_IDSF_recoToLoose);
      snm->read(leptonSF_looseToTight,                  FloatVariableType_bbww::lepton_IDSF_looseToTight);
      snm->read(pileupJetIDSF,                          FloatVariableType_bbww::PU_jetID_SF);
      snm->read(eventInfo.pileupWeight,                 FloatVariableType_bbww::PU_weight);
      snm->read(eventInfo.genWeight,                    FloatVariableType_bbww::MC_weight);
      snm->read(met.pt(),                               FloatVariableType_bbww::PFMET);
      snm->read(met.phi(),                              FloatVariableType_bbww::PFMETphi);
      if ( jpa.jpaCategory() != (int)JPA::Category_resolved::kUndefined )
      {
        snm->read(jpaInterface);
      }

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
    if ( isDEBUG )
    {
      std::cout << evtWeightRecorder << '\n';
    }
  }
  if ( snm )
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
  for ( const std::string & central_or_shift: central_or_shifts_local )
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
  /*h_genmatch->GetXaxis()->SetTitle("target");
  h_genmatch->GetYaxis()->SetTitle("evtCategory");
  std::string binlabel[] = {"jpa_4jet", "jpa_missingWjet", "jpa_missingBjet", "jpa_missingAllWjet", "jpa_missingBjetmissingWjet", "jpa_missingBjetmissingAllWjet", "jpa_restOfcat"};
  for(int i=0; i<h_genmatch->GetNbinsX(); i++) h_genmatch->GetXaxis()->SetBinLabel(i+1, binlabel[i].data());
  for(int i=0; i<h_genmatch->GetNbinsY(); i++) h_genmatch->GetYaxis()->SetBinLabel(i+1, binlabel[i].data());
  h_genmatch->Write();
  h_genmatchBoosted->GetXaxis()->SetTitle("target");
  h_genmatchBoosted->GetYaxis()->SetTitle("evtCategory");
  std::string boosted_binlabel[] = {"jpa_4jet", "jpa_missingWjet", "jpa_restOfcat"};
  for(int i=0; i<h_genmatchBoosted->GetNbinsX(); i++) h_genmatchBoosted->GetXaxis()->SetBinLabel(i+1, boosted_binlabel[i].data());
  for(int i=0; i<h_genmatchBoosted->GetNbinsY(); i++) h_genmatchBoosted->GetYaxis()->SetBinLabel(i+1, boosted_binlabel[i].data());
  h_genmatchBoosted->Write();*/

  //histogram_analyzedEntries->Write();
  //histogram_selectedEntries->Write();
  HistManagerBase::writeHistograms();

//--- memory clean-up
  delete dataToMCcorrectionInterface;

  delete leptonFakeRateInterface;

  delete run_lumi_eventSelector;

  delete selEventsFile;
  delete genParticleFromHiggsReader;
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

  delete bdt_filler;
  for(auto & kv: genEvtHistManager_beforeCuts)
  {
    delete kv.second;
  }
  for(auto & kv: genEvtHistManager_afterCuts)
  {
    delete kv.second;
  }
  for(auto & kv: lheInfoHistManager)
  {
    delete kv.second;
  }
  for(auto & bdt: BDT_resonant_spin2_boosted)
  {
    delete bdt;
  }
  for(auto & bdt: BDT_resonant_spin0_boosted)
  {
    delete bdt;
  }
  for(auto & bdt: BDT_nonresonant_boosted)
  {
    delete bdt;
  }
  for(auto & bdt: BDT_resonant_spin2_resolved)
  {
    delete bdt;
  }
  for(auto & bdt: BDT_resonant_spin0_resolved)
  {
    delete bdt;
  }
  for(auto & bdt: BDT_nonresonant_resolved)
  {
    delete bdt;
  }
  for(auto & bdt: LBN_resonant_spin2_boosted)
  {
    delete bdt;
  }
  for(auto & bdt: LBN_resonant_spin0_boosted)
  {
    delete bdt;
  }
  for(auto & bdt: LBN_nonresonant_boosted)
  {
    delete bdt;
  }
  for(auto & bdt: LBN_resonant_spin2_resolved)
  {
    delete bdt;
  }
  for(auto & bdt: LBN_resonant_spin0_resolved)
  {
    delete bdt;
  }
  for(auto & bdt: LBN_nonresonant_resolved)
  {
    delete bdt;
  }
 
  delete cutFlowHistManager;
  delete eventWeightManager;

  delete HHWeight_calc;
  delete HHWeight_calc_LOtoNLO;

  hltPaths_delete(triggers_1e);
  hltPaths_delete(triggers_1mu);

  delete inputTree;
  delete snm;

  clock.Show("analyze_hh_bb1l");

  return EXIT_SUCCESS;
}
