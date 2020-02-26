#include "FWCore/ParameterSet/interface/ParameterSet.h" // edm::ParameterSet
#include "FWCore/PythonParameterSet/interface/MakeParameterSets.h" // edm::readPSetsFrom()
#include "FWCore/Utilities/interface/Exception.h" // cms::Exception
#include "PhysicsTools/FWLite/interface/TFileService.h" // fwlite::TFileService
#include "DataFormats/FWLite/interface/InputSource.h" // fwlite::InputSource
#include "DataFormats/FWLite/interface/OutputFiles.h" // fwlite::OutputFiles
#include "DataFormats/Math/interface/LorentzVector.h" // math::PtEtaPhiMLorentzVector

#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronReader.h" // RecoElectronReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonReader.h" // RecoMuonReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetReader.h" // RecoJetReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetReaderAK8.h" // RecoJetReaderAK8
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEtReader.h" // RecoMEtReader, RecoMEt
#include "tthAnalysis/HiggsToTauTau/interface/EventInfoReader.h" // EventInfoReader, EventInfo
#include "tthAnalysis/HiggsToTauTau/interface/GenLeptonReader.h" // GenLeptonReader
#include "tthAnalysis/HiggsToTauTau/interface/GenParticleReader.h" // GenParticleReader
#include "tthAnalysis/HiggsToTauTau/interface/TMVAInterface.h" // TMVAInterface
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
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronWriter.h" // RecoElectronWriter
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonWriter.h" // RecoMuonWriter
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetWriter.h" // RecoJetWriter
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetWriterAK8.h" // RecoJetWriterAK8
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEtWriter.h" // RecoMEtWriter
#include "tthAnalysis/HiggsToTauTau/interface/EventInfoWriter.h" // EventInfoWriter
#include "tthAnalysis/HiggsToTauTau/interface/MEMPermutationWriter.h" // MEMPermutationWriter::get_maxPermutations_addMEM_pattern()
#include "tthAnalysis/HiggsToTauTau/interface/GenParticleWriter.h" // GenParticleWriter
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // selectObjects(), get_selection(), get_era(), kLoose, kFakeable, kTight, convert_to_genParticles
#include "tthAnalysis/HiggsToTauTau/interface/sysUncertOptions.h" // k*_central
#include "tthAnalysis/HiggsToTauTau/interface/memAuxFunctions.h" // get_memObjectBranchName(), get_memPermutationBranchName()
#include "tthAnalysis/HiggsToTauTau/interface/cutFlowTable.h" // cutFlowTableType
#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // createSubdirectory_recursively()
#include "tthAnalysis/HiggsToTauTau/interface/branchEntryTypeAuxFunctions.h" // copyBranches_singleType(), copyBranches_vectorType()
#include "tthAnalysis/HiggsToTauTau/interface/branchEntryType.h" // branchEntryBaseType
#include "tthAnalysis/HiggsToTauTau/interface/copyHistograms.h" // copyHistograms

#include "hhAnalysis/multilepton/interface/RecoJetCollectionSelectorAK8_hh_Wjj.h" // RecoJetSelectorAK8_hh_Wjj

#include "hhAnalysis/bbww/interface/RecoJetCollectionSelectorAK8_hh_bbWW_Hbb.h" // RecoJetSelectorAK8_hh_bbWW_Hbb
#include "hhAnalysis/bbww/interface/MEMInterface_hh_bb1l.h" // MEMInterface_hh_bb1l
#include "hhAnalysis/bbww/interface/MEMOutputWriter_hh_bb1l.h" // MEMOutputWriter_hh_bb1l
#include "hhAnalysis/bbww/interface/MEMOutput_hh_bb1l.h" // MEMOutput_hh_bb1l
#include "hhAnalysis/bbww/interface/JetPair.h" // initialize_mva_Wjj
#include "hhAnalysis/bbww/interface/GenParticleMatcherFromHiggs.h" // GenParticleMatcherFromHiggs
#include "hhAnalysis/bbww/interface/GenParticleMatcherFromTop.h" // GenParticleMatcherFromTop
#include "hhAnalysis/bbww/interface/jetSelectionAuxFunctions.h" // selJetsType_Hbb, selectJets_Hbb, selJetsType_Wjj, selectJets_Wjj

#include <TChain.h> // TChain
#include <TTree.h> // TTree
#include <TBenchmark.h> // TBenchmark
#include <TString.h> // TString, Form
#include <TError.h> // gErrorAbortLevel, kError

#include <boost/algorithm/string/predicate.hpp> // boost::algorithm::starts_with(), boost::algorithm::ends_with()

#include <iostream> // std::cerr, std::fixed
#include <cstdlib> // EXIT_SUCCESS, EXIT_FAILURE
#include <assert.h> // assert
#include <regex> // std::regex_match(), std::regex, std::smatch

typedef std::vector<std::string> vstring;

MEMOutput_hh_bb1l 
compMEM(const EventInfo& eventInfo,
        const RecoLepton* selLepton, const RecoJetBase* selJet1_Wjj, const RecoJetBase* selJet2_Wjj,
        const RecoJetBase* selJet1_Hbb, const RecoJetBase* selJet2_Hbb, 
        const RecoMEt& met, 	
	MEMInterface_hh_bb1l& memInterface, bool switchToGen, bool dryRun,
        int& idxPermutation, int maxPermutations, 
	const std::string& branchName_memOutput, const std::string& central_or_shift, bool isDEBUG)
{
  MEMOutput_hh_bb1l memOutput;
  if ( maxPermutations == -1 || idxPermutation <= maxPermutations )
  {
    ++idxPermutation;
    if ( isDEBUG )
    {
      std::cout << "computing MEM for branch " << "'" << branchName_memOutput << "'" << std::endl;
      std::cout << eventInfo << " (idxPermutation = " << idxPermutation << "):" << std::endl;
      std::cout << "inputs:" << std::endl;
      std::cout << " lepton:            " << *(static_cast<const ChargedParticle *>(selLepton)) << std::endl;
      std::cout << " jet from W->jj #1: " << *(static_cast<const Particle *>(selJet1_Wjj)) << std::endl;
      std::cout << " jet from W->jj #2: ";
      if ( selJet2_Wjj )
      {
        std::cout << *(static_cast<const Particle *>(selJet2_Wjj)) << std::endl;
      }
      else
      {
        std::cout << "N/A" << std::endl;
      }
      std::cout << " b-jet #1:          " << *(static_cast<const Particle *>(selJet1_Hbb)) << std::endl;
      std::cout << " b-jet #2:          ";
      if ( selJet2_Hbb )
      {
        std::cout << *(static_cast<const Particle *>(selJet2_Hbb)) << std::endl;
      }
      else
      {
        std::cout << "N/A" << std::endl;
      }
      std::cout << " MET:               " << met << std::endl;
    }

    if ( selLepton && (selJet1_Wjj || selJet2_Wjj) && (selJet1_Hbb || selJet2_Hbb) )
    {
      if ( dryRun )
      {
        memOutput.fillInputs(selLepton, selJet1_Wjj, selJet2_Wjj, selJet1_Hbb, selJet2_Hbb);
      }
      else
      {
        memOutput = memInterface(selLepton, selJet1_Wjj, selJet2_Wjj, selJet1_Hbb, selJet2_Hbb, met, switchToGen);
      }

      if ( isDEBUG )
      {
        std::cout << "output (" << central_or_shift << "): " << memOutput << std::endl;
      }
    }
  } 
  else 
  {
    // CV: print warning only once per event
    std::cout << "Warning in " << eventInfo << ":" << std::endl;
    std::cout << "Number of permutations exceeds 'maxPermutations_addMEM_hh_bb1l' = " << maxPermutations 
	      << " --> skipping MEM computation for branch " << "'" << branchName_memOutput << "'" 
	      << " after " << maxPermutations << " permutations !!" << std::endl;
  }
  memOutput.eventInfo_ = eventInfo; 
  return memOutput;
}

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

  std::cout << "<addMEM_hh_bb1l>:\n";

