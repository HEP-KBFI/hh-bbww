#include "hhAnalysis/bbww/interface/dumpGenParticles.h"

#include <iostream> // std::cerr, std::fixed
#include <iomanip> // std::setprecision(), std::setw()

void dumpGenLeptons(const std::string& label, const std::vector<GenLepton>& genLeptons)
{
  for ( size_t idxLepton = 0; idxLepton < genLeptons.size(); ++idxLepton ) {
    std::cout << label << " #" << idxLepton << ":" << " ";
    std::cout << genLeptons[idxLepton];
    std::cout << std::endl;
  }
}

void dumpGenParticles(const std::string& label, const std::vector<GenParticle>& genParticles)
{
  for ( size_t idxParticle = 0; idxParticle < genParticles.size(); ++idxParticle ) {
    std::cout << label << " #" << idxParticle << ":" << " ";
    std::cout << genParticles[idxParticle];
    std::cout << std::endl;
  }
}

void dumpGenJets(const std::string& label, const std::vector<GenJet>& genJets)
{
  for ( size_t idxJet = 0; idxJet < genJets.size(); ++idxJet ) {
    std::cout << label << " #" << idxJet << ":" << " ";
    std::cout << genJets[idxJet];
    std::cout << std::endl;
  }
}
