#include "FWCore/ParameterSet/interface/ParameterSet.h" // edm::ParameterSet
#include "FWCore/PythonParameterSet/interface/MakeParameterSets.h" // edm::readPSetsFrom()
#include "FWCore/Utilities/interface/Exception.h" // cms::Exception
#include "PhysicsTools/FWLite/interface/TFileService.h" // fwlite::TFileService
#include "DataFormats/FWLite/interface/InputSource.h" // fwlite::InputSource
#include "DataFormats/FWLite/interface/OutputFiles.h" // fwlite::OutputFiles
#include "DataFormats/Math/interface/LorentzVector.h" // math::PtEtaPhiMLorentzVector, math::XYZTLorentzVectorD
#include "DataFormats/Math/interface/deltaR.h" // deltaR
#include "DataFormats/Math/interface/deltaPhi.h" // deltaPhi

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
#include "tthAnalysis/HiggsToTauTau/interface/mvaInputVariables.h" // deltaPhi_rf
#include "tthAnalysis/HiggsToTauTau/interface/generalAuxFunctions.h" // format_vstring
#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow
#include "tthAnalysis/HiggsToTauTau/interface/cutFlowTable.h" // cutFlowTableType
#include "tthAnalysis/HiggsToTauTau/interface/TTreeWrapper.h" // TTreeWrapper
#include "tthAnalysis/HiggsToTauTau/interface/EvtWeightManager.h" // EvtWeightManager
#include "tthAnalysis/HiggsToTauTau/interface/GenLeptonCollectionSelector.h" // GenLeptonCollectionSelector
#include "tthAnalysis/HiggsToTauTau/interface/GenJetCollectionSelector.h" // GenJetCollectionSelector

#include "hhAnalysis/multilepton/interface/EvtWeightRecorderHH.h" // EvtWeightRecorderHH

#include "hhAnalysis/bbww/interface/RecoJetCollectionSelectorAK8_hh_bbWW_Hbb.h" // RecoJetSelectorAK8_hh_bbWW_Hbb
#include "hhAnalysis/bbww/interface/MEMOutput_hh_bb2l.h" // MEMOutput_hh_bb2l
#include "hhAnalysis/bbww/interface/MEMOutputReader_hh_bb2l.h" // MEMOutputReader_hh_bb2l
#include "hhAnalysis/bbww/interface/jetSelectionAuxFunctions.h" // selectJets_Hbb, countBJetsJets_Hbb
#include "hhAnalysis/bbww/interface/genMatchingAuxFunctions.h" // isGenMatched, countGenMatchedParticles
#include "hhAnalysis/bbww/interface/GenParticleMatcherFromHiggs.h" // GenParticleMatcherFromHiggs
#include "hhAnalysis/bbww/interface/GenParticleMatcherFromTop.h" // GenParticleMatcherFromTop
#include "hhAnalysis/bbww/interface/analyzeMEM_genJetHistograms.h" // genJetHistograms, fillHistograms_genJets
#include "hhAnalysis/bbww/interface/analyzeMEM_jetHistograms.h" // jetHistograms, fillHistograms_jets
#include "hhAnalysis/bbww/interface/analyzeMEM_memHistograms.h" // memHistograms, fillHistograms_mem
#include "hhAnalysis/bbww/interface/dumpGenParticles.h" // dumpGenParticles, dumpGenLeptons, dumpGenJets
#include "hhAnalysis/bbww/interface/genBoostedAuxFunctions.h" // isBoosted_genHb
#include "hhAnalysis/bbww/interface/BM_list.h" // BMS



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

