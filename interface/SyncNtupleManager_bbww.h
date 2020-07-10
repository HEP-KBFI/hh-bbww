#ifndef hhAnalysis_bbww_SyncNtupleManager_bbww_h
#define hhAnalysis_bbww_SyncNtupleManager_bbww_h

#include "tthAnalysis/HiggsToTauTau/interface/SyncNtupleManagerBase.h"

// forward declarations
class RecoMuon;
class RecoElectron;
class RecoJet;
class RecoJetAK8;
class hltPath;

enum class FloatVariableType_bbww
{
//--- MET/MHT
  trigger_SF,
  lepton_IDSF,
  lepton_IDSF_recoToLoose,
  lepton_IDSF_looseToTight,
  btag_SF,
  btag_SF_ratio,
  topPt_wgt,
  fakeRate,
  L1prefire,
  PFMET,
  PFMETphi,
  HME,
  MEM_LR,
  MEM_LR_up,
  MEM_LR_down,
  PU_weight,               ///< PU weight
  MC_weight                ///< MC weight
};

class SyncNtupleManager_bbww
  : public virtual SyncNtupleManagerBase
{
public:
  SyncNtupleManager_bbww(const std::string & outputFileName,
                         const std::string & outputTreeName);
  ~SyncNtupleManager_bbww() override;

  void initializeBranches() override;
  void initializeHLTBranches(const std::vector<std::vector<hltPath *>> & hltPaths);
  void read(const EventInfo & eventInfo);
  void read(const std::vector<const RecoMuon *> & muons,
            const std::vector<const RecoMuon *> & fakeable_muons,
            const std::vector<const RecoMuon *> & tight_muons);
  void read(const std::vector<const RecoElectron *> & electrons,
            const std::vector<const RecoElectron *> & fakeable_electrons,
            const std::vector<const RecoElectron *> & tight_electrons);
  void read(const std::vector<const RecoJet *> & jets,
            int n_bjet_loose,
            int n_bjet_medium);
  void read(const std::vector<const RecoJetAK8 *> & jetsAk8,
            bool isLS);
  void read(Float_t value,
            FloatVariableType_bbww type);
  void read(const std::vector<std::vector<hltPath *>> & hltPaths);
  void read(bool is_boosted,
            bool is_semiboosted,
            bool is_resolved);
  void read(bool is_ee,
            bool is_mm,
            bool is_em,
            int  is_ss);
  void resetBranches() override;

protected:
  const Int_t nof_mus;
  const Int_t nof_eles;
  const Int_t nof_jets;
  const Int_t nof_jetsAk8;
  const Int_t nof_jetsAk8LS;

  Long64_t nEvent;
  Int_t ls;
  Int_t run;

  Int_t n_presel_mu;
  Int_t n_fakeablesel_mu;
  Int_t n_mvasel_mu;
  Int_t n_presel_ele;
  Int_t n_fakeablesel_ele;
  Int_t n_mvasel_ele;
  Int_t n_presel_jet;
  Int_t n_presel_jetAK8;
  Int_t n_presel_jetAK8LS;
  Int_t n_loose_bjet;
  Int_t n_medium_bjet;

  Int_t flag_boosted;
  Int_t flag_semiboosted;
  Int_t flag_resolved;

  Int_t flag_ee;
  Int_t flag_mm;
  Int_t flag_em;
  int flag_ss;

  Float_t * mu_pt;
  Float_t * mu_conept;
  Float_t * mu_eta;
  Float_t * mu_phi;
  Float_t * mu_E;
  Int_t * mu_charge;
  Float_t * mu_miniRelIso;
  Float_t * mu_pfRelIso04All;
  Int_t * mu_jetNDauChargedMVASel;
  Float_t * mu_jetPtRel;
  Float_t * mu_jetRelIso;
  Float_t * mu_jetDeepJet;
  Float_t * mu_sip3D;
  Float_t * mu_dxyAbs;
  Float_t * mu_dxy;
  Float_t * mu_dz;
  Float_t * mu_segmentCompatibility;
  Float_t * mu_leptonMVA;
  Float_t * mu_dpt_div_pt;
  Int_t * mu_mediumID;
  Int_t * mu_isfakeablesel;
  Int_t * mu_ismvasel;
  Int_t * mu_isGenMatched;

  Float_t * ele_pt;
  Float_t * ele_conept;
  Float_t * ele_eta;
  Float_t * ele_phi;
  Float_t * ele_E;
  Int_t * ele_charge;
  Float_t * ele_miniRelIso;
  Float_t * ele_pfRelIso04All;
  Int_t * ele_jetNDauChargedMVASel;
  Float_t * ele_jetPtRel;
  Float_t * ele_jetRelIso;
  Float_t * ele_jetDeepJet;
  Float_t * ele_sip3D;
  Float_t * ele_dxyAbs;
  Float_t * ele_dxy;
  Float_t * ele_dz;
  Float_t * ele_ntMVAeleID;
  Float_t * ele_leptonMVA;
  Int_t * ele_passesConversionVeto;
  Int_t * ele_nMissingHits;
  Float_t * ele_sigmaEtaEta;
  Float_t * ele_HoE;
  Float_t * ele_OoEminusOoP;
  Int_t * ele_isfakeablesel;
  Int_t * ele_ismvasel;
  Int_t * ele_isGenMatched;

  Float_t * jet_pt;
  Float_t * jet_eta;
  Float_t * jet_phi;
  Float_t * jet_E;
  Float_t * jet_CSV;
  Float_t * jet_btagSF;

  Float_t * jetAk8_pt;
  Float_t * jetAk8_eta;
  Float_t * jetAk8_phi;
  Float_t * jetAk8_E;
  Float_t * jetAk8_msoftdrop;
  Float_t * jetAk8_tau1;
  Float_t * jetAk8_tau2;
  Float_t * jetAk8_subjet0_pt;
  Float_t * jetAk8_subjet0_eta;
  Float_t * jetAk8_subjet0_phi;
  Float_t * jetAk8_subjet0_CSV;
  Float_t * jetAk8_subjet1_pt;
  Float_t * jetAk8_subjet1_eta;
  Float_t * jetAk8_subjet1_phi;
  Float_t * jetAk8_subjet1_CSV;

  Float_t * jetAk8Ls_pt;
  Float_t * jetAk8Ls_eta;
  Float_t * jetAk8Ls_phi;
  Float_t * jetAk8Ls_E;
  Float_t * jetAk8Ls_msoftdrop;
  Float_t * jetAk8Ls_tau1;
  Float_t * jetAk8Ls_tau2;
  Float_t * jetAk8Ls_subjet0_pt;
  Float_t * jetAk8Ls_subjet0_eta;
  Float_t * jetAk8Ls_subjet0_phi;
  Float_t * jetAk8Ls_subjet0_CSV;
  Float_t * jetAk8Ls_subjet1_pt;
  Float_t * jetAk8Ls_subjet1_eta;
  Float_t * jetAk8Ls_subjet1_phi;
  Float_t * jetAk8Ls_subjet1_CSV;

  std::map<std::string, Int_t> hltMap;

  std::map<FloatVariableType_bbww, Float_t> floatMap;
};

#endif // hhAnalysis_bbww_SyncNtupleManager_bbww_h
