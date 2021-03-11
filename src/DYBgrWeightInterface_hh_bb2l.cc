#include "hhAnalysis/bbww/interface/DYBgrWeightInterface_hh_bb2l.h"

#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h" // cmsException()

#include <cmath> // std::sqrt()

namespace
{
  std::string
  getFileName(Era era, DYBgrWeightInterface_hh_bb2l::LeptonFlavor leptonFlavor, bool isBoosted, bool isMCClosure)
  {
    std::string fileName = "hhAnalysis/bbww/data/DrellYanWeights/weight";
    if ( isBoosted ) fileName.append("_fatjetsoftDropmass");
    else fileName.append("_HT");
    if      ( leptonFlavor == DYBgrWeightInterface_hh_bb2l::LeptonFlavor::kElecElec ) fileName.append("_ElEl");
    else if ( leptonFlavor == DYBgrWeightInterface_hh_bb2l::LeptonFlavor::kMuMu     ) fileName.append("_MuMu");
    else throw cmsException(__func__, __LINE__)
      << "Invalid Configuration parameter 'leptonFlavor' = " << leptonFlavor << " !!\n";
    if ( isMCClosure ) fileName.append("_mc");
    else fileName.append("_data");
    fileName.append("_1D");
    if      ( era == Era::k2016 ) fileName.append("_2016");
    else if ( era == Era::k2017 ) fileName.append("_2017");
    else if ( era == Era::k2018 ) fileName.append("_2018");
    else throw cmsException(__func__, __LINE__)
      << "Invalid Configuration parameter 'era' = " << (int)era << " !!\n";
    fileName.append(".root");
    return fileName;
  }
}

DYBgrWeightInterface_hh_bb2l::DYBgrWeightInterface_hh_bb2l(Era era, bool isMCClosure)
  : era_(era)
  , isMCClosure_(isMCClosure)
  , weight_ee_resolved_1b_(nullptr)
  , weight_ee_resolved_2b_(nullptr)
  , weight_ee_boosted_(nullptr)
  , weight_mm_resolved_1b_(nullptr)
  , weight_mm_resolved_2b_(nullptr)
  , weight_mm_boosted_(nullptr)
{
  weight_ee_resolved_1b_ = new lutWrapperTH1(
    inputFiles_,
    getFileName(era_, kElecElec, false, isMCClosure_),
    "Weight1B",
    lut::kXpt, 50., 1000., lut::kLimit
  );
  weight_ee_resolved_2b_ = new lutWrapperTH1(
    inputFiles_,
    getFileName(era_, kElecElec, false, isMCClosure_),
    "Weight2B",
    lut::kXpt, 50., 1000., lut::kLimit
  );
  weight_ee_boosted_ = new lutWrapperTH1(
    inputFiles_,
    getFileName(era_, kElecElec, true, isMCClosure_),
    "Weight1B",
    lut::kXpt, 30., 210., lut::kLimit
  );

  weight_mm_resolved_1b_ = new lutWrapperTH1(
    inputFiles_,
    getFileName(era_, kMuMu, false, isMCClosure_),
    "Weight1B",
    lut::kXpt, 50., 1000., lut::kLimit
  );
  weight_mm_resolved_2b_ = new lutWrapperTH1(
    inputFiles_,
    getFileName(era_, kMuMu, false, isMCClosure_),
    "Weight2B",
    lut::kXpt, 50., 1000., lut::kLimit
  );
  weight_mm_boosted_ = new lutWrapperTH1(
    inputFiles_,
    getFileName(era_, kMuMu, true, isMCClosure_),
    "Weight1B",
    lut::kXpt, 30., 210., lut::kLimit
  );
}

DYBgrWeightInterface_hh_bb2l::~DYBgrWeightInterface_hh_bb2l()
{
  delete weight_ee_resolved_1b_;
  delete weight_ee_resolved_2b_;
  delete weight_ee_boosted_;

  delete weight_mm_resolved_1b_;
  delete weight_mm_resolved_2b_;
  delete weight_mm_boosted_;

  for(auto & kv: inputFiles_)
  {
    delete kv.second;
  }
}

double
DYBgrWeightInterface_hh_bb2l::getWeight_resolved(double HT, LeptonFlavor leptonFlavor, int numBJets) const
{
  double weight = 1.;
  if ( leptonFlavor == kElecElec ) 
  {
    if      ( numBJets == 1 ) weight = weight_ee_resolved_1b_->getSF(HT, -1.);
    else if ( numBJets == 2 ) weight = weight_ee_resolved_2b_->getSF(HT, -1.);
    else throw cmsException(this, __func__, __LINE__)
      << "Invalid parameter 'numBJets' = " << numBJets << " !!\n";
  }
  else if ( leptonFlavor == kElecMu ) 
  {
    if      ( numBJets == 1 ) weight = std::sqrt(weight_ee_resolved_1b_->getSF(HT, -1.)*weight_mm_resolved_1b_->getSF(HT, -1.));
    else if ( numBJets == 2 ) weight = std::sqrt(weight_ee_resolved_2b_->getSF(HT, -1.)*weight_mm_resolved_2b_->getSF(HT, -1.));
    else throw cmsException(this, __func__, __LINE__)
      << "Invalid parameter 'numBJets' = " << numBJets << " !!\n";
  }
  else if ( leptonFlavor == kMuMu ) 
  {
    if      ( numBJets == 1 ) weight = weight_mm_resolved_1b_->getSF(HT, -1.);
    else if ( numBJets == 2 ) weight = weight_mm_resolved_2b_->getSF(HT, -1.);
    else throw cmsException(this, __func__, __LINE__)
      << "Invalid parameter 'numBJets' = " << numBJets << " !!\n";
  }
  else throw cmsException(this, __func__, __LINE__)
    << "Invalid parameter 'leptonFlavor' = " << leptonFlavor << " !!\n";
  return weight;
}

double
DYBgrWeightInterface_hh_bb2l::getWeight_boosted(double msoftdrop, LeptonFlavor leptonFlavor) const
{
  double weight = 1.;
  if ( leptonFlavor == kElecElec ) 
  {
    weight = weight_ee_boosted_->getSF(msoftdrop, -1.);
  }
  else if ( leptonFlavor == kElecMu ) 
  {
    weight = std::sqrt(weight_ee_boosted_->getSF(msoftdrop, -1.)*weight_mm_boosted_->getSF(msoftdrop, -1.));
  }
  else if ( leptonFlavor == kMuMu ) 
  {
    weight = weight_mm_boosted_->getSF(msoftdrop, -1.);
  }
  else throw cmsException(this, __func__, __LINE__)
    << "Invalid parameter 'leptonFlavor' = " << leptonFlavor << " !!\n";
  return weight;
}
