#include "tthAnalysis/HiggsToTauTau/interface/mvaInputVariables.h" // comp_*()
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronReader.h" // RecoElectronReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonReader.h" // RecoMuonReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetReader.h" // RecoJetReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetReaderAK8.h" // RecoJetReaderAK8
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEtReader.h" // RecoMEtReader
#include "tthAnalysis/HiggsToTauTau/interface/convert_to_ptrs.h" // convert_to_ptrs()
#include "tthAnalysis/HiggsToTauTau/interface/ParticleCollectionCleaner.h" // Reco*CollectionCleaner
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronCollectionSelectorLoose.h" // RecoElectronCollectionSelectorLoose
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonCollectionSelectorLoose.h" // RecoMuonCollectionSelectorLoose
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetCollectionSelector.h" // RecoJetCollectionSelector
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetCollectionSelectorAK8.h" // RecoJetCollectionSelectorAK8
#include "tthAnalysis/HiggsToTauTau/interface/RunLumiEventSelector.h" // RunLumiEventSelector
#include "tthAnalysis/HiggsToTauTau/interface/leptonTypes.h" // kElectron, kMuon
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // isHigherConePt(), mergeLeptonCollections()
#include "tthAnalysis/HiggsToTauTau/interface/sysUncertOptions.h" // k*_central
#include "tthAnalysis/HiggsToTauTau/interface/hltPath.h" // hltPath, create_hltPaths(), hltPaths_isTriggered()re
#include "tthAnalysis/HiggsToTauTau/interface/hltPathReader.h" // hltPathReader
#include "tthAnalysis/HiggsToTauTau/interface/TTreeWrapper.h" // TTreeWrapper

#include "hhAnalysis/multilepton/interface/EventInfoHH.h" // EventInfoHH
#include "hhAnalysis/multilepton/interface/EventInfoHHReader.h" // EventInfoHHReader
#include "hhAnalysis/multilepton/interface/RecoJetCollectionSelectorAK8_hh_Wjj.h" // RecoJetSelectorAK8_hh_Wjj

#include "hhAnalysis/bbww/interface/SyncNtupleManager_bbww.h" // SyncNtupleManager_bbww
#include "hhAnalysis/bbww/interface/RecoJetCollectionSelectorAK8_hh_bbWW_Hbb.h" // RecoJetSelectorAK8_hh_bbWW_Hbb

#include <FWCore/ParameterSet/interface/ParameterSet.h> // edm::ParameterSet
#include <FWCore/PythonParameterSet/interface/MakeParameterSets.h> // edm::readPSetsFrom()
#include <DataFormats/FWLite/interface/InputSource.h> // fwlite::InputSource
#include <DataFormats/Math/interface/deltaR.h> // deltaR()

#include <TBenchmark.h> // TBenchmark
#include <TError.h> // gErrorAbortLevel, kError

#include <boost/math/special_functions/sign.hpp> // boost::math::sign()

#include <cstdlib> // EXIT_SUCCESS, EXIT_FAILURE
#include <fstream> // std::ofstream
#include <numeric> // std::accumulate()

typedef std::vector<std::string> vstring;

/**
 * @brief Run sync Ntuple in inclusive mode
 */
