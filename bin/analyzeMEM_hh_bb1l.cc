#include "FWCore/ParameterSet/interface/ParameterSet.h" // edm::ParameterSet
#include "FWCore/PythonParameterSet/interface/MakeParameterSets.h" // edm::readPSetsFrom()
#include "FWCore/Utilities/interface/Exception.h" // cms::Exception
#include "PhysicsTools/FWLite/interface/TFileService.h" // fwlite::TFileService
#include "DataFormats/FWLite/interface/InputSource.h" // fwlite::InputSource
#include "DataFormats/FWLite/interface/OutputFiles.h" // fwlite::OutputFiles
#include "DataFormats/Math/interface/LorentzVector.h" // math::PtEtaPhiMLorentzVector, math::XYZTLorentzVectorD
#include "DataFormats/Math/interface/deltaR.h" // deltaR

#include <TBenchmark.h> // TBenchmark
#include <TString.h> // TString, Form
#include <TError.h> // gErrorAbortLevel, kError
#include <TRandom3.h> // TRandom3
#include <TROOT.h> // TROOT

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

#include "hhAnalysis/multilepton/interface/EvtWeightRecorderHH.h" // EvtWeightRecorderHH

#include "hhAnalysis/bbww/interface/RecoJetCollectionSelectorAK8_hh_bbWW_Hbb.h" // RecoJetSelectorAK8_hh_bbWW_Hbb
#include "hhAnalysis/bbww/interface/MEMOutput_hh_bb1l.h" // MEMOutput_hh_bb1l
#include "hhAnalysis/bbww/interface/MEMOutputReader_hh_bb1l.h" // MEMOutputReader_hh_bb1l

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

bool 
isGenMatched(double eta, double phi, const std::vector<GenParticle>& genParticles, 
	     const std::vector<int>* pdgIds = nullptr, double dRmax = 0.3)
{
  bool isMatched = false;
  for ( std::vector<GenParticle>::const_iterator genParticle = genParticles.begin();
	genParticle != genParticles.end(); ++genParticle ) {
    bool isSelected = false;
    if ( pdgIds )
    {
      int genParticle_pdgId = genParticle->pdgId();
      for ( std::vector<int>::const_iterator pdgId = pdgIds->begin();
	    pdgId != pdgIds->end(); ++pdgId ) {
	if ( genParticle_pdgId == (*pdgId) ) isSelected = true;
      }
    }
    if ( pdgIds && !isSelected ) continue;
    double dR = deltaR(eta, phi, genParticle->eta(), genParticle->phi());
    if ( dR < dRmax ) isMatched = true;
  }
  return isMatched;
}

struct jetHistograms
{
  jetHistograms(const std::string& label)
    : label_(label)
    , histogram_pt_(nullptr)
    , histogram_btagCSV_(nullptr)
  {}
  ~jetHistograms() {}
  void bookHistograms(fwlite::TFileService& fs)
  {
    std::string histogramName_pt = Form("%s_pt", label_.data());
    histogram_pt_ = fs.make<TH1D>(histogramName_pt.data(), histogramName_pt.data(), 50, 0., 250.);
    std::string histogramName_btagCSV = Form("%s_btagCSV", label_.data());
    histogram_btagCSV_ = fs.make<TH1D>(histogramName_btagCSV.data(), histogramName_btagCSV.data(), 50, 0., 1.);
  }
  void fillHistograms(const RecoJetBase* jet, double evtWeight)
  {
    fillWithOverFlow(histogram_pt_, jet->pt(), evtWeight); 
    if ( dynamic_cast<const RecoJet*>(jet) ) 
    {
      fillWithOverFlow(histogram_btagCSV_, (dynamic_cast<const RecoJet*>(jet))->BtagCSV(), evtWeight);
    }    
    else if ( dynamic_cast<const RecoSubjetAK8*>(jet) ) 
    {
      fillWithOverFlow(histogram_btagCSV_, (dynamic_cast<const RecoSubjetAK8*>(jet))->BtagCSV(), evtWeight);
    } else assert(0);
  }	
  std::string label_;
  TH1* histogram_pt_;
  TH1* histogram_btagCSV_;
};

