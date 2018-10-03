#include "hhAnalysis/bbww/interface/RecoJetCollectionSelectorAK8_bbWW_Hbb.h" // RecoJetSelectorAK8_bbWW_Hbb

RecoJetSelectorAK8_bbWW_Hbb::RecoJetSelectorAK8_bbWW_Hbb(int era, int index, bool debug)
  : min_pt_(200.)
  , max_absEta_(2.4)
  , min_jetId_(2)
  , min_msoftdrop_(30.)
  , max_msoftdrop_(210.)
  , max_tau2_div_tau1_(+1.e+3)
  , min_subjet1_pt_(20.)
  , max_subjet1_absEta_(2.4)
  , min_subjet1_BtagCSV_(-1.e+3)
  , min_subjet2_pt_(20.)
  , max_subjet2_absEta_(2.4)
  , min_subjet2_BtagCSV_(-1.e+3)
  , debug_(debug)
{}

void
RecoJetSelectorAK8_bbWW_Hbb::set_min_pt(double min_pt)
{
  min_pt_ = min_pt;
}

void
RecoJetSelectorAK8_bbWW_Hbb::set_max_absEta(double max_absEta)
{
  max_absEta_ = max_absEta;
}

void
RecoJetSelectorAK8_bbWW_Hbb::set_min_msoftdrop(double min_msoftdrop)
{
  min_msoftdrop_ = min_msoftdrop;
}

void
RecoJetSelectorAK8_bbWW_Hbb::set_max_msoftdrop(double max_msoftdrop)
{
  max_msoftdrop_ = max_msoftdrop;
}

void
RecoJetSelectorAK8_bbWW_Hbb::set_max_tau2_div_tau1(double max_tau2_div_tau1)
{
  max_tau2_div_tau1_ = max_tau2_div_tau1;
}

void
RecoJetSelectorAK8_bbWW_Hbb::set_min_subjet1_pt(double min_pt)
{
  min_subjet1_pt_ = min_pt;
}

void
RecoJetSelectorAK8_bbWW_Hbb::set_max_subjet1_absEta(double max_absEta)
{
  max_subjet1_absEta_ = max_absEta;
}

void
RecoJetSelectorAK8_bbWW_Hbb::set_min_subjet1_BtagCSV(double min_BtagCSV)
{
  min_subjet1_BtagCSV_ = min_BtagCSV;
}

void
RecoJetSelectorAK8_bbWW_Hbb::set_min_subjet2_pt(double min_pt)
{
  min_subjet2_pt_ = min_pt;
}

void
RecoJetSelectorAK8_bbWW_Hbb::set_max_subjet2_absEta(double max_absEta)
{
  max_subjet2_absEta_ = max_absEta;
}

void
RecoJetSelectorAK8_bbWW_Hbb::set_min_subjet2_BtagCSV(double min_BtagCSV)
{
  min_subjet2_BtagCSV_ = min_BtagCSV;
}

void 
RecoJetSelectorAK8_bbWW_Hbb::set_min_jetId(int min_jetId)
{
  min_jetId_ = min_jetId;
}

double
RecoJetSelectorAK8_bbWW_Hbb::get_min_pt() const
{
  return min_pt_;
}

double
RecoJetSelectorAK8_bbWW_Hbb::get_max_absEta() const
{
  return max_absEta_;
}

double
RecoJetSelectorAK8_bbWW_Hbb::get_min_msoftdrop() const
{
  return min_msoftdrop_;
}

double
RecoJetSelectorAK8_bbWW_Hbb::get_max_msoftdrop() const
{
  return max_msoftdrop_;
}

double
RecoJetSelectorAK8_bbWW_Hbb::get_max_tau2_div_tau1() const
{
  return max_tau2_div_tau1_;
}

double
RecoJetSelectorAK8_bbWW_Hbb::get_min_subjet1_pt() const
{
  return min_subjet1_pt_;
}

double
RecoJetSelectorAK8_bbWW_Hbb::get_max_subjet1_absEta() const
{
  return max_subjet1_absEta_;
}

double
RecoJetSelectorAK8_bbWW_Hbb::get_min_subjet1_BtagCSV() const
{
  return min_subjet1_BtagCSV_;
}

double
RecoJetSelectorAK8_bbWW_Hbb::get_min_subjet2_pt() const
{
  return min_subjet2_pt_;
}

double
RecoJetSelectorAK8_bbWW_Hbb::get_max_subjet2_absEta() const
{
  return max_subjet2_absEta_;
}

double
RecoJetSelectorAK8_bbWW_Hbb::get_min_subjet2_BtagCSV() const
{
  return min_subjet2_BtagCSV_;
}

bool
RecoJetSelectorAK8_bbWW_Hbb::operator()(const RecoJetAK8 & jet) const
{
  const bool passes =
    jet.pt()                 >= min_pt_              &&
    jet.absEta()             <= max_absEta_          &&
    (jet.jetId() % 4)        >= min_jetId_           && // CV: loose (tight) jetId is stored in bit 0 (1), 
                                                        //     with value of 1 (2) in case the jet passes the loose (tight) jetId
    jet.msoftdrop()          >= min_msoftdrop_       &&
    jet.msoftdrop()          >= max_msoftdrop_       &&
    (jet.tau2()/jet.tau1())  <= max_tau2_div_tau1_   && // cut on N-subjettiness ratio tau2/tau1
    jet.subJet1()                                    && 
    jet.subJet1()->pt()      >= min_subjet1_pt_      && 
    jet.subJet1()->absEta()  <= max_subjet1_absEta_  && 
    jet.subJet1()->BtagCSV() >= min_subjet1_BtagCSV_ &&
    jet.subJet2()                                    && 
    jet.subJet2()->pt()      >= min_subjet2_pt_      && 
    jet.subJet2()->absEta()  <= max_subjet2_absEta_  && 
    jet.subJet2()->BtagCSV() >= min_subjet2_BtagCSV_ 
  ;
  if(debug_)
  {
    std::cout << "<RecoJetSelectorAK8_bbWW_Hbb::operator()>:\n jet: " << jet << " "
                 "(" << (passes ? "passes" : "fails") << ")\n"
    ;
  }
  return passes;
}