int
main(int argc,
     char * argv[])
{
//--- throw an exception in case ROOT encounters an error
  gErrorAbortLevel = kError;

//--- parse command-line arguments
  if(argc < 2)
  {
    std::cout << "Usage: " << argv[0] << " [parameters.py]\n";
    return EXIT_FAILURE;
  }

  std::cout << "<analyze_hh_bbww_inclusive>:\n";

//--- keep track of time it takes the macro to execute
  TBenchmark clock;
  clock.Start("analyze_hh_bbww_inclusive");

//--- read python configuration parameters
  if(! edm::readPSetsFrom(argv[1])->existsAs<edm::ParameterSet>("process"))
  {
    throw cmsException("analyze_inclusive")
      << "No ParameterSet 'process' found in configuration file = " << argv[1] << " !!\n";
  }

  const edm::ParameterSet cfg = edm::readPSetsFrom(argv[1])->getParameter<edm::ParameterSet>("process");
  const edm::ParameterSet cfg_analyze = cfg.getParameter<edm::ParameterSet>("analyze_hh_bbww_inclusive");

  const std::string treeName = cfg_analyze.getParameter<std::string>("treeName");
  const std::string process_string = cfg_analyze.getParameter<std::string>("process");

  const std::string era_string = cfg_analyze.getParameter<std::string>("era");
  const int era = get_era(era_string);

  vstring triggerNames_1e = cfg_analyze.getParameter<vstring>("triggers_1e");
  std::vector<hltPath*> triggers_1e = create_hltPaths(triggerNames_1e);
  vstring triggerNames_2e = cfg_analyze.getParameter<vstring>("triggers_2e");
  std::vector<hltPath*> triggers_2e = create_hltPaths(triggerNames_2e);
  vstring triggerNames_1mu = cfg_analyze.getParameter<vstring>("triggers_1mu");
  std::vector<hltPath*> triggers_1mu = create_hltPaths(triggerNames_1mu);
  vstring triggerNames_2mu = cfg_analyze.getParameter<vstring>("triggers_2mu");
  std::vector<hltPath*> triggers_2mu = create_hltPaths(triggerNames_2mu);
  vstring triggerNames_1e1mu = cfg_analyze.getParameter<vstring>("triggers_1e1mu");
  std::vector<hltPath*> triggers_1e1mu = create_hltPaths(triggerNames_1e1mu);

  const std::string central_or_shift = cfg_analyze.getParameter<std::string>("central_or_shift");

  const bool isMC               = cfg_analyze.getParameter<bool>("isMC");
  const bool useNonNominal      = cfg_analyze.getParameter<bool>("useNonNominal");
  const bool useNonNominal_jetmet = useNonNominal || ! isMC;

  checkOptionValidity(central_or_shift, isMC);
  const int jetBtagSF_option           = getBTagWeight_option   (central_or_shift);

  const int met_option   = useNonNominal_jetmet ? kMEt_central_nonNominal : getMET_option(central_or_shift, isMC);
  const int jetPt_option = useNonNominal_jetmet ? kJet_central_nonNominal : getJet_option(central_or_shift, isMC);

  const bool isDEBUG = cfg_analyze.getParameter<bool>("isDEBUG");

  const std::string branchName_electrons = cfg_analyze.getParameter<std::string>("branchName_electrons");
  const std::string branchName_muons     = cfg_analyze.getParameter<std::string>("branchName_muons");
  const std::string branchName_jets      = cfg_analyze.getParameter<std::string>("branchName_jets");
  const std::string branchName_fatJets   = cfg_analyze.getParameter<std::string>("branchName_fatJets");
  const std::string branchName_subJets   = cfg_analyze.getParameter<std::string>("branchName_subJets");
  const std::string branchName_fatJetsLS = cfg_analyze.getParameter<std::string>("branchName_fatJetsLS");
  const std::string branchName_subJetsLS = cfg_analyze.getParameter<std::string>("branchName_subJetsLS");
  const std::string branchName_met       = cfg_analyze.getParameter<std::string>("branchName_met");

  const std::string selEventsFileName_input = cfg_analyze.getParameter<std::string>("selEventsFileName_input");
  std::cout << "selEventsFileName_input = " << selEventsFileName_input << '\n';
  RunLumiEventSelector * run_lumi_eventSelector = nullptr;
  if(! selEventsFileName_input.empty())
  {
    edm::ParameterSet cfgRunLumiEventSelector;
    cfgRunLumiEventSelector.addParameter<std::string>("inputFileName", selEventsFileName_input);
    cfgRunLumiEventSelector.addParameter<std::string>("separator", ":");
    run_lumi_eventSelector = new RunLumiEventSelector(cfgRunLumiEventSelector);
  }

  const fwlite::InputSource inputFiles(cfg);
  const int maxEvents = inputFiles.maxEvents();
  std::cout << " maxEvents = " << maxEvents << '\n';
  const unsigned reportEvery = inputFiles.reportAfter();

  TTreeWrapper * const inputTree = new TTreeWrapper(treeName.data(), inputFiles.files(), maxEvents);
  std::cout << "Loaded " << inputTree->getFileCount() << " file(s).\n";

//--- prepare sync Ntuple
  const edm::ParameterSet syncNtuple_cfg = cfg_analyze.getParameter<edm::ParameterSet>("syncNtuple");
  const std::string syncNtuple_tree = syncNtuple_cfg.getParameter<std::string>("tree");
  const std::string syncNtuple_output = syncNtuple_cfg.getParameter<std::string>("output");
  if(syncNtuple_tree.empty() || syncNtuple_output.empty())
  {
    throw cmsException("analyze_inclusive", __LINE__)
      << "Need to specify both analyze_inclusive.syncNtuple.tree and "
         "analyze_inclusive.syncNtuple.output in order to run this program";
  }
  SyncNtupleManager_bbww * const snm = new SyncNtupleManager_bbww(syncNtuple_output, syncNtuple_tree);
  snm->initializeBranches();
  snm->initializeHLTBranches({
    triggers_1e, triggers_1mu, triggers_2e, triggers_1e1mu, triggers_2mu,
  });

//--- declare event-level variables
  EventInfoHH eventInfo(isMC);
  EventInfoHHReader eventInfoReader(&eventInfo);
  inputTree->registerReader(&eventInfoReader);

  hltPathReader hltPathReader_instance({
    triggers_1e, triggers_1mu, triggers_2e, triggers_1e1mu, triggers_2mu,
  });
  inputTree -> registerReader(&hltPathReader_instance);

//--- declare particle collections
  RecoMuonReader * const muonReader = new RecoMuonReader(era, branchName_muons, false);
  inputTree->registerReader(muonReader);
  const RecoMuonCollectionSelectorLoose preselMuonSelector(era, -1, isDEBUG);

  RecoElectronReader * const electronReader = new RecoElectronReader(era, branchName_electrons, false);
  //electronReader->readUncorrected(useNonNominal);
  inputTree->registerReader(electronReader);
  const RecoElectronCollectionCleaner electronCleaner(0.05, isDEBUG);
  const RecoElectronCollectionSelectorLoose preselElectronSelector(era, -1, isDEBUG);

  RecoJetReader * const jetReader = new RecoJetReader(era, isMC, branchName_jets, false);
  jetReader->setPtMass_central_or_shift(jetPt_option);
  jetReader->setBranchName_BtagWeight(jetBtagSF_option);
  inputTree->registerReader(jetReader);
  const RecoJetCollectionCleaner jetCleaner(0.4, isDEBUG);
  const RecoJetCollectionSelector jetSelector(era, -1, isDEBUG);

  RecoJetReaderAK8 * const jetReaderAK8 = new RecoJetReaderAK8(era, branchName_fatJets, branchName_subJets);
  inputTree->registerReader(jetReaderAK8);
  RecoJetCollectionSelectorAK8_hh_Wjj jetSelectorAK8_Wjj(era, -1, isDEBUG);
  const RecoJetCollectionCleanerAK8 jetCleanerAK8_dR08(0.8, isDEBUG);
  RecoJetCollectionSelectorAK8_hh_bbWW_Hbb jetSelectorAK8_Hbb(era, -1, isDEBUG);

  RecoJetReaderAK8 * const jetReaderAK8LS = new RecoJetReaderAK8(era, branchName_fatJetsLS, branchName_subJetsLS);
  inputTree->registerReader(jetReaderAK8LS);
  const RecoJetCollectionSelectorAK8 jetSelectorAK8LS(era, -1, isDEBUG);
  const RecoJetCollectionCleanerAK8 jetCleanerAK8_dR12(1.2, isDEBUG);
  const RecoJetCollectionCleanerAK8 jetCleanerAK8_dR16(1.6, isDEBUG);

//--- declare missing transverse energy
  RecoMEtReader * const metReader = new RecoMEtReader(era, isMC, branchName_met);
  metReader->setMEt_central_or_shift(met_option);
  inputTree->registerReader(metReader);

  int analyzedEntries = 0;
  int selectedEntries = 0;

  while(inputTree->hasNextEvent() && (! run_lumi_eventSelector || (run_lumi_eventSelector && ! run_lumi_eventSelector -> areWeDone())))
  {
    if(inputTree->canReport(reportEvery))
    {
      std::cout << "processing Entry " << inputTree->getCurrentMaxEventIdx()
                << " or " << inputTree->getCurrentEventIdx() << " entry in #"
                << (inputTree->getProcessedFileCount() - 1)
                << " (" << eventInfo
                << ") file (" << selectedEntries << " Entries selected)\n";
    }
    //if (!(eventInfo.run ==  1 && eventInfo.lumi ==  9909 &&  eventInfo.event == 16803200)) continue; // :
    //if (!( eventInfo.event ==  13863835)) continue; // :
    ++analyzedEntries;

    if(run_lumi_eventSelector && ! (*run_lumi_eventSelector)(eventInfo))
    {
      continue;
    }

    if(run_lumi_eventSelector)
    {
      std::cout << "processing Entry " << inputTree->getCurrentMaxEventIdx() << ": " << eventInfo << '\n';
      if(inputTree->isOpen())
      {
        std::cout << "input File = " << inputTree->getCurrentFileName() << '\n';
      }
    }

    snm->read(eventInfo);
    snm->read(eventInfo.pileupWeight,                 FloatVariableType_bbww::PU_weight);
    snm->read(boost::math::sign(eventInfo.genWeight), FloatVariableType_bbww::MC_weight);

    snm->read({
      triggers_1e, triggers_1mu, triggers_2e, triggers_1e1mu, triggers_2mu,
    });

//--- build collections of electrons, muons and jets
//    resolve overlaps in order of priority: muon, electron,
    const std::vector<RecoMuon> muons = muonReader->read();
    const std::vector<const RecoMuon *> muon_ptrs = convert_to_ptrs(muons);
    // CV: no cleaning needed for muons, as they have the highest priority in the overlap removal
    const std::vector<const RecoMuon *> cleanedMuons = muon_ptrs;
    const std::vector<const RecoMuon *> preselMuons  = preselMuonSelector(cleanedMuons, isHigherPt);
    const std::vector<const RecoMuon *> selMuons     = preselMuons;
    if(isDEBUG)
    {
      printCollection("preselMuons", preselMuons);
    }

    snm->read(preselMuons);

    const std::vector<RecoElectron> electrons = electronReader->read();
    const std::vector<const RecoElectron *> electron_ptrs = convert_to_ptrs(electrons);
    const std::vector<const RecoElectron *> cleanedElectrons = electronCleaner(electron_ptrs, selMuons);
    const std::vector<const RecoElectron *> preselElectrons  = preselElectronSelector(cleanedElectrons, isHigherPt);
    const std::vector<const RecoElectron *> selElectrons     = preselElectrons;
    if(isDEBUG)
    {
      printCollection("preselElectrons", preselElectrons);
    }

    snm->read(preselElectrons);

    const std::vector<const RecoLepton *> preselLeptons = mergeLeptonCollections(preselElectrons, preselMuons, isHigherPt);
    if(isDEBUG)
    {
      printCollection("preselLeptons", preselLeptons);
    }

//--- build collections of jets and select subset of jets passing b-tagging criteria
    const std::vector<RecoJet> jets = jetReader->read();
    const std::vector<const RecoJet *> jet_ptrs = convert_to_ptrs(jets);
    const std::vector<const RecoJet *> cleanedJets = jetCleaner (jet_ptrs, preselLeptons);
    std::vector<const RecoJet *> selJets  = jetSelector(cleanedJets, isHigherPt);
    if(isDEBUG)
    {
      printCollection("cleanedJets", cleanedJets);
      printCollection("selJets", selJets);
    }
    // preselected AK4 jets, sorted by pT in decreasing order
    snm->read(selJets);

    const std::vector<RecoJetAK8> fatJets = jetReaderAK8->read();
    const std::vector<const RecoJetAK8 *> fatJet_ptrs = convert_to_ptrs(fatJets);
    const std::vector<const RecoJetAK8 *> cleanedFatJets = jetCleanerAK8_dR08(fatJet_ptrs, preselLeptons);
    std::vector<const RecoJetAK8 *> selFatJets = jetSelectorAK8_Hbb(cleanedFatJets, isHigherPt);
    if(isDEBUG)
    {
      printCollection("cleanedFatJets", cleanedFatJets);
      printCollection("selFatJets", selFatJets);
    }
    // "regular" AK8 jets, selected to target H->bb decay, sorted by pT in decreasing order
    snm->read(selFatJets, false);

    const std::vector<RecoJetAK8> fatJetsLS = jetReaderAK8LS->read();
    const std::vector<const RecoJetAK8 *> fatJetLS_ptrs = convert_to_ptrs(fatJetsLS);

    std::vector<const RecoJetAK8 *> selFatJetsLS;
    if(! preselLeptons.empty())
    {
      if(isDEBUG)
      {
        std::cout << "Number of preselected leptons = " << preselLeptons.size() << " > 0\n";
      }
      jetSelectorAK8_Wjj.getSelector().set_leptons(preselLeptons);
      if(! selFatJets.empty())
      {
        // sort "regular" AK8 jets that passed H->bb selection by their b-tagging score
        std::sort(selFatJets.begin(), selFatJets.end(), isHigherCSV_ak8);
        // pick the AK8 jet with the highest b-tagging score that passed H->bb selection
        const std::vector<const RecoJetAK8 *> selFatJets_Hbb = { selFatJets[0] };
        const std::vector<const RecoJetAK8 *> cleaned_selFatJetsLS = jetCleanerAK8_dR16(fatJetLS_ptrs, selFatJets_Hbb);
        if(isDEBUG)
        {
          printCollection("cleaned_selFatJetsLS", cleaned_selFatJetsLS);
        }
        std::cout << "Number of AK8 jets = " << selFatJets.size() << " > 0\n";
        selFatJetsLS = jetSelectorAK8_Wjj(cleaned_selFatJetsLS, isHigherPt);
      }
      else if(selJets.size() >= 2)
      {
        // sort AK4 jets by their b-tagging score
        std::sort(selJets.begin(), selJets.end(), isHigherCSV);
        // pick the two AK4 jets with the highest b-tagging score
        std::vector<const RecoJet *> selJetsAK4_Hbb = { selJets[0], selJets[1] };
        const std::vector<const RecoJetAK8 *> cleaned_selFatJetsLS = jetCleanerAK8_dR12(fatJetLS_ptrs, selJetsAK4_Hbb);
        if(isDEBUG)
        {
          std::cout << "Number of AK4 jets = " << selJets.size() << " >= 2\n";
          printCollection("cleaned_selFatJetsLS", cleaned_selFatJetsLS);
        }
        selFatJetsLS = jetSelectorAK8_Wjj(cleaned_selFatJetsLS, isHigherPt);
      }
      else if(isDEBUG)
      {
        std::cout << "Not enough AK4 or AK8 jets to clean AK8LS jets\n";
        selFatJetsLS = jetSelectorAK8_Wjj(fatJetLS_ptrs, isHigherPt);
      }
    }
    // lepton-subtracted AK8 jets in which the leptons that are subtracted from pass loose preselection
    // the AK8 jets have been selected to target H->WW*->lnujj decays, sorted by pT in decreasing order
    snm->read(selFatJetsLS, true);

    if(isDEBUG)
    {
      printCollection("fatJetLS_ptrs", fatJetLS_ptrs);
      printCollection("selFatJetsLS", selFatJetsLS);
    }

//--- compute MHT and linear MET discriminant (met_LD)
    RecoMEt met = metReader->read();

    snm->read(met.pt(),  FloatVariableType_bbww::PFMET);
    snm->read(met.phi(), FloatVariableType_bbww::PFMETphi);

    snm->fill();

    ++selectedEntries;
  }

  snm->write();

  std::cout << "max num. Entries = " << inputTree->getCumulativeMaxEventCount()
            << " (limited by " << maxEvents << ") processed in "
            << inputTree->getProcessedFileCount() << " file(s) (out of "
            << inputTree->getFileCount() << ")\n"
            << " analyzed = " << analyzedEntries << '\n'
            << " selected = " << selectedEntries << "\n\n";

  delete run_lumi_eventSelector;

  delete muonReader;
  delete electronReader;
  delete jetReader;
  delete metReader;

  delete inputTree;
  delete snm;

  clock.Show("analyze_hh_bbww_inclusive");

  return EXIT_SUCCESS;
}
