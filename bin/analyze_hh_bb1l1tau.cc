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
#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTau.h" // RecoHadTau
#include "tthAnalysis/HiggsToTauTau/interface/RecoJet.h" // RecoJet
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEt.h" // RecoMEt
#include "tthAnalysis/HiggsToTauTau/interface/GenLepton.h" // GenLepton
#include "tthAnalysis/HiggsToTauTau/interface/GenJet.h" // GenJet
#include "tthAnalysis/HiggsToTauTau/interface/GenHadTau.h" // GenHadTau
#include "tthAnalysis/HiggsToTauTau/interface/LeptonFakeRateInterface.h" // LeptonFakeRateInterface
#include "tthAnalysis/HiggsToTauTau/interface/JetToTauFakeRateInterface.h" // JetToTauFakeRateInterface
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronReader.h" // RecoElectronReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonReader.h" // RecoMuonReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTauReader.h" // RecoHadTauReader
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
#include "tthAnalysis/HiggsToTauTau/interface/convert_to_ptrs.h" // convert_to_ptrs
#include "tthAnalysis/HiggsToTauTau/interface/ParticleCollectionCleaner.h" // RecoElectronCollectionCleaner, RecoMuonCollectionCleaner, RecoHadTauCollectionCleaner, RecoJetCollectionCleaner
#include "tthAnalysis/HiggsToTauTau/interface/ParticleCollectionGenMatcher.h" // RecoElectronCollectionGenMatcher, RecoMuonCollectionGenMatcher, RecoHadTauCollectionGenMatcher, RecoJetCollectionGenMatcher
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronCollectionSelectorLoose.h" // RecoElectronCollectionSelectorLoose
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronCollectionSelectorFakeable.h" // RecoElectronCollectionSelectorFakeable
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronCollectionSelectorTight.h" // RecoElectronCollectionSelectorTight
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonCollectionSelectorLoose.h" // RecoMuonCollectionSelectorLoose
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonCollectionSelectorFakeable.h" // RecoMuonCollectionSelectorFakeable
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonCollectionSelectorTight.h" // RecoMuonCollectionSelectorTight
#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTauCollectionSelectorLoose.h" // RecoHadTauCollectionSelectorLoose
#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTauCollectionSelectorFakeable.h" // RecoHadTauCollectionSelectorFakeable
#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTauCollectionSelectorTight.h" // RecoHadTauCollectionSelectorTight
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetCollectionSelector.h" // RecoJetCollectionSelector
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetCollectionSelectorBtag.h" // RecoJetCollectionSelectorBtagLoose, RecoJetCollectionSelectorBtagMedium
#include "tthAnalysis/HiggsToTauTau/interface/RunLumiEventSelector.h" // RunLumiEventSelector
#include "tthAnalysis/HiggsToTauTau/interface/MEtFilterSelector.h" // MEtFilterSelector
#include "tthAnalysis/HiggsToTauTau/interface/ElectronHistManager.h" // ElectronHistManager
#include "tthAnalysis/HiggsToTauTau/interface/MuonHistManager.h" // MuonHistManager
#include "tthAnalysis/HiggsToTauTau/interface/HadTauHistManager.h" // HadTauHistManager
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
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // getBTagWeight_option, getHadTau_genPdgId, isHigherPt, isMatched
#include "tthAnalysis/HiggsToTauTau/interface/leptonGenMatchingAuxFunctions.h" // getLeptonGenMatch_definitions_1lepton, getLeptonGenMatch_string, getLeptonGenMatch_int
#include "tthAnalysis/HiggsToTauTau/interface/hadTauGenMatchingAuxFunctions.h" // getHadTauGenMatch_definitions_1tau, getHadTauGenMatch_string, getHadTauGenMatch_int
#include "tthAnalysis/HiggsToTauTau/interface/fakeBackgroundAuxFunctions.h"
#include "tthAnalysis/HiggsToTauTau/interface/generalAuxFunctions.h" // format_vstring
#include "tthAnalysis/HiggsToTauTau/interface/mvaInputVariables.h" // comp_lep1_conePt, comp_lep2_conePt
#include "tthAnalysis/HiggsToTauTau/interface/hltPath.h" // hltPath, create_hltPaths, hltPaths_isTriggered, hltPaths_delete
#include "tthAnalysis/HiggsToTauTau/interface/hltPathReader.h" // hltPathReader
#include "tthAnalysis/HiggsToTauTau/interface/Data_to_MC_CorrectionInterface_2016.h"
#include "tthAnalysis/HiggsToTauTau/interface/Data_to_MC_CorrectionInterface_2017.h"
#include "tthAnalysis/HiggsToTauTau/interface/Data_to_MC_CorrectionInterface_2018.h"
#include "tthAnalysis/HiggsToTauTau/interface/Data_to_MC_CorrectionInterface_1l_1tau_trigger.h" // Data_to_MC_CorrectionInterface_1l_1tau_trigger
#include "tthAnalysis/HiggsToTauTau/interface/DYMCReweighting.h" // DYMCReweighting
#include "tthAnalysis/HiggsToTauTau/interface/lutAuxFunctions.h" // loadTH2, get_sf_from_TH2
#include "tthAnalysis/HiggsToTauTau/interface/L1PreFiringWeightReader.h" // L1PreFiringWeightReader
#include "tthAnalysis/HiggsToTauTau/interface/cutFlowTable.h" // cutFlowTableType
#include "tthAnalysis/HiggsToTauTau/interface/NtupleFillerBDT.h" // NtupleFillerBDT
#include "tthAnalysis/HiggsToTauTau/interface/TTreeWrapper.h" // TTreeWrapper
#include "tthAnalysis/HiggsToTauTau/interface/hltFilter.h" // hltFilter()
#include "tthAnalysis/HiggsToTauTau/interface/EvtWeightManager.h" // EvtWeightManager
#include "tthAnalysis/HiggsToTauTau/interface/mT2_2particle.h" // mT2_2particle
#include "tthAnalysis/HiggsToTauTau/interface/mT2_3particle.h" // mT2_3particle

#include "hhAnalysis/multilepton/interface/EventInfoHH.h" // EventInfoHH
#include "hhAnalysis/multilepton/interface/EventInfoHHReader.h" // EventInfoHHReader

#include "hhAnalysis/bbww/interface/EvtHistManager_hh_bb1l1tau.h" // EvtHistManager_hh_bb1l1tau
#include "hhAnalysis/bbww/interface/RecoJetCollectionSelectorAK8_hh_bbWW_Hbb.h" // RecoJetSelectorAK8_hh_bbWW_Hbb

#include "TauAnalysis/ClassicSVfit/interface/ClassicSVfit.h" // ClassicSVfit
#include "TauAnalysis/ClassicSVfit/interface/MeasuredTauLepton.h" // classic_svFit::MeasuredTauLepton
#include "TauAnalysis/ClassicSVfit/interface/svFitHistogramAdapter.h"
#include "TauAnalysis/ClassicSVfit/interface/svFitAuxFunctions.h"

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

//const int hadTauSelection_antiElectron = 1; // vLoose
//const int hadTauSelection_antiMuon = 1; // Loose
const int hadTauSelection_antiElectron = -1; // not applied
const int hadTauSelection_antiMuon = -1; // not applied

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
    if      ( numElectrons_ >= 1 ) name_ += "1e1tau";
    else if ( numMuons_     >= 1 ) name_ += "1mu1tau";
    else name_ += "1l1tau";
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

  std::cout << "<analyze_hh_bb1l1tau>:" << std::endl;

//--- keep track of time it takes the macro to execute
  TBenchmark clock;
  clock.Start("analyze_hh_bb1l1tau");

