#include "hhAnalysis/bbww/interface/memNtupleAuxFunctions_singlelepton.h"

#include "DataFormats/Math/interface/deltaR.h"                         // deltaR

#include "hhAnalysis/bbwwMEM/interface/measuredParticleAuxFunctions.h" // findGenMatch

std::vector<MEMEvent_singlelepton>
buildMEMEvents_singlelepton_boosted(const std::vector<const std::pair<mem::MeasuredParticle, mem::MeasuredParticle>*>& measuredJetsAK8_Hbb,
                                    const std::vector<const std::pair<mem::MeasuredParticle, mem::MeasuredParticle>*>& measuredJetsAK8_Wjj,
                                    const std::vector<const mem::MeasuredParticle*>& measuredLeptons,
                                    double measuredMEtPx, double measuredMEtPy, const TMatrixD& measuredMEtCov)
{
  std::vector<MEMEvent_singlelepton> memEvents;
  for ( std::vector<const std::pair<mem::MeasuredParticle, mem::MeasuredParticle>*>::const_iterator measuredJet_Hbb = measuredJetsAK8_Hbb.begin();
        measuredJet_Hbb != measuredJetsAK8_Hbb.end(); ++measuredJet_Hbb ) {    
    for ( std::vector<const std::pair<mem::MeasuredParticle, mem::MeasuredParticle>*>::const_iterator measuredJet_Wjj = measuredJetsAK8_Wjj.begin();
        measuredJet_Wjj != measuredJetsAK8_Wjj.end(); ++measuredJet_Wjj ) {
      if ( deltaR((*measuredJet_Hbb)->first.p4(),  (*measuredJet_Wjj)->first.p4())  < 0.3 ||
           deltaR((*measuredJet_Hbb)->second.p4(), (*measuredJet_Wjj)->first.p4())  < 0.3 ||
           deltaR((*measuredJet_Hbb)->first.p4(),  (*measuredJet_Wjj)->second.p4()) < 0.3 ||
           deltaR((*measuredJet_Hbb)->second.p4(), (*measuredJet_Wjj)->second.p4()) < 0.3 ) continue;
      for ( std::vector<const mem::MeasuredParticle*>::const_iterator lepton = measuredLeptons.begin();
            lepton != measuredLeptons.end(); ++lepton ) {
        MEMEvent_singlelepton memEvent(
          &(*measuredJet_Hbb)->first, &(*measuredJet_Hbb)->second, 
          &(*measuredJet_Wjj)->first, &(*measuredJet_Wjj)->second, 
          *lepton, 
          measuredMEtPx, measuredMEtPy, measuredMEtCov);
        memEvent.isBoosted_Hbb_ = true;
        memEvent.isBoosted_Wjj_ = true;
        memEvents.push_back(memEvent);
      }
    }
  }
  return memEvents;
}

