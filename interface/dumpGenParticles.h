#ifndef hhAnalysis_bbww_analyzeMEM_dumpGenParticles_h
#define hhAnalysis_bbww_analyzeMEM_dumpGenParticles_h

#include "tthAnalysis/HiggsToTauTau/interface/GenParticle.h" // GenParticle
#include "tthAnalysis/HiggsToTauTau/interface/GenLepton.h"   // GenLepton
#include "tthAnalysis/HiggsToTauTau/interface/GenJet.h"      // GenJet

#include <vector> // std::vector<>
#include <string> // std::string

void dumpGenLeptons(const std::string& label, const std::vector<GenLepton>& genLeptons);

void dumpGenParticles(const std::string& label, const std::vector<GenParticle>& genParticles);

void dumpGenJets(const std::string& label, const std::vector<GenJet>& genJets);

#endif // dumpGenParticles_h
