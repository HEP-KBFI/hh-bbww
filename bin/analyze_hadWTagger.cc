#include "FWCore/ParameterSet/interface/ParameterSet.h" // edm::ParameterSet
#include "FWCore/Utilities/interface/Exception.h" // cms::Exception
#include "PhysicsTools/FWLite/interface/TFileService.h" // fwlite::TFileService
#include "DataFormats/FWLite/interface/InputSource.h" // fwlite::InputSource
#include "DataFormats/FWLite/interface/OutputFiles.h" // fwlite::OutputFiles
#include "DataFormats/Math/interface/LorentzVector.h" // math::PtEtaPhiMLorentzVector
#include "DataFormats/Math/interface/deltaR.h" // deltaR
#include "DataFormats/Math/interface/deltaPhi.h" // deltaPhi

#if __has_include (<FWCore/ParameterSetReader/interface/ParameterSetReader.h>)
#  include <FWCore/ParameterSetReader/interface/ParameterSetReader.h> // edm::readPSetsFrom()
#else
#  include <FWCore/PythonParameterSet/interface/MakeParameterSets.h> // edm::readPSetsFrom()
#endif

#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronReader.h" // RecoElectronReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonReader.h" // RecoMuonReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetReader.h" // RecoJetReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetReaderAK8.h" // RecoJetReaderAK8
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEtReader.h" // RecoMEtReader, RecoMEt
#include "tthAnalysis/HiggsToTauTau/interface/EventInfoReader.h" // EventInfoReader, EventInfo
#include "tthAnalysis/HiggsToTauTau/interface/GenLeptonReader.h" // GenLeptonReader
#include "tthAnalysis/HiggsToTauTau/interface/GenJetReader.h" // GenJetReader
#include "tthAnalysis/HiggsToTauTau/interface/GenParticleReader.h" // GenParticleReader
#include "tthAnalysis/HiggsToTauTau/interface/LHEInfoReader.h" // LHEInfoReader
#include "tthAnalysis/HiggsToTauTau/interface/convert_to_ptrs.h" // convert_to_ptrs
#include "tthAnalysis/HiggsToTauTau/interface/ParticleCollectionCleaner.h" // RecoElectronCollectionCleaner, RecoMuonCollectionCleaner, RecoJetCollectionCleaner
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronCollectionSelectorLoose.h" // RecoElectronCollectionSelectorLoose
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronCollectionSelectorFakeable.h" // RecoElectronCollectionSelectorFakeable
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronCollectionSelectorTight.h" // RecoElectronCollectionSelectorTight
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonCollectionSelectorLoose.h" // RecoMuonCollectionSelectorLoose
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonCollectionSelectorFakeable.h" // RecoMuonCollectionSelectorFakeable
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonCollectionSelectorTight.h" // RecoMuonCollectionSelectorTight
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetCollectionSelector.h" // RecoJetCollectionSelector
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetCollectionSelectorBtag.h" // RecoJetCollectionSelectorBtagLoose, RecoJetCollectionSelectorBtagMedium
#include "tthAnalysis/HiggsToTauTau/interface/RunLumiEventSelector.h" // RunLumiEventSelector
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // selectObjects(), get_selection(), get_era(), kLoose, kFakeable, kTight
#include "tthAnalysis/HiggsToTauTau/interface/mvaInputVariables.h" // comp_MT_met
#include "tthAnalysis/HiggsToTauTau/interface/sysUncertOptions.h" // k*_central
#include "tthAnalysis/HiggsToTauTau/interface/memAuxFunctions.h" // get_memObjectBranchName(), get_memPermutationBranchName()
#include "tthAnalysis/HiggsToTauTau/interface/cutFlowTable.h" // cutFlowTableType
#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // createSubdirectory_recursively()
#include "tthAnalysis/HiggsToTauTau/interface/NtupleFillerBDT.h" // NtupleFillerBDT
#include "tthAnalysis/HiggsToTauTau/interface/TTreeWrapper.h" // TTreeWrapper

#include "hhAnalysis/multilepton/interface/EvtWeightRecorderHH.h" // EvtWeightRecorderHH

#include "hhAnalysis/bbww/interface/RecoJetCollectionSelectorAK8_hh_bbWW_Hbb.h" // RecoJetSelectorAK8_hh_bbWW_Hbb
#include "hhAnalysis/bbww/interface/jetSelectionAuxFunctions.h" // selectJets_Hbb, countBJetsJets_Hbb, selectJets_Wjj
#include "hhAnalysis/bbww/interface/genMatchingAuxFunctions.h" // isGenMatched
#include "hhAnalysis/bbww/interface/GenParticleMatcherFromHiggs.h" // GenParticleMatcherFromHiggs
#include "hhAnalysis/bbww/interface/GenParticleMatcherFromTop.h" // GenParticleMatcherFromTop
#include "hhAnalysis/bbww/interface/comp_metP4_B2G_18_008.h" // comp_metP4_B2G_18_008

#include <TChain.h> // TChain
#include <TTree.h> // TTree
#include <TBenchmark.h> // TBenchmark
#include <TString.h> // TString, Form
#include <TError.h> // gErrorAbortLevel, kError
#include <TH2D.h>
#include <TLorentzVector.h> // TLorentzVector

#include <boost/algorithm/string/predicate.hpp> // boost::starts_with()
#include <boost/math/special_functions/sign.hpp> // boost::math::sign()

#include <iostream> // std::cerr, std::fixed
#include <cstdlib> // EXIT_SUCCESS, EXIT_FAILURE
#include <assert.h> // assert

typedef std::vector<std::string> vstring;

const double higgsBosonMass = 125.;
const double topMass = 172.9; // CV: taken from http://pdg.lbl.gov/2019/listings/rpp2019-list-t-quark.pdf ("OUR AVERAGE")

enum { kMode_undefined, kMode_hadWTagger, kMode_jpa_4jet, kMode_jpa_missingBJet, kMode_jpa_missingWJet, kMode_jpa_missingBJet_missingWJet, kMode_jpa_missingAllWJet, kMode_jpa_missingBJet_missingAllWJet, kMode_jpa_restOfcat };
TH2D* h_genmatch = new TH2D("genmatc", "" , 3, -0.5,2.5, 3, -0.5, 2.5);
//TH1D* h_genmatch = new TH1D("genmatch", "" ,3, -0.5, 2.5);
NtupleFillerBDT<float, int>* createNtuple(std::string mode, std::string histogramDir, std::string era_string, std::string process_string) {

  NtupleFillerBDT<float, int>* bdt_filler = new std::remove_pointer<decltype(bdt_filler)>::type(
			makeHistManager_cfg(process_string, Form("%s/sel/evtntuple_%s", histogramDir.data(), mode.data()), era_string, "central")
  );
  typedef std::remove_pointer<decltype(bdt_filler)>::type::float_type float_type;
  typedef std::remove_pointer<decltype(bdt_filler)>::type::int_type int_type;

  bdt_filler->register_variable<float_type>(
    "lepton_pt", "lepton_eta", "lepton_phi", "lepton_mass", "lepton_charge",
    "neutrino_pt", "neutrino_eta", "neutrino_phi", "neutrino_mass",
    "bjet1_pt", "bjet1_ptReg", "bjet1_eta", "bjet1_phi", "bjet1_mass","bjet1_btagCSV", "bjet1_qgDiscr", "bjet1_charge", "dR_bjet1_lep", "dPhi_bjet1_lep", "dEta_bjet1_lep",
    "bjet2_pt", "bjet2_ptReg", "bjet2_eta", "bjet2_phi", "bjet2_mass", "bjet2_btagCSV", "bjet2_qgDiscr", "bjet2_charge", "dR_bjet2_lep", "dPhi_bjet2_lep", "dEta_bjet2_lep",
    "wjet1_pt", "wjet1_ptReg", "wjet1_eta", "wjet1_phi", "wjet1_mass", "wjet1_btagCSV", "wjet1_qgDiscr", "wjet1_charge", "dR_wjet1_lep", "dPhi_wjet1_lep", "dEta_wjet1_lep",
    "wjet2_pt", "wjet2_ptReg", "wjet2_eta", "wjet2_phi", "wjet2_mass", "wjet2_btagCSV", "wjet2_qgDiscr", "wjet2_charge", "dR_wjet2_lep", "dPhi_wjet2_lep", "dEta_wjet2_lep",
    "Hbb_pt", "Hbb_ptReg", "Hbb_eta", "Hbb_etaReg", "Hbb_phi", "Hbb_phiReg", "Hbb_mass", "Hbb_massReg",
    "dR_bjet1bjet2", "dPhi_bjet1bjet2",
    "HadW_pt", "HadW_eta", "HadW_phi", "HadW_mass", "HadW_cosTheta", "dR_HadW_lep", "dPhi_HadW_lep", "dEta_HadW_lep",
    "min_dR_HadW_bjet", "max_dR_HadW_bjet",
    "dR_wjet1wjet2", "dPhi_wjet1wjet2",
    "LepW_mT",
    "Hww_mT", "Hww_mass",
    "mTop1", "mTop2",
    "dR_W1W2",
    "nRowsPerEvent",
    "evtWeight"
   );

  bdt_filler->register_variable<int_type>(
   "bjet1_isGenBJet", "bjet1_isGenWJet",
   "bjet2_isGenBJet", "bjet2_isGenWJet",
   "wjet1_isGenBJet", "wjet1_isGenWJet",
   "wjet2_isGenBJet", "wjet2_isGenWJet",
   "Hbb_isBoosted",
   "nJet", "nGenMatchedJet_Hbb", "nGenMatchedJet_Wjj", "nBJetLoose", "nBJetMedium", "nLep",
   "nGenJet_Hbb", "nGenJet_Wjj",
  "idxRow",
   "isGenMatched"
  );
  return bdt_filler;
}

