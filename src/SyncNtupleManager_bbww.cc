#include "hhAnalysis/bbww/interface/SyncNtupleManager_bbww.h"

#include "tthAnalysis/HiggsToTauTau/interface/RecoMuon.h" // RecoMuon
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectron.h" // RecoElectron
#include "tthAnalysis/HiggsToTauTau/interface/RecoJet.h" // RecoJet
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetAK8.h" // RecoJetAK8
#include "tthAnalysis/HiggsToTauTau/interface/hltPath.h" // hltPath
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // as_integer()

#include <TFile.h> // TFile

#include <boost/algorithm/string/predicate.hpp> // boost::starts_with()

#include <algorithm> // std::min()

const Int_t SyncNtupleManager_bbww::placeholder_value = -9999;

SyncNtupleManager_bbww::SyncNtupleManager_bbww(const std::string & outputFileName,
                                               const std::string & outputTreeName)
  : outputFile(new TFile(outputFileName.c_str(), "recreate"))
  , outputDir(nullptr)
  , outputTree(nullptr)
  , nof_mus(2)
  , nof_eles(2)
  , nof_jets(4)
  , nof_jetsAk8(2)
  , nof_jetsAk8LS(2)
{
  std::string outputDirName_;
  std::string outputTreeName_ = outputTreeName;
  const auto nofSlashes = std::count(outputTreeName.cbegin(), outputTreeName.cend(), '/');
  if(nofSlashes == 1)
  {
    const std::size_t slashPos = outputTreeName.find('/');
    outputDirName_ = outputTreeName.substr(0, slashPos);
    outputTreeName_ = outputTreeName.substr(slashPos + 1);
  }
  else if(nofSlashes > 1)
  {
    throw cmsException(this) << "Invalid name for TTree = " << outputTreeName;
  }

  if(! outputDirName_.empty())
  {
    outputDir = outputFile->mkdir(outputDirName_.c_str());
    outputDir -> cd();
  }

  outputTree = new TTree(outputTreeName_.c_str(), outputTreeName_.c_str());
  if(outputDir)
  {
    outputTree->SetDirectory(outputDir);
  }
  for(int var = as_integer(FloatVariableType_bbww::PFMET); var <= as_integer(FloatVariableType_bbww::MC_weight); ++var)
  {
    floatMap[static_cast<FloatVariableType_bbww>(var)] = placeholder_value;
  }
}

SyncNtupleManager_bbww::~SyncNtupleManager_bbww()
{
  outputFile -> Close();
  delete outputFile;
  outputTree = nullptr;
  outputDir = nullptr;
  outputFile = nullptr;
}

