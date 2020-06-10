#include "FWCore/ParameterSet/interface/ParameterSet.h" // edm::ParameterSet
#include "FWCore/PythonParameterSet/interface/MakeParameterSets.h" // edm::readPSetsFrom()
#include "FWCore/Utilities/interface/Exception.h" // cms::Exception
#include "PhysicsTools/FWLite/interface/TFileService.h" // fwlite::TFileService
#include "DataFormats/FWLite/interface/InputSource.h" // fwlite::InputSource
#include "DataFormats/FWLite/interface/OutputFiles.h" // fwlite::OutputFiles
#include "DataFormats/Math/interface/LorentzVector.h" // math::PtEtaPhiMLorentzVector
#include "DataFormats/Math/interface/deltaR.h" // deltaR
#include "DataFormats/Math/interface/deltaPhi.h" // deltaPhi

#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronReader.h" // RecoElectronReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonReader.h" // RecoMuonReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetReader.h" // RecoJetReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetReaderAK8.h" // RecoJetReaderAK8
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEtReader.h" // RecoMEtReader, RecoMEt
#include "tthAnalysis/HiggsToTauTau/interface/EventInfoReader.h" // EventInfoReader, EventInfo
#include "tthAnalysis/HiggsToTauTau/interface/GenLeptonReader.h" // GenLeptonReader
#include "tthAnalysis/HiggsToTauTau/interface/GenJetReader.h" // GenJetReader
#include "tthAnalysis/HiggsToTauTau/interface/GenParticleReader.h" // GenParticleReader
#include "tthAnalysis/HiggsToTauTau/interface/LHEInfoReader.h" // LHEInfoReader
#include "tthAnalysis/HiggsToTauTau/interface/convert_to_ptrs.h" // convert_to_ptrs
#include "tthAnalysis/HiggsToTauTau/interface/ParticleCollectionCleaner.h" // RecoElectronCollectionCleaner, RecoMuonCollectionCleaner, RecoJetCollectionCleaner
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronCollectionSelectorLoose.h" // RecoElectronCollectionSelectorLoose
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronCollectionSelectorFakeable.h" // RecoElectronCollectionSelectorFakeable
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronCollectionSelectorTight.h" // RecoElectronCollectionSelectorTight
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonCollectionSelectorLoose.h" // RecoMuonCollectionSelectorLoose
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonCollectionSelectorFakeable.h" // RecoMuonCollectionSelectorFakeable
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonCollectionSelectorTight.h" // RecoMuonCollectionSelectorTight
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetCollectionSelector.h" // RecoJetCollectionSelector
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetCollectionSelectorBtag.h" // RecoJetCollectionSelectorBtagLoose, RecoJetCollectionSelectorBtagMedium
#include "tthAnalysis/HiggsToTauTau/interface/RunLumiEventSelector.h" // RunLumiEventSelector
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // selectObjects(), get_selection(), get_era(), kLoose, kFakeable, kTight
#include "tthAnalysis/HiggsToTauTau/interface/mvaInputVariables.h" // comp_MT_met
#include "tthAnalysis/HiggsToTauTau/interface/sysUncertOptions.h" // k*_central
#include "tthAnalysis/HiggsToTauTau/interface/memAuxFunctions.h" // get_memObjectBranchName(), get_memPermutationBranchName()
#include "tthAnalysis/HiggsToTauTau/interface/cutFlowTable.h" // cutFlowTableType
#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // createSubdirectory_recursively()
#include "tthAnalysis/HiggsToTauTau/interface/NtupleFillerBDT.h" // NtupleFillerBDT
#include "tthAnalysis/HiggsToTauTau/interface/TTreeWrapper.h" // TTreeWrapper

#include "hhAnalysis/multilepton/interface/EvtWeightRecorderHH.h" // EvtWeightRecorderHH

#include "hhAnalysis/bbww/interface/RecoJetCollectionSelectorAK8_hh_bbWW_Hbb.h" // RecoJetSelectorAK8_hh_bbWW_Hbb
#include "hhAnalysis/bbww/interface/jetSelectionAuxFunctions.h" // selectJets_Hbb, countBJetsJets_Hbb, selectJets_Wjj
#include "hhAnalysis/bbww/interface/GenParticleMatcherFromHiggs.h" // GenParticleMatcherFromHiggs
#include "hhAnalysis/bbww/interface/GenParticleMatcherFromTop.h" // GenParticleMatcherFromTop
#include "hhAnalysis/bbww/interface/comp_metP4_B2G_18_008.h" // comp_metP4_B2G_18_008

#include <TChain.h> // TChain
#include <TTree.h> // TTree
#include <TBenchmark.h> // TBenchmark
#include <TString.h> // TString, Form
#include <TError.h> // gErrorAbortLevel, kError
#include <TLorentzVector.h> // TLorentzVector

#include <boost/algorithm/string/predicate.hpp> // boost::starts_with()
#include <boost/math/special_functions/sign.hpp> // boost::math::sign()

#include <iostream> // std::cerr, std::fixed
#include <cstdlib> // EXIT_SUCCESS, EXIT_FAILURE
#include <assert.h> // assert

typedef std::vector<std::string> vstring;

const double higgsBosonMass = 125.;
const double topMass = 172.9; // CV: taken from http://pdg.lbl.gov/2019/listings/rpp2019-list-t-quark.pdf ("OUR AVERAGE")

bool 
isGenMatched(const RecoJetBase* recJet, const std::vector<GenJet>& genJets, double dRmax = 0.3)
{
  for ( std::vector<GenJet>::const_iterator genJet = genJets.begin();
	genJet != genJets.end(); ++genJet ) {
    double dR = deltaR(recJet->p4(), genJet->p4());
    if ( dR < dRmax ) return true;
  }
  return false;
}