//--- keep track of time it takes the macro to execute
  TBenchmark clock;
  clock.Start(argv[0]);

//--- read python configuration parameters
  if ( !edm::readPSetsFrom(argv[1])->existsAs<edm::ParameterSet>("process") )
    throw cms::Exception(argv[0])
      << "No ParameterSet 'process' found in configuration file = " << argv[1] << " !!\n";

  const edm::ParameterSet cfg                  = edm::readPSetsFrom(argv[1])->getParameter<edm::ParameterSet>("process");
  const edm::ParameterSet cfg_addMEM           = cfg.getParameter<edm::ParameterSet>("addMEM_hh_bb1l");
  const vstring central_or_shifts_mem          = cfg_addMEM.getParameter<vstring>("central_or_shift_mem");
  const std::string treeName                   = cfg_addMEM.getParameter<std::string>("treeName");
  const std::string selEventsFileName_input    = cfg_addMEM.getParameter<std::string>("selEventsFileName_input");
  const std::string process_string             = cfg_addMEM.getParameter<std::string>("process");
  const bool isMC                              = cfg_addMEM.getParameter<bool>("isMC");
  const bool isMC_HH                           = isMC && process_string.find("hh_bbvv")!= std::string::npos;
  const bool isMC_TT                           = isMC && process_string.find("TT")     != std::string::npos;
  const bool addMEM_forGenParticles            = cfg_addMEM.getParameter<bool>("addMEM_forGenParticles");
  const bool isDEBUG                           = cfg_addMEM.getParameter<bool>("isDEBUG");
  const bool dryRun                            = cfg_addMEM.getParameter<bool>("dryRun");
  const bool copy_all_branches                 = cfg_addMEM.getParameter<bool>("copy_all_branches");
  const bool readGenObjects                    = cfg_addMEM.getParameter<bool>("readGenObjects");
  const bool jetCleaningByIndex                = cfg_addMEM.getParameter<bool>("jetCleaningByIndex");
  const bool useNonNominal                     = cfg_addMEM.getParameter<bool>("useNonNominal");
  const bool useNonNominal_jetmet              = useNonNominal || ! isMC;
  const bool method_MEM                        = cfg_addMEM.getParameter<bool>("method_mem");

  const std::string branchName_electrons       = cfg_addMEM.getParameter<std::string>("branchName_electrons");
  const std::string branchName_muons           = cfg_addMEM.getParameter<std::string>("branchName_muons");
  const std::string branchName_jets_ak4        = cfg_addMEM.getParameter<std::string>("branchName_jets_ak4");
  const std::string branchName_jets_ak8        = cfg_addMEM.getParameter<std::string>("branchName_jets_ak8");
  const std::string branchName_subjets_ak8     = cfg_addMEM.getParameter<std::string>("branchName_subjets_ak8");
  const std::string branchName_jets_ak8LS      = cfg_addMEM.getParameter<std::string>("branchName_jets_ak8LS");
  const std::string branchName_subjets_ak8LS   = cfg_addMEM.getParameter<std::string>("branchName_subjets_ak8LS");
  const std::string branchName_met             = cfg_addMEM.getParameter<std::string>("branchName_met");

  const int mem_maxWJetPairs = cfg_addMEM.getParameter<int>("mem_maxWJetPairs");
  const int mem_maxWJets = cfg_addMEM.getParameter<int>("mem_maxWJets");

  // branches specific to HH->bbWW signal events
  std::string branchName_genLeptons;
  std::string branchName_genNeutrinos;
  std::string branchName_genParticlesFromHiggs;
  std::string branchName_genWJets;
  // branches specific to tt+jets background events   
  std::string branchName_genLeptonsFromTop;
  std::string branchName_genNeutrinosFromTop;
  std::string branchName_genBJetsFromTop;
  std::string branchName_genWJetsFromTop;  
  if ( addMEM_forGenParticles )
  {
    edm::ParameterSet cfg_branchNames_genParticles = cfg_addMEM.getParameter<edm::ParameterSet>("branchNames_genParticles");
    if ( isMC_HH )
    {
      branchName_genLeptons = cfg_branchNames_genParticles.getParameter<std::string>("branchName_genLeptons");
      branchName_genNeutrinos = cfg_branchNames_genParticles.getParameter<std::string>("branchName_genNeutrinos");
      branchName_genParticlesFromHiggs = cfg_branchNames_genParticles.getParameter<std::string>("branchName_genParticlesFromHiggs");
      branchName_genWJets = cfg_branchNames_genParticles.getParameter<std::string>("branchName_genWJets");
    }
    else if ( isMC_TT )
    {
      branchName_genLeptonsFromTop = cfg_branchNames_genParticles.getParameter<std::string>("branchName_genLeptonsFromTop");
      branchName_genNeutrinosFromTop = cfg_branchNames_genParticles.getParameter<std::string>("branchName_genNeutrinosFromTop");
      branchName_genBJetsFromTop = cfg_branchNames_genParticles.getParameter<std::string>("branchName_genBJetsFromTop");
      branchName_genWJetsFromTop = cfg_branchNames_genParticles.getParameter<std::string>("branchName_genWJetsFromTop");
    }
  }

  GenParticleMatcherFromHiggs genParticleMatcherFromHiggs;
  GenParticleMatcherFromTop genParticleMatcherFromTop;

  const vstring copy_histograms = cfg_addMEM.getParameter<vstring>("copy_histograms");
  std::vector<std::regex> copy_histograms_regex;
  std::transform(
    copy_histograms.begin(), copy_histograms.end(), std::back_inserter(copy_histograms_regex),
    [](const std::string & copy_histogram_regex) -> std::regex { return std::regex(copy_histogram_regex); }
  );

  const std::string era_string = cfg_addMEM.getParameter<std::string>("era");
  const int era = get_era(era_string);

  if ( central_or_shifts_mem.empty() )
  {
    throw cms::Exception(argv[0]) << "central_or_shift cannot be empty! provide at least 'central'!";
  }

  std::vector<std::string> central_or_shifts;
  for(const std::string & central_or_shift_mem: central_or_shifts_mem)
  {
    if(std::find(central_or_shifts.begin(), central_or_shifts.end(), central_or_shift_mem) == central_or_shifts.end())
    {
      central_or_shifts.push_back(central_or_shift_mem);
    }
  }
  const int nof_central_or_shift_mem = central_or_shifts_mem.size();

  MEMInterface_hh_bb1l memInterface_hh_bb1l;

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

  //const std::string branchName_maxPermutations_addMEM = get_memPermutationBranchName("hh_bb1l", leptonSelection_string);
  const std::string branchName_maxPermutations_addMEM = cfg_addMEM.getParameter<std::string>("branchName_maxPermutations_addMEM");

