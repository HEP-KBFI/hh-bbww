#include "hhAnalysis/bbww/interface/TopKinRecoInterface.h"

#include "FWCore/Utilities/interface/Exception.h"     // cms::Exception
#include <DataFormats/Math/interface/LorentzVector.h> // math::XYZTLorentzVector

#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h"    // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/GenLepton.h"     // GenLepton
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetBase.h"   // RecoJetBase
#include "tthAnalysis/HiggsToTauTau/interface/RecoJet.h"       // RecoJet
#include "tthAnalysis/HiggsToTauTau/interface/RecoSubjetAK8.h" // RecoSubjetAK8
#include "tthAnalysis/HiggsToTauTau/interface/GenJet.h"        // GenJet

#include "TopAnalysis/KinematicReconstruction/interface/KinematicReconstructionSolution.h" // KinematicReconstructionSolutions
#include "TopAnalysis/KinematicReconstruction/interface/classesFwd.h"                      // LV, VLV

#include <TLorentzVector.h> // TLorentzVector
#include <TMath.h>          // TMath::Cos(), TMath::Sin(), TMath::Sqrt()

TopKinRecoInterface::TopKinRecoInterface(double btag_wp)
  : algo_(nullptr)
  , clock_(nullptr)
{
  algo_ = new KinematicReconstruction(1, btag_wp, true);

  clock_ = new TBenchmark();
}

TopKinRecoInterface::~TopKinRecoInterface()
{
  delete algo_;

  delete clock_;
}

namespace
{
  LV
  convert_to_LV(const Particle::LorentzVector& particleP4)
  {
    return LV(particleP4.pt(), particleP4.eta(), particleP4.phi(), particleP4.mass());
  }

  VLV
  convert_to_TLorentzVector(const std::vector<const Particle::LorentzVector*>& particleP4s)
  {
    VLV retVal;
    for ( const Particle::LorentzVector* p4 : particleP4s )
    {      
      retVal.push_back(convert_to_LV(*p4));
    }
    return retVal;
  }

  std::vector<double>
  extract_btagCSV(const std::vector<const RecoJetBase*>& jets)
  {
    std::vector<double> retVal;
    for ( std::vector<const RecoJetBase*>::const_iterator jet = jets.begin();
          jet != jets.end(); ++jet ) {
      double btagCSV = -1.;
      if ( dynamic_cast<const RecoJet*>(*jet) )
      {
        btagCSV = (dynamic_cast<const RecoJet*>(*jet))->BtagCSV();
      } 
      else if ( dynamic_cast<const RecoSubjetAK8*>(*jet) )
      {
        btagCSV = (dynamic_cast<const RecoSubjetAK8*>(*jet))->BtagCSV();
      }
      retVal.push_back(btagCSV);
    }
    return retVal;
  }

  Particle::LorentzVector
  convert_to_P4(const LV& particleP4)
  {
    return Particle::LorentzVector(particleP4.pt(), particleP4.eta(), particleP4.phi(), particleP4.mass());
  }

  void
  resetP4(Particle::LorentzVector& p4)
  {
    p4.SetPxPyPzE(0., 0., 0., 0.);
  }
} 

