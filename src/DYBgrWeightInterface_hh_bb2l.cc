#include "hhAnalysis/bbww/interface/DYBgrWeightInterface_hh_bb2l.h"

#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h" // cmsException()

#include <cmath> // std::sqrt()

namespace
{
  std::string
  getFileName(Era era, bool isBoosted, bool isMCClosure)
  {
    std::string fileName = "hhAnalysis/bbww/data/DYBgrWeights/weight";
    if ( isBoosted ) fileName.append("_fatjetsoftDropmass");
    else fileName.append("_HT");
    fileName.append("_SF");
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
  , weight_resolved_1b_(nullptr)
  , weight_resolved_2b_(nullptr)
  , weight_boosted_(nullptr)
{
  weight_resolved_1b_ = new lutWrapperTH1(
    inputFiles_,
    getFileName(era_, false, isMCClosure_),
    "Weight1B",
    lut::kXpt, 50., 1000., lut::kLimit
  );
  weight_resolved_2b_ = new lutWrapperTH1(
    inputFiles_,
    getFileName(era_, false, isMCClosure_),
    "Weight2B",
    lut::kXpt, 50., 1000., lut::kLimit
  );
  weight_boosted_ = new lutWrapperTH1(
    inputFiles_,
    getFileName(era_, true, isMCClosure_),
    "Weight1B",
    lut::kXpt, 30., 210., lut::kLimit
  );
}

DYBgrWeightInterface_hh_bb2l::~DYBgrWeightInterface_hh_bb2l()
{
  delete weight_resolved_1b_;
  delete weight_resolved_2b_;
  delete weight_boosted_;

  for(auto & kv: inputFiles_)
  {
    delete kv.second;
  }
}

double
DYBgrWeightInterface_hh_bb2l::getWeight_resolved(double HT, int numBJets) const
{
  double weight = 1.;
  if      ( numBJets == 1 ) weight = weight_resolved_1b_->getSF(HT, -1.);
  else if ( numBJets == 2 ) weight = weight_resolved_2b_->getSF(HT, -1.);
  else throw cmsException(this, __func__, __LINE__)
    << "Invalid parameter 'numBJets' = " << numBJets << " !!\n";
  return weight;
}

double
DYBgrWeightInterface_hh_bb2l::getWeight_boosted(double msoftdrop) const
{
  double weight = weight_boosted_->getSF(msoftdrop, -1.);
  return weight;
}