//--- declare particle collections
  RecoMuonReader* muonReader = new RecoMuonReader(era, branchName_muons, isMC, readGenObjects);
  muonReader->setBranchAddresses(inputTree);
  const RecoMuonCollectionSelectorLoose    preselMuonSelector  (era);
  const RecoMuonCollectionSelectorFakeable fakeableMuonSelector(era);
  const RecoMuonCollectionSelectorTight    tightMuonSelector   (era);
  
  RecoElectronReader* electronReader = new RecoElectronReader(era, branchName_electrons, isMC, readGenObjects);
  electronReader->setBranchAddresses(inputTree);
  const RecoElectronCollectionCleaner electronCleaner(0.3);
  const RecoElectronCollectionSelectorLoose    preselElectronSelector  (era);
  const RecoElectronCollectionSelectorFakeable fakeableElectronSelector(era);
  const RecoElectronCollectionSelectorTight    tightElectronSelector   (era);
  
  RecoJetReader* jetReaderAK4 = new RecoJetReader(era, isMC, branchName_jets_ak4, readGenObjects);
  // CV: apply jet pT cut on JEC upward shift, to make sure pT cut is loose enough
  //     to allow systematic uncertainty on JEC to be estimated on analysis level
  jetReaderAK4->setPtMass_central_or_shift(useNonNominal_jetmet ? kJetMET_central_nonNominal : kJetMET_central);
  jetReaderAK4->read_ptMass_systematics(isMC);
  jetReaderAK4->read_btag_systematics(isMC);
  jetReaderAK4->setBranchAddresses(inputTree);
  RecoJetCollectionCleaner jetCleanerAK4_dR04(0.4, isDEBUG);
  RecoJetCollectionCleanerByIndex jetCleanerAK4_byIndex(isDEBUG);
  RecoJetCollectionCleaner jetCleanerAK4_dR08(0.8, isDEBUG);
  RecoJetCollectionCleaner jetCleanerAK4_dR12(1.2, isDEBUG);
  RecoJetCollectionSelector jetSelectorAK4_Hbb(era, -1, isDEBUG);
  RecoJetCollectionSelector jetSelectorAK4_Wjj(era, -1, isDEBUG);
  //jetSelectorAK4_Wjj.getSelector().set_max_absEta(4.7);
  RecoJetCollectionSelectorBtagLoose jetSelectorAK4_bTagLoose(era, -1, isDEBUG);
  RecoJetCollectionSelectorBtagMedium jetSelectorAK4_bTagMedium(era, -1, isDEBUG);

  RecoJetReaderAK8* jetReaderAK8 = new RecoJetReaderAK8(era, branchName_jets_ak8, branchName_subjets_ak8); 
  // TO-DO: implement jet energy scale uncertainties, b-tag weights,  
  //        and jet  pT and (softdrop) mass corrections described in Section 3.4.3 of AN-2018/058 (v4)
  //jetReaderAK8->setPtMass_central_or_shift(useNonNominal_jetmet ? kJetMET_central_nonNominal : kJetMET_central);
  //jetReaderAK8->read_ptMass_systematics(isMC);
  //jetReaderAK8->read_BtagWeight_systematics(isMC);
  jetReaderAK8->setBranchAddresses(inputTree);
  RecoJetReaderAK8* jetReaderAK8LS = new RecoJetReaderAK8(era, branchName_jets_ak8LS, branchName_subjets_ak8LS); 
  //jetReaderAK8LS->setPtMass_central_or_shift(useNonNominal_jetmet ? kJetMET_central_nonNominal : kJetMET_central);
  //jetReaderAK8LS->read_ptMass_systematics(isMC);
  //jetReaderAK8LS->read_BtagWeight_systematics(isMC);
  jetReaderAK8LS->setBranchAddresses(inputTree);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR08(0.8, isDEBUG);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR12(1.2, isDEBUG);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR16(1.6, isDEBUG);
  RecoJetCollectionSelectorAK8_hh_bbWW_Hbb jetSelectorAK8_Hbb(era, -1, isDEBUG);
  RecoJetCollectionSelectorAK8_hh_Wjj jetSelectorAK8LS_Wjj(era, -1, isDEBUG);

//--- declare missing transverse energy
  RecoMEtReader* metReader = new RecoMEtReader(era, isMC, branchName_met);
  metReader->setMEt_central_or_shift(useNonNominal_jetmet ? kJetMET_central_nonNominal : kJetMET_central);
  metReader->read_ptPhi_systematics(isMC);
  metReader->setBranchAddresses(inputTree);

//--- declare genParticle readers
  GenLeptonReader *   genLeptonReader            = nullptr;
  GenParticleReader * genNeutrinoReader          = nullptr;
  GenParticleReader * genParticleFromHiggsReader = nullptr;
  GenParticleReader * genWJetReader              = nullptr;
  GenLeptonReader *   genLeptonFromTopReader     = nullptr;
  GenParticleReader * genNeutrinoFromTopReader   = nullptr;
  GenParticleReader * genBJetFromTopReader       = nullptr;
  GenParticleReader * genWJetFromTopReader       = nullptr;
  if ( addMEM_forGenParticles )
  {
    if ( isMC_HH )
    {
      genLeptonReader = new GenLeptonReader(branchName_genLeptons);
      genLeptonReader->setBranchAddresses(inputTree);
      genNeutrinoReader = new GenParticleReader(branchName_genNeutrinos);
      genNeutrinoReader->setBranchAddresses(inputTree);
      genParticleFromHiggsReader = new GenParticleReader(branchName_genParticlesFromHiggs);
      genParticleFromHiggsReader->setBranchAddresses(inputTree);
      genWJetReader = new GenParticleReader(branchName_genWJets);
      genWJetReader->setBranchAddresses(inputTree);
    }
    else if ( isMC_TT )
    {
      genLeptonFromTopReader = new GenLeptonReader(branchName_genLeptonsFromTop);
      genLeptonFromTopReader->setBranchAddresses(inputTree);
      genNeutrinoFromTopReader = new GenParticleReader(branchName_genNeutrinosFromTop);
      genNeutrinoFromTopReader->setBranchAddresses(inputTree);
      genBJetFromTopReader = new GenParticleReader(branchName_genBJetsFromTop);
      genBJetFromTopReader->setBranchAddresses(inputTree);
      genWJetFromTopReader = new GenParticleReader(branchName_genWJetsFromTop);
      genWJetFromTopReader->setBranchAddresses(inputTree);
    }
  }

