#ifndef hhAnalysis_bbww_HMEOutputWriter_hh_bb2l_h
#define hhAnalysis_bbww_HMEOutputWriter_hh_bb2l_h

#include "hhAnalysis/bbww/interface/HMEOutput_hh_bb2l.h" // HMEOutput_hh_bb2l

#include <vector> // std::vector<>

// forward declaration
class TTree;

class HMEOutputWriter_hh_bb2l
{
public:
  HMEOutputWriter_hh_bb2l(const std::string & branchName_num,
<<<<<<< HEAD
			  const std::string & branchName_obj);
=======
                          const std::string & branchName_obj);
>>>>>>> c36b464bd8141e4e029b19d7f5b0fd84cfe65f63
  ~HMEOutputWriter_hh_bb2l();

  /**
   * @brief Call tree->Branch for all HMEOutput_hh_bb2l branches
   */
  void setBranches(TTree * tree);

  /**
   * @brief Write collection of HMEOutput_hh_bb2l objects to tree
   */
  void write(const std::vector<HMEOutput_hh_bb2l> & memOutputs);
  
protected:
 /**
   * @brief Initialize names of branches to be read from tree
   */
  void setBranchNames();

  const int max_nHMEOutputs_;
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
  std::string branchName_m_HH_hme_;
  std::string branchName_cpuTime_;
  std::string branchName_realTime_;
  std::string branchName_isValid_;
  std::string branchName_errorFlag_;

  Int_t nHMEOutputs_;
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
  Float_t * m_HH_hme_;
  Float_t * cpuTime_;
  Float_t * realTime_;
  Int_t * isValid_;
  Int_t * errorFlag_;
};

#endif // hhAnalysis_bbww_HMEOutputWriter_hh_bb2l_h