template<typename T>
void 
fillHistograms_jets(const std::vector<const T*>& jets, 
		    const std::vector<GenParticle>& genParticles, const std::vector<int>* pdgIds,
		    jetHistograms& histograms_jet1, TH1* histogram_idx1, 
		    jetHistograms& histograms_jet2, TH1* histogram_idx2, TH1* histogram_numIndices, TH1* histogram_mjj, double evtWeight)
{
  std::vector<int> indices;
  size_t numJets = jets.size();
  for ( size_t idxJet = 0; idxJet < numJets; ++idxJet )
  {
    const T* jet = jets[idxJet];
    bool isMatched = isGenMatched(jet->eta(), jet->phi(), genParticles, pdgIds);
    if ( isMatched ) indices.push_back(idxJet);
  }
  const T* jet1 = nullptr;
  if ( indices.size() >= 1 ) 
  {
    size_t idx1 = indices[0];
    jet1 = jets[idx1];
    histograms_jet1.fillHistograms(jet1, evtWeight);
    fillWithOverFlow(histogram_idx1, idx1, evtWeight);
  }
  const T* jet2 = nullptr;
  if ( indices.size() >= 2 ) 
  {
    size_t idx2 = indices[1];
    jet2 = jets[idx2];
    histograms_jet2.fillHistograms(jet2, evtWeight);
    fillWithOverFlow(histogram_idx2, idx2, evtWeight);
  }
  fillWithOverFlow(histogram_numIndices, indices.size(), evtWeight);
  if ( jet1 && jet2 ) 
  {
    fillWithOverFlow(histogram_mjj, (jet1->p4() + jet2->p4()).mass(), evtWeight); 
  }
}

struct memHistograms
{ 
  memHistograms(const std::string& label, int numUnmatchedLeptons, int numUnmatchedBJets, int numUnmatchedWJets)
    : label_(label)
    , numUnmatchedLeptons_(numUnmatchedLeptons)
    , numUnmatchedBJets_(numUnmatchedBJets)
    , numUnmatchedWJets_(numUnmatchedWJets)
    , histogram_LR_(nullptr)
    , histogram_weightS_(nullptr)
    , histogram_weightB_(nullptr)
    , histogram_isValid_(nullptr) 
  {}
  ~memHistograms() {}
  void bookHistograms(fwlite::TFileService& fs)
  {
    std::string histogramName_prefix = "mem";
    if ( label_ != "" ) histogramName_prefix.append("_").append(label_);
    std::string histogramName_suffix;
    if ( numUnmatchedLeptons_ == 0 && numUnmatchedBJets_ == 0 && numUnmatchedWJets_ == 0 ) 
    {
      histogramName_suffix = "fullyMatched";
    }
    else if ( numUnmatchedLeptons_ >= 1 && numUnmatchedBJets_ == 0 && numUnmatchedWJets_ == 0 ) 
    {
      histogramName_suffix = "unmatchedLepton";
    }
    else if ( numUnmatchedLeptons_ == 0 && numUnmatchedBJets_ >= 1 && numUnmatchedWJets_ == 0 ) 
    {
      histogramName_suffix = "unmatchedBJet";
    }
    else if ( numUnmatchedLeptons_ == 0 && numUnmatchedBJets_ == 0 && numUnmatchedWJets_ >= 1 ) 
    {
      histogramName_suffix = "unmatchedWJet";
    }
    else assert(0);
    std::string histogramName_LR = Form("%s_LR_%s", histogramName_prefix.data(), histogramName_suffix.data());
    histogram_LR_ = fs.make<TH1D>(histogramName_LR.data(), histogramName_LR.data(), 50, 0., 1.);
    std::string histogramName_weightS = Form("%s_weightS_%s", histogramName_prefix.data(), histogramName_suffix.data());
    histogram_weightS_ = fs.make<TH1D>(histogramName_weightS.data(), histogramName_weightS.data(), 100, -50., 0.);
    std::string histogramName_weightB = Form("%s_weightB_%s", histogramName_prefix.data(), histogramName_suffix.data());
    histogram_weightB_ = fs.make<TH1D>(histogramName_weightB.data(), histogramName_weightB.data(), 100, -50., 0.);
    std::string histogramName_isValid = Form("%s_isValid_%s", histogramName_prefix.data(), histogramName_suffix.data());
    histogram_isValid_ = fs.make<TH1D>(histogramName_isValid.data(), histogramName_isValid.data(), 2, -0.5, +1.5);
  }
  void fillHistograms(const MEMOutput_hh_bb1l& memOutput, double evtWeight)
  {
    if ( memOutput.isValid() )
    { 
      fillWithOverFlow(histogram_LR_, memOutput.LR(), evtWeight);
      fillWithOverFlow(histogram_weightS_, memOutput.weight_signal(), evtWeight);
      fillWithOverFlow(histogram_weightB_, memOutput.weight_background(), evtWeight);
    }
    fillWithOverFlow(histogram_isValid_, memOutput.isValid(), evtWeight);
  }
  std::string label_;
  int numUnmatchedLeptons_;
  int numUnmatchedBJets_;
  int numUnmatchedWJets_;
  TH1* histogram_LR_;
  TH1* histogram_weightS_;
  TH1* histogram_weightB_;
  TH1* histogram_isValid_; 
};

