#include "hhAnalysis/bbww/interface/MEMInterface_hh_bb1l.h" 

#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h" // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetBase.h" // RecoJetBase

#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // findFile
#include "hhAnalysis/bbwwMEM/interface/MeasuredParticle.h" // MeasuredParticle
#include "hhAnalysis/bbwwMEM/interface/memAuxFunctions.h"

#include <TBenchmark.h> // TBenchmark
#include <TMath.h> // TMath::Cos, TMath::Sin

MEMInterface_hh_bb1l::MEMInterface_hh_bb1l()
  : memAlgo_(nullptr)
  , clock_(nullptr)
{
  std::cout << "<MEMInterface_hh_bb1l>:\n";
  
  const double sqrtS = 13.e+3;
  const std::string pdfName = "MSTW2008lo68cl";
  const std::string madgraphFileName_signal     = "hhAnalysis/bbwwMEM/data/param_hh.dat";
  const std::string madgraphFileName_background = "hhAnalysis/bbwwMEM/data/param_ttbar.dat";
  const bool applyOnshellWmassConstraint_signal = false;
  const int memAlgo_verbosity = 0;
  const int maxObjFunctionCalls_signal = 2500;
  const int maxObjFunctionCalls_background = 25000;

  memAlgo_ = new MEMbbwwAlgoSingleLepton(sqrtS, pdfName, findFile(madgraphFileName_signal), findFile(madgraphFileName_background), memAlgo_verbosity);
  memAlgo_->applyOnshellWmassConstraint_signal(applyOnshellWmassConstraint_signal);
  memAlgo_->setIntMode(MEMbbwwAlgoSingleLepton::kVAMP);
  memAlgo_->setMaxObjFunctionCalls_signal(maxObjFunctionCalls_signal);
  memAlgo_->setMaxObjFunctionCalls_background(maxObjFunctionCalls_background);

  clock_ = new TBenchmark();
}

MEMInterface_hh_bb1l::~MEMInterface_hh_bb1l()
{
  delete memAlgo_;

  delete clock_;
}

namespace
{

void
addMeasuredLepton(std::vector<mem::MeasuredParticle>& measuredParticles, const RecoLepton * selLepton)
{
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
addMeasuredHadWJet(std::vector<mem::MeasuredParticle>& measuredParticles, const RecoJetBase * selJet)
{
  measuredParticles.push_back(mem::MeasuredParticle(mem::MeasuredParticle::kHadWJet,
    selJet->pt(), selJet->eta(), selJet->phi(), 
    0.));
}

void
addMeasuredBJet(std::vector<mem::MeasuredParticle>& measuredParticles, const RecoJetBase * selJet)
{
  measuredParticles.push_back(mem::MeasuredParticle(mem::MeasuredParticle::kBJet,
    selJet->pt(), selJet->eta(), selJet->phi(), 
    mem::bottomQuarkMass));
}

}

MEMOutput_hh_bb1l
MEMInterface_hh_bb1l::operator()(const RecoLepton * selLepton,
				 const RecoJetBase * selJet_Wjj_lead,
				 const RecoJetBase * selJet_Wjj_sublead,
				 const RecoJetBase * selJet_Hbb_lead,
				 const RecoJetBase * selJet_Hbb_sublead,
				 const RecoMEt & met) const
{
  MEMOutput_hh_bb1l result;
  if ( !(selJet_Wjj_lead || selJet_Wjj_sublead) )
  {
    std::cerr << "Warning in <MEMInterface_hh_bb1l::operator()>: Failed to find at least one jet from W->jj decay !!\n";
    result.errorFlag_ = 1;
    return result;
  }
  if ( !(selJet_Hbb_lead || selJet_Hbb_sublead) )
  {
    std::cerr << "Warning in <MEMInterface_hh_bb1l::operator()>: Failed to find at least one b-jet !!\n";
    result.errorFlag_ = 1;
    return result;
  }

  std::vector<mem::MeasuredParticle> measuredParticles;
  addMeasuredLepton(measuredParticles, selLepton);
  if ( selJet_Wjj_lead ) 
  {
    addMeasuredHadWJet(measuredParticles, selJet_Wjj_lead);
  }
  if ( selJet_Wjj_sublead ) 
  {
    addMeasuredHadWJet(measuredParticles, selJet_Wjj_sublead);
  }
  if ( selJet_Hbb_lead ) 
  {
    addMeasuredBJet(measuredParticles, selJet_Hbb_lead);
  }
  if ( selJet_Hbb_sublead ) 
  {
    addMeasuredBJet(measuredParticles, selJet_Hbb_sublead);
  }
  double metPx = met.pt()*TMath::Cos(met.phi());
  double metPy = met.pt()*TMath::Sin(met.phi());

  clock_->Reset();
  clock_->Start("<MEMInterface_hh_bb1l::operator()>");
  memAlgo_->integrate(measuredParticles, metPx, metPy, met.cov());
  MEMbbwwResultSingleLepton memResult = memAlgo_->getResult();
  clock_->Stop("<MEMInterface_hh_bb1l::operator()>");

  result.fillInputs(selLepton, selJet_Wjj_lead, selJet_Wjj_sublead, selJet_Hbb_lead, selJet_Hbb_sublead);
  result.weight_signal_ = memResult.getProb_signal(); 
  result.weightErr_signal_ = memResult.getProbErr_signal();
  result.weight_background_ = memResult.getProb_background();
  result.weightErr_background_ = memResult.getProbErr_background();
  result.LR_ = memResult.getLikelihoodRatio();
  result.LRErr_ = memResult.getLikelihoodRatioErr();
  result.Score_ = memResult.getScore();
  result.cpuTime_ = clock_->GetCpuTime("<MEMInterface_hh_bb1l::operator()>");
  result.realTime_ = clock_->GetRealTime("<MEMInterface_hh_bb1l::operator()>");
  result.isValid_ = (memResult.getProb_signal() + memResult.getProb_background()) > 0.;

  return result;
}

