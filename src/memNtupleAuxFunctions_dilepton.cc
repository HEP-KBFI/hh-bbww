#include "hhAnalysis/bbww/interface/memNtupleAuxFunctions_dilepton.h"

#include "DataFormats/Math/interface/deltaR.h"                         // deltaR

#include "hhAnalysis/bbwwMEM/interface/measuredParticleAuxFunctions.h" // findGenMatch

std::vector<MEMEvent_dilepton>
buildMEMEvents_dilepton_boosted(const std::vector<const std::pair<mem::MeasuredParticle, mem::MeasuredParticle>*>& measuredJetsAK8_Hbb,
                                const std::vector<const mem::MeasuredParticle*>& measuredLeptons,
                                double measuredMEtPx, double measuredMEtPy, const TMatrixD& measuredMEtCov)
{
  std::vector<MEMEvent_dilepton> memEvents;
  for ( std::vector<const std::pair<mem::MeasuredParticle, mem::MeasuredParticle>*>::const_iterator measuredJet = measuredJetsAK8_Hbb.begin();
        measuredJet != measuredJetsAK8_Hbb.end(); ++measuredJet ) {
    for ( std::vector<const mem::MeasuredParticle*>::const_iterator lepton1 = measuredLeptons.begin();
          lepton1 != measuredLeptons.end(); ++lepton1 ) {
      for ( std::vector<const mem::MeasuredParticle*>::const_iterator lepton2 = lepton1 + 1;
            lepton2 != measuredLeptons.end(); ++lepton2 ) {
        MEMEvent_dilepton memEvent(
          &(*measuredJet)->first, &(*measuredJet)->second,
          *lepton1, *lepton2,
          measuredMEtPx, measuredMEtPy, measuredMEtCov);
        memEvent.isBoosted_Hbb_ = true;
        memEvents.push_back(memEvent);
      }
    }
  }
  return memEvents;
}

std::vector<MEMEvent_dilepton>
buildMEMEvents_dilepton_resolved(const std::vector<const mem::MeasuredParticle*>& measuredJetsAK4, int numBJets,
                                 const std::vector<const mem::MeasuredParticle*>& measuredLeptons,
                                 double measuredMEtPx, double measuredMEtPy, const TMatrixD& measuredMEtCov)
{
  assert(numBJets == 1 || numBJets == 2);
  std::vector<const mem::MeasuredParticle*> bjets1 = measuredJetsAK4;
  std::vector<const mem::MeasuredParticle*> bjets2 = ( numBJets == 2 ) ? measuredJetsAK4 : std::vector<const mem::MeasuredParticle*>({ nullptr });
  std::vector<MEMEvent_dilepton> memEvents;
  for ( std::vector<const mem::MeasuredParticle*>::const_iterator bjet1 = bjets1.begin();
        bjet1 != bjets1.end(); ++bjet1 ) {
    for ( std::vector<const mem::MeasuredParticle*>::const_iterator bjet2 = bjets2.begin();
          bjet2 != bjets2.end(); ++bjet2 ) {
      assert(!((*bjet1) == nullptr && (*bjet2) != nullptr));
      if ( (*bjet1) && (*bjet2) ) {
        if ( !((*bjet1)->pt() >= (*bjet2)->pt()) ) continue;
        if ( deltaR((*bjet1)->p4(), (*bjet2)->p4()) < 0.3 ) continue;
      }
      for ( std::vector<const mem::MeasuredParticle*>::const_iterator lepton1 = measuredLeptons.begin();
            lepton1 != measuredLeptons.end(); ++lepton1 ) {
        for ( std::vector<const mem::MeasuredParticle*>::const_iterator lepton2 = lepton1 + 1;
              lepton2 != measuredLeptons.end(); ++lepton2 ) {
          MEMEvent_dilepton memEvent(
            *bjet1, *bjet2,
            *lepton1, *lepton2,
            measuredMEtPx, measuredMEtPy, measuredMEtCov);
          memEvent.isBoosted_Hbb_ = false;
          memEvents.push_back(memEvent);
        }
      }
    }
  }
  return memEvents;
}

void
addGenMatches_dilepton(std::vector<MEMEvent_dilepton>& memEvents,
                       const std::vector<const GenJet*>& genBJets,
                       const std::vector<const GenLepton*>& genLeptons,
                       double genMEtPx, double genMEtPy)
{
  for ( std::vector<MEMEvent_dilepton>::iterator memEvent = memEvents.begin();
        memEvent != memEvents.end(); ++memEvent ) {
    memEvent->genBJet1_   = mem::findGenMatch(memEvent->measuredBJet1_,   genBJets);
    memEvent->genBJet2_   = mem::findGenMatch(memEvent->measuredBJet2_,   genBJets);
    memEvent->genLepton1_ = mem::findGenMatch(memEvent->measuredLepton1_, genLeptons);
    memEvent->genLepton2_ = mem::findGenMatch(memEvent->measuredLepton2_, genLeptons);
  }
}

std::map<int, std::vector<const MEMEvent_dilepton*>>
buildMEMEventMap_dilepton(const std::vector<MEMEvent_dilepton>& memEvents)
{
  std::map<int, std::vector<const MEMEvent_dilepton*>> memEventMap;
  for ( std::vector<MEMEvent_dilepton>::const_iterator memEvent = memEvents.begin();
        memEvent != memEvents.end(); ++memEvent ) {
    int key = 0;
    if      ( memEvent->measuredLepton1_ && memEvent->genLepton1_ ) key += (1 << 7); // 128
    else if ( memEvent->measuredLepton1_                          ) key += (1 << 6); //  64
    if      ( memEvent->measuredLepton2_ && memEvent->genLepton2_ ) key += (1 << 5); //  32
    else if ( memEvent->measuredLepton2_                          ) key += (1 << 4); //  16
    if      ( memEvent->measuredBJet1_   && memEvent->genBJet1_   ) key += (1 << 3); //   8
    else if ( memEvent->measuredBJet1_                            ) key += (1 << 2); //   4
    if      ( memEvent->measuredBJet2_   && memEvent->genBJet2_   ) key += (1 << 1); //   2
    else if ( memEvent->measuredBJet2_                            ) key += (1 << 0); //   1
    memEvent->key_ = key;
    memEventMap[key].push_back(&(*memEvent));
  }
  return memEventMap;
}