void
SyncNtupleManager_bbww::initializeBranches()
{
  const char * lstr = "lep";
  const char * mstr = "mu";
  const char * estr = "ele";
  const char * jstr = "ak4Jet";
  const char * jstrAk8 = "ak8Jet";
  const char * jstrAk8Ls = "ak8lsJet";

  const std::string n_sel_lep_str         = Form("n_%s",             lstr);
  const std::string n_presel_mu_str       = Form("n_presel_%s",      mstr);
  const std::string n_presel_ele_str      = Form("n_presel_%s",      estr);
  const std::string n_presel_jet_str      = Form("n_presel_%s",      jstr);

  setBranches(
    nEvent,            "event",
    ls,                "ls",
    run,               "run",
    n_presel_mu,       n_presel_mu_str,
    n_presel_ele,      n_presel_ele_str,
    n_presel_jet,      n_presel_jet_str,

//--- MET/MHT
    floatMap[FloatVariableType_bbww::PFMET],                    "PFMET",
    floatMap[FloatVariableType_bbww::PFMETphi],                 "PFMETphi",
    floatMap[FloatVariableType_bbww::PU_weight],                "PU_weight",
    floatMap[FloatVariableType_bbww::MC_weight],                "MC_weight"
  );

  setBranches(
    mstr, nof_mus,
    mu_pt,                   "pt",
    mu_eta,                  "eta",
    mu_phi,                  "phi",
    mu_E,                    "E",
    mu_charge,               "charge",
    mu_miniRelIso,           "miniRelIso",
    mu_sip3D,                "sip3D",
    mu_dxyAbs,               "dxyAbs",
    mu_dxy,                  "dxy",
    mu_dz,                   "dz",
    mu_segmentCompatibility, "segmentCompatibility",
    mu_leptonMVA,            "leptonMVA",
    mu_mediumID,             "mediumID"
  );

  setBranches(
    estr, nof_eles,
    ele_pt,                   "pt",
    ele_eta,                  "eta",
    ele_phi,                  "phi",
    ele_E,                    "E",
    ele_charge,               "charge",
    ele_miniRelIso,           "miniRelIso",
    ele_sip3D,                "sip3D",
    ele_dxyAbs,               "dxyAbs",
    ele_dxy,                  "dxy",
    ele_dz,                   "dz",
    ele_ntMVAeleID,           "ntMVAeleID",
    ele_leptonMVA,            "leptonMVA"
  );

  setBranches(
    jstr, nof_jets,
    jet_pt,           "pt",
    jet_eta,          "eta",
    jet_phi,          "phi",
    jet_E,            "E",
    jet_CSV,          "CSV"
  );

  setBranches(
    jstrAk8, nof_jetsAk8,
    jetAk8_pt,          "pt",
    jetAk8_eta,         "eta",
    jetAk8_phi,         "phi",
    jetAk8_E,           "E",
    jetAk8_msoftdrop,   "msoftdrop",
    jetAk8_tau1,        "tau1",
    jetAk8_tau2,        "tau2",
    jetAk8_subjet0_pt,  "subjet0_pt",
    jetAk8_subjet0_eta, "subjet0_eta",
    jetAk8_subjet0_phi, "subjet0_phi",
    jetAk8_subjet0_CSV, "subjet0_CSV",
    jetAk8_subjet1_pt,  "subjet1_pt",
    jetAk8_subjet1_eta, "subjet1_eta",
    jetAk8_subjet1_phi, "subjet1_phi",
    jetAk8_subjet1_CSV, "subjet1_CSV"
  );

  setBranches(
    jstrAk8Ls, nof_jetsAk8,
    jetAk8Ls_pt,          "pt",
    jetAk8Ls_eta,         "eta",
    jetAk8Ls_phi,         "phi",
    jetAk8Ls_E,           "E",
    jetAk8Ls_msoftdrop,   "msoftdrop",
    jetAk8Ls_tau1,        "tau1",
    jetAk8Ls_tau2,        "tau2",
    jetAk8Ls_subjet0_pt,  "subjet0_pt",
    jetAk8Ls_subjet0_eta, "subjet0_eta",
    jetAk8Ls_subjet0_phi, "subjet0_phi",
    jetAk8Ls_subjet0_CSV, "subjet0_CSV",
    jetAk8Ls_subjet1_pt,  "subjet1_pt",
    jetAk8Ls_subjet1_eta, "subjet1_eta",
    jetAk8Ls_subjet1_phi, "subjet1_phi",
    jetAk8Ls_subjet1_CSV, "subjet1_CSV"
  );

  reset();
}

void
SyncNtupleManager_bbww::initializeHLTBranches(const std::vector<std::vector<hltPath *>> & hltPaths)
{
  for(const auto & hltVector: hltPaths)
  {
    for(const auto & hlt: hltVector)
    {
      hltMap[hlt -> getBranchName()] = -1;
    }
  }
  for(auto & kv: hltMap)
  {
    setBranches(hltMap[kv.first], kv.first);
  }
}

void
SyncNtupleManager_bbww::read(const EventInfo & eventInfo)
{
  run = eventInfo.run;
  ls = eventInfo.lumi;
  nEvent = eventInfo.event;
}

void
SyncNtupleManager_bbww::read(const std::vector<const RecoMuon *> & muons)
{
  n_presel_mu = muons.size();

  const Int_t nof_iterations = std::min(n_presel_mu, nof_mus);
  for(Int_t i = 0; i < nof_iterations; ++i)
  {
    const RecoMuon * const muon = muons[i];
    mu_pt[i] = muon -> pt();
    mu_eta[i] = muon -> eta();
    mu_phi[i] = muon -> phi();
    mu_E[i] = (muon -> p4()).E();
    mu_charge[i] = muon -> charge();
    mu_miniRelIso[i] = muon -> relIso();
    mu_sip3D[i] = muon -> sip3d();
    mu_dxyAbs[i] = std::fabs(muon -> dxy());
    mu_dxy[i] = muon -> dxy();
    mu_dz[i] = muon -> dz();
    mu_segmentCompatibility[i] = muon -> segmentCompatibility();
    mu_leptonMVA[i] = muon -> mvaRawTTH();
    mu_mediumID[i] = muon -> passesMediumIdPOG();
  }
}

