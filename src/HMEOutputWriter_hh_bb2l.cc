#include "hhAnalysis/bbww/interface/HMEOutputWriter_hh_bb2l.h" // MEMOutputWriter_hh_bb2l

#include "tthAnalysis/HiggsToTauTau/interface/BranchAddressInitializer.h" // BranchAddressInitializer, TTree, Form()

HMEOutputWriter_hh_bb2l::HMEOutputWriter_hh_bb2l(const std::string & branchName_num,
                                                 const std::string & branchName_obj)
  : max_nHMEOutputs_(100)
  , branchName_num_(branchName_num)
  , branchName_obj_(branchName_obj)
  , run_(nullptr)
  , lumi_(nullptr)
  , evt_(nullptr)
  , leadLepton_eta_(nullptr)
  , leadLepton_phi_(nullptr)
  , subleadLepton_eta_(nullptr)
  , subleadLepton_phi_(nullptr)
  , bjet1_eta_(nullptr)
  , bjet1_phi_(nullptr)
  , bjet1_isReconstructed_(nullptr)
  , bjet2_eta_(nullptr)
  , bjet2_phi_(nullptr)
  , bjet2_isReconstructed_(nullptr)
  , type_(nullptr)
  , m_HH_hme_(nullptr)
  , cpuTime_(nullptr)
  , realTime_(nullptr)
  , isValid_(nullptr)
  , errorFlag_(nullptr)
{
  setBranchNames();
}

HMEOutputWriter_hh_bb2l::~HMEOutputWriter_hh_bb2l()
{
  delete[] run_;
  delete[] lumi_;
  delete[] evt_;
  delete[] leadLepton_eta_;
  delete[] leadLepton_phi_;
  delete[] subleadLepton_eta_;
  delete[] subleadLepton_phi_;
  delete[] bjet1_eta_;
  delete[] bjet1_phi_;
  delete[] bjet1_isReconstructed_;
  delete[] bjet2_eta_;
  delete[] bjet2_phi_;
  delete[] bjet2_isReconstructed_;
  delete[] type_;
  delete[] m_HH_hme_;
  delete[] cpuTime_;
  delete[] realTime_;
  delete[] isValid_;
  delete[] errorFlag_;
}

void HMEOutputWriter_hh_bb2l::setBranchNames()
{
  branchName_run_ = Form("%s_%s", branchName_obj_.data(), "run");
  branchName_lumi_ = Form("%s_%s", branchName_obj_.data(), "lumi");
  branchName_evt_ = Form("%s_%s", branchName_obj_.data(), "evt");
  branchName_leadLepton_eta_ = Form("%s_%s", branchName_obj_.data(), "leadLepton_eta");
  branchName_leadLepton_phi_ = Form("%s_%s", branchName_obj_.data(), "leadLepton_phi");
  branchName_subleadLepton_eta_ = Form("%s_%s", branchName_obj_.data(), "subleadLepton_eta");
  branchName_subleadLepton_phi_ = Form("%s_%s", branchName_obj_.data(), "subleadLepton_phi");
  branchName_bjet1_eta_ = Form("%s_%s", branchName_obj_.data(), "bjet1_eta");
  branchName_bjet1_phi_ = Form("%s_%s", branchName_obj_.data(), "bjet1_phi");
  branchName_bjet1_isReconstructed_ = Form("%s_%s", branchName_obj_.data(), "bjet1_isReconstructed");
  branchName_bjet2_eta_ = Form("%s_%s", branchName_obj_.data(), "bjet2_eta");
  branchName_bjet2_phi_ = Form("%s_%s", branchName_obj_.data(), "bjet2_phi");
  branchName_bjet2_isReconstructed_ = Form("%s_%s", branchName_obj_.data(), "bjet2_isReconstructed");
  branchName_type_ = Form("%s_%s", branchName_obj_.data(), "type");
  branchName_m_HH_hme_ = Form("%s_%s", branchName_obj_.data(), "m_HH_hme");
  branchName_cpuTime_ = Form("%s_%s", branchName_obj_.data(), "cpuTime");
  branchName_realTime_ = Form("%s_%s", branchName_obj_.data(), "realTime");
  branchName_isValid_ = Form("%s_%s", branchName_obj_.data(), "isValid");
  branchName_errorFlag_ = Form("%s_%s", branchName_obj_.data(), "errorFlag");
}

