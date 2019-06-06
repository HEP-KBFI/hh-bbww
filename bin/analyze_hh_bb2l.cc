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
#include "tthAnalysis/HiggsToTauTau/interface/GenHadTau.h" // GenHadTau
#include "tthAnalysis/HiggsToTauTau/interface/EventInfo.h" // EventInfo
#include "tthAnalysis/HiggsToTauTau/interface/LeptonFakeRateInterface.h" // LeptonFakeRateInterface
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronReader.h" // RecoElectronReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonReader.h" // RecoMuonReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetReader.h" // RecoJetReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetReaderAK8.h" // RecoJetReaderAK8
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEtReader.h" // RecoMEtReader
#include "tthAnalysis/HiggsToTauTau/interface/MEtFilterReader.h" // MEtFilterReader
#include "tthAnalysis/HiggsToTauTau/interface/GenLeptonReader.h" // GenLeptonReader
#include "tthAnalysis/HiggsToTauTau/interface/GenParticleReader.h" // GenParticleReader
#include "tthAnalysis/HiggsToTauTau/interface/GenHadTauReader.h" // GenHadTauReader
#include "tthAnalysis/HiggsToTauTau/interface/GenPhotonReader.h" // GenPhotonReader
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
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // getBTagWeight_option, getHadTau_genPdgId, isHigherPt, isMatched, contains
#include "tthAnalysis/HiggsToTauTau/interface/leptonGenMatchingAuxFunctions.h" // getLeptonGenMatch_definitions_2lepton, getLeptonGenMatch_string, getLeptonGenMatch_int
#include "tthAnalysis/HiggsToTauTau/interface/fakeBackgroundAuxFunctions.h"
#include "tthAnalysis/HiggsToTauTau/interface/generalAuxFunctions.h" // format_vstring
#include "tthAnalysis/HiggsToTauTau/interface/mvaInputVariables.h" // comp_lep1_conePt, comp_lep2_conePt
#include "tthAnalysis/HiggsToTauTau/interface/hltPath.h" // hltPath, create_hltPaths, hltPaths_isTriggered, hltPaths_delete
#include "tthAnalysis/HiggsToTauTau/interface/hltPathReader.h" // hltPathReader
#include "tthAnalysis/HiggsToTauTau/interface/Data_to_MC_CorrectionInterface_2016.h"
#include "tthAnalysis/HiggsToTauTau/interface/Data_to_MC_CorrectionInterface_2017.h"
#include "tthAnalysis/HiggsToTauTau/interface/Data_to_MC_CorrectionInterface_2018.h"
#include "tthAnalysis/HiggsToTauTau/interface/DYMCReweighting.h" // DYMCReweighting
#include "tthAnalysis/HiggsToTauTau/interface/lutAuxFunctions.h" // loadTH2, get_sf_from_TH2
#include "tthAnalysis/HiggsToTauTau/interface/cutFlowTable.h" // cutFlowTableType
#include "tthAnalysis/HiggsToTauTau/interface/NtupleFillerBDT.h" // NtupleFillerBDT
#include "tthAnalysis/HiggsToTauTau/interface/TTreeWrapper.h" // TTreeWrapper
#include "tthAnalysis/HiggsToTauTau/interface/hltFilter.h" // hltFilter()
#include "tthAnalysis/HiggsToTauTau/interface/EvtWeightManager.h" // EvtWeightManager

#include "hhAnalysis/bbww/interface/SyncNtupleManager_bbww.h" // SyncNtupleManager_bbww
#include "hhAnalysis/bbww/interface/EvtHistManager_hh_bb2l.h" // EvtHistManager_hh_bb2l
#include "hhAnalysis/bbww/interface/RecoJetCollectionSelectorAK8_hh_bbWW_Hbb.h" // RecoJetSelectorAK8_hh_bbWW_Hbb
#include "tthAnalysis/HiggsToTauTau/interface/mT2_2particle.h" // mT2_2particle
#include "tthAnalysis/HiggsToTauTau/interface/mT2_3particle.h" // mT2_3particle
#include "tthAnalysis/HiggsToTauTau/interface/Higgsness.h" // Higgsness
#include "tthAnalysis/HiggsToTauTau/interface/Topness.h" // Topness
#include "hhAnalysis/Heavymassestimator/interface/heavyMassEstimator.h" // heavyMassEstimator (HME) algorithm for computation of HH mass
#include "tthAnalysis/HiggsToTauTau/interface/LocalFileInPath.h" // LocalFileInPath

#include <boost/math/special_functions/sign.hpp> // boost::math::sign()
#include "tthAnalysis/HiggsToTauTau/interface/XGBInterface.h" // XGBInterface
#include "tthAnalysis/HiggsToTauTau/interface/MVAInputVarHistManager.h" // MVAInputVarHistManager
#include "hhAnalysis/bbww/interface/HHWeightInterface.h" // HHWeightInterface

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

enum { kFR_disabled, kFR_enabled };

const double wBosonMass = 80.379; // GeV

enum { kHbb_undefined, kHbb_resolved, kHbb_boosted };
enum { kVBF_undefined, kVBF_nottagged, kVBF_tagged };

struct categoryEntryType
{
  categoryEntryType(int numElectrons, int numMuons, int numBJets_medium, int numBJets_loose, int type_Hbb, int type_vbf)
    : numElectrons_(numElectrons)
    , numMuons_(numMuons)
    , numBJets_medium_(numBJets_medium)
    , numBJets_loose_(numBJets_loose)
    , type_Hbb_(type_Hbb)
    , type_vbf_(type_vbf)
  {
    name_ = "hh_";
    if      ( numBJets_medium_ >= 2                         ) name_ += "2bM";
    else if ( numBJets_medium_ >= 1 && numBJets_loose_ >= 2 ) name_ += "1bM1bL";
    else if ( numBJets_medium_ >= 1                         ) name_ += "1bM";
    else name_ += "bb";
    if      ( numElectrons_ >= 2                   ) name_ += "2e";
    else if (                       numMuons_ >= 2 ) name_ += "2mu";
    else if ( numElectrons_ >= 1 && numMuons_ >= 1 ) name_ += "1e1mu";
    else name_ += "2l";
    if      ( type_Hbb_ == kHbb_resolved           ) name_ += "_resolvedHbb";
    else if ( type_Hbb_ == kHbb_boosted            ) name_ += "_boostedHbb";
    if      ( type_vbf_ == kVBF_tagged             ) name_ += "_vbf";
    else if ( type_vbf_ == kVBF_nottagged          ) name_ += "_nonvbf";
  }
  ~categoryEntryType() {}
  std::string name_;
  int numElectrons_;
  int numMuons_;
  int numBJets_medium_;
  int numBJets_loose_;
  int type_Hbb_; // 0 = either resolved or boosted, 1 = resolved, 2 = boosted
  int type_vbf_; // 0 = either tagged or not tagged, 1 = not tagged; 2 = tagged
};

void addCategory_conditionally(std::vector<categoryEntryType>& categories_evt, const categoryEntryType& category, const std::vector<std::string>& evtCategories)
{
  if ( contains(evtCategories, category.name_) ) {
    categories_evt.push_back(category);
  }
}

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

  std::cout << "<analyze_hh_bb2l>:" << std::endl;

//--- keep track of time it takes the macro to execute
  TBenchmark clock;
  clock.Start("analyze_hh_bb2l");