void
SyncNtupleManager_bbww::read(const std::vector<const RecoElectron *> & electrons)
{
  n_presel_ele = electrons.size();

  const Int_t nof_iterations = std::min(n_presel_ele, nof_eles);
  for(Int_t i = 0; i < nof_iterations; ++i)
  {
    const RecoElectron * const electron = electrons[i];
    ele_pt[i] = electron -> pt();
    ele_eta[i] = electron -> eta();
    ele_phi[i] = electron -> phi();
    ele_E[i] = (electron -> p4()).E();
    ele_charge[i] = electron -> charge();
    ele_miniRelIso[i] = electron -> relIso();
    ele_sip3D[i] = electron -> sip3d();
    ele_dxyAbs[i] = std::fabs(electron -> dxy());
    ele_dxy[i] = electron -> dxy();
    ele_dz[i] = electron -> dz();
    ele_ntMVAeleID[i] = electron -> mvaRaw_POG();
    ele_leptonMVA[i] = electron -> mvaRawTTH();
  }
}

void
SyncNtupleManager_bbww::read(const std::vector<const RecoJet *> & jets)
{
  n_presel_jet = jets.size();
  const Int_t nof_iterations = std::min(n_presel_jet, nof_jets);
  for(Int_t i = 0; i < nof_iterations; ++i)
  {
    const RecoJet * const jet = jets[i];
    jet_pt[i] = jet -> pt();
    jet_eta[i] = jet -> eta();
    jet_phi[i] = jet -> phi();
    jet_E[i] = (jet -> p4()).E();
    jet_CSV[i] = std::max(jet -> BtagCSV(), 0.);
  }
}

void
SyncNtupleManager_bbww::read(const std::vector<const RecoJetAK8 *> & jets,
                             bool isLS)
{
  const Int_t nof_iterations = std::min(static_cast<int>(jets.size()), isLS ? nof_jetsAk8LS : nof_jetsAk8);
  for(Int_t i = 0; i < nof_iterations; ++i)
  {
    const RecoJetAK8 * const jet = jets[i];
    if(isLS)
    {
      jetAk8Ls_pt[i] = jet -> pt();
      jetAk8Ls_eta[i] = jet -> eta();
      jetAk8Ls_phi[i] = jet -> phi();
      jetAk8Ls_E[i] = (jet -> p4()).E();
      jetAk8Ls_msoftdrop[i] = jet -> msoftdrop();
      jetAk8Ls_tau1[i] = jet -> tau1();
      jetAk8Ls_tau2[i] = jet -> tau2();
      const RecoSubjetAK8 * const subJet1 = jet -> subJet1();
      if(subJet1)
      {
        jetAk8Ls_subjet0_pt[i] = subJet1 -> pt();
        jetAk8Ls_subjet0_eta[i] = subJet1 -> eta();
        jetAk8Ls_subjet0_phi[i] = subJet1 -> phi();
        jetAk8Ls_subjet0_CSV[i] = subJet1 -> BtagCSV();
      }
      const RecoSubjetAK8 * const subJet2 = jet -> subJet2();
      if(subJet1)
      {
        jetAk8Ls_subjet1_pt[i] = subJet2 -> pt();
        jetAk8Ls_subjet1_eta[i] = subJet2 -> eta();
        jetAk8Ls_subjet1_phi[i] = subJet2 -> phi();
        jetAk8Ls_subjet1_CSV[i] = subJet2 -> BtagCSV();
      }
    }
    else
    {
      jetAk8_pt[i] = jet -> pt();
      jetAk8_eta[i] = jet -> eta();
      jetAk8_phi[i] = jet -> phi();
      jetAk8_E[i] = (jet -> p4()).E();
      jetAk8_msoftdrop[i] = jet -> msoftdrop();
      jetAk8_tau1[i] = jet -> tau1();
      jetAk8_tau2[i] = jet -> tau2();
      const RecoSubjetAK8 * const subJet1 = jet -> subJet1();
      if(subJet1)
      {
        jetAk8_subjet0_pt[i] = subJet1 -> pt();
        jetAk8_subjet0_eta[i] = subJet1 -> eta();
        jetAk8_subjet0_phi[i] = subJet1 -> phi();
        jetAk8_subjet0_CSV[i] = subJet1 -> BtagCSV();
      }
      const RecoSubjetAK8 * const subJet2 = jet -> subJet2();
      if(subJet1)
      {
        jetAk8_subjet1_pt[i] = subJet2 -> pt();
        jetAk8_subjet1_eta[i] = subJet2 -> eta();
        jetAk8_subjet1_phi[i] = subJet2 -> phi();
        jetAk8_subjet1_CSV[i] = subJet2 -> BtagCSV();
      }
    }
  }
}

