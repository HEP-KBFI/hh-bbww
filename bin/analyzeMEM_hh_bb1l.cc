#include "FWCore/ParameterSet/interface/ParameterSet.h" // edm::ParameterSet
#include "FWCore/PythonParameterSet/interface/MakeParameterSets.h" // edm::readPSetsFrom()
#include "FWCore/Utilities/interface/Exception.h" // cms::Exception
#include "PhysicsTools/FWLite/interface/TFileService.h" // fwlite::TFileService
#include "DataFormats/FWLite/interface/InputSource.h" // fwlite::InputSource
#include "DataFormats/FWLite/interface/OutputFiles.h" // fwlite::OutputFiles
#include "DataFormats/Math/interface/LorentzVector.h" // math::PtEtaPhiMLorentzVector, math::XYZTLorentzVectorD
#include "DataFormats/Math/interface/deltaR.h" // deltaR

#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h" // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/RecoJet.h" // RecoJet
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEt.h" // RecoMEt
#include "tthAnalysis/HiggsToTauTau/interface/GenLepton.h" // GenLepton
#include "tthAnalysis/HiggsToTauTau/interface/GenJet.h" // GenJet
#include "tthAnalysis/HiggsToTauTau/interface/GenParticle.h" // GenParticle
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronReader.h" // RecoElectronReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonReader.h" // RecoMuonReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetReader.h" // RecoJetReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetReaderAK8.h" // RecoJetReaderAK8
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEtReader.h" // RecoMEtReader
#include "tthAnalysis/HiggsToTauTau/interface/GenLeptonReader.h" // GenLeptonReader
#include "tthAnalysis/HiggsToTauTau/interface/GenJetReader.h" // GenJetReader
#include "tthAnalysis/HiggsToTauTau/interface/GenParticleReader.h" // GenParticleReader
#include "tthAnalysis/HiggsToTauTau/interface/LHEInfoReader.h" // LHEInfoReader
#include "tthAnalysis/HiggsToTauTau/interface/TMVAInterface.h" // TMVAInterface
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
#include "tthAnalysis/HiggsToTauTau/interface/leptonTypes.h" // getLeptonType, kElectron, kMuon
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // getBTagWeight_option, getHadTau_genPdgId, isHigherPt, isMatched
#include "tthAnalysis/HiggsToTauTau/interface/generalAuxFunctions.h" // format_vstring
#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow
#include "tthAnalysis/HiggsToTauTau/interface/cutFlowTable.h" // cutFlowTableType
#include "tthAnalysis/HiggsToTauTau/interface/TTreeWrapper.h" // TTreeWrapper
#include "tthAnalysis/HiggsToTauTau/interface/EvtWeightManager.h" // EvtWeightManager
#include "tthAnalysis/HiggsToTauTau/interface/GenLeptonCollectionSelector.h" // GenLeptonCollectionSelector
#include "tthAnalysis/HiggsToTauTau/interface/GenJetCollectionSelector.h" // GenJetCollectionSelector

#include "hhAnalysis/multilepton/interface/EvtWeightRecorderHH.h" // EvtWeightRecorderHH
#include "hhAnalysis/multilepton/interface/RecoJetCollectionSelectorAK8_hh_Wjj.h" // RecoJetSelectorAK8_hh_Wjj

#include "hhAnalysis/bbww/interface/RecoJetCollectionSelectorAK8_hh_bbWW_Hbb.h" // RecoJetSelectorAK8_hh_bbWW_Hbb
#include "hhAnalysis/bbww/interface/MEMOutput_hh_bb1l.h" // MEMOutput_hh_bb1l
#include "hhAnalysis/bbww/interface/MEMOutputReader_hh_bb1l.h" // MEMOutputReader_hh_bb1l
#include "hhAnalysis/bbww/interface/jetSelectionAuxFunctions.h" // selectJets_Hbb, countBJetsJets_Hbb, selectJets_Wjj
#include "hhAnalysis/bbww/interface/JetPair.h" // JetPair_Wjj, makeJetPairs_Wjj, initialize_mva_Wjj, rankJetPairs_Wjj, getIndex_isGenMatched
#include "hhAnalysis/bbww/interface/genMatchingAuxFunctions.h" // isGenMatched, countGenMatchedParticles
#include "hhAnalysis/bbww/interface/GenParticleMatcherFromHiggs.h" // GenParticleMatcherFromHiggs
#include "hhAnalysis/bbww/interface/GenParticleMatcherFromTop.h" // GenParticleMatcherFromTop
#include "hhAnalysis/bbww/interface/analyzeMEM_genJetHistograms.h" // genJetHistograms, fillHistograms_genJets
#include "hhAnalysis/bbww/interface/analyzeMEM_jetHistograms.h" // jetHistograms, fillHistograms_jets
#include "hhAnalysis/bbww/interface/analyzeMEM_memHistograms.h" // memHistograms, fillHistograms_mem
#include "hhAnalysis/bbww/interface/dumpGenParticles.h" // dumpGenParticles, dumpGenLeptons, dumpGenJets
#include "hhAnalysis/bbww/interface/genBoostedAuxFunctions.h" // isBoosted_genHbb, isBoosted_genWjj

#include <TBenchmark.h> // TBenchmark
#include <TString.h> // TString, Form
#include <TError.h> // gErrorAbortLevel, kError
#include <TRandom3.h> // TRandom3
#include <TROOT.h> // TROOT
#include <TH1.h> // TH1, TH1D
#include <TH2.h> // TH2, TH2D
#include <TMath.h> // TMath::Abs

#include <boost/algorithm/string/predicate.hpp> // boost::starts_with()
#include <boost/math/special_functions/sign.hpp> // boost::math::sign()
#include <boost/algorithm/string/replace.hpp> // boost::replace_all_copy()

#include <iostream> // std::cerr, std::fixed
#include <iomanip> // std::setprecision(), std::setw()
#include <string> // std::string
#include <vector> // std::vector<>
#include <cstdlib> // EXIT_SUCCESS, EXIT_FAILURE
#include <cmath> // std::abs
#include <fstream> // std::ofstream
#include <assert.h> // assert

typedef math::PtEtaPhiMLorentzVector LV;
typedef std::vector<std::string> vstring;
typedef std::vector<double> vdouble;

void 
fillHistograms_numGenWJets(const std::vector<const RecoJet*>& jet_ptrs_ak4,
                           const std::vector<const RecoJet*>& cleanedJetsAK4_wrtLeptons,
                           const RecoJetCollectionCleaner& jetCleanerAK4_dR04, 
                           const RecoJetCollectionSelector& jetSelectorAK4_Wjj,
                           const RecoJetBase* selJet1_Hbb, const RecoJetBase* selJet2_Hbb, 
                           const RecoLepton* selLepton,
                           int nBJetMedium, 
                           const TMVAInterface& mva_Wjj,
                           const EventInfo& eventInfo,
                           const std::vector<const GenJet*>& genWJets, const std::vector<const GenJet*>& genBJets, 
                           TH1* histogram_numGenWJets_ak4,
                           TH1* histogram_numGenWJets_ak4cleanedWrtLeptons,
                           TH1* histogram_numGenWJets_ak4cleanedWrtGenHbb,
                           TH1* histogram_numGenWJets_ak4cleanedWrtHbb,
                           TH1* histogram_numGenWJets_ak4selected,
                           TH1* histogram_numGenWJets_ak4byWjjPairs,
                           double evtWeight)
{
  int numGenWJets_ak4 = selectGenMatchedParticles(jet_ptrs_ak4, genWJets).size();
  fillWithOverFlow(histogram_numGenWJets_ak4, numGenWJets_ak4, evtWeight);

  int numGenWJets_ak4cleanedWrtLeptons = selectGenMatchedParticles(cleanedJetsAK4_wrtLeptons, genWJets).size();
  fillWithOverFlow(histogram_numGenWJets_ak4cleanedWrtLeptons, numGenWJets_ak4cleanedWrtLeptons, evtWeight);

  const std::vector<const RecoJet*> cleanedJetsAK4_wrtGenHbb = jetCleanerAK4_dR04(cleanedJetsAK4_wrtLeptons, genBJets);
  int numGenWJets_ak4cleanedWrtGenHbb = selectGenMatchedParticles(cleanedJetsAK4_wrtGenHbb, genWJets).size();
  fillWithOverFlow(histogram_numGenWJets_ak4cleanedWrtGenHbb, numGenWJets_ak4cleanedWrtGenHbb, evtWeight);

  assert(selJet1_Hbb && selJet2_Hbb);
  const std::vector<const RecoJet*> cleanedJetsAK4_wrtHbb = jetCleanerAK4_dR04(cleanedJetsAK4_wrtLeptons, std::vector<const RecoJetBase*>({ selJet1_Hbb, selJet2_Hbb }));
  int numGenWJets_ak4cleanedWrtHbb = selectGenMatchedParticles(cleanedJetsAK4_wrtHbb, genWJets).size();
  fillWithOverFlow(histogram_numGenWJets_ak4cleanedWrtHbb, numGenWJets_ak4cleanedWrtHbb, evtWeight);

  const std::vector<const RecoJet*> selJetsAK4_Wjj = jetSelectorAK4_Wjj(cleanedJetsAK4_wrtHbb, isHigherPt);
  int numGenWJets_ak4selected = selectGenMatchedParticles(selJetsAK4_Wjj, genWJets).size();
  fillWithOverFlow(histogram_numGenWJets_ak4selected, numGenWJets_ak4selected, evtWeight);

  std::vector<JetPair_Wjj> jetPairs_Wjj = makeJetPairs_Wjj(selJetsAK4_Wjj, &genWJets);
  assert(selLepton);
  rankJetPairs_Wjj(jetPairs_Wjj, selJetsAK4_Wjj, *selLepton, nBJetMedium, mva_Wjj, eventInfo);
  std::vector<const RecoJetBase*> selJetsAK4_byWjjPairs;
  if ( jetPairs_Wjj.size() >= 1 )
  {
    selJetsAK4_byWjjPairs.push_back(jetPairs_Wjj[0].jet1_);
    selJetsAK4_byWjjPairs.push_back(jetPairs_Wjj[0].jet2_);
  }
  int numGenWJets_ak4byWjjPairs = selectGenMatchedParticles(selJetsAK4_byWjjPairs, genWJets).size();
  fillWithOverFlow(histogram_numGenWJets_ak4byWjjPairs, numGenWJets_ak4byWjjPairs, evtWeight);
}