std::pair<int, int> matchedJets(const std::vector<const RecoJet*>& cleanedJetsAK4_wrtLeptons,
				const std::vector<const GenJet*>& genBJets_ptrs, const std::vector<const GenJet*>& genWJets_ptrs,
				bool Hbb_isBoosted = false) {
  int matchedBJet(0);
  int matchedWJet(0);
  for ( std::vector<const RecoJet*>::const_iterator selJet1 = cleanedJetsAK4_wrtLeptons.begin();
	selJet1 != cleanedJetsAK4_wrtLeptons.end(); ++selJet1 ) {

    if ( !Hbb_isBoosted && isGenMatched((*selJet1)->eta(), (*selJet1)->phi(), genBJets_ptrs) ) {
      ++matchedBJet;
    }
    else if ( isGenMatched((*selJet1)->eta(), (*selJet1)->phi(), genWJets_ptrs) )  {
      ++matchedWJet;
    }
  }
  return std::pair<int, int>(matchedBJet, matchedWJet);
}

double
compCosTheta(const Particle::LorentzVector& recWJet1, const Particle::LorentzVector& recWJet2)
{
  TLorentzVector PWj1, PWj2;
  PWj1.SetPtEtaPhiM(recWJet1.pt(), recWJet1.eta(), recWJet1.phi(), recWJet1.mass());
  PWj2.SetPtEtaPhiM(recWJet2.pt(), recWJet2.eta(), recWJet2.phi(), recWJet2.mass());
  TLorentzVector PW = PWj1 + PWj2;

  TLorentzVector PWj1boost, PWj2boost;
  PWj1boost = PWj1;
  PWj1boost.Boost(-PW.BoostVector());
  PWj2boost = PWj2;
  PWj2boost.Boost(-PW.BoostVector());

  double cosTheta = -100;
  if ( PWj1.Pt() > PWj2.Pt() )
  {
    cosTheta = PWj1boost.CosTheta();
  }
  else
  {
    cosTheta = PWj2boost.CosTheta();
  }
  return cosTheta;
}

template<typename T>
size_t 
countGenMatchedJets(const std::vector<const T*>& recJets, const std::vector<const GenJet*>& genJets)
{
  size_t numGenMatchedJets = 0;
  for ( std::vector<const GenJet*>::const_iterator genJet = genJets.begin();
        genJet != genJets.end(); ++genJet ) {
    bool isMatched = false;
    for ( typename std::vector<const T*>::const_iterator recJet = recJets.begin();
          recJet != recJets.end(); ++recJet ) {
      if ( deltaR((*genJet)->p4(), (*recJet)->p4()) < 0.3 ) 
      {
        isMatched = true;
        break;
      }
    }
    if ( isMatched ) ++numGenMatchedJets;
  }
  return numGenMatchedJets;
}

bool
isWithinRoundingErrors_abs(double x1, double x2, double epsilon = 2.e-1)
{
  if ( std::fabs(x1 - x2) < epsilon ) return true;
  else return false;	
}

bool
isWithinRoundingErrors_rel(double x1, double x2, double epsilon = 5.e-2)
{
  if ( std::fabs(x1 - x2) < epsilon*(std::fabs(x1) + std::fabs(x2)) ) return true;
  else return false;	
}

void
writeToNtuple(NtupleFillerBDT<float, int>& bdt_filler,
              const RecoLepton* selLepton, 
              const std::string& branchName, const RecoJetBase* selJet_base, 
              const std::vector<const GenJet*>& genBJets, const std::vector<const GenJet*>& genWJets)
{
  Particle::LorentzVector selJetP4;
  Particle::LorentzVector selJetP4_reg;
  double selJet_btagCSV = 0.;
  double selJet_qgDiscr = 0.;
  double selJet_charge = 0.;
  int selJet_isGenBJet = 0;
  int selJet_isGenWJet = 0;
  double dR_jet_lep = 0.;
  double dPhi_jet_lep = 0.;
  double dEta_jet_lep = 0.;
  if ( selJet_base ) 
  {  
    selJetP4 = selJet_base->p4();
    if ( dynamic_cast<const RecoJet*>(selJet_base) )
    {
      const RecoJet* selJet = dynamic_cast<const RecoJet*>(selJet_base);
      selJetP4_reg = selJet->p4_bRegCorr();
      selJet_btagCSV = selJet->BtagCSV();
      selJet_qgDiscr = selJet->QGDiscr();
    }
    selJet_charge = selJet_base->charge();
    selJet_isGenBJet = isGenMatched(selJet_base->eta(), selJet_base->phi(), genBJets);
    selJet_isGenWJet = isGenMatched(selJet_base->eta(), selJet_base->phi(), genWJets);
    dR_jet_lep = deltaR(selJetP4, selLepton->p4());
    dPhi_jet_lep = deltaPhi(selJetP4.phi(), selLepton->phi());
    dEta_jet_lep = TMath::Abs(selJetP4.eta() - selLepton->eta());
  }
  bdt_filler(Form("%s_pt", branchName.data()), selJetP4.pt());
  bdt_filler(Form("%s_ptReg", branchName.data()), selJetP4_reg.pt());
  bdt_filler(Form("%s_eta", branchName.data()), selJetP4.eta());
  bdt_filler(Form("%s_phi", branchName.data()), selJetP4.phi());
  bdt_filler(Form("%s_mass", branchName.data()), selJetP4.mass());
  bdt_filler(Form("%s_btagCSV", branchName.data()), selJet_btagCSV);
  bdt_filler(Form("%s_qgDiscr", branchName.data()), selJet_qgDiscr);
  bdt_filler(Form("%s_charge", branchName.data()), selJet_charge);
  bdt_filler(Form("%s_isGenBJet", branchName.data()), selJet_isGenBJet);
  bdt_filler(Form("%s_isGenWJet", branchName.data()), selJet_isGenWJet);
  bdt_filler(Form("dR_%s_lep", branchName.data()), dR_jet_lep);
  bdt_filler(Form("dPhi_%s_lep", branchName.data()), dPhi_jet_lep);
  bdt_filler(Form("dEta_%s_lep", branchName.data()), dEta_jet_lep);
}