void 
fillHistograms_mem(const MEMOutput_hh_bb1l& memOutput, 
		   const std::vector<GenParticle>& genLeptons, 
		   const std::vector<GenParticle>& genBJets, 
		   const std::vector<GenParticle>& genWJets, 
		   memHistograms& histograms_fullyMatched, 
		   memHistograms& histograms_unmatchedLepton, 
		   memHistograms& histograms_unmatchedBJet, 
		   memHistograms& histograms_unmatchedWJet, double evtWeight)
{
  int numUnmatchedLeptons = 0;
  if ( !isGenMatched(memOutput.lepton_eta_, memOutput.lepton_phi_, genLeptons) ) 
  {
    ++numUnmatchedLeptons;
  }
  int numUnmatchedBJets = 0;
  std::vector<int> genBJet_pdgIds = { -5, +5 }; 
  if ( memOutput.bjet1_isReconstructed_ && !isGenMatched(memOutput.bjet1_eta_, memOutput.bjet1_phi_, genBJets, &genBJet_pdgIds) )
  { 
    ++numUnmatchedBJets;
  }
  if ( memOutput.bjet2_isReconstructed_ && !isGenMatched(memOutput.bjet2_eta_, memOutput.bjet2_phi_, genBJets, &genBJet_pdgIds) )
  { 
    ++numUnmatchedBJets;
  }
  int numUnmatchedWJets = 0;
  if ( memOutput.wjet1_isReconstructed_ && !isGenMatched(memOutput.wjet1_eta_, memOutput.wjet1_phi_, genWJets) )
  { 
    ++numUnmatchedWJets;
  }
  if ( memOutput.wjet2_isReconstructed_ && !isGenMatched(memOutput.wjet2_eta_, memOutput.wjet2_phi_, genWJets) )
  { 
    ++numUnmatchedWJets;
  }
  if      ( numUnmatchedLeptons == 0 && numUnmatchedBJets == 0 && numUnmatchedWJets == 0 ) 
  {
    histograms_fullyMatched.fillHistograms(memOutput, evtWeight);
  }
  else if ( numUnmatchedLeptons >= 1 && numUnmatchedBJets == 0 && numUnmatchedWJets == 0 ) 
  {
    histograms_unmatchedLepton.fillHistograms(memOutput, evtWeight);
  }
  else if ( numUnmatchedLeptons == 0 && numUnmatchedBJets >= 1 && numUnmatchedWJets == 0 ) 
  {
    histograms_unmatchedBJet.fillHistograms(memOutput, evtWeight);
  }
  else if ( numUnmatchedLeptons == 0 && numUnmatchedBJets == 0 && numUnmatchedWJets >= 1 ) 
  {
    histograms_unmatchedWJet.fillHistograms(memOutput, evtWeight);
  }
}

