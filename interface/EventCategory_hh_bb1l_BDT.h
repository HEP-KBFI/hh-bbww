#ifndef hhAnalysis_bbww_EventCategory_hh_bb1l_BDT_h
#define hhAnalysis_bbww_EventCategory_hh_bb1l_BDT_h

/** \class EventCategoryBase
 *
 * Event categories used for BDT-based signal extraction
 * in HH->bbWW single lepton channel
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "FWCore/ParameterSet/interface/ParameterSet.h" // edm::ParameterSet

#include "hhAnalysis/multilepton/interface/EventCategory.h" // EventCategory

#include <vector>
#include <string>

class EventCategory_hh_bb1l_BDT
  : public EventCategory
{
 public:
  enum { 
    kUndefined = -1, 
    kBoosted, kResolved_2b, kResolved_2b_vbf, kResolved_2b_nonvbf, kResolved_1b 
  };
  EventCategory_hh_bb1l_BDT();
  ~EventCategory_hh_bb1l_BDT() {}

  void set(bool isBoosted, int numBJets, bool isVBF);

  bool isSelected(int for_category) const;
 
 private:
  bool isBoosted_;
  int numBJets_;
  bool isVBF_;
};

#endif