//--- read python configuration parameters
  if ( !edm::readPSetsFrom(argv[1])->existsAs<edm::ParameterSet>("process") )
    throw cms::Exception("analyze_hh_bb1l1tau")
      << "No ParameterSet 'process' found in configuration file = " << argv[1] << " !!\n";

  edm::ParameterSet cfg = edm::readPSetsFrom(argv[1])->getParameter<edm::ParameterSet>("process");

  edm::ParameterSet cfg_analyze = cfg.getParameter<edm::ParameterSet>("analyze_hh_bb1l1tau");

  std::string treeName = cfg_analyze.getParameter<std::string>("treeName");

  std::string process_string = cfg_analyze.getParameter<std::string>("process");
  const bool isMC_tH = process_string == "TH";
  const bool isMC_ttH = process_string == "TTH";

  std::string histogramDir = cfg_analyze.getParameter<std::string>("histogramDir");
  bool isMCClosure_e = histogramDir.find("mcClosure_e") != std::string::npos;
  bool isMCClosure_m = histogramDir.find("mcClosure_m") != std::string::npos;
  bool isMCClosure_t = histogramDir.find("mcClosure_t") != std::string::npos;

  std::string era_string = cfg_analyze.getParameter<std::string>("era");
  const int era = get_era(era_string);

  vstring triggerNames_1e = cfg_analyze.getParameter<vstring>("triggers_1e");
  std::vector<hltPath*> triggers_1e = create_hltPaths(triggerNames_1e, "triggers_1e");
  bool use_triggers_1e = cfg_analyze.getParameter<bool>("use_triggers_1e");
  vstring triggerNames_1e1tau = cfg_analyze.getParameter<vstring>("triggers_1e1tau");
  std::vector<hltPath*> triggers_1e1tau = create_hltPaths(triggerNames_1e1tau, "triggers_1e1tau");
  bool use_triggers_1e1tau = cfg_analyze.getParameter<bool>("use_triggers_1e1tau");
  vstring triggerNames_1mu = cfg_analyze.getParameter<vstring>("triggers_1mu");
  std::vector<hltPath*> triggers_1mu = create_hltPaths(triggerNames_1mu, "triggers_1mu");
  bool use_triggers_1mu = cfg_analyze.getParameter<bool>("use_triggers_1mu");
  vstring triggerNames_1mu1tau = cfg_analyze.getParameter<vstring>("triggers_1mu1tau");
  std::vector<hltPath*> triggers_1mu1tau = create_hltPaths(triggerNames_1mu1tau, "triggers_1mu1tau");
  bool use_triggers_1mu1tau = cfg_analyze.getParameter<bool>("use_triggers_1mu1tau");

  bool apply_offline_e_trigger_cuts_1e = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_1e");
  bool apply_offline_e_trigger_cuts_1e1tau = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_1e1tau");
  bool apply_offline_e_trigger_cuts_1mu = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_1mu");
  bool apply_offline_e_trigger_cuts_1mu1tau = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_1mu1tau");

  const std::string electronSelection_string = cfg_analyze.getParameter<std::string>("electronSelection");
  const std::string muonSelection_string     = cfg_analyze.getParameter<std::string>("muonSelection");
  std::cout << "electronSelection_string = " << electronSelection_string << "\n"
               "muonSelection_string     = " << muonSelection_string     << '\n'
  ;
  const int electronSelection = get_selection(electronSelection_string);
  const int muonSelection     = get_selection(muonSelection_string);

  bool apply_leptonGenMatching = cfg_analyze.getParameter<bool>("apply_leptonGenMatching");
  std::vector<leptonGenMatchEntry> leptonGenMatch_definitions = getLeptonGenMatch_definitions_1lepton(apply_leptonGenMatching);
  std::cout << "leptonGenMatch_definitions:" << std::endl;
  std::cout << leptonGenMatch_definitions;

  TString hadTauSelection_string = cfg_analyze.getParameter<std::string>("hadTauSelection").data();
  TObjArray* hadTauSelection_parts = hadTauSelection_string.Tokenize("|");
  assert(hadTauSelection_parts->GetEntries() >= 1);
  const std::string hadTauSelection_part1 = (dynamic_cast<TObjString*>(hadTauSelection_parts->At(0)))->GetString().Data();
  const int hadTauSelection = get_selection(hadTauSelection_part1);
  std::string hadTauSelection_part2 = ( hadTauSelection_parts->GetEntries() == 2 ) ? (dynamic_cast<TObjString*>(hadTauSelection_parts->At(1)))->GetString().Data() : "";
  delete hadTauSelection_parts;

  bool apply_hadTauGenMatching = cfg_analyze.getParameter<bool>("apply_hadTauGenMatching");
  std::vector<hadTauGenMatchEntry> hadTauGenMatch_definitions = getHadTauGenMatch_definitions_1tau(apply_hadTauGenMatching);
  std::cout << "hadTauGenMatch_definitions:" << std::endl;
  std::cout << hadTauGenMatch_definitions;

  enum { kOS, kSS, kDisabled };
  std::string chargeSumSelection_string = cfg_analyze.getParameter<std::string>("chargeSumSelection");
  int chargeSumSelection = -1;
  if      ( chargeSumSelection_string == "OS"       ) chargeSumSelection = kOS;
  else if ( chargeSumSelection_string == "SS"       ) chargeSumSelection = kSS;
  else if ( chargeSumSelection_string == "disabled" ) chargeSumSelection = kDisabled;
  else throw cms::Exception("analyze_hh_bb1l1tau")
    << "Invalid Configuration parameter 'chargeSumSelection' = " << chargeSumSelection_string << " !!\n";

  vstring evtCategoryNames = cfg_analyze.getParameter<vstring>("evtCategories");
  std::cout << "evtCategories = " << format_vstring(evtCategoryNames) << std::endl;

  bool isMC = cfg_analyze.getParameter<bool>("isMC");
  bool hasLHE = cfg_analyze.getParameter<bool>("hasLHE");
  std::string central_or_shift = cfg_analyze.getParameter<std::string>("central_or_shift");
  double lumiScale = ( process_string != "data_obs" ) ? cfg_analyze.getParameter<double>("lumiScale") : 1.;
  bool apply_genWeight = cfg_analyze.getParameter<bool>("apply_genWeight");
  bool apply_l1PreFireWeight = cfg_analyze.getParameter<bool>("apply_l1PreFireWeight");
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
  const int jetToLeptonFakeRate_option        = getJetToLeptonFR_option       (central_or_shift);
  const int hadTauPt_option                   = getHadTauPt_option            (central_or_shift);
  const int jetToTauFakeRate_option           = getJetToTauFR_option          (central_or_shift);
  const int lheScale_option                   = getLHEscale_option            (central_or_shift);
  const int jetBtagSF_option                  = getBTagWeight_option          (central_or_shift);
  const int dyMCReweighting_option            = getDYMCReweighting_option     (central_or_shift);
  const PUsys puSys_option                    = getPUsys_option               (central_or_shift);
  const L1PreFiringWeightSys l1PreFire_option = getL1PreFiringWeightSys_option(central_or_shift);

  const int met_option   = useNonNominal_jetmet ? kMEt_central_nonNominal : getMET_option(central_or_shift, isMC);
  const int jetPt_option = useNonNominal_jetmet ? kMEt_central_nonNominal : getJet_option(central_or_shift, isMC);

  std::cout
    << "central_or_shift = "                << central_or_shift             << "\n"
       " -> jetToLeptonFakeRate_option  = " << jetToLeptonFakeRate_option   << "\n"
       " -> hadTauPt_option             = " << hadTauPt_option              << "\n"
       " -> jetToTauFakeRate_option     = " << jetToTauFakeRate_option      << "\n"
       " -> lheScale_option             = " << lheScale_option              << "\n"
       " -> jetBtagSF_option            = " << jetBtagSF_option             << "\n"
       " -> met_option                  = " << met_option                   << "\n"
       " -> jetPt_option                = " << jetPt_option                 << "\n"
       " -> puSys_option                = " << as_integer(puSys_option)     << "\n"
       " -> dyMCReweighting_option      = " << dyMCReweighting_option       << "\n"
       " -> l1PreFire_option            = " << as_integer(l1PreFire_option) << '\n'
  ;

  DYMCReweighting* dyReweighting = nullptr;
  if ( apply_DYMCReweighting ) {
    dyReweighting = new DYMCReweighting(era, dyMCReweighting_option);
  }

  edm::ParameterSet cfg_dataToMCcorrectionInterface;
  cfg_dataToMCcorrectionInterface.addParameter<std::string>("era", era_string);
  cfg_dataToMCcorrectionInterface.addParameter<std::string>("hadTauSelection", hadTauSelection_part2);
  cfg_dataToMCcorrectionInterface.addParameter<int>("hadTauSelection_antiElectron", hadTauSelection_antiElectron);
  cfg_dataToMCcorrectionInterface.addParameter<int>("hadTauSelection_antiMuon", hadTauSelection_antiMuon);
  cfg_dataToMCcorrectionInterface.addParameter<std::string>("central_or_shift", central_or_shift);
  cfg_dataToMCcorrectionInterface.addParameter<bool>("isDEBUG", isDEBUG);
  Data_to_MC_CorrectionInterface_Base * dataToMCcorrectionInterface = nullptr;
  switch(era)
  {
    case kEra_2016: dataToMCcorrectionInterface = new Data_to_MC_CorrectionInterface_2016(cfg_dataToMCcorrectionInterface); break;
    case kEra_2017: dataToMCcorrectionInterface = new Data_to_MC_CorrectionInterface_2017(cfg_dataToMCcorrectionInterface); break;
    case kEra_2018: dataToMCcorrectionInterface = new Data_to_MC_CorrectionInterface_2018(cfg_dataToMCcorrectionInterface); break;
    default: throw cmsException("analyze_hh_bb1l1tau", __LINE__) << "Invalid era = " << era;
  }
  Data_to_MC_CorrectionInterface_1l_1tau_trigger* dataToMCcorrectionInterface_1l_1tau_trigger = new Data_to_MC_CorrectionInterface_1l_1tau_trigger(cfg_dataToMCcorrectionInterface);

  std::string applyFakeRateWeights_string = cfg_analyze.getParameter<std::string>("applyFakeRateWeights");
  int applyFakeRateWeights = -1;
  if      ( applyFakeRateWeights_string == "disabled" ) applyFakeRateWeights = kFR_disabled;
  else if ( applyFakeRateWeights_string == "enabled"  ) applyFakeRateWeights = kFR_enabled;
  else throw cms::Exception("analyze_hh_bb1l1tau")
    << "Invalid Configuration parameter 'applyFakeRateWeights' = " << applyFakeRateWeights_string << " !!\n";

  LeptonFakeRateInterface* leptonFakeRateInterface = 0;
  if ( applyFakeRateWeights == kFR_enabled ) {
    edm::ParameterSet cfg_leptonFakeRateWeight = cfg_analyze.getParameter<edm::ParameterSet>("leptonFakeRateWeight");
    leptonFakeRateInterface = new LeptonFakeRateInterface(cfg_leptonFakeRateWeight, jetToLeptonFakeRate_option);
  }

  JetToTauFakeRateInterface* jetToTauFakeRateInterface = 0;
  if ( applyFakeRateWeights == kFR_enabled ) {
    edm::ParameterSet cfg_hadTauFakeRateWeight = cfg_analyze.getParameter<edm::ParameterSet>("hadTauFakeRateWeight");
    cfg_hadTauFakeRateWeight.addParameter<std::string>("hadTauSelection", hadTauSelection_part2);
    jetToTauFakeRateInterface = new JetToTauFakeRateInterface(cfg_hadTauFakeRateWeight, jetToTauFakeRate_option);
  }

  bool fillGenEvtHistograms = cfg_analyze.getParameter<bool>("fillGenEvtHistograms");
  edm::ParameterSet cfg_EvtYieldHistManager = cfg_analyze.getParameter<edm::ParameterSet>("cfgEvtYieldHistManager");

  std::string branchName_electrons = cfg_analyze.getParameter<std::string>("branchName_electrons");
  std::string branchName_muons = cfg_analyze.getParameter<std::string>("branchName_muons");
  std::string branchName_hadTaus = cfg_analyze.getParameter<std::string>("branchName_hadTaus");
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

  const double maxAbsEta_lepton = 2.1;
  const double minPt_e = 30.;
  const double minPt_mu = 25.;
  const double minPt_hadTau = 30.;

  fwlite::InputSource inputFiles(cfg);
  int maxEvents = inputFiles.maxEvents();
  std::cout << " maxEvents = " << maxEvents << std::endl;
  unsigned reportEvery = inputFiles.reportAfter();

  fwlite::OutputFiles outputFile(cfg);
  fwlite::TFileService fs = fwlite::TFileService(outputFile.file().data());

  TTreeWrapper* inputTree = new TTreeWrapper(treeName.data(), inputFiles.files(), maxEvents);
  std::cout << "Loaded " << inputTree->getFileCount() << " file(s)." << std::endl;