void dumpGenParticles(const std::string& label, const std::vector<GenParticle>& particles)
{
  for ( size_t idxParticle = 0; idxParticle < particles.size(); ++idxParticle ) {
    std::cout << label << " #" << idxParticle << ":" << " ";
    std::cout << particles[idxParticle];
    std::cout << std::endl;
  }
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
  std::string branchName_jets_ak8_Hbb = cfg_analyze.getParameter<std::string>("branchName_jets_ak8_Hbb");
  std::string branchName_subjets_ak8_Hbb = cfg_analyze.getParameter<std::string>("branchName_subjets_ak8_Hbb");
  std::string branchName_jets_ak8_Wjj = cfg_analyze.getParameter<std::string>("branchName_jets_ak8_Wjj");
  std::string branchName_subjets_ak8_Wjj = cfg_analyze.getParameter<std::string>("branchName_subjets_ak8_Wjj");
  std::string branchName_met = cfg_analyze.getParameter<std::string>("branchName_met");

  std::string branchName_memOutput = cfg_analyze.getParameter<std::string>("branchName_memOutput");
  std::string branchName_memOutput_missingBJet = cfg_analyze.getParameter<std::string>("branchName_memOutput_missingBJet");
  std::string branchName_memOutput_missingHadWJet = cfg_analyze.getParameter<std::string>("branchName_memOutput_missingHadWJet");
  std::string branchName_memOutput_missingBJet_and_HadWJet = cfg_analyze.getParameter<std::string>("branchName_memOutput_missingBJet_and_HadWJet");

  std::string branchName_genLeptons = cfg_analyze.getParameter<std::string>("branchName_genLeptons");
  std::string branchName_genBJets = cfg_analyze.getParameter<std::string>("branchName_genBJets");
  std::string branchName_genWJets = cfg_analyze.getParameter<std::string>("branchName_genWJets");

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
  RecoMuonCollectionSelectorTight tightMuonSelector(era, -1, isDEBUG);

  RecoElectronReader* electronReader = new RecoElectronReader(era, branchName_electrons, isMC, false);
  inputTree->registerReader(electronReader);
  RecoElectronCollectionGenMatcher electronGenMatcher;
  RecoElectronCollectionCleaner electronCleaner(0.3, isDEBUG);
  RecoElectronCollectionSelectorTight tightElectronSelector(era, -1, isDEBUG);

  RecoJetReader* jetReaderAK4 = new RecoJetReader(era, isMC, branchName_jets_ak4, false);
  inputTree->registerReader(jetReaderAK4);
  RecoJetCollectionGenMatcher jetGenMatcherAK4;
  RecoJetCollectionCleaner jetCleanerAK4_dR04(0.4, isDEBUG);
  RecoJetCollectionCleaner jetCleanerAK4_dR08(0.8, isDEBUG);
  RecoJetCollectionCleaner jetCleanerAK4_dR12(1.2, isDEBUG);
  RecoJetCollectionSelector jetSelectorAK4(era, -1, isDEBUG);
  RecoJetCollectionSelectorBtagLoose jetSelectorAK4_bTagLoose(era, -1, isDEBUG);
  RecoJetCollectionSelectorBtagMedium jetSelectorAK4_bTagMedium(era, -1, isDEBUG);

  RecoJetReaderAK8* jetReaderAK8_Hbb = new RecoJetReaderAK8(era, branchName_jets_ak8_Hbb, branchName_subjets_ak8_Hbb);
  inputTree->registerReader(jetReaderAK8_Hbb);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR08(0.8, isDEBUG);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR12(1.2, isDEBUG);
  RecoJetCollectionSelectorAK8_hh_bbWW_Hbb jetSelectorAK8_Hbb(era, -1, isDEBUG);

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
  MEMOutputReader_hh_bb1l* memReader_missingBJet_and_HadWJet = nullptr;
  if ( !branchName_memOutput_missingBJet_and_HadWJet.empty() )
  {
    memReader_missingBJet_and_HadWJet = new MEMOutputReader_hh_bb1l(
      Form("n%s", branchName_memOutput_missingBJet_and_HadWJet.data()), branchName_memOutput_missingBJet_and_HadWJet);
    inputTree->registerReader(memReader_missingBJet_and_HadWJet);
  }

  GenParticleReader* genLeptonReader = new GenParticleReader(branchName_genLeptons);
  inputTree->registerReader(genLeptonReader);
  GenParticleReader* genBJetReader = new GenParticleReader(branchName_genBJets);
  inputTree->registerReader(genBJetReader);
  GenParticleReader* genWJetReader = new GenParticleReader(branchName_genWJets);
  inputTree->registerReader(genWJetReader);

//--- declare missing transverse energy
  RecoMEtReader* metReader = new RecoMEtReader(era, isMC, branchName_met);
  inputTree->registerReader(metReader);

//--- declare generator level information
  LHEInfoReader* lheInfoReader = new LHEInfoReader(hasLHE);
  inputTree->registerReader(lheInfoReader);
  
  jetHistograms* histograms_boostedHbb_bjet1 = new jetHistograms("boostedHbb_bjet1");
  histograms_boostedHbb_bjet1->bookHistograms(fs);
  TH1* histogram_boostedHbb_bjet1_idx = fs.make<TH1D>("boostedHbb_bjet1_idx", "boostedHbb_bjet1_idx", 25, -0.5, +24.5);
  jetHistograms* histograms_boostedHbb_bjet2 = new jetHistograms("boostedHbb_bjet2");
  histograms_boostedHbb_bjet2->bookHistograms(fs);
  TH1* histogram_boostedHbb_bjet2_idx = fs.make<TH1D>("boostedHbb_bjet2_idx", "boostedHbb_bjet2_idx", 25, -0.5, +24.5);
  TH1* histogram_boostedHbb_bjet_numIndices = fs.make<TH1D>("boostedHbb_bjet_numIndices", "boostedHbb_bjet_numIndices", 25, -0.5, +24.5);
  TH1* histogram_boostedHbb_bjet_mjj = fs.make<TH1D>("boostedHbb_bjet_mjj", "boostedHbb_bjet_mjj", 50, 0., 250.);

  jetHistograms* histograms_resolvedHbb_bjet1 = new jetHistograms("resolvedHbb_bjet1");
  histograms_resolvedHbb_bjet1->bookHistograms(fs);
  TH1* histogram_resolvedHbb_bjet1_idx = fs.make<TH1D>("resolvedHbb_bjet1_idx", "resolvedHbb_bjet1_idx", 25, -0.5, +24.5);
  jetHistograms* histograms_resolvedHbb_bjet2 = new jetHistograms("resolvedHbb_bjet2");
  histograms_resolvedHbb_bjet2->bookHistograms(fs);
  TH1* histogram_resolvedHbb_bjet2_idx = fs.make<TH1D>("resolvedHbb_bjet2_idx", "resolvedHbb_bjet2_idx", 25, -0.5, +24.5);
  TH1* histogram_resolvedHbb_bjet_numIndices = fs.make<TH1D>("resolvedHbb_bjet_numIndices", "resolvedHbb_bjet_numIndices", 25, -0.5, +24.5);
  TH1* histogram_resolvedHbb_bjet_mjj = fs.make<TH1D>("resolvedHbb_bjet_mjj", "resolvedHbb_bjet_mjj", 50, 0., 250.);
  
  jetHistograms* histograms_Wjj_jet1 = new jetHistograms("Wjj_jet1");
  histograms_Wjj_jet1->bookHistograms(fs);
  TH1* histogram_Wjj_jet1_idx = fs.make<TH1D>("Wjj_jet1_idx", "Wjj_jet1_idx", 25, -0.5, +24.5);
  jetHistograms* histograms_Wjj_jet2 = new jetHistograms("Wjj_jet2");
  histograms_Wjj_jet2->bookHistograms(fs);
  TH1* histogram_Wjj_jet2_idx = fs.make<TH1D>("Wjj_jet2_idx", "Wjj_jet2_idx", 25, -0.5, +24.5);
  TH1* histogram_Wjj_jet_numIndices = fs.make<TH1D>("Wjj_jet_numIndices", "Wjj_jet_numIndices", 25, -0.5, +24.5);
  TH1* histogram_Wjj_jet_mjj = fs.make<TH1D>("Wjj_jet_mjj", "Wjj_jet_mjj", 50, 0., 250.);

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

  memHistograms* histograms_memOutput_missingBJet_and_HadWJet_fullyMatched = new memHistograms("missingBJet_and_HadWJet", 0, 0, 0);
  histograms_memOutput_missingBJet_and_HadWJet_fullyMatched->bookHistograms(fs);
  memHistograms* histograms_memOutput_missingBJet_and_HadWJet_unmatchedLepton = new memHistograms("missingBJet_and_HadWJet", 1, 0, 0);
  histograms_memOutput_missingBJet_and_HadWJet_unmatchedLepton->bookHistograms(fs);
  memHistograms* histograms_memOutput_missingBJet_and_HadWJet_unmatchedBJet = new memHistograms("missingBJet_and_HadWJet", 0, 1, 0);
  histograms_memOutput_missingBJet_and_HadWJet_unmatchedBJet->bookHistograms(fs);
  memHistograms* histograms_memOutput_missingBJet_and_HadWJet_unmatchedWJet = new memHistograms("missingBJet_and_HadWJet", 0, 0, 1);
  histograms_memOutput_missingBJet_and_HadWJet_unmatchedWJet->bookHistograms(fs);

  int analyzedEntries = 0;
  int selectedEntries = 0;
  double selectedEntries_weighted = 0.;
  TH1* histogram_analyzedEntries = fs.make<TH1D>("analyzedEntries", "analyzedEntries", 1, -0.5, +0.5);
  TH1* histogram_selectedEntries = fs.make<TH1D>("selectedEntries", "selectedEntries", 1, -0.5, +0.5);
  cutFlowTableType cutFlowTable;
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

//--- build collections of generator level particles
    std::vector<GenParticle> genLeptons = genLeptonReader->read();
    std::vector<GenParticle> genBJets = genBJetReader->read();
    std::vector<GenParticle> genWJets = genWJetReader->read();
    if ( isDEBUG ) {
      dumpGenParticles("genLepton", genLeptons);
      dumpGenParticles("genBJet", genBJets);
      dumpGenParticles("genWJet", genWJets);
    }
    
    if ( apply_genWeight ) evtWeightRecorder.record_genWeight(boost::math::sign(eventInfo.genWeight));
    lheInfoReader->read();
    evtWeightRecorder.record_lheScaleWeight(lheInfoReader);
    evtWeightRecorder.record_puWeight(&eventInfo);

//--- build collections of electrons, muons and hadronic taus;
//    resolve overlaps in order of priority: muon, electron,
    const std::vector<RecoMuon> muons = muonReader->read();
    const std::vector<const RecoMuon*> muon_ptrs = convert_to_ptrs(muons);
    const std::vector<const RecoMuon*> cleanedMuons = muon_ptrs; 
    const std::vector<const RecoMuon*> tightMuons = tightMuonSelector(cleanedMuons, isHigherConePt);
    if ( isDEBUG ) {
      printCollection("tightMuons", tightMuons);
    }

    const std::vector<RecoElectron> electrons = electronReader->read();
    const std::vector<const RecoElectron*> electron_ptrs = convert_to_ptrs(electrons);
    const std::vector<const RecoElectron*> cleanedElectrons = electronCleaner(electron_ptrs, tightMuons);
    const std::vector<const RecoElectron*> tightElectrons = tightElectronSelector(cleanedElectrons, isHigherConePt);
    if ( isDEBUG ) {
      printCollection("tightElectrons", tightElectrons);
    }

    const std::vector<const RecoLepton*> tightLeptonsFull = mergeLeptonCollections(tightElectrons, tightMuons, isHigherConePt);
    const std::vector<const RecoLepton*> tightLeptons = pickFirstNobjects(tightLeptonsFull, 1);

//--- build collections of jets and select subset of jets passing b-tagging criteria
    const std::vector<RecoJet> jets_ak4 = jetReaderAK4->read();
    const std::vector<const RecoJet*> jet_ptrs_ak4 = convert_to_ptrs(jets_ak4);
    const std::vector<const RecoJet*> cleanedJetsAK4_wrtLeptons = jetCleanerAK4_dR04(jet_ptrs_ak4, tightLeptons);
    const std::vector<const RecoJet*> selJetsAK4 = jetSelectorAK4(cleanedJetsAK4_wrtLeptons, isHigherPt);
    const std::vector<const RecoJet*> selBJetsAK4_loose = jetSelectorAK4_bTagLoose(cleanedJetsAK4_wrtLeptons, isHigherPt);
    const std::vector<const RecoJet*> selBJetsAK4_medium = jetSelectorAK4_bTagMedium(cleanedJetsAK4_wrtLeptons, isHigherPt);

    double evtWeight = evtWeightRecorder.get(central_or_shift);

    if ( isDEBUG ) {
      printCollection("uncleaned AK4 jets", jet_ptrs_ak4);
      printCollection("cleaned AK4 jets(wrtLeptons)", cleanedJetsAK4_wrtLeptons);
      printCollection("selected AK4 jets", selJetsAK4);
    }

    // require at least one lepton passing tight selection criteria
    if ( !(tightLeptons.size() >= 1) ) {
      continue;
    }
    cutFlowTable.update(">= 1 sel leptons", evtWeight);
    const RecoLepton* tightLepton = tightLeptons[0];

    const double minPt_lead = 25.;
    if ( !(tightLepton->cone_pt() > minPt_lead) ) {
      continue;
    }
    cutFlowTable.update("lepton pT > 25 GeV", evtWeight);

    // require exactly one lepton passing tight selection criteria, to avoid overlap with other channels
    if ( !(tightLeptonsFull.size() <= 1) ) {
      continue;
    }
    cutFlowTable.update("<= 1 tight leptons", evtWeight);

    const std::vector<RecoJetAK8> jets_ak8_Hbb = jetReaderAK8_Hbb->read();
    const std::vector<const RecoJetAK8*> jet_ptrs_ak8_Hbb = convert_to_ptrs(jets_ak8_Hbb);

    if ( isDEBUG ) {
      printCollection("uncleaned AK8 jets (Hbb)", jet_ptrs_ak8_Hbb);
    }

    // select jets from H->bb decay
    const std::vector<const RecoJetAK8*> cleanedJetsAK8_wrtLeptons = jetCleanerAK8_dR08(jet_ptrs_ak8_Hbb, tightLeptons);
    const std::vector<const RecoJetAK8*> selJetsAK8_Hbb = jetSelectorAK8_Hbb(cleanedJetsAK8_wrtLeptons, isHigherCSV_ak8);
    const std::vector<const RecoJet*> selJetsAK4_Hbb = jetSelectorAK4(cleanedJetsAK4_wrtLeptons, isHigherCSV);
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
      if ( isDEBUG ) {
	std::cout << "found boosted H->bb decay:" << std::endl;
	std::cout << "AK8 jet: pT = " << selJetAK8_Hbb->pt() << ", eta = " << selJetAK8_Hbb->eta() << ", phi = " << selJetAK8_Hbb->phi() << ","
		  << " dR(selLepton) = " << deltaR(selJetAK8_Hbb->p4(), tightLepton->p4()) << std::endl;
	std::cout << " subjet #1: pT = " << selJet1_Hbb->pt() << ", eta = " << selJet1_Hbb->eta() << ", phi = " << selJet1_Hbb->phi() << ","
		  << " dR(selLepton) = " << deltaR(selJet1_Hbb->p4(), tightLepton->p4()) << std::endl;
	std::cout << " subjet #2: pT = " << selJet2_Hbb->pt() << ", eta = " << selJet2_Hbb->eta() << ", phi = " << selJet2_Hbb->phi() << ","
		  << " dR(selLepton) = " << deltaR(selJet2_Hbb->p4(), tightLepton->p4()) << std::endl;
      }
      double min_BtagCSV_loose = jetSelectorAK8_Hbb.getSelector().get_min_BtagCSV_loose();
      if ( selJetAK8_Hbb->subJet1()->BtagCSV() >= min_BtagCSV_loose  ) ++numBJets_loose;
      if ( selJetAK8_Hbb->subJet2()->BtagCSV() >= min_BtagCSV_loose  ) ++numBJets_loose;
      double min_BtagCSV_medium = jetSelectorAK8_Hbb.getSelector().get_min_BtagCSV_medium();
      if ( selJetAK8_Hbb->subJet1()->BtagCSV() >= min_BtagCSV_medium ) ++numBJets_medium;
      if ( selJetAK8_Hbb->subJet2()->BtagCSV() >= min_BtagCSV_medium ) ++numBJets_medium;
    } else if ( selJetsAK4_Hbb.size() >= 2 ) {
      selJet1_Hbb = selJetsAK4_Hbb[0];
      selJet2_Hbb = selJetsAK4_Hbb[1];
      if ( isDEBUG ) {
	std::cout << "found resolved H->bb decay:" << std::endl;
	std::cout << "AK4 jet #1: pT = " << selJet1_Hbb->pt() << ", eta = " << selJet1_Hbb->eta() << ", phi = " << selJet1_Hbb->phi() << std::endl;
	std::cout << "AK4 jet #2: pT = " << selJet2_Hbb->pt() << ", eta = " << selJet2_Hbb->eta() << ", phi = " << selJet2_Hbb->phi() << std::endl;
      }
      const std::vector<const RecoJet*> particles = { selJetsAK4_Hbb[0], selJetsAK4_Hbb[1] };
      numBJets_loose = jetSelectorAK4_bTagLoose(particles, isHigherPt).size();
      numBJets_medium = jetSelectorAK4_bTagMedium(particles, isHigherPt).size();
    }
    if ( !(selJet1_Hbb && selJet2_Hbb) ) {
      continue;
    }
    cutFlowTable.update(">= 2 jets from H->bb", evtWeight);

    std::vector<const RecoJetBase*> selJets_Hbb = { selJet1_Hbb, selJet2_Hbb };
    std::sort(selJets_Hbb.begin(), selJets_Hbb.end(), isHigherPt);
    //const RecoJetBase* selJet_Hbb_lead = selJets_Hbb[0];
    //const RecoJetBase* selJet_Hbb_sublead = selJets_Hbb[1];

    if ( !(numBJets_medium >= 1) ) {
      continue;
    }
    cutFlowTable.update(">= 1 medium b-jet", evtWeight);

    // select jets from W->jj decay
    std::vector<const RecoJetAK8*> cleanedJetsAK8_wrtHbb;
    std::vector<const RecoJet*> cleanedJetsAK4_wrtHbb;
    if ( selJetAK8_Hbb ) {
      const std::vector<const RecoJetAK8*> overlaps = { selJetAK8_Hbb };
      cleanedJetsAK4_wrtHbb = jetCleanerAK4_dR12(cleanedJetsAK4_wrtLeptons, overlaps);
    } else {
      cleanedJetsAK4_wrtHbb = jetCleanerAK4_dR08(cleanedJetsAK4_wrtLeptons, selJets_Hbb);
    }
    const std::vector<const RecoJet*> selJetsAK4_Wjj = jetSelectorAK4(cleanedJetsAK4_wrtHbb, isHigherPt);
    const RecoJetBase* selJet1_Wjj = nullptr;
    const RecoJetBase* selJet2_Wjj = nullptr;
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
    if ( isDEBUG ) {
      std::cout << "found resolved W->jj decay:" << std::endl;
      std::cout << "AK4 jet #1:";
      if ( selJet1_Wjj ) std::cout << " pT = " << selJet1_Hbb->pt() << ", eta = " << selJet1_Hbb->eta() << ", phi = " << selJet1_Hbb->phi() << std::endl;
      else std::cout << " N/A" << std::endl;
      std::cout << "AK4 jet #2:";
      if ( selJet1_Wjj ) std::cout << " pT = " << selJet2_Hbb->pt() << ", eta = " << selJet2_Hbb->eta() << ", phi = " << selJet2_Hbb->phi() << std::endl;
      else std::cout << " N/A" << std::endl;
    }
    if ( !(selJet1_Wjj || selJet2_Wjj) ) {
      continue;
    }
    cutFlowTable.update(">= 1 jets from W->jj", evtWeight);
  
    std::vector<const RecoJetBase*> selJets_Wjj;
    if ( selJet1_Wjj ) selJets_Wjj.push_back(selJet1_Wjj);
    if ( selJet2_Wjj ) selJets_Wjj.push_back(selJet2_Wjj);
    std::sort(selJets_Wjj.begin(), selJets_Wjj.end(), isHigherPt);
    assert(selJets_Wjj.size() >= 1);
    //const RecoJetBase* selJet_Wjj_lead = selJets_Wjj[0];
    //const RecoJetBase* selJet_Wjj_sublead = nullptr;
    //if ( selJets_Wjj.size() >= 2 ) {
    //  selJet_Wjj_sublead = selJets_Wjj[1];
    //}

