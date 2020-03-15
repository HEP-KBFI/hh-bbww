#include "hhAnalysis/bbww/interface/HMEInterface_hh_bb2l.h" 

#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h" // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetBase.h" // RecoJetBase

#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // findFile

#include <TBenchmark.h> // TBenchmark
#include <TMath.h> // TMath::Cos, TMath::Sin

HMEInterface_hh_bb2l::HMEInterface_hh_bb2l()
  : PUSample_(true)
  , iterations_(100000)
  , bjetrescaleAlgo_(2)
  , metcorrection_(5)
  , weightfromonshellnupt_func_(false)
  , weightfromonshellnupt_hist_(true)
  , weightfromonoffshellWmass_hist_(true)
  , useMET_(true)
  , RefPDFfile_(LocalFileInPath("hhAnalysis/Heavymassestimator/data/REFPDFPU40.root"))
  , clock_(nullptr) 
{
  std::cout << "<HMEInterface_hh_bb2l>:\n";
  
  if( RefPDFfile_.fullPath().empty() )
    throw cms::Exception("analyze_hh_bb2l") << "Failed to find file = 'REFPDFPU40.root'\n";

  clock_ = new TBenchmark();
}

HMEInterface_hh_bb2l::~HMEInterface_hh_bb2l()
{
  delete clock_;
}

HMEOutput_hh_bb2l
HMEInterface_hh_bb2l::operator()(const RecoLepton * selLepton_lead,
                                 const RecoLepton * selLepton_sublead,
                                 const RecoJetBase * selJet_Hbb_lead,
                                 const RecoJetBase * selJet_Hbb_sublead,
                                 const RecoMEt & met,
                                 const int & ievent) const
{
  HMEOutput_hh_bb2l result;
  if ( !(selJet_Hbb_lead || selJet_Hbb_sublead) )
  {
    std::cerr << "Warning in <HMEInterface_hh_bb2l::operator()>: Failed to find at least one b-jet !!\n";
    result.errorFlag_ = 1;
    return result;
  }
  TLorentzVector hmeLepton1P4(selLepton_lead->p4().px(), selLepton_lead->p4().py(), selLepton_lead->p4().pz(), selLepton_lead->p4().energy());
  TLorentzVector hmeLepton2P4(selLepton_sublead->p4().px(), selLepton_sublead->p4().py(), selLepton_sublead->p4().pz(), selLepton_sublead->p4().energy());
  TLorentzVector hmeBJet1P4(selJet_Hbb_lead->p4().px(), selJet_Hbb_lead->p4().py(), selJet_Hbb_lead->p4().pz(), selJet_Hbb_lead->p4().energy());
  TLorentzVector hmeBJet2P4(selJet_Hbb_sublead->p4().px(), selJet_Hbb_sublead->p4().py(), selJet_Hbb_sublead->p4().pz(), selJet_Hbb_sublead->p4().energy());
  TLorentzVector hmeMEtP4(met.p4().px(), met.p4().py(), 0., met.p4().pt());
  double hmeSumJetsPx = -(selLepton_lead->p4().px() + selLepton_sublead->p4().px() + selJet_Hbb_lead->p4().px() + selJet_Hbb_sublead->p4().px() + met.p4().px());
  double hmeSumJetsPy = -(selLepton_lead->p4().py() + selLepton_sublead->p4().py() + selJet_Hbb_lead->p4().py() + selJet_Hbb_sublead->p4().py() + met.p4().py());
  double hmeSumJetsPz = 0.;
  double hmeSumJetsEn = TMath::Sqrt(hmeSumJetsPx*hmeSumJetsPx + hmeSumJetsPy*hmeSumJetsPy);
  TLorentzVector hmeSumJetsP4(hmeSumJetsPx, hmeSumJetsPy, hmeSumJetsPz, hmeSumJetsEn);
  
  clock_->Reset();
  clock_->Start("<HMEInterface_hh_bb2l::operator()>");
  heavyMassEstimator hmeAlgo(
    hmeLepton1P4, hmeLepton2P4, hmeBJet1P4, hmeBJet2P4, hmeSumJetsP4, hmeMEtP4,
    PUSample_, ievent, weightfromonshellnupt_func_, weightfromonshellnupt_hist_, weightfromonoffshellWmass_hist_,
    iterations_, RefPDFfile_.fullPath(), useMET_, bjetrescaleAlgo_, metcorrection_
  );
  double m_HH_hme = -1.;
  bool hme_isValidSolution = hmeAlgo.runheavyMassEstimator();
  if ( hme_isValidSolution )
  {
    const TH1F& hmeHist = hmeAlgo.getheavyMassEstimatorh2();
    m_HH_hme = hmeHist.GetXaxis()->GetBinCenter(hmeHist.GetMaximumBin());
  }

  clock_->Stop("<HMEInterface_hh_bb2l::operator()>");

  result.fillInputs(selLepton_lead, selLepton_sublead, selJet_Hbb_lead, selJet_Hbb_sublead);
  result.m_HH_hme_ = m_HH_hme;
  result.cpuTime_ = clock_->GetCpuTime("<HMEInterface_hh_bb2l::operator()>");
  result.realTime_ = clock_->GetRealTime("<HMEInterface_hh_bb2l::operator()>");
  result.isValid_ = (hme_isValidSolution);

  return result;
}

