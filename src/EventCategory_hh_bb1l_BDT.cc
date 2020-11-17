#include "hhAnalysis/bbww/interface/EventCategory_hh_bb1l_BDT.h"

#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h" // cmsException

EventCategory_hh_bb1l_BDT::EventCategory_hh_bb1l_BDT()
  : isBoosted_(false)
  , numBJets_(-1)
  , isVBF_(false)
{}

void 
EventCategory_hh_bb1l_BDT::set(bool isBoosted, int numBJets, bool isVBF)
{
  isBoosted_ = isBoosted;
  numBJets_ = numBJets;
  isVBF_ = isVBF;
  isInitialized_ = true;
}

bool 
EventCategory_hh_bb1l_BDT::isSelected(int for_category) const
{
  if ( !isInitialized_ )
    throw cmsException(this, __func__, __LINE__)
            << "EventCategory_hh_bb1l_BDT object has not been initialized. You need to call the 'set' function before calling the 'isSelected' function !!\n";
  if      ( for_category == (int)kBoosted            ) return  isBoosted_;
  else if ( for_category == (int)kResolved_2b        ) return !isBoosted_ && numBJets_ == 2;
  else if ( for_category == (int)kResolved_2b_vbf    ) return !isBoosted_ && numBJets_ == 2 &&  isVBF_;
  else if ( for_category == (int)kResolved_2b_nonvbf ) return !isBoosted_ && numBJets_ == 2 && !isVBF_;
  else if ( for_category == (int)kResolved_1b        ) return !isBoosted_ && numBJets_ == 1;
  else throw cmsException(this, __func__, __LINE__)
               << "Invalid parameter 'category' = " << for_category << " !!\n";
}
