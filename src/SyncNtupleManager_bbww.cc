#include "hhAnalysis/bbww/interface/SyncNtupleManager_bbww.h"

#include "tthAnalysis/HiggsToTauTau/interface/RecoMuon.h" // RecoMuon
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectron.h" // RecoElectron
#include "tthAnalysis/HiggsToTauTau/interface/RecoJet.h" // RecoJet
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetAK8.h" // RecoJetAK8
#include "tthAnalysis/HiggsToTauTau/interface/hltPath.h" // hltPath
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // as_integer()
#include "tthAnalysis/HiggsToTauTau/interface/generalAuxFunctions.h"  // format_vdouble()

#include <TFile.h>   // TFile
#include <TString.h> // TString, Form

#include <boost/algorithm/string/predicate.hpp> // boost::starts_with()

#include <algorithm> // std::min()

SyncNtupleManager_bbww::SyncNtupleManager_bbww(const std::string & outputFileName,
                                               const std::string & outputTreeName)
  : SyncNtupleManagerBase(new TFile(outputFileName.c_str(), "recreate"), outputTreeName)
  , nof_mus(2)
  , nof_eles(2)
  , nof_jets(4)
  , nof_jets_vbf(5)
  , nof_jets_vbf_pair(2)
  , nof_jetsAk8(2)
  , nof_jetsAk8LS(2)
{
  for(int var = as_integer(FloatVariableType_bbww::trigger_SF); var <= as_integer(FloatVariableType_bbww::MC_weight); ++var)
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
  const char * lstr      = "lep";
  const char * mstr      = "mu";
  const char * estr      = "ele";
  const char * jstr      = "ak4Jet";
  const char * jvbfstr   = "ak4JetVBF";
  const char * jvbfpstr  = "ak4JetVBFPair";
  const char * jstrAk8   = "ak8Jet";
  const char * jstrAk8Ls = "ak8lsJet";
  const char * bjstr     = "ak4BJet";

  const std::string n_sel_lep_str                = Form("n_%s",                     lstr);
  const std::string n_presel_mu_str              = Form("n_presel_%s",              mstr);
  const std::string n_fakeablesel_mu_str         = Form("n_fakeablesel_%s",         mstr);
  const std::string n_mvasel_mu_str              = Form("n_mvasel_%s",              mstr);
  const std::string n_presel_ele_str             = Form("n_presel_%s",              estr);
  const std::string n_fakeablesel_ele_str        = Form("n_fakeablesel_%s",         estr);
  const std::string n_mvasel_ele_str             = Form("n_mvasel_%s",              estr);
  const std::string n_presel_jet_str             = Form("n_presel_%s",              jstr);
  const std::string n_presel_jet_vbf_str         = Form("n_presel_%s",              jvbfstr);
  const std::string n_presel_jet_vbf_pairs_str   = Form("n_presel_%spairs",         jvbfstr);
  const std::string n_presel_jet_vbf_postlep_str = Form("n_presel_%s_postLepClean", jvbfstr);
  const std::string n_presel_jet_vbf_postjet_str = Form("n_presel_%s_postJetClean", jvbfstr);
  const std::string n_presel_jetAK8_str          = Form("n_presel_%s",              jstrAk8);
  const std::string n_presel_jetAK8LS_str        = Form("n_presel_%s",              jstrAk8Ls);
  const std::string n_loose_bjet_str             = Form("n_loose_%s",               bjstr);
  const std::string n_medium_bjet_str            = Form("n_medium_%s",              bjstr);

  setBranches(
    nEvent,                       "event",
    ls,                           "ls",
    run,                          "run",
    flag_boosted,                 "is_boosted",
    flag_semiboosted,             "is_semiboosted",
    flag_resolved,                "is_resolved",
    flag_ee,                      "is_ee",
    flag_mm,                      "is_mm",
    flag_em,                      "is_em",
    flag_ss,                      "is_ss",
    n_presel_mu,                  n_presel_mu_str,
    n_fakeablesel_mu,             n_fakeablesel_mu_str,
    n_mvasel_mu,                  n_mvasel_mu_str,
    n_presel_ele,                 n_presel_ele_str,
    n_fakeablesel_ele,            n_fakeablesel_ele_str,
    n_mvasel_ele,                 n_mvasel_ele_str,
    n_presel_jet,                 n_presel_jet_str,
    n_presel_jet_vbf,             n_presel_jet_vbf_str,
    n_presel_jet_vbfPairs,        n_presel_jet_vbf_pairs_str,
    n_presel_jet_vbfPostLepClean, n_presel_jet_vbf_postlep_str,
    n_presel_jet_vbfPostJetClean, n_presel_jet_vbf_postjet_str,
    n_presel_jetAK8,              n_presel_jetAK8_str,
    n_presel_jetAK8LS,            n_presel_jetAK8LS_str,
    n_loose_bjet,                 n_loose_bjet_str,
    n_medium_bjet,                n_medium_bjet_str,

//--- MET/MHT
    floatMap[FloatVariableType_bbww::trigger_SF],               "trigger_SF",
    floatMap[FloatVariableType_bbww::vbf_m_jj],                 "vbf_m_jj",
    floatMap[FloatVariableType_bbww::vbf_dEta_jj],              "vbf_dEta_jj",
    floatMap[FloatVariableType_bbww::lepton_IDSF],              "lepton_IDSF",
    floatMap[FloatVariableType_bbww::btag_SF],                  "btag_SF",
    floatMap[FloatVariableType_bbww::btag_SF_ratio],            "btag_SF_ratio",
    floatMap[FloatVariableType_bbww::topPt_wgt],                "topPt_wgt",
    floatMap[FloatVariableType_bbww::fakeRate],                 "fakeRate",
    floatMap[FloatVariableType_bbww::L1prefire],                "L1prefire",
    floatMap[FloatVariableType_bbww::lepton_IDSF_recoToLoose],  "lepton_IDSF_recoToLoose",
    floatMap[FloatVariableType_bbww::lepton_IDSF_looseToTight], "lepton_IDSF_looseToTight",
    floatMap[FloatVariableType_bbww::PFMET],                    "PFMET",
    floatMap[FloatVariableType_bbww::PFMETphi],                 "PFMETphi",
    floatMap[FloatVariableType_bbww::HME],                      "HME",
    floatMap[FloatVariableType_bbww::MEM_LR],                   "MEM_LR",
    floatMap[FloatVariableType_bbww::MEM_LR_up],                "MEM_LR_up",
    floatMap[FloatVariableType_bbww::MEM_LR_down],              "MEM_LR_down",
    floatMap[FloatVariableType_bbww::PU_jetID_SF],              "PU_jetID_SF",
    floatMap[FloatVariableType_bbww::PU_weight],                "PU_weight",
    floatMap[FloatVariableType_bbww::MC_weight],                "MC_weight"
  );

  setBranches(
    mstr,                     nof_mus,
    mu_pt,                    "pt",
    mu_conept,                "conept",
    mu_eta,                   "eta",
    mu_phi,                   "phi",
    mu_E,                     "E",
    mu_charge,                "charge",
    mu_miniRelIso,            "miniRelIso",
    mu_pfRelIso04All,         "PFRelIso04",
    mu_jetNDauChargedMVASel,  "jetNDauChargedMVASel",
    mu_jetPtRel,              "jetPtRel",
    mu_jetRelIso,             "jetRelIso",
    mu_jetDeepJet,            "jetDeepJet",
    mu_sip3D,                 "sip3D",
    mu_dxy,                   "dxy",
    mu_dxyAbs,                "dxyAbs",
    mu_dz,                    "dz",
    mu_segmentCompatibility,  "segmentCompatibility",
    mu_leptonMVA,             "leptonMVA",
    mu_dpt_div_pt,            "dpt_div_pt",
    mu_mediumID,              "mediumID",
    mu_isfakeablesel,         "isfakeablesel",
    mu_ismvasel,              "ismvasel",
    mu_isGenMatched,          "isGenMatched"
  );

  setBranches(
    estr, nof_eles,
    ele_pt,                   "pt",
    ele_conept,               "conept",
    ele_eta,                  "eta",
    ele_phi,                  "phi",
    ele_E,                    "E",
    ele_charge,               "charge",
    ele_miniRelIso,           "miniRelIso",
    ele_pfRelIso04All,        "PFRelIso04",
    ele_jetNDauChargedMVASel, "jetNDauChargedMVASel",
    ele_jetPtRel,             "jetPtRel",
    ele_jetRelIso,            "jetRelIso",
    ele_jetDeepJet,           "jetDeepJet",
    ele_sip3D,                "sip3D",
    ele_dxyAbs,               "dxyAbs",
    ele_dxy,                  "dxy",
    ele_dz,                   "dz",
    ele_ntMVAeleID,           "ntMVAeleID",
    ele_leptonMVA,            "leptonMVA",
    ele_passesConversionVeto, "passesConversionVeto",
    ele_nMissingHits,         "nMissingHits",
    ele_sigmaEtaEta,          "sigmaEtaEta",
    ele_HoE,                  "HoE",
    ele_OoEminusOoP,          "OoEminusOoP",
    ele_isfakeablesel,        "isfakeablesel",
    ele_ismvasel,             "ismvasel",
    ele_isGenMatched,         "isGenMatched"
  );

  setBranches(
    jstr, nof_jets,
    jet_pt,                   "pt",
    jet_eta,                  "eta",
    jet_phi,                  "phi",
    jet_E,                    "E",
    jet_CSV,                  "CSV",
    jet_btagSF,               "btagSF"
  );

  setBranches(
    jvbfpstr, nof_jets_vbf_pair,
    jet_vbf_pair_pt,              "pt",
    jet_vbf_pair_eta,             "eta",
    jet_vbf_pair_phi,             "phi",
    jet_vbf_pair_E,               "E",
    jet_vbf_pair_CSV,             "CSV",
    jet_vbf_pair_btagSF,          "btagSF"
  );

  setBranches(
    jvbfstr, nof_jets_vbf,
    jet_vbf_pt,              "pt",
    jet_vbf_eta,             "eta",
    jet_vbf_phi,             "phi",
    jet_vbf_E,               "E",
    jet_vbf_CSV,             "CSV",
    jet_vbf_btagSF,          "btagSF"
  );

  setBranches(
    jstrAk8,                  nof_jetsAk8,
    jetAk8_pt,                "pt",
    jetAk8_eta,               "eta",
    jetAk8_phi,               "phi",
    jetAk8_E,                 "E",
    jetAk8_msoftdrop,         "msoftdrop",
    jetAk8_tau1,              "tau1",
    jetAk8_tau2,              "tau2",
    jetAk8_subjet0_pt,        "subjet0_pt",
    jetAk8_subjet0_eta,       "subjet0_eta",
    jetAk8_subjet0_phi,       "subjet0_phi",
    jetAk8_subjet0_CSV,       "subjet0_CSV",
    jetAk8_subjet1_pt,        "subjet1_pt",
    jetAk8_subjet1_eta,       "subjet1_eta",
    jetAk8_subjet1_phi,       "subjet1_phi",
    jetAk8_subjet1_CSV,       "subjet1_CSV"
  );

  setBranches(
    jstrAk8Ls,                nof_jetsAk8,
    jetAk8Ls_pt,              "pt",
    jetAk8Ls_eta,             "eta",
    jetAk8Ls_phi,             "phi",
    jetAk8Ls_E,               "E",
    jetAk8Ls_msoftdrop,       "msoftdrop",
    jetAk8Ls_tau1,            "tau1",
    jetAk8Ls_tau2,            "tau2",
    jetAk8Ls_subjet0_pt,      "subjet0_pt",
    jetAk8Ls_subjet0_eta,     "subjet0_eta",
    jetAk8Ls_subjet0_phi,     "subjet0_phi",
    jetAk8Ls_subjet0_CSV,     "subjet0_CSV",
    jetAk8Ls_subjet1_pt,      "subjet1_pt",
    jetAk8Ls_subjet1_eta,     "subjet1_eta",
    jetAk8Ls_subjet1_phi,     "subjet1_phi",
    jetAk8Ls_subjet1_CSV,     "subjet1_CSV"
  );

  for ( int jpaCategory = (int)JPA::Category_resolved::k2b2W; jpaCategory <= (int)JPA::Category_resolved::k0b; ++jpaCategory )
  {
    const std::string branchName_suffix = TString(get_jpaCategory_string(jpaCategory).data()).ReplaceAll(" ", "").ReplaceAll("(", "_").ReplaceAll(")", "").Data();
    if ( jpaCategory <= (int)JPA::Category_resolved::k1b0W )
    {
      const std::string jpaCatName = Form("jpa_1stLayer_%s", branchName_suffix.data());
      setBranches(jpaMap_1stLayer[jpaCategory], jpaCatName);

      jpaInputNames[jpaCategory] = get_jpaInputs(jpaCategory);
      for(const std::string & jpaInputVarName: jpaInputNames.at(jpaCategory))
      {
        setBranches(jpaInputs_1stLayer[jpaCategory][jpaInputVarName], Form("%s_%s", jpaCatName.data(), jpaInputVarName.data()));
      }
    }
    setBranches(jpaMap_2ndLayer[jpaCategory], Form("jpa_2ndLayer_%s", branchName_suffix.data()));
  }
  for ( int jpaCategory = (int)JPA::Category_boosted::k2b2W; jpaCategory <= (int)JPA::Category_boosted::k2b0W; ++jpaCategory )
  {
    const std::string branchName_suffix = TString(get_jpaCategory_string(jpaCategory).data()).ReplaceAll(" ", "").ReplaceAll("(", "_").ReplaceAll(")", "").Data();
    const std::string jpaCatName = Form("jpa_1stLayer_%s", branchName_suffix.data());
    setBranches(jpaMap_1stLayer[jpaCategory], jpaCatName);
    setBranches(jpaMap_2ndLayer[jpaCategory], Form("jpa_2ndLayer_%s", branchName_suffix.data()));

    if(jpaCategory <= (int)JPA::Category_boosted::k2b1W)
    {
      jpaInputNames[jpaCategory] = get_jpaInputs(jpaCategory);
      for(const std::string & jpaInputVarName: jpaInputNames.at(jpaCategory))
      {
        setBranches(jpaInputs_1stLayer[jpaCategory][jpaInputVarName], Form("%s_%s", jpaCatName.data(), jpaInputVarName.data()));
      }
    }
  }

  resetBranches();
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
SyncNtupleManager_bbww::read(const std::vector<const RecoMuon *> & muons,
                             const std::vector<const RecoMuon *> & fakeable_muons,
                             const std::vector<const RecoMuon *> & tight_muons)
{
  n_presel_mu = muons.size();
  n_fakeablesel_mu = fakeable_muons.size();
  n_mvasel_mu = tight_muons.size();

  const Int_t nof_iterations = std::min(n_presel_mu, nof_mus);
  for(Int_t i = 0; i < nof_iterations; ++i)
  {
    const RecoMuon * const muon = muons[i];
    mu_pt[i] = muon -> pt();
    mu_conept[i] = muon -> cone_pt();
    mu_eta[i] = muon -> eta();
    mu_phi[i] = muon -> phi();
    mu_E[i] = (muon -> p4()).E();
    mu_charge[i] = muon -> charge();
    mu_miniRelIso[i] = muon -> relIso();
    mu_pfRelIso04All[i] = muon -> pfRelIso04All();
    mu_jetNDauChargedMVASel[i] = muon -> jetNDauChargedMVASel();
    mu_jetPtRel[i] = muon -> jetPtRel();
    mu_jetRelIso[i] = muon -> jetRelIso();
    mu_jetDeepJet[i] = std::max(0., muon -> jetBtagCSV(Btag::kDeepJet));
    mu_sip3D[i] = muon -> sip3d();
    mu_dxyAbs[i] = std::fabs(muon -> dxy());
    mu_dxy[i] = muon -> dxy();
    mu_dz[i] = muon -> dz();
    mu_segmentCompatibility[i] = muon -> segmentCompatibility();
    mu_leptonMVA[i] = muon -> mvaRawTTH();
    mu_dpt_div_pt[i] = muon -> dpt_div_pt();
    mu_mediumID[i] = muon -> passesMediumIdPOG();

    mu_isfakeablesel[i] = 0;
    for(const auto & fakeable_muon: fakeable_muons)
    {
      if(muon == fakeable_muon)
      {
        mu_isfakeablesel[i] = 1;
        break;
      }
    }
    mu_ismvasel[i] = 0;
    for(const auto & tight_muon: tight_muons)
    {
      if(muon == tight_muon)
      {
        mu_ismvasel[i] = 1;
        break;
      }
    }

    mu_isGenMatched[i] = muon -> isGenMatched(false);
  }
}

void
SyncNtupleManager_bbww::read(const std::vector<const RecoElectron *> & electrons,
                             const std::vector<const RecoElectron *> & fakeable_electrons,
                             const std::vector<const RecoElectron *> & tight_electrons)
{
  n_presel_ele = electrons.size();
  n_fakeablesel_ele = fakeable_electrons.size();
  n_mvasel_ele = tight_electrons.size();

  const Int_t nof_iterations = std::min(n_presel_ele, nof_eles);
  for(Int_t i = 0; i < nof_iterations; ++i)
  {
    const RecoElectron * const electron = electrons[i];
    ele_pt[i] = electron -> pt();
    ele_conept[i] = electron -> cone_pt();
    ele_eta[i] = electron -> eta();
    ele_phi[i] = electron -> phi();
    ele_E[i] = (electron -> p4()).E();
    ele_charge[i] = electron -> charge();
    ele_miniRelIso[i] = electron -> relIso();
    ele_pfRelIso04All[i] = electron -> pfRelIso04All();
    ele_jetNDauChargedMVASel[i] = electron -> jetNDauChargedMVASel();
    ele_jetPtRel[i] = electron -> jetPtRel();
    ele_jetRelIso[i] = electron -> jetRelIso();
    ele_jetDeepJet[i] = std::max(0., electron -> jetBtagCSV(Btag::kDeepJet));
    ele_sip3D[i] = electron -> sip3d();
    ele_dxyAbs[i] = std::fabs(electron -> dxy());
    ele_dxy[i] = electron -> dxy();
    ele_dz[i] = electron -> dz();
    ele_ntMVAeleID[i] = electron -> mvaRaw_POG();
    ele_leptonMVA[i] = electron -> mvaRawTTH();
    ele_passesConversionVeto[i] = electron -> passesConversionVeto();
    ele_nMissingHits[i] = electron -> nLostHits();
    ele_sigmaEtaEta[i] = electron -> sigmaEtaEta();
    ele_HoE[i] = electron -> HoE();
    ele_OoEminusOoP[i] = electron -> OoEminusOoP();

    ele_isfakeablesel[i] = 0;
    for(const auto & fakeable_electron: fakeable_electrons)
    {
      if(electron == fakeable_electron)
      {
        ele_isfakeablesel[i] = 1;
        break;
      }
    }
    ele_ismvasel[i] = 0;
    for(const auto & tight_electron: tight_electrons)
    {
      if(electron == tight_electron)
      {
        ele_ismvasel[i] = 1;
        break;
      }
    }

    ele_isGenMatched[i] = electron -> isGenMatched(false);
  }
}

void
SyncNtupleManager_bbww::read(const std::vector<const RecoJet *> & jets_vbf,
                             const std::vector<const RecoJet *> & jets_vbf_pair,
                             int n_presel_vbf_postLep,
                             int n_presel_vbf_postJet)
{
  n_presel_jet_vbf = jets_vbf.size();
  n_presel_jet_vbfPairs = static_cast<int>(static_cast<bool>(jets_vbf_pair.size()));
  n_presel_jet_vbfPostLepClean = n_presel_vbf_postLep;
  n_presel_jet_vbfPostJetClean = n_presel_vbf_postJet;

  const Int_t nof_iterations_pair = std::min(static_cast<int>(jets_vbf_pair.size()), nof_jets_vbf_pair);
  for(Int_t i = 0; i < nof_iterations_pair; ++i)
  {
    const RecoJet * const jet = jets_vbf_pair[i];
    jet_vbf_pair_pt[i] = jet -> pt();
    jet_vbf_pair_eta[i] = jet -> eta();
    jet_vbf_pair_phi[i] = jet -> phi();
    jet_vbf_pair_E[i] = (jet -> p4()).E();
    jet_vbf_pair_CSV[i] = std::max(jet -> BtagCSV(), 0.);
    jet_vbf_pair_btagSF[i] = jet -> BtagWeight();
  }

  const Int_t nof_iterations = std::min(static_cast<int>(jets_vbf.size()), nof_jets_vbf);
  for(Int_t i = 0; i < nof_iterations; ++i)
  {
    const RecoJet * const jet = jets_vbf[i];
    jet_vbf_pt[i] = jet -> pt();
    jet_vbf_eta[i] = jet -> eta();
    jet_vbf_phi[i] = jet -> phi();
    jet_vbf_E[i] = (jet -> p4()).E();
    jet_vbf_CSV[i] = std::max(jet -> BtagCSV(), 0.);
    jet_vbf_btagSF[i] = jet -> BtagWeight();
  }
}

void
SyncNtupleManager_bbww::read(const std::vector<const RecoJet *> & jets,
                             int n_bjet_loose,
                             int n_bjet_medium)
{
  n_presel_jet = jets.size();
  n_loose_bjet = n_bjet_loose;
  n_medium_bjet = n_bjet_medium;
  const Int_t nof_iterations = std::min(n_presel_jet, nof_jets);
  for(Int_t i = 0; i < nof_iterations; ++i)
  {
    const RecoJet * const jet = jets[i];
    jet_pt[i] = jet -> pt();
    jet_eta[i] = jet -> eta();
    jet_phi[i] = jet -> phi();
    jet_E[i] = (jet -> p4()).E();
    jet_CSV[i] = std::max(jet -> BtagCSV(), 0.);
    jet_btagSF[i] = jet -> BtagWeight();
  }
}

void
SyncNtupleManager_bbww::read(const std::vector<const RecoJetAK8 *> & jets,
                             bool isLS)
{
  if(isLS)
  {
    n_presel_jetAK8LS = jets.size();
  }
  else
  {
    n_presel_jetAK8 = jets.size();
  }
  const Int_t nof_iterations = std::min(isLS ? n_presel_jetAK8LS : n_presel_jetAK8, isLS ? nof_jetsAk8LS : nof_jetsAk8);
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
SyncNtupleManager_bbww::read(bool is_boosted,
                             bool is_semiboosted,
                             bool is_resolved)
{
  flag_boosted = is_boosted;
  flag_semiboosted = is_semiboosted;
  flag_resolved = is_resolved;
}

void
SyncNtupleManager_bbww::read(bool is_ee,
                             bool is_mm,
                             bool is_em,
                             int  is_ss)
{
  flag_ee = is_ee;
  flag_mm = is_mm;
  flag_em = is_em;
  flag_ss = is_ss;
}

void 
SyncNtupleManager_bbww::read(const JPAInterface & jpaInterface)
{
  for ( int jpaCategory = (int)JPA::Category_resolved::k2b2W; jpaCategory <= (int)JPA::Category_resolved::k0b; ++jpaCategory )
  {
    if ( jpaCategory <= (int)JPA::Category_resolved::k1b0W ) 
    {
      jpaMap_1stLayer[jpaCategory] = jpaInterface.mvaOutput_1stLayer(jpaCategory);
      const std::map<std::string, double> jpaInputs = jpaInterface.get_mvaInputs_1stLayer(jpaCategory);
      for(const auto & kv: jpaInputs)
      {
        jpaInputs_1stLayer[jpaCategory][kv.first] = kv.second;
      }
    }
    jpaMap_2ndLayer[jpaCategory] = jpaInterface.mvaOutput_2ndLayer(jpaCategory);
  }
  for ( int jpaCategory = (int)JPA::Category_boosted::k2b2W; jpaCategory <= (int)JPA::Category_boosted::k2b0W; ++jpaCategory )
  {
    jpaMap_1stLayer[jpaCategory] = jpaInterface.mvaOutput_1stLayer(jpaCategory);
    jpaMap_2ndLayer[jpaCategory] = jpaInterface.mvaOutput_2ndLayer(jpaCategory);
    if( jpaCategory <= (int)JPA::Category_boosted::k2b1W )
    {
      const std::map<std::string, double> jpaInputs = jpaInterface.get_mvaInputs_1stLayer(jpaCategory);
      for(const auto & kv: jpaInputs)
      {
        jpaInputs_1stLayer[jpaCategory][kv.first] = kv.second;
      }
    }
  }
}

void
SyncNtupleManager_bbww::resetBranches()
{
  nEvent = 0;
  ls = 0;
  run = 0;

  reset(
    flag_boosted,
    flag_semiboosted,
    flag_resolved,
    flag_ee,
    flag_mm,
    flag_em,
    flag_ss,
    n_presel_mu,
    n_fakeablesel_mu,
    n_mvasel_mu,
    n_presel_ele,
    n_fakeablesel_ele,
    n_mvasel_ele,
    n_presel_jet,
    n_presel_jet_vbf,
    n_presel_jet_vbfPairs,
    n_presel_jet_vbfPostLepClean,
    n_presel_jet_vbfPostJetClean,
    n_presel_jetAK8,
    n_presel_jetAK8LS,
    n_loose_bjet,
    n_medium_bjet
  );

  for(auto & kv: floatMap)
  {
    kv.second = placeholder_value;
  }

  reset(
    nof_mus,
    mu_pt,
    mu_conept,
    mu_eta,
    mu_phi,
    mu_E,
    mu_charge,
    mu_miniRelIso,
    mu_pfRelIso04All,
    mu_jetNDauChargedMVASel,
    mu_jetPtRel,
    mu_jetRelIso,
    mu_jetDeepJet,
    mu_sip3D,
    mu_dxy,
    mu_dxyAbs,
    mu_dz,
    mu_segmentCompatibility,
    mu_leptonMVA,
    mu_dpt_div_pt,
    mu_mediumID,
    mu_isfakeablesel,
    mu_ismvasel,
    mu_isGenMatched
  );

  reset(
    nof_eles,
    ele_pt,
    ele_conept,
    ele_eta,
    ele_phi,
    ele_E,
    ele_charge,
    ele_miniRelIso,
    ele_pfRelIso04All,
    ele_jetNDauChargedMVASel,
    ele_jetPtRel,
    ele_jetRelIso,
    ele_jetDeepJet,
    ele_sip3D,
    ele_dxy,
    ele_dxyAbs,
    ele_dz,
    ele_ntMVAeleID,
    ele_leptonMVA,
    ele_passesConversionVeto,
    ele_nMissingHits,
    ele_sigmaEtaEta,
    ele_HoE,
    ele_OoEminusOoP,
    ele_isfakeablesel,
    ele_ismvasel,
    ele_isGenMatched
  );

  reset(
    nof_jets,
    jet_pt,
    jet_eta,
    jet_phi,
    jet_E,
    jet_CSV,
    jet_btagSF
  );

  reset(
    nof_jets_vbf_pair,
    jet_vbf_pair_pt,
    jet_vbf_pair_eta,
    jet_vbf_pair_phi,
    jet_vbf_pair_E,
    jet_vbf_pair_CSV,
    jet_vbf_pair_btagSF
  );

  reset(
    nof_jets_vbf,
    jet_vbf_pt,
    jet_vbf_eta,
    jet_vbf_phi,
    jet_vbf_E,
    jet_vbf_CSV,
    jet_vbf_btagSF
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

  for ( int jpaCategory = (int)JPA::Category_resolved::k2b2W; jpaCategory <= (int)JPA::Category_resolved::k0b; ++jpaCategory )
  {
    if ( jpaCategory <= (int)JPA::Category_resolved::k1b0W )
    {
      jpaMap_1stLayer[jpaCategory] = -1.;
      const std::vector<std::string> & jpaInputs = jpaInputNames.at(jpaCategory);
      for(const std::string & jpaInputName: jpaInputs)
      {
        jpaInputs_1stLayer[jpaCategory][jpaInputName] = placeholder_value;
      }
    }
    jpaMap_2ndLayer[jpaCategory] = -1.;
  }
  for ( int jpaCategory = (int)JPA::Category_boosted::k2b2W; jpaCategory <= (int)JPA::Category_boosted::k2b0W; ++jpaCategory )
  {
    jpaMap_1stLayer[jpaCategory] = -1.;
    jpaMap_2ndLayer[jpaCategory] = -1.;
    if( jpaCategory <= (int)JPA::Category_boosted::k2b1W )
    {
      const std::vector<std::string> & jpaInputs = jpaInputNames.at(jpaCategory);
      for(const std::string & jpaInputName: jpaInputs)
      {
        jpaInputs_1stLayer[jpaCategory][jpaInputName] = placeholder_value;
      }
    }
  }

  for(auto & kv: hltMap)
  {
    hltMap[kv.first] = -1;
  }
}
