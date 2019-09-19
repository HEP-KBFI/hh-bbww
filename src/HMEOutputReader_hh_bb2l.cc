#include "hhAnalysis/bbww/interface/HMEOutputReader_hh_bb2l.h" // HMEOutputReader_hh_bb2l

#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h" // cmsException()
#include "tthAnalysis/HiggsToTauTau/interface/BranchAddressInitializer.h" // BranchAddressInitializer, TTree, Form()

#include <cassert> // assert()

std::map<std::string, int> HMEOutputReader_hh_bb2l::numInstances_;
std::map<std::string, HMEOutputReader_hh_bb2l *> HMEOutputReader_hh_bb2l::instances_;

HMEOutputReader_hh_bb2l::HMEOutputReader_hh_bb2l(const std::string & branchName_num,
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

HMEOutputReader_hh_bb2l::~HMEOutputReader_hh_bb2l()
{
  --numInstances_[branchName_obj_];
  assert(numInstances_[branchName_obj_] >= 0);
  if(numInstances_[branchName_obj_] == 0)
  {
    HMEOutputReader_hh_bb2l* gInstance = instances_[branchName_obj_];
    assert(gInstance);
    delete[] gInstance -> run_;
    delete[] gInstance -> lumi_;
    delete[] gInstance -> evt_;
    delete[] gInstance -> leadLepton_eta_;
    delete[] gInstance -> leadLepton_phi_;
    delete[] gInstance -> subleadLepton_eta_;
    delete[] gInstance -> subleadLepton_phi_;
    delete[] gInstance -> bjet1_eta_;
    delete[] gInstance -> bjet1_phi_;
    delete[] gInstance -> bjet1_isReconstructed_;
    delete[] gInstance -> bjet2_eta_;
    delete[] gInstance -> bjet2_phi_;
    delete[] gInstance -> bjet2_isReconstructed_;
    delete[] gInstance -> type_;
    delete[] gInstance -> m_HH_hme_;
    delete[] gInstance -> cpuTime_;
    delete[] gInstance -> realTime_;
    delete[] gInstance -> isValid_;
    delete[] gInstance -> errorFlag_;
    instances_[branchName_obj_] = nullptr;
  }
}

void
HMEOutputReader_hh_bb2l::setBranchNames()
{
  if(numInstances_[branchName_obj_] == 0)
  {
    branchName_run_                   = Form("%s_%s", branchName_obj_.data(), "run");
    branchName_lumi_                  = Form("%s_%s", branchName_obj_.data(), "lumi");
    branchName_evt_                   = Form("%s_%s", branchName_obj_.data(), "evt");
    branchName_leadLepton_eta_        = Form("%s_%s", branchName_obj_.data(), "leadLepton_eta");
    branchName_leadLepton_phi_        = Form("%s_%s", branchName_obj_.data(), "leadLepton_phi");
    branchName_subleadLepton_eta_     = Form("%s_%s", branchName_obj_.data(), "subleadLepton_eta");
    branchName_subleadLepton_phi_     = Form("%s_%s", branchName_obj_.data(), "subleadLepton_phi");
    branchName_bjet1_eta_             = Form("%s_%s", branchName_obj_.data(), "bjet1_eta");
    branchName_bjet1_phi_             = Form("%s_%s", branchName_obj_.data(), "bjet1_phi");
    branchName_bjet1_isReconstructed_ = Form("%s_%s", branchName_obj_.data(), "bjet1_isReconstructed");
    branchName_bjet2_eta_             = Form("%s_%s", branchName_obj_.data(), "bjet2_eta");
    branchName_bjet2_phi_             = Form("%s_%s", branchName_obj_.data(), "bjet2_phi");
    branchName_bjet2_isReconstructed_ = Form("%s_%s", branchName_obj_.data(), "bjet2_isReconstructed");
    branchName_type_                  = Form("%s_%s", branchName_obj_.data(), "type");
    branchName_m_HH_hme_              = Form("%s_%s", branchName_obj_.data(), "m_HH_hme");
    branchName_cpuTime_               = Form("%s_%s", branchName_obj_.data(), "cpuTime");
    branchName_realTime_              = Form("%s_%s", branchName_obj_.data(), "realTime");
    branchName_isValid_               = Form("%s_%s", branchName_obj_.data(), "isValid");
    branchName_errorFlag_             = Form("%s_%s", branchName_obj_.data(), "errorFlag");
    instances_[branchName_obj_] = this;
  }
  else
  {
    if(branchName_num_ != instances_[branchName_obj_]->branchName_num_)
    {
      throw cmsException(this)
        << "Association between configuration parameters 'branchName_num' and 'branchName_obj' must be unique:"
           " present association 'branchName_num' = " << branchName_num_ << " with 'branchName_obj' = " << branchName_obj_
        << " does not match previous association 'branchName_num' = " << instances_[branchName_obj_] -> branchName_num_
        << " with 'branchName_obj' = " << instances_[branchName_obj_] -> branchName_obj_ << " !!\n";
    }
  }
  ++numInstances_[branchName_obj_];
}

void
HMEOutputReader_hh_bb2l::setBranchAddresses(TTree * tree)
{
  if(instances_[branchName_obj_] == this)
  {
    BranchAddressInitializer bai(tree, max_nHMEOutputs_);
    bai.setBranchAddress(nHMEOutputs_, branchName_num_);
    bai.setBranchAddress(run_, branchName_run_);
    bai.setBranchAddress(lumi_, branchName_lumi_);
    bai.setBranchAddress(evt_, branchName_evt_);
    bai.setBranchAddress(leadLepton_eta_, branchName_leadLepton_eta_);
    bai.setBranchAddress(leadLepton_phi_, branchName_leadLepton_phi_);
    bai.setBranchAddress(subleadLepton_eta_, branchName_subleadLepton_eta_);
    bai.setBranchAddress(subleadLepton_phi_, branchName_subleadLepton_phi_);
    bai.setBranchAddress(bjet1_eta_, branchName_bjet1_eta_);
    bai.setBranchAddress(bjet1_phi_, branchName_bjet1_phi_);
    bai.setBranchAddress(bjet1_isReconstructed_, branchName_bjet1_isReconstructed_);
    bai.setBranchAddress(bjet2_eta_, branchName_bjet2_eta_);
    bai.setBranchAddress(bjet2_phi_, branchName_bjet2_phi_);
    bai.setBranchAddress(bjet2_isReconstructed_, branchName_bjet2_isReconstructed_);
    bai.setBranchAddress(type_, branchName_type_);
    bai.setBranchAddress(m_HH_hme_, branchName_m_HH_hme_);
    bai.setBranchAddress(cpuTime_, branchName_cpuTime_);
    bai.setBranchAddress(realTime_, branchName_realTime_);
    bai.setBranchAddress(errorFlag_, branchName_errorFlag_);
    bai.setBranchAddress(isValid_, branchName_isValid_);
  }
}

std::vector<HMEOutput_hh_bb2l>
HMEOutputReader_hh_bb2l::read() const
{
  HMEOutputReader_hh_bb2l* gInstance = instances_[branchName_obj_];
  assert(gInstance);
  Int_t nHMEOutputs = gInstance -> nHMEOutputs_;
  if(nHMEOutputs > max_nHMEOutputs_)
  {
    throw cmsException(this)
      << "Number of HMEOutputs stored in Ntuple = " << nHMEOutputs << ", "
         "exceeds max_nHMEOutputs = " << max_nHMEOutputs_ << " !!\n";
  }
  std::vector<HMEOutput_hh_bb2l> hmeOutputs;
  if(nHMEOutputs > 0)
  {
    hmeOutputs.reserve(nHMEOutputs);
    for(Int_t idxHMEOutput = 0; idxHMEOutput < nHMEOutputs; ++idxHMEOutput)
    {
      HMEOutput_hh_bb2l hmeOutput;
      hmeOutput.eventInfo_.run         = gInstance -> run_[idxHMEOutput];
      hmeOutput.eventInfo_.lumi        = gInstance -> lumi_[idxHMEOutput];
      hmeOutput.eventInfo_.event       = gInstance -> evt_[idxHMEOutput];
      hmeOutput.leadLepton_eta_        = gInstance -> leadLepton_eta_[idxHMEOutput];
      hmeOutput.leadLepton_phi_        = gInstance -> leadLepton_phi_[idxHMEOutput];
      hmeOutput.subleadLepton_eta_     = gInstance -> subleadLepton_eta_[idxHMEOutput];
      hmeOutput.subleadLepton_phi_     = gInstance -> subleadLepton_phi_[idxHMEOutput];
      hmeOutput.bjet1_eta_             = gInstance -> bjet1_eta_[idxHMEOutput];
      hmeOutput.bjet1_phi_             = gInstance -> bjet1_phi_[idxHMEOutput];
      hmeOutput.bjet1_isReconstructed_ = gInstance -> bjet1_isReconstructed_[idxHMEOutput];
      hmeOutput.bjet2_eta_             = gInstance -> bjet2_eta_[idxHMEOutput];
      hmeOutput.bjet2_phi_             = gInstance -> bjet2_phi_[idxHMEOutput];
      hmeOutput.bjet2_isReconstructed_ = gInstance -> bjet2_isReconstructed_[idxHMEOutput];
      hmeOutput.type_                  = gInstance -> type_[idxHMEOutput];
      hmeOutput.m_HH_hme_              = gInstance -> m_HH_hme_[idxHMEOutput];
      hmeOutput.cpuTime_               = gInstance -> cpuTime_[idxHMEOutput];
      hmeOutput.realTime_              = gInstance -> realTime_[idxHMEOutput];
      hmeOutput.isValid_               = gInstance -> isValid_[idxHMEOutput];
      hmeOutput.errorFlag_             = gInstance -> errorFlag_[idxHMEOutput];
      hmeOutputs.push_back(hmeOutput);
    }
  }
  return hmeOutputs;
}
