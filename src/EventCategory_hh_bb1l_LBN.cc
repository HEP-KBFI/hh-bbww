#include "hhAnalysis/bbww/interface/EventCategory_hh_bb1l_LBN.h"

#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h" // cmsException

EventCategory_hh_bb1l_LBN::EventCategory_hh_bb1l_LBN()
  : isBoosted_(false)
  , numBJets_(-1)
  , isVBF_(false)
{
  categoryMap_ = {
    { kUndefined,              "undefined"             },
    { kHH_boosted,             "HH_boosted"            },
    { kHH_resolved_2b,         "HH_resolved_2b"        },
    { kHH_resolved_2b_vbf,     "HH_resolved_2b_vbf"    },
    { kHH_resolved_2b_nonvbf,  "HH_resolved_2b_nonvbf" },
    { kHH_resolved_1b,         "HH_resolved_1b"        },
    { kTT_boosted,             "TT_boosted"            },
    { kTT_resolved,            "TT_resolved"           },
    { kW_boosted,              "W_boosted"             },
    { kW_resolved,             "W_resolved"            },
    { kDY_boosted,             "DY_boosted"            },
    { kDY_resolved,            "DY_resolved"           },
    { kSingleTop_boosted,      "SingleTop_boosted"     },
    { kSingleTop_resolved,     "SingleTop_resolved"    },
    { kOther,                  "Other"                 }
  };
  initialize();
}

void 
EventCategory_hh_bb1l_LBN::set(bool isBoosted, int numBJets, bool isVBF)
{
  isBoosted_ = isBoosted;
  numBJets_ = numBJets;
  isVBF_ = isVBF;
  isInitialized_ = true;
}

bool 
EventCategory_hh_bb1l_LBN::isSelected(int for_category, const std::string & for_class) const
{
  if ( !isInitialized_ )
    throw cmsException(this, __func__, __LINE__)
            << "EventCategory_hh_bb1l_BDT object has not been initialized." 
            << " You need to call the 'set' function before calling the 'isSelected' function !!\n";
  if      ( for_category == (int)kUndefined             ) return false;
  else if ( for_category == (int)kHH_boosted            ) return for_class == "HH"    &&  isBoosted_;
  else if ( for_category == (int)kHH_resolved_2b        ) return for_class == "HH"    && !isBoosted_ && numBJets_ == 2;
  else if ( for_category == (int)kHH_resolved_2b_vbf    ) return for_class == "HH"    && !isBoosted_ && numBJets_ == 2 &&  isVBF_;
  else if ( for_category == (int)kHH_resolved_2b_nonvbf ) return for_class == "HH"    && !isBoosted_ && numBJets_ == 2 && !isVBF_;
  else if ( for_category == (int)kHH_resolved_1b        ) return for_class == "HH"    && !isBoosted_ && numBJets_ == 1;
  else if ( for_category == (int)kTT_boosted            ) return for_class == "TT"    &&  isBoosted_;
  else if ( for_category == (int)kTT_resolved           ) return for_class == "TT"    && !isBoosted_;
  else if ( for_category == (int)kW_boosted             ) return for_class == "W"     &&  isBoosted_;
  else if ( for_category == (int)kW_resolved            ) return for_class == "W"     && !isBoosted_;
  else if ( for_category == (int)kDY_boosted            ) return for_class == "DY"    &&  isBoosted_;
  else if ( for_category == (int)kDY_resolved           ) return for_class == "DY"    && !isBoosted_;
  else if ( for_category == (int)kSingleTop_boosted     ) return for_class == "ST"    &&  isBoosted_;
  else if ( for_category == (int)kSingleTop_resolved    ) return for_class == "ST"    && !isBoosted_;
  else if ( for_category == (int)kOther                 ) return for_class == "Other";
  else throw cmsException(this, __func__, __LINE__)
               << "Invalid parameter 'category' = " << for_category << " !!\n";
}