//--- compute MHT and linear MET discriminant (met_LD)
    //RecoMEt met = metReader->read();
    //const Particle::LorentzVector& metP4 = met.p4();
    //const std::vector<const RecoJet*> selJetsAK4_mht = jetSelectorAK4(cleanedJetsAK4_wrtLeptons, isHigherPt);
    //Particle::LorentzVector mhtP4 = compMHT(tightLeptons, {}, selJetsAK4_mht);
    //double met_LD = compMEt_LD(metP4, mhtP4);

//--- fill histograms with events passing final selection
    std::vector<int> genBJet_pdgIds = { -5, +5 }; 
    if ( selJetAK8_Hbb )
    {
      fillHistograms_jets(
        selJets_Hbb,
	genBJets, &genBJet_pdgIds,
	*histograms_boostedHbb_bjet1, histogram_boostedHbb_bjet1_idx,
	*histograms_boostedHbb_bjet2, histogram_boostedHbb_bjet2_idx,
	histogram_boostedHbb_bjet_numIndices, histogram_boostedHbb_bjet_mjj, evtWeight);
    }
    else 
    {
      fillHistograms_jets(
        selJetsAK4_Hbb,
	genBJets, &genBJet_pdgIds,
	*histograms_resolvedHbb_bjet1, histogram_resolvedHbb_bjet1_idx,
	*histograms_resolvedHbb_bjet2, histogram_resolvedHbb_bjet2_idx,
	histogram_resolvedHbb_bjet_numIndices, histogram_resolvedHbb_bjet_mjj, evtWeight);
    }
    fillHistograms_jets(
      selJetsAK4_Wjj,
      genWJets, nullptr,
      *histograms_Wjj_jet1, histogram_Wjj_jet1_idx,
      *histograms_Wjj_jet2, histogram_Wjj_jet2_idx,
      histogram_Wjj_jet_numIndices, histogram_Wjj_jet_mjj, evtWeight);

    std::vector<MEMOutput_hh_bb1l> memOutputs_hh_bb1l = memReader->read();
    for ( std::vector<MEMOutput_hh_bb1l>::const_iterator memOutput = memOutputs_hh_bb1l.begin();
	  memOutput != memOutputs_hh_bb1l.end(); ++memOutput ) {
      fillHistograms_mem(
        *memOutput, 
	genLeptons, genBJets, genWJets, 
	*histograms_memOutput_fullyMatched, 
	*histograms_memOutput_unmatchedLepton, 
	*histograms_memOutput_unmatchedBJet, 
	*histograms_memOutput_unmatchedWJet, evtWeight);
    }
    std::vector<MEMOutput_hh_bb1l> memOutputs_hh_bb1l_missingBJet = memReader_missingBJet->read();
    for ( std::vector<MEMOutput_hh_bb1l>::const_iterator memOutput = memOutputs_hh_bb1l_missingBJet.begin();
	  memOutput != memOutputs_hh_bb1l_missingBJet.end(); ++memOutput ) {
      fillHistograms_mem(
        *memOutput, 
	genLeptons, genBJets, genWJets, 
	*histograms_memOutput_missingBJet_fullyMatched, 
	*histograms_memOutput_missingBJet_unmatchedLepton, 
	*histograms_memOutput_missingBJet_unmatchedBJet, 
	*histograms_memOutput_missingBJet_unmatchedWJet, evtWeight);
    }
    std::vector<MEMOutput_hh_bb1l> memOutputs_hh_bb1l_missingHadWJet = memReader_missingHadWJet->read();
    for ( std::vector<MEMOutput_hh_bb1l>::const_iterator memOutput = memOutputs_hh_bb1l_missingHadWJet.begin();
	  memOutput != memOutputs_hh_bb1l_missingHadWJet.end(); ++memOutput ) {
      fillHistograms_mem(
        *memOutput, 
	genLeptons, genBJets, genWJets, 
	*histograms_memOutput_missingHadWJet_fullyMatched, 
	*histograms_memOutput_missingHadWJet_unmatchedLepton, 
	*histograms_memOutput_missingHadWJet_unmatchedBJet, 
	*histograms_memOutput_missingHadWJet_unmatchedWJet, evtWeight);
    }
    std::vector<MEMOutput_hh_bb1l> memOutputs_hh_bb1l_missingBJet_and_HadWJet = memReader_missingBJet_and_HadWJet->read();
    for ( std::vector<MEMOutput_hh_bb1l>::const_iterator memOutput = memOutputs_hh_bb1l_missingBJet_and_HadWJet.begin();
	  memOutput != memOutputs_hh_bb1l_missingBJet_and_HadWJet.end(); ++memOutput ) {
      fillHistograms_mem(
        *memOutput, 
	genLeptons, genBJets, genWJets, 
	*histograms_memOutput_missingBJet_and_HadWJet_fullyMatched, 
	*histograms_memOutput_missingBJet_and_HadWJet_unmatchedLepton, 
	*histograms_memOutput_missingBJet_and_HadWJet_unmatchedBJet, 
	*histograms_memOutput_missingBJet_and_HadWJet_unmatchedWJet, evtWeight);
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
  delete jetReaderAK8_Hbb;
  delete metReader;
  delete genLeptonReader;
  delete genBJetReader;
  delete genWJetReader;
  delete lheInfoReader;

  delete inputTree;

  clock.Show("analyzeMEM_hh_bb1l");

  return EXIT_SUCCESS;
}