void
writeToNtuple(NtupleFillerBDT<float, int>& bdt_filler,
              const EventInfo& eventInfo,
              const RecoLepton* selLepton, const std::vector<const GenLepton*>& genLeptons,
              const Particle::LorentzVector& metP4,
              const RecoJetBase* selBJet1_base, const RecoJetBase* selBJet2_base, bool Hbb_isBoosted, const std::vector<const GenJet*>& genBJets, 
              const RecoJet* selWJet1, const RecoJet* selWJet2, const std::vector<const GenJet*>& genWJets,
              int numJets, int numJets_genMatched_to_Hbb, int numJets_genMatched_to_Wjj, int numBJetsLoose, int numBJetsMedium, int numLeptons,
              int idxRow, double numRowsPerEvent,
              bool isGenMatched_value,
              double evtWeight)
{
  if ( !isGenMatched(selLepton->eta(), selLepton->phi(), genLeptons) ) return;

  Particle::LorentzVector selBJet1P4;
  Particle::LorentzVector selBJet1P4_reg;
  if ( selBJet1_base ) 
  {  
    selBJet1P4 = selBJet1_base->p4();
    if ( dynamic_cast<const RecoJet*>(selBJet1_base) )
    {
      const RecoJet* selBJet1 = dynamic_cast<const RecoJet*>(selBJet1_base);
      selBJet1P4_reg = selBJet1->p4_bRegCorr();
    }
  }
  Particle::LorentzVector selBJet2P4;
  Particle::LorentzVector selBJet2P4_reg;
  if ( selBJet2_base ) 
  { 
    selBJet2P4 = selBJet2_base->p4();
    if ( dynamic_cast<const RecoJet*>(selBJet2_base) )
    {
      const RecoJet* selBJet2 = dynamic_cast<const RecoJet*>(selBJet2_base);
      selBJet2P4_reg = selBJet2->p4_bRegCorr();
    }
  }

  Particle::LorentzVector selWJet1P4;
  if ( selWJet1 ) selWJet1P4 = selWJet1->p4();
  Particle::LorentzVector selWJet2P4;
  if ( selWJet2 ) selWJet2P4 = selWJet2->p4();

  Particle::LorentzVector HbbP4;
  Particle::LorentzVector HbbP4_reg;
  double dR_bjet1bjet2 = 0.;
  double dPhi_bjet1bjet2 = 0.;
  if ( selBJet1_base && selBJet2_base )
  {
    HbbP4 = selBJet1P4 + selBJet2P4;
    HbbP4_reg = selBJet1P4_reg + selBJet2P4_reg;
    dR_bjet1bjet2 = deltaR(selBJet1P4, selBJet2P4);
    dPhi_bjet1bjet2 = deltaPhi(selBJet1P4.phi(), selBJet2P4.phi());
  }

  Particle::LorentzVector HadWP4;
  double HadW_cosTheta = 0.;
  double dR_HadW_lep = 0.;
  double dPhi_HadW_lep = 0.;
  double dEta_HadW_lep = 0.;
  double min_dR_HadW_bjet = 0.;
  double max_dR_HadW_bjet = 0.;
  double dR_wjet1wjet2 = 0.;
  double dPhi_wjet1wjet2 = 0.;
  Particle::LorentzVector neutrinoP4_B2G_18_008;
  Particle::LorentzVector LepWP4;
  double LepW_mT = 0.;
  Particle::LorentzVector HwwP4;
  double Hww_mT = 0.;
  double mTop1 = 0.;
  double mTop2 = 0.; 
  double dR_W1W2 = 0.; 
  if ( selWJet1 && selWJet2 )
  {
    HadWP4 = selWJet1P4 + selWJet2P4;
    HadW_cosTheta = compCosTheta(selWJet1P4, selWJet2P4);
    dR_HadW_lep = deltaR(HadWP4, selLepton->p4());
    dPhi_HadW_lep = deltaPhi(HadWP4.phi(), selLepton->phi());
    dEta_HadW_lep = TMath::Abs(HadWP4.eta() - selLepton->eta());
    if ( selBJet1_base && selBJet2_base )
    {
      double dR_HadW_bjet1 = deltaR(HadWP4, selBJet1P4);
      double dR_HadW_bjet2 = deltaR(HadWP4, selBJet2P4);
      min_dR_HadW_bjet = TMath::Min(dR_HadW_bjet1, dR_HadW_bjet2);
      max_dR_HadW_bjet = TMath::Max(dR_HadW_bjet1, dR_HadW_bjet2);    
    }
    else
    {
      min_dR_HadW_bjet = deltaR(HadWP4, selBJet1P4);
    } 
    dR_wjet1wjet2 = deltaR(selWJet1P4, selWJet2P4);
    dPhi_wjet1wjet2 = deltaPhi(selWJet1P4.phi(), selWJet2P4.phi());

    // compute four-vector of neutrino produced in H->WW*->jj lnu decay,
    // using Higgs boson mass constraint, as described in Section 3.4.2 of AN-2018/058 (v4)
    //
    // Note: mass of lepton + jets from W->jj decay + neutrino is not equal to 125 GeV
    //       in case the Higgs boson mass constraint yields a complex solution for the logitudinal momentum of the neutrino
    //      (of which we then take the real part and discard the complex part)
    neutrinoP4_B2G_18_008 = comp_metP4_B2G_18_008(selLepton->p4() + selWJet1P4 + selWJet2P4, metP4.px(), metP4.py(), higgsBosonMass);

    LepWP4 = selLepton->p4() + neutrinoP4_B2G_18_008;
    LepW_mT = comp_MT_met(selLepton->p4(), metP4.pt(), metP4.phi());

    HwwP4 = LepWP4 + HadWP4;
    double HwwEt = selWJet1P4.Et() + selWJet2P4.Et() + selLepton->pt()      + metP4.pt();
    double HwwPx = selWJet1P4.px() + selWJet2P4.px() + selLepton->p4().px() + metP4.px();
    double HwwPy = selWJet1P4.py() + selWJet2P4.py() + selLepton->p4().py() + metP4.py();
    Hww_mT = TMath::Sqrt(TMath::Max(0., HwwEt*HwwEt - (HwwPx*HwwPx + HwwPy*HwwPy)));

    if ( selBJet1_base && selBJet2_base )
    {
      Particle::LorentzVector top1P4 = selBJet1P4_reg + HadWP4;
      Particle::LorentzVector top2P4 = selBJet2P4_reg + HadWP4;
      if ( TMath::Abs(top1P4.mass() - topMass) < TMath::Abs(top2P4.mass() - topMass) )
      {
        mTop1 = top1P4.mass();
        mTop2 = top2P4.mass();
      }
      else
      {
        mTop1 = top2P4.mass();
        mTop2 = top1P4.mass();
      }
    } 
    else if ( selBJet1_base )
    {
      mTop1 = (selBJet1P4_reg + HadWP4).mass();
    }
    
    dR_W1W2 = deltaR(HadWP4, LepWP4);
  }

  bdt_filler({ eventInfo.run, eventInfo.lumi, eventInfo.event })
    ("lepton_pt",              selLepton->pt())
    ("lepton_eta",             selLepton->eta())
    ("lepton_phi",             selLepton->phi())
    ("lepton_mass",             selLepton->mass())
    ("lepton_charge",          selLepton->charge())
    ("neutrino_pt",            neutrinoP4_B2G_18_008.pt())
    ("neutrino_eta",           neutrinoP4_B2G_18_008.eta())
    ("neutrino_phi",           neutrinoP4_B2G_18_008.phi())
    ("neutrino_mass",           neutrinoP4_B2G_18_008.mass());
  writeToNtuple(bdt_filler, selLepton, "bjet1", selBJet1_base, genBJets, genWJets);
  writeToNtuple(bdt_filler, selLepton, "bjet2", selBJet2_base, genBJets, genWJets);
  writeToNtuple(bdt_filler, selLepton, "wjet1", selWJet1, genBJets, genWJets);
  writeToNtuple(bdt_filler, selLepton, "wjet2", selWJet2, genBJets, genWJets);
  bdt_filler(
     "Hbb_pt",                 HbbP4.pt())
    ("Hbb_ptReg",              HbbP4_reg.pt())
    ("Hbb_eta",                HbbP4.eta())
    ("Hbb_etaReg",             HbbP4_reg.eta())
    ("Hbb_phi",                HbbP4.phi())
    ("Hbb_phiReg",             HbbP4_reg.phi())
    ("Hbb_mass",               HbbP4.mass())
    ("Hbb_massReg",            HbbP4_reg.mass())
    ("Hbb_isBoosted",          Hbb_isBoosted)
    ("dR_bjet1bjet2",          dR_bjet1bjet2)
    ("dPhi_bjet1bjet2",        dPhi_bjet1bjet2)
    ("HadW_pt",                HadWP4.pt())
    ("HadW_eta",               HadWP4.eta())
    ("HadW_phi",               HadWP4.phi())
    ("HadW_mass",              HadWP4.mass())
    ("HadW_cosTheta",          HadW_cosTheta)
    ("dR_HadW_lep",            dR_HadW_lep)
    ("dPhi_HadW_lep",          dPhi_HadW_lep)
    ("dEta_HadW_lep",          dEta_HadW_lep)
    ("min_dR_HadW_bjet",       min_dR_HadW_bjet)
    ("max_dR_HadW_bjet",       max_dR_HadW_bjet)
    ("dR_wjet1wjet2",          dR_wjet1wjet2)
    ("dPhi_wjet1wjet2",        dPhi_wjet1wjet2)
    ("LepW_mT",                LepW_mT)
    ("Hww_mT",                 Hww_mT)
    ("Hww_mass",               HwwP4.mass())
    ("mTop1",                  mTop1)
    ("mTop2",                  mTop2)
    ("dR_W1W2",                dR_W1W2)
    ("nJet",                   numJets)
    ("nGenMatchedJet_Hbb",     numJets_genMatched_to_Hbb)
    ("nGenMatchedJet_Wjj",     numJets_genMatched_to_Wjj)
    ("nBJetLoose",             numBJetsLoose)
    ("nBJetMedium",            numBJetsMedium)
    ("nLep",                   numLeptons)
    ("nGenJet_Hbb",            genBJets.size())
    ("nGenJet_Wjj",            genWJets.size())
    ("idxRow",                 idxRow)
    ("nRowsPerEvent",          numRowsPerEvent) 
    ("isGenMatched",           isGenMatched_value)
    ("evtWeight",              evtWeight)
        .fill();
}

