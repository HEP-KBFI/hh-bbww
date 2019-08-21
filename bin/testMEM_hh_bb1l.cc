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
#include <TLorentzVector.h> // TLorentzVector

#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h" // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/RecoJet.h" // RecoJet
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEt.h" // RecoMEt
#include "tthAnalysis/HiggsToTauTau/interface/GenLepton.h" // GenLepton
#include "tthAnalysis/HiggsToTauTau/interface/GenJet.h" // GenJet
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
#include "tthAnalysis/HiggsToTauTau/interface/GenJetReader.h" // GenJetReader
#include "tthAnalysis/HiggsToTauTau/interface/LHEInfoReader.h" // LHEInfoReader
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
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // getBTagWeight_option, getHadTau_genPdgId, isHigherPt, isMatched, findFile
#include "tthAnalysis/HiggsToTauTau/interface/generalAuxFunctions.h" // format_vstring
#include "tthAnalysis/HiggsToTauTau/interface/mvaInputVariables.h" // comp_lep1_conePt, comp_lep2_conePt
#include "tthAnalysis/HiggsToTauTau/interface/hltPath.h" // hltPath, create_hltPaths, hltPaths_isTriggered, hltPaths_delete
#include "tthAnalysis/HiggsToTauTau/interface/hltPathReader.h" // hltPathReader
#include "tthAnalysis/HiggsToTauTau/interface/Data_to_MC_CorrectionInterface_2016.h"
#include "tthAnalysis/HiggsToTauTau/interface/Data_to_MC_CorrectionInterface_2017.h"
#include "tthAnalysis/HiggsToTauTau/interface/Data_to_MC_CorrectionInterface_2018.h"
#include "tthAnalysis/HiggsToTauTau/interface/lutAuxFunctions.h" // loadTH2, get_sf_from_TH2
#include "tthAnalysis/HiggsToTauTau/interface/cutFlowTable.h" // cutFlowTableType
#include "tthAnalysis/HiggsToTauTau/interface/TTreeWrapper.h" // TTreeWrapper
#include "tthAnalysis/HiggsToTauTau/interface/hltFilter.h" // hltFilter()
#include "tthAnalysis/HiggsToTauTau/interface/mT2_2particle.h" // mT2_2particle::comp_mT
#include "tthAnalysis/HiggsToTauTau/interface/mT2_3particle.h" // mT2_3particle::comp_mT
#include "tthAnalysis/HiggsToTauTau/interface/XGBInterface.h" // XGBInterface
#include "tthAnalysis/HiggsToTauTau/interface/MVAInputVarHistManager.h" // MVAInputVarHistManager
#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow()

#include "hhAnalysis/multilepton/interface/RecoJetCollectionSelectorAK8_hh_Wjj.h" // RecoJetSelectorAK8_hh_Wjj
#include "hhAnalysis/multilepton/interface/EventInfoHH.h" // EventInfoHH
#include "hhAnalysis/multilepton/interface/EventInfoHHReader.h" // EventInfoHHReader

#include "hhAnalysis/bbww/interface/EvtHistManager_hh_bb1l.h" // EvtHistManager_hh_bb1l
#include "hhAnalysis/bbww/interface/RecoJetCollectionSelectorAK8_hh_bbWW_Hbb.h" // RecoJetSelectorAK8_hh_bbWW_Hbb
#include "hhAnalysis/bbww/interface/testMEMauxFunctions.h" // findGenLepton_and_NeutrinoFromWBoson, findGenJetsFromWBoson

#include "hhAnalysis/bbwwMEM/interface/MEMbbwwAlgoSingleLepton.h"
#include "hhAnalysis/bbwwMEM/interface/MeasuredParticle.h" // MeasuredParticle
#include "hhAnalysis/bbwwMEM/interface/memAuxFunctions.h"

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

void dumpGenParticles(const std::string& label, const std::vector<GenParticle>& particles)
{
  for ( size_t idxParticle = 0; idxParticle < particles.size(); ++idxParticle ) {
    std::cout << label << " #" << idxParticle << ":" << " ";
    std::cout << particles[idxParticle];
    std::cout << std::endl;
  }
}

void printHbb(const std::vector<const RecoJetAK8*>& jets_ak8, const RecoJetCollectionSelectorAK8_hh_bbWW_Hbb& jetSelectorAK8_Hbb,
	      const std::vector<GenParticle>& genBJets)
{
  std::cout << "<printHbb>:" << std::endl;
  std::cout << "#genBJets = " << genBJets.size() << std::endl;
  for ( size_t idxBJet = 0; idxBJet < genBJets.size(); ++idxBJet ) {
    const GenParticle& genBJet = genBJets[idxBJet];
    std::cout << " genBJet #" << idxBJet << ": pT = " << genBJet.pt() << ", eta = " << genBJet.eta() << ", phi = " << genBJet.phi() << std::endl;
  }
  if ( genBJets.size() == 2 ) {
    bool isMatched = false;
    Particle::LorentzVector genHbbP4 = genBJets[0].p4() + genBJets[1].p4();
    std::cout << "genHbb: pT = " << genHbbP4.pt() << ", eta = " << genHbbP4.eta() << ", phi = " << genHbbP4.phi() << std::endl;
    for ( std::vector<const RecoJetAK8*>::const_iterator jet_ak8 = jets_ak8.begin();
	  jet_ak8 != jets_ak8.end(); ++jet_ak8 ) {
      double dR = deltaR(genHbbP4, (*jet_ak8)->p4());
      if ( dR < 0.8 ) {
	std::cout << "matches reconstructed AK8 jet: pT = " << (*jet_ak8)->pt() << ", eta = " << (*jet_ak8)->eta() << ", phi = " << (*jet_ak8)->phi() << ", which ";
	if ( jetSelectorAK8_Hbb.getSelector()(**jet_ak8) ) {
	  std::cout << "PASSES";
	  isMatched = true;
	} else {
	  std::cout << "FAILS";
	}
	std::cout << " the H->bb jet selection." << std::endl;
      }
    }
    if ( genHbbP4.pt() > 100. && !isMatched ) std::cout << "--> DEBUG (Hbb) !!" << std::endl;
  }
}

