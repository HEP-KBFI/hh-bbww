#include "FWCore/ParameterSet/interface/ParameterSet.h" // edm::ParameterSet
#include "FWCore/Utilities/interface/Exception.h" // cms::Exception
#include "PhysicsTools/FWLite/interface/TFileService.h" // fwlite::TFileService
#include "DataFormats/FWLite/interface/InputSource.h" // fwlite::InputSource
#include "DataFormats/FWLite/interface/OutputFiles.h" // fwlite::OutputFiles
#include "DataFormats/Math/interface/LorentzVector.h" // math::PtEtaPhiMLorentzVector
#include "DataFormats/Math/interface/deltaR.h" // deltaR
#include "DataFormats/Math/interface/deltaPhi.h" // deltaPhi

#if __has_include (<FWCore/ParameterSetReader/interface/ParameterSetReader.h>)
#  include <FWCore/ParameterSetReader/interface/ParameterSetReader.h> // edm::readPSetsFrom()
#else
#  include <FWCore/PythonParameterSet/interface/MakeParameterSets.h> // edm::readPSetsFrom()
#endif

#include <TBenchmark.h> // TBenchmark
#include <TString.h> // TString, Form
#include <TError.h> // gErrorAbortLevel, kError
#include <TRandom3.h> // TRandom3
#include <TLorentzVector.h> // TLorentzVector
#include <TROOT.h> // TROOT

#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h" // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/RecoJet.h" // RecoJet
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEt.h" // RecoMEt
#include "tthAnalysis/HiggsToTauTau/interface/GenLepton.h" // GenLepton
#include "tthAnalysis/HiggsToTauTau/interface/GenJet.h" // GenJet
#include "tthAnalysis/HiggsToTauTau/interface/GenHadTau.h" // GenHadTau
#include "tthAnalysis/HiggsToTauTau/interface/ObjectMultiplicity.h" // ObjectMultiplicity
#include "tthAnalysis/HiggsToTauTau/interface/LeptonFakeRateInterface.h" // LeptonFakeRateInterface
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronReader.h" // RecoElectronReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonReader.h" // RecoMuonReader
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
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // getBTagWeight_option, getHadTau_genPdgId, isHigherPt, isMatched, contains, pileupJetID
#include "tthAnalysis/HiggsToTauTau/interface/leptonGenMatchingAuxFunctions.h" // getLeptonGenMatch_definitions_2lepton, getLeptonGenMatch_string, getLeptonGenMatch_int
#include "tthAnalysis/HiggsToTauTau/interface/GenMatchInterface.h" // GenMatchInterface
#include "tthAnalysis/HiggsToTauTau/interface/fakeBackgroundAuxFunctions.h"
#include "tthAnalysis/HiggsToTauTau/interface/generalAuxFunctions.h" // format_vstring
#include "tthAnalysis/HiggsToTauTau/interface/mvaInputVariables.h" // comp_lep1_conePt(), comp_lep2_conePt(), comp_cosThetaStar()
#include "tthAnalysis/HiggsToTauTau/interface/hltPath.h" // hltPath, create_hltPaths, hltPaths_isTriggered, hltPaths_delete
#include "tthAnalysis/HiggsToTauTau/interface/hltPathReader.h" // hltPathReader
#include "tthAnalysis/HiggsToTauTau/interface/Data_to_MC_CorrectionInterface_2016.h"
#include "tthAnalysis/HiggsToTauTau/interface/Data_to_MC_CorrectionInterface_2017.h"
#include "tthAnalysis/HiggsToTauTau/interface/Data_to_MC_CorrectionInterface_2018.h"
#include "tthAnalysis/HiggsToTauTau/interface/DYMCReweighting.h" // DYMCReweighting
#include "tthAnalysis/HiggsToTauTau/interface/lutAuxFunctions.h" // loadTH2, get_sf_from_TH2
#include "tthAnalysis/HiggsToTauTau/interface/L1PreFiringWeightReader.h" // L1PreFiringWeightReader
#include "tthAnalysis/HiggsToTauTau/interface/cutFlowTable.h" // cutFlowTableType
#include "tthAnalysis/HiggsToTauTau/interface/NtupleFillerBDT.h" // NtupleFillerBDT
#include "tthAnalysis/HiggsToTauTau/interface/TTreeWrapper.h" // TTreeWrapper
#include "tthAnalysis/HiggsToTauTau/interface/hltFilter.h" // hltFilter()
#include "tthAnalysis/HiggsToTauTau/interface/EvtWeightManager.h" // EvtWeightManager
#include "tthAnalysis/HiggsToTauTau/interface/TMVAInterface.h" // TMVAInterface
#include "tthAnalysis/HiggsToTauTau/interface/TensorFlowInterfaceLBN.h" // TensorFlowInterfaceLBN
#include "tthAnalysis/HiggsToTauTau/interface/MVAInputVarHistManager.h" // MVAInputVarHistManager
#include "tthAnalysis/HiggsToTauTau/interface/mT2_2particle.h" // mT2_2particle
#include "tthAnalysis/HiggsToTauTau/interface/mT2_3particle.h" // mT2_3particle
#include "tthAnalysis/HiggsToTauTau/interface/Higgsness.h" // Higgsness
#include "tthAnalysis/HiggsToTauTau/interface/Topness.h" // Topness
#include "tthAnalysis/HiggsToTauTau/interface/LocalFileInPath.h" // LocalFileInPath
#include "tthAnalysis/HiggsToTauTau/interface/HHWeightInterface2.h" // HHWeightInterface2
#include "tthAnalysis/HiggsToTauTau/interface/HHWeightInterfaceLOtoNLO.h" // HHWeightInterfaceLOtoNLO
#include "tthAnalysis/HiggsToTauTau/interface/DYMCNormScaleFactors.h" // DYMCNormScaleFactors
#include "tthAnalysis/HiggsToTauTau/interface/BtagSFRatioFacility.h" // BtagSFRatioFacility
#include "tthAnalysis/HiggsToTauTau/interface/LHEParticle.h" // LHEParticle
#include "tthAnalysis/HiggsToTauTau/interface/RecoVertex.h" // RecoVertex
#include "tthAnalysis/HiggsToTauTau/interface/RecoVertexReader.h" // RecoVertexReader

#include "hhAnalysis/Heavymassestimator/interface/heavyMassEstimator.h" // heavyMassEstimator (HME) algorithm for computation of HH mass

#include "hhAnalysis/multilepton/interface/EvtWeightRecorderHH.h" // EvtWeightRecorderHH
#include "hhAnalysis/multilepton/interface/AnalysisConfig_hh.h" // AnalysisConfig_hh
#include "hhAnalysis/multilepton/interface/DatacardHistManager_hh.h" // DatacardHistManager_hh
#include "hhAnalysis/multilepton/interface/DatacardHistManager_hh_multiclass.h" // DatacardHistManager_hh_multiclass
#include "hhAnalysis/multilepton/interface/RecoElectronCollectionSelectorFakeable_hh_multilepton.h" // RecoElectronCollectionSelectorFakeable_hh_multilepton
#include "hhAnalysis/multilepton/interface/RecoMuonCollectionSelectorFakeable_hh_multilepton.h" // RecoMuonCollectionSelectorFakeable_hh_multilepton
#include "hhAnalysis/multilepton/interface/HHGenKinematicsHistManager.h"

#include "hhAnalysis/bbww/interface/EvtHistManager2_hh_bb2l.h" // EvtHistManager2_hh_bb2l
#include "hhAnalysis/bbww/interface/MEMHistManager_hh_bb2l.h" // MEMHistManager_hh_bb2l
#include "hhAnalysis/bbww/interface/RecoJetCollectionSelectorAK8_hh_bbWW_Hbb.h" // RecoJetSelectorAK8_hh_bbWW_Hbb
#include "hhAnalysis/bbww/interface/MEMOutput_hh_bb2l.h" // MEMOutput_hh_bb2l
#include "hhAnalysis/bbww/interface/MEMOutputReader_hh_bb2l.h" // MEMOutputReader_hh_bb2l
#include "hhAnalysis/bbww/interface/HMEInterface_hh_bb2l.h" // HMEInterface_hh_bb2l // CV: switcht to HMEOutputReader_hh_bb2l in the future !!
#include "hhAnalysis/bbww/interface/HMEOutput_hh_bb2l.h" // HMEOutput_hh_bb2l
#include "hhAnalysis/bbww/interface/HMEOutputReader_hh_bb2l.h" // HMEOutputReader_hh_bb2l
#include "hhAnalysis/bbww/interface/jetSelectionAuxFunctions.h" // selectJets_Hbb, countBJets_Hbb
#include "hhAnalysis/bbww/interface/SyncNtupleManager_bbww.h" // SyncNtupleManager_bbww
#include "hhAnalysis/bbww/interface/BM_list.h" // BMS
#include "hhAnalysis/bbww/interface/EventCategory_hh_bb2l_BDT.h" // EventCategory_hh_bb2l_BDT
#include "hhAnalysis/bbww/interface/EventCategory_hh_bb2l_LBN.h" // EventCategory_hh_bb2l_LBN
#include "hhAnalysis/bbww/interface/analysisAuxFunctions_hh_bbWW.h" // makeTMVAInterface, makeTensorFlowInterfaceLBN
#include "hhAnalysis/bbww/interface/dumpGenParticles.h" // dumpGenParticles

#include <boost/algorithm/string/predicate.hpp> // boost::starts_with()

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

  std::cout << "<analyze_hh_bb2l>:" << std::endl;

//--- keep track of time it takes the macro to execute
  TBenchmark clock;
  clock.Start("analyze_hh_bb2l");

