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

#include <TBenchmark.h> // TBenchmark
#include <TString.h> // TString, Form
#include <TError.h> // gErrorAbortLevel, kError
#include <TRandom3.h> // TRandom3
#include <TLorentzVector.h> // TLore

#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h" // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronReader.h" // RecoElectronReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronCollectionSelectorLoose.h" // RecoElectronCollectionSelectorLoose
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronCollectionSelectorFakeable.h" // RecoElectronCollectionSelectorFakeable
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronCollectionSelectorTight.h" // RecoElectronCollectionSelectorTight
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonReader.h" // RecoMuonReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonCollectionSelectorLoose.h" // RecoMuonCollectionSelectorLoose
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonCollectionSelectorFakeable.h" // RecoMuonCollectionSelectorFakeable
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonCollectionSelectorTight.h" // RecoMuonCollectionSelectorTight
#include "tthAnalysis/HiggsToTauTau/interface/GenLepton.h" // GenLepton
#include "tthAnalysis/HiggsToTauTau/interface/GenLeptonReader.h" // GenLeptonReader
#include "tthAnalysis/HiggsToTauTau/interface/GenLeptonCollectionSelector.h" // GenLeptonCollectionSelector
#include "tthAnalysis/HiggsToTauTau/interface/RecoJet.h" // RecoJet
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetReader.h" // RecoJetReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetCollectionSelector.h" // RecoJetCollectionSelector
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetCollectionSelectorBtag.h" // RecoJetCollectionSelectorBtagLoose, RecoJetCollectionSelectorBtagMedium
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetAK8.h" // RecoJetAK8
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetReaderAK8.h" // RecoJetReaderAK8
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEt.h" // RecoMEt
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEtReader.h" // RecoMEtReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoVertex.h" // RecoVertex
#include "tthAnalysis/HiggsToTauTau/interface/RecoVertexReader.h" // RecoVertexReader
#include "tthAnalysis/HiggsToTauTau/interface/GenParticleReader.h" // GenParticleReader
#include "tthAnalysis/HiggsToTauTau/interface/GenJet.h" // GenJet
#include "tthAnalysis/HiggsToTauTau/interface/GenJetReader.h" // GenJetReader
#include "tthAnalysis/HiggsToTauTau/interface/GenJetCollectionSelector.h" // GenJetCollectionSelector
#include "tthAnalysis/HiggsToTauTau/interface/LHEInfoReader.h" // LHEInfoReader
#include "tthAnalysis/HiggsToTauTau/interface/EventInfo.h" // EventInfo
#include "tthAnalysis/HiggsToTauTau/interface/EventInfoReader.h" // EventInfoReader
#include "tthAnalysis/HiggsToTauTau/interface/convert_to_ptrs.h" // convert_to_ptrs
#include "tthAnalysis/HiggsToTauTau/interface/ParticleCollectionCleaner.h" // RecoElectronCollectionCleaner, RecoMuonCollectionCleaner, RecoJetCollectionCleaner
#include "tthAnalysis/HiggsToTauTau/interface/ParticleCollectionGenMatcher.h" // RecoElectronCollectionGenMatcher, RecoMuonCollectionGenMatcher, RecoJetCollectionGenMatcher
#include "tthAnalysis/HiggsToTauTau/interface/RunLumiEventSelector.h" // RunLumiEventSelector
#include "tthAnalysis/HiggsToTauTau/interface/CutFlowTableHistManager.h" // CutFlowTableHistManager
#include "tthAnalysis/HiggsToTauTau/interface/WeightHistManager.h" // WeightHistManager
#include "tthAnalysis/HiggsToTauTau/interface/GenEvtHistManager.h" // GenEvtHistManager
#include "tthAnalysis/HiggsToTauTau/interface/LHEInfoHistManager.h" // LHEInfoHistManager
#include "tthAnalysis/HiggsToTauTau/interface/leptonTypes.h" // getLeptonType, kElectron, kMuon
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // getBTagWeight_option, isHigherPt, isMatched, contains, pileupJetID, findGenJetsFromWBoson
#include "tthAnalysis/HiggsToTauTau/interface/generalAuxFunctions.h" // format_vstring
#include "tthAnalysis/HiggsToTauTau/interface/cutFlowTable.h" // cutFlowTableType
#include "tthAnalysis/HiggsToTauTau/interface/TTreeWrapper.h" // TTreeWrapper

#include "hhAnalysis/multilepton/interface/AnalysisConfig_hh.h" // AnalysisConfig_hh
#include "hhAnalysis/multilepton/interface/RecoElectronCollectionSelectorFakeable_hh_multilepton.h" // RecoElectronCollectionSelectorFakeable_hh_multilepton
#include "hhAnalysis/multilepton/interface/RecoMuonCollectionSelectorFakeable_hh_multilepton.h" // RecoMuonCollectionSelectorFakeable_hh_multilepton
#include "hhAnalysis/multilepton/interface/RecoJetCollectionSelectorAK8_hh_Wjj.h" // RecoJetSelectorAK8_hh_Wjj

#include "hhAnalysis/bbww/interface/RecoJetCollectionSelectorAK8_hh_bbWW_Hbb.h" // RecoJetSelectorAK8_hh_bbWW_Hbb
#include "hhAnalysis/bbww/interface/jetSelectionAuxFunctions.h" // selectJets_Hbb, countBJets_Hbb
#include "hhAnalysis/bbww/interface/genMatchingAuxFunctions.h" // findGenLepton_and_NeutrinoFromWBoson
#include "hhAnalysis/bbww/interface/measuredParticleAuxFunctions.h" // convert_to_MeasuredParticles
#include "hhAnalysis/bbww/interface/memNtupleAuxFunctions_singlelepton.h" // MEMEvent_singlelepton, buildMEMEvents_singlelepton_boosted, buildMEMEvents_singlelepton_semiboosted, buildMEMEvents_singlelepton_resolved, addGenMatches_singlelepton, buildMEMEventMap_singlelepton
#include "hhAnalysis/bbww/interface/comp_metP4_B2G_18_008.h" // comp_metP4_B2G_18_008

#include "hhAnalysis/bbwwMEM/interface/MeasuredParticle.h" // MeasuredParticle
#include "hhAnalysis/bbwwMEM/interface/MEMbbwwAlgoSingleLepton.h" // MEMbbwwAlgoSingleLepton

#include "hhAnalysis/bbwwMEMPerformanceStudies/interface/MEMbbwwNtupleManager_singlelepton.h" // MEMbbwwNtupleManager_singlelepton


#include <boost/math/special_functions/sign.hpp> // boost::math::sign()

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

