#include "FWCore/ParameterSet/interface/ParameterSet.h" // edm::ParameterSet
#include "FWCore/PythonParameterSet/interface/MakeParameterSets.h" // edm::readPSetsFrom()
#include "FWCore/Utilities/interface/Exception.h" // cms::Exception
#include "PhysicsTools/FWLite/interface/TFileService.h" // fwlite::TFileService
#include "DataFormats/FWLite/interface/InputSource.h" // fwlite::InputSource
#include "DataFormats/FWLite/interface/OutputFiles.h" // fwlite::OutputFiles
#include "DataFormats/Math/interface/LorentzVector.h" // math::PtEtaPhiMLorentzVector, math::XYZTLorentzVectorD
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
#include "tthAnalysis/HiggsToTauTau/interface/mvaAuxFunctions.h" // check_mvaInputs, get_mvaInputVariables
#include "tthAnalysis/HiggsToTauTau/interface/mvaAuxFunctions_Hj_and_Hjj_taggers.h" // comp_mvaOutput_Hj_tagger, comp_mvaOutput_Hjj_tagger
#include "tthAnalysis/HiggsToTauTau/interface/mvaInputVariables.h" // auxiliary functions for computing input variables of the MVA used for signal extraction
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
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // getBTagWeight_option, getHadTau_genPdgId, isHigherPt, isMatched
#include "tthAnalysis/HiggsToTauTau/interface/leptonGenMatchingAuxFunctions.h" // getLeptonGenMatch_definitions_3lepton, getLeptonGenMatch_string, getLeptonGenMatch_int
#include "tthAnalysis/HiggsToTauTau/interface/fakeBackgroundAuxFunctions.h"
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

#include "hhAnalysis/bbww/interface/EvtHistManager_hh_bb1l.h" // EvtHistManager_hh_bb1l
#include "hhAnalysis/bbww/interface/RecoJetCollectionSelectorAK8_bbWW_Hbb.h" // RecoJetSelectorAK8_bbWW_Hbb
#include "hhAnalysis/bbww/interface/RecoJetCollectionSelectorAK8_bbWW_Wjj.h" // RecoJetSelectorAK8_bbWW_Wjj
#include "tthAnalysis/HiggsToTauTau/interface/mT2_2particle.h" // mT2_2particle::comp_mT
#include "tthAnalysis/HiggsToTauTau/interface/mT2_3particle.h" // mT2_3particle::comp_mT

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
const double higgsBosonMass = 125.;

enum { kHbb_undefined, kHbb_resolved, kHbb_boosted };
enum { kWjj_undefined, kWjj_resolved, kWjj_boosted_lowPurity, kWjj_boosted_highPurity };
enum { kVBF_undefined, kVBF_nottagged, kVBF_tagged };