//--- initialize BDT for ranking of W->jj decays
  TMVAInterface mva_Wjj = initialize_mva_Wjj();

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

  RecoMuonWriter *      muonWriter                 = nullptr;
  RecoElectronWriter *  electronWriter             = nullptr;
  RecoJetWriter *       jetWriterAK4               = nullptr;
  RecoJetWriterAK8 *    jetWriterAK8               = nullptr;
  RecoJetWriterAK8 *    jetWriterAK8LS             = nullptr;
  RecoMEtWriter *       metWriter                  = nullptr;
  EventInfoWriter *     eventInfoWriter            = nullptr;

  GenParticleWriter *   genLeptonWriter            = nullptr;
  GenParticleWriter *   genNeutrinoWriter          = nullptr;
  GenParticleWriter *   genParticleFromHiggsWriter = nullptr;
  GenParticleWriter *   genWJetWriter              = nullptr;
  GenParticleWriter *   genLeptonFromTopWriter     = nullptr;
  GenParticleWriter *   genNeutrinoFromTopWriter   = nullptr;
  GenParticleWriter *   genBJetFromTopWriter       = nullptr;
  GenParticleWriter *   genWJetFromTopWriter       = nullptr;

  std::map<std::string, branchEntryBaseType*> branchesToKeep;
  if ( copy_all_branches )
  {
    eventInfoWriter = new EventInfoWriter(eventInfo.is_signal(), eventInfo.is_mc());
    eventInfoWriter->setBranches(outputTree);

    muonWriter = new RecoMuonWriter(era, isMC, Form("n%s", branchName_muons.data()), branchName_muons);
    muonWriter->setBranches(outputTree);
    electronWriter = new RecoElectronWriter(era, isMC, Form("n%s", branchName_electrons.data()), branchName_electrons);
    electronWriter->writeUncorrected(false);
    electronWriter->setBranches(outputTree);
    jetWriterAK4 = new RecoJetWriter(era, isMC, Form("n%s", branchName_jets_ak4.data()), branchName_jets_ak4);
    jetWriterAK4->setPtMass_central_or_shift(useNonNominal_jetmet ? kJetMET_central_nonNominal : kJetMET_central);
    jetWriterAK4->setBranches(outputTree);
    jetWriterAK8 = new RecoJetWriterAK8(era, Form("n%s", branchName_jets_ak8.data()), branchName_jets_ak8, 
      Form("n%s", branchName_subjets_ak8.data()), branchName_subjets_ak8);
    // TO-DO: implement jet energy scale uncertainties, b-tag weights,  
    //        and jet  pT and (softdrop) mass corrections described in Section 3.4.3 of AN-2018/058 (v4)
    //jetWriterAK8->setPtMass_central_or_shift(useNonNominal_jetmet ? kJetMET_central_nonNominal : kJetMET_central);
    //jetWriterAK8->write_ptMass_systematics(isMC);
    //jetWriterAK8->write_BtagWeight_systematics(isMC);
    jetWriterAK8->setBranches(outputTree);
    jetWriterAK8LS = new RecoJetWriterAK8(era, Form("n%s", branchName_jets_ak8LS.data()), branchName_jets_ak8LS, 
      Form("n%s", branchName_subjets_ak8LS.data()), branchName_subjets_ak8LS);
    // TO-DO: implement jet energy scale uncertainties, b-tag weights,  
    //        and jet  pT and (softdrop) mass corrections described in Section 3.4.3 of AN-2018/058 (v4)
    //jetWriterAK8LS->setPtMass_central_or_shift(useNonNominal_jetmet ? kJetMET_central_nonNominal : kJetMET_central);
    //jetWriterAK8LS->write_ptMass_systematics(isMC);
    //jetWriterAK8LS->write_BtagWeight_systematics(isMC);
    jetWriterAK8LS->setBranches(outputTree);
    metWriter = new RecoMEtWriter(era, isMC, branchName_met);
    metWriter->setPtPhi_central_or_shift(useNonNominal_jetmet ? kJetMET_central_nonNominal : kJetMET_central);
    metWriter->write_ptPhi_systematics(isMC);
    metWriter->setBranches(outputTree);
  
    vstring outputCommands_string = {
      "keep *",
      Form("drop %s", eventInfoWriter->getBranchName_run().data()),
      Form("drop %s", eventInfoWriter->getBranchName_lumi().data()),
      Form("drop %s", eventInfoWriter->getBranchName_event().data()),
      Form("drop %s", eventInfoWriter->getBranchName_PV_ndof().data()),
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
      Form("drop n%s", branchName_jets_ak8LS.data()),
      Form("drop %s_*", branchName_jets_ak8LS.data()),
      Form("drop n%s", branchName_subjets_ak8LS.data()),
      Form("drop %s_*", branchName_subjets_ak8LS.data()),
      Form("drop %s_*", branchName_met.data())
    };

    if ( addMEM_forGenParticles )
    {
      if ( isMC_HH )
      {
        genLeptonWriter = new GenParticleWriter(Form("n%s", branchName_genLeptons.data()), branchName_genLeptons);
        genLeptonWriter->setBranches(outputTree);
        genNeutrinoWriter = new GenParticleWriter(Form("n%s", branchName_genNeutrinos.data()), branchName_genNeutrinos);
        genNeutrinoWriter->setBranches(outputTree);
        genParticleFromHiggsWriter = new GenParticleWriter(Form("n%s", branchName_genParticlesFromHiggs.data()), branchName_genParticlesFromHiggs);
        genParticleFromHiggsWriter->setBranches(outputTree);
        genWJetWriter = new GenParticleWriter(Form("n%s", branchName_genWJets.data()), branchName_genWJets);
        genWJetWriter->setBranches(outputTree);

        outputCommands_string.push_back(Form("drop n%s", branchName_genLeptons.data()));
        outputCommands_string.push_back(Form("drop n%s_*", branchName_genLeptons.data()));
        outputCommands_string.push_back(Form("drop %s_*", branchName_genLeptons.data()));
        outputCommands_string.push_back(Form("drop n%s", branchName_genNeutrinos.data()));
        outputCommands_string.push_back(Form("drop n%s_*", branchName_genNeutrinos.data()));
        outputCommands_string.push_back(Form("drop %s_*", branchName_genNeutrinos.data()));
        outputCommands_string.push_back(Form("drop n%s", branchName_genParticlesFromHiggs.data()));
        outputCommands_string.push_back(Form("drop n%s_*", branchName_genParticlesFromHiggs.data()));
        outputCommands_string.push_back(Form("drop %s_*", branchName_genParticlesFromHiggs.data()));
        outputCommands_string.push_back(Form("drop n%s", branchName_genWJets.data()));
        outputCommands_string.push_back(Form("drop n%s_*", branchName_genWJets.data()));
        outputCommands_string.push_back(Form("drop %s_*", branchName_genWJets.data())); 
      }
      else if ( isMC_TT )
      {
        genLeptonFromTopWriter = new GenParticleWriter(Form("n%s", branchName_genLeptonsFromTop.data()), branchName_genLeptonsFromTop);
        genLeptonFromTopWriter->setBranches(outputTree);
        genNeutrinoFromTopWriter = new GenParticleWriter(Form("n%s", branchName_genNeutrinosFromTop.data()), branchName_genNeutrinosFromTop);
        genNeutrinoFromTopWriter->setBranches(outputTree);
        genBJetFromTopWriter = new GenParticleWriter(Form("n%s", branchName_genBJetsFromTop.data()), branchName_genBJetsFromTop);
        genBJetFromTopWriter->setBranches(outputTree);
        genWJetFromTopWriter = new GenParticleWriter(Form("n%s", branchName_genWJetsFromTop.data()), branchName_genWJetsFromTop);
        genWJetFromTopWriter->setBranches(outputTree);
 
        outputCommands_string.push_back(Form("drop n%s", branchName_genLeptonsFromTop.data()));
        outputCommands_string.push_back(Form("drop n%s_*", branchName_genLeptonsFromTop.data()));
        outputCommands_string.push_back(Form("drop %s_*", branchName_genLeptonsFromTop.data()));
        outputCommands_string.push_back(Form("drop n%s", branchName_genNeutrinosFromTop.data()));
        outputCommands_string.push_back(Form("drop n%s_*", branchName_genNeutrinosFromTop.data()));
        outputCommands_string.push_back(Form("drop %s_*", branchName_genNeutrinosFromTop.data()));
        outputCommands_string.push_back(Form("drop n%s", branchName_genBJetsFromTop.data()));
        outputCommands_string.push_back(Form("drop n%s_*", branchName_genBJetsFromTop.data()));
        outputCommands_string.push_back(Form("drop %s_*", branchName_genBJetsFromTop.data()));
        outputCommands_string.push_back(Form("drop n%s", branchName_genWJetsFromTop.data()));
        outputCommands_string.push_back(Form("drop n%s_*", branchName_genWJetsFromTop.data()));
        outputCommands_string.push_back(Form("drop %s_*", branchName_genWJetsFromTop.data()));
      }
    }

    std::vector<outputCommandEntry> outputCommands = getOutputCommands(outputCommands_string);
    std::map<std::string, bool> isBranchToKeep = getBranchesToKeep(inputTree, outputCommands);
    copyBranches_singleType(inputTree, outputTree, isBranchToKeep, branchesToKeep);
    copyBranches_vectorType(inputTree, outputTree, isBranchToKeep, branchesToKeep);
  }

  if ( branchName_maxPermutations_addMEM != "" && !branchesToKeep.count(branchName_maxPermutations_addMEM) )
  {
    throw cmsException(__func__, __LINE__)
      << "No such branch: " << branchName_maxPermutations_addMEM;
  }

  const std::string branchName_memOutput = get_memObjectBranchName("hh_bb1l", leptonSelection_string, "", "");
  const std::string branchName_memOutput_missingBJet = Form("%s_missingBJet", branchName_memOutput.data());
  const std::string branchName_memOutput_missingHadWJet = Form("%s_missingHadWJet", branchName_memOutput.data());
  
  std::map<std::string, MEMOutputWriter_hh_bb1l *> memWriter;
  std::map<std::string, MEMOutputWriter_hh_bb1l *> memWriter_missingBJet;
  std::map<std::string, MEMOutputWriter_hh_bb1l *> memWriter_missingHadWJet;

  for ( const std::string & central_or_shift: central_or_shifts_mem )
  {
    const std::string branchName_memOutput_cos(Form("%s_%s", branchName_memOutput.data(), central_or_shift.data()));
    std::cout << "writing MEMOutput_hh_bb1l objects for systematic " << central_or_shift
              << " to branch = '" << branchName_memOutput_cos << "'\n";	
    memWriter[central_or_shift] = new MEMOutputWriter_hh_bb1l(
      Form("n%s", branchName_memOutput_cos.data()), branchName_memOutput_cos
    );
    memWriter[central_or_shift]->setBranches(outputTree);

    const std::string branchName_memOutput_missingBJet_cos(Form("%s_%s", branchName_memOutput_missingBJet.data(), central_or_shift.data()));
    std::cout << "writing MEMOutput_hh_bb1l objects (missingBJet) for systematic " << central_or_shift
              << " to branch = '" << branchName_memOutput_missingBJet_cos << "'\n";
    memWriter_missingBJet[central_or_shift] = new MEMOutputWriter_hh_bb1l(
      Form("n%s", branchName_memOutput_missingBJet_cos.data()), branchName_memOutput_missingBJet_cos
    );
    memWriter_missingBJet[central_or_shift]->setBranches(outputTree);

    const std::string branchName_memOutput_missingHadWJet_cos(Form("%s_%s", branchName_memOutput_missingHadWJet.data(), central_or_shift.data()));
    std::cout << "writing MEMOutput_hh_bb1l objects (missingHadWJet) for systematic " << central_or_shift
              << " to branch = '" << branchName_memOutput_missingHadWJet_cos << "'\n";
    memWriter_missingHadWJet[central_or_shift] = new MEMOutputWriter_hh_bb1l(
      Form("n%s", branchName_memOutput_missingHadWJet_cos.data()), branchName_memOutput_missingHadWJet_cos
    );
    memWriter_missingHadWJet[central_or_shift]->setBranches(outputTree);
  }

  const std::string branchName_memOutput_gen = Form("%s_gen", branchName_memOutput.data());
  const std::string branchName_memOutput_gen_missingBJet = Form("%s_missingBJet", branchName_memOutput_gen.data());
  const std::string branchName_memOutput_gen_missingHadWJet = Form("%s_missingHadWJet", branchName_memOutput_gen.data());

  MEMOutputWriter_hh_bb1l * memWriter_gen                = nullptr;
  MEMOutputWriter_hh_bb1l * memWriter_gen_missingBJet    = nullptr;
  MEMOutputWriter_hh_bb1l * memWriter_gen_missingHadWJet = nullptr;  
  if ( addMEM_forGenParticles )
  {
    memWriter_gen = new MEMOutputWriter_hh_bb1l(Form("n%s", branchName_memOutput_gen.data()), branchName_memOutput_gen);
    memWriter_gen->setBranches(outputTree);
    memWriter_gen_missingBJet = new MEMOutputWriter_hh_bb1l(Form("n%s", branchName_memOutput_gen_missingBJet.data()), branchName_memOutput_gen_missingBJet);
    memWriter_gen_missingBJet->setBranches(outputTree);
    memWriter_gen_missingHadWJet = new MEMOutputWriter_hh_bb1l(Form("n%s", branchName_memOutput_gen_missingHadWJet.data()), branchName_memOutput_gen_missingHadWJet);
    memWriter_gen_missingHadWJet->setBranches(outputTree);
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

    const std::vector<const RecoLepton*> preselLeptonsFull = mergeLeptonCollections(preselElectrons, preselMuons, isHigherConePt);
    const std::vector<const RecoLepton*> fakeableLeptonsFull = mergeLeptonCollections(fakeableElectrons, fakeableMuons, isHigherConePt);
    const std::vector<const RecoLepton*> tightLeptonsFull = mergeLeptonCollections(tightElectrons, tightMuons, isHigherConePt);

    const std::vector<const RecoLepton*> preselLeptons = pickFirstNobjects(preselLeptonsFull, 1);
    const std::vector<const RecoLepton*> fakeableLeptons = pickFirstNobjects(fakeableLeptonsFull, 1);
    const std::vector<const RecoLepton*> tightLeptons = getIntersection(fakeableLeptons, tightLeptonsFull, isHigherConePt);

//--- build collections of jets 
    const std::vector<RecoJet> jets_ak4 = jetReaderAK4->read();
    const std::vector<const RecoJet*> jet_ptrs_ak4 = convert_to_ptrs(jets_ak4);
    const std::vector<RecoJetAK8> jets_ak8 = jetReaderAK8->read();
    const std::vector<const RecoJetAK8*> jet_ptrs_ak8 = convert_to_ptrs(jets_ak8);
    const std::vector<RecoJetAK8> jets_ak8LS = jetReaderAK8LS->read();
    const std::vector<const RecoJetAK8*> jet_ptrs_ak8LS = convert_to_ptrs(jets_ak8LS);

    const RecoMEt met = metReader->read();

//--- build collections of generator level particles 
    std::vector<GenLepton>   genLeptons;
    std::vector<GenParticle> genNeutrinos;
    std::vector<GenParticle> genParticlesFromHiggs;
    std::vector<GenParticle> genWJets;
    std::vector<GenLepton>   genLeptonsFromTop;
    std::vector<GenParticle> genNeutrinosFromTop;
    std::vector<GenParticle> genBJetsFromTop;
    std::vector<GenParticle> genWJetsFromTop;
    if ( addMEM_forGenParticles )
    {
      if ( isMC_HH )
      {
        genLeptons            = genLeptonReader->read();
        genNeutrinos          = genNeutrinoReader->read();
        genParticlesFromHiggs = genParticleFromHiggsReader->read();
        genWJets              = genWJetReader->read();       
      }
      else if ( isMC_TT )
      {
        genLeptonsFromTop     = genLeptonFromTopReader->read();
        genNeutrinosFromTop   = genNeutrinoFromTopReader->read();
        genBJetsFromTop       = genBJetFromTopReader->read();
        genWJetsFromTop       = genWJetFromTopReader->read();         
      }
    }

    std::map<std::string, std::vector<MEMOutput_hh_bb1l>> memOutputs_hh_bb1l;
    std::map<std::string, std::vector<MEMOutput_hh_bb1l>> memOutputs_hh_bb1l_missingBJet;
    std::map<std::string, std::vector<MEMOutput_hh_bb1l>> memOutputs_hh_bb1l_missingHadWJet;	

    for ( const std::string & central_or_shift: central_or_shifts_mem )
    {
      memOutputs_hh_bb1l[central_or_shift] = {};
      memOutputs_hh_bb1l_missingBJet[central_or_shift] = {};
      memOutputs_hh_bb1l_missingHadWJet[central_or_shift] = {};
    }

    std::vector<MEMOutput_hh_bb1l> memOutputs_hh_bb1l_gen;
    std::vector<MEMOutput_hh_bb1l> memOutputs_hh_bb1l_gen_missingBJet;
    std::vector<MEMOutput_hh_bb1l> memOutputs_hh_bb1l_gen_missingHadWJet;

//--- fill the branches here since because we want to re-use the readers
//    however, the readers obtain pointers to gen level objects and pass them to the reco objects
//    thus, if we try to re-read the objects, these pointers will be overwritten and become invalid
//    therefore, we have to write the reco objects before re-reading new stuff
    if ( copy_all_branches )
    {
      eventInfoWriter->write(eventInfo);
      muonWriter->write(preselMuons);
      electronWriter->write(preselElectronsUncleaned);
      jetWriterAK4->write(jet_ptrs_ak4);     // save central
      jetWriterAK8->write(jet_ptrs_ak8);     // save central
      jetWriterAK8LS->write(jet_ptrs_ak8LS); // save central
      metWriter->write(met);                 // save central

      if ( addMEM_forGenParticles )
      {
        if ( isMC_HH )
        {
          genLeptonWriter->write(convert_to_genParticles(genLeptons));
          genNeutrinoWriter->write(genNeutrinos);
          genParticleFromHiggsWriter->write(genParticlesFromHiggs);
          genWJetWriter->write(genWJets);
        }
        else if ( isMC_TT )
        {
          genLeptonFromTopWriter->write(convert_to_genParticles(genLeptonsFromTop));
          genNeutrinoFromTopWriter->write(genNeutrinosFromTop);
          genBJetFromTopWriter->write(genBJetsFromTop);
          genWJetFromTopWriter->write(genWJetsFromTop);
        }
      }

      for ( const auto & branchEntry: branchesToKeep )
      {
        branchEntry.second->copyBranch();
      }
    }

    int maxPermutations_addMEM_hh_bb1l = -1;
    if ( branchName_maxPermutations_addMEM != "" ) 
    {
      maxPermutations_addMEM_hh_bb1l = branchesToKeep.at(branchName_maxPermutations_addMEM)->getValue_int();
      if ( isDEBUG )
      {
        std::cout << "Found " << maxPermutations_addMEM_hh_bb1l << " possible combination(s) to compute MEM\n";
      }
    }
    if ( branchName_maxPermutations_addMEM == "" || maxPermutations_addMEM_hh_bb1l >= 1 )
    {
      int idxPermutation_mem = 0;
      int idxPermutation_mem_missingBJet = 0;
      int idxPermutation_mem_missingHadWJet = 0;
      int idxPermutation_mem_gen = 0;
      int idxPermutation_mem_gen_missingBJet = 0;
      int idxPermutation_mem_gen_missingHadWJet = 0;
      const std::vector<const RecoLepton*> selLeptons = mergeLeptonCollections(selElectrons, selMuons, isHigherConePt);
      for ( std::size_t selLepton_idx = 0; selLepton_idx < selLeptons.size(); ++selLepton_idx )
      {
        const RecoLepton * selLepton = selLeptons[selLepton_idx];
        if(isDEBUG)
        {
          std::cout << "selLepton: " << *selLepton << '\n';
        }
        for ( const std::string & central_or_shift: central_or_shifts )
        {
          checkOptionValidity(central_or_shift, isMC);
          const int jetPt_option = useNonNominal_jetmet ? kJetMET_central_nonNominal : getJet_option(central_or_shift, isMC);
          const int met_option   = useNonNominal_jetmet ? kJetMET_central_nonNominal : getMET_option(central_or_shift, isMC);

          if((
               (
                 jetPt_option    == kJetMET_central &&
                 met_option      == kJetMET_central &&
                 ! useNonNominal_jetmet
               ) ||
              useNonNominal_jetmet
             ) &&
             central_or_shift != "central")
          {
            std::cout << "Skipping systematics: " << central_or_shift << '\n';
            continue;
          }
          else if(isDEBUG)
          {
            std::cout << "Attempting to evaluate the MEM score for systematics: " << central_or_shift << "\n"
                      << "jetPt_option    = " << jetPt_option    << "\n"
                      << "met_option      = " << met_option      << '\n'
            ;
          }
          const bool is_central_or_shift_mem = std::find(
              central_or_shifts_mem.begin(), central_or_shifts_mem.end(), central_or_shift
            ) != central_or_shifts_mem.end()
          ;

          jetReaderAK4->setPtMass_central_or_shift(jetPt_option);
          //jetReaderAK8->setPtMass_central_or_shift(jetPt_option);
          //jetReaderAK8LS->setPtMass_central_or_shift(jetPt_option);
          metReader->setMEt_central_or_shift(met_option);

          const std::vector<RecoJet> jets_ak4_mem = jetReaderAK4->read();
          const std::vector<const RecoJet*> jet_ptrs_ak4_mem = convert_to_ptrs(jets_ak4_mem);
          const std::vector<const RecoJet*> cleanedJetsAK4_wrtLeptons = jetCleaningByIndex ?
            jetCleanerAK4_byIndex(jet_ptrs_ak4_mem, fakeableLeptons) :
            jetCleanerAK4_dR04   (jet_ptrs_ak4_mem, fakeableLeptons)
          ;
          const std::vector<const RecoJet*> selBJetsAK4_medium = jetSelectorAK4_bTagMedium(cleanedJetsAK4_wrtLeptons, isHigherPt);
          const std::vector<RecoJetAK8> jets_ak8_mem = jetReaderAK8->read();
          const std::vector<const RecoJetAK8*> jet_ptrs_ak8_mem = convert_to_ptrs(jets_ak8_mem);
          const std::vector<RecoJetAK8> jets_ak8LS_mem = jetReaderAK8LS->read();
          const std::vector<const RecoJetAK8*> jet_ptrs_ak8LS_mem = convert_to_ptrs(jets_ak8LS_mem);
          
          // select jets from H->bb decay
          const std::vector<const RecoJetAK8*> cleanedJetsAK8_Hbb_wrtLeptons = jetCleanerAK8_dR08(jet_ptrs_ak8_mem, fakeableLeptons);
          const std::vector<const RecoJetAK8*> selJetsAK8_Hbb = jetSelectorAK8_Hbb(cleanedJetsAK8_Hbb_wrtLeptons, isHigherCSV_ak8);
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

          // select jets from W->jj decay
          std::vector<selJetsType_Wjj> selJetsT_Wjj = selectJets_Wjj(
            jet_ptrs_ak8LS_mem, jetCleanerAK8_dR12, jetCleanerAK8_dR16, jetSelectorAK8LS_Wjj, 
            cleanedJetsAK4_wrtLeptons, jetCleanerAK4_dR08, jetCleanerAK4_dR12, jetSelectorAK4_Wjj,
            *selJetT_Hbb, 
            selLepton, selBJetsAK4_medium, mva_Wjj, eventInfo, 
            nullptr,
            mem_maxWJetPairs);

          selJetsType_Hbb selJetT_Hbb_missingBJet1;
          selJetT_Hbb_missingBJet1.fatjet_ = selJetAK8_Hbb;
          selJetT_Hbb_missingBJet1.jet_or_subjet1_ = selJet2_Hbb;
          std::vector<selJetsType_Wjj> selJetsT_Wjj_missingBJet1 = selectJets_Wjj(
            jet_ptrs_ak8LS_mem, jetCleanerAK8_dR12, jetCleanerAK8_dR16, jetSelectorAK8LS_Wjj, 
            cleanedJetsAK4_wrtLeptons, jetCleanerAK4_dR08, jetCleanerAK4_dR12, jetSelectorAK4_Wjj,
            selJetT_Hbb_missingBJet1, 
            selLepton, selBJetsAK4_medium, mva_Wjj, eventInfo, 
            nullptr,
            mem_maxWJetPairs);

          selJetsType_Hbb selJetT_Hbb_missingBJet2;
          selJetT_Hbb_missingBJet2.fatjet_ = selJetAK8_Hbb;
          selJetT_Hbb_missingBJet2.jet_or_subjet1_ = selJet1_Hbb;
          std::vector<selJetsType_Wjj> selJetsT_Wjj_missingBJet2 = selectJets_Wjj(
            jet_ptrs_ak8LS_mem, jetCleanerAK8_dR12, jetCleanerAK8_dR16, jetSelectorAK8LS_Wjj, 
            cleanedJetsAK4_wrtLeptons, jetCleanerAK4_dR08, jetCleanerAK4_dR12, jetSelectorAK4_Wjj,
            selJetT_Hbb_missingBJet2, 
            selLepton, selBJetsAK4_medium, mva_Wjj, eventInfo, 
            nullptr,
            mem_maxWJetPairs);

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
          const std::vector<const RecoJet*> selJetsAK4_Wjj = jetSelectorAK4_Wjj(cleanedJetsAK4_wrtHbb, isHigherPt);
          //-------------------------------------------------------------------
           
          const RecoMEt met_mem = metReader->read();

          // match reconstructed to generator-level particles
          if ( addMEM_forGenParticles )
          {
            std::vector<const RecoJetBase*> selJets_Hbb_base;
            if ( selJet1_Hbb ) selJets_Hbb_base.push_back(selJet1_Hbb);
            if ( selJet2_Hbb ) selJets_Hbb_base.push_back(selJet2_Hbb);
            const std::vector<const RecoJetBase*> selJets_Wjj_base = convert_to_RecoJetBase(selJetsAK4_Wjj);
            if ( isMC_HH )
            {
              genParticleMatcherFromHiggs.setGenParticles(genParticlesFromHiggs, genLeptons, genNeutrinos, genWJets);
              genParticleMatcherFromHiggs({ selLepton }, selJets_Hbb_base, selJets_Wjj_base, met);
            }
            else if ( isMC_TT )
            {
              genParticleMatcherFromTop.setGenParticles(genLeptonsFromTop, genNeutrinosFromTop, genWJetsFromTop, genBJetsFromTop);
              genParticleMatcherFromTop({ selLepton }, selJets_Hbb_base, selJets_Wjj_base, met);
            }
          }

          if ( selJet1_Hbb && selJet2_Hbb )
          {
            const bool run_mem = method_MEM && is_central_or_shift_mem;
            if ( run_mem )
            {
	      std::cout << "computing MEMOutput_hh_bb1l objects for branch = '" << branchName_memOutput << "'," 
	                << " systematic = '" << central_or_shift << "'\n";
              for ( std::vector<selJetsType_Wjj>::const_iterator jetPair = selJetsT_Wjj.begin(); 
                    jetPair != selJetsT_Wjj.end(); ++jetPair ) {
                MEMOutput_hh_bb1l memOutput = compMEM(
                  eventInfo,
                  selLepton, jetPair->jet_or_subjet1_, jetPair->jet_or_subjet2_,
                  selJet1_Hbb, selJet2_Hbb, 
                  met,
	          memInterface_hh_bb1l, false, dryRun, 
	          idxPermutation_mem, maxPermutations_addMEM_hh_bb1l*nof_central_or_shift_mem,
	          branchName_memOutput, central_or_shift, isDEBUG);
                memOutputs_hh_bb1l[central_or_shift].push_back(memOutput);
                ++memComputations;
                if ( isDEBUG )
                {
                  std::cout << "#memOutputs_hh_bb1l = " 
                            << memOutputs_hh_bb1l[central_or_shift].size() << std::endl;
                }

                if ( addMEM_forGenParticles && (central_or_shift == "central" ||  central_or_shift == "") )
                {
                  MEMOutput_hh_bb1l memOutput_gen = compMEM(
                    eventInfo,
                    selLepton, jetPair->jet_or_subjet1_, jetPair->jet_or_subjet2_,
                    selJet1_Hbb, selJet2_Hbb, 
                    met,
	            memInterface_hh_bb1l, true, dryRun, 
	            idxPermutation_mem_gen, maxPermutations_addMEM_hh_bb1l,
	            branchName_memOutput_gen, central_or_shift, isDEBUG);
                  memOutputs_hh_bb1l_gen.push_back(memOutput_gen);
                  ++memComputations;
                }
              }             

              std::cout << "computing MEMOutput_hh_bb1l objects for branch = '" << branchName_memOutput_missingBJet << "'," 
	                << " systematic = '" << central_or_shift << "'\n";
              for ( std::vector<selJetsType_Wjj>::const_iterator jetPair = selJetsT_Wjj_missingBJet1.begin(); 
	            jetPair != selJetsT_Wjj_missingBJet1.end(); ++jetPair ) {
                MEMOutput_hh_bb1l memOutput = compMEM(
                  eventInfo,
                  selLepton, jetPair->jet_or_subjet1_, jetPair->jet_or_subjet2_,
                  selJet2_Hbb, nullptr, 
                  met, 
	          memInterface_hh_bb1l, false, dryRun, 
                  idxPermutation_mem_missingBJet, maxPermutations_addMEM_hh_bb1l*nof_central_or_shift_mem,
	          branchName_memOutput_missingBJet, central_or_shift, isDEBUG);
                memOutputs_hh_bb1l_missingBJet[central_or_shift].push_back(memOutput);
                ++memComputations;
                if ( isDEBUG )
                {
                  std::cout << "#memOutputs_hh_bb1l_missingBJet = " 
                            << memOutputs_hh_bb1l_missingBJet[central_or_shift].size() << std::endl;
                }

                if ( addMEM_forGenParticles && (central_or_shift == "central" ||  central_or_shift == "") )
                {
                  MEMOutput_hh_bb1l memOutput_gen = compMEM(
                    eventInfo,
                    selLepton, jetPair->jet_or_subjet1_, jetPair->jet_or_subjet2_,
                    selJet2_Hbb, nullptr, 
                    met,
	            memInterface_hh_bb1l, true, dryRun, 
	            idxPermutation_mem_gen_missingBJet, maxPermutations_addMEM_hh_bb1l,
	            branchName_memOutput_gen_missingBJet, central_or_shift, isDEBUG);
                  memOutputs_hh_bb1l_gen_missingBJet.push_back(memOutput_gen);
                  ++memComputations;
                }
              }
              for ( std::vector<selJetsType_Wjj>::const_iterator jetPair = selJetsT_Wjj_missingBJet2.begin(); 
	            jetPair != selJetsT_Wjj_missingBJet2.end(); ++jetPair ) {
                MEMOutput_hh_bb1l memOutput = compMEM(
                  eventInfo,
                  selLepton, jetPair->jet_or_subjet1_, jetPair->jet_or_subjet2_,
                  selJet1_Hbb, nullptr, 
                  met, 
	          memInterface_hh_bb1l, false, dryRun, 
                  idxPermutation_mem_missingBJet, maxPermutations_addMEM_hh_bb1l*nof_central_or_shift_mem,
	          branchName_memOutput_missingBJet, central_or_shift, isDEBUG);
                  memOutputs_hh_bb1l_missingBJet[central_or_shift].push_back(memOutput);
                ++memComputations;
                if ( isDEBUG )
                {
                  std::cout << "#memOutputs_hh_bb1l_missingBJet = " 
                            << memOutputs_hh_bb1l_missingBJet[central_or_shift].size() << std::endl;
                }

	        if ( addMEM_forGenParticles && (central_or_shift == "central" ||  central_or_shift == "") )
                {
                  MEMOutput_hh_bb1l memOutput_gen = compMEM(
                    eventInfo,
                    selLepton, jetPair->jet_or_subjet1_, jetPair->jet_or_subjet2_,
                    selJet1_Hbb, nullptr, 
                    met,
	            memInterface_hh_bb1l, true, dryRun, 
	            idxPermutation_mem_gen_missingBJet, maxPermutations_addMEM_hh_bb1l,
	            branchName_memOutput_gen_missingBJet, central_or_shift, isDEBUG);
                  memOutputs_hh_bb1l_gen_missingBJet.push_back(memOutput_gen);
                  ++memComputations;
                }
              }

              std::cout << "computing MEMOutput_hh_bb1l objects for branch = '" << branchName_memOutput_missingHadWJet << "'," 
	                << " systematic = '" << central_or_shift << "'\n";
              size_t numWJets = selJetsAK4_Wjj.size();
              if ( mem_maxWJets >= 0 ) numWJets = std::min(numWJets, (size_t)mem_maxWJets);
              for ( size_t idxWJet = 0; idxWJet < numWJets; ++idxWJet )
              {
                const RecoJet* selJet_Wjj = selJetsAK4_Wjj[idxWJet];
                MEMOutput_hh_bb1l memOutput = compMEM(
                  eventInfo,
                  selLepton, selJet_Wjj, nullptr,
                  selJet1_Hbb, selJet2_Hbb, 
                  met, 
	          memInterface_hh_bb1l, false, dryRun,  
                  idxPermutation_mem_missingHadWJet, maxPermutations_addMEM_hh_bb1l*nof_central_or_shift_mem, 
	          branchName_memOutput_missingHadWJet, central_or_shift, isDEBUG);
                memOutputs_hh_bb1l_missingHadWJet[central_or_shift].push_back(memOutput);
                ++memComputations;
                if ( isDEBUG )
                {
                  std::cout << "#memOutputs_hh_bb1l_missingHadWJet = " 
	                    << memOutputs_hh_bb1l_missingHadWJet[central_or_shift].size() << std::endl;
                }

                if ( addMEM_forGenParticles && (central_or_shift == "central" ||  central_or_shift == "") )
                {
                  MEMOutput_hh_bb1l memOutput_gen = compMEM(
                    eventInfo,
                    selLepton, selJet_Wjj, nullptr,
                    selJet1_Hbb, selJet2_Hbb, 
                    met,
	            memInterface_hh_bb1l, true, dryRun, 
	            idxPermutation_mem_gen_missingHadWJet, maxPermutations_addMEM_hh_bb1l,
	            branchName_memOutput_gen_missingHadWJet, central_or_shift, isDEBUG);
                  memOutputs_hh_bb1l_gen_missingHadWJet.push_back(memOutput_gen);
                  ++memComputations;
                }
              }
            } // run_mem
          } // selJet1_Hbb && selJet2_Hbb
        } // central_or_shift
      } // selLepton_idx
    } // maxPermutations_addMEM_hh_bb1l >= 1
    
    for ( const std::string & central_or_shift: central_or_shifts_mem )
    {
      memWriter[central_or_shift]->write(memOutputs_hh_bb1l[central_or_shift]);
      memWriter_missingBJet[central_or_shift]->write(memOutputs_hh_bb1l_missingBJet[central_or_shift]);
      memWriter_missingHadWJet[central_or_shift]->write(memOutputs_hh_bb1l_missingHadWJet[central_or_shift]);
    }

    if ( addMEM_forGenParticles )
    {
      memWriter_gen->write(memOutputs_hh_bb1l_gen);
      memWriter_gen_missingBJet->write(memOutputs_hh_bb1l_gen_missingBJet);
      memWriter_gen_missingHadWJet->write(memOutputs_hh_bb1l_gen_missingHadWJet);
    }

    outputTree->Fill();
    ++selectedEntries;
  } // idxEntry

  std::cout << "num. Entries = "      << numEntries      << "\n"
               " analyzed = "         << analyzedEntries << "\n"
               " selected = "         << selectedEntries << "\n"
               "#MEM computations = " << memComputations << "\n"
               "cut-flow table\n"     << cutFlowTable    << "\n"
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
  delete jetReaderAK8LS;
  delete metReader;

  delete genLeptonReader;
  delete genNeutrinoReader;
  delete genParticleFromHiggsReader;
  delete genWJetReader;
  delete genLeptonFromTopReader;
  delete genNeutrinoFromTopReader;
  delete genBJetFromTopReader;
  delete genWJetFromTopReader;

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
  for ( auto & kv: memWriter_missingHadWJet )
  {
    if ( kv.second )
    {
      delete kv.second;
      kv.second = nullptr;
    }
  }

  delete memWriter_gen;
  delete memWriter_gen_missingBJet;
  delete memWriter_gen_missingHadWJet;

  delete inputTree;

//--- copy histograms keeping track of number of processed events from input files to output file
  copyHistograms(inputFiles, copy_histograms_regex, fs);

  clock.Show("addMEM_hh_bb1l");

  return EXIT_SUCCESS;
}
