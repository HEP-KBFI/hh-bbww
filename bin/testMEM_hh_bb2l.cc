#include "FWCore/ParameterSet/interface/ParameterSet.h" // edm::ParameterSet
#include "FWCore/PythonParameterSet/interface/MakeParameterSets.h" // edm::readPSetsFrom()
#include "FWCore/Utilities/interface/Exception.h" // cms::Exception
#include "PhysicsTools/FWLite/interface/TFileService.h" // fwlite::TFileService
#include "DataFormats/FWLite/interface/InputSource.h" // fwlite::InputSource
#include "DataFormats/FWLite/interface/OutputFiles.h" // fwlite::OutputFiles
#include "DataFormats/Math/interface/LorentzVector.h" // math::PtEtaPhiMLorentzVector
#include "DataFormats/Math/interface/deltaR.h" // deltaR
#include "DataFormats/Math/interface/deltaPhi.h" // deltaPhi

#include <TBenchmark.h> // TBenchmark
#include <TString.h> // TString, Form
#include <TError.h> // gErrorAbortLevel, kError
#include <TRandom3.h> // TRandom3
#include <TLorentzVector.h> // TLorentzVector 

#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h" // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/RecoJet.h" // RecoJet
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEt.h" // RecoMEt
#include "tthAnalysis/HiggsToTauTau/interface/GenLepton.h" // GenLepton
#include "tthAnalysis/HiggsToTauTau/interface/GenJet.h" // GenJet
#include "tthAnalysis/HiggsToTauTau/interface/EventInfo.h" // EventInfo
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronReader.h" // RecoElectronReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonReader.h" // RecoMuonReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetReader.h" // RecoJetReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetReaderAK8.h" // RecoJetReaderAK8
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEtReader.h" // RecoMEtReader
#include "tthAnalysis/HiggsToTauTau/interface/MEtFilterReader.h" // MEtFilterReader
#include "tthAnalysis/HiggsToTauTau/interface/GenLeptonReader.h" // GenLeptonReader
#include "tthAnalysis/HiggsToTauTau/interface/GenParticleReader.h" // GenParticleReader
#include "tthAnalysis/HiggsToTauTau/interface/GenJetReader.h" // GenJetReader
#include "tthAnalysis/HiggsToTauTau/interface/LHEInfoReader.h" // LHEInfoReader
#include "tthAnalysis/HiggsToTauTau/interface/EventInfoReader.h" // EventInfoReader
#include "tthAnalysis/HiggsToTauTau/interface/convert_to_ptrs.h" // convert_to_ptrs
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
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // getBTagWeight_option, getHadTau_genPdgId, isHigherPt, isMatched, contains, findFile
#include "tthAnalysis/HiggsToTauTau/interface/generalAuxFunctions.h" // format_vstring
#include "tthAnalysis/HiggsToTauTau/interface/mvaInputVariables.h" // comp_lep1_conePt, comp_lep2_conePt
#include "tthAnalysis/HiggsToTauTau/interface/hltPath.h" // hltPath, create_hltPaths, hltPaths_isTriggered, hltPaths_delete
#include "tthAnalysis/HiggsToTauTau/interface/hltPathReader.h" // hltPathReader
#include "tthAnalysis/HiggsToTauTau/interface/Data_to_MC_CorrectionInterface_2016.h"
#include "tthAnalysis/HiggsToTauTau/interface/Data_to_MC_CorrectionInterface_2017.h"
#include "tthAnalysis/HiggsToTauTau/interface/Data_to_MC_CorrectionInterface_2018.h"
#include "tthAnalysis/HiggsToTauTau/interface/lutAuxFunctions.h" // loadTH2, get_sf_from_TH2
#include "tthAnalysis/HiggsToTauTau/interface/cutFlowTable.h" // cutFlowTableType
#include "tthAnalysis/HiggsToTauTau/interface/TTreeWrapper.h" // TTreeWrapper
#include "tthAnalysis/HiggsToTauTau/interface/hltFilter.h" // hltFilter()

#include "hhAnalysis/bbww/interface/EvtHistManager_hh_bb2l.h" // EvtHistManager_hh_bb2l
#include "hhAnalysis/bbww/interface/RecoJetCollectionSelectorAK8_bbWW_Hbb.h" // RecoJetSelectorAK8_bbWW_Hbb
#include "tthAnalysis/HiggsToTauTau/interface/mT2_2particle.h" // mT2_2particle
#include "tthAnalysis/HiggsToTauTau/interface/mT2_3particle.h" // mT2_3particle
#include "tthAnalysis/HiggsToTauTau/interface/Higgsness.h" // Higgsness
#include "tthAnalysis/HiggsToTauTau/interface/Topness.h" // Topness
#include "hhAnalysis/Heavymassestimator/interface/heavyMassEstimator.h" // heavyMassEstimator (HME) algorithm for computation of HH mass
#include "tthAnalysis/HiggsToTauTau/interface/LocalFileInPath.h" // LocalFileInPath
#include "hhAnalysis/bbwwMEM/interface/MEMbbwwAlgoDilepton.h"
#include "hhAnalysis/bbwwMEM/interface/MeasuredParticle.h" // MeasuredParticle
#include "hhAnalysis/bbwwMEM/interface/memAuxFunctions.h"
#include "hhAnalysis/bbww/interface/testMEMauxFunctions.h" // findGenLepton_and_NeutrinoFromWBoson
#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow()

#include <boost/math/special_functions/sign.hpp> // boost::math::sign()
#include "tthAnalysis/HiggsToTauTau/interface/XGBInterface.h" // XGBInterface
#include "tthAnalysis/HiggsToTauTau/interface/MVAInputVarHistManager.h" // MVAInputVarHistManager

#include <iostream> // std::cerr, std::fixed
#include <iomanip> // std::setprecision(), std::setw()
#include <string> // std::string
#include <vector> // std::vector<>
#include <cstdlib> // EXIT_SUCCESS, EXIT_FAILURE
#include <fstream> // std::ofstream
#include <assert.h> // assert
#include "tthAnalysis/HiggsToTauTau/interface/TMVAInterface.h" // TMVAInterface

typedef math::PtEtaPhiMLorentzVector LV;
typedef std::vector<std::string> vstring;
typedef std::vector<double> vdouble;

/**
 * @brief Produce datacard and control plots for dilepton category of the HH->bbWW analysis.
 */
