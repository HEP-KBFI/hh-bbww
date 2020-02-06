#include "hhAnalysis/bbww/interface/MEMOutputWriter_hh_bb1l.h" // MEMOutputWriter_hh_bb1l

#include "tthAnalysis/HiggsToTauTau/interface/BranchAddressInitializer.h" // BranchAddressInitializer, TTree, Form()

MEMOutputWriter_hh_bb1l::MEMOutputWriter_hh_bb1l(const std::string & branchName_num,
						 const std::string & branchName_obj)
  : max_nMEMOutputs_(100)
  , branchName_num_(branchName_num)
  , branchName_obj_(branchName_obj)
  , nMEMOutputs_(0)
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

MEMOutputWriter_hh_bb1l::~MEMOutputWriter_hh_bb1l()
{
  delete[] run_;
  delete[] lumi_;
  delete[] evt_;
  delete[] lepton_eta_;
  delete[] lepton_phi_;
  delete[] wjet1_eta_;
  delete[] wjet1_phi_;
  delete[] wjet1_isReconstructed_;
  delete[] wjet2_eta_;
  delete[] wjet2_phi_;
  delete[] wjet2_isReconstructed_;
  delete[] bjet1_eta_;
  delete[] bjet1_phi_;
  delete[] bjet1_isReconstructed_;
  delete[] bjet2_eta_;
  delete[] bjet2_phi_;
  delete[] bjet2_isReconstructed_;
  delete[] type_;
  delete[] weight_signal_;
  delete[] weightErr_signal_;
  delete[] weight_background_;
  delete[] weightErr_background_;
  delete[] LR_;
  delete[] cpuTime_;
  delete[] realTime_;
  delete[] isValid_;
  delete[] errorFlag_;
}

void MEMOutputWriter_hh_bb1l::setBranchNames()
{
  branchName_run_ = Form("%s_%s", branchName_obj_.data(), "run");
  branchName_lumi_ = Form("%s_%s", branchName_obj_.data(), "lumi");
  branchName_evt_ = Form("%s_%s", branchName_obj_.data(), "evt");
  branchName_lepton_eta_ = Form("%s_%s", branchName_obj_.data(), "lepton_eta");
  branchName_lepton_phi_ = Form("%s_%s", branchName_obj_.data(), "lepton_phi");
  branchName_wjet1_eta_ = Form("%s_%s", branchName_obj_.data(), "wjet1_eta");
  branchName_wjet1_phi_ = Form("%s_%s", branchName_obj_.data(), "wjet1_phi");
  branchName_wjet1_isReconstructed_ = Form("%s_%s", branchName_obj_.data(), "wjet1_isReconstructed");
  branchName_wjet2_eta_ = Form("%s_%s", branchName_obj_.data(), "wjet2_eta");
  branchName_wjet2_phi_ = Form("%s_%s", branchName_obj_.data(), "wjet2_phi");
  branchName_wjet2_isReconstructed_ = Form("%s_%s", branchName_obj_.data(), "wjet2_isReconstructed");
  branchName_bjet1_eta_ = Form("%s_%s", branchName_obj_.data(), "bjet1_eta");
  branchName_bjet1_phi_ = Form("%s_%s", branchName_obj_.data(), "bjet1_phi");
  branchName_bjet1_isReconstructed_ = Form("%s_%s", branchName_obj_.data(), "bjet1_isReconstructed");
  branchName_bjet2_eta_ = Form("%s_%s", branchName_obj_.data(), "bjet2_eta");
  branchName_bjet2_phi_ = Form("%s_%s", branchName_obj_.data(), "bjet2_phi");
  branchName_bjet2_isReconstructed_ = Form("%s_%s", branchName_obj_.data(), "bjet2_isReconstructed");
  branchName_type_ = Form("%s_%s", branchName_obj_.data(), "type");
  branchName_weight_signal_ = Form("%s_%s", branchName_obj_.data(), "weight_signal");
  branchName_weightErr_signal_ = Form("%s_%s", branchName_obj_.data(), "weightErr_signal");
  branchName_weight_background_ = Form("%s_%s", branchName_obj_.data(), "weight_background");
  branchName_weightErr_background_ = Form("%s_%s", branchName_obj_.data(), "weightErr_background");
  branchName_LR_ = Form("%s_%s", branchName_obj_.data(), "LR");
  branchName_cpuTime_ = Form("%s_%s", branchName_obj_.data(), "cpuTime");
  branchName_realTime_ = Form("%s_%s", branchName_obj_.data(), "realTime");
  branchName_isValid_ = Form("%s_%s", branchName_obj_.data(), "isValid");
  branchName_errorFlag_ = Form("%s_%s", branchName_obj_.data(), "errorFlag");
}