void
SyncNtupleManager_bbww::read(Float_t value,
                             FloatVariableType_bbww type)
{
  floatMap[type] = value;
}

void
SyncNtupleManager_bbww::read(const std::vector<std::vector<hltPath *>> & hltPaths)
{
  for(const auto & hltVector: hltPaths)
  {
    for(const auto & hlt: hltVector)
    {
      hltMap[hlt -> getBranchName()] = hlt -> getValue();
    }
  }
}

void
SyncNtupleManager_bbww::reset()
{
  nEvent = 0;
  ls = 0;
  run = 0;

  reset(
    n_presel_mu,
    n_presel_ele,
    n_presel_jet
  );

  for(auto & kv: floatMap)
  {
    kv.second = placeholder_value;
  }

  reset(
    nof_mus,
    mu_pt,
    mu_eta,
    mu_phi,
    mu_E,
    mu_charge,
    mu_miniRelIso,
    mu_sip3D,
    mu_dxy,
    mu_dxyAbs,
    mu_dz,
    mu_segmentCompatibility,
    mu_leptonMVA,
    mu_mediumID
  );

  reset(
    nof_eles,
    ele_pt,
    ele_eta,
    ele_phi,
    ele_E,
    ele_charge,
    ele_miniRelIso,
    ele_sip3D,
    ele_dxy,
    ele_dxyAbs,
    ele_dz,
    ele_ntMVAeleID,
    ele_leptonMVA
  );

  reset(
    nof_jets,
    jet_pt,
    jet_eta,
    jet_phi,
    jet_E,
    jet_CSV
  );

  reset(
    nof_jetsAk8,
    jetAk8_pt,
    jetAk8_eta,
    jetAk8_phi,
    jetAk8_E,
    jetAk8_msoftdrop,
    jetAk8_tau1,
    jetAk8_tau2,
    jetAk8_subjet0_pt,
    jetAk8_subjet0_eta,
    jetAk8_subjet0_phi,
    jetAk8_subjet0_CSV,
    jetAk8_subjet1_pt,
    jetAk8_subjet1_eta,
    jetAk8_subjet1_phi,
    jetAk8_subjet1_CSV
  );

  reset(
    nof_jetsAk8LS,
    jetAk8Ls_pt,
    jetAk8Ls_eta,
    jetAk8Ls_phi,
    jetAk8Ls_E,
    jetAk8Ls_msoftdrop,
    jetAk8Ls_tau1,
    jetAk8Ls_tau2,
    jetAk8Ls_subjet0_pt,
    jetAk8Ls_subjet0_eta,
    jetAk8Ls_subjet0_phi,
    jetAk8Ls_subjet0_CSV,
    jetAk8Ls_subjet1_pt,
    jetAk8Ls_subjet1_eta,
    jetAk8Ls_subjet1_phi,
    jetAk8Ls_subjet1_CSV
  );

  for(auto & kv: hltMap)
  {
    hltMap[kv.first] = -1;
  }
}

void
SyncNtupleManager_bbww::fill()
{
  if(outputDir)
  {
    outputDir -> cd();
  }
  else
  {
    outputFile -> cd();
  }
  outputTree -> Fill();
  reset();
}

void
SyncNtupleManager_bbww::write()
{
  if(outputDir)
  {
    outputDir -> cd();
  }
  else
  {
    outputFile -> cd();
  }
  outputTree -> Write();
}