void
TopKinRecoInterface::setInputs(const RecoLepton * selLepton_lead,
                               const RecoLepton * selLepton_sublead,
                               const RecoJetBase * selBJet_lead,
	                       const RecoJetBase * selBJet_sublead,
                               const RecoMEt & met, 
                               bool switchToGen)
{
  clock_->Reset();
  clock_->Start("<TopKinRecoInterface::setInputs>");
  const Particle::LorentzVector* selLeptonP4_lead    = nullptr;
  const Particle::LorentzVector* selLeptonP4_sublead = nullptr;
  const Particle::LorentzVector* selBJetP4_lead      = nullptr;
  const Particle::LorentzVector* selBJetP4_sublead   = nullptr;
  LV metP4;
  if ( switchToGen )
  {
    if ( selLepton_lead->genLepton()    ) selLeptonP4_lead    = &selLepton_lead->genLepton()->p4();
    if ( selLepton_sublead->genLepton() ) selLeptonP4_sublead = &selLepton_sublead->genLepton()->p4();
    if ( selBJet_lead->genJet()         ) selBJetP4_lead      = &selBJet_lead->genJet()->p4();
    if ( selBJet_sublead->genJet()      ) selBJetP4_sublead   = &selBJet_sublead->genJet()->p4();
    metP4 = convert_to_LV(Particle::LorentzVector(met.genPt(), 0., met.genPhi(), 0.));
  }
  else
  {
    selLeptonP4_lead    = &selLepton_lead->p4();
    selLeptonP4_sublead = &selLepton_sublead->p4();
    selBJetP4_lead      = &selBJet_lead->p4();
    selBJetP4_sublead   = &selBJet_sublead->p4();
    metP4 = convert_to_LV(Particle::LorentzVector(met.pt(), 0., met.phi(), 0.));
  }
  isValid_ = false;
  if ( selLeptonP4_lead && selLeptonP4_sublead && selBJetP4_lead && selBJetP4_sublead && metP4.Pt() > 0. )
  {
    VLV allLeptons = convert_to_TLorentzVector({ selLeptonP4_lead, selLeptonP4_sublead });  
    int leptonIndex = -1;
    int antiLeptonIndex = -1;
    if ( selLepton_lead->charge() < 0 && selLepton_sublead->charge() > 0 ) 
    {
      leptonIndex = 0;
      antiLeptonIndex = 1;
    } 
    else if ( selLepton_sublead->charge() < 0 && selLepton_lead->charge() > 0 ) 
    {
      leptonIndex = 1;
      antiLeptonIndex = 0;
    } 
    else throw cms::Exception("TopKinRecoInterface::setInputs") << "Given lepton pair does not have opposite charge !!\n";
    VLV jets = convert_to_TLorentzVector({ selBJetP4_lead, selBJetP4_sublead });
    std::vector<double> jetBtags = extract_btagCSV(std::vector<const RecoJetBase*>({ selBJet_lead, selBJet_sublead }));
    std::vector<int> bjetIndices = { 0, 1 };
    KinematicReconstructionSolutions solutions = algo_->solutions(
      std::vector<int>({ leptonIndex }), std::vector<int>({ antiLeptonIndex }), std::vector<int>(), bjetIndices, 
      allLeptons, jets, jetBtags, metP4);
    double max_weight = -1.;
    size_t numSolutions = solutions.numberOfSolutions();
    for ( size_t idxSolution = 0; idxSolution < numSolutions; ++idxSolution )
    {
      const KinematicReconstructionSolution& solution = solutions.solution(KinematicReconstructionSolution::defaultForMethod, idxSolution);
      std::cout << "solution #" << idxSolution << ":" << std::endl;
      solution.print();
      double solution_weight = solution.weight(KinematicReconstructionSolution::defaultForMethod);
      if ( solution_weight > max_weight )
      {
        leptonP4_top_ = convert_to_P4(solution.antiLepton());
        neutrinoP4_top_ = convert_to_P4(solution.neutrino());
        bJetP4_top_ = convert_to_P4(solution.bjet());
        topQuarkP4_top_ = convert_to_P4(solution.top());
        assert(TMath::Abs(leptonP4_top_.energy() + neutrinoP4_top_.energy() + bJetP4_top_.energy() - topQuarkP4_top_.energy()) < 1.e-2*topQuarkP4_top_.energy());
        leptonP4_antitop_ = convert_to_P4(solution.lepton());
        neutrinoP4_antitop_ = convert_to_P4(solution.antiNeutrino());
        bJetP4_antitop_ = convert_to_P4(solution.antiBjet());
        topQuarkP4_antitop_ = convert_to_P4(solution.antiTop());
        assert(TMath::Abs(leptonP4_antitop_.energy() + neutrinoP4_antitop_.energy() + bJetP4_antitop_.energy() - topQuarkP4_antitop_.energy()) < 1.e-2*topQuarkP4_antitop_.energy());
        metP4_ = neutrinoP4_top_ + neutrinoP4_antitop_;
        isValid_ = true;
        max_weight = solution_weight;
      }
    }
  }
  if ( !isValid_ )
  {
    resetP4(leptonP4_top_);
    resetP4(bJetP4_top_);
    resetP4(topQuarkP4_top_);
    resetP4(neutrinoP4_top_);
    resetP4(leptonP4_antitop_);
    resetP4(bJetP4_antitop_);
    resetP4(topQuarkP4_antitop_);
    resetP4(neutrinoP4_antitop_);
  }
  clock_->Stop("<TopKinRecoInterface::setInputs>");
  cpuTime_ = clock_->GetCpuTime("<TopKinRecoInterface::setInputs>");
  realTime_ = clock_->GetRealTime("<TopKinRecoInterface::setInputs>");
}

bool
TopKinRecoInterface::isValid() const
{
  return isValid_;
}

const Particle::LorentzVector&
TopKinRecoInterface::getLeptonP4_top() const
{
  return leptonP4_top_;
}

const Particle::LorentzVector&
TopKinRecoInterface::getBJetP4_top() const
{
  return bJetP4_top_;
}

const Particle::LorentzVector&
TopKinRecoInterface::getTopQuarkP4_top() const
{
  return topQuarkP4_top_;
}

const Particle::LorentzVector&
TopKinRecoInterface::getLeptonP4_antitop() const
{
  return leptonP4_antitop_;
}

const Particle::LorentzVector&
TopKinRecoInterface::getBJetP4_antitop() const
{
  return bJetP4_antitop_;
}

const Particle::LorentzVector&
TopKinRecoInterface::getTopQuarkP4_antitop() const
{
  return topQuarkP4_antitop_;
}

const Particle::LorentzVector&
TopKinRecoInterface::getMEtP4() const
{
  return metP4_;
}