int main(int argc, char* argv[])
{
//--- throw an exception in case ROOT encounters an error
  gErrorAbortLevel = kError;

//--- parse command-line arguments
  if ( argc < 2 ) {
    std::cout << "Usage: " << argv[0] << " [parameters.py]" << std::endl;
    return EXIT_FAILURE;
  }

  std::cout << "<testMEM_hh_bb2l>:" << std::endl;

//--- keep track of time it takes the macro to execute
  TBenchmark clock;
  clock.Start("testMEM_hh_bb2l");

//--- read python configuration parameters
  if ( !edm::readPSetsFrom(argv[1])->existsAs<edm::ParameterSet>("process") )
    throw cms::Exception("testMEM_hh_bb2l")
      << "No ParameterSet 'process' found in configuration file = " << argv[1] << " !!\n";

  edm::ParameterSet cfg = edm::readPSetsFrom(argv[1])->getParameter<edm::ParameterSet>("process");

  edm::ParameterSet cfg_testMEM = cfg.getParameter<edm::ParameterSet>("testMEM_hh_bb2l");

  std::string treeName = cfg_testMEM.getParameter<std::string>("treeName");

  std::string process_string = cfg_testMEM.getParameter<std::string>("process");
  bool isSignal = ( process_string == "signal" ) ? true : false;

  std::string histogramDir = cfg_testMEM.getParameter<std::string>("histogramDir");
  
  std::string era_string = cfg_testMEM.getParameter<std::string>("era");
  const int era = get_era(era_string);

  vstring triggerNames_1e = cfg_testMEM.getParameter<vstring>("triggers_1e");
  std::vector<hltPath*> triggers_1e = create_hltPaths(triggerNames_1e);
  bool use_triggers_1e = cfg_testMEM.getParameter<bool>("use_triggers_1e");
  vstring triggerNames_2e = cfg_testMEM.getParameter<vstring>("triggers_2e");
  std::vector<hltPath*> triggers_2e = create_hltPaths(triggerNames_2e);
  bool use_triggers_2e = cfg_testMEM.getParameter<bool>("use_triggers_2e");
  vstring triggerNames_1mu = cfg_testMEM.getParameter<vstring>("triggers_1mu");
  std::vector<hltPath*> triggers_1mu = create_hltPaths(triggerNames_1mu);
  bool use_triggers_1mu = cfg_testMEM.getParameter<bool>("use_triggers_1mu");
  vstring triggerNames_2mu = cfg_testMEM.getParameter<vstring>("triggers_2mu");
  std::vector<hltPath*> triggers_2mu = create_hltPaths(triggerNames_2mu);
  bool use_triggers_2mu = cfg_testMEM.getParameter<bool>("use_triggers_2mu");
  vstring triggerNames_1e1mu = cfg_testMEM.getParameter<vstring>("triggers_1e1mu");
  std::vector<hltPath*> triggers_1e1mu = create_hltPaths(triggerNames_1e1mu);
  bool use_triggers_1e1mu = cfg_testMEM.getParameter<bool>("use_triggers_1e1mu");

  bool apply_offline_e_trigger_cuts_1e = cfg_testMEM.getParameter<bool>("apply_offline_e_trigger_cuts_1e");
  bool apply_offline_e_trigger_cuts_2e = cfg_testMEM.getParameter<bool>("apply_offline_e_trigger_cuts_2e");
  bool apply_offline_e_trigger_cuts_1mu = cfg_testMEM.getParameter<bool>("apply_offline_e_trigger_cuts_1mu");
  bool apply_offline_e_trigger_cuts_2mu = cfg_testMEM.getParameter<bool>("apply_offline_e_trigger_cuts_2mu");
  bool apply_offline_e_trigger_cuts_1e1mu = cfg_testMEM.getParameter<bool>("apply_offline_e_trigger_cuts_1e1mu");

  enum { kOS, kSS, kDisabled };
  std::string leptonChargeSelection_string = cfg_testMEM.getParameter<std::string>("leptonChargeSelection");
  int leptonChargeSelection = -1;
  if      ( leptonChargeSelection_string == "OS"       ) leptonChargeSelection = kOS;
  else if ( leptonChargeSelection_string == "SS"       ) leptonChargeSelection = kSS;
  else if ( leptonChargeSelection_string == "disabled" ) leptonChargeSelection = kDisabled;
  else throw cms::Exception("testMEM_hh_bb2l")
    << "Invalid Configuration parameter 'leptonChargeSelection' = " << leptonChargeSelection_string << " !!\n";

  const std::string electronSelection_string = cfg_testMEM.getParameter<std::string>("electronSelection");
  const std::string muonSelection_string     = cfg_testMEM.getParameter<std::string>("muonSelection");
  std::cout << "electronSelection_string = " << electronSelection_string << "\n"
               "muonSelection_string     = " << muonSelection_string     << '\n'
  ;
  const int electronSelection = get_selection(electronSelection_string);
  const int muonSelection     = get_selection(muonSelection_string);
  double lep_mva_cut = cfg_testMEM.getParameter<double>("lep_mva_cut"); // CV: used for tight lepton selection only

  bool isMC = true;
  bool isMC_tH = ( process_string == "tHq" || process_string == "tHW" ) ? true : false;
  bool hasLHE = cfg_testMEM.getParameter<bool>("hasLHE");
  std::string central_or_shift = cfg_testMEM.getParameter<std::string>("central_or_shift");
  double lumiScale = 1.;
  bool apply_genWeight = cfg_testMEM.getParameter<bool>("apply_genWeight");
  bool apply_hlt_filter = cfg_testMEM.getParameter<bool>("apply_hlt_filter");
  bool apply_met_filters = cfg_testMEM.getParameter<bool>("apply_met_filters");
  edm::ParameterSet cfgMEtFilter = cfg_testMEM.getParameter<edm::ParameterSet>("cfgMEtFilter");
  MEtFilterSelector metFilterSelector(cfgMEtFilter, isMC);

  bool isDEBUG = cfg_testMEM.getParameter<bool>("isDEBUG");

  edm::ParameterSet cfg_dataToMCcorrectionInterface;
  cfg_dataToMCcorrectionInterface.addParameter<std::string>("era", era_string);
  cfg_dataToMCcorrectionInterface.addParameter<std::string>("hadTauSelection", "dR03mvaMedium"); // CV: dummy value (no taus used in HH->bbWW channel)
  cfg_dataToMCcorrectionInterface.addParameter<int>("hadTauSelection_antiElectron", -1);
  cfg_dataToMCcorrectionInterface.addParameter<int>("hadTauSelection_antiMuon", -1);
  cfg_dataToMCcorrectionInterface.addParameter<std::string>("central_or_shift", central_or_shift);
  Data_to_MC_CorrectionInterface_Base * dataToMCcorrectionInterface = nullptr;
  switch(era)
  {
    case kEra_2016: dataToMCcorrectionInterface = new Data_to_MC_CorrectionInterface_2016(cfg_dataToMCcorrectionInterface); break;
    case kEra_2017: dataToMCcorrectionInterface = new Data_to_MC_CorrectionInterface_2017(cfg_dataToMCcorrectionInterface); break;
    case kEra_2018: dataToMCcorrectionInterface = new Data_to_MC_CorrectionInterface_2018(cfg_dataToMCcorrectionInterface); break;
    default: throw cmsException("testMEM_hh_bb2l", __LINE__) << "Invalid era = " << era;
  }

  std::string branchName_electrons = cfg_testMEM.getParameter<std::string>("branchName_electrons");
  std::string branchName_muons = cfg_testMEM.getParameter<std::string>("branchName_muons");
  std::string branchName_jets_ak4 = cfg_testMEM.getParameter<std::string>("branchName_jets_ak4");
  std::string branchName_jets_ak8 = cfg_testMEM.getParameter<std::string>("branchName_jets_ak8");
  std::string branchName_subjets_ak8 = cfg_testMEM.getParameter<std::string>("branchName_subjets_ak8");
  std::string branchName_met = cfg_testMEM.getParameter<std::string>("branchName_met");

  std::string branchName_genLeptons = cfg_testMEM.getParameter<std::string>("branchName_genLeptons");
  std::string branchName_genNeutrinos = cfg_testMEM.getParameter<std::string>("branchName_genNeutrinos");
  std::string branchName_genJets = cfg_testMEM.getParameter<std::string>("branchName_genJets");

  // branches specific to HH signal
  std::string branchName_genParticlesFromHiggs = cfg_testMEM.getParameter<std::string>("branchName_genParticlesFromHiggs");
  
  // branches specific to ttbar background
  std::string branchName_genLeptonsFromTop = cfg_testMEM.getParameter<std::string>("branchName_genLeptonsFromTop");
  std::string branchName_genNeutrinosFromTop = cfg_testMEM.getParameter<std::string>("branchName_genNeutrinosFromTop");
  std::string branchName_genBQuarksFromTop = cfg_testMEM.getParameter<std::string>("branchName_genBQuarksFromTop");

  int genMatchingOption = cfg_testMEM.getParameter<int>("genMatchingOption");

  std::string selEventsFileName_input = cfg_testMEM.getParameter<std::string>("selEventsFileName_input");
  std::cout << "selEventsFileName_input = " << selEventsFileName_input << std::endl;
  RunLumiEventSelector* run_lumi_eventSelector = 0;
  if ( selEventsFileName_input != "" ) {
    edm::ParameterSet cfg_runLumiEventSelector;
    cfg_runLumiEventSelector.addParameter<std::string>("inputFileName", selEventsFileName_input);
    cfg_runLumiEventSelector.addParameter<std::string>("separator", ":");
    run_lumi_eventSelector = new RunLumiEventSelector(cfg_runLumiEventSelector);
  }

  std::string selEventsFileName_output = cfg_testMEM.getParameter<std::string>("selEventsFileName_output");
  std::cout << "selEventsFileName_output = " << selEventsFileName_output << std::endl;

  fwlite::InputSource inputFiles(cfg);
  int maxEvents = inputFiles.maxEvents();
  std::cout << " maxEvents = " << maxEvents << std::endl;
  int maxSelEvents = cfg_testMEM.getParameter<int>("maxSelEvents");
  std::cout << " maxSelEvents = " << maxSelEvents << std::endl;
  unsigned reportEvery = inputFiles.reportAfter();

  fwlite::OutputFiles outputFile(cfg);
  fwlite::TFileService fs = fwlite::TFileService(outputFile.file().data());

  TTreeWrapper* inputTree = new TTreeWrapper(treeName.data(), inputFiles.files(), maxEvents);
  std::cout << "Loaded " << inputTree->getFileCount() << " file(s)." << std::endl;

//--- declare event-level variables
  EventInfo eventInfo(isSignal, isMC, isMC_tH);
  EventInfoReader eventInfoReader(&eventInfo);
  inputTree->registerReader(&eventInfoReader);

  hltPathReader hltPathReader_instance({ triggers_1e, triggers_2e, triggers_1mu, triggers_2mu, triggers_1e1mu });
  inputTree->registerReader(&hltPathReader_instance);

//--- declare particle collections
  const bool readGenObjects = false;
  RecoMuonReader* muonReader = new RecoMuonReader(era, branchName_muons, readGenObjects);
  inputTree->registerReader(muonReader);
  RecoMuonCollectionGenMatcher muonGenMatcher;
  RecoMuonCollectionSelectorLoose preselMuonSelector(era, -1, isDEBUG);
  RecoMuonCollectionSelectorFakeable fakeableMuonSelector(era, -1, isDEBUG);
  RecoMuonCollectionSelectorTight tightMuonSelector(era, -1, isDEBUG);
  tightMuonSelector.getSelector().set_min_mvaTTH(lep_mva_cut);

  RecoElectronReader* electronReader = new RecoElectronReader(era, branchName_electrons, readGenObjects);
  inputTree->registerReader(electronReader);
  RecoElectronCollectionGenMatcher electronGenMatcher;
  RecoElectronCollectionCleaner electronCleaner(0.3, isDEBUG);
  RecoElectronCollectionSelectorLoose preselElectronSelector(era, -1, isDEBUG);
  RecoElectronCollectionSelectorFakeable fakeableElectronSelector(era, -1, isDEBUG);
  RecoElectronCollectionSelectorTight tightElectronSelector(era, -1, isDEBUG);
  tightElectronSelector.getSelector().set_min_mvaTTH(lep_mva_cut);

  RecoJetReader* jetReaderAK4 = new RecoJetReader(era, isMC, branchName_jets_ak4, readGenObjects);
  inputTree->registerReader(jetReaderAK4);
  RecoJetCollectionGenMatcher jetGenMatcherAK4;
  RecoJetCollectionCleaner jetCleanerAK4_dR04(0.4, isDEBUG);
  RecoJetCollectionCleaner jetCleanerAK4_dR08(0.8, isDEBUG);
  RecoJetCollectionCleaner jetCleanerAK4_dR12(1.2, isDEBUG);
  RecoJetCollectionSelector jetSelectorAK4(era, -1, isDEBUG);
  RecoJetCollectionSelector jetSelectorAK4_vbf(era, -1, isDEBUG);
  //jetSelectorAK4_vbf.getSelector().set_min_pt(30.);
  jetSelectorAK4_vbf.getSelector().set_max_absEta(4.7);
  RecoJetCollectionSelectorBtagLoose jetSelectorAK4_bTagLoose(era, -1, isDEBUG);
  RecoJetCollectionSelectorBtagMedium jetSelectorAK4_bTagMedium(era, -1, isDEBUG);

  RecoJetReaderAK8* jetReaderAK8 = new RecoJetReaderAK8(era, branchName_jets_ak8, branchName_subjets_ak8); 
  // TO-DO: implement jet energy scale uncertainties, b-tag weights,  
  //        and jet  pT and (softdrop) mass corrections described in Section 3.4.3 of AN-2018/058 (v4)
  inputTree->registerReader(jetReaderAK8);
  RecoJetBaseCollectionGenMatcher subjetGenMatcherAK8;
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR08(0.8, isDEBUG);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR12(1.2, isDEBUG);
  RecoJetCollectionSelectorAK8_bbWW_Hbb jetSelectorAK8_Hbb(era, -1, isDEBUG);

//--- declare missing transverse energy
  RecoMEtReader* metReader = new RecoMEtReader(era, isMC, branchName_met);
  inputTree->registerReader(metReader);

  MEtFilter metFilters;
  MEtFilterReader* metFilterReader = new MEtFilterReader(&metFilters, era);
  inputTree->registerReader(metFilterReader);

//--- declare generator level information
  GenLeptonReader* genLeptonReader = nullptr;
  if ( branchName_genLeptons != "" ) {
    genLeptonReader = new GenLeptonReader(branchName_genLeptons);
    inputTree->registerReader(genLeptonReader);
  }
  GenParticleReader* genNeutrinoReader = nullptr;
  if ( branchName_genNeutrinos != "" ) {
    genNeutrinoReader = new GenParticleReader(branchName_genNeutrinos);
    inputTree->registerReader(genNeutrinoReader);
  }
  GenJetReader* genJetReader = nullptr;
  if ( branchName_genJets != "" ) {
    genJetReader = new GenJetReader(branchName_genJets);
    inputTree->registerReader(genJetReader);
  }
  LHEInfoReader* lheInfoReader = new LHEInfoReader(hasLHE);
  inputTree->registerReader(lheInfoReader);
  
  // information specific to HH signal
  GenParticleReader* genParticleFromHiggsReader = nullptr;
  if ( branchName_genParticlesFromHiggs != "" ) {
    genParticleFromHiggsReader = new GenParticleReader(branchName_genParticlesFromHiggs);
    inputTree->registerReader(genParticleFromHiggsReader);
  }

  // information specific to ttbar background
  GenLeptonReader* genLeptonFromTopReader = nullptr;
  if ( branchName_genLeptonsFromTop != "" ) {
    genLeptonFromTopReader = new GenLeptonReader(branchName_genLeptonsFromTop);
    inputTree->registerReader(genLeptonFromTopReader);
  }
  GenParticleReader* genNeutrinoFromTopReader = nullptr;
  if ( branchName_genNeutrinosFromTop != "" ) {
    genNeutrinoFromTopReader = new GenParticleReader(branchName_genNeutrinosFromTop);
    inputTree->registerReader(genNeutrinoFromTopReader);
  }
  GenParticleReader* genBQuarksFromTopReader = nullptr;
  if ( branchName_genBQuarksFromTop != "" ) {
    genBQuarksFromTopReader = new GenParticleReader(branchName_genBQuarksFromTop);
    inputTree->registerReader(genBQuarksFromTopReader);
  }

//--- open output file containing run:lumi:event numbers of events passing final event selection criteria
  std::ostream* selEventsFile = ( selEventsFileName_output != "" ) ? new std::ofstream(selEventsFileName_output.data(), std::ios::out) : 0;
  std::cout << "selEventsFileName_output = " << selEventsFileName_output << std::endl;

//--- declare histograms
  GenEvtHistManager* genEvtHistManager_beforeCuts = nullptr;
  LHEInfoHistManager* lheInfoHistManager_beforeCuts = nullptr;
  if ( isMC ) {
    genEvtHistManager_beforeCuts = new GenEvtHistManager(makeHistManager_cfg(process_string,
      Form("%s/unbiased/genEvt", histogramDir.data()), era_string, central_or_shift));
    genEvtHistManager_beforeCuts->bookHistograms(fs);
    lheInfoHistManager_beforeCuts = new LHEInfoHistManager(makeHistManager_cfg(process_string,
      Form("%s/unbiased/lheInfo", histogramDir.data()), era_string, central_or_shift));
    lheInfoHistManager_beforeCuts->bookHistograms(fs);
  }

  std::string xmlFileName_bb2l = "hhAnalysis/bbww/data/bb2l_HH_XGB_noTopness_evtLevelSUM_HH_bb2l_res_15Var_test.xml";
  std::string xgbFileName_bb2l = "hhAnalysis/bbww/data/bb2l_HH_XGB_noTopness_evtLevelSUM_HH_bb2l_res_15Var.pkl";
  std::string xgbFileNamenohiggnessnotopness_bb2l = "hhAnalysis/bbww/data/bb2l_HH_XGB_noTopness_evtLevelSUM_HH_bb2l_res_13Var_nohiggnessnotopness.pkl";

  std::vector<std::string> xgbInputVariables_bb2l = 
    {"m_ll", "m_Hbb", "nBJetMedium", "m_Hww", "logTopness_fixedChi2", "logHiggsness_fixedChi2", "mT2_top_3particle", "pT_HH", "dPhi_HH", "min_dPhi_lepMEt", "max_dR_b_lep", "met", 
     "max_lep_pt", "max_bjet_pt", "gen_mHH"
  };

  std::vector<std::string> xgbInputVariablesnohiggnessnotopness_bb2l =
    {"m_ll", "m_Hbb", "nBJetMedium", "m_Hww", "mT2_top_3particle", "pT_HH", "dPhi_HH", "min_dPhi_lepMEt", "max_dR_b_lep", "met",
     "max_lep_pt", "max_bjet_pt", "gen_mHH"
    };

  XGBInterface mva_xgb_bb2l(xgbFileName_bb2l, xgbInputVariables_bb2l);
  XGBInterface mva_xgbnohiggnessnotopness_bb2l(xgbFileNamenohiggnessnotopness_bb2l, xgbInputVariablesnohiggnessnotopness_bb2l);
  std::map<std::string, double> mvaInputs_XGB;
  std::map<std::string, double> mvaInputsnohiggnessnotopness_XGB;
  TMVAInterface * mva_xml_bb2l;
  mva_xml_bb2l = new TMVAInterface(xmlFileName_bb2l, xgbInputVariables_bb2l);
  mva_xml_bb2l->enableBDTTransform();

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
    EvtHistManager_hh_bb2l* evt_;
    GenEvtHistManager* genEvtHistManager_afterCuts_;
    LHEInfoHistManager* lheInfoHistManager_afterCuts_;
    WeightHistManager* weights_;
  };
  selHistManagerType* selHistManager = new selHistManagerType();
  selHistManager->electrons_ = new ElectronHistManager(makeHistManager_cfg(process_string,
    Form("%s/sel/electrons", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
  selHistManager->electrons_->bookHistograms(fs);
  selHistManager->leadElectron_ = new ElectronHistManager(makeHistManager_cfg(process_string,
    Form("%s/sel/leadElectron", histogramDir.data()), era_string, central_or_shift, "minimalHistograms", 0));
  selHistManager->leadElectron_->bookHistograms(fs);
  selHistManager->subleadElectron_ = new ElectronHistManager(makeHistManager_cfg(process_string,
    Form("%s/sel/subleadElectron", histogramDir.data()), era_string, central_or_shift, "minimalHistograms", 1));
  selHistManager->subleadElectron_->bookHistograms(fs);
  selHistManager->muons_ = new MuonHistManager(makeHistManager_cfg(process_string,
    Form("%s/sel/muons", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
  selHistManager->muons_->bookHistograms(fs);
  selHistManager->leadMuon_ = new MuonHistManager(makeHistManager_cfg(process_string,
    Form("%s/sel/leadMuon", histogramDir.data()), era_string, central_or_shift, "minimalHistograms", 0));
  selHistManager->leadMuon_->bookHistograms(fs);
  selHistManager->subleadMuon_ = new MuonHistManager(makeHistManager_cfg(process_string,
    Form("%s/sel/subleadMuon", histogramDir.data()), era_string, central_or_shift, "minimalHistograms", 1));
  selHistManager->subleadMuon_->bookHistograms(fs);
  selHistManager->jetsAK4_ = new JetHistManager(makeHistManager_cfg(process_string,
    Form("%s/sel/jetsAK4", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
  selHistManager->jetsAK4_->bookHistograms(fs);
  selHistManager->leadJetAK4_ = new JetHistManager(makeHistManager_cfg(process_string,
    Form("%s/sel/leadJetAK4", histogramDir.data()), era_string, central_or_shift, "minimalHistograms", 0));
  selHistManager->leadJetAK4_->bookHistograms(fs);
  selHistManager->subleadJetAK4_ = new JetHistManager(makeHistManager_cfg(process_string,
    Form("%s/sel/subleadJetAK4", histogramDir.data()), era_string, central_or_shift, "minimalHistograms", 1));
  selHistManager->subleadJetAK4_->bookHistograms(fs);
  selHistManager->jetsAK8_Hbb_ = new JetHistManagerAK8(makeHistManager_cfg(process_string,
    Form("%s/sel/jetsAK8_Hbb", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
  selHistManager->jetsAK8_Hbb_->bookHistograms(fs);
  selHistManager->BJetsAK4_loose_ = new JetHistManager(makeHistManager_cfg(process_string,
    Form("%s/sel/BJetsAK4_loose", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
  selHistManager->BJetsAK4_loose_->bookHistograms(fs);
  selHistManager->leadBJetAK4_loose_ = new JetHistManager(makeHistManager_cfg(process_string,
    Form("%s/sel/leadBJetAK4_loose", histogramDir.data()), era_string, central_or_shift, "minimalHistograms", 0));
  selHistManager->leadBJetAK4_loose_->bookHistograms(fs);
  selHistManager->subleadBJetAK4_loose_ = new JetHistManager(makeHistManager_cfg(process_string,
    Form("%s/sel/subleadBJetAK4_loose", histogramDir.data()), era_string, central_or_shift, "minimalHistograms", 1));
  selHistManager->subleadBJetAK4_loose_->bookHistograms(fs);
  selHistManager->BJetsAK4_medium_ = new JetHistManager(makeHistManager_cfg(process_string,
    Form("%s/sel/BJetsAK4_medium", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
  selHistManager->BJetsAK4_medium_->bookHistograms(fs);
  selHistManager->met_ = new MEtHistManager(makeHistManager_cfg(process_string,
    Form("%s/sel/met", histogramDir.data()), era_string, central_or_shift));
  selHistManager->met_->bookHistograms(fs);
  selHistManager->metFilters_ = new MEtFilterHistManager(makeHistManager_cfg(process_string,
    Form("%s/sel/metFilters", histogramDir.data()), era_string, central_or_shift));
  selHistManager->metFilters_->bookHistograms(fs);
  selHistManager->evt_ = new EvtHistManager_hh_bb2l(makeHistManager_cfg(process_string,
    Form("%s/sel/evt", histogramDir.data()), era_string, central_or_shift, "memEnabled"));
  selHistManager->evt_->bookHistograms(fs);
  selHistManager->genEvtHistManager_afterCuts_ = new GenEvtHistManager(makeHistManager_cfg(process_string,
    Form("%s/sel/genEvt", histogramDir.data()), era_string, central_or_shift));
  selHistManager->genEvtHistManager_afterCuts_->bookHistograms(fs);
  selHistManager->lheInfoHistManager_afterCuts_ = new LHEInfoHistManager(makeHistManager_cfg(process_string,
    Form("%s/sel/lheInfo", histogramDir.data()), era_string, central_or_shift));
  selHistManager->lheInfoHistManager_afterCuts_->bookHistograms(fs);
  selHistManager->weights_ = new WeightHistManager(makeHistManager_cfg(process_string,
    Form("%s/sel/weights", histogramDir.data()), era_string, central_or_shift));
  selHistManager->weights_->bookHistograms(fs, { "genWeight", "pileupWeight", "triggerWeight", "data_to_MC_correction" });

  TH1* histogram_badMEM_genLepton_lead_matchType           = bookHistogram1d(fs, "badMEM_genLepton_lead_matchType",             6,   -0.5,  +5.5);
  TH1* histogram_badMEM_genLepton_sublead_matchType        = bookHistogram1d(fs, "badMEM_genLepton_sublead_matchType",          6,   -0.5,  +5.5);
  TH1* histogram_badMEM_genJet_Hbb_lead_matchType          = bookHistogram1d(fs, "badMEM_genJet_Hbb_lead_matchType",            6,   -0.5,  +5.5);
  TH1* histogram_badMEM_genJet_Hbb_sublead_matchType       = bookHistogram1d(fs, "badMEM_genJet_Hbb_sublead_matchType",         6,   -0.5,  +5.5);
  TH1* histogram_badMEM_numBJets_loose                     = bookHistogram1d(fs, "badMEM_numBJets_loose",                      10,   -0.5,  +9.5);
  TH1* histogram_badMEM_numBJets_medium                    = bookHistogram1d(fs, "badMEM_numBJets_medium",                     10,   -0.5,  +9.5);
  TH1* histogram_badMEM_log_memProb_signal                 = bookHistogram1d(fs, "badMEM_log_memProb_signal",                 200, -200.,    0.);
  TH1* histogram_badMEM_log_memProb_signal_missingBJet     = bookHistogram1d(fs, "badMEM_log_memProb_signal_missingBJet",     200, -200.,    0.);
  TH1* histogram_badMEM_log_memProb_background             = bookHistogram1d(fs, "badMEM_log_memProb_background",             200, -200.,    0.);
  TH1* histogram_badMEM_log_memProb_background_missingBJet = bookHistogram1d(fs, "badMEM_log_memProb_background_missingBJet", 200, -200.,    0.);
  TH1* histogram_badMEM_memLR_missingBJet                  = bookHistogram1d(fs, "badMEM_memLR_missingBJet",                  360,    0.,    1.);

  TH1* histogram_numGenMatchedBJets_higherCSV              = bookHistogram1d(fs, "numGenMatchedBJets_higherCSV",               10,   -0.5,  +9.5);
  TH1* histogram_numGenMatchedBJets_minDeltaMass1Lor1M     = bookHistogram1d(fs, "numGenMatchedBJets_minDeltaMass1Lor1M",      10,   -0.5,  +9.5);
  TH1* histogram_numGenMatchedBJets_minDeltaMass2Lor1M     = bookHistogram1d(fs, "numGenMatchedBJets_minDeltaMass2Lor1M",      10,   -0.5,  +9.5);

  TH1* histogram_deltaMEtPx                                = bookHistogram1d(fs, "deltaMEtPx",                                400, -100., +100.);
  TH1* histogram_deltaMEtPy                                = bookHistogram1d(fs, "deltaMEtPy",                                400, -100., +100.);

  int analyzedEntries = 0;
  int selectedEntries = 0;
  double selectedEntries_weighted = 0.;
  TH1* histogram_analyzedEntries = fs.make<TH1D>("analyzedEntries", "analyzedEntries", 1, -0.5, +0.5);
  TH1* histogram_selectedEntries = fs.make<TH1D>("selectedEntries", "selectedEntries", 1, -0.5, +0.5);
  cutFlowTableType cutFlowTable;
  const edm::ParameterSet cutFlowTableCfg = makeHistManager_cfg(
    process_string, Form("%s/sel/cutFlow", histogramDir.data()), era_string, central_or_shift
  );
  const std::vector<std::string> cuts = {
    "run:ls:event selection",
    "trigger",
    ">= 2 presel leptons",
    ">= 2 sel leptons",
    "lead lepton pT > 25 GeV && sublead lepton pT > 15 GeV",
    Form("sel lepton-pair %s charge", leptonChargeSelection_string.data()),
    "<= 2 tight leptons",
    "fakeable lepton trigger match",
    "HLT filter matching",
    ">= 2 jets from H->bb",
    ">= 1 medium b-jet",
    "m(ll) < 76 GeV",
    "m(ll) > 12 GeV",
    "Z-boson mass veto",
    "MEt filters",
    "signal region veto"
  };
  CutFlowTableHistManager * cutFlowHistManager = new CutFlowTableHistManager(cutFlowTableCfg, cuts);
  cutFlowHistManager->bookHistograms(fs);
  while ( inputTree->hasNextEvent() && (! run_lumi_eventSelector || (run_lumi_eventSelector && ! run_lumi_eventSelector -> areWeDone())) && selectedEntries < maxSelEvents ) {
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
    cutFlowTable.update("run:ls:event selection");
    cutFlowHistManager->fillHistograms("run:ls:event selection", lumiScale);

    if ( run_lumi_eventSelector ) {
      std::cout << "processing Entry #" << inputTree->getCumulativeMaxEventCount() << ": " << eventInfo << std::endl;
      if ( inputTree -> isOpen() ) {
        std::cout << "input File = " << inputTree->getCurrentFileName() << std::endl;
      }
    }

//--- build collections of generator level particles (before any cuts are applied, to check distributions in unbiased event samples)
    std::vector<GenLepton> genLeptons;
    std::vector<GenLepton> genElectrons;
    std::vector<GenLepton> genMuons;
    if ( genLeptonReader ) {
      genLeptons = genLeptonReader->read();
      for ( std::vector<GenLepton>::const_iterator genLepton = genLeptons.begin();
	    genLepton != genLeptons.end(); ++genLepton ) {
	int abs_pdgId = std::abs(genLepton->pdgId());
	if      ( abs_pdgId == 11 ) genElectrons.push_back(*genLepton);
	else if ( abs_pdgId == 13 ) genMuons.push_back(*genLepton);
      }
    }
    std::vector<GenParticle> genNeutrinos;
    if ( genNeutrinoReader ) {
      genNeutrinos = genNeutrinoReader->read();
    }
    std::vector<GenJet> genJets;
    if ( genJetReader ) {
      genJets = genJetReader->read();
    }
    if ( isDEBUG ) {
      printCollection("genLeptons", genLeptons);
      printCollection("genNeutrinos", genNeutrinos);
      printCollection("genJets", genJets);
    }

    double evtWeight_inclusive = 1.;
    if ( isMC ) {
      if ( apply_genWeight       ) evtWeight_inclusive *= boost::math::sign(eventInfo.genWeight);
      if ( isMC_tH               ) evtWeight_inclusive *= eventInfo.genWeight_tH;
      lheInfoReader->read();
      evtWeight_inclusive *= lheInfoReader->getWeight_scale(kLHE_scale_central);
      evtWeight_inclusive *= eventInfo.pileupWeight;
      genEvtHistManager_beforeCuts->fillHistograms(genElectrons, genMuons, {}, {}, genJets, evtWeight_inclusive);
    }

    std::vector<GenParticle> genParticlesFromHiggs;
    if ( isSignal ) {
      genParticlesFromHiggs = genParticleFromHiggsReader->read();
      if ( isDEBUG ) {
	printCollection("genParticlesFromHiggs", genParticlesFromHiggs);
      }
      if ( !(genParticlesFromHiggs.size() == 4) ) {
	if ( run_lumi_eventSelector ) {
	  std::cout << "event " << eventInfo.str() << " FAILS generator-level selection." << std::endl;
	  std::cout << "#genParticlesFromHiggs = " << genParticlesFromHiggs.size() << std::endl;
	}
	continue;
      }
    } 
    std::vector<GenLepton> genLeptonsFromTop;
    std::vector<GenParticle> genNeutrinosFromTop;
    std::vector<GenParticle> genBQuarksFromTop;
    if ( !isSignal ) {
      genLeptonsFromTop = genLeptonFromTopReader->read();
      genNeutrinosFromTop = genNeutrinoFromTopReader->read();
      genBQuarksFromTop = genBQuarksFromTopReader->read();
      if ( isDEBUG ) {
	printCollection("genLeptonsFromTop", genLeptonsFromTop);
	printCollection("genNeutrinosFromTop", genNeutrinosFromTop);
	printCollection("genBQuarksFromTop", genBQuarksFromTop);	
      }
      if ( !(genLeptonsFromTop.size() == 2 && genNeutrinosFromTop.size() == 2 && genBQuarksFromTop.size() == 2) ) {
	if ( run_lumi_eventSelector ) {
	  std::cout << "event " << eventInfo.str() << " FAILS generator-level selection." << std::endl;
	  std::cout << "#genLeptonsFromTop = " << genLeptonsFromTop.size() << std::endl;
	  std::cout << "#genNeutrinosFromTop = " << genNeutrinosFromTop.size() << std::endl;
	  std::cout << "#genBQuarksFromTop = " << genBQuarksFromTop.size() << std::endl;
	}
	continue;
      }
    }
    cutFlowTable.update("generator-level selection (1)", evtWeight_inclusive);

    bool isTriggered_1e = hltPaths_isTriggered(triggers_1e);
    bool isTriggered_2e = hltPaths_isTriggered(triggers_2e);
    bool isTriggered_1mu = hltPaths_isTriggered(triggers_1mu);
    bool isTriggered_2mu = hltPaths_isTriggered(triggers_2mu);
    bool isTriggered_1e1mu = hltPaths_isTriggered(triggers_1e1mu);

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

//--- rank triggers by priority and ignore triggers of lower priority if a trigger of higher priority has fired for given event;
//    the ranking of the triggers is as follows: 2mu, 1e1mu, 2e, 1mu, 1e
// CV: this logic is necessary to avoid that the same event is selected multiple times when processing different primary datasets
    if ( !isMC && !isDEBUG ) {
      if ( selTrigger_1e && (isTriggered_2e || isTriggered_1mu || isTriggered_2mu || isTriggered_1e1mu) ) {
        if ( run_lumi_eventSelector ) {
	  std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
          std::cout << " (selTrigger_1e = " << selTrigger_1e
                    << ", isTriggered_2e = " << isTriggered_2e
                    << ", isTriggered_1mu = " << isTriggered_1mu
                    << ", isTriggered_2mu = " << isTriggered_2mu
                    << ", isTriggered_1e1mu = " << isTriggered_1e1mu << ")" << std::endl;
        }
        continue;
      }
      if ( selTrigger_2e && (isTriggered_2mu || isTriggered_1e1mu) ) {
        if ( run_lumi_eventSelector ) {
	  std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
          std::cout << " (selTrigger_2e = " << selTrigger_2e
                    << ", isTriggered_2mu = " << isTriggered_2mu
                    << ", isTriggered_1e1mu = " << isTriggered_1e1mu << ")" << std::endl;
        }
        continue;
      }
      if ( selTrigger_1mu && (isTriggered_2e || isTriggered_2mu || isTriggered_1e1mu) ) {
        if ( run_lumi_eventSelector ) {
	  std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
          std::cout << " (selTrigger_1mu = " << selTrigger_1mu
                    << ", isTriggered_2e = " << isTriggered_2e
                    << ", isTriggered_2mu = " << isTriggered_2mu
                    << ", isTriggered_1e1mu = " << isTriggered_1e1mu << ")" << std::endl;
        }
        continue;
      }
      if ( selTrigger_1e1mu && isTriggered_2mu ) {
        if ( run_lumi_eventSelector ) {
	  std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
          std::cout << " (selTrigger_1e1mu = " << selTrigger_1e1mu
                    << ", isTriggered_2mu = " << isTriggered_2mu << ")" << std::endl;
        }
        continue;
      }
    }
    cutFlowTable.update("trigger", evtWeight_inclusive);
    cutFlowHistManager->fillHistograms("trigger", evtWeight_inclusive);

    if ( (selTrigger_2e    && !apply_offline_e_trigger_cuts_2e)    ||
         (selTrigger_1e1mu && !apply_offline_e_trigger_cuts_1e1mu) ||
         (selTrigger_1e    && !apply_offline_e_trigger_cuts_1e)    ||
         (selTrigger_1mu   && !apply_offline_e_trigger_cuts_1mu)   ||
         (selTrigger_2mu   && !apply_offline_e_trigger_cuts_2mu)  ) {
      fakeableElectronSelector.disable_offline_e_trigger_cuts();
      tightElectronSelector.disable_offline_e_trigger_cuts();
    } else {
      tightElectronSelector.enable_offline_e_trigger_cuts();
      fakeableElectronSelector.enable_offline_e_trigger_cuts();
    }

//--- build collections of electrons, muons and hadronic taus;
//    resolve overlaps in order of priority: muon, electron,
    std::vector<RecoMuon> muons = muonReader->read();
    std::vector<const RecoMuon*> muon_ptrs = convert_to_ptrs(muons);
    std::vector<const RecoMuon*> cleanedMuons = muon_ptrs; // CV: no cleaning needed for muons, as they have the highest priority in the overlap removal
    std::vector<const RecoMuon*> preselMuons = preselMuonSelector(cleanedMuons, isHigherConePt);
    std::vector<const RecoMuon*> fakeableMuons = fakeableMuonSelector(preselMuons, isHigherConePt);
    std::vector<const RecoMuon*> tightMuons = tightMuonSelector(fakeableMuons, isHigherConePt);
    if ( isDEBUG || run_lumi_eventSelector ) {
      printCollection("preselMuons",   preselMuons);
      printCollection("fakeableMuons", fakeableMuons);
      printCollection("tightMuons",    tightMuons);
    }

    std::vector<RecoElectron> electrons = electronReader->read();
    std::vector<const RecoElectron*> electron_ptrs = convert_to_ptrs(electrons);
    std::vector<const RecoElectron*> cleanedElectrons = electronCleaner(electron_ptrs, preselMuons);
    std::vector<const RecoElectron*> preselElectrons = preselElectronSelector(cleanedElectrons, isHigherConePt);
    std::vector<const RecoElectron*> fakeableElectrons = fakeableElectronSelector(preselElectrons, isHigherConePt);
    std::vector<const RecoElectron*> tightElectrons = tightElectronSelector(fakeableElectrons, isHigherConePt);
    if ( isDEBUG || run_lumi_eventSelector ) {
      printCollection("preselElectrons",   preselElectrons);
      printCollection("fakeableElectrons", fakeableElectrons);
      printCollection("tightElectrons",    tightElectrons);
    }

    std::vector<const RecoLepton*> preselLeptonsFull = mergeLeptonCollections(preselElectrons, preselMuons, isHigherConePt);
    std::vector<const RecoLepton*> fakeableLeptonsFull = mergeLeptonCollections(fakeableElectrons, fakeableMuons, isHigherConePt);
    std::vector<const RecoLepton*> tightLeptonsFull = mergeLeptonCollections(tightElectrons, tightMuons, isHigherConePt);

    std::vector<const RecoLepton*> preselLeptons = pickFirstNobjects(preselLeptonsFull, 2);
    std::vector<const RecoLepton*> fakeableLeptons = pickFirstNobjects(fakeableLeptonsFull, 2);
    std::vector<const RecoLepton*> tightLeptons = getIntersection(fakeableLeptons, tightLeptonsFull, isHigherConePt);

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
      std::vector<const RecoLepton*> selLeptons_full = mergeLeptonCollections(selElectrons, selMuons, isHigherConePt);
      selLeptons = getIntersection(fakeableLeptons, selLeptons_full, isHigherConePt);
    }

    if ( isDEBUG || run_lumi_eventSelector ) {
      printCollection("selMuons", selMuons);
      printCollection("selElectrons", selElectrons);
      printCollection("selLeptons", selLeptons);
    }

//--- build collections of jets and select subset of jets passing b-tagging criteria
    std::vector<RecoJet> jets_ak4 = jetReaderAK4->read();
    std::vector<const RecoJet*> jet_ptrs_ak4 = convert_to_ptrs(jets_ak4);
    std::vector<const RecoJet*> cleanedJetsAK4_wrtLeptons = jetCleanerAK4_dR04(jet_ptrs_ak4, fakeableLeptons);
    std::vector<const RecoJet*> selJetsAK4 = jetSelectorAK4(cleanedJetsAK4_wrtLeptons, isHigherPt);
    std::vector<const RecoJet*> selBJetsAK4_loose = jetSelectorAK4_bTagLoose(cleanedJetsAK4_wrtLeptons, isHigherPt);
    std::vector<const RecoJet*> selBJetsAK4_medium = jetSelectorAK4_bTagMedium(cleanedJetsAK4_wrtLeptons, isHigherPt);

    if ( isDEBUG || run_lumi_eventSelector ) {
      printCollection("uncleaned AK4 jets", jet_ptrs_ak4);
      printCollection("cleaned AK4 jets(wrtLeptons)", cleanedJetsAK4_wrtLeptons);
      printCollection("selected AK4 jets", selJetsAK4);
    }

//--- match reconstructed to generator level particles
    std::vector<GenLepton> genLeptonsForMatching;
    std::vector<GenJet> genBJetsForMatching;
    double genMEtPx = 0.;
    double genMEtPy = 0.;
    if ( isSignal ) {
      const GenParticle* genBQuark      = nullptr;
      const GenParticle* genAntiBQuark  = nullptr;
      const GenParticle* genWBosonPlus  = nullptr;
      const GenParticle* genWBosonMinus = nullptr;
      for ( std::vector<GenParticle>::const_iterator genParticle = genParticlesFromHiggs.begin();
	    genParticle != genParticlesFromHiggs.end(); ++genParticle ) {
	if      ( genParticle->pdgId() ==  +5 ) genBQuark      = &(*genParticle);
	else if ( genParticle->pdgId() ==  -5 ) genAntiBQuark  = &(*genParticle);
	else if ( genParticle->pdgId() == +24 ) genWBosonPlus  = &(*genParticle);
	else if ( genParticle->pdgId() == -24 ) genWBosonMinus = &(*genParticle);
      }
      if ( genBQuark && genAntiBQuark ) {
	genBJetsForMatching.push_back(GenJet(
          genBQuark->pt(), genBQuark->eta(), genBQuark->phi(), mem::bottomQuarkMass, genBQuark->pdgId()));
	genBJetsForMatching.push_back(GenJet(
          genAntiBQuark->pt(), genAntiBQuark->eta(), genAntiBQuark->phi(), mem::bottomQuarkMass, genAntiBQuark->pdgId()));	
      }
      if ( genWBosonPlus && genWBosonMinus ) {
	std::pair<const GenLepton*, const GenParticle*> genLepton_and_NeutrinoFromWBosonPlus =
          findGenLepton_and_NeutrinoFromWBoson(genWBosonPlus, genLeptons, genNeutrinos);
	const GenLepton* genLeptonPlus = genLepton_and_NeutrinoFromWBosonPlus.first;
	const GenParticle* genNeutrino = genLepton_and_NeutrinoFromWBosonPlus.second;
	std::pair<const GenLepton*, const GenParticle*> genLepton_and_NeutrinoFromWBosonMinus =
          findGenLepton_and_NeutrinoFromWBoson(genWBosonMinus, genLeptons, genNeutrinos);
	const GenLepton* genLeptonMinus = genLepton_and_NeutrinoFromWBosonMinus.first;
	const GenParticle* genAntiNeutrino = genLepton_and_NeutrinoFromWBosonMinus.second;
	if ( !(genLeptonPlus && genNeutrino && genLeptonMinus && genAntiNeutrino) ) continue;
	genLeptonsForMatching.push_back(*genLeptonPlus);
	genLeptonsForMatching.push_back(*genLeptonMinus);
	genMEtPx = genNeutrino->p4().px() + genAntiNeutrino->p4().px();
	genMEtPy = genNeutrino->p4().py() + genAntiNeutrino->p4().py();
      }
    } else {
      genLeptonsForMatching = genLeptonsFromTop;
      assert(genNeutrinosFromTop.size() == 2);
      genMEtPx = genNeutrinosFromTop[0].p4().px() + genNeutrinosFromTop[1].p4().px();
      genMEtPy = genNeutrinosFromTop[0].p4().py() + genNeutrinosFromTop[1].p4().py();
      for ( std::vector<GenParticle>::const_iterator genBQuark = genBQuarksFromTop.begin();
	    genBQuark != genBQuarksFromTop.end(); ++genBQuark ) {
	genBJetsForMatching.push_back(GenJet(
          genBQuark->pt(), genBQuark->eta(), genBQuark->phi(), mem::bottomQuarkMass, genBQuark->pdgId()));
      }
    }
    std::sort(genLeptonsForMatching.begin(), genLeptonsForMatching.end(), isHigherPt_GenLepton);
    std::sort(genBJetsForMatching.begin(), genBJetsForMatching.end(), isHigherPt_GenJet);
    if ( !(genLeptonsForMatching.size() == 2 && genBJetsForMatching.size() == 2) ) {
      if ( run_lumi_eventSelector ) {
	std::cout << "event " << eventInfo.str() << " FAILS generator-level selection." << std::endl;
	std::cout << "#genLeptonsForMatching = " << genLeptonsForMatching.size() << std::endl;
	std::cout << "#genBJetsForMatching = " << genBJetsForMatching.size() << std::endl;
      }
      continue;
    }
    cutFlowTable.update("generator-level selection (2)", evtWeight_inclusive);
    muonGenMatcher.addGenLeptonMatch(preselMuons, genLeptonsForMatching, 0.2);
    electronGenMatcher.addGenLeptonMatch(preselElectrons, genLeptonsForMatching, 0.2);

    // require at least two leptons passing loose preselection criteria
    if ( !(preselLeptonsFull.size() >= 2) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS preselLeptons selection." << std::endl;
        printCollection("preselLeptons", preselLeptonsFull);
      }
      continue;
    }
    cutFlowTable.update(">= 2 presel leptons", evtWeight_inclusive);
    cutFlowHistManager->fillHistograms(">= 2 presel leptons", evtWeight_inclusive);

    // require at least two leptons passing tight selection criteria of final event selection
    if ( !(selLeptons.size() >= 2) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS selLeptons selection." << std::endl;
        printCollection("selLeptons", selLeptons);
      }
      continue;
    }
    cutFlowTable.update(">= 2 sel leptons", evtWeight_inclusive);
    cutFlowHistManager->fillHistograms(">= 2 sel leptons", evtWeight_inclusive);
    const RecoLepton* selLepton_lead = selLeptons[0];
    const Particle::LorentzVector& selLeptonP4_lead = selLepton_lead->p4();
    int selLepton_lead_type = getLeptonType(selLepton_lead->pdgId());
    const RecoLepton* selLepton_sublead = selLeptons[1];
    const Particle::LorentzVector& selLeptonP4_sublead = selLepton_sublead->p4();
    int selLepton_sublead_type = getLeptonType(selLepton_sublead->pdgId());

    lheInfoReader->read();
    
//--- compute event-level weight for data/MC correction of b-tagging efficiency and mistag rate
//   (using the method "Event reweighting using scale factors calculated with a tag and probe method",
//    described on the BTV POG twiki https://twiki.cern.ch/twiki/bin/view/CMS/BTagShapeCalibration )
    double evtWeight = evtWeight_inclusive;    
    double btagWeight = get_BtagWeight(selJetsAK4);
    evtWeight *= btagWeight;
    if ( isDEBUG ) {
      if ( apply_genWeight ) std::cout << "genWeight = " << boost::math::sign(eventInfo.genWeight) << std::endl;
      std::cout << "pileupWeight = " << eventInfo.pileupWeight << std::endl;
      std::cout << "btagWeight = " << btagWeight << std::endl;
    }
  
    double minPt_lead = -1.;
    if      ( era == kEra_2016 ) minPt_lead = 25.;
    else if ( era == kEra_2017 ) minPt_lead = 25.;
    else assert(0);
    double minPt_sublead = 15.;
    if ( !(selLepton_lead->cone_pt() > minPt_lead && selLepton_sublead->cone_pt() > minPt_sublead) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS lepton pT selection." << std::endl;
        std::cout << " (leading selLepton pT = " << selLepton_lead->pt() << ", minPt_lead = " << minPt_lead
                  << ", subleading selLepton pT = " << selLepton_sublead->pt() << ", minPt_sublead = " << minPt_sublead << ")" << std::endl;
      }
      continue;
    }
    cutFlowTable.update("lead lepton pT > 25 GeV && sublead lepton pT > 15 GeV", evtWeight);
    cutFlowHistManager->fillHistograms("lead lepton pT > 25 GeV && sublead lepton pT > 15 GeV", evtWeight);

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
      cutFlowTable.update(Form("sel lepton-pair %s charge", leptonChargeSelection_string.data()), evtWeight);
    }
    cutFlowHistManager->fillHistograms("sel lepton-pair OS/SS charge", evtWeight);

    // require exactly two leptons passing tight selection criteria, to avoid overlap with other channels
    if ( !(tightLeptonsFull.size() <= 2) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS tightLeptons selection." << std::endl;
        printCollection("tightLeptonsFull", tightLeptonsFull);
      }
      continue;
    }
    cutFlowTable.update("<= 2 tight leptons", evtWeight);
    cutFlowHistManager->fillHistograms("<= 2 tight leptons", evtWeight);

    // require that trigger paths match event category (with event category based on fakeableLeptons)
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
    cutFlowTable.update("fakeable lepton trigger match", evtWeight);
    cutFlowHistManager->fillHistograms("fakeable lepton trigger match", evtWeight);

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
    cutFlowTable.update("HLT filter matching", evtWeight);
    cutFlowHistManager->fillHistograms("HLT filter matching", evtWeight);

    double weight_data_to_MC_correction = 1.;
    double triggerWeight = 1.;
    double leptonSF_weight = 1.;
    dataToMCcorrectionInterface->setLeptons(
      selLepton_lead_type, selLepton_lead->pt(), selLepton_lead->eta(),
      selLepton_sublead_type, selLepton_sublead->pt(), selLepton_sublead->eta());

//--- apply data/MC corrections for trigger efficiency
    double sf_triggerEff = dataToMCcorrectionInterface->getSF_leptonTriggerEff();
    if ( isDEBUG ) {
      std::cout << "sf_triggerEff = " << sf_triggerEff << std::endl;
    }
    triggerWeight *= sf_triggerEff;
    weight_data_to_MC_correction *= sf_triggerEff;

//--- apply data/MC corrections for efficiencies for lepton to pass loose identification and isolation criteria
    leptonSF_weight *= dataToMCcorrectionInterface->getSF_leptonID_and_Iso_loose();

//--- apply data/MC corrections for efficiencies of leptons passing the loose identification and isolation criteria
//    to also pass the tight identification and isolation criteria
    if ( electronSelection == kFakeable && muonSelection == kFakeable ) {
      leptonSF_weight *= dataToMCcorrectionInterface->getSF_leptonID_and_Iso_fakeable_to_loose();
    } else if ( electronSelection >= kFakeable && muonSelection >= kFakeable ) {
      // apply loose-to-tight lepton ID SFs if either of the following is true:
      // 1) both electron and muon selections are tight -> corresponds to SR
      // 2) electron selection is relaxed to fakeable and muon selection is kept as tight -> corresponds to MC closure w/ relaxed e selection
      // 3) muon selection is relaxed to fakeable and electron selection is kept as tight -> corresponds to MC closure w/ relaxed mu selection
      // we allow (2) and (3) so that the MC closure regions would more compatible w/ the SR (1) in comparison
      leptonSF_weight *= dataToMCcorrectionInterface->getSF_leptonID_and_Iso_tight_to_loose_wTightCharge();
    }
    weight_data_to_MC_correction *= leptonSF_weight;
    if ( isDEBUG ) {
      std::cout << "weight_data_to_MC_correction = " << weight_data_to_MC_correction << std::endl;
    }
    
    evtWeight *= weight_data_to_MC_correction;
    if ( isDEBUG ) {
      std::cout << "evtWeight = " << evtWeight << std::endl;
    }

    std::vector<RecoJetAK8> jets_ak8 = jetReaderAK8->read();
    std::vector<const RecoJetAK8*> jet_ptrs_ak8 = convert_to_ptrs(jets_ak8);
    
    if ( isDEBUG || run_lumi_eventSelector ) {
      printCollection("uncleaned AK8 jets", jet_ptrs_ak8);
    }

    // select jets from H->bb decay
    std::vector<const RecoJetAK8*> cleanedJetsAK8_wrtLeptons = jetCleanerAK8_dR08(jet_ptrs_ak8, fakeableLeptons);
    std::vector<const RecoJetAK8*> selJetsAK8_Hbb = jetSelectorAK8_Hbb(cleanedJetsAK8_wrtLeptons, isHigherCSV_ak8);
    std::vector<const RecoJet*> selJetsAK4_Hbb = jetSelectorAK4(cleanedJetsAK4_wrtLeptons, isHigherCSV);
    if ( selJetsAK4_Hbb.size() >= 2 ) {
      std::pair<const RecoJet*, const RecoJet*> selBJets_higherCSV(selJetsAK4_Hbb[0], selJetsAK4_Hbb[1]);
      fillWithOverFlow(histogram_numGenMatchedBJets_higherCSV, countGenMatchedBJets(selBJets_higherCSV, genBJetsForMatching, 0.2), evtWeight);
      std::pair<const RecoJet*, const RecoJet*> selBJets_minDeltaMass1Lor1M = selectBJetsFromHbb(selJetsAK4_Hbb,
        jetSelectorAK4_bTagLoose, 1, jetSelectorAK4_bTagMedium, 1);
      fillWithOverFlow(histogram_numGenMatchedBJets_minDeltaMass1Lor1M, countGenMatchedBJets(selBJets_minDeltaMass1Lor1M, genBJetsForMatching, 0.2), evtWeight);
      std::pair<const RecoJet*, const RecoJet*> selBJets_minDeltaMass2Lor1M = selectBJetsFromHbb(selJetsAK4_Hbb,
        jetSelectorAK4_bTagLoose, 2, jetSelectorAK4_bTagMedium, 1);
      fillWithOverFlow(histogram_numGenMatchedBJets_minDeltaMass2Lor1M, countGenMatchedBJets(selBJets_minDeltaMass2Lor1M, genBJetsForMatching, 0.2), evtWeight);
    }
    const RecoJetAK8* selJetAK8_Hbb = nullptr;
    const RecoJetBase* selJet1_Hbb = nullptr;
    const RecoJetBase* selJet2_Hbb = nullptr;
    int numBJets_loose = 0;
    int numBJets_medium = 0;
    if ( selJetsAK8_Hbb.size() >= 1 ) {
      selJetAK8_Hbb = selJetsAK8_Hbb[0];    
      assert(selJetAK8_Hbb->subJet1() && selJetAK8_Hbb->subJet2());
      if ( selJetAK8_Hbb->subJet1()->BtagCSV() > selJetAK8_Hbb->subJet2()->BtagCSV() ) {
	selJet1_Hbb = selJetAK8_Hbb->subJet1();
	selJet2_Hbb = selJetAK8_Hbb->subJet2();
      } else {
	selJet1_Hbb = selJetAK8_Hbb->subJet2();
	selJet2_Hbb = selJetAK8_Hbb->subJet1();
      }
      double min_BtagCSV_loose = jetSelectorAK8_Hbb.getSelector().get_min_BtagCSV_loose();
      if ( selJetAK8_Hbb->subJet1()->BtagCSV() >= min_BtagCSV_loose  ) ++numBJets_loose;
      if ( selJetAK8_Hbb->subJet2()->BtagCSV() >= min_BtagCSV_loose  ) ++numBJets_loose;
      double min_BtagCSV_medium = jetSelectorAK8_Hbb.getSelector().get_min_BtagCSV_medium();
      if ( selJetAK8_Hbb->subJet1()->BtagCSV() >= min_BtagCSV_medium ) ++numBJets_medium;
      if ( selJetAK8_Hbb->subJet2()->BtagCSV() >= min_BtagCSV_medium ) ++numBJets_medium;
    } else if ( selJetsAK4_Hbb.size() >= 2 ) {
      selJet1_Hbb = selJetsAK4_Hbb[0];
      selJet2_Hbb = selJetsAK4_Hbb[1];
      std::vector<const RecoJet*> particles = { selJetsAK4_Hbb[0], selJetsAK4_Hbb[1] };
      numBJets_loose = jetSelectorAK4_bTagLoose(particles, isHigherPt).size();
      numBJets_medium = jetSelectorAK4_bTagMedium(particles, isHigherPt).size();
    }
    if ( !(selJet1_Hbb && selJet2_Hbb) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS >= 2 jets from H->bb selection\n";
      }
      continue;
    }
    cutFlowTable.update(">= 2 jets from H->bb", evtWeight_inclusive);
    cutFlowHistManager->fillHistograms(">= 2 jets from H->bb", evtWeight_inclusive);

    std::vector<const RecoJetBase*> selJets_Hbb = { selJet1_Hbb, selJet2_Hbb };
    std::sort(selJets_Hbb.begin(), selJets_Hbb.end(), isHigherPt);
    subjetGenMatcherAK8.addGenJetMatch(selJets_Hbb, genBJetsForMatching, 0.2);
    const RecoJetBase* selJet_Hbb_lead = selJets_Hbb[0];
    const Particle::LorentzVector& selJetP4_Hbb_lead = selJet_Hbb_lead->p4();
    const RecoJetBase* selJet_Hbb_sublead = selJets_Hbb[1];
    const Particle::LorentzVector& selJetP4_Hbb_sublead = selJet_Hbb_sublead->p4();

    if ( !(numBJets_medium >= 1) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS >= 1 medium b-jet selection\n";
      }
      continue;
    }
    cutFlowTable.update(">= 1 medium b-jet", evtWeight_inclusive);
    cutFlowHistManager->fillHistograms(">= 1 medium b-jet", evtWeight_inclusive);

    if ( !((selLeptonP4_lead + selLeptonP4_sublead).mass() < 76.) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS m_ll < 76 GeV cut." << std::endl;
      }
      continue;
    }
    cutFlowTable.update("m(ll) < 76 GeV", evtWeight);
    cutFlowHistManager->fillHistograms("m(ll) < 76 GeV", evtWeight);

    bool failsLowMassVeto = false;
    for ( std::vector<const RecoLepton*>::const_iterator lepton1 = preselLeptonsFull.begin();
	  lepton1 != preselLeptonsFull.end(); ++lepton1 ) {
      for ( std::vector<const RecoLepton*>::const_iterator lepton2 = lepton1 + 1;
	    lepton2 != preselLeptonsFull.end(); ++lepton2 ) {
        double mass = ((*lepton1)->p4() + (*lepton2)->p4()).mass();
        if ( mass < 12. ) {
          failsLowMassVeto = true;
        }
      }
    }
    if ( failsLowMassVeto ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS low mass lepton pair veto." << std::endl;
      }
      continue;
    }
    cutFlowTable.update("m(ll) > 12 GeV", evtWeight);
    cutFlowHistManager->fillHistograms("m(ll) > 12 GeV", evtWeight);
    
    bool isSameFlavor_OS = false;
    double massSameFlavor_OS = -1.;
    for ( std::vector<const RecoLepton*>::const_iterator lepton1 = preselLeptonsFull.begin();
	  lepton1 != preselLeptonsFull.end(); ++lepton1 ) {
      for ( std::vector<const RecoLepton*>::const_iterator lepton2 = lepton1 + 1;
	    lepton2 != preselLeptonsFull.end(); ++lepton2 ) {
        if ( (*lepton1)->pdgId() == -(*lepton2)->pdgId() ) { // pair of same flavor leptons of opposite charge
          isSameFlavor_OS = true;
          double mass = ((*lepton1)->p4() + (*lepton2)->p4()).mass();
          if ( std::fabs(mass - z_mass) < std::fabs(massSameFlavor_OS - z_mass) ) massSameFlavor_OS = mass;
        }
      }
    }
    bool failsZbosonMassVeto = isSameFlavor_OS && std::fabs(massSameFlavor_OS - z_mass) < z_window;
    if ( failsZbosonMassVeto ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS Z-boson veto." << std::endl;
      }
      continue;
    }
    cutFlowTable.update("Z-boson mass veto", evtWeight);
    cutFlowHistManager->fillHistograms("Z-boson mass veto", evtWeight);
    
//--- compute MHT and linear MET discriminant (met_LD)
    RecoMEt met = metReader->read();
    const Particle::LorentzVector& metP4 = met.p4();
    std::vector<const RecoJet*> selJetsAK4_mht = jetSelectorAK4(cleanedJetsAK4_wrtLeptons, isHigherPt);
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
    cutFlowTable.update("MEt filters", evtWeight);
    cutFlowHistManager->fillHistograms("MEt filters", evtWeight);
    
    fillWithOverFlow(histogram_deltaMEtPx, metP4.px() - genMEtPx, evtWeight);
    fillWithOverFlow(histogram_deltaMEtPy, metP4.py() - genMEtPy, evtWeight);

    // compute signal extraction observables
    Particle::LorentzVector HbbP4 = selJetP4_Hbb_lead + selJetP4_Hbb_sublead;
    double m_Hbb    = HbbP4.mass();
    double dR_Hbb   = deltaR(selJetP4_Hbb_lead, selJetP4_Hbb_sublead);
    double dPhi_Hbb = TMath::Abs(deltaPhi(selJetP4_Hbb_lead.phi(), selJetP4_Hbb_sublead.phi())); // CV: map dPhi into interval [0..pi]
    double pT_Hbb   = HbbP4.pt();
    Particle::LorentzVector llP4 = selLeptonP4_lead + selLeptonP4_sublead;
    double m_ll  = llP4.mass();
    double dR_ll = deltaR(selLeptonP4_lead, selLeptonP4_sublead);
    double dPhi_ll = TMath::Abs(deltaPhi(selLeptonP4_lead.phi(), selLeptonP4_sublead.phi())); 
    double pT_ll = llP4.pt();
    double dPhi_lep1MEt = TMath::Abs(deltaPhi(selLeptonP4_lead.phi(), metP4.phi()));
    double dPhi_lep2MEt = TMath::Abs(deltaPhi(selLeptonP4_sublead.phi(), metP4.phi()));
    double min_dPhi_lepMEt = TMath::Min(dPhi_lep1MEt, dPhi_lep2MEt);
    //double max_dPhi_lepMEt = TMath::Max(dPhi_lep1MEt, dPhi_lep2MEt);
    Particle::LorentzVector HwwP4 = selLeptonP4_lead + selLeptonP4_sublead + metP4;
    double m_Hww = HwwP4.mass();
    double pT_Hww = HwwP4.pt();
    double Smin_Hww = comp_Smin(selLeptonP4_lead + selLeptonP4_sublead, metP4.px(), metP4.py());
    double dR_b1lep1 = deltaR(selJetP4_Hbb_lead, selLeptonP4_lead);
    double dR_b1lep2 = deltaR(selJetP4_Hbb_lead, selLeptonP4_sublead);
    double dR_b2lep1 = deltaR(selJetP4_Hbb_sublead, selLeptonP4_lead);
    double dR_b2lep2 = deltaR(selJetP4_Hbb_sublead, selLeptonP4_sublead);
    Particle::LorentzVector HHvisP4 = HbbP4 + selLeptonP4_lead + selLeptonP4_sublead;
    double m_HHvis = HHvisP4.mass();
    //double pT_HHvis = HHvisP4.pt();
    //double dPhi_HHvis = TMath::Abs(deltaPhi(HbbP4.phi(), (selLeptonP4_lead + selLeptonP4_sublead).phi())); 
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
    int mT2_W_step = mT2Algo_2particle.get_min_step();
    double cSumPx = selLeptonP4_lead.px() + selLeptonP4_sublead.px() + metP4.px();
    double cSumPy = selLeptonP4_lead.py() + selLeptonP4_sublead.py() + metP4.py();
    mT2Algo_2particle(
      selJetP4_Hbb_lead.px(), selJetP4_Hbb_lead.py(), selJetP4_Hbb_lead.mass(), 
      selJetP4_Hbb_sublead.px(), selJetP4_Hbb_sublead.py(), selJetP4_Hbb_sublead.mass(), 
      cSumPx, cSumPy, mem::wBosonMass);
    double mT2_top_2particle = mT2Algo_2particle.get_min_mT2();
    int mT2_top_2particle_step = mT2Algo_2particle.get_min_step();
    mT2_3particle mT2Algo_3particle;
    mT2Algo_3particle(
      selJetP4_Hbb_lead.px(), selJetP4_Hbb_lead.py(), selJetP4_Hbb_lead.mass(), 
      selJetP4_Hbb_sublead.px(), selJetP4_Hbb_sublead.py(), selJetP4_Hbb_sublead.mass(), 
      selLeptonP4_lead.px(), selLeptonP4_lead.py(), selLeptonP4_lead.mass(),  
      selLeptonP4_sublead.px(), selLeptonP4_sublead.py(), selLeptonP4_sublead.mass(),
      metP4.px(), metP4.py(), 0.);
    double mT2_top_3particle_permutation1 = mT2Algo_3particle.get_min_mT2();
    int mT2_top_3particle_permutation1_step = mT2Algo_3particle.get_min_step();
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
    TLorentzVector hmeLepton1P4(selLeptonP4_lead.px(), selLeptonP4_lead.py(), selLeptonP4_lead.pz(), selLeptonP4_lead.energy());
    TLorentzVector hmeLepton2P4(selLeptonP4_sublead.px(), selLeptonP4_sublead.py(), selLeptonP4_sublead.pz(), selLeptonP4_sublead.energy());
    TLorentzVector hmeBJet1P4(selJetP4_Hbb_lead.px(), selJetP4_Hbb_lead.py(), selJetP4_Hbb_lead.pz(), selJetP4_Hbb_lead.energy());
    TLorentzVector hmeBJet2P4(selJetP4_Hbb_sublead.px(), selJetP4_Hbb_sublead.py(), selJetP4_Hbb_sublead.pz(), selJetP4_Hbb_sublead.energy());
    TLorentzVector hmeMEtP4(metP4.px(), metP4.py(), 0., metP4.pt());
    double hmeSumJetsPx = -(selLeptonP4_lead.px() + selLeptonP4_sublead.px() + selJetP4_Hbb_lead.px() + selJetP4_Hbb_sublead.px() + metP4.px());
    double hmeSumJetsPy = -(selLeptonP4_lead.py() + selLeptonP4_sublead.py() + selJetP4_Hbb_lead.py() + selJetP4_Hbb_sublead.py() + metP4.py());
    double hmeSumJetsPz = 0.;
    double hmeSumJetsEn = TMath::Sqrt(hmeSumJetsPx*hmeSumJetsPx + hmeSumJetsPy*hmeSumJetsPy);
    TLorentzVector hmeSumJetsP4(hmeSumJetsPx, hmeSumJetsPy, hmeSumJetsPz, hmeSumJetsEn);
    const bool PUSample = true;
    const int ievent = eventInfo.event;
    const int iterations = 10000;
    const int bjetrescaleAlgo = 2;
    const int metcorrection = 5;
    const bool weightfromonshellnupt_func = false;
    const bool weightfromonshellnupt_hist = true;
    const bool weightfromonoffshellWmass_hist = true;
    const bool useMET = true;
    LocalFileInPath RefPDFfile = LocalFileInPath("hhAnalysis/Heavymassestimator/data/REFPDFPU40.root");
    if( RefPDFfile.fullPath().empty() )
      throw cms::Exception("analyze_hh_bb2l")
	<< "Failed to find file = 'REFPDFPU40.root' !!\n";
    clock.Reset();
    clock.Start("hmeAlgo");
    heavyMassEstimator hmeAlgo(
      &hmeLepton1P4, &hmeLepton2P4, &hmeBJet1P4, &hmeBJet2P4, &hmeSumJetsP4, &hmeMEtP4,
      PUSample, ievent, weightfromonshellnupt_func, weightfromonshellnupt_hist, weightfromonoffshellWmass_hist,
      iterations, RefPDFfile.fullPath(), useMET, bjetrescaleAlgo, metcorrection);
    double m_HH_hme = -1.; 
    bool hme_isValidSolution = hmeAlgo.runheavyMassEstimator();
    if ( hme_isValidSolution ) {
      TH1F hmeHist = hmeAlgo.getheavyMassEstimatorh2();
      m_HH_hme = hmeHist.GetXaxis()->GetBinCenter(hmeHist.GetMaximumBin());
    }
    clock.Stop("hmeAlgo");
    double hmeCpuTime = clock.GetCpuTime("hmeAlgo");
    //std::cout << "m_HH_hme = " << m_HH_hme << std::endl;
    //---------------------------------------------------------------------------

    //---------------------------------------------------------------------------
    // CV: compute matrix element method (MEM) likelihood ratio of HH signal and ttbar background hypotheses

    // check that reconstructed leptons and b-jets are generator-level matched
    if ( genMatchingOption == 1 || genMatchingOption == 2 ) {
      if ( !(selLepton_lead->genLepton() && selLepton_sublead->genLepton() && selJet_Hbb_lead->genJet() && selJet_Hbb_sublead->genJet()) ) {
	if ( run_lumi_eventSelector ) {
	  std::cout << "event " << eventInfo.str() << " FAILS generator-level matching." << std::endl;
	  std::cout << "selLepton_lead->genLepton = " << selLepton_lead->genLepton() << std::endl;
	  std::cout << "selLepton_sublead->genLepton = " << selLepton_sublead->genLepton() << std::endl;
	  std::cout << "selJet_Hbb_lead->genJet = " << selJet_Hbb_lead->genJet() << std::endl;
	  std::cout << "selJet_Hbb_sublead->genJet = " << selJet_Hbb_sublead->genJet() << std::endl;
	}
	continue;
      }
    }
    cutFlowTable.update("generator-level matching", evtWeight_inclusive);

    // use either generator-level or reconstructed momenta as input for MEM computation
    Particle::LorentzVector memLeptonP4_lead;    
    Particle::LorentzVector memLeptonP4_sublead;
    Particle::LorentzVector memBJetP4_lead;
    Particle::LorentzVector memBJetP4_sublead;
    Particle::LorentzVector memBJetP4_highestCSV;
    double memMEtPx = 0.;
    double memMEtPy = 0.;
    if ( genMatchingOption == 1 ) {
      memLeptonP4_lead = selLepton_lead->genLepton()->p4();
      memLeptonP4_sublead = selLepton_sublead->genLepton()->p4();
      memBJetP4_lead = selJet_Hbb_lead->genJet()->p4();
      memBJetP4_sublead = selJet_Hbb_sublead->genJet()->p4();
      memBJetP4_highestCSV = selJet1_Hbb->genJet()->p4();
      memMEtPx = genMEtPx;
      memMEtPy = genMEtPy;
    } else {
      memLeptonP4_lead = selLepton_lead->p4();
      memLeptonP4_sublead = selLepton_sublead->p4();
      memBJetP4_lead = selJet_Hbb_lead->p4();
      memBJetP4_sublead = selJet_Hbb_sublead->p4();
      memBJetP4_highestCSV = selJet1_Hbb->p4();
      memMEtPx = metP4.px();
      memMEtPy = metP4.py();
    }
    int memLeptonType_lead;   
    double memLeptonMass_lead;   
    if ( selLepton_lead->is_electron() ) {
      memLeptonType_lead = mem::MeasuredParticle::kElectron;
      memLeptonMass_lead = mem::electronMass;
    } else if ( selLepton_lead->is_muon() ) {
      memLeptonType_lead = mem::MeasuredParticle::kMuon;
      memLeptonMass_lead = mem::muonMass;
    } else assert(0);
    int memLeptonType_sublead;   
    double memLeptonMass_sublead;   
    if ( selLepton_sublead->is_electron() ) {
      memLeptonType_sublead = mem::MeasuredParticle::kElectron;
      memLeptonMass_sublead = mem::electronMass;
    } else if ( selLepton_sublead->is_muon() ) {
      memLeptonType_sublead = mem::MeasuredParticle::kMuon;
      memLeptonMass_sublead = mem::muonMass;
    } else assert(0);

    mem::MeasuredParticle memMeasuredLepton_lead(memLeptonType_lead, 
      memLeptonP4_lead.pt(), memLeptonP4_lead.eta(), memLeptonP4_lead.phi(), 
      memLeptonMass_lead, selLepton_lead->charge());
    mem::MeasuredParticle memMeasuredLepton_sublead(memLeptonType_sublead, 
      memLeptonP4_sublead.pt(), memLeptonP4_sublead.eta(), memLeptonP4_sublead.phi(), 
      memLeptonMass_sublead, selLepton_sublead->charge());
    mem::MeasuredParticle memMeasuredBJet_lead(mem::MeasuredParticle::kBJet,
      memBJetP4_lead.pt(), memBJetP4_lead.eta(), memBJetP4_lead.phi(), 
      mem::bottomQuarkMass);
    mem::MeasuredParticle memMeasuredBJet_sublead(mem::MeasuredParticle::kBJet,
      memBJetP4_sublead.pt(), memBJetP4_sublead.eta(), memBJetP4_sublead.phi(), 
      mem::bottomQuarkMass);
    mem::MeasuredParticle memMeasuredBJet_highestCSV(mem::MeasuredParticle::kBJet,
      memBJetP4_highestCSV.pt(), memBJetP4_highestCSV.eta(), memBJetP4_highestCSV.phi(), 
      mem::bottomQuarkMass);

    std::vector<mem::MeasuredParticle> memMeasuredParticles;
    memMeasuredParticles.push_back(memMeasuredLepton_lead);
    memMeasuredParticles.push_back(memMeasuredLepton_sublead);
    memMeasuredParticles.push_back(memMeasuredBJet_lead);
    memMeasuredParticles.push_back(memMeasuredBJet_sublead);
    
    std::vector<mem::MeasuredParticle> memMeasuredParticles_missingBJet;
    memMeasuredParticles_missingBJet.push_back(memMeasuredLepton_lead);
    memMeasuredParticles_missingBJet.push_back(memMeasuredLepton_sublead);
    memMeasuredParticles_missingBJet.push_back(memMeasuredBJet_highestCSV);

    const double sqrtS = 13.e+3;
    const std::string pdfName = "MSTW2008lo68cl";
    const std::string madgraphFileName_signal     = "hhAnalysis/bbwwMEM/data/param_hh.dat";
    const std::string madgraphFileName_background = "hhAnalysis/bbwwMEM/data/param_ttbar.dat";
    const bool applyOnshellWmassConstraint_signal = false;
    const int memAlgo_verbosity = 1;
    //const int memAlgo_verbosity = 3;
    //const int maxObjFunctionCalls_signal = 2500;
    //const int maxObjFunctionCalls_background = 25000;
    const int maxObjFunctionCalls_signal = 1000;
    const int maxObjFunctionCalls_background = 10000;
    //const int maxObjFunctionCalls_background = 1000;

    clock.Reset();
    clock.Start("memAlgo");
    MEMbbwwAlgoDilepton memAlgo(sqrtS, pdfName, findFile(madgraphFileName_signal), findFile(madgraphFileName_background), memAlgo_verbosity);
    memAlgo.applyOnshellWmassConstraint_signal(applyOnshellWmassConstraint_signal);
    memAlgo.setIntMode(MEMbbwwAlgoDilepton::kVAMP);
    memAlgo.setMaxObjFunctionCalls_signal(maxObjFunctionCalls_signal);
    memAlgo.setMaxObjFunctionCalls_background(maxObjFunctionCalls_background);
    memAlgo.integrate(memMeasuredParticles, memMEtPx, memMEtPy, met.cov());
    MEMbbwwResultDilepton memResult = memAlgo.getResult();
    clock.Stop("memAlgo");

    double memCpuTime = clock.GetCpuTime("memAlgo");
    std::cout << "MEM:"
	      << " probability for signal hypothesis = " << memResult.getProb_signal() << " +/- " << memResult.getProbErr_signal() << ","
	      << " probability for background hypothesis = " << memResult.getProb_background() << " +/- " << memResult.getProbErr_background() << " " 
	      << "--> likelihood ratio = " << memResult.getLikelihoodRatio() << " +/- " << memResult.getLikelihoodRatioErr() 
	      << " (CPU time = " << memCpuTime << ")" << std::endl;

    clock.Reset();
    clock.Start("memAlgo_missingBJet");
    MEMbbwwAlgoDilepton memAlgo_missingBJet(sqrtS, pdfName, findFile(madgraphFileName_signal), findFile(madgraphFileName_background), memAlgo_verbosity);
    memAlgo_missingBJet.applyOnshellWmassConstraint_signal(applyOnshellWmassConstraint_signal);
    memAlgo_missingBJet.setIntMode(MEMbbwwAlgoDilepton::kVAMP);
    memAlgo_missingBJet.setMaxObjFunctionCalls_signal(maxObjFunctionCalls_signal);
    memAlgo_missingBJet.setMaxObjFunctionCalls_background(maxObjFunctionCalls_background);
    memAlgo_missingBJet.integrate(memMeasuredParticles_missingBJet, memMEtPx, memMEtPy, met.cov());
    MEMbbwwResultDilepton memResult_missingBJet = memAlgo_missingBJet.getResult();
    clock.Stop("memAlgo_missingBJet");
    
    double memCpuTime_missingBJet = clock.GetCpuTime("memAlgo_missingBJet");
    std::cout << "MEM (missing b-jet case):" 
	      << " probability for signal hypothesis = " << memResult_missingBJet.getProb_signal() << " +/- " << memResult_missingBJet.getProbErr_signal() << ","
	      << " probability for background hypothesis = " << memResult_missingBJet.getProb_background() << " +/- " << memResult_missingBJet.getProbErr_background() << " " 
	      << "--> likelihood ratio = " << memResult_missingBJet.getLikelihoodRatio() << " +/- " << memResult_missingBJet.getLikelihoodRatioErr() 
	      << " (CPU time = " << memCpuTime_missingBJet << ")" << std::endl;

    std::cout << "selLepton_lead->genLepton = " << selLepton_lead->genLepton() << std::endl;
    std::cout << "selLepton_lead: pT = " << selLepton_lead->pt() << ", eta = " << selLepton_lead->eta() << ", phi = " << selLepton_lead->phi() << std::endl;
    std::cout << "selLepton_sublead->genLepton = " << selLepton_sublead->genLepton() << std::endl;
    std::cout << "selLepton_sublead: pT = " << selLepton_sublead->pt() << ", eta = " << selLepton_sublead->eta() << ", phi = " << selLepton_sublead->phi() << std::endl;
    const GenJet* genBJet1 = &genBJetsForMatching[0];
    std::cout << "genBJet #0: pT = " << genBJet1->pt() << ", eta = " << genBJet1->eta() << ", phi = " << genBJet1->phi() << std::endl;
    const GenJet* genBJet2 = &genBJetsForMatching[1];
    std::cout << "genBJet #1: pT = " << genBJet2->pt() << ", eta = " << genBJet2->eta() << ", phi = " << genBJet2->phi() << std::endl;
    printCollection("uncleaned AK4 jets", jet_ptrs_ak4);
    printCollection("selJetsAK4_Hbb", selJetsAK4_Hbb);
    std::cout << "selJet_Hbb_lead->genJet = " << selJet_Hbb_lead->genJet() << std::endl;
    printBJet("selJet_Hbb_lead", selJet_Hbb_lead);
    std::cout << "selJet_Hbb_sublead->genJet = " << selJet_Hbb_sublead->genJet() << std::endl;
    printBJet("selJet_Hbb_sublead", selJet_Hbb_sublead);
    std::cout << "numBJets: loose = " << numBJets_loose << ", medium = " << numBJets_medium << std::endl;

    if ( (memResult.getLikelihoodRatio() < 0.02 &&  isSignal) || 
	 (memResult.getLikelihoodRatio() > 0.98 && !isSignal) ) {
      const GenLepton* genLepton_lead = &genLeptonsForMatching[0];
      int genLepton_lead_matchType = compGenMatchType(genLepton_lead, std::vector<const RecoLepton*>({ selLepton_lead, selLepton_sublead }), preselLeptonsFull, tightLeptonsFull);
      fillWithOverFlow(histogram_badMEM_genLepton_lead_matchType, genLepton_lead_matchType, evtWeight);
      const GenLepton* genLepton_sublead = &genLeptonsForMatching[1];
      int genLepton_sublead_matchType = compGenMatchType(genLepton_sublead, std::vector<const RecoLepton*>({ selLepton_lead, selLepton_sublead }), preselLeptonsFull, tightLeptonsFull);
      fillWithOverFlow(histogram_badMEM_genLepton_sublead_matchType, genLepton_sublead_matchType, evtWeight);
      const GenJet* genJet_Hbb_lead = &genBJetsForMatching[0];
      int genJet_Hbb_lead_matchType = compGenMatchType(genJet_Hbb_lead, std::vector<const RecoJetBase*>({ selJet_Hbb_lead, selJet_Hbb_sublead }), jet_ptrs_ak4, selJetsAK4);
      fillWithOverFlow(histogram_badMEM_genJet_Hbb_lead_matchType, genJet_Hbb_lead_matchType, evtWeight);
      const GenJet* genJet_Hbb_sublead = &genBJetsForMatching[1];
      int genJet_Hbb_sublead_matchType = compGenMatchType(genJet_Hbb_sublead, std::vector<const RecoJetBase*>({ selJet_Hbb_lead, selJet_Hbb_sublead }), jet_ptrs_ak4, selJetsAK4);
      fillWithOverFlow(histogram_badMEM_genJet_Hbb_sublead_matchType, genJet_Hbb_sublead_matchType, evtWeight);
      fillWithOverFlow(histogram_badMEM_numBJets_loose, numBJets_loose, evtWeight);
      fillWithOverFlow(histogram_badMEM_numBJets_medium, numBJets_medium, evtWeight);
      const double nonzero = 1.e-30;
      fillWithOverFlow(histogram_badMEM_log_memProb_signal, TMath::Log(TMath::Max(nonzero, memResult.getProb_signal())), evtWeight);
      fillWithOverFlow(histogram_badMEM_log_memProb_signal_missingBJet, TMath::Log(TMath::Max(nonzero, memResult_missingBJet.getProb_signal())), evtWeight);
      fillWithOverFlow(histogram_badMEM_log_memProb_background, TMath::Log(TMath::Max(nonzero, memResult.getProb_background())), evtWeight);
      fillWithOverFlow(histogram_badMEM_log_memProb_background_missingBJet, TMath::Log(TMath::Max(nonzero, memResult_missingBJet.getProb_background())), evtWeight);
      fillWithOverFlow(histogram_badMEM_memLR_missingBJet, memResult_missingBJet.getLikelihoodRatio(), evtWeight);
      std::cout << "--> CHECK !!" << std::endl;
    }
    //---------------------------------------------------------------------------
      
    mvaInputs_XGB["m_ll"] = m_ll;
    mvaInputs_XGB["m_Hbb"] = m_Hbb;
    mvaInputs_XGB["nBJetMedium"] = selBJetsAK4_medium.size();
    mvaInputs_XGB["m_Hww"] = m_Hww;
    mvaInputs_XGB["logTopness_fixedChi2"] = logTopness_fixedChi2;
    mvaInputs_XGB["logHiggsness_fixedChi2"] = logHiggsness_fixedChi2;
    mvaInputs_XGB["mT2_top_3particle"] = mT2_top_3particle;
    mvaInputs_XGB["pT_HH"] = pT_HH;
    mvaInputs_XGB["dPhi_HH"] = dPhi_HH;
    mvaInputs_XGB["min_dPhi_lepMEt"] = min_dPhi_lepMEt;
    mvaInputs_XGB["max_dR_b_lep"] = std::max(dR_b1lep1,std::max(dR_b1lep2,std::max(dR_b2lep1,dR_b2lep2)));
    mvaInputs_XGB["met"] =  metP4.pt();
    mvaInputs_XGB["max_lep_pt"] = std::max(selLepton_lead->pt(),selLepton_sublead->pt());
    mvaInputs_XGB["max_bjet_pt"] = std::max(selJetP4_Hbb_lead.pt(),selJetP4_Hbb_sublead.pt());
    mvaInputs_XGB["gen_mHH"] = 300;
    double mvaoutput_bb2l300 = mva_xgb_bb2l(mvaInputs_XGB);
    mvaInputs_XGB["gen_mHH"] = 400;
    double mvaoutput_bb2l400 = mva_xgb_bb2l(mvaInputs_XGB);
    mvaInputs_XGB["gen_mHH"] = 750;
    double mvaoutput_bb2l750 = mva_xgb_bb2l(mvaInputs_XGB);
    /*    mvaInputs_XGB["m_ll"] = 117.5084;
    mvaInputs_XGB["m_Hbb"] = 111.439705;
    mvaInputs_XGB["nBJetMedium"] = 1;
    mvaInputs_XGB["m_Hww"] = 172.971237;
    mvaInputs_XGB["logTopness_fixedChi2"] = 0.128858;
    mvaInputs_XGB["logHiggsness_fixedChi2"] = 2.700845;
    mvaInputs_XGB["mT2_top_3particle"]= 93.844116;
    mvaInputs_XGB["pT_HH"] = 61.046185;
    mvaInputs_XGB["dPhi_HH"] = 2.411219;
    mvaInputs_XGB["min_dPhi_lepMEt"] = 1.493288;
    mvaInputs_XGB["max_dR_b_lep"] = 2.863791;
    mvaInputs_XGB["met"] =  43.858006;
    mvaInputs_XGB["max_lep_pt"] = 56.038994;
    mvaInputs_XGB["max_bjet_pt"] = 82.440727;
    mvaInputs_XGB["gen_mHH"] = 400;
    double mvaoutput_bb2l300 = mva_xgb_bb2l(mvaInputs_XGB);
    std::cout << "mva    ============== " << mvaoutput_bb2l300 << std::endl;
    mvaoutput_bb2l300 = (*mva_xml_bb2l)(mvaInputs_XGB); //mva 0.813011(test),0.14326528(true)
    std::cout << "mva    ============== " << mvaoutput_bb2l300 << std::endl;*/

    mvaInputsnohiggnessnotopness_XGB["m_ll"] = m_ll;
    mvaInputsnohiggnessnotopness_XGB["m_Hbb"] = m_Hbb;
    mvaInputsnohiggnessnotopness_XGB["nBJetMedium"] = selBJetsAK4_medium.size();
    mvaInputsnohiggnessnotopness_XGB["m_Hww"] = m_Hww;
    mvaInputsnohiggnessnotopness_XGB["mT2_top_3particle"] = mT2_top_3particle;
    mvaInputsnohiggnessnotopness_XGB["pT_HH"] = pT_HH;
    mvaInputsnohiggnessnotopness_XGB["dPhi_HH"] = dPhi_HH;
    mvaInputsnohiggnessnotopness_XGB["min_dPhi_lepMEt"] = min_dPhi_lepMEt;
    mvaInputsnohiggnessnotopness_XGB["max_dR_b_lep"] = std::max(dR_b1lep1,std::max(dR_b1lep2,std::max(dR_b2lep1,dR_b2lep2)));
    mvaInputsnohiggnessnotopness_XGB["met"] =  metP4.pt();
    mvaInputsnohiggnessnotopness_XGB["max_lep_pt"] = std::max(selLepton_lead->pt(),selLepton_sublead->pt());
    mvaInputsnohiggnessnotopness_XGB["max_bjet_pt"] = std::max(selJetP4_Hbb_lead.pt(),selJetP4_Hbb_sublead.pt());
    mvaInputsnohiggnessnotopness_XGB["gen_mHH"] = 300;
    double mvaoutputnohiggnessnotopness_bb2l300 = mva_xgbnohiggnessnotopness_bb2l(mvaInputsnohiggnessnotopness_XGB);
    mvaInputsnohiggnessnotopness_XGB["gen_mHH"] = 400;
    double mvaoutputnohiggnessnotopness_bb2l400 = mva_xgbnohiggnessnotopness_bb2l(mvaInputsnohiggnessnotopness_XGB);
    mvaInputsnohiggnessnotopness_XGB["gen_mHH"] = 750;
    double mvaoutputnohiggnessnotopness_bb2l750 = mva_xgbnohiggnessnotopness_bb2l(mvaInputsnohiggnessnotopness_XGB);

//--- fill histograms with events passing final selection
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
      m_Hww, pT_Hww, Smin_Hww,
      m_HHvis, m_HH, m_HH_hme, hmeCpuTime, dR_HH, dPhi_HH, pT_HH, Smin_HH,
      mT2_W, mT2_W_step, mT2_top_2particle, mT2_top_2particle_step, mT2_top_3particle, mT2_top_3particle_step, 
      logHiggsness_publishedChi2, logTopness_publishedChi2,
      -1., -1., -1., -1., -1., -1., 
      &memResult, memCpuTime, 
      &memResult_missingBJet, memCpuTime_missingBJet, 
      mvaoutput_bb2l300, mvaoutput_bb2l400, mvaoutput_bb2l750,
      mvaoutputnohiggnessnotopness_bb2l300, mvaoutputnohiggnessnotopness_bb2l400, mvaoutputnohiggnessnotopness_bb2l750,
      evtWeight);
    selHistManager->genEvtHistManager_afterCuts_->fillHistograms(genElectrons, genMuons, {}, {}, genJets, evtWeight_inclusive);
    selHistManager->lheInfoHistManager_afterCuts_->fillHistograms(*lheInfoReader, evtWeight);
    selHistManager->weights_->fillHistograms("genWeight", eventInfo.genWeight);
    selHistManager->weights_->fillHistograms("pileupWeight", eventInfo.pileupWeight);
    selHistManager->weights_->fillHistograms("triggerWeight", triggerWeight);
    selHistManager->weights_->fillHistograms("data_to_MC_correction", weight_data_to_MC_correction);

    if ( selEventsFile ) {
      (*selEventsFile) << eventInfo.run << ':' << eventInfo.lumi << ':' << eventInfo.event << '\n';
    }

    ++selectedEntries;
    selectedEntries_weighted += evtWeight;
    histogram_selectedEntries->Fill(0.);
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

  delete dataToMCcorrectionInterface;

  delete run_lumi_eventSelector;

  delete selEventsFile;

  delete muonReader;
  delete electronReader;
  delete jetReaderAK4;
  delete jetReaderAK8; 
  delete metReader;
  delete metFilterReader;
  delete genLeptonReader;
  delete genNeutrinoReader;
  delete genJetReader;
  delete lheInfoReader;

  delete genEvtHistManager_beforeCuts;

  hltPaths_delete(triggers_1e);
  hltPaths_delete(triggers_2e);
  hltPaths_delete(triggers_1mu);
  hltPaths_delete(triggers_2mu);
  hltPaths_delete(triggers_1e1mu);

  delete inputTree;

  clock.Show("testMEM_hh_bb2l");

  return EXIT_SUCCESS;
}