void
HMEOutputWriter_hh_bb2l::setBranches(TTree * tree)
{
  BranchAddressInitializer bai(tree, max_nHMEOutputs_, branchName_num_);
  bai.setBranch(nHMEOutputs_, branchName_num_);
  bai.setBranch(run_, branchName_run_);
  bai.setBranch(lumi_, branchName_lumi_);
  bai.setBranch(evt_, branchName_evt_);
  bai.setBranch(leadLepton_eta_, branchName_leadLepton_eta_);
  bai.setBranch(leadLepton_phi_, branchName_leadLepton_phi_);
  bai.setBranch(subleadLepton_eta_, branchName_subleadLepton_eta_);
  bai.setBranch(subleadLepton_phi_, branchName_subleadLepton_phi_);
  bai.setBranch(bjet1_eta_, branchName_bjet1_eta_);
  bai.setBranch(bjet1_phi_, branchName_bjet1_phi_);
  bai.setBranch(bjet1_isReconstructed_, branchName_bjet1_isReconstructed_);
  bai.setBranch(bjet2_eta_, branchName_bjet2_eta_);
  bai.setBranch(bjet2_phi_, branchName_bjet2_phi_);
  bai.setBranch(bjet2_isReconstructed_, branchName_bjet2_isReconstructed_);
  bai.setBranch(type_, branchName_type_);
  bai.setBranch(m_HH_hme_, branchName_m_HH_hme_);
  bai.setBranch(cpuTime_, branchName_cpuTime_);
  bai.setBranch(realTime_, branchName_realTime_);
  bai.setBranch(isValid_, branchName_isValid_);
  bai.setBranch(errorFlag_, branchName_errorFlag_);
}

void HMEOutputWriter_hh_bb2l::write(const std::vector<HMEOutput_hh_bb2l> & hmeOutputs)
{
  nHMEOutputs_ = hmeOutputs.size();
  if(nHMEOutputs_ > max_nHMEOutputs_)
  {
    std::cout << "Warning: Number of HMEOutputs computed = " << nHMEOutputs_ << ", exceeds max_nHMEOutputs = "
              << max_nHMEOutputs_ << " that can be stored in Ntuple --> truncating the collection after "
              << max_nHMEOutputs_ << " objects !!\n";
    nHMEOutputs_ = max_nHMEOutputs_;
  }

  for(Int_t idxHMEOutput = 0; idxHMEOutput < nHMEOutputs_; ++idxHMEOutput)
  {
    const HMEOutput_hh_bb2l & hmeOutput = hmeOutputs[idxHMEOutput];
    run_[idxHMEOutput] = hmeOutput.eventInfo_.run;
    lumi_[idxHMEOutput] = hmeOutput.eventInfo_.lumi;
    evt_[idxHMEOutput] = hmeOutput.eventInfo_.event;
    leadLepton_eta_[idxHMEOutput] = hmeOutput.leadLepton_eta_;
    leadLepton_phi_[idxHMEOutput] = hmeOutput.leadLepton_phi_;
    subleadLepton_eta_[idxHMEOutput] = hmeOutput.subleadLepton_eta_;
    subleadLepton_phi_[idxHMEOutput] = hmeOutput.subleadLepton_phi_;
    bjet1_eta_[idxHMEOutput] = hmeOutput.bjet1_eta_;
    bjet1_phi_[idxHMEOutput] = hmeOutput.bjet1_phi_;
    bjet1_isReconstructed_[idxHMEOutput] = hmeOutput.bjet1_isReconstructed_;
    bjet2_eta_[idxHMEOutput] = hmeOutput.bjet2_eta_;
    bjet2_phi_[idxHMEOutput] = hmeOutput.bjet2_phi_;
    bjet2_isReconstructed_[idxHMEOutput] = hmeOutput.bjet2_isReconstructed_;
    type_[idxHMEOutput] = hmeOutput.type();
    m_HH_hme_[idxHMEOutput] = hmeOutput.m_HH_hme();
    cpuTime_[idxHMEOutput] = hmeOutput.cpuTime();
    realTime_[idxHMEOutput] = hmeOutput.realTime();
    isValid_[idxHMEOutput] = hmeOutput.isValid();
    errorFlag_[idxHMEOutput] = hmeOutput.errorFlag();
  }
}
