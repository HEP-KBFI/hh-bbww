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

const Particle::LorentzVector dummyLV;

TopKinRecoInterface::TopKinRecoInterface(double btag_wp, bool considerOnlyBJets)
  : algo_(nullptr)
  , clock_(nullptr)
{
  algo_ = new KinematicReconstruction(1, btag_wp, considerOnlyBJets);

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
  convert_to_LV(const std::vector<const Particle::LorentzVector*>& particleP4s)
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
    VLV allLeptons = convert_to_LV({ selLeptonP4_lead, selLeptonP4_sublead });  
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
    VLV jets = convert_to_LV({ selBJetP4_lead, selBJetP4_sublead });
    std::vector<double> jetBtags = extract_btagCSV(std::vector<const RecoJetBase*>({ selBJet_lead, selBJet_sublead }));
    std::vector<int> bjetIndices = { 0, 1 };
    KinematicReconstructionSolutions solutions = algo_->solutions(
      std::vector<int>({ leptonIndex }), std::vector<int>({ antiLeptonIndex }), bjetIndices, bjetIndices, 
      allLeptons, jets, jetBtags, metP4);
    
    leptonP4_top_.clear();
    neutrinoP4_top_.clear();
    bJetP4_top_.clear();
    topQuarkP4_top_.clear();
    leptonP4_antitop_.clear();
    neutrinoP4_antitop_.clear();
    bJetP4_antitop_.clear();
    topQuarkP4_antitop_.clear();
    sumNeutrinoP4_.clear();

    resetP4(leptonP4_top_maxWeight_);
    resetP4(bJetP4_top_maxWeight_);
    resetP4(topQuarkP4_top_maxWeight_);
    resetP4(neutrinoP4_top_maxWeight_);
    resetP4(leptonP4_antitop_maxWeight_);
    resetP4(bJetP4_antitop_maxWeight_);
    resetP4(topQuarkP4_antitop_maxWeight_);
    resetP4(neutrinoP4_antitop_maxWeight_);	
    resetP4(sumNeutrinoP4_maxWeight_);

    double max_weight = -1.;
    size_t numSolutions = solutions.numberOfSolutions();
    for ( size_t idxSolution = 0; idxSolution < numSolutions; ++idxSolution )
    {
      const KinematicReconstructionSolution& solution = solutions.solution(KinematicReconstructionSolution::defaultForMethod, idxSolution);
      double solution_weight = solution.weight(KinematicReconstructionSolution::defaultForMethod);
      std::cout << "Solution #" << idxSolution << ": weight = " << solution_weight << std::endl;
      solution.print();

      Particle::LorentzVector leptonP4_top = convert_to_P4(solution.antiLepton());
      leptonP4_top_.push_back(leptonP4_top);
      Particle::LorentzVector neutrinoP4_top = convert_to_P4(solution.neutrino());
      neutrinoP4_top_.push_back(neutrinoP4_top);
      Particle::LorentzVector bJetP4_top = convert_to_P4(solution.bjet());
      bJetP4_top_.push_back(bJetP4_top);
      Particle::LorentzVector topQuarkP4_top = convert_to_P4(solution.top());
      topQuarkP4_top_.push_back(topQuarkP4_top);
      Particle::LorentzVector leptonP4_antitop = convert_to_P4(solution.lepton());
      leptonP4_antitop_.push_back(leptonP4_antitop);
      Particle::LorentzVector neutrinoP4_antitop = convert_to_P4(solution.antiNeutrino());
      neutrinoP4_antitop_.push_back(neutrinoP4_antitop);
      Particle::LorentzVector bJetP4_antitop = convert_to_P4(solution.antiBjet());
      bJetP4_antitop_.push_back(bJetP4_antitop);
      Particle::LorentzVector topQuarkP4_antitop = convert_to_P4(solution.antiTop());
      topQuarkP4_antitop_.push_back(topQuarkP4_antitop);
      Particle::LorentzVector sumNeutrinoP4 = neutrinoP4_top + neutrinoP4_antitop;
      sumNeutrinoP4_.push_back(sumNeutrinoP4);

      if ( solution_weight > max_weight )
      {
        leptonP4_top_maxWeight_ = leptonP4_top;
        neutrinoP4_top_maxWeight_ = neutrinoP4_top;
        bJetP4_top_maxWeight_ = bJetP4_top;
        topQuarkP4_top_maxWeight_ = topQuarkP4_top;
        leptonP4_antitop_maxWeight_ = leptonP4_antitop;
        neutrinoP4_antitop_maxWeight_ = neutrinoP4_antitop;
        bJetP4_antitop_maxWeight_ = bJetP4_antitop;
        topQuarkP4_antitop_maxWeight_ = topQuarkP4_antitop;
        sumNeutrinoP4_maxWeight_ = sumNeutrinoP4;
        isValid_ = true;
        max_weight = solution_weight;
      }
    }
  }

  clock_->Stop("<TopKinRecoInterface::setInputs>");
  cpuTime_ = clock_->GetCpuTime("<TopKinRecoInterface::setInputs>");
  realTime_ = clock_->GetRealTime("<TopKinRecoInterface::setInputs>");
  //std::cout << "cpuTime = " << cpuTime_ << ", realTime = " << realTime_ << std::endl;
}