/**
 * @brief Produce Ntuple for training a BDT to identify pairs of jets originating from W->jj decays
 */
int main(int argc,
         char ** argv)
{
//--- throw an exception in case ROOT encounters an error
  gErrorAbortLevel = kError;

//--- parse command-line arguments
  if ( argc < 2 )
  {
    std::cout << "Usage: " << argv[0] << " [parameters.py]\n";
    return EXIT_FAILURE;
  }

  std::cout << "<produceNtuple_HadWJetBDT>:\n";

//--- keep track of time it takes the macro to execute
  TBenchmark clock;
  clock.Start(argv[0]);

//--- read python configuration parameters
  if ( !edm::readPSetsFrom(argv[1])->existsAs<edm::ParameterSet>("process") )
    throw cms::Exception(argv[0])
      << "No ParameterSet 'process' found in configuration file = " << argv[1] << " !!\n";

  const edm::ParameterSet cfg               = edm::readPSetsFrom(argv[1])->getParameter<edm::ParameterSet>("process");
  const edm::ParameterSet cfg_analyze       = cfg.getParameter<edm::ParameterSet>("analyze_hadWTagger");
  const std::string treeName                = cfg_analyze.getParameter<std::string>("treeName");
  const std::string process_string          = cfg_analyze.getParameter<std::string>("process");
  const std::string selEventsFileName_input = cfg_analyze.getParameter<std::string>("selEventsFileName_input");
  const bool isDEBUG                        = cfg_analyze.getParameter<bool>("isDEBUG");

  const std::string mode_string             = cfg_analyze.getParameter<std::string>("mode");

  const bool isMC                           = cfg_analyze.getParameter<bool>("isMC");
  bool isMC_HH = isMC && process_string.find("hh_bbvv")!= std::string::npos;
  bool isMC_TT = isMC && process_string.find("TT")     != std::string::npos;
  bool hasLHE                               = cfg_analyze.getParameter<bool>("hasLHE");
  std::string central_or_shift              = "central";
  edm::VParameterSet lumiScale              = cfg_analyze.getParameter<edm::VParameterSet>("lumiScale");
  bool apply_genWeight                      = cfg_analyze.getParameter<bool>("apply_genWeight");

  const std::string branchName_electrons    = cfg_analyze.getParameter<std::string>("branchName_electrons");
  const std::string branchName_muons        = cfg_analyze.getParameter<std::string>("branchName_muons");
  const std::string branchName_jets_ak4     = cfg_analyze.getParameter<std::string>("branchName_jets_ak4");
  const std::string branchName_jets_ak8     = cfg_analyze.getParameter<std::string>("branchName_jets_ak8");
  const std::string branchName_subjets_ak8  = cfg_analyze.getParameter<std::string>("branchName_subjets_ak8");
  const std::string branchName_met          = cfg_analyze.getParameter<std::string>("branchName_met");

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

  std::string histogramDir = cfg_analyze.getParameter<std::string>("histogramDir");	

  const std::string era_string = cfg_analyze.getParameter<std::string>("era");
  const Era era = get_era(era_string);

  const std::string leptonSelection_string = cfg_analyze.getParameter<std::string>("leptonSelection");
  const int leptonSelection = get_selection(leptonSelection_string);

  std::cout << "selEventsFileName_input = " << selEventsFileName_input << '\n';
  RunLumiEventSelector* run_lumi_eventSelector = nullptr;
  if ( selEventsFileName_input != "" )
  {
    edm::ParameterSet cfgRunLumiEventSelector;
    cfgRunLumiEventSelector.addParameter<std::string>("inputFileName", selEventsFileName_input);
    cfgRunLumiEventSelector.addParameter<std::string>("separator", ":");
    run_lumi_eventSelector = new RunLumiEventSelector(cfgRunLumiEventSelector);
  }

  const fwlite::InputSource inputFiles(cfg);
  const int maxEvents        = inputFiles.maxEvents();
  const unsigned reportEvery = inputFiles.reportAfter();
  std::cout << " maxEvents = " << maxEvents << '\n';

  const fwlite::OutputFiles outputFile(cfg);
  fwlite::TFileService fs = fwlite::TFileService(outputFile.file().data());

  TTreeWrapper* inputTree = new TTreeWrapper(treeName.data(), inputFiles.files(), maxEvents);
  std::cout << "Loaded " << inputTree->getFileCount() << " file(s)\n";
  
//--- declare event-level variables
  EventInfo eventInfo;
  EventInfoReader eventInfoReader(&eventInfo);
  inputTree->registerReader(&eventInfoReader);

//--- declare particle collections
  const bool readGenObjects = isMC;
  RecoMuonReader* muonReader = new RecoMuonReader(era, branchName_muons, isMC, readGenObjects);
  inputTree->registerReader(muonReader);
  const RecoMuonCollectionSelectorLoose    preselMuonSelector  (era);
  const RecoMuonCollectionSelectorFakeable fakeableMuonSelector(era);
  const RecoMuonCollectionSelectorTight    tightMuonSelector   (era);
  
  RecoElectronReader* electronReader = new RecoElectronReader(era, branchName_electrons, isMC, readGenObjects);
  inputTree->registerReader(electronReader);
  const RecoElectronCollectionCleaner electronCleaner(0.3);
  const RecoElectronCollectionSelectorLoose    preselElectronSelector  (era);
  const RecoElectronCollectionSelectorFakeable fakeableElectronSelector(era);
  const RecoElectronCollectionSelectorTight    tightElectronSelector   (era);
  
  RecoJetReader* jetReaderAK4 = new RecoJetReader(era, isMC, branchName_jets_ak4, readGenObjects);
  jetReaderAK4->setPtMass_central_or_shift(kJetMET_central);
  jetReaderAK4->read_btag_systematics(false);
  inputTree->registerReader(jetReaderAK4);
  //RecoJetCollectionCleaner jetCleanerAK4_dR02(0.2, isDEBUG);
  RecoJetCollectionCleaner jetCleanerAK4_dR04(0.4, isDEBUG);
  RecoJetCollectionCleanerByIndex jetCleanerAK4_byIndex(isDEBUG);
  RecoJetCollectionCleaner jetCleanerAK4_dR08(0.8, isDEBUG);
  RecoJetCollectionCleaner jetCleanerAK4_dR12(1.2, isDEBUG);
  RecoJetCollectionSelector jetSelectorAK4_Hbb(era, -1, isDEBUG);
  RecoJetCollectionSelector jetSelectorAK4_Wjj(era, -1, isDEBUG);
  //jetSelectorAK4_Wjj.getSelector().set_max_absEta(4.7);
  jetSelectorAK4_Wjj.getSelector().set_max_absEta(2.4);
  RecoJetCollectionSelectorBtagLoose jetSelectorAK4_bTagLoose(era, -1, isDEBUG);
  RecoJetCollectionSelectorBtagMedium jetSelectorAK4_bTagMedium(era, -1, isDEBUG);

  RecoJetReaderAK8* jetReaderAK8 = new RecoJetReaderAK8(era, isMC, branchName_jets_ak8, branchName_subjets_ak8);
  inputTree->registerReader(jetReaderAK8);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR08(0.8, isDEBUG);
  RecoJetCollectionSelectorAK8_hh_bbWW_Hbb jetSelectorAK8_Hbb(era, -1, isDEBUG);

  RecoMEtReader* metReader = new RecoMEtReader(era, isMC, branchName_met);
  metReader->setMEt_central_or_shift(kJetMET_central);
  inputTree->registerReader(metReader);

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

  LHEInfoReader* lheInfoReader = new LHEInfoReader(hasLHE);
  inputTree->registerReader(lheInfoReader);

//--- book Ntuple for BDT training
  NtupleFillerBDT<float, int>* bdt_filler_oldHadWTagger = nullptr; 
  NtupleFillerBDT<float, int>* bdt_filler_jpa_4jet = nullptr;
  NtupleFillerBDT<float, int>* bdt_filler_missingBJet =nullptr;
  NtupleFillerBDT<float, int>* bdt_filler_missingWJet =nullptr;
  NtupleFillerBDT<float, int>* bdt_filler_missingBJet_missingWJet =nullptr;
  NtupleFillerBDT<float, int>* bdt_filler_missingAllWJet =nullptr;
  NtupleFillerBDT<float, int>* bdt_filler_missingBJet_missingAllWJet =nullptr;
  NtupleFillerBDT<float, int>* bdt_filler_boosted_missingWJet = nullptr;
  NtupleFillerBDT<float, int>* bdt_filler_boosted_2jet = nullptr;

  if      ( mode_string == "forBDTtraining_hadWTagger"      ) {
    bdt_filler_oldHadWTagger = createNtuple("oldHadWTagger", histogramDir, era_string, process_string);
    bdt_filler_oldHadWTagger->bookTree(fs);
  }
  else if ( mode_string == "forBDTtraining_jpa_4jet"      ) {
    bdt_filler_jpa_4jet = createNtuple("jpa_4jet", histogramDir, era_string, process_string);
    bdt_filler_jpa_4jet->bookTree(fs);
    bdt_filler_missingBJet = createNtuple("jpa_missingBJet", histogramDir, era_string, process_string);
    bdt_filler_missingBJet->bookTree(fs);
    bdt_filler_missingWJet = createNtuple("jpa_missingWJet", histogramDir, era_string, process_string);
    bdt_filler_missingWJet->bookTree(fs);
    bdt_filler_missingBJet_missingWJet = createNtuple("jpa_missingBJet_missingWJet", histogramDir, era_string, process_string);
    bdt_filler_missingBJet_missingWJet->bookTree(fs);
    bdt_filler_missingAllWJet = createNtuple("jpa_missingAllWJet", histogramDir, era_string, process_string);
    bdt_filler_missingAllWJet->bookTree(fs);
    bdt_filler_missingBJet_missingAllWJet = createNtuple("jpa_missingBJet_missingAllWJet", histogramDir, era_string, process_string);
    bdt_filler_missingBJet_missingAllWJet->bookTree(fs);
    bdt_filler_boosted_missingWJet = createNtuple("jpa_boosted_missingWJet", histogramDir, era_string, process_string);
    bdt_filler_boosted_missingWJet->bookTree(fs);
    bdt_filler_boosted_2jet = createNtuple("jpa_boosted_2jet", histogramDir, era_string, process_string);
    bdt_filler_boosted_2jet->bookTree(fs);
  }
  else throw cmsException(__func__)
	 << "Invalid Configuration parameter 'mode' = " << mode_string << "!!";

  int analyzedEntries = 0;
  int selectedEntries = 0;
  cutFlowTableType cutFlowTable;
  while ( inputTree->hasNextEvent() && (! run_lumi_eventSelector || (run_lumi_eventSelector && ! run_lumi_eventSelector -> areWeDone())) ) {
    if ( inputTree -> canReport(reportEvery) ) {
      std::cout << "processing Entry " << inputTree -> getCurrentMaxEventIdx()
                << " or " << inputTree -> getCurrentEventIdx() << " entry in #"
                << (inputTree -> getProcessedFileCount() - 1)
                << " (" << eventInfo
                << ") file (" << selectedEntries << " Entries selected)\n";
    }
    ++analyzedEntries;

    if ( isDEBUG ) {
      std::cout << "event #" << inputTree -> getCurrentMaxEventIdx() << ' ' << eventInfo << '\n';
    }

    EvtWeightRecorderHH evtWeightRecorder({ "central" }, central_or_shift, isMC);

    double evtWeight = 1.;
    if ( isMC )
    {
      if ( apply_genWeight ) evtWeightRecorder.record_genWeight(boost::math::sign(eventInfo.genWeight));
      lheInfoReader->read();
      evtWeightRecorder.record_lheScaleWeight(lheInfoReader);
      evtWeightRecorder.record_puWeight(&eventInfo);
      evtWeightRecorder.record_lumiScale(lumiScale);
      evtWeight = evtWeightRecorder.get_inclusive(central_or_shift);
    }

    if ( run_lumi_eventSelector && !(*run_lumi_eventSelector)(eventInfo) ) continue;
    cutFlowTable.update("run:ls:event selection", evtWeight);

    if ( run_lumi_eventSelector ) {
      std::cout << "processing Entry #" << inputTree->getCumulativeMaxEventCount() << ": " << eventInfo << std::endl;
      if ( inputTree -> isOpen() ) {
        std::cout << "input File = " << inputTree->getCurrentFileName() << std::endl;
      }
    }
    
//--- build collections of electrons, muons and hadronic taus;
//    resolve overlaps in order of priority: muon, electron,
    const std::vector<RecoMuon> muons = muonReader->read();
    const std::vector<const RecoMuon *> muon_ptrs = convert_to_ptrs(muons);
    // CV: no cleaning needed for muons, as they have the highest priority in the overlap removal
    const std::vector<const RecoMuon *> cleanedMuons  = muon_ptrs;
    const std::vector<const RecoMuon *> preselMuons   = preselMuonSelector  (cleanedMuons,  isHigherConePt);
    const std::vector<const RecoMuon *> fakeableMuons = fakeableMuonSelector(preselMuons,   isHigherConePt);
    const std::vector<const RecoMuon *> tightMuons    = tightMuonSelector   (fakeableMuons, isHigherConePt);
    const std::vector<const RecoMuon *> selMuons      = selectObjects(
      leptonSelection, preselMuons, fakeableMuons, tightMuons
    );
    if ( isDEBUG )
    {
      printCollection("selMuons", selMuons);
    }

    const std::vector<RecoElectron> electrons = electronReader->read();
    const std::vector<const RecoElectron *> electron_ptrs     = convert_to_ptrs(electrons);
    const std::vector<const RecoElectron *> cleanedElectrons  = electronCleaner(electron_ptrs, fakeableMuons);
    const std::vector<const RecoElectron *> preselElectronsUncleaned = preselElectronSelector  (electron_ptrs,     isHigherConePt);
    const std::vector<const RecoElectron *> preselElectrons          = preselElectronSelector  (cleanedElectrons,  isHigherConePt);
    const std::vector<const RecoElectron *> fakeableElectrons        = fakeableElectronSelector(preselElectrons,   isHigherConePt);
    const std::vector<const RecoElectron *> tightElectrons           = tightElectronSelector   (fakeableElectrons, isHigherConePt);
    const std::vector<const RecoElectron *> selElectrons             = selectObjects(
      leptonSelection, preselElectrons, fakeableElectrons, tightElectrons
    );
    if ( isDEBUG )
    {
      printCollection("selElectrons", selElectrons);
    }

    const std::vector<const RecoLepton*> preselLeptons = mergeLeptonCollections(preselElectrons, preselMuons, isHigherConePt);
    const std::vector<const RecoLepton*> fakeableLeptons = mergeLeptonCollections(fakeableElectrons, fakeableMuons, isHigherConePt);
    const std::vector<const RecoLepton*> tightLeptons = mergeLeptonCollections(tightElectrons, tightMuons, isHigherConePt);
    const std::vector<const RecoLepton*> selLeptons = mergeLeptonCollections(selElectrons, selMuons, isHigherConePt);	

    // require at least one lepton passing fakeable or tight selection criteria
    // (fakeable lepton selection applied in fake background control region,
    //  tight lepton selection applied in signal region)
    if ( !(selLeptons.size() >= 1) ) {
      continue;
    }
    cutFlowTable.update(">= 1 sel leptons", evtWeight);
    const RecoLepton* selLepton = selLeptons[0];

    const double minPt_lead = 25.;
    if ( !(selLepton->cone_pt() > minPt_lead) ) {
      continue;
    }
    cutFlowTable.update("lepton pT > 25 GeV", evtWeight);

    // require exactly one lepton passing tight selection criteria, to avoid overlap with other channels
    if ( !(tightLeptons.size() <= 1) ) {
      continue;
    }
    cutFlowTable.update("<= 1 tight leptons", evtWeight);
//--- build collections of jets 
    const std::vector<RecoJet> jets_ak4 = jetReaderAK4->read();
    const std::vector<const RecoJet*> jet_ptrs_ak4 = convert_to_ptrs(jets_ak4);
    std::vector<const RecoJet*> cleanedJetsAK4_wrtLeptons = jetCleaningByIndex ?
      jetCleanerAK4_byIndex(jet_ptrs_ak4, fakeableLeptons) :
      jetCleanerAK4_dR04   (jet_ptrs_ak4, fakeableLeptons)
      //jetCleanerAK4_dR02   (jet_ptrs_ak4, fakeableLeptons)
    ;
    const std::vector<const RecoJet*> selBJetsAK4_loose = jetSelectorAK4_bTagLoose(cleanedJetsAK4_wrtLeptons, isHigherPt);
    const std::vector<const RecoJet*> selBJetsAK4_medium = jetSelectorAK4_bTagMedium(cleanedJetsAK4_wrtLeptons, isHigherPt);
   
    const std::vector<RecoJetAK8> jets_ak8 = jetReaderAK8->read();
    const std::vector<const RecoJetAK8*> jet_ptrs_ak8 = convert_to_ptrs(jets_ak8);

    RecoMEt met = metReader->read();
    const Particle::LorentzVector& metP4 = met.p4();

    //-------------------------------------------------------------------
    // select the two jets from the H->bb decay from either the AK4 (resolved H->bb) or AK8 (boosted H->bb) collection
    //
    // WARNING: logic to select the two jets from H->bb decay 
    //          needs to match the code in analyze_hh_bb1l.cc !!
    const std::vector<const RecoJetAK8*> cleanedJetsAK8_wrtLeptons = jetCleanerAK8_dR08(jet_ptrs_ak8, fakeableLeptons);
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
    /*if ( !(selJet1_Hbb && selJet2_Hbb) ) 
    {
      continue;
    }
    cutFlowTable.update(">= 2 jets from H->bb", evtWeight);*/
    //-------------------------------------------------------------------

    //-------------------------------------------------------------------
    // select jets from W->jj decay
    //
    // WARNING: logic to clean the AK4 jets with respect to jets from the H->bb decay 
    //          needs to match the code in jetSelectionAuxFunctions.cc !!
    std::vector<const RecoJet*> cleanedJetsAK4_wrtHbb;
    if ( selJetAK8_Hbb ) 
    {
      const std::vector<const RecoJetAK8*> overlaps = { selJetAK8_Hbb };
      cleanedJetsAK4_wrtHbb = jetCleanerAK4_dR12(cleanedJetsAK4_wrtLeptons, overlaps);
    } 
    else 
    {
      std::vector<const RecoJetBase*> overlaps;
      if ( selJet1_Hbb ) overlaps.push_back(selJet1_Hbb);
      if ( selJet2_Hbb ) overlaps.push_back(selJet2_Hbb);
      cleanedJetsAK4_wrtHbb = jetCleanerAK4_dR08(cleanedJetsAK4_wrtLeptons, overlaps);
    }
    const std::vector<const RecoJet*> selJetsAK4_Wjj = jetSelectorAK4_Wjj(cleanedJetsAK4_wrtHbb, isHigherPt);
    /*if ( !(selJetsAK4_Wjj.size() >= 2) ) {
      continue;
    }
    cutFlowTable.update(">= 2 jets from W->jj", evtWeight);*/
    //-------------------------------------------------------------------

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
    std::vector<const GenLepton*> genLeptons_ptrs = convert_to_ptrs(genLeptons);
    std::vector<GenJet> genBJets = genParticleMatcher->getBJets();
    std::vector<const GenJet*> genBJets_ptrs = convert_to_ptrs(genBJets);
    std::vector<GenJet> genWJets = genParticleMatcher->getWJets();
    std::vector<const GenJet*> genWJets_ptrs = convert_to_ptrs(genWJets);
    //const Particle::LorentzVector& genMEtP4 = genParticleMatcher->getMEt();
    if ( !(genLeptons.size() == 1) ) {
      continue;
    }
    cutFlowTable.update("exactly 1 gen-lepton", evtWeight);

    bool Hbb_isBoosted = ( selJetAK8_Hbb ) ? true : false;
    int numJetsAK4_genMatched_to_Hbb = (int)countGenMatchedJets(cleanedJetsAK4_wrtLeptons, genBJets_ptrs);
    int numJetsAK4_genMatched_to_Wjj = (int)countGenMatchedJets(cleanedJetsAK4_wrtLeptons, genWJets_ptrs);
    int numLeptons = (int)preselLeptons.size();
    std::pair<int, int> matchedJets_ = matchedJets(cleanedJetsAK4_wrtLeptons, genBJets_ptrs, genWJets_ptrs);
    if ( !Hbb_isBoosted ) h_genmatch->Fill(matchedJets_.first, matchedJets_.second);
    int mode = kMode_undefined;
    if      ( mode_string == "forBDTtraining_hadWTagger"      ) mode = kMode_hadWTagger;
    else if ( mode_string == "forBDTtraining_jpa_4jet"        ) {
      if ( matchedJets_.first ==2 && matchedJets_.second ==2 ) {
	mode = kMode_jpa_4jet;
      }
      else if ( matchedJets_.first ==1 && matchedJets_.second ==2 ) {
	mode = kMode_jpa_missingBJet;
      }
      else if ( matchedJets_.first ==2 && matchedJets_.second ==1 ) {
	mode = kMode_jpa_missingWJet;
      }
      else if ( matchedJets_.first ==1 && matchedJets_.second ==1) {
	mode = kMode_jpa_missingBJet_missingWJet;
      }
      else if ( matchedJets_.first ==2 && matchedJets_.second ==0) {
        mode = kMode_jpa_missingAllWJet;
      }
      else if ( matchedJets_.first ==1 && matchedJets_.second ==0) {
        mode = kMode_jpa_missingBJet_missingAllWJet;
      }
      else {
	mode = kMode_jpa_restOfcat;
      }
    }
    else throw cmsException(__func__)
	   << "Invalid Configuration parameter 'mode' = " << mode << "!!";

    if ( Hbb_isBoosted ) {
      std::pair<int, int> HbbBoosted_matchedJets_ = matchedJets(selJetsAK4_Wjj, genBJets_ptrs, genWJets_ptrs, true);
      //h_genmatch->Fill(matchedJets_.second);
      if ( HbbBoosted_matchedJets_.second ==1 ) {
	int idxRow = 0;
	double numRowsPerEvent = selJetsAK4_Wjj.size();
	for ( std::vector<const RecoJet*>::const_iterator selJet_Wjj = selJetsAK4_Wjj.begin();
	      selJet_Wjj != selJetsAK4_Wjj.end(); ++selJet_Wjj ) {
	  writeToNtuple(
	     *bdt_filler_boosted_missingWJet,
	     eventInfo,
	     selLepton, genLeptons_ptrs,
	     metP4,
	     selJetAK8_Hbb->subJet1(), selJetAK8_Hbb->subJet2(), true, genBJets_ptrs,
	     *selJet_Wjj, nullptr, genWJets_ptrs,
	     cleanedJetsAK4_wrtLeptons.size(), 0, numJetsAK4_genMatched_to_Wjj, selBJetsAK4_loose.size(), selBJetsAK4_medium.size(), numLeptons,
	     idxRow, numRowsPerEvent,
	     isGenMatched((*selJet_Wjj)->eta(), (*selJet_Wjj)->phi(), genWJets_ptrs),
	     evtWeight);
	  ++idxRow;
	}
      }
      else if ( HbbBoosted_matchedJets_.second == 2 ) {
	int idxRow = 0;
	double numRowsPerEvent = 0.5*selJetsAK4_Wjj.size()*(selJetsAK4_Wjj.size() - 1);
	for ( std::vector<const RecoJet*>::const_iterator selJet1_Wjj = selJetsAK4_Wjj.begin();
	      selJet1_Wjj != selJetsAK4_Wjj.end(); ++selJet1_Wjj ) {
	  for ( std::vector<const RecoJet*>::const_iterator selJet2_Wjj = selJet1_Wjj + 1;
		selJet2_Wjj != selJetsAK4_Wjj.end(); ++selJet2_Wjj ) {
	    assert((*selJet1_Wjj)->pt() >= (*selJet2_Wjj)->pt());
	    writeToNtuple(
	      *bdt_filler_boosted_2jet,
	      eventInfo,
	      selLepton, genLeptons_ptrs,
	      metP4,
	      selJetAK8_Hbb->subJet1(), selJetAK8_Hbb->subJet2(), Hbb_isBoosted, genBJets_ptrs,
	      *selJet1_Wjj, *selJet2_Wjj, genWJets_ptrs,
	      cleanedJetsAK4_wrtLeptons.size(), numJetsAK4_genMatched_to_Hbb, numJetsAK4_genMatched_to_Wjj, selBJetsAK4_loose.size(), selBJetsAK4_medium.size(), numLeptons,
	      idxRow, numRowsPerEvent,
	      isGenMatched((*selJet1_Wjj)->eta(), (*selJet1_Wjj)->phi(), genWJets_ptrs) &&
	      isGenMatched((*selJet2_Wjj)->eta(), (*selJet2_Wjj)->phi(), genWJets_ptrs),
	      evtWeight);
	    ++idxRow;
	  }
	}
      }
    }

    if ( mode == kMode_hadWTagger )
    {
      int idxRow = 0;
      double numRowsPerEvent = 0.5*selJetsAK4_Wjj.size()*(selJetsAK4_Wjj.size() - 1);
      for ( std::vector<const RecoJet*>::const_iterator selJet1_Wjj = selJetsAK4_Wjj.begin();
	    selJet1_Wjj != selJetsAK4_Wjj.end(); ++selJet1_Wjj ) {
        for ( std::vector<const RecoJet*>::const_iterator selJet2_Wjj = selJet1_Wjj + 1;
     	      selJet2_Wjj != selJetsAK4_Wjj.end(); ++selJet2_Wjj ) {
          assert((*selJet1_Wjj)->pt() >= (*selJet2_Wjj)->pt());        
          writeToNtuple(
           *bdt_filler_oldHadWTagger,
            eventInfo,
            selLepton, genLeptons_ptrs,
            metP4,
            selJet1_Hbb, selJet2_Hbb, Hbb_isBoosted, genBJets_ptrs, 
            *selJet1_Wjj, *selJet2_Wjj, genWJets_ptrs,
            cleanedJetsAK4_wrtLeptons.size(), numJetsAK4_genMatched_to_Hbb, numJetsAK4_genMatched_to_Wjj, selBJetsAK4_loose.size(), selBJetsAK4_medium.size(), numLeptons,
            idxRow, numRowsPerEvent,
            isGenMatched(selJet1_Hbb->eta(), selJet1_Hbb->phi(), genBJets_ptrs) && 
            isGenMatched(selJet2_Hbb->eta(), selJet2_Hbb->phi(), genBJets_ptrs) && 
            isGenMatched((*selJet1_Wjj)->eta(), (*selJet1_Wjj)->phi(), genWJets_ptrs) && 
            isGenMatched((*selJet2_Wjj)->eta(), (*selJet2_Wjj)->phi(), genWJets_ptrs),
            evtWeight);
          ++idxRow;
        }
      }
    }
    else if ( mode == kMode_jpa_4jet ) 
    {
      int idxRow = 0;
      double numRowsPerEvent = 0.5*cleanedJetsAK4_wrtLeptons.size()*(cleanedJetsAK4_wrtLeptons.size() - 1)
	*0.5*(cleanedJetsAK4_wrtLeptons.size() - 2)*(cleanedJetsAK4_wrtLeptons.size() - 3);
      for ( std::vector<const RecoJet*>::const_iterator selBJet1 = cleanedJetsAK4_wrtLeptons.begin();
            selBJet1 != cleanedJetsAK4_wrtLeptons.end(); ++selBJet1 ) {
        for ( std::vector<const RecoJet*>::const_iterator selBJet2 = selBJet1 + 1;
              selBJet2 != cleanedJetsAK4_wrtLeptons.end(); ++selBJet2 ) {
          assert((*selBJet1)->pt() >= (*selBJet2)->pt());
          for ( std::vector<const RecoJet*>::const_iterator selWJet1 = cleanedJetsAK4_wrtLeptons.begin();
                selWJet1 != cleanedJetsAK4_wrtLeptons.end(); ++selWJet1 ) {            
            for ( std::vector<const RecoJet*>::const_iterator selWJet2 = selWJet1 + 1;
	          selWJet2 != cleanedJetsAK4_wrtLeptons.end(); ++selWJet2 ) {
              assert((*selWJet1)->pt() >= (*selWJet2)->pt());
              if ( deltaR((*selWJet1)->p4(), (*selBJet1)->p4()) < 0.3 || deltaR((*selWJet1)->p4(), (*selBJet2)->p4()) < 0.3 ) continue;
              if ( deltaR((*selWJet2)->p4(), (*selBJet1)->p4()) < 0.3 || deltaR((*selWJet2)->p4(), (*selBJet2)->p4()) < 0.3 ) continue;
              writeToNtuple(
               *bdt_filler_jpa_4jet,
                eventInfo,
                selLepton, genLeptons_ptrs,
                metP4,
                *selBJet1, *selBJet2, Hbb_isBoosted, genBJets_ptrs, 
                *selWJet1, *selWJet2, genWJets_ptrs,
                cleanedJetsAK4_wrtLeptons.size(), numJetsAK4_genMatched_to_Hbb, numJetsAK4_genMatched_to_Wjj, selBJetsAK4_loose.size(), selBJetsAK4_medium.size(), numLeptons,
                idxRow, numRowsPerEvent,
                isGenMatched((*selBJet1)->eta(), (*selBJet1)->phi(), genBJets_ptrs) && 
                isGenMatched((*selBJet2)->eta(), (*selBJet2)->phi(), genBJets_ptrs) && 
                isGenMatched((*selWJet1)->eta(), (*selWJet1)->phi(), genWJets_ptrs) && 
                isGenMatched((*selWJet2)->eta(), (*selWJet2)->phi(), genWJets_ptrs),
                evtWeight);
	      ++idxRow;
	    }
          }
        }
      }
    }
    else if ( mode == kMode_jpa_missingBJet )
    {
      int idxRow = 0;
      double numRowsPerEvent = cleanedJetsAK4_wrtLeptons.size()
        *0.5*(cleanedJetsAK4_wrtLeptons.size() - 1)*(cleanedJetsAK4_wrtLeptons.size() - 2);
      for ( std::vector<const RecoJet*>::const_iterator selBJet1 = cleanedJetsAK4_wrtLeptons.begin();
            selBJet1 != cleanedJetsAK4_wrtLeptons.end(); ++selBJet1 ) {
        for ( std::vector<const RecoJet*>::const_iterator selWJet1 = cleanedJetsAK4_wrtLeptons.begin();
              selWJet1 != cleanedJetsAK4_wrtLeptons.end(); ++selWJet1 ) {            
          for ( std::vector<const RecoJet*>::const_iterator selWJet2 = selWJet1 + 1;
	        selWJet2 != cleanedJetsAK4_wrtLeptons.end(); ++selWJet2 ) {
            assert((*selWJet1)->pt() >= (*selWJet2)->pt());
            if ( deltaR((*selWJet1)->p4(), (*selBJet1)->p4()) < 0.3 ) continue;
            if ( deltaR((*selWJet2)->p4(), (*selBJet1)->p4()) < 0.3 ) continue;
            writeToNtuple(
             *bdt_filler_missingBJet,
              eventInfo,
              selLepton, genLeptons_ptrs,
              metP4,
              *selBJet1, nullptr, Hbb_isBoosted, genBJets_ptrs, 
              *selWJet1, *selWJet2, genWJets_ptrs,
              cleanedJetsAK4_wrtLeptons.size(), numJetsAK4_genMatched_to_Hbb, numJetsAK4_genMatched_to_Wjj, selBJetsAK4_loose.size(), selBJetsAK4_medium.size(), numLeptons,
              idxRow, numRowsPerEvent,
              isGenMatched((*selBJet1)->eta(), (*selBJet1)->phi(), genBJets_ptrs) && 
              isGenMatched((*selWJet1)->eta(), (*selWJet1)->phi(), genWJets_ptrs) && 
              isGenMatched((*selWJet2)->eta(), (*selWJet2)->phi(), genWJets_ptrs),
              evtWeight);
            ++idxRow;
          }
        }
      }
    }
    else if ( mode == kMode_jpa_missingWJet )
    {
      int idxRow = 0;
      double numRowsPerEvent = 0.5*cleanedJetsAK4_wrtLeptons.size()*(cleanedJetsAK4_wrtLeptons.size() - 1)
        *(cleanedJetsAK4_wrtLeptons.size() - 2);
      for ( std::vector<const RecoJet*>::const_iterator selBJet1 = cleanedJetsAK4_wrtLeptons.begin();
            selBJet1 != cleanedJetsAK4_wrtLeptons.end(); ++selBJet1 ) {
        for ( std::vector<const RecoJet*>::const_iterator selBJet2 = selBJet1 + 1;
              selBJet2 != cleanedJetsAK4_wrtLeptons.end(); ++selBJet2 ) {
          assert((*selBJet1)->pt() >= (*selBJet2)->pt());
          for ( std::vector<const RecoJet*>::const_iterator selWJet1 = cleanedJetsAK4_wrtLeptons.begin();
                selWJet1 != cleanedJetsAK4_wrtLeptons.end(); ++selWJet1 ) {            
            if ( deltaR((*selWJet1)->p4(), (*selBJet1)->p4()) < 0.3 || deltaR((*selWJet1)->p4(), (*selBJet2)->p4()) < 0.3 ) continue;
            writeToNtuple(
             *bdt_filler_missingWJet,
              eventInfo,
              selLepton, genLeptons_ptrs,
              metP4,
              *selBJet1, *selBJet2, Hbb_isBoosted, genBJets_ptrs, 
              *selWJet1, nullptr, genWJets_ptrs,
              cleanedJetsAK4_wrtLeptons.size(), numJetsAK4_genMatched_to_Hbb, numJetsAK4_genMatched_to_Wjj, selBJetsAK4_loose.size(), selBJetsAK4_medium.size(), numLeptons,
              idxRow, numRowsPerEvent,
              isGenMatched((*selBJet1)->eta(), (*selBJet1)->phi(), genBJets_ptrs) && 
              isGenMatched((*selBJet2)->eta(), (*selBJet2)->phi(), genBJets_ptrs) && 
              isGenMatched((*selWJet1)->eta(), (*selWJet1)->phi(), genWJets_ptrs),
              evtWeight);
            ++idxRow;
          }
        }
      }
    } 
    else if ( mode == kMode_jpa_missingBJet_missingWJet ) {
      int idxRow = 0;
      double numRowsPerEvent = cleanedJetsAK4_wrtLeptons.size()*(cleanedJetsAK4_wrtLeptons.size() - 1);
      for ( std::vector<const RecoJet*>::const_iterator selBJet = cleanedJetsAK4_wrtLeptons.begin();
	    selBJet != cleanedJetsAK4_wrtLeptons.end(); ++selBJet ) {
	for ( std::vector<const RecoJet*>::const_iterator selWJet = cleanedJetsAK4_wrtLeptons.begin();
	      selWJet != cleanedJetsAK4_wrtLeptons.end(); ++selWJet ) {
	  if ( (*selWJet)->eta() == (*selBJet)->eta() && (*selWJet)->phi() == (*selBJet)->phi() )  continue;
	  writeToNtuple(
	     *bdt_filler_missingBJet_missingWJet,
	     eventInfo,
	     selLepton, genLeptons_ptrs,
	     metP4,
	     *selBJet, nullptr, Hbb_isBoosted, genBJets_ptrs,
	     *selWJet, nullptr, genWJets_ptrs,
	     cleanedJetsAK4_wrtLeptons.size(), numJetsAK4_genMatched_to_Hbb, numJetsAK4_genMatched_to_Wjj, selBJetsAK4_loose.size(), selBJetsAK4_medium.size(), numLeptons,
	     idxRow, numRowsPerEvent,
	     isGenMatched((*selBJet)->eta(), (*selBJet)->phi(), genBJets_ptrs) &&
	     isGenMatched((*selWJet)->eta(), (*selWJet)->phi(), genWJets_ptrs),
	     evtWeight);
	  ++idxRow;
	}
      }
    }
    else if ( mode == kMode_jpa_missingAllWJet ) {
      int idxRow = 0;
      double numRowsPerEvent = 0.5*cleanedJetsAK4_wrtLeptons.size()*(cleanedJetsAK4_wrtLeptons.size() - 1);
      for ( std::vector<const RecoJet*>::const_iterator selBJet1 = cleanedJetsAK4_wrtLeptons.begin();
	    selBJet1 != cleanedJetsAK4_wrtLeptons.end(); ++selBJet1 ) {
	for ( std::vector<const RecoJet*>::const_iterator selBJet2 = selBJet1+1;
	      selBJet2 != cleanedJetsAK4_wrtLeptons.end(); ++selBJet2 ) {
	  assert((*(selBJet1))->pt() >= (*(selBJet2))->pt());
	  writeToNtuple(
            *bdt_filler_missingAllWJet,
	    eventInfo,
	    selLepton, genLeptons_ptrs,
	    metP4,
	    *selBJet1, *selBJet2, Hbb_isBoosted, genBJets_ptrs,
	    nullptr, nullptr, genWJets_ptrs,
	    cleanedJetsAK4_wrtLeptons.size(), numJetsAK4_genMatched_to_Hbb, numJetsAK4_genMatched_to_Wjj, selBJetsAK4_loose.size(), selBJetsAK4_medium.size(), numLeptons,
	    idxRow, numRowsPerEvent,
	    isGenMatched((*selBJet1)->eta(), (*selBJet1)->phi(), genBJets_ptrs) &&
	    isGenMatched((*selBJet2)->eta(), (*selBJet2)->phi(), genBJets_ptrs) ,
	    evtWeight);
	  ++idxRow;
	} 
      }
    }
    else if ( mode == kMode_jpa_missingBJet_missingAllWJet ) {
      int idxRow = 0;
      double numRowsPerEvent = cleanedJetsAK4_wrtLeptons.size();
      for ( std::vector<const RecoJet*>::const_iterator selBJet = cleanedJetsAK4_wrtLeptons.begin();
	    selBJet != cleanedJetsAK4_wrtLeptons.end(); ++selBJet ) {
	writeToNtuple(
	   *bdt_filler_missingBJet_missingAllWJet,
	   eventInfo,
	   selLepton, genLeptons_ptrs,
	   metP4,
	   *selBJet, nullptr, Hbb_isBoosted, genBJets_ptrs,
	   nullptr, nullptr, genWJets_ptrs,
	   cleanedJetsAK4_wrtLeptons.size(), numJetsAK4_genMatched_to_Hbb, numJetsAK4_genMatched_to_Wjj, selBJetsAK4_loose.size(), selBJetsAK4_medium.size(), numLeptons,
	   idxRow, numRowsPerEvent,
	   isGenMatched((*selBJet)->eta(), (*selBJet)->phi(), genBJets_ptrs),
	   evtWeight);
	++idxRow;
      }
      }
    else if ( mode == kMode_jpa_restOfcat ) {
      continue;
    }
    else {
      assert(0);
    }
    ++selectedEntries;
  } // idxEntry

  std::cout << "max num. Entries = " << inputTree -> getCumulativeMaxEventCount()
            << " (limited by " << maxEvents << ") processed in "
            << inputTree -> getProcessedFileCount() << " file(s) (out of "
            << inputTree -> getFileCount() << ")\n"
            << " analyzed = " << analyzedEntries << '\n'
            << " selected = " << selectedEntries << "\n\n"
            << "cut-flow table" << std::endl;
  fs.file().cd();
  h_genmatch->Write();
  //  delete h_genmatch;
  delete run_lumi_eventSelector;
  delete muonReader;
  delete electronReader;
  delete jetReaderAK4;
  delete jetReaderAK8;

  delete inputTree;

  clock.Show("analyze_hadWTagger");

  return EXIT_SUCCESS;
}
