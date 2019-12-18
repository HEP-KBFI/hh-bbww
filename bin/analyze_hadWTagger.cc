#include "FWCore/ParameterSet/interface/ParameterSet.h" // edm::ParameterSet
#include "FWCore/PythonParameterSet/interface/MakeParameterSets.h" // edm::readPSetsFrom()
#include "FWCore/Utilities/interface/Exception.h" // cms::Exception
#include "PhysicsTools/FWLite/interface/TFileService.h" // fwlite::TFileService
#include "DataFormats/FWLite/interface/InputSource.h" // fwlite::InputSource
#include "DataFormats/FWLite/interface/OutputFiles.h" // fwlite::OutputFiles
#include "DataFormats/Math/interface/LorentzVector.h" // math::PtEtaPhiMLorentzVector

#include <TChain.h> // TChain
#include <TTree.h> // TTree
#include <TBenchmark.h> // TBenchmark
#include <TString.h> // TString, Form
#include <TError.h> // gErrorAbortLevel, kError
#include <TLorentzVector.h> // TLorentzVector

#include "hhAnalysis/bbww/interface/MEMOutput_hh_bb1l.h" // MEMOutput_hh_bb1l
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronReader.h" // RecoElectronReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonReader.h" // RecoMuonReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetReader.h" // RecoJetReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetReaderAK8.h" // RecoJetReaderAK8
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEtReader.h" // RecoMEtReader, RecoMEt
#include "tthAnalysis/HiggsToTauTau/interface/EventInfoReader.h" // EventInfoReader, EventInfo
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
#include "hhAnalysis/bbww/interface/RecoJetCollectionSelectorAK8_hh_bbWW_Hbb.h" // RecoJetSelectorAK8_hh_bbWW_Hbb
#include "hhAnalysis/multilepton/interface/EvtWeightRecorderHH.h" // EvtWeightRecorderHH
#include "tthAnalysis/HiggsToTauTau/interface/RunLumiEventSelector.h" // RunLumiEventSelector
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // selectObjects(), get_selection(), get_era(), kLoose, kFakeable, kTight
#include "tthAnalysis/HiggsToTauTau/interface/sysUncertOptions.h" // k*_central
#include "tthAnalysis/HiggsToTauTau/interface/memAuxFunctions.h" // get_memObjectBranchName(), get_memPermutationBranchName()
#include "tthAnalysis/HiggsToTauTau/interface/cutFlowTable.h" // cutFlowTableType
#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // createSubdirectory_recursively()
#include "tthAnalysis/HiggsToTauTau/interface/NtupleFillerBDT.h" // NtupleFillerBDT
#include "tthAnalysis/HiggsToTauTau/interface/TTreeWrapper.h" // TTreeWrapper

#include <boost/algorithm/string/predicate.hpp> // boost::starts_with()
#include <boost/math/special_functions/sign.hpp> // boost::math::sign()

#include <iostream> // std::cerr, std::fixed
#include <cstdlib> // EXIT_SUCCESS, EXIT_FAILURE
#include <assert.h> // assert

typedef std::vector<std::string> vstring;

