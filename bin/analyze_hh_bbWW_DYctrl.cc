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
#include "tthAnalysis/HiggsToTauTau/interface/TriggerHistManager.h" // TriggerHistManager
#include "tthAnalysis/HiggsToTauTau/interface/EvtYieldHistManager.h" // EvtYieldHistManager
#include "tthAnalysis/HiggsToTauTau/interface/CutFlowTableHistManager.h" // CutFlowTableHistManager
#include "tthAnalysis/HiggsToTauTau/interface/WeightHistManager.h" // WeightHistManager
#include "tthAnalysis/HiggsToTauTau/interface/GenEvtHistManager.h" // GenEvtHistManager
#include "tthAnalysis/HiggsToTauTau/interface/LHEInfoHistManager.h" // LHEInfoHistManager
#include "tthAnalysis/HiggsToTauTau/interface/leptonTypes.h" // getLeptonType, kElectron, kMuon
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // getBTagWeight_option, getHadTau_genPdgId, isHigherPt, isMatched
#include "tthAnalysis/HiggsToTauTau/interface/leptonGenMatchingAuxFunctions.h" // getLeptonGenMatch_definitions_2lepton, getLeptonGenMatch_string, getLeptonGenMatch_int
#include "tthAnalysis/HiggsToTauTau/interface/fakeBackgroundAuxFunctions.h"
#include "tthAnalysis/HiggsToTauTau/interface/mvaInputVariables.h" // comp_lep1_conePt
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
#include "tthAnalysis/HiggsToTauTau/interface/generalAuxFunctions.h" // format_vstring

#include "hhAnalysis/bbww/interface/EvtHistManager_hh_bbWW_DYctrl.h" // EvtHistManager_hh_bbWW_DYctrl
#include "hhAnalysis/bbww/interface/RecoJetCollectionSelectorAK8_bbWW_Hbb.h" // RecoJetSelectorAK8_bbWW_Hbb
#include "tthAnalysis/HiggsToTauTau/interface/mT2_2particle.h" // mT2_2particle
#include "tthAnalysis/HiggsToTauTau/interface/mT2_3particle.h" // mT2_3particle
#include "tthAnalysis/HiggsToTauTau/interface/Higgsness.h" // Higgsness
#include "tthAnalysis/HiggsToTauTau/interface/Topness.h" // Topness

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

enum { kFR_disabled, kFR_enabled };

const double wBosonMass = 80.379; // GeV

enum { kHbb_undefined, kHbb_resolved, kHbb_boosted };
enum { kVBF_undefined, kVBF_nottagged, kVBF_tagged };
enum { kDilepton, kDielectron, kDimuon };

struct categoryEntryType
{
  categoryEntryType(int numElectrons, int numMuons, int numBJets_medium, int numBJets_loose, int minNumJets, int maxNumJets, int type_Hbb, int type_vbf)
    : numElectrons_(numElectrons)
    , numMuons_(numMuons)
    , minNumJets_(minNumJets)
    , maxNumJets_(maxNumJets)
    , numBJets_medium_(numBJets_medium)
    , numBJets_loose_(numBJets_loose)
    , type_Hbb_(type_Hbb)
    , type_vbf_(type_vbf)
  {
    //std::cout << "<categoryEntryType>:" << std::endl;
    //std::cout << " numElectrons = " << numElectrons << std::endl;
    //std::cout << " numMuons = " << numMuons << std::endl;
    //std::cout << " numBJets: loose = " << numBJets_loose << ", medium = " << numBJets_medium << std::endl;
    //std::cout << " numJets: min = " << minNumJets << ", max = " << maxNumJets << std::endl;
    //std::cout << " type_Hbb = " << type_Hbb << std::endl;
    //std::cout << " type_vbf = " << type_vbf << std::endl;
    name_ = "bbWW_";
    if      ( numBJets_medium_ >= 2                         ) name_ += "2bM";
    else if ( numBJets_medium_ >= 1 && numBJets_loose_ >= 2 ) name_ += "1bM2bL";
    else if ( numBJets_medium_ >= 1                         ) name_ += "1bM";
    else if (                          numBJets_loose_ >= 2 ) name_ += "2bL";
    else if (                          numBJets_loose_ >= 1 ) name_ += "1bL";    
    else if (                          numBJets_loose_ == 0 ) name_ += "nobL";    
    if      ( minNumJets == -1 && maxNumJets == -1          ) (void)0; // CV: do nothing ("no operation")
    else if ( minNumJets == maxNumJets                      ) name_ += Form("%ij", minNumJets);
    else if ( minNumJets == -1                              ) name_ += Form("le%ij", maxNumJets);
    else if ( maxNumJets == -1                              ) name_ += Form("ge%ij", minNumJets);
    else if ( maxNumJets >  minNumJets                      ) name_ += Form("%ito%ij", minNumJets, maxNumJets);
    else assert(0);
    if      ( numElectrons_ >= 2                            ) name_ += "2e";
    else if ( numMuons_ >= 2                                ) name_ += "2mu";
    else                                                      name_ += "2l";
    name_ += "_DYctrl";
    if      ( type_Hbb_ == kHbb_resolved                    ) name_ += "_resolvedHbb";
    else if ( type_Hbb_ == kHbb_boosted                     ) name_ += "_boostedHbb";
    if      ( type_vbf_ == kVBF_tagged                      ) name_ += "_vbf";
    else if ( type_vbf_ == kVBF_nottagged                   ) name_ += "_nonvbf";
    //std::cout << "name = '" << name_ << "'" << std::endl;
  }
  ~categoryEntryType() {}
  std::string name_;
  int numElectrons_;
  int numMuons_;
  int minNumJets_;
  int maxNumJets_;
  int numBJets_medium_;
  int numBJets_loose_;
  int type_Hbb_; // 0 = either resolved or boosted, 1 = resolved, 2 = boosted
  int type_vbf_; // 0 = either tagged or not tagged, 1 = not tagged; 2 = tagged 
};