//--- declare event-level variables
  EventInfoHH eventInfo(isMC);
  EventInfoHHReader eventInfoReader(&eventInfo, puSys_option);
  inputTree->registerReader(&eventInfoReader);

  hltPathReader hltPathReader_instance({ triggers_1e, triggers_1e1tau, triggers_1mu, triggers_1mu1tau });
  inputTree->registerReader(&hltPathReader_instance);

  if ( eventWeightManager ) {
    inputTree->registerReader(eventWeightManager);
  }

  L1PreFiringWeightReader * l1PreFiringWeightReader = nullptr;
  if(apply_l1PreFireWeight)
  {
    l1PreFiringWeightReader = new L1PreFiringWeightReader(era, l1PreFire_option);
    inputTree->registerReader(l1PreFiringWeightReader);
  }

//--- declare particle collections
  const bool readGenObjects = isMC && !redoGenMatching;
  RecoMuonReader* muonReader = new RecoMuonReader(era, branchName_muons, isMC, readGenObjects);
  inputTree->registerReader(muonReader);
  RecoMuonCollectionGenMatcher muonGenMatcher;
  RecoMuonCollectionSelectorLoose preselMuonSelector(era, -1, isDEBUG);
  RecoMuonCollectionSelectorFakeable fakeableMuonSelector(era, -1, isDEBUG);
  RecoMuonCollectionSelectorTight tightMuonSelector(era, -1, isDEBUG);

  RecoElectronReader* electronReader = new RecoElectronReader(era, branchName_electrons, isMC, readGenObjects);
  electronReader->readUncorrected(useNonNominal);
  inputTree->registerReader(electronReader);
  RecoElectronCollectionGenMatcher electronGenMatcher;
  RecoElectronCollectionCleaner electronCleaner(0.05, isDEBUG);
  RecoElectronCollectionSelectorLoose preselElectronSelector(era, -1, isDEBUG);
  RecoElectronCollectionSelectorFakeable fakeableElectronSelector(era, -1, isDEBUG);
  RecoElectronCollectionSelectorTight tightElectronSelector(era, -1, isDEBUG);

  RecoHadTauReader* hadTauReader = new RecoHadTauReader(era, branchName_hadTaus, isMC, readGenObjects);
  hadTauReader->setHadTauPt_central_or_shift(hadTauPt_option);
  inputTree->registerReader(hadTauReader);
  RecoHadTauCollectionGenMatcher hadTauGenMatcher;
  RecoHadTauCollectionCleaner hadTauCleaner(0.3, isDEBUG);
  RecoHadTauCollectionSelectorLoose preselHadTauSelector(era, -1, isDEBUG);
  preselHadTauSelector.set_if_looser(hadTauSelection_part2);
  preselHadTauSelector.set_min_antiElectron(hadTauSelection_antiElectron);
  preselHadTauSelector.set_min_antiMuon(hadTauSelection_antiMuon);
  RecoHadTauCollectionSelectorFakeable fakeableHadTauSelector(era, -1, isDEBUG);
  fakeableHadTauSelector.set_if_looser(hadTauSelection_part2);
  fakeableHadTauSelector.set_min_antiElectron(hadTauSelection_antiElectron);
  fakeableHadTauSelector.set_min_antiMuon(hadTauSelection_antiMuon);
  RecoHadTauCollectionSelectorTight tightHadTauSelector(era, -1, isDEBUG);
  tightHadTauSelector.set(hadTauSelection_part2);
  tightHadTauSelector.set_min_antiElectron(hadTauSelection_antiElectron);
  tightHadTauSelector.set_min_antiMuon(hadTauSelection_antiMuon);

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
    lheInfoReader = new LHEInfoReader(hasLHE);
    inputTree->registerReader(lheInfoReader);
  }

  const std::vector<edm::ParameterSet> tHweights = cfg_analyze.getParameterSetVector("tHweights");
  if((isMC_tH || isMC_ttH) && ! tHweights.empty())
  {
    eventInfo.loadWeight_tH(tHweights);
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

  struct selHistManagerType
  {
    ElectronHistManager* electrons_;
    MuonHistManager* muons_;
    HadTauHistManager* hadTaus_;
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
    EvtHistManager_hh_bb1l1tau* evt_;
    std::map<std::string, EvtHistManager_hh_bb1l1tau*> evt_in_categories_;
    GenEvtHistManager* genEvtHistManager_afterCuts_;
    LHEInfoHistManager* lheInfoHistManager_afterCuts_;
    std::map<std::string, LHEInfoHistManager*> lheInfoHistManager_afterCuts_in_categories_;
    EvtYieldHistManager* evtYield_;
    WeightHistManager* weights_;
  };
  typedef std::map<int, selHistManagerType*> int_to_selHistManagerMap;
  std::map<int, int_to_selHistManagerMap> selHistManagers;
  std::vector<categoryEntryType> categories_evt;
  for ( int type_Hbb = kHbb_undefined; type_Hbb <= kHbb_boosted; ++type_Hbb ) {
    for ( int type_vbf = kVBF_undefined; type_vbf <= kVBF_tagged; ++type_vbf ) {
      if ( !(type_Hbb == kHbb_undefined && type_vbf == kVBF_undefined) ) {
	addCategory_conditionally(categories_evt, categoryEntryType(-1, -1, -1, -1, type_Hbb, type_vbf), evtCategoryNames); // hh_bb1l1tau
      }
      addCategory_conditionally(categories_evt, categoryEntryType(-1, -1,  2, -1, type_Hbb, type_vbf), evtCategoryNames); // hh_2bM1l1tau
      addCategory_conditionally(categories_evt, categoryEntryType(-1, -1,  1,  2, type_Hbb, type_vbf), evtCategoryNames); // hh_1bM1bL1l1tau
      addCategory_conditionally(categories_evt, categoryEntryType(-1, -1,  1, -1, type_Hbb, type_vbf), evtCategoryNames); // hh_1bM1l1tau
      addCategory_conditionally(categories_evt, categoryEntryType( 1, -1, -1, -1, type_Hbb, type_vbf), evtCategoryNames); // hh_bb1e1tau
      addCategory_conditionally(categories_evt, categoryEntryType( 1, -1,  2, -1, type_Hbb, type_vbf), evtCategoryNames); // hh_2bM1e1tau
      addCategory_conditionally(categories_evt, categoryEntryType( 1, -1,  1,  2, type_Hbb, type_vbf), evtCategoryNames); // hh_1bM1bL1e1tau
      addCategory_conditionally(categories_evt, categoryEntryType( 1, -1,  1, -1, type_Hbb, type_vbf), evtCategoryNames); // hh_1bM1e1tau
      addCategory_conditionally(categories_evt, categoryEntryType(-1,  1, -1, -1, type_Hbb, type_vbf), evtCategoryNames); // hh_bb1mu1tau
      addCategory_conditionally(categories_evt, categoryEntryType(-1,  1,  2, -1, type_Hbb, type_vbf), evtCategoryNames); // hh_2bM1mu1tau
      addCategory_conditionally(categories_evt, categoryEntryType(-1,  1,  1,  2, type_Hbb, type_vbf), evtCategoryNames); // hh_1bM1bL1mu1tau
      addCategory_conditionally(categories_evt, categoryEntryType(-1,  1,  1, -1, type_Hbb, type_vbf), evtCategoryNames); // hh_1bM1mu1tau
    }
  }
  // check that all categories specified in python configuration (by evtCategories) have been added
  vstring undefinedEvtCategories;
  for ( vstring::const_iterator evtCategoryName = evtCategoryNames.begin();
	evtCategoryName != evtCategoryNames.end(); ++evtCategoryName ) {
    if ( (*evtCategoryName) == "hh_bb1l1tau" ) continue; // CV: skip "inclusive" event category, as it is added automatically
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
  if ( undefinedEvtCategories.size() >= 1 ) {
    throw cms::Exception("analyze_hh_bb1l1tau")
      << "Invalid Configuration parameter 'evtCategories'. The following event categories are undefined: " << format_vstring(undefinedEvtCategories) << " !!\n";
  }
  for ( std::vector<leptonGenMatchEntry>::const_iterator leptonGenMatch_definition = leptonGenMatch_definitions.begin();
        leptonGenMatch_definition != leptonGenMatch_definitions.end(); ++leptonGenMatch_definition ) {
    for ( std::vector<hadTauGenMatchEntry>::const_iterator hadTauGenMatch_definition = hadTauGenMatch_definitions.begin();
          hadTauGenMatch_definition != hadTauGenMatch_definitions.end(); ++hadTauGenMatch_definition ) {

      std::string process_and_genMatch = process_string;
      if ( apply_leptonGenMatching ) process_and_genMatch += leptonGenMatch_definition->name_;
      if ( apply_leptonGenMatching && apply_hadTauGenMatching ) process_and_genMatch += "&";
      if ( apply_hadTauGenMatching ) process_and_genMatch += hadTauGenMatch_definition->name_;
      int idxLepton = leptonGenMatch_definition->idx_;
      int idxHadTau = hadTauGenMatch_definition->idx_;

      selHistManagerType* selHistManager = new selHistManagerType();
      selHistManager->electrons_ = new ElectronHistManager(makeHistManager_cfg(process_and_genMatch,
        Form("%s/sel/electrons", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
      selHistManager->electrons_->bookHistograms(fs);
      selHistManager->muons_ = new MuonHistManager(makeHistManager_cfg(process_and_genMatch,
        Form("%s/sel/muons", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
      selHistManager->muons_->bookHistograms(fs);
      selHistManager->hadTaus_ = new HadTauHistManager(makeHistManager_cfg(process_and_genMatch,
        Form("%s/sel/hadTaus", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
      selHistManager->hadTaus_->bookHistograms(fs);
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
      selHistManager->evt_ = new EvtHistManager_hh_bb1l1tau(makeHistManager_cfg(process_and_genMatch,
        Form("%s/sel/evt", histogramDir.data()), era_string, era_string, central_or_shift));
      selHistManager->evt_->bookHistograms(fs);
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
        histogramDir_category.ReplaceAll("hh_bb1l1tau", category->name_.data());
        selHistManager->evt_in_categories_[category->name_] = new EvtHistManager_hh_bb1l1tau(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/evt", histogramDir_category.Data()), era_string, central_or_shift));
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
      selHistManagers[idxLepton][idxHadTau] = selHistManager;
    }
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
      "lep_pt", "lep_conePt", "lep_eta",
      "hadTau_pt", "hadTau_eta",
      "bjet1_pt", "bjet1_eta",
      "bjet2_pt", "bjet2_eta",
      "met", "mht", "met_LD",
      "HT", "STMET",
      "m_Hbb", "dR_Hbb", "dPhi_Hbb", "pT_Hbb",
      "m_ltau", "dR_ltau", "dPhi_ltau", "pT_ltau",
      "min_dPhi_ltauMEt", "max_dPhi_ltauMEt",
      "m_Hww", "pT_Hww",
      "dR_b1lep", "dR_b1hadTau", "dR_b2lep", "dR_b2hadTau",
      "m_HHvis", "pT_HHvis", "dPhi_HHvis",
      "m_HH", "pT_HH", "dPhi_HH",
      "mT2_W", "mT2_top_2particle", "mT2_top_3particle",
      "vbf_jet1_pt", "vbf_jet1_eta", "vbf_jet2_pt", "vbf_jet2_eta", "vbf_m_jj", "vbf_dEta_jj",
      "genWeight", "evtWeight"
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
    ">= 1 presel leptons",
    ">= 1 sel leptons",
    Form("lepton pT > %.0f(e)/%.0f(mu) GeV", minPt_e, minPt_mu),
    Form("lepton abs(eta) < %.1f", maxAbsEta_lepton),
    ">= 1 presel taus",
    ">= 1 sel taus",
    Form("hadTau pT > %.0f GeV", minPt_hadTau),
    Form("sel lepton+tau %s charge", chargeSumSelection_string.data()),
    "<= 1 tight leptons",
    "fakeable lepton trigger match",
    "HLT filter matching",
    ">= 2 jets from H->bb",
    ">= 1 medium b-jet",
    "m(ltau) < 76 GeV",
    "SVFit mass veto",
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
      if(apply_genWeight)         evtWeight_inclusive *= boost::math::sign(eventInfo.genWeight);
      if(apply_DYMCReweighting)   evtWeight_inclusive *= dyReweighting->getWeight(genTauLeptons);
      if(eventWeightManager)      evtWeight_inclusive *= eventWeightManager->getWeight();
      if(l1PreFiringWeightReader) evtWeight_inclusive *= l1PreFiringWeightReader->getWeight();
      lheInfoReader->read();
      evtWeight_inclusive *= lheInfoReader->getWeight_scale(lheScale_option);
      evtWeight_inclusive *= eventInfo.pileupWeight;
      evtWeight_inclusive *= eventInfo.genWeight_tH();
      evtWeight_inclusive *= lumiScale;
      genEvtHistManager_beforeCuts->fillHistograms(genElectrons, genMuons, genHadTaus, genPhotons, genJets, evtWeight_inclusive);
      if(eventWeightManager)
      {
        genEvtHistManager_beforeCuts->fillHistograms(eventWeightManager, evtWeight_inclusive);
      }
    }

    bool isTriggered_1e = hltPaths_isTriggered(triggers_1e, isDEBUG);
    bool isTriggered_1e1tau = hltPaths_isTriggered(triggers_1e1tau, isDEBUG);
    bool isTriggered_1mu = hltPaths_isTriggered(triggers_1mu, isDEBUG);
    bool isTriggered_1mu1tau = hltPaths_isTriggered(triggers_1mu1tau, isDEBUG);

    bool selTrigger_1e = use_triggers_1e && isTriggered_1e;
    bool selTrigger_1e1tau = use_triggers_1e1tau && isTriggered_1e1tau;
    bool selTrigger_1mu = use_triggers_1mu && isTriggered_1mu;
    bool selTrigger_1mu1tau = use_triggers_1mu1tau && isTriggered_1mu1tau;

    if ( !(selTrigger_1e || selTrigger_1e1tau || selTrigger_1mu || selTrigger_1mu1tau) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
        std::cout << " (selTrigger_1e = " << selTrigger_1e
                  << ", selTrigger_1e1tau = " << selTrigger_1e1tau
                  << ", selTrigger_1mu = " << selTrigger_1mu
                  << ", selTrigger_1mu1tau = " << selTrigger_1mu1tau << ")" << std::endl;
      }
      continue;
    }

//--- Rank triggers by priority and ignore triggers of lower priority if a trigger of higher priority has fired for given event;
//    the ranking of the triggers is as follows: 1mu || 1mu1tau, 1e || 1e1tau
// CV: This logic is necessary to avoid that the same event is selected multiple times when processing different primary datasets.
//     The mu+tau (e+tau) cross trigger is stored in the same primary dataset as the single muon (single electron) trigger during the 2017 data-taking period!!
    if ( !isMC && !isDEBUG ) {
      //bool isTriggered_SingleElectron = isTriggered_1e || isTriggered_1e1tau;
      bool isTriggered_SingleMuon = isTriggered_1mu || isTriggered_1mu1tau;
      //bool isTriggered_Tau = isTriggered_1e1tau || isTriggered_1mu1tau;

      bool selTrigger_SingleElectron = selTrigger_1e || selTrigger_1e1tau;
      //bool selTrigger_SingleMuon = selTrigger_1mu || selTrigger_1mu1tau;
      //bool selTrigger_Tau = selTrigger_1e1tau || selTrigger_1mu1tau;

      if ( selTrigger_SingleElectron && isTriggered_SingleMuon ) {
        if ( run_lumi_eventSelector ) {
          std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
          std::cout << " (selTrigger_SingleElectron = " << selTrigger_SingleElectron
                    << ", isTriggered_SingleMuon = " << isTriggered_SingleMuon << ")" << std::endl;
        }
        continue;
      }
      // CV: commented-out for 2017 data-taking period,
      //     as mu+tau (e+tau) cross trigger is stored in the same primary dataset as the single muon (single electron) trigger
      //if ( selTrigger_Tau && (isTriggered_SingleMuon || isTriggered_SingleElectron) ) {
      //  if ( run_lumi_eventSelector ) {
      //    std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
      //    std::cout << " (selTrigger_Tau = " << selTrigger_Tau
      //              << ", isTriggered_SingleMuon = " << isTriggered_SingleMuon
      //              << ", isTriggered_SingleElectron = " << isTriggered_SingleElectron << ")" << std::endl;
      //  }
      //  continue;
      //}
    }
    cutFlowTable.update("trigger");
    cutFlowHistManager->fillHistograms("trigger", lumiScale);

    if ( (selTrigger_1mu     && !apply_offline_e_trigger_cuts_1mu)     ||
         (selTrigger_1mu1tau && !apply_offline_e_trigger_cuts_1mu1tau) ||
         (selTrigger_1e      && !apply_offline_e_trigger_cuts_1e)      ||
         (selTrigger_1e1tau  && !apply_offline_e_trigger_cuts_1e1tau)  ) {
      fakeableElectronSelector.disable_offline_e_trigger_cuts();
      tightElectronSelector.disable_offline_e_trigger_cuts();
    } else {
      fakeableElectronSelector.enable_offline_e_trigger_cuts();
      tightElectronSelector.enable_offline_e_trigger_cuts();
    }

//--- Rank triggers by priority and ignore triggers of lower priority if a trigger of higher priority has fired for given event;
//    the ranking of the triggers is as follows: 1mu || 1mu1tau, 1e || 1e1tau
// CV: This logic is necessary to avoid that the same event is selected multiple times when processing different primary datasets.
//     The mu+tau (e+tau) cross trigger is stored in the same primary dataset as the single muon (single electron) trigger during the 2017 data-taking period!!
    if ( !isMC && !isDEBUG ) {
      bool isTriggered_SingleElectron = isTriggered_1e || isTriggered_1e1tau;
      bool isTriggered_SingleMuon = isTriggered_1mu || isTriggered_1mu1tau;
      //bool isTriggered_Tau = isTriggered_1e1tau || isTriggered_1mu1tau;

      bool selTrigger_SingleElectron = selTrigger_1e || selTrigger_1e1tau;
      //bool selTrigger_SingleMuon = selTrigger_1mu || selTrigger_1mu1tau;
      bool selTrigger_Tau = selTrigger_1e1tau || selTrigger_1mu1tau;

      if ( selTrigger_SingleElectron && isTriggered_SingleMuon ) {
        if ( run_lumi_eventSelector ) {
          std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
          std::cout << " (selTrigger_SingleElectron = " << selTrigger_SingleElectron
                    << ", isTriggered_SingleMuon = " << isTriggered_SingleMuon << ")" << std::endl;
        }
        continue;
      }
    }
    cutFlowTable.update("trigger");
    cutFlowHistManager->fillHistograms("trigger", lumiScale);

    if ( (selTrigger_1mu     && !apply_offline_e_trigger_cuts_1mu)     ||
         (selTrigger_1mu1tau && !apply_offline_e_trigger_cuts_1mu1tau) ||
         (selTrigger_1e      && !apply_offline_e_trigger_cuts_1e)      ||
         (selTrigger_1e1tau  && !apply_offline_e_trigger_cuts_1e1tau)  ) {
      fakeableElectronSelector.disable_offline_e_trigger_cuts();
      tightElectronSelector.disable_offline_e_trigger_cuts();
    } else {
      fakeableElectronSelector.enable_offline_e_trigger_cuts();
      tightElectronSelector.enable_offline_e_trigger_cuts();
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

    std::vector<RecoHadTau> hadTaus = hadTauReader->read();
    std::vector<const RecoHadTau*> hadTau_ptrs = convert_to_ptrs(hadTaus);
    std::vector<const RecoHadTau*> cleanedHadTaus = hadTauCleaner(hadTau_ptrs, preselMuons, preselElectrons);
    std::vector<const RecoHadTau*> preselHadTausFull = preselHadTauSelector(cleanedHadTaus, isHigherPt);
    std::vector<const RecoHadTau*> fakeableHadTausFull = fakeableHadTauSelector(preselHadTausFull, isHigherPt);
    std::vector<const RecoHadTau*> tightHadTausFull = tightHadTauSelector(fakeableHadTausFull, isHigherPt);

    std::vector<const RecoHadTau*> preselHadTaus = pickFirstNobjects(preselHadTausFull, 1);
    std::vector<const RecoHadTau*> fakeableHadTaus = pickFirstNobjects(fakeableHadTausFull, 1);
    std::vector<const RecoHadTau*> tightHadTaus = getIntersection(fakeableHadTaus, tightHadTausFull, isHigherPt);
    std::vector<const RecoHadTau*> selHadTaus = selectObjects(hadTauSelection, preselHadTaus, fakeableHadTaus, tightHadTaus);
    if(isDEBUG || run_lumi_eventSelector)
    {
      printCollection("preselHadTaus",   preselHadTaus);
      printCollection("fakeableHadTaus", fakeableHadTaus);
      printCollection("tightHadTaus",    tightHadTaus);
    }

    if(isDEBUG || run_lumi_eventSelector)
    {
      printCollection("selMuons", selMuons);
      printCollection("selElectrons", selElectrons);
      printCollection("selLeptons", selLeptons);
      printCollection("selHadTaus", selHadTaus);
    }

//--- build collections of jets and select subset of jets passing b-tagging criteria
    std::vector<RecoJet> jets_ak4 = jetReaderAK4->read();
    std::vector<const RecoJet*> jet_ptrs_ak4 = convert_to_ptrs(jets_ak4);
    std::vector<const RecoJet*> cleanedJetsAK4_wrtLeptons_and_hadTaus = jetCleanerAK4_dR04(jet_ptrs_ak4, fakeableLeptons, fakeableHadTaus);
    std::vector<const RecoJet*> selJetsAK4 = jetSelectorAK4(cleanedJetsAK4_wrtLeptons_and_hadTaus, isHigherPt);
    std::vector<const RecoJet*> selBJetsAK4_loose = jetSelectorAK4_bTagLoose(cleanedJetsAK4_wrtLeptons_and_hadTaus, isHigherPt);
    std::vector<const RecoJet*> selBJetsAK4_medium = jetSelectorAK4_bTagMedium(cleanedJetsAK4_wrtLeptons_and_hadTaus, isHigherPt);

    if ( isDEBUG || run_lumi_eventSelector ) {
      printCollection("uncleaned AK4 jets", jet_ptrs_ak4);
      printCollection("cleaned AK4 jets(wrtLeptons)", cleanedJetsAK4_wrtLeptons_and_hadTaus);
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

      hadTauGenMatcher.addGenLeptonMatch(preselHadTausFull, genLeptons, 0.2);
      hadTauGenMatcher.addGenHadTauMatch(preselHadTausFull, genHadTaus, 0.2);
      hadTauGenMatcher.addGenJetMatch(preselHadTausFull, genJets, 0.2);

      jetGenMatcherAK4.addGenLeptonMatch(cleanedJetsAK4_wrtLeptons_and_hadTaus, genLeptons, 0.2);
      jetGenMatcherAK4.addGenHadTauMatch(cleanedJetsAK4_wrtLeptons_and_hadTaus, genHadTaus, 0.2);
      jetGenMatcherAK4.addGenJetMatch(cleanedJetsAK4_wrtLeptons_and_hadTaus, genJets, 0.2);
    }

    // require at least two leptons passing loose preselection criteria
    if ( !(preselLeptonsFull.size() >= 1) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS preselLeptons selection." << std::endl;
        printCollection("preselLeptons", preselLeptonsFull);
      }
      continue;
    }
    cutFlowTable.update(">= 1 presel leptons", evtWeight_inclusive);
    cutFlowHistManager->fillHistograms(">= 1 presel leptons", evtWeight_inclusive);

    // require at least two leptons passing tight selection criteria of final event selection
    if ( !(selLeptons.size() >= 1) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS selLeptons selection." << std::endl;
        printCollection("selLeptons", selLeptons);
      }
      continue;
    }
    cutFlowTable.update(">= 1 sel leptons", evtWeight_inclusive);
    cutFlowHistManager->fillHistograms(">= 1 sel leptons", evtWeight_inclusive);
    const RecoLepton* selLepton = selLeptons[0];
    const Particle::LorentzVector& selLeptonP4 = selLepton->p4();
    int selLepton_type = getLeptonType(selLepton->pdgId());
    const leptonGenMatchEntry& selLepton_genMatch = getLeptonGenMatch(leptonGenMatch_definitions, selLepton);
    int idxSelLepton_genMatch = selLepton_genMatch.idx_;
    assert(idxSelLepton_genMatch != kGen_LeptonUndefined1);

    const double minPt_lepton = selLepton->is_electron() ? minPt_e : minPt_mu;
    if ( !(selLepton->cone_pt() > minPt_lepton) ) {
      if ( run_lumi_eventSelector || isDEBUG ) {
        std::cout << "event " << eventInfo.str() << " FAILS minPt = " << minPt_lepton << " < cut on the selected lepton\n";
      }
      continue;
    }
    cutFlowTable.update(Form("lepton pT > %.0f(e)/%.0f(mu) GeV", minPt_e, minPt_mu), evtWeight_inclusive);
    cutFlowHistManager->fillHistograms(Form("lepton pT > %.0f(e)/%.0f(mu) GeV", minPt_e, minPt_mu), evtWeight_inclusive);

    if ( !(selLepton->absEta() < maxAbsEta_lepton) ) {
      if ( run_lumi_eventSelector || isDEBUG ) {
        std::cout << "event " << eventInfo.str() << " FAILS maxAbsEta = " << maxAbsEta_lepton << " > cut on the selected lepton\n";
      }
      continue;
    }
    cutFlowTable.update(Form("lepton abs(eta) < %.1f", maxAbsEta_lepton), evtWeight_inclusive);
    cutFlowHistManager->fillHistograms(Form("lepton abs(eta) < %.1f", maxAbsEta_lepton), evtWeight_inclusive);

    if ( !(preselHadTaus.size() >= 1) ) continue;
    cutFlowTable.update(">= 1 presel taus");
    cutFlowHistManager->fillHistograms(">= 1 presel taus", evtWeight_inclusive);

    if ( !(selHadTaus.size() >= 1) ) continue;
    cutFlowTable.update(">= 1 sel taus");
    cutFlowHistManager->fillHistograms(">= 1 sel taus", evtWeight_inclusive);
    const RecoHadTau* selHadTau = selHadTaus[0];
    const Particle::LorentzVector& selHadTauP4 = selHadTau->p4();
    const hadTauGenMatchEntry& selHadTau_genMatch = getHadTauGenMatch(hadTauGenMatch_definitions, selHadTau);
    int idxSelHadTau_genMatch = selHadTau_genMatch.idx_;
    assert(idxSelHadTau_genMatch != kGen_HadTauUndefined1);

    if ( !(selHadTau->pt() > minPt_hadTau) ) {
      if ( run_lumi_eventSelector || isDEBUG) {
        std::cout << "event " << eventInfo.str() << " FAILS minPt = " << minPt_hadTau << " < cut on the selected leading tau\n";
      }
      continue;
    }
    cutFlowTable.update(Form("hadTau pT > %.0f GeV", minPt_hadTau), evtWeight_inclusive);
    cutFlowHistManager->fillHistograms(Form("hadTau pT > %.0f GeV", minPt_hadTau), evtWeight_inclusive);

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

    bool isCharge_SS = selLepton->charge()*selHadTau->charge() > 0;
    bool isCharge_OS = selLepton->charge()*selHadTau->charge() < 0;
    if ( chargeSumSelection == kOS && isCharge_SS ) {
      if ( run_lumi_eventSelector ) {
	std::cout << "event " << eventInfo.str() << " FAILS lepton charge selection." << std::endl;
        std::cout << " (selLepton charge = " << selLepton->charge()
                  << ", selHadTau charge = " << selHadTau->charge() << ", chargeSumSelection = OS)" << std::endl;
      }
      continue;
    }
    if ( chargeSumSelection == kSS && isCharge_OS ) {
      if ( run_lumi_eventSelector ) {
	std::cout << "event " << eventInfo.str() << " FAILS lepton charge selection." << std::endl;
        std::cout << " (selLepton charge = " << selLepton->charge()
                  << ", selHadTau charge = " << selHadTau->charge() << ", chargeSumSelection = SS)" << std::endl;
      }
      continue;
    }
    if ( chargeSumSelection != kDisabled ) {
      cutFlowTable.update(Form("sel lepton+tau %s charge", chargeSumSelection_string.data()), evtWeight);
    }
    cutFlowHistManager->fillHistograms("sel lepton+tau OS/SS charge", evtWeight);

    // require exactly two leptons passing tight selection criteria, to avoid overlap with other channels
    if ( !(tightLeptonsFull.size() <= 1) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS tightLeptons selection." << std::endl;
        printCollection("tightLeptonsFull", tightLeptonsFull);
      }
      continue;
    }
    cutFlowTable.update("<= 1 tight leptons", evtWeight);
    cutFlowHistManager->fillHistograms("<= 1 tight leptons", evtWeight);

    // require that trigger paths match event category (with event category based on fakeableLeptons)
    if ( !((fakeableElectrons.size() >= 1 && (selTrigger_1e  || selTrigger_1e1tau )) ||
           (fakeableMuons.size()     >= 1 && (selTrigger_1mu || selTrigger_1mu1tau))) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS trigger selection for given fakeableLepton multiplicity." << std::endl;
        std::cout << " (#fakeableElectrons = " << fakeableElectrons.size()
                  << ", #fakeableMuons = " << fakeableMuons.size()
                  << ", selTrigger_1mu = " << selTrigger_1mu
                  << ", selTrigger_1mu1tau = " << selTrigger_1mu1tau
                  << ", selTrigger_1e = " << selTrigger_1e
                  << ", selTrigger_1e1tau = " << selTrigger_1e1tau << ")" << std::endl;
      }
      continue;
    }
    cutFlowTable.update("fakeable lepton trigger match", evtWeight);
    cutFlowHistManager->fillHistograms("fakeable lepton trigger match", evtWeight);

//--- apply HLT filter
    if ( apply_hlt_filter ) {
      const std::map<hltPathsE, bool> trigger_bits = {
        { hltPathsE::trigger_1e,      selTrigger_1e      },
        { hltPathsE::trigger_1mu,     selTrigger_1mu     },
        { hltPathsE::trigger_1e1tau,  selTrigger_1e1tau  },
        { hltPathsE::trigger_1mu1tau, selTrigger_1mu1tau },
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
    double hadTauSF_weight = 1.;
    if ( isMC ) {
      int selHadTau_genPdgId = getHadTau_genPdgId(selHadTau);

      dataToMCcorrectionInterface->setLeptons(selLepton_type, selLepton->pt(), selLepton->eta());
      dataToMCcorrectionInterface->setHadTaus(selHadTau_genPdgId, selHadTau->pt(), selHadTau->eta());

      dataToMCcorrectionInterface_1l_1tau_trigger->setLeptons(selLepton_type, selLepton->pt(), selLepton->eta());
      dataToMCcorrectionInterface_1l_1tau_trigger->setHadTaus(selHadTau_genPdgId, selHadTau->pt(), selHadTau->eta(), selHadTau->decayMode());
      dataToMCcorrectionInterface_1l_1tau_trigger->setTriggerBits(isTriggered_1e, isTriggered_1e1tau, isTriggered_1mu, isTriggered_1mu1tau);

//--- apply data/MC corrections for trigger efficiency
      double sf_triggerEff = dataToMCcorrectionInterface_1l_1tau_trigger->getSF_triggerEff();
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

//--- apply data/MC corrections for hadronic tau identification efficiency
//    and for e->tau and mu->tau misidentification rates
      hadTauSF_weight *= dataToMCcorrectionInterface->getSF_hadTauID_and_Iso();
      hadTauSF_weight *= dataToMCcorrectionInterface->getSF_eToTauFakeRate();
      hadTauSF_weight *= dataToMCcorrectionInterface->getSF_muToTauFakeRate();
      if ( isDEBUG ) {
        std::cout << "hadTauSF_weight = " << hadTauSF_weight << std::endl;
      }
      weight_data_to_MC_correction *= hadTauSF_weight;
      if ( isDEBUG ) {
        std::cout << "weight_data_to_MC_correction = " << weight_data_to_MC_correction << std::endl;
      }

      evtWeight *= weight_data_to_MC_correction;
    }

    bool passesTight_lepton = isMatched(*selLepton, tightElectrons) || isMatched(*selLepton, tightMuons);
    bool passesTight_hadTau = isMatched(*selHadTau, tightHadTausFull);

    double weight_fakeRate = 1.;
    double prob_fake_lepton = 1.;
    double prob_fake_hadTau = 1.;
    if ( leptonFakeRateInterface ) {
      if ( std::abs(selLepton->pdgId()) == 11 ) {
	prob_fake_lepton = leptonFakeRateInterface->getWeight_e(selLepton->cone_pt(), selLepton->absEta());
      } else if ( std::abs(selLepton->pdgId()) == 13 ) {
	prob_fake_lepton = leptonFakeRateInterface->getWeight_mu(selLepton->cone_pt(), selLepton->absEta());
      } else assert(0);
    }
    if ( jetToTauFakeRateInterface ) {
      prob_fake_hadTau = jetToTauFakeRateInterface->getWeight_lead(selHadTau->pt(), selHadTau->absEta());
    }

    if ( applyFakeRateWeights == kFR_enabled ) {
      weight_fakeRate = getWeight_2L(
        prob_fake_lepton, passesTight_lepton,
        prob_fake_hadTau, passesTight_hadTau
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
    std::vector<const RecoJetAK8*> cleanedJetsAK8_wrtLeptons_and_hadTaus = jetCleanerAK8_dR08(jet_ptrs_ak8, fakeableLeptons, fakeableHadTaus);
    std::vector<const RecoJetAK8*> selJetsAK8_Hbb = jetSelectorAK8_Hbb(cleanedJetsAK8_wrtLeptons_and_hadTaus, isHigherCSV_ak8);
    std::vector<const RecoJet*> selJetsAK4_Hbb = jetSelectorAK4(cleanedJetsAK4_wrtLeptons_and_hadTaus, isHigherCSV);
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
      cleanedJetsAK4_vbf = jetCleanerAK4_dR12(cleanedJetsAK4_wrtLeptons_and_hadTaus, overlaps);
    } else {
      cleanedJetsAK4_vbf = jetCleanerAK4_dR08(cleanedJetsAK4_wrtLeptons_and_hadTaus, selJets_Hbb);
    }
    std::vector<const RecoJet*> selJetsAK4_vbf = jetSelectorAK4_vbf(cleanedJetsAK4_vbf, isHigherPt);

    if ( !((selLeptonP4 + selHadTauP4).mass() < 76.) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS m_ltau < 76 GeV cut." << std::endl;
      }
      continue;
    }
    cutFlowTable.update("m(ltau) < 76 GeV", evtWeight);
    cutFlowHistManager->fillHistograms("m(ltau) < 76 GeV", evtWeight);

//--- compute MHT and linear MET discriminant (met_LD)
    RecoMEt met = metReader->read();
    const Particle::LorentzVector& metP4 = met.p4();
    std::vector<const RecoJet*> selJetsAK4_mht = jetSelectorAK4(cleanedJetsAK4_wrtLeptons_and_hadTaus, isHigherPt);
    Particle::LorentzVector mhtP4 = compMHT(fakeableLeptons, fakeableHadTaus, selJetsAK4_mht);
    double met_LD = compMEt_LD(metP4, mhtP4);

    //---------------------------------------------------------------------------
    // CV: Veto events with 81 < mTauTau < 151 GeV
    //     to avoid overlap with etau and mutau channels of HH->bbtautau analysis (HIG-17-002).
    //     The mass mTauTau is reconstructed using the SVFit algorithm, published in the paper
    //     [1]  "Reconstruction of the Higgs mass in events with Higgs bosons decaying into a pair of tau leptons using matrix element techniques",
    //          L. Bianchini, B. Calpas, J. Conway, A. Fowlie, L. Marzola, L. Perrini, C. Veelken
    //        Nucl.Instrum.Meth. A 862 (2017) 54
    std::vector<classic_svFit::MeasuredTauLepton> measuredTauLeptons;
    classic_svFit::MeasuredTauLepton::kDecayType leg1Type = classic_svFit::MeasuredTauLepton::kUndefinedDecayType;
    double leg1Mass = -1.;
    if ( selLepton_type == kElectron ) {
      leg1Type = classic_svFit::MeasuredTauLepton::kTauToElecDecay;
      leg1Mass = classic_svFit::electronMass;
    } else if ( selLepton_type == kMuon ) {
      leg1Type = classic_svFit::MeasuredTauLepton::kTauToMuDecay;
      leg1Mass = classic_svFit::muonMass;
    } else assert(0);
    classic_svFit::MeasuredTauLepton::kDecayType leg2Type = classic_svFit::MeasuredTauLepton::kTauToHadDecay;
    double leg2Mass = selHadTau->mass();
    if ( leg2Mass < classic_svFit::chargedPionMass ) leg2Mass = classic_svFit::chargedPionMass;
    if ( leg2Mass > 1.5                            ) leg2Mass = 1.5;
    measuredTauLeptons.push_back(classic_svFit::MeasuredTauLepton(leg1Type, selLepton->pt(), selLepton->eta(), selLepton->phi(), leg1Mass));
    measuredTauLeptons.push_back(classic_svFit::MeasuredTauLepton(leg2Type, selHadTau->pt(), selHadTau->eta(), selHadTau->phi(), leg2Mass));
    ClassicSVfit svFitAlgo;
    svFitAlgo.addLogM_dynamic(false);
    svFitAlgo.addLogM_fixed(true, 4.);
    svFitAlgo.integrate(measuredTauLeptons, metP4.px(), metP4.py(), met.cov());
    //double mSVFit = -1.; // CV: temporarily comment-out the following line, to make code compile with "old" and "new" version of ClassicSVfit
    double mSVFit = ( svFitAlgo.isValidSolution() ) ? static_cast<classic_svFit::HistogramAdapterDiTau*>(svFitAlgo.getHistogramAdapter())->getMass() : -1.;
    if ( mSVFit > 81. && mSVFit < 151. ) { // CV: veto region defined by Eq. (2) in AN-2017/007 v8
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS SVFit mass veto." << std::endl;
      }
      continue;
    }
    cutFlowTable.update("SVFit mass veto", evtWeight);
    cutFlowHistManager->fillHistograms("SVFit mass veto", evtWeight);
    //---------------------------------------------------------------------------

    const bool failsLowMassVeto = isfailsLowMassVeto(preselLeptonsFull);
    if ( failsLowMassVeto ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS low mass lepton pair veto." << std::endl;
      }
      continue;
    }
    cutFlowTable.update("m(ll) > 12 GeV", evtWeight);
    cutFlowHistManager->fillHistograms("m(ll) > 12 GeV", evtWeight);

    const bool failsZbosonMassVeto = isfailsZbosonMassVetoSFOS(preselLeptonsFull);
    if ( failsZbosonMassVeto ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS Z-boson veto." << std::endl;
      }
      continue;
    }
    cutFlowTable.update("Z-boson mass veto", evtWeight);
    cutFlowHistManager->fillHistograms("Z-boson mass veto", evtWeight);

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
    if ( isMCClosure_e || isMCClosure_m || isMCClosure_t ) {
      bool applySignalRegionVeto_lepton = (isMCClosure_e && countFakeElectrons(selLeptons) >= 1) || (isMCClosure_m && countFakeMuons(selLeptons) >= 1);
      bool applySignalRegionVeto_hadTau = isMCClosure_t && countFakeHadTaus(selHadTaus) >= 1;
      if ( applySignalRegionVeto_lepton && tightLeptons.size() >= 1 ) failsSignalRegionVeto = true;
      if ( applySignalRegionVeto_hadTau && tightHadTaus.size() >= 1 ) failsSignalRegionVeto = true;
    } else if ( electronSelection == kFakeable || muonSelection == kFakeable || hadTauSelection == kFakeable ) {
      if ( tightLeptons.size() >= 1 && tightHadTaus.size() >= 1 ) failsSignalRegionVeto = true;
    }
    if ( failsSignalRegionVeto ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS overlap w/ the SR: "
	             "# tight leptons = " << tightLeptons.size() << " >= 1 and "
                     "# tight taus = " << tightHadTaus.size() << " >= 2\n"
        ;
	printCollection("tightLeptons", tightLeptons);
	printCollection("tightHadTaus", tightHadTaus);
      }
      continue; // CV: avoid overlap with signal region
    }
    cutFlowTable.update("signal region veto", evtWeight);
    cutFlowHistManager->fillHistograms("signal region veto", evtWeight);

    // compute signal extraction observables
    Particle::LorentzVector HbbP4 = selJetP4_Hbb_lead + selJetP4_Hbb_sublead;
    double m_Hbb    = HbbP4.mass();
    double dR_Hbb   = deltaR(selJetP4_Hbb_lead, selJetP4_Hbb_sublead);
    double dPhi_Hbb = TMath::Abs(deltaPhi(selJetP4_Hbb_lead.phi(), selJetP4_Hbb_sublead.phi())); // CV: map dPhi into interval [0..pi]
    double pT_Hbb   = HbbP4.pt();
    Particle::LorentzVector ltauP4 = selLeptonP4 + selHadTauP4;
    double m_ltau  = ltauP4.mass();
    double dR_ltau = deltaR(selLeptonP4, selHadTauP4);
    double dPhi_ltau = TMath::Abs(deltaPhi(selLeptonP4.phi(), selHadTauP4.phi()));
    double pT_ltau = ltauP4.pt();
    double dPhi_lepMEt = TMath::Abs(deltaPhi(selLeptonP4.phi(), metP4.phi()));
    double dPhi_hadTauMEt = TMath::Abs(deltaPhi(selHadTauP4.phi(), metP4.phi()));
    double min_dPhi_ltauMEt = TMath::Min(dPhi_lepMEt, dPhi_hadTauMEt);
    double max_dPhi_ltauMEt = TMath::Max(dPhi_lepMEt, dPhi_hadTauMEt);
    Particle::LorentzVector HwwP4 = selLeptonP4 + selHadTauP4 + metP4;
    double m_Hww = HwwP4.mass();
    double pT_Hww = HwwP4.pt();
    double dR_b1lep = deltaR(selJetP4_Hbb_lead, selLeptonP4);
    double dR_b1hadTau = deltaR(selJetP4_Hbb_lead, selHadTauP4);
    double dR_b2lep = deltaR(selJetP4_Hbb_sublead, selLeptonP4);
    double dR_b2hadTau = deltaR(selJetP4_Hbb_sublead, selHadTauP4);
    Particle::LorentzVector HHvisP4 = HbbP4 + selLeptonP4 + selHadTauP4;
    double m_HHvis = HHvisP4.mass();
    double pT_HHvis = HHvisP4.pt();
    double dPhi_HHvis = TMath::Abs(deltaPhi(HbbP4.phi(), (selLeptonP4 + selHadTauP4).phi()));
    Particle::LorentzVector HHP4 = HbbP4 + HwwP4;
    double m_HH = HHP4.mass();
    double pT_HH = HHP4.pt();
    double dPhi_HH = TMath::Abs(deltaPhi(HbbP4.phi(), HwwP4.phi()));
    mT2_2particle mT2Algo_2particle;
    mT2Algo_2particle(
      selLeptonP4.px(), selLeptonP4.py(), selLeptonP4.mass(),
      selHadTauP4.px(), selHadTauP4.py(), selHadTauP4.mass(),
      metP4.px(), metP4.py(), 0.);
    double mT2_W = mT2Algo_2particle.get_min_mT2();
    int mT2_W_step = mT2Algo_2particle.get_min_step();
    //std::cout << "mT2_W = " << mT2_W << " (found @ step #" << mT2_W_step << ")" << std::endl;
    double cSumPx = selLeptonP4.px() + selHadTauP4.px() + metP4.px();
    double cSumPy = selLeptonP4.py() + selHadTauP4.py() + metP4.py();
    mT2Algo_2particle(
      selJetP4_Hbb_lead.px(), selJetP4_Hbb_lead.py(), selJetP4_Hbb_lead.mass(),
      selJetP4_Hbb_sublead.px(), selJetP4_Hbb_sublead.py(), selJetP4_Hbb_sublead.mass(),
      cSumPx, cSumPy, wBosonMass);
    double mT2_top_2particle = mT2Algo_2particle.get_min_mT2();
    int mT2_top_2particle_step = mT2Algo_2particle.get_min_step();
    //std::cout << "mT2_top_2particle = " << mT2_top_2particle << " (found @ step #" << mT2_top_2particle_step << ")" << std::endl;
    mT2_3particle mT2Algo_3particle;
    mT2Algo_3particle(
      selJetP4_Hbb_lead.px(), selJetP4_Hbb_lead.py(), selJetP4_Hbb_lead.mass(),
      selJetP4_Hbb_sublead.px(), selJetP4_Hbb_sublead.py(), selJetP4_Hbb_sublead.mass(),
      selLeptonP4.px(), selLeptonP4.py(), selLeptonP4.mass(),
      selHadTauP4.px(), selHadTauP4.py(), selHadTauP4.mass(),
      metP4.px(), metP4.py(), 0.);
    double mT2_top_3particle_permutation1 = mT2Algo_3particle.get_min_mT2();
    int mT2_top_3particle_permutation1_step = mT2Algo_3particle.get_min_step();
    mT2Algo_3particle(
      selJetP4_Hbb_lead.px(), selJetP4_Hbb_lead.py(), selJetP4_Hbb_lead.mass(),
      selJetP4_Hbb_sublead.px(), selJetP4_Hbb_sublead.py(), selJetP4_Hbb_sublead.mass(),
      selHadTauP4.px(), selHadTauP4.py(), selHadTauP4.mass(),
      selLeptonP4.px(), selLeptonP4.py(), selLeptonP4.mass(),
      metP4.px(), metP4.py(), 0.);
    double mT2_top_3particle_permutation2 = mT2Algo_3particle.get_min_mT2();
    double mT2_top_3particle_permutation2_step = mT2Algo_3particle.get_min_step();
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


//--- fill histograms with events passing final selection
    selHistManagerType* selHistManager = selHistManagers[idxSelLepton_genMatch][idxSelHadTau_genMatch];
    assert(selHistManager != 0);
    selHistManager->electrons_->fillHistograms(selElectrons, evtWeight);
    selHistManager->muons_->fillHistograms(selMuons, evtWeight);
    selHistManager->hadTaus_->fillHistograms(selHadTaus, evtWeight);
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
      selHadTaus.size(),
      selJetsAK4.size(),
      selBJetsAK4_loose.size(),
      selBJetsAK4_medium.size(),
      HT,
      STMET,
      m_Hbb, dR_Hbb, dPhi_Hbb, pT_Hbb,
      m_ltau, dR_ltau, dPhi_ltau, pT_ltau,
      m_Hww, pT_Hww,
      m_HHvis, m_HH, dPhi_HH, pT_HH,
      mT2_W, mT2_W_step, mT2_top_2particle, mT2_top_2particle_step, mT2_top_3particle, mT2_top_3particle_step,
      vbf_jet1_pt, vbf_jet1_eta, vbf_jet2_pt, vbf_jet2_eta, vbf_m_jj, vbf_dEta_jj,
      evtWeight);
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
    if ( selLepton_type == kElectron ) ++numElectrons;
    int numMuons = 0;
    if ( selLepton_type == kMuon     ) ++numMuons;
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
	    selHadTaus.size(),
	    selJetsAK4.size(),
	    selBJetsAK4_loose.size(),
	    selBJetsAK4_medium.size(),
	    HT,
	    STMET,
	    m_Hbb, dR_Hbb, dPhi_Hbb, pT_Hbb,
	    m_ltau, dR_ltau, dPhi_ltau, pT_ltau,
	    m_Hww, pT_Hww,
	    m_HHvis, m_HH, dPhi_HH, pT_HH,
	    mT2_W, mT2_W_step, mT2_top_2particle, mT2_top_2particle_step, mT2_top_3particle, mT2_top_3particle_step,
	    vbf_jet1_pt, vbf_jet1_eta, vbf_jet2_pt, vbf_jet2_eta, vbf_m_jj, vbf_dEta_jj,
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

    if ( bdt_filler ) {
      bdt_filler -> operator()({ eventInfo.run, eventInfo.lumi, eventInfo.event })
          ("lep_pt",                        selLepton->pt())
          ("lep_conePt",                    comp_lep1_conePt(*selLepton))
          ("lep_eta",                       selLepton->eta())
          ("hadTau_pt",                     selHadTau->pt())
          ("hadTau_eta",                    selHadTau->eta())
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
          ("m_ltau",                        m_ltau)
          ("dR_ltau",                       dR_ltau)
          ("dPhi_ltau",                     dPhi_ltau)
          ("pT_ltau",                       pT_ltau)
	  ("min_dPhi_ltauMEt",              min_dPhi_ltauMEt)
	  ("max_dPhi_ltauMEt",              max_dPhi_ltauMEt)
          ("m_Hww",                         m_Hww)
	  ("pT_Hww",                        pT_Hww)
	  ("dR_b1lep",                      dR_b1lep)
          ("dR_b1hadTau",                   dR_b1hadTau)
          ("dR_b2lep",                      dR_b2lep)
          ("dR_b2hadTau",                   dR_b2hadTau)
          ("m_HHvis",                       m_HHvis)
          ("pT_HHvis",                      pT_HHvis)
          ("dPhi_HHvis",                    dPhi_HHvis)
          ("m_HH",                          m_HH)
          ("pT_HH",                         pT_HH)
          ("dPhi_HH",                       dPhi_HH)
          ("mT2_W",                         mT2_W)
          ("mT2_top_2particle",             mT2_top_2particle)
          ("mT2_top_3particle",             mT2_top_3particle)
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
        .fill()
      ;
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
    for ( std::vector<hadTauGenMatchEntry>::const_iterator hadTauGenMatch_definition = hadTauGenMatch_definitions.begin();
          hadTauGenMatch_definition != hadTauGenMatch_definitions.end(); ++hadTauGenMatch_definition ) {

      std::string process_and_genMatch = process_string;
      if ( apply_leptonGenMatching ) process_and_genMatch += leptonGenMatch_definition->name_;
      if ( apply_leptonGenMatching && apply_hadTauGenMatching ) process_and_genMatch += "&";
      if ( apply_hadTauGenMatching ) process_and_genMatch += hadTauGenMatch_definition->name_;

      int idxLepton = leptonGenMatch_definition->idx_;
      int idxHadTau = hadTauGenMatch_definition->idx_;

      const TH1* histogram_EventCounter = selHistManagers[idxLepton][idxHadTau]->evt_->getHistogram_EventCounter();
      std::cout << " " << process_and_genMatch << " = " << histogram_EventCounter->GetEntries() << " (weighted = " << histogram_EventCounter->Integral() << ")" << std::endl;
    }
  }
  std::cout << std::endl;

  delete dataToMCcorrectionInterface;
  delete dataToMCcorrectionInterface_1l_1tau_trigger;

  delete leptonFakeRateInterface;
  delete jetToTauFakeRateInterface;

  delete run_lumi_eventSelector;

  delete selEventsFile;

  delete muonReader;
  delete electronReader;
  delete hadTauReader;
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

  delete genEvtHistManager_beforeCuts;
  delete eventWeightManager;

  hltPaths_delete(triggers_1e);
  hltPaths_delete(triggers_1e1tau);
  hltPaths_delete(triggers_1mu);
  hltPaths_delete(triggers_1mu1tau);

  delete inputTree;

  clock.Show("analyze_hh_bb1l1tau");

  return EXIT_SUCCESS;
}
