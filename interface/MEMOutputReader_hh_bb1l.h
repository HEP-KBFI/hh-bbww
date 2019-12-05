#ifndef hhAnalysis_bbww_MEMOutputReader_hh_bb1l_h
#define hhAnalysis_bbww_MEMOutputReader_hh_bb1l_h

#include "tthAnalysis/HiggsToTauTau/interface/ReaderBase.h" // ReaderBase
#include "hhAnalysis/bbww/interface/MEMOutput_hh_bb1l.h" // MEMOutput_hh_bb1l

// forward declarations
class TTree;

class MEMOutputReader_hh_bb1l
  : public ReaderBase
{
public:
  MEMOutputReader_hh_bb1l(const std::string & branchName_num,
                          const std::string & branchName_obj);
  ~MEMOutputReader_hh_bb1l();

  /**
   * @brief Call tree->SetBranchAddress for all MEMOutput_hh_bb1l branches
   */
  void
  setBranchAddresses(TTree * tree) override;

  /**
   * @brief Read branches from tree and use information to fill collection of MEMOutput_hh_bb1l objects
   * @return Collection of MEMOutput_hh_bb1l objects
   */
  std::vector<MEMOutput_hh_bb1l>
  read() const;

protected:
 /**
   * @brief Initialize names of branches to be read from tree
   */
  void
  setBranchNames();

  const int max_nMEMOutputs_;
  std::string branchName_num_;
  std::string branchName_obj_;

  std::string branchName_run_;
  std::string branchName_lumi_;
  std::string branchName_evt_;
  std::string branchName_lepton_eta_;
  std::string branchName_lepton_phi_;
  std::string branchName_wjet1_eta_;
  std::string branchName_wjet1_phi_;
  std::string branchName_wjet1_isReconstructed_;
  std::string branchName_wjet2_eta_;
  std::string branchName_wjet2_phi_;
  std::string branchName_wjet2_isReconstructed_;
  std::string branchName_bjet1_eta_;
  std::string branchName_bjet1_phi_;
  std::string branchName_bjet1_isReconstructed_;
  std::string branchName_bjet2_eta_;
  std::string branchName_bjet2_phi_;
  std::string branchName_bjet2_isReconstructed_;
  std::string branchName_type_;
  std::string branchName_weight_signal_;
  std::string branchName_weightErr_signal_;
  std::string branchName_weight_background_;
  std::string branchName_weightErr_background_;
  std::string branchName_LR_;
  std::string branchName_cpuTime_;
  std::string branchName_realTime_;
  std::string branchName_isValid_;
  std::string branchName_errorFlag_;

  Int_t nMEMOutputs_;
  UInt_t * run_;
  UInt_t * lumi_;
  ULong64_t * evt_;
  Float_t * lepton_eta_;
  Float_t * lepton_phi_;
  Float_t * wjet1_eta_;
  Float_t * wjet1_phi_;
  Float_t * wjet1_isReconstructed_;
  Float_t * wjet2_eta_;
  Float_t * wjet2_phi_;
  Float_t * wjet2_isReconstructed_;
  Float_t * bjet1_eta_;
  Float_t * bjet1_phi_;
  Float_t * bjet1_isReconstructed_;
  Float_t * bjet2_eta_;
  Float_t * bjet2_phi_;
  Float_t * bjet2_isReconstructed_;
  Int_t * type_;
  Float_t * weight_signal_;
  Float_t * weightErr_signal_;
  Float_t * weight_background_;
  Float_t * weightErr_background_;
  Float_t * LR_;
  Float_t * cpuTime_;
  Float_t * realTime_;
  Int_t * isValid_;
  Int_t * errorFlag_;

  // CV: make sure that only one MEMOutputReader_hh_bb1l instance exists for a given branchName,
  //     as ROOT cannot handle multiple TTree::SetBranchAddress calls for the same branch.
  static std::map<std::string, int> numInstances_;
  static std::map<std::string, MEMOutputReader_hh_bb1l *> instances_;
};

#endif // hhAnalysis_bbww_MEMOutputReader_hh_bb1l_h