void printWjj(const std::vector<const RecoJetAK8*>& jets_ak8, const RecoJetCollectionSelectorAK8_hh_Wjj& jetSelectorAK8_Wjj,
	      const std::vector<GenParticle>& genWBosons, const std::vector<GenParticle>& genWJets)
{
  std::cout << "<printWjj>:" << std::endl;
  std::cout << "#genWBosons = " << genWBosons.size() << std::endl;
  for ( size_t idxWBoson = 0; idxWBoson < genWBosons.size(); ++idxWBoson ) {
    const GenParticle& genWBoson = genWBosons[idxWBoson];
    std::cout << " genWBoson #" << idxWBoson << ": pT = " << genWBoson.pt() << ", eta = " << genWBoson.eta() << ", phi = " << genWBoson.phi() << std::endl;
  }
  std::cout << "#genWJets = " << genWJets.size() << std::endl;
  for ( size_t idxWJet = 0; idxWJet < genWJets.size(); ++idxWJet ) {
    const GenParticle& genWJet = genWJets[idxWJet];
    std::cout << " genWJet #" << idxWJet << ": pT = " << genWJet.pt() << ", eta = " << genWJet.eta() << ", phi = " << genWJet.phi() << std::endl;
  }
  if ( genWBosons.size() == 1 ) {
    bool isMatched = false;
    Particle::LorentzVector genWjjP4 = genWBosons[0].p4();
    std::cout << "genWjj: pT = " << genWjjP4.pt() << ", eta = " << genWjjP4.eta() << ", phi = " << genWjjP4.phi() << std::endl;
    for ( std::vector<const RecoJetAK8*>::const_iterator jet_ak8 = jets_ak8.begin();
	  jet_ak8 != jets_ak8.end(); ++jet_ak8 ) {
      double dR = deltaR(genWjjP4, (*jet_ak8)->p4());
      if ( dR < 0.8 ) {
	std::cout << "matches reconstructed AK8 jet: pT = " << (*jet_ak8)->pt() << ", eta = " << (*jet_ak8)->eta() << ", phi = " << (*jet_ak8)->phi() << ","
		  << " msoftdrop = " << (*jet_ak8)->msoftdrop() << ", tau21 = " << (*jet_ak8)->tau2()/(*jet_ak8)->tau1() << ", which ";
	if ( jetSelectorAK8_Wjj.getSelector()(**jet_ak8) ) {
	  std::cout << "PASSES";
	  isMatched = true;
	} else {
	  std::cout << "FAILS";
	}
	std::cout << " the W->jj jet selection." << std::endl;
	std::cout << "generator-level subjets:" << std::endl;
	for ( std::vector<GenParticle>::const_iterator genWJet1 = genWJets.begin();
	      genWJet1 != genWJets.end(); ++genWJet1 ) {
	  for ( std::vector<GenParticle>::const_iterator genWJet2 = genWJet1 + 1;
		genWJet2 != genWJets.end(); ++genWJet2 ) {
	    if ( deltaR(genWJet1->p4() + genWJet2->p4(), genWjjP4) < 1.e-1 && std::fabs((genWJet1->p4() + genWJet2->p4()).mass() - genWjjP4.mass()) < 1.e+1 ) {
	      std::cout << " genWJet #1: pT = " << genWJet1->pt() << ", eta = " << genWJet1->eta() << ", phi = " << genWJet1->phi() << std::endl;
	      std::cout << " genWJet #2: pT = " << genWJet2->pt() << ", eta = " << genWJet2->eta() << ", phi = " << genWJet2->phi() << std::endl;
	    }
	  }
	}
	std::cout << "reconstructed subjets:" << std::endl;
	const RecoSubjetAK8* subjet1 = (*jet_ak8)->subJet1();
	if ( subjet1 ) std::cout << " subjet #1: pT = " << subjet1->pt() << ", eta = " << subjet1->eta() << ", phi = " << subjet1->phi() << std::endl;
	const RecoSubjetAK8* subjet2 = (*jet_ak8)->subJet2();
	if ( subjet2 ) std::cout << " subjet #2: pT = " << subjet2->pt() << ", eta = " << subjet2->eta() << ", phi = " << subjet2->phi() << std::endl;
      }
    }
    if ( genWjjP4.pt() > 100. && !isMatched ) std::cout << "--> DEBUG (Wjj) !!" << std::endl;
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

  std::cout << "<testMEM_hh_bb1l>:" << std::endl;

//--- keep track of time it takes the macro to execute
  TBenchmark clock;
  clock.Start("testMEM_hh_bb1l");

//--- read python configuration parameters
  if ( !edm::readPSetsFrom(argv[1])->existsAs<edm::ParameterSet>("process") )
    throw cms::Exception("testMEM_hh_bb1l")
      << "No ParameterSet 'process' found in configuration file = " << argv[1] << " !!\n";

  edm::ParameterSet cfg = edm::readPSetsFrom(argv[1])->getParameter<edm::ParameterSet>("process");

  edm::ParameterSet cfg_testMEM = cfg.getParameter<edm::ParameterSet>("testMEM_hh_bb1l");

  std::string treeName = cfg_testMEM.getParameter<std::string>("treeName");

  std::string process_string = cfg_testMEM.getParameter<std::string>("process");
  bool isSignal = ( process_string == "signal" ) ? true : false;
  const bool isMC_tH = process_string == "TH";
  const bool isMC_ttH = process_string == "TTH";

  std::string histogramDir = cfg_testMEM.getParameter<std::string>("histogramDir");

  std::string era_string = cfg_testMEM.getParameter<std::string>("era");
  const int era = get_era(era_string);

  vstring triggerNames_1e = cfg_testMEM.getParameter<vstring>("triggers_1e");
  std::vector<hltPath*> triggers_1e = create_hltPaths(triggerNames_1e);
  bool use_triggers_1e = cfg_testMEM.getParameter<bool>("use_triggers_1e");
  vstring triggerNames_1mu = cfg_testMEM.getParameter<vstring>("triggers_1mu");
  std::vector<hltPath*> triggers_1mu = create_hltPaths(triggerNames_1mu);
  bool use_triggers_1mu = cfg_testMEM.getParameter<bool>("use_triggers_1mu");

  bool apply_offline_e_trigger_cuts_1e = cfg_testMEM.getParameter<bool>("apply_offline_e_trigger_cuts_1e");
  bool apply_offline_e_trigger_cuts_1mu = cfg_testMEM.getParameter<bool>("apply_offline_e_trigger_cuts_1mu");

  const std::string electronSelection_string = cfg_testMEM.getParameter<std::string>("electronSelection");
  const std::string muonSelection_string     = cfg_testMEM.getParameter<std::string>("muonSelection");
  std::cout << "electronSelection_string = " << electronSelection_string << "\n"
               "muonSelection_string     = " << muonSelection_string     << '\n'
  ;
  const int electronSelection = get_selection(electronSelection_string);
  const int muonSelection     = get_selection(muonSelection_string);

  bool isMC = true;
  bool hasLHE = cfg_testMEM.getParameter<bool>("hasLHE");
  std::string central_or_shift = cfg_testMEM.getParameter<std::string>("central_or_shift");
  double lumiScale = 1.;
  bool apply_genWeight = cfg_testMEM.getParameter<bool>("apply_genWeight");
  bool apply_hlt_filter = cfg_testMEM.getParameter<bool>("apply_hlt_filter");
  bool apply_met_filters = cfg_testMEM.getParameter<bool>("apply_met_filters");
  edm::ParameterSet cfgMEtFilter = cfg_testMEM.getParameter<edm::ParameterSet>("cfgMEtFilter");
  MEtFilterSelector metFilterSelector(cfgMEtFilter, isMC);

  bool isDEBUG = cfg_testMEM.getParameter<bool>("isDEBUG");

  edm::ParameterSet cfg_dataToMCcorrectionInterface;
  cfg_dataToMCcorrectionInterface.addParameter<std::string>("era", era_string);
  cfg_dataToMCcorrectionInterface.addParameter<std::string>("hadTauSelection", "dR03mvaMedium"); // CV: dummy value (no taus used in HH->bbWW channel)
  cfg_dataToMCcorrectionInterface.addParameter<int>("hadTauSelection_antiElectron", -1);
  cfg_dataToMCcorrectionInterface.addParameter<int>("hadTauSelection_antiMuon", -1);
  cfg_dataToMCcorrectionInterface.addParameter<std::string>("central_or_shift", central_or_shift);
  Data_to_MC_CorrectionInterface_Base * dataToMCcorrectionInterface = nullptr;
  switch(era)
  {
    case kEra_2016: dataToMCcorrectionInterface = new Data_to_MC_CorrectionInterface_2016(cfg_dataToMCcorrectionInterface); break;
    case kEra_2017: dataToMCcorrectionInterface = new Data_to_MC_CorrectionInterface_2017(cfg_dataToMCcorrectionInterface); break;
    case kEra_2018: dataToMCcorrectionInterface = new Data_to_MC_CorrectionInterface_2018(cfg_dataToMCcorrectionInterface); break;
    default: throw cmsException("testMEM_hh_bb1l", __LINE__) << "Invalid era = " << era;
  }

  std::string branchName_electrons = cfg_testMEM.getParameter<std::string>("branchName_electrons");
  std::string branchName_muons = cfg_testMEM.getParameter<std::string>("branchName_muons");
  std::string branchName_jets_ak4 = cfg_testMEM.getParameter<std::string>("branchName_jets_ak4");
  std::string branchName_jets_ak8_Hbb = cfg_testMEM.getParameter<std::string>("branchName_jets_ak8_Hbb");
  std::string branchName_subjets_ak8_Hbb = cfg_testMEM.getParameter<std::string>("branchName_subjets_ak8_Hbb");
  std::string branchName_jets_ak8_Wjj = cfg_testMEM.getParameter<std::string>("branchName_jets_ak8_Wjj");
  std::string branchName_subjets_ak8_Wjj = cfg_testMEM.getParameter<std::string>("branchName_subjets_ak8_Wjj");
  std::string branchName_met = cfg_testMEM.getParameter<std::string>("branchName_met");

  std::string branchName_genLeptons = cfg_testMEM.getParameter<std::string>("branchName_genLeptons");
  std::string branchName_genNeutrinos = cfg_testMEM.getParameter<std::string>("branchName_genNeutrinos");
  std::string branchName_genJets = cfg_testMEM.getParameter<std::string>("branchName_genJets");

  std::string branchName_genBJets = cfg_testMEM.getParameter<std::string>("branchName_genBJets");
  std::string branchName_genWBosons = cfg_testMEM.getParameter<std::string>("branchName_genWBosons");
  std::string branchName_genWJets = cfg_testMEM.getParameter<std::string>("branchName_genWJets");

  // branches specific to HH signal
  std::string branchName_genParticlesFromHiggs = cfg_testMEM.getParameter<std::string>("branchName_genParticlesFromHiggs");

  // branches specific to ttbar background
  std::string branchName_genLeptonsFromTop = cfg_testMEM.getParameter<std::string>("branchName_genLeptonsFromTop");
  std::string branchName_genNeutrinosFromTop = cfg_testMEM.getParameter<std::string>("branchName_genNeutrinosFromTop");
  std::string branchName_genBQuarksFromTop = cfg_testMEM.getParameter<std::string>("branchName_genBQuarksFromTop");
  std::string branchName_genLightQuarksFromTop = cfg_testMEM.getParameter<std::string>("branchName_genLightQuarksFromTop");

  int genMatchingOption = cfg_testMEM.getParameter<int>("genMatchingOption");

  std::string selEventsFileName_input = cfg_testMEM.getParameter<std::string>("selEventsFileName_input");
  std::cout << "selEventsFileName_input = " << selEventsFileName_input << std::endl;
  RunLumiEventSelector* run_lumi_eventSelector = 0;
  if ( selEventsFileName_input != "" ) {
    edm::ParameterSet cfg_runLumiEventSelector;
    cfg_runLumiEventSelector.addParameter<std::string>("inputFileName", selEventsFileName_input);
    cfg_runLumiEventSelector.addParameter<std::string>("separator", ":");
    run_lumi_eventSelector = new RunLumiEventSelector(cfg_runLumiEventSelector);
  }

  std::string selEventsFileName_output = cfg_testMEM.getParameter<std::string>("selEventsFileName_output");
  std::cout << "selEventsFileName_output = " << selEventsFileName_output << std::endl;

  fwlite::InputSource inputFiles(cfg);
  int maxEvents = inputFiles.maxEvents();
  std::cout << " maxEvents = " << maxEvents << std::endl;
  int maxSelEvents = cfg_testMEM.getParameter<int>("maxSelEvents");
  std::cout << " maxSelEvents = " << maxSelEvents << std::endl;
  unsigned reportEvery = inputFiles.reportAfter();

  fwlite::OutputFiles outputFile(cfg);
  fwlite::TFileService fs = fwlite::TFileService(outputFile.file().data());

  TTreeWrapper* inputTree = new TTreeWrapper(treeName.data(), inputFiles.files(), maxEvents);
  std::cout << "Loaded " << inputTree->getFileCount() << " file(s)." << std::endl;

//--- declare event-level variables
  EventInfoHH eventInfo(isMC, isSignal);
  const std::vector<edm::ParameterSet> tHweights = cfg_testMEM.getParameterSetVector("tHweights");
  if((isMC_tH || isMC_ttH) && ! tHweights.empty())
  {
    eventInfo.loadWeight_tH(tHweights);
  }
  EventInfoHHReader eventInfoReader(&eventInfo);
  inputTree->registerReader(&eventInfoReader);

  hltPathReader hltPathReader_instance({ triggers_1e, triggers_1mu });
  inputTree->registerReader(&hltPathReader_instance);

//--- declare particle collections
  const bool readGenObjects = false;
  RecoMuonReader* muonReader = new RecoMuonReader(era, branchName_muons, isMC, readGenObjects);
  inputTree->registerReader(muonReader);
  RecoMuonCollectionGenMatcher muonGenMatcher;
  RecoMuonCollectionSelectorLoose preselMuonSelector(era, -1, isDEBUG);
  RecoMuonCollectionSelectorFakeable fakeableMuonSelector(era, -1, isDEBUG);
  RecoMuonCollectionSelectorTight tightMuonSelector(era, -1, isDEBUG);

  RecoElectronReader* electronReader = new RecoElectronReader(era, branchName_electrons, isMC, readGenObjects);
  inputTree->registerReader(electronReader);
  RecoElectronCollectionGenMatcher electronGenMatcher;
  RecoElectronCollectionCleaner electronCleaner(0.3, isDEBUG);
  RecoElectronCollectionSelectorLoose preselElectronSelector(era, -1, isDEBUG);
  RecoElectronCollectionSelectorFakeable fakeableElectronSelector(era, -1, isDEBUG);
  RecoElectronCollectionSelectorTight tightElectronSelector(era, -1, isDEBUG);

  RecoJetReader* jetReaderAK4 = new RecoJetReader(era, isMC, branchName_jets_ak4, readGenObjects);
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

  RecoJetReaderAK8* jetReaderAK8_Hbb = new RecoJetReaderAK8(era, branchName_jets_ak8_Hbb, branchName_subjets_ak8_Hbb);
  RecoJetReaderAK8* jetReaderAK8_Wjj = nullptr;
  if ( branchName_jets_ak8_Wjj != branchName_jets_ak8_Hbb ) {
    jetReaderAK8_Wjj = new RecoJetReaderAK8(era, branchName_jets_ak8_Wjj, branchName_subjets_ak8_Wjj);
  } else {
    jetReaderAK8_Wjj = jetReaderAK8_Hbb;
  }
  // TO-DO: implement jet energy scale uncertainties, b-tag weights,
  //        and jet  pT and (softdrop) mass corrections described in Section 3.4.3 of AN-2018/058 (v4)
  inputTree->registerReader(jetReaderAK8_Hbb);
  inputTree->registerReader(jetReaderAK8_Wjj);
  RecoJetBaseCollectionGenMatcher subjetGenMatcherAK8;
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR08(0.8, isDEBUG);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR12(1.2, isDEBUG);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR16(1.6, isDEBUG);
  RecoJetCollectionSelectorAK8_hh_bbWW_Hbb jetSelectorAK8_Hbb(era, -1, isDEBUG);
  RecoJetCollectionSelectorAK8_hh_Wjj jetSelectorAK8_Wjj(era, -1, isDEBUG);

  GenParticleReader* genBJetReader = new GenParticleReader(branchName_genBJets);
  inputTree->registerReader(genBJetReader);
  GenParticleReader* genWBosonReader = new GenParticleReader(branchName_genWBosons);
  inputTree->registerReader(genWBosonReader);
  GenParticleReader* genWJetReader = new GenParticleReader(branchName_genWJets);
  inputTree->registerReader(genWJetReader);

//--- declare missing transverse energy
  RecoMEtReader* metReader = new RecoMEtReader(era, isMC, branchName_met);
  inputTree->registerReader(metReader);

  MEtFilter metFilters;
  MEtFilterReader* metFilterReader = new MEtFilterReader(&metFilters, era);
  inputTree->registerReader(metFilterReader);

//--- declare generator level information
  GenLeptonReader* genLeptonReader = nullptr;
  if ( branchName_genLeptons != "" ) {
    genLeptonReader = new GenLeptonReader(branchName_genLeptons);
    inputTree->registerReader(genLeptonReader);
  }
  GenParticleReader* genNeutrinoReader = nullptr;
  if ( branchName_genNeutrinos != "" ) {
    genNeutrinoReader = new GenParticleReader(branchName_genNeutrinos);
    inputTree->registerReader(genNeutrinoReader);
  }
  GenJetReader* genJetReader = nullptr;
  if ( branchName_genJets != "" ) {
    genJetReader = new GenJetReader(branchName_genJets);
    inputTree->registerReader(genJetReader);
  }
  LHEInfoReader* lheInfoReader = new LHEInfoReader(hasLHE);
  inputTree->registerReader(lheInfoReader);

  // information specific to HH signal
  GenParticleReader* genParticleFromHiggsReader = nullptr;
  if ( branchName_genParticlesFromHiggs != "" ) {
    genParticleFromHiggsReader = new GenParticleReader(branchName_genParticlesFromHiggs);
    inputTree->registerReader(genParticleFromHiggsReader);
  }

  // information specific to ttbar background
  GenLeptonReader* genLeptonFromTopReader = nullptr;
  if ( branchName_genLeptonsFromTop != "" ) {
    genLeptonFromTopReader = new GenLeptonReader(branchName_genLeptonsFromTop);
    inputTree->registerReader(genLeptonFromTopReader);
  }
  GenParticleReader* genNeutrinoFromTopReader = nullptr;
  if ( branchName_genNeutrinosFromTop != "" ) {
    genNeutrinoFromTopReader = new GenParticleReader(branchName_genNeutrinosFromTop);
    inputTree->registerReader(genNeutrinoFromTopReader);
  }
  GenParticleReader* genBQuarksFromTopReader = nullptr;
  if ( branchName_genBQuarksFromTop != "" ) {
    genBQuarksFromTopReader = new GenParticleReader(branchName_genBQuarksFromTop);
    inputTree->registerReader(genBQuarksFromTopReader);
  }
  GenParticleReader* genLightQuarksFromTopReader = nullptr;
  if ( branchName_genLightQuarksFromTop != "" ) {
    genLightQuarksFromTopReader = new GenParticleReader(branchName_genLightQuarksFromTop);
    inputTree->registerReader(genLightQuarksFromTopReader);
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
      Form("%s/unbiased/genEvt", histogramDir.data()), era_string, central_or_shift));
    genEvtHistManager_beforeCuts->bookHistograms(fs);
    lheInfoHistManager_beforeCuts = new LHEInfoHistManager(makeHistManager_cfg(process_string,
      Form("%s/unbiased/lheInfo", histogramDir.data()), era_string, central_or_shift));
    lheInfoHistManager_beforeCuts->bookHistograms(fs);
  }

  std::string xgbFileName_bb1l = "hhAnalysis/bbww/data/bb1l_HH_XGB_noTopness_evtLevelSUM_HH_bb1l_res_12Var.pkl";
  std::vector<std::string> xgbInputVariables_bb1l =
    {"met", "HT", "m_Hbb", "dR_Hbb", "dR_Hww", "dR_b1lep", "dR_b2lep", "pT_HH", "mT_W", "mT_top_2particle", "mvaOutput_Hj_tagger", "gen_mHH"
    };

  XGBInterface mva_xgb_bb1l(xgbFileName_bb1l, xgbInputVariables_bb1l);
  std::map<std::string, double> mvaInputs_XGB;

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
    GenEvtHistManager* genEvtHistManager_afterCuts_;
    LHEInfoHistManager* lheInfoHistManager_afterCuts_;
    WeightHistManager* weights_;
  };
  selHistManagerType* selHistManager = new selHistManagerType();
  selHistManager->electrons_ = new ElectronHistManager(makeHistManager_cfg(process_string,
    Form("%s/sel/electrons", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
  selHistManager->electrons_->bookHistograms(fs);
  selHistManager->muons_ = new MuonHistManager(makeHistManager_cfg(process_string,
    Form("%s/sel/muons", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
  selHistManager->muons_->bookHistograms(fs);
  selHistManager->jetsAK4_ = new JetHistManager(makeHistManager_cfg(process_string,
    Form("%s/sel/jetsAK4", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
  selHistManager->jetsAK4_->bookHistograms(fs);
  selHistManager->leadJetAK4_ = new JetHistManager(makeHistManager_cfg(process_string,
    Form("%s/sel/leadJetAK4", histogramDir.data()), era_string, central_or_shift, "minimalHistograms", 0));
  selHistManager->leadJetAK4_->bookHistograms(fs);
  selHistManager->subleadJetAK4_ = new JetHistManager(makeHistManager_cfg(process_string,
    Form("%s/sel/subleadJetAK4", histogramDir.data()), era_string, central_or_shift, "minimalHistograms", 1));
  selHistManager->subleadJetAK4_->bookHistograms(fs);
  selHistManager->jetsAK8_Hbb_ = new JetHistManagerAK8(makeHistManager_cfg(process_string,
    Form("%s/sel/jetsAK8_Hbb", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
  selHistManager->jetsAK8_Hbb_->bookHistograms(fs);
  selHistManager->jetsAK8_Wjj_ = new JetHistManagerAK8(makeHistManager_cfg(process_string,
    Form("%s/sel/jetsAK8_Wjj", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
  selHistManager->jetsAK8_Wjj_->bookHistograms(fs);
  selHistManager->BJetsAK4_loose_ = new JetHistManager(makeHistManager_cfg(process_string,
    Form("%s/sel/BJetsAK4_loose", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
  selHistManager->BJetsAK4_loose_->bookHistograms(fs);
  selHistManager->leadBJetAK4_loose_ = new JetHistManager(makeHistManager_cfg(process_string,
    Form("%s/sel/leadBJetAK4_loose", histogramDir.data()), era_string, central_or_shift, "minimalHistograms", 0));
  selHistManager->leadBJetAK4_loose_->bookHistograms(fs);
  selHistManager->subleadBJetAK4_loose_ = new JetHistManager(makeHistManager_cfg(process_string,
    Form("%s/sel/subleadBJetAK4_loose", histogramDir.data()), era_string, central_or_shift, "minimalHistograms", 1));
  selHistManager->subleadBJetAK4_loose_->bookHistograms(fs);
  selHistManager->BJetsAK4_medium_ = new JetHistManager(makeHistManager_cfg(process_string,
    Form("%s/sel/BJetsAK4_medium", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
  selHistManager->BJetsAK4_medium_->bookHistograms(fs);
  selHistManager->met_ = new MEtHistManager(makeHistManager_cfg(process_string,
    Form("%s/sel/met", histogramDir.data()), era_string, central_or_shift));
  selHistManager->met_->bookHistograms(fs);
  selHistManager->metFilters_ = new MEtFilterHistManager(makeHistManager_cfg(process_string,
    Form("%s/sel/metFilters", histogramDir.data()), era_string, central_or_shift));
  selHistManager->metFilters_->bookHistograms(fs);
  selHistManager->evt_ = new EvtHistManager_hh_bb1l(makeHistManager_cfg(process_string,
    Form("%s/sel/evt", histogramDir.data()), era_string, central_or_shift, "memEnabled"));
  selHistManager->evt_->bookHistograms(fs);
  selHistManager->genEvtHistManager_afterCuts_ = new GenEvtHistManager(makeHistManager_cfg(process_string,
    Form("%s/sel/genEvt", histogramDir.data()), era_string, central_or_shift));
  selHistManager->genEvtHistManager_afterCuts_->bookHistograms(fs);
  selHistManager->lheInfoHistManager_afterCuts_ = new LHEInfoHistManager(makeHistManager_cfg(process_string,
    Form("%s/sel/lheInfo", histogramDir.data()), era_string, central_or_shift));
  selHistManager->lheInfoHistManager_afterCuts_->bookHistograms(fs);
  selHistManager->weights_ = new WeightHistManager(makeHistManager_cfg(process_string,
    Form("%s/sel/weights", histogramDir.data()), era_string, central_or_shift));
  selHistManager->weights_->bookHistograms(fs, { "genWeight", "pileupWeight", "triggerWeight", "data_to_MC_correction" });

  TH1* histogram_badMEM_genLepton_matchType          = bookHistogram1d(fs, "badMEM_genLepton_matchType",           6, -0.5, +5.5);
  TH1* histogram_badMEM_genJet_Hbb_lead_matchType    = bookHistogram1d(fs, "badMEM_genJet_Hbb_lead_matchType",     6, -0.5, +5.5);
  TH1* histogram_badMEM_genJet_Hbb_sublead_matchType = bookHistogram1d(fs, "badMEM_genJet_Hbb_sublead_matchType",  6, -0.5, +5.5);
  TH1* histogram_badMEM_genJet_Wjj_lead_matchType    = bookHistogram1d(fs, "badMEM_genJet_Wjj_lead_matchType",     6, -0.5, +5.5);
  TH1* histogram_badMEM_genJet_Wjj_sublead_matchType = bookHistogram1d(fs, "badMEM_genJet_Wjj_sublead_matchType",  6, -0.5, +5.5);
  TH1* histogram_badMEM_numBJets_loose               = bookHistogram1d(fs, "badMEM_numBJets_loose",               10, -0.5, +9.5);
  TH1* histogram_badMEM_numBJets_medium              = bookHistogram1d(fs, "badMEM_numBJets_medium",              10, -0.5, +9.5);

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
    "lepton pT > 25 GeV",
    "<= 1 tight leptons",
    "fakeable lepton trigger match",
    "HLT filter matching",
    ">= 2 jets from H->bb",
    ">= 1 medium b-jet",
    ">= 2 jets from W->jj",
    "tau veto",
    "m(ll) > 12 GeV",
    "Z-boson mass veto",
    "boosted W->jj: mD < 125 GeV",
    "boosted W->jj: pT_HWW/mHH > 0.3",
    "MEt filters",
    "signal region veto"
  };
  CutFlowTableHistManager * cutFlowHistManager = new CutFlowTableHistManager(cutFlowTableCfg, cuts);
  cutFlowHistManager->bookHistograms(fs);
  while ( inputTree->hasNextEvent() && (! run_lumi_eventSelector || (run_lumi_eventSelector && ! run_lumi_eventSelector -> areWeDone())) && selectedEntries < maxSelEvents ) {
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
    if ( genLeptonReader ) {
      genLeptons = genLeptonReader->read();
      for ( std::vector<GenLepton>::const_iterator genLepton = genLeptons.begin();
	    genLepton != genLeptons.end(); ++genLepton ) {
	int abs_pdgId = std::abs(genLepton->pdgId());
	if      ( abs_pdgId == 11 ) genElectrons.push_back(*genLepton);
	else if ( abs_pdgId == 13 ) genMuons.push_back(*genLepton);
      }
    }
    std::vector<GenParticle> genNeutrinos;
    if ( genNeutrinoReader ) {
      genNeutrinos = genNeutrinoReader->read();
    }
    std::vector<GenJet> genJets;
    if ( genJetReader ) {
      genJets = genJetReader->read();
    }
    if ( isDEBUG ) {
      printCollection("genLeptons", genLeptons);
      printCollection("genNeutrinos", genNeutrinos);
      printCollection("genJets", genJets);
    }

    std::vector<GenParticle> genBJets = genBJetReader->read();
    std::vector<GenParticle> genWBosons = genWBosonReader->read();
    std::vector<GenParticle> genWJets = genWJetReader->read();
    if ( isDEBUG ) {
      dumpGenParticles("genBJet", genBJets);
      dumpGenParticles("genWBoson", genWBosons);
      dumpGenParticles("genWJet", genWJets);
    }

    double evtWeight_inclusive = 1.;
    if ( isMC ) {
      if(apply_genWeight) evtWeight_inclusive *= boost::math::sign(eventInfo.genWeight);
      lheInfoReader->read();
      evtWeight_inclusive *= lheInfoReader->getWeight_scale(kLHE_scale_central);
      evtWeight_inclusive *= eventInfo.pileupWeight;
      evtWeight_inclusive *= eventInfo.genWeight_tH();
      genEvtHistManager_beforeCuts->fillHistograms(genElectrons, genMuons, {}, {}, genJets, evtWeight_inclusive);
    }

    std::vector<GenParticle> genParticlesFromHiggs;
    if ( isSignal ) {
      genParticlesFromHiggs = genParticleFromHiggsReader->read();
      if ( isDEBUG ) {
	printCollection("genParticlesFromHiggs", genParticlesFromHiggs);
      }
      if ( !(genParticlesFromHiggs.size() == 4) ) {
	if ( run_lumi_eventSelector ) {
	  std::cout << "event " << eventInfo.str() << " FAILS generator-level selection." << std::endl;
	  std::cout << "#genParticlesFromHiggs = " << genParticlesFromHiggs.size() << std::endl;
	}
	continue;
      }
    }
    std::vector<GenLepton> genLeptonsFromTop;
    std::vector<GenParticle> genNeutrinosFromTop;
    std::vector<GenParticle> genBQuarksFromTop;
    std::vector<GenParticle> genLightQuarksFromTop;
    if ( !isSignal ) {
      genLeptonsFromTop = genLeptonFromTopReader->read();
      genNeutrinosFromTop = genNeutrinoFromTopReader->read();
      genBQuarksFromTop = genBQuarksFromTopReader->read();
      genLightQuarksFromTop = genLightQuarksFromTopReader->read();
      if ( isDEBUG ) {
	printCollection("genLeptonsFromTop", genLeptonsFromTop);
	printCollection("genNeutrinosFromTop", genNeutrinosFromTop);
	printCollection("genBQuarksFromTop", genBQuarksFromTop);
	printCollection("genLightQuarksFromTop", genLightQuarksFromTop);
      }
      if ( !(genLeptonsFromTop.size() == 1 && genNeutrinosFromTop.size() == 1 && genBQuarksFromTop.size() == 2 && genLightQuarksFromTop.size() == 2) ) {
	if ( run_lumi_eventSelector ) {
	  std::cout << "event " << eventInfo.str() << " FAILS generator-level selection." << std::endl;
	  std::cout << "#genLeptonsFromTop = " << genLeptonsFromTop.size() << std::endl;
	  std::cout << "#genNeutrinosFromTop = " << genNeutrinosFromTop.size() << std::endl;
	  std::cout << "#genBQuarksFromTop = " << genBQuarksFromTop.size() << std::endl;
	  std::cout << "#genLightQuarksFromTop = " << genLightQuarksFromTop.size() << std::endl;
	}
	continue;
      }
    }
    cutFlowTable.update("generator-level selection (1)", evtWeight_inclusive);

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

//--- match reconstructed to generator level particles
    std::vector<GenLepton> genLeptonsForMatching;
    std::vector<GenJet> genJetsFromWBosonForMatching;
    std::vector<GenJet> genBJetsForMatching;
    double genMEtPx = 0.;
    double genMEtPy = 0.;
    if ( isSignal ) {
      const GenParticle* genBQuark      = nullptr;
      const GenParticle* genAntiBQuark  = nullptr;
      const GenParticle* genWBosonPlus  = nullptr;
      const GenParticle* genWBosonMinus = nullptr;
      for ( std::vector<GenParticle>::const_iterator genParticle = genParticlesFromHiggs.begin();
	    genParticle != genParticlesFromHiggs.end(); ++genParticle ) {
	if      ( genParticle->pdgId() ==  +5 ) genBQuark      = &(*genParticle);
	else if ( genParticle->pdgId() ==  -5 ) genAntiBQuark  = &(*genParticle);
	else if ( genParticle->pdgId() == +24 ) genWBosonPlus  = &(*genParticle);
	else if ( genParticle->pdgId() == -24 ) genWBosonMinus = &(*genParticle);
      }
      if ( genBQuark && genAntiBQuark ) {
	genBJetsForMatching.push_back(GenJet(
          genBQuark->pt(), genBQuark->eta(), genBQuark->phi(), mem::bottomQuarkMass, genBQuark->pdgId()));
	genBJetsForMatching.push_back(GenJet(
          genAntiBQuark->pt(), genAntiBQuark->eta(), genAntiBQuark->phi(), mem::bottomQuarkMass, genAntiBQuark->pdgId()));
      }
      if ( genWBosonPlus && genWBosonMinus ) {
	std::pair<const GenLepton*, const GenParticle*> genLepton_and_NeutrinoFromWBosonPlus =
          findGenLepton_and_NeutrinoFromWBoson(genWBosonPlus, genLeptons, genNeutrinos);
	std::pair<const GenLepton*, const GenParticle*> genLepton_and_NeutrinoFromWBosonMinus =
          findGenLepton_and_NeutrinoFromWBoson(genWBosonMinus, genLeptons, genNeutrinos);
	const GenLepton* genLepton = nullptr;
	const GenParticle* genNeutrino = nullptr;
	//const GenJet* genJet1_Wjj = nullptr;
	//const GenJet* genJet2_Wjj = nullptr;
	const GenParticle* genJet1_Wjj = nullptr;
	const GenParticle* genJet2_Wjj = nullptr;
	if (  (genLepton_and_NeutrinoFromWBosonPlus.first  && genLepton_and_NeutrinoFromWBosonPlus.second ) &&
	     !(genLepton_and_NeutrinoFromWBosonMinus.first && genLepton_and_NeutrinoFromWBosonMinus.second) ) {
	  genLepton = genLepton_and_NeutrinoFromWBosonPlus.first;
	  genNeutrino = genLepton_and_NeutrinoFromWBosonPlus.second;
	  //std::pair<const GenJet*, const GenJet*> genJetsFromWBoson =
          //  findGenJetsFromWBoson(genWBosonMinus, genJets);
	  std::pair<const GenParticle*, const GenParticle*> genJetsFromWBoson =
            findGenJetsFromWBoson(genWBosonMinus, genWJets);
	  genJet1_Wjj = genJetsFromWBoson.first;
	  genJet2_Wjj = genJetsFromWBoson.second;
	} else if (  (genLepton_and_NeutrinoFromWBosonMinus.first && genLepton_and_NeutrinoFromWBosonMinus.second) &&
		    !(genLepton_and_NeutrinoFromWBosonPlus.first  && genLepton_and_NeutrinoFromWBosonPlus.second ) ) {
	  genLepton = genLepton_and_NeutrinoFromWBosonMinus.first;
	  genNeutrino = genLepton_and_NeutrinoFromWBosonMinus.second;
	  //std::pair<const GenJet*, const GenJet*> genJetsFromWBoson =
          //  findGenJetsFromWBoson(genWBosonPlus, genJets);
	  std::pair<const GenParticle*, const GenParticle*> genJetsFromWBoson =
            findGenJetsFromWBoson(genWBosonMinus, genWJets);
	  genJet1_Wjj = genJetsFromWBoson.first;
	  genJet2_Wjj = genJetsFromWBoson.second;
	}
	if ( !(genLepton && genNeutrino && genJet1_Wjj && genJet2_Wjj) ) continue;
	genLeptonsForMatching.push_back(*genLepton);
	//genJetsFromWBosonForMatching.push_back(*genJet1_Wjj);
	//genJetsFromWBosonForMatching.push_back(*genJet2_Wjj);
	genJetsFromWBosonForMatching.push_back(GenJet(
          genJet1_Wjj->pt(), genJet1_Wjj->eta(), genJet1_Wjj->phi(), genJet1_Wjj->mass(), genJet1_Wjj->pdgId()));
	genJetsFromWBosonForMatching.push_back(GenJet(
          genJet2_Wjj->pt(), genJet2_Wjj->eta(), genJet2_Wjj->phi(), genJet2_Wjj->mass(), genJet2_Wjj->pdgId()));
	genMEtPx = genNeutrino->p4().px();
	genMEtPy = genNeutrino->p4().py();
      }
    } else {
      genLeptonsForMatching = genLeptonsFromTop;
      for ( std::vector<GenParticle>::const_iterator genLightQuark = genLightQuarksFromTop.begin();
	    genLightQuark != genLightQuarksFromTop.end(); ++genLightQuark ) {
	genJetsFromWBosonForMatching.push_back(GenJet(
	  genLightQuark->pt(), genLightQuark->eta(), genLightQuark->phi(), genLightQuark->mass(), genLightQuark->pdgId()));
      }
      assert(genNeutrinosFromTop.size() == 1);
      genMEtPx = genNeutrinosFromTop[0].p4().px();
      genMEtPy = genNeutrinosFromTop[0].p4().py();
      for ( std::vector<GenParticle>::const_iterator genBQuark = genBQuarksFromTop.begin();
	    genBQuark != genBQuarksFromTop.end(); ++genBQuark ) {
	genBJetsForMatching.push_back(GenJet(
          genBQuark->pt(), genBQuark->eta(), genBQuark->phi(), mem::bottomQuarkMass, genBQuark->pdgId()));
      }
    }
    //std::sort(genLeptonsForMatching.begin(), genLeptonsForMatching.end(), isHigherPt_GenLepton);
    std::sort(genJetsFromWBosonForMatching.begin(), genJetsFromWBosonForMatching.end(), isHigherPt_GenJet);
    std::sort(genBJetsForMatching.begin(), genBJetsForMatching.end(), isHigherPt_GenJet);
    if ( !(genLeptonsForMatching.size() == 1 && genJetsFromWBosonForMatching.size() == 2 && genBJetsForMatching.size() == 2) ) {
      if ( run_lumi_eventSelector ) {
	std::cout << "event " << eventInfo.str() << " FAILS generator-level selection." << std::endl;
	std::cout << "#genLeptonsForMatching = " << genLeptonsForMatching.size() << std::endl;
	std::cout << "#genJetsFromWBosonForMatching = " << genJetsFromWBosonForMatching.size() << std::endl;
	std::cout << "#genBJetsForMatching = " << genBJetsForMatching.size() << std::endl;
      }
      continue;
    }
    cutFlowTable.update("generator-level selection (2)", evtWeight_inclusive);
    muonGenMatcher.addGenLeptonMatch(preselMuons, genLeptonsForMatching, 0.2);
    electronGenMatcher.addGenLeptonMatch(preselElectrons, genLeptonsForMatching, 0.2);

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

    lheInfoReader->read();

//--- compute event-level weight for data/MC correction of b-tagging efficiency and mistag rate
//   (using the method "Event reweighting using scale factors calculated with a tag and probe method",
//    described on the BTV POG twiki https://twiki.cern.ch/twiki/bin/view/CMS/BTagShapeCalibration )
    double evtWeight = evtWeight_inclusive;
    double btagWeight = get_BtagWeight(selJetsAK4);
    evtWeight *= btagWeight;
    if ( isDEBUG ) {
      if ( apply_genWeight ) std::cout << "genWeight = " << boost::math::sign(eventInfo.genWeight) << std::endl;
      std::cout << "pileupWeight = " << eventInfo.pileupWeight << std::endl;
      std::cout << "btagWeight = " << btagWeight << std::endl;
    }

    const double minPt_lead = 25.;
    if ( !(selLepton->cone_pt() > minPt_lead) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS lepton pT selection." << std::endl;
        std::cout << " (selLepton pT = " << selLepton->pt() << ", minPt_lead = " << minPt_lead << ")" << std::endl;
      }
      continue;
    }
    cutFlowTable.update("lepton pT > 25 GeV", evtWeight);
    cutFlowHistManager->fillHistograms("lepton pT > 25 GeV", evtWeight);

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
    if ( isDEBUG ) {
      std::cout << "evtWeight = " << evtWeight << std::endl;
    }

    std::vector<RecoJetAK8> jets_ak8_Hbb = jetReaderAK8_Hbb->read();
    std::vector<const RecoJetAK8*> jet_ptrs_ak8_Hbb = convert_to_ptrs(jets_ak8_Hbb);
    std::vector<RecoJetAK8> jets_ak8_Wjj = jetReaderAK8_Wjj->read();
    std::vector<const RecoJetAK8*> jet_ptrs_ak8_Wjj = convert_to_ptrs(jets_ak8_Wjj);

    if ( isDEBUG || run_lumi_eventSelector ) {
      printCollection("uncleaned AK8 jets (Hbb)", jet_ptrs_ak8_Hbb);
      printHbb(jet_ptrs_ak8_Hbb, jetSelectorAK8_Hbb, genBJets);
      printCollection("uncleaned AK8 jets (Wjj)", jet_ptrs_ak8_Wjj);
      printWjj(jet_ptrs_ak8_Wjj, jetSelectorAK8_Wjj, genWBosons, genWJets);
    }

    // select jets from H->bb decay
    std::vector<const RecoJetAK8*> cleanedJetsAK8_wrtLeptons = jetCleanerAK8_dR08(jet_ptrs_ak8_Hbb, fakeableLeptons);
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
      if ( isDEBUG ) {
	std::cout << "found boosted H->bb decay:" << std::endl;
	std::cout << "AK8 jet: pT = " << selJetAK8_Hbb->pt() << ", eta = " << selJetAK8_Hbb->eta() << ", phi = " << selJetAK8_Hbb->phi() << ","
		  << " dR(selLepton) = " << deltaR(selJetAK8_Hbb->p4(), selLepton->p4()) << std::endl;
	std::cout << " subjet #1: pT = " << selJet1_Hbb->pt() << ", eta = " << selJet1_Hbb->eta() << ", phi = " << selJet1_Hbb->phi() << ","
		  << " dR(selLepton) = " << deltaR(selJet1_Hbb->p4(), selLepton->p4()) << std::endl;
	std::cout << " subjet #2: pT = " << selJet2_Hbb->pt() << ", eta = " << selJet2_Hbb->eta() << ", phi = " << selJet2_Hbb->phi() << ","
		  << " dR(selLepton) = " << deltaR(selJet2_Hbb->p4(), selLepton->p4()) << std::endl;
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
    subjetGenMatcherAK8.addGenJetMatch(selJets_Hbb, genBJetsForMatching, 0.2);
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
      cleanedJetsAK8_wrtHbb = jetCleanerAK8_dR16(jet_ptrs_ak8_Wjj, overlaps); // CV: do *not* clean W->jj "fat" jet collection with respect to leptons!
      cleanedJetsAK4_wrtHbb = jetCleanerAK4_dR12(cleanedJetsAK4_wrtLeptons, overlaps);
    } else {
      cleanedJetsAK8_wrtHbb = jetCleanerAK8_dR12(jet_ptrs_ak8_Wjj, selJets_Hbb);
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
      if ( isDEBUG ) {
	std::cout << "found boosted W->jj decay:" << std::endl;
	std::cout << "AK8LS jet: pT = " << selJetAK8_Wjj->pt() << ", eta = " << selJetAK8_Wjj->eta() << ", phi = " << selJetAK8_Wjj->phi() << ","
		  << " dR(selLepton) = " << deltaR(selJetAK8_Wjj->p4(), selLepton->p4()) << std::endl;
	std::cout << " subjet #1: pT = " << selJet1_Wjj->pt() << ", eta = " << selJet1_Wjj->eta() << ", phi = " << selJet1_Wjj->phi() << ","
		  << " dR(selLepton) = " << deltaR(selJet1_Wjj->p4(), selLepton->p4()) << std::endl;
	std::cout << " subjet #2: pT = " << selJet2_Wjj->pt() << ", eta = " << selJet2_Wjj->eta() << ", phi = " << selJet2_Wjj->phi() << ","
		  << " dR(selLepton) = " << deltaR(selJet2_Wjj->p4(), selLepton->p4()) << std::endl;
      }
    } else {
      double minRank = 1.e+3;
      int idxSelJet1 = 0;
      for ( std::vector<const RecoJet*>::const_iterator selJet1 = selJetsAK4_Wjj.begin();
	    selJet1 != selJetsAK4_Wjj.end(); ++selJet1 ) {
	int idxSelJet2 = idxSelJet2 + 1;
	for ( std::vector<const RecoJet*>::const_iterator selJet2 = selJet1 + 1;
	      selJet2 != selJetsAK4_Wjj.end(); ++selJet2 ) {
	  Particle::LorentzVector jjP4 = (*selJet1)->p4() + (*selJet2)->p4();
	  double m_jj = jjP4.mass();
	  double pT_jj = jjP4.pt();
	  double rank = TMath::Abs(m_jj - mem::wBosonMass)/TMath::Sqrt(TMath::Max(10., pT_jj));
	  //std::cout << "selJet1: pT = " << (*selJet1)->pt() << ", eta = " << (*selJet1)->eta() << ", phi = " << (*selJet1)->phi() << std::endl;
	  //std::cout << "selJet2: pT = " << (*selJet2)->pt() << ", eta = " << (*selJet2)->eta() << ", phi = " << (*selJet2)->phi() << std::endl;
	  //std::cout << "abs(m_jj - mW) = " << TMath::Abs(m_jj - mem::wBosonMass) << ", pT_jj = " << pT_jj << ": rank  = " << rank << std::endl;
	  if ( rank < minRank ) {
	    selJet1_Wjj = (*selJet1);
	    selJet2_Wjj = (*selJet2);
	    minRank = rank;
	  }
	  ++idxSelJet2;
	}
	++idxSelJet1;
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
    }
    //if ( !(selJet1_Wjj || selJet2_Wjj) ) {
    //  if ( run_lumi_eventSelector ) {
    //    std::cout << "event " << eventInfo.str() << " FAILS >= 1 jets from W->jj selection\n";
    //  }
    //  continue;
    //}
    //cutFlowTable.update(">= 1 jets from W->jj", evtWeight_inclusive);
    //cutFlowHistManager->fillHistograms(">= 1 jets from W->jj", evtWeight_inclusive);
    // CV: need two jets from W->jj in order to compute matrix element method likelihood ratio of HH signal and ttbar background hypotheses
    if ( !(selJet1_Wjj && selJet2_Wjj) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS >= 1 jets from W->jj selection\n";
      }
      continue;
    }
    cutFlowTable.update(">= 2 jets from W->jj", evtWeight_inclusive);
    cutFlowHistManager->fillHistograms(">= 2 jets from W->jj", evtWeight_inclusive);

    std::vector<const RecoJetBase*> selJets_Wjj = { selJet1_Wjj, selJet2_Wjj };
    std::sort(selJets_Wjj.begin(), selJets_Wjj.end(), isHigherPt);
    subjetGenMatcherAK8.addGenJetMatch(selJets_Wjj, genJetsFromWBosonForMatching, 0.2);
    const RecoJetBase* selJet_Wjj_lead = selJets_Wjj[0];
    const Particle::LorentzVector& selJetP4_Wjj_lead = selJet_Wjj_lead->p4();
    const RecoJetBase* selJet_Wjj_sublead = selJets_Wjj[1];
    Particle::LorentzVector selJetP4_Wjj_sublead = selJet_Wjj_sublead->p4();

    const bool failsLowMassVeto = isfailsLowMassVeto(preselLeptonsFull);
    if ( failsLowMassVeto ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS low mass lepton pair veto." << std::endl;
      }
      continue;
    }
    cutFlowTable.update("m(ll) > 12 GeV", evtWeight);
    cutFlowHistManager->fillHistograms("m(ll) > 12 GeV", evtWeight);

    const bool failsZbosonMassVeto = isfailsZbosonMassVeto(preselLeptonsFull);
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
    Particle::LorentzVector neutrinoP4_B2G_18_008 = comp_metP4_B2G_18_008(selLeptonP4 + selJetP4_Wjj_lead + selJetP4_Wjj_sublead, metP4.px(), metP4.py(), mem::higgsBosonMass);

    // compute HT and STMET variables used for signal extraction in EXO analyses
    std::vector<const RecoJetBase*> selJets_HT_and_STMET;
    selJets_HT_and_STMET.insert(selJets_HT_and_STMET.end(), selJets_Hbb.begin(), selJets_Hbb.end());
    selJets_HT_and_STMET.insert(selJets_HT_and_STMET.end(), selJets_Wjj.begin(), selJets_Wjj.end());
    double HT = compHT(fakeableLeptons, {}, selJets_HT_and_STMET);
    double STMET = compSTMEt(fakeableLeptons, {}, selJets_HT_and_STMET, met.p4());

    // apply cut on mD variable, defined by Eq.(3) in AN-2018/058 (v4)
    //bool fails_mD_cut = false;
    if ( selJetAK8_Wjj ) {
      Particle::LorentzVector WjjP4 = selJetAK8_Wjj->p4();
      Particle::LorentzVector WlnuP4 = selLepton->p4() + neutrinoP4_B2G_18_008;
      double mD = deltaR(WjjP4, WlnuP4)*0.5*(WjjP4 + WlnuP4).pt();
      if ( !(mD <= mem::higgsBosonMass) ) {
	if ( run_lumi_eventSelector ) {
	  std::cout << "event " << eventInfo.str() << " FAILS mD < 125 GeV selection\n";
	}
	continue;
	//fails_mD_cut = true;
      }
    }
    cutFlowTable.update("boosted W->jj: mD < 125 GeV selection", evtWeight);
    cutFlowHistManager->fillHistograms("boosted W->jj: mD < 125 GeV selection", evtWeight);

    // apply cut on event centrality variable, defined in Table 9 of AN-2018/058 (v4)
    //bool fails_centrality_cut = false;
    if ( selJetAK8_Wjj ) {
      //std::cout << "met: pT = " << metP4.pt() << ", phi = " << metP4.phi() << std::endl;
      //std::cout << "neutrino (B2G-18-008): pT = " << neutrinoP4_B2G_18_008.pt() << ", eta = " << neutrinoP4_B2G_18_008.eta() << ", phi = " << neutrinoP4_B2G_18_008.phi() << std::endl;
      double pT_HWW = (selJetAK8_Wjj->p4() + selLepton->p4() + neutrinoP4_B2G_18_008).pt();
      //std::cout << "pT_HWW = " << pT_HWW << std::endl;
      double mHH = (selJetP4_Hbb_lead + selJetP4_Hbb_sublead + selJetAK8_Wjj->p4() + selLepton->p4() + neutrinoP4_B2G_18_008).mass();
      //std::cout << "mHH = " << mHH << std::endl;
      if ( !((pT_HWW/mHH) >= 0.3) ) {
	if ( run_lumi_eventSelector ) {
	  std::cout << "event " << eventInfo.str() << " FAILS pT_HWW/mHH > 0.3 selection\n";
	}
	continue;
	//fails_centrality_cut = true;
      }
    }
    cutFlowTable.update("boosted W->jj: pT_HWW/mHH > 0.3", evtWeight);
    cutFlowHistManager->fillHistograms("boosted W->jj: pT_HWW/mHH > 0.3", evtWeight);

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

    // compute signal extraction observables
    Particle::LorentzVector HbbP4 = selJetP4_Hbb_lead + selJetP4_Hbb_sublead;
    double m_Hbb    = HbbP4.mass();
    double dR_Hbb   = deltaR(selJetP4_Hbb_lead, selJetP4_Hbb_sublead);
    double dPhi_Hbb = TMath::Abs(deltaPhi(selJetP4_Hbb_lead.phi(), selJetP4_Hbb_sublead.phi())); // CV: map dPhi into interval [0..pi]
    double pT_Hbb   = HbbP4.pt();
    Particle::LorentzVector WjjP4 = selJetP4_Wjj_lead + selJetP4_Wjj_sublead;
    double m_Wjj    = -1.;
    double dR_Wjj   = -1.;
    double dPhi_Wjj = -1.;
    double pT_Wjj   = -1.;
    if ( selJet_Wjj_lead && selJet_Wjj_sublead ) {
      m_Wjj    = WjjP4.mass();
      dR_Wjj   = deltaR(selJetP4_Wjj_lead, selJetP4_Wjj_sublead);
      dPhi_Wjj = TMath::Abs(deltaPhi(selJetP4_Wjj_lead.phi(), selJetP4_Wjj_sublead.phi()));
      pT_Wjj   = WjjP4.pt();
    }
    //double tau21_Wjj = ( selJetAK8_Wjj ) ? selJetAK8_Wjj->tau2()/selJetAK8_Wjj->tau1() : -1.;
    Particle::LorentzVector WlnuP4 = selLeptonP4 + neutrinoP4_B2G_18_008;
    double dR_Hww = deltaR(WjjP4, WlnuP4);
    double dPhi_Hww = TMath::Abs(deltaPhi(WjjP4.phi(), WlnuP4.phi()));
    Particle::LorentzVector HwwP4 = WjjP4 + WlnuP4;
    double pT_Hww = HwwP4.pt();
    double Smin_Hww = comp_Smin(WjjP4 + selLeptonP4, metP4.px(), metP4.py());
    double dR_b1lep = deltaR(selJetP4_Hbb_lead, selLeptonP4);
    double dR_b2lep = deltaR(selJetP4_Hbb_sublead, selLeptonP4);
    Particle::LorentzVector HHvisP4 = HbbP4 + WjjP4 + selLeptonP4;
    double m_HHvis = HHvisP4.mass();
    //double pT_HHvis = HHvisP4.pt();
    //double dPhi_HHvis = TMath::Abs(deltaPhi(HbbP4.phi(), (WjjP4 + selLeptonP4).phi()));
    Particle::LorentzVector HHP4_B2G_18_008 = HbbP4 + WjjP4 + selLeptonP4 + neutrinoP4_B2G_18_008;
    Particle::LorentzVector HHP4 = HbbP4 + WjjP4 + selLeptonP4 + metP4;
    double m_HH = HHP4.mass();
    double m_HH_B2G_18_008 = HHP4_B2G_18_008.mass();
    double pT_HH = HHP4.pt();
    double Smin_HH = comp_Smin(HHvisP4, metP4.px(), metP4.py());
    double dR_HH = deltaR(HbbP4, WjjP4 + selLeptonP4 + neutrinoP4_B2G_18_008);
    double dPhi_HH = TMath::Abs(deltaPhi(HbbP4.phi(), (WjjP4 + selLeptonP4 + metP4).phi()));
    double mT_W = mT2_2particle::comp_mT(selLeptonP4.px(), selLeptonP4.py(), selLeptonP4.mass(), metP4.px(), metP4.py(), 0.);
    double mT_top_2particle_permutation1 = mT2_2particle::comp_mT(
      selJetP4_Hbb_lead.px(), selJetP4_Hbb_lead.py(), selJetP4_Hbb_lead.mass(),
      selLeptonP4.px() + metP4.px(), selLeptonP4.py() + metP4.py(), mem::wBosonMass);
    double mT_top_2particle_permutation2 = mT2_2particle::comp_mT(
      selJetP4_Hbb_sublead.px(), selJetP4_Hbb_sublead.py(), selJetP4_Hbb_sublead.mass(),
      selLeptonP4.px() + metP4.px(), selLeptonP4.py() + metP4.py(), mem::wBosonMass);
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

    //---------------------------------------------------------------------------
    // CV: compute matrix element method (MEM) likelihood ratio of HH signal and ttbar background hypotheses

    // check that reconstructed leptons and b-jets are generator-level matched
    if ( genMatchingOption == 1 || genMatchingOption == 2 ) {
      if ( !(selLepton->genLepton() && selJet_Wjj_lead->genJet() && selJet_Wjj_sublead->genJet() && selJet_Hbb_lead->genJet() && selJet_Hbb_sublead->genJet()) ) {
	//if ( run_lumi_eventSelector ) {
	  std::cout << "event " << eventInfo.str() << " FAILS generator-level matching." << std::endl;
	  std::cout << "selLepton->genLepton = " << selLepton->genLepton() << std::endl;
	  std::cout << "selLepton: pT = " << selLepton->pt() << ", eta = " << selLepton->eta() << ", phi = " << selLepton->phi() << std::endl;
	  const GenJet* genJetFromWBoson1 = &genJetsFromWBosonForMatching[0];
	  std::cout << "genJetFromWBoson #0: pT = " << genJetFromWBoson1->pt() << ", eta = " << genJetFromWBoson1->eta() << ", phi = " << genJetFromWBoson1->phi() << std::endl;
	  const GenJet* genJetFromWBoson2 = &genJetsFromWBosonForMatching[1];
	  std::cout << "genJetFromWBoson #1: pT = " << genJetFromWBoson2->pt() << ", eta = " << genJetFromWBoson2->eta() << ", phi = " << genJetFromWBoson2->phi() << std::endl;
	  const GenJet* genBJet1 = &genBJetsForMatching[0];
	  std::cout << "genBJet #0: pT = " << genBJet1->pt() << ", eta = " << genBJet1->eta() << ", phi = " << genBJet1->phi() << std::endl;
	  const GenJet* genBJet2 = &genBJetsForMatching[1];
	  std::cout << "genBJet #1: pT = " << genBJet2->pt() << ", eta = " << genBJet2->eta() << ", phi = " << genBJet2->phi() << std::endl;
	  printCollection("uncleaned AK4 jets", jet_ptrs_ak4);
	  printCollection("selJetsAK4_Hbb", selJetsAK4_Hbb);
	  printCollection("selJetsAK4_Wjj", selJetsAK4_Wjj);
	  std::cout << "selJet_Wjj_lead->genJet = " << selJet_Wjj_lead->genJet() << std::endl;
          std::cout << "selJet_Wjj_lead: pT = " << selJet_Wjj_lead->pt() << ", eta = " << selJet_Wjj_lead->eta() << ", phi = " << selJet_Wjj_lead->phi() << std::endl;
	  std::cout << "selJet_Wjj_sublead->genJet = " << selJet_Wjj_sublead->genJet() << std::endl;
	  std::cout << "selJet_Wjj_sublead: pT = " << selJet_Wjj_sublead->pt() << ", eta = " << selJet_Wjj_sublead->eta() << ", phi = " << selJet_Wjj_sublead->phi() << std::endl;
	  std::cout << "selJet_Hbb_lead->genJet = " << selJet_Hbb_lead->genJet() << std::endl;
	  printBJet("selJet_Hbb_lead", selJet_Hbb_lead);
	  std::cout << "selJet_Hbb_sublead->genJet = " << selJet_Hbb_sublead->genJet() << std::endl;
	  printBJet("selJet_Hbb_sublead", selJet_Hbb_sublead);
	  std::cout << "--> CHECK !!" << std::endl;
	//}
	continue;
      }
    }
    cutFlowTable.update("generator-level matching", evtWeight_inclusive);

    // use either generator-level or reconstructed momenta as input for MEM computation
    Particle::LorentzVector memLeptonP4;
    Particle::LorentzVector memJetFromWBosonP4_lead;
    Particle::LorentzVector memJetFromWBosonP4_sublead;
    Particle::LorentzVector memBJetP4_lead;
    Particle::LorentzVector memBJetP4_sublead;
    double memMEtPx = 0.;
    double memMEtPy = 0.;
    if ( genMatchingOption == 1 ) {
      memLeptonP4 = selLepton->genLepton()->p4();
      memJetFromWBosonP4_lead = selJet_Wjj_lead->genJet()->p4();
      memJetFromWBosonP4_sublead = selJet_Wjj_sublead->genJet()->p4();
      memBJetP4_lead = selJet_Hbb_lead->genJet()->p4();
      memBJetP4_sublead = selJet_Hbb_sublead->genJet()->p4();
      memMEtPx = genMEtPx;
      memMEtPy = genMEtPy;
    } else {
      memLeptonP4 = selLepton->p4();
      memJetFromWBosonP4_lead = selJet_Wjj_lead->p4();
      memJetFromWBosonP4_sublead = selJet_Wjj_sublead->p4();
      memBJetP4_lead = selJet_Hbb_lead->p4();
      memBJetP4_sublead = selJet_Hbb_sublead->p4();
      memMEtPx = metP4.px();
      memMEtPy = metP4.py();
    }
    int memLeptonType;
    double memLeptonMass;
    if ( selLepton->is_electron() ) {
      memLeptonType = mem::MeasuredParticle::kElectron;
      memLeptonMass = mem::electronMass;
    } else if ( selLepton->is_muon() ) {
      memLeptonType = mem::MeasuredParticle::kMuon;
      memLeptonMass = mem::muonMass;
    } else assert(0);

    std::vector<mem::MeasuredParticle> memMeasuredParticles;
    memMeasuredParticles.push_back(mem::MeasuredParticle(memLeptonType,
      memLeptonP4.pt(), memLeptonP4.eta(), memLeptonP4.phi(),
      memLeptonMass, selLepton->charge()));
    memMeasuredParticles.push_back(mem::MeasuredParticle(mem::MeasuredParticle::kHadWJet,
      memJetFromWBosonP4_lead.pt(), memJetFromWBosonP4_lead.eta(), memJetFromWBosonP4_lead.phi(),
      0.));
    memMeasuredParticles.push_back(mem::MeasuredParticle(mem::MeasuredParticle::kHadWJet,
      memJetFromWBosonP4_sublead.pt(), memJetFromWBosonP4_sublead.eta(), memJetFromWBosonP4_sublead.phi(),
      0.));
    memMeasuredParticles.push_back(mem::MeasuredParticle(mem::MeasuredParticle::kBJet,
      memBJetP4_lead.pt(), memBJetP4_lead.eta(), memBJetP4_lead.phi(),
      mem::bottomQuarkMass));
    memMeasuredParticles.push_back(mem::MeasuredParticle(mem::MeasuredParticle::kBJet,
      memBJetP4_sublead.pt(), memBJetP4_sublead.eta(), memBJetP4_sublead.phi(),
      mem::bottomQuarkMass));

    const double sqrtS = 13.e+3;
    const std::string pdfName = "MSTW2008lo68cl";
    const std::string madgraphFileName_signal     = "hhAnalysis/bbwwMEM/data/param_hh.dat";
    const std::string madgraphFileName_background = "hhAnalysis/bbwwMEM/data/param_ttbar.dat";
    const bool applyOnshellWmassConstraint_signal = false;

    clock.Start("memAlgo");
    const int verbosity = 1;
    MEMbbwwAlgoSingleLepton memAlgo(sqrtS, pdfName, findFile(madgraphFileName_signal), findFile(madgraphFileName_background), verbosity);
    memAlgo.applyOnshellWmassConstraint_signal(applyOnshellWmassConstraint_signal);
    memAlgo.setIntMode(MEMbbwwAlgoSingleLepton::kVAMP);
    memAlgo.setMaxObjFunctionCalls_signal(2500);
    memAlgo.setMaxObjFunctionCalls_background(25000);
    memAlgo.integrate(memMeasuredParticles, memMEtPx, memMEtPy, met.cov());
    const MEMbbwwResultSingleLepton& memResult = memAlgo.getResult();
    clock.Stop("memAlgo");

    double memCpuTime = clock.GetCpuTime("memAlgo");
    std::cout << "MEM: likelihood ratio = " << memResult.getLikelihoodRatio() << " +/- " << memResult.getLikelihoodRatioErr() << " (CPU time = " << memCpuTime << ")" << std::endl;

    if ( (memResult.getLikelihoodRatio() < 0.01 &&  isSignal) ||
	 (memResult.getLikelihoodRatio() > 0.99 && !isSignal) ) {
      const GenLepton* genLepton = &genLeptonsForMatching[0];
      int genLepton_matchType = compGenMatchType(genLepton, std::vector<const RecoLepton*>({ selLepton }), preselLeptonsFull, tightLeptonsFull);
      fillWithOverFlow(histogram_badMEM_genLepton_matchType, genLepton_matchType, evtWeight);
      const GenJet* genJet_Hbb_lead = &genBJetsForMatching[0];
      int genJet_Hbb_lead_matchType = compGenMatchType(genJet_Hbb_lead, std::vector<const RecoJetBase*>({ selJet_Hbb_lead, selJet_Hbb_sublead }), jet_ptrs_ak4, selJetsAK4);
      fillWithOverFlow(histogram_badMEM_genJet_Hbb_lead_matchType, genJet_Hbb_lead_matchType, evtWeight);
      const GenJet* genJet_Hbb_sublead = &genBJetsForMatching[1];
      int genJet_Hbb_sublead_matchType = compGenMatchType(genJet_Hbb_sublead, std::vector<const RecoJetBase*>({ selJet_Hbb_lead, selJet_Hbb_sublead }), jet_ptrs_ak4, selJetsAK4);
      fillWithOverFlow(histogram_badMEM_genJet_Hbb_sublead_matchType, genJet_Hbb_sublead_matchType, evtWeight);
      const GenJet* genJet_Wjj_lead = &genJetsFromWBosonForMatching[0];
      int genJet_Wjj_lead_matchType = compGenMatchType(genJet_Wjj_lead, std::vector<const RecoJetBase*>({ selJet_Wjj_lead, selJet_Wjj_sublead }), jet_ptrs_ak4, selJetsAK4);
      fillWithOverFlow(histogram_badMEM_genJet_Wjj_lead_matchType, genJet_Wjj_lead_matchType, evtWeight);
      const GenJet* genJet_Wjj_sublead = &genJetsFromWBosonForMatching[1];
      int genJet_Wjj_sublead_matchType = compGenMatchType(genJet_Wjj_sublead, std::vector<const RecoJetBase*>({ selJet_Wjj_lead, selJet_Wjj_sublead }), jet_ptrs_ak4, selJetsAK4);
      fillWithOverFlow(histogram_badMEM_genJet_Wjj_sublead_matchType, genJet_Wjj_sublead_matchType, evtWeight);
      fillWithOverFlow(histogram_badMEM_numBJets_loose, numBJets_loose, evtWeight);
      fillWithOverFlow(histogram_badMEM_numBJets_medium, numBJets_medium, evtWeight);
    }
    //---------------------------------------------------------------------------

    mvaInputs_XGB["met"] = metP4.pt();
    mvaInputs_XGB["HT"] = HT;
    mvaInputs_XGB["m_Hbb"] = m_Hbb;
    mvaInputs_XGB["dR_Hbb"] = dR_Hbb;
    mvaInputs_XGB["dR_Hww"] = dR_Hww;
    mvaInputs_XGB["dR_b1lep"] = dR_b1lep;
    mvaInputs_XGB["dR_b2lep"] = dR_b2lep;
    mvaInputs_XGB["pT_HH"] = pT_HH;
    mvaInputs_XGB["mT_W"] = mT_W;
    mvaInputs_XGB["mT_top_2particle"] = mT_top_2particle;
    mvaInputs_XGB["mvaOutput_Hj_tagger"] = mvaOutput_Hj_tagger;
    mvaInputs_XGB["gen_mHH"] = 350;
    double mvaoutput_bb1l350 = mva_xgb_bb1l(mvaInputs_XGB);
    mvaInputs_XGB["gen_mHH"] = 400;
    double mvaoutput_bb1l400 = mva_xgb_bb1l(mvaInputs_XGB);
    mvaInputs_XGB["gen_mHH"] = 750;
    double mvaoutput_bb1l750 = mva_xgb_bb1l(mvaInputs_XGB);

//--- fill histograms with events passing final selection
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
      -1., -1., -1., -1., -1., -1.,
      &memResult, memCpuTime,
      mvaoutput_bb1l350, mvaoutput_bb1l400, mvaoutput_bb1l750,
      evtWeight);
    if ( isMC ) {
      selHistManager->genEvtHistManager_afterCuts_->fillHistograms(genElectrons, genMuons, {}, {}, genJets, evtWeight_inclusive);
      selHistManager->lheInfoHistManager_afterCuts_->fillHistograms(*lheInfoReader, evtWeight);
    }
    selHistManager->weights_->fillHistograms("genWeight", eventInfo.genWeight);
    selHistManager->weights_->fillHistograms("pileupWeight", eventInfo.pileupWeight);
    selHistManager->weights_->fillHistograms("triggerWeight", triggerWeight);
    selHistManager->weights_->fillHistograms("data_to_MC_correction", weight_data_to_MC_correction);

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

  delete dataToMCcorrectionInterface;

  delete run_lumi_eventSelector;

  delete selEventsFile;

  delete muonReader;
  delete electronReader;
  delete jetReaderAK4;
  delete jetReaderAK8_Hbb;
  if ( jetReaderAK8_Wjj != jetReaderAK8_Hbb ) {
    delete jetReaderAK8_Wjj;
  }
  delete metReader;
  delete metFilterReader;
  delete genLeptonReader;
  delete genJetReader;
  delete lheInfoReader;

  delete genEvtHistManager_beforeCuts;

  hltPaths_delete(triggers_1e);
  hltPaths_delete(triggers_1mu);

  delete inputTree;

  clock.Show("testMEM_hh_bb1l");

  return EXIT_SUCCESS;
}