//--- read python configuration parameters
  if ( !edm::readPSetsFrom(argv[1])->existsAs<edm::ParameterSet>("process") )
    throw cms::Exception("analyze_hh_bb2l")
      << "No ParameterSet 'process' found in configuration file = " << argv[1] << " !!\n";

  edm::ParameterSet cfg = edm::readPSetsFrom(argv[1])->getParameter<edm::ParameterSet>("process");

  edm::ParameterSet cfg_analyze = cfg.getParameter<edm::ParameterSet>("analyze_hh_bb2l");

  std::string treeName = cfg_analyze.getParameter<std::string>("treeName");

  std::string process_string = cfg_analyze.getParameter<std::string>("process");
  bool isSignal = ( process_string == "signal" ) ? true : false;

  std::string histogramDir = cfg_analyze.getParameter<std::string>("histogramDir");
  bool isMCClosure_e = histogramDir.find("mcClosure_e") != std::string::npos;
  bool isMCClosure_m = histogramDir.find("mcClosure_m") != std::string::npos;

  std::string era_string = cfg_analyze.getParameter<std::string>("era");
  const int era = get_era(era_string);

  vstring triggerNames_1e = cfg_analyze.getParameter<vstring>("triggers_1e");
  std::vector<hltPath*> triggers_1e = create_hltPaths(triggerNames_1e);
  bool use_triggers_1e = cfg_analyze.getParameter<bool>("use_triggers_1e");
  vstring triggerNames_2e = cfg_analyze.getParameter<vstring>("triggers_2e");
  std::vector<hltPath*> triggers_2e = create_hltPaths(triggerNames_2e);
  bool use_triggers_2e = cfg_analyze.getParameter<bool>("use_triggers_2e");
  vstring triggerNames_1mu = cfg_analyze.getParameter<vstring>("triggers_1mu");
  std::vector<hltPath*> triggers_1mu = create_hltPaths(triggerNames_1mu);
  bool use_triggers_1mu = cfg_analyze.getParameter<bool>("use_triggers_1mu");
  vstring triggerNames_2mu = cfg_analyze.getParameter<vstring>("triggers_2mu");
  std::vector<hltPath*> triggers_2mu = create_hltPaths(triggerNames_2mu);
  bool use_triggers_2mu = cfg_analyze.getParameter<bool>("use_triggers_2mu");
  vstring triggerNames_1e1mu = cfg_analyze.getParameter<vstring>("triggers_1e1mu");
  std::vector<hltPath*> triggers_1e1mu = create_hltPaths(triggerNames_1e1mu);
  bool use_triggers_1e1mu = cfg_analyze.getParameter<bool>("use_triggers_1e1mu");

  bool apply_offline_e_trigger_cuts_1e = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_1e");
  bool apply_offline_e_trigger_cuts_2e = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_2e");
  bool apply_offline_e_trigger_cuts_1mu = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_1mu");
  bool apply_offline_e_trigger_cuts_2mu = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_2mu");
  bool apply_offline_e_trigger_cuts_1e1mu = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_1e1mu");

  enum { kOS, kSS, kDisabled };
  std::string leptonChargeSelection_string = cfg_analyze.getParameter<std::string>("leptonChargeSelection");
  int leptonChargeSelection = -1;
  if      ( leptonChargeSelection_string == "OS"       ) leptonChargeSelection = kOS;
  else if ( leptonChargeSelection_string == "SS"       ) leptonChargeSelection = kSS;
  else if ( leptonChargeSelection_string == "disabled" ) leptonChargeSelection = kDisabled;
  else throw cms::Exception("analyze_hh_bb2l")
    << "Invalid Configuration parameter 'leptonChargeSelection' = " << leptonChargeSelection_string << " !!\n";

  const std::string electronSelection_string = cfg_analyze.getParameter<std::string>("electronSelection");
  const std::string muonSelection_string     = cfg_analyze.getParameter<std::string>("muonSelection");
  std::cout << "electronSelection_string = " << electronSelection_string << "\n"
               "muonSelection_string     = " << muonSelection_string     << '\n'
  ;
  const int electronSelection = get_selection(electronSelection_string);
  const int muonSelection     = get_selection(muonSelection_string);
  double lep_mva_cut = cfg_analyze.getParameter<double>("lep_mva_cut"); // CV: used for tight lepton selection only

  bool apply_leptonGenMatching = cfg_analyze.getParameter<bool>("apply_leptonGenMatching");
  std::vector<leptonGenMatchEntry> leptonGenMatch_definitions = getLeptonGenMatch_definitions_2lepton(apply_leptonGenMatching);
  std::cout << "leptonGenMatch_definitions:" << std::endl;
  std::cout << leptonGenMatch_definitions;

  vstring evtCategoryNames = cfg_analyze.getParameter<vstring>("evtCategories");
  std::cout << "evtCategories = " << format_vstring(evtCategoryNames) << std::endl;

  bool isMC = cfg_analyze.getParameter<bool>("isMC");
  bool isMC_tH = ( process_string == "tHq" || process_string == "tHW" ) ? true : false;
  bool isMC_HH_nonres = ( process_string == "signal_ggf_nonresonant_bbvv" ) ? true : false;
  bool hasLHE = cfg_analyze.getParameter<bool>("hasLHE");
  std::string central_or_shift = cfg_analyze.getParameter<std::string>("central_or_shift");
  double lumiScale = ( process_string != "data_obs" ) ? cfg_analyze.getParameter<double>("lumiScale") : 1.;
  bool apply_genWeight = cfg_analyze.getParameter<bool>("apply_genWeight");
  bool apply_DYMCReweighting = cfg_analyze.getParameter<bool>("apply_DYMCReweighting");
  bool apply_hlt_filter = cfg_analyze.getParameter<bool>("apply_hlt_filter");
  bool apply_met_filters = cfg_analyze.getParameter<bool>("apply_met_filters");
  edm::ParameterSet cfgMEtFilter = cfg_analyze.getParameter<edm::ParameterSet>("cfgMEtFilter");
  MEtFilterSelector metFilterSelector(cfgMEtFilter, isMC);
  const bool useNonNominal = cfg_analyze.getParameter<bool>("useNonNominal");
  const bool useNonNominal_jetmet = useNonNominal || ! isMC;

  const edm::ParameterSet syncNtuple_cfg = cfg_analyze.getParameter<edm::ParameterSet>("syncNtuple");
  const std::string syncNtuple_tree = syncNtuple_cfg.getParameter<std::string>("tree");
  const std::string syncNtuple_output = syncNtuple_cfg.getParameter<std::string>("output");
  const bool sync_requireGenMatching = syncNtuple_cfg.getParameter<bool>("requireGenMatching");
  const bool do_sync = ! syncNtuple_tree.empty() && ! syncNtuple_output.empty();

  const edm::ParameterSet additionalEvtWeight = cfg_analyze.getParameter<edm::ParameterSet>("evtWeight");
  const bool applyAdditionalEvtWeight = additionalEvtWeight.getParameter<bool>("apply");
  EvtWeightManager * eventWeightManager = nullptr;
  if ( applyAdditionalEvtWeight ) {
    eventWeightManager = new EvtWeightManager(additionalEvtWeight);
  }

  bool isDEBUG = cfg_analyze.getParameter<bool>("isDEBUG");
  if ( isDEBUG ) std::cout << "Warning: DEBUG mode enabled -> trigger selection will not be applied for data !!" << std::endl;

  checkOptionValidity(central_or_shift, isMC);
  const int jetToLeptonFakeRate_option = getJetToLeptonFR_option  (central_or_shift);
  const int lheScale_option            = getLHEscale_option       (central_or_shift);
  const int jetBtagSF_option           = getBTagWeight_option     (central_or_shift);
  const int dyMCReweighting_option     = getDYMCReweighting_option(central_or_shift);

  const int met_option   = useNonNominal_jetmet ? kMEt_central_nonNominal : getMET_option(central_or_shift, isMC);
  const int jetPt_option = useNonNominal_jetmet ? kMEt_central_nonNominal : getJet_option(central_or_shift, isMC);

  std::cout
    << "central_or_shift = "               << central_or_shift           << "\n"
       " -> jetToLeptonFakeRate_option = " << jetToLeptonFakeRate_option << "\n"
       " -> lheScale_option            = " << lheScale_option            << "\n"
       " -> jetBtagSF_option           = " << jetBtagSF_option           << "\n"
       " -> met_option                 = " << met_option                 << "\n"
       " -> jetPt_option               = " << jetPt_option               << '\n'
  ;

  DYMCReweighting* dyReweighting = nullptr;
  if ( apply_DYMCReweighting ) {
    dyReweighting = new DYMCReweighting(era, dyMCReweighting_option);
  }

  edm::ParameterSet cfg_dataToMCcorrectionInterface;
  cfg_dataToMCcorrectionInterface.addParameter<std::string>("era", era_string);
  cfg_dataToMCcorrectionInterface.addParameter<std::string>("hadTauSelection", "dR03mvaMedium"); // CV: dummy value (no taus used in HH->bbWW channel)
  cfg_dataToMCcorrectionInterface.addParameter<int>("hadTauSelection_antiElectron", -1);
  cfg_dataToMCcorrectionInterface.addParameter<int>("hadTauSelection_antiMuon", -1);
  cfg_dataToMCcorrectionInterface.addParameter<std::string>("central_or_shift", central_or_shift);
  cfg_dataToMCcorrectionInterface.addParameter<bool>("isDEBUG", isDEBUG);
  Data_to_MC_CorrectionInterface_Base * dataToMCcorrectionInterface = nullptr;
  switch(era)
  {
    case kEra_2016: dataToMCcorrectionInterface = new Data_to_MC_CorrectionInterface_2016(cfg_dataToMCcorrectionInterface); break;
    case kEra_2017: dataToMCcorrectionInterface = new Data_to_MC_CorrectionInterface_2017(cfg_dataToMCcorrectionInterface); break;
    case kEra_2018: dataToMCcorrectionInterface = new Data_to_MC_CorrectionInterface_2018(cfg_dataToMCcorrectionInterface); break;
    default: throw cmsException("analyze_hh_bb2l", __LINE__) << "Invalid era = " << era;
  }

  std::string applyFakeRateWeights_string = cfg_analyze.getParameter<std::string>("applyFakeRateWeights");
  int applyFakeRateWeights = -1;
  if      ( applyFakeRateWeights_string == "disabled" ) applyFakeRateWeights = kFR_disabled;
  else if ( applyFakeRateWeights_string == "enabled"  ) applyFakeRateWeights = kFR_enabled;
  else throw cms::Exception("analyze_hh_bb2l")
    << "Invalid Configuration parameter 'applyFakeRateWeights' = " << applyFakeRateWeights_string << " !!\n";

  LeptonFakeRateInterface* leptonFakeRateInterface = 0;
  if ( applyFakeRateWeights == kFR_enabled ) {
    edm::ParameterSet cfg_leptonFakeRateWeight = cfg_analyze.getParameter<edm::ParameterSet>("leptonFakeRateWeight");
    leptonFakeRateInterface = new LeptonFakeRateInterface(cfg_leptonFakeRateWeight, jetToLeptonFakeRate_option);
  }

  bool fillGenEvtHistograms = cfg_analyze.getParameter<bool>("fillGenEvtHistograms");
  edm::ParameterSet cfg_EvtYieldHistManager = cfg_analyze.getParameter<edm::ParameterSet>("cfgEvtYieldHistManager");

  std::string branchName_electrons = cfg_analyze.getParameter<std::string>("branchName_electrons");
  std::string branchName_muons = cfg_analyze.getParameter<std::string>("branchName_muons");
  std::string branchName_jets_ak4 = cfg_analyze.getParameter<std::string>("branchName_jets_ak4");
  std::string branchName_jets_ak8 = cfg_analyze.getParameter<std::string>("branchName_jets_ak8");
  std::string branchName_subjets_ak8 = cfg_analyze.getParameter<std::string>("branchName_subjets_ak8");
  std::string branchName_met = cfg_analyze.getParameter<std::string>("branchName_met");

  std::string branchName_genLeptons = cfg_analyze.getParameter<std::string>("branchName_genLeptons");
  std::string branchName_genHadTaus = cfg_analyze.getParameter<std::string>("branchName_genHadTaus");
  std::string branchName_genPhotons = cfg_analyze.getParameter<std::string>("branchName_genPhotons");
  std::string branchName_genJets = cfg_analyze.getParameter<std::string>("branchName_genJets");
  std::string branchName_genHiggses = cfg_analyze.getParameter<std::string>("branchName_genHiggses");
  bool redoGenMatching = cfg_analyze.getParameter<bool>("redoGenMatching");

  std::string branchName_genTauLeptons = cfg_analyze.getParameter<std::string>("branchName_genTauLeptons");

  bool selectBDT = ( cfg_analyze.exists("selectBDT") ) ? cfg_analyze.getParameter<bool>("selectBDT") : false;

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
  unsigned reportEvery = inputFiles.reportAfter();

  fwlite::OutputFiles outputFile(cfg);
  fwlite::TFileService fs = fwlite::TFileService(outputFile.file().data());

  TTreeWrapper* inputTree = new TTreeWrapper(treeName.data(), inputFiles.files(), maxEvents);
  std::cout << "Loaded " << inputTree->getFileCount() << " file(s)." << std::endl;

//--- prepare sync Ntuple
  SyncNtupleManager_bbww * snm = nullptr;
  if(do_sync)
  {
    snm = new SyncNtupleManager_bbww(syncNtuple_output, syncNtuple_tree);
    snm->initializeBranches();
    snm->initializeHLTBranches({ triggers_1e, triggers_2e, triggers_1mu, triggers_2mu, triggers_1e1mu });
  }

//--- declare event-level variables
  EventInfo eventInfo(isSignal, isMC, isMC_tH);
  EventInfoReader eventInfoReader(&eventInfo);
  inputTree->registerReader(&eventInfoReader);

  hltPathReader hltPathReader_instance({ triggers_1e, triggers_2e, triggers_1mu, triggers_2mu, triggers_1e1mu });
  inputTree->registerReader(&hltPathReader_instance);

  if ( eventWeightManager ) {
    inputTree->registerReader(eventWeightManager);
  }

