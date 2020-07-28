#ifndef hhAnalysis_bbww_MEMOutputWriter_hh_bb2l_h
#define hhAnalysis_bbww_MEMOutputWriter_hh_bb2l_h

#include "hhAnalysis/bbww/interface/MEMOutput_hh_bb2l.h" // MEMOutput_hh_bb2l
typedef std::vector<std::string> vstring;
#include <vector> // std::vector<>

// forward declaration
class TTree;

class MEMOutputWriter_hh_bb2l
{
public:
  MEMOutputWriter_hh_bb2l(const std::string & branchName_num,
			  const std::string & branchName_obj
      );
  ~MEMOutputWriter_hh_bb2l();

  /**
   * @brief Call tree->Branch for all MEMOutput_hh_bb2l branches
   */
  void setBranches(TTree * tree);

  /**
   * @brief Write collection of MEMOutput_hh_bb2l objects to tree
   */
  void write(const  std::vector<MEMOutput_hh_bb2l> & memOutputs);

protected:
 /**
   * @brief Initialize names of branches to be read from tree
   */
  void setBranchNames();

  const int max_nMEMOutputs_;
  std::string branchName_num_;
  std::string branchName_obj_;

  std::string branchName_run_;
  std::string branchName_lumi_;
  std::string branchName_evt_;
  std::string branchName_leadLepton_eta_;
  std::string branchName_leadLepton_phi_;
  std::string branchName_subleadLepton_eta_;
  std::string branchName_subleadLepton_phi_;
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
  Float_t * leadLepton_eta_;
  Float_t * leadLepton_phi_;
  Float_t * subleadLepton_eta_;
  Float_t * subleadLepton_phi_;
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
};

#endif // hhAnalysis_bbww_MEMOutputWriter_hh_bb2l_h
