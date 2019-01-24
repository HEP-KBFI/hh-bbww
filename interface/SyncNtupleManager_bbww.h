#ifndef SYNCNTUPLEMANAGER_H
#define SYNCNTUPLEMANAGER_H

#include "tthAnalysis/HiggsToTauTau/interface/TypeTraits.h" // Traits<>
#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h" // cmsException()
#include "tthAnalysis/HiggsToTauTau/interface/EventInfo.h" // EventInfo

#include <TTree.h> // TTree

#include <type_traits> // std::enable_if<,>, std::is_arithmetic<>

// forward declarations
class TFile;
class RecoMuon;
class RecoElectron;
class RecoJet;
class RecoJetAK8;
class hltPath;

enum class FloatVariableType_bbww
{
//--- MET/MHT
  PFMET,
  PFMETphi,
  PU_weight,               ///< PU weight
  MC_weight                ///< MC weight
};

class SyncNtupleManager_bbww
{
public:
  SyncNtupleManager_bbww(const std::string & outputFileName,
                         const std::string & outputTreeName);
  ~SyncNtupleManager_bbww();

  void initializeBranches();
  void initializeHLTBranches(const std::vector<std::vector<hltPath *>> & hltPaths);
  void read(const EventInfo & eventInfo);
  void read(const std::vector<const RecoMuon *> & muons);
  void read(const std::vector<const RecoElectron *> & electrons);
  void read(const std::vector<const RecoJet *> & jets);
  void read(const std::vector<const RecoJetAK8 *> & jetsAk8,
            bool isLS);
  void read(Float_t value,
            FloatVariableType_bbww type);
  void read(const std::vector<std::vector<hltPath *>> & hltPaths);
  void fill();
  void write();
  void reset();

  static const Int_t placeholder_value;

private:
  template<typename T,
           typename = std::enable_if<std::is_arithmetic<T>::value && ! std::is_pointer<T>::value>>
  void
  setBranches(const std::string & infix,
              int count,
              T * & var,
              const std::string & label)
  {
    if(count > 0)
    {
      var = new T[count];
      for(int i = 0; i < count; ++i)
      {
        var[i] = placeholder_value;
        const std::string branchName = Form("%s%d_%s", infix.c_str(), i + 1, label.c_str());
        outputTree -> Branch(branchName.c_str(), &(var[i]), Form("%s/%s", branchName.c_str(), Traits<T>::TYPE_NAME));
      }
    }
    else
    {
      throw cmsException(this, __func__)
        << "Invalid array size = " << count << " for variable " << label << " with infix = " << infix;
    }
  }

  template<typename T,
           typename... Args,
           typename = std::enable_if<std::is_arithmetic<T>::value && ! std::is_pointer<T>::value>>
  void
  setBranches(const std::string & infix,
              int count,
              T * & var,
              const std::string & label,
              Args & ... remainingVars)
  {
    if(! outputTree)
    {
      throw cmsException(this, __func__) << "Input tree uninitialized";
    }
    setBranches(infix, count, var, label);
    setBranches(infix, count, remainingVars...);
  }

  template<typename T,
           typename = std::enable_if<std::is_arithmetic<T>::value && ! std::is_pointer<T>::value>>
  void
  setBranches(T & var,
              const std::string & label)
  {
    var = placeholder_value;
    outputTree -> Branch(label.c_str(), &var, Form("%s/%s", label.c_str(), Traits<T>::TYPE_NAME));
  }

  template<typename T,
           typename... Args,
           typename = std::enable_if<std::is_arithmetic<T>::value && ! std::is_pointer<T>::value>>
  void
  setBranches(T & var,
              const std::string & label,
              Args & ... remainingVars)
  {
    if(! outputTree)
    {
      throw cmsException(this, __func__) << "Input tree uninitialized";
    }
    setBranches(var, label);
    setBranches(remainingVars...);
  }

  template<typename T,
           typename = std::enable_if<std::is_arithmetic<T>::value && ! std::is_pointer<T>::value>>
  void
  reset(int count,
        T * & var)
  {
    for(int i = 0; i < count; ++i)
    {
      var[i] = typeid(T) != typeid(Bool_t) ? placeholder_value : 0;
    }
  }

  template<typename T,
           typename... Args,
           typename = std::enable_if<std::is_arithmetic<T>::value && ! std::is_pointer<T>::value>>
  void
  reset(int count,
        T * & var,
        Args & ... remainingVars)
  {
    reset(count, var);
    reset(count, remainingVars...);
  }

  template<typename T,
           typename = std::enable_if<std::is_arithmetic<T>::value && ! std::is_pointer<T>::value>>
  void
  reset(T & var)
  {
    var = typeid(T) != typeid(Bool_t) ? placeholder_value : 0;
  }

  template<typename T,
           typename... Args,
           typename = std::enable_if<std::is_arithmetic<T>::value && ! std::is_pointer<T>::value>>
  void
  reset(T & var,
        Args & ... remainingVars)
  {
    reset(var);
    reset(remainingVars...);
  }

  TFile * outputFile;
  TDirectory * outputDir;
  TTree * outputTree;

  const Int_t nof_mus;
  const Int_t nof_eles;
  const Int_t nof_jets;
  const Int_t nof_jetsAk8;
  const Int_t nof_jetsAk8LS;

  Long64_t nEvent;
  Int_t ls;
  Int_t run;

  Int_t n_presel_mu;
  Int_t n_presel_ele;
  Int_t n_presel_jet;

  Float_t * mu_pt;
  Float_t * mu_eta;
  Float_t * mu_phi;
  Float_t * mu_E;
  Int_t * mu_charge;
  Float_t * mu_miniRelIso;
  Float_t * mu_sip3D;
  Float_t * mu_dxyAbs;
  Float_t * mu_dxy;
  Float_t * mu_dz;
  Float_t * mu_segmentCompatibility;
  Float_t * mu_leptonMVA;
  Bool_t * mu_mediumID;

  Float_t * ele_pt;
  Float_t * ele_eta;
  Float_t * ele_phi;
  Float_t * ele_E;
  Int_t * ele_charge;
  Float_t * ele_miniRelIso;
  Float_t * ele_sip3D;
  Float_t * ele_dxyAbs;
  Float_t * ele_dxy;
  Float_t * ele_dz;
  Float_t * ele_ntMVAeleID;
  Float_t * ele_leptonMVA;

  Float_t * jet_pt;
  Float_t * jet_eta;
  Float_t * jet_phi;
  Float_t * jet_E;
  Float_t * jet_CSV;

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

#endif // SYNCNTUPLEMANAGER_H