//--- declare particle collections
  const bool readGenObjects = isMC && !redoGenMatching;
  RecoMuonReader* muonReader = new RecoMuonReader(era, branchName_muons, readGenObjects);
  inputTree->registerReader(muonReader);
  RecoMuonCollectionGenMatcher muonGenMatcher;
  RecoMuonCollectionSelectorLoose preselMuonSelector(era, -1, isDEBUG);
  RecoMuonCollectionSelectorFakeable fakeableMuonSelector(era, -1, isDEBUG);
  RecoMuonCollectionSelectorTight tightMuonSelector(era, -1, isDEBUG);
  tightMuonSelector.getSelector().set_min_mvaTTH(lep_mva_cut);

  RecoElectronReader* electronReader = new RecoElectronReader(era, branchName_electrons, readGenObjects);
  electronReader->readUncorrected(useNonNominal);
  inputTree->registerReader(electronReader);
  RecoElectronCollectionGenMatcher electronGenMatcher;
  RecoElectronCollectionCleaner electronCleaner(0.3, isDEBUG);
  RecoElectronCollectionSelectorLoose preselElectronSelector(era, -1, isDEBUG);
  RecoElectronCollectionSelectorFakeable fakeableElectronSelector(era, -1, isDEBUG);
  RecoElectronCollectionSelectorTight tightElectronSelector(era, -1, isDEBUG);
  tightElectronSelector.getSelector().set_min_mvaTTH(lep_mva_cut);

  RecoJetReader* jetReaderAK4 = new RecoJetReader(era, isMC, branchName_jets_ak4, readGenObjects);
  jetReaderAK4->setPtMass_central_or_shift(jetPt_option);
  jetReaderAK4->setBranchName_BtagWeight(jetBtagSF_option);
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
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR08(0.8, isDEBUG);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR12(1.2, isDEBUG);
  RecoJetCollectionSelectorAK8_hh_bbWW_Hbb jetSelectorAK8_Hbb(era, -1, isDEBUG);

  GenParticleReader* genTauLeptonReader = nullptr;
  if ( isMC && apply_DYMCReweighting ) {
    genTauLeptonReader = new GenParticleReader(branchName_genTauLeptons);
    inputTree->registerReader(genTauLeptonReader);
  }

//--- declare missing transverse energy
  RecoMEtReader* metReader = new RecoMEtReader(era, isMC, branchName_met);
  metReader->setMEt_central_or_shift(met_option);
  inputTree->registerReader(metReader);

  MEtFilter metFilters;
  MEtFilterReader* metFilterReader = new MEtFilterReader(&metFilters, era);
  inputTree->registerReader(metFilterReader);

