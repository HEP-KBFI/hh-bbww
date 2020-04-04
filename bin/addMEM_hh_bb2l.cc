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

#include "hhAnalysis/bbww/interface/RecoJetCollectionSelectorAK8_hh_bbWW_Hbb.h" // RecoJetSelectorAK8_hh_bbWW_Hbb
#include "hhAnalysis/bbww/interface/MEMInterface_hh_bb2l.h" // MEMInterface_hh_bb2l
#include "hhAnalysis/bbww/interface/MEMOutput_hh_bb2l.h" // MEMOutput_hh_bb2l
#include "hhAnalysis/bbww/interface/MEMOutputWriter_hh_bb2l.h" // MEMOutputWriter_hh_bb2l
#include "hhAnalysis/bbww/interface/HMEInterface_hh_bb2l.h" // HMEInterface_hh_bb2l
#include "hhAnalysis/bbww/interface/HMEOutput_hh_bb2l.h" // HMEOutput_hh_bb2l
#include "hhAnalysis/bbww/interface/HMEOutputWriter_hh_bb2l.h" // HMEOutputWriter_hh_bb2l
#include "hhAnalysis/bbww/interface/hmeAuxFunctions.h" // get_hmeObjectBranchName()
#include "hhAnalysis/bbww/interface/GenParticleMatcherFromHiggs.h" // GenParticleMatcherFromHiggs
#include "hhAnalysis/bbww/interface/GenParticleMatcherFromTop.h" // GenParticleMatcherFromTop
#include "hhAnalysis/bbww/interface/jetSelectionAuxFunctions.h" // selJetsType_Hbb, selectJets_Hbb
#include "hhAnalysis/bbww/interface/BM_list.h" // BMS

#include "hhAnalysis/Heavymassestimator/interface/heavyMassEstimator.h" // heavyMassEstimator (HME) algorithm for computation of HH mass

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

