#ifndef hhAnalysis_bbww_memNtupleAuxFunctions_dilepton_h
#define hhAnalysis_bbww_memNtupleAuxFunctions_dilepton_h

#include "tthAnalysis/HiggsToTauTau/interface/RecoJet.h"    // RecoJet
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetAK8.h" // RecoJetAK8
#include "tthAnalysis/HiggsToTauTau/interface/GenJet.h"     // GenJet
#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h" // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/GenLepton.h"  // GenLepton

#include "hhAnalysis/bbwwMEM/interface/MeasuredParticle.h"  // MeasuredParticle
#include "hhAnalysis/bbwwMEM/interface/MEMResult.h"         // MEMResultBase

#include "hhAnalysis/bbwwMEMPerformanceStudies/interface/MEMEvent_dilepton.h" // MEMEvent_dilepton

#include <TMatrixD.h>                                       // TMatrixD

std::vector<MEMEvent_dilepton>
buildMEMEvents_dilepton_boosted(const EventInfo & eventInfo, bool isSignal,
                                const std::vector<const std::pair<mem::MeasuredParticle, mem::MeasuredParticle>*> & measuredJetsAK8_Hbb,
                                const std::vector<const mem::MeasuredParticle*> & measuredLeptons,
                                double measuredMEtPx, double measuredMEtPy, const TMatrixD & measuredMEtCov);

std::vector<MEMEvent_dilepton>
buildMEMEvents_dilepton_resolved(const EventInfo & eventInfo, bool isSignal,
                                 const std::vector<const mem::MeasuredParticle*> & measuredJetsAK4, int numBJets,
                                 const std::vector<const mem::MeasuredParticle*> & measuredLeptons,
                                 double measuredMEtPx, double measuredMEtPy, const TMatrixD & measuredMEtCov);

void
addGenMatches_dilepton(std::vector<MEMEvent_dilepton> & memEvents,
                       const std::vector<const GenJet*> & genBJets,
                       const std::vector<const GenLepton*> & genLeptons,
                       double genMEtPx, double genMEtPy);

std::map<int, std::vector<const MEMEvent_dilepton*>>
buildMEMEventMap_dilepton(const std::vector<MEMEvent_dilepton> & memEvents);

#endif
