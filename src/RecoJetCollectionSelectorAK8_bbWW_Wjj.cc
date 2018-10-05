#include "hhAnalysis/bbww/interface/RecoJetCollectionSelectorAK8_bbWW_Wjj.h" // RecoJetSelectorAK8_bbWW_Wjj

#include "FWCore/Utilities/interface/Exception.h" // cms::Exception
#include "DataFormats/Math/interface/deltaR.h" // deltaR

RecoJetSelectorAK8_bbWW_Wjj::RecoJetSelectorAK8_bbWW_Wjj(int era, int index, bool debug)
  : min_pt_(100.)
  , max_absEta_(2.4)
  , min_jetId_(2)
  , min_msoftdrop_(-1.e+3)
  , max_msoftdrop_(+1.e+3)
  , max_tau2_div_tau1_(0.75)
  , max_mD_(125.)
  , max_dR_lepton_(1.2)
  , min_subJet1_pt_(20.)
  , max_subJet1_absEta_(2.4)
  , min_subJet2_pt_(20.)
  , max_subJet2_absEta_(2.4)
  , lepton_(nullptr)
  , debug_(debug)
{}

void
RecoJetSelectorAK8_bbWW_Wjj::set_min_pt(double min_pt)
{
  min_pt_ = min_pt;
}

void
RecoJetSelectorAK8_bbWW_Wjj::set_max_absEta(double max_absEta)
{
  max_absEta_ = max_absEta;
}

void
RecoJetSelectorAK8_bbWW_Wjj::set_min_msoftdrop(double min_msoftdrop)
{
  min_msoftdrop_ = min_msoftdrop;
}

void
RecoJetSelectorAK8_bbWW_Wjj::set_max_msoftdrop(double max_msoftdrop)
{
  max_msoftdrop_ = max_msoftdrop;
}

void
RecoJetSelectorAK8_bbWW_Wjj::set_max_tau2_div_tau1(double max_tau2_div_tau1)
{
  max_tau2_div_tau1_ = max_tau2_div_tau1;
}

void
RecoJetSelectorAK8_bbWW_Wjj::set_max_mD(double max_mD)
{
  max_mD_ = max_mD;
}

void
RecoJetSelectorAK8_bbWW_Wjj::set_max_dR_lepton(double max_dR_lepton)
{
  max_dR_lepton_ = max_dR_lepton;
}

void
RecoJetSelectorAK8_bbWW_Wjj::set_min_subJet1_pt(double min_pt)
{
  min_subJet1_pt_ = min_pt;
}

void
RecoJetSelectorAK8_bbWW_Wjj::set_max_subJet1_absEta(double max_absEta)
{
  max_subJet1_absEta_ = max_absEta;
}

void
RecoJetSelectorAK8_bbWW_Wjj::set_min_subJet2_pt(double min_pt)
{
  min_subJet2_pt_ = min_pt;
}

void
RecoJetSelectorAK8_bbWW_Wjj::set_max_subJet2_absEta(double max_absEta)
{
  max_subJet2_absEta_ = max_absEta;
}

void 
RecoJetSelectorAK8_bbWW_Wjj::set_min_jetId(int min_jetId)
{
  min_jetId_ = min_jetId;
}

void
RecoJetSelectorAK8_bbWW_Wjj::set_lepton(const RecoLepton* lepton)
{
  lepton_ = lepton;
}

void
RecoJetSelectorAK8_bbWW_Wjj::set_neutrinoP4(const Particle::LorentzVector& neutrinoP4)
{
  neutrinoP4_ = neutrinoP4;
}

double
RecoJetSelectorAK8_bbWW_Wjj::get_min_pt() const
{
  return min_pt_;
}

double
RecoJetSelectorAK8_bbWW_Wjj::get_max_absEta() const
{
  return max_absEta_;
}

double
RecoJetSelectorAK8_bbWW_Wjj::get_min_msoftdrop() const
{
  return min_msoftdrop_;
}

