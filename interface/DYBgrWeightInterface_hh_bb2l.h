#ifndef hhAnalysis_bbww_DYBgrWeightInterface_hh_bb2l_h
#define hhAnalysis_bbww_DYBgrWeightInterface_hh_bb2l_h

#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // Era
#include "tthAnalysis/HiggsToTauTau/interface/lutAuxFunctions.h"      // lutWrapperBase

#include <TFile.h>

#include <string>
#include <map>

class DYBgrWeightInterface_hh_bb2l
{
public:
  DYBgrWeightInterface_hh_bb2l(Era era, bool isMCClosure);
  ~DYBgrWeightInterface_hh_bb2l();

  double
  getWeight_resolved(double HT, int numBJets) const;

  double
  getWeight_boosted(double msoftdrop) const;

protected:
  Era era_;
  bool isMCClosure_;

  std::map<std::string, TFile *> inputFiles_;

  lutWrapperBase * weight_resolved_1b_;
  lutWrapperBase * weight_resolved_2b_;
  lutWrapperBase * weight_boosted_;
};

#endif // hhAnalysis_bbww_DYBgrWeightInterface_hh_bb2l_h
