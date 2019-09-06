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

#include "hhAnalysis/bbww/interface/MEMOutput_hh_bb2l.h" // MEMOutput_hh_bb2l
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronReader.h" // RecoElectronReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonReader.h" // RecoMuonReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetReader.h" // RecoJetReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetReaderAK8.h" // RecoJetReaderAK8
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEtReader.h" // RecoMEtReader, RecoMEt
#include "tthAnalysis/HiggsToTauTau/interface/EventInfoReader.h" // EventInfoReader, EventInfo
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
#include "tthAnalysis/HiggsToTauTau/interface/RunLumiEventSelector.h" // RunLumiEventSelector
#include "hhAnalysis/bbww/interface/MEMInterface_hh_bb2l.h" // MEMInterface_hh_bb2l
#include "hhAnalysis/bbww/interface/MEMOutputWriter_hh_bb2l.h" // MEMOutputWriter_hh_bb2l
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronWriter.h" // RecoElectronWriter
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonWriter.h" // RecoMuonWriter
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetWriter.h" // RecoJetWriter
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetWriterAK8.h" // RecoJetWriterAK8
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEtWriter.h" // RecoMEtWriter
#include "tthAnalysis/HiggsToTauTau/interface/EventInfoWriter.h" // EventInfoWriter
#include "tthAnalysis/HiggsToTauTau/interface/MEMPermutationWriter.h" // MEMPermutationWriter::get_maxPermutations_addMEM_pattern()
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // selectObjects(), get_selection(), get_era(), kLoose, kFakeable, kTight
#include "tthAnalysis/HiggsToTauTau/interface/sysUncertOptions.h" // k*_central
#include "tthAnalysis/HiggsToTauTau/interface/memAuxFunctions.h" // get_memObjectBranchName(), get_memPermutationBranchName()
#include "tthAnalysis/HiggsToTauTau/interface/cutFlowTable.h" // cutFlowTableType
#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // createSubdirectory_recursively()
#include "tthAnalysis/HiggsToTauTau/interface/branchEntryTypeAuxFunctions.h" // copyBranches_singleType(), copyBranches_vectorType()
#include "tthAnalysis/HiggsToTauTau/interface/branchEntryType.h" // branchEntryBaseType

#include <boost/algorithm/string/predicate.hpp> // boost::algorithm::starts_with(), boost::algorithm::ends_with()

#include <iostream> // std::cerr, std::fixed
#include <cstdlib> // EXIT_SUCCESS, EXIT_FAILURE
#include <assert.h> // assert

typedef std::vector<std::string> vstring;