bool
TopKinRecoInterface::isValid() const
{
  return isValid_;
}

const Particle::LorentzVector&
TopKinRecoInterface::getLeptonP4_top(int idx) const
{
  if      ( idx == -1                                    ) return leptonP4_top_maxWeight_;
  else if ( idx >=  0 && idx < (int)leptonP4_top_.size() ) return leptonP4_top_[idx];
  else throw cms::Exception("TopKinRecoInterface::getLeptonP4_top") << "Invalid index = " << idx << ", #solutions = " << leptonP4_top_.size() << " !!\n";
  return dummyLV;
}

const Particle::LorentzVector&
TopKinRecoInterface::getBJetP4_top(int idx) const
{
  if      ( idx == -1                                  ) return bJetP4_top_maxWeight_;
  else if ( idx >=  0 && idx < (int)bJetP4_top_.size() ) return bJetP4_top_[idx];
  else throw cms::Exception("TopKinRecoInterface::getBJetP4_top") << "Invalid index = " << idx << ", #solutions = " << bJetP4_top_.size() << " !!\n";
  return dummyLV;
}

const Particle::LorentzVector&
TopKinRecoInterface::getTopQuarkP4_top(int idx) const
{
  if      ( idx == -1                                      ) return topQuarkP4_top_maxWeight_;
  else if ( idx >=  0 && idx < (int)topQuarkP4_top_.size() ) return topQuarkP4_top_[idx];
  else throw cms::Exception("TopKinRecoInterface::getTopQuarkP4_top") << "Invalid index = " << idx << ", #solutions = " << topQuarkP4_top_.size() << " !!\n";
  return dummyLV;
}

const Particle::LorentzVector&
TopKinRecoInterface::getLeptonP4_antitop(int idx) const
{
  if      ( idx == -1                                        ) return leptonP4_antitop_maxWeight_;
  else if ( idx >=  0 && idx < (int)leptonP4_antitop_.size() ) return leptonP4_antitop_[idx];
  else throw cms::Exception("TopKinRecoInterface::getLeptonP4_antitop") << "Invalid index = " << idx << ", #solutions = " << leptonP4_antitop_.size() << " !!\n";
  return dummyLV;
}

const Particle::LorentzVector&
TopKinRecoInterface::getBJetP4_antitop(int idx) const
{
  if      ( idx == -1                                      ) return bJetP4_antitop_maxWeight_;
  else if ( idx >=  0 && idx < (int)bJetP4_antitop_.size() ) return bJetP4_antitop_[idx];
  else throw cms::Exception("TopKinRecoInterface::getBJetP4_antitop") << "Invalid index = " << idx << ", #solutions = " << bJetP4_antitop_.size() << " !!\n";
  return dummyLV;
}

const Particle::LorentzVector&
TopKinRecoInterface::getTopQuarkP4_antitop(int idx) const
{
  if      ( idx == -1                                          ) return topQuarkP4_antitop_maxWeight_;
  else if ( idx >=  0 && idx < (int)topQuarkP4_antitop_.size() ) return topQuarkP4_antitop_[idx];
  else throw cms::Exception("TopKinRecoInterface::getTopQuarkP4_antitop") << "Invalid index = " << idx << ", #solutions = " << topQuarkP4_antitop_.size() << " !!\n";
  return dummyLV;
}

const Particle::LorentzVector&
TopKinRecoInterface::getMEtP4(int idx) const
{
  if      ( idx == -1                                     ) return sumNeutrinoP4_maxWeight_;
  else if ( idx >=  0 && idx < (int)sumNeutrinoP4_.size() ) return sumNeutrinoP4_[idx];
  else throw cms::Exception("TopKinRecoInterface::getMEtP4") << "Invalid index = " << idx << ", #solutions = " << sumNeutrinoP4_.size() << " !!\n";
  return dummyLV;
}
