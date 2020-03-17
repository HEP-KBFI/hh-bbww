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
  : //memAlgo_({{nullptr, nullptr}}),
  clock_(nullptr)
{
  std::cout << "<MEMInterface_hh_bb2l>:\n";

  const double sqrtS = 13.e+3;
  const std::string pdfName = "MSTW2008lo68cl";
  map<std::string, std::string> madgraphFileName_signal     =
  {
    {"SM",  "hhAnalysis/bbwwMEM/data/param_hh_SM.dat"},
    {"BM1",  "hhAnalysis/bbwwMEM/data/param_hh_BM1.dat"},
    {"BM2",  "hhAnalysis/bbwwMEM/data/param_hh_BM2.dat"},
    {"BM3",  "hhAnalysis/bbwwMEM/data/param_hh_BM3.dat"},
    {"BM4",  "hhAnalysis/bbwwMEM/data/param_hh_BM4.dat"},
    {"BM5",  "hhAnalysis/bbwwMEM/data/param_hh_BM5.dat"},
    {"BM6",  "hhAnalysis/bbwwMEM/data/param_hh_BM6.dat"},
    {"BM7",  "hhAnalysis/bbwwMEM/data/param_hh_BM7.dat"},
    {"BM8",  "hhAnalysis/bbwwMEM/data/param_hh_BM8.dat"},
    {"BM9",  "hhAnalysis/bbwwMEM/data/param_hh_BM9.dat"},
    {"BM10", "hhAnalysis/bbwwMEM/data/param_hh_BM10.dat"},
    {"BM11", "hhAnalysis/bbwwMEM/data/param_hh_BM11.dat"},
    {"BM12", "hhAnalysis/bbwwMEM/data/param_hh_BM12.dat"}
    };

  const std::string madgraphFileName_background = "hhAnalysis/bbwwMEM/data/param_ttbar.dat";
  const bool applyOnshellWmassConstraint_signal = false;
  const int memAlgo_verbosity = 0;
  const int maxObjFunctionCalls_signal = 2500;
  const int maxObjFunctionCalls_background = 25000;
  std::cout<< "Size of dictionary: " << madgraphFileName_signal.size() << "\n";

  for(auto iter: madgraphFileName_signal)
  {
    std::cout<< iter.first << " " << iter.second << "\n";
    memAlgo_[iter.first] = new MEMbbwwAlgoDilepton(sqrtS, pdfName, findFile(iter.second), findFile(madgraphFileName_background), memAlgo_verbosity);
    memAlgo_[iter.first]->applyOnshellWmassConstraint_signal(applyOnshellWmassConstraint_signal);
    memAlgo_[iter.first]->setIntMode(MEMbbwwAlgoDilepton::kVAMP);
    memAlgo_[iter.first]->setMaxObjFunctionCalls_signal(maxObjFunctionCalls_signal);
    memAlgo_[iter.first]->setMaxObjFunctionCalls_background(maxObjFunctionCalls_background);
  }

  clock_ = new TBenchmark();
}

MEMInterface_hh_bb2l::~MEMInterface_hh_bb2l()
{
  //delete memAlgo_;
  for (auto BM : memAlgo_)
  {
    delete (BM.second);
  }

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

//map<std::string, MEMOutput_hh_bb2l>
MEMOutput_hh_bb2l
MEMInterface_hh_bb2l::operator()(const RecoLepton * selLepton_lead,
				 const RecoLepton * selLepton_sublead,
				 const RecoJetBase * selJet_Hbb_lead,
				 const RecoJetBase * selJet_Hbb_sublead,
				 const RecoMEt & met,
         std::string BM,
	       bool switchToGen
        ) const
{
  //std::string BM = "SM";
  //map<std::string, MEMOutput_hh_bb2l> result;
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

  for(auto iter: memAlgo_)
  {
    std::string key = iter.first;
    if (!(key == BM) ) continue;
    std::cout<<"<MEMInterface_hh_bb2l::operator()> Doing BM:" << key << " " << BM << "\n";
    //std::cout<<"<MEMInterface_hh_bb2l::operator()> Doing BM:" << BM << "\n";
    clock_->Reset();
    clock_->Start("<MEMInterface_hh_bb2l::operator()>");
    iter.second->integrate(measuredParticles, metPx, metPy, met.cov());
    MEMbbwwResultDilepton memResult = iter.second->getResult();
    //memAlgo_[BM]->integrate(measuredParticles, metPx, metPy, met.cov());
    //MEMbbwwResultDilepton memResult = memAlgo_[BM]->getResult();
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
    result = result_local;
  }

  return result;
}