double
compCosTheta(const Particle::LorentzVector& recWJet1, const Particle::LorentzVector& recWJet2)
{
  TLorentzVector PWj1, PWj2;
  PWj1.SetPtEtaPhiM(recWJet1.pt(), recWJet1.eta(), recWJet1.phi(), recWJet1.mass());
  PWj2.SetPtEtaPhiM(recWJet2.pt(), recWJet2.eta(), recWJet2.phi(), recWJet2.mass());
  TLorentzVector PW = PWj1 + PWj2;

  TLorentzVector PWj1boost, PWj2boost;
  PWj1boost = PWj1;
  PWj1boost.Boost(-PW.BoostVector());
  PWj2boost = PWj2;
  PWj2boost.Boost(-PW.BoostVector());

  double cosTheta = -100;
  if ( PWj1.Pt() > PWj2.Pt() )
  {
    cosTheta = PWj1boost.CosTheta();
  }
  else
  {
    cosTheta = PWj2boost.CosTheta();
  }
  return cosTheta;
}

bool
isWithinRoundingErrors_abs(double x1, double x2, double epsilon = 2.e-1)
{
  if ( std::fabs(x1 - x2) < epsilon ) return true;
  else return false;	
}

bool
isWithinRoundingErrors_rel(double x1, double x2, double epsilon = 5.e-2)
{
  if ( std::fabs(x1 - x2) < epsilon*(std::fabs(x1) + std::fabs(x2)) ) return true;
  else return false;	
}

/**
 * @brief Produce Ntuple for training a BDT to identify pairs of jets originating from W->jj decays
 */