MEMOutput_hh_bb2l
compMEM(const EventInfo& eventInfo,
        const RecoLepton* selLepton_lead, const RecoLepton* selLepton_sublead,
        const RecoJetBase* selJet1_Hbb, const RecoJetBase* selJet2_Hbb,
        const RecoMEt& met,
              MEMInterface_hh_bb2l& memInterface, std::string BM,
        bool switchToGen, bool dryRun,
        int& idxPermutation, int maxPermutations,
              const std::string& branchName_memOutput, const std::string& central_or_shift, bool isDEBUG)
{
  MEMOutput_hh_bb2l memOutput;
  if ( maxPermutations == -1 || idxPermutation <= maxPermutations )
  {
    ++idxPermutation;
    if ( isDEBUG )
    {
      std::cout << "computing MEM for branch " << "'" << branchName_memOutput << "'" << std::endl;
      std::cout << eventInfo << " (idxPermutation = " << idxPermutation << "):" << std::endl;
      std::cout << "inputs:" << std::endl;
      std::cout << " leading lepton:    " << *(static_cast<const ChargedParticle *>(selLepton_lead)) << std::endl;
      std::cout << " subleading lepton: " << *(static_cast<const ChargedParticle *>(selLepton_sublead)) << std::endl;
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

    if ( selLepton_lead && selLepton_sublead && (selJet1_Hbb || selJet2_Hbb) )
    {

      if ( dryRun )
      {
        memOutput.fillInputs(selLepton_lead, selLepton_sublead, selJet1_Hbb, selJet2_Hbb);
      }
      else
      {
        memOutput = memInterface(selLepton_lead, selLepton_sublead, selJet1_Hbb, selJet2_Hbb, met, BM, switchToGen, isDEBUG);
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
    std::cout << "Number of permutations exceeds 'maxPermutations_addMEM_hh_bb2l' = " << maxPermutations
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
  const vstring central_or_shifts_mem       = cfg_addMEM.getParameter<vstring>("central_or_shift_mem");
  const vstring central_or_shifts_hme       = cfg_addMEM.getParameter<vstring>("central_or_shift_hme");
  const std::string treeName                = cfg_addMEM.getParameter<std::string>("treeName");
  const std::string selEventsFileName_input = cfg_addMEM.getParameter<std::string>("selEventsFileName_input");
  const std::string process_string          = cfg_addMEM.getParameter<std::string>("process");
  const bool isMC                           = cfg_addMEM.getParameter<bool>("isMC");
  const bool isMC_HH                        = isMC && process_string.find("hh_bbvv")!= std::string::npos;
  const bool isMC_TT                        = isMC && process_string.find("TT")     != std::string::npos;
  std::cout << "isMC_HH = " << isMC_HH << ", isMC_TT = " << isMC_TT << std::endl;
  const bool addMEM_forGenParticles         = cfg_addMEM.getParameter<bool>("addMEM_forGenParticles");
  const bool isDEBUG                        = cfg_addMEM.getParameter<bool>("isDEBUG");
  const bool dryRun                         = cfg_addMEM.getParameter<bool>("dryRun");
  const bool copy_all_branches              = cfg_addMEM.getParameter<bool>("copy_all_branches");
  const bool readGenObjects                 = cfg_addMEM.getParameter<bool>("readGenObjects");
  const bool jetCleaningByIndex             = cfg_addMEM.getParameter<bool>("jetCleaningByIndex");
  const bool useNonNominal                  = cfg_addMEM.getParameter<bool>("useNonNominal");
  const bool useNonNominal_jetmet           = useNonNominal || ! isMC;
  const bool method_MEM                     = cfg_addMEM.getParameter<bool>("method_mem");
  const bool method_HME                     = cfg_addMEM.getParameter<bool>("method_hme");

  const std::string branchName_electrons   = cfg_addMEM.getParameter<std::string>("branchName_electrons");
  const std::string branchName_muons       = cfg_addMEM.getParameter<std::string>("branchName_muons");
  const std::string branchName_jets_ak4    = cfg_addMEM.getParameter<std::string>("branchName_jets_ak4");
  const std::string branchName_jets_ak8    = cfg_addMEM.getParameter<std::string>("branchName_jets_ak8");
  const std::string branchName_subjets_ak8 = cfg_addMEM.getParameter<std::string>("branchName_subjets_ak8");
  const std::string branchName_met         = cfg_addMEM.getParameter<std::string>("branchName_met");

  // branches specific to HH->bbWW signal events
  std::string branchName_genLeptons;
  std::string branchName_genNeutrinos;
  std::string branchName_genParticlesFromHiggs;
  // branches specific to tt+jets background events
  std::string branchName_genLeptonsFromTop;
  std::string branchName_genNeutrinosFromTop;
  std::string branchName_genBJetsFromTop;
  if ( addMEM_forGenParticles )
  {
    edm::ParameterSet cfg_branchNames_genParticles = cfg_addMEM.getParameter<edm::ParameterSet>("branchNames_genParticles");
    if ( isMC_HH )
    {
      branchName_genLeptons = cfg_branchNames_genParticles.getParameter<std::string>("branchName_genLeptons");
      branchName_genNeutrinos = cfg_branchNames_genParticles.getParameter<std::string>("branchName_genNeutrinos");
      branchName_genParticlesFromHiggs = cfg_branchNames_genParticles.getParameter<std::string>("branchName_genParticlesFromHiggs");
    }
    else if ( isMC_TT )
    {
      branchName_genLeptonsFromTop = cfg_branchNames_genParticles.getParameter<std::string>("branchName_genLeptonsFromTop");
      branchName_genNeutrinosFromTop = cfg_branchNames_genParticles.getParameter<std::string>("branchName_genNeutrinosFromTop");
      branchName_genBJetsFromTop = cfg_branchNames_genParticles.getParameter<std::string>("branchName_genBJetsFromTop");
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

  if ( central_or_shifts_mem.empty() || central_or_shifts_hme.empty())
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
  for(const std::string & central_or_shift_hme: central_or_shifts_hme)
  {
    if(std::find(central_or_shifts.begin(), central_or_shifts.end(), central_or_shift_hme) == central_or_shifts.end())
    {
      central_or_shifts.push_back(central_or_shift_hme);
    }
  }
  const int nof_central_or_shift_mem = central_or_shifts_mem.size();
  const int nof_central_or_shift_hme = central_or_shifts_hme.size();

  HMEInterface_hh_bb2l hmeInterface_hh_bb2l;
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
  RecoJetCollectionSelector jetSelectorAK4(era, -1, isDEBUG);
  RecoJetCollectionSelectorBtagLoose jetSelectorAK4_bTagLoose(era, -1, isDEBUG);
  RecoJetCollectionSelectorBtagMedium jetSelectorAK4_bTagMedium(era, -1, isDEBUG);

  RecoJetReaderAK8* jetReaderAK8 = new RecoJetReaderAK8(era, isMC, branchName_jets_ak8, branchName_subjets_ak8);
  jetReaderAK8->set_central_or_shift(useNonNominal_jetmet ? kJetMET_central_nonNominal : kJetMET_central);
  jetReaderAK8->read_sys(isMC);
  jetReaderAK8->setBranchAddresses(inputTree);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR08(0.8, isDEBUG);
  RecoJetCollectionSelectorAK8_hh_bbWW_Hbb jetSelectorAK8_Hbb(era, -1, isDEBUG);

//--- declare missing transverse energy
  RecoMEtReader* metReader = new RecoMEtReader(era, isMC, branchName_met);
  metReader->setMEt_central_or_shift(useNonNominal_jetmet ? kJetMET_central_nonNominal : kJetMET_central);
  metReader->read_ptPhi_systematics(isMC);
  metReader->setBranchAddresses(inputTree);

//--- declare genParticle readers
  GenLeptonReader *   genLeptonReader            = nullptr;
  GenParticleReader * genNeutrinoReader          = nullptr;
  GenParticleReader * genParticleFromHiggsReader = nullptr;
  GenLeptonReader *   genLeptonFromTopReader     = nullptr;
  GenParticleReader * genNeutrinoFromTopReader   = nullptr;
  GenParticleReader * genBJetFromTopReader       = nullptr;
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
    }
    else if ( isMC_TT )
    {
      genLeptonFromTopReader = new GenLeptonReader(branchName_genLeptonsFromTop);
      genLeptonFromTopReader->setBranchAddresses(inputTree);
      genNeutrinoFromTopReader = new GenParticleReader(branchName_genNeutrinosFromTop);
      genNeutrinoFromTopReader->setBranchAddresses(inputTree);
      genBJetFromTopReader = new GenParticleReader(branchName_genBJetsFromTop);
      genBJetFromTopReader->setBranchAddresses(inputTree);
    }
  }

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

  RecoMuonWriter *     muonWriter                 = nullptr;
  RecoElectronWriter * electronWriter             = nullptr;
  RecoJetWriter *      jetWriterAK4               = nullptr;
  RecoJetWriterAK8 *   jetWriterAK8               = nullptr;
  RecoMEtWriter *      metWriter                  = nullptr;
  EventInfoWriter *    eventInfoWriter            = nullptr;

  GenParticleWriter *  genLeptonWriter            = nullptr;
  GenParticleWriter *  genNeutrinoWriter          = nullptr;
  GenParticleWriter *  genParticleFromHiggsWriter = nullptr;
  GenParticleWriter *  genLeptonFromTopWriter     = nullptr;
  GenParticleWriter *  genNeutrinoFromTopWriter   = nullptr;
  GenParticleWriter *  genBJetFromTopWriter       = nullptr;

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
    jetWriterAK8 = new RecoJetWriterAK8(era, isMC, Form("n%s", branchName_jets_ak8.data()), branchName_jets_ak8, Form("n%s", branchName_subjets_ak8.data()), branchName_subjets_ak8);
    jetWriterAK8->set_central_or_shift(useNonNominal_jetmet ? kJetMET_central_nonNominal : kJetMET_central);
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

        outputCommands_string.push_back(Form("drop n%s", branchName_genLeptons.data()));
        outputCommands_string.push_back(Form("drop n%s_*", branchName_genLeptons.data()));
        outputCommands_string.push_back(Form("drop %s_*", branchName_genLeptons.data()));
        outputCommands_string.push_back(Form("drop n%s", branchName_genNeutrinos.data()));
        outputCommands_string.push_back(Form("drop n%s_*", branchName_genNeutrinos.data()));
        outputCommands_string.push_back(Form("drop %s_*", branchName_genNeutrinos.data()));
        outputCommands_string.push_back(Form("drop n%s", branchName_genParticlesFromHiggs.data()));
        outputCommands_string.push_back(Form("drop n%s_*", branchName_genParticlesFromHiggs.data()));
        outputCommands_string.push_back(Form("drop %s_*", branchName_genParticlesFromHiggs.data()));
      }
      else if ( isMC_TT )
      {
        genLeptonFromTopWriter = new GenParticleWriter(Form("n%s", branchName_genLeptonsFromTop.data()), branchName_genLeptonsFromTop);
        genLeptonFromTopWriter->setBranches(outputTree);
        genNeutrinoFromTopWriter = new GenParticleWriter(Form("n%s", branchName_genNeutrinosFromTop.data()), branchName_genNeutrinosFromTop);
        genNeutrinoFromTopWriter->setBranches(outputTree);
        genBJetFromTopWriter = new GenParticleWriter(Form("n%s", branchName_genBJetsFromTop.data()), branchName_genBJetsFromTop);
        genBJetFromTopWriter->setBranches(outputTree);

        outputCommands_string.push_back(Form("drop n%s", branchName_genLeptonsFromTop.data()));
        outputCommands_string.push_back(Form("drop n%s_*", branchName_genLeptonsFromTop.data()));
        outputCommands_string.push_back(Form("drop %s_*", branchName_genLeptonsFromTop.data()));
        outputCommands_string.push_back(Form("drop n%s", branchName_genNeutrinosFromTop.data()));
        outputCommands_string.push_back(Form("drop n%s_*", branchName_genNeutrinosFromTop.data()));
        outputCommands_string.push_back(Form("drop %s_*", branchName_genNeutrinosFromTop.data()));
        outputCommands_string.push_back(Form("drop n%s", branchName_genBJetsFromTop.data()));
        outputCommands_string.push_back(Form("drop n%s_*", branchName_genBJetsFromTop.data()));
        outputCommands_string.push_back(Form("drop %s_*", branchName_genBJetsFromTop.data()));
      }
    }

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

  const std::string branchName_memOutput = get_memObjectBranchName("hh_bb2l", leptonSelection_string, "", "");
  const std::string branchName_memOutput_missingBJet = Form("%s_missingBJet", branchName_memOutput.data());

  std::map<std::string, std::map<std::string, MEMOutputWriter_hh_bb2l *>> memWriter;
  std::map<std::string, std::map<std::string, MEMOutputWriter_hh_bb2l *>> memWriter_missingBJet;

  for ( const std::string & central_or_shift: central_or_shifts_mem )
  {
    for(auto BMlocal : BMS)
    {
      std::string namebranch;
      if ( BMlocal == "SM") namebranch = Form("%s_%s", branchName_memOutput.data(), central_or_shift.data());
      else namebranch = Form("%s_%s_%s", branchName_memOutput.data(), central_or_shift.data(), BMlocal.c_str());
      const std::string branchName_memOutput_cos(namebranch);
      memWriter[BMlocal][central_or_shift] = new MEMOutputWriter_hh_bb2l(
        Form("n%s", branchName_memOutput_cos.data()), branchName_memOutput_cos
      );
      memWriter[BMlocal][central_or_shift]->setBranches(outputTree);
      //
      std::string namebranch_missingBJet;
      if ( BMlocal == "SM") namebranch = Form("%s_%s", branchName_memOutput_missingBJet.data(), central_or_shift.data());
      else namebranch_missingBJet = Form("%s_%s_%s", branchName_memOutput_missingBJet.data(), central_or_shift.data(), BMlocal.c_str());
      const std::string branchName_memOutput_missingBJet_cos(namebranch_missingBJet);
      memWriter_missingBJet[BMlocal][central_or_shift] = new MEMOutputWriter_hh_bb2l(
        Form("n%s", branchName_memOutput_missingBJet_cos.data()), branchName_memOutput_missingBJet_cos
      );
      memWriter_missingBJet[BMlocal][central_or_shift]->setBranches(outputTree);
      std::cout << "writing MEMOutput_hh_bb2l objects for systematic " << central_or_shift
                << " to branch = '" << branchName_memOutput_cos << "'\n";
    }
  }

  const std::string branchName_memOutput_gen = Form("%s_gen", branchName_memOutput.data());
  const std::string branchName_memOutput_gen_missingBJet = Form("%s_missingBJet", branchName_memOutput_gen.data());
  const std::string branchName_memOutput_gen_missingHadWJet = Form("%s_missingHadWJet", branchName_memOutput_gen.data());

  std::map<std::string, MEMOutputWriter_hh_bb2l *> memWriter_gen;//             = nullptr;
  std::map<std::string, MEMOutputWriter_hh_bb2l *> memWriter_gen_missingBJet;// = nullptr;
  for(auto BMlocal : memWriter_gen) BMlocal.second = nullptr;
  for(auto BMlocal : memWriter_gen_missingBJet) BMlocal.second = nullptr;

  if ( addMEM_forGenParticles )
  {
    for(auto BMlocal : BMS)
    {
      std::string namebranch;
      if ( BMlocal == "SM") namebranch = branchName_memOutput_gen.data();
      else namebranch = Form("%s_%s", branchName_memOutput_gen.data(), BMlocal.c_str());
      memWriter_gen[BMlocal] = new MEMOutputWriter_hh_bb2l(Form("n%s", namebranch.c_str()), branchName_memOutput_gen);
      memWriter_gen[BMlocal]->setBranches(outputTree);
      //
      std::string namebranch_missingBJet;
      if ( BMlocal == "SM") namebranch = branchName_memOutput_gen_missingBJet.data();
      else namebranch = Form("%s_%s", branchName_memOutput_gen_missingBJet.data(), BMlocal.c_str());
      memWriter_gen_missingBJet[BMlocal] = new MEMOutputWriter_hh_bb2l(Form("n%s", namebranch_missingBJet.c_str()), branchName_memOutput_gen_missingBJet);
      memWriter_gen_missingBJet[BMlocal]->setBranches(outputTree);
    }
  }

  const std::string branchName_hmeOutput = get_hmeObjectBranchName("hh_bb2l", leptonSelection_string, "", "");

  std::map<std::string, HMEOutputWriter_hh_bb2l *> hmeWriter;

  for ( const std::string & central_or_shift: central_or_shifts_hme )
  {
    const std::string branchName_hmeOutput_cos(
      Form("%s_%s", branchName_hmeOutput.data(), central_or_shift.data())
    );
    hmeWriter[central_or_shift] = new HMEOutputWriter_hh_bb2l(
      Form("n%s", branchName_hmeOutput_cos.data()), branchName_hmeOutput_cos
    );
    hmeWriter[central_or_shift]->setBranches(outputTree);
    std::cout << "writing HMEOutput_hh_bb2l objects for systematic " << central_or_shift
              << " to branch = '" << branchName_hmeOutput_cos << "'\n";
  }

  const int numEntries = inputTree->GetEntries();
  int analyzedEntries = 0;
  int selectedEntries = 0;
  int memComputations = 0;
  int hmeComputations = 0;
  cutFlowTableType cutFlowTable;
  for ( int idxEntry = skipEvents; idxEntry < numEntries && (maxEvents == -1 || idxEntry < (skipEvents + maxEvents)); ++idxEntry )
  {
    //if (analyzedEntries > 0) break;

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

    const std::vector<const RecoLepton*> preselLeptons = pickFirstNobjects(preselLeptonsFull, 2);
    const std::vector<const RecoLepton*> fakeableLeptons = pickFirstNobjects(fakeableLeptonsFull, 2);
    const std::vector<const RecoLepton*> tightLeptons = getIntersection(fakeableLeptons, tightLeptonsFull, isHigherConePt);

//--- build collections of jets
    const std::vector<RecoJet> jets_ak4 = jetReaderAK4->read();
    const std::vector<const RecoJet*> jet_ptrs_ak4 = convert_to_ptrs(jets_ak4);
    const std::vector<RecoJetAK8> jets_ak8 = jetReaderAK8->read();
    const std::vector<const RecoJetAK8*> jet_ptrs_ak8 = convert_to_ptrs(jets_ak8);

    const RecoMEt met = metReader->read();

//--- build collections of generator level particles
    std::vector<GenLepton>   genLeptons;
    std::vector<GenParticle> genNeutrinos;
    std::vector<GenParticle> genParticlesFromHiggs;
    std::vector<GenLepton>   genLeptonsFromTop;
    std::vector<GenParticle> genNeutrinosFromTop;
    std::vector<GenParticle> genBJetsFromTop;
    if ( addMEM_forGenParticles )
    {
      if ( isMC_HH )
      {
        genLeptons            = genLeptonReader->read();
        genNeutrinos          = genNeutrinoReader->read();
        genParticlesFromHiggs = genParticleFromHiggsReader->read();
      }
      else if ( isMC_TT )
      {
        genLeptonsFromTop     = genLeptonFromTopReader->read();
        genNeutrinosFromTop   = genNeutrinoFromTopReader->read();
        genBJetsFromTop       = genBJetFromTopReader->read();
      }
    }

    std::map<std::string, std::map<std::string, std::vector<MEMOutput_hh_bb2l>>> memOutputs_hh_bb2l;
    std::map<std::string, std::map<std::string, std::vector<MEMOutput_hh_bb2l>>> memOutputs_hh_bb2l_missingBJet;

    for ( const std::string & central_or_shift: central_or_shifts_mem )
    {
      for(auto BMlocal : BMS)
      {
        memOutputs_hh_bb2l[BMlocal][central_or_shift] = {};
        memOutputs_hh_bb2l_missingBJet[BMlocal][central_or_shift] = {};
      }
    }

    std::map<std::string, std::vector<MEMOutput_hh_bb2l>> memOutputs_hh_bb2l_gen;
    std::map<std::string, std::vector<MEMOutput_hh_bb2l>> memOutputs_hh_bb2l_gen_missingBJet;
    for(auto BMlocal : BMS)
    {
      memOutputs_hh_bb2l_gen[BMlocal] = {};
      memOutputs_hh_bb2l_gen_missingBJet[BMlocal] = {};
    }

    std::map<std::string, std::vector<HMEOutput_hh_bb2l>> hmeOutputs_hh_bb2l;

    for ( const std::string & central_or_shift: central_or_shifts_hme )
    {
      hmeOutputs_hh_bb2l[central_or_shift] = {};
    }

//--- fill the branches here since because we want to re-use the readers
//    however, the readers obtain pointers to gen level objects and pass them to the reco objects
//    thus, if we try to re-read the objects, these pointers will be overwritten and become invalid
//    therefore, we have to write the reco objects before re-reading new stuff
    if ( copy_all_branches )
    {
      eventInfoWriter->write(eventInfo);
      muonWriter->write(preselMuons);
      electronWriter->write(preselElectronsUncleaned);
      jetWriterAK4->write(jet_ptrs_ak4); // save central
      jetWriterAK8->write(jet_ptrs_ak8); // save central
      metWriter->write(met); // save central

      if ( addMEM_forGenParticles )
      {
        if ( isMC_HH )
        {
          genLeptonWriter->write(convert_to_genParticles(genLeptons));
          genNeutrinoWriter->write(genNeutrinos);
          genParticleFromHiggsWriter->write(genParticlesFromHiggs);
        }
        else if ( isMC_TT )
        {
          genLeptonFromTopWriter->write(convert_to_genParticles(genLeptonsFromTop));
          genNeutrinoFromTopWriter->write(genNeutrinosFromTop);
          genBJetFromTopWriter->write(genBJetsFromTop);
        }
      }

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
      std::map<std::string, int> idxPermutation_mem;
      std::map<std::string, int> idxPermutation_mem_missingBJet;
      std::map<std::string, int> idxPermutation_mem_gen;
      std::map<std::string, int> idxPermutation_mem_gen_missingBJet;
      int idxPermutation_hme = 0;
      for(auto BMlocal : BMS)
      {
        idxPermutation_mem[BMlocal] = 0;
        idxPermutation_mem_missingBJet[BMlocal] = 0;
        idxPermutation_mem_gen[BMlocal] = 0;
        idxPermutation_mem_gen_missingBJet[BMlocal] = 0;
      }

      const std::vector<const RecoLepton*> selLeptons = mergeLeptonCollections(selElectrons, selMuons, isHigherConePt);
      for ( std::size_t selLepton_lead_idx = 0; selLepton_lead_idx < selLeptons.size(); ++selLepton_lead_idx )
      {
        const RecoLepton * selLepton_lead = selLeptons[selLepton_lead_idx];
        if(isDEBUG)
        {
          std::cout << "selLepton_lead: " << *selLepton_lead << '\n';
        }
        for ( std::size_t selLepton_sublead_idx = selLepton_lead_idx + 1; selLepton_sublead_idx < selLeptons.size(); ++selLepton_sublead_idx )
        {
          const RecoLepton * selLepton_sublead = selLeptons[selLepton_sublead_idx];
          if(isDEBUG)
          {
            std::cout << "selLepton_sublead: " << *selLepton_sublead << '\n';
          }
          for ( const std::string & central_or_shift: central_or_shifts )
          {
            checkOptionValidity(central_or_shift, isMC);
            const int jetPt_option = useNonNominal_jetmet ? kJetMET_central_nonNominal : getJet_option(central_or_shift, isMC);
            const int met_option   = useNonNominal_jetmet ? kJetMET_central_nonNominal : getMET_option(central_or_shift, isMC);
            const int fatJetPt_option = useNonNominal_jetmet ? kFatJet_central_nonNominal : getFatJet_option(central_or_shift, isMC);

            if((
                 (
                   jetPt_option    == kJetMET_central &&
                   met_option      == kJetMET_central &&
                   fatJetPt_option == kFatJet_central &&
                   ! useNonNominal_jetmet
                 ) ||
                useNonNominal_jetmet
               ) &&
               central_or_shift != "central")
            {
              if(isDEBUG)
              {
                std::cout << "Skipping systematics: " << central_or_shift << '\n';
              }
              continue;
            }
            else if(isDEBUG)
            {
              std::cout << "Attempting to evaluate the MEM score for systematics: " << central_or_shift << "\n"
                        << "jetPt_option    = " << jetPt_option    << "\n"
                        << "fatJetPt_option = " << fatJetPt_option << "\n"
                        << "met_option      = " << met_option      << '\n'
              ;
            }
            const bool is_central_or_shift_mem = std::find(
                central_or_shifts_mem.begin(), central_or_shifts_mem.end(), central_or_shift
              ) != central_or_shifts_mem.end()
            ;
            const bool is_central_or_shift_hme = std::find(
                central_or_shifts_hme.begin(), central_or_shifts_hme.end(), central_or_shift
              ) != central_or_shifts_hme.end()
            ;

            jetReaderAK4->setPtMass_central_or_shift(jetPt_option);
            jetReaderAK8->set_central_or_shift(fatJetPt_option);
            metReader->setMEt_central_or_shift(met_option);

            const std::vector<RecoJet> jets_ak4_mem = jetReaderAK4->read();
            const std::vector<const RecoJet*> jet_ptrs_ak4_mem = convert_to_ptrs(jets_ak4_mem);
            const std::vector<const RecoJet*> cleanedJetsAK4_wrtLeptons = jetCleaningByIndex ?
              jetCleanerAK4_byIndex(jet_ptrs_ak4_mem, fakeableLeptons) :
              jetCleanerAK4_dR04   (jet_ptrs_ak4_mem, fakeableLeptons)
            ;
            const std::vector<RecoJetAK8> jets_ak8_mem = jetReaderAK8->read();
            const std::vector<const RecoJetAK8*> jet_ptrs_ak8_mem = convert_to_ptrs(jets_ak8_mem);
            const std::vector<const RecoJetAK8*> cleanedJetsAK8_wrtLeptons = jetCleanerAK8_dR08(jet_ptrs_ak8_mem, fakeableLeptons);
            const std::vector<const RecoJetAK8*> selJetsAK8_Hbb = jetSelectorAK8_Hbb(cleanedJetsAK8_wrtLeptons, isHigherCSV_ak8);
            const std::vector<const RecoJet*> selJetsAK4_Hbb = jetSelectorAK4(cleanedJetsAK4_wrtLeptons, isHigherCSV);

            // select jets from H->bb decay
            std::vector<selJetsType_Hbb> selJets_Hbb = selectJets_Hbb(selJetsAK8_Hbb, selJetsAK4_Hbb);
            assert(selJets_Hbb.size() == 1);
            const selJetsType_Hbb& selJets1_Hbb = selJets_Hbb[0];
            //const RecoJetAK8* selJetAK8_Hbb = selJets1_Hbb.fatjet_;
            const RecoJetBase* selJet1_Hbb = selJets1_Hbb.jet_or_subjet1_;
            const RecoJetBase* selJet2_Hbb = selJets1_Hbb.jet_or_subjet2_;

            const RecoMEt met_mem = metReader->read();

            // match reconstructed to generator-level particles
            if ( addMEM_forGenParticles )
            {
              std::vector<const RecoJetBase*> selJets_Hbb_base;
              if ( selJet1_Hbb ) selJets_Hbb_base.push_back(selJet1_Hbb);
              if ( selJet2_Hbb ) selJets_Hbb_base.push_back(selJet2_Hbb);
              if ( isMC_HH )
              {
                genParticleMatcherFromHiggs.setGenParticles(genParticlesFromHiggs, genLeptons, genNeutrinos, {});
                genParticleMatcherFromHiggs({ selLepton_lead, selLepton_sublead }, selJets_Hbb_base, {}, met);
              }
              else if ( isMC_TT )
              {
                genParticleMatcherFromTop.setGenParticles(genLeptonsFromTop, genNeutrinosFromTop, {}, genBJetsFromTop);
                genParticleMatcherFromTop({ selLepton_lead, selLepton_sublead }, selJets_Hbb_base, {}, met);
              }
            }

            if ( selJet1_Hbb && selJet2_Hbb && (selLepton_lead->charge()*selLepton_sublead->charge() < 0) )
            {
              const bool run_mem = method_MEM && is_central_or_shift_mem;
              if ( run_mem )
              {
                for(auto BMlocal : BMS)
                {
                  if ( isDEBUG )
                  {
                    std::cout<<"Doing BM:" << BMlocal << "\n";
                    std::cout << "computing MEMOutput_hh_bb2l objects for branch = '" << branchName_memOutput << "',"
                              << " systematic = '" << central_or_shift << "'\n";
                  }
                  MEMOutput_hh_bb2l memOutput = compMEM(
                    eventInfo,
                    selLepton_lead, selLepton_sublead,
                    selJet1_Hbb, selJet2_Hbb,
                    met,
                    memInterface_hh_bb2l, BMlocal, false, dryRun,
                    idxPermutation_mem[BMlocal], maxPermutations_addMEM_hh_bb2l*nof_central_or_shift_mem,
                    branchName_memOutput, central_or_shift, isDEBUG
                  );
                    memOutputs_hh_bb2l[BMlocal][central_or_shift].push_back(memOutput);
                    if (BMlocal == "SM") ++memComputations;
                  if ( isDEBUG )
                  {
                    std::cout << "#memOutputs_hh_bb2l = "
                              << memOutputs_hh_bb2l[BMlocal][central_or_shift].size() << '\n';
                    for (auto out : memOutputs_hh_bb2l[BMlocal][central_or_shift])
                    {
                      std::cout << BMlocal << " " << out << '\n';
                    }
                  }

                  if ( addMEM_forGenParticles && (central_or_shift == "central" ||  central_or_shift == "") )
                  {
                    MEMOutput_hh_bb2l memOutput_gen = compMEM(
                      eventInfo,
                      selLepton_lead, selLepton_sublead,
                      selJet1_Hbb, selJet2_Hbb,
                      met,
                      memInterface_hh_bb2l, BMlocal, true, dryRun,
                      idxPermutation_mem_gen[BMlocal], maxPermutations_addMEM_hh_bb2l,
                      branchName_memOutput_gen, central_or_shift, isDEBUG);
                    memOutputs_hh_bb2l_gen[BMlocal].push_back(memOutput_gen);
                    if (BMlocal == "SM") ++memComputations;
                  }
                  if ( isDEBUG )
                  {
                    std::cout << "computing MEMOutput_hh_bb2l objects for branch = '" << branchName_memOutput_missingBJet << "',"
                              << " systematic = '" << central_or_shift << "'\n";
                  }
                  MEMOutput_hh_bb2l memOutput_missingBJet1 = compMEM(
                    eventInfo,
                    selLepton_lead, selLepton_sublead,
                    selJet2_Hbb, nullptr,
                    met,
                          memInterface_hh_bb2l, BMlocal, false, dryRun,
                    idxPermutation_mem_missingBJet[BMlocal], maxPermutations_addMEM_hh_bb2l*nof_central_or_shift_mem,
                          branchName_memOutput_missingBJet, central_or_shift, isDEBUG);
                    memOutputs_hh_bb2l_missingBJet[BMlocal][central_or_shift].push_back(memOutput_missingBJet1);
                    if(BMlocal == "SM")
                    {
                      ++memComputations;
                    }
                    if ( isDEBUG )
                    {
                      std::cout << "#memOutputs_hh_bb2l_missingBJet = "
                                << memOutputs_hh_bb2l_missingBJet[BMlocal][central_or_shift].size() << std::endl;
                    }

                  if ( addMEM_forGenParticles && (central_or_shift == "central" ||  central_or_shift == "") )
                  {
                    MEMOutput_hh_bb2l memOutput_gen_missingBJet1 = compMEM(
                      eventInfo,
                      selLepton_lead, selLepton_sublead,
                      selJet2_Hbb, nullptr,
                      met,
                      memInterface_hh_bb2l, BMlocal, true, dryRun,
                      idxPermutation_mem_gen_missingBJet[BMlocal], maxPermutations_addMEM_hh_bb2l,
                      branchName_memOutput_gen_missingBJet, central_or_shift, isDEBUG);
                    memOutputs_hh_bb2l_gen_missingBJet[BMlocal].push_back(memOutput_gen_missingBJet1);
                    if (BMlocal == "SM") ++memComputations;
                  }
                  MEMOutput_hh_bb2l memOutput_missingBJet2 = compMEM(
                    eventInfo,
                    selLepton_lead, selLepton_sublead,
                    selJet1_Hbb, nullptr,
                    met,
                    memInterface_hh_bb2l, BMlocal, false, dryRun,
                    idxPermutation_mem_missingBJet[BMlocal], maxPermutations_addMEM_hh_bb2l*nof_central_or_shift_mem,
                    branchName_memOutput_missingBJet, central_or_shift, isDEBUG);
                    memOutputs_hh_bb2l_missingBJet[BMlocal][central_or_shift].push_back(memOutput_missingBJet2);
                  if (BMlocal == "SM") ++memComputations;
                  if ( isDEBUG )
                  {
                    std::cout << "#memOutputs_hh_bb2l_missingBJet = "
                              << memOutputs_hh_bb2l_missingBJet[BMlocal][central_or_shift].size() << std::endl;
                  }

                  if ( addMEM_forGenParticles && (central_or_shift == "central" ||  central_or_shift == "") )
                  {
                    MEMOutput_hh_bb2l memOutput_gen_missingBJet2 = compMEM(
                      eventInfo,
                      selLepton_lead, selLepton_sublead,
                      selJet1_Hbb, nullptr,
                      met,
                      memInterface_hh_bb2l, BMlocal, true, dryRun,
                      idxPermutation_mem_gen_missingBJet[BMlocal], maxPermutations_addMEM_hh_bb2l,
                      branchName_memOutput_gen_missingBJet, central_or_shift, isDEBUG);
                    memOutputs_hh_bb2l_gen_missingBJet[BMlocal].push_back(memOutput_gen_missingBJet2);
                    if (BMlocal == "SM") ++memComputations;
                  }
                } // for BMS
              } // run_mem

              const bool run_hme = method_HME && is_central_or_shift_hme;
              if ( run_hme )
              {
                if ( idxPermutation_hme <= maxPermutations_addMEM_hh_bb2l * nof_central_or_shift_hme )
                {
                  ++idxPermutation_hme;
                  std::cout << "computing HME for " << eventInfo
                            << " (idxPermutation = " << idxPermutation_hme << "):\n"
                               "inputs:\n"
                            << " leading lepton:    " << *(static_cast<const ChargedParticle *>(selLepton_lead)) << "\n"
                            << " subleading lepton: " << *(static_cast<const ChargedParticle *>(selLepton_sublead)) << "\n"
                            << " b-jet #1:          " << *(static_cast<const Particle *>(selJet1_Hbb)) << "\n"
                            << " b-jet #2:          " << *(static_cast<const Particle *>(selJet2_Hbb)) << "\n"
                            << " MET:               " << met << '\n'
                  ;

                  HMEOutput_hh_bb2l hmeOutput_hh_bb2l;
                  if ( dryRun )
                  {
                    hmeOutput_hh_bb2l.fillInputs(selLepton_lead, selLepton_sublead, selJet1_Hbb, selJet2_Hbb);
                  }
                  else
                  {
                    const int ievent = eventInfo.event;
                    hmeOutput_hh_bb2l = hmeInterface_hh_bb2l(selLepton_lead, selLepton_sublead, selJet1_Hbb, selJet2_Hbb, met_mem, ievent);
                  }
                  hmeOutput_hh_bb2l.eventInfo_ = eventInfo;
                  std::cout << "output (" << central_or_shift << "): " << hmeOutput_hh_bb2l
                  ;
                  hmeOutputs_hh_bb2l[central_or_shift].push_back(hmeOutput_hh_bb2l);

                  ++hmeComputations;
                  if ( isDEBUG )
                  {
                    std::cout << "#hmeOutputs_hh_bb2l = " << hmeOutputs_hh_bb2l[central_or_shift].size() << '\n';
                  }
                }
                else if ( idxPermutation_hme == (maxPermutations_addMEM_hh_bb2l * nof_central_or_shift_hme + 1) )
                {
                  // CV: print warning only once per event
                  std::cout << "Warning in " << eventInfo << ":\n"
                    "Number of permutations exceeds 'maxPermutations_addMEM_hh_bb2l' = "
                            << maxPermutations_addMEM_hh_bb2l << " --> skipping HME computation after "
                            << maxPermutations_addMEM_hh_bb2l << " permutations !!\n";
                }
              } // run_hme
            } // selJet1_Hbb && selJet2_Hbb
          } // central_or_shift
        } // selLepton_sublead_idx
      } // selLepton_lead_idx
    } // maxPermutations_addMEM_hh_bb2l >= 1

    for ( const std::string & central_or_shift: central_or_shifts_mem )
    {
      for(auto BMlocal : BMS)
      {
        memWriter[BMlocal][central_or_shift]->write(memOutputs_hh_bb2l[BMlocal][central_or_shift]);
        memWriter_missingBJet[BMlocal][central_or_shift]->write(memOutputs_hh_bb2l_missingBJet[BMlocal][central_or_shift]);
      }
    }

    if ( addMEM_forGenParticles )
    {
      for(auto BMlocal : BMS)
      {
        memWriter_gen[BMlocal]->write(memOutputs_hh_bb2l_gen[BMlocal]);
        memWriter_gen_missingBJet[BMlocal]->write(memOutputs_hh_bb2l_gen_missingBJet[BMlocal]);
      }
    }

    for ( const std::string & central_or_shift: central_or_shifts_hme )
    {
      hmeWriter[central_or_shift]->write(hmeOutputs_hh_bb2l[central_or_shift]);
    }

    outputTree->Fill();
    ++selectedEntries;
  } // idxEntry

  std::cout << "num. Entries = "      << numEntries      << "\n"
               " analyzed = "         << analyzedEntries << "\n"
               " selected = "         << selectedEntries << "\n"
               "#MEM computations = " << memComputations << "\n"
               "#HME computations = " << hmeComputations << "\n"
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
  delete metReader;

  delete genLeptonReader;
  delete genNeutrinoReader;
  delete genParticleFromHiggsReader;
  delete genLeptonFromTopReader;
  delete genNeutrinoFromTopReader;
  delete genBJetFromTopReader;

  for ( auto & kv: memWriter_gen )
  {
    if ( kv.second )
    {
      delete kv.second;
      kv.second = nullptr;
    }
  }

  for ( auto & kv: memWriter_gen_missingBJet )
  {
    if ( kv.second )
    {
      delete kv.second;
      kv.second = nullptr;
    }
  }

  for ( auto & kv: hmeWriter )
  {
    if ( kv.second )
    {
      delete kv.second;
      kv.second = nullptr;
    }
  }

  delete inputTree;

//--- copy histograms keeping track of number of processed events from input files to output file
  copyHistograms(inputFiles, copy_histograms_regex, fs);

  clock.Show("addMEM_hh_bb2l");

  return EXIT_SUCCESS;
}