std::vector<MEMEvent_singlelepton>
buildMEMEvents_singlelepton_semiboosted(const std::vector<const std::pair<mem::MeasuredParticle, mem::MeasuredParticle>*>& measuredJetsAK8_Hbb,
                                        const std::vector<const mem::MeasuredParticle*>& measuredJetsAK4, int numWJets,
                                        const std::vector<const mem::MeasuredParticle*>& measuredLeptons,
                                        double measuredMEtPx, double measuredMEtPy, const TMatrixD& measuredMEtCov)
{
  std::vector<MEMEvent_singlelepton> memEvents;
  for ( std::vector<const std::pair<mem::MeasuredParticle, mem::MeasuredParticle>*>::const_iterator measuredJet_Hbb = measuredJetsAK8_Hbb.begin();
        measuredJet_Hbb != measuredJetsAK8_Hbb.end(); ++measuredJet_Hbb ) {
    for ( std::vector<const mem::MeasuredParticle*>::const_iterator wjet1 = measuredJetsAK4.begin();
            wjet1 != measuredJetsAK4.end(); ++wjet1 ) {
      if ( ((*wjet1) && deltaR((*measuredJet_Hbb)->first.p4(),  (*wjet1)->p4()) < 0.3) || 
           ((*wjet1) && deltaR((*measuredJet_Hbb)->second.p4(), (*wjet1)->p4()) < 0.3) ) continue; 
      for ( std::vector<const mem::MeasuredParticle*>::const_iterator wjet2 = measuredJetsAK4.begin();
            wjet2 != measuredJetsAK4.end(); ++wjet2 ) {
        if ( ((*wjet2) && deltaR((*measuredJet_Hbb)->first.p4(),  (*wjet2)->p4()) < 0.3) || 
             ((*wjet2) && deltaR((*measuredJet_Hbb)->second.p4(), (*wjet2)->p4()) < 0.3) ) continue; 
        assert(!((*wjet1) == nullptr && (*wjet2) != nullptr));       
        if ( (*wjet1) && (*wjet2) ) {
          if ( !((*wjet1)->pt() >= (*wjet2)->pt()) ) continue;
          if ( deltaR((*wjet1)->p4(), (*wjet2)->p4()) < 0.3 ) continue;
        }
        for ( std::vector<const mem::MeasuredParticle*>::const_iterator lepton = measuredLeptons.begin();
              lepton != measuredLeptons.end(); ++lepton ) {
            MEMEvent_singlelepton memEvent(
              &(*measuredJet_Hbb)->first, &(*measuredJet_Hbb)->second,
              *wjet1, *wjet2,
              *lepton,
              measuredMEtPx, measuredMEtPy, measuredMEtCov);
            memEvent.isBoosted_Hbb_ = true;
            memEvent.isBoosted_Wjj_ = false;
            memEvents.push_back(memEvent);
        }
      }
    }
  }
  return memEvents;   
}

std::vector<MEMEvent_singlelepton>
buildMEMEvents_singlelepton_resolved(const std::vector<const mem::MeasuredParticle*>& measuredJetsAK4, int numBJets, int numWJets,
                                     const std::vector<const mem::MeasuredParticle*>& measuredLeptons,
                                     double measuredMEtPx, double measuredMEtPy, const TMatrixD& measuredMEtCov)
{
  assert(numBJets == 1 || numBJets == 2);
  std::vector<const mem::MeasuredParticle*> bjets1 = measuredJetsAK4;
  std::vector<const mem::MeasuredParticle*> bjets2 = ( numBJets == 2 ) ? measuredJetsAK4 : std::vector<const mem::MeasuredParticle*>({ nullptr });
  assert(numWJets == 1 || numWJets == 2);
  std::vector<const mem::MeasuredParticle*> wjets1 = measuredJetsAK4;
  std::vector<const mem::MeasuredParticle*> wjets2 = ( numWJets == 2 ) ? measuredJetsAK4 : std::vector<const mem::MeasuredParticle*>({ nullptr });
  std::vector<MEMEvent_singlelepton> memEvents;
  for ( std::vector<const mem::MeasuredParticle*>::const_iterator bjet1 = bjets1.begin();
        bjet1 != bjets1.end(); ++bjet1 ) {
    for ( std::vector<const mem::MeasuredParticle*>::const_iterator bjet2 = bjets2.begin();
          bjet2 != bjets2.end(); ++bjet2 ) {
      assert(!((*bjet1) == nullptr && (*bjet2) != nullptr));
      if ( (*bjet1) && (*bjet2) ) {
        if ( !((*bjet1)->pt() >= (*bjet2)->pt()) ) continue;
        if ( deltaR((*bjet1)->p4(), (*bjet2)->p4()) < 0.3 ) continue;
      }
      for ( std::vector<const mem::MeasuredParticle*>::const_iterator wjet1 = wjets1.begin();
            wjet1 != wjets1.end(); ++wjet1 ) {
        if ( ((*bjet1) && (*wjet1) && deltaR((*bjet1)->p4(), (*wjet1)->p4()) < 0.3) || 
             ((*bjet2) && (*wjet1) && deltaR((*bjet2)->p4(), (*wjet1)->p4()) < 0.3) ) continue;
        for ( std::vector<const mem::MeasuredParticle*>::const_iterator wjet2 = wjets2.begin();
              wjet2 != wjets2.end(); ++wjet2 ) {
          if ( ((*bjet1) && (*wjet2) && deltaR((*bjet1)->p4(), (*wjet2)->p4()) < 0.3) || 
               ((*bjet2) && (*wjet2) && deltaR((*bjet2)->p4(), (*wjet2)->p4()) < 0.3) ) continue;
          assert(!((*wjet1) == nullptr && (*wjet2) != nullptr));       
          if ( (*wjet1) && (*wjet2) ) {
            if ( !((*wjet1)->pt() >= (*wjet2)->pt()) ) continue;
            if ( deltaR((*wjet1)->p4(), (*wjet2)->p4()) < 0.3 ) continue;
          }
          for ( std::vector<const mem::MeasuredParticle*>::const_iterator lepton = measuredLeptons.begin();
                lepton != measuredLeptons.end(); ++lepton ) {
            MEMEvent_singlelepton memEvent(
              *bjet1, *bjet2,
              *wjet1, *wjet2,
              *lepton,
              measuredMEtPx, measuredMEtPy, measuredMEtCov);
            memEvent.isBoosted_Hbb_ = false;
            memEvent.isBoosted_Wjj_ = false;
            memEvents.push_back(memEvent);
          }
        }
      }
    }
  }
  return memEvents;
}