struct categoryEntryType
{
  categoryEntryType(int numElectrons, int numMuons, int numBJets_medium, int numBJets_loose, int type_Hbb, int type_Wjj, int type_vbf)
    : numElectrons_(numElectrons)
    , numMuons_(numMuons)
    , numBJets_medium_(numBJets_medium)
    , numBJets_loose_(numBJets_loose)
    , type_Hbb_(type_Hbb)
    , type_Wjj_(type_Wjj)
    , type_vbf_(type_vbf)
  {
    name_ = "";
    if      ( numBJets_medium_ >= 2                         ) name_ += "2bM";
    else if ( numBJets_medium_ >= 1 && numBJets_loose_ >= 2 ) name_ += "1bM1bL";
    else if ( numBJets_medium_ >= 1                         ) name_ += "1bM";
    else name_ += "bb";
    if      ( numElectrons_ >= 1 ) name_ += "1e";
    else if ( numMuons_     >= 1 ) name_ += "1mu";
    else name_ += "1l";
    if      ( type_Hbb_ == kHbb_resolved           ) name_ += "_resolvedHbb";
    else if ( type_Hbb_ == kHbb_boosted            ) name_ += "_boostedHbb";
    if      ( type_Wjj_ == kWjj_resolved           ) name_ += "_resolvedWjj";
    else if ( type_Wjj_ == kWjj_boosted_lowPurity  ) name_ += "_boostedWjj_lowPurity";
    else if ( type_Wjj_ == kWjj_boosted_highPurity ) name_ += "_boostedWjj_highPurity";
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
  int type_Wjj_; // 0 = either resolved or boosted (any purity); 1 = resolved; 2 = boosted, low purity; 3 = boosted, high purity
  int type_vbf_; // 0 = either tagged or not tagged, 1 = not tagged; 2 = tagged 
};

Particle::LorentzVector comp_metP4_B2G_18_008(const Particle::LorentzVector& visP4, double metPx, double metPy, double mH)
{
  // compute four-vector of neutrino produced in H->WW*->jj lnu decay,
  // using Higgs boson mass constraint, as described in Section 3.4.2 of AN-2018/058 (v4)
  // (CV: code obtained by email from Nickolas Mc Coll on October 4th 2018)
  double a = mH*mH - visP4.mass()*visP4.mass() + 2.*visP4.px()*metPx + 2.*visP4.py()*metPy;
  double A = 4.*(visP4.energy()*visP4.energy() - visP4.pz()*visP4.pz());
  double B = -4.*a*visP4.pz();
  double C = 4.*visP4.energy()*visP4.energy()*(metPx*metPx + metPy*metPy) - a*a;
  double delta = B*B - 4.*A*C;

  double metPz = 0.;
  if ( delta < 0. ) {
    metPz = -B/(2.*A);
  } else {
    double pos = (-B + std::sqrt(delta))/(2.*A);
    double neg = (-B - std::sqrt(delta))/(2.*A);
    if ( std::fabs(pos) < std::fabs(neg) ) metPz = pos;
    else metPz = neg;
  }
  math::XYZTLorentzVectorD metP4(metPx, metPy, metPz, std::sqrt(metPx*metPx + metPy*metPy + metPz*metPz));
  return Particle::LorentzVector(metP4.pt(), metP4.eta(), metP4.phi(), 0.);
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

  std::cout << "<analyze_hh_bb1l>:" << std::endl;

//--- keep track of time it takes the macro to execute
  TBenchmark clock;
  clock.Start("analyze_hh_bb1l");

//--- read python configuration parameters
  if ( !edm::readPSetsFrom(argv[1])->existsAs<edm::ParameterSet>("process") )
    throw cms::Exception("analyze_hh_bb1l")
      << "No ParameterSet 'process' found in configuration file = " << argv[1] << " !!\n";

  edm::ParameterSet cfg = edm::readPSetsFrom(argv[1])->getParameter<edm::ParameterSet>("process");

  edm::ParameterSet cfg_analyze = cfg.getParameter<edm::ParameterSet>("analyze_hh_bb1l");

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
  vstring triggerNames_1mu = cfg_analyze.getParameter<vstring>("triggers_1mu");
  std::vector<hltPath*> triggers_1mu = create_hltPaths(triggerNames_1mu);
  bool use_triggers_1mu = cfg_analyze.getParameter<bool>("use_triggers_1mu");

  bool apply_offline_e_trigger_cuts_1e = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_1e");
  bool apply_offline_e_trigger_cuts_1mu = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_1mu");

  const std::string electronSelection_string = cfg_analyze.getParameter<std::string>("electronSelection");
  const std::string muonSelection_string     = cfg_analyze.getParameter<std::string>("muonSelection");
  std::cout << "electronSelection_string = " << electronSelection_string << "\n"
               "muonSelection_string     = " << muonSelection_string     << '\n'
  ;
  const int electronSelection = get_selection(electronSelection_string);
  const int muonSelection     = get_selection(muonSelection_string);
  double lep_mva_cut = cfg_analyze.getParameter<double>("lep_mva_cut"); // CV: used for tight lepton selection only

  bool apply_leptonGenMatching = cfg_analyze.getParameter<bool>("apply_leptonGenMatching");
  std::vector<leptonGenMatchEntry> leptonGenMatch_definitions = getLeptonGenMatch_definitions_1lepton(apply_leptonGenMatching);
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
  if(applyAdditionalEvtWeight)
  {
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
    default: throw cmsException("analyze_hh_bb1l", __LINE__) << "Invalid era = " << era;
  }

  std::string applyFakeRateWeights_string = cfg_analyze.getParameter<std::string>("applyFakeRateWeights");
  int applyFakeRateWeights = -1;
  if      ( applyFakeRateWeights_string == "disabled" ) applyFakeRateWeights = kFR_disabled;
  else if ( applyFakeRateWeights_string == "enabled"  ) applyFakeRateWeights = kFR_enabled;
  else throw cms::Exception("analyze_hh_bb1l")
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

//--- declare event-level variables
  EventInfo eventInfo(isSignal, isMC, isMC_tH);
  EventInfoReader eventInfoReader(&eventInfo);
  inputTree->registerReader(&eventInfoReader);

  hltPathReader hltPathReader_instance({ triggers_1e, triggers_1mu });
  inputTree -> registerReader(&hltPathReader_instance);

  if(eventWeightManager)
  {
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
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR16(1.6, isDEBUG);
  RecoJetCollectionSelectorAK8_bbWW_Hbb jetSelectorAK8_Hbb(era, -1, isDEBUG);
  RecoJetCollectionSelectorAK8_bbWW_Wjj jetSelectorAK8_Wjj(era, -1, isDEBUG);
  
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
    if ( !readGenObjects ) {
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

  // initialize Hj-tagger
  std::string mvaFileName_Hj_tagger = "tthAnalysis/HiggsToTauTau/data/Hj_deepcsv_BDTG_2017.weights.xml";
  std::vector<std::string> mvaInputVariables_Hj_tagger = {
    "Jet25_lepdrmin", "max(Jet25_bDiscriminator,0.)",
    "max(Jet25_qg,0.)", "Jet25_lepdrmax", "Jet25_pt" };
  TMVAInterface mva_Hj_tagger(mvaFileName_Hj_tagger, mvaInputVariables_Hj_tagger);

  // initialize Hjj-tagger
  std::string mvaFileName_Hjj_tagger = "tthAnalysis/HiggsToTauTau/data/Hjj_csv_BDTG.weights.xml";
  std::vector<std::string> mvaInputVariables_Hjj_tagger = {
    "bdtJetPair_minlepmass", "bdtJetPair_sumbdt", "bdtJetPair_dr",
    "bdtJetPair_minjdr", "bdtJetPair_mass", "bdtJetPair_minjOvermaxjdr"};
  TMVAInterface mva_Hjj_tagger(mvaFileName_Hjj_tagger, mvaInputVariables_Hjj_tagger);

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
    MuonHistManager* muons_;
    JetHistManager* jetsAK4_;
    JetHistManager* leadJetAK4_;
    JetHistManager* subleadJetAK4_;
    JetHistManagerAK8* jetsAK8_Hbb_;
    JetHistManagerAK8* jetsAK8_Wjj_;
    JetHistManager* BJetsAK4_loose_;
    JetHistManager* leadBJetAK4_loose_;
    JetHistManager* subleadBJetAK4_loose_;
    JetHistManager* BJetsAK4_medium_;
    MEtHistManager* met_;
    MEtFilterHistManager* metFilters_;
    EvtHistManager_hh_bb1l* evt_;
    std::map<std::string, EvtHistManager_hh_bb1l*> evt_in_categories_;
    GenEvtHistManager* genEvtHistManager_afterCuts_;
    LHEInfoHistManager* lheInfoHistManager_afterCuts_;
    std::map<std::string, LHEInfoHistManager*> lheInfoHistManager_afterCuts_in_categories_;
    EvtYieldHistManager* evtYield_;
    WeightHistManager* weights_;
  };
  std::map<int, selHistManagerType*> selHistManagers;
  std::vector<categoryEntryType> categories_evt;
  for ( int type_Hbb = kHbb_undefined; type_Hbb <= kHbb_boosted; ++type_Hbb ) {
    for ( int type_Wjj = kWjj_undefined; type_Wjj <= kWjj_boosted_highPurity; ++type_Wjj ) {
      if ( type_Hbb == kHbb_undefined && type_Wjj != kWjj_undefined ) continue;
      if ( type_Hbb != kHbb_undefined && type_Wjj == kWjj_undefined ) continue;
      for ( int type_vbf = kVBF_undefined; type_vbf <= kVBF_tagged; ++type_vbf ) {
	if ( !(type_Hbb == kHbb_undefined && type_Wjj == kWjj_undefined && type_vbf == kVBF_undefined) ) {
	  categories_evt.push_back(categoryEntryType(-1, -1, -1, -1, type_Hbb, type_Wjj, type_vbf)); // hh_bb1l
	}
	categories_evt.push_back(categoryEntryType(-1, -1,  2, -1, type_Hbb, type_Wjj, type_vbf)); // hh_2bM1l
	categories_evt.push_back(categoryEntryType(-1, -1,  1,  2, type_Hbb, type_Wjj, type_vbf)); // hh_1bM1bL1l
	categories_evt.push_back(categoryEntryType(-1, -1,  1, -1, type_Hbb, type_Wjj, type_vbf)); // hh_1bM1l
	categories_evt.push_back(categoryEntryType( 1, -1, -1, -1, type_Hbb, type_Wjj, type_vbf)); // hh_bb1e
	categories_evt.push_back(categoryEntryType( 1, -1,  2, -1, type_Hbb, type_Wjj, type_vbf)); // hh_2bM1e
	categories_evt.push_back(categoryEntryType( 1, -1,  1,  2, type_Hbb, type_Wjj, type_vbf)); // hh_1bM1bL1e
	categories_evt.push_back(categoryEntryType( 1, -1,  1, -1, type_Hbb, type_Wjj, type_vbf)); // hh_1bM1e
	categories_evt.push_back(categoryEntryType(-1,  1, -1, -1, type_Hbb, type_Wjj, type_vbf)); // hh_bb1mu
	categories_evt.push_back(categoryEntryType(-1,  1,  2, -1, type_Hbb, type_Wjj, type_vbf)); // hh_2bM1mu
	categories_evt.push_back(categoryEntryType(-1,  1,  1,  2, type_Hbb, type_Wjj, type_vbf)); // hh_1bM1bL1mu
	categories_evt.push_back(categoryEntryType(-1,  1,  1, -1, type_Hbb, type_Wjj, type_vbf)); // hh_1bM1mu     
      }
    }
  }
  for ( std::vector<leptonGenMatchEntry>::const_iterator leptonGenMatch_definition = leptonGenMatch_definitions.begin();
        leptonGenMatch_definition != leptonGenMatch_definitions.end(); ++leptonGenMatch_definition ) {

    std::string process_and_genMatch = process_string;
    if ( apply_leptonGenMatching ) process_and_genMatch += leptonGenMatch_definition->name_;
    int idxLepton = leptonGenMatch_definition->idx_;

    selHistManagerType* selHistManager = new selHistManagerType();
    selHistManager->electrons_ = new ElectronHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/electrons", histogramDir.data()), central_or_shift));
    selHistManager->electrons_->bookHistograms(fs);
    selHistManager->muons_ = new MuonHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/muons", histogramDir.data()), central_or_shift));
    selHistManager->muons_->bookHistograms(fs);
    selHistManager->jetsAK4_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/jetsAK4", histogramDir.data()), central_or_shift));
    selHistManager->jetsAK4_->bookHistograms(fs);
    selHistManager->leadJetAK4_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/leadJetAK4", histogramDir.data()), central_or_shift, 0));
    selHistManager->leadJetAK4_->bookHistograms(fs);
    selHistManager->subleadJetAK4_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/subleadJetAK4", histogramDir.data()), central_or_shift, 1));
    selHistManager->subleadJetAK4_->bookHistograms(fs);
    selHistManager->jetsAK8_Hbb_ = new JetHistManagerAK8(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/jetsAK8_Hbb", histogramDir.data()), central_or_shift));
    selHistManager->jetsAK8_Hbb_->bookHistograms(fs);
    selHistManager->jetsAK8_Wjj_ = new JetHistManagerAK8(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/jetsAK8_Wjj", histogramDir.data()), central_or_shift));
    selHistManager->jetsAK8_Wjj_->bookHistograms(fs);
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
    selHistManager->evt_ = new EvtHistManager_hh_bb1l(makeHistManager_cfg(process_and_genMatch,
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
      TString histogramDir_category = histogramDir.data();
      histogramDir_category.ReplaceAll("bb1l", category->name_.data());
      selHistManager->evt_in_categories_[category->name_] = new EvtHistManager_hh_bb1l(makeHistManager_cfg(process_and_genMatch,
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

  std::cout << "Book BDT filling" << std::endl;
  NtupleFillerBDT<float, int>* bdt_filler = nullptr;
  typedef std::remove_pointer<decltype(bdt_filler)>::type::float_type float_type;
  typedef std::remove_pointer<decltype(bdt_filler)>::type::int_type int_type;

  if ( selectBDT ) {
    bdt_filler = new std::remove_pointer<decltype(bdt_filler)>::type(
      makeHistManager_cfg(process_string, Form("%s/sel/evtntuple", histogramDir.data()), central_or_shift)
    );
    bdt_filler->register_variable<float_type>(
      "lep_pt", "lep_conePt", "lep_eta", 
      "bjet1_pt", "bjet1_eta",
      "bjet2_pt", "bjet2_eta",
      "met", "mht", "met_LD", 
      "HT", "STMET", 
      "m_Hbb", "dR_Hbb", "dPhi_Hbb", "pT_Hbb",
      "m_Wjj", "dR_Wjj", "dPhi_Wjj", "tau21_Wjj",
      "dR_Hww", "dPhi_Hww", "pT_Hww", "Smin_Hww",
      "dR_b1lep", "dR_b2lep",
      "m_HHvis", "pT_HHvis", "dPhi_HHvis", 
      "m_HH", "m_HH_B2G_18_008", "pT_HH", "dPhi_HH", "Smin_HH",
      "mT_W", "mT_top_2particle", "mT_top_3particle", 
      "m_HH_hme",
      "mvaOutput_Hj_tagger", "mvaOutput_Hjj_tagger",
      "vbf_m_jj", "vbf_dEta_jj",
      "genWeight", "evtWeight"
    );
    bdt_filler->register_variable<int_type>(
      "lep_charge", 
      "nJet", "nBJetLoose", "nBJetMedium", 
      "isHbb_boosted", "isWjj_boosted", "isWjj_boosted_highPurity", 
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
    process_string, Form("%s/sel/cutFlow", histogramDir.data()), central_or_shift
  );
  const std::vector<std::string> cuts = {
    "run:ls:event selection",
    "trigger",
    ">= 1 presel leptons",
    ">= 1 sel leptons",
    "<= 1 tight leptons",
    "lepton pT > 25 GeV",
    "fakeable lepton trigger match",
    "HLT filter matching",
    ">= 2 jets from H->bb",
    ">= 1 medium b-jet",
    ">= 1 jets from W->jj",    
    "m(ll) > 12 GeV",
    "Z-boson mass veto",
    "boosted W->jj: mD < 125 GeV", 
    "boosted W->jj: pT_HWW/mHH < 0.3", 
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
    bool isTriggered_1mu = hltPaths_isTriggered(triggers_1mu);

    bool selTrigger_1e = use_triggers_1e && isTriggered_1e;
    bool selTrigger_1mu = use_triggers_1mu && isTriggered_1mu;
    if ( !(selTrigger_1e || selTrigger_1mu) ) {
      if ( run_lumi_eventSelector ) {
	std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
        std::cout << " (selTrigger_1e = " << selTrigger_1e
                  << ", selTrigger_1mu = " << selTrigger_1mu << ")" << std::endl;
      }
      continue;
    }

//--- rank triggers by priority and ignore triggers of lower priority if a trigger of higher priority has fired for given event;
//    the ranking of the triggers is as follows: 2mu, 1e1mu, 2e, 1mu, 1e
// CV: this logic is necessary to avoid that the same event is selected multiple times when processing different primary datasets
    if ( !isMC && !isDEBUG ) {
      if ( selTrigger_1e && isTriggered_1mu ) {
        if ( run_lumi_eventSelector ) {
	  std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
          std::cout << " (selTrigger_1e = " << selTrigger_1e
                    << ", isTriggered_1mu = " << isTriggered_1mu << ")" << std::endl;
        }
        continue;
      }
    }
    cutFlowTable.update("trigger", evtWeight_inclusive);
    cutFlowHistManager->fillHistograms("trigger", evtWeight_inclusive);

    if ( (selTrigger_1e  && !apply_offline_e_trigger_cuts_1e)  ||
         (selTrigger_1mu && !apply_offline_e_trigger_cuts_1mu) ) {
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

    std::vector<const RecoLepton*> preselLeptons = pickFirstNobjects(preselLeptonsFull, 1);
    std::vector<const RecoLepton*> fakeableLeptons = pickFirstNobjects(fakeableLeptonsFull, 1);
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

    // require at least one lepton passing loose preselection criteria
    if ( !(preselLeptonsFull.size() >= 1) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS preselLeptons selection." << std::endl;
        printCollection("preselLeptons", preselLeptonsFull);
      }
      continue;
    }
    cutFlowTable.update(">= 1 presel leptons", evtWeight_inclusive);
    cutFlowHistManager->fillHistograms(">= 1 presel leptons", evtWeight_inclusive);

    // require at least one lepton passing fakeable or tight selection criteria 
    // (fakeable lepton selection applied in fake background control region, 
    //  tight lepton selection applied in signal region)
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
      btagWeight = get_BtagWeight(selJetsAK4); // TO-DO: add b-tag weights for boosted case (AK8 jets)
      evtWeight *= btagWeight;
      if ( isDEBUG ) {
        std::cout << "lumiScale = " << lumiScale << std::endl;
        if ( apply_genWeight ) std::cout << "genWeight = " << boost::math::sign(eventInfo.genWeight) << std::endl;
        std::cout << "pileupWeight = " << eventInfo.pileupWeight << std::endl;
        std::cout << "btagWeight = " << btagWeight << std::endl;
      }
    }

    // require exactly one lepton passing tight selection criteria, to avoid overlap with other channels
    if ( !(tightLeptonsFull.size() <= 1) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS tightLeptons selection." << std::endl;
        printCollection("tightLeptonsFull", tightLeptonsFull);
      }
      continue;
    }
    cutFlowTable.update("<= 1 tight leptons", evtWeight);
    cutFlowHistManager->fillHistograms("<= 1 tight leptons", evtWeight);

    double minPt_lead = -1.;
    if      ( era == kEra_2016 ) minPt_lead = 25.;
    else if ( era == kEra_2017 ) minPt_lead = 25.;
    else assert(0);
    if ( !(selLepton->cone_pt() > minPt_lead) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS lepton pT selection." << std::endl;
        std::cout << " (selLepton pT = " << selLepton->pt() << ", minPt_lead = " << minPt_lead << ")" << std::endl;
      }
      continue;
    }
    cutFlowTable.update("lepton pT > 25 GeV", evtWeight);
    cutFlowHistManager->fillHistograms("lepton pT > 25 GeV", evtWeight);

    // require that trigger paths match event category (with event category based on fakeableLeptons)
    if ( !((fakeableElectrons.size() >= 1 && selTrigger_1e) ||
           (fakeableMuons.size()     >= 1 && selTrigger_1mu)) ) {
      if ( run_lumi_eventSelector ) {
	std::cout << "event " << eventInfo.str() << " FAILS trigger selection for given fakeableLepton multiplicity." << std::endl;
        std::cout << " (#fakeableElectrons = " << fakeableElectrons.size()
                  << ", #fakeableMuons = " << fakeableMuons.size()
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
        { hltPathsE::trigger_1e,  selTrigger_1e  },
        { hltPathsE::trigger_1mu, selTrigger_1mu },
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
      dataToMCcorrectionInterface->setLeptons(selLepton_type, selLepton->pt(), selLepton->eta());

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

    bool passesTight_lepton = isMatched(*selLepton, tightElectrons) || isMatched(*selLepton, tightMuons);

    double weight_fakeRate = 1.;
    double prob_fake_lepton = 1.;
    if ( leptonFakeRateInterface ) {
      if ( std::abs(selLepton->pdgId()) == 11 ) {
	prob_fake_lepton = leptonFakeRateInterface->getWeight_e(selLepton->cone_pt(), selLepton->absEta());
      } else if ( std::abs(selLepton->pdgId()) == 13 ) {
	prob_fake_lepton = leptonFakeRateInterface->getWeight_mu(selLepton->cone_pt(), selLepton->absEta());
      } else assert(0);
    }

    if ( applyFakeRateWeights == kFR_enabled ) {
      weight_fakeRate = getWeight_1L(prob_fake_lepton, passesTight_lepton);
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

    // select jets from W->jj decay
    std::vector<const RecoJetAK8*> cleanedJetsAK8_wrtHbb;
    std::vector<const RecoJet*> cleanedJetsAK4_wrtHbb;
    if ( selJetAK8_Hbb ) {
      std::vector<const RecoJetAK8*> overlaps = { selJetAK8_Hbb };
      cleanedJetsAK8_wrtHbb = jetCleanerAK8_dR16(jet_ptrs_ak8, overlaps); // CV: do *not* clean W->jj "fat" jet collection with respect to leptons!
      cleanedJetsAK4_wrtHbb = jetCleanerAK4_dR12(cleanedJetsAK4_wrtLeptons, overlaps);
    } else {
      cleanedJetsAK8_wrtHbb = jetCleanerAK8_dR12(jet_ptrs_ak8, selJets_Hbb);
      cleanedJetsAK4_wrtHbb = jetCleanerAK4_dR08(cleanedJetsAK4_wrtLeptons, selJets_Hbb);
    }
    jetSelectorAK8_Wjj.getSelector().set_lepton(selLepton);
    std::vector<const RecoJetAK8*> selJetsAK8_Wjj = jetSelectorAK8_Wjj(cleanedJetsAK8_wrtHbb, isHigherPt);
    std::vector<const RecoJet*> selJetsAK4_Wjj = jetSelectorAK4(cleanedJetsAK4_wrtHbb, isHigherPt);
    const RecoJetAK8* selJetAK8_Wjj = nullptr;
    const RecoJetBase* selJet1_Wjj = nullptr;
    const RecoJetBase* selJet2_Wjj = nullptr;
    if ( selJetsAK8_Wjj.size() >= 1 ) {
      selJetAK8_Wjj = selJetsAK8_Wjj[0];
      selJet1_Wjj = selJetAK8_Wjj->subJet1();
      selJet2_Wjj = selJetAK8_Wjj->subJet2();
      assert(selJet1_Wjj && selJet2_Wjj);
    } else {
      double minRank = 1.e+3;
      for ( std::vector<const RecoJet*>::const_iterator selJet1 = selJetsAK4_Wjj.begin();
	    selJet1 != selJetsAK4_Wjj.end(); ++selJet1 ) {
	for ( std::vector<const RecoJet*>::const_iterator selJet2 = selJet1 + 1;
	      selJet2 != selJetsAK4_Wjj.end(); ++selJet2 ) {
	  Particle::LorentzVector jjP4 = (*selJet1)->p4() + (*selJet2)->p4();
	  double m_jj = jjP4.mass();
	  double pT_jj = jjP4.pt();
	  double rank = TMath::Abs(m_jj - wBosonMass)/TMath::Sqrt(TMath::Max(10., pT_jj));
	  if ( rank < minRank ) {
	    selJet1_Wjj = (*selJet1);
	    selJet2_Wjj = (*selJet2);
	    minRank = rank;
	  }
	} 
      }    
      if ( !selJet1_Wjj && selJetsAK4_Wjj.size() >= 1 ) selJet1_Wjj = selJetsAK4_Wjj[0];
      if ( !selJet2_Wjj && selJetsAK4_Wjj.size() >= 2 ) selJet2_Wjj = selJetsAK4_Wjj[1];
    }
    if ( !(selJet1_Wjj || selJet2_Wjj) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS >= 1 jets from W->jj selection\n";
      }
      continue;
    }
    cutFlowTable.update(">= 1 jets from W->jj", evtWeight_inclusive);
    cutFlowHistManager->fillHistograms(">= 1 jets from W->jj", evtWeight_inclusive);

    std::vector<const RecoJetBase*> selJets_Wjj;
    if ( selJet1_Wjj ) selJets_Wjj.push_back(selJet1_Wjj);
    if ( selJet2_Wjj ) selJets_Wjj.push_back(selJet2_Wjj);    
    std::sort(selJets_Wjj.begin(), selJets_Wjj.end(), isHigherPt);
    assert(selJets_Wjj.size() >= 1);
    const RecoJetBase* selJet_Wjj_lead = selJets_Wjj[0];
    const Particle::LorentzVector& selJetP4_Wjj_lead = selJet_Wjj_lead->p4();
    const RecoJetBase* selJet_Wjj_sublead = nullptr;
    Particle::LorentzVector selJetP4_Wjj_sublead;
    if ( selJets_Wjj.size() >= 2 ) {
      selJet_Wjj_sublead = selJets_Wjj[1];
      selJetP4_Wjj_sublead = selJet_Wjj_sublead->p4();
    }

    // select VBF jet candidates
    std::vector<const RecoJet*> cleanedJetsAK4_vbf;
    if ( selJetAK8_Wjj ) {
      std::vector<const RecoJetAK8*> overlaps = { selJetAK8_Wjj };
      cleanedJetsAK4_vbf = jetCleanerAK4_dR12(cleanedJetsAK4_wrtHbb, overlaps);
    } else {
      cleanedJetsAK4_vbf = jetCleanerAK4_dR08(cleanedJetsAK4_wrtHbb, selJets_Wjj);
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

    // compute four-vector of neutrino produced in H->WW*->jj lnu decay,
    // using Higgs boson mass constraint, as described in Section 3.4.2 of AN-2018/058 (v4)
    Particle::LorentzVector neutrinoP4_B2G_18_008 = comp_metP4_B2G_18_008(selLeptonP4 + selJetP4_Wjj_lead + selJetP4_Wjj_sublead, metP4.px(), metP4.py(), higgsBosonMass);

    // compute HT and STMET variables used for signal extraction in EXO analyses
    std::vector<const RecoJetBase*> selJets_HT_and_STMET;
    selJets_HT_and_STMET.insert(selJets_HT_and_STMET.end(), selJets_Hbb.begin(), selJets_Hbb.end());
    selJets_HT_and_STMET.insert(selJets_HT_and_STMET.end(), selJets_Wjj.begin(), selJets_Wjj.end());
    double HT = compHT(fakeableLeptons, {}, selJets_HT_and_STMET);
    double STMET = compSTMEt(fakeableLeptons, {}, selJets_HT_and_STMET, met.p4());

    // apply cut on mD variable, defined by Eq.(3) in AN-2018/058 (v4)
    bool fails_mD_cut = false;
    if ( selJetAK8_Wjj ) {
      Particle::LorentzVector WjjP4 = selJetAK8_Wjj->p4();
      Particle::LorentzVector WlnuP4 = selLepton->p4() + neutrinoP4_B2G_18_008;
      double mD = deltaR(WjjP4, WlnuP4)*0.5*(WjjP4 + WlnuP4).pt();
      if ( !(mD <= higgsBosonMass) ) {
	if ( run_lumi_eventSelector ) {
	  std::cout << "event " << eventInfo.str() << " FAILS mD < 125 GeV selection\n";
	}
	//continue;
	fails_mD_cut = true;
      }
    }
    cutFlowTable.update("boosted W->jj: mD < 125 GeV selection", evtWeight);
    cutFlowHistManager->fillHistograms("boosted W->jj: mD < 125 GeV selection", evtWeight);
    
    // apply cut on event centrality variable, defined in Table 9 of AN-2018/058 (v4)
    bool fails_centrality_cut = false;
    if ( selJetAK8_Wjj ) {
      double pT_HWW = (selJetAK8_Wjj->p4() + selLepton->p4() + neutrinoP4_B2G_18_008).pt();
      double mHH = (selJetP4_Hbb_lead + selJetP4_Hbb_sublead + selJetAK8_Wjj->p4() + selLepton->p4() + neutrinoP4_B2G_18_008).mass();
      if ( !((pT_HWW/mHH) <= 0.3) ) {
	if ( run_lumi_eventSelector ) {
	  std::cout << "event " << eventInfo.str() << " FAILS pT_HWW/mHH < 0.3 selection\n";
	}
	//continue;
	fails_centrality_cut = true;
      }
    }
    cutFlowTable.update("boosted W->jj: pT_HWW/mHH < 0.3", evtWeight);
    cutFlowHistManager->fillHistograms("boosted W->jj: pT_HWW/mHH < 0.3", evtWeight);

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
      if ( applySignalRegionVeto && tightLeptons.size() >= 1 ) failsSignalRegionVeto = true;
    } else if ( electronSelection == kFakeable || muonSelection == kFakeable ) {
      if ( tightLeptons.size() >= 1 ) failsSignalRegionVeto = true;
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

    //std::cout << "selJet_Hbb_lead:" << (*selJet_Hbb_lead) << std::endl;
    //std::cout << "selJet_Hbb_sublead:" << (*selJet_Hbb_sublead) << std::endl;
    //std::cout << "(m_Hbb = " << (selJetP4_Hbb_lead + selJetP4_Hbb_sublead).mass() << ")" << std::endl;    
    //std::cout << "selJet_Wjj_lead:" << (*selJet_Wjj_lead) << std::endl;
    //if ( selJet_Wjj_sublead ) {
    //  std::cout << "selJet_Wjj_sublead:" << (*selJet_Wjj_sublead) << std::endl;
    //  std::cout << "(m_Wjj = " << (selJetP4_Wjj_lead + selJetP4_Wjj_sublead).mass() << ")" << std::endl;
    //}

    // compute signal extraction observables    
    Particle::LorentzVector HbbP4 = selJetP4_Hbb_lead + selJetP4_Hbb_sublead;
    double m_Hbb    = HbbP4.mass();
    double dR_Hbb   = deltaR(selJetP4_Hbb_lead, selJetP4_Hbb_sublead);
    double dPhi_Hbb = deltaPhi(selJetP4_Hbb_lead.phi(), selJetP4_Hbb_sublead.phi());
    double pT_Hbb   = HbbP4.pt();
    Particle::LorentzVector WjjP4 = selJetP4_Wjj_lead + selJetP4_Wjj_sublead;
    double m_Wjj    = -1.;
    double dR_Wjj   = -1.;
    double dPhi_Wjj = -1.;
    double pT_Wjj   = -1.;
    if ( selJet_Wjj_lead && selJet_Wjj_sublead ) {
      m_Wjj    = WjjP4.mass();
      dR_Wjj   = deltaR(selJetP4_Wjj_lead, selJetP4_Wjj_sublead);
      dPhi_Wjj = deltaPhi(selJetP4_Wjj_lead.phi(), selJetP4_Wjj_sublead.phi());
      pT_Wjj   = WjjP4.pt();
    }
    double tau21_Wjj = ( selJetAK8_Wjj ) ? selJetAK8_Wjj->tau2()/selJetAK8_Wjj->tau1() : -1.;
    Particle::LorentzVector WlnuP4 = selLeptonP4 + neutrinoP4_B2G_18_008;
    double dR_Hww = deltaR(WjjP4, WlnuP4);
    double dPhi_Hww = deltaPhi(WjjP4.phi(), WlnuP4.phi());
    Particle::LorentzVector HwwP4 = WjjP4 + WlnuP4;
    double pT_Hww = HwwP4.pt();
    double Smin_Hww = comp_Smin(WjjP4 + selLeptonP4, metP4.px(), metP4.py());
    double dR_b1lep = deltaR(selJetP4_Hbb_lead, selLeptonP4);
    double dR_b2lep = deltaR(selJetP4_Hbb_sublead, selLeptonP4);
    Particle::LorentzVector HHvisP4 = HbbP4 + WjjP4 + selLeptonP4;    
    double m_HHvis = HHvisP4.mass();
    double pT_HHvis = HHvisP4.pt();
    double dPhi_HHvis = deltaPhi(HbbP4.phi(), (WjjP4 + selLeptonP4).phi());        
    Particle::LorentzVector HHP4_B2G_18_008 = HbbP4 + WjjP4 + selLeptonP4 + neutrinoP4_B2G_18_008;
    Particle::LorentzVector HHP4 = HbbP4 + WjjP4 + selLeptonP4 + metP4;
    double m_HH = HHP4.mass();
    double m_HH_B2G_18_008 = HHP4_B2G_18_008.mass(); 
    double pT_HH = HHP4.pt();
    double Smin_HH = comp_Smin(HHvisP4, metP4.px(), metP4.py());
    double dR_HH = deltaR(HbbP4, WjjP4 + selLeptonP4 + neutrinoP4_B2G_18_008);
    double dPhi_HH = deltaPhi(HbbP4.phi(), (WjjP4 + selLeptonP4 + metP4).phi());
    double mT_W = mT2_2particle::comp_mT(selLeptonP4.px(), selLeptonP4.py(), selLeptonP4.mass(), metP4.px(), metP4.py(), 0.);
    double mT_top_2particle_permutation1 = mT2_2particle::comp_mT(
      selJetP4_Hbb_lead.px(), selJetP4_Hbb_lead.py(), selJetP4_Hbb_lead.mass(), 
      selLeptonP4.px() + metP4.px(), selLeptonP4.py() + metP4.py(), wBosonMass);
    double mT_top_2particle_permutation2 = mT2_2particle::comp_mT(
      selJetP4_Hbb_sublead.px(), selJetP4_Hbb_sublead.py(), selJetP4_Hbb_sublead.mass(), 
      selLeptonP4.px() + metP4.px(), selLeptonP4.py() + metP4.py(), wBosonMass);
    double mT_top_2particle = TMath::Min(mT_top_2particle_permutation1, mT_top_2particle_permutation2);
    double mT_top_3particle_permutation1 = mT2_3particle::comp_mT(
      selJetP4_Hbb_lead.px(), selJetP4_Hbb_lead.py(), selJetP4_Hbb_lead.mass(), 
      selLeptonP4.px(), selLeptonP4.py(), selLeptonP4.mass(), metP4.px(), metP4.py(), 0.);
    double mT_top_3particle_permutation2 = mT2_3particle::comp_mT(
      selJetP4_Hbb_sublead.px(), selJetP4_Hbb_sublead.py(), selJetP4_Hbb_sublead.mass(), 
      selLeptonP4.px(), selLeptonP4.py(), selLeptonP4.mass(), metP4.px(), metP4.py(), 0.);
    double mT_top_3particle = TMath::Min(mT_top_3particle_permutation1, mT_top_3particle_permutation2);
    double m_HH_hme = -1.; // CV: not implemented yet

    std::map<std::string, double> mvaInputs_Hj_tagger;
    double mvaOutput_Hj_tagger = -1.;
    for ( std::vector<const RecoJet*>::const_iterator selJet = selJetsAK4.begin();
          selJet != selJetsAK4.end(); ++selJet ) {
      if ( deltaR((*selJet)->p4(), selJetP4_Hbb_lead) < 0.4 || deltaR((*selJet)->p4(), selJetP4_Hbb_sublead) < 0.4 ) continue;
      double mvaOutput = comp_mvaOutput_Hj_tagger(
        *selJet, fakeableLeptons, mvaInputs_Hj_tagger, mva_Hj_tagger,
        eventInfo);
      if ( mvaOutput > mvaOutput_Hj_tagger ) mvaOutput_Hj_tagger = mvaOutput;
    }

    std::map<std::string, double> mvaInputs_Hjj_tagger;
    double mvaOutput_Hjj_tagger = -1.;
    for ( std::vector<const RecoJet*>::const_iterator selJet1 = selJetsAK4.begin();
	  selJet1 != selJetsAK4.end(); ++selJet1 ) {
      if ( deltaR((*selJet1)->p4(), selJetP4_Hbb_lead) < 0.4 || deltaR((*selJet1)->p4(), selJetP4_Hbb_sublead) < 0.4 ) continue;
      for ( std::vector<const RecoJet*>::const_iterator selJet2 = selJet1 + 1;
            selJet2 != selJetsAK4.end(); ++selJet2 ) {
	 if ( deltaR((*selJet2)->p4(), selJetP4_Hbb_lead) < 0.4 || deltaR((*selJet2)->p4(), selJetP4_Hbb_sublead) < 0.4 ) continue;
	 double mvaOutput = comp_mvaOutput_Hjj_tagger(
           *selJet1, *selJet2, selJetsAK4, fakeableLeptons,
	   mvaInputs_Hjj_tagger, mva_Hjj_tagger,
	   mvaInputs_Hj_tagger, mva_Hj_tagger, eventInfo);
	 if ( mvaOutput > mvaOutput_Hjj_tagger ) mvaOutput_Hjj_tagger = mvaOutput;
      }
    }

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
	  if ( dEta_jj > vbf_dEta_jj ) vbf_dEta_jj = dEta_jj;
	  if ( m_jj    > vbf_m_jj    ) vbf_m_jj    = m_jj;
	  isVBF = true;
	}
      }
    }

//--- fill histograms with events passing final selection
    selHistManagerType* selHistManager = selHistManagers[idxSelLepton_genMatch];
    assert(selHistManager != 0);
    selHistManager->electrons_->fillHistograms(selElectrons, evtWeight);
    selHistManager->muons_->fillHistograms(selMuons, evtWeight);
    selHistManager->jetsAK4_->fillHistograms(selJetsAK4, evtWeight);
    selHistManager->leadJetAK4_->fillHistograms(selJetsAK4, evtWeight);
    selHistManager->subleadJetAK4_->fillHistograms(selJetsAK4, evtWeight);
    if ( selJetAK8_Hbb ) {
      selHistManager->jetsAK8_Hbb_->fillHistograms({ selJetAK8_Hbb }, evtWeight);
    }
    if ( selJetAK8_Wjj ) {
      selHistManager->jetsAK8_Wjj_->fillHistograms({ selJetAK8_Wjj }, evtWeight);
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
      HT, 
      STMET,
      m_Hbb, dR_Hbb, dPhi_Hbb, pT_Hbb, 
      m_Wjj, dR_Wjj, dPhi_Wjj, pT_Wjj, 
      dR_Hww, dPhi_Hww, pT_Hww, Smin_Hww,
      m_HHvis, m_HH, m_HH_B2G_18_008, m_HH_hme, dR_HH, dPhi_HH, pT_HH, Smin_HH,
      mT_W, mT_top_2particle, mT_top_3particle,
      mvaOutput_Hj_tagger, mvaOutput_Hjj_tagger,
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
    
    int numElectrons = ( selLepton_type == kElectron ) ?            1 : 0;
    int numMuons     = ( selLepton_type == kMuon     ) ?            1 : 0;
    int type_Hbb     = ( selJetAK8_Hbb               ) ? kHbb_boosted : kHbb_resolved; 
    int type_Wjj     = kWjj_resolved;
    if ( selJetAK8_Wjj && !fails_mD_cut && !fails_centrality_cut ) {
      if ( (selJetAK8_Wjj->tau2()/selJetAK8_Wjj->tau1()) < 0.55 ) type_Wjj = kWjj_boosted_highPurity;
      else type_Wjj = kWjj_boosted_lowPurity;
    }
    int type_vbf     = ( isVBF                       ) ?  kVBF_tagged : kVBF_nottagged;
    for ( std::vector<categoryEntryType>::const_iterator category = categories_evt.begin();
	  category != categories_evt.end(); ++category ) {
      if ( (category->numElectrons_    ==             -1 || numElectrons    == category->numElectrons_)    &&
	   (category->numMuons_        ==             -1 || numMuons        == category->numMuons_)        &&
	   (category->numBJets_medium_ ==             -1 || numBJets_medium == category->numBJets_medium_) &&
	   (category->numBJets_loose_  ==             -1 || numBJets_loose  == category->numBJets_loose_)  &&
	   (category->type_Hbb_        == kHbb_undefined || type_Hbb        == category->type_Hbb_)        &&
	   (category->type_Wjj_        == kWjj_undefined || type_Wjj        == category->type_Wjj_)        &&
	   (category->type_vbf_        == kVBF_undefined || type_vbf        == category->type_vbf_)        ) {
	if ( selHistManager->evt_in_categories_.find(category->name_) != selHistManager->evt_in_categories_.end() ) {
	  selHistManager->evt_in_categories_[category->name_]->fillHistograms(
	    selElectrons.size(),
	    selMuons.size(),
	    selJetsAK4.size(),
	    selBJetsAK4_loose.size(),
	    selBJetsAK4_medium.size(),
	    HT, 
	    STMET,
	    m_Hbb, dR_Hbb, dPhi_Hbb, pT_Hbb, 
	    m_Wjj, dR_Wjj, dPhi_Wjj, pT_Wjj, 
	    dR_Hww, dPhi_Hww, pT_Hww, Smin_Hww,
	    m_HHvis, m_HH, m_HH_B2G_18_008, m_HH_hme, dR_HH, dPhi_HH, pT_HH, Smin_HH,
	    mT_W, mT_top_2particle, mT_top_3particle,
	    mvaOutput_Hj_tagger, mvaOutput_Hjj_tagger,
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

    if ( bdt_filler ) {
      bdt_filler -> operator()({ eventInfo.run, eventInfo.lumi, eventInfo.event })
          ("lep_pt",                        selLepton->pt())
          ("lep_conePt",                    comp_lep1_conePt(*selLepton))
          ("lep_eta",                       selLepton->eta())
          ("lep_charge",                    selLepton->charge())
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
          ("m_Wjj",                         m_Wjj)
          ("dR_Wjj",                        dR_Wjj)
          ("dPhi_Wjj",                      dPhi_Wjj)
          ("pT_Wjj",                        pT_Wjj)
	  ("tau21_Wjj",                     tau21_Wjj)
          ("dR_Hww",                        dR_Hww)
          ("dPhi_Hww",                      dPhi_Hww)
          ("Smin_Hww",                      Smin_Hww)
          ("pT_Hww",                        pT_Hww)
          ("dR_b1lep",                      dR_b1lep)
          ("dR_b2lep",                      dR_b2lep)
          ("m_HHvis",                       m_HHvis)
          ("pT_HHvis",                      pT_HHvis)
          ("dPhi_HHvis",                    dPhi_HHvis)
          ("m_HH",                          m_HH)
          ("m_HH_B2G_18_008",               m_HH_B2G_18_008)
          ("pT_HH",                         pT_HH)
          ("dPhi_HH",                       dPhi_HH)
  	  ("Smin_HH",                       Smin_HH)          
          ("mT_W",                          mT_W)
          ("mT_top_2particle",              mT_top_2particle)
          ("mT_top_3particle",              mT_top_3particle)
          ("m_HH_hme",                      m_HH_hme)
	  ("mvaOutput_Hj_tagger",           mvaOutput_Hj_tagger)
	  ("mvaOutput_Hjj_tagger",          mvaOutput_Hjj_tagger)
          ("vbf_dEta_jj",                   vbf_dEta_jj)
          ("vbf_m_jj",                      vbf_m_jj)
          ("genWeight",                     eventInfo.genWeight)
          ("evtWeight",                     evtWeight)
          ("nJet",                          comp_n_jet25_recl(selJetsAK4))
          ("nBJetLoose",                    selBJetsAK4_loose.size())
          ("nBJetMedium",                   selBJetsAK4_medium.size())
          ("nJet_vbf",                      selJetsAK4_vbf.size())
	  ("isHbb_boosted",                 type_Hbb == kHbb_boosted)
          ("isWjj_boosted",                 type_Wjj == kWjj_boosted_lowPurity || type_Wjj == kWjj_boosted_highPurity)
          ("isWjj_boosted_highPurity",      type_Wjj == kWjj_boosted_highPurity)
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
  hltPaths_delete(triggers_1mu);

  delete inputTree;

  clock.Show("analyze_hh_bb1l");

  return EXIT_SUCCESS;
}