/**
 * @brief Produce MEM Ntuple for BDT/LBN regression training in HH->bbWW single lepton channel
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

  std::cout << "<produceMEMNtuple_hh_bb1l>:" << std::endl;

//--- keep track of time it takes the macro to execute
  TBenchmark clock;
  clock.Start("produceMEMNtuple_hh_bb1l");

//--- read python configuration parameters
  if ( !edm::readPSetsFrom(argv[1])->existsAs<edm::ParameterSet>("process") )
    throw cms::Exception("produceMEMNtuple_hh_bb1l")
      << "No ParameterSet 'process' found in configuration file = " << argv[1] << " !!\n";

  edm::ParameterSet cfg = edm::readPSetsFrom(argv[1])->getParameter<edm::ParameterSet>("process");

  edm::ParameterSet cfg_analyze = cfg.getParameter<edm::ParameterSet>("analyze_hh_bbwwMEM_singlelepton");
  AnalysisConfig_hh analysisConfig("HH->bbWW", cfg_analyze);

  std::string treeName = cfg_analyze.getParameter<std::string>("treeName");

  std::string process_string = cfg_analyze.getParameter<std::string>("process");
  bool isSignal = ( process_string.find("signal") != std::string::npos ) ? true : false;

  std::string histogramDir = cfg_analyze.getParameter<std::string>("histogramDir");

  std::string era_string = cfg_analyze.getParameter<std::string>("era");
  const Era era = get_era(era_string);

  std::string branchName_electrons = cfg_analyze.getParameter<std::string>("branchName_electrons");
  std::string branchName_muons = cfg_analyze.getParameter<std::string>("branchName_muons");
  std::string branchName_jets_ak4 = cfg_analyze.getParameter<std::string>("branchName_jets_ak4");
  std::string branchName_jets_ak8 = cfg_analyze.getParameter<std::string>("branchName_jets_ak8");
  std::string branchName_subjets_ak8 = cfg_analyze.getParameter<std::string>("branchName_subjets_ak8");
  std::string branchName_jets_ak8LS = cfg_analyze.getParameter<std::string>("branchName_jets_ak8LS");
  std::string branchName_subjets_ak8LS = cfg_analyze.getParameter<std::string>("branchName_subjets_ak8LS");
  std::string branchName_met = cfg_analyze.getParameter<std::string>("branchName_met");
  std::string branchName_vertex = cfg_analyze.getParameter<std::string>("branchName_vertex");

  std::string branchName_genLeptons = cfg_analyze.getParameter<std::string>("branchName_genLeptons");
  std::string branchName_genNeutrinos = cfg_analyze.getParameter<std::string>("branchName_genNeutrinos");
  std::string branchName_genJets = cfg_analyze.getParameter<std::string>("branchName_genJets");

  // branches specific to HH signal
  std::string branchName_genParticlesFromHiggs = cfg_analyze.getParameter<std::string>("branchName_genParticlesFromHiggs");
  std::string branchName_genWBosons = cfg_analyze.getParameter<std::string>("branchName_genWBosons");
  std::string branchName_genWJets = cfg_analyze.getParameter<std::string>("branchName_genWJets");

  // branches specific to ttbar background
  std::string branchName_genLeptonsFromTop = cfg_analyze.getParameter<std::string>("branchName_genLeptonsFromTop");
  std::string branchName_genNeutrinosFromTop = cfg_analyze.getParameter<std::string>("branchName_genNeutrinosFromTop");
  std::string branchName_genBQuarksFromTop = cfg_analyze.getParameter<std::string>("branchName_genBQuarksFromTop");
  std::string branchName_genWJetsFromTop = cfg_analyze.getParameter<std::string>("branchName_genWJetsFromTop");

  bool jetCleaningByIndex = cfg_analyze.getParameter<bool>("jetCleaningByIndex");

  // random number generator for choosing events for which to run the MEM computation
  TRandom3 rnd;
  rnd.SetSeed(12345);

  const std::string central_or_shift = "central";
  bool hasLHE = cfg_analyze.getParameter<bool>("hasLHE");
  bool apply_genWeight = cfg_analyze.getParameter<bool>("apply_genWeight");

  const std::string apply_pileupJetID_string = cfg_analyze.getParameter<std::string>("apply_pileupJetID");
  const pileupJetID apply_pileupJetID = get_pileupJetID(apply_pileupJetID_string);

  bool useAssocJetBtag = cfg_analyze.getParameter<bool>("useAssocJetBtag");

  const double lep_mva_cut_mu = cfg_analyze.getParameter<double>("lep_mva_cut_mu");
  const double lep_mva_cut_e  = cfg_analyze.getParameter<double>("lep_mva_cut_e");
  const std::string lep_mva_wp = cfg_analyze.getParameter<std::string>("lep_mva_wp");

  bool isDEBUG = cfg_analyze.getParameter<bool>("isDEBUG");

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
  int skipSelEvents = cfg_analyze.getParameter<int>("skipSelEvents");
  std::cout << " skipSelEvents = " << skipSelEvents << std::endl;
  int maxSelEvents = cfg_analyze.getParameter<int>("maxSelEvents");
  std::cout << " maxSelEvents = " << maxSelEvents << std::endl;
  unsigned reportEvery = inputFiles.reportAfter();

  fwlite::OutputFiles outputFile(cfg);
  fwlite::TFileService fs = fwlite::TFileService(outputFile.file().data());

  TTreeWrapper* inputTree = new TTreeWrapper(treeName.data(), inputFiles.files(), maxEvents);
  std::cout << "Loaded " << inputTree->getFileCount() << " file(s)." << std::endl;

//--- declare event-level variables
  EventInfo eventInfo(analysisConfig);
  EventInfoReader eventInfoReader(&eventInfo);
  inputTree->registerReader(&eventInfoReader);

  RecoVertex vertex;
  RecoVertexReader vertexReader(&vertex, branchName_vertex);
  inputTree->registerReader(&vertexReader);

  inputTree->registerReader(&eventInfoReader);

//--- declare collections of reconstructed particles
  const bool isMC = true;
  const bool readGenObjects = false;
  RecoMuonReader* muonReader = new RecoMuonReader(era, branchName_muons, isMC, readGenObjects);
  inputTree->registerReader(muonReader);
  RecoMuonCollectionSelectorLoose preselMuonSelector(era, -1, isDEBUG);
  RecoMuonCollectionSelectorFakeable fakeableMuonSelector_default(era, -1, isDEBUG);
  RecoMuonCollectionSelectorFakeable_hh_multilepton fakeableMuonSelector_hh_multilepton(era, -1, isDEBUG);
  fakeableMuonSelector_default.getSelector().set_assocJetBtag(useAssocJetBtag);
  fakeableMuonSelector_hh_multilepton.getSelector().set_assocJetBtag(useAssocJetBtag);
  muonReader->set_mvaTTH_wp(lep_mva_cut_mu);

  RecoElectronReader* electronReader = new RecoElectronReader(era, branchName_electrons, isMC, readGenObjects);
  inputTree->registerReader(electronReader);
  RecoElectronCollectionCleaner electronCleaner(0.3, isDEBUG);
  RecoElectronCollectionSelectorLoose preselElectronSelector(era, -1, isDEBUG);
  RecoElectronCollectionSelectorFakeable fakeableElectronSelector_default(era, -1, isDEBUG);
  RecoElectronCollectionSelectorFakeable_hh_multilepton fakeableElectronSelector_hh_multilepton(era, -1, isDEBUG);
  fakeableElectronSelector_default.getSelector().set_assocJetBtag(useAssocJetBtag);
  fakeableElectronSelector_hh_multilepton.getSelector().set_assocJetBtag(useAssocJetBtag);
  electronReader->set_mvaTTH_wp(lep_mva_cut_e);

  RecoJetReader* jetReaderAK4 = new RecoJetReader(era, isMC, branchName_jets_ak4, readGenObjects);
  inputTree->registerReader(jetReaderAK4);
  RecoJetCollectionCleaner jetCleanerAK4_dR04(0.4, isDEBUG);
  RecoJetCollectionCleanerByIndex jetCleanerAK4_byIndex(isDEBUG);
  RecoJetCollectionCleaner jetCleanerAK4_dR12(1.2, isDEBUG);
  RecoJetCollectionSelector jetSelectorAK4_wPileupJetId(era, -1, isDEBUG);
  jetSelectorAK4_wPileupJetId.getSelector().set_pileupJetId(apply_pileupJetID);
  RecoJetCollectionSelectorBtagLoose jetSelectorAK4_bTagLoose(era, -1, isDEBUG);
  jetSelectorAK4_bTagLoose.getSelector().set_pileupJetId(apply_pileupJetID);
  RecoJetCollectionSelectorBtagMedium jetSelectorAK4_bTagMedium(era, -1, isDEBUG);
  jetSelectorAK4_bTagMedium.getSelector().set_pileupJetId(apply_pileupJetID);

  RecoJetReaderAK8* jetReaderAK8 = new RecoJetReaderAK8(era, isMC, branchName_jets_ak8, branchName_subjets_ak8);
  inputTree->registerReader(jetReaderAK8);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR08(0.8, isDEBUG);
  RecoJetCollectionSelectorAK8_hh_bbWW_Hbb jetSelectorAK8_Hbb(era, -1, isDEBUG);
  RecoJetReaderAK8* jetReaderAK8LS = nullptr;
  if ( branchName_jets_ak8LS != branchName_jets_ak8 ) {
    jetReaderAK8LS = new RecoJetReaderAK8(era, isMC, branchName_jets_ak8LS, branchName_subjets_ak8LS);
    inputTree->registerReader(jetReaderAK8LS);
  } else {
    jetReaderAK8LS = jetReaderAK8;
  }
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR12(1.2, isDEBUG);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR16(1.6, isDEBUG);
  RecoJetCollectionSelectorAK8_hh_Wjj jetSelectorAK8_Wjj(era, -1, isDEBUG);

  RecoMEtReader* metReader = new RecoMEtReader(era, isMC, branchName_met);
  metReader->set_phiModulationCorrDetails(&eventInfo, &vertex);
  inputTree->registerReader(metReader);

//--- declare collections of generator-level particles
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
    
  // collections specific to HH signal
  GenParticleReader* genParticleFromHiggsReader = nullptr;
  if ( branchName_genParticlesFromHiggs != "" ) {
    genParticleFromHiggsReader = new GenParticleReader(branchName_genParticlesFromHiggs);
    inputTree->registerReader(genParticleFromHiggsReader);
  }
  GenParticleReader* genWBosonReader = nullptr;
  if ( branchName_genWBosons != "" ) {
    genWBosonReader = new GenParticleReader(branchName_genWBosons);
    inputTree->registerReader(genWBosonReader);
  }
  GenParticleReader* genWJetReader = nullptr;
  if ( branchName_genWJets != "" ) {
    genWJetReader = new GenParticleReader(branchName_genWJets);
    inputTree->registerReader(genWJetReader);
  }

  // collections specific to ttbar background
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
  GenParticleReader* genWJetsFromTopReader = nullptr;
  if ( branchName_genWJetsFromTop != "" ) {
    genWJetsFromTopReader = new GenParticleReader(branchName_genWJetsFromTop);
    inputTree->registerReader(genWJetsFromTopReader);
  }

  GenLeptonCollectionSelector genLeptonSelector(era, -1, isDEBUG);
  genLeptonSelector.getSelector().set_max_absEta_muon(2.4);
  genLeptonSelector.getSelector().set_max_absEta_electron(2.4);

  GenJetCollectionSelector genJetSelector(era, -1, isDEBUG);
  genJetSelector.getSelector().set_min_pt(20.);
  genJetSelector.getSelector().set_max_absEta(2.4);
  GenJetCollectionCleaner genJetCleaner(0.4, isDEBUG);

//--- declare other generator level information
  LHEInfoReader* lheInfoReader = new LHEInfoReader(hasLHE);
  inputTree->registerReader(lheInfoReader);

//--- open output file containing run:lumi:event numbers of events passing final event selection criteria
  std::ostream* selEventsFile = ( selEventsFileName_output != "" ) ? new std::ofstream(selEventsFileName_output.data(), std::ios::out) : 0;
  std::cout << "selEventsFileName_output = " << selEventsFileName_output << std::endl;

//--- declare MEM Ntuple
  MEMbbwwNtupleManager_singlelepton* mem_ntuple = new MEMbbwwNtupleManager_singlelepton("mem");
  mem_ntuple->makeTree(fs);
  mem_ntuple->initializeBranches();

  std::map<int, int> memEventCounter;
  
  int analyzedEntries = 0;
  int skippedEntries = 0;
  int selectedEntries = 0;
  double selectedEntries_weighted = 0.;
  int memEvents_total = 0;
  TH1* histogram_analyzedEntries = fs.make<TH1D>("analyzedEntries", "analyzedEntries", 1, -0.5, +0.5);
  TH1* histogram_selectedEntries = fs.make<TH1D>("selectedEntries", "selectedEntries", 1, -0.5, +0.5);
  cutFlowTableType cutFlowTable;
  const edm::ParameterSet cutFlowTableCfg = makeHistManager_cfg(
    process_string, Form("%s/sel/cutFlow", histogramDir.data()), era_string, central_or_shift
  );
  const std::vector<std::string> cuts = {
    "run:ls:event selection",
    ">= 1 fakeable lepton",
    "electron pT > 32 GeV / muon pT > 25 GeV",
    ">= 2 jets from H->bb",
    ">= 1 medium b-jet",
    ">= 1 jets from W->jj",
    "generator-level selection (1)",
    "generator-level selection (2)",
    ">= 1 memEvent (1)",
    ">= 1 memEvent (2)"
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

    double evtWeight = 1.;
    if ( apply_genWeight ) evtWeight *= boost::math::sign(eventInfo.genWeight);
    lheInfoReader->read();
    evtWeight *= lheInfoReader->getWeight_scale(kLHE_scale_central);
    evtWeight *= eventInfo.pileupWeight;

    if ( run_lumi_eventSelector && !(*run_lumi_eventSelector)(eventInfo) ) continue;
    cutFlowTable.update("run:ls:event selection");
    cutFlowHistManager->fillHistograms("run:ls:event selection", evtWeight);

    if ( run_lumi_eventSelector ) {
      std::cout << "processing Entry #" << inputTree->getCumulativeMaxEventCount() << ": " << eventInfo << std::endl;
      if ( inputTree -> isOpen() ) {
        std::cout << "input File = " << inputTree->getCurrentFileName() << std::endl;
      }
    }

//--- build collections of electrons and muons
//    resolve overlaps in order of priority: muon, electron,
    const std::vector<RecoMuon> muons = muonReader->read();
    const std::vector<const RecoMuon*> muon_ptrs = convert_to_ptrs(muons);
    const std::vector<const RecoMuon*> cleanedMuons = muon_ptrs; // CV: no cleaning needed for muons, as they have the highest priority in the overlap removal
    const std::vector<const RecoMuon*> preselMuons = preselMuonSelector(cleanedMuons, isHigherConePt);
    const std::vector<const RecoMuon*> fakeableMuons = lep_mva_wp == "hh_multilepton" ?
      fakeableMuonSelector_hh_multilepton(preselMuons, isHigherConePt) :
      fakeableMuonSelector_default(preselMuons, isHigherConePt)
    ;

    const std::vector<RecoElectron> electrons = electronReader->read();
    const std::vector<const RecoElectron*> electron_ptrs = convert_to_ptrs(electrons);
    const std::vector<const RecoElectron*> cleanedElectrons = electronCleaner(electron_ptrs, preselMuons);
    const std::vector<const RecoElectron*> preselElectrons = preselElectronSelector(cleanedElectrons, isHigherConePt);
    const std::vector<const RecoElectron*> preselElectronsUncleaned = preselElectronSelector(electron_ptrs, isHigherConePt);
    const std::vector<const RecoElectron*> fakeableElectrons = lep_mva_wp == "hh_multilepton" ?
      fakeableElectronSelector_hh_multilepton(preselElectrons, isHigherConePt) :
      fakeableElectronSelector_default(preselElectrons, isHigherConePt)
    ;

    const std::vector<const RecoLepton*> preselLeptonsFullUncleaned = mergeLeptonCollections(preselElectronsUncleaned, preselMuons, isHigherConePt);
    const std::vector<const RecoLepton*> fakeableLeptonsFull = mergeLeptonCollections(fakeableElectrons, fakeableMuons, isHigherConePt);
    const std::vector<const RecoLepton*> fakeableLeptons = pickFirstNobjects(fakeableLeptonsFull, 2);

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

    std::vector<RecoJetAK8> jets_ak8 = jetReaderAK8->read();
    std::vector<const RecoJetAK8*> jet_ptrs_ak8 = convert_to_ptrs(jets_ak8);
    const std::vector<const RecoJetAK8*> cleanedJetsAK8_wrtLeptons = jetCleanerAK8_dR08(jet_ptrs_ak8, fakeableLeptons);
    const std::vector<const RecoJetAK8*> selJetsAK8_Hbb = jetSelectorAK8_Hbb(cleanedJetsAK8_wrtLeptons, isHigherCSV_ak8);
    const std::vector<const RecoJet*> selJetsAK4_Hbb = jetSelectorAK4_wPileupJetId(cleanedJetsAK4_wrtLeptons, isHigherCSV);
    const std::vector<RecoJetAK8> jets_ak8LS = jetReaderAK8LS->read();
    const std::vector<const RecoJetAK8*> jet_ptrs_ak8LS = convert_to_ptrs(jets_ak8LS);

    // require at least two leptons passing fakeable selection criteria
    if ( !(fakeableLeptons.size() >= 1) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS fakeableLepton selection." << std::endl;
        printCollection("fakeableLeptons", fakeableLeptons);
      }
      continue;
    }
    cutFlowTable.update(">= 1 fakeable lepton", evtWeight);
    cutFlowHistManager->fillHistograms(">= 1 fakeable lepton", evtWeight);

    const RecoLepton* fakeableLepton = fakeableLeptons[0];
    //const Particle::LorentzVector& fakeableLeptonP4 = fakeableLepton->p4();
    //int fakeableLepton_lead = getLeptonType(fakeableLepton->pdgId());

    const double minPt_electron = 32.;
    const double minPt_muon = 25.;
    if ( !((fakeableLepton->is_electron() && fakeableLepton->cone_pt() > minPt_electron) || (fakeableLepton->is_muon() && fakeableLepton->cone_pt() > minPt_muon)) ) 
    {
      if ( run_lumi_eventSelector ) 
      {
        std::cout << "event " << eventInfo.str() << " FAILS lepton pT selection." << std::endl;
        if      ( fakeableLepton->is_electron() )
        { 
          std::cout << " (fakeableElectron pT = " << fakeableLepton->pt() << "," 
                    << " minPt_electron = " << minPt_electron << ")" << std::endl;
        }
        else if ( fakeableLepton->is_muon() )
        {
          std::cout << " (fakeableMuon pT = " << fakeableLepton->pt() << "," 
                    << " minPt_muon = " << minPt_muon << ")" << std::endl;
        }
        else assert(0);
      }
      continue;
    }
    cutFlowTable.update(Form("electron pT > %0.0f GeV / muon pT > %0.0f GeV", minPt_electron, minPt_muon), evtWeight);
    cutFlowHistManager->fillHistograms("electron pT > 32 GeV / muon pT > 25 GeV", evtWeight);

    std::vector<selJetsType_Hbb> selJetsT_Hbb = selectJets_Hbb(selJetsAK8_Hbb, selJetsAK4_Hbb);
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
    cutFlowTable.update(">= 2 jets from H->bb", evtWeight);
    cutFlowHistManager->fillHistograms(">= 2 jets from H->bb", evtWeight);

    if ( !(selJetAK8_Hbb || selBJetsAK4_medium.size() >= 1) )
    {
      if ( run_lumi_eventSelector ) 
      {
        std::cout << "event " << eventInfo.str() << " FAILS >= 1 medium b-jet selection\n";
      }
      continue;
    }
    cutFlowTable.update(">= 1 medium b-jet", evtWeight);
    cutFlowHistManager->fillHistograms(">= 1 medium b-jet", evtWeight);

    const RecoMEt met = metReader->read();
    const Particle::LorentzVector& metP4 = met.p4();

    std::vector<const RecoJetAK8*> selJetsAK8_Wjj;
    const RecoJetAK8* selJetAK8_Wjj = nullptr;
    const RecoJetBase* selJet1_Wjj = nullptr;
    const RecoJetBase* selJet2_Wjj = nullptr;
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
      if ( fakeableLepton && selJet1_Hbb && selJet2_Hbb )
      {
        jetSelectorAK8_Wjj.getSelector().set_lepton(fakeableLepton);
        std::vector<const RecoJetAK8*> preselJetsAK8_Wjj = jetSelectorAK8_Wjj(cleanedJetsAK8LS_wrtHbb, isHigherPt);
        for ( const RecoJetAK8* preselJetAK8_Wjj: preselJetsAK8_Wjj )
        {
          const RecoJetBase* subJet1_Wjj = preselJetAK8_Wjj->subJet1();
          const RecoJetBase* subJet2_Wjj = preselJetAK8_Wjj->subJet2();
          if ( !(subJet1_Wjj && subJet2_Wjj) ) continue;

          Particle::LorentzVector neutrinoP4_B2G_18_008 = comp_metP4_B2G_18_008(
            fakeableLepton->p4() + subJet1_Wjj->p4() + subJet2_Wjj->p4(), 
            metP4.px(), metP4.py(),
            mem::higgsBosonMass);
          Particle::LorentzVector WjjP4 = subJet1_Wjj->p4() + subJet2_Wjj->p4();
          Particle::LorentzVector WlnuP4 = fakeableLepton->p4() + neutrinoP4_B2G_18_008;

          // apply cut on mD variable, defined by Eq.(3) in AN-2018/058 (v4)
          double mD = deltaR(WjjP4, WlnuP4)*0.5*(WjjP4 + WlnuP4).pt();
          if ( !(mD <= mem::higgsBosonMass) ) continue;

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
      std::sort(selJetsAK8_Wjj.begin(), selJetsAK8_Wjj.end(), isHigherPt);
      if ( selJetsAK8_Wjj.size() >= 1 ) 
      {
        selJetAK8_Wjj = selJetsAK8_Wjj[0];
        selJet1_Wjj = selJetAK8_Wjj->subJet1();
        selJet2_Wjj = selJetAK8_Wjj->subJet2();
      }
      std::vector<const RecoJet*> cleanedJetsAK4_wrtHbb;
      if ( selJetAK8_Hbb )
      {
        cleanedJetsAK4_wrtHbb = jetCleanerAK4_dR12(selJetsAK4, std::vector<const RecoJetBase*>({ selJetAK8_Hbb }));
      } 
      else 
      {
        std::vector<const RecoJetBase*> overlaps;
        if ( selJet1_Hbb ) { overlaps.push_back(selJet1_Hbb); }
        if ( selJet2_Hbb ) { overlaps.push_back(selJet2_Hbb); }
        cleanedJetsAK4_wrtHbb = jetCleanerAK4_dR04(selJetsAK4, overlaps);
        if ( cleanedJetsAK4_wrtHbb.size() >= 1 ) selJet1_Wjj = cleanedJetsAK4_wrtHbb[0];
        if ( cleanedJetsAK4_wrtHbb.size() >= 2 ) selJet2_Wjj = cleanedJetsAK4_wrtHbb[1];
      }
    }
    if ( !(selJet1_Wjj || selJet2_Wjj) )
    {
      if ( run_lumi_eventSelector )
      {
        std::cout << "event " << eventInfo.str() << " FAILS >= 1 jets from W->jj selection\n";
      }
      continue;
    }
    cutFlowTable.update(">= 1 jets from W->jj", evtWeight);
    cutFlowHistManager->fillHistograms(">= 1 jets from W->jj", evtWeight);

//--- build collections of generator level particles
    std::vector<GenLepton> genLeptons;
    if ( genLeptonReader ) {
      genLeptons = genLeptonReader->read();
    }
    std::vector<GenParticle> genNeutrinos;
    if ( genNeutrinoReader ) {
      genNeutrinos = genNeutrinoReader->read();
    }
    std::vector<GenJet> genJets;
    if ( genJetReader ) {
      genJets = genJetReader->read();
    }

    std::vector<GenParticle> genParticlesFromHiggs;
    std::vector<GenParticle> genWBosons;
    std::vector<GenParticle> genWJets;
    if ( isSignal ) {
      genParticlesFromHiggs = genParticleFromHiggsReader->read();
      genWBosons = genWBosonReader->read();
      genWJets = genWJetReader->read();
      if ( isDEBUG ) {
	printCollection("genParticlesFromHiggs", genParticlesFromHiggs);
        printCollection("genWBosons", genWBosons);
        printCollection("genWJets", genWJets);        
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
    std::vector<GenParticle> genWJetsFromTop;
    if ( !isSignal ) {
      genLeptonsFromTop = genLeptonFromTopReader->read();
      genNeutrinosFromTop = genNeutrinoFromTopReader->read();
      genBQuarksFromTop = genBQuarksFromTopReader->read();
      genWJetsFromTop = genWJetsFromTopReader->read();
      if ( isDEBUG ) {
	printCollection("genLeptonsFromTop", genLeptonsFromTop);
	printCollection("genNeutrinosFromTop", genNeutrinosFromTop);
	printCollection("genBQuarksFromTop", genBQuarksFromTop);	
        printCollection("genWJetsFromTop", genWJetsFromTop);
      }
      if ( !(genLeptonsFromTop.size() == 2 && genNeutrinosFromTop.size() == 2 && genBQuarksFromTop.size() == 2 && genWJetsFromTop.size() == 2) ) {
	if ( run_lumi_eventSelector ) {
	  std::cout << "event " << eventInfo.str() << " FAILS generator-level selection." << std::endl;
	  std::cout << "#genLeptonsFromTop = " << genLeptonsFromTop.size() << std::endl;
	  std::cout << "#genNeutrinosFromTop = " << genNeutrinosFromTop.size() << std::endl;
	  std::cout << "#genBQuarksFromTop = " << genBQuarksFromTop.size() << std::endl;
          std::cout << "#genWJetsFromTop = " << genWJetsFromTop.size() << std::endl;
	}
	continue;
      }
    }
    cutFlowTable.update("generator-level selection (1)", evtWeight);
    cutFlowHistManager->fillHistograms("generator-level selection (1)", evtWeight);

//--- select leptons, jets and b-jets from H->WW->lnuqq and H->bb decays (signal)
//    and from tt->bWbW->blnu bqq decays (background)
    std::vector<GenLepton> genLeptonsForMatching;
    std::vector<GenJet> genBJetsForMatching;
    std::vector<GenJet> genWJetsForMatching;
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
        const GenParticle* genWJet1 = nullptr;
        const GenParticle* genWJet2 = nullptr;
	std::pair<const GenLepton*, const GenParticle*> genLepton_and_NeutrinoFromWBosonPlus =
          findGenLepton_and_NeutrinoFromWBoson(*genWBosonPlus, genLeptons, genNeutrinos);
	const GenLepton* genLeptonPlus = genLepton_and_NeutrinoFromWBosonPlus.first;
	const GenParticle* genNeutrino = genLepton_and_NeutrinoFromWBosonPlus.second;
        if ( genLeptonPlus && genNeutrino )
        {
          std::vector<const GenParticle*> genJetsFromWBosonMinus =
            findGenJetsFromWBoson(*genWBosonMinus, genWJets);
          if ( genJetsFromWBosonMinus.size() == 2 )
          {
            genWJet1 = genJetsFromWBosonMinus[0];
	    genWJet2 = genJetsFromWBosonMinus[1];
          }
        }
	std::pair<const GenLepton*, const GenParticle*> genLepton_and_NeutrinoFromWBosonMinus =
          findGenLepton_and_NeutrinoFromWBoson(*genWBosonMinus, genLeptons, genNeutrinos);
	const GenLepton* genLeptonMinus = genLepton_and_NeutrinoFromWBosonMinus.first;
	const GenParticle* genAntiNeutrino = genLepton_and_NeutrinoFromWBosonMinus.second;
        if ( genLeptonMinus && genAntiNeutrino )
        {
          std::vector<const GenParticle*> genJetsFromWBosonPlus =
            findGenJetsFromWBoson(*genWBosonPlus, genWJets);
          if ( genJetsFromWBosonPlus.size() == 2 )
          {
            genWJet1 = genJetsFromWBosonPlus[0];
	    genWJet2 = genJetsFromWBosonPlus[1];
          }
        }
        if ( genLeptonPlus && genNeutrino && genLeptonMinus && genAntiNeutrino) continue;
        if ( !(genWJet1 && genWJet2) ) continue;
        if ( genLeptonPlus  ) genLeptonsForMatching.push_back(*genLeptonPlus);
        if ( genLeptonMinus ) genLeptonsForMatching.push_back(*genLeptonMinus); 
        genWJetsForMatching.push_back(GenJet(
          genWJet1->pt(), genWJet1->eta(), genWJet1->phi(), genWJet1->mass(), genWJet1->pdgId()));
        genWJetsForMatching.push_back(GenJet(
          genWJet2->pt(), genWJet2->eta(), genWJet2->phi(), genWJet2->mass(), genWJet2->pdgId()));
        if ( genNeutrino )
        {
	  genMEtPx += genNeutrino->p4().px();
	  genMEtPy += genNeutrino->p4().py();
        }
        if ( genAntiNeutrino )
        {
	  genMEtPx += genAntiNeutrino->p4().px();
	  genMEtPy += genAntiNeutrino->p4().py();
        }
      }
    } else {
      genLeptonsForMatching = genLeptonsFromTop;
      for ( std::vector<GenParticle>::const_iterator genWJet = genWJetsFromTop.begin();
	    genWJet != genWJetsFromTop.end(); ++genWJet ) {
	genWJetsForMatching.push_back(GenJet(
          genWJet->pt(), genWJet->eta(), genWJet->phi(), genWJet->mass(), genWJet->pdgId()));
      }
      assert(genNeutrinosFromTop.size() == 1);
      genMEtPx = genNeutrinosFromTop[0].p4().px();
      genMEtPy = genNeutrinosFromTop[0].p4().py();
      for ( std::vector<GenParticle>::const_iterator genBQuark = genBQuarksFromTop.begin();
	    genBQuark != genBQuarksFromTop.end(); ++genBQuark ) {
	genBJetsForMatching.push_back(GenJet(
          genBQuark->pt(), genBQuark->eta(), genBQuark->phi(), mem::bottomQuarkMass, genBQuark->pdgId()));
      }
    }
    if ( !(genLeptonsForMatching.size() == 1 && genBJetsForMatching.size() == 2 && genWJetsForMatching.size() == 2) ) {
      if ( run_lumi_eventSelector ) {
	std::cout << "event " << eventInfo.str() << " FAILS generator-level selection." << std::endl;
	std::cout << "#genLeptonsForMatching = " << genLeptonsForMatching.size() << std::endl;
	std::cout << "#genBJetsForMatching = " << genBJetsForMatching.size() << std::endl;
        std::cout << "#genWJetsForMatching = " << genWJetsForMatching.size() << std::endl;
      }
      continue;
    }
    cutFlowTable.update("generator-level selection (2)", evtWeight);
    cutFlowHistManager->fillHistograms("generator-level selection (2)", evtWeight);

    std::vector<const GenLepton*> genLeptonsForMatching_ptrs = convert_to_ptrs(genLeptonsForMatching);
    std::vector<const GenJet*> genBJetsForMatching_ptrs = convert_to_ptrs(genBJetsForMatching);
    std::vector<const GenJet*> genWJetsForMatching_ptrs = convert_to_ptrs(genWJetsForMatching);
    std::vector<const GenJet*> genJets_ptrs = convert_to_ptrs(genJets);

//--- build collections of "MEM events":
//    permutations of reconstructed leptons and jets, 
//    with different associations between reconstructed jets and quarks from H->bb and W->jj decays    
    std::vector<mem::MeasuredParticle> measuredLeptons = convert_to_MeasuredParticles(fakeableLeptons);
    std::vector<const mem::MeasuredParticle*> measuredLeptons_ptrs = convert_to_ptrs(measuredLeptons);

    std::vector<mem::MeasuredParticle> measuredJets_AK4 = convert_to_MeasuredParticles(selJetsAK4, true);
    std::vector<const mem::MeasuredParticle*> measuredJets_AK4_ptrs = convert_to_ptrs(measuredJets_AK4);
    std::vector<std::pair<mem::MeasuredParticle, mem::MeasuredParticle>> measuredJets_AK8_Hbb = convert_to_MeasuredParticles(selJetsAK8_Hbb, true);
    std::vector<const std::pair<mem::MeasuredParticle, mem::MeasuredParticle>*> measuredJets_AK8_Hbb_ptrs = convert_to_ptrs(measuredJets_AK8_Hbb);
    std::vector<std::pair<mem::MeasuredParticle, mem::MeasuredParticle>> measuredJets_AK8_Wjj = convert_to_MeasuredParticles(selJetsAK8_Wjj, true);
    std::vector<const std::pair<mem::MeasuredParticle, mem::MeasuredParticle>*> measuredJets_AK8_Wjj_ptrs = convert_to_ptrs(measuredJets_AK8_Wjj);

    double measuredMEtPx = met.pt()*cos(met.phi());
    double measuredMEtPy = met.pt()*sin(met.phi());
    const TMatrixD& measuredMEtCov = met.cov();

    std::vector<MEMEvent_singlelepton> memEvents_boosted = buildMEMEvents_singlelepton_boosted(
      measuredJets_AK8_Hbb_ptrs, measuredJets_AK8_Wjj_ptrs, 
      measuredLeptons_ptrs, 
      measuredMEtPx, measuredMEtPy, measuredMEtCov);
    std::vector<MEMEvent_singlelepton> memEvents_semiboosted = buildMEMEvents_singlelepton_semiboosted(
      measuredJets_AK8_Hbb_ptrs, measuredJets_AK4_ptrs, 2, 
      measuredLeptons_ptrs, 
      measuredMEtPx, measuredMEtPy, measuredMEtCov);
    std::vector<MEMEvent_singlelepton> memEvents_resolved = buildMEMEvents_singlelepton_resolved(
      measuredJets_AK4_ptrs, 2, 2,
      measuredLeptons_ptrs, 
      measuredMEtPx, measuredMEtPy, measuredMEtCov);
    std::vector<MEMEvent_singlelepton> memEvents_resolved_missingBJet = buildMEMEvents_singlelepton_resolved(
      measuredJets_AK4_ptrs, 1, 2, 
      measuredLeptons_ptrs, 
      measuredMEtPx, measuredMEtPy, measuredMEtCov);
    std::vector<MEMEvent_singlelepton> memEvents_resolved_missingWJet = buildMEMEvents_singlelepton_resolved(
      measuredJets_AK4_ptrs, 2, 1, 
      measuredLeptons_ptrs, 
      measuredMEtPx, measuredMEtPy, measuredMEtCov);
    std::vector<MEMEvent_singlelepton> memEvents_resolved_missingBnWJet = buildMEMEvents_singlelepton_resolved(
      measuredJets_AK4_ptrs, 1, 1, 
      measuredLeptons_ptrs, 
      measuredMEtPx, measuredMEtPy, measuredMEtCov);
    std::vector<MEMEvent_singlelepton> memEvents;
    memEvents.insert(memEvents.end(), memEvents_boosted.begin(), memEvents_boosted.end());
    memEvents.insert(memEvents.end(), memEvents_semiboosted.begin(), memEvents_semiboosted.end());
    memEvents.insert(memEvents.end(), memEvents_resolved.begin(), memEvents_resolved.end());
    memEvents.insert(memEvents.end(), memEvents_resolved_missingBJet.begin(), memEvents_resolved_missingBJet.end());
    memEvents.insert(memEvents.end(), memEvents_resolved_missingWJet.begin(), memEvents_resolved_missingWJet.end());
    memEvents.insert(memEvents.end(), memEvents_resolved_missingBnWJet.begin(), memEvents_resolved_missingBnWJet.end());
    addGenMatches_singlelepton(memEvents, genBJetsForMatching_ptrs, genWJetsForMatching_ptrs, genLeptonsForMatching_ptrs, genMEtPx, genMEtPy);
    //std::cout << "#memEvents:" << std::endl;
    //std::cout << " boosted = " << memEvents_boosted.size() << std::endl;
    //std::cout << " resolved = " << memEvents_resolved.size() << "," 
    //          << " missingBJet = " << memEvents_resolved_missingBJet.size() << ","
    //          << " missingWJet = " << memEvents_resolved_missingWJet.size() << ","
    //          << " missingB&WJet = " << memEvents_resolved_missingBnWJet.size() << std::endl;
    //std::cout << "total = " << memEvents.size() << std::endl;

    if ( !(memEvents.size() > 0) ) {
      if ( run_lumi_eventSelector ) {
	std::cout << "event " << eventInfo.str() << " FAILS memEvent selection." << std::endl;
      }
      continue;
    }
    cutFlowTable.update(">= 1 memEvent (1)", evtWeight);
    cutFlowHistManager->fillHistograms(">= 1 memEvent (1)", evtWeight);

    std::map<int, std::vector<const MEMEvent_singlelepton*>> memEventMap = buildMEMEventMap_singlelepton(memEvents);

    // CV: Define "physical" values of i that are to be checke.
    //     Skip values of i corresponding to missing leptons or to missing first jet (from W->jj) or first b-jet (from H->bb)
    //     and also values of i that have "reconstructed" as well as "missing" bit set for any lepton, jet or b-jet.
    std::set<int> i_values_to_check = {  
      512+128+32+8+2, 512+128+32+8+1, 512+128+32+8+0,
      512+128+32+4+2, 512+128+32+4+1, 512+128+32+4+0,
      512+128+16+8+2, 512+128+16+8+1, 512+128+16+8+0,
      512+128+16+4+2, 512+128+16+4+1, 512+128+16+4+0,
      512+128+ 0+8+2, 512+128+ 0+8+1, 512+128+ 0+8+0,
      512+128+ 0+4+2, 512+128+ 0+4+1, 512+128+ 0+4+0,
      512+ 64+32+8+2, 512+ 64+32+8+1, 512+ 64+32+8+0,
      512+ 64+32+4+2, 512+ 64+32+4+1, 512+ 64+32+4+0,
      512+ 64+16+8+2, 512+ 64+16+8+1, 512+ 64+16+8+0,
      512+ 64+16+4+2, 512+ 64+16+4+1, 512+ 64+16+4+0,
      512+ 64+ 0+8+2, 512+ 64+ 0+8+1, 512+ 64+ 0+8+0,
      512+ 64+ 0+4+2, 512+ 64+ 0+4+1, 512+ 64+ 0+4+0,
      256+128+32+8+2, 256+128+32+8+1, 256+128+32+8+0,
      256+128+32+4+2, 256+128+32+4+1, 256+128+32+4+0,
      256+128+16+8+2, 256+128+16+8+1, 256+128+16+8+0,
      256+128+16+4+2, 256+128+16+4+1, 256+128+16+4+0,
      256+128+ 0+8+2, 256+128+ 0+8+1, 256+128+ 0+8+0,
      256+128+ 0+4+2, 256+128+ 0+4+1, 256+128+ 0+4+0,
      256+ 64+32+8+2, 256+ 64+32+8+1, 256+ 64+32+8+0,
      256+ 64+32+4+2, 256+ 64+32+4+1, 256+ 64+32+4+0,
      256+ 64+16+8+2, 256+ 64+16+8+1, 256+ 64+16+8+0,
      256+ 64+16+4+2, 256+ 64+16+4+1, 256+ 64+16+4+0,
      256+ 64+ 0+8+2, 256+ 64+ 0+8+1, 256+ 64+ 0+8+0,
      256+ 64+ 0+4+2, 256+ 64+ 0+4+1, 256+ 64+ 0+4+0
    };

    std::map<int, int> memEventCounter_update = memEventCounter;
    int min_memEventCounter_update = -1;
    for ( int i = 0; i < (1 << 8); ++i ) {
      if ( memEventMap.find(i) != memEventMap.end() ) {
        memEventCounter_update[i] += memEventMap[i].size();
      }
      // CV: skip values of i corresponding to "unphysical" values of i
      if ( i_values_to_check.find(i) == i_values_to_check.end() ) continue;
      // CV: skip values of i that occur very unfrequently
      if ( memEventCounter_update[i] == 0 ) continue;
      if ( min_memEventCounter_update == -1 || memEventCounter_update[i] < min_memEventCounter_update ) {
        min_memEventCounter_update = memEventCounter_update[i];
      }
    }
    //std::cout << "min_memEventCounter_update = " << min_memEventCounter_update << std::endl;    

    //---------------------------------------------------------------------------
    // CV: Skip running matrix element method (MEM) computation for the first 'skipSelEvents' events.
    //     This feature allows to process the HH signal samples in chunks of 'maxSelEvents' events per job.
    ++skippedEntries;
    if ( skippedEntries < skipSelEvents ) continue;
    //---------------------------------------------------------------------------

    int memEvents_currentEvent = 0;
    for ( std::map<int, std::vector<const MEMEvent_singlelepton*>>::const_iterator memEventMap_iter = memEventMap.begin();
          memEventMap_iter != memEventMap.end(); ++memEventMap_iter ) {
      for ( std::vector<const MEMEvent_singlelepton*>::const_iterator memEvent = memEventMap_iter->second.begin();
            memEvent != memEventMap_iter->second.end(); ++memEvent ) {
        // CV: For a balanced BDT/LBN regression training, we aim to have an equal number of MEM events for each MEM event type i.
        //     This objective is achieved by adding MEM events to the Ntuple with a probability of min_memEventCounter_update/(double)memEventMap[i].size().
        //     To save computing time, only run MEM computation for those MEM events that are added to the Ntuple.
        const int margin = 10;
        const double p = (min_memEventCounter_update + margin)/(double)memEventCounter_update[memEventMap_iter->first];
        double u = rnd.Rndm();
        if ( u > p ) continue;

        std::vector<mem::MeasuredParticle> memMeasuredParticles;
        if ( (*memEvent)->measuredBJet1_  ) memMeasuredParticles.push_back(*(*memEvent)->measuredBJet1_);
        if ( (*memEvent)->measuredBJet2_  ) memMeasuredParticles.push_back(*(*memEvent)->measuredBJet2_);
        if ( (*memEvent)->measuredLepton_ ) memMeasuredParticles.push_back(*(*memEvent)->measuredLepton_);
        if ( (*memEvent)->measuredWJet1_  ) memMeasuredParticles.push_back(*(*memEvent)->measuredWJet1_);
        if ( (*memEvent)->measuredWJet2_  ) memMeasuredParticles.push_back(*(*memEvent)->measuredWJet2_);

        const double sqrtS = 13.e+3;
        const std::string pdfName = "MSTW2008lo68cl";
        const std::string madgraphFileName_signal     = "hhAnalysis/bbwwMEM/data/param_hh_SM.dat";
        const std::string madgraphFileName_background = "hhAnalysis/bbwwMEM/data/param_ttbar.dat";
        const bool applyOnshellWmassConstraint_signal = false;
        const int memAlgo_verbosity = 0;
        //const int maxObjFunctionCalls_signal = 2500;
        //const int maxObjFunctionCalls_background = 25000;
        const int maxObjFunctionCalls_signal = 1000;
        const int maxObjFunctionCalls_background = 10000;

        clock.Reset();
        clock.Start("memAlgo");
        MEMbbwwAlgoSingleLepton memAlgo(sqrtS, pdfName, findFile(madgraphFileName_signal), findFile(madgraphFileName_background), memAlgo_verbosity);
        memAlgo.applyOnshellWmassConstraint_signal(applyOnshellWmassConstraint_signal);
        memAlgo.setIntMode(MEMbbwwAlgoSingleLepton::kVAMP);
        memAlgo.setMaxObjFunctionCalls_signal(maxObjFunctionCalls_signal);
        memAlgo.setMaxObjFunctionCalls_background(maxObjFunctionCalls_background);
        memAlgo.integrate(memMeasuredParticles, (*memEvent)->measuredMEtPx_, (*memEvent)->measuredMEtPy_, (*memEvent)->measuredMEtCov_);
        MEMbbwwResultSingleLepton memResult = memAlgo.getResult();
        clock.Stop("memAlgo");
 
        double memCpuTime = clock.GetCpuTime("memAlgo");
        if ( isDEBUG ) {
          std::cout << "MEM:"
	            << " probability for signal hypothesis = " << memResult.getProb_signal() 
                    << " +/- " << memResult.getProbErr_signal() << ","
	            << " probability for background hypothesis = " << memResult.getProb_background() 
                    << " +/- " << memResult.getProbErr_background() << " " 
   	            << "--> likelihood ratio = " << memResult.getLikelihoodRatio() 
                    << " +/- " << memResult.getLikelihoodRatioErr() 
	            << " (CPU time = " << memCpuTime << ")" << std::endl;
        }

        (const_cast<MEMEvent_singlelepton*>(*memEvent))->memResult_ = memResult;
        (const_cast<MEMEvent_singlelepton*>(*memEvent))->memCpuTime_ = memCpuTime;

        mem_ntuple->read(eventInfo, (*memEvent)->key_);
        mem_ntuple->read(memResult, memCpuTime);
        mem_ntuple->read(memMeasuredParticles, (*memEvent)->measuredMEtPx_, (*memEvent)->measuredMEtPy_, (*memEvent)->measuredMEtCov_);
        mem_ntuple->read(genBJetsForMatching_ptrs, genWJetsForMatching_ptrs, genLeptonsForMatching_ptrs[0], (*memEvent)->genMEtPx_, (*memEvent)->genMEtPy_);
        mem_ntuple->fill();

        ++memEventCounter[memEventMap_iter->first];
        ++memEvents_currentEvent;
      }
    }

    memEvents_total += memEvents_currentEvent;

    if ( !(memEvents_currentEvent > 0) ) {
      if ( run_lumi_eventSelector ) {
	std::cout << "event " << eventInfo.str() << " FAILS memEvent selection." << std::endl;
      }
      continue;
    }
    cutFlowTable.update(">= 1 memEvent (2)", evtWeight);
    cutFlowHistManager->fillHistograms(">= 1 memEvent (2)", evtWeight);

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

  std::cout << "num. MEM events added to Ntuple = " << memEvents_total << std::endl;
  std::cout << std::endl;

  delete run_lumi_eventSelector;

  delete selEventsFile;

  delete muonReader;
  delete electronReader;
  delete jetReaderAK4;
  delete jetReaderAK8;  
  delete metReader;
  delete genLeptonReader;
  delete genNeutrinoReader;
  delete genJetReader;
  delete genParticleFromHiggsReader;
  delete genWBosonReader;
  delete genWJetReader;
  delete genLeptonFromTopReader;
  delete genNeutrinoFromTopReader;
  delete genBQuarksFromTopReader;
  delete genWJetsFromTopReader;
  delete lheInfoReader;

  delete mem_ntuple;

  delete inputTree;

  clock.Show("produceMEMNtuple_hh_bb1l");

  return EXIT_SUCCESS;
}

