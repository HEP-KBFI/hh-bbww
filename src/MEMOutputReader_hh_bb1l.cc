#include "hhAnalysis/bbww/interface/MEMOutputReader_hh_bb1l.h" // MEMOutputReader_hh_bb1l

#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h" // cmsException()
#include "tthAnalysis/HiggsToTauTau/interface/BranchAddressInitializer.h" // BranchAddressInitializer, TTree, Form()

#include <cassert> // assert()

std::map<std::string, int> MEMOutputReader_hh_bb1l::numInstances_;
std::map<std::string, MEMOutputReader_hh_bb1l *> MEMOutputReader_hh_bb1l::instances_;

MEMOutputReader_hh_bb1l::MEMOutputReader_hh_bb1l(const std::string & branchName_num,
						 const std::string & branchName_obj)
  : max_nMEMOutputs_(100)
  , branchName_num_(branchName_num)
  , branchName_obj_(branchName_obj)
  , run_(nullptr)
  , lumi_(nullptr)
  , evt_(nullptr)
  , lepton_eta_(nullptr)
  , lepton_phi_(nullptr)
  , wjet1_eta_(nullptr)
  , wjet1_phi_(nullptr)
  , wjet1_isReconstructed_(nullptr)
  , wjet2_eta_(nullptr)
  , wjet2_phi_(nullptr)
  , wjet2_isReconstructed_(nullptr)
  , bjet1_eta_(nullptr)
  , bjet1_phi_(nullptr)
  , bjet1_isReconstructed_(nullptr)
  , bjet2_eta_(nullptr)
  , bjet2_phi_(nullptr)
  , bjet2_isReconstructed_(nullptr)
  , type_(nullptr)
  , weight_signal_(nullptr)
  , weightErr_signal_(nullptr)
  , weight_background_(nullptr)
  , weightErr_background_(nullptr)
  , LR_(nullptr)
  , cpuTime_(nullptr)
  , realTime_(nullptr)
  , isValid_(nullptr)
  , errorFlag_(nullptr)
{
  setBranchNames();
}

MEMOutputReader_hh_bb1l::~MEMOutputReader_hh_bb1l()
{
  --numInstances_[branchName_obj_];
  assert(numInstances_[branchName_obj_] >= 0);
  if(numInstances_[branchName_obj_] == 0)
  {
    MEMOutputReader_hh_bb1l* gInstance = instances_[branchName_obj_];
    assert(gInstance);
    delete[] gInstance -> run_;
    delete[] gInstance -> lumi_;
    delete[] gInstance -> evt_;
    delete[] gInstance -> lepton_eta_;
    delete[] gInstance -> lepton_phi_;
    delete[] gInstance -> wjet1_eta_;
    delete[] gInstance -> wjet1_phi_;
    delete[] gInstance -> wjet1_isReconstructed_;
    delete[] gInstance -> wjet2_eta_;
    delete[] gInstance -> wjet2_phi_;
    delete[] gInstance -> wjet2_isReconstructed_;
    delete[] gInstance -> bjet1_eta_;
    delete[] gInstance -> bjet1_phi_;
    delete[] gInstance -> bjet1_isReconstructed_;
    delete[] gInstance -> bjet2_eta_;
    delete[] gInstance -> bjet2_phi_;
    delete[] gInstance -> bjet2_isReconstructed_;
    delete[] gInstance -> type_;
    delete[] gInstance -> weight_signal_;
    delete[] gInstance -> weightErr_signal_;
    delete[] gInstance -> weight_background_;
    delete[] gInstance -> weightErr_background_;
    delete[] gInstance -> LR_;
    delete[] gInstance -> cpuTime_;
    delete[] gInstance -> realTime_;
    delete[] gInstance -> isValid_;
    delete[] gInstance -> errorFlag_;
    instances_[branchName_obj_] = nullptr;
  }
}

