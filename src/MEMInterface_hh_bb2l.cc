#include "hhAnalysis/bbww/interface/MEMInterface_hh_bb2l.h" 

#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h" // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetBase.h" // RecoJetBase

#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // findFile
#include "hhAnalysis/bbwwMEM/interface/MEMbbwwAlgoDilepton.h"
#include "hhAnalysis/bbwwMEM/interface/MeasuredParticle.h" // MeasuredParticle
#include "hhAnalysis/bbwwMEM/interface/memAuxFunctions.h"

#include <TBenchmark.h> // TBenchmark
#include <TMath.h> // TMath::Cos, TMath::Sin

MEMInterface_hh_bb2l::MEMInterface_hh_bb2l()
  : clock_(nullptr)
{
  std::cout << "<MEMInterface_hh_bb2l>:\n";
  
  clock_ = new TBenchmark();
}

MEMInterface_hh_bb2l::~MEMInterface_hh_bb2l()
{
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
addMeasuredBJet(std::vector<mem::MeasuredParticle>& measuredParticles, const RecoJetBase * selJet)
{
  measuredParticles.push_back(mem::MeasuredParticle(mem::MeasuredParticle::kBJet,
    selJet->pt(), selJet->eta(), selJet->phi(), 
    mem::bottomQuarkMass));
}

}

MEMOutput_hh_bb2l
MEMInterface_hh_bb2l::operator()(const RecoLepton * selLepton_lead,
				 const RecoLepton * selLepton_sublead,
				 const RecoJetBase * selJet_Hbb_lead,
				 const RecoJetBase * selJet_Hbb_sublead,
				 const RecoMEt & met) const
{
  MEMOutput_hh_bb2l result;

  if ( !(selJet_Hbb_lead || selJet_Hbb_sublead) )
  {
    std::cerr << "Warning in <MEMInterface_hh_bb2l::operator()>: Failed to find at least one b-jet !!\n";
    result.errorFlag_ = 1;
    return result;
  }

  std::vector<mem::MeasuredParticle> measuredParticles;
  addMeasuredLepton(measuredParticles, selLepton_lead);
  addMeasuredLepton(measuredParticles, selLepton_sublead);
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

  const double sqrtS = 13.e+3;
  const std::string pdfName = "MSTW2008lo68cl";
  const std::string madgraphFileName_signal     = "hhAnalysis/bbwwMEM/data/param_hh.dat";
  const std::string madgraphFileName_background = "hhAnalysis/bbwwMEM/data/param_ttbar.dat";
  const bool applyOnshellWmassConstraint_signal = false;
  const int memAlgo_verbosity = 1;
  const int maxObjFunctionCalls_signal = 1000;
  const int maxObjFunctionCalls_background = 10000;

  clock_->Reset();
  clock_->Start("<MEMInterface_hh_bb2l::operator()>");
  MEMbbwwAlgoDilepton memAlgo(sqrtS, pdfName, findFile(madgraphFileName_signal), findFile(madgraphFileName_background), memAlgo_verbosity);
  memAlgo.applyOnshellWmassConstraint_signal(applyOnshellWmassConstraint_signal);
  memAlgo.setIntMode(MEMbbwwAlgoDilepton::kVAMP);
  memAlgo.setMaxObjFunctionCalls_signal(maxObjFunctionCalls_signal);
  memAlgo.setMaxObjFunctionCalls_background(maxObjFunctionCalls_background);
  memAlgo.integrate(measuredParticles, metPx, metPy, met.cov());
  MEMbbwwResultDilepton memResult = memAlgo.getResult();
  clock_->Stop("<MEMInterface_hh_bb2l::operator()>");

  result.fillInputs(selLepton_lead, selLepton_sublead, selJet_Hbb_lead, selJet_Hbb_sublead);
  result.weight_signal_ = memResult.getProb_signal(); 
  result.weight_background_ = memResult.getProb_background();
  result.LR_ = memResult.getLikelihoodRatio();
  result.cpuTime_ = clock_->GetCpuTime("<MEMInterface_2lss_1tau::operator()>");
  result.realTime_ = clock_->GetRealTime("<MEMInterface_2lss_1tau::operator()>");
  result.isValid_ = (memResult.getProb_signal() + memResult.getProb_background()) > 0.;

  return result;
}