void updateCutFlowTable(cutFlowTableType& cutFlowTable, const std::string& column, bool passesBoosted_Hbb, bool passesBoosted_Wjj, double evtWeight)
{
  if      ( passesBoosted_Hbb && passesBoosted_Wjj ) cutFlowTable.update("boosted",      column, evtWeight);
  else if ( passesBoosted_Hbb                      ) cutFlowTable.update("semi-boosted", column, evtWeight);
  else                                               cutFlowTable.update("resolved",     column, evtWeight);
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

  std::cout << "<analyzeMEM_hh_bb1l>:" << std::endl;

//--- keep track of time it takes the macro to execute
  TBenchmark clock;
  clock.Start("analyzeMEM_hh_bb1l");

//--- read python configuration parameters
  if ( !edm::readPSetsFrom(argv[1])->existsAs<edm::ParameterSet>("process") )
    throw cms::Exception("analyzeMEM_hh_bb1l")
      << "No ParameterSet 'process' found in configuration file = " << argv[1] << " !!\n";

  edm::ParameterSet cfg = edm::readPSetsFrom(argv[1])->getParameter<edm::ParameterSet>("process");

  edm::ParameterSet cfg_analyze = cfg.getParameter<edm::ParameterSet>("analyzeMEM_hh_bb1l");

  std::string treeName = cfg_analyze.getParameter<std::string>("treeName");

  std::string process_string = cfg_analyze.getParameter<std::string>("process");

  std::string histogramDir = cfg_analyze.getParameter<std::string>("histogramDir");

  std::string era_string = cfg_analyze.getParameter<std::string>("era");
  const int era = get_era(era_string);

  bool isMC = true;
  bool isMC_HH = isMC && process_string.find("hh_bbvv")!= std::string::npos;
  bool isMC_TT = isMC && process_string.find("TT")     != std::string::npos;
  bool isSignal = boost::starts_with(process_string, "signal_") && process_string.find("_hh_") != std::string::npos;
  //bool isMC_HH_nonres = boost::starts_with(process_string, "signal_ggf_nonresonant_");
  bool isMC_HH_nonres = false; // CV: temporary work-around, as branch "mHH_lhe" is missing in Ntuple containing AK4LS jets produced by Karl
  bool hasLHE = cfg_analyze.getParameter<bool>("hasLHE");
  std::string central_or_shift = "central";
  bool apply_genWeight = cfg_analyze.getParameter<bool>("apply_genWeight");

  bool isDEBUG = cfg_analyze.getParameter<bool>("isDEBUG");
  if ( isDEBUG ) std::cout << "Warning: DEBUG mode enabled -> trigger selection will not be applied for data !!" << std::endl;

  std::string branchName_electrons = cfg_analyze.getParameter<std::string>("branchName_electrons");
  std::string branchName_muons = cfg_analyze.getParameter<std::string>("branchName_muons");
  std::string branchName_jets_ak4 = cfg_analyze.getParameter<std::string>("branchName_jets_ak4");
  std::string branchName_jets_ak4LS = cfg_analyze.getParameter<std::string>("branchName_jets_ak4LS");
  std::string branchName_jets_ak8 = cfg_analyze.getParameter<std::string>("branchName_jets_ak8");
  std::string branchName_subjets_ak8 = cfg_analyze.getParameter<std::string>("branchName_subjets_ak8");
  std::string branchName_jets_ak8LS = cfg_analyze.getParameter<std::string>("branchName_jets_ak8LS");
  std::string branchName_subjets_ak8LS = cfg_analyze.getParameter<std::string>("branchName_subjets_ak8LS");
  std::string branchName_met = cfg_analyze.getParameter<std::string>("branchName_met");

  std::string branchName_memOutput = cfg_analyze.getParameter<std::string>("branchName_memOutput");
  std::string branchName_memOutput_missingBJet = cfg_analyze.getParameter<std::string>("branchName_memOutput_missingBJet");
  std::string branchName_memOutput_missingHadWJet = cfg_analyze.getParameter<std::string>("branchName_memOutput_missingHadWJet");

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

  //bool jetCleaningByIndex = cfg_analyze.getParameter<bool>("jetCleaningByIndex");

  fwlite::InputSource inputFiles(cfg);
  int maxEvents = inputFiles.maxEvents();
  std::cout << " maxEvents = " << maxEvents << std::endl;
  unsigned reportEvery = inputFiles.reportAfter();

  fwlite::OutputFiles outputFile(cfg);
  fwlite::TFileService fs = fwlite::TFileService(outputFile.file().data());

  TTreeWrapper* inputTree = new TTreeWrapper(treeName.data(), inputFiles.files(), maxEvents);
  std::cout << "Loaded " << inputTree->getFileCount() << " file(s)\n";

//--- declare event-level variables
  EventInfo eventInfo(true, isSignal, isMC_HH_nonres);
  const std::string default_cat_str = "default";
  std::vector<std::string> evt_cat_strs = { default_cat_str };

  EventInfoReader eventInfoReader(&eventInfo);
  inputTree->registerReader(&eventInfoReader);

//--- declare particle collections
  RecoMuonReader* muonReader = new RecoMuonReader(era, branchName_muons, isMC, false);
  inputTree->registerReader(muonReader);
  RecoMuonCollectionGenMatcher muonGenMatcher;
  RecoMuonCollectionSelectorLoose preselMuonSelector(era, -1, isDEBUG);
  RecoMuonCollectionSelectorTight tightMuonSelector(era, -1, isDEBUG);

  RecoElectronReader* electronReader = new RecoElectronReader(era, branchName_electrons, isMC, false);
  inputTree->registerReader(electronReader);
  RecoElectronCollectionGenMatcher electronGenMatcher;
  RecoElectronCollectionCleaner electronCleaner(0.3, isDEBUG);
  RecoElectronCollectionSelectorLoose preselElectronSelector(era, -1, isDEBUG);
  RecoElectronCollectionSelectorTight tightElectronSelector(era, -1, isDEBUG);

  const double selElectron_min_pt = 32.;
  const double selElectron_max_absEta = 2.5;
  const double selMuon_min_pt = 25.;
  const double selMuon_max_absEta = 2.4;  

  RecoJetReader* jetReaderAK4 = new RecoJetReader(era, isMC, branchName_jets_ak4, false);
  inputTree->registerReader(jetReaderAK4);
  RecoJetReader* jetReaderAK4LS = nullptr;
  if ( branchName_jets_ak4LS != branchName_jets_ak4 )
  {
    jetReaderAK4LS = new RecoJetReader(era, isMC, branchName_jets_ak4LS, false);
    inputTree->registerReader(jetReaderAK4LS); 
  }
  RecoJetCollectionCleaner jetCleanerAK4_dR04(0.4, isDEBUG);
  //RecoJetCollectionCleaner jetCleanerAK4_dR04(0.2, isDEBUG); // CV: ONLY FOR TESTING !!
  //RecoJetCollectionCleanerByIndex jetCleanerAK4_byIndex(isDEBUG);
  RecoJetCollectionCleaner jetCleanerAK4_dR08(0.8, isDEBUG);
  RecoJetCollectionCleaner jetCleanerAK4_dR12(1.2, isDEBUG);
  RecoJetCollectionSelector jetSelectorAK4(era, -1, isDEBUG);
  RecoJetCollectionSelectorBtagLoose jetSelectorAK4_bTagLoose(era, -1, isDEBUG);
  RecoJetCollectionSelectorBtagMedium jetSelectorAK4_bTagMedium(era, -1, isDEBUG);
  
  // define pT and eta cuts for "resolved" (AK4) jets from H->bb decay
  const double selJetAK4_min_pt_Hbb = 25.;
  const double selJetAK4_max_absEta_Hbb = 2.4;

  RecoJetCollectionSelector jetSelectorAK4_Hbb(era, -1, isDEBUG);
  jetSelectorAK4_Hbb.getSelector().set_min_pt(selJetAK4_min_pt_Hbb);
  jetSelectorAK4_Hbb.getSelector().set_max_absEta(selJetAK4_max_absEta_Hbb);

  // define pT and eta cuts for "resolved" (AK4) jets from W->jj decay
  const double selJetAK4_min_pt_Wjj = 25.;
  //const double selJetAK4_max_absEta_Wjj = 4.7;
  const double selJetAK4_max_absEta_Wjj = 2.4;

  RecoJetCollectionSelector jetSelectorAK4_Wjj(era, -1, isDEBUG);
  jetSelectorAK4_Wjj.getSelector().set_min_pt(selJetAK4_min_pt_Wjj);
  jetSelectorAK4_Wjj.getSelector().set_max_absEta(selJetAK4_max_absEta_Wjj);

  RecoJetReaderAK8* jetReaderAK8 = new RecoJetReaderAK8(era, isMC, branchName_jets_ak8, branchName_subjets_ak8);
  inputTree->registerReader(jetReaderAK8);
  RecoJetReaderAK8* jetReaderAK8LS = new RecoJetReaderAK8(era, isMC, branchName_jets_ak8LS, branchName_subjets_ak8LS);
  inputTree->registerReader(jetReaderAK8LS);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR08(0.8, isDEBUG);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR12(1.2, isDEBUG);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR16(1.6, isDEBUG);
  RecoJetCollectionSelectorAK8_hh_bbWW_Hbb jetSelectorAK8_Hbb(era, -1, isDEBUG);
  RecoJetCollectionSelectorAK8_hh_Wjj jetSelectorAK8LS_Wjj(era, -1, isDEBUG);
 
  MEMOutputReader_hh_bb1l* memReader = nullptr;
  if ( !branchName_memOutput.empty() )
  {
    memReader = new MEMOutputReader_hh_bb1l(
      Form("n%s", branchName_memOutput.data()), branchName_memOutput);
    inputTree->registerReader(memReader);
  }
  MEMOutputReader_hh_bb1l* memReader_missingBJet = nullptr;
  if ( !branchName_memOutput_missingBJet.empty() )
  {
    memReader_missingBJet = new MEMOutputReader_hh_bb1l(
      Form("n%s", branchName_memOutput_missingBJet.data()), branchName_memOutput_missingBJet);
    inputTree->registerReader(memReader_missingBJet);
  }
  MEMOutputReader_hh_bb1l* memReader_missingHadWJet = nullptr;
  if ( !branchName_memOutput_missingHadWJet.empty() )
  {
    memReader_missingHadWJet = new MEMOutputReader_hh_bb1l(
      Form("n%s", branchName_memOutput_missingHadWJet.data()), branchName_memOutput_missingHadWJet);
    inputTree->registerReader(memReader_missingHadWJet);
  }

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
  
  GenLeptonCollectionSelector genLeptonSelector(era, -1, isDEBUG);
  genLeptonSelector.getSelector().set_min_pt_muon(selMuon_min_pt);
  genLeptonSelector.getSelector().set_max_absEta_muon(selMuon_max_absEta);
  genLeptonSelector.getSelector().set_min_pt_electron(selElectron_min_pt);
  genLeptonSelector.getSelector().set_max_absEta_electron(selElectron_max_absEta);

  GenJetCollectionSelector genWJetSelector(era, -1, isDEBUG);
  genWJetSelector.getSelector().set_min_pt(selJetAK4_min_pt_Wjj);
  genWJetSelector.getSelector().set_max_absEta(selJetAK4_max_absEta_Wjj);

  GenJetCollectionSelector genBJetSelector(era, -1, isDEBUG);
  genBJetSelector.getSelector().set_min_pt(selJetAK4_min_pt_Hbb);
  genBJetSelector.getSelector().set_max_absEta(selJetAK4_max_absEta_Hbb);

  //GenJetCollectionCleaner genJetCleaner_dR04(0.4);
  GenJetCollectionCleaner genJetCleaner_dR04(0.2); // CV: ONLY FOR TESTING !!

//--- declare missing transverse energy
  RecoMEtReader* metReader = new RecoMEtReader(era, isMC, branchName_met);
  inputTree->registerReader(metReader);

//--- declare generator level information
  LHEInfoReader* lheInfoReader = new LHEInfoReader(hasLHE);
  inputTree->registerReader(lheInfoReader);
  
//--- initialize BDT for ranking of W->jj decays
  TMVAInterface mva_Wjj = initialize_mva_Wjj();
 
  TH1* histogram_genLepton_pt = fs.make<TH1D>("genLepton_pt", "genLepton_pt", 70, 0., 350.);
  TH1* histogram_genLepton_absEta = fs.make<TH1D>("genLepton_absEta", "genLepton_absEta", 100, 0., 10.);

  genJetHistograms* histograms_genBJet = new genJetHistograms("genBJet");
  histograms_genBJet->bookHistograms(fs);
  genJetHistograms* histograms_genWJet = new genJetHistograms("genWJet");
  histograms_genWJet->bookHistograms(fs);

  TH1* histograms_dRmin_genWJets_to_genLepton = fs.make<TH1D>("dRmin_genWJets_to_genLepton", "dRmin_genWJets_to_genLepton", 50, 0., 5.);
  TH1* histograms_dRmax_genWJets_to_genLepton = fs.make<TH1D>("dRmax_genWJets_to_genLepton", "dRmax_genWJets_to_genLepton", 50, 0., 5.);
  TH1* histograms_genLepton_times_genJetCharge_dRmin = fs.make<TH1D>("genLepton_times_genJetCharge_dRmin", "genLepton_times_genJetCharge_dRmin", 22, -1.1, +1.1);
  TH1* histograms_genAntiLepton_times_genJetCharge_dRmin = fs.make<TH1D>("genAntiLepton_times_genJetCharge_dRmin", "genAntiLepton_times_genJetCharge_dRmin", 22, -1.1, +1.1);
  TH2* histograms_dRmax_vs_dRmin_genWJets_to_genLepton = fs.make<TH2D>("dRmax_vs_dRmin_genWJets_to_genLepton", "dRmax_vs_dRmin_genWJets_to_genLepton", 50, 0., 5., 50, 0., 5.);
  TH1* histograms_dR_genWJets = fs.make<TH1D>("dR_genWJets", "dR_genWJets", 50, 0., 5.);
  TH2* histograms_dR_genWJets_vs_ptWjj = fs.make<TH2D>("dR_genWJets_vs_ptWjj", "dR_genWJets_vs_ptWjj", 50, 0., 500., 50, 0., 5.);
  TH2* histograms_dR_genWJets_vs_ptH = fs.make<TH2D>("dR_genWJets_vs_ptH", "dR_genWJets_vs_ptH", 50, 0., 500., 50, 0., 5.);
  TH2* histograms_dRmin_genWJets_to_genLepton_vs_dR_genWJets = fs.make<TH2D>("dRmin_genWJets_to_genLepton_vs_dR_genWJets", "dRmin_genWJets_to_genLepton_vs_dR_genWJets", 50, 0., 5., 50, 0., 5.);
  TH2* histograms_dRmax_genWJets_to_genLepton_vs_dR_genWJets = fs.make<TH2D>("dRmax_genWJets_to_genLepton_vs_dR_genWJets", "dRmax_genWJets_to_genLepton_vs_dR_genWJets", 50, 0., 5., 50, 0., 5.);
  TH1* histograms_dR_genBJets = fs.make<TH1D>("dR_genBJets", "dR_genBJets", 50, 0., 5.);
  TH2* histograms_dR_genBJets_vs_ptHbb = fs.make<TH2D>("dR_genBJets_vs_ptWjj", "dR_genBJets_vs_ptWHbb", 50, 0., 500., 50, 0., 5.);

  TH2* histogram_selJetCorrelation = fs.make<TH2D>("selJetCorrelation", "selJetCorrelation", 6, -0.5, 5.5, 6, -0.5, 5.5);
  enum { k2Rec2Sel, k2Rec1Sel, k2Rec0Sel, k1Rec1Sel, k1Rec0Sel, k0Rec };
  TAxis* xAxis_selJetCorrelation = histogram_selJetCorrelation->GetXaxis();
  xAxis_selJetCorrelation->SetTitle("H->bb");
  xAxis_selJetCorrelation->SetBinLabel(1, "2Rec2Sel");
  xAxis_selJetCorrelation->SetBinLabel(2, "2Rec1Sel");
  xAxis_selJetCorrelation->SetBinLabel(3, "2Rec0Sel");
  xAxis_selJetCorrelation->SetBinLabel(4, "1Rec1Sel");
  xAxis_selJetCorrelation->SetBinLabel(5, "1Rec0Sel");	
  xAxis_selJetCorrelation->SetBinLabel(6, "0Rec");
  TAxis* yAxis_selJetCorrelation = histogram_selJetCorrelation->GetYaxis();
  yAxis_selJetCorrelation->SetTitle("W->jj");
  yAxis_selJetCorrelation->SetBinLabel(1, "2Rec2Sel");
  yAxis_selJetCorrelation->SetBinLabel(2, "2Rec1Sel");
  yAxis_selJetCorrelation->SetBinLabel(3, "2Rec0Sel");
  yAxis_selJetCorrelation->SetBinLabel(4, "1Rec1Sel");
  yAxis_selJetCorrelation->SetBinLabel(5, "1Rec0Sel");
  yAxis_selJetCorrelation->SetBinLabel(6, "0Rec");

  TH1* histogram_numGenWJets_ak4                  = fs.make<TH1D>("numGenWJets_ak4",                  "numGenWJets_ak4",                  4, -0.5, +3.5);
  TH1* histogram_numGenWJets_ak4cleanedWrtLeptons = fs.make<TH1D>("numGenWJets_ak4cleanedWrtLeptons", "numGenWJets_ak4cleanedWrtLeptons", 4, -0.5, +3.5);
  TH1* histogram_numGenWJets_ak4cleanedWrtGenHbb  = fs.make<TH1D>("numGenWJets_ak4cleanedWrtGenHbb",  "numGenWJets_ak4cleanedWrtGenHbb",  4, -0.5, +3.5);
  TH1* histogram_numGenWJets_ak4cleanedWrtHbb     = fs.make<TH1D>("numGenWJets_ak4cleanedWrtHbb",     "numGenWJets_ak4cleanedWrtHbb",     4, -0.5, +3.5);
  TH1* histogram_numGenWJets_ak4selected          = fs.make<TH1D>("numGenWJets_ak4selected",          "numGenWJets_ak4selected",          4, -0.5, +3.5);
  TH1* histogram_numGenWJets_ak4byWjjPairs        = fs.make<TH1D>("numGenWJets_ak4byWjjPairs",        "numGenWJets_ak4byWjjPairs",        4, -0.5, +3.5);

  TH1* histogram_ak4_genTimesRecJetCharge_upTypeQuarks = fs.make<TH1D>("histogram_ak4_genTimesRececJetCharge_upTypeQuarks", "histogram_ak4_genTimesRecJetCharge_upTypeQuarks", 22, -1.1, +1.1);
  TH1* histogram_ak4_genTimesRecJetCharge_downTypeQuarks = fs.make<TH1D>("histogram_ak4_genTimesRecJetCharge_downTypeQuarks", "histogram_ak4_genTimesRecJetCharge_downTypeQuarks", 22, -1.1, +1.1);
  
  TH1* histogram_ak8_ptWjj_fullyMatched = fs.make<TH1D>("ak8_ptWjj_fullyMatched", "ak8_ptWjj_fullyMatched", 50, 0., 500.);
  TH1* histogram_ak8_ptH_fullyMatched = fs.make<TH1D>("ak8_ptH_fullyMatched", "ak8_ptH_fullyMatched", 50, 0., 500.);

  jetHistograms* histograms_boostedHbb_bjet1 = new jetHistograms("boostedHbb_bjet1");
  histograms_boostedHbb_bjet1->bookHistograms(fs);
  TH1* histogram_boostedHbb_bjet1_idx = fs.make<TH1D>("boostedHbb_bjet1_idx", "boostedHbb_bjet1_idx", 26, -1.5, +24.5);
  jetHistograms* histograms_boostedHbb_bjet2 = new jetHistograms("boostedHbb_bjet2");
  histograms_boostedHbb_bjet2->bookHistograms(fs);
  TH1* histogram_boostedHbb_bjet2_idx = fs.make<TH1D>("boostedHbb_bjet2_idx", "boostedHbb_bjet2_idx", 26, -1.5, +24.5);
  TH1* histogram_boostedHbb_bjet_numIndices = fs.make<TH1D>("boostedHbb_bjet_numIndices", "boostedHbb_bjet_numIndices", 25, -0.5, +24.5);
  TH1* histogram_boostedHbb_bjet_mjj = fs.make<TH1D>("boostedHbb_bjet_mjj", "boostedHbb_bjet_mjj", 50, 0., 250.);

  jetHistograms* histograms_resolvedHbb_bjet1 = new jetHistograms("resolvedHbb_bjet1");
  histograms_resolvedHbb_bjet1->bookHistograms(fs);
  TH1* histogram_resolvedHbb_bjet1_idx = fs.make<TH1D>("resolvedHbb_bjet1_idx", "resolvedHbb_bjet1_idx", 26, -1.5, +24.5);
  jetHistograms* histograms_resolvedHbb_bjet2 = new jetHistograms("resolvedHbb_bjet2");
  histograms_resolvedHbb_bjet2->bookHistograms(fs);
  TH1* histogram_resolvedHbb_bjet2_idx = fs.make<TH1D>("resolvedHbb_bjet2_idx", "resolvedHbb_bjet2_idx", 26, -1.5, +24.5);
  TH1* histogram_resolvedHbb_bjet_numIndices = fs.make<TH1D>("resolvedHbb_bjet_numIndices", "resolvedHbb_bjet_numIndices", 25, -0.5, +24.5);
  TH1* histogram_resolvedHbb_bjet_mjj = fs.make<TH1D>("resolvedHbb_bjet_mjj", "resolvedHbb_bjet_mjj", 50, 0., 250.);
  
  jetHistograms* histograms_Wjj_jet1 = new jetHistograms("Wjj_jet1");
  histograms_Wjj_jet1->bookHistograms(fs);
  TH1* histogram_Wjj_jet1_idx = fs.make<TH1D>("Wjj_jet1_idx", "Wjj_jet1_idx", 26, -1.5, +24.5);
  jetHistograms* histograms_Wjj_jet2 = new jetHistograms("Wjj_jet2");
  histograms_Wjj_jet2->bookHistograms(fs);
  TH1* histogram_Wjj_jet2_idx = fs.make<TH1D>("Wjj_jet2_idx", "Wjj_jet2_idx", 26, -1.5, +24.5);
  TH1* histogram_Wjj_jet_numIndices = fs.make<TH1D>("Wjj_jet_numIndices", "Wjj_jet_numIndices", 25, -0.5, +24.5);
  TH1* histogram_Wjj_jet_mjj = fs.make<TH1D>("Wjj_jet_mjj", "Wjj_jet_mjj", 50, 0., 250.);

  TH1* histogram_hadWJetPair_sortedByMass_idx = fs.make<TH1D>("hadWJetPair_sortedByMass_idx", "hadWJetPair_sortedByMass_idx", 101, -1.5, +99.5);
  TH1* histogram_hadWJetPair_sortedByDeltaR_idx = fs.make<TH1D>("hadWJetPair_sortedByDeltaR_idx", "hadWJetPair_sortedByDeltaR_idx", 101, -1.5, +99.5);
  TH1* histogram_hadWJetPair_sortedByPt_idx = fs.make<TH1D>("hadWJetPair_sortedByPt_idx", "hadWJetPair_sortedByPt_idx", 101, -1.5, +99.5);
  TH1* histogram_hadWJetPair_sortedByScalarPt_idx = fs.make<TH1D>("hadWJetPair_sortedByScalarPt_idx", "hadWJetPair_sortedByScalarPt_idx", 101, -1.5, +99.5);
  TH1* histogram_hadWJetPair_sortedByBDT_idx = fs.make<TH1D>("hadWJetPair_sortedByBDT_idx", "hadWJetPair_sortedByBDT_idx", 101, -1.5, +99.5);
  TH1* histogram_hadWJetPair_numIndices = fs.make<TH1D>("hadWJetPair_numIndices", "hadWJetPair_numIndices", 100, -0.5, +99.5);

  memHistograms* histograms_memOutput_fullyMatched = new memHistograms("", 0, 0, 0);
  histograms_memOutput_fullyMatched->bookHistograms(fs);
  memHistograms* histograms_memOutput_unmatchedLepton = new memHistograms("", 1, 0, 0);
  histograms_memOutput_unmatchedLepton->bookHistograms(fs);
  memHistograms* histograms_memOutput_unmatchedBJet = new memHistograms("", 0, 1, 0);
  histograms_memOutput_unmatchedBJet->bookHistograms(fs);
  memHistograms* histograms_memOutput_unmatchedWJet = new memHistograms("", 0, 0, 1);
  histograms_memOutput_unmatchedWJet->bookHistograms(fs);

  memHistograms* histograms_memOutput_missingBJet_fullyMatched = new memHistograms("missingBJet", 0, 0, 0);
  histograms_memOutput_missingBJet_fullyMatched->bookHistograms(fs);
  memHistograms* histograms_memOutput_missingBJet_unmatchedLepton = new memHistograms("missingBJet", 1, 0, 0);
  histograms_memOutput_missingBJet_unmatchedLepton->bookHistograms(fs);
  memHistograms* histograms_memOutput_missingBJet_unmatchedBJet = new memHistograms("missingBJet", 0, 1, 0);
  histograms_memOutput_missingBJet_unmatchedBJet->bookHistograms(fs);
  memHistograms* histograms_memOutput_missingBJet_unmatchedWJet = new memHistograms("missingBJet", 0, 0, 1);
  histograms_memOutput_missingBJet_unmatchedWJet->bookHistograms(fs);

  memHistograms* histograms_memOutput_missingHadWJet_fullyMatched = new memHistograms("missingHadWJet", 0, 0, 0);
  histograms_memOutput_missingHadWJet_fullyMatched->bookHistograms(fs);
  memHistograms* histograms_memOutput_missingHadWJet_unmatchedLepton = new memHistograms("missingHadWJet", 1, 0, 0);
  histograms_memOutput_missingHadWJet_unmatchedLepton->bookHistograms(fs);
  memHistograms* histograms_memOutput_missingHadWJet_unmatchedBJet = new memHistograms("missingHadWJet", 0, 1, 0);
  histograms_memOutput_missingHadWJet_unmatchedBJet->bookHistograms(fs);
  memHistograms* histograms_memOutput_missingHadWJet_unmatchedWJet = new memHistograms("missingHadWJet", 0, 0, 1);
  histograms_memOutput_missingHadWJet_unmatchedWJet->bookHistograms(fs);

  int analyzedEntries = 0;
  int selectedEntries = 0;
  double selectedEntries_weighted = 0.;
  TH1* histogram_analyzedEntries = fs.make<TH1D>("analyzedEntries", "analyzedEntries", 1, -0.5, +0.5);
  TH1* histogram_selectedEntries = fs.make<TH1D>("selectedEntries", "selectedEntries", 1, -0.5, +0.5);
  cutFlowTableType cutFlowTable({ "gen", "rec", "gen&rec" });
  while ( inputTree->hasNextEvent() ) {
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

    EvtWeightRecorderHH evtWeightRecorder({ "central" }, central_or_shift, isMC);

    if ( apply_genWeight ) evtWeightRecorder.record_genWeight(boost::math::sign(eventInfo.genWeight));
    lheInfoReader->read();
    evtWeightRecorder.record_lheScaleWeight(lheInfoReader);
    evtWeightRecorder.record_puWeight(&eventInfo);

    double evtWeight = evtWeightRecorder.get(central_or_shift);

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
    if ( isDEBUG ) {
      dumpGenLeptons("genLepton", genLeptons);      
      dumpGenJets("genBJet", genBJets);
      dumpGenJets("genWJet", genWJets);
    }
    const Particle::LorentzVector& genMEtP4 = genParticleMatcher->getMEt();

    if ( !(genLeptons.size() == 1) ) {
      continue;
    }
    for ( std::string column : { "gen", "rec", "gen&rec" } ) {
      cutFlowTable.update("exactly 1 gen-lepton", column, evtWeight);
    }

    if ( !(genBJets.size() == 2) ) {
      continue;
    }
    for ( std::string column : { "gen", "rec", "gen&rec" } ) {
      cutFlowTable.update("exactly 2 gen-jets from H->bb decay", column, evtWeight);
    }

    if ( !(genWJets.size() == 2) ) {
      continue;
    }
    for ( std::string column : { "gen", "rec", "gen&rec" } ) {
      cutFlowTable.update("exactly 2 gen-jets from W->jj decay", column, evtWeight);
    }
    
    std::vector<const GenLepton*> genLeptons_ptrs = convert_to_ptrs(genLeptons);
    genLeptonSelector.getSelector().set_min_pt_muon(-1.);
    genLeptonSelector.getSelector().set_min_pt_electron(-1.);
    std::vector<const GenLepton*> genLeptons_passingEta = genLeptonSelector(genLeptons_ptrs);
    genLeptonSelector.getSelector().set_min_pt_muon(selMuon_min_pt);
    genLeptonSelector.getSelector().set_min_pt_electron(selElectron_min_pt);
    std::vector<const GenLepton*> genLeptons_passingPt_and_Eta = genLeptonSelector(genLeptons_ptrs);

    if ( genLeptons_ptrs.size() == 1 )
    {
      const GenLepton* genLepton = genLeptons_ptrs[0];
      fillWithOverFlow(histogram_genLepton_absEta, genLepton->absEta(), evtWeight);
      if ( (genLepton->is_electron() && genLepton->absEta() < selElectron_max_absEta) ||
           (genLepton->is_muon()     && genLepton->absEta() < selMuon_max_absEta    ) ) {
        fillWithOverFlow(histogram_genLepton_pt, genLepton->pt(), evtWeight);
      }
    }

    std::vector<const GenJet*> genBJets_ptrs = convert_to_ptrs(genBJets);
    std::sort(genBJets_ptrs.begin(), genBJets_ptrs.end(), isHigherPt);
    genBJetSelector.getSelector().set_max_absEta(1.e+3);
    std::vector<const GenJet*> genBJets_passingPt = genBJetSelector(genBJets_ptrs);
    genBJetSelector.getSelector().set_max_absEta(selJetAK4_max_absEta_Hbb);
    std::vector<const GenJet*> genBJets_passingPt_and_Eta = genBJetSelector(genBJets_ptrs);
    std::vector<const GenJet*> cleanedGenBJets_wrtLeptons = genJetCleaner_dR04(genBJets_passingPt_and_Eta, genLeptons_passingEta);

    fillHistograms_genJets(genBJets_ptrs, genBJetSelector, *histograms_genBJet, evtWeight);

    std::vector<const GenJet*> genWJets_ptrs = convert_to_ptrs(genWJets);
    std::sort(genWJets_ptrs.begin(), genWJets_ptrs.end(), isHigherPt);
    genWJetSelector.getSelector().set_max_absEta(1.e+3);
    std::vector<const GenJet*> genWJets_passingPt = genWJetSelector(genWJets_ptrs);
    genWJetSelector.getSelector().set_max_absEta(selJetAK4_max_absEta_Wjj);
    std::vector<const GenJet*> genWJets_passingPt_and_Eta = genWJetSelector(genWJets_ptrs);
    std::vector<const GenJet*> cleanedGenWJets_wrtLeptons;
    if ( jetReaderAK4LS )
    {
      cleanedGenWJets_wrtLeptons = genWJets_passingPt_and_Eta; // CV: disable jet cleaning wrt leptons if using ak4LS jets for W->jj decay
    }
    else
    { 
      cleanedGenWJets_wrtLeptons = genJetCleaner_dR04(genWJets_passingPt_and_Eta, genLeptons_passingEta);
    }
    genBJetSelector.getSelector().set_min_pt(10.);
    genBJetSelector.getSelector().set_max_absEta(selJetAK4_max_absEta_Hbb);  
    std::vector<const GenJet*> genBJets_passingEta = genBJetSelector(genBJets_ptrs);
    std::vector<const GenJet*> cleanedGenWJets_wrtHbb = genJetCleaner_dR04(cleanedGenWJets_wrtLeptons, genBJets_passingEta);

    fillHistograms_genJets(genWJets_ptrs, genWJetSelector, *histograms_genWJet, evtWeight);
    
    if ( genLeptons_passingPt_and_Eta.size() == 1 )
    {
      const GenLepton* genLepton = genLeptons_passingPt_and_Eta[0];
      if ( genWJets_passingPt_and_Eta.size() == 2 )
      {
        const GenJet* genWJet1 = genWJets_passingPt_and_Eta[0];
        const GenJet* genWJet2 = genWJets_passingPt_and_Eta[1];
        double dR_genWJet1_to_genLepton = deltaR(genLepton->p4(), genWJet1->p4());
        double dR_genWJet2_to_genLepton = deltaR(genLepton->p4(), genWJet2->p4());
        double dRmin_genWJets_to_genLepton = TMath::Min(dR_genWJet1_to_genLepton, dR_genWJet2_to_genLepton);
        double dRmax_genWJets_to_genLepton = TMath::Max(dR_genWJet1_to_genLepton, dR_genWJet2_to_genLepton);
        fillWithOverFlow(histograms_dRmin_genWJets_to_genLepton, dRmin_genWJets_to_genLepton, evtWeight);
        fillWithOverFlow(histograms_dRmax_genWJets_to_genLepton, dRmax_genWJets_to_genLepton, evtWeight);
        const GenJet* genWJet_dRmin = nullptr;
        if ( dR_genWJet1_to_genLepton < dR_genWJet2_to_genLepton ) genWJet_dRmin = genWJet1;
        else                                                       genWJet_dRmin = genWJet2;
        assert(genLepton->charge() != 0.);
        TH1* histogram = nullptr;
        if ( genLepton->charge() < 0. ) histogram = histograms_genLepton_times_genJetCharge_dRmin;
        else                            histogram = histograms_genAntiLepton_times_genJetCharge_dRmin;
        fillWithOverFlow(histogram, genLepton->charge()*genWJet_dRmin->charge(), evtWeight);
        fillWithOverFlow2d(histograms_dRmax_vs_dRmin_genWJets_to_genLepton, dRmin_genWJets_to_genLepton, dRmax_genWJets_to_genLepton, evtWeight);
        double dR_genWJets = deltaR(genWJet1->p4(), genWJet2->p4());
        fillWithOverFlow(histograms_dR_genWJets, dR_genWJets, evtWeight);
        Particle::LorentzVector genWjjP4 = genWJet1->p4() + genWJet2->p4();
        fillWithOverFlow2d(histograms_dR_genWJets_vs_ptWjj, genWjjP4.pt(), dR_genWJets, evtWeight);
        fillWithOverFlow2d(histograms_dR_genWJets_vs_ptH, (genWjjP4 + genLepton->p4() + genMEtP4).pt(), dR_genWJets, evtWeight);
        fillWithOverFlow2d(histograms_dRmin_genWJets_to_genLepton_vs_dR_genWJets, dR_genWJets, dRmin_genWJets_to_genLepton, evtWeight);
        fillWithOverFlow2d(histograms_dRmax_genWJets_to_genLepton_vs_dR_genWJets, dR_genWJets, dRmax_genWJets_to_genLepton, evtWeight);
      }
    }
    if ( genBJets_passingPt_and_Eta.size() == 2 )
    {
      const GenJet* genBJet1 = genBJets_passingPt_and_Eta[0];
      const GenJet* genBJet2 = genBJets_passingPt_and_Eta[1];
      double dR_genBJets = deltaR(genBJet1->p4(), genBJet2->p4());
      fillWithOverFlow(histograms_dR_genBJets, dR_genBJets, evtWeight);
      fillWithOverFlow2d(histograms_dR_genBJets_vs_ptHbb, (genBJet1->p4() + genBJet2->p4()).pt(), dR_genBJets, evtWeight);
    }

//--- build collections of reconstructed electrons and muons
//    resolve overlaps in order of priority: muon, electron
    const std::vector<RecoMuon> muons = muonReader->read();
    const std::vector<const RecoMuon*> muon_ptrs = convert_to_ptrs(muons);
    const std::vector<const RecoMuon*> cleanedMuons = muon_ptrs; 
    preselMuonSelector.getSelector().set_min_pt(10.);
    const std::vector<const RecoMuon*> looseMuons_passingEta = preselMuonSelector(cleanedMuons, isHigherConePt);
    preselMuonSelector.getSelector().set_min_pt(selMuon_min_pt);
    const std::vector<const RecoMuon*> looseMuons_passingPt_and_Eta = preselMuonSelector(cleanedMuons, isHigherConePt);
    const std::vector<const RecoMuon*> tightMuons_passingPt_and_Eta = tightMuonSelector(looseMuons_passingPt_and_Eta, isHigherConePt);
    if ( isDEBUG ) {
      printCollection("tightMuons", tightMuons_passingPt_and_Eta);
    }

    const std::vector<RecoElectron> electrons = electronReader->read();
    const std::vector<const RecoElectron*> electron_ptrs = convert_to_ptrs(electrons);
    const std::vector<const RecoElectron*> cleanedElectrons = electronCleaner(electron_ptrs, tightMuons_passingPt_and_Eta);
    preselElectronSelector.getSelector().set_min_pt(10.);
    const std::vector<const RecoElectron*> looseElectrons_passingEta = preselElectronSelector(cleanedElectrons, isHigherConePt);
    preselElectronSelector.getSelector().set_min_pt(selElectron_min_pt);
    const std::vector<const RecoElectron*> looseElectrons_passingPt_and_Eta = preselElectronSelector(cleanedElectrons, isHigherConePt);
    const std::vector<const RecoElectron*> tightElectrons_passingPt_and_Eta = tightElectronSelector(looseElectrons_passingPt_and_Eta, isHigherConePt);
    if ( isDEBUG ) {
      printCollection("tightElectrons", tightElectrons_passingPt_and_Eta);
    }

    const std::vector<const RecoLepton*> looseLeptonsFull_passingEta = mergeLeptonCollections(looseElectrons_passingEta, looseMuons_passingEta, isHigherConePt);
    const std::vector<const RecoLepton*> looseLeptons_passingEta = pickFirstNobjects(looseLeptonsFull_passingEta, 1);
    const std::vector<const RecoLepton*> looseLeptonsFull_passingPt_and_Eta = mergeLeptonCollections(looseElectrons_passingPt_and_Eta, looseMuons_passingPt_and_Eta, isHigherConePt);
    const std::vector<const RecoLepton*> looseLeptons_passingPt_and_Eta = pickFirstNobjects(looseLeptonsFull_passingPt_and_Eta, 1);
    const std::vector<const RecoLepton*> tightLeptonsFull_passingPt_and_Eta = mergeLeptonCollections(tightElectrons_passingPt_and_Eta, tightMuons_passingPt_and_Eta, isHigherConePt);
    const std::vector<const RecoLepton*> tightLeptons_passingPt_and_Eta = pickFirstNobjects(tightLeptonsFull_passingPt_and_Eta, 1);

//--- build collections of jets and select subset of jets passing b-tagging criteria
    const std::vector<RecoJet> jets_ak4 = jetReaderAK4->read();
    const std::vector<const RecoJet*> jet_ptrs_ak4 = convert_to_ptrs(jets_ak4);
    //const std::vector<const RecoJet*> cleanedJetsAK4_wrtLeptons = jetCleaningByIndex ?
    //  jetCleanerAK4_byIndex(jet_ptrs_ak4, tightLeptons_passingPt_and_Eta) :
    //  jetCleanerAK4_dR04   (jet_ptrs_ak4, tightLeptons_passingPt_and_Eta)
    //;
    const std::vector<const RecoJet*> cleanedJetsAK4_wrtLeptons = jetCleanerAK4_dR04(jet_ptrs_ak4, tightLeptons_passingPt_and_Eta); 
    const std::vector<const RecoJet*> selJetsAK4 = jetSelectorAK4(cleanedJetsAK4_wrtLeptons, isHigherPt);
    const std::vector<const RecoJet*> selBJetsAK4_loose = jetSelectorAK4_bTagLoose(cleanedJetsAK4_wrtLeptons, isHigherPt);
    const std::vector<const RecoJet*> selBJetsAK4_medium = jetSelectorAK4_bTagMedium(cleanedJetsAK4_wrtLeptons, isHigherPt);
    std::vector<RecoJet> jets_ak4LS;
    std::vector<const RecoJet*> jet_ptrs_ak4LS;
    std::vector<const RecoJet*> selJetsAK4LS;
    if ( jetReaderAK4LS )
    {
      jets_ak4LS = jetReaderAK4LS->read();
      jet_ptrs_ak4LS = convert_to_ptrs(jets_ak4LS);
      selJetsAK4LS = jetSelectorAK4(jet_ptrs_ak4LS, isHigherPt);
    }

    bool passesEvtSel_rec         = true;
    bool passesEvtSel_gen         = true;
    bool passesEvtSel_rec_and_gen = true;

//--- require exactly one reconstructed lepton passing tight selection criteria
    passesEvtSel_rec         = passesEvtSel_rec         && looseLeptons_passingEta.size() >= 1;
    passesEvtSel_gen         = passesEvtSel_gen         && genLeptons_passingEta.size() >= 1;
    passesEvtSel_rec_and_gen = passesEvtSel_rec_and_gen && selectGenMatchedParticles(looseLeptons_passingEta, genLeptons_passingEta).size() >= 1;
    const std::string cutLooseLeptonEta = ">= 1 loose lepton";
    if ( passesEvtSel_rec         ) cutFlowTable.update(cutLooseLeptonEta,        "rec",     evtWeight);
    if ( passesEvtSel_gen         ) cutFlowTable.update(cutLooseLeptonEta,        "gen",     evtWeight);
    if ( passesEvtSel_rec_and_gen ) cutFlowTable.update(cutLooseLeptonEta,        "gen&rec", evtWeight);
        
    passesEvtSel_rec         = passesEvtSel_rec         && looseLeptons_passingPt_and_Eta.size() >= 1;
    passesEvtSel_gen         = passesEvtSel_gen         && genLeptons_passingPt_and_Eta.size() >= 1;
    passesEvtSel_rec_and_gen = passesEvtSel_rec_and_gen && selectGenMatchedParticles(looseLeptons_passingPt_and_Eta, genLeptons_passingPt_and_Eta).size() >= 1;
    const std::string cutLooseLeptonPt_and_Eta = Form("loose electron (muon) pT > %2.0f (%2.0f) GeV", selElectron_min_pt, selMuon_min_pt);
    if ( passesEvtSel_rec         ) cutFlowTable.update(cutLooseLeptonPt_and_Eta, "rec",     evtWeight);
    if ( passesEvtSel_gen         ) cutFlowTable.update(cutLooseLeptonPt_and_Eta, "gen",     evtWeight);
    if ( passesEvtSel_rec_and_gen ) cutFlowTable.update(cutLooseLeptonPt_and_Eta, "gen&rec", evtWeight);

    passesEvtSel_rec         = passesEvtSel_rec         && tightLeptons_passingPt_and_Eta.size() >= 1;
    passesEvtSel_gen         = passesEvtSel_gen         && true;
    passesEvtSel_rec_and_gen = passesEvtSel_rec_and_gen && selectGenMatchedParticles(tightLeptons_passingPt_and_Eta, genLeptons_passingPt_and_Eta).size() >= 1;
    const std::string cutTightLeptonPt_and_Eta = ">= 1 tight lepton";
    if ( passesEvtSel_rec         ) cutFlowTable.update(cutTightLeptonPt_and_Eta, "rec",     evtWeight);
    if ( passesEvtSel_gen         ) cutFlowTable.update(cutTightLeptonPt_and_Eta, "gen",     evtWeight);
    if ( passesEvtSel_rec_and_gen ) cutFlowTable.update(cutTightLeptonPt_and_Eta, "gen&rec", evtWeight);

    const RecoLepton* tightLepton = nullptr;
    if ( tightLeptons_passingPt_and_Eta.size() >= 1 ) 
    {
      tightLepton = tightLeptons_passingPt_and_Eta[0];
    }

    const std::vector<RecoJetAK8> jets_ak8 = jetReaderAK8->read();
    const std::vector<const RecoJetAK8*> jet_ptrs_ak8 = convert_to_ptrs(jets_ak8);
    const std::vector<RecoJetAK8> jets_ak8LS = jetReaderAK8LS->read();
    const std::vector<const RecoJetAK8*> jet_ptrs_ak8LS = convert_to_ptrs(jets_ak8LS);

//--- select jets from H->bb decay
    const std::vector<const RecoJetAK8*> cleanedJetsAK8_wrtLeptons = jetCleanerAK8_dR08(jet_ptrs_ak8, tightLeptons_passingPt_and_Eta);
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
    std::vector<const RecoJetBase*> selJets_Hbb;
    if ( selJet1_Hbb && selJet2_Hbb )
    {  
      selJets_Hbb = { selJet1_Hbb, selJet2_Hbb };
      std::sort(selJets_Hbb.begin(), selJets_Hbb.end(), isHigherPt);
    }

    passesEvtSel_rec         = passesEvtSel_rec         && selJets_Hbb.size() >= 2;
    passesEvtSel_gen         = passesEvtSel_gen         && genBJets_passingPt.size() >= 2;
    passesEvtSel_rec_and_gen = passesEvtSel_rec_and_gen && selectGenMatchedParticles(selJets_Hbb, genBJets_passingPt).size() >= 2;
    const std::string cutBJetPt = ">= 2 jets from H->bb decay, passing pT > 25 GeV";
    if ( passesEvtSel_rec         ) cutFlowTable.update(cutBJetPt,         "rec",     evtWeight);
    if ( passesEvtSel_gen         ) cutFlowTable.update(cutBJetPt,         "gen",     evtWeight);
    if ( passesEvtSel_rec_and_gen ) cutFlowTable.update(cutBJetPt,         "gen&rec", evtWeight);

    passesEvtSel_rec         = passesEvtSel_rec         && selJets_Hbb.size() >= 2;
    passesEvtSel_gen         = passesEvtSel_gen         && genBJets_passingPt_and_Eta.size() >= 2;
    passesEvtSel_rec_and_gen = passesEvtSel_rec_and_gen && selectGenMatchedParticles(selJets_Hbb, genBJets_passingPt_and_Eta).size() >= 2;
    const std::string cutBJetPt_and_Eta = ">= 2 jets from H->bb decay, passing pT > 25 GeV & abs(eta) < 2.4";
    if ( passesEvtSel_rec         ) cutFlowTable.update(cutBJetPt_and_Eta, "rec",     evtWeight);
    if ( passesEvtSel_gen         ) cutFlowTable.update(cutBJetPt_and_Eta, "gen",     evtWeight);
    if ( passesEvtSel_rec_and_gen ) cutFlowTable.update(cutBJetPt_and_Eta, "gen&rec", evtWeight);

    passesEvtSel_rec         = passesEvtSel_rec         && true;
    passesEvtSel_gen         = passesEvtSel_gen         && cleanedGenBJets_wrtLeptons.size() >= 2;
    passesEvtSel_rec_and_gen = passesEvtSel_rec_and_gen && selectGenMatchedParticles(selJets_Hbb, cleanedGenBJets_wrtLeptons).size() >= 2;
    const std::string cutBJetCleaning_wrtLeptons = ">= 2 jets from H->bb decay, passing cleaning wrt leptons";
    if ( passesEvtSel_rec         ) cutFlowTable.update(cutBJetCleaning_wrtLeptons, "rec",     evtWeight);
    if ( passesEvtSel_gen         ) cutFlowTable.update(cutBJetCleaning_wrtLeptons, "gen",     evtWeight);
    if ( passesEvtSel_rec_and_gen ) cutFlowTable.update(cutBJetCleaning_wrtLeptons, "gen&rec", evtWeight);

    int numBJets_loose  = 0;
    int numBJets_medium = 0;
    if ( selJetT_Hbb ) 
    {
      countBJetsJets_Hbb(*selJetT_Hbb, jetSelectorAK8_Hbb, jetSelectorAK4_bTagLoose, jetSelectorAK4_bTagMedium, numBJets_loose, numBJets_medium);
    }

    passesEvtSel_rec         = passesEvtSel_rec         && numBJets_medium >= 1;
    passesEvtSel_gen         = passesEvtSel_gen         && true;
    passesEvtSel_rec_and_gen = passesEvtSel_rec_and_gen && numBJets_medium >= 1;
    const std::string cutBJetCSV = ">= 1 medium b-jet";
    if ( passesEvtSel_rec         ) cutFlowTable.update(cutBJetCSV,        "rec",     evtWeight);
    if ( passesEvtSel_gen         ) cutFlowTable.update(cutBJetCSV,        "gen",     evtWeight);
    if ( passesEvtSel_rec_and_gen ) cutFlowTable.update(cutBJetCSV,        "gen&rec", evtWeight);

//--- select jets from W->jj decay
    std::vector<const RecoJet*> selJetsAK4_or_AK4LS_Wjj;
    if ( jetReaderAK4LS )
    {
      selJetsAK4_or_AK4LS_Wjj = selJetsAK4LS;
    }
    else
    {
      selJetsAK4_or_AK4LS_Wjj = cleanedJetsAK4_wrtLeptons;
    }
    std::vector<selJetsType_Wjj> selJetsT_Wjj;
    if ( selJetT_Hbb )
    {
      selJetsT_Wjj = selectJets_Wjj(
        jet_ptrs_ak8LS, jetCleanerAK8_dR12, jetCleanerAK8_dR16, jetSelectorAK8LS_Wjj,
        selJetsAK4_or_AK4LS_Wjj, jetCleanerAK4_dR08, jetCleanerAK4_dR12, jetSelectorAK4_Wjj,
        *selJetT_Hbb, 
        tightLepton, selBJetsAK4_medium, mva_Wjj, eventInfo,
        &genWJets_ptrs);
    }
    const selJetsType_Wjj* selJetT_Wjj = nullptr;
    const RecoJetAK8* selJetAK8_Wjj = nullptr;
    const RecoJetBase* selJet1_Wjj = nullptr;
    const RecoJetBase* selJet2_Wjj = nullptr;
    if ( selJetsT_Wjj.size() >= 1 ) 
    {
      selJetT_Wjj = &selJetsT_Wjj[0];
      selJetAK8_Wjj = selJetT_Wjj->fatjet_;
      selJet1_Wjj = selJetT_Wjj->jet_or_subjet1_;
      selJet2_Wjj = selJetT_Wjj->jet_or_subjet2_;
    }
    std::vector<const RecoJetBase*> selJets_Wjj;
    if ( selJet1_Wjj ) selJets_Wjj.push_back(selJet1_Wjj);
    if ( selJet2_Wjj ) selJets_Wjj.push_back(selJet2_Wjj);
    std::sort(selJets_Wjj.begin(), selJets_Wjj.end(), isHigherPt);

    passesEvtSel_rec         = passesEvtSel_rec         && selJets_Wjj.size() >= 2;
    passesEvtSel_gen         = passesEvtSel_gen         && genWJets_passingPt.size() >= 2;
    passesEvtSel_rec_and_gen = passesEvtSel_rec_and_gen && selectGenMatchedParticles(selJets_Wjj, genWJets_passingPt).size() >= 2;
    const std::string cutWJetPt = ">= 2 jets from W->jj decay, passing pT > 25 GeV";
    if ( passesEvtSel_rec         ) cutFlowTable.update(cutWJetPt,         "rec",     evtWeight);
    if ( passesEvtSel_gen         ) cutFlowTable.update(cutWJetPt,         "gen",     evtWeight);
    if ( passesEvtSel_rec_and_gen ) cutFlowTable.update(cutWJetPt,         "gen&rec", evtWeight);

    passesEvtSel_rec         = passesEvtSel_rec         && selJets_Wjj.size() >= 2;
    passesEvtSel_gen         = passesEvtSel_gen         && genWJets_passingPt_and_Eta.size() >= 2;
    passesEvtSel_rec_and_gen = passesEvtSel_rec_and_gen && selectGenMatchedParticles(selJets_Wjj, genWJets_passingPt_and_Eta).size() >= 2;
    const std::string cutWJetPt_and_Eta = Form(">= 2 jets from W->jj decay, passing pT > 25 GeV & abs(eta) < %1.1f", selJetAK4_max_absEta_Wjj);
    if ( passesEvtSel_rec         ) cutFlowTable.update(cutWJetPt_and_Eta, "rec",     evtWeight);
    if ( passesEvtSel_gen         ) cutFlowTable.update(cutWJetPt_and_Eta, "gen",     evtWeight);
    if ( passesEvtSel_rec_and_gen ) cutFlowTable.update(cutWJetPt_and_Eta, "gen&rec", evtWeight);

    passesEvtSel_rec         = passesEvtSel_rec         && true;
    passesEvtSel_gen         = passesEvtSel_gen         && cleanedGenWJets_wrtLeptons.size() >= 2;
    passesEvtSel_rec_and_gen = passesEvtSel_rec_and_gen && selectGenMatchedParticles(selJets_Wjj, cleanedGenWJets_wrtLeptons).size() >= 2;
    const std::string cutWJetCleaning_wrtLeptons = ">= 2 jets from W->jj decay, passing cleaning wrt leptons";
    if ( passesEvtSel_rec         ) cutFlowTable.update(cutWJetCleaning_wrtLeptons, "rec",     evtWeight);
    if ( passesEvtSel_gen         ) cutFlowTable.update(cutWJetCleaning_wrtLeptons, "gen",     evtWeight);
    if ( passesEvtSel_rec_and_gen ) cutFlowTable.update(cutWJetCleaning_wrtLeptons, "gen&rec", evtWeight);

    passesEvtSel_rec         = passesEvtSel_rec         && true;
    passesEvtSel_gen         = passesEvtSel_gen         && cleanedGenWJets_wrtHbb.size() >= 2;
    passesEvtSel_rec_and_gen = passesEvtSel_rec_and_gen && selectGenMatchedParticles(selJets_Wjj, cleanedGenWJets_wrtHbb).size() >= 2;
    const std::string cutWJetCleaning_wrtHbb = ">= 2 jets from W->jj decay, passing cleaning wrt jets from H->bb decay";
    if ( passesEvtSel_rec         ) cutFlowTable.update(cutWJetCleaning_wrtHbb, "rec",     evtWeight);
    if ( passesEvtSel_gen         ) cutFlowTable.update(cutWJetCleaning_wrtHbb, "gen",     evtWeight);
    if ( passesEvtSel_rec_and_gen ) cutFlowTable.update(cutWJetCleaning_wrtHbb, "gen&rec", evtWeight);

    bool passesBoosted_recHbb          = selJetAK8_Hbb;
    bool passesBoosted_genHbb          = isBoosted_genHbb(genBJets_ptrs);
    bool passesBoosted_rec_and_genHbb  = passesBoosted_recHbb && passesBoosted_genHbb;
    bool passesBoosted_recWjj          = selJetAK8_Wjj;
    bool passesBoosted_genWjj          = isBoosted_genWjj(genWJets_ptrs, genLeptons_passingPt_and_Eta);
    bool passesBoosted_rec_and_genWjj  = passesBoosted_recWjj && passesBoosted_genWjj;
    if ( passesEvtSel_rec         ) updateCutFlowTable(cutFlowTable, "rec",     passesBoosted_recHbb,         passesBoosted_recWjj,         evtWeight);
    if ( passesEvtSel_gen         ) updateCutFlowTable(cutFlowTable, "gen",     passesBoosted_genHbb,         passesBoosted_genWjj,         evtWeight);
    if ( passesEvtSel_rec_and_gen ) updateCutFlowTable(cutFlowTable, "gen&rec", passesBoosted_rec_and_genHbb, passesBoosted_rec_and_genWjj, evtWeight);

//--- compute MHT and linear MET discriminant (met_LD)
    RecoMEt met = metReader->read();
    const Particle::LorentzVector& metP4 = met.p4();
    //const std::vector<const RecoJet*> selJetsAK4_mht = jetSelectorAK4(cleanedJetsAK4_wrtLeptons, isHigherPt);
    //Particle::LorentzVector mhtP4 = compMHT(tightLeptons, {}, selJetsAK4_mht);
    //double met_LD = compMEt_LD(metP4, mhtP4);

//--- apply final selection
    bool isSelected = false;
    if ( tightLepton ) {
      if ( (tightLepton->is_electron() && tightLepton->cone_pt() > selElectron_min_pt) || 
           (tightLepton->is_muon()     && tightLepton->cone_pt() > selMuon_min_pt    ) ) {
        if ( selJet1_Hbb && selJet2_Hbb   &&
             numBJets_medium >= 1         &&
             (selJet1_Wjj || selJet2_Wjj) ) {
          isSelected = true;
        }
      }
    }
    if ( !isSelected )
    {
      continue;
    }

//--- fill two-dimensional correlation plot between generator-level and reconstruction-level jets from W->jj vs H->bb decay
    const std::vector<const RecoJetBase*> selJets_Hbb_genMatched = selectGenMatchedParticles(selJets_Hbb, genBJets_ptrs);
    int numSel_Hbb = selJets_Hbb_genMatched.size();
    int numRec_Hbb = TMath::Max(numSel_Hbb, (int)selectGenMatchedParticles(jet_ptrs_ak4, genBJets_ptrs).size());
    int idxHbb = -1;
    if      ( numRec_Hbb >= 2 && numSel_Hbb >= 2 ) idxHbb = k2Rec2Sel;
    else if ( numRec_Hbb >= 2 && numSel_Hbb >= 1 ) idxHbb = k2Rec1Sel;
    else if ( numRec_Hbb >= 2                    ) idxHbb = k2Rec0Sel;
    else if ( numRec_Hbb >= 1 && numSel_Hbb >= 1 ) idxHbb = k1Rec1Sel;
    else if ( numRec_Hbb >= 1                    ) idxHbb = k1Rec0Sel;
    else                                           idxHbb = k0Rec;

    const std::vector<const RecoJetBase*> selJets_Wjj_genMatched = selectGenMatchedParticles(selJets_Wjj, genWJets_ptrs);
    int numSel_Wjj = selJets_Wjj_genMatched.size();
    int numRec_Wjj = TMath::Max(numSel_Wjj, (int)selectGenMatchedParticles(jet_ptrs_ak4, genWJets_ptrs).size());
    int idxWjj = -1;
    if      ( numRec_Wjj >= 2 && numSel_Wjj >= 2 ) idxWjj = k2Rec2Sel;
    else if ( numRec_Wjj >= 2 && numSel_Wjj >= 1 ) idxWjj = k2Rec1Sel;
    else if ( numRec_Wjj >= 2                    ) idxWjj = k2Rec0Sel;
    else if ( numRec_Wjj >= 1 && numSel_Wjj >= 1 ) idxWjj = k1Rec1Sel;
    else if ( numRec_Wjj >= 1                    ) idxWjj = k1Rec0Sel;
    else                                           idxWjj = k0Rec;

    histogram_selJetCorrelation->Fill(idxHbb, idxWjj, evtWeight);

    fillHistograms_numGenWJets(
      jet_ptrs_ak4, cleanedJetsAK4_wrtLeptons, jetCleanerAK4_dR04, jetSelectorAK4_Wjj, selJet1_Hbb, selJet2_Hbb,  
      tightLepton, selBJetsAK4_medium.size(), mva_Wjj, eventInfo, 
      genWJets_ptrs, genBJets_passingPt_and_Eta,
      histogram_numGenWJets_ak4, 
      histogram_numGenWJets_ak4cleanedWrtLeptons, 
      histogram_numGenWJets_ak4cleanedWrtGenHbb, 
      histogram_numGenWJets_ak4cleanedWrtHbb, 
      histogram_numGenWJets_ak4selected, 
      histogram_numGenWJets_ak4byWjjPairs, evtWeight);

    for ( const RecoJetBase* recJet_base : selJets_Wjj_genMatched )
    {  
      if ( dynamic_cast<const RecoJet*>(recJet_base) ) // CV: jet charge is only available for AK4 jets, not for subjets !!
      {
        const RecoJet* recJet = dynamic_cast<const RecoJet*>(recJet_base);
        double recJet_charge = recJet->charge();
        for ( const GenJet* genJet : genWJets_passingPt_and_Eta )
        {
          double dR = deltaR(recJet->p4(), genJet->p4());
          if ( dR < 0.1 ) 
          {
            int genJet_pdgId = genJet->pdgId();
            double genJet_charge = 0.;
            if      ( genJet_pdgId == +2 || genJet_pdgId == +4 ||genJet_pdgId == +6 ) genJet_charge = +0.666; // up, charm, top quark
            else if ( genJet_pdgId == -1 || genJet_pdgId == -3 ||genJet_pdgId == -5 ) genJet_charge = +0.333; // anti-down, anti-strange, anti-bottom quark
            else if ( genJet_pdgId == +1 || genJet_pdgId == +3 ||genJet_pdgId == +5 ) genJet_charge = -0.333; // down, strange, bottom quark
            else if ( genJet_pdgId == -2 || genJet_pdgId == -4 ||genJet_pdgId == -6 ) genJet_charge = -0.666; // anti-up, anti-charm, anti-top quark
            double genTimesRecJetCharge = recJet_charge*genJet_charge;
            TH1* histogram = nullptr;
            if ( TMath::Abs(genJet_charge) > 0.5 ) histogram = histogram_ak4_genTimesRecJetCharge_upTypeQuarks;
            else                                   histogram = histogram_ak4_genTimesRecJetCharge_downTypeQuarks;
            fillWithOverFlow(histogram, genTimesRecJetCharge, evtWeight);
          }
        }
      }
    }

    for ( const RecoJetAK8* fatjet : jet_ptrs_ak8LS )
    {
      if ( fatjet->subJet1() && fatjet->subJet1()->pt() > 20. && fatjet->subJet1()->absEta() < 2.4 &&
           isGenMatchedT<GenJet>(fatjet->subJet1()->eta(), fatjet->subJet1()->phi(), genWJets_ptrs, nullptr, 0.1) &&
           fatjet->subJet2() && fatjet->subJet2()->pt() > 20. && fatjet->subJet2()->absEta() < 2.4 &&
           isGenMatchedT<GenJet>(fatjet->subJet1()->eta(), fatjet->subJet1()->phi(), genWJets_ptrs, nullptr, 0.1) ) {
        fillWithOverFlow(histogram_ak8_ptWjj_fullyMatched, fatjet->pt(), evtWeight);
        fillWithOverFlow(histogram_ak8_ptH_fullyMatched, (fatjet->p4() + tightLepton->p4() + metP4).pt(), evtWeight);
      }
    }

//--- fill histograms with events passing final selection
    if ( selJetAK8_Hbb )
    {
      fillHistograms_jets(
        selJets_Hbb,
	genBJets_ptrs, 
	*histograms_boostedHbb_bjet1, histogram_boostedHbb_bjet1_idx,
	*histograms_boostedHbb_bjet2, histogram_boostedHbb_bjet2_idx,
	histogram_boostedHbb_bjet_numIndices, histogram_boostedHbb_bjet_mjj, evtWeight);
    }
    else 
    {
      fillHistograms_jets(
        selJetsAK4_Hbb,
	genBJets_ptrs,
	*histograms_resolvedHbb_bjet1, histogram_resolvedHbb_bjet1_idx,
	*histograms_resolvedHbb_bjet2, histogram_resolvedHbb_bjet2_idx,
	histogram_resolvedHbb_bjet_numIndices, histogram_resolvedHbb_bjet_mjj, evtWeight);
    }
    const std::vector<const RecoJet*> cleanedJetsAK4_wrtHbb = jetCleanerAK4_dR04(cleanedJetsAK4_wrtLeptons, std::vector<const RecoJetBase*>({ selJet1_Hbb, selJet2_Hbb }));
    const std::vector<const RecoJet*> selJetsAK4_Wjj = jetSelectorAK4_Wjj(cleanedJetsAK4_wrtHbb, isHigherPt);
    std::vector<JetPair_Wjj> jetPairs_Wjj = makeJetPairs_Wjj(selJetsAK4_Wjj, &genWJets_ptrs);
    rankJetPairs_Wjj(jetPairs_Wjj, selJetsAK4_Wjj, *tightLepton, numBJets_medium, mva_Wjj, eventInfo);
    fillHistograms_jets(
      selJetsAK4_Wjj,
      genWJets_ptrs, 
      *histograms_Wjj_jet1, histogram_Wjj_jet1_idx,
      *histograms_Wjj_jet2, histogram_Wjj_jet2_idx,
      histogram_Wjj_jet_numIndices, histogram_Wjj_jet_mjj, evtWeight);
 
    std::sort(jetPairs_Wjj.begin(), jetPairs_Wjj.end(), isHigherRankedByMass);
    int hadWJetPair_sortedByMass_idx = getIndex_isGenMatched(jetPairs_Wjj);
    fillWithOverFlow(histogram_hadWJetPair_sortedByMass_idx, hadWJetPair_sortedByMass_idx, evtWeight); 
    std::sort(jetPairs_Wjj.begin(), jetPairs_Wjj.end(), isHigherRankedByDeltaR);
    int hadWJetPair_sortedByDeltaR_idx = getIndex_isGenMatched(jetPairs_Wjj);
    fillWithOverFlow(histogram_hadWJetPair_sortedByDeltaR_idx, hadWJetPair_sortedByDeltaR_idx, evtWeight); 
    std::sort(jetPairs_Wjj.begin(), jetPairs_Wjj.end(), isHigherRankedByPt);
    int hadWJetPair_sortedByPt_idx = getIndex_isGenMatched(jetPairs_Wjj);
    fillWithOverFlow(histogram_hadWJetPair_sortedByPt_idx, hadWJetPair_sortedByPt_idx, evtWeight); 
    std::sort(jetPairs_Wjj.begin(), jetPairs_Wjj.end(), isHigherRankedByScalarPt);
    int hadWJetPair_sortedByScalarPt_idx = getIndex_isGenMatched(jetPairs_Wjj);
    fillWithOverFlow(histogram_hadWJetPair_sortedByScalarPt_idx, hadWJetPair_sortedByScalarPt_idx, evtWeight); 
    std::sort(jetPairs_Wjj.begin(), jetPairs_Wjj.end(), isHigherRankedByBDT);
    int hadWJetPair_sortedByBDT_idx = getIndex_isGenMatched(jetPairs_Wjj);
    fillWithOverFlow(histogram_hadWJetPair_sortedByBDT_idx, hadWJetPair_sortedByBDT_idx, evtWeight); 
    fillWithOverFlow(histogram_hadWJetPair_numIndices, jetPairs_Wjj.size(), evtWeight); 

    if ( memReader ) 
    {
      std::vector<MEMOutput_hh_bb1l> memOutputs_hh_bb1l = memReader->read();
      for ( std::vector<MEMOutput_hh_bb1l>::const_iterator memOutput = memOutputs_hh_bb1l.begin();
  	    memOutput != memOutputs_hh_bb1l.end(); ++memOutput ) {
        fillHistograms_mem(
          *memOutput, 
  	  genLeptons_ptrs, genBJets_ptrs, genWJets_ptrs, 
	  *histograms_memOutput_fullyMatched, 
	  *histograms_memOutput_unmatchedLepton, 
	  *histograms_memOutput_unmatchedBJet, 
	  *histograms_memOutput_unmatchedWJet, evtWeight);
      }
    }
    if ( memReader_missingBJet )
    {
      std::vector<MEMOutput_hh_bb1l> memOutputs_hh_bb1l_missingBJet = memReader_missingBJet->read();
      for ( std::vector<MEMOutput_hh_bb1l>::const_iterator memOutput = memOutputs_hh_bb1l_missingBJet.begin();
  	    memOutput != memOutputs_hh_bb1l_missingBJet.end(); ++memOutput ) {
        fillHistograms_mem(
          *memOutput, 
	  genLeptons_ptrs, genBJets_ptrs, genWJets_ptrs, 
	  *histograms_memOutput_missingBJet_fullyMatched, 
	  *histograms_memOutput_missingBJet_unmatchedLepton, 
	  *histograms_memOutput_missingBJet_unmatchedBJet, 
	  *histograms_memOutput_missingBJet_unmatchedWJet, evtWeight);
      }
    }
    if ( memReader_missingHadWJet )
    {
      std::vector<MEMOutput_hh_bb1l> memOutputs_hh_bb1l_missingHadWJet = memReader_missingHadWJet->read();
      for ( std::vector<MEMOutput_hh_bb1l>::const_iterator memOutput = memOutputs_hh_bb1l_missingHadWJet.begin();
	    memOutput != memOutputs_hh_bb1l_missingHadWJet.end(); ++memOutput ) {
        fillHistograms_mem(
          *memOutput, 
	  genLeptons_ptrs, genBJets_ptrs, genWJets_ptrs, 
	  *histograms_memOutput_missingHadWJet_fullyMatched, 
	  *histograms_memOutput_missingHadWJet_unmatchedLepton, 
	  *histograms_memOutput_missingHadWJet_unmatchedBJet, 
	  *histograms_memOutput_missingHadWJet_unmatchedWJet, evtWeight);
      }
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

//--- memory clean-up
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
  delete lheInfoReader;

  delete inputTree;

  clock.Show("analyzeMEM_hh_bb1l");

  return EXIT_SUCCESS;
}