void
MEMOutputWriter_hh_bb1l::setBranches(TTree * tree)
{
  BranchAddressInitializer bai(tree, max_nMEMOutputs_, branchName_num_);
  bai.setBranch(nMEMOutputs_, branchName_num_);
  bai.setBranch(run_, branchName_run_);
  bai.setBranch(lumi_, branchName_lumi_);
  bai.setBranch(evt_, branchName_evt_);
  bai.setBranch(lepton_eta_, branchName_lepton_eta_);
  bai.setBranch(lepton_phi_, branchName_lepton_phi_);
  bai.setBranch(wjet1_eta_, branchName_wjet1_eta_);
  bai.setBranch(wjet1_phi_, branchName_wjet1_phi_);
  bai.setBranch(wjet1_isReconstructed_, branchName_wjet1_isReconstructed_);
  bai.setBranch(wjet2_eta_, branchName_wjet2_eta_);
  bai.setBranch(wjet2_phi_, branchName_wjet2_phi_);
  bai.setBranch(wjet2_isReconstructed_, branchName_wjet2_isReconstructed_);
  bai.setBranch(bjet1_eta_, branchName_bjet1_eta_);
  bai.setBranch(bjet1_phi_, branchName_bjet1_phi_);
  bai.setBranch(bjet1_isReconstructed_, branchName_bjet1_isReconstructed_);
  bai.setBranch(bjet2_eta_, branchName_bjet2_eta_);
  bai.setBranch(bjet2_phi_, branchName_bjet2_phi_);
  bai.setBranch(bjet2_isReconstructed_, branchName_bjet2_isReconstructed_);
  bai.setBranch(type_, branchName_type_);
  bai.setBranch(weight_signal_, branchName_weight_signal_);
  bai.setBranch(weightErr_signal_, branchName_weightErr_signal_);
  bai.setBranch(weight_background_, branchName_weight_background_);
  bai.setBranch(weightErr_background_, branchName_weightErr_background_);
  bai.setBranch(LR_, branchName_LR_);
  bai.setBranch(cpuTime_, branchName_cpuTime_);
  bai.setBranch(realTime_, branchName_realTime_);
  bai.setBranch(isValid_, branchName_isValid_);
  bai.setBranch(errorFlag_, branchName_errorFlag_);
}

void MEMOutputWriter_hh_bb1l::write(const std::vector<MEMOutput_hh_bb1l> & memOutputs)
{
  nMEMOutputs_ = memOutputs.size();
  if(nMEMOutputs_ > max_nMEMOutputs_)
  {
    std::cout << "Warning: Number of MEMOutputs computed = " << nMEMOutputs_ << ", exceeds max_nMEMOutputs = "
              << max_nMEMOutputs_ << " that can be stored in Ntuple --> truncating the collection after "
              << max_nMEMOutputs_ << " objects !!\n";
    nMEMOutputs_ = max_nMEMOutputs_;
  }

  for(Int_t idxMEMOutput = 0; idxMEMOutput < nMEMOutputs_; ++idxMEMOutput)
  {
    const MEMOutput_hh_bb1l & memOutput = memOutputs[idxMEMOutput];
    run_[idxMEMOutput] = memOutput.eventInfo_.run;
    lumi_[idxMEMOutput] = memOutput.eventInfo_.lumi;
    evt_[idxMEMOutput] = memOutput.eventInfo_.event;
    lepton_eta_[idxMEMOutput] = memOutput.lepton_eta_;
    lepton_phi_[idxMEMOutput] = memOutput.lepton_phi_;
    wjet1_eta_[idxMEMOutput] = memOutput.wjet1_eta_;
    wjet1_phi_[idxMEMOutput] = memOutput.wjet1_phi_;
    wjet1_isReconstructed_[idxMEMOutput] = memOutput.wjet1_isReconstructed_;
    wjet2_eta_[idxMEMOutput] = memOutput.wjet2_eta_;
    wjet2_phi_[idxMEMOutput] = memOutput.wjet2_phi_;
    wjet2_isReconstructed_[idxMEMOutput] = memOutput.wjet2_isReconstructed_;
    bjet1_eta_[idxMEMOutput] = memOutput.bjet1_eta_;
    bjet1_phi_[idxMEMOutput] = memOutput.bjet1_phi_;
    bjet1_isReconstructed_[idxMEMOutput] = memOutput.bjet1_isReconstructed_;
    bjet2_eta_[idxMEMOutput] = memOutput.bjet2_eta_;
    bjet2_phi_[idxMEMOutput] = memOutput.bjet2_phi_;
    bjet2_isReconstructed_[idxMEMOutput] = memOutput.bjet2_isReconstructed_;
    type_[idxMEMOutput] = memOutput.type();
    weight_signal_[idxMEMOutput] = memOutput.weight_signal();
    weightErr_signal_[idxMEMOutput] = memOutput.weightErr_signal();
    weight_background_[idxMEMOutput] = memOutput.weight_background();
    weightErr_background_[idxMEMOutput] = memOutput.weightErr_background();
    LR_[idxMEMOutput] = memOutput.LR();
    cpuTime_[idxMEMOutput] = memOutput.cpuTime();
    realTime_[idxMEMOutput] = memOutput.realTime();
    isValid_[idxMEMOutput] = memOutput.isValid();
    errorFlag_[idxMEMOutput] = memOutput.errorFlag();
  }
}
