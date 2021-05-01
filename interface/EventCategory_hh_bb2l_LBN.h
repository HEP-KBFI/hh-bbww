#ifndef hhAnalysis_bbww_EventCategory_hh_bb2l_LBN_h
#define hhAnalysis_bbww_EventCategory_hh_bb2l_LBN_h

/** \class EventCategoryBase
 *
 * Event categories used for signal extraction based on Lorentz-Boost Network (LBN)
 * in HH->bbWW dilepton channel
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "hhAnalysis/multilepton/interface/EventCategory_multiclass.h"

#include <vector>
#include <string>

class EventCategory_hh_bb2l_LBN
  : public EventCategory_multiclass
{
 public:
  enum { 
    kUndefined = -1,
    kHH_boosted_vbf, kHH_boosted_nonvbf, kHH_resolved_2b_vbf, kHH_resolved_2b_nonvbf, kHH_resolved_1b_vbf, kHH_resolved_1b_nonvbf,
    kTT_boosted, kTT_resolved,
    kDY_boosted, kDY_resolved,
    kSingleTop_boosted, kSingleTop_resolved,
    kOther
  };
  EventCategory_hh_bb2l_LBN();
  ~EventCategory_hh_bb2l_LBN() {}

  void set(bool isBoosted, int numBJets, bool isVBF);

  bool isSelected(int for_category, const std::string & for_class, bool isNonRes) const;

 private:
  bool isBoosted_;
  int numBJets_;
  bool isVBF_;
};

#endif