//--- declare generator level information
  GenLeptonReader* genLeptonReader = 0;
  GenHadTauReader* genHadTauReader = 0;
  GenPhotonReader* genPhotonReader = 0;
  GenJetReader* genJetReader = 0;
  GenParticleReader* genHiggsReader = 0;
  LHEInfoReader* lheInfoReader = 0;
  if ( isMC ) {
    if(! readGenObjects)
    {
      if ( branchName_genLeptons != "" ) {
        genLeptonReader = new GenLeptonReader(branchName_genLeptons);
        inputTree->registerReader(genLeptonReader);
      }
      if ( branchName_genHadTaus != "" ) {
        genHadTauReader = new GenHadTauReader(branchName_genHadTaus);
        inputTree->registerReader(genHadTauReader);
      }
      if ( branchName_genPhotons != "" ) {
        genPhotonReader = new GenPhotonReader(branchName_genPhotons);
        inputTree->registerReader(genPhotonReader);
      }
      if ( branchName_genJets != "" ) {
        genJetReader = new GenJetReader(branchName_genJets);
        inputTree->registerReader(genJetReader);
      }
    }
    if ( branchName_genHiggses != "" ) {
      genHiggsReader = new GenParticleReader(branchName_genHiggses);
      inputTree->registerReader(genHiggsReader);
    }
    lheInfoReader = new LHEInfoReader(hasLHE);
    inputTree->registerReader(lheInfoReader);
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

    if(eventWeightManager)
    {
      genEvtHistManager_beforeCuts->bookHistograms(fs, eventWeightManager);
    }
  }

  std::string xmlFileName_bb2l = "hhAnalysis/bbww/data/bb2l_HH_XGB_noTopness_evtLevelSUM_HH_bb2l_res_15Var_test.xml";
  std::string xgbFileName_bb2l_res = "hhAnalysis/bbww/data/bb2l_HH_XGB_noTopness_evtLevelSUM_HH_bb2l_res_12Var.pkl";
  std::string xgbFileNamenohiggnessnotopness_bb2l = "hhAnalysis/bbww/data/bb2l_HH_XGB_noTopness_evtLevelSUM_HH_bb2l_res_10Var_nohiggnessnotopness.pkl";
  std::string xgbFileName_bb2l_nonres = "hhAnalysis/bbww/data/bb2l_HH_XGB_noTopness_evtLevelSUM_HH_bb2l_nonres_13Var.pkl";

  std::vector<std::string> xgbInputVariables_bb2l_res =
    {"mht", "m_Hbb", "m_ll", "Smin_Hww", "m_HHvis", "pT_HH", "mT2_top_2particle", "m_HH_hme", "logTopness_fixedChi2", "logHiggsness_fixedChi2", "nBJetLoose", "gen_mHH"
  };

  std::vector<std::string> xgbInputVariablesnohiggnessnotopness_bb2l =
    {
      "mht", "m_Hbb", "m_ll", "Smin_Hww", "m_HHvis", "pT_HH","mT2_top_2particle","m_HH_hme","nBJetLoose","gen_mHH"
    };

  std::vector<std::string> xgbInputVariables_bb2l_nonres =
    {"mht", "m_Hbb", "m_ll", "Smin_Hww", "dR_b1lep1", "dR_b2lep1", "m_HHvis", "pT_HH", "mT2_top_2particle", "m_HH_hme", "logTopness_fixedChi2", "logHiggsness_fixedChi2", "nBJetLoose", "node"
    };

  XGBInterface mva_xgb_bb2l_res(xgbFileName_bb2l_res, xgbInputVariables_bb2l_res);
  XGBInterface mva_xgbnohiggnessnotopness_bb2l(xgbFileNamenohiggnessnotopness_bb2l, xgbInputVariablesnohiggnessnotopness_bb2l);
  XGBInterface mva_xgb_bb2l_nonres(xgbFileName_bb2l_nonres, xgbInputVariables_bb2l_nonres);
  std::map<std::string, double> mvaInputs_XGB;
  std::cout << "declared bdts " << '\n';

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
    std::map<int, EvtHistManager_hh_bb2l*> evt_BMs_;
    //std::map<int, EvtHistManager_hh_bb2l*> evt_scan_;
    std::map<std::string, EvtHistManager_hh_bb2l*> evt_in_categories_;
    GenEvtHistManager* genEvtHistManager_afterCuts_;
    LHEInfoHistManager* lheInfoHistManager_afterCuts_;
    std::map<std::string, LHEInfoHistManager*> lheInfoHistManager_afterCuts_in_categories_;
    EvtYieldHistManager* evtYield_;
    WeightHistManager* weights_;
  };
  std::cout << "selHistManagers " << '\n';
  std::map<int, selHistManagerType*> selHistManagers;
  std::vector<categoryEntryType> categories_evt;
  for ( int type_Hbb = kHbb_undefined; type_Hbb <= kHbb_boosted; ++type_Hbb ) {
    for ( int type_vbf = kVBF_undefined; type_vbf <= kVBF_tagged; ++type_vbf ) {
      if ( !(type_Hbb == kHbb_undefined && type_vbf == kVBF_undefined) ) {
	addCategory_conditionally(categories_evt, categoryEntryType(-1, -1, -1, -1, type_Hbb, type_vbf), evtCategoryNames); // hh_bb2l
      }
      addCategory_conditionally(categories_evt, categoryEntryType(-1, -1,  2, -1, type_Hbb, type_vbf), evtCategoryNames); // hh_2bM2l
      addCategory_conditionally(categories_evt, categoryEntryType(-1, -1,  1,  2, type_Hbb, type_vbf), evtCategoryNames); // hh_1bM1bL2l
      addCategory_conditionally(categories_evt, categoryEntryType(-1, -1,  1, -1, type_Hbb, type_vbf), evtCategoryNames); // hh_1bM2l
      addCategory_conditionally(categories_evt, categoryEntryType( 2, -1, -1, -1, type_Hbb, type_vbf), evtCategoryNames); // hh_bb2e
      addCategory_conditionally(categories_evt, categoryEntryType( 2, -1,  2, -1, type_Hbb, type_vbf), evtCategoryNames); // hh_2bM2e
      addCategory_conditionally(categories_evt, categoryEntryType( 2, -1,  1,  2, type_Hbb, type_vbf), evtCategoryNames); // hh_1bM1bL2e
      addCategory_conditionally(categories_evt, categoryEntryType( 2, -1,  1, -1, type_Hbb, type_vbf), evtCategoryNames); // hh_1bM2e
      addCategory_conditionally(categories_evt, categoryEntryType(-1,  2, -1, -1, type_Hbb, type_vbf), evtCategoryNames); // hh_bb2mu
      addCategory_conditionally(categories_evt, categoryEntryType(-1,  2,  2, -1, type_Hbb, type_vbf), evtCategoryNames); // hh_2bM2mu
      addCategory_conditionally(categories_evt, categoryEntryType(-1,  2,  1,  2, type_Hbb, type_vbf), evtCategoryNames); // hh_1bM1bL2mu
      addCategory_conditionally(categories_evt, categoryEntryType(-1,  2,  1, -1, type_Hbb, type_vbf), evtCategoryNames); // hh_1bM2mu
      addCategory_conditionally(categories_evt, categoryEntryType( 1,  1, -1, -1, type_Hbb, type_vbf), evtCategoryNames); // hh_bb1e1mu
      addCategory_conditionally(categories_evt, categoryEntryType( 1,  1,  2, -1, type_Hbb, type_vbf), evtCategoryNames); // hh_2bM1e1mu
      addCategory_conditionally(categories_evt, categoryEntryType( 1,  1,  1,  2, type_Hbb, type_vbf), evtCategoryNames); // hh_1bM1bL1e1mu
      addCategory_conditionally(categories_evt, categoryEntryType( 1,  1,  1, -1, type_Hbb, type_vbf), evtCategoryNames); // hh_1bM1e1mu
    }
  }
  std::cout << "check that all categories specified in python " << '\n';
  // check that all categories specified in python configuration (by evtCategories) have been added
  vstring undefinedEvtCategories;
  for ( vstring::const_iterator evtCategoryName = evtCategoryNames.begin();
	evtCategoryName != evtCategoryNames.end(); ++evtCategoryName ) {
    if ( (*evtCategoryName) == "hh_bb2l" ) continue; // CV: skip "inclusive" event category, as it is added automatically
    bool isUndefined = true;
    for ( std::vector<categoryEntryType>::const_iterator category_evt = categories_evt.begin();
	  category_evt != categories_evt.end(); ++category_evt ) {
      if ( category_evt->name_ == (*evtCategoryName) ) {
	isUndefined = false;
	break;
      }
    }
    if ( isUndefined ) {
      undefinedEvtCategories.push_back(*evtCategoryName);
    }
  }
  std::cout << "check that all categories specified in python 2" << '\n';
  if ( undefinedEvtCategories.size() >= 1 ) {
    throw cms::Exception("analyze_hh_bb2l")
      << "Invalid Configuration parameter 'evtCategories'. The following event categories are undefined: " << format_vstring(undefinedEvtCategories) << " !!\n";
  }

  std::vector<double> BM_klScan;
  int Nscan = 0;
  std::cout << "Before Entered CX interface " << '\n';
  std::string year = "-1";
  if ( era == kEra_2017 ) year = "2017";
  else throw cms::Exception("HHWeightInterface")
    << "The reweighting is set only to 2017";
  HHWeightInterface HHWeight_calc(BM_klScan, Nscan, year, isDEBUG);
  std::cout << "Number of points being scanned = " << Nscan << "\n ";

  for ( std::vector<leptonGenMatchEntry>::const_iterator leptonGenMatch_definition = leptonGenMatch_definitions.begin();
        leptonGenMatch_definition != leptonGenMatch_definitions.end(); ++leptonGenMatch_definition ) {

    std::string process_and_genMatch = process_string;
    if ( apply_leptonGenMatching ) process_and_genMatch += leptonGenMatch_definition->name_;
    int idxLepton = leptonGenMatch_definition->idx_;

    selHistManagerType* selHistManager = new selHistManagerType();
    selHistManager->electrons_ = new ElectronHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/electrons", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
    selHistManager->electrons_->bookHistograms(fs);
    selHistManager->leadElectron_ = new ElectronHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/leadElectron", histogramDir.data()), era_string, central_or_shift, "minimalHistograms", 0));
    selHistManager->leadElectron_->bookHistograms(fs);
    selHistManager->subleadElectron_ = new ElectronHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/subleadElectron", histogramDir.data()), era_string, central_or_shift, "minimalHistograms", 1));
    selHistManager->subleadElectron_->bookHistograms(fs);
    selHistManager->muons_ = new MuonHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/muons", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
    selHistManager->muons_->bookHistograms(fs);
    selHistManager->leadMuon_ = new MuonHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/leadMuon", histogramDir.data()), era_string, central_or_shift, "minimalHistograms", 0));
    selHistManager->leadMuon_->bookHistograms(fs);
    selHistManager->subleadMuon_ = new MuonHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/subleadMuon", histogramDir.data()), era_string, central_or_shift, "minimalHistograms", 1));
    selHistManager->subleadMuon_->bookHistograms(fs);
    selHistManager->jetsAK4_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/jetsAK4", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
    selHistManager->jetsAK4_->bookHistograms(fs);
    selHistManager->leadJetAK4_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/leadJetAK4", histogramDir.data()), era_string, central_or_shift, "minimalHistograms", 0));
    selHistManager->leadJetAK4_->bookHistograms(fs);
    selHistManager->subleadJetAK4_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/subleadJetAK4", histogramDir.data()), era_string, central_or_shift, "minimalHistograms", 1));
    selHistManager->subleadJetAK4_->bookHistograms(fs);
    selHistManager->jetsAK8_Hbb_ = new JetHistManagerAK8(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/jetsAK8_Hbb", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
    selHistManager->jetsAK8_Hbb_->bookHistograms(fs);
    selHistManager->BJetsAK4_loose_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/BJetsAK4_loose", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
    selHistManager->BJetsAK4_loose_->bookHistograms(fs);
    selHistManager->leadBJetAK4_loose_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/leadBJetAK4_loose", histogramDir.data()), era_string, central_or_shift, "minimalHistograms", 0));
    selHistManager->leadBJetAK4_loose_->bookHistograms(fs);
    selHistManager->subleadBJetAK4_loose_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/subleadBJetAK4_loose", histogramDir.data()), era_string, central_or_shift, "minimalHistograms", 1));
    selHistManager->subleadBJetAK4_loose_->bookHistograms(fs);
    selHistManager->BJetsAK4_medium_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/BJetsAK4_medium", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
    selHistManager->BJetsAK4_medium_->bookHistograms(fs);
    selHistManager->met_ = new MEtHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/met", histogramDir.data()), era_string, central_or_shift));
    selHistManager->met_->bookHistograms(fs);
    selHistManager->metFilters_ = new MEtFilterHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/metFilters", histogramDir.data()), era_string, central_or_shift));
    selHistManager->metFilters_->bookHistograms(fs);
    selHistManager->evt_ = new EvtHistManager_hh_bb2l(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/evt", histogramDir.data()), era_string, central_or_shift, "memDisabled"));
    selHistManager->evt_->bookHistograms(fs);
    if ( isMC_HH_nonres ) {
      for (unsigned int bm_list = 0; bm_list < 13; bm_list++)
      {
        std::string process_and_genMatch_BM = process_string;
        process_and_genMatch_BM += "_BM";
        process_and_genMatch_BM += std::to_string(bm_list);
        process_and_genMatch_BM += "_";
        if ( apply_leptonGenMatching ) process_and_genMatch_BM += leptonGenMatch_definition->name_;
        selHistManager->evt_BMs_[bm_list] = new EvtHistManager_hh_bb2l(makeHistManager_cfg(process_and_genMatch_BM,
          Form("%s/sel/evt", histogramDir.data()), era_string, central_or_shift, "memDisabled"));
        selHistManager->evt_BMs_[bm_list]->bookHistograms(fs);
      }
      /*for (int bm_list = 0; bm_list < Nscan; bm_list++)
      {
        std::string process_and_genMatch_BM = process_string;
        process_and_genMatch_BM += "_scan";
        process_and_genMatch_BM += std::to_string(bm_list);
        process_and_genMatch_BM += "_";
        if ( apply_leptonGenMatching ) process_and_genMatch_BM += leptonGenMatch_definition->name_;
        selHistManager->evt_scan_[bm_list] = new EvtHistManager_hh_bb2l(makeHistManager_cfg(process_and_genMatch_BM,
          Form("%s/sel/evt", histogramDir.data()), era_string, central_or_shift, "memDisabled"));
        selHistManager->evt_scan_[bm_list]->bookHistograms(fs);
      }*/
    }
    if ( isMC ) {
      selHistManager->genEvtHistManager_afterCuts_ = new GenEvtHistManager(makeHistManager_cfg(process_and_genMatch,
        Form("%s/sel/genEvt", histogramDir.data()), era_string, central_or_shift));
      selHistManager->genEvtHistManager_afterCuts_->bookHistograms(fs);
      selHistManager->lheInfoHistManager_afterCuts_ = new LHEInfoHistManager(makeHistManager_cfg(process_and_genMatch,
        Form("%s/sel/lheInfo", histogramDir.data()), era_string, central_or_shift));
      selHistManager->lheInfoHistManager_afterCuts_->bookHistograms(fs);

      if(eventWeightManager)
      {
        selHistManager->genEvtHistManager_afterCuts_->bookHistograms(fs, eventWeightManager);
      }
    }
    for ( std::vector<categoryEntryType>::const_iterator category = categories_evt.begin();
	  category != categories_evt.end(); ++category ) {
      TString histogramDir_category = histogramDir.data();
      histogramDir_category.ReplaceAll("hh_bb2l", category->name_.data());
      selHistManager->evt_in_categories_[category->name_] = new EvtHistManager_hh_bb2l(makeHistManager_cfg(process_and_genMatch,
        Form("%s/sel/evt", histogramDir_category.Data()), era_string, central_or_shift, "memDisabled"));
      selHistManager->evt_in_categories_[category->name_]->bookHistograms(fs);
      if ( isMC ) {
	selHistManager->lheInfoHistManager_afterCuts_in_categories_[category->name_] = new LHEInfoHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/lheInfo", histogramDir_category.Data()), era_string, central_or_shift));
	selHistManager->lheInfoHistManager_afterCuts_in_categories_[category->name_]->bookHistograms(fs);
      }
    }
    edm::ParameterSet cfg_EvtYieldHistManager_sel = makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/evtYield", histogramDir.data()), era_string, central_or_shift);
    cfg_EvtYieldHistManager_sel.addParameter<edm::ParameterSet>("runPeriods", cfg_EvtYieldHistManager);
    cfg_EvtYieldHistManager_sel.addParameter<bool>("isMC", isMC);
    selHistManager->evtYield_ = new EvtYieldHistManager(cfg_EvtYieldHistManager_sel);
    selHistManager->evtYield_->bookHistograms(fs);
    selHistManager->weights_ = new WeightHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/weights", histogramDir.data()), era_string, central_or_shift));
    selHistManager->weights_->bookHistograms(fs, { "genWeight", "pileupWeight", "triggerWeight", "data_to_MC_correction", "fakeRate" });
    selHistManagers[idxLepton] = selHistManager;
  }

  std::cout << "Book BDT filling" << std::endl;
  NtupleFillerBDT<float, int>* bdt_filler = nullptr;
  typedef std::remove_pointer<decltype(bdt_filler)>::type::float_type float_type;
  typedef std::remove_pointer<decltype(bdt_filler)>::type::int_type int_type;

  if ( selectBDT ) {
    bdt_filler = new std::remove_pointer<decltype(bdt_filler)>::type(
      makeHistManager_cfg(process_string, Form("%s/sel/evtntuple", histogramDir.data()), era_string, central_or_shift)
    );
    bdt_filler->register_variable<float_type>(
      "lep1_pt", "lep1_conePt", "lep1_eta",
      "lep2_pt", "lep2_conePt", "lep2_eta",
      "bjet1_pt", "bjet1_eta",
      "bjet2_pt", "bjet2_eta",
      "met", "mht", "met_LD",
      "HT", "STMET",
      "m_Hbb", "dR_Hbb", "dPhi_Hbb", "pT_Hbb",
      "m_ll", "dR_ll", "dPhi_ll", "dEta_ll", "pT_ll",
      "min_dPhi_lepMEt", "max_dPhi_lepMEt",
      "m_Hww", "mT_Hww", "pT_Hww", "Smin_Hww",
      "met_pt_proj",
      "dR_b1lep1", "dR_b1lep2", "dR_b2lep1", "dR_b2lep2",
      "m_HHvis", "pT_HHvis", "dPhi_HHvis",
      "m_HH", "pT_HH", "dPhi_HH", "Smin_HH",
      "mT2_W", "mT2_top_2particle", "mT2_top_3particle",
      "m_HH_hme",
      "logTopness_publishedChi2", "logHiggsness_publishedChi2", "logTopness_fixedChi2", "logHiggsness_fixedChi2",
      "vbf_jet1_pt", "vbf_jet1_eta", "vbf_jet2_pt", "vbf_jet2_eta", "vbf_m_jj", "vbf_dEta_jj",
      "genWeight", "evtWeight",
      "SM_HHWeight",
      "BM1_HHWeight", "BM2_HHWeight", "BM3_HHWeight", "BM4_HHWeight", "BM5_HHWeight", "BM6_HHWeight", "BM7_HHWeight", "BM8_HHWeight", "BM9_HHWeight", "BM10_HHWeight", "BM11_HHWeight", "BM12_HHWeight",
      // X: test points -- for now hardcoded the numbers
      "klm10_HHWeight", "kl1_HHWeight", "kl2p4_HHWeight", "kl2p45_HHWeight", "kl2p455_HHWeight", "kl10_HHWeight",
      "mhh_gen","costS_gen"
    );
    bdt_filler->register_variable<int_type>(
      "nJet", "nBJetLoose", "nBJetMedium",
      "isHbb_boosted",
      "nJet_vbf", "isVBF"
    );
    bdt_filler->bookTree(fs);
  }

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

  while ( inputTree->hasNextEvent() && (! run_lumi_eventSelector || (run_lumi_eventSelector && ! run_lumi_eventSelector -> areWeDone())) ) {
    if ( inputTree -> canReport(reportEvery) ) {
      std::cout << "processing Entry " << inputTree -> getCurrentMaxEventIdx()
                << " or " << inputTree -> getCurrentEventIdx() << " entry in #"
                << (inputTree -> getProcessedFileCount() - 1)
                << " (" << eventInfo
                << ") file (" << selectedEntries << " Entries selected)\n";
    }
    ++analyzedEntries;
    histogram_analyzedEntries->Fill(0.);
    //if ( analyzedEntries > 100 ) break;

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
    std::vector<GenHadTau> genHadTaus;
    std::vector<GenPhoton> genPhotons;
    std::vector<GenJet> genJets;
    std::vector<GenParticle> genHiggses;
    if ( isMC && fillGenEvtHistograms ) {
      if ( genLeptonReader ) {
        genLeptons = genLeptonReader->read();
        for ( std::vector<GenLepton>::const_iterator genLepton = genLeptons.begin();
              genLepton != genLeptons.end(); ++genLepton ) {
          int abs_pdgId = std::abs(genLepton->pdgId());
          if      ( abs_pdgId == 11 ) genElectrons.push_back(*genLepton);
          else if ( abs_pdgId == 13 ) genMuons.push_back(*genLepton);
        }
      }
      if ( genHadTauReader ) {
        genHadTaus = genHadTauReader->read();
      }
      if ( genPhotonReader ) {
        genPhotons = genPhotonReader->read();
      }
      if ( genHiggsReader ) {
        genHiggses = genHiggsReader->read();
      }
      if ( genJetReader ) {
        genJets = genJetReader->read();
      }
      if ( isDEBUG ) {
        printCollection("genLeptons", genLeptons);
        printCollection("genHadTaus", genHadTaus);
        printCollection("genPhotons", genPhotons);
        printCollection("genJets", genJets);
      }
    }

    std::vector<GenParticle> genTauLeptons;
    if ( isMC && apply_DYMCReweighting ) {
      genTauLeptons = genTauLeptonReader->read();
    }

    double evtWeight_inclusive = 1.;
    if ( isMC ) {
      if ( apply_genWeight       ) evtWeight_inclusive *= boost::math::sign(eventInfo.genWeight);
      if ( apply_DYMCReweighting ) evtWeight_inclusive *= dyReweighting->getWeight(genTauLeptons);
      if ( isMC_tH               ) evtWeight_inclusive *= eventInfo.genWeight_tH;
      if ( eventWeightManager    ) evtWeight_inclusive *= eventWeightManager->getWeight();
      lheInfoReader->read();
      evtWeight_inclusive *= lheInfoReader->getWeight_scale(lheScale_option);
      evtWeight_inclusive *= eventInfo.pileupWeight;
      evtWeight_inclusive *= lumiScale;
      genEvtHistManager_beforeCuts->fillHistograms(genElectrons, genMuons, genHadTaus, genPhotons, genJets, evtWeight_inclusive);
      if(eventWeightManager)
      {
        genEvtHistManager_beforeCuts->fillHistograms(eventWeightManager, evtWeight_inclusive);
      }
    }

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

//--- build collections of generator level particles (after some cuts are applied, to save computing time)
    if ( isMC && redoGenMatching && !fillGenEvtHistograms ) {
      if ( genLeptonReader ) {
        genLeptons = genLeptonReader->read();
        for ( std::vector<GenLepton>::const_iterator genLepton = genLeptons.begin();
              genLepton != genLeptons.end(); ++genLepton ) {
          int abs_pdgId = std::abs(genLepton->pdgId());
          if      ( abs_pdgId == 11 ) genElectrons.push_back(*genLepton);
          else if ( abs_pdgId == 13 ) genMuons.push_back(*genLepton);
        }
      }
      if ( genHadTauReader ) {
        genHadTaus = genHadTauReader->read();
      }
      if ( genPhotonReader ) {
        genPhotons = genPhotonReader->read();
      }
      if ( genJetReader ) {
        genJets = genJetReader->read();
      }
    }

//--- match reconstructed to generator level particles
    if ( isMC && redoGenMatching ) {
      muonGenMatcher.addGenLeptonMatch(preselMuons, genLeptons, 0.2);
      muonGenMatcher.addGenHadTauMatch(preselMuons, genHadTaus, 0.2);
      muonGenMatcher.addGenJetMatch(preselMuons, genJets, 0.2);

      electronGenMatcher.addGenLeptonMatch(preselElectrons, genLeptons, 0.2);
      electronGenMatcher.addGenHadTauMatch(preselElectrons, genHadTaus, 0.2);
      electronGenMatcher.addGenPhotonMatch(preselElectrons, genPhotons, 0.2);
      electronGenMatcher.addGenJetMatch(preselElectrons, genJets, 0.2);

      jetGenMatcherAK4.addGenLeptonMatch(cleanedJetsAK4_wrtLeptons, genLeptons, 0.2);
      jetGenMatcherAK4.addGenHadTauMatch(cleanedJetsAK4_wrtLeptons, genHadTaus, 0.2);
      jetGenMatcherAK4.addGenJetMatch(cleanedJetsAK4_wrtLeptons, genJets, 0.2);
    }

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
    const leptonGenMatchEntry& selLepton_genMatch = getLeptonGenMatch(leptonGenMatch_definitions, selLepton_lead, selLepton_sublead);
    int idxSelLepton_genMatch = selLepton_genMatch.idx_;
    assert(idxSelLepton_genMatch != kGen_LeptonUndefined2);

    if ( isMC ) {
      lheInfoReader->read();
    }

//--- compute event-level weight for data/MC correction of b-tagging efficiency and mistag rate
//   (using the method "Event reweighting using scale factors calculated with a tag and probe method",
//    described on the BTV POG twiki https://twiki.cern.ch/twiki/bin/view/CMS/BTagShapeCalibration )
    double evtWeight = 1.;
    double btagWeight = 1.;
    if ( isMC ) {
      evtWeight *= evtWeight_inclusive;
      btagWeight = get_BtagWeight(selJetsAK4);
      evtWeight *= btagWeight;
      if ( isDEBUG ) {
        std::cout << "lumiScale = " << lumiScale << std::endl;
        if ( apply_genWeight ) std::cout << "genWeight = " << boost::math::sign(eventInfo.genWeight) << std::endl;
        std::cout << "pileupWeight = " << eventInfo.pileupWeight << std::endl;
        std::cout << "btagWeight = " << btagWeight << std::endl;
      }
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
    if ( isMC ) {
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
    }

    bool passesTight_lepton_lead = isMatched(*selLepton_lead, tightElectrons) || isMatched(*selLepton_lead, tightMuons);
    bool passesTight_lepton_sublead = isMatched(*selLepton_sublead, tightElectrons) || isMatched(*selLepton_sublead, tightMuons);

    double weight_fakeRate = 1.;
    double prob_fake_lepton_lead = 1.;
    double prob_fake_lepton_sublead = 1.;
    if ( leptonFakeRateInterface ) {
      if ( std::abs(selLepton_lead->pdgId()) == 11 ) {
	prob_fake_lepton_lead = leptonFakeRateInterface->getWeight_e(selLepton_lead->cone_pt(), selLepton_lead->absEta());
      } else if ( std::abs(selLepton_lead->pdgId()) == 13 ) {
	prob_fake_lepton_lead = leptonFakeRateInterface->getWeight_mu(selLepton_lead->cone_pt(), selLepton_lead->absEta());
      } else assert(0);
      if ( std::abs(selLepton_sublead->pdgId()) == 11 ) {
	prob_fake_lepton_sublead = leptonFakeRateInterface->getWeight_e(selLepton_sublead->cone_pt(), selLepton_sublead->absEta());
      } else if ( std::abs(selLepton_sublead->pdgId()) == 13 ) {
	prob_fake_lepton_sublead = leptonFakeRateInterface->getWeight_mu(selLepton_sublead->cone_pt(), selLepton_sublead->absEta());
      } else assert(0);
    }

    if ( applyFakeRateWeights == kFR_enabled ) {
      weight_fakeRate = getWeight_2L(
        prob_fake_lepton_lead, passesTight_lepton_lead,
        prob_fake_lepton_sublead, passesTight_lepton_sublead
      );
      evtWeight *= weight_fakeRate;
    }

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
    const RecoJetAK8* selJetAK8_Hbb = nullptr;
    const RecoJetBase* selJet1_Hbb = nullptr;
    const RecoJetBase* selJet2_Hbb = nullptr;
    int numBJets_loose = 0;
    int numBJets_medium = 0;
    if ( selJetsAK8_Hbb.size() >= 1 ) {
      selJetAK8_Hbb = selJetsAK8_Hbb[0];
      selJet1_Hbb = selJetAK8_Hbb->subJet1();
      selJet2_Hbb = selJetAK8_Hbb->subJet2();
      assert(selJet1_Hbb && selJet2_Hbb);
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

    // select VBF jet candidates
    std::vector<const RecoJet*> cleanedJetsAK4_vbf;
    if ( selJetAK8_Hbb ) {
      std::vector<const RecoJetAK8*> overlaps = { selJetAK8_Hbb };
      cleanedJetsAK4_vbf = jetCleanerAK4_dR12(cleanedJetsAK4_wrtLeptons, overlaps);
    } else {
      cleanedJetsAK4_vbf = jetCleanerAK4_dR08(cleanedJetsAK4_wrtLeptons, selJets_Hbb);
    }
    std::vector<const RecoJet*> selJetsAK4_vbf = jetSelectorAK4_vbf(cleanedJetsAK4_vbf, isHigherPt);

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

    bool failsSignalRegionVeto = false;
    if ( isMCClosure_e || isMCClosure_m ) {
      bool applySignalRegionVeto = (isMCClosure_e && countFakeElectrons(selLeptons) >= 1) || (isMCClosure_m && countFakeMuons(selLeptons) >= 1);
      if ( applySignalRegionVeto && tightLeptons.size() >= 2 ) failsSignalRegionVeto = true;
    } else if ( electronSelection == kFakeable || muonSelection == kFakeable ) {
      if ( tightLeptons.size() >= 2 ) failsSignalRegionVeto = true;
    }
    if ( failsSignalRegionVeto ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS overlap w/ the SR: "
	  "# tight leptons = " << tightLeptons.size() << " >= 2\n"
	;
        printCollection("tightLeptons", tightLeptons);
      }
      continue; // CV: avoid overlap with signal region
    }
    cutFlowTable.update("signal region veto", evtWeight);
    cutFlowHistManager->fillHistograms("signal region veto", evtWeight);

    std::vector<double> WeightBM; // weights to do histograms for BMs
    std::vector<double> Weight_klScan; // weights to do histograms for BMs
    double mhh_gen = 0.;
    double costS_gen = 0.;
    double HHWeight = 1.0; // X: for the SM point -- the point explicited on this code
    if ( isMC_HH_nonres )
    {
      if ( isDEBUG ) std::cout << "===================================\n";
      if ( genHiggses.size() == 2 )
      {
        mhh_gen = ( genHiggses[0].p4() + genHiggses[1].p4() ).mass();
        costS_gen = comp_cosThetaS( genHiggses[0].p4() , genHiggses[1].p4() );
        if (mhh_gen > 247.)
        {
          HHWeight_calc(mhh_gen, costS_gen, WeightBM, Weight_klScan, isDEBUG);
          evtWeight_inclusive *= WeightBM[0]; // SM by default

          if ( isDEBUG ) {
            std::cout<< "genHiggses weights " << genHiggses.size() << " mhh = " << mhh_gen << " : cost " << costS_gen << " : weight = " << HHWeight << std::endl;
            std::cout << "Calculated " << WeightBM.size() << "BM weights - SM (BM = 0) + 12 shape benchmarks \n";
            for (unsigned int bm_list = 0; bm_list < WeightBM.size(); bm_list++)
            {std::cout << "BM = " << bm_list << "; Weight = " <<  WeightBM[bm_list] << " \n";}
            std::cout << "\n";
            ///////////
            std::cout << "Calculated " << Weight_klScan.size() << " scan weights\n";
            for (unsigned int bm_list = 0; bm_list < Weight_klScan.size(); bm_list++)
            {std::cout << "line = " << bm_list << "; Weight = " <<  Weight_klScan[bm_list] << " \n";}
            std::cout << "\n";
          }

        } else throw cms::Exception("analyze_hh_bb2l")
          << "mhh_gen = " << mhh_gen << " < 247 GeV; Check that this is realy a file for HH production !!\n";
      }
      evtWeight_inclusive *= HHWeight;
    }


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
    double dEta_ll = TMath::Abs(selLeptonP4_lead.eta() - selLeptonP4_sublead.eta());
    double pT_ll = llP4.pt();
    double dPhi_lep1MEt = TMath::Abs(deltaPhi(selLeptonP4_lead.phi(), metP4.phi()));
    double dPhi_lep2MEt = TMath::Abs(deltaPhi(selLeptonP4_sublead.phi(), metP4.phi()));
    double min_dPhi_lepMEt = TMath::Min(dPhi_lep1MEt, dPhi_lep2MEt);
    double max_dPhi_lepMEt = TMath::Max(dPhi_lep1MEt, dPhi_lep2MEt);
    Particle::LorentzVector HwwP4 = selLeptonP4_lead + selLeptonP4_sublead + metP4;
    double m_Hww = HwwP4.mass();
    double mT_Hww = TMath::Sqrt(2.*llP4.pt()*metP4.pt()*(1. - TMath::Cos(deltaPhi(llP4.phi(), metP4.phi())))); // suggested in section 4.4 of arXiv:1212.5581
    double pT_Hww = HwwP4.pt();
    double Smin_Hww = comp_Smin(selLeptonP4_lead + selLeptonP4_sublead, metP4.px(), metP4.py());
    double met_pt_proj; // suggested in section 4.4 of arXiv:1212.5581
    if ( min_dPhi_lepMEt < 0.5*TMath::Pi() ) met_pt_proj = metP4.pt()*TMath::Sin(min_dPhi_lepMEt);
    else met_pt_proj = metP4.pt();
    double dR_b1lep1 = deltaR(selJetP4_Hbb_lead, selLeptonP4_lead);
    double dR_b1lep2 = deltaR(selJetP4_Hbb_lead, selLeptonP4_sublead);
    double dR_b2lep1 = deltaR(selJetP4_Hbb_sublead, selLeptonP4_lead);
    double dR_b2lep2 = deltaR(selJetP4_Hbb_sublead, selLeptonP4_sublead);
    Particle::LorentzVector HHvisP4 = HbbP4 + selLeptonP4_lead + selLeptonP4_sublead;
    double m_HHvis = HHvisP4.mass();
    double pT_HHvis = HHvisP4.pt();
    double dPhi_HHvis = TMath::Abs(deltaPhi(HbbP4.phi(), (selLeptonP4_lead + selLeptonP4_sublead).phi()));
    Particle::LorentzVector HHP4 = HbbP4 + HwwP4;
    double m_HH = HHP4.mass();
    double pT_HH = HHP4.pt();
    double Smin_HH = comp_Smin(HHvisP4, metP4.px(), metP4.py());
    double dR_HH = deltaR(HbbP4, HwwP4);
    double dPhi_HH = TMath::Abs(deltaPhi(HbbP4.phi(), HwwP4.phi()));
    /*mT2_2particle mT2Algo_2particle;
    mT2Algo_2particle(
      selLeptonP4_lead.px(), selLeptonP4_lead.py(), selLeptonP4_lead.mass(),
      selLeptonP4_sublead.px(), selLeptonP4_sublead.py(), selLeptonP4_sublead.mass(),
      metP4.px(), metP4.py(), 0.);*/
    double mT2_W = 1.0; //mT2Algo_2particle.get_min_mT2();
    int mT2_W_step = 1.0; //mT2Algo_2particle.get_min_step();
    //std::cout << "mT2_W = " << mT2_W << " (found @ step #" << mT2_W_step << ")" << std::endl;
    //double cSumPx = selLeptonP4_lead.px() + selLeptonP4_sublead.px() + metP4.px();
    //double cSumPy = selLeptonP4_lead.py() + selLeptonP4_sublead.py() + metP4.py();
    /*mT2Algo_2particle(
      selJetP4_Hbb_lead.px(), selJetP4_Hbb_lead.py(), selJetP4_Hbb_lead.mass(),
      selJetP4_Hbb_sublead.px(), selJetP4_Hbb_sublead.py(), selJetP4_Hbb_sublead.mass(),
      cSumPx, cSumPy, wBosonMass);*/
    double mT2_top_2particle = 1.0; //mT2Algo_2particle.get_min_mT2();
    int mT2_top_2particle_step = 1.0; //mT2Algo_2particle.get_min_step();
    //std::cout << "mT2_top_2particle = " << mT2_top_2particle << " (found @ step #" << mT2_top_2particle_step << ")" << std::endl;
    /*mT2_3particle mT2Algo_3particle;
    mT2Algo_3particle(
      selJetP4_Hbb_lead.px(), selJetP4_Hbb_lead.py(), selJetP4_Hbb_lead.mass(),
      selJetP4_Hbb_sublead.px(), selJetP4_Hbb_sublead.py(), selJetP4_Hbb_sublead.mass(),
      selLeptonP4_lead.px(), selLeptonP4_lead.py(), selLeptonP4_lead.mass(),
      selLeptonP4_sublead.px(), selLeptonP4_sublead.py(), selLeptonP4_sublead.mass(),
      metP4.px(), metP4.py(), 0.);*/
    double mT2_top_3particle_permutation1 = 1.0; // mT2Algo_3particle.get_min_mT2();
    int mT2_top_3particle_permutation1_step = 1.0; // mT2Algo_3particle.get_min_step();
    /*mT2Algo_3particle(
      selJetP4_Hbb_lead.px(), selJetP4_Hbb_lead.py(), selJetP4_Hbb_lead.mass(),
      selJetP4_Hbb_sublead.px(), selJetP4_Hbb_sublead.py(), selJetP4_Hbb_sublead.mass(),
      selLeptonP4_sublead.px(), selLeptonP4_sublead.py(), selLeptonP4_sublead.mass(),
      selLeptonP4_lead.px(), selLeptonP4_lead.py(), selLeptonP4_lead.mass(),
      metP4.px(), metP4.py(), 0.);*/
    double mT2_top_3particle_permutation2 = 1.0; //mT2Algo_3particle.get_min_mT2();
    double mT2_top_3particle_permutation2_step = 1.0; //mT2Algo_3particle.get_min_step();
    double mT2_top_3particle = -1.;
    double mT2_top_3particle_step = -1;
    if ( mT2_top_3particle_permutation1 <= mT2_top_3particle_permutation2 ) {
      mT2_top_3particle = mT2_top_3particle_permutation1;
      mT2_top_3particle_step = mT2_top_3particle_permutation1_step;
    } else {
      mT2_top_3particle = mT2_top_3particle_permutation2;
      mT2_top_3particle_step = mT2_top_3particle_permutation2_step;
    }
    //std::cout << "mT2_top_3particle:"
    //	        << " permutation1 = " << mT2_top_3particle_permutation1 << " (found @ step #" << mT2_top_3particle_permutation1_step << "),"
    //	        << " permutation2 = " << mT2_top_3particle_permutation2 << " (found @ step #" << mT2_top_3particle_permutation2_step << "),"
    //	        << " min = " << mT2_top_3particle << " (found @ step #" << mT2_top_3particle_step << ")" << std::endl;
    //Higgsness algoHiggsness_publishedChi2(Higgsness::kPublishedChi2);
    //algoHiggsness_publishedChi2.fit(selLeptonP4_lead, selLeptonP4_sublead, metP4.px(), metP4.py());
    double logHiggsness_publishedChi2 = -99.;
    /*if ( algoHiggsness_publishedChi2.isValidSolution() ) {
      logHiggsness_publishedChi2 = algoHiggsness_publishedChi2.logHiggsness();
    }
    Topness algoTopness_publishedChi2(Topness::kPublishedChi2);
    algoTopness_publishedChi2.fit(selLeptonP4_lead, selLeptonP4_sublead, selJetP4_Hbb_lead, selJetP4_Hbb_sublead, metP4.px(), metP4.py());*/
    double logTopness_publishedChi2 = -99.;
    /*if ( algoTopness_publishedChi2.isValidSolution() ) {
      logTopness_publishedChi2 = algoTopness_publishedChi2.logTopness();
    }
    Higgsness algoHiggsness_fixedChi2(Higgsness::kFixedChi2);
    algoHiggsness_fixedChi2.fit(selLeptonP4_lead, selLeptonP4_sublead, metP4.px(), metP4.py());*/
    double logHiggsness_fixedChi2 = -99.;
    /*if ( algoHiggsness_fixedChi2.isValidSolution() ) {
      logHiggsness_fixedChi2 = algoHiggsness_fixedChi2.logHiggsness();
    }
    Topness algoTopness_fixedChi2(Topness::kFixedChi2);
    algoTopness_fixedChi2.fit(selLeptonP4_lead, selLeptonP4_sublead, selJetP4_Hbb_lead, selJetP4_Hbb_sublead, metP4.px(), metP4.py());*/
    double logTopness_fixedChi2 = -99.;
    /*if ( algoTopness_fixedChi2.isValidSolution() ) {
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
    const int iterations = 100000;
    //const int iterations = 20000;
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
      iterations, RefPDFfile.fullPath(), useMET, bjetrescaleAlgo, metcorrection);*/
    double m_HH_hme = -1.;
    /*bool hme_isValidSolution = hmeAlgo.runheavyMassEstimator();
    if ( hme_isValidSolution ) {
      TH1F hmeHist = hmeAlgo.getheavyMassEstimatorh2();
      m_HH_hme = hmeHist.GetXaxis()->GetBinCenter(hmeHist.GetMaximumBin());
    }
    clock.Stop("hmeAlgo");
    */
    double hmeCpuTime = clock.GetCpuTime("hmeAlgo");
    //std::cout << "m_HH_hme = " << m_HH_hme << std::endl;
    //---------------------------------------------------------------------------

    const RecoJet* selJet_vbf_lead = nullptr;
    const RecoJet* selJet_vbf_sublead = nullptr;
    double vbf_dEta_jj = -1.;
    double vbf_m_jj = -1.;
    bool isVBF = false;
    for ( std::vector<const RecoJet*>::const_iterator selJet1_vbf = selJetsAK4_vbf.begin();
          selJet1_vbf != selJetsAK4_vbf.end(); ++selJet1_vbf ) {
      for ( std::vector<const RecoJet*>::const_iterator selJet2_vbf = selJet1_vbf + 1;
	    selJet2_vbf != selJetsAK4_vbf.end(); ++selJet2_vbf ) {
	double dEta_jj = TMath::Abs((*selJet1_vbf)->eta() - (*selJet2_vbf)->eta());
	double m_jj = ((*selJet1_vbf)->p4() + (*selJet2_vbf)->p4()).mass();
	if ( dEta_jj > 4. && m_jj > 500. ) {
	  if ( m_jj > vbf_m_jj ) { // CV: in case of ambiguity, take the jet pair of highest mass
	    selJet_vbf_lead = (*selJet1_vbf);
	    selJet_vbf_sublead = (*selJet2_vbf);
	    vbf_dEta_jj = dEta_jj;
	    vbf_m_jj = m_jj;
	  }
	  isVBF = true;
	}
      }
    }
    double vbf_jet1_pt = -1.;
    double vbf_jet1_eta = 0.;
    if ( selJet_vbf_lead ) {
      vbf_jet1_pt = selJet_vbf_lead->pt();
      vbf_jet1_eta = selJet_vbf_lead->eta();
    }
    double vbf_jet2_pt = -1.;
    double vbf_jet2_eta = 0.;
    if ( selJet_vbf_sublead ) {
      vbf_jet2_pt = selJet_vbf_sublead->pt();
      vbf_jet2_eta = selJet_vbf_sublead->eta();
    }
    mvaInputs_XGB["mht"] = mhtP4.pt();
    mvaInputs_XGB["m_Hbb"] = m_Hbb;
    mvaInputs_XGB["m_ll"] = m_ll;
    mvaInputs_XGB["Smin_Hww"] = Smin_Hww;
    mvaInputs_XGB["m_HHvis"] = m_HHvis;
    mvaInputs_XGB["pT_HH"] = pT_HH;
    mvaInputs_XGB["mT2_top_2particle"] = mT2_top_2particle;
    mvaInputs_XGB["m_HH_hme"] = m_HH_hme;
    mvaInputs_XGB["logTopness_fixedChi2"] = logTopness_fixedChi2;
    mvaInputs_XGB["logHiggsness_fixedChi2"] = logHiggsness_fixedChi2;
    mvaInputs_XGB["nBJetLoose"] = selBJetsAK4_loose.size();
    mvaInputs_XGB["gen_mHH"] = 300;
    double mvaoutput_bb2l300 = mva_xgb_bb2l_res(mvaInputs_XGB);
    mvaInputs_XGB["gen_mHH"] = 400;
    double mvaoutput_bb2l400 = mva_xgb_bb2l_res(mvaInputs_XGB);
    mvaInputs_XGB["gen_mHH"] = 750;
    double mvaoutput_bb2l750 = mva_xgb_bb2l_res(mvaInputs_XGB);

    double mvaoutputnohiggnessnotopness_bb2l300 = mva_xgbnohiggnessnotopness_bb2l(mvaInputs_XGB);
    mvaInputs_XGB["gen_mHH"] = 400;
    double mvaoutputnohiggnessnotopness_bb2l400 = mva_xgbnohiggnessnotopness_bb2l(mvaInputs_XGB);
    mvaInputs_XGB["gen_mHH"] = 750;
    double mvaoutputnohiggnessnotopness_bb2l750 = mva_xgbnohiggnessnotopness_bb2l(mvaInputs_XGB);
    mvaInputs_XGB.clear();

    double mvaoutput_bb2l_node3 = 1.0; //mva_xgb_bb2l_nonres(mvaInputs_XGB);
    double mvaoutput_bb2l_node7 = 1.0; //mva_xgb_bb2l_nonres(mvaInputs_XGB);
    double mvaoutput_bb2l_sm = 1.0; //mva_xgb_bb2l_nonres(mvaInputs_XGB);


//--- fill histograms with events passing final selection
    selHistManagerType* selHistManager = selHistManagers[idxSelLepton_genMatch];
    assert(selHistManager != 0);
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
      nullptr, -1.,
      nullptr, -1.,
      mvaoutput_bb2l300, mvaoutput_bb2l400, mvaoutput_bb2l750,
      mvaoutputnohiggnessnotopness_bb2l300, mvaoutputnohiggnessnotopness_bb2l400, mvaoutputnohiggnessnotopness_bb2l750, mvaoutput_bb2l_node3, mvaoutput_bb2l_node7, mvaoutput_bb2l_sm,
      evtWeight);
    if ( isMC_HH_nonres ) {
      for (unsigned int bm_list = 0; bm_list < WeightBM.size(); bm_list++)
      {
        double evtWeight0 = evtWeight * WeightBM[bm_list]/HHWeight;
        selHistManager->evt_BMs_[bm_list]->fillHistograms(
          selElectrons.size(),
          selMuons.size(),
          selJetsAK4.size(),
          selBJetsAK4_loose.size(),
          selBJetsAK4_medium.size(),
          nullptr, -1.,
          nullptr, -1.,
          mvaoutput_bb2l300, mvaoutput_bb2l400, mvaoutput_bb2l750,
          mvaoutputnohiggnessnotopness_bb2l300, mvaoutputnohiggnessnotopness_bb2l400, mvaoutputnohiggnessnotopness_bb2l750, mvaoutput_bb2l_node3, mvaoutput_bb2l_node7, mvaoutput_bb2l_sm,
          evtWeight0);
      }
      /*for (unsigned int bm_list = 0; bm_list < Weight_klScan.size(); bm_list++)
      {
        double evtWeight0 = evtWeight * Weight_klScan[bm_list]/HHWeight;
        selHistManager->evt_scan_[bm_list]->fillHistograms(
          selElectrons.size(),
          selMuons.size(),
          selJetsAK4.size(),
          selBJetsAK4_loose.size(),
          selBJetsAK4_medium.size(),
          nullptr, -1.,
          nullptr, -1.,
          mvaoutput_bb2l300, mvaoutput_bb2l400, mvaoutput_bb2l750,
          mvaoutputnohiggnessnotopness_bb2l300, mvaoutputnohiggnessnotopness_bb2l400, mvaoutputnohiggnessnotopness_bb2l750, mvaoutput_bb2l_node3, mvaoutput_bb2l_node7, mvaoutput_bb2l_sm,
          evtWeight0);
      }*/
    }
    if ( isMC ) {
      selHistManager->genEvtHistManager_afterCuts_->fillHistograms(genElectrons, genMuons, genHadTaus, genPhotons, genJets, evtWeight_inclusive);
      selHistManager->lheInfoHistManager_afterCuts_->fillHistograms(*lheInfoReader, evtWeight);

      if(eventWeightManager)
      {
        selHistManager->genEvtHistManager_afterCuts_->fillHistograms(eventWeightManager, evtWeight_inclusive);
      }
    }
    selHistManager->evtYield_->fillHistograms(eventInfo, evtWeight);
    selHistManager->weights_->fillHistograms("genWeight", eventInfo.genWeight);
    selHistManager->weights_->fillHistograms("pileupWeight", eventInfo.pileupWeight);
    selHistManager->weights_->fillHistograms("triggerWeight", triggerWeight);
    selHistManager->weights_->fillHistograms("data_to_MC_correction", weight_data_to_MC_correction);
    selHistManager->weights_->fillHistograms("fakeRate", weight_fakeRate);

    int numElectrons = 0;
    if ( selLepton_lead_type    == kElectron ) ++numElectrons;
    if ( selLepton_sublead_type == kElectron ) ++numElectrons;
    int numMuons = 0;
    if ( selLepton_lead_type    == kMuon     ) ++numMuons;
    if ( selLepton_sublead_type == kMuon     ) ++numMuons;
    int type_Hbb = ( selJetAK8_Hbb ) ? kHbb_boosted : kHbb_resolved;
    int type_vbf = ( isVBF         ) ?  kVBF_tagged : kVBF_nottagged;
    for ( std::vector<categoryEntryType>::const_iterator category = categories_evt.begin();
	  category != categories_evt.end(); ++category ) {
      if ( (category->numElectrons_    ==             -1 || numElectrons    == category->numElectrons_)    &&
	   (category->numMuons_        ==             -1 || numMuons        == category->numMuons_)        &&
	   (category->numBJets_medium_ ==             -1 || numBJets_medium == category->numBJets_medium_) &&
	   (category->numBJets_loose_  ==             -1 || numBJets_loose  == category->numBJets_loose_)  &&
	   (category->type_Hbb_        == kHbb_undefined || type_Hbb        == category->type_Hbb_)        &&
	   (category->type_vbf_        == kVBF_undefined || type_vbf        == category->type_vbf_)        ) {
	if ( selHistManager->evt_in_categories_.find(category->name_) != selHistManager->evt_in_categories_.end() ) {
	  selHistManager->evt_in_categories_[category->name_]->fillHistograms(
            selElectrons.size(),
	    selMuons.size(),
	    selJetsAK4.size(),
	    selBJetsAK4_loose.size(),
	    selBJetsAK4_medium.size(),
	    nullptr, -1.,
	    nullptr, -1.,
	    mvaoutput_bb2l300, mvaoutput_bb2l400, mvaoutput_bb2l750,
	    mvaoutputnohiggnessnotopness_bb2l300, mvaoutputnohiggnessnotopness_bb2l400, mvaoutputnohiggnessnotopness_bb2l750, mvaoutput_bb2l_node3, mvaoutput_bb2l_node7, mvaoutput_bb2l_sm,
	    evtWeight);
	}
	if ( selHistManager->lheInfoHistManager_afterCuts_in_categories_.find(category->name_) != selHistManager->lheInfoHistManager_afterCuts_in_categories_.end() ) {
	  selHistManager->lheInfoHistManager_afterCuts_in_categories_[category->name_]->fillHistograms(*lheInfoReader, evtWeight);
	}
      }
    }

    if ( selEventsFile ) {
      (*selEventsFile) << eventInfo.run << ':' << eventInfo.lumi << ':' << eventInfo.event << '\n';
    }

    const bool isGenMatched = isMC &&
      ((apply_leptonGenMatching && selLepton_genMatch.numGenMatchedJets_ == 0) || ! apply_leptonGenMatching)
    ;

    if ( bdt_filler ) {
      bdt_filler -> operator()({ eventInfo.run, eventInfo.lumi, eventInfo.event })
          ("lep1_pt",                       selLepton_lead->pt())
          ("lep1_conePt",                   comp_lep1_conePt(*selLepton_lead))
          ("lep1_eta",                      selLepton_lead->eta())
          ("lep2_pt",                       selLepton_sublead->pt())
          ("lep2_conePt",                   comp_lep2_conePt(*selLepton_sublead))
          ("lep2_eta",                      selLepton_sublead->eta())
          ("bjet1_pt",                      selJetP4_Hbb_lead.pt())
          ("bjet1_eta",                     selJetP4_Hbb_lead.eta())
          ("bjet2_pt",                      selJetP4_Hbb_sublead.pt())
          ("bjet2_eta",                     selJetP4_Hbb_sublead.eta())
          ("met",                           metP4.pt())
          ("mht",                           mhtP4.pt())
          ("met_LD",                        met_LD)
          ("HT",                            HT)
          ("STMET",                         STMET)
          ("m_Hbb",                         m_Hbb)
          ("dR_Hbb",                        dR_Hbb)
          ("dPhi_Hbb",                      dPhi_Hbb)
          ("pT_Hbb",                        pT_Hbb)
          ("m_ll",                          m_ll)
          ("dR_ll",                         dR_ll)
          ("dPhi_ll",                       dPhi_ll)
          ("dEta_ll",                       dEta_ll)
          ("pT_ll",                         pT_ll)
	  ("min_dPhi_lepMEt",               min_dPhi_lepMEt)
	  ("max_dPhi_lepMEt",               max_dPhi_lepMEt)
          ("m_Hww",                         m_Hww)
          ("mT_Hww",                        mT_Hww)
          ("Smin_Hww",                      Smin_Hww)
          ("pT_Hww",                        pT_Hww)
	  ("met_pt_proj",                   met_pt_proj)
	  ("dR_b1lep1",                     dR_b1lep1)
          ("dR_b1lep2",                     dR_b1lep2)
          ("dR_b2lep1",                     dR_b2lep1)
          ("dR_b2lep2",                     dR_b2lep2)
          ("m_HHvis",                       m_HHvis)
          ("pT_HHvis",                      pT_HHvis)
          ("dPhi_HHvis",                    dPhi_HHvis)
          ("m_HH",                          m_HH)
          ("pT_HH",                         pT_HH)
          ("dPhi_HH",                       dPhi_HH)
  	  ("Smin_HH",                       Smin_HH)
          ("mT2_W",                         mT2_W)
          ("mT2_top_2particle",             mT2_top_2particle)
          ("mT2_top_3particle",             mT2_top_3particle)
          ("m_HH_hme",                      m_HH_hme)
          ("logTopness_publishedChi2",      logTopness_publishedChi2)
          ("logHiggsness_publishedChi2",    logHiggsness_publishedChi2)
          ("logTopness_fixedChi2",          logTopness_fixedChi2)
          ("logHiggsness_fixedChi2",        logHiggsness_fixedChi2)
          ("vbf_jet1_pt",                   vbf_jet1_pt)
          ("vbf_jet1_eta",                  vbf_jet1_eta)
          ("vbf_jet2_pt",                   vbf_jet2_pt)
	  ("vbf_jet2_eta",                  vbf_jet2_eta)
          ("vbf_dEta_jj",                   vbf_dEta_jj)
          ("vbf_m_jj",                      vbf_m_jj)
          ("genWeight",                     eventInfo.genWeight)
          ("evtWeight",                     evtWeight)
          ("nJet",                          comp_n_jet25_recl(selJetsAK4))
          ("nBJetLoose",                    selBJetsAK4_loose.size())
          ("nBJetMedium",                   selBJetsAK4_medium.size())
          ("nJet_vbf",                      selJetsAK4_vbf.size())
	  ("isHbb_boosted",                 type_Hbb == kHbb_boosted)
          ("isVBF",                         isVBF)
          ("SM_HHWeight",                   WeightBM[0])
          ("BM1_HHWeight",                  WeightBM[1])
          ("BM2_HHWeight",                  WeightBM[2])
          ("BM3_HHWeight",                  WeightBM[3])
          ("BM4_HHWeight",                  WeightBM[4])
          ("BM5_HHWeight",                  WeightBM[5])
          ("BM6_HHWeight",                  WeightBM[6])
          ("BM7_HHWeight",                  WeightBM[7])
          ("BM8_HHWeight",                  WeightBM[8])
          ("BM9_HHWeight",                  WeightBM[9])
          ("BM10_HHWeight",                 WeightBM[10])
          ("BM11_HHWeight",                 WeightBM[11])
          ("BM12_HHWeight",                 WeightBM[12])
          // X: test points -- for now hardcoded the numbers
          ("klm10_HHWeight",                Weight_klScan[5])
          ("kl1_HHWeight",                  Weight_klScan[11])
          ("kl2p4_HHWeight",                Weight_klScan[13])
          ("kl10_HHWeight",                 Weight_klScan[17])
          ("mhh_gen",                       mhh_gen)
          ("costS_gen",                     costS_gen)
        .fill()
      ;
    }

    if(snm)
    {
      snm->read(eventInfo);
      snm->read({
        triggers_1e, triggers_1mu, triggers_2e, triggers_1e1mu, triggers_2mu,
      });

      snm->read(preselMuons);
      snm->read(preselElectrons);
      snm->read(selJetsAK4);
      snm->read(selJetsAK8_Hbb, false);

      snm->read(eventInfo.pileupWeight,                 FloatVariableType_bbww::PU_weight);
      snm->read(boost::math::sign(eventInfo.genWeight), FloatVariableType_bbww::MC_weight);
      snm->read(met.pt(),                               FloatVariableType_bbww::PFMET);
      snm->read(met.phi(),                              FloatVariableType_bbww::PFMETphi);

      if((sync_requireGenMatching && isGenMatched) || ! sync_requireGenMatching)
      {
        snm->fill();
      }
      else
      {
        snm->reset();
      }
    }

    ++selectedEntries;
    selectedEntries_weighted += evtWeight;
    histogram_selectedEntries->Fill(0.);
  }

  if(snm)
  {
    snm->write();
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

  std::cout << "sel. Entries by gen. matching:" << std::endl;
  for ( std::vector<leptonGenMatchEntry>::const_iterator leptonGenMatch_definition = leptonGenMatch_definitions.begin();
        leptonGenMatch_definition != leptonGenMatch_definitions.end(); ++leptonGenMatch_definition ) {

    std::string process_and_genMatch = process_string;
    if ( apply_leptonGenMatching ) process_and_genMatch += leptonGenMatch_definition->name_;

    int idxLepton = leptonGenMatch_definition->idx_;

    const TH1* histogram_EventCounter = selHistManagers[idxLepton]->evt_->getHistogram_EventCounter();
    std::cout << " " << process_and_genMatch << " = " << histogram_EventCounter->GetEntries() << " (weighted = " << histogram_EventCounter->Integral() << ")" << std::endl;
  }
  std::cout << std::endl;

  delete dataToMCcorrectionInterface;

  delete leptonFakeRateInterface;

  delete run_lumi_eventSelector;

  delete selEventsFile;

  delete muonReader;
  delete electronReader;
  delete jetReaderAK4;
  delete jetReaderAK8;
  delete metReader;
  delete metFilterReader;
  delete genLeptonReader;
  delete genHadTauReader;
  delete genPhotonReader;
  delete genJetReader;
  delete genHiggsReader;
  delete genTauLeptonReader;
  delete lheInfoReader;

  delete genEvtHistManager_beforeCuts;
  delete eventWeightManager;

  hltPaths_delete(triggers_1e);
  hltPaths_delete(triggers_2e);
  hltPaths_delete(triggers_1mu);
  hltPaths_delete(triggers_2mu);
  hltPaths_delete(triggers_1e1mu);

  delete inputTree;
  delete snm;

  clock.Show("analyze_hh_bb2l");

  return EXIT_SUCCESS;
}
