#include "hhAnalysis/bbww/interface/MEMInterface_hh_bb2l.h" 

#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h" // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetBase.h" // RecoJetBase
#include "tthAnalysis/HiggsToTauTau/interface/GenLepton.h" // GenLepton
#include "tthAnalysis/HiggsToTauTau/interface/GenJet.h" // GenJet

#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // findFile
#include "hhAnalysis/bbwwMEM/interface/MeasuredParticle.h" // MeasuredParticle
#include "hhAnalysis/bbwwMEM/interface/memAuxFunctions.h"

#include <TBenchmark.h> // TBenchmark
#include <TMath.h> // TMath::Cos, TMath::Sin

MEMInterface_hh_bb2l::MEMInterface_hh_bb2l()
  : memAlgo_(nullptr)
  , clock_(nullptr)
{
  //std::cout << "<MEMInterface_hh_bb2l>:\n";
  
  const double sqrtS = 13.e+3;
  const std::string pdfName = "MSTW2008lo68cl";
  const std::string madgraphFileName_signal     = "hhAnalysis/bbwwMEM/data/param_hh.dat";
  const std::string madgraphFileName_background = "hhAnalysis/bbwwMEM/data/param_ttbar.dat";
  const bool applyOnshellWmassConstraint_signal = false;
  const int memAlgo_verbosity = 0;
  const int maxObjFunctionCalls_signal = 2500;
  const int maxObjFunctionCalls_background = 25000;

  memAlgo_ = new MEMbbwwAlgoDilepton(sqrtS, pdfName, findFile(madgraphFileName_signal), findFile(madgraphFileName_background), memAlgo_verbosity);
  memAlgo_->applyOnshellWmassConstraint_signal(applyOnshellWmassConstraint_signal);
  memAlgo_->setIntMode(MEMbbwwAlgoDilepton::kVAMP);
  memAlgo_->setMaxObjFunctionCalls_signal(maxObjFunctionCalls_signal);
  memAlgo_->setMaxObjFunctionCalls_background(maxObjFunctionCalls_background);

  clock_ = new TBenchmark();
}

MEMInterface_hh_bb2l::~MEMInterface_hh_bb2l()
{
  delete memAlgo_;

  delete clock_;
}

namespace
{

void
addMeasuredLepton(std::vector<mem::MeasuredParticle>& measuredParticles, const RecoLepton * selLepton, bool switchToGen)
{
  Particle::LorentzVector selLeptonP4;
  if ( switchToGen ) 
  {
    assert(selLepton->genLepton());
    selLeptonP4 = selLepton->genLepton()->p4();
  }
  else 
  {
    selLeptonP4 = selLepton->p4();
  }
  int selLeptonType;   
  double selLeptonMass;   
  if ( selLepton->is_electron() ) 
  {
    selLeptonType = mem::MeasuredParticle::kElectron;
    selLeptonMass = mem::electronMass;
  } 
  else if ( selLepton->is_muon() ) 
  {
    selLeptonType = mem::MeasuredParticle::kMuon;
    selLeptonMass = mem::muonMass;
  } 
  else assert(0);
  measuredParticles.push_back(mem::MeasuredParticle(selLeptonType, 
    selLepton->pt(), selLepton->eta(), selLepton->phi(), 
    selLeptonMass, selLepton->charge()));
}

void
addMeasuredBJet(std::vector<mem::MeasuredParticle>& measuredParticles, const RecoJetBase * selJet, bool switchToGen)
{
  Particle::LorentzVector selJetP4;
  if ( switchToGen ) 
  {
    assert(selJet->genJet());
    selJetP4 = selJet->genJet()->p4();
  }
  else 
  {
    selJetP4 = selJet->p4();
  }
  measuredParticles.push_back(mem::MeasuredParticle(mem::MeasuredParticle::kBJet,
    selJetP4.pt(), selJetP4.eta(), selJetP4.phi(), 
    mem::bottomQuarkMass));
}

}

MEMOutput_hh_bb2l
MEMInterface_hh_bb2l::operator()(const RecoLepton * selLepton_lead,
				 const RecoLepton * selLepton_sublead,
				 const RecoJetBase * selJet_Hbb_lead,
				 const RecoJetBase * selJet_Hbb_sublead,
				 const RecoMEt & met, 
	                         bool switchToGen) const
{
  MEMOutput_hh_bb2l result;
  if ( !(selJet_Hbb_lead || selJet_Hbb_sublead) )
  {
    std::cerr << "Warning in <MEMInterface_hh_bb2l::operator()>: Failed to find at least one b-jet !!\n";
    result.errorFlag_ = 1;
    return result;
  }

  if ( switchToGen ) 
  {
    if ( (selLepton_lead     && !selLepton_lead->genLepton()   ) ||
         (selLepton_sublead  && !selLepton_sublead->genLepton()) ||
         (selJet_Hbb_lead    && !selJet_Hbb_lead->genJet()     ) ||
         (selJet_Hbb_sublead && !selJet_Hbb_sublead->genJet()  ) )
    {
      result.errorFlag_ = 1;
      return result;
    }
  }

  std::vector<mem::MeasuredParticle> measuredParticles;
  addMeasuredLepton(measuredParticles, selLepton_lead, switchToGen);
  addMeasuredLepton(measuredParticles, selLepton_sublead, switchToGen);
  if ( selJet_Hbb_lead ) 
  {
    addMeasuredBJet(measuredParticles, selJet_Hbb_lead, switchToGen);
  }
  if ( selJet_Hbb_sublead ) 
  {
    addMeasuredBJet(measuredParticles, selJet_Hbb_sublead, switchToGen);
  }

  double metPx, metPy;
  if ( switchToGen )
  {
    metPx = met.genPt()*TMath::Cos(met.genPhi());
    metPy = met.genPt()*TMath::Sin(met.genPhi());
  }
  else
  {
    metPx = met.pt()*TMath::Cos(met.phi());
    metPy = met.pt()*TMath::Sin(met.phi());
  }

  clock_->Reset();
  clock_->Start("<MEMInterface_hh_bb2l::operator()>");
  memAlgo_->integrate(measuredParticles, metPx, metPy, met.cov());
  MEMbbwwResultDilepton memResult = memAlgo_->getResult();
  clock_->Stop("<MEMInterface_hh_bb2l::operator()>");

  result.fillInputs(selLepton_lead, selLepton_sublead, selJet_Hbb_lead, selJet_Hbb_sublead);
  result.weight_signal_ = memResult.getProb_signal(); 
  result.weightErr_signal_ = memResult.getProbErr_signal();
  result.weight_background_ = memResult.getProb_background();
  result.weightErr_background_ = memResult.getProbErr_background();
  result.LR_ = memResult.getLikelihoodRatio();
  result.LRErr_ = memResult.getLikelihoodRatioErr();
  result.Score_ = memResult.getScore();
  result.cpuTime_ = clock_->GetCpuTime("<MEMInterface_hh_bb2l::operator()>");
  result.realTime_ = clock_->GetRealTime("<MEMInterface_hh_bb2l::operator()>");
  result.isValid_ = (memResult.getProb_signal() + memResult.getProb_background()) > 0.;

  return result;
}

