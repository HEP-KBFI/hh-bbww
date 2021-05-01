#ifndef hhAnalysis_bbww_EventCategory_hh_bb1l_LBN_h
#define hhAnalysis_bbww_EventCategory_hh_bb1l_LBN_h

/** \class EventCategoryBase
 *
 * Event categories used for signal extraction based on Lorentz-Boost Network (LBN)
 * in HH->bbWW single lepton channel
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "hhAnalysis/multilepton/interface/EventCategory_multiclass.h"

#include <vector>
#include <string>

class EventCategory_hh_bb1l_LBN
  : public EventCategory_multiclass
{
 public:
  enum { 
    kUndefined = -1,
    kHH_boosted, kHH_resolved_2b_vbf, kHH_resolved_2b_nonvbf, kHH_resolved_1b_vbf, kHH_resolved_1b_nonvbf,
    kHH_resolved_2b, kHH_resolved_1b,
    kTT_boosted, kTT_resolved,
    kW_boosted, kW_resolved,
    kDY_boosted, kDY_resolved,
    kSingleTop_boosted, kSingleTop_resolved,
    kH_boosted, kH_resolved_2b, kH_resolved_1b,
    kOther
  };
  EventCategory_hh_bb1l_LBN(bool isNonRes=true);
  ~EventCategory_hh_bb1l_LBN() {}

  void set(bool isBoosted, int numBJets, bool isVBF);

  bool isSelected(int for_category, const std::string & for_class, bool isNonres) const;

 private:
  bool isBoosted_;
  int numBJets_;
  bool isVBF_;
};

#endif
