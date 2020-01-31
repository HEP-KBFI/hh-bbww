#include "hhAnalysis/bbww/interface/analyzeMEM_genJetHistograms.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow

genJetHistograms::genJetHistograms(const std::string& label)
  : label_(label)
  , histogram_genJet1_pt_(nullptr)
  , histogram_genJet1_absEta_(nullptr)
  , histogram_genJet2_pt_(nullptr)
  , histogram_genJet2_absEta_(nullptr)
{}

genJetHistograms::~genJetHistograms() 
{}
  
void 
genJetHistograms::bookHistograms(fwlite::TFileService& fs)
{
  std::string histogramName_genJet1_pt = Form("%s1_pt", label_.data());
  histogram_genJet1_pt_ = fs.make<TH1D>(histogramName_genJet1_pt.data(), histogramName_genJet1_pt.data(), 70, 0., 350.);
  std::string histogramName_genJet1_absEta = Form("%s1_absEta", label_.data());
  histogram_genJet1_absEta_ = fs.make<TH1D>(histogramName_genJet1_absEta.data(), histogramName_genJet1_absEta.data(), 50, 0., 5.);
  std::string histogramName_genJet2_pt = Form("%s2_pt", label_.data());
  histogram_genJet2_pt_ = fs.make<TH1D>(histogramName_genJet2_pt.data(), histogramName_genJet2_pt.data(), 70, 0., 350.);
  std::string histogramName_genJet2_absEta = Form("%s2_absEta", label_.data());
  histogram_genJet2_absEta_ = fs.make<TH1D>(histogramName_genJet2_absEta.data(), histogramName_genJet2_absEta.data(), 50, 0., 5.);
}

void 
genJetHistograms::fillHistograms(const GenJet* genJet_lead, const GenJet* genJet_sublead, double min_pt, double max_absEta, double evtWeight)
{
  fillWithOverFlow(histogram_genJet1_pt_, genJet_lead->pt(), evtWeight);
  if ( genJet_lead->pt() > min_pt )
  {
    fillWithOverFlow(histogram_genJet1_absEta_, genJet_lead->absEta(), evtWeight);
  }
  fillWithOverFlow(histogram_genJet2_pt_, genJet_sublead->pt(), evtWeight);
  if ( genJet_sublead->pt() > min_pt )
  {
    fillWithOverFlow(histogram_genJet2_absEta_, genJet_sublead->absEta(), evtWeight);
  }
}

void 
fillHistograms_genJets(const std::vector<const GenJet*>& genJets, const GenJetCollectionSelector& genJetSelector,
                       genJetHistograms& histograms, double evtWeight) 
{
  if ( genJets.size() == 2 )
  {
    const GenJet* genJet_lead = genJets[0];
    const GenJet* genJet_sublead = genJets[1];
    double min_pt = genJetSelector.getSelector().get_min_pt();
    double max_absEta = genJetSelector.getSelector().get_max_absEta();
    histograms.fillHistograms(genJet_lead, genJet_sublead, min_pt, max_absEta, evtWeight);
  }
}