void
MEMOutputReader_hh_bb1l::setBranchNames()
{
  if(numInstances_[branchName_obj_] == 0)
  {
    branchName_run_                   = Form("%s_%s", branchName_obj_.data(), "run");
    branchName_lumi_                  = Form("%s_%s", branchName_obj_.data(), "lumi");
    branchName_evt_                   = Form("%s_%s", branchName_obj_.data(), "evt");
    //branchName_lepton_eta_            = Form("%s_%s", branchName_obj_.data(), "lepton_eta");
    //branchName_lepton_phi_            = Form("%s_%s", branchName_obj_.data(), "lepton_phi");
    branchName_lepton_eta_            = Form("%s_%s", branchName_obj_.data(), "leadLepton_eta");
    branchName_lepton_phi_            = Form("%s_%s", branchName_obj_.data(), "leadLepton_phi");
    branchName_wjet1_eta_             = Form("%s_%s", branchName_obj_.data(), "wjet1_eta");
    branchName_wjet1_phi_             = Form("%s_%s", branchName_obj_.data(), "wjet1_phi");
    branchName_wjet1_isReconstructed_ = Form("%s_%s", branchName_obj_.data(), "wjet1_isReconstructed");
    branchName_wjet2_eta_             = Form("%s_%s", branchName_obj_.data(), "wjet2_eta");
    branchName_wjet2_phi_             = Form("%s_%s", branchName_obj_.data(), "wjet2_phi");
    branchName_wjet2_isReconstructed_ = Form("%s_%s", branchName_obj_.data(), "wjet2_isReconstructed");
    branchName_bjet1_eta_             = Form("%s_%s", branchName_obj_.data(), "bjet1_eta");
    branchName_bjet1_phi_             = Form("%s_%s", branchName_obj_.data(), "bjet1_phi");
    branchName_bjet1_isReconstructed_ = Form("%s_%s", branchName_obj_.data(), "bjet1_isReconstructed");
    branchName_bjet2_eta_             = Form("%s_%s", branchName_obj_.data(), "bjet2_eta");
    branchName_bjet2_phi_             = Form("%s_%s", branchName_obj_.data(), "bjet2_phi");
    branchName_bjet2_isReconstructed_ = Form("%s_%s", branchName_obj_.data(), "bjet2_isReconstructed");
    branchName_type_                  = Form("%s_%s", branchName_obj_.data(), "type");
    branchName_weight_signal_         = Form("%s_%s", branchName_obj_.data(), "weight_signal");
    //branchName_weightErr_signal_         = Form("%s_%s", branchName_obj_.data(), "weightErr_signal");
    branchName_weight_background_     = Form("%s_%s", branchName_obj_.data(), "weight_background");
    //branchName_weightErr_background_     = Form("%s_%s", branchName_obj_.data(), "weightErr_background");
    branchName_LR_                    = Form("%s_%s", branchName_obj_.data(), "LR");
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
MEMOutputReader_hh_bb1l::setBranchAddresses(TTree * tree)
{
  if(instances_[branchName_obj_] == this)
  {
    BranchAddressInitializer bai(tree, max_nMEMOutputs_);
    bai.setBranchAddress(nMEMOutputs_, branchName_num_);
    bai.setBranchAddress(run_, branchName_run_);
    bai.setBranchAddress(lumi_, branchName_lumi_);
    bai.setBranchAddress(evt_, branchName_evt_);
    bai.setBranchAddress(lepton_eta_, branchName_lepton_eta_);
    bai.setBranchAddress(lepton_phi_, branchName_lepton_phi_);
    bai.setBranchAddress(wjet1_eta_, branchName_wjet1_eta_);
    bai.setBranchAddress(wjet1_phi_, branchName_wjet1_phi_);
    bai.setBranchAddress(wjet1_isReconstructed_, branchName_wjet1_isReconstructed_);
    bai.setBranchAddress(wjet2_eta_, branchName_wjet2_eta_);
    bai.setBranchAddress(wjet2_phi_, branchName_wjet2_phi_);
    bai.setBranchAddress(wjet2_isReconstructed_, branchName_wjet2_isReconstructed_);
    bai.setBranchAddress(bjet1_eta_, branchName_bjet1_eta_);
    bai.setBranchAddress(bjet1_phi_, branchName_bjet1_phi_);
    bai.setBranchAddress(bjet1_isReconstructed_, branchName_bjet1_isReconstructed_);
    bai.setBranchAddress(bjet2_eta_, branchName_bjet2_eta_);
    bai.setBranchAddress(bjet2_phi_, branchName_bjet2_phi_);
    bai.setBranchAddress(bjet2_isReconstructed_, branchName_bjet2_isReconstructed_);
    bai.setBranchAddress(type_, branchName_type_);
    bai.setBranchAddress(weight_signal_, branchName_weight_signal_);
    //bai.setBranchAddress(weightErr_signal_, branchName_weightErr_signal_);
    bai.setBranchAddress(weight_background_, branchName_weight_background_);
    //bai.setBranchAddress(weightErr_background_, branchName_weightErr_background_);
    bai.setBranchAddress(LR_, branchName_LR_);
    bai.setBranchAddress(cpuTime_, branchName_cpuTime_);
    bai.setBranchAddress(realTime_, branchName_realTime_);
    bai.setBranchAddress(errorFlag_, branchName_errorFlag_);
    bai.setBranchAddress(isValid_, branchName_isValid_);
  }
}

std::vector<MEMOutput_hh_bb1l>
MEMOutputReader_hh_bb1l::read() const
{
  MEMOutputReader_hh_bb1l* gInstance = instances_[branchName_obj_];
  assert(gInstance);
  Int_t nMEMOutputs = gInstance -> nMEMOutputs_;
  if(nMEMOutputs > max_nMEMOutputs_)
  {
    throw cmsException(this)
      << "Number of MEMOutputs stored in Ntuple = " << nMEMOutputs << ", "
         "exceeds max_nMEMOutputs = " << max_nMEMOutputs_ << " !!\n";
  }
  std::vector<MEMOutput_hh_bb1l> memOutputs;
  if(nMEMOutputs > 0)
  {
    memOutputs.reserve(nMEMOutputs);
    for(Int_t idxMEMOutput = 0; idxMEMOutput < nMEMOutputs; ++idxMEMOutput)
    {
      MEMOutput_hh_bb1l memOutput;
      memOutput.eventInfo_.run         = gInstance -> run_[idxMEMOutput];
      memOutput.eventInfo_.lumi        = gInstance -> lumi_[idxMEMOutput];
      memOutput.eventInfo_.event       = gInstance -> evt_[idxMEMOutput];
      memOutput.lepton_eta_            = gInstance -> lepton_eta_[idxMEMOutput];
      memOutput.lepton_phi_            = gInstance -> lepton_phi_[idxMEMOutput];
      memOutput.wjet1_eta_             = gInstance -> wjet1_eta_[idxMEMOutput];
      memOutput.wjet1_phi_             = gInstance -> wjet1_phi_[idxMEMOutput];
      memOutput.wjet1_isReconstructed_ = gInstance -> wjet1_isReconstructed_[idxMEMOutput];
      memOutput.wjet2_eta_             = gInstance -> wjet2_eta_[idxMEMOutput];
      memOutput.wjet2_phi_             = gInstance -> wjet2_phi_[idxMEMOutput];
      memOutput.wjet2_isReconstructed_ = gInstance -> wjet2_isReconstructed_[idxMEMOutput];
      memOutput.bjet1_eta_             = gInstance -> bjet1_eta_[idxMEMOutput];
      memOutput.bjet1_phi_             = gInstance -> bjet1_phi_[idxMEMOutput];
      memOutput.bjet1_isReconstructed_ = gInstance -> bjet1_isReconstructed_[idxMEMOutput];
      memOutput.bjet2_eta_             = gInstance -> bjet2_eta_[idxMEMOutput];
      memOutput.bjet2_phi_             = gInstance -> bjet2_phi_[idxMEMOutput];
      memOutput.bjet2_isReconstructed_ = gInstance -> bjet2_isReconstructed_[idxMEMOutput];
      memOutput.type_                  = gInstance -> type_[idxMEMOutput];
      memOutput.weight_signal_         = gInstance -> weight_signal_[idxMEMOutput];
      //      memOutput.weightErr_signal_         = gInstance -> weightErr_signal_[idxMEMOutput];
      memOutput.weight_background_     = gInstance -> weight_background_[idxMEMOutput];
      //memOutput.weightErr_background_     = gInstance -> weightErr_background_[idxMEMOutput];
      memOutput.LR_                    = gInstance -> LR_[idxMEMOutput];
      memOutput.cpuTime_               = gInstance -> cpuTime_[idxMEMOutput];
      memOutput.realTime_              = gInstance -> realTime_[idxMEMOutput];
      memOutput.isValid_               = gInstance -> isValid_[idxMEMOutput];
      memOutput.errorFlag_             = gInstance -> errorFlag_[idxMEMOutput];
      memOutputs.push_back(memOutput);
    }
  }
  return memOutputs;
}
