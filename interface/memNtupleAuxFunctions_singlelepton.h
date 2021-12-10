#ifndef hhAnalysis_bbww_memNtupleAuxFunctions_singlelepton_h
#define hhAnalysis_bbww_memNtupleAuxFunctions_singlelepton_h

#include "tthAnalysis/HiggsToTauTau/interface/RecoJet.h"    // RecoJet
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetAK8.h" // RecoJetAK8
#include "tthAnalysis/HiggsToTauTau/interface/GenJet.h"     // GenJet
#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h" // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/GenLepton.h"  // GenLepton

#include "hhAnalysis/bbwwMEM/interface/MeasuredParticle.h"  // MeasuredParticle
#include "hhAnalysis/bbwwMEM/interface/MEMResult.h"         // MEMResultBase

#include "hhAnalysis/bbwwMEMPerformanceStudies/interface/MEMEvent_singlelepton.h" // MEMEvent_singlelepton

#include <TMatrixD.h>                                       // TMatrixD

std::vector<MEMEvent_singlelepton>
buildMEMEvents_singlelepton_boosted(const EventInfo & eventInfo, bool isSignal,
                                    const std::vector<const std::pair<mem::MeasuredParticle, mem::MeasuredParticle>*> & measuredJetsAK8_Hbb,
                                    const std::vector<const std::pair<mem::MeasuredParticle, mem::MeasuredParticle>*> & measuredJetsAK8_Wjj,
                                    const std::vector<const mem::MeasuredParticle*> & measuredLeptons,
                                    double measuredMEtPx, double measuredMEtPy, const TMatrixD & measuredMEtCov);

std::vector<MEMEvent_singlelepton>
buildMEMEvents_singlelepton_semiboosted(const EventInfo & eventInfo, bool isSignal,
                                        const std::vector<const std::pair<mem::MeasuredParticle, mem::MeasuredParticle>*> & measuredJetsAK8_Hbb,
                                        const std::vector<const mem::MeasuredParticle*> & measuredJetsAK4_Wjj, int numWJets,
                                        const std::vector<const mem::MeasuredParticle*> & measuredLeptons,
                                        double measuredMEtPx, double measuredMEtPy, const TMatrixD & measuredMEtCov);

std::vector<MEMEvent_singlelepton>
buildMEMEvents_singlelepton_resolved(const EventInfo & eventInfo, bool isSignal,
                                     const std::vector<const mem::MeasuredParticle*> & measuredJetsAK4_Hbb, int numBJets, 
                                     const std::vector<const mem::MeasuredParticle*> & measuredJetsAK4_Wjj, int numWJets,
                                     const std::vector<const mem::MeasuredParticle*> & measuredLeptons,
                                     double measuredMEtPx, double measuredMEtPy, const TMatrixD & measuredMEtCov);

void
addGenMatches_singlelepton(std::vector<MEMEvent_singlelepton> & memEvents,
              const std::vector<const GenJet*> & genBJets,
              const std::vector<const GenJet*> & genWJets,
              const std::vector<const GenLepton*> & genLeptons,
              double genMEtPx, double genMEtPy);

std::map<int, std::vector<const MEMEvent_singlelepton*>>
buildMEMEventMap_singlelepton(const std::vector<MEMEvent_singlelepton> & memEvents);

#endif