double
RecoJetSelectorAK8_bbWW_Wjj::get_max_msoftdrop() const
{
  return max_msoftdrop_;
}

double
RecoJetSelectorAK8_bbWW_Wjj::get_max_tau2_div_tau1() const
{
  return max_tau2_div_tau1_;
}

double
RecoJetSelectorAK8_bbWW_Wjj::get_max_mD() const
{
  return max_mD_;
}

double
RecoJetSelectorAK8_bbWW_Wjj::get_max_dR_lepton() const
{
  return max_dR_lepton_;
}

double
RecoJetSelectorAK8_bbWW_Wjj::get_min_subJet1_pt() const
{
  return min_subJet1_pt_;
}

double
RecoJetSelectorAK8_bbWW_Wjj::get_max_subJet1_absEta() const
{
  return max_subJet1_absEta_;
}

double
RecoJetSelectorAK8_bbWW_Wjj::get_min_subJet2_pt() const
{
  return min_subJet2_pt_;
}

double
RecoJetSelectorAK8_bbWW_Wjj::get_max_subJet2_absEta() const
{
  return max_subJet2_absEta_;
}

int 
RecoJetSelectorAK8_bbWW_Wjj::get_min_jetId() const
{
  return min_jetId_;
}

bool
RecoJetSelectorAK8_bbWW_Wjj::operator()(const RecoJetAK8 & jet) const
{
  if ( !lepton_ ) 
    throw cms::Exception("RecoJetSelectorAK8_bbWW_Wjj::operator()")
      << "Value of 'lepton' has not been set. Did you call the 'set_lepton' function prior to calling operator() ?\n";
  if ( !(neutrinoP4_.energy() > 0.) )
    throw cms::Exception("RecoJetSelectorAK8_bbWW_Wjj::operator()")
      << "Value of 'neutrinoP4' has not been set. Did you call the 'set_neutrinoP4' function prior to calling operator() ?\n";
  Particle::LorentzVector WjjP4 = jet.p4();
  Particle::LorentzVector WlnuP4 = lepton_->p4() + neutrinoP4_;
  double mD = deltaR(WjjP4, WlnuP4)*0.5*(WjjP4 + WlnuP4).pt();
  double dR_lepton = deltaR(WjjP4, lepton_->p4());
  const bool passes =
    jet.pt()                 >= min_pt_               &&
    jet.absEta()             <= max_absEta_           &&
    (jet.jetId() % 4)        >= min_jetId_            && // CV: loose (tight) jetId is stored in bit 0 (1), 
                                                         //     with value of 1 (2) in case the jet passes the loose (tight) jetId
    jet.msoftdrop()          >= min_msoftdrop_        &&
    jet.msoftdrop()          >= max_msoftdrop_        &&
    (jet.tau2()/jet.tau1())  <= max_tau2_div_tau1_    && // cut on N-subjettiness ratio tau2/tau1
    mD                       <= max_mD_               && // cut on mD variable, defined by Eq.(3) in AN-2018/058 (v4)
    dR_lepton                <= max_dR_lepton_        &&
    jet.subJet1() && jet.subJet2() &&
    ((jet.subJet1()->pt()      >= min_subJet1_pt_     && 
      jet.subJet1()->absEta()  <= max_subJet1_absEta_ && 
      jet.subJet2()->pt()      >= min_subJet2_pt_     && 
      jet.subJet2()->absEta()  <= max_subJet2_absEta_) ||
     (jet.subJet1()->pt()      >= min_subJet2_pt_     && 
      jet.subJet1()->absEta()  <= max_subJet2_absEta_ && 
      jet.subJet2()->pt()      >= min_subJet1_pt_     && 
      jet.subJet2()->absEta()  <= max_subJet1_absEta_))
  ;
  if(debug_)
  {
    std::cout << "<RecoJetSelectorAK8_bbWW_Wjj::operator()>:\n jet: " << jet << " "
                 "(" << (passes ? "passes" : "fails") << ")\n"
    ;
  }
  return passes;
}