bool 
isGenMatched(const RecoJet* recJet, const std::vector<const GenParticle*>& genParticles, double dRmax = 0.3)
{
  for ( std::vector<const GenParticle*>::const_iterator genParticle = genParticles.begin();
	genParticle != genParticles.end(); ++genParticle ) {
    double dR = deltaR(recJet->p4(), (*genParticle)->p4());
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
  const bool isMC_HH                        = process_string.find("hh_bbvv") != std::string::npos;
  bool hasLHE                               = cfg_analyze.getParameter<bool>("hasLHE");
  std::string central_or_shift              = "central";
  edm::VParameterSet lumiScale              = cfg_analyze.getParameter<edm::VParameterSet>("lumiScale");
  bool apply_genWeight                      = cfg_analyze.getParameter<bool>("apply_genWeight");

  const std::string branchName_electrons    = cfg_analyze.getParameter<std::string>("branchName_electrons");
  const std::string branchName_muons        = cfg_analyze.getParameter<std::string>("branchName_muons");
  const std::string branchName_jets_ak4     = cfg_analyze.getParameter<std::string>("branchName_jets_ak4");
  const std::string branchName_jets_ak8     = cfg_analyze.getParameter<std::string>("branchName_jets_ak8_Hbb");
  const std::string branchName_subjets_ak8  = cfg_analyze.getParameter<std::string>("branchName_subjets_ak8_Hbb");

  const std::string branchName_genLeptons   = cfg_analyze.getParameter<std::string>("branchName_genLeptons");
  const std::string branchName_genJets      = cfg_analyze.getParameter<std::string>("branchName_genJets");
  const std::string branchName_genBJets     = cfg_analyze.getParameter<std::string>("branchName_genBJets");
  const std::string branchName_genWBosons   = cfg_analyze.getParameter<std::string>("branchName_genWBosons");
  const std::string branchName_genWJets     = cfg_analyze.getParameter<std::string>("branchName_genWJets");

  bool jetCleaningByIndex = cfg_analyze.getParameter<bool>("jetCleaningByIndex");

  std::string histogramDir = cfg_analyze.getParameter<std::string>("histogramDir");	

  const std::string era_string = cfg_analyze.getParameter<std::string>("era");
  const int era = get_era(era_string);

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
  RecoJetCollectionCleaner jetCleanerAK4_dR04(0.4, isDEBUG);
  RecoJetCollectionCleanerByIndex jetCleanerAK4_byIndex(isDEBUG);
  RecoJetCollectionCleaner jetCleanerAK4_dR08(0.8, isDEBUG);
  RecoJetCollectionCleaner jetCleanerAK4_dR12(1.2, isDEBUG);
  RecoJetCollectionSelector jetSelectorAK4(era, -1, isDEBUG);
  RecoJetCollectionSelectorBtagLoose jetSelectorAK4_bTagLoose(era, -1, isDEBUG);
  RecoJetCollectionSelectorBtagMedium jetSelectorAK4_bTagMedium(era, -1, isDEBUG);

  RecoJetReaderAK8* jetReaderAK8 = new RecoJetReaderAK8(era, branchName_jets_ak8, branchName_subjets_ak8); 
  inputTree->registerReader(jetReaderAK8);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR08(0.8, isDEBUG);
  RecoJetCollectionSelectorAK8_hh_bbWW_Hbb jetSelectorAK8_Hbb(era, -1, isDEBUG);

  GenParticleReader* genLeptonReader = new GenParticleReader(branchName_genLeptons);
  inputTree->registerReader(genLeptonReader);
  GenParticleReader* genJetReader = new GenParticleReader(branchName_genJets);
  inputTree->registerReader(genJetReader);
  GenParticleReader* genBJetReader = new GenParticleReader(branchName_genBJets);
  inputTree->registerReader(genBJetReader);
  GenParticleReader* genWBosonReader = new GenParticleReader(branchName_genWBosons);
  inputTree->registerReader(genWBosonReader);
  GenParticleReader* genWJetReader = new GenParticleReader(branchName_genWJets);
  inputTree->registerReader(genWJetReader);	

  LHEInfoReader* lheInfoReader = new LHEInfoReader(hasLHE);
  inputTree->registerReader(lheInfoReader);

//--- book Ntuple for BDT training
  NtupleFillerBDT<float, int>* bdt_filler = new std::remove_pointer<decltype(bdt_filler)>::type(
    makeHistManager_cfg(process_string, Form("%s/sel/evtntuple", histogramDir.data()), era_string, "central")
  );
  typedef std::remove_pointer<decltype(bdt_filler)>::type::float_type float_type;
  typedef std::remove_pointer<decltype(bdt_filler)>::type::int_type int_type;

  bdt_filler->register_variable<float_type>(
    "jet1_pt", "jet1_eta", "jet1_phi", "jet1_btagCSV", "jet1_qgDiscr", "dr_jet1_lep",
    "jet2_pt", "jet2_eta", "jet2_phi", "jet2_btagCSV", "jet2_qgDiscr", "dr_jet2_lep",
    "HadW_pt", "HadW_eta", "HadW_phi", "HadW_mass", "dr_HadW_lep", 
    "dR_jj", "dPhi_jj",
    "cosTheta",
    "evtWeight"
  );
  bdt_filler->register_variable<int_type>(
    "nJet", "nBJetLoose", "nBJetMedium", "nLep", 
    "nGenHadWJets",
    "jet1_isGenMatched", "jet2_isGenMatched",
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
    ;
    const std::vector<const RecoJet*> selJetsAK4 = jetSelectorAK4(cleanedJetsAK4_wrtLeptons, isHigherPt);
    const std::vector<const RecoJet*> selBJetsAK4_loose = jetSelectorAK4_bTagLoose(cleanedJetsAK4_wrtLeptons, isHigherPt);
    const std::vector<const RecoJet*> selBJetsAK4_medium = jetSelectorAK4_bTagMedium(cleanedJetsAK4_wrtLeptons, isHigherPt);
      
    const std::vector<RecoJetAK8> jets_ak8 = jetReaderAK8->read();
    const std::vector<const RecoJetAK8*> jet_ptrs_ak8 = convert_to_ptrs(jets_ak8);
    const std::vector<const RecoJetAK8*> cleanedJetsAK8_wrtLeptons = jetCleanerAK8_dR08(jet_ptrs_ak8, fakeableLeptons);
    const std::vector<const RecoJetAK8*> selJetsAK8_Hbb = jetSelectorAK8_Hbb(cleanedJetsAK8_wrtLeptons, isHigherCSV_ak8);
    const std::vector<const RecoJet*> selJetsAK4_Hbb = jetSelectorAK4(cleanedJetsAK4_wrtLeptons, isHigherCSV);
    //-------------------------------------------------------------------
    // select the two jets from the H->bb decay from either the AK4 (resolved H->bb) or AK8 (boosted H->bb) collection
    //
    // WARNING: logic to select the two jets from H->bb decay needs to match the code in analyze_hh_bb1l.cc !!
    const RecoJetAK8* selJetAK8_Hbb = nullptr;
    const RecoJetBase* selJet1_Hbb = nullptr;
    const RecoJetBase* selJet2_Hbb = nullptr;
    if ( selJetsAK8_Hbb.size() >= 1 )
    {
      selJetAK8_Hbb = selJetsAK8_Hbb[0];
      assert(selJetAK8_Hbb->subJet1() && selJetAK8_Hbb->subJet2());
      if ( selJetAK8_Hbb->subJet1()->BtagCSV() > selJetAK8_Hbb->subJet2()->BtagCSV() )
      {
        selJet1_Hbb = selJetAK8_Hbb->subJet1();
        selJet2_Hbb = selJetAK8_Hbb->subJet2();
      }
      else
      {
        selJet1_Hbb = selJetAK8_Hbb->subJet2();
        selJet2_Hbb = selJetAK8_Hbb->subJet1();
      }
    }
    else if ( selJetsAK4_Hbb.size() >= 2 )
    {
      selJet1_Hbb = selJetsAK4_Hbb[0];
      selJet2_Hbb = selJetsAK4_Hbb[1];
    }
    //-------------------------------------------------------------------
          
    if ( !(selJet1_Hbb && selJet2_Hbb) ) {
      continue;
    }
    cutFlowTable.update(">= 2 jets from H->bb", evtWeight);

    //-------------------------------------------------------------------
    // select jets from W->jj decay
    std::vector<const RecoJet*> cleanedJetsAK4_wrtHbb;
    if ( selJetAK8_Hbb ) {
      const std::vector<const RecoJetAK8*> overlaps = { selJetAK8_Hbb };
      cleanedJetsAK4_wrtHbb = jetCleanerAK4_dR12(cleanedJetsAK4_wrtLeptons, overlaps);
    } else {
      std::vector<const RecoJetBase*> overlaps;
      if ( selJet1_Hbb ) overlaps.push_back(selJet1_Hbb);
      if ( selJet2_Hbb ) overlaps.push_back(selJet2_Hbb);
      cleanedJetsAK4_wrtHbb = jetCleanerAK4_dR08(cleanedJetsAK4_wrtLeptons, overlaps);
    }
    const std::vector<const RecoJet*> selJetsAK4_Wjj = jetSelectorAK4(cleanedJetsAK4_wrtHbb, isHigherPt);
    //-------------------------------------------------------------------
           
    if ( !(selJetsAK4_Wjj.size() >= 2) ) {
      continue;
    }
    cutFlowTable.update(">= 2 jets from W->jj", evtWeight);

    std::vector<GenParticle> genLeptons = genLeptonReader->read();
    std::vector<GenParticle> genJets    = genJetReader->read();
    std::vector<GenParticle> genBJets   = genBJetReader->read();
    std::vector<GenParticle> genWBosons = genWBosonReader->read();
    std::vector<GenParticle> genWJets   = genWJetReader->read();

    std::vector<const GenParticle*> genWJets_ptrs = convert_to_ptrs(genWJets);

    for ( std::vector<const RecoJet*>::const_iterator selJet1_Wjj = selJetsAK4_Wjj.begin();
	  selJet1_Wjj != selJetsAK4_Wjj.end(); ++selJet1_Wjj ) {
      for ( std::vector<const RecoJet*>::const_iterator selJet2_Wjj = selJet1_Wjj + 1;
     	    selJet2_Wjj != selJetsAK4_Wjj.end(); ++selJet2_Wjj ) {

        Particle::LorentzVector selJet1P4_Wjj = (*selJet1_Wjj)->p4();
        bool selJet1_Wjj_isGenMatched = isGenMatched(*selJet1_Wjj, genWJets_ptrs);
        Particle::LorentzVector selJet2P4_Wjj = (*selJet2_Wjj)->p4();
        bool selJet2_Wjj_isGenMatched = isGenMatched(*selJet2_Wjj, genWJets_ptrs);
        Particle::LorentzVector hadWP4 = selJet1P4_Wjj + selJet2P4_Wjj;     
        double cosTheta = compCosTheta(selJet1P4_Wjj, selJet2P4_Wjj);

        if ( bdt_filler ) {
          bdt_filler -> operator()({ eventInfo.run, eventInfo.lumi, eventInfo.event })
          ("jet1_pt",              selJet1P4_Wjj.pt())
          ("jet1_eta",             selJet1P4_Wjj.eta())
          ("jet1_phi",             selJet1P4_Wjj.phi())
          ("jet1_btagCSV",         (*selJet1_Wjj)->BtagCSV())
          ("jet1_qgDiscr",         (*selJet1_Wjj)->QGDiscr())
          ("dr_jet1_lep",          deltaR(selJet1P4_Wjj, selLepton->p4()))
          ("jet2_pt",              selJet2P4_Wjj.pt())
          ("jet2_eta",             selJet2P4_Wjj.eta())
          ("jet2_phi",             selJet2P4_Wjj.phi())
          ("jet2_btagCSV",         (*selJet2_Wjj)->BtagCSV())
          ("jet2_qgDiscr",         (*selJet2_Wjj)->QGDiscr())
          ("dr_jet2_lep",          deltaR(selJet2P4_Wjj, selLepton->p4()))
          ("HadW_pt",              hadWP4.pt())
          ("HadW_eta",             hadWP4.eta())
          ("HadW_phi",             hadWP4.phi())
          ("HadW_mass",            hadWP4.mass())
          ("dr_HadW_lep",          deltaR(hadWP4, selLepton->p4()))
          ("dR_jj",                deltaR(selJet1P4_Wjj, selJet2P4_Wjj))
          ("dPhi_jj",              deltaPhi(selJet1P4_Wjj.phi(), selJet2P4_Wjj.phi()))
          ("cosTheta",             cosTheta)
          ("evtWeight",            evtWeight)
          ("nJet",                 selJetsAK4_Wjj.size())
          ("nBJetLoose",           selBJetsAK4_loose.size())
          ("nBJetMedium",          selBJetsAK4_medium.size())
          ("nLep",                 preselLeptons.size())
          ("nGenHadWJets",         genWJets_ptrs.size())
          ("jet1_isGenMatched",    selJet1_Wjj_isGenMatched)
          ("jet2_isGenMatched",    selJet2_Wjj_isGenMatched)
          ("HadW_isGenMatched",    selJet1_Wjj_isGenMatched && selJet2_Wjj_isGenMatched)
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
  delete jetReaderAK8;

  delete inputTree;

  clock.Show("analyze_hadWTagger");

  return EXIT_SUCCESS;
}