/**
 * @brief Compute MEM for events passing preselection in dilepton channel of HH->bbWW analysis
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

  std::cout << "<addMEM_hh_bb2l>:\n";

//--- keep track of time it takes the macro to execute
  TBenchmark clock;
  clock.Start(argv[0]);

//--- read python configuration parameters
  if ( !edm::readPSetsFrom(argv[1])->existsAs<edm::ParameterSet>("process") )
    throw cms::Exception(argv[0])
      << "No ParameterSet 'process' found in configuration file = " << argv[1] << " !!\n";

  const edm::ParameterSet cfg        = edm::readPSetsFrom(argv[1])->getParameter<edm::ParameterSet>("process");
  const edm::ParameterSet cfg_addMEM = cfg.getParameter<edm::ParameterSet>("addMEM_hh_bb2l");
  const vstring central_or_shifts           = cfg_addMEM.getParameter<vstring>("central_or_shift");
  const std::string treeName                = cfg_addMEM.getParameter<std::string>("treeName");
  const std::string selEventsFileName_input = cfg_addMEM.getParameter<std::string>("selEventsFileName_input");
  const bool isMC                           = cfg_addMEM.getParameter<bool>("isMC");
  const bool isDEBUG                        = cfg_addMEM.getParameter<bool>("isDEBUG");
  const bool dryRun                         = cfg_addMEM.getParameter<bool>("dryRun");
  const bool copy_all_branches              = cfg_addMEM.getParameter<bool>("copy_all_branches");
  const bool readGenObjects                 = cfg_addMEM.getParameter<bool>("readGenObjects");
  const bool useNonNominal                  = cfg_addMEM.getParameter<bool>("useNonNominal");
  const bool useNonNominal_jetmet           = useNonNominal || ! isMC;

  const std::string branchName_electrons   = cfg_addMEM.getParameter<std::string>("branchName_electrons");
  const std::string branchName_muons       = cfg_addMEM.getParameter<std::string>("branchName_muons");
  const std::string branchName_jets_ak4    = cfg_addMEM.getParameter<std::string>("branchName_jets_ak4");
  const std::string branchName_jets_ak8    = cfg_addMEM.getParameter<std::string>("branchName_jets_ak8");
  const std::string branchName_subjets_ak8 = cfg_addMEM.getParameter<std::string>("branchName_subjets_ak8");
  const std::string branchName_met         = cfg_addMEM.getParameter<std::string>("branchName_met");
  const vstring copy_histograms            = cfg_addMEM.getParameter<vstring>("copy_histograms");

  const std::string era_string = cfg_addMEM.getParameter<std::string>("era");
  const int era = get_era(era_string);

  if ( central_or_shifts.empty() )
  {
    throw cms::Exception(argv[0]) << "central_or_shift cannot be empty! provide at least 'central'!";
  }

  MEMInterface_hh_bb2l memInterface_hh_bb2l;

  const std::string leptonSelection_string = cfg_addMEM.getParameter<std::string>("leptonSelection");
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
  const int skipEvents       = cfg.getParameter<edm::ParameterSet>("fwliteInput").getParameter<unsigned>("skipEvents");
  const unsigned reportEvery = inputFiles.reportAfter();
  std::cout << " maxEvents = " << maxEvents << "\n skipEvents = " << skipEvents << '\n';

  const fwlite::OutputFiles outputFile(cfg);
  fwlite::TFileService fs = fwlite::TFileService(outputFile.file().data());

  TChain* inputTree = new TChain(treeName.data());
  for ( const std::string & inputFileName: inputFiles.files() )
  {
    std::cout << "input Tree: adding file = " << inputFileName << '\n';
    inputTree->AddFile(inputFileName.data());
  }
  if ( inputTree->GetListOfFiles()->GetEntries() < 1 )
  {
    throw cms::Exception(argv[0]) << "Failed to identify input Tree !!\n";
  }
  
  // CV: need to call TChain::LoadTree before processing first event 
  //     in order to prevent ROOT causing a segmentation violation,
  //     cf. http://root.cern.ch/phpBB3/viewtopic.php?t=10062
  inputTree->LoadTree(0);
  std::cout << "input Tree contains " << inputTree->GetEntries()
            << " Entries in "         << inputTree->GetListOfFiles()->GetEntries() << " files.\n";
  
//--- declare event-level variables
  EventInfo eventInfo;
  EventInfoReader eventInfoReader(&eventInfo);
  eventInfoReader.setBranchAddresses(inputTree);

  const std::string branchName_maxPermutations_addMEM = get_memPermutationBranchName("hh_bb2l", leptonSelection_string);

//--- declare particle collections
  RecoMuonReader* muonReader = new RecoMuonReader(era, branchName_muons, isMC, readGenObjects);
  muonReader->setBranchAddresses(inputTree);
  const RecoMuonCollectionSelectorLoose    preselMuonSelector  (era);
  const RecoMuonCollectionSelectorFakeable fakeableMuonSelector(era);
  const RecoMuonCollectionSelectorTight    tightMuonSelector   (era);
  
  RecoElectronReader* electronReader = new RecoElectronReader(era, branchName_electrons, isMC, readGenObjects);
  electronReader->readUncorrected(useNonNominal);
  electronReader->setBranchAddresses(inputTree);
  const RecoElectronCollectionCleaner electronCleaner(0.3);
  const RecoElectronCollectionSelectorLoose    preselElectronSelector  (era);
  const RecoElectronCollectionSelectorFakeable fakeableElectronSelector(era);
  const RecoElectronCollectionSelectorTight    tightElectronSelector   (era);
  
  RecoJetReader* jetReaderAK4 = new RecoJetReader(era, isMC, branchName_jets_ak4, readGenObjects);
  // CV: apply jet pT cut on JEC upward shift, to make sure pT cut is loose enough
  //     to allow systematic uncertainty on JEC to be estimated on analysis level
  jetReaderAK4->setPtMass_central_or_shift(useNonNominal_jetmet ? kJetMET_central_nonNominal : kJetMET_central);
  jetReaderAK4->setBranchAddresses(inputTree);
  RecoJetCollectionCleaner jetCleanerAK4_dR04(0.4, isDEBUG);
  RecoJetCollectionSelector jetSelectorAK4(era, -1, isDEBUG);

  RecoJetReaderAK8* jetReaderAK8 = new RecoJetReaderAK8(era, branchName_jets_ak8, branchName_subjets_ak8); 
  // TO-DO: implement jet energy scale uncertainties, b-tag weights,  
  //        and jet  pT and (softdrop) mass corrections described in Section 3.4.3 of AN-2018/058 (v4)
  //jetReaderAK8->setPtMass_central_or_shift(useNonNominal_jetmet ? kJetMET_central_nonNominal : kJetMET_central);
  //jetReaderAK8->read_ptMass_systematics(isMC);
  //jetReaderAK8->read_BtagWeight_systematics(isMC);
  jetReaderAK8->setBranchAddresses(inputTree);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR08(0.8, isDEBUG);
  RecoJetCollectionSelectorAK8_hh_bbWW_Hbb jetSelectorAK8_Hbb(era, -1, isDEBUG);

//--- declare missing transverse energy
  RecoMEtReader* metReader = new RecoMEtReader(era, isMC, branchName_met);
  metReader->setMEt_central_or_shift(useNonNominal_jetmet ? kJetMET_central_nonNominal : kJetMET_central);
  metReader->read_ptPhi_systematics(isMC);
  metReader->setBranchAddresses(inputTree);

  std::string outputTreeName = treeName;
  std::string outputDirName = "";
  if ( outputTreeName.find_last_of("/") != std::string::npos )
  {
    std::size_t pos = outputTreeName.find_last_of("/");
    outputTreeName = std::string(outputTreeName, pos + 1);
    outputDirName  = std::string(outputTreeName, 0, pos);
  }
  if ( !outputDirName.empty() )
  {
    TDirectory* dir = createSubdirectory_recursively(fs, outputDirName.data());
    dir->cd();
  }
  else
  {
    fs.cd();
  }
  TTree* outputTree = new TTree(outputTreeName.data(), outputTreeName.data());

  RecoMuonWriter *     muonWriter      = nullptr;
  RecoElectronWriter * electronWriter  = nullptr;
  RecoJetWriter *      jetWriterAK4    = nullptr;
  RecoJetWriterAK8 *   jetWriterAK8    = nullptr;
  RecoMEtWriter *      metWriter       = nullptr;
  EventInfoWriter *    eventInfoWriter = nullptr;

  std::map<std::string, branchEntryBaseType*> branchesToKeep;
  if ( copy_all_branches )
  {
    eventInfoWriter = new EventInfoWriter(eventInfo.is_signal(), eventInfo.is_mc());
    eventInfoWriter->setBranches(outputTree);

    muonWriter = new RecoMuonWriter(era, isMC, Form("n%s", branchName_muons.data()), branchName_muons);
    muonWriter->setBranches(outputTree);
    electronWriter = new RecoElectronWriter(era, isMC, Form("n%s", branchName_electrons.data()), branchName_electrons);
    electronWriter->writeUncorrected(useNonNominal);
    electronWriter->setBranches(outputTree);
    jetWriterAK4 = new RecoJetWriter(era, isMC, Form("n%s", branchName_jets_ak4.data()), branchName_jets_ak4);
    jetWriterAK4->setPtMass_central_or_shift(useNonNominal_jetmet ? kJetMET_central_nonNominal : kJetMET_central);
    jetWriterAK4->setBranches(outputTree);
    jetWriterAK8 = new RecoJetWriterAK8(era, Form("n%s", branchName_jets_ak8.data()), branchName_jets_ak8, Form("n%s", branchName_subjets_ak8.data()), branchName_subjets_ak8);
    // TO-DO: implement jet energy scale uncertainties, b-tag weights,  
    //        and jet  pT and (softdrop) mass corrections described in Section 3.4.3 of AN-2018/058 (v4)
    //jetWriterAK8->setPtMass_central_or_shift(useNonNominal_jetmet ? kJetMET_central_nonNominal : kJetMET_central);
    //jetWriterAK8->write_ptMass_systematics(isMC);
    //jetWriterAK8->write_BtagWeight_systematics(isMC);
    jetWriterAK8->setBranches(outputTree);
    metWriter = new RecoMEtWriter(era, isMC, branchName_met);
    metWriter->setPtPhi_central_or_shift(useNonNominal_jetmet ? kJetMET_central_nonNominal : kJetMET_central);
    metWriter->write_ptPhi_systematics(isMC);
    metWriter->setBranches(outputTree);

    vstring outputCommands_string = {
      "keep *",
      Form("drop %s", eventInfoWriter->getBranchName_run().data()),
      Form("drop %s", eventInfoWriter->getBranchName_lumi().data()),
      Form("drop %s", eventInfoWriter->getBranchName_event().data()),
      Form("drop n%s", branchName_muons.data()),
      Form("drop n%s_*", branchName_muons.data()),
      Form("drop %s_*", branchName_muons.data()),
      Form("drop n%s", branchName_electrons.data()),
      Form("drop n%s_*", branchName_electrons.data()),
      Form("drop %s_*", branchName_electrons.data()),
      Form("drop n%s", branchName_jets_ak4.data()),
      Form("drop n%s_*", branchName_jets_ak4.data()),
      Form("drop %s_*", branchName_jets_ak4.data()),
      Form("drop n%s", branchName_jets_ak8.data()),
      Form("drop %s_*", branchName_jets_ak8.data()),
      Form("drop n%s", branchName_subjets_ak8.data()),
      Form("drop %s_*", branchName_subjets_ak8.data()),
      Form("drop %s_*", branchName_met.data())
    };
    std::vector<outputCommandEntry> outputCommands = getOutputCommands(outputCommands_string);
    std::map<std::string, bool> isBranchToKeep = getBranchesToKeep(inputTree, outputCommands);
    copyBranches_singleType(inputTree, outputTree, isBranchToKeep, branchesToKeep);
    copyBranches_vectorType(inputTree, outputTree, isBranchToKeep, branchesToKeep);
  }

  if ( !branchesToKeep.count(branchName_maxPermutations_addMEM) )
  {
    throw cmsException(__func__, __LINE__)
      << "No such branch: " << branchName_maxPermutations_addMEM;
  }

  const std::string branchName_memOutput = get_memObjectBranchName(
    "hh_bb2l", leptonSelection_string, "", ""
  );
  const std::string branchName_memOutput_missingBJet = Form("%s_missingBJet", branchName_memOutput.data());
  std::map<std::string, MEMOutputWriter_hh_bb2l *> memWriter;
  std::map<std::string, MEMOutputWriter_hh_bb2l *> memWriter_missingBJet;
  for ( const std::string & central_or_shift: central_or_shifts )
  {
    const std::string branchName_memOutput_cos(Form("%s_%s", branchName_memOutput.data(), central_or_shift.data()));
    memWriter[central_or_shift] = new MEMOutputWriter_hh_bb2l(
      Form("n%s", branchName_memOutput_cos.data()), branchName_memOutput_cos
    );
    memWriter[central_or_shift]->setBranches(outputTree);
    const std::string branchName_memOutput_missingBJet_cos(Form("%s_%s", branchName_memOutput_missingBJet.data(), central_or_shift.data()));
    memWriter_missingBJet[central_or_shift] = new MEMOutputWriter_hh_bb2l(
      Form("n%s", branchName_memOutput_missingBJet_cos.data()), branchName_memOutput_missingBJet_cos
    );
    memWriter_missingBJet[central_or_shift]->setBranches(outputTree);
    std::cout << "writing MEMOutput_hh_bb2l objects for systematic " << central_or_shift
              << " to branch = '" << branchName_memOutput_cos << "'\n";
  }

  const int numEntries = inputTree->GetEntries();
  int analyzedEntries = 0;
  int selectedEntries = 0;
  int memComputations = 0;
  cutFlowTableType cutFlowTable;
  for ( int idxEntry = skipEvents; idxEntry < numEntries && (maxEvents == -1 || idxEntry < (skipEvents + maxEvents)); ++idxEntry )
  {

    if ( isDEBUG )
    {
      std::cout << std::string(80, '-') << '\n';
    }

    if ( run_lumi_eventSelector && run_lumi_eventSelector->areWeDone() )
    {
      break;
    }

    inputTree->GetEntry(idxEntry);

    if ( (idxEntry >= 0 && (idxEntry % reportEvery) == 0) || isDEBUG )
    {
      std::cout << "processing Entry " << idxEntry << ": " << eventInfo
                << " (" << selectedEntries << " Entries selected)\n";
    }
    ++analyzedEntries;
    
    cutFlowTable.update("read from file");

    if ( run_lumi_eventSelector && !(*run_lumi_eventSelector)(eventInfo) )
    {
      continue;
    }
    cutFlowTable.update("run:ls:event selection");

//--- build collections of electrons, muons and hadronic taus;
//    resolve overlaps in order of priority: muon, electron,
    const std::vector<RecoMuon> muons = muonReader->read();
    const std::vector<const RecoMuon *> muon_ptrs = convert_to_ptrs(muons);
    // CV: no cleaning needed for muons, as they have the highest priority in the overlap removal
    const std::vector<const RecoMuon *> cleanedMuons  = muon_ptrs;
    const std::vector<const RecoMuon *> preselMuons   = preselMuonSelector  (cleanedMuons);
    const std::vector<const RecoMuon *> fakeableMuons = fakeableMuonSelector(preselMuons);
    const std::vector<const RecoMuon *> tightMuons    = tightMuonSelector   (preselMuons);
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
    const std::vector<const RecoElectron *> preselElectrons   = preselElectronSelector(cleanedElectrons);
    const std::vector<const RecoElectron *> fakeableElectrons = fakeableElectronSelector(preselElectrons);
    const std::vector<const RecoElectron *> tightElectrons    = tightElectronSelector(preselElectrons);
    const std::vector<const RecoElectron *> selElectrons      = selectObjects(
      leptonSelection, preselElectrons, fakeableElectrons, tightElectrons
    );
    if ( isDEBUG )
    {
      printCollection("selElectrons", selElectrons);
    }

    const std::vector<const RecoLepton*> preselLeptonsFull = mergeLeptonCollections(preselElectrons, preselMuons, isHigherConePt);
    const std::vector<const RecoLepton*> fakeableLeptonsFull = mergeLeptonCollections(fakeableElectrons, fakeableMuons, isHigherConePt);
    const std::vector<const RecoLepton*> tightLeptonsFull = mergeLeptonCollections(tightElectrons, tightMuons, isHigherConePt);

    const std::vector<const RecoLepton*> preselLeptons = pickFirstNobjects(preselLeptonsFull, 2);
    const std::vector<const RecoLepton*> fakeableLeptons = pickFirstNobjects(fakeableLeptonsFull, 2);
    const std::vector<const RecoLepton*> tightLeptons = getIntersection(fakeableLeptons, tightLeptonsFull, isHigherConePt);

//--- build collections of jets 
    const std::vector<RecoJet> jets_ak4 = jetReaderAK4->read();
    const std::vector<const RecoJet*> jet_ptrs_ak4 = convert_to_ptrs(jets_ak4);
    const std::vector<RecoJetAK8> jets_ak8 = jetReaderAK8->read();
    const std::vector<const RecoJetAK8*> jet_ptrs_ak8 = convert_to_ptrs(jets_ak8);

    const RecoMEt met = metReader->read();

    std::map<std::string, std::vector<MEMOutput_hh_bb2l>> memOutputs_hh_bb2l;
    std::map<std::string, std::vector<MEMOutput_hh_bb2l>> memOutputs_hh_bb2l_missingBJet;
    for ( const std::string & central_or_shift: central_or_shifts )
    {
      memOutputs_hh_bb2l[central_or_shift] = {};
      memOutputs_hh_bb2l_missingBJet[central_or_shift] = {};
    }

//--- fill the branches here since because we want to re-use the readers
//--- however, the readers obtain pointers to gen level objects and pass them to the reco objects
//--- thus, if we try to re-read the objects, these pointers will be overwritten and become invalid
//--- therefore, we have to write the reco objects before re-reading new stuff
    if ( copy_all_branches )
    {
      eventInfoWriter->write(eventInfo);
      muonWriter->write(preselMuons);
      electronWriter->write(preselElectrons);
      jetWriterAK4->write(jet_ptrs_ak4); // save central
      jetWriterAK8->write(jet_ptrs_ak8); // save central
      metWriter->write(met); // save central

      for ( const auto & branchEntry: branchesToKeep )
      {
        branchEntry.second->copyBranch();
      }
    }

    const Int_t maxPermutations_addMEM_hh_bb2l = branchesToKeep.at(branchName_maxPermutations_addMEM)->getValue_int();
    if ( isDEBUG )
    {
      std::cout << "Found " << maxPermutations_addMEM_hh_bb2l << " possible combination(s) to compute MEM\n";
    }
    if ( maxPermutations_addMEM_hh_bb2l >= 1 )
    {
      int idxPermutation = -1;
      const std::vector<const RecoLepton*> selLeptons = mergeLeptonCollections(selElectrons, selMuons);
      for ( std::size_t selLepton_lead_idx = 0; selLepton_lead_idx < selLeptons.size(); ++selLepton_lead_idx )
      {
        const RecoLepton * selLepton_lead = selLeptons[selLepton_lead_idx];
        for ( std::size_t selLepton_sublead_idx = selLepton_lead_idx + 1; selLepton_sublead_idx < selLeptons.size(); ++selLepton_sublead_idx )
        {
          const RecoLepton * selLepton_sublead = selLeptons[selLepton_sublead_idx];
          for ( const std::string central_or_shift: central_or_shifts )
          {
            checkOptionValidity(central_or_shift, isMC);
            const int jetPt_option = getJet_option(central_or_shift, isMC);
            const int met_option   = getMET_option(central_or_shift, isMC);

            if ( jetPt_option == kJetMET_central &&
                 met_option   == kJetMET_central &&
		 central_or_shift != "central")
            {
              std::cout << "Skipping systematics: " << central_or_shift << '\n';
              continue;
            }
            if(isDEBUG)
            {
              std::cout << "Attempting to evaluate the MEM score for systematics: " << central_or_shift << '\n';
            }

            jetReaderAK4->setPtMass_central_or_shift(jetPt_option);
	    //jetReaderAK8->setPtMass_central_or_shift(jetPt_option);
            metReader->setMEt_central_or_shift(met_option);

            const std::vector<RecoJet> jets_ak4_mem = jetReaderAK4->read();
            const std::vector<const RecoJet*> jet_ptrs_ak4_mem = convert_to_ptrs(jets_ak4_mem);
            const std::vector<const RecoJet*> cleanedJetsAK4_wrtLeptons = jetCleanerAK4_dR04(jet_ptrs_ak4_mem, fakeableLeptons);
            const std::vector<RecoJetAK8> jets_ak8_mem = jetReaderAK8->read();
            const std::vector<const RecoJetAK8*> jet_ptrs_ak8_mem = convert_to_ptrs(jets_ak8_mem);
            const std::vector<const RecoJetAK8*> cleanedJetsAK8_wrtLeptons = jetCleanerAK8_dR08(jet_ptrs_ak8_mem, fakeableLeptons);
            const std::vector<const RecoJetAK8*> selJetsAK8_Hbb = jetSelectorAK8_Hbb(cleanedJetsAK8_wrtLeptons, isHigherCSV_ak8);
            const std::vector<const RecoJet*> selJetsAK4_Hbb = jetSelectorAK4(cleanedJetsAK4_wrtLeptons, isHigherCSV);
	    //-------------------------------------------------------------------
	    // select the two jets from the H->bb decay from either the AK4 (resolved H->bb) or AK8 (boosted H->bb) collection
	    //
	    // WARNING: logic to select the two jets from H->bb decay needs to match the code in analyze_hh_bb2l.cc !!
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

	    const RecoMEt met_mem = metReader->read();
	    
	    if ( selJet1_Hbb && selJet2_Hbb ) 
	    {
	      ++idxPermutation;
	      if ( idxPermutation < maxPermutations_addMEM_hh_bb2l )
	      {
	        std::cout << "computing MEM for " << eventInfo
		  	  << " (idxPermutation = " << idxPermutation << "):\n"
                             "inputs:\n"
                          << " leading lepton:     " << *(static_cast<const ChargedParticle *>(selLepton_lead)) << "\n"
                          << " subleading lepton:  " << *(static_cast<const ChargedParticle *>(selLepton_sublead)) << "\n"
		          << " b-jet #1:  " << *(static_cast<const Particle *>(selJet1_Hbb)) << "\n"
                          << " b-jet #2:  " << *(static_cast<const Particle *>(selJet2_Hbb)) << "\n"
			  << " MET:                " << met << "\n";

  	        MEMOutput_hh_bb2l memOutput_hh_bb2l;
                MEMOutput_hh_bb2l memOutput_hh_bb2l_missingBJet;
	        if ( dryRun )
	        {
	  	  memOutput_hh_bb2l.fillInputs(selLepton_lead, selLepton_sublead, selJet1_Hbb, selJet2_Hbb);
		  memOutput_hh_bb2l_missingBJet.fillInputs(selLepton_lead, selLepton_sublead, selJet1_Hbb, nullptr);
	        }
	        else
	        {
	  	  memOutput_hh_bb2l = memInterface_hh_bb2l(selLepton_lead, selLepton_sublead, selJet1_Hbb, selJet2_Hbb, met_mem);
		  memOutput_hh_bb2l_missingBJet = memInterface_hh_bb2l(selLepton_lead, selLepton_sublead, selJet1_Hbb, nullptr, met);
	        }
	        memOutput_hh_bb2l.eventInfo_ = eventInfo;
	        memOutput_hh_bb2l_missingBJet.eventInfo_ = eventInfo;
	        std::cout << "output (" << central_or_shift << "): " << memOutput_hh_bb2l;
	        std::cout << "output (missing b-jet, " << central_or_shift << "): " << memOutput_hh_bb2l_missingBJet;
	        memOutputs_hh_bb2l[central_or_shift].push_back(memOutput_hh_bb2l);
	        memOutputs_hh_bb2l_missingBJet[central_or_shift].push_back(memOutput_hh_bb2l_missingBJet);

		++memComputations;
	      } // idxPermutation < maxPermutations_addMEM_hh_bb2l
	      else if ( idxPermutation == maxPermutations_addMEM_hh_bb2l ) // CV: print warning only once per event
	      {
	        std::cout << "Warning in " << eventInfo << ":\n"
		             "Number of permutations exceeds 'maxPermutations_addMEM_hh_bb2l' = "
			  << maxPermutations_addMEM_hh_bb2l << " --> skipping MEM computation after "
			  << maxPermutations_addMEM_hh_bb2l << " permutations !!\n";
	      }

	      if ( isDEBUG )
	      {
	        std::cout << "#memOutputs_hh_bb2l = " << memOutputs_hh_bb2l[central_or_shift].size() << '\n';	      
	      }
	    } // selJet1_Hbb && selJet2_Hbb
	  } // central_or_shift
	} // selLepton_sublead_idx
      } // selLepton_lead_idx
    } // maxPermutations_addMEM_hh_bb2l >= 1
    
    for ( const std::string & central_or_shift: central_or_shifts )
    {
      memWriter[central_or_shift]->write(memOutputs_hh_bb2l[central_or_shift]);
      memWriter_missingBJet[central_or_shift]->write(memOutputs_hh_bb2l_missingBJet[central_or_shift]);
    }

    outputTree->Fill();
    ++selectedEntries;
  } // idxEntry

  std::cout << "num. Entries = "  << numEntries << "\n"
               " analyzed = "     << analyzedEntries << "\n"
               " selected = "     << selectedEntries << "\n"
               "#MEM computations = " << memComputations << "\n"
               "cut-flow table\n" << cutFlowTable << "\n"
               "output Tree:\n";
  if(isDEBUG)
  {
    outputTree->Print();
  }

  delete run_lumi_eventSelector;
  delete muonReader;
  delete electronReader;
  delete jetReaderAK4;
  delete jetReaderAK8;
  delete metReader;

  for ( auto & kv: memWriter )
  {
    if ( kv.second )
    {
      delete kv.second;
      kv.second = nullptr;
    }
  }
  for ( auto & kv: memWriter_missingBJet )
  {
    if ( kv.second )
    {
      delete kv.second;
      kv.second = nullptr;
    }
  }

  delete inputTree;

//--- copy histograms keeping track of number of processed events from input files to output file
  std::cout << "copying histograms:\n";
  std::map<std::string, TH1*> histograms;
  for ( const std::string & inputFileName: inputFiles.files() )
  {
    TFile* inputFile = new TFile(inputFileName.data());
    if ( !inputFile || inputFile -> IsZombie() )
    {
      throw cms::Exception(argv[0]) << "Failed to open input File = '" << inputFileName << "' !!\n";
    }

    for ( const std::string & histogramName: copy_histograms )
    {
      if ( inputFiles.files().size() > 1 )
      {
        std::cout << ' ' << histogramName << " from input File = '" << inputFileName << "'\n";
      }
      else
      {
        std::cout << ' ' << histogramName << '\n';
      }
      TH1* histogram_input = dynamic_cast<TH1*>(inputFile->Get(histogramName.data()));
      if ( !histogram_input )
      {
        continue;
      }
      TH1* histogram_output = histograms[histogramName];
      if ( histogram_output )
      {
        histogram_output->Add(histogram_input);
      }
      else
      {
        if     ( dynamic_cast<TH1F*>(histogram_input) )
        {
          histogram_output = fs.make<TH1F>(*(dynamic_cast<TH1F*>(histogram_input)));
        }
        else if( dynamic_cast<TH1D*>(histogram_input) )
        {
          histogram_output = fs.make<TH1D>(*(dynamic_cast<TH1D*>(histogram_input)));
        }
        assert(histogram_output);
        histograms[histogramName] = histogram_output;
      } // ! histogram_output
    } // histogramName
    delete inputFile;
  } // inputFileName

  clock.Show("addMEM_hh_bb2l");

  return EXIT_SUCCESS;
}