void
addGenMatches_singlelepton(std::vector<MEMEvent_singlelepton>& memEvents,
                           const std::vector<const GenJet*>& genBJets,
                           const std::vector<const GenJet*>& genWJets,
                           const std::vector<const GenLepton*>& genLeptons,
                           double genMEtPx, double genMEtPy)
{
  for ( std::vector<MEMEvent_singlelepton>::iterator memEvent = memEvents.begin();
        memEvent != memEvents.end(); ++memEvent ) {
    memEvent->genBJet1_  = mem::findGenMatch(memEvent->measuredBJet1_,  genBJets);
    memEvent->genBJet2_  = mem::findGenMatch(memEvent->measuredBJet2_,  genBJets);
    memEvent->genWJet1_  = mem::findGenMatch(memEvent->measuredWJet1_,  genWJets);
    memEvent->genWJet2_  = mem::findGenMatch(memEvent->measuredWJet2_,  genWJets);
    memEvent->genLepton_ = mem::findGenMatch(memEvent->measuredLepton_, genLeptons);
  }
}

std::map<int, std::vector<const MEMEvent_singlelepton*>>
buildMEMEventMap_singlelepton(const std::vector<MEMEvent_singlelepton>& memEvents)
{
  std::map<int, std::vector<const MEMEvent_singlelepton*>> memEventMap;
  for ( std::vector<MEMEvent_singlelepton>::const_iterator memEvent = memEvents.begin();
        memEvent != memEvents.end(); ++memEvent ) {
    int key = 0;
    if      ( memEvent->measuredLepton_ && memEvent->genLepton_ ) key += (1 << 9); // 512
    else if ( memEvent->measuredLepton_                         ) key += (1 << 8); // 256
    if      ( memEvent->measuredBJet1_  && memEvent->genBJet1_  ) key += (1 << 7); // 128
    else if ( memEvent->measuredBJet1_                          ) key += (1 << 6); //  64
    if      ( memEvent->measuredBJet2_  && memEvent->genBJet2_  ) key += (1 << 5); //  32
    else if ( memEvent->measuredBJet2_                          ) key += (1 << 4); //  16
    if      ( memEvent->measuredWJet1_  && memEvent->genWJet1_  ) key += (1 << 3); //   8
    else if ( memEvent->measuredWJet1_                          ) key += (1 << 2); //   4
    if      ( memEvent->measuredWJet2_  && memEvent->genWJet2_  ) key += (1 << 1); //   2
    else if ( memEvent->measuredWJet2_                          ) key += (1 << 0); //   1
    memEvent->key_ = key;
    memEventMap[key].push_back(&(*memEvent));
  }
  return memEventMap;
}