//--- read python configuration parameters
  if ( !edm::readPSetsFrom(argv[1])->existsAs<edm::ParameterSet>("process") )
    throw cms::Exception("analyze_hh_bb2l")
      << "No ParameterSet 'process' found in configuration file = " << argv[1] << " !!\n";

  edm::ParameterSet cfg = edm::readPSetsFrom(argv[1])->getParameter<edm::ParameterSet>("process");

  edm::ParameterSet cfg_analyze = cfg.getParameter<edm::ParameterSet>("analyze_hh_bb2l");
  AnalysisConfig_hh analysisConfig("HH->bbWW", cfg_analyze);

  std::string treeName = cfg_analyze.getParameter<std::string>("treeName");

  std::string process_string = cfg_analyze.getParameter<std::string>("process");
  std::string process_string_hh = ( process_string.find("signal_") != std::string::npos ) ? cfg_analyze.getParameter<std::string>("process_hh") : "";
  bool isMC = cfg_analyze.getParameter<bool>("isMC");
  bool isSignal = isMC && boost::starts_with(process_string_hh, "signal_") && process_string_hh.find("_hh_") != std::string::npos;
  bool isMC_tH  = isMC && process_string == "TH";
  bool isMC_ttH = isMC && process_string == "TTH";

  std::string histogramDir = cfg_analyze.getParameter<std::string>("histogramDir");
  bool isMCClosure_e = histogramDir.find("mcClosure_e") != std::string::npos;
  bool isMCClosure_m = histogramDir.find("mcClosure_m") != std::string::npos;

  std::string era_string = cfg_analyze.getParameter<std::string>("era");
  const Era era = get_era(era_string);

  vstring triggerNames_1e = cfg_analyze.getParameter<vstring>("triggers_1e");
  std::vector<hltPath*> triggers_1e = create_hltPaths(triggerNames_1e);
  bool use_triggers_1e = cfg_analyze.getParameter<bool>("use_triggers_1e");
  vstring triggerNames_2e = cfg_analyze.getParameter<vstring>("triggers_2e");
  std::vector<hltPath*> triggers_2e = create_hltPaths(triggerNames_2e);
  bool use_triggers_2e = cfg_analyze.getParameter<bool>("use_triggers_2e");
  vstring triggerNames_1mu = cfg_analyze.getParameter<vstring>("triggers_1mu");
  std::vector<hltPath*> triggers_1mu = create_hltPaths(triggerNames_1mu);
  bool use_triggers_1mu = cfg_analyze.getParameter<bool>("use_triggers_1mu");
  vstring triggerNames_2mu = cfg_analyze.getParameter<vstring>("triggers_2mu");
  std::vector<hltPath*> triggers_2mu = create_hltPaths(triggerNames_2mu);
  bool use_triggers_2mu = cfg_analyze.getParameter<bool>("use_triggers_2mu");
  vstring triggerNames_1e1mu = cfg_analyze.getParameter<vstring>("triggers_1e1mu");
  std::vector<hltPath*> triggers_1e1mu = create_hltPaths(triggerNames_1e1mu);
  bool use_triggers_1e1mu = cfg_analyze.getParameter<bool>("use_triggers_1e1mu");

  bool apply_offline_e_trigger_cuts_1e = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_1e");
  bool apply_offline_e_trigger_cuts_2e = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_2e");
  bool apply_offline_e_trigger_cuts_1mu = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_1mu");
  bool apply_offline_e_trigger_cuts_2mu = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_2mu");
  bool apply_offline_e_trigger_cuts_1e1mu = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_1e1mu");

  enum { kOS, kSS, kDisabled };
  std::string leptonChargeSelection_string = cfg_analyze.getParameter<std::string>("leptonChargeSelection");
  int leptonChargeSelection = -1;
  if      ( leptonChargeSelection_string == "OS"       ) leptonChargeSelection = kOS;
  else if ( leptonChargeSelection_string == "SS"       ) leptonChargeSelection = kSS;
  else if ( leptonChargeSelection_string == "disabled" ) leptonChargeSelection = kDisabled;
  else throw cms::Exception("analyze_hh_bb2l")
    << "Invalid Configuration parameter 'leptonChargeSelection' = " << leptonChargeSelection_string << " !!\n";

  const std::string electronSelection_string = cfg_analyze.getParameter<std::string>("electronSelection");
  const std::string muonSelection_string     = cfg_analyze.getParameter<std::string>("muonSelection");
  std::cout << "electronSelection_string = " << electronSelection_string << "\n"
               "muonSelection_string     = " << muonSelection_string     << '\n'
  ;
  const int electronSelection = get_selection(electronSelection_string);
  const int muonSelection     = get_selection(muonSelection_string);

  bool apply_leptonGenMatching = cfg_analyze.getParameter<bool>("apply_leptonGenMatching");
  std::vector<leptonGenMatchEntry> leptonGenMatch_definitions = getLeptonGenMatch_definitions_2lepton(true);
  std::cout << "leptonGenMatch_definitions:" << std::endl;
  std::cout << leptonGenMatch_definitions;

  GenMatchInterface genMatchInterface(2, apply_leptonGenMatching, false);

  const std::string apply_pileupJetID_string = cfg_analyze.getParameter<std::string>("apply_pileupJetID");
  const pileupJetID apply_pileupJetID = get_pileupJetID(apply_pileupJetID_string);

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

  bool run_hme = cfg_analyze.getParameter<bool>("run_hme");

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
  if ( applyAdditionalEvtWeight ) {
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

  const MEMsys mem_option_main = getMEMsys_option(central_or_shift_main);
  assert(mem_option_main == MEMsys::nominal);

  std::cout
    << "central_or_shift = "    << central_or_shift_main << "\n"
       " -> hadTauPt_option = " << hadTauPt_option       << "\n"
       " -> met_option      = " << met_option            << "\n"
       " -> jetPt_option    = " << jetPt_option          << "\n"
       "--> fatJetPt_option = " << fatJetPt_option       << "\n"
       " -> MEMsys option   = " << as_integer(mem_option_main) << '\n'
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
    default: throw cmsException("analyze_hh_bb2l", __LINE__) << "Invalid era = " << static_cast<int>(era);
  }

  std::string applyFakeRateWeights_string = cfg_analyze.getParameter<std::string>("applyFakeRateWeights");
  int applyFakeRateWeights = -1;
  if      ( applyFakeRateWeights_string == "disabled" ) applyFakeRateWeights = kFR_disabled;
  else if ( applyFakeRateWeights_string == "enabled"  ) applyFakeRateWeights = kFR_enabled;
  else throw cms::Exception("analyze_hh_bb2l")
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
  std::string branchName_jets_ak4 = cfg_analyze.getParameter<std::string>("branchName_jets_ak4");
  std::string branchName_jets_ak8 = cfg_analyze.getParameter<std::string>("branchName_jets_ak8");
  std::string branchName_subjets_ak8 = cfg_analyze.getParameter<std::string>("branchName_subjets_ak8");
  std::string branchName_met = cfg_analyze.getParameter<std::string>("branchName_met");
  std::string branchName_vertex = cfg_analyze.getParameter<std::string>("branchName_vertex");

  std::string branchName_genLeptons = cfg_analyze.getParameter<std::string>("branchName_genLeptons");
  std::string branchName_genHadTaus = cfg_analyze.getParameter<std::string>("branchName_genHadTaus");
  std::string branchName_genPhotons = cfg_analyze.getParameter<std::string>("branchName_genPhotons");
  std::string branchName_genJets = cfg_analyze.getParameter<std::string>("branchName_genJets");
  std::string branchName_memOutput = cfg_analyze.getParameter<std::string>("branchName_memOutput");
  std::string branchName_hmeOutput = cfg_analyze.getParameter<std::string>("branchName_hmeOutput");

  std::string branchName_muonGenMatch     = cfg_analyze.getParameter<std::string>("branchName_muonGenMatch");
  std::string branchName_electronGenMatch = cfg_analyze.getParameter<std::string>("branchName_electronGenMatch");
  std::string branchName_jetGenMatch      = cfg_analyze.getParameter<std::string>("branchName_jetGenMatch");

  bool redoGenMatching = cfg_analyze.getParameter<bool>("redoGenMatching");
  bool jetCleaningByIndex = cfg_analyze.getParameter<bool>("jetCleaningByIndex");
  bool genMatchingByIndex = cfg_analyze.getParameter<bool>("genMatchingByIndex");

  std::string branchName_genBJets = cfg_analyze.getParameter<std::string>("branchName_genBJets");
  std::string branchName_genWBosons = cfg_analyze.getParameter<std::string>("branchName_genWBosons");

  bool selectBDT = ( cfg_analyze.exists("selectBDT") ) ? cfg_analyze.getParameter<bool>("selectBDT") : false;

  std::vector<double> gen_mHH = analysisConfig.get_HH_resonant_mass_points();
  std::vector<double> nonRes_BMs = cfg_analyze.getParameter<std::vector<double>>("nonRes_BMs");

  bool fillHistograms_nonresonant = cfg_analyze.getParameter<bool>("fillHistograms_nonresonant");
  bool fillHistograms_resonant_spin0 = cfg_analyze.getParameter<bool>("fillHistograms_resonant_spin0");
  bool fillHistograms_resonant_spin2 = cfg_analyze.getParameter<bool>("fillHistograms_resonant_spin2");

  // initialize BDT-based signal extraction for resonant and non-resonant HH signal
  bool fillHistograms_BDT = cfg_analyze.getParameter<bool>("fillHistograms_BDT");
  std::vector<TMVAInterface *> BDT_resonant_spin2_boosted;//  = nullptr;
  std::vector<TMVAInterface *> BDT_resonant_spin2_resolved;
  std::vector<TMVAInterface *> BDT_resonant_spin0_boosted;
  std::vector<TMVAInterface *> BDT_resonant_spin0_resolved;
  std::vector<TMVAInterface *> BDT_nonresonant_boosted;
  std::vector<TMVAInterface *> BDT_nonresonant_resolved;
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
    snm->initializeHLTBranches({ triggers_1e, triggers_2e, triggers_1mu, triggers_2mu, triggers_1e1mu });
  }

