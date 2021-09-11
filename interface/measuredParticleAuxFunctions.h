#ifndef hhAnalysis_bbww_measuredParticleAuxFunctions_h
#define hhAnalysis_bbww_measuredParticleAuxFunctions_h

#include "tthAnalysis/HiggsToTauTau/interface/RecoJet.h"    // RecoJet
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetAK8.h" // RecoJetAK8
#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h" // RecoLepton

#include "hhAnalysis/bbwwMEM/interface/MeasuredParticle.h"  // MeasuredParticle

#include <vector>                                           // std::vector
#include <utility>                                          // std::pair

mem::MeasuredParticle
convert_to_MeasuredParticle(const RecoLepton& lepton);
std::vector<mem::MeasuredParticle>
convert_to_MeasuredParticles(const std::vector<const RecoLepton*>& leptons);

std::pair<mem::MeasuredParticle, mem::MeasuredParticle>
convert_to_MeasuredParticle(const RecoJetAK8& jet, bool isHbb);
std::vector<std::pair<mem::MeasuredParticle, mem::MeasuredParticle>>
convert_to_MeasuredParticles(const std::vector<const RecoJetAK8*> jets, bool isHbb);

mem::MeasuredParticle
convert_to_MeasuredParticle(const RecoJet& jet, bool isBJet);
std::vector<mem::MeasuredParticle>
convert_to_MeasuredParticles(const std::vector<const RecoJet*>& jets, bool isBJet);

#endif