int main(int argc,
         char ** argv)
{
//--- throw an exception in case ROOT encounters an error
  gErrorAbortLevel = kError;

//--- parse command-line arguments
  if ( argc < 2 )
  {
    std::cout << "Usage: " << argv[0] << " [parameters.py]\n";
    return EXIT_FAILURE;
  }

  std::cout << "<produceNtuple_HadWJetBDT>:\n";

//--- keep track of time it takes the macro to execute
  TBenchmark clock;
  clock.Start(argv[0]);

//--- read python configuration parameters
  if ( !edm::readPSetsFrom(argv[1])->existsAs<edm::ParameterSet>("process") )
    throw cms::Exception(argv[0])
      << "No ParameterSet 'process' found in configuration file = " << argv[1] << " !!\n";

  const edm::ParameterSet cfg               = edm::readPSetsFrom(argv[1])->getParameter<edm::ParameterSet>("process");
  const edm::ParameterSet cfg_analyze       = cfg.getParameter<edm::ParameterSet>("analyze_hadWTagger");
  const std::string treeName                = cfg_analyze.getParameter<std::string>("treeName");
  const std::string process_string          = cfg_analyze.getParameter<std::string>("process");
  const std::string selEventsFileName_input = cfg_analyze.getParameter<std::string>("selEventsFileName_input");
  const bool isDEBUG                        = cfg_analyze.getParameter<bool>("isDEBUG");

  const bool isMC                           = cfg_analyze.getParameter<bool>("isMC");
  bool isMC_HH = isMC && process_string.find("hh_bbvv")!= std::string::npos;
  bool isMC_TT = isMC && process_string.find("TT")     != std::string::npos;
  bool hasLHE                               = cfg_analyze.getParameter<bool>("hasLHE");
  std::string central_or_shift              = "central";
  edm::VParameterSet lumiScale              = cfg_analyze.getParameter<edm::VParameterSet>("lumiScale");
  bool apply_genWeight                      = cfg_analyze.getParameter<bool>("apply_genWeight");

  const std::string branchName_electrons    = cfg_analyze.getParameter<std::string>("branchName_electrons");
  const std::string branchName_muons        = cfg_analyze.getParameter<std::string>("branchName_muons");
  const std::string branchName_jets_ak4     = cfg_analyze.getParameter<std::string>("branchName_jets_ak4");
  const std::string branchName_jets_ak8     = cfg_analyze.getParameter<std::string>("branchName_jets_ak8");
  const std::string branchName_subjets_ak8  = cfg_analyze.getParameter<std::string>("branchName_subjets_ak8");
  const std::string branchName_met          = cfg_analyze.getParameter<std::string>("branchName_met");

  edm::ParameterSet cfg_branchNames_genParticles = cfg_analyze.getParameter<edm::ParameterSet>("branchNames_genParticles");
  // branches specific to HH->bbWW signal events
  std::string branchName_genLeptons = cfg_branchNames_genParticles.getParameter<std::string>("branchName_genLeptons");
  std::string branchName_genNeutrinos = cfg_branchNames_genParticles.getParameter<std::string>("branchName_genNeutrinos");
  std::string branchName_genParticlesFromHiggs = cfg_branchNames_genParticles.getParameter<std::string>("branchName_genParticlesFromHiggs");
  std::string branchName_genWJets = cfg_branchNames_genParticles.getParameter<std::string>("branchName_genWJets");
  // branches specific to tt+jets background events   
  std::string branchName_genLeptonsFromTop = cfg_branchNames_genParticles.getParameter<std::string>("branchName_genLeptonsFromTop");
  std::string branchName_genNeutrinosFromTop = cfg_branchNames_genParticles.getParameter<std::string>("branchName_genNeutrinosFromTop");
  std::string branchName_genBJetsFromTop = cfg_branchNames_genParticles.getParameter<std::string>("branchName_genBJetsFromTop");
  std::string branchName_genWJetsFromTop = cfg_branchNames_genParticles.getParameter<std::string>("branchName_genWJetsFromTop");  

  GenParticleMatcherFromHiggs genParticleMatcherFromHiggs;
  GenParticleMatcherFromTop genParticleMatcherFromTop;

  bool jetCleaningByIndex = cfg_analyze.getParameter<bool>("jetCleaningByIndex");

  std::string histogramDir = cfg_analyze.getParameter<std::string>("histogramDir");	

  const std::string era_string = cfg_analyze.getParameter<std::string>("era");
  const Era era = get_era(era_string);

  const std::string leptonSelection_string = cfg_analyze.getParameter<std::string>("leptonSelection");
  const int leptonSelection = get_selection(leptonSelection_string);

  std::cout << "selEventsFileName_input = " << selEventsFileName_input << '\n';
  RunLumiEventSelector* run_lumi_eventSelector = nullptr;
  if ( selEventsFileName_input != "" )
  {
    edm::ParameterSet cfgRunLumiEventSelector;
    cfgRunLumiEventSelector.addParameter<std::string>("inputFileName", selEventsFileName_input);
    cfgRunLumiEventSelector.addParameter<std::string>("separator", ":");
    run_lumi_eventSelector = new RunLumiEventSelector(cfgRunLumiEventSelector);
  }

  const fwlite::InputSource inputFiles(cfg);
  const int maxEvents        = inputFiles.maxEvents();
  const unsigned reportEvery = inputFiles.reportAfter();
  std::cout << " maxEvents = " << maxEvents << '\n';

  const fwlite::OutputFiles outputFile(cfg);
  fwlite::TFileService fs = fwlite::TFileService(outputFile.file().data());

  TTreeWrapper* inputTree = new TTreeWrapper(treeName.data(), inputFiles.files(), maxEvents);
  std::cout << "Loaded " << inputTree->getFileCount() << " file(s)\n";
  
//--- declare event-level variables
  EventInfo eventInfo;
  EventInfoReader eventInfoReader(&eventInfo);
  inputTree->registerReader(&eventInfoReader);

//--- declare particle collections
  const bool readGenObjects = isMC;
  RecoMuonReader* muonReader = new RecoMuonReader(era, branchName_muons, isMC, readGenObjects);
  inputTree->registerReader(muonReader);
  const RecoMuonCollectionSelectorLoose    preselMuonSelector  (era);
  const RecoMuonCollectionSelectorFakeable fakeableMuonSelector(era);
  const RecoMuonCollectionSelectorTight    tightMuonSelector   (era);
  
  RecoElectronReader* electronReader = new RecoElectronReader(era, branchName_electrons, isMC, readGenObjects);
  inputTree->registerReader(electronReader);
  const RecoElectronCollectionCleaner electronCleaner(0.3);
  const RecoElectronCollectionSelectorLoose    preselElectronSelector  (era);
  const RecoElectronCollectionSelectorFakeable fakeableElectronSelector(era);
  const RecoElectronCollectionSelectorTight    tightElectronSelector   (era);
  
  RecoJetReader* jetReaderAK4 = new RecoJetReader(era, isMC, branchName_jets_ak4, readGenObjects);
  jetReaderAK4->setPtMass_central_or_shift(kJetMET_central);
  jetReaderAK4->read_btag_systematics(false);
  inputTree->registerReader(jetReaderAK4);
  //RecoJetCollectionCleaner jetCleanerAK4_dR02(0.2, isDEBUG);
  RecoJetCollectionCleaner jetCleanerAK4_dR04(0.4, isDEBUG);
  RecoJetCollectionCleanerByIndex jetCleanerAK4_byIndex(isDEBUG);
  RecoJetCollectionCleaner jetCleanerAK4_dR08(0.8, isDEBUG);
  RecoJetCollectionCleaner jetCleanerAK4_dR12(1.2, isDEBUG);
  RecoJetCollectionSelector jetSelectorAK4_Hbb(era, -1, isDEBUG);
  RecoJetCollectionSelector jetSelectorAK4_Wjj(era, -1, isDEBUG);
  //jetSelectorAK4_Wjj.getSelector().set_max_absEta(4.7);
  jetSelectorAK4_Wjj.getSelector().set_max_absEta(2.4);
  RecoJetCollectionSelectorBtagLoose jetSelectorAK4_bTagLoose(era, -1, isDEBUG);
  RecoJetCollectionSelectorBtagMedium jetSelectorAK4_bTagMedium(era, -1, isDEBUG);

  RecoJetReaderAK8* jetReaderAK8 = new RecoJetReaderAK8(era, isMC, branchName_jets_ak8, branchName_subjets_ak8);
  inputTree->registerReader(jetReaderAK8);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR08(0.8, isDEBUG);
  RecoJetCollectionSelectorAK8_hh_bbWW_Hbb jetSelectorAK8_Hbb(era, -1, isDEBUG);

  RecoMEtReader* metReader = new RecoMEtReader(era, isMC, branchName_met);
  metReader->setMEt_central_or_shift(kJetMET_central);
  inputTree->registerReader(metReader);

//--- declare genParticle readers
  GenLeptonReader *   genLeptonReader            = nullptr;
  GenParticleReader * genNeutrinoReader          = nullptr;
  GenParticleReader * genParticleFromHiggsReader = nullptr;
  GenParticleReader * genWJetReader              = nullptr;
  GenLeptonReader *   genLeptonFromTopReader     = nullptr;
  GenParticleReader * genNeutrinoFromTopReader   = nullptr;
  GenParticleReader * genBJetFromTopReader       = nullptr;
  GenParticleReader * genWJetFromTopReader       = nullptr;
  if ( isMC_HH )
  {
    genLeptonReader = new GenLeptonReader(branchName_genLeptons);
    inputTree->registerReader(genLeptonReader);
    genNeutrinoReader = new GenParticleReader(branchName_genNeutrinos);
    inputTree->registerReader(genNeutrinoReader);
    genParticleFromHiggsReader = new GenParticleReader(branchName_genParticlesFromHiggs);
    inputTree->registerReader(genParticleFromHiggsReader);
    genWJetReader = new GenParticleReader(branchName_genWJets);
    inputTree->registerReader(genWJetReader);
  }
  else if ( isMC_TT )
  {
    genLeptonFromTopReader = new GenLeptonReader(branchName_genLeptonsFromTop);
    inputTree->registerReader(genLeptonFromTopReader);
    genNeutrinoFromTopReader = new GenParticleReader(branchName_genNeutrinosFromTop);
    inputTree->registerReader(genNeutrinoFromTopReader);
    genBJetFromTopReader = new GenParticleReader(branchName_genBJetsFromTop);
    inputTree->registerReader(genBJetFromTopReader);
    genWJetFromTopReader = new GenParticleReader(branchName_genWJetsFromTop);
    inputTree->registerReader(genWJetFromTopReader);
  }

  LHEInfoReader* lheInfoReader = new LHEInfoReader(hasLHE);
  inputTree->registerReader(lheInfoReader);

//--- book Ntuple for BDT training
  NtupleFillerBDT<float, int>* bdt_filler = new std::remove_pointer<decltype(bdt_filler)>::type(
    makeHistManager_cfg(process_string, Form("%s/sel/evtntuple", histogramDir.data()), era_string, "central")
  );
  typedef std::remove_pointer<decltype(bdt_filler)>::type::float_type float_type;
  typedef std::remove_pointer<decltype(bdt_filler)>::type::int_type int_type;

  bdt_filler->register_variable<float_type>(
    "lepton_pt", "lepton_eta", "lepton_phi", "lepton_charge",
    "neutrino_pt", "neutrino_eta", "neutrino_phi", 
    "bjet1_pt", "bjet1_ptReg", "bjet1_eta", "bjet1_phi", "bjet1_btagCSV", "bjet1_qgDiscr", "bjet1_charge", "dR_bjet1_lep", "dPhi_bjet1_lep", "dEta_bjet1_lep",
    "bjet2_pt", "bjet2_ptReg", "bjet2_eta", "bjet2_phi", "bjet2_btagCSV", "bjet2_qgDiscr", "bjet2_charge", "dR_bjet2_lep", "dPhi_bjet2_lep", "dEta_bjet2_lep",   
    "jet1_pt", "jet1_ptReg", "jet1_eta", "jet1_phi", "jet1_btagCSV", "jet1_qgDiscr", "jet1_charge", "dR_jet1_lep", "dPhi_jet1_lep", "dEta_jet1_lep",
    "jet2_pt", "jet2_ptReg", "jet2_eta", "jet2_phi", "jet2_btagCSV", "jet2_qgDiscr", "jet2_charge", "dR_jet2_lep", "dPhi_jet2_lep", "dEta_jet2_lep",
    "Hbb_pt", "Hbb_ptReg", "Hbb_eta", "Hbb_etaReg", "Hbb_phi", "Hbb_phiReg", "Hbb_mass", "Hbb_massReg", 
    "dR_bjet1bjet2", "dPhi_bjet1bjet2",
    "HadW_pt", "HadW_eta", "HadW_phi", "HadW_mass", "dR_HadW_lep", "dPhi_HadW_lep", "dEta_HadW_lep", "HadW_cosTheta",
    "dR_jet1jet2", "dPhi_jet1jet2",
    "LepW_mT", 
    "dR_W1W2", "min_dR_HadW_bjet", "max_dR_HadW_bjet",
    "Hww_mT", "Hww_mass",
    "mTop1", "mTop2",
    "dR_W1W2",
    "evtWeight"
  );
  bdt_filler->register_variable<int_type>(
    "bjet1_isGenMatched_Hbb", "bjet1_isGenMatched_Wjj", 
    "bjet2_isGenMatched_Hbb", "bjet2_isGenMatched_Wjj",
    "jet1_isGenMatched_Hbb", "jet1_isGenMatched_Wjj", 
    "jet2_isGenMatched_Hbb", "jet2_isGenMatched_Wjj",
    "Hbb_isBoosted", 
    "nJet", "nBJetLoose", "nBJetMedium", "nLep", 
    "nGenJets_Hbb", "nGenJets_Wjj",
    "HadW_isGenMatched"
  );
  bdt_filler->bookTree(fs);

  int analyzedEntries = 0;
  int selectedEntries = 0;
  cutFlowTableType cutFlowTable;
  while ( inputTree->hasNextEvent() && (! run_lumi_eventSelector || (run_lumi_eventSelector && ! run_lumi_eventSelector -> areWeDone())) ) {
    if ( inputTree -> canReport(reportEvery) ) {
      std::cout << "processing Entry " << inputTree -> getCurrentMaxEventIdx()
                << " or " << inputTree -> getCurrentEventIdx() << " entry in #"
                << (inputTree -> getProcessedFileCount() - 1)
                << " (" << eventInfo
                << ") file (" << selectedEntries << " Entries selected)\n";
    }
    ++analyzedEntries;

    if ( isDEBUG ) {
      std::cout << "event #" << inputTree -> getCurrentMaxEventIdx() << ' ' << eventInfo << '\n';
    }

    EvtWeightRecorderHH evtWeightRecorder({ "central" }, central_or_shift, isMC);

    double evtWeight = 1.;
    if ( isMC )
    {
      if ( apply_genWeight ) evtWeightRecorder.record_genWeight(boost::math::sign(eventInfo.genWeight));
      lheInfoReader->read();
      evtWeightRecorder.record_lheScaleWeight(lheInfoReader);
      evtWeightRecorder.record_puWeight(&eventInfo);
      evtWeightRecorder.record_lumiScale(lumiScale);
      evtWeight = evtWeightRecorder.get_inclusive(central_or_shift);
    }

    if ( run_lumi_eventSelector && !(*run_lumi_eventSelector)(eventInfo) ) continue;
    cutFlowTable.update("run:ls:event selection", evtWeight);

    if ( run_lumi_eventSelector ) {
      std::cout << "processing Entry #" << inputTree->getCumulativeMaxEventCount() << ": " << eventInfo << std::endl;
      if ( inputTree -> isOpen() ) {
        std::cout << "input File = " << inputTree->getCurrentFileName() << std::endl;
      }
    }
    
//--- build collections of electrons, muons and hadronic taus;
//    resolve overlaps in order of priority: muon, electron,
    const std::vector<RecoMuon> muons = muonReader->read();
    const std::vector<const RecoMuon *> muon_ptrs = convert_to_ptrs(muons);
    // CV: no cleaning needed for muons, as they have the highest priority in the overlap removal
    const std::vector<const RecoMuon *> cleanedMuons  = muon_ptrs;
    const std::vector<const RecoMuon *> preselMuons   = preselMuonSelector  (cleanedMuons,  isHigherConePt);
    const std::vector<const RecoMuon *> fakeableMuons = fakeableMuonSelector(preselMuons,   isHigherConePt);
    const std::vector<const RecoMuon *> tightMuons    = tightMuonSelector   (fakeableMuons, isHigherConePt);
    const std::vector<const RecoMuon *> selMuons      = selectObjects(
      leptonSelection, preselMuons, fakeableMuons, tightMuons
    );
    if ( isDEBUG )
    {
      printCollection("selMuons", selMuons);
    }

    const std::vector<RecoElectron> electrons = electronReader->read();
    const std::vector<const RecoElectron *> electron_ptrs     = convert_to_ptrs(electrons);
    const std::vector<const RecoElectron *> cleanedElectrons  = electronCleaner(electron_ptrs, fakeableMuons);
    const std::vector<const RecoElectron *> preselElectronsUncleaned = preselElectronSelector  (electron_ptrs,     isHigherConePt);
    const std::vector<const RecoElectron *> preselElectrons          = preselElectronSelector  (cleanedElectrons,  isHigherConePt);
    const std::vector<const RecoElectron *> fakeableElectrons        = fakeableElectronSelector(preselElectrons,   isHigherConePt);
    const std::vector<const RecoElectron *> tightElectrons           = tightElectronSelector   (fakeableElectrons, isHigherConePt);
    const std::vector<const RecoElectron *> selElectrons             = selectObjects(
      leptonSelection, preselElectrons, fakeableElectrons, tightElectrons
    );
    if ( isDEBUG )
    {
      printCollection("selElectrons", selElectrons);
    }

    const std::vector<const RecoLepton*> preselLeptons = mergeLeptonCollections(preselElectrons, preselMuons, isHigherConePt);
    const std::vector<const RecoLepton*> fakeableLeptons = mergeLeptonCollections(fakeableElectrons, fakeableMuons, isHigherConePt);
    const std::vector<const RecoLepton*> tightLeptons = mergeLeptonCollections(tightElectrons, tightMuons, isHigherConePt);
    const std::vector<const RecoLepton*> selLeptons = mergeLeptonCollections(selElectrons, selMuons, isHigherConePt);	

    // require at least one lepton passing fakeable or tight selection criteria
    // (fakeable lepton selection applied in fake background control region,
    //  tight lepton selection applied in signal region)
    if ( !(selLeptons.size() >= 1) ) {
      continue;
    }
    cutFlowTable.update(">= 1 sel leptons", evtWeight);
    const RecoLepton* selLepton = selLeptons[0];

    const double minPt_lead = 25.;
    if ( !(selLepton->cone_pt() > minPt_lead) ) {
      continue;
    }
    cutFlowTable.update("lepton pT > 25 GeV", evtWeight);

    // require exactly one lepton passing tight selection criteria, to avoid overlap with other channels
    if ( !(tightLeptons.size() <= 1) ) {
      continue;
    }
    cutFlowTable.update("<= 1 tight leptons", evtWeight);

//--- build collections of jets 
    const std::vector<RecoJet> jets_ak4 = jetReaderAK4->read();
    const std::vector<const RecoJet*> jet_ptrs_ak4 = convert_to_ptrs(jets_ak4);
    const std::vector<const RecoJet*> cleanedJetsAK4_wrtLeptons = jetCleaningByIndex ?
      jetCleanerAK4_byIndex(jet_ptrs_ak4, fakeableLeptons) :
      jetCleanerAK4_dR04   (jet_ptrs_ak4, fakeableLeptons)
      //jetCleanerAK4_dR02   (jet_ptrs_ak4, fakeableLeptons)
    ;
    const std::vector<const RecoJet*> selBJetsAK4_loose = jetSelectorAK4_bTagLoose(cleanedJetsAK4_wrtLeptons, isHigherPt);
    const std::vector<const RecoJet*> selBJetsAK4_medium = jetSelectorAK4_bTagMedium(cleanedJetsAK4_wrtLeptons, isHigherPt);
   
    const std::vector<RecoJetAK8> jets_ak8 = jetReaderAK8->read();
    const std::vector<const RecoJetAK8*> jet_ptrs_ak8 = convert_to_ptrs(jets_ak8);

    RecoMEt met = metReader->read();
    const Particle::LorentzVector& metP4 = met.p4();

    //-------------------------------------------------------------------
    // select the two jets from the H->bb decay from either the AK4 (resolved H->bb) or AK8 (boosted H->bb) collection
    //
    // WARNING: logic to select the two jets from H->bb decay 
    //          needs to match the code in analyze_hh_bb1l.cc !!
    const std::vector<const RecoJetAK8*> cleanedJetsAK8_wrtLeptons = jetCleanerAK8_dR08(jet_ptrs_ak8, fakeableLeptons);
    const std::vector<const RecoJetAK8*> selJetsAK8_Hbb = jetSelectorAK8_Hbb(cleanedJetsAK8_wrtLeptons, isHigherCSV_ak8);
    const std::vector<const RecoJet*> selJetsAK4_Hbb = jetSelectorAK4_Hbb(cleanedJetsAK4_wrtLeptons, isHigherCSV);
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
    if ( !(selJet1_Hbb && selJet2_Hbb) ) 
    {
      continue;
    }
    cutFlowTable.update(">= 2 jets from H->bb", evtWeight);
    //-------------------------------------------------------------------

    //-------------------------------------------------------------------
    // select jets from W->jj decay
    //
    // WARNING: logic to clean the AK4 jets with respect to jets from the H->bb decay 
    //          needs to match the code in jetSelectionAuxFunctions.cc !!
    std::vector<const RecoJet*> cleanedJetsAK4_wrtHbb;
    if ( selJetAK8_Hbb ) 
    {
       const std::vector<const RecoJetAK8*> overlaps = { selJetAK8_Hbb };
      cleanedJetsAK4_wrtHbb = jetCleanerAK4_dR12(cleanedJetsAK4_wrtLeptons, overlaps);
    } 
    else 
    {
      std::vector<const RecoJetBase*> overlaps;
      if ( selJet1_Hbb ) overlaps.push_back(selJet1_Hbb);
      if ( selJet2_Hbb ) overlaps.push_back(selJet2_Hbb);
      cleanedJetsAK4_wrtHbb = jetCleanerAK4_dR08(cleanedJetsAK4_wrtLeptons, overlaps);
    }
    const std::vector<const RecoJet*> selJetsAK4_Wjj = jetSelectorAK4_Wjj(cleanedJetsAK4_wrtHbb, isHigherPt);
    if ( !(selJetsAK4_Wjj.size() >= 2) ) {
      continue;
    }
    cutFlowTable.update(">= 2 jets from W->jj", evtWeight);
    //-------------------------------------------------------------------

//--- build collections of generator level particles 
    GenParticleMatcherBase* genParticleMatcher = nullptr;
    if ( isMC_HH )
    {
      std::vector<GenLepton> genLeptons = genLeptonReader->read();
      std::vector<GenParticle> genNeutrinos = genNeutrinoReader->read();
      std::vector<GenParticle> genParticlesFromHiggs = genParticleFromHiggsReader->read();
      std::vector<GenParticle> genWJets = genWJetReader->read();
      genParticleMatcherFromHiggs.setGenParticles(genParticlesFromHiggs, genLeptons, genNeutrinos, genWJets);
      genParticleMatcher = &genParticleMatcherFromHiggs;
    }
    else if ( isMC_TT )
    {
      std::vector<GenLepton> genLeptonsFromTop = genLeptonFromTopReader->read();
      std::vector<GenParticle> genNeutrinosFromTop = genNeutrinoFromTopReader->read();
      std::vector<GenParticle> genBJetsFromTop = genBJetFromTopReader->read();
      std::vector<GenParticle> genWJetsFromTop = genWJetFromTopReader->read();
      genParticleMatcherFromTop.setGenParticles(genLeptonsFromTop, genNeutrinosFromTop, genWJetsFromTop, genBJetsFromTop);
      genParticleMatcher = &genParticleMatcherFromTop;
    }
    else assert(0);
    std::vector<GenLepton> genLeptons = genParticleMatcher->getLeptons();
    std::vector<GenJet> genBJets = genParticleMatcher->getBJets();
    std::vector<GenJet> genWJets = genParticleMatcher->getWJets();
    //const Particle::LorentzVector& genMEtP4 = genParticleMatcher->getMEt();
    if ( !(genLeptons.size() == 1) ) {
      continue;
    }
    cutFlowTable.update("exactly 1 gen-lepton", evtWeight);

    for ( std::vector<const RecoJet*>::const_iterator selJet1_Wjj = selJetsAK4_Wjj.begin();
	  selJet1_Wjj != selJetsAK4_Wjj.end(); ++selJet1_Wjj ) {
      for ( std::vector<const RecoJet*>::const_iterator selJet2_Wjj = selJet1_Wjj + 1;
     	    selJet2_Wjj != selJetsAK4_Wjj.end(); ++selJet2_Wjj ) {

        Particle::LorentzVector selJet1P4_Hbb = selJet1_Hbb->p4();
        Particle::LorentzVector selJet2P4_Hbb = selJet2_Hbb->p4();

        Particle::LorentzVector selJet1P4_Wjj = (*selJet1_Wjj)->p4();
        Particle::LorentzVector selJet2P4_Wjj = (*selJet2_Wjj)->p4();

        Particle::LorentzVector HbbP4 = selJet1P4_Hbb + selJet1P4_Hbb;
        Particle::LorentzVector HbbP4_reg = HbbP4;
        if ( dynamic_cast<const RecoJet*>(selJet1_Hbb) && dynamic_cast<const RecoJet*>(selJet2_Hbb) )
        {
          HbbP4_reg = selJet1_Hbb->p4()*(dynamic_cast<const RecoJet*>(selJet1_Hbb))->bRegCorr() 
                    + selJet2_Hbb->p4()*(dynamic_cast<const RecoJet*>(selJet2_Hbb))->bRegCorr();
        }

        Particle::LorentzVector HadWP4 = selJet1P4_Wjj + selJet2P4_Wjj;     
        double HadW_cosTheta = compCosTheta(selJet1P4_Wjj, selJet2P4_Wjj);

        // compute four-vector of neutrino produced in H->WW*->jj lnu decay,
        // using Higgs boson mass constraint, as described in Section 3.4.2 of AN-2018/058 (v4)
        //
        // Note: mass of lepton + jets from W->jj decay + neutrino is not equal to 125 GeV
        //       in case the Higgs boson mass constraint yields a complex solution for the logitudinal momentum of the neutrino
        //      (of which we then take the real part and discard the complex part)
        Particle::LorentzVector neutrinoP4_B2G_18_008 = comp_metP4_B2G_18_008(selLepton->p4() + selJet1P4_Wjj + selJet2P4_Wjj, metP4.px(), metP4.py(), higgsBosonMass);

        Particle::LorentzVector LepWP4 = selLepton->p4() + neutrinoP4_B2G_18_008;
        double LepW_mT = comp_MT_met(selLepton->p4(), metP4.pt(), metP4.phi());

        Particle::LorentzVector HwwP4 = LepWP4 + HadWP4;
        double HwwEt = selJet1P4_Wjj.Et() + selJet2P4_Wjj.Et() + selLepton->pt()      + metP4.pt();
        double HwwPx = selJet1P4_Wjj.px() + selJet2P4_Wjj.px() + selLepton->p4().px() + metP4.px();
        double HwwPy = selJet1P4_Wjj.py() + selJet2P4_Wjj.py() + selLepton->p4().py() + metP4.py();
        double Hww_mT = TMath::Sqrt(TMath::Max(0., HwwEt*HwwEt - (HwwPx*HwwPx + HwwPy*HwwPy)));

        Particle::LorentzVector top1P4 = selJet1_Hbb->p4() + selJet1P4_Wjj + selJet2P4_Wjj;
        Particle::LorentzVector top2P4 = selJet2_Hbb->p4() + selJet1P4_Wjj + selJet2P4_Wjj;
        double mTop1, mTop2;
        if ( TMath::Abs(top1P4.mass() - topMass) < TMath::Abs(top2P4.mass() - topMass) )
        {
          mTop1 = top1P4.mass();
          mTop2 = top2P4.mass();
        }
        else
        {
          mTop1 = top2P4.mass();
          mTop2 = top1P4.mass();
        }

        double dR_HadW_bjet1 = deltaR(HadWP4, selJet1P4_Hbb);
        double dR_HadW_bjet2 = deltaR(HadWP4, selJet2P4_Hbb);

        if ( bdt_filler ) {
          bdt_filler -> operator()({ eventInfo.run, eventInfo.lumi, eventInfo.event })
          ("lepton_pt",              selLepton->pt())
          ("lepton_eta",             selLepton->eta())
          ("lepton_phi",             selLepton->phi())
          ("lepton_charge",          selLepton->charge())
          ("neutrino_pt",            neutrinoP4_B2G_18_008.pt())
          ("neutrino_eta",           neutrinoP4_B2G_18_008.eta())
          ("neutrino_phi",           neutrinoP4_B2G_18_008.phi())
          ("bjet1_pt",               selJet1P4_Hbb.pt())
          ("bjet1_ptReg",            dynamic_cast<const RecoJet*>(selJet1_Hbb) ? (dynamic_cast<const RecoJet*>(selJet1_Hbb))->bRegCorr()*selJet1P4_Hbb.pt() : selJet1P4_Hbb.pt())
          ("bjet1_eta",              selJet1P4_Hbb.eta())
          ("bjet1_phi",              selJet1P4_Hbb.phi())
          ("bjet1_btagCSV",          dynamic_cast<const RecoJet*>(selJet1_Hbb) ? (dynamic_cast<const RecoJet*>(selJet1_Hbb))->BtagCSV() : 0.)
          ("bjet1_qgDiscr",          dynamic_cast<const RecoJet*>(selJet1_Hbb) ? (dynamic_cast<const RecoJet*>(selJet1_Hbb))->QGDiscr() : 0.)
          ("bjet1_charge",           selJet1_Hbb->charge())  
          ("bjet1_isGenMatched_Hbb", isGenMatched(selJet1_Hbb, genBJets))
          ("bjet1_isGenMatched_Wjj", isGenMatched(selJet1_Hbb, genWJets))
          ("dR_bjet1_lep",           deltaR(selJet1P4_Hbb, selLepton->p4()))
          ("dPhi_bjet1_lep",         deltaPhi(selJet1P4_Hbb.phi(), selLepton->phi()))
          ("dEta_bjet1_lep",         TMath::Abs(selJet1P4_Hbb.eta() - selLepton->eta()))
          ("bjet2_pt",               selJet2P4_Hbb.pt())
          ("bjet2_ptReg",            dynamic_cast<const RecoJet*>(selJet2_Hbb) ? (dynamic_cast<const RecoJet*>(selJet2_Hbb))->bRegCorr()*selJet2P4_Hbb.pt() : selJet2P4_Hbb.pt())
          ("bjet2_eta",              selJet2P4_Hbb.eta())
          ("bjet2_phi",              selJet2P4_Hbb.phi())
          ("bjet2_btagCSV",          dynamic_cast<const RecoJet*>(selJet2_Hbb) ? (dynamic_cast<const RecoJet*>(selJet2_Hbb))->BtagCSV() : 0.)
          ("bjet2_qgDiscr",          dynamic_cast<const RecoJet*>(selJet2_Hbb) ? (dynamic_cast<const RecoJet*>(selJet2_Hbb))->QGDiscr() : 0.)
          ("bjet2_charge",           selJet2_Hbb->charge())  
          ("bjet2_isGenMatched_Hbb", isGenMatched(selJet2_Hbb, genBJets))
          ("bjet2_isGenMatched_Wjj", isGenMatched(selJet2_Hbb, genWJets))
          ("dR_bjet2_lep",           deltaR(selJet2P4_Hbb, selLepton->p4()))
          ("dPhi_bjet2_lep",         deltaPhi(selJet2P4_Hbb.phi(), selLepton->phi()))
          ("dEta_bjet2_lep",         TMath::Abs(selJet2P4_Hbb.eta() - selLepton->eta()))
          ("Hbb_pt",                 HbbP4.pt())
          ("Hbb_ptReg",              HbbP4_reg.pt())
          ("Hbb_eta",                HbbP4.eta())
          ("Hbb_etaReg",             HbbP4_reg.eta())
          ("Hbb_phi",                HbbP4.phi())
          ("Hbb_phiReg",             HbbP4_reg.phi())
          ("Hbb_mass",               HbbP4.mass())
          ("Hbb_massReg",            HbbP4_reg.mass())
          ("dR_bjet1bjet2",          deltaR(selJet1P4_Hbb, selJet2P4_Hbb))
          ("dPhi_bjet1bjet2",        deltaPhi(selJet1P4_Hbb.phi(), selJet2P4_Hbb.phi()))
          ("jet1_pt",                selJet1P4_Wjj.pt())
          ("jet1_ptReg",             (*selJet1_Wjj)->bRegCorr()*selJet1P4_Wjj.pt())
          ("jet1_eta",               selJet1P4_Wjj.eta())
          ("jet1_phi",               selJet1P4_Wjj.phi())
          ("jet1_btagCSV",           (*selJet1_Wjj)->BtagCSV())
          ("jet1_qgDiscr",           (*selJet1_Wjj)->QGDiscr())
          ("jet1_charge",            (*selJet1_Wjj)->charge())
          ("jet1_isGenMatched_Hbb",  isGenMatched(*selJet1_Wjj, genBJets))
          ("jet1_isGenMatched_Wjj",  isGenMatched(*selJet1_Wjj, genWJets))
          ("dR_jet1_lep",            deltaR(selJet1P4_Wjj, selLepton->p4()))
          ("dPhi_jet1_lep",          deltaPhi(selJet1P4_Wjj.phi(), selLepton->phi()))
          ("dEta_jet1_lep",          TMath::Abs(selJet1P4_Wjj.eta() - selLepton->eta()))
          ("jet2_pt",                selJet2P4_Wjj.pt())
          ("jet2_ptReg",             (*selJet2_Wjj)->bRegCorr()*selJet2P4_Wjj.pt())
          ("jet2_eta",               selJet2P4_Wjj.eta())
          ("jet2_phi",               selJet2P4_Wjj.phi())
          ("jet2_btagCSV",           (*selJet2_Wjj)->BtagCSV())
          ("jet2_qgDiscr",           (*selJet2_Wjj)->QGDiscr())
          ("jet2_charge",            (*selJet2_Wjj)->charge())
          ("jet2_isGenMatched_Hbb",  isGenMatched(*selJet2_Wjj, genBJets))
          ("jet2_isGenMatched_Wjj",  isGenMatched(*selJet2_Wjj, genWJets))
          ("dR_jet2_lep",            deltaR(selJet2P4_Wjj, selLepton->p4()))
          ("dPhi_jet2_lep",          deltaPhi(selJet2P4_Wjj.phi(), selLepton->phi()))
          ("dEta_jet2_lep",          TMath::Abs(selJet2P4_Wjj.eta() - selLepton->eta()))
          ("HadW_pt",                HadWP4.pt())
          ("HadW_eta",               HadWP4.eta())
          ("HadW_phi",               HadWP4.phi())
          ("HadW_mass",              HadWP4.mass())
          ("dR_HadW_lep",            deltaR(HadWP4, selLepton->p4()))
          ("dPhi_HadW_lep",          deltaPhi(HadWP4.phi(), selLepton->phi()))
          ("dEta_HadW_lep",          TMath::Abs(HadWP4.eta() - selLepton->eta()))
          ("HadW_cosTheta",          HadW_cosTheta)
          ("dR_jet1jet2",            deltaR(selJet1P4_Wjj, selJet2P4_Wjj))
          ("dPhi_jet1jet2",          deltaPhi(selJet1P4_Wjj.phi(), selJet2P4_Wjj.phi()))
          ("LepW_mT",                LepW_mT)
          ("Hww_mT",                 Hww_mT)
          ("Hww_mass",               HwwP4.mass())
          ("mTop1",                  mTop1)
          ("mTop2",                  mTop2)
          ("dR_W1W2",                deltaR(HadWP4, LepWP4))
          ("min_dR_HadW_bjet",       TMath::Min(dR_HadW_bjet1, dR_HadW_bjet2))
          ("max_dR_HadW_bjet",       TMath::Max(dR_HadW_bjet1, dR_HadW_bjet2))          
          ("evtWeight",              evtWeight)
          ("Hbb_isBoosted",          ( selJetAK8_Hbb ) ? true : false)
          ("nJet",                   selJetsAK4_Wjj.size())
          ("nBJetLoose",             selBJetsAK4_loose.size())
          ("nBJetMedium",            selBJetsAK4_medium.size())
          ("nLep",                   preselLeptons.size())
          ("nGenJets_Hbb",           genBJets.size())
          ("nGenJets_Wjj",           genWJets.size())
          ("HadW_isGenMatched",      isGenMatched(*selJet1_Wjj, genWJets) && isGenMatched(*selJet2_Wjj, genWJets))
              .fill();
	}
      }
    }

    ++selectedEntries;
  } // idxEntry

  std::cout << "max num. Entries = " << inputTree -> getCumulativeMaxEventCount()
            << " (limited by " << maxEvents << ") processed in "
            << inputTree -> getProcessedFileCount() << " file(s) (out of "
            << inputTree -> getFileCount() << ")\n"
            << " analyzed = " << analyzedEntries << '\n'
            << " selected = " << selectedEntries << "\n\n"
            << "cut-flow table" << std::endl;

  delete run_lumi_eventSelector;
  delete muonReader;
  delete electronReader;
  delete jetReaderAK4;
  //delete jetReaderAK8;

  delete inputTree;

  clock.Show("analyze_hadWTagger");

  return EXIT_SUCCESS;
}