//--- declare event-level variables
  EventInfo eventInfo(analysisConfig);
  if(isMC)
  {
    const double ref_genWeight = cfg_analyze.getParameter<double>("ref_genWeight");
    eventInfo.set_refGetWeight(ref_genWeight);
  }
  const std::string default_cat_str = "default";
  std::vector<std::string> evt_cat_strs = { default_cat_str };
  
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

  hltPathReader hltPathReader_instance({ triggers_1e, triggers_2e, triggers_1mu, triggers_2mu, triggers_1e1mu });
  inputTree->registerReader(&hltPathReader_instance);

  if ( eventWeightManager ) {
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

  std::map<std::string, MEMOutputReader_hh_bb2l *> memReader;
  for(auto BMlocal : memReader) BMlocal.second = nullptr;
  std::map<std::string, MEMOutputReader_hh_bb2l *> memReader_missingBjet;
  std::string missingBjet = "missingBJet";
  std::string centralstr = "central";
  if(! branchName_memOutput.empty())
  {
    for(auto BMlocal : BMS)
    {
      std::string namebranchN;
      std::string namebranch;
      if ( BMlocal == "SM")
      {
        namebranch = Form("%s_%s", branchName_memOutput.data(),  centralstr.data());
        namebranchN = Form("n%s_%s", branchName_memOutput.data(), centralstr.data());
      }
      else {
        namebranch = Form("%s_%s_%s", branchName_memOutput.data(), centralstr.data(), BMlocal.c_str());
        namebranchN = Form("n%s_%s_%s", branchName_memOutput.data(), centralstr.data(), BMlocal.c_str());
      }
      memReader[BMlocal] = new MEMOutputReader_hh_bb2l(namebranchN, namebranch);
      inputTree -> registerReader(memReader[BMlocal]);
      ////////////////////////////////////
      std::string namebranchN_missingBjet;
      std::string namebranch_missingBjet;
      if ( BMlocal == "SM")
      {
        std::string BMSM = "BM4";
        // TOFIX: SM not being booked now using BM4, that is the cluster that contains the SM
        namebranch_missingBjet = Form("%s_%s_%s_%s", branchName_memOutput.data(), missingBjet.data(), centralstr.data(), BMSM.data());
        namebranchN_missingBjet = Form("n%s_%s_%s_%s", branchName_memOutput.data(), missingBjet.data(), centralstr.data(), BMSM.data());
      }
      else {
        namebranch_missingBjet = Form("%s_%s_%s_%s", branchName_memOutput.data(), missingBjet.data(), centralstr.data(), BMlocal.c_str());
        namebranchN_missingBjet = Form("n%s_%s_%s_%s", branchName_memOutput.data(), missingBjet.data(), centralstr.data(), BMlocal.c_str());
      }
      memReader_missingBjet[BMlocal] = new MEMOutputReader_hh_bb2l(namebranchN_missingBjet, namebranch_missingBjet);
      inputTree -> registerReader(memReader_missingBjet[BMlocal]);
    }
  }

  HMEOutputReader_hh_bb2l* hmeReader = nullptr;
  if ( branchName_hmeOutput.length() > 0 )
  {
    hmeReader = new HMEOutputReader_hh_bb2l(Form("n%s", branchName_hmeOutput.data()), branchName_hmeOutput);
    inputTree->registerReader(hmeReader);
  }

//--- declare particle collections
  const bool readGenObjects = isMC && !redoGenMatching;
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
  RecoJetCollectionSelectorBtagMedium jetSelectorAK4_bTagMedium(era, -1, isDEBUG);
  RecoJetCollectionSelectorForward jetSelectorForward(era, -1, isDEBUG);

  RecoJetReaderAK8* jetReaderAK8 = new RecoJetReaderAK8(era, isMC, branchName_jets_ak8, branchName_subjets_ak8);
  jetReaderAK8->set_central_or_shift(fatJetPt_option);
  inputTree->registerReader(jetReaderAK8);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR08(0.8, isDEBUG);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR12(1.2, isDEBUG);
  RecoJetCollectionSelectorAK8_hh_bbWW_Hbb jetSelectorAK8_Hbb(era, -1, isDEBUG);

  GenParticleReader* genBJetReader = nullptr;
  GenParticleReader* genWBosonReader = nullptr;

  if ( isMC ) {
    genBJetReader = new GenParticleReader(branchName_genBJets);
    inputTree->registerReader(genBJetReader);
    genWBosonReader = new GenParticleReader(branchName_genWBosons);
    inputTree->registerReader(genWBosonReader);
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

//--- initialize algorithm for reconstruction of H boson pair mass in HH->bbWW dilepton events
//   (as described in arXiv:1701.04442)
  HMEInterface_hh_bb2l hmeInterface_hh_bb2l;

//--- open output file containing run:lumi:event numbers of events passing final event selection criteria
  std::ostream* selEventsFile = ( selEventsFileName_output != "" ) ? new std::ofstream(selEventsFileName_output.data(), std::ios::out) : 0;
  std::cout << "selEventsFileName_output = " << selEventsFileName_output << std::endl;

//--- declare histograms
  struct selHistManagerType
  {
    ElectronHistManager* electrons_;
    ElectronHistManager* leadElectron_;
    ElectronHistManager* subleadElectron_;
    MuonHistManager* muons_;
    MuonHistManager* leadMuon_;
    MuonHistManager* subleadMuon_;
    JetHistManager* jetsAK4_;
    JetHistManager* leadJetAK4_;
    JetHistManager* subleadJetAK4_;
    JetHistManagerAK8* jetsAK8_Hbb_;
    JetHistManager* BJetsAK4_loose_;
    JetHistManager* leadBJetAK4_loose_;
    JetHistManager* subleadBJetAK4_loose_;
    JetHistManager* BJetsAK4_medium_;
    MEtHistManager* met_;
    MEtFilterHistManager* metFilters_;
    EvtHistManager2_hh_bb2l* evt_;
    //MEMHistManager_hh_bb2l* mem_;
    HHGenKinematicsHistManager* genKinematics_HH_;
    DatacardHistManager_hh* datacard_BDT_;
    DatacardHistManager_hh_multiclass* datacard_LBN_;
    EvtYieldHistManager* evtYield_;
    WeightHistManager* weights_;
  };

  EventCategory_hh_bb2l_BDT eventCategory_BDT;
  EventCategory_hh_bb2l_LBN eventCategory_LBN;

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
        selHistManager->leadElectron_ = new ElectronHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/leadElectron", histogramDir.data()), era_string, central_or_shift, "minimalHistograms"));
        selHistManager->leadElectron_->bookHistograms(fs);
        selHistManager->subleadElectron_ = new ElectronHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/subleadElectron", histogramDir.data()), era_string, central_or_shift, "minimalHistograms"));
        selHistManager->subleadElectron_->bookHistograms(fs);
        selHistManager->muons_ = new MuonHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/muons", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
        selHistManager->muons_->bookHistograms(fs);
        selHistManager->leadMuon_ = new MuonHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/leadMuon", histogramDir.data()), era_string, central_or_shift, "minimalHistograms"));
        selHistManager->leadMuon_->bookHistograms(fs);
        selHistManager->subleadMuon_ = new MuonHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/subleadMuon", histogramDir.data()), era_string, central_or_shift, "minimalHistograms"));
        selHistManager->subleadMuon_->bookHistograms(fs);
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
        selHistManager->evt_ = new EvtHistManager2_hh_bb2l(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/evt", histogramDir.data()), era_string, central_or_shift));
        selHistManager->evt_->bookHistograms(fs);
        //selHistManager->mem_ = new MEMHistManager_hh_bb2l(makeHistManager_cfg(process_and_genMatch,
        //  Form("%s/sel/mem", histogramDir.data()), era_string, central_or_shift));
        //selHistManager->mem_->bookHistograms(fs);
        selHistManager->genKinematics_HH_ = new HHGenKinematicsHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/genKinematics_HH", histogramDir.data()), era_string, central_or_shift),
          analysisConfig, eventInfo, HHWeight_calc, HHWeight_calc_LOtoNLO);
        selHistManager->genKinematics_HH_->bookHistograms(fs);
      }

      //if ( fillHistograms_BDT )
      //{
        selHistManager->datacard_BDT_ = new DatacardHistManager_hh(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/datacard/BDT", histogramDir.data()), era_string, central_or_shift),
          analysisConfig, eventInfo, HHWeight_calc, HHWeight_calc_LOtoNLO, &eventCategory_BDT,
          isDEBUG, 
          fillHistograms_nonresonant, fillHistograms_resonant_spin0, fillHistograms_resonant_spin2);
        selHistManager->datacard_BDT_->bookHistograms(fs);
      //}
      //if ( fillHistograms_LBN )
      //{
        selHistManager->datacard_LBN_ = new DatacardHistManager_hh_multiclass(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/datacard/LBN", histogramDir.data()), era_string, central_or_shift),
          analysisConfig, eventInfo, HHWeight_calc, HHWeight_calc_LOtoNLO, &eventCategory_LBN,
          isDEBUG, 
          fillHistograms_nonresonant, fillHistograms_resonant_spin0, fillHistograms_resonant_spin2);
        selHistManager->datacard_LBN_->bookHistograms(fs);
      //}

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

    if(isMC && ! skipBooking)
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

  if ( selectBDT ) {
    bdt_filler = new std::remove_pointer<decltype(bdt_filler)>::type(
      makeHistManager_cfg(process_string, Form("%s/sel/evtntuple", histogramDir.data()), era_string, central_or_shift_main)
    );
    for ( const std::string & evt_cat_str: HHWeightNames )
    {
      if (!apply_HH_rwgt) continue;
      bdt_filler->register_variable<float_type>(Form(evt_cat_str.c_str()));
    }
    //for(const std::string & evt_cat_str: BMS)
    //{
    //  bdt_filler->register_variable<float_type>( Form("memweight_signal_%s", evt_cat_str.c_str()) );
    //  bdt_filler->register_variable<float_type>( Form("memweight_background_%s", evt_cat_str.c_str()) );
    //  bdt_filler->register_variable<float_type>( Form("memOutput_LR_%s", evt_cat_str.c_str()) );
    //  bdt_filler->register_variable<float_type>( Form("memOutput_LR_missingBjet_%s", evt_cat_str.c_str()) );
    //}
    bdt_filler->register_variable<float_type>(     
      "lep1_pt", "lep1_conePt", "lep1_eta", "lep1_phi", "lep1_mass",
      "lep1_e", "lep1_px", "lep1_py", "lep1_pz",
      "lep1_frWeight",
      "lep2_pt", "lep2_conePt", "lep2_eta", "lep2_phi", "lep2_mass",
      "lep2_e", "lep2_px", "lep2_py", "lep2_pz",
      "lep2_frWeight",
      "bjet1_pt", "bjet1_eta", "bjet1_phi", "bjet1_mass",
      "bjet1_e", "bjet1_px", "bjet1_py", "bjet1_pz",
      "bjet2_pt", "bjet2_eta", "bjet2_phi", "bjet2_mass",
      "bjet2_e", "bjet2_px", "bjet2_py", "bjet2_pz",
      "bjet1_btagCSV", "bjet2_btagCSV",
      "met", "mht", "met_LD",
      "HT", "STMET",
      "m_Hbb", "m_Hbb_regCorr", "m_Hbb_regRes", "dR_Hbb", "dPhi_Hbb", "pT_Hbb", "eta_Hbb", "tau21_Hbb",
      "m_ll", "dR_ll", "dPhi_ll", "dEta_ll", "pT_ll",
      "min_dPhi_lepMEt", "max_dPhi_lepMEt",
      "m_Hww", "mT_Hww", "pT_Hww", "Smin_Hww",
      "met_pt_proj",
      "dR_b1lep1", "dR_b1lep2", "dR_b2lep1", "dR_b2lep2",
      "m_HHvis", "pT_HHvis", "eta_HHvis", "dPhi_HHvis",
      "m_HH", "pT_HH", "dPhi_HH", "Smin_HH", "dR_HH",
      "mT2_W", "mT2_top_2particle", "mT2_top_3particle",
      "m_HH_hme",
      "logTopness_publishedChi2", "logHiggsness_publishedChi2", "logTopness_fixedChi2", "logHiggsness_fixedChi2",
      "vbf_jet1_pt", "vbf_jet1_eta", "vbf_jet2_pt", "vbf_jet2_eta", "vbf_m_jj", "vbf_dEta_jj",
      "genWeight", "evtWeight",
      "mhh_gen", "costS_gen",
      "mindr_lep1_jet", "mindr_lep2_jet",
      "avg_dr_jet_central",  "mbb_loose", "mbb_medium", 
      "massLT",  "max_Lep_eta",
      "cosThetaS_Hbb", "cosThetaS_Hbb_reg",
      "mostFwdJet_eta", "mostFwdJet_pt", "mostFwdJet_phi", "mostFwdJet_E",
      "leadFwdJet_eta", "leadFwdJet_pt", "leadFwdJet_phi", "leadFwdJet_E"
    );
    bdt_filler->register_variable<int_type>(
      "lep1_charge", "lep2_charge", "numElectrons", 
      "numJets", "numBJets_loose", "numBJets_medium",
      "isHbb_boosted", 
      "sum_Lep_charge",
      "numJets_vbf", "isVBF", 
      "numJetsForward", "lepPairType"
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
  const std::vector<std::string> cuts = {
    "run:ls:event selection",
    "object multiplicity",
    "trigger",
    ">= 2 presel leptons",
    ">= 2 sel leptons",
    "lead lepton pT > 25 GeV && sublead lepton pT > 15 GeV",
    Form("sel lepton-pair %s charge", leptonChargeSelection_string.data()),
    "<= 2 tight leptons",
    "trigger & fakeable lepton flavor matching",
    "trigger & dataset matching",
    "HLT filter matching",
    ">= 2 jets from H->bb",
    ">= 1 medium b-jet",
    //"m(ll) < 76 GeV",
    "m(ll) > 12 GeV",
    "Z-boson mass veto",
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
      if(objectMultiplicity.getNRecoLepton(minLeptonSelection) < 2 ||
         objectMultiplicity.getNRecoLepton(kTight)             > 2  )
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
    if ( isMC ) {
      genBJets = genBJetReader->read();
      genWBosons = genWBosonReader->read();
    }
    if ( isDEBUG ) {
      dumpGenParticles("genBJet", genBJets);
      dumpGenParticles("genWBoson", genWBosons);
    }

    eventInfo.reset_productionMode();
    if ( isMC ) {
      if(analysisConfig.isMC_VH())
      {
        eventInfo.set_productionMode(get_VH_productionMode(genWBosons));
      }
    }

    std::vector<GenParticle> genLeptonsDY;
    if(isMC)
    {
      for(const GenParticle & genLepton: genLeptons)
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
    bool isTriggered_2e = hltPaths_isTriggered(triggers_2e, triggerWhiteList, eventInfo, isMC);
    bool isTriggered_1mu = hltPaths_isTriggered(triggers_1mu, triggerWhiteList, eventInfo, isMC);
    bool isTriggered_2mu = hltPaths_isTriggered(triggers_2mu, triggerWhiteList, eventInfo, isMC);
    bool isTriggered_1e1mu = hltPaths_isTriggered(triggers_1e1mu, triggerWhiteList, eventInfo, isMC);

    bool selTrigger_1e = use_triggers_1e && isTriggered_1e;
    bool selTrigger_2e = use_triggers_2e && isTriggered_2e;
    bool selTrigger_1mu = use_triggers_1mu && isTriggered_1mu;
    bool selTrigger_2mu = use_triggers_2mu && isTriggered_2mu;
    bool selTrigger_1e1mu = use_triggers_1e1mu && isTriggered_1e1mu;
    if ( !(selTrigger_1e || selTrigger_2e || selTrigger_1mu || selTrigger_2mu || selTrigger_1e1mu) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
        std::cout << " (selTrigger_1e = " << selTrigger_1e
                  << ", selTrigger_2e = " << selTrigger_2e
                  << ", selTrigger_1mu = " << selTrigger_1mu
                  << ", selTrigger_2mu = " << selTrigger_2mu
                  << ", selTrigger_1e1mu = " << selTrigger_1e1mu << ")" << std::endl;
      }
      continue;
    }
    cutFlowTable.update("trigger", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("trigger", evtWeightRecorder.get(central_or_shift_main));

    if ( (selTrigger_2e    && !apply_offline_e_trigger_cuts_2e)    ||
         (selTrigger_1e1mu && !apply_offline_e_trigger_cuts_1e1mu) ||
         (selTrigger_1e    && !apply_offline_e_trigger_cuts_1e)    ||
         (selTrigger_1mu   && !apply_offline_e_trigger_cuts_1mu)   ||
         (selTrigger_2mu   && !apply_offline_e_trigger_cuts_2mu)  ) {
      fakeableElectronSelector_default.disable_offline_e_trigger_cuts();
      tightElectronSelector.disable_offline_e_trigger_cuts();
    } else {
      tightElectronSelector.enable_offline_e_trigger_cuts();
      fakeableElectronSelector_default.enable_offline_e_trigger_cuts();
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
    const std::vector<const RecoElectron*> fakeableElectrons = lep_mva_wp == "hh_multilepton" ?
      fakeableElectronSelector_hh_multilepton(preselElectrons, isHigherConePt) :
      fakeableElectronSelector_default(preselElectrons, isHigherConePt)
    ;
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

    const std::vector<const RecoLepton*> preselLeptons = pickFirstNobjects(preselLeptonsFull, 2);
    const std::vector<const RecoLepton*> fakeableLeptons = pickFirstNobjects(fakeableLeptonsFull, 2);
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

//--- build collections of jets and select subset of jets passing b-tagging criteria
    const std::vector<RecoJet> jets_ak4 = jetReaderAK4->read();
    const std::vector<const RecoJet*> jet_ptrs_ak4 = convert_to_ptrs(jets_ak4);
    const std::vector<const RecoJet*> cleanedJetsAK4_wrtLeptons = jetCleaningByIndex ?
      jetCleanerAK4_byIndex(jet_ptrs_ak4, fakeableLeptons) :
      jetCleanerAK4_dR04   (jet_ptrs_ak4, fakeableLeptons)
    ;
    const std::vector<const RecoJet*> selJetsAK4 = jetSelectorAK4_wPileupJetId(cleanedJetsAK4_wrtLeptons, isHigherPt);
    const std::vector<const RecoJet*> selBJetsAK4_loose = jetSelectorAK4_bTagLoose(cleanedJetsAK4_wrtLeptons, isHigherPt);
    const std::vector<const RecoJet*> selBJetsAK4_medium = jetSelectorAK4_bTagMedium(cleanedJetsAK4_wrtLeptons, isHigherPt);
    const std::vector<const RecoJet *> selJetsForward = jetSelectorForward(cleanedJetsAK4_wrtLeptons, isHigherPt);

    if ( isDEBUG || run_lumi_eventSelector ) {
      printCollection("uncleaned AK4 jets", jet_ptrs_ak4);
      printCollection("cleaned AK4 jets(wrtLeptons)", cleanedJetsAK4_wrtLeptons);
      printCollection("selected AK4 jets", selJetsAK4);
      printCollection("selJetsForward", selJetsForward);
    }

//--- build collections of generator level particles (after some cuts are applied, to save computing time)
    if ( isMC && redoGenMatching && ! fillGenEvtHistograms )
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

        jetGenMatcherAK4.addGenLeptonMatch(jet_ptrs_ak4, genLeptons);
        jetGenMatcherAK4.addGenHadTauMatch(jet_ptrs_ak4, genHadTaus);
        jetGenMatcherAK4.addGenJetMatch(jet_ptrs_ak4, genJets);
      }
    }

    // require at least two leptons passing loose preselection criteria
    if ( !(preselLeptonsFull.size() >= 2) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS preselLeptons selection." << std::endl;
        printCollection("preselLeptons", preselLeptonsFull);
      }
      continue;
    }
    cutFlowTable.update(">= 2 presel leptons", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(">= 2 presel leptons", evtWeightRecorder.get(central_or_shift_main));

    // require at least two leptons passing tight selection criteria of final event selection
    if ( !(selLeptons.size() >= 2) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS selLeptons selection." << std::endl;
        printCollection("selLeptons", selLeptons);
      }
      continue;
    }
    cutFlowTable.update(">= 2 sel leptons", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(">= 2 sel leptons", evtWeightRecorder.get(central_or_shift_main));

    const RecoLepton* selLepton_lead = selLeptons[0];
    const Particle::LorentzVector& selLeptonP4_lead = selLepton_lead->p4();
    int selLepton_lead_type = getLeptonType(selLepton_lead->pdgId());
    const RecoLepton* selLepton_sublead = selLeptons[1];
    const Particle::LorentzVector& selLeptonP4_sublead = selLepton_sublead->p4();
    int selLepton_sublead_type = getLeptonType(selLepton_sublead->pdgId());
    const leptonGenMatchEntry& selLepton_genMatch = getLeptonGenMatch(leptonGenMatch_definitions, selLepton_lead, selLepton_sublead);

    const double minPt_lead = 25.;
    const double minPt_sublead = 15.;
    if ( !(selLepton_lead->cone_pt() > minPt_lead && selLepton_sublead->cone_pt() > minPt_sublead) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS lepton pT selection." << std::endl;
        std::cout << " (leading selLepton pT = " << selLepton_lead->pt() << ", minPt_lead = " << minPt_lead
                  << ", subleading selLepton pT = " << selLepton_sublead->pt() << ", minPt_sublead = " << minPt_sublead << ")" << std::endl;
      }
      continue;
    }
    cutFlowTable.update("lead lepton pT > 25 GeV && sublead lepton pT > 15 GeV", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("lead lepton pT > 25 GeV && sublead lepton pT > 15 GeV", evtWeightRecorder.get(central_or_shift_main));

    bool isLeptonCharge_SS = selLepton_lead->charge()*selLepton_sublead->charge() > 0;
    bool isLeptonCharge_OS = selLepton_lead->charge()*selLepton_sublead->charge() < 0;
    if ( leptonChargeSelection == kOS && isLeptonCharge_SS ) {
      if ( run_lumi_eventSelector ) {
	std::cout << "event " << eventInfo.str() << " FAILS lepton charge selection." << std::endl;
        std::cout << " (leading selLepton charge = " << selLepton_lead->charge()
                  << ", subleading selLepton charge = " << selLepton_sublead->charge() << ", leptonChargeSelection = OS)" << std::endl;
      }
      continue;
    }
    if ( leptonChargeSelection == kSS && isLeptonCharge_OS ) {
      if ( run_lumi_eventSelector ) {
	std::cout << "event " << eventInfo.str() << " FAILS lepton charge selection." << std::endl;
        std::cout << " (leading selLepton charge = " << selLepton_lead->charge()
                  << ", subleading selLepton charge = " << selLepton_sublead->charge() << ", leptonChargeSelection = SS)" << std::endl;
      }
      continue;
    }
    if ( leptonChargeSelection != kDisabled ) {
      cutFlowTable.update(Form("sel lepton-pair %s charge", leptonChargeSelection_string.data()), evtWeightRecorder.get(central_or_shift_main));
    }
    cutFlowHistManager->fillHistograms("sel lepton-pair OS/SS charge", evtWeightRecorder.get(central_or_shift_main));

    // require exactly two leptons passing tight selection criteria, to avoid overlap with other channels
    if ( !(tightLeptonsFull.size() <= 2) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS tightLeptons selection." << std::endl;
        printCollection("tightLeptonsFull", tightLeptonsFull);
      }
      continue;
    }
    cutFlowTable.update("<= 2 tight leptons", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("<= 2 tight leptons", evtWeightRecorder.get(central_or_shift_main));

    // require that trigger paths match lepton flavor (for fakeable leptons)
    if ( !((fakeableElectrons.size() >= 2 &&                              (selTrigger_2e    || selTrigger_1e                  )) ||
           (fakeableElectrons.size() >= 1 && fakeableMuons.size() >= 1 && (selTrigger_1e1mu || selTrigger_1mu || selTrigger_1e)) ||
           (                                 fakeableMuons.size() >= 2 && (selTrigger_2mu   || selTrigger_1mu                 ))) ) {
      if ( run_lumi_eventSelector ) {
	std::cout << "event " << eventInfo.str() << " FAILS trigger selection for given fakeableLepton multiplicity." << std::endl;
        std::cout << " (#fakeableElectrons = " << fakeableElectrons.size()
                  << ", #fakeableMuons = " << fakeableMuons.size()
                  << ", selTrigger_2mu = " << selTrigger_2mu
                  << ", selTrigger_1e1mu = " << selTrigger_1e1mu
                  << ", selTrigger_2e = " << selTrigger_2e
                  << ", selTrigger_1mu = " << selTrigger_1mu
                  << ", selTrigger_1e = " << selTrigger_1e << ")" << std::endl;
      }
      continue;
    }
    cutFlowTable.update("trigger & fakeable lepton flavor matching", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("trigger & fakeable lepton flavor matching", evtWeightRecorder.get(central_or_shift_main));

    // Require that trigger paths match primary datasets,
    // to avoid that the same event is selected multiple times when processing different primary datasets.
    // In case the same event passes the triggers paths for more than one primary datasets,
    // the event is selected in the dataset of highest priority only. 
    // The ranking of the triggers in priority is as follows: 2mu, 1e1mu, 2e, 1mu, 1e
    if ( !isMC && !isDEBUG ) 
    {
      if ( fakeableElectrons.size() >= 2 )
      {
        if ( selTrigger_1e && isTriggered_2e && era != Era::k2018 ) 
        {
          if ( run_lumi_eventSelector ) 
          {
            std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
            std::cout << " (selTrigger_1e = " << selTrigger_1e
                      << ", isTriggered_2e = " << isTriggered_2e << ")" << std::endl;
          }
          continue;
        }
      }
      if ( fakeableElectrons.size() >= 1 && fakeableMuons.size() >= 1 )
      {
        if ( selTrigger_1e && (isTriggered_1mu || isTriggered_1e1mu) )
        {
          if ( run_lumi_eventSelector )
          {
            std::cout << " (selTrigger_1e = " << selTrigger_1e
                      << ", isTriggered_1mu = " << isTriggered_1mu 
                      << ", isTriggered_1e1mu = " << isTriggered_1e1mu << ")" << std::endl;
          }
          continue;
        }
        if ( selTrigger_1mu && isTriggered_1e1mu )
        {
          if ( run_lumi_eventSelector )
          {
            std::cout << " (selTrigger_mu = " << selTrigger_1mu
                      << ", isTriggered_1e1mu = " << isTriggered_1e1mu << ")" << std::endl;
          }
          continue;
        }
      }
      if ( fakeableMuons.size() >= 2 )
      {
        if ( selTrigger_1mu && isTriggered_2mu )
        {
          if ( run_lumi_eventSelector ) {
            std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
            std::cout << " (selTrigger_1mu = " << selTrigger_1mu
                      << ", isTriggered_2mu = " << isTriggered_2mu << ")" << std::endl;
          }
          continue;
        }
      }
    }              
    cutFlowTable.update("trigger & dataset matching", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("trigger & dataset matching", evtWeightRecorder.get(central_or_shift_main));

//--- apply HLT filter
    if ( apply_hlt_filter ) {
      const std::map<hltPathsE, bool> trigger_bits = {
        { hltPathsE::trigger_1e,    selTrigger_1e    },
        { hltPathsE::trigger_1mu,   selTrigger_1mu   },
        { hltPathsE::trigger_2e,    selTrigger_2e    },
        { hltPathsE::trigger_2mu,   selTrigger_2mu   },
        { hltPathsE::trigger_1e1mu, selTrigger_1e1mu },
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
      if(apply_DYMCNormScaleFactors)
      {
        evtWeightRecorder.record_dy_norm(
          dyNormScaleFactors, genLeptonsDY, selJetsAK4.size(), selBJetsAK4_loose.size(), selBJetsAK4_medium.size()
        );
      }

//--- compute event-level weight for data/MC correction of b-tagging efficiency and mistag rate
//   (using the method "Event reweighting using scale factors calculated with a tag and probe method",
//    described on the BTV POG twiki https://twiki.cern.ch/twiki/bin/view/CMS/BTagShapeCalibration )
      evtWeightRecorder.record_btagWeight(selJetsAK4);
      if(btagSFRatioFacility)
      {
        evtWeightRecorder.record_btagSFRatio(btagSFRatioFacility, selJetsAK4.size());
      }

      dataToMCcorrectionInterface->setLeptons({ selLepton_lead, selLepton_sublead });

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
      if( electronSelection >= kFakeable && muonSelection >= kFakeable)
      {
        // apply looseToTight SF to leptons matched to generator-level prompt leptons and passing Tight selection conditions
        evtWeightRecorder.record_leptonIDSF_looseToTight(dataToMCcorrectionInterface);
      }
    }

    bool passesTight_lepton_lead = isMatched(*selLepton_lead, tightElectrons) || isMatched(*selLepton_lead, tightMuons);
    bool passesTight_lepton_sublead = isMatched(*selLepton_sublead, tightElectrons) || isMatched(*selLepton_sublead, tightMuons);

    if(leptonFakeRateInterface)
    {
      evtWeightRecorder.record_jetToLepton_FR_lead(leptonFakeRateInterface, selLepton_lead);
      evtWeightRecorder.record_jetToLepton_FR_sublead(leptonFakeRateInterface, selLepton_sublead);
    }

    if ( !selectBDT ) 
    {
      if(applyFakeRateWeights == kFR_enabled)
      {
        evtWeightRecorder.compute_FR_2l(passesTight_lepton_lead, passesTight_lepton_sublead);
      }
    }

    std::vector<RecoJetAK8> jets_ak8 = jetReaderAK8->read();
    std::vector<const RecoJetAK8*> jet_ptrs_ak8 = convert_to_ptrs(jets_ak8);

    if ( isDEBUG || run_lumi_eventSelector ) {
      printCollection("uncleaned AK8 jets", jet_ptrs_ak8);
    }

    // select jets from H->bb decay
    const std::vector<const RecoJetAK8*> cleanedJetsAK8_wrtLeptons = jetCleanerAK8_dR08(jet_ptrs_ak8, fakeableLeptons);
    const std::vector<const RecoJetAK8*> selJetsAK8_Hbb = jetSelectorAK8_Hbb(cleanedJetsAK8_wrtLeptons, isHigherCSV_ak8);
    const std::vector<const RecoJet*> selJetsAK4_Hbb = jetSelectorAK4_wPileupJetId(cleanedJetsAK4_wrtLeptons, isHigherCSV);
    std::vector<selJetsType_Hbb> selJetsT_Hbb = selectJets_Hbb(selJetsAK8_Hbb, selJetsAK4_Hbb);
    //std::vector<selJetsType_Hbb> selJetsT_Hbb = selectJets_Hbb({}, selJetsAK4_Hbb);
    const selJetsType_Hbb* selJetT_Hbb = nullptr;
    const RecoJetAK8* selJetAK8_Hbb = nullptr;
    const RecoJetBase* selJet1_Hbb = nullptr;
    const RecoJetBase* selJet2_Hbb = nullptr;
    if ( selJetsT_Hbb.size() >= 1 )
    {
      selJetT_Hbb = &selJetsT_Hbb[0];
      selJetAK8_Hbb = selJetT_Hbb->fatjet_;
      selJet1_Hbb = selJetT_Hbb->jet_or_subjet1_;
      selJet2_Hbb = selJetT_Hbb->jet_or_subjet2_;
    }
    if ( !(selJet1_Hbb && selJet2_Hbb) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS >= 2 jets from H->bb selection\n";
      }
      continue;
    }
    cutFlowTable.update(">= 2 jets from H->bb", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(">= 2 jets from H->bb", evtWeightRecorder.get(central_or_shift_main));

    std::vector<const RecoJetBase*> selJets_Hbb = { selJet1_Hbb, selJet2_Hbb };
    std::sort(selJets_Hbb.begin(), selJets_Hbb.end(), isHigherPt);
    const RecoJetBase* selJet_Hbb_lead = selJets_Hbb[0];
    const Particle::LorentzVector& selJetP4_Hbb_lead = selJet_Hbb_lead->p4();
    const RecoJetBase* selJet_Hbb_sublead = selJets_Hbb[1];
    const Particle::LorentzVector& selJetP4_Hbb_sublead = selJet_Hbb_sublead->p4();

    int numBJets_loose, numBJets_medium;
    countBJets_Hbb(*selJetT_Hbb, jetSelectorAK8_Hbb, jetSelectorAK4_bTagLoose, jetSelectorAK4_bTagMedium, numBJets_loose, numBJets_medium);
    if ( !(numBJets_medium >= 1) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS >= 1 medium b-jet selection\n";
      }
      continue;
    }
    cutFlowTable.update(">= 1 medium b-jet", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(">= 1 medium b-jet", evtWeightRecorder.get(central_or_shift_main));

    // select VBF jet candidates
    const std::vector<const RecoJet*> selJetsAK4_vbf_beforeCleaning = jetSelectorAK4_vbf(jet_ptrs_ak4, isHigherPt);
    const std::vector<const RecoJet*> selJetsAK4_vbf_postLeptonCleaning = jetCleaningByIndex ?
      jetCleanerAK4_byIndex(selJetsAK4_vbf_beforeCleaning, fakeableLeptons) :
      jetCleanerAK4_dR04   (selJetsAK4_vbf_beforeCleaning, fakeableLeptons)
    ;
    std::vector<const RecoJet*> selJetsAK4_vbf;
    if ( selJetAK8_Hbb ) {
      const std::vector<const RecoJetAK8*> overlaps = { selJetAK8_Hbb };
      selJetsAK4_vbf = jetCleanerAK4_dR12(selJetsAK4_vbf_postLeptonCleaning, overlaps);
    } else {
      selJetsAK4_vbf = jetCleanerAK4_dR08(selJetsAK4_vbf_postLeptonCleaning, selJets_Hbb);
    }
    if(isDEBUG)
    {
      printCollection("selJetsAK4_vbf", selJetsAK4_vbf);
    }

    //if ( !((selLeptonP4_lead + selLeptonP4_sublead).mass() < 76.) ) {
    //  if ( run_lumi_eventSelector ) {
    //    std::cout << "event " << eventInfo.str() << " FAILS m_ll < 76 GeV cut." << std::endl;
    //  }
    //  continue;
    //}
    //cutFlowTable.update("m(ll) < 76 GeV", evtWeightRecorder.get(central_or_shift_main));
    //cutFlowHistManager->fillHistograms("m(ll) < 76 GeV", evtWeightRecorder.get(central_or_shift_main));

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
    const RecoMEt met = metReader->read();
    const Particle::LorentzVector& metP4 = met.p4();
    const std::vector<const RecoJet*> selJetsAK4_mht = jetSelectorAK4_wPileupJetId(cleanedJetsAK4_wrtLeptons, isHigherPt);
    Particle::LorentzVector mhtP4 = compMHT(fakeableLeptons, {}, selJetsAK4_mht);
    double met_LD = compMEt_LD(metP4, mhtP4);

    // compute HT and STMET variables used for signal extraction in EXO analyses
    std::vector<const RecoJetBase*> selJets_HT_and_STMET;
    selJets_HT_and_STMET.insert(selJets_HT_and_STMET.end(), selJets_Hbb.begin(), selJets_Hbb.end());
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
      if ( applySignalRegionVeto && tightLeptons.size() >= 2 ) failsSignalRegionVeto = true;
    } else if ( electronSelection == kFakeable || muonSelection == kFakeable ) {
      if ( tightLeptons.size() >= 2 ) failsSignalRegionVeto = true;
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

    MEMOutput_hh_bb2l memOutput_hh_bb2l_matched;
    if(memReader.size() > 0)
    {
      const std::string BM = "SM"; // BMS
      //std::cout<<" Reading MEM -- for the basic variables read only to SM \n";
      const std::vector<MEMOutput_hh_bb2l> memOutputs_hh_bb2l = memReader[BM]->read();
      for(const MEMOutput_hh_bb2l & memOutput_hh_bb2l: memOutputs_hh_bb2l)
      {
        const double selLepton_lead_dR = deltaR(
          selLepton_lead->eta(), selLepton_lead->phi(),
          memOutput_hh_bb2l.leadLepton_eta_, memOutput_hh_bb2l.leadLepton_phi_
        );
        if(selLepton_lead_dR > 1.e-2)
        {
          continue;
        }
        const double selLepton_sublead_dR = deltaR(
          selLepton_sublead->eta(), selLepton_sublead->phi(),
          memOutput_hh_bb2l.subleadLepton_eta_, memOutput_hh_bb2l.subleadLepton_phi_
        );

        if(selLepton_sublead_dR > 1.e-2)
        {
          continue;
        }
        memOutput_hh_bb2l_matched = memOutput_hh_bb2l;
        break;
      }
      if(! memOutput_hh_bb2l_matched.is_initialized())
      {
        std::cout << "Warning in " << eventInfo << '\n'
                  << "No MEMOutput_hh_bb2l object found for:\n"
                  << "\tselLepton_lead: pT = " << selLepton_lead->pt()
                  << ", eta = "                << selLepton_lead->eta()
                  << ", phi = "                << selLepton_lead->phi()
                  << ", pdgId = "              << selLepton_lead->pdgId() << "\n"
                     "\tselLepton_sublead: pT = " << selLepton_sublead->pt()
                  << ", eta = "                   << selLepton_sublead->eta()
                  << ", phi = "                   << selLepton_sublead->phi()
                  << ", pdgId = "                 << selLepton_sublead->pdgId() << "\n"
                     "Number of MEM objects read: " << memOutputs_hh_bb2l.size() << '\n'
        ;
        if(! memOutputs_hh_bb2l.empty())
        {
          for(unsigned mem_idx = 0; mem_idx < memOutputs_hh_bb2l.size(); ++mem_idx)
          {
            std::cout << "\t#" << mem_idx << " mem object;\n"
                      << "\t\tlead lepton eta = "    << memOutputs_hh_bb2l[mem_idx].leadLepton_eta_
                      << "; phi = "                  << memOutputs_hh_bb2l[mem_idx].leadLepton_phi_ << '\n'
                      << "\t\tsublead lepton eta = " << memOutputs_hh_bb2l[mem_idx].subleadLepton_eta_
                      << "; phi = "                  << memOutputs_hh_bb2l[mem_idx].subleadLepton_phi_ << '\n'
            ;
          }
        }
        else
        {
          std::cout << "Event contains no MEM objects whatsoever !!\n";
        }
      }
    }
    ////read MEM result by BM
    std::map<std::string, std::map<MEMsys, double>> memOutput_LR;
    std::map<std::string, double> memweight_signal;
    std::map<std::string, double> memweight_background;
    std::map<std::string, double> memOutput_LR_missingBjet;

    std::map<std::string, double> memOutput_LR_toBDT;
    MEMOutput_hh_bb2l memOutput_hh_bb2l_matched_BM;
    for(auto BMlocal : BMS)
    {
      if( memReader.size() > 0 )
      {
        const std::vector<MEMOutput_hh_bb2l> memOutputs_hh_bb2l_BM = memReader[BMlocal]->read(); // Xanda crashing here
        for(const MEMOutput_hh_bb2l & memOutput_hh_bb2l_BM: memOutputs_hh_bb2l_BM)
        {
	        memOutput_hh_bb2l_matched_BM = memOutput_hh_bb2l_BM;
          memOutput_LR[BMlocal] = memOutput_hh_bb2l_matched_BM.get_LR_map();
          memOutput_LR_toBDT[BMlocal] = memOutput_LR[BMlocal][MEMsys::nominal];
          memweight_signal[BMlocal] = memOutput_hh_bb2l_matched_BM.weight_signal();
          memweight_background[BMlocal] = memOutput_hh_bb2l_matched_BM.weight_background();
          if (isDEBUG) std::cout << "To " << BMlocal << " = "<< memOutput_LR[BMlocal][MEMsys::nominal] << " " << memweight_signal[BMlocal] << " " << memweight_background[BMlocal] << "\n";
        }
      } else {
        memOutput_LR[BMlocal] = memOutput_hh_bb2l_matched_BM.get_LR_map();
        memOutput_LR_toBDT[BMlocal] = -1.;
        memweight_signal[BMlocal] = -1.;
        memweight_background[BMlocal] = -1.;
      }
      ///////
      if( memReader_missingBjet.size() > 0 )
      {
        const std::vector<MEMOutput_hh_bb2l> memOutputs_hh_bb2l_missingBjet_BM = memReader_missingBjet[BMlocal]->read();
        //std::cout << "Size " << BMlocal << " = "<< memOutputs_hh_bb2l_missingBjet_BM.size() << "\n";
        for(const MEMOutput_hh_bb2l & memOutput_hh_bb2l_BM: memOutputs_hh_bb2l_missingBjet_BM)
        {
          MEMOutput_hh_bb2l memOutput_hh_bb2l_matched_BM_missingBje = memOutput_hh_bb2l_BM;
          memOutput_LR_missingBjet[BMlocal] = memOutput_hh_bb2l_matched_BM_missingBje.isValid() ? memOutput_hh_bb2l_matched_BM_missingBje.LR() : -1.;
          if (isDEBUG ) std::cout << "To " << BMlocal << " = "<< memOutput_LR_missingBjet[BMlocal] << " (missing bjet) \n";
        }
      } else {
        memOutput_LR_missingBjet[BMlocal] = -1.;
      }
    }

    // compute signal extraction observables
    Particle::LorentzVector HbbP4 = selJetP4_Hbb_lead + selJetP4_Hbb_sublead;
    double m_Hbb             = HbbP4.mass();
    double m_Hbb_regCorr     = 0.;
    double m_Hbb_regRes      = 0.;
    double cosThetaS_Hbb     = -10.;
    double cosThetaS_Hbb_reg = -10.;
    if ( dynamic_cast<const RecoJet*>(selJet_Hbb_lead) && dynamic_cast<const RecoJet*>(selJet_Hbb_sublead) )
    {
      cosThetaS_Hbb = comp_cosThetaStar(selJetP4_Hbb_lead, selJetP4_Hbb_sublead);
      const RecoJet* selJetAK4_Hbb_lead    = dynamic_cast<const RecoJet*>(selJet_Hbb_lead);
      const RecoJet* selJetAK4_Hbb_sublead = dynamic_cast<const RecoJet*>(selJet_Hbb_sublead);
      Particle::LorentzVector HbbP4_reg = selJetAK4_Hbb_lead->p4_bRegCorr() + selJetAK4_Hbb_sublead->p4_bRegCorr();
      cosThetaS_Hbb_reg = comp_cosThetaStar(selJetAK4_Hbb_lead->p4_bRegCorr(), selJetAK4_Hbb_sublead->p4_bRegCorr());
      m_Hbb_regCorr = HbbP4_reg.mass();
      m_Hbb_regRes  = m_Hbb_regCorr*TMath::Sqrt(
         mem::square(selJetAK4_Hbb_lead->bRegRes()/selJetAK4_Hbb_lead->bRegCorr())
       + mem::square(selJetAK4_Hbb_sublead->bRegRes()/selJetAK4_Hbb_sublead->bRegCorr()));
    }
    double tau21_Hbb = -1.;
    if ( selJetAK8_Hbb )
    {
      tau21_Hbb = selJetAK8_Hbb->tau2()/selJetAK8_Hbb->tau1();
    }
    double dR_Hbb    = deltaR(selJetP4_Hbb_lead, selJetP4_Hbb_sublead);
    
    double dPhi_Hbb  = TMath::Abs(deltaPhi(selJetP4_Hbb_lead.phi(), selJetP4_Hbb_sublead.phi())); // CV: map dPhi into interval [0..pi]
    double pT_Hbb    = HbbP4.pt();
    double eta_Hbb   = HbbP4.eta();
    Particle::LorentzVector llP4 = selLeptonP4_lead + selLeptonP4_sublead;
    double m_ll  = llP4.mass();
    double dR_ll = deltaR(selLeptonP4_lead, selLeptonP4_sublead);
    double dPhi_ll = TMath::Abs(deltaPhi(selLeptonP4_lead.phi(), selLeptonP4_sublead.phi()));
    double dEta_ll = TMath::Abs(selLeptonP4_lead.eta() - selLeptonP4_sublead.eta());
    double pT_ll = llP4.pt();
    double dPhi_lep1MEt = TMath::Abs(deltaPhi(selLeptonP4_lead.phi(), metP4.phi()));
    double dPhi_lep2MEt = TMath::Abs(deltaPhi(selLeptonP4_sublead.phi(), metP4.phi()));
    double min_dPhi_lepMEt = TMath::Min(dPhi_lep1MEt, dPhi_lep2MEt);
    double max_dPhi_lepMEt = TMath::Max(dPhi_lep1MEt, dPhi_lep2MEt);
    Particle::LorentzVector HwwP4 = selLeptonP4_lead + selLeptonP4_sublead + metP4;
    double m_Hww = HwwP4.mass();
    double mT_Hww = TMath::Sqrt(2.*llP4.pt()*metP4.pt()*(1. - TMath::Cos(deltaPhi(llP4.phi(), metP4.phi())))); // suggested in section 4.4 of arXiv:1212.5581
    double pT_Hww = HwwP4.pt();
    double Smin_Hww = comp_Smin(selLeptonP4_lead + selLeptonP4_sublead, metP4.px(), metP4.py());
    double met_pt_proj; // suggested in section 4.4 of arXiv:1212.5581
    if ( min_dPhi_lepMEt < 0.5*TMath::Pi() ) met_pt_proj = metP4.pt()*TMath::Sin(min_dPhi_lepMEt);
    else met_pt_proj = metP4.pt();
    double dR_b1lep1 = deltaR(selJetP4_Hbb_lead, selLeptonP4_lead);
    double dR_b1lep2 = deltaR(selJetP4_Hbb_lead, selLeptonP4_sublead);
    double dR_b2lep1 = deltaR(selJetP4_Hbb_sublead, selLeptonP4_lead);
    double dR_b2lep2 = deltaR(selJetP4_Hbb_sublead, selLeptonP4_sublead);
    Particle::LorentzVector HHvisP4 = HbbP4 + selLeptonP4_lead + selLeptonP4_sublead;
    double m_HHvis = HHvisP4.mass();
    double pT_HHvis = HHvisP4.pt();
    double eta_HHvis = HHvisP4.eta();
    double dPhi_HHvis = TMath::Abs(deltaPhi(HbbP4.phi(), (selLeptonP4_lead + selLeptonP4_sublead).phi()));
    Particle::LorentzVector HHP4 = HbbP4 + HwwP4;
    double m_HH = HHP4.mass();
    double pT_HH = HHP4.pt();
    double Smin_HH = comp_Smin(HHvisP4, metP4.px(), metP4.py());
    double dR_HH = deltaR(HbbP4, HwwP4);
    double dPhi_HH = TMath::Abs(deltaPhi(HbbP4.phi(), HwwP4.phi()));
    mT2_2particle mT2Algo_2particle;
    mT2Algo_2particle(
      selLeptonP4_lead.px(), selLeptonP4_lead.py(), selLeptonP4_lead.mass(),
      selLeptonP4_sublead.px(), selLeptonP4_sublead.py(), selLeptonP4_sublead.mass(),
      metP4.px(), metP4.py(), 0.);
    double mT2_W = mT2Algo_2particle.get_min_mT2();
    //int mT2_W_step = mT2Algo_2particle.get_min_step();
    //std::cout << "mT2_W = " << mT2_W << " (found @ step #" << mT2_W_step << ")" << std::endl;
    double cSumPx = selLeptonP4_lead.px() + selLeptonP4_sublead.px() + metP4.px();
    double cSumPy = selLeptonP4_lead.py() + selLeptonP4_sublead.py() + metP4.py();
    mT2Algo_2particle(
      selJetP4_Hbb_lead.px(), selJetP4_Hbb_lead.py(), selJetP4_Hbb_lead.mass(),
      selJetP4_Hbb_sublead.px(), selJetP4_Hbb_sublead.py(), selJetP4_Hbb_sublead.mass(),
      cSumPx, cSumPy, wBosonMass);
    double mT2_top_2particle = mT2Algo_2particle.get_min_mT2();
    //int mT2_top_2particle_step = mT2Algo_2particle.get_min_step();
    //std::cout << "mT2_top_2particle = " << mT2_top_2particle << " (found @ step #" << mT2_top_2particle_step << ")" << std::endl;
    mT2_3particle mT2Algo_3particle;
    mT2Algo_3particle(
      selJetP4_Hbb_lead.px(), selJetP4_Hbb_lead.py(), selJetP4_Hbb_lead.mass(),
      selJetP4_Hbb_sublead.px(), selJetP4_Hbb_sublead.py(), selJetP4_Hbb_sublead.mass(),
      selLeptonP4_lead.px(), selLeptonP4_lead.py(), selLeptonP4_lead.mass(),
      selLeptonP4_sublead.px(), selLeptonP4_sublead.py(), selLeptonP4_sublead.mass(),
      metP4.px(), metP4.py(), 0.);
    double mT2_top_3particle_permutation1 = mT2Algo_3particle.get_min_mT2();
    int mT2_top_3particle_permutation1_step =  mT2Algo_3particle.get_min_step();
    mT2Algo_3particle(
      selJetP4_Hbb_lead.px(), selJetP4_Hbb_lead.py(), selJetP4_Hbb_lead.mass(),
      selJetP4_Hbb_sublead.px(), selJetP4_Hbb_sublead.py(), selJetP4_Hbb_sublead.mass(),
      selLeptonP4_sublead.px(), selLeptonP4_sublead.py(), selLeptonP4_sublead.mass(),
      selLeptonP4_lead.px(), selLeptonP4_lead.py(), selLeptonP4_lead.mass(),
      metP4.px(), metP4.py(), 0.);
    double mT2_top_3particle_permutation2 = mT2Algo_3particle.get_min_mT2();
    double mT2_top_3particle_permutation2_step = mT2Algo_3particle.get_min_step();
    double mT2_top_3particle = -1.;
    double mT2_top_3particle_step = -1;
    if ( mT2_top_3particle_permutation1 <= mT2_top_3particle_permutation2 ) {
      mT2_top_3particle = mT2_top_3particle_permutation1;
      mT2_top_3particle_step = mT2_top_3particle_permutation1_step;
    } else {
      mT2_top_3particle = mT2_top_3particle_permutation2;
      mT2_top_3particle_step = mT2_top_3particle_permutation2_step;
    }
    //std::cout << "mT2_top_3particle:"
    //	        << " permutation1 = " << mT2_top_3particle_permutation1 << " (found @ step #" << mT2_top_3particle_permutation1_step << "),"
    //	        << " permutation2 = " << mT2_top_3particle_permutation2 << " (found @ step #" << mT2_top_3particle_permutation2_step << "),"
    //	        << " min = " << mT2_top_3particle << " (found @ step #" << mT2_top_3particle_step << ")" << std::endl;
    Higgsness algoHiggsness_publishedChi2(Higgsness::kPublishedChi2);
    algoHiggsness_publishedChi2.fit(selLeptonP4_lead, selLeptonP4_sublead, metP4.px(), metP4.py());
    double logHiggsness_publishedChi2 = -99.;
    if ( algoHiggsness_publishedChi2.isValidSolution() ) {
      logHiggsness_publishedChi2 = algoHiggsness_publishedChi2.logHiggsness();
    }
    Topness algoTopness_publishedChi2(Topness::kPublishedChi2);
    algoTopness_publishedChi2.fit(selLeptonP4_lead, selLeptonP4_sublead, selJetP4_Hbb_lead, selJetP4_Hbb_sublead, metP4.px(), metP4.py());
    double logTopness_publishedChi2 = -99.;
    if ( algoTopness_publishedChi2.isValidSolution() ) {
      logTopness_publishedChi2 = algoTopness_publishedChi2.logTopness();
    }
    Higgsness algoHiggsness_fixedChi2(Higgsness::kFixedChi2);
    algoHiggsness_fixedChi2.fit(selLeptonP4_lead, selLeptonP4_sublead, metP4.px(), metP4.py());
    double logHiggsness_fixedChi2 = -99.;
    if ( algoHiggsness_fixedChi2.isValidSolution() ) {
      logHiggsness_fixedChi2 = algoHiggsness_fixedChi2.logHiggsness();
    }
    Topness algoTopness_fixedChi2(Topness::kFixedChi2);
    algoTopness_fixedChi2.fit(selLeptonP4_lead, selLeptonP4_sublead, selJetP4_Hbb_lead, selJetP4_Hbb_sublead, metP4.px(), metP4.py());
    double logTopness_fixedChi2 = -99.;
    if ( algoTopness_fixedChi2.isValidSolution() ) {
      logTopness_fixedChi2 = algoTopness_fixedChi2.logTopness();
    }

    //---------------------------------------------------------------------------
    // CV: compute mass of HH system using "Heavy Mass Estimator" (HME) algorithm
    //    (switch to HMEOutputReader_hh_bb2l in the future !!)

    HMEOutput_hh_bb2l hmeOutput;
    double m_HH_hme = -1.;
    if(run_hme)
    {
      const int ievent = eventInfo.event;
      hmeOutput = hmeInterface_hh_bb2l(selLepton_lead, selLepton_sublead, selJet_Hbb_lead, selJet_Hbb_sublead, met, ievent);
      hmeOutput.eventInfo_ = eventInfo;
    }
    else
    {
      if(hmeReader)
      {
        const std::vector<HMEOutput_hh_bb2l> hmeOutputs_hh_bb2l = hmeReader->read();
        std::cout<<"number of read: " << hmeOutputs_hh_bb2l.size() << "\n";
        for(const HMEOutput_hh_bb2l & hmeOutput_hh_bb2l: hmeOutputs_hh_bb2l)
        {
          std::cout<<" Reading HME -- " << hmeOutput_hh_bb2l.leadLepton_eta_ << " " << hmeOutput_hh_bb2l.leadLepton_phi_<< "\n";
          const double selLepton_lead_dR = deltaR(
            selLepton_lead->eta(), selLepton_lead->phi(),
            hmeOutput_hh_bb2l.leadLepton_eta_, hmeOutput_hh_bb2l.leadLepton_phi_
          );
          if(selLepton_lead_dR > 1.e-2)
          {
            continue;
          }
          const double selLepton_sublead_dR = deltaR(
            selLepton_sublead->eta(), selLepton_sublead->phi(),
            hmeOutput_hh_bb2l.subleadLepton_eta_, hmeOutput_hh_bb2l.subleadLepton_phi_
          );

          if(selLepton_sublead_dR > 1.e-2)
          {
            continue;
          }
          hmeOutput = hmeOutput_hh_bb2l;
          break;
        }
        if(! hmeOutput.is_initialized())
	{
          std::cout << "Warning in " << eventInfo << '\n'
                    << "No HMEOutput_hh_bb2l object found for:\n"
                    << "\tselLepton_lead: pT = " << selLepton_lead->pt()
                    << ", eta = "                << selLepton_lead->eta()
                    << ", phi = "                << selLepton_lead->phi()
                    << ", pdgId = "              << selLepton_lead->pdgId() << "\n"
                    << "\tselLepton_sublead: pT = " << selLepton_sublead->pt()
                    << ", eta = "                   << selLepton_sublead->eta()
                    << ", phi = "                   << selLepton_sublead->phi()
                    << ", pdgId = "                 << selLepton_sublead->pdgId() << "\n"
                    << "Number of HME objects read: " << hmeOutputs_hh_bb2l.size() << '\n'
          ;
          if(! hmeOutputs_hh_bb2l.empty())
          {
            for(unsigned hme_idx = 0; hme_idx < hmeOutputs_hh_bb2l.size(); ++hme_idx)
            {
              std::cout << "\t#" << hme_idx << " hme object;\n"
                        << "\t\tlead lepton eta = "    << hmeOutputs_hh_bb2l[hme_idx].leadLepton_eta_
                        << "; phi = "                  << hmeOutputs_hh_bb2l[hme_idx].leadLepton_phi_ << '\n'
                        << "\t\tsublead lepton eta = " << hmeOutputs_hh_bb2l[hme_idx].subleadLepton_eta_
                        << "; phi = "                  << hmeOutputs_hh_bb2l[hme_idx].subleadLepton_phi_ << '\n'
              ;
            }
          }
          else
          {
            std::cout << "Event contains no HME objects whatsoever !!\n";
          }
        }
      }
    }

    bool hme_isValidSolution = hmeOutput.isValid();
    if ( hme_isValidSolution ) {
      m_HH_hme = hmeOutput.m_HH_hme();
    }
    double hmeCpuTime = hmeOutput.cpuTime();
    if ( isDEBUG ) std::cout << "m_HH_hme = " << m_HH_hme << std::endl;
    //---------------------------------------------------------------------------

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
	if ( dEta_jj > 3.0 && m_jj > 500. ) {
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

    // take the highest eta selJetsForward
    Particle::LorentzVector mostFwdJet = HighestEtaFwdJet(selJetsForward); 

    const std::map<std::string, Particle> ll_inputs = {
      { "bjet1",  Particle(selJetP4_Hbb_lead)       },
      { "bjet2",  Particle(selJetP4_Hbb_sublead)    },
      { "lep1",   Particle(selLepton_lead->p4())    },
      { "lep2",   Particle(selLepton_sublead->p4()) }
    };
    std::map<std::string, const Particle *> ll_inputs_ptr;
    for( const auto & kv: ll_inputs )
    {
      ll_inputs_ptr[kv.first] = &kv.second;
    }

    int numElectrons = 0;
    if ( selLepton_lead_type    == kElectron ) ++numElectrons;
    if ( selLepton_sublead_type == kElectron ) ++numElectrons;
    int numMuons = 0;
    if ( selLepton_lead_type    == kMuon     ) ++numMuons;
    if ( selLepton_sublead_type == kMuon     ) ++numMuons;

    std::map<std::string, double> mvaInputVariables_list = {
      {"mT_lep1",                 comp_MT_met(selLepton_lead, met.pt(), met.phi())},
      {"mT_lep2",                 comp_MT_met(selLepton_sublead, met.pt(), met.phi())},
      {"lep2_conePt",             comp_lep_conePt(*selLepton_sublead)},
      {"bjet2_pt",                selJetP4_Hbb_sublead.pt()},
      {"m_Hww",                   m_Hww},
      {"m_ll",                    m_ll},
      {"pT_ll",                   pT_ll},
      {"m_Hbb",                   m_Hbb},
      {"pT_Hbb",                  pT_Hbb},
      {"pT_HH",                   pT_HH},
      {"pT_Hww",                   pT_Hww},
      {"numBJets_medium",         selBJetsAK4_medium.size()},
      {"met_pt_proj",             met_pt_proj},
      {"m_HHvis",                 m_HHvis},
      {"dPhi_HHvis",                 dPhi_HHvis},
      {"m_HH_hme",                m_HH_hme},
      {"mT2_W",                   mT2_W},
      {"mT2_top_3particle",       mT2_top_3particle},
      {"mT2_top_2particle",       mT2_top_2particle},
      {"met_LD",                  met_LD > 0},
      {"min_dR_blep",             std::min({dR_b1lep1, dR_b1lep2, dR_b2lep1, dR_b2lep2})},
      {"logTopness_fixedChi2",    logTopness_fixedChi2 < 50 ? -0.01 : logTopness_fixedChi2  },
      {"logHiggsness_fixedChi2",  logHiggsness_fixedChi2 < 50 ? -0.01 : logHiggsness_fixedChi2},
      {"logTopness_publishedChi2", logTopness_publishedChi2},
      {"m_Hbb_regCorr",           m_Hbb_regCorr},
      {"Smin_Hww",                Smin_Hww},
      {"mbb_loose",               selBJetsAK4_loose.size()>1  ? (selBJetsAK4_loose[0]->p4()+selBJetsAK4_loose[1]->p4()).mass() : 0},
      {"dR_ll",                   dR_ll},
      {"mht",                     mhtP4.pt()},
      {"mbb_medium",                  selBJetsAK4_medium.size()>1 ? (selBJetsAK4_medium[0]->p4()+selBJetsAK4_medium[1]->p4()).mass() : 0},
      {"lep2_pt",                 selLepton_sublead->pt()},
      {"dR_Hbb",                  dR_Hbb},
      {"dPhi_Hbb",                dPhi_Hbb},
      {"dPhi_HH",                dPhi_HH},
      {"mindr_lep1_jet",           comp_mindr_jet(*selLepton_lead, selJetsAK4)},
      {"max_dPhi_lepMEt",        max_dPhi_lepMEt},
      {"tau21_Hbb",        tau21_Hbb},
      {"STMET",            STMET},
      {"bjet2_pt",                    selJetP4_Hbb_sublead.pt()},
      {"avg_dr_jet_central",          comp_avg_dr_jet(selJetsAK4)},
      {"lep1_e",                      selLepton_lead->p4().e()},
      {"eta_HHvis",                   eta_HHvis},
      {"dR_b1lep2",                   dR_b1lep2}
    };

    if ( bdt_filler )
      {
        double bjet1_btagCSV  = ( selJetAK8_Hbb ) ? selJetAK8_Hbb->subJet1()->BtagCSV() : ( (selJet1_Hbb) ? dynamic_cast<const RecoJet*>(selJet1_Hbb)->BtagCSV() : -1 );
        double bjet2_btagCSV  = ( selJetAK8_Hbb ) ? selJetAK8_Hbb->subJet2()->BtagCSV() : ( (selJet2_Hbb) ? dynamic_cast<const RecoJet*>(selJet2_Hbb)->BtagCSV() : -1 );

        double mindr_lep1_jet = comp_mindr_jet(*selLepton_lead, selJetsAK4);
        double mindr_lep2_jet = comp_mindr_jet(*selLepton_sublead, selJetsAK4);

        double lep1_frWeight  = ( selLepton_lead->genLepton()    ) ? 1. : evtWeightRecorder.get_jetToLepton_FR_lead(central_or_shift_main);
        double lep2_frWeight  = ( selLepton_sublead->genLepton() ) ? 1. : evtWeightRecorder.get_jetToLepton_FR_sublead(central_or_shift_main);

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
          ("bjet1_btagCSV",               bjet1_btagCSV)
          ("bjet2_btagCSV",               bjet2_btagCSV)
          ("lep1_pt",                     selLepton_lead->pt())
          ("lep1_conePt",                 comp_lep_conePt(*selLepton_lead))
          ("lep1_eta",                    selLepton_lead->eta())
          ("lep1_phi",                    selLepton_lead->phi())
          ("lep1_mass",                   selLepton_lead->mass())
          ("lep1_charge",                 selLepton_lead->charge())
          ("lep1_e",                      selLepton_lead->p4().e())
          ("lep1_px",                     selLepton_lead->p4().px())
          ("lep1_py",                     selLepton_lead->p4().py())
          ("lep1_pz",                     selLepton_lead->p4().pz())
          ("lep1_frWeight",               lep1_frWeight)
          ("lep2_pt",                     selLepton_sublead->pt())
          ("lep2_conePt",                 comp_lep_conePt(*selLepton_sublead))
          ("lep2_eta",                    selLepton_sublead->eta())
          ("lep2_phi",                    selLepton_sublead->phi())
          ("lep2_mass",                   selLepton_sublead->mass())
          ("lep2_charge",                 selLepton_sublead->charge())
          ("lep2_e",                      selLepton_sublead->p4().e())
          ("lep2_px",                     selLepton_sublead->p4().px())
          ("lep2_py",                     selLepton_sublead->p4().py())
          ("lep2_pz",                     selLepton_sublead->p4().pz())
          ("lep2_frWeight",               lep2_frWeight)
          ("bjet1_pt",                    selJetP4_Hbb_lead.pt())
          ("bjet1_eta",                   selJetP4_Hbb_lead.eta())
          ("bjet1_phi",                   selJetP4_Hbb_lead.phi())
          ("bjet1_mass",                  selJetP4_Hbb_lead.mass())
          ("bjet1_e",                     selJetP4_Hbb_lead.energy())
          ("bjet1_px",                    selJetP4_Hbb_lead.px())
          ("bjet1_py",                    selJetP4_Hbb_lead.py())
          ("bjet1_pz",                    selJetP4_Hbb_lead.pz())
          ("bjet2_pt",                    selJetP4_Hbb_sublead.pt())
          ("bjet2_eta",                   selJetP4_Hbb_sublead.eta())
          ("bjet2_phi",                   selJetP4_Hbb_sublead.phi())
          ("bjet2_mass",                  selJetP4_Hbb_sublead.mass())
          ("bjet2_e",                     selJetP4_Hbb_sublead.energy())
          ("bjet2_px",                    selJetP4_Hbb_sublead.px())
          ("bjet2_py",                    selJetP4_Hbb_sublead.py())
          ("bjet2_pz",                    selJetP4_Hbb_sublead.pz())
          ("mindr_lep1_jet",              mindr_lep1_jet)
          ("mindr_lep2_jet",              mindr_lep2_jet)
          ("avg_dr_jet_central",          comp_avg_dr_jet(selJetsAK4))
          ("mbb_loose",                   selBJetsAK4_loose.size()>1  ? (selBJetsAK4_loose[0]->p4()+selBJetsAK4_loose[1]->p4()).mass() : 0)
          ("mbb_medium",                  selBJetsAK4_medium.size()>1 ? (selBJetsAK4_medium[0]->p4()+selBJetsAK4_medium[1]->p4()).mass() : 0 )
          ("numElectrons",                selElectrons.size())
          ("sum_Lep_charge",              selLepton_lead -> charge() + selLepton_sublead -> charge())
          ("massLT",                      comp_massL2(selLepton_lead, selLepton_sublead, metP4.pt(), metP4.phi()))
          ("max_Lep_eta",                 TMath::Max(std::abs(selLepton_lead -> eta()), std::abs(selLepton_sublead -> eta())))
          ("dR_HH",                       dR_HH)
          ("met",                         metP4.pt())
          ("mht",                         mhtP4.pt())
          ("met_LD",                      met_LD)
          ("HT",                          HT)
          ("STMET",                       STMET)
          ("m_Hbb",                       m_Hbb)
          ("m_Hbb_regCorr",               m_Hbb_regCorr)
          ("m_Hbb_regRes",                m_Hbb_regRes)
          ("dR_Hbb",                      dR_Hbb)
          ("dPhi_Hbb",                    dPhi_Hbb)
          ("pT_Hbb",                      pT_Hbb)
          ("eta_Hbb",                     eta_Hbb)
          ("tau21_Hbb",                   tau21_Hbb)
          ("cosThetaS_Hbb",               cosThetaS_Hbb)
          ("cosThetaS_Hbb_reg",           cosThetaS_Hbb_reg)
          ("m_ll",                        m_ll)
          ("dR_ll",                       dR_ll)
          ("dPhi_ll",                     dPhi_ll)
          ("dEta_ll",                     dEta_ll)
          ("pT_ll",                       pT_ll)
          ("min_dPhi_lepMEt",             min_dPhi_lepMEt)
          ("max_dPhi_lepMEt",             max_dPhi_lepMEt)
          ("m_Hww",                       m_Hww)
          ("mT_Hww",                      mT_Hww)
          ("Smin_Hww",                    Smin_Hww)
          ("pT_Hww",                      pT_Hww)
          ("met_pt_proj",                 met_pt_proj)
          ("dR_b1lep1",                   dR_b1lep1)
          ("dR_b1lep2",                   dR_b1lep2)
          ("dR_b2lep1",                   dR_b2lep1)
          ("dR_b2lep2",                   dR_b2lep2)
          ("m_HHvis",                     m_HHvis)
          ("pT_HHvis",                    pT_HHvis)
          ("eta_HHvis",                   eta_HHvis)
          ("dPhi_HHvis",                  dPhi_HHvis)
          ("m_HH",                        m_HH)
          ("pT_HH",                       pT_HH)
          ("dPhi_HH",                     dPhi_HH)
          ("Smin_HH",                     Smin_HH)
          ("mT2_W",                       mT2_W)
          ("mT2_top_2particle",           mT2_top_2particle)
          ("mT2_top_3particle",           mT2_top_3particle)
          ("m_HH_hme",                    m_HH_hme)
          ("logTopness_publishedChi2",    logTopness_publishedChi2)
          ("logHiggsness_publishedChi2",  logHiggsness_publishedChi2)
          ("logTopness_fixedChi2",        logTopness_fixedChi2)
          ("logHiggsness_fixedChi2",      logHiggsness_fixedChi2)
          ("vbf_jet1_pt",                 vbf_jet1_pt)
          ("vbf_jet1_eta",                vbf_jet1_eta)
          ("vbf_jet2_pt",                 vbf_jet2_pt)
          ("vbf_jet2_eta",                vbf_jet2_eta)
          ("vbf_dEta_jj",                 vbf_dEta_jj)
          ("vbf_m_jj",                    vbf_m_jj)
          ("genWeight",                   eventInfo.genWeight)
          ("evtWeight",                   evtWeightRecorder.get(central_or_shift_main))
          ("numJets",                     comp_n_jet25_recl(selJetsAK4))
          ("numBJets_loose",              selBJetsAK4_loose.size())
          ("numBJets_medium",             selBJetsAK4_medium.size())
          ("numJets_vbf",                 selJetsAK4_vbf.size())
          ("isHbb_boosted",               selJetAK8_Hbb ? true : false)
          ("isVBF",                       isVBF)
          ("mhh_gen",                     eventInfo.gen_mHH)
          ("costS_gen",                   eventInfo.gen_cosThetaStar)
          //(memweight_signal,              "memweight_signal")
          //(memweight_background,          "memweight_background")
          //(memOutput_LR_toBDT,            "memOutput_LR")                                                                                                                                                   
          //(memOutput_LR_missingBjet,      "memOutput_LR_missingBjet")                                                                                                                                       
          ("mostFwdJet_eta",              selJetsForward.size() >= 1 ? std::abs(mostFwdJet.Eta()) : -1000)
          ("mostFwdJet_pt",               selJetsForward.size() >= 1 ? mostFwdJet.pt() : -1000)
          ("mostFwdJet_phi",              selJetsForward.size() >= 1 ? mostFwdJet.phi() : -1000)
          ("mostFwdJet_E",                selJetsForward.size() >= 1 ? mostFwdJet.energy() : -1000)
          ("leadFwdJet_eta",              selJetsForward.size() >= 1 ? selJetsForward[0] -> absEta() : -1000)
          ("leadFwdJet_pt",               selJetsForward.size() >= 1 ? selJetsForward[0] -> pt() : -1000)
          ("leadFwdJet_phi",              selJetsForward.size() >= 1 ? selJetsForward[0] -> phi() : -1000)
          ("leadFwdJet_E",                selJetsForward.size() >= 1 ? selJetsForward[0] -> p4().energy() : -1000)
          ("numJetsForward",              selJetsForward.size())
          ("lepPairType",                 fabs(selLepton_lead->pdgId()) == fabs(selLepton_sublead->pdgId()))
          (weightMapHH)
          .fill()
          ;
        continue;
      }

//--- compute event-level BDT outputs
    std::map<std::string, double> bdtOutputs_resonant_spin2;
    std::map<std::string, double> bdtOutputs_resonant_spin0;
    std::map<std::string, double> bdtOutputs_nonresonant;
    if ( fillHistograms_BDT )
    {
      if ( selJetAK8_Hbb )
      {
        std::map<std::string, double> bdtInputs_resonant_spin2 = InitializeInputVarMap(mvaInputVariables_list, BDT_resonant_spin2_boosted[0]->mvaInputVariables(), true);
        bdtOutputs_resonant_spin2 = CreateBDTOutputMap(gen_mHH, BDT_resonant_spin2_boosted, bdtInputs_resonant_spin2, eventInfo.event, false, "_spin2");
        std::map<std::string, double> bdtInputs_resonant_spin0 = InitializeInputVarMap(mvaInputVariables_list, BDT_resonant_spin0_boosted[0]->mvaInputVariables(), true);
        bdtOutputs_resonant_spin0 = CreateBDTOutputMap(gen_mHH, BDT_resonant_spin0_boosted, bdtInputs_resonant_spin0, eventInfo.event, false, "_spin0");
        std::map<std::string, double> bdtInputs_nonresonant = InitializeInputVarMap(mvaInputVariables_list, BDT_nonresonant_boosted[0]->mvaInputVariables(), true);
        bdtOutputs_nonresonant = CreateBDTOutputMap(nonRes_BMs, BDT_nonresonant_boosted, bdtInputs_nonresonant, eventInfo.event, true, "");
      }
      else
      {
        std::map<std::string, double> bdtInputs_resonant_spin2 = InitializeInputVarMap(mvaInputVariables_list, BDT_resonant_spin2_resolved[0]->mvaInputVariables(), true);
        bdtOutputs_resonant_spin2 = CreateBDTOutputMap(gen_mHH, BDT_resonant_spin2_resolved, bdtInputs_resonant_spin2, eventInfo.event, false, "_spin2");
        std::map<std::string, double> bdtInputs_resonant_spin0 = InitializeInputVarMap(mvaInputVariables_list, BDT_resonant_spin0_resolved[0]->mvaInputVariables(), true);
        bdtOutputs_resonant_spin0 = CreateBDTOutputMap(gen_mHH, BDT_resonant_spin0_resolved, bdtInputs_resonant_spin0, eventInfo.event, false, "_spin0");
        std::map<std::string, double> bdtInputs_nonresonant = InitializeInputVarMap(mvaInputVariables_list, BDT_nonresonant_resolved[0]->mvaInputVariables(), true);
        bdtOutputs_nonresonant = CreateBDTOutputMap(nonRes_BMs, BDT_nonresonant_resolved, bdtInputs_nonresonant, eventInfo.event, true, "");
      }
    }

//--- compute event-level LBN outputs
    std::map<std::string, std::map<std::string, double>> lbnOutputs_resonant_spin2;
    std::map<std::string, std::map<std::string, double>> lbnOutputs_resonant_spin0;
    std::map<std::string, std::map<std::string, double>> lbnOutputs_nonresonant;
    if ( fillHistograms_LBN )
    {
      if ( selJetAK8_Hbb )
      {
        std::map<std::string, double> hl_inputs_resonant_spin2 = InitializeInputVarMap(mvaInputVariables_list, LBN_resonant_spin2_boosted[0]->hl_mvaInputVariables(), false);
        lbnOutputs_resonant_spin2 = CreateLBNOutputMap(gen_mHH, LBN_resonant_spin2_boosted, ll_inputs_ptr, hl_inputs_resonant_spin2, eventInfo.event, false, "_spin2");
        std::map<std::string, double> hl_inputs_resonant_spin0 = InitializeInputVarMap(mvaInputVariables_list, LBN_resonant_spin0_boosted[0]->hl_mvaInputVariables(), false);
        lbnOutputs_resonant_spin0 = CreateLBNOutputMap(gen_mHH, LBN_resonant_spin0_boosted, ll_inputs_ptr, hl_inputs_resonant_spin0, eventInfo.event, false, "_spin0");
        std::map<std::string, double> hl_inputs_nonresonant = InitializeInputVarMap(mvaInputVariables_list, LBN_nonresonant_boosted[0]->hl_mvaInputVariables());
        lbnOutputs_nonresonant = CreateLBNOutputMap(nonRes_BMs, LBN_nonresonant_boosted, ll_inputs_ptr, hl_inputs_nonresonant, eventInfo.event, true, "");
      }
      else
      {
        std::map<std::string, double> hl_inputs_resonant_spin2 = InitializeInputVarMap(mvaInputVariables_list, LBN_resonant_spin2_resolved[0]->hl_mvaInputVariables(), false);
        lbnOutputs_resonant_spin2 = CreateLBNOutputMap(gen_mHH, LBN_resonant_spin2_resolved, ll_inputs_ptr, hl_inputs_resonant_spin2, eventInfo.event, false, "_spin2");
        std::map<std::string, double> hl_inputs_resonant_spin0 = InitializeInputVarMap(mvaInputVariables_list, LBN_resonant_spin0_resolved[0]->hl_mvaInputVariables(), false);
        lbnOutputs_resonant_spin0 = CreateLBNOutputMap(gen_mHH, LBN_resonant_spin0_resolved, ll_inputs_ptr, hl_inputs_resonant_spin0, eventInfo.event, false, "_spin0");
        std::map<std::string, double> hl_inputs_nonresonant = InitializeInputVarMap(mvaInputVariables_list, LBN_nonresonant_resolved[0]->hl_mvaInputVariables());
        lbnOutputs_nonresonant = CreateLBNOutputMap(nonRes_BMs, LBN_nonresonant_resolved, ll_inputs_ptr, hl_inputs_nonresonant, eventInfo.event, true, "");
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
          if ( selElectrons.size() >= 1 ) {
            selHistManager->leadElectron_->fillHistograms({ selElectrons[0] }, evtWeight);
          }
          if ( selElectrons.size() >= 2 ) {
            selHistManager->subleadElectron_->fillHistograms({ selElectrons[1] }, evtWeight);
          }
          selHistManager->muons_->fillHistograms(selMuons, evtWeight);
          if ( selMuons.size() >= 1 ) {
            selHistManager->leadMuon_->fillHistograms({ selMuons[0] }, evtWeight);
          }
          if ( selMuons.size() >= 2 ) {
            selHistManager->subleadMuon_->fillHistograms({ selMuons[1] }, evtWeight);
          }
          selHistManager->jetsAK4_->fillHistograms(selJetsAK4, evtWeight);
          selHistManager->leadJetAK4_->fillHistograms(selJetsAK4, evtWeight);
          selHistManager->subleadJetAK4_->fillHistograms(selJetsAK4, evtWeight);
          if ( selJetAK8_Hbb ) {
            selHistManager->jetsAK8_Hbb_->fillHistograms({ selJetAK8_Hbb }, evtWeight);
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
            m_ll, dR_ll, dPhi_ll, pT_ll,
            m_HHvis, m_HH,
            m_HH_hme, hmeCpuTime,
            vbf_jet1_pt, vbf_jet1_eta, vbf_jet2_pt, vbf_jet2_eta, vbf_m_jj, vbf_dEta_jj,
            evtWeight
          );
          //if(memReader.size() > 0)
          //{
          //  selHistManager->mem_->fillHistograms(
          //    &memOutput_hh_bb2l_matched,
          //    evtWeight
          //  );
          //}
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
            -1., // CV: bdtOutput for nonresonant_allBMs case not implemented yet !!
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
            { { "HH", -1.} }, // CV: lbnOutput for nonresonant_allBMs case not implemented yet !!
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

    /*if ( bdt_filler ) 
    {
      double bjet1_btagCSV  = ( selJetAK8_Hbb ) ? selJetAK8_Hbb->subJet1()->BtagCSV() : ( (selJet1_Hbb) ? dynamic_cast<const RecoJet*>(selJet1_Hbb)->BtagCSV() : -1 );
      double bjet2_btagCSV  = ( selJetAK8_Hbb ) ? selJetAK8_Hbb->subJet2()->BtagCSV() : ( (selJet2_Hbb) ? dynamic_cast<const RecoJet*>(selJet2_Hbb)->BtagCSV() : -1 );

      double mindr_lep1_jet = comp_mindr_jet(*selLepton_lead, selJetsAK4);
      double mindr_lep2_jet = comp_mindr_jet(*selLepton_sublead, selJetsAK4);

      double lep1_frWeight  = ( selLepton_lead->genLepton()    ) ? 1. : evtWeightRecorder.get_jetToLepton_FR_lead(central_or_shift_main);
      double lep2_frWeight  = ( selLepton_sublead->genLepton() ) ? 1. : evtWeightRecorder.get_jetToLepton_FR_sublead(central_or_shift_main);
      
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
        ("bjet1_btagCSV",               bjet1_btagCSV)
	("bjet2_btagCSV",               bjet2_btagCSV)
        ("lep1_pt",                     selLepton_lead->pt())
	("lep1_conePt",                 comp_lep_conePt(*selLepton_lead))
	("lep1_eta",                    selLepton_lead->eta())
	("lep1_phi",                    selLepton_lead->phi())
	("lep1_mass",                   selLepton_lead->mass())
	("lep1_charge",                 selLepton_lead->charge())
	("lep1_e",                      selLepton_lead->p4().e())
        ("lep1_px",                     selLepton_lead->p4().px())
        ("lep1_py",                     selLepton_lead->p4().py())
        ("lep1_pz",                     selLepton_lead->p4().pz())
        ("lep1_frWeight",               lep1_frWeight)  
        ("lep2_pt",                     selLepton_sublead->pt())
	("lep2_conePt",                 comp_lep_conePt(*selLepton_sublead))
	("lep2_eta",                    selLepton_sublead->eta())
	("lep2_phi",                    selLepton_sublead->phi())
	("lep2_mass",                   selLepton_sublead->mass())
	("lep2_charge",                 selLepton_sublead->charge())
	("lep2_e",                      selLepton_sublead->p4().e())
        ("lep2_px",                     selLepton_sublead->p4().px())
        ("lep2_py",                     selLepton_sublead->p4().py())
        ("lep2_pz",                     selLepton_sublead->p4().pz())
        ("lep2_frWeight",               lep2_frWeight) 
        ("bjet1_pt",                    selJetP4_Hbb_lead.pt())
	("bjet1_eta",                   selJetP4_Hbb_lead.eta())
	("bjet1_phi",                   selJetP4_Hbb_lead.phi())
	("bjet1_mass",                  selJetP4_Hbb_lead.mass())
	("bjet1_e",                     selJetP4_Hbb_lead.energy())
        ("bjet1_px",                    selJetP4_Hbb_lead.px())
        ("bjet1_py",                    selJetP4_Hbb_lead.py())
        ("bjet1_pz",                    selJetP4_Hbb_lead.pz())
	("bjet2_pt",                    selJetP4_Hbb_sublead.pt())
	("bjet2_eta",                   selJetP4_Hbb_sublead.eta())
	("bjet2_phi",                   selJetP4_Hbb_sublead.phi())
	("bjet2_mass",                  selJetP4_Hbb_sublead.mass())
	("bjet2_e",                     selJetP4_Hbb_sublead.energy())
        ("bjet2_px",                    selJetP4_Hbb_sublead.px())
        ("bjet2_py",                    selJetP4_Hbb_sublead.py())
        ("bjet2_pz",                    selJetP4_Hbb_sublead.pz())
        ("mindr_lep1_jet",              mindr_lep1_jet)
        ("mindr_lep2_jet",              mindr_lep2_jet)
        ("avg_dr_jet_central",          comp_avg_dr_jet(selJetsAK4))
        ("mbb_loose",                   selBJetsAK4_loose.size()>1  ? (selBJetsAK4_loose[0]->p4()+selBJetsAK4_loose[1]->p4()).mass() : 0)
        ("mbb_medium",                  selBJetsAK4_medium.size()>1 ? (selBJetsAK4_medium[0]->p4()+selBJetsAK4_medium[1]->p4()).mass() : 0 )
        ("numElectrons",                selElectrons.size())
        ("sum_Lep_charge",              selLepton_lead -> charge() + selLepton_sublead -> charge())
        ("massLT",                      comp_massL2(selLepton_lead, selLepton_sublead, metP4.pt(), metP4.phi()))
        ("max_Lep_eta",                 TMath::Max(std::abs(selLepton_lead -> eta()), std::abs(selLepton_sublead -> eta())))
        ("dR_HH",                       dR_HH)
        ("met",                         metP4.pt())
        ("mht",                         mhtP4.pt())
        ("met_LD",                      met_LD)
        ("HT",                          HT)
        ("STMET",                       STMET)
        ("m_Hbb",                       m_Hbb)
        ("m_Hbb_regCorr",               m_Hbb_regCorr)
        ("m_Hbb_regRes",                m_Hbb_regRes)
        ("dR_Hbb",                      dR_Hbb)
        ("dPhi_Hbb",                    dPhi_Hbb)
        ("pT_Hbb",                      pT_Hbb)
        ("eta_Hbb",                     eta_Hbb)
        ("tau21_Hbb",                   tau21_Hbb)
	("cosThetaS_Hbb",               cosThetaS_Hbb)
	("cosThetaS_Hbb_reg",           cosThetaS_Hbb_reg)
        ("m_ll",                        m_ll)
        ("dR_ll",                       dR_ll)
        ("dPhi_ll",                     dPhi_ll)
        ("dEta_ll",                     dEta_ll)
        ("pT_ll",                       pT_ll)
      	("min_dPhi_lepMEt",             min_dPhi_lepMEt)
      	("max_dPhi_lepMEt",             max_dPhi_lepMEt)
        ("m_Hww",                       m_Hww)
        ("mT_Hww",                      mT_Hww)
        ("Smin_Hww",                    Smin_Hww)
        ("pT_Hww",                      pT_Hww)
      	("met_pt_proj",                 met_pt_proj)
      	("dR_b1lep1",                   dR_b1lep1)
        ("dR_b1lep2",                   dR_b1lep2)
        ("dR_b2lep1",                   dR_b2lep1)
        ("dR_b2lep2",                   dR_b2lep2)
        ("m_HHvis",                     m_HHvis)
        ("pT_HHvis",                    pT_HHvis)
        ("eta_HHvis",                   eta_HHvis)
        ("dPhi_HHvis",                  dPhi_HHvis)
        ("m_HH",                        m_HH)
        ("pT_HH",                       pT_HH)
        ("dPhi_HH",                     dPhi_HH)
      	("Smin_HH",                     Smin_HH)
        ("mT2_W",                       mT2_W)
        ("mT2_top_2particle",           mT2_top_2particle)
        ("mT2_top_3particle",           mT2_top_3particle)
        ("m_HH_hme",                    m_HH_hme)
        ("logTopness_publishedChi2",    logTopness_publishedChi2)
        ("logHiggsness_publishedChi2",  logHiggsness_publishedChi2)
        ("logTopness_fixedChi2",        logTopness_fixedChi2)
        ("logHiggsness_fixedChi2",      logHiggsness_fixedChi2)
        ("vbf_jet1_pt",                 vbf_jet1_pt)
        ("vbf_jet1_eta",                vbf_jet1_eta)
        ("vbf_jet2_pt",                 vbf_jet2_pt)
      	("vbf_jet2_eta",                vbf_jet2_eta)
        ("vbf_dEta_jj",                 vbf_dEta_jj)
        ("vbf_m_jj",                    vbf_m_jj)
        ("genWeight",                   eventInfo.genWeight)
        ("evtWeight",                   evtWeightRecorder.get(central_or_shift_main))
        ("numJets",                     comp_n_jet25_recl(selJetsAK4))
        ("numBJets_loose",              selBJetsAK4_loose.size())
        ("numBJets_medium",             selBJetsAK4_medium.size())
        ("numJets_vbf",                 selJetsAK4_vbf.size())
      	("isHbb_boosted",               selJetAK8_Hbb ? true : false)
        ("isVBF",                       isVBF)
        ("mhh_gen",                     eventInfo.gen_mHH)
        ("costS_gen",                   eventInfo.gen_cosThetaStar)
        //(memweight_signal,              "memweight_signal")
        //(memweight_background,          "memweight_background")
        //(memOutput_LR_toBDT,            "memOutput_LR")
        //(memOutput_LR_missingBjet,      "memOutput_LR_missingBjet")
        ("mostFwdJet_eta",              selJetsForward.size() >= 1 ? std::abs(mostFwdJet.Eta()) : -1000)
	("mostFwdJet_pt",               selJetsForward.size() >= 1 ? mostFwdJet.pt() : -1000)
	("mostFwdJet_phi",              selJetsForward.size() >= 1 ? mostFwdJet.phi() : -1000)
	("mostFwdJet_E",                selJetsForward.size() >= 1 ? mostFwdJet.energy() : -1000)
	("leadFwdJet_eta",              selJetsForward.size() >= 1 ? selJetsForward[0] -> absEta() : -1000)
	("leadFwdJet_pt",               selJetsForward.size() >= 1 ? selJetsForward[0] -> pt() : -1000)
	("leadFwdJet_phi",              selJetsForward.size() >= 1 ? selJetsForward[0] -> phi() : -1000)
	("leadFwdJet_E",                selJetsForward.size() >= 1 ? selJetsForward[0] -> p4().energy() : -1000)
	("numJetsForward",              selJetsForward.size())
        ("lepPairType",                 fabs(selLepton_lead->pdgId()) == fabs(selLepton_sublead->pdgId())) 
        (weightMapHH)
        .fill()
      ;
      }*/

    if(snm)
    {
      snm->read(eventInfo);
      snm->read(evtWeightRecorder.get_toppt_rwgt("central"),  FloatVariableType_bbww::topPt_wgt);
      snm->read({
        triggers_1e, triggers_1mu, triggers_2e, triggers_1e1mu, triggers_2mu,
      });

      snm->read(preselMuons, fakeableMuons, tightMuons);
      snm->read(preselElectrons, fakeableElectrons, tightElectrons);
      snm->read(selJetsAK4, selBJetsAK4_loose.size(), selBJetsAK4_medium.size());
      snm->read(selJetsAK8_Hbb, false);

      std::vector<const RecoJet*> tmpJets_vbf;
      if(selJet_vbf_lead)    { tmpJets_vbf.push_back(selJet_vbf_lead);    }
      if(selJet_vbf_sublead) { tmpJets_vbf.push_back(selJet_vbf_sublead); }
      snm->read(
        selJetsAK4_vbf_beforeCleaning,
        tmpJets_vbf,
        selJetsAK4_vbf_postLeptonCleaning.size(),
        selJetsAK4_vbf.size()
      );
      if(isVBF)
      {
        snm->read(vbf_m_jj,    FloatVariableType_bbww::vbf_m_jj);
        snm->read(vbf_dEta_jj, FloatVariableType_bbww::vbf_dEta_jj);
      }
    
      bool isHbb_boosted = ( selJetAK8_Hbb ) ? true : false;
      snm->read(isHbb_boosted, false, !isHbb_boosted);
      const bool is_ee = selLepton_lead_type == kElectron && selLepton_sublead_type == kElectron;
      const bool is_mm = selLepton_lead_type == kMuon     && selLepton_sublead_type == kMuon;
      const bool is_em = ! (is_ee || is_mm);
      snm->read(is_ee, is_mm, is_em, static_cast<int>(isLeptonCharge_SS));

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
      snm->read(eventInfo.pileupWeight,                 FloatVariableType_bbww::PU_weight);
      snm->read(eventInfo.genWeight,                    FloatVariableType_bbww::MC_weight);
      snm->read(m_HH_hme,                               FloatVariableType_bbww::HME);
      snm->read(pileupJetIDSF,                          FloatVariableType_bbww::PU_jetID_SF);
      snm->read(met.pt(),                               FloatVariableType_bbww::PFMET);
      snm->read(met.phi(),                              FloatVariableType_bbww::PFMETphi);
      snm->read(memOutput_LR["SM"][MEMsys::nominal],    FloatVariableType_bbww::MEM_LR);
      snm->read(memOutput_LR["SM"][MEMsys::up],         FloatVariableType_bbww::MEM_LR_up);
      snm->read(memOutput_LR["SM"][MEMsys::down],       FloatVariableType_bbww::MEM_LR_down);

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
    if(isDEBUG)
    {
      std::cout << evtWeightRecorder << '\n';
    }
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
                << " (weighted = " << selectedEntries_weighted_byGenMatchType[central_or_shift][process_and_genMatch] << ")\n"
      ;
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
  delete metReader;
  delete metFilterReader;
  delete genLeptonReader;
  delete genHadTauReader;
  delete genPhotonReader;
  delete genJetReader;
  delete lheInfoReader;
  delete psWeightReader;
  //delete memReader;
  for (auto BM : memReader)
  {
    delete (BM.second);
  }

  for(auto & kv: genEvtHistManager_beforeCuts)
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

  delete eventWeightManager;

  delete HHWeight_calc;
  delete HHWeight_calc_LOtoNLO;

  hltPaths_delete(triggers_1e);
  hltPaths_delete(triggers_2e);
  hltPaths_delete(triggers_1mu);
  hltPaths_delete(triggers_2mu);
  hltPaths_delete(triggers_1e1mu);

  delete inputTree;
  delete snm;

  clock.Show("analyze_hh_bb2l");

  return EXIT_SUCCESS;
}
