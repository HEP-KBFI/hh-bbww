#ifndef hhAnalysis_bbww_jpaAuxFunctions_h
#define hhAnalysis_bbww_jpaAuxFunctions_h

#include "tthAnalysis/HiggsToTauTau/interface/RecoJet.h"    // RecoJet
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetAK8.h" // RecoJetAK8
#include "hhAnalysis/bbww/interface/JPAInterface.h"         // JPAJet

#include <vector> // std::vector

JPAJet 
convert_to_JPAJet(const RecoJet* ak4Jet);

std::pair<JPAJet, JPAJet> 
convert_to_JPAJets(const RecoJetAK8* ak8Jet);

const RecoJetBase* 
convert_to_RecoJet(const JPAJet* ak4Jet_jpa, const std::vector<const RecoJet*>& ak4Jets);

#endif