void updateCutFlowTable(cutFlowTableType& cutFlowTable, const std::string& column, bool passesBoosted_Hbb, double evtWeight)
{
  if   ( passesBoosted_Hbb ) cutFlowTable.update("boosted",  column, evtWeight);
  else                       cutFlowTable.update("resolved", column, evtWeight);
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

  std::cout << "<analyzeMEM_hh_bb2l>:" << std::endl;

//--- keep track of time it takes the macro to execute
  TBenchmark clock;
  clock.Start("analyzeMEM_hh_bb2l");

//--- read python configuration parameters
  if ( !edm::readPSetsFrom(argv[1])->existsAs<edm::ParameterSet>("process") )
    throw cms::Exception("analyzeMEM_hh_bb2l")
      << "No ParameterSet 'process' found in configuration file = " << argv[1] << " !!\n";

  edm::ParameterSet cfg = edm::readPSetsFrom(argv[1])->getParameter<edm::ParameterSet>("process");

  edm::ParameterSet cfg_analyze = cfg.getParameter<edm::ParameterSet>("analyzeMEM_hh_bb2l");

  std::string treeName = cfg_analyze.getParameter<std::string>("treeName");

  std::string process_string = cfg_analyze.getParameter<std::string>("process");

  std::string histogramDir = cfg_analyze.getParameter<std::string>("histogramDir");

  std::string era_string = cfg_analyze.getParameter<std::string>("era");
  const int era = get_era(era_string);

  bool isMC = true;
  bool isMC_HH = isMC && process_string.find("hh_bbvv")!= std::string::npos;
  bool isMC_TT = isMC && process_string.find("TT")     != std::string::npos;
  bool isSignal = boost::starts_with(process_string, "signal_") && process_string.find("_hh_") != std::string::npos;
  bool isMC_HH_nonres = boost::starts_with(process_string, "signal_ggf_nonresonant_");
  bool hasLHE = cfg_analyze.getParameter<bool>("hasLHE");
  std::string central_or_shift = "central";
  bool apply_genWeight = cfg_analyze.getParameter<bool>("apply_genWeight");

  bool isDEBUG = cfg_analyze.getParameter<bool>("isDEBUG");
  if ( isDEBUG ) std::cout << "Warning: DEBUG mode enabled -> trigger selection will not be applied for data !!" << std::endl;

  std::string branchName_electrons = cfg_analyze.getParameter<std::string>("branchName_electrons");
  std::string branchName_muons = cfg_analyze.getParameter<std::string>("branchName_muons");
  std::string branchName_jets_ak4 = cfg_analyze.getParameter<std::string>("branchName_jets_ak4");
  std::string branchName_jets_ak8 = cfg_analyze.getParameter<std::string>("branchName_jets_ak8");
  std::string branchName_subjets_ak8 = cfg_analyze.getParameter<std::string>("branchName_subjets_ak8");
  std::string branchName_met = cfg_analyze.getParameter<std::string>("branchName_met");

  std::string branchName_memOutput = cfg_analyze.getParameter<std::string>("branchName_memOutput");
  std::string branchName_memOutput_missingBJet = cfg_analyze.getParameter<std::string>("branchName_memOutput_missingBJet");

  edm::ParameterSet cfg_branchNames_genParticles = cfg_analyze.getParameter<edm::ParameterSet>("branchNames_genParticles");
  // branches specific to HH->bbWW signal events
  std::string branchName_genLeptons = cfg_branchNames_genParticles.getParameter<std::string>("branchName_genLeptons");
  std::string branchName_genNeutrinos = cfg_branchNames_genParticles.getParameter<std::string>("branchName_genNeutrinos");
  std::string branchName_genParticlesFromHiggs = cfg_branchNames_genParticles.getParameter<std::string>("branchName_genParticlesFromHiggs");
  // branches specific to tt+jets background events
  std::string branchName_genLeptonsFromTop = cfg_branchNames_genParticles.getParameter<std::string>("branchName_genLeptonsFromTop");
  std::string branchName_genNeutrinosFromTop = cfg_branchNames_genParticles.getParameter<std::string>("branchName_genNeutrinosFromTop");
  std::string branchName_genBJetsFromTop = cfg_branchNames_genParticles.getParameter<std::string>("branchName_genBJetsFromTop");

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

  const double selElectron_lead_min_pt = 25.;
  const double selElectron_sublead_min_pt = 15.;
  const double selElectron_max_absEta = 2.5;
  const double selMuon_lead_min_pt = 25.;
  const double selMuon_sublead_min_pt = 15.;
  const double selMuon_max_absEta = 2.4;

  RecoJetReader* jetReaderAK4 = new RecoJetReader(era, isMC, branchName_jets_ak4, false);
  inputTree->registerReader(jetReaderAK4);
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

  RecoJetReaderAK8* jetReaderAK8 = new RecoJetReaderAK8(era, isMC, branchName_jets_ak8, branchName_subjets_ak8);
  inputTree->registerReader(jetReaderAK8);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR08(0.8, isDEBUG);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR12(1.2, isDEBUG);
  RecoJetCollectionSelectorAK8_hh_bbWW_Hbb jetSelectorAK8_Hbb(era, -1, isDEBUG);

  MEMOutputReader_hh_bb2l* memReader = nullptr;
  const std::string BM = "SM"; // BMS
  if ( !branchName_memOutput.empty() )
  {
    std::string namebranchN;
    std::string namebranch;
    if ( BM == "SM")
    {
      namebranch = branchName_memOutput.data();
      namebranchN = Form("n%s", branchName_memOutput.data());
    }
    else {
      namebranch = Form("%s_%s", branchName_memOutput.data(), BM.c_str());
      namebranchN = Form("n%s_%s", branchName_memOutput.data(), BM.c_str());
    }
    memReader = new MEMOutputReader_hh_bb2l(namebranchN , branchName_memOutput);
    inputTree->registerReader(memReader);
  }
  MEMOutputReader_hh_bb2l* memReader_missingBJet = nullptr;
  if ( !branchName_memOutput_missingBJet.empty() )
  {
    std::string namebranchN_missingBJet;
    std::string namebranch_missingBJet;
    if ( BM == "SM")
    {
      namebranch_missingBJet = branchName_memOutput.data();
      namebranchN_missingBJet = Form("n%s", branchName_memOutput.data());
    }
    else {
      namebranch_missingBJet = Form("%s_%s", branchName_memOutput.data(), BM.c_str());
      namebranchN_missingBJet = Form("n%s_%s", branchName_memOutput.data(), BM.c_str());
    }
    memReader_missingBJet = new MEMOutputReader_hh_bb2l(namebranchN_missingBJet , branchName_memOutput_missingBJet);
    inputTree->registerReader(memReader_missingBJet);
  }

//--- declare genParticle readers
  GenLeptonReader *   genLeptonReader            = nullptr;
  GenParticleReader * genNeutrinoReader          = nullptr;
  GenParticleReader * genParticleFromHiggsReader = nullptr;
  GenLeptonReader *   genLeptonFromTopReader     = nullptr;
  GenParticleReader * genNeutrinoFromTopReader   = nullptr;
  GenParticleReader * genBJetFromTopReader       = nullptr;
  if ( isMC_HH )
  {
    genLeptonReader = new GenLeptonReader(branchName_genLeptons);
    inputTree->registerReader(genLeptonReader);
    genNeutrinoReader = new GenParticleReader(branchName_genNeutrinos);
    inputTree->registerReader(genNeutrinoReader);
    genParticleFromHiggsReader = new GenParticleReader(branchName_genParticlesFromHiggs);
    inputTree->registerReader(genParticleFromHiggsReader);
  }
  else if ( isMC_TT )
  {
    genLeptonFromTopReader = new GenLeptonReader(branchName_genLeptonsFromTop);
    inputTree->registerReader(genLeptonFromTopReader);
    genNeutrinoFromTopReader = new GenParticleReader(branchName_genNeutrinosFromTop);
    inputTree->registerReader(genNeutrinoFromTopReader);
    genBJetFromTopReader = new GenParticleReader(branchName_genBJetsFromTop);
    inputTree->registerReader(genBJetFromTopReader);
  }

  GenLeptonCollectionSelector genLeptonSelector(era, -1, isDEBUG);
  genLeptonSelector.getSelector().set_min_pt_muon(selMuon_sublead_min_pt);
  genLeptonSelector.getSelector().set_max_absEta_muon(selMuon_max_absEta);
  genLeptonSelector.getSelector().set_min_pt_electron(selElectron_sublead_min_pt);
  genLeptonSelector.getSelector().set_max_absEta_electron(selElectron_max_absEta);

  GenJetCollectionSelector genBJetSelector(era, -1, isDEBUG);
  genBJetSelector.getSelector().set_min_pt(selJetAK4_min_pt_Hbb);
  genBJetSelector.getSelector().set_max_absEta(selJetAK4_max_absEta_Hbb);

  GenJetCollectionCleaner genJetCleaner_dR04(0.4);

//--- declare missing transverse energy
  RecoMEtReader* metReader = new RecoMEtReader(era, isMC, branchName_met);
  inputTree->registerReader(metReader);

//--- declare generator level information
  LHEInfoReader* lheInfoReader = new LHEInfoReader(hasLHE);
  inputTree->registerReader(lheInfoReader);

  TH1* histogram_genLepton_lead_pt = fs.make<TH1D>("genLepton_lead_pt", "genLepton_lead_pt", 70, 0., 350.);
  TH1* histogram_genLepton_lead_absEta = fs.make<TH1D>("genLepton_lead_absEta", "genLepton_lead_absEta", 100, 0., 10.);
  TH1* histogram_genLepton_sublead_pt = fs.make<TH1D>("genLepton_sublead_pt", "genLepton_sublead_pt", 70, 0., 350.);
  TH1* histogram_genLepton_sublead_absEta = fs.make<TH1D>("genLepton_sublead_absEta", "genLepton_sublead_absEta", 100, 0., 10.);
  TH1* histograms_dR_genLeptons = fs.make<TH1D>("dR_genLeptons", "dR_genLeptons", 50, 0., 5.);
  TH1* histograms_dEta_genLeptons = fs.make<TH1D>("dEta_genLeptons", "dEta_genLeptons", 50, 0., 5.);
  TH1* histograms_dPhi_genLeptons = fs.make<TH1D>("dPhi_genLeptons", "dPhi_genLeptons", 36, 0., TMath::Pi());
  TH1* histograms_dPhi_rf_genLeptons = fs.make<TH1D>("dPhi_rf_genLeptons", "dPhi_rf_genLeptons", 36, 0., TMath::Pi());
  TH2* histograms_dR_genLeptons_vs_ptH = fs.make<TH2D>("dR_genLeptons_vs_ptH", "dR_genLeptons_vs_ptH", 50, 0., 500., 50, 0., 5.);

  genJetHistograms* histograms_genBJet = new genJetHistograms("genBJet");
  histograms_genBJet->bookHistograms(fs);
  TH1* histograms_dR_genBJets = fs.make<TH1D>("dR_genBJets", "dR_genBJets", 50, 0., 5.);
  TH2* histograms_dR_genBJets_vs_ptHbb = fs.make<TH2D>("dR_genBJets_vs_ptHbb", "dR_genBJets_vs_ptHbb", 50, 0., 500., 50, 0., 5.);

  TH1* histogram_selJetCorrelation = fs.make<TH1D>("selJetCorrelation", "selJetCorrelation", 6, -0.5, 5.5);
  enum { k2Rec2Sel, k2Rec1Sel, k2Rec0Sel, k1Rec1Sel, k1Rec0Sel, k0Rec };
  TAxis* xAxis_selJetCorrelation = histogram_selJetCorrelation->GetXaxis();
  xAxis_selJetCorrelation->SetTitle("H->bb");
  xAxis_selJetCorrelation->SetBinLabel(1, "2Rec2Sel");
  xAxis_selJetCorrelation->SetBinLabel(2, "2Rec1Sel");
  xAxis_selJetCorrelation->SetBinLabel(3, "2Rec0Sel");
  xAxis_selJetCorrelation->SetBinLabel(4, "1Rec1Sel");
  xAxis_selJetCorrelation->SetBinLabel(5, "1Rec0Sel");
  xAxis_selJetCorrelation->SetBinLabel(6, "0Rec");

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

  memHistograms* histograms_memOutput_fullyMatched = new memHistograms("", 0, 0);
  histograms_memOutput_fullyMatched->bookHistograms(fs);
  memHistograms* histograms_memOutput_unmatchedLepton = new memHistograms("", 1, 0);
  histograms_memOutput_unmatchedLepton->bookHistograms(fs);
  memHistograms* histograms_memOutput_unmatchedBJet = new memHistograms("", 0, 1);
  histograms_memOutput_unmatchedBJet->bookHistograms(fs);

  memHistograms* histograms_memOutput_missingBJet_fullyMatched = new memHistograms("missingBJet", 0, 0);
  histograms_memOutput_missingBJet_fullyMatched->bookHistograms(fs);
  memHistograms* histograms_memOutput_missingBJet_unmatchedLepton = new memHistograms("missingBJet", 1, 0);
  histograms_memOutput_missingBJet_unmatchedLepton->bookHistograms(fs);
  memHistograms* histograms_memOutput_missingBJet_unmatchedBJet = new memHistograms("missingBJet", 0, 1);
  histograms_memOutput_missingBJet_unmatchedBJet->bookHistograms(fs);

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
      genParticleMatcherFromHiggs.setGenParticles(genParticlesFromHiggs, genLeptons, genNeutrinos, {});
      genParticleMatcher = &genParticleMatcherFromHiggs;
    }
    else if ( isMC_TT )
    {
      std::vector<GenLepton> genLeptonsFromTop = genLeptonFromTopReader->read();
      std::vector<GenParticle> genNeutrinosFromTop = genNeutrinoFromTopReader->read();
      std::vector<GenParticle> genBJetsFromTop = genBJetFromTopReader->read();
      genParticleMatcherFromTop.setGenParticles(genLeptonsFromTop, genNeutrinosFromTop, {}, genBJetsFromTop);
      genParticleMatcher = &genParticleMatcherFromTop;
    }
    else assert(0);
    std::vector<GenLepton> genLeptons = genParticleMatcher->getLeptons();
    std::vector<GenJet> genBJets = genParticleMatcher->getBJets();
    if ( isDEBUG ) {
      dumpGenLeptons("genLepton", genLeptons);
      dumpGenJets("genBJet", genBJets);
    }
    const Particle::LorentzVector& genMEtP4 = genParticleMatcher->getMEt();

    if ( !(genLeptons.size() == 2) ) {
      continue;
    }
    for ( std::string column : { "gen", "rec", "gen&rec" } ) {
      cutFlowTable.update("exactly 2 gen-lepton", column, evtWeight);
    }

    if ( !(genBJets.size() == 2) ) {
      continue;
    }
    for ( std::string column : { "gen", "rec", "gen&rec" } ) {
      cutFlowTable.update("exactly 2 gen-jets from H->bb decay", column, evtWeight);
    }

    std::vector<const GenLepton*> genLeptons_ptrs = convert_to_ptrs(genLeptons);
    genLeptonSelector.getSelector().set_min_pt_muon(-1.);
    genLeptonSelector.getSelector().set_min_pt_electron(-1.);
    std::vector<const GenLepton*> genLeptons_passingEta = genLeptonSelector(genLeptons_ptrs);
    genLeptonSelector.getSelector().set_min_pt_muon(selMuon_lead_min_pt);
    genLeptonSelector.getSelector().set_min_pt_electron(selElectron_lead_min_pt);
    std::vector<const GenLepton*> genLeptons_passingLeadPt_and_Eta = genLeptonSelector(genLeptons_ptrs);
    genLeptonSelector.getSelector().set_min_pt_muon(selMuon_sublead_min_pt);
    genLeptonSelector.getSelector().set_min_pt_electron(selElectron_sublead_min_pt);
    std::vector<const GenLepton*> genLeptons_passingSubleadPt_and_Eta = genLeptonSelector(genLeptons_ptrs);

    if ( genLeptons_ptrs.size() == 2 )
    {
      const GenLepton* genLepton_lead = genLeptons_ptrs[0];
      fillWithOverFlow(histogram_genLepton_lead_absEta, genLepton_lead->absEta(), evtWeight);
      if ( (genLepton_lead->is_electron() && genLepton_lead->absEta() < selElectron_max_absEta) ||
           (genLepton_lead->is_muon()     && genLepton_lead->absEta() < selMuon_max_absEta    ) ) {
        fillWithOverFlow(histogram_genLepton_lead_pt, genLepton_lead->pt(), evtWeight);
      }
      const GenLepton* genLepton_sublead = genLeptons_ptrs[1];
      fillWithOverFlow(histogram_genLepton_sublead_absEta, genLepton_sublead->absEta(), evtWeight);
      if ( (genLepton_sublead->is_electron() && genLepton_sublead->absEta() < selElectron_max_absEta) ||
           (genLepton_sublead->is_muon()     && genLepton_sublead->absEta() < selMuon_max_absEta    ) ) {
        fillWithOverFlow(histogram_genLepton_sublead_pt, genLepton_sublead->pt(), evtWeight);
      }
      double dR_genLeptons = deltaR(genLepton_lead->p4(), genLepton_sublead->p4());
      fillWithOverFlow(histograms_dR_genLeptons, dR_genLeptons, evtWeight);
      double dEta_genLeptons = TMath::Abs(genLepton_lead->eta() - genLepton_sublead->eta());
      fillWithOverFlow(histograms_dEta_genLeptons, dEta_genLeptons, evtWeight);
      double dPhi_genLeptons = TMath::Abs(deltaPhi(genLepton_lead->phi(), genLepton_sublead->phi())); // CV: map dPhi into interval [0..pi]
      fillWithOverFlow(histograms_dPhi_genLeptons, dPhi_genLeptons, evtWeight);
      Particle::LorentzVector genHlnulnuP4 = genLepton_lead->p4() + genLepton_sublead->p4() + genMEtP4;
      double dPhi_rf_genLeptons = TMath::Abs(deltaPhi_rf(genLepton_lead->p4(), genLepton_sublead->p4(), genHlnulnuP4));
      fillWithOverFlow(histograms_dPhi_rf_genLeptons, dPhi_rf_genLeptons, evtWeight);
      fillWithOverFlow2d(histograms_dR_genLeptons_vs_ptH, genHlnulnuP4.pt(), dR_genLeptons, evtWeight);
    }

    std::vector<const GenJet*> genBJets_ptrs = convert_to_ptrs(genBJets);
    std::sort(genBJets_ptrs.begin(), genBJets_ptrs.end(), isHigherPt);
    genBJetSelector.getSelector().set_max_absEta(1.e+3);
    std::vector<const GenJet*> genBJets_passingPt = genBJetSelector(genBJets_ptrs);
    genBJetSelector.getSelector().set_max_absEta(selJetAK4_max_absEta_Hbb);
    std::vector<const GenJet*> genBJets_passingPt_and_Eta = genBJetSelector(genBJets_ptrs);
    std::vector<const GenJet*> cleanedGenBJets_wrtLeptons = genJetCleaner_dR04(genBJets_passingPt_and_Eta, genLeptons_passingEta);

    fillHistograms_genJets(genBJets_ptrs, genBJetSelector, *histograms_genBJet, evtWeight);

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
    preselMuonSelector.getSelector().set_min_pt(selMuon_sublead_min_pt);
    const std::vector<const RecoMuon*> looseMuons_passingSubleadPt_and_Eta = preselMuonSelector(cleanedMuons, isHigherConePt);
    const std::vector<const RecoMuon*> tightMuons_passingSubleadPt_and_Eta = tightMuonSelector(looseMuons_passingSubleadPt_and_Eta, isHigherConePt);
    preselMuonSelector.getSelector().set_min_pt(selMuon_lead_min_pt);
    const std::vector<const RecoMuon*> looseMuons_passingLeadPt_and_Eta = preselMuonSelector(looseMuons_passingSubleadPt_and_Eta, isHigherConePt);
    const std::vector<const RecoMuon*> tightMuons_passingLeadPt_and_Eta = tightMuonSelector(looseMuons_passingLeadPt_and_Eta, isHigherConePt);
    if ( isDEBUG ) {
      printCollection(Form("tightMuons (pT > %2.0f)", selMuon_sublead_min_pt), tightMuons_passingSubleadPt_and_Eta);
    }

    const std::vector<RecoElectron> electrons = electronReader->read();
    const std::vector<const RecoElectron*> electron_ptrs = convert_to_ptrs(electrons);
    const std::vector<const RecoElectron*> cleanedElectrons = electronCleaner(electron_ptrs, tightMuons_passingSubleadPt_and_Eta);
    preselElectronSelector.getSelector().set_min_pt(10.);
    const std::vector<const RecoElectron*> looseElectrons_passingEta = preselElectronSelector(cleanedElectrons, isHigherConePt);
    preselElectronSelector.getSelector().set_min_pt(selElectron_sublead_min_pt);
    const std::vector<const RecoElectron*> looseElectrons_passingSubleadPt_and_Eta = preselElectronSelector(cleanedElectrons, isHigherConePt);
    const std::vector<const RecoElectron*> tightElectrons_passingSubleadPt_and_Eta = tightElectronSelector(looseElectrons_passingSubleadPt_and_Eta, isHigherConePt);
    preselElectronSelector.getSelector().set_min_pt(selElectron_lead_min_pt);
    const std::vector<const RecoElectron*> looseElectrons_passingLeadPt_and_Eta = preselElectronSelector(looseElectrons_passingSubleadPt_and_Eta, isHigherConePt);
    const std::vector<const RecoElectron*> tightElectrons_passingLeadPt_and_Eta = tightElectronSelector(looseElectrons_passingLeadPt_and_Eta, isHigherConePt);
    if ( isDEBUG ) {
      printCollection(Form("tightElectrons (pT > %2.0f)", selElectron_sublead_min_pt), tightElectrons_passingSubleadPt_and_Eta);
    }

    const std::vector<const RecoLepton*> looseLeptonsFull_passingEta = mergeLeptonCollections(
      looseElectrons_passingEta, looseMuons_passingEta, isHigherConePt);
    const std::vector<const RecoLepton*> looseLeptons_passingEta = pickFirstNobjects(looseLeptonsFull_passingEta, 2);
    const std::vector<const RecoLepton*> looseLeptonsFull_passingSubleadPt_and_Eta = mergeLeptonCollections(
      looseElectrons_passingSubleadPt_and_Eta, looseMuons_passingSubleadPt_and_Eta, isHigherConePt);
    const std::vector<const RecoLepton*> looseLeptons_passingSubleadPt_and_Eta = pickFirstNobjects(looseLeptonsFull_passingSubleadPt_and_Eta, 2);
    const std::vector<const RecoLepton*> tightLeptonsFull_passingSubleadPt_and_Eta = mergeLeptonCollections(
      tightElectrons_passingSubleadPt_and_Eta, tightMuons_passingSubleadPt_and_Eta, isHigherConePt);
    const std::vector<const RecoLepton*> tightLeptons_passingSubleadPt_and_Eta = pickFirstNobjects(tightLeptonsFull_passingSubleadPt_and_Eta, 2);
    const std::vector<const RecoLepton*> looseLeptonsFull_passingLeadPt_and_Eta = mergeLeptonCollections(
      looseElectrons_passingLeadPt_and_Eta, looseMuons_passingLeadPt_and_Eta, isHigherConePt);
    const std::vector<const RecoLepton*> looseLeptons_passingLeadPt_and_Eta = pickFirstNobjects(looseLeptonsFull_passingLeadPt_and_Eta, 2);
    const std::vector<const RecoLepton*> tightLeptonsFull_passingLeadPt_and_Eta = mergeLeptonCollections(
      tightElectrons_passingLeadPt_and_Eta, tightMuons_passingLeadPt_and_Eta, isHigherConePt);
    const std::vector<const RecoLepton*> tightLeptons_passingLeadPt_and_Eta = pickFirstNobjects(tightLeptonsFull_passingLeadPt_and_Eta, 2);