/**
 * @brief Produce datacard and control plots for Drell-Yan (DY) control region of the HH->bbWW analysis.
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

  std::cout << "<analyze_hh_bbWW_DYctrl>:" << std::endl;

//--- keep track of time it takes the macro to execute
  TBenchmark clock;
  clock.Start("analyze_hh_bbWW_DYctrl");

//--- read python configuration parameters
  if ( !edm::readPSetsFrom(argv[1])->existsAs<edm::ParameterSet>("process") )
    throw cms::Exception("analyze_hh_bbWW_DYctrl")
      << "No ParameterSet 'process' found in configuration file = " << argv[1] << " !!\n";

  edm::ParameterSet cfg = edm::readPSetsFrom(argv[1])->getParameter<edm::ParameterSet>("process");

  edm::ParameterSet cfg_analyze = cfg.getParameter<edm::ParameterSet>("analyze_hh_bbWW_DYctrl");

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

  bool apply_offline_e_trigger_cuts_1e = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_1e");
  bool apply_offline_e_trigger_cuts_2e = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_2e");
  bool apply_offline_e_trigger_cuts_1mu = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_1mu");
  bool apply_offline_e_trigger_cuts_2mu = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_2mu");

  enum { kOS, kSS, kDisabled };
  std::string leptonChargeSelection_string = cfg_analyze.getParameter<std::string>("leptonChargeSelection");
  int leptonChargeSelection = -1;
  if      ( leptonChargeSelection_string == "OS"       ) leptonChargeSelection = kOS;
  else if ( leptonChargeSelection_string == "SS"       ) leptonChargeSelection = kSS;
  else if ( leptonChargeSelection_string == "disabled" ) leptonChargeSelection = kDisabled;
  else throw cms::Exception("analyze_hh_bbWW_DYctrl")
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

  bool isMC = cfg_analyze.getParameter<bool>("isMC");
  bool isMC_tH = ( process_string == "tHq" || process_string == "tHW" ) ? true : false;
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
  cfg_dataToMCcorrectionInterface.addParameter<std::string>("hadTauSelection", "dR03mvaMedium"); // CV: dummy value (no taus used in HH->bbWW analysis)
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
    default: throw cmsException("analyze_hh_bbWW_DYctrl", __LINE__) << "Invalid era = " << era;
  }

  std::string applyFakeRateWeights_string = cfg_analyze.getParameter<std::string>("applyFakeRateWeights");
  int applyFakeRateWeights = -1;
  if      ( applyFakeRateWeights_string == "disabled" ) applyFakeRateWeights = kFR_disabled;
  else if ( applyFakeRateWeights_string == "enabled"  ) applyFakeRateWeights = kFR_enabled;
  else throw cms::Exception("analyze_hh_bbWW_DYctrl")
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
  bool redoGenMatching = cfg_analyze.getParameter<bool>("redoGenMatching");

  std::string branchName_genTauLeptons = cfg_analyze.getParameter<std::string>("branchName_genTauLeptons");

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

//--- declare event-level variables
  EventInfo eventInfo(isSignal, isMC, isMC_tH);
  EventInfoReader eventInfoReader(&eventInfo);
  inputTree->registerReader(&eventInfoReader);

  hltPathReader hltPathReader_instance({ triggers_1e, triggers_2e, triggers_1mu, triggers_2mu });
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
  RecoElectronCollectionCleaner electronCleaner(0.05, isDEBUG);
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
  RecoJetCollectionSelectorAK8_bbWW_Hbb jetSelectorAK8_Hbb(era, -1, isDEBUG);

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
  inputTree -> registerReader(metFilterReader);

//--- declare generator level information
  GenLeptonReader* genLeptonReader = 0;
  GenHadTauReader* genHadTauReader = 0;
  GenPhotonReader* genPhotonReader = 0;
  GenJetReader* genJetReader = 0;
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
        inputTree -> registerReader(genPhotonReader);
      }
      if ( branchName_genJets != "" ) {
        genJetReader = new GenJetReader(branchName_genJets);
        inputTree->registerReader(genJetReader);
      }
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
      Form("%s/unbiased/genEvt", histogramDir.data()), central_or_shift));
    genEvtHistManager_beforeCuts->bookHistograms(fs);
    lheInfoHistManager_beforeCuts = new LHEInfoHistManager(makeHistManager_cfg(process_string,
      Form("%s/unbiased/lheInfo", histogramDir.data()), central_or_shift));
    lheInfoHistManager_beforeCuts->bookHistograms(fs);
  }

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
    JetHistManager* thirdJetAK4_;
    JetHistManager* fourthJetAK4_;    
    JetHistManagerAK8* jetsAK8_Hbb_;
    JetHistManager* BJetsAK4_loose_;
    JetHistManager* leadBJetAK4_loose_;
    JetHistManager* subleadBJetAK4_loose_;
    JetHistManager* BJetsAK4_medium_;
    MEtHistManager* met_;
    MEtFilterHistManager* metFilters_;
    TriggerHistManager* triggers_1e_;
    TriggerHistManager* triggers_2e_;
    TriggerHistManager* triggers_1mu_;
    TriggerHistManager* triggers_2mu_;
    EvtHistManager_hh_bbWW_DYctrl* evt_;
    std::map<std::string, EvtHistManager_hh_bbWW_DYctrl*> evt_in_categories_;
    GenEvtHistManager* genEvtHistManager_afterCuts_;
    LHEInfoHistManager* lheInfoHistManager_afterCuts_;
    std::map<std::string, LHEInfoHistManager*> lheInfoHistManager_afterCuts_in_categories_;
    EvtYieldHistManager* evtYield_;
    WeightHistManager* weights_;
  };
  std::map<int, selHistManagerType*> selHistManagers;
  std::vector<categoryEntryType> categories_evt;
  for ( int type_lepton = kDielectron; type_lepton <= kDimuon; ++type_lepton ) {
    int numElectrons = ( type_lepton == kDielectron ) ? 2 : -1;
    int numMuons     = ( type_lepton == kDimuon     ) ? 2 : -1;
    // CV: add categories for "resolved" b-jets without VBF jet selection
    categories_evt.push_back(categoryEntryType(numElectrons, numMuons,  2, -1, -1, -1, kHbb_resolved, kVBF_undefined)); // hh_bbWW_2bM2e_DYctrl,        hh_bbWW_2bM2mu_DYctrl
    categories_evt.push_back(categoryEntryType(numElectrons, numMuons,  2, -1,  2,  2, kHbb_resolved, kVBF_undefined)); // hh_bbWW_2bM2j2e_DYctrl,      hh_bbWW_2bM2j2mu_DYctrl 
    categories_evt.push_back(categoryEntryType(numElectrons, numMuons,  2, -1,  3,  3, kHbb_resolved, kVBF_undefined)); // hh_bbWW_2bM3j2e_DYctrl,      hh_bbWW_2bM3j2mu_DYctrl
    categories_evt.push_back(categoryEntryType(numElectrons, numMuons,  2, -1,  4, -1, kHbb_resolved, kVBF_undefined)); // hh_bbWW_2bMge4j2e_DYctrl,    hh_bbWW_2bMge4j2mu_DYctrl
    categories_evt.push_back(categoryEntryType(numElectrons, numMuons,  1,  2, -1, -1, kHbb_resolved, kVBF_undefined)); // hh_bbWW_1bM2bL2e_DYctrl,     hh_bbWW_1bM2bL2mu_DYctrl
    categories_evt.push_back(categoryEntryType(numElectrons, numMuons,  1,  2,  2,  2, kHbb_resolved, kVBF_undefined)); // hh_bbWW_1bM2bL2j2e_DYctrl,   hh_bbWW_1bM2bL2j2mu_DYctrl
    categories_evt.push_back(categoryEntryType(numElectrons, numMuons,  1,  2,  3,  3, kHbb_resolved, kVBF_undefined)); // hh_bbWW_1bM2bL3j2e_DYctrl,   hh_bbWW_1bM2bL3j2mu_DYctrl
    categories_evt.push_back(categoryEntryType(numElectrons, numMuons,  1,  2,  4, -1, kHbb_resolved, kVBF_undefined)); // hh_bbWW_1bM2bLge4j2e_DYctrl, hh_bbWW_1bM2bLge4j2mu_DYctrl
    categories_evt.push_back(categoryEntryType(numElectrons, numMuons,  1, -1, -1, -1, kHbb_resolved, kVBF_undefined)); // hh_bbWW_1bM2e_DYctrl,        hh_bbWW_1bM2mu_DYctrl
    categories_evt.push_back(categoryEntryType(numElectrons, numMuons,  1, -1,  1,  1, kHbb_resolved, kVBF_undefined)); // hh_bbWW_1bM1j2e_DYctrl,      hh_bbWW_1bM2j2mu_DYctrl 
    categories_evt.push_back(categoryEntryType(numElectrons, numMuons,  1, -1,  2,  2, kHbb_resolved, kVBF_undefined)); // hh_bbWW_1bM2j2e_DYctrl,      hh_bbWW_1bM2j2mu_DYctrl 
    categories_evt.push_back(categoryEntryType(numElectrons, numMuons,  1, -1,  3,  3, kHbb_resolved, kVBF_undefined)); // hh_bbWW_1bM3j2e_DYctrl,      hh_bbWW_1bM3j2mu_DYctrl
    categories_evt.push_back(categoryEntryType(numElectrons, numMuons,  1, -1,  4, -1, kHbb_resolved, kVBF_undefined)); // hh_bbWW_1bMge4j2e_DYctrl,    hh_bbWW_1bMge4j2mu_DYctrl
    categories_evt.push_back(categoryEntryType(numElectrons, numMuons, -1,  2, -1, -1, kHbb_resolved, kVBF_undefined)); // hh_bbWW_2bL2e_DYctrl,        hh_bbWW_2bL2mu_DYctrl
    categories_evt.push_back(categoryEntryType(numElectrons, numMuons, -1,  2,  2,  2, kHbb_resolved, kVBF_undefined)); // hh_bbWW_2bL2j2e_DYctrl,      hh_bbWW_2bL2j2mu_DYctrl 
    categories_evt.push_back(categoryEntryType(numElectrons, numMuons, -1,  2,  3,  3, kHbb_resolved, kVBF_undefined)); // hh_bbWW_2bL3j2e_DYctrl,      hh_bbWW_2bL3j2mu_DYctrl
    categories_evt.push_back(categoryEntryType(numElectrons, numMuons, -1,  2,  4, -1, kHbb_resolved, kVBF_undefined)); // hh_bbWW_2bLge4j2e_DYctrl,    hh_bbWW_2bLge4j2mu_DYctrl
    categories_evt.push_back(categoryEntryType(numElectrons, numMuons, -1,  1, -1, -1, kHbb_resolved, kVBF_undefined)); // hh_bbWW_1bL2e_DYctrl,        hh_bbWW_1bL2mu_DYctrl
    categories_evt.push_back(categoryEntryType(numElectrons, numMuons, -1,  1,  1,  1, kHbb_resolved, kVBF_undefined)); // hh_bbWW_1bL1j2e_DYctrl,      hh_bbWW_1bL1j2mu_DYctrl 
    categories_evt.push_back(categoryEntryType(numElectrons, numMuons, -1,  1,  2,  2, kHbb_resolved, kVBF_undefined)); // hh_bbWW_1bL2j2e_DYctrl,      hh_bbWW_1bL2j2mu_DYctrl 
    categories_evt.push_back(categoryEntryType(numElectrons, numMuons, -1,  1,  3,  3, kHbb_resolved, kVBF_undefined)); // hh_bbWW_1bL3j2e_DYctrl,      hh_bbWW_1bL3j2mu_DYctrl
    categories_evt.push_back(categoryEntryType(numElectrons, numMuons, -1,  1,  4, -1, kHbb_resolved, kVBF_undefined)); // hh_bbWW_1bLge4j2e_DYctrl,    hh_bbWW_1bLge4j2mu_DYctrl
    categories_evt.push_back(categoryEntryType(numElectrons, numMuons, -1,  0, -1, -1, kHbb_resolved, kVBF_undefined)); // hh_bbWW_nobL2e_DYctrl,       hh_bbWW_nobL2mu_DYctrl
    categories_evt.push_back(categoryEntryType(numElectrons, numMuons, -1,  0,  0,  0, kHbb_resolved, kVBF_undefined)); // hh_bbWW_nobL0j2e_DYctrl,     hh_bbWW_nobL0j2mu_DYctrl 
    categories_evt.push_back(categoryEntryType(numElectrons, numMuons, -1,  0,  1,  1, kHbb_resolved, kVBF_undefined)); // hh_bbWW_nobL1j2e_DYctrl,     hh_bbWW_nobL1j2mu_DYctrl 
    categories_evt.push_back(categoryEntryType(numElectrons, numMuons, -1,  0,  2,  2, kHbb_resolved, kVBF_undefined)); // hh_bbWW_nobL2j2e_DYctrl,     hh_bbWW_nobL2j2mu_DYctrl 
    categories_evt.push_back(categoryEntryType(numElectrons, numMuons, -1,  0,  3,  3, kHbb_resolved, kVBF_undefined)); // hh_bbWW_nobL3j2e_DYctrl,     hh_bbWW_nobL3j2mu_DYctrl
    categories_evt.push_back(categoryEntryType(numElectrons, numMuons, -1,  0,  4, -1, kHbb_resolved, kVBF_undefined)); // hh_bbWW_nobLge4j2e_DYctrl,   hh_bbWW_nobLge4j2mu_DYctrl    
    // CV: add categories for "resolved" b-jets with VBF jet selection
    categories_evt.push_back(categoryEntryType(numElectrons, numMuons,  2, -1, -1, -1, kHbb_resolved, kVBF_tagged));    // hh_bbWW_2bM2e_DYctrl,        hh_bbWW_2bM2mu_DYctrl
    categories_evt.push_back(categoryEntryType(numElectrons, numMuons,  1,  2, -1, -1, kHbb_resolved, kVBF_tagged));    // hh_bbWW_1bM2bL2e_DYctrl,     hh_bbWW_1bM2bL2mu_DYctrl
    categories_evt.push_back(categoryEntryType(numElectrons, numMuons,  1, -1, -1, -1, kHbb_resolved, kVBF_tagged));    // hh_bbWW_1bM2e_DYctrl,        hh_bbWW_1bM2mu_DYctrl
    categories_evt.push_back(categoryEntryType(numElectrons, numMuons, -1,  2, -1, -1, kHbb_resolved, kVBF_tagged));    // hh_bbWW_2bL2e_DYctrl,        hh_bbWW_2bL2mu_DYctrl
    // CV: add categories for "boosted" b-jets (no VBF jet selection)
    categories_evt.push_back(categoryEntryType(numElectrons, numMuons,  2, -1, -1, -1, kHbb_boosted,  kVBF_undefined)); // hh_bbWW_2bM2e_DYctrl,        hh_bbWW_2bM2mu_DYctrl
    categories_evt.push_back(categoryEntryType(numElectrons, numMuons,  1,  2, -1, -1, kHbb_boosted,  kVBF_undefined)); // hh_bbWW_1bM2bL2e_DYctrl,     hh_bbWW_1bM2bL2mu_DYctrl
    categories_evt.push_back(categoryEntryType(numElectrons, numMuons,  1, -1, -1, -1, kHbb_boosted,  kVBF_undefined)); // hh_bbWW_1bM2e_DYctrl,        hh_bbWW_1bM2mu_DYctrl
  }
  vstring categoryNames_evt;
  for ( std::vector<categoryEntryType>::const_iterator category = categories_evt.begin();
	category != categories_evt.end(); ++category ) {
    categoryNames_evt.push_back(category->name_);
  }
  std::cout << "Processing " << categoryNames_evt.size() << " categories: " << format_vstring(categoryNames_evt) << std::endl;
  for ( std::vector<leptonGenMatchEntry>::const_iterator leptonGenMatch_definition = leptonGenMatch_definitions.begin();
        leptonGenMatch_definition != leptonGenMatch_definitions.end(); ++leptonGenMatch_definition ) {

    std::string process_and_genMatch = process_string;
    if ( apply_leptonGenMatching ) process_and_genMatch += leptonGenMatch_definition->name_;
    int idxLepton = leptonGenMatch_definition->idx_;

    selHistManagerType* selHistManager = new selHistManagerType();
    selHistManager->electrons_ = new ElectronHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/electrons", histogramDir.data()), central_or_shift));
    selHistManager->electrons_->bookHistograms(fs);
    selHistManager->leadElectron_ = new ElectronHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/leadElectron", histogramDir.data()), central_or_shift, 0));
    selHistManager->leadElectron_->bookHistograms(fs);
    selHistManager->subleadElectron_ = new ElectronHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/subleadElectron", histogramDir.data()), central_or_shift, 1));
    selHistManager->subleadElectron_->bookHistograms(fs);
    selHistManager->muons_ = new MuonHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/muons", histogramDir.data()), central_or_shift));
    selHistManager->muons_->bookHistograms(fs);
    selHistManager->leadMuon_ = new MuonHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/leadMuon", histogramDir.data()), central_or_shift, 0));
    selHistManager->leadMuon_->bookHistograms(fs);
    selHistManager->subleadMuon_ = new MuonHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/subleadMuon", histogramDir.data()), central_or_shift, 1));
    selHistManager->subleadMuon_->bookHistograms(fs);
    selHistManager->jetsAK4_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/jetsAK4", histogramDir.data()), central_or_shift));
    selHistManager->jetsAK4_->bookHistograms(fs);
    selHistManager->leadJetAK4_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/leadJetAK4", histogramDir.data()), central_or_shift, 0));
    selHistManager->leadJetAK4_->bookHistograms(fs);
    selHistManager->subleadJetAK4_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/subleadJetAK4", histogramDir.data()), central_or_shift, 1));
    selHistManager->subleadJetAK4_->bookHistograms(fs);
    selHistManager->thirdJetAK4_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/thirdJetAK4", histogramDir.data()), central_or_shift, 2));
    selHistManager->thirdJetAK4_->bookHistograms(fs);
    selHistManager->fourthJetAK4_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/fourthJetAK4", histogramDir.data()), central_or_shift, 3));
    selHistManager->fourthJetAK4_->bookHistograms(fs);
    selHistManager->jetsAK8_Hbb_ = new JetHistManagerAK8(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/jetsAK8_Hbb", histogramDir.data()), central_or_shift));
    selHistManager->jetsAK8_Hbb_->bookHistograms(fs);
    selHistManager->BJetsAK4_loose_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/BJetsAK4_loose", histogramDir.data()), central_or_shift));
    selHistManager->BJetsAK4_loose_->bookHistograms(fs);
    selHistManager->leadBJetAK4_loose_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/leadBJetAK4_loose", histogramDir.data()), central_or_shift, 0));
    selHistManager->leadBJetAK4_loose_->bookHistograms(fs);
    selHistManager->subleadBJetAK4_loose_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/subleadBJetAK4_loose", histogramDir.data()), central_or_shift, 1));
    selHistManager->subleadBJetAK4_loose_->bookHistograms(fs);
    selHistManager->BJetsAK4_medium_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/BJetsAK4_medium", histogramDir.data()), central_or_shift));
    selHistManager->BJetsAK4_medium_->bookHistograms(fs);
    selHistManager->met_ = new MEtHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/met", histogramDir.data()), central_or_shift));
    selHistManager->met_->bookHistograms(fs);
    selHistManager->metFilters_ = new MEtFilterHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/metFilters", histogramDir.data()), central_or_shift));
    selHistManager->metFilters_->bookHistograms(fs);
    selHistManager->triggers_1e_ = new TriggerHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/triggers_1e", histogramDir.data()), central_or_shift));
    selHistManager->triggers_1e_->add_hltPaths(triggers_1e);
    selHistManager->triggers_1e_->bookHistograms(fs);
    selHistManager->triggers_2e_ = new TriggerHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/triggers_2e", histogramDir.data()), central_or_shift));
    selHistManager->triggers_2e_->add_hltPaths(triggers_2e);
    selHistManager->triggers_2e_->bookHistograms(fs);
    selHistManager->triggers_1mu_ = new TriggerHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/triggers_1mu", histogramDir.data()), central_or_shift));
    selHistManager->triggers_1mu_->add_hltPaths(triggers_1mu);
    selHistManager->triggers_1mu_->bookHistograms(fs);
    selHistManager->triggers_2mu_ = new TriggerHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/triggers_2mu", histogramDir.data()), central_or_shift));
    selHistManager->triggers_2mu_->add_hltPaths(triggers_2mu);
    selHistManager->triggers_2mu_->bookHistograms(fs);
    selHistManager->evt_ = new EvtHistManager_hh_bbWW_DYctrl(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/evt", histogramDir.data()), era_string, central_or_shift));
    selHistManager->evt_->bookHistograms(fs);
    if ( isMC ) {
      selHistManager->genEvtHistManager_afterCuts_ = new GenEvtHistManager(makeHistManager_cfg(process_and_genMatch,
        Form("%s/sel/genEvt", histogramDir.data()), central_or_shift));
      selHistManager->genEvtHistManager_afterCuts_->bookHistograms(fs);
      selHistManager->lheInfoHistManager_afterCuts_ = new LHEInfoHistManager(makeHistManager_cfg(process_and_genMatch,
        Form("%s/sel/lheInfo", histogramDir.data()), central_or_shift));
      selHistManager->lheInfoHistManager_afterCuts_->bookHistograms(fs);
    }
    for ( std::vector<categoryEntryType>::const_iterator category = categories_evt.begin();
	  category != categories_evt.end(); ++category ) {
      //std::cout << "booking histograms for category = '" << category->name_ << "'" << std::endl;
      TString histogramDir_category = histogramDir.data();
      histogramDir_category.ReplaceAll("bbWW_2l_DYctrl", category->name_.data());
      selHistManager->evt_in_categories_[category->name_] = new EvtHistManager_hh_bbWW_DYctrl(makeHistManager_cfg(process_and_genMatch,
        Form("%s/sel/evt", histogramDir_category.Data()), central_or_shift));
      selHistManager->evt_in_categories_[category->name_]->bookHistograms(fs);
      if ( isMC ) {
	selHistManager->lheInfoHistManager_afterCuts_in_categories_[category->name_] = new LHEInfoHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/lheInfo", histogramDir_category.Data()), central_or_shift));
	selHistManager->lheInfoHistManager_afterCuts_in_categories_[category->name_]->bookHistograms(fs);
      }
    }
    edm::ParameterSet cfg_EvtYieldHistManager_sel = makeHistManager_cfg(process_and_genMatch, 
      Form("%s/sel/evtYield", histogramDir.data()), central_or_shift);
    cfg_EvtYieldHistManager_sel.addParameter<edm::ParameterSet>("runPeriods", cfg_EvtYieldHistManager);
    cfg_EvtYieldHistManager_sel.addParameter<bool>("isMC", isMC);
    selHistManager->evtYield_ = new EvtYieldHistManager(cfg_EvtYieldHistManager_sel);
    selHistManager->evtYield_->bookHistograms(fs);  
    selHistManager->weights_ = new WeightHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/weights", histogramDir.data()), central_or_shift));
    selHistManager->weights_->bookHistograms(fs, { "genWeight", "pileupWeight", "triggerWeight", "data_to_MC_correction", "fakeRate" });
    selHistManagers[idxLepton] = selHistManager;
  }

  int analyzedEntries = 0;
  int selectedEntries = 0;
  double selectedEntries_weighted = 0.;
  TH1* histogram_analyzedEntries = fs.make<TH1D>("analyzedEntries", "analyzedEntries", 1, -0.5, +0.5);
  TH1* histogram_selectedEntries = fs.make<TH1D>("selectedEntries", "selectedEntries", 1, -0.5, +0.5);
  cutFlowTableType cutFlowTable;
  const edm::ParameterSet cutFlowTableCfg = makeHistManager_cfg(
    process_string, Form("%s/sel/cutFlow", histogramDir.data()), central_or_shift
  );
  const std::vector<std::string> cuts = {
    "run:ls:event selection",
    "trigger",
    ">= 2 presel leptons",
    ">= 2 sel leptons",
    "sel SF lepton pair",
    "lead lepton pT > 25 GeV && sublead lepton pT > 15 GeV",
    "sel lepton-pair OS/SS charge",
    "<= 2 tight leptons",
    "fakeable lepton trigger match",
    "HLT filter matching",
    //">= 2 b-jet candidates",
    //">= 2 loose b-jets || 1 medium b-jet",
    "m(ll) > 12 GeV",
    "Z-boson mass",
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
    }

    bool isTriggered_1e = hltPaths_isTriggered(triggers_1e);
    bool isTriggered_2e = hltPaths_isTriggered(triggers_2e);
    bool isTriggered_1mu = hltPaths_isTriggered(triggers_1mu);
    bool isTriggered_2mu = hltPaths_isTriggered(triggers_2mu);

    bool selTrigger_1e = use_triggers_1e && isTriggered_1e;
    bool selTrigger_2e = use_triggers_2e && isTriggered_2e;
    bool selTrigger_1mu = use_triggers_1mu && isTriggered_1mu;
    bool selTrigger_2mu = use_triggers_2mu && isTriggered_2mu;
    if ( !(selTrigger_1e || selTrigger_2e || selTrigger_1mu || selTrigger_2mu) ) {
      if ( run_lumi_eventSelector ) {
    std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
        std::cout << " (selTrigger_1e = " << selTrigger_1e
                  << ", selTrigger_2e = " << selTrigger_2e
                  << ", selTrigger_1mu = " << selTrigger_1mu
                  << ", selTrigger_2mu = " << selTrigger_2mu << ")" << std::endl;
      }
      continue;
    }

//--- rank triggers by priority and ignore triggers of lower priority if a trigger of higher priority has fired for given event;
//    the ranking of the triggers is as follows: 2mu, 2e, 1mu, 1e
// CV: this logic is necessary to avoid that the same event is selected multiple times when processing different primary datasets
    if ( !isMC && !isDEBUG ) {
      if ( selTrigger_1e && (isTriggered_2e || isTriggered_1mu || isTriggered_2mu) ) {
        if ( run_lumi_eventSelector ) {
      std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
          std::cout << " (selTrigger_1e = " << selTrigger_1e
                    << ", isTriggered_2e = " << isTriggered_2e
                    << ", isTriggered_1mu = " << isTriggered_1mu
                    << ", isTriggered_2mu = " << isTriggered_2mu << ")" << std::endl;
        }
        continue;
      }
      if ( selTrigger_2e && (isTriggered_2mu) ) {
        if ( run_lumi_eventSelector ) {
      std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
          std::cout << " (selTrigger_2e = " << selTrigger_2e
                    << ", isTriggered_2mu = " << isTriggered_2mu<< ")" << std::endl;
        }
        continue;
      }
      if ( selTrigger_1mu && (isTriggered_2e || isTriggered_2mu) ) {
        if ( run_lumi_eventSelector ) {
      std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
          std::cout << " (selTrigger_1mu = " << selTrigger_1mu
                    << ", isTriggered_2e = " << isTriggered_2e
                    << ", isTriggered_2mu = " << isTriggered_2mu << ")" << std::endl;
        }
        continue;
      }
    }
    cutFlowTable.update("trigger", evtWeight_inclusive);
    cutFlowHistManager->fillHistograms("trigger", evtWeight_inclusive);

    if ( (selTrigger_2e    && !apply_offline_e_trigger_cuts_2e)    ||
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

    if ( !(selElectrons.size() >= 2 || selMuons.size() >= 2) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS sel SF lepton pair selection." << std::endl;
        printCollection("selElectrons", selElectrons);
	printCollection("selMuons", selMuons);
      }
      continue;
    }
    cutFlowTable.update("sel SF lepton pair", evtWeight);
    cutFlowHistManager->fillHistograms("sel SF lepton pair", evtWeight);

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

    // require exactly two leptons passing tight selection criteria
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
    if ( !((fakeableElectrons.size() >= 2 &&                              (selTrigger_2e    || selTrigger_1e  )) ||
           (                                 fakeableMuons.size() >= 2 && (selTrigger_2mu   || selTrigger_1mu ))) ) {
      if ( run_lumi_eventSelector ) {
	std::cout << "event " << eventInfo.str() << " FAILS trigger selection for given fakeableLepton multiplicity." << std::endl;
        std::cout << " (#fakeableElectrons = " << fakeableElectrons.size()
                  << ", #fakeableMuons = " << fakeableMuons.size()
                  << ", selTrigger_2mu = " << selTrigger_2mu
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

    // select b-jet candidate pair 
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
    //if ( !(selJet1_Hbb && selJet2_Hbb) ) {
    //  if ( run_lumi_eventSelector ) {
    //    std::cout << "event " << eventInfo.str() << " FAILS b-jet candidate pair selection\n";
    //  }
    //  continue;
    //}
    //cutFlowTable.update(">= 2 b-jet candidates", evtWeight_inclusive);
    //cutFlowHistManager->fillHistograms(">= 2 b-jet candidates", evtWeight_inclusive);

    std::vector<const RecoJetBase*> selJets_Hbb;
    if ( selJet1_Hbb ) selJets_Hbb.push_back(selJet1_Hbb);
    if ( selJet2_Hbb ) selJets_Hbb.push_back(selJet2_Hbb);
    std::sort(selJets_Hbb.begin(), selJets_Hbb.end(), isHigherPt);
    const RecoJetBase* selJet_Hbb_lead = nullptr;
    Particle::LorentzVector selJetP4_Hbb_lead;
    if ( selJets_Hbb.size() >= 1 ) {
      selJet_Hbb_lead = selJets_Hbb[0];
      selJetP4_Hbb_lead = selJet_Hbb_lead->p4();
    }
    const RecoJetBase* selJet_Hbb_sublead = nullptr;
    Particle::LorentzVector selJetP4_Hbb_sublead;
    if ( selJets_Hbb.size() >= 2 ) {
      selJet_Hbb_sublead = selJets_Hbb[1];
      selJetP4_Hbb_sublead = selJet_Hbb_sublead->p4();
    }

    //if ( !(numBJets_loose >= 1) ) {
    //  if ( run_lumi_eventSelector ) {
    //    std::cout << "event " << eventInfo.str() << " FAILS >= 2 loose b-jets || 1 medium b-jet selection\n";
    //  }
    //  continue;
    //}
    //cutFlowTable.update(">= 2 loose b-jets || 1 medium b-jet", evtWeight_inclusive);
    //cutFlowHistManager->fillHistograms(">= 2 loose b-jets || 1 medium b-jet", evtWeight_inclusive);

    // select jets not overlapping with b-jet candidate pair 
    std::vector<const RecoJet*> cleanedJetsAK4_wrtHbb;
    if ( selJetAK8_Hbb ) {
      std::vector<const RecoJetAK8*> overlaps = { selJetAK8_Hbb };
      cleanedJetsAK4_wrtHbb = jetCleanerAK4_dR12(cleanedJetsAK4_wrtLeptons, overlaps);
    } else {
      //cleanedJetsAK4_wrtHbb = jetCleanerAK4_dR08(cleanedJetsAK4_wrtLeptons, selJets_Hbb);
      cleanedJetsAK4_wrtHbb = cleanedJetsAK4_wrtLeptons;
    }
    std::vector<const RecoJet*> selJetsAK4_nonHbb = jetSelectorAK4(cleanedJetsAK4_wrtHbb, isHigherPt);
    int numJets_nonHbb = selJetsAK4_nonHbb.size();
    
    // select VBF jet candidates
    std::vector<const RecoJet*> cleanedJetsAK4_vbf;
    if ( selJetAK8_Hbb ) {
      std::vector<const RecoJetAK8*> overlaps = { selJetAK8_Hbb };
      cleanedJetsAK4_vbf = jetCleanerAK4_dR12(cleanedJetsAK4_wrtLeptons, overlaps);
    } else {
      cleanedJetsAK4_vbf = jetCleanerAK4_dR08(cleanedJetsAK4_wrtLeptons, selJets_Hbb);
    }
    std::vector<const RecoJet*> selJetsAK4_vbf = jetSelectorAK4_vbf(cleanedJetsAK4_vbf, isHigherPt);

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
    for ( std::vector<const RecoLepton*>::const_iterator lepton1 = selLeptons.begin();
	  lepton1 != selLeptons.end(); ++lepton1 ) {
      for ( std::vector<const RecoLepton*>::const_iterator lepton2 = lepton1 + 1;
	    lepton2 != selLeptons.end(); ++lepton2 ) {
        if ( (*lepton1)->pdgId() == -(*lepton2)->pdgId() ) { // pair of same flavor leptons of opposite charge
          isSameFlavor_OS = true;
          double mass = ((*lepton1)->p4() + (*lepton2)->p4()).mass();
          if ( std::fabs(mass - z_mass) < std::fabs(massSameFlavor_OS - z_mass) ) massSameFlavor_OS = mass;
        }
      }
    }
    bool passesZbosonMass = isSameFlavor_OS && massSameFlavor_OS > 60. && massSameFlavor_OS < 120.;
    if ( !passesZbosonMass ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS Z-boson selection." << std::endl;
      }
      continue;
    }
    cutFlowTable.update("Z-boson mass", evtWeight);
    cutFlowHistManager->fillHistograms("Z-boson mass", evtWeight);
    
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

    // compute signal extraction observables
    Particle::LorentzVector bbP4 = selJetP4_Hbb_lead + selJetP4_Hbb_sublead;
    double m_bb    = bbP4.mass();
    double dR_bb   = deltaR(selJetP4_Hbb_lead, selJetP4_Hbb_sublead);
    double dPhi_bb = deltaPhi(selJetP4_Hbb_lead.phi(), selJetP4_Hbb_sublead.phi());
    double pT_bb   = bbP4.pt();
    Particle::LorentzVector llP4 = selLeptonP4_lead + selLeptonP4_sublead;
    double m_ll  = llP4.mass();
    double dR_ll = deltaR(selLeptonP4_lead, selLeptonP4_sublead);
    double dPhi_ll = deltaPhi(selLeptonP4_lead.phi(), selLeptonP4_sublead.phi());
    double pT_ll = llP4.pt();
    Particle::LorentzVector bbllP4 = bbP4 + llP4;
    double m_bbll = bbllP4.mass();
    double pT_bbll = bbllP4.pt();
    double dPhi_bbll = deltaPhi(bbP4.phi(), llP4.phi()); 
    Particle::LorentzVector bbllMEtP4 = bbllP4 + metP4;
    double m_bbllMEt = bbllMEtP4.mass();
    double pT_bbllMEt = bbllMEtP4.pt();
    double Smin_bbllMEt = comp_Smin(bbllP4, metP4.px(), metP4.py());
    double dPhi_bbllMEt = deltaPhi(bbP4.phi(), (llP4 + metP4).phi());
    double m_HH_hme = -1.; // CV: not implemented yet
    
    double vbf_dEta_jj = -1.;
    double vbf_m_jj = -1.;
    const RecoJet* selJet_vbf_lead = nullptr;
    const RecoJet* selJet_vbf_sublead = nullptr;
    for ( std::vector<const RecoJet*>::const_iterator selJet1_vbf = selJetsAK4_vbf.begin();
          selJet1_vbf != selJetsAK4_vbf.end(); ++selJet1_vbf ) {
      for ( std::vector<const RecoJet*>::const_iterator selJet2_vbf = selJet1_vbf + 1;
	    selJet2_vbf != selJetsAK4_vbf.end(); ++selJet2_vbf ) {
	double dEta_jj = TMath::Abs((*selJet1_vbf)->eta() - (*selJet2_vbf)->eta());
	double m_jj = ((*selJet1_vbf)->p4() + (*selJet2_vbf)->p4()).mass();
	if ( dEta_jj > 4. && m_jj > 500. ) {
	  if ( m_jj > vbf_m_jj ) { // CV: in case of ambiguity, take the jet pair of highest mass
	    vbf_dEta_jj = dEta_jj;
	    vbf_m_jj = m_jj;
	    selJet_vbf_lead = (*selJet1_vbf);
	    selJet_vbf_sublead = (*selJet1_vbf);
	  }
	}
      }
    }
    bool isVBF = false;    
    std::vector<const RecoJet*> selJetsAK4_nonVBF;
    if ( selJet_vbf_lead && selJet_vbf_sublead ) {
      std::vector<const RecoJet*> overlaps = { selJet_vbf_lead, selJet_vbf_sublead };
      std::vector<const RecoJet*> cleanedJetsAK4_wrtVBF = jetCleanerAK4_dR08(cleanedJetsAK4_wrtHbb, overlaps);
      selJetsAK4_nonVBF = jetSelectorAK4(cleanedJetsAK4_wrtVBF, isHigherPt);
      if ( selJetsAK4_nonVBF.size() >= 1 ) {
	isVBF = true;
      }
    }
    int numSelJetsAK4_nonVBF = ( isVBF ) ? selJetsAK4_nonVBF.size() : selJetsAK4_nonHbb.size();

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
    selHistManager->jetsAK4_->fillHistograms(selJetsAK4_nonHbb, evtWeight);
    selHistManager->leadJetAK4_->fillHistograms(selJetsAK4_nonHbb, evtWeight);
    selHistManager->subleadJetAK4_->fillHistograms(selJetsAK4_nonHbb, evtWeight);
    selHistManager->thirdJetAK4_->fillHistograms(selJetsAK4_nonHbb, evtWeight);
    selHistManager->fourthJetAK4_->fillHistograms(selJetsAK4_nonHbb, evtWeight);   
    if ( selJetAK8_Hbb ) {
      selHistManager->jetsAK8_Hbb_->fillHistograms({ selJetAK8_Hbb }, evtWeight);
    }
    selHistManager->BJetsAK4_loose_->fillHistograms(selBJetsAK4_loose, evtWeight);
    selHistManager->leadBJetAK4_loose_->fillHistograms(selBJetsAK4_loose, evtWeight);
    selHistManager->subleadBJetAK4_loose_->fillHistograms(selBJetsAK4_loose, evtWeight);
    selHistManager->BJetsAK4_medium_->fillHistograms(selBJetsAK4_medium, evtWeight);
    selHistManager->met_->fillHistograms(met, mhtP4, met_LD, evtWeight);
    selHistManager->metFilters_->fillHistograms(metFilters, evtWeight);
    selHistManager->triggers_1e_->fillHistograms(triggers_1e, evtWeight);
    selHistManager->triggers_2e_->fillHistograms(triggers_2e, evtWeight);
    selHistManager->triggers_1mu_->fillHistograms(triggers_1mu, evtWeight);
    selHistManager->triggers_2mu_->fillHistograms(triggers_2mu, evtWeight);
    selHistManager->evt_->fillHistograms(
      selElectrons.size(),
      selMuons.size(),
      numSelJetsAK4_nonVBF,
      selBJetsAK4_loose.size(),
      selBJetsAK4_medium.size(),
      HT, 
      STMET,
      m_bb, dR_bb, dPhi_bb, pT_bb, 
      m_ll, dR_ll, dPhi_ll, pT_ll,
      m_bbll, dPhi_bbll, pT_bbll, 
      m_bbllMEt, m_HH_hme, dPhi_bbllMEt, pT_bbllMEt, Smin_bbllMEt,
      vbf_m_jj, vbf_dEta_jj,
      evtWeight);
    if ( isMC ) {
      selHistManager->genEvtHistManager_afterCuts_->fillHistograms(genElectrons, genMuons, genHadTaus, genPhotons, genJets, evtWeight_inclusive);
      selHistManager->lheInfoHistManager_afterCuts_->fillHistograms(*lheInfoReader, evtWeight);
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
    int numJets_forCategorization = ( selJetAK8_Hbb ) ? numJets_nonHbb + 2 : numJets_nonHbb; // CV: add the two subjets of the AK8 "fat" jet
    int type_Hbb = ( selJetAK8_Hbb ) ? kHbb_boosted : kHbb_resolved; 
    int type_vbf = ( isVBF         ) ?  kVBF_tagged : kVBF_nottagged;
    for ( std::vector<categoryEntryType>::const_iterator category = categories_evt.begin();
	  category != categories_evt.end(); ++category ) {
      if ( (category->numElectrons_    ==             -1 || numElectrons              == category->numElectrons_)    &&
	   (category->numMuons_        ==             -1 || numMuons                  == category->numMuons_)        &&
	   (category->numBJets_medium_ ==             -1 || numBJets_medium           == category->numBJets_medium_) &&
	   (category->numBJets_loose_  ==             -1 || numBJets_loose            == category->numBJets_loose_)  &&
	   (category->minNumJets_      ==             -1 || numJets_forCategorization >= category->minNumJets_)      && 
	   (category->maxNumJets_      ==             -1 || numJets_forCategorization <= category->maxNumJets_)      && 
	   (category->type_Hbb_        == kHbb_undefined || type_Hbb                  == category->type_Hbb_)        &&
	   (category->type_vbf_        == kVBF_undefined || type_vbf                  == category->type_vbf_)        ) {
	if ( selHistManager->evt_in_categories_.find(category->name_) != selHistManager->evt_in_categories_.end() ) {
	  selHistManager->evt_in_categories_[category->name_]->fillHistograms(
            selElectrons.size(),
	    selMuons.size(),
	    numSelJetsAK4_nonVBF,
	    selBJetsAK4_loose.size(),
	    selBJetsAK4_medium.size(),
	    HT, 
	    STMET,
	    m_bb, dR_bb, dPhi_bb, pT_bb, 
	    m_ll, dR_ll, dPhi_ll, pT_ll,
	    m_bbll, dPhi_bbll, pT_bbll, 
	    m_bbllMEt, m_HH_hme, dPhi_bbllMEt, pT_bbllMEt, Smin_bbllMEt,
	    vbf_m_jj, vbf_dEta_jj,
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
  delete genTauLeptonReader;
  delete lheInfoReader;

  hltPaths_delete(triggers_1e);
  hltPaths_delete(triggers_2e);
  hltPaths_delete(triggers_1mu);
  hltPaths_delete(triggers_2mu);

  delete inputTree;

  clock.Show("analyze_hh_bbWW_DYctrl");

  return EXIT_SUCCESS;
}
