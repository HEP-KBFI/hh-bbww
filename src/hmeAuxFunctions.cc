#include "hhAnalysis/bbww/interface/hmeAuxFunctions.h" // get_addMEM_systematics() 
#include "tthAnalysis/HiggsToTauTau/interface/memAuxFunctions.h"
#include <TString.h> // Form()

std::string
get_hmeBranchName(const std::string & identifier,
                  const std::string & channel,
                  const std::string & lepSelection,
                  const std::string & hadTauSelection,
                  const std::string & hadTauWorkingPoint)
{
  if ( hadTauSelection != "" )
    {
      return Form(
		  "%s_%s_lep%s_tau%s_%s",
		  identifier.data(), channel.data(), lepSelection.data(), hadTauSelection.data(), hadTauWorkingPoint.data()
		  );
    }
  else
    {
      return Form(
		  "%s_%s_lep%s",
		  identifier.data(), channel.data(), lepSelection.data()
		  );
    }
}

std::string
get_hmeObjectBranchName(const std::string & channel,
                        const std::string & lepSelection,
                        const std::string & hadTauSelection,
                        const std::string & hadTauWorkingPoint)

{
  return get_memBranchName("hmeObjects", channel, lepSelection, hadTauSelection, hadTauWorkingPoint);
}

