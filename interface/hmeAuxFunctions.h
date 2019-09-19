#ifndef HMMAUXFUNCTIONS_H
#define HMEAUXFUNCTIONS_H

#include <string> // std::string

std::string
get_hmeBranchName(const std::string & identifier,
                  const std::string & channel,
                  const std::string & lepSelection,
                  const std::string & hadTauSelection,
                  const std::string & hadTauWorkingPoint);


std::string
get_hmeObjectBranchName(const std::string & channel,
                        const std::string & lepSelection,
                        const std::string & hadTauSelection,
                        const std::string & hadTauWorkingPoint);

#endif // HMEAUXFUNCTIONS_H
