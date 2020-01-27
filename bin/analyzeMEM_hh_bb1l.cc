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

#include "hhAnalysis/bbww/interface/RecoJetCollectionSelectorAK8_hh_bbWW_Hbb.h" // RecoJetSelectorAK8_hh_bbWW_Hbb
#include "hhAnalysis/bbww/interface/MEMOutput_hh_bb1l.h" // MEMOutput_hh_bb1l
#include "hhAnalysis/bbww/interface/MEMOutputReader_hh_bb1l.h" // MEMOutputReader_hh_bb1l
#include "hhAnalysis/bbww/interface/jetSelectionAuxFunctions.h" // selectJets_Hbb, countBJetsJets_Hbb, selectJets_Wjj
#include "hhAnalysis/bbww/interface/JetPair.h" // JetPair_Wjj
#include "hhAnalysis/bbww/interface/genMatchingAuxFunctions.h" // isGenMatched, countGenMatchedParticles
#include "hhAnalysis/bbww/interface/GenParticleMatcherFromHiggs.h" // GenParticleMatcherFromHiggs
#include "hhAnalysis/bbww/interface/GenParticleMatcherFromTop.h" // GenParticleMatcherFromTop

#include <TBenchmark.h> // TBenchmark
#include <TString.h> // TString, Form
#include <TError.h> // gErrorAbortLevel, kError
#include <TRandom3.h> // TRandom3
#include <TROOT.h> // TROOT
#include <TH1.h> // TH1, TH1D
#include <TH2.h> // TH2, TH2D

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
fillHistograms_genJets(const std::vector<const GenJet*>& genJets, const GenJetCollectionSelector& genJetSelector,
                       TH1* histogram_genJet1_pt, TH1* histogram_genJet1_absEta, 
	               TH1* histogram_genJet2_pt, TH1* histogram_genJet2_absEta, double evtWeight) 
{
  if ( genJets.size() == 2 )
  {
    const GenJet* genJet_lead = genJets[0];
    fillWithOverFlow(histogram_genJet1_pt, genJet_lead->pt(), evtWeight);
    if ( genJet_lead->pt() > genJetSelector.getSelector().get_min_pt() )
    {
      fillWithOverFlow(histogram_genJet1_absEta, genJet_lead->absEta(), evtWeight);
    }

    const GenJet* genJet_sublead = genJets[1];
    fillWithOverFlow(histogram_genJet2_pt, genJet_sublead->pt(), evtWeight);
    if ( genJet_sublead->pt() > genJetSelector.getSelector().get_min_pt() )
    {
      fillWithOverFlow(histogram_genJet2_absEta, genJet_sublead->absEta(), evtWeight);
    }
  }
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
		    const std::vector<const GenJet*>& genJets, 
		    jetHistograms& histograms_jet1, TH1* histogram_idx1, 
		    jetHistograms& histograms_jet2, TH1* histogram_idx2, TH1* histogram_numIndices, TH1* histogram_mjj, double evtWeight)
{
  std::vector<int> indices;
  size_t numJets = jets.size();
  for ( size_t idxJet = 0; idxJet < numJets; ++idxJet )
  {
    const T* jet = jets[idxJet];
    bool isMatched = isGenMatchedT<GenJet>(jet->eta(), jet->phi(), genJets);
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
    histogram_LR_ = fs.make<TH1D>(histogramName_LR.data(), histogramName_LR.data(), 500, -40., +10.);
    std::string histogramName_weightS = Form("%s_weightS_%s", histogramName_prefix.data(), histogramName_suffix.data());
    histogram_weightS_ = fs.make<TH1D>(histogramName_weightS.data(), histogramName_weightS.data(), 500, -40., +10.);
    std::string histogramName_weightB = Form("%s_weightB_%s", histogramName_prefix.data(), histogramName_suffix.data());
    histogram_weightB_ = fs.make<TH1D>(histogramName_weightB.data(), histogramName_weightB.data(), 500, -40., +10.);
    std::string histogramName_isValid = Form("%s_isValid_%s", histogramName_prefix.data(), histogramName_suffix.data());
    histogram_isValid_ = fs.make<TH1D>(histogramName_isValid.data(), histogramName_isValid.data(), 2, -0.5, +1.5);
  }
  void fillHistograms(const MEMOutput_hh_bb1l& memOutput, double evtWeight)
  {
    if ( memOutput.isValid() )
    { 
      fillWithOverFlow(histogram_LR_, TMath::Log10(TMath::Max(1.e-37, 1. - memOutput.LR())), evtWeight);
      fillWithOverFlow(histogram_weightS_, TMath::Log10(TMath::Max((Float_t)1.e-37, memOutput.weight_signal())), evtWeight);
      fillWithOverFlow(histogram_weightB_, TMath::Log10(TMath::Max((Float_t)1.e-37, memOutput.weight_background())), evtWeight);
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
		   const std::vector<const GenLepton*>& genLeptons, 
		   const std::vector<const GenJet*>& genBJets, 
		   const std::vector<const GenJet*>& genWJets, 
		   memHistograms& histograms_fullyMatched, 
		   memHistograms& histograms_unmatchedLepton, 
		   memHistograms& histograms_unmatchedBJet, 
		   memHistograms& histograms_unmatchedWJet, double evtWeight)
{
  int numUnmatchedLeptons = 0;
  if ( !isGenMatchedT<GenLepton>(memOutput.lepton_eta_, memOutput.lepton_phi_, genLeptons) ) 
  {
    ++numUnmatchedLeptons;
  }
  int numUnmatchedBJets = 0;
  if ( memOutput.bjet1_isReconstructed_ && !isGenMatchedT<GenJet>(memOutput.bjet1_eta_, memOutput.bjet1_phi_, genBJets) )
  { 
    ++numUnmatchedBJets;
  }
  if ( memOutput.bjet2_isReconstructed_ && !isGenMatchedT<GenJet>(memOutput.bjet2_eta_, memOutput.bjet2_phi_, genBJets) )
  { 
    ++numUnmatchedBJets;
  }
  int numUnmatchedWJets = 0;
  if ( memOutput.wjet1_isReconstructed_ && !isGenMatchedT<GenJet>(memOutput.wjet1_eta_, memOutput.wjet1_phi_, genWJets) )
  { 
    ++numUnmatchedWJets;
  }
  if ( memOutput.wjet2_isReconstructed_ && !isGenMatchedT<GenJet>(memOutput.wjet2_eta_, memOutput.wjet2_phi_, genWJets) )
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

void dumpGenLeptons(const std::string& label, const std::vector<GenLepton>& genLeptons)
{
  for ( size_t idxLepton = 0; idxLepton < genLeptons.size(); ++idxLepton ) {
    std::cout << label << " #" << idxLepton << ":" << " ";
    std::cout << genLeptons[idxLepton];
    std::cout << std::endl;
  }
}

void dumpGenParticles(const std::string& label, const std::vector<GenParticle>& genParticles)
{
  for ( size_t idxParticle = 0; idxParticle < genParticles.size(); ++idxParticle ) {
    std::cout << label << " #" << idxParticle << ":" << " ";
    std::cout << genParticles[idxParticle];
    std::cout << std::endl;
  }
}

void dumpGenJets(const std::string& label, const std::vector<GenJet>& genJets)
{
  for ( size_t idxJet = 0; idxJet < genJets.size(); ++idxJet ) {
    std::cout << label << " #" << idxJet << ":" << " ";
    std::cout << genJets[idxJet];
    std::cout << std::endl;
  }
}

int
getIndex(const std::vector<JetPair_Wjj>& pairs)
{
  size_t numPairs = pairs.size();
  for ( size_t idx = 0; idx < numPairs; ++idx ) 
  {
    const JetPair_Wjj& pair = pairs[idx];
    if ( pair.jet1_isGenMatched_ && pair.jet2_isGenMatched_ )
    {
      return idx;
    }
  }
  return -1;
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

  bool jetCleaningByIndex = cfg_analyze.getParameter<bool>("jetCleaningByIndex");

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

  const double selElectron_min_pt = 32.;
  const double selElectron_max_absEta = 2.5;
  const double selMuon_min_pt = 25.;
  const double selMuon_max_absEta = 2.4;  

  RecoJetReader* jetReaderAK4 = new RecoJetReader(era, isMC, branchName_jets_ak4, false);
  inputTree->registerReader(jetReaderAK4);
  RecoJetCollectionCleaner jetCleanerAK4_dR04(0.4, isDEBUG);
  RecoJetCollectionCleanerByIndex jetCleanerAK4_byIndex(isDEBUG);
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
  const double selJetAK4_max_absEta_Wjj = 4.7;
  //const double selJetAK4_max_absEta_Wjj = 2.4;

  RecoJetCollectionSelector jetSelectorAK4_Wjj(era, -1, isDEBUG);
  jetSelectorAK4_Wjj.getSelector().set_min_pt(selJetAK4_min_pt_Wjj);
  jetSelectorAK4_Wjj.getSelector().set_max_absEta(selJetAK4_max_absEta_Wjj);

  RecoJetReaderAK8* jetReaderAK8_Hbb = new RecoJetReaderAK8(era, branchName_jets_ak8_Hbb, branchName_subjets_ak8_Hbb); 
  inputTree->registerReader(jetReaderAK8_Hbb);
  RecoJetReaderAK8* jetReaderAK8_Wjj = new RecoJetReaderAK8(era, branchName_jets_ak8_Wjj, branchName_subjets_ak8_Wjj); 
  inputTree->registerReader(jetReaderAK8_Wjj);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR08(0.8, isDEBUG);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR12(1.2, isDEBUG);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR16(1.6, isDEBUG);
  RecoJetCollectionSelectorAK8_hh_bbWW_Hbb jetSelectorAK8_Hbb(era, -1, isDEBUG);
  RecoJetCollectionSelectorAK8_hh_Wjj jetSelectorAK8_Wjj(era, -1, isDEBUG);
 
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

  GenJetCollectionCleaner genJetCleaner_dR04(0.4);

//--- declare missing transverse energy
  RecoMEtReader* metReader = new RecoMEtReader(era, isMC, branchName_met);
  inputTree->registerReader(metReader);

//--- declare generator level information
  LHEInfoReader* lheInfoReader = new LHEInfoReader(hasLHE);
  inputTree->registerReader(lheInfoReader);
  
//--- initialize BDT for ranking of W->jj decays
  TMVAInterface mva_Wjj = initialize_mva_Wjj();
 
  TH1* histogram_genLepton_pt = fs.make<TH1D>("histogram_genLepton_pt", "histogram_genLepton_pt", 50, 0., 250.);
  TH1* histogram_genLepton_absEta = fs.make<TH1D>("histogram_genLepton_absEta", "histogram_genLepton_absEta", 100, 0., 10.);

  TH1* histogram_genBJet1_pt = fs.make<TH1D>("histogram_genBJet1_pt", "histogram_genBJet1_pt", 50, 0., 250.);
  TH1* histogram_genBJet1_absEta = fs.make<TH1D>("histogram_genBJet1_absEta", "histogram_genBJet1_absEta", 100, 0., 10.);
  TH1* histogram_genBJet2_pt = fs.make<TH1D>("histogram_genBJet2_pt", "histogram_genBJet2_pt", 50, 0., 250.);
  TH1* histogram_genBJet2_absEta = fs.make<TH1D>("histogram_genBJet2_absEta", "histogram_genBJet2_absEta", 100, 0., 10.);

  TH1* histogram_genWJet1_pt = fs.make<TH1D>("histogram_genWJet1_pt", "histogram_genWJet1_pt", 50, 0., 250.);
  TH1* histogram_genWJet1_absEta = fs.make<TH1D>("histogram_genWJet1_absEta", "histogram_genWJet1_absEta", 100, 0., 10.);
  TH1* histogram_genWJet2_pt = fs.make<TH1D>("histogram_genWJet2_pt", "histogram_genWJet2_pt", 50, 0., 250.);
  TH1* histogram_genWJet2_absEta = fs.make<TH1D>("histogram_genWJet2_absEta", "histogram_genWJet2_absEta", 100, 0., 10.);

  TH2* histogram_selJetCorrelation = fs.make<TH2D>("selJetCorrelation", "selJetCorrelation", 4, -0.5, 3.5, 4, -0.5, 3.5);
  enum { k2Rec2Matched, k2Rec1Matched, k1Rec1Matched, k0Matched };
  TAxis* xAxis_selJetCorrelation = histogram_selJetCorrelation->GetXaxis();
  xAxis_selJetCorrelation->SetTitle("H->bb");
  xAxis_selJetCorrelation->SetBinLabel(1, "2Rec2Matched");
  xAxis_selJetCorrelation->SetBinLabel(2, "2Rec1Matched");
  xAxis_selJetCorrelation->SetBinLabel(3, "1Rec1Matched");
  xAxis_selJetCorrelation->SetBinLabel(4, "0Matched");
  TAxis* yAxis_selJetCorrelation = histogram_selJetCorrelation->GetYaxis();
  yAxis_selJetCorrelation->SetTitle("W->jj");
  yAxis_selJetCorrelation->SetBinLabel(1, "2Rec2Matched");
  yAxis_selJetCorrelation->SetBinLabel(2, "2Rec1Matched");
  yAxis_selJetCorrelation->SetBinLabel(3, "1Rec1Matched");
  yAxis_selJetCorrelation->SetBinLabel(4, "0Matched");

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
dumpGenLeptons("genLepton", genLeptons);      
dumpGenParticles("genNeutrino", genNeutrinos);
dumpGenParticles("genParticleFromHiggs", genParticlesFromHiggs);
dumpGenParticles("genWJet", genWJets);
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
    double genMEtPt, genMEtPhi;
    genParticleMatcher->getMEt(genMEtPt, genMEtPhi);

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
    std::vector<const GenJet*> cleanedGenBJets_wrtLeptons = genJetCleaner_dR04(genBJets_ptrs, genLeptons_passingEta);
    std::sort(cleanedGenBJets_wrtLeptons.begin(), cleanedGenBJets_wrtLeptons.end(), isHigherPt);
    genBJetSelector.getSelector().set_max_absEta(1.e+3);
    std::vector<const GenJet*> genBJets_passingPt = genBJetSelector(cleanedGenBJets_wrtLeptons);
    genBJetSelector.getSelector().set_max_absEta(selJetAK4_max_absEta_Hbb);
    std::vector<const GenJet*> genBJets_passingPt_and_Eta = genBJetSelector(cleanedGenBJets_wrtLeptons);

    fillHistograms_genJets(cleanedGenBJets_wrtLeptons, genBJetSelector,
      histogram_genBJet1_pt, histogram_genBJet1_absEta, histogram_genBJet2_pt, histogram_genBJet2_absEta, evtWeight);

    std::vector<const GenJet*> genWJets_ptrs = convert_to_ptrs(genWJets);
    std::vector<const GenJet*> cleanedGenWJets_wrtLeptons = genJetCleaner_dR04(genWJets_ptrs, genLeptons_passingEta);
    std::sort(cleanedGenWJets_wrtLeptons.begin(), cleanedGenWJets_wrtLeptons.end(), isHigherPt);
    genWJetSelector.getSelector().set_max_absEta(1.e+3);
    std::vector<const GenJet*> genWJets_passingPt = genWJetSelector(cleanedGenWJets_wrtLeptons);
    genWJetSelector.getSelector().set_max_absEta(selJetAK4_max_absEta_Wjj);
    std::vector<const GenJet*> genWJets_passingPt_and_Eta = genWJetSelector(cleanedGenWJets_wrtLeptons);
    
    fillHistograms_genJets(cleanedGenWJets_wrtLeptons, genWJetSelector,
      histogram_genWJet1_pt, histogram_genWJet1_absEta, histogram_genWJet2_pt, histogram_genWJet2_absEta, evtWeight);
    
//--- build collections of reconstructed electrons and muons
//    resolve overlaps in order of priority: muon, electron
    const std::vector<RecoMuon> muons = muonReader->read();
    const std::vector<const RecoMuon*> muon_ptrs = convert_to_ptrs(muons);
    const std::vector<const RecoMuon*> cleanedMuons = muon_ptrs; 
    tightMuonSelector.getSelector().set_min_pt(10.);
    const std::vector<const RecoMuon*> tightMuons_passingEta = tightMuonSelector(cleanedMuons, isHigherConePt);
    tightMuonSelector.getSelector().set_min_pt(selMuon_min_pt);
    const std::vector<const RecoMuon*> tightMuons_passingPt_and_Eta = tightMuonSelector(cleanedMuons, isHigherConePt);
    if ( isDEBUG ) {
      printCollection("tightMuons", tightMuons_passingPt_and_Eta);
    }

    const std::vector<RecoElectron> electrons = electronReader->read();
    const std::vector<const RecoElectron*> electron_ptrs = convert_to_ptrs(electrons);
    const std::vector<const RecoElectron*> cleanedElectrons = electronCleaner(electron_ptrs, tightMuons_passingPt_and_Eta);
    tightElectronSelector.getSelector().set_min_pt(10.);
    const std::vector<const RecoElectron*> tightElectrons_passingEta = tightElectronSelector(cleanedElectrons, isHigherConePt);
    tightElectronSelector.getSelector().set_min_pt(selElectron_min_pt);
    const std::vector<const RecoElectron*> tightElectrons_passingPt_and_Eta = tightElectronSelector(cleanedElectrons, isHigherConePt);
    if ( isDEBUG ) {
      printCollection("tightElectrons", tightElectrons_passingPt_and_Eta);
    }

    const std::vector<const RecoLepton*> tightLeptonsFull_passingEta = mergeLeptonCollections(tightElectrons_passingEta, tightMuons_passingEta, isHigherConePt);
    const std::vector<const RecoLepton*> tightLeptons_passingEta = pickFirstNobjects(tightLeptonsFull_passingEta, 1);
    const std::vector<const RecoLepton*> tightLeptonsFull_passingPt_and_Eta = mergeLeptonCollections(tightElectrons_passingPt_and_Eta, tightMuons_passingPt_and_Eta, isHigherConePt);
    const std::vector<const RecoLepton*> tightLeptons_passingPt_and_Eta = pickFirstNobjects(tightLeptonsFull_passingPt_and_Eta, 1);

//--- build collections of jets and select subset of jets passing b-tagging criteria
    const std::vector<RecoJet> jets_ak4 = jetReaderAK4->read();
    const std::vector<const RecoJet*> jet_ptrs_ak4 = convert_to_ptrs(jets_ak4);
    const std::vector<const RecoJet*> cleanedJetsAK4_wrtLeptons = jetCleaningByIndex ?
      jetCleanerAK4_byIndex(jet_ptrs_ak4, tightLeptons_passingPt_and_Eta) :
      jetCleanerAK4_dR04   (jet_ptrs_ak4, tightLeptons_passingPt_and_Eta)
    ;
    const std::vector<const RecoJet*> selJetsAK4 = jetSelectorAK4(cleanedJetsAK4_wrtLeptons, isHigherPt);
    const std::vector<const RecoJet*> selBJetsAK4_loose = jetSelectorAK4_bTagLoose(cleanedJetsAK4_wrtLeptons, isHigherPt);
    const std::vector<const RecoJet*> selBJetsAK4_medium = jetSelectorAK4_bTagMedium(cleanedJetsAK4_wrtLeptons, isHigherPt);

//--- require exactly one reconstructed lepton passing tight selection criteria
    bool passesTightLeptonEta_rec                = tightLeptons_passingEta.size() >= 1;
    bool passesTightLeptonEta_gen                = genLeptons_passingEta.size() >= 1;
    bool passesTightLeptonEta_rec_and_gen        = selectGenMatchedParticles(tightLeptons_passingEta, genLeptons_passingEta).size() >= 1;
    const std::string cutTightLeptonEta = ">= 1 tight lepton";
    if ( passesTightLeptonEta_rec                ) cutFlowTable.update(cutTightLeptonEta,        "rec",     evtWeight);
    if ( passesTightLeptonEta_gen                ) cutFlowTable.update(cutTightLeptonEta,        "gen",     evtWeight);
    if ( passesTightLeptonEta_rec_and_gen        ) cutFlowTable.update(cutTightLeptonEta,        "gen&rec", evtWeight);
    
    bool passesTightLeptonPt_and_Eta_rec         = tightLeptons_passingPt_and_Eta.size() >= 1;
    bool passesTightLeptonPt_and_Eta_gen         = genLeptons_passingPt_and_Eta.size() >= 1;
    bool passesTightLeptonPt_and_Eta_rec_and_gen = selectGenMatchedParticles(tightLeptons_passingPt_and_Eta, genLeptons_passingPt_and_Eta).size() >= 1;
    const std::string cutTightLeptonPt_and_Eta = Form("tight electron (muon) pT > %2.0f (%2.0f) GeV", selElectron_min_pt, selMuon_min_pt);
    if ( passesTightLeptonPt_and_Eta_rec         ) cutFlowTable.update(cutTightLeptonPt_and_Eta, "rec",     evtWeight);
    if ( passesTightLeptonPt_and_Eta_gen         ) cutFlowTable.update(cutTightLeptonPt_and_Eta, "gen",     evtWeight);
    if ( passesTightLeptonPt_and_Eta_rec_and_gen ) cutFlowTable.update(cutTightLeptonPt_and_Eta, "gen&rec", evtWeight);

    const RecoLepton* tightLepton = nullptr;
    if ( tightLeptons_passingPt_and_Eta.size() >= 1 ) 
    {
      tightLepton = tightLeptons_passingPt_and_Eta[0];
    }

    const std::vector<RecoJetAK8> jets_ak8_Hbb = jetReaderAK8_Hbb->read();
    const std::vector<const RecoJetAK8*> jet_ptrs_ak8_Hbb = convert_to_ptrs(jets_ak8_Hbb);
    const std::vector<RecoJetAK8> jets_ak8_Wjj = jetReaderAK8_Wjj->read();
    const std::vector<const RecoJetAK8*> jet_ptrs_ak8_Wjj = convert_to_ptrs(jets_ak8_Wjj);

//--- select jets from H->bb decay
    const std::vector<const RecoJetAK8*> cleanedJetsAK8_wrtLeptons = jetCleanerAK8_dR08(jet_ptrs_ak8_Hbb, tightLeptons_passingPt_and_Eta);
    const std::vector<const RecoJetAK8*> selJetsAK8_Hbb = jetSelectorAK8_Hbb(cleanedJetsAK8_wrtLeptons, isHigherCSV_ak8);
    const std::vector<const RecoJet*> selJetsAK4_Hbb = jetSelectorAK4(cleanedJetsAK4_wrtLeptons, isHigherCSV);
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

    bool passesBJetPt_rec                = selJets_Hbb.size() >= 2;
    bool passesBJetPt_gen                = genBJets_passingPt.size() >= 2;
    bool passesBJetPt_rec_and_gen        = selectGenMatchedParticles(selJets_Hbb, genBJets_passingPt).size() >= 2;
    const std::string cutBJetPt = ">= 2 jets from H->bb decay, passing pT > 25 GeV";
    if ( passesBJetPt_rec                 ) cutFlowTable.update(cutBJetPt,         "rec",     evtWeight);
    if ( passesBJetPt_gen                 ) cutFlowTable.update(cutBJetPt,         "gen",     evtWeight);
    if ( passesBJetPt_rec_and_gen         ) cutFlowTable.update(cutBJetPt,         "gen&rec", evtWeight);

    bool passesBJetPt_and_Eta_rec         = selJets_Hbb.size() >= 2;
    bool passesBJetPt_and_Eta_gen         = genBJets_passingPt_and_Eta.size() >= 2;
    bool passesBJetPt_and_Eta_rec_and_gen = selectGenMatchedParticles(selJets_Hbb, genBJets_passingPt_and_Eta).size() >= 2;
    const std::string cutBJetPt_and_Eta = ">= 2 jets from H->bb decay, passing pT > 25 GeV & abs(eta) < 2.4";
    if ( passesBJetPt_and_Eta_rec         ) cutFlowTable.update(cutBJetPt_and_Eta, "rec",     evtWeight);
    if ( passesBJetPt_and_Eta_gen         ) cutFlowTable.update(cutBJetPt_and_Eta, "gen",     evtWeight);
    if ( passesBJetPt_and_Eta_rec_and_gen ) cutFlowTable.update(cutBJetPt_and_Eta, "gen&rec", evtWeight);

    int numBJets_loose  = 0;
    int numBJets_medium = 0;
    if ( selJetT_Hbb ) 
    {
      countBJetsJets_Hbb(*selJetT_Hbb, jetSelectorAK8_Hbb, jetSelectorAK4_bTagLoose, jetSelectorAK4_bTagMedium, numBJets_loose, numBJets_medium);
    }

    bool passesBJetCSV_rec                = numBJets_medium >= 1;
    bool passesBJetCSV_gen                = passesBJetPt_and_Eta_gen;
    bool passesBJetCSV_rec_and_gen        = passesBJetPt_and_Eta_rec_and_gen && passesBJetCSV_rec;
    const std::string cutBJetCSV = ">= 1 medium b-jet";
    if ( passesBJetCSV_rec                ) cutFlowTable.update(cutBJetCSV,        "rec",     evtWeight);
    if ( passesBJetCSV_gen                ) cutFlowTable.update(cutBJetCSV,        "gen",     evtWeight);
    if ( passesBJetCSV_rec_and_gen        ) cutFlowTable.update(cutBJetCSV,        "gen&rec", evtWeight);

//--- select jets from W->jj decay
    std::vector<selJetsType_Wjj> selJetsT_Wjj;
    if ( selJetT_Hbb )
    {
      selJetsT_Wjj = selectJets_Wjj(
        jet_ptrs_ak8_Wjj, jetCleanerAK8_dR12, jetCleanerAK8_dR16, jetSelectorAK8_Wjj, 
        cleanedJetsAK4_wrtLeptons, jetCleanerAK4_dR08, jetCleanerAK4_dR12, jetSelectorAK4,
        *selJetT_Hbb, 
        tightLepton, selBJetsAK4_medium, mva_Wjj, eventInfo);
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

    bool passesWJetPt_rec                 = selJets_Wjj.size() >= 2;
    bool passesWJetPt_gen                 = genWJets_passingPt.size() >= 2;
    bool passesWJetPt_rec_and_gen         = selectGenMatchedParticles(selJets_Wjj, genWJets_passingPt).size() >= 2;
    const std::string cutWJetPt = ">= 2 jets from H->bb decay, passing pT > 25 GeV";
    if ( passesWJetPt_rec                 ) cutFlowTable.update(cutWJetPt,         "rec",     evtWeight);
    if ( passesWJetPt_gen                 ) cutFlowTable.update(cutWJetPt,         "gen",     evtWeight);
    if ( passesWJetPt_rec_and_gen         ) cutFlowTable.update(cutWJetPt,         "gen&rec", evtWeight);

    bool passesWJetPt_and_Eta_rec         = selJets_Wjj.size() >= 2;
    bool passesWJetPt_and_Eta_gen         = genWJets_passingPt_and_Eta.size() >= 2;
    bool passesWJetPt_and_Eta_rec_and_gen = selectGenMatchedParticles(selJets_Wjj, genWJets_passingPt_and_Eta).size() >= 2;
    const std::string cutWJetPt_and_Eta = Form(">= 2 jets from H->bb decay, passing pT > 25 GeV & abs(eta) < %1.1f", selJetAK4_max_absEta_Wjj);
    if ( passesWJetPt_and_Eta_rec         ) cutFlowTable.update(cutWJetPt_and_Eta, "rec",     evtWeight);
    if ( passesWJetPt_and_Eta_gen         ) cutFlowTable.update(cutWJetPt_and_Eta, "gen",     evtWeight);
    if ( passesWJetPt_and_Eta_rec_and_gen ) cutFlowTable.update(cutWJetPt_and_Eta, "gen&rec", evtWeight);

//--- compute MHT and linear MET discriminant (met_LD)
    //RecoMEt met = metReader->read();
    //const Particle::LorentzVector& metP4 = met.p4();
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
    const std::vector<const RecoJet*> tmpJetsAK4_Hbb = jetSelectorAK4(cleanedJetsAK4_wrtLeptons, isHigherCSV);
    const std::vector<const RecoJet*> selJetsAK4_Hbb_genMatched = selectGenMatchedParticles(tmpJetsAK4_Hbb, genBJets_ptrs);
    int idxHbb = -1;
    if      ( selJetsAK4_Hbb.size() == 2 && selJetsAK4_Hbb_genMatched.size() == 2 ) idxHbb = k2Rec2Matched;
    else if ( selJetsAK4_Hbb.size() == 2 && selJetsAK4_Hbb_genMatched.size() == 1 ) idxHbb = k2Rec1Matched;
    else if ( selJetsAK4_Hbb.size() == 1 && selJetsAK4_Hbb_genMatched.size() == 1 ) idxHbb = k1Rec1Matched;
    else                                                                            idxHbb = k0Matched;

    const std::vector<const RecoJet*> cleanedJetsAK4_wrtHbb = jetCleanerAK4_dR04(cleanedJetsAK4_wrtLeptons, std::vector<const RecoJetBase*>({ selJet1_Hbb, selJet2_Hbb }));
    const std::vector<const RecoJet*> selJetsAK4_Wjj = jetSelectorAK4(cleanedJetsAK4_wrtHbb, isHigherPt);
    std::vector<JetPair_Wjj> jetPairs_Wjj = makeJetPairs_Wjj(selJetsAK4_Wjj, &genWJets_ptrs);
    rankJetPairs_Wjj(jetPairs_Wjj, selJetsAK4_Wjj, *tightLepton, numBJets_medium, mva_Wjj, eventInfo);
    std::vector<const RecoJet*> tmpJetsAK4_Wjj;
    if ( jetPairs_Wjj.size() >= 1 ) 
    {
      const JetPair_Wjj& jetPair1_Wjj = jetPairs_Wjj[0];
      tmpJetsAK4_Wjj.push_back(jetPair1_Wjj.jet1_);
      tmpJetsAK4_Wjj.push_back(jetPair1_Wjj.jet2_);
    } 
    else 
    {
      if ( selJetsAK4_Wjj.size() >= 1 ) tmpJetsAK4_Wjj.push_back(selJetsAK4_Wjj[0]);
      if ( selJetsAK4_Wjj.size() >= 2 ) tmpJetsAK4_Wjj.push_back(selJetsAK4_Wjj[1]);
    }
    const std::vector<const RecoJet*> selJetsAK4_Wjj_genMatched = selectGenMatchedParticles(tmpJetsAK4_Wjj, genWJets_ptrs);
    int idxWjj = -1;
    if      ( selJetsAK4_Wjj.size() >= 2 && selJetsAK4_Wjj_genMatched.size() >= 2 ) idxWjj = k2Rec2Matched;
    else if ( selJetsAK4_Wjj.size() >= 2 && selJetsAK4_Wjj_genMatched.size() >= 1 ) idxWjj = k2Rec1Matched;
    else if ( selJetsAK4_Wjj.size() >= 1 && selJetsAK4_Wjj_genMatched.size() >= 1 ) idxWjj = k1Rec1Matched;
    else                                                                            idxWjj = k0Matched;

    histogram_selJetCorrelation->Fill(idxHbb, idxWjj, evtWeight);

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
    fillHistograms_jets(
      selJetsAK4_Wjj,
      genWJets_ptrs, 
      *histograms_Wjj_jet1, histogram_Wjj_jet1_idx,
      *histograms_Wjj_jet2, histogram_Wjj_jet2_idx,
      histogram_Wjj_jet_numIndices, histogram_Wjj_jet_mjj, evtWeight);
 
    std::sort(jetPairs_Wjj.begin(), jetPairs_Wjj.end(), isHigherRankedByMass);
    int hadWJetPair_sortedByMass_idx = getIndex(jetPairs_Wjj);
    fillWithOverFlow(histogram_hadWJetPair_sortedByMass_idx, hadWJetPair_sortedByMass_idx, evtWeight); 
    std::sort(jetPairs_Wjj.begin(), jetPairs_Wjj.end(), isHigherRankedByDeltaR);
    int hadWJetPair_sortedByDeltaR_idx = getIndex(jetPairs_Wjj);
    fillWithOverFlow(histogram_hadWJetPair_sortedByDeltaR_idx, hadWJetPair_sortedByDeltaR_idx, evtWeight); 
    std::sort(jetPairs_Wjj.begin(), jetPairs_Wjj.end(), isHigherRankedByPt);
    int hadWJetPair_sortedByPt_idx = getIndex(jetPairs_Wjj);
    fillWithOverFlow(histogram_hadWJetPair_sortedByPt_idx, hadWJetPair_sortedByPt_idx, evtWeight); 
    std::sort(jetPairs_Wjj.begin(), jetPairs_Wjj.end(), isHigherRankedByScalarPt);
    int hadWJetPair_sortedByScalarPt_idx = getIndex(jetPairs_Wjj);
    fillWithOverFlow(histogram_hadWJetPair_sortedByScalarPt_idx, hadWJetPair_sortedByScalarPt_idx, evtWeight); 
    std::sort(jetPairs_Wjj.begin(), jetPairs_Wjj.end(), isHigherRankedByBDT);
    int hadWJetPair_sortedByBDT_idx = getIndex(jetPairs_Wjj);
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
  delete jetReaderAK8_Hbb;
  delete jetReaderAK8_Wjj;
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