//--- build collections of jets and select subset of jets passing b-tagging criteria
    const std::vector<RecoJet> jets_ak4 = jetReaderAK4->read();
    const std::vector<const RecoJet*> jet_ptrs_ak4 = convert_to_ptrs(jets_ak4);
    //const std::vector<const RecoJet*> cleanedJetsAK4_wrtLeptons = jetCleaningByIndex ?
    //  jetCleanerAK4_byIndex(jet_ptrs_ak4, tightLeptons_passingPt_and_Eta) :
    //  jetCleanerAK4_dR04   (jet_ptrs_ak4, tightLeptons_passingPt_and_Eta)
    //;
    const std::vector<const RecoJet*> cleanedJetsAK4_wrtLeptons = jetCleanerAK4_dR04(jet_ptrs_ak4, tightLeptons_passingSubleadPt_and_Eta);
    const std::vector<const RecoJet*> selJetsAK4 = jetSelectorAK4(cleanedJetsAK4_wrtLeptons, isHigherPt);
    const std::vector<const RecoJet*> selBJetsAK4_loose = jetSelectorAK4_bTagLoose(cleanedJetsAK4_wrtLeptons, isHigherPt);
    const std::vector<const RecoJet*> selBJetsAK4_medium = jetSelectorAK4_bTagMedium(cleanedJetsAK4_wrtLeptons, isHigherPt);

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

    passesEvtSel_rec         = passesEvtSel_rec         && looseLeptons_passingLeadPt_and_Eta.size() >= 1;
    passesEvtSel_gen         = passesEvtSel_gen         && genLeptons_passingLeadPt_and_Eta.size() >= 1;
    passesEvtSel_rec_and_gen = passesEvtSel_rec_and_gen && selectGenMatchedParticles(looseLeptons_passingLeadPt_and_Eta, genLeptons_passingLeadPt_and_Eta).size() >= 1;
    const std::string cutLooseLeadLeptonPt_and_Eta = Form("loose leading electron (muon) pT > %2.0f (%2.0f) GeV", selElectron_lead_min_pt, selMuon_lead_min_pt);
    if ( passesEvtSel_rec         ) cutFlowTable.update(cutLooseLeadLeptonPt_and_Eta, "rec",     evtWeight);
    if ( passesEvtSel_gen         ) cutFlowTable.update(cutLooseLeadLeptonPt_and_Eta, "gen",     evtWeight);
    if ( passesEvtSel_rec_and_gen ) cutFlowTable.update(cutLooseLeadLeptonPt_and_Eta, "gen&rec", evtWeight);

    passesEvtSel_rec         = passesEvtSel_rec         && looseLeptons_passingSubleadPt_and_Eta.size() >= 2;
    passesEvtSel_gen         = passesEvtSel_gen         && genLeptons_passingSubleadPt_and_Eta.size() >= 2;
    passesEvtSel_rec_and_gen = passesEvtSel_rec_and_gen && selectGenMatchedParticles(looseLeptons_passingSubleadPt_and_Eta, genLeptons_passingSubleadPt_and_Eta).size() >= 2;
    const std::string cutLooseSubleadLeptonPt_and_Eta = Form("loose subleading electron (muon) pT > %2.0f (%2.0f) GeV", selElectron_sublead_min_pt, selMuon_sublead_min_pt);
    if ( passesEvtSel_rec         ) cutFlowTable.update(cutLooseSubleadLeptonPt_and_Eta, "rec",     evtWeight);
    if ( passesEvtSel_gen         ) cutFlowTable.update(cutLooseSubleadLeptonPt_and_Eta, "gen",     evtWeight);
    if ( passesEvtSel_rec_and_gen ) cutFlowTable.update(cutLooseSubleadLeptonPt_and_Eta, "gen&rec", evtWeight);

    passesEvtSel_rec         = passesEvtSel_rec         && tightLeptons_passingSubleadPt_and_Eta.size() >= 2 &&
                                                           tightLeptons_passingLeadPt_and_Eta.size()    >= 1;
    passesEvtSel_gen         = passesEvtSel_gen         && true;
    passesEvtSel_rec_and_gen = passesEvtSel_rec_and_gen && selectGenMatchedParticles(tightLeptons_passingSubleadPt_and_Eta, genLeptons_passingSubleadPt_and_Eta).size() >= 2 &&
                                                           selectGenMatchedParticles(tightLeptons_passingLeadPt_and_Eta,    genLeptons_passingLeadPt_and_Eta).size()    >= 1;
    const std::string cutTightLeptonPt_and_Eta = ">= 2 tight leptons";
    if ( passesEvtSel_rec         ) cutFlowTable.update(cutTightLeptonPt_and_Eta, "rec",     evtWeight);
    if ( passesEvtSel_gen         ) cutFlowTable.update(cutTightLeptonPt_and_Eta, "gen",     evtWeight);
    if ( passesEvtSel_rec_and_gen ) cutFlowTable.update(cutTightLeptonPt_and_Eta, "gen&rec", evtWeight);

    const RecoLepton* tightLepton_lead    = nullptr;
    const RecoLepton* tightLepton_sublead = nullptr;
    if ( tightLeptons_passingSubleadPt_and_Eta.size() >= 2 )
    {
      tightLepton_lead    = tightLeptons_passingSubleadPt_and_Eta[0];
      tightLepton_sublead = tightLeptons_passingSubleadPt_and_Eta[1];
    }

    const std::vector<RecoJetAK8> jets_ak8 = jetReaderAK8->read();
    const std::vector<const RecoJetAK8*> jet_ptrs_ak8 = convert_to_ptrs(jets_ak8);

//--- select jets from H->bb decay
    const std::vector<const RecoJetAK8*> cleanedJetsAK8_wrtLeptons = jetCleanerAK8_dR08(jet_ptrs_ak8, tightLeptons_passingSubleadPt_and_Eta);
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

    bool passesBoosted_recHbb          = selJetAK8_Hbb;
    bool passesBoosted_genHbb          = isBoosted_genHbb(genBJets_ptrs);
    bool passesBoosted_rec_and_genHbb  = passesBoosted_recHbb && passesBoosted_genHbb;
    if ( passesEvtSel_rec         ) updateCutFlowTable(cutFlowTable, "rec",     passesBoosted_recHbb,         evtWeight);
    if ( passesEvtSel_gen         ) updateCutFlowTable(cutFlowTable, "gen",     passesBoosted_genHbb,         evtWeight);
    if ( passesEvtSel_rec_and_gen ) updateCutFlowTable(cutFlowTable, "gen&rec", passesBoosted_rec_and_genHbb, evtWeight);

//--- compute MHT and linear MET discriminant (met_LD)
    //RecoMEt met = metReader->read();
    //const Particle::LorentzVector& metP4 = met.p4();
    //const std::vector<const RecoJet*> selJetsAK4_mht = jetSelectorAK4(cleanedJetsAK4_wrtLeptons, isHigherPt);
    //Particle::LorentzVector mhtP4 = compMHT(tightLeptons, {}, selJetsAK4_mht);
    //double met_LD = compMEt_LD(metP4, mhtP4);

//--- apply final selection
    bool isSelected = false;
    if ( tightLepton_lead && tightLepton_sublead ) {
      if ( ((tightLepton_lead->is_electron()    && tightLepton_lead->cone_pt()    > selElectron_lead_min_pt   ) ||
            (tightLepton_lead->is_muon()        && tightLepton_lead->cone_pt()    > selMuon_lead_min_pt       )) &&
           ((tightLepton_sublead->is_electron() && tightLepton_sublead->cone_pt() > selElectron_sublead_min_pt) ||
            (tightLepton_sublead->is_muon()     && tightLepton_sublead->cone_pt() > selMuon_sublead_min_pt    )) ) {
        if ( selJet1_Hbb && selJet2_Hbb   &&
             numBJets_medium >= 1         ) {
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

    histogram_selJetCorrelation->Fill(idxHbb, evtWeight);

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

    if ( memReader )
    {
      std::vector<MEMOutput_hh_bb2l> memOutputs_hh_bb2l = memReader->read();
      for ( std::vector<MEMOutput_hh_bb2l>::const_iterator memOutput = memOutputs_hh_bb2l.begin();
  	    memOutput != memOutputs_hh_bb2l.end(); ++memOutput ) {
        fillHistograms_mem(
          *memOutput,
  	  genLeptons_ptrs, genBJets_ptrs,
	  *histograms_memOutput_fullyMatched,
	  *histograms_memOutput_unmatchedLepton,
	  *histograms_memOutput_unmatchedBJet, evtWeight);
      }
    }
    if ( memReader_missingBJet )
    {
      std::vector<MEMOutput_hh_bb2l> memOutputs_hh_bb2l_missingBJet = memReader_missingBJet->read();
      for ( std::vector<MEMOutput_hh_bb2l>::const_iterator memOutput = memOutputs_hh_bb2l_missingBJet.begin();
  	    memOutput != memOutputs_hh_bb2l_missingBJet.end(); ++memOutput ) {
        fillHistograms_mem(
          *memOutput,
	  genLeptons_ptrs, genBJets_ptrs,
	  *histograms_memOutput_missingBJet_fullyMatched,
	  *histograms_memOutput_missingBJet_unmatchedLepton,
	  *histograms_memOutput_missingBJet_unmatchedBJet, evtWeight);
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
  delete metReader;
  delete genLeptonReader;
  delete genNeutrinoReader;
  delete genParticleFromHiggsReader;
  delete genLeptonFromTopReader;
  delete genNeutrinoFromTopReader;
  delete genBJetFromTopReader;
  delete lheInfoReader;

  delete inputTree;

  clock.Show("analyzeMEM_hh_bb2l");

  return EXIT_SUCCESS;
}
