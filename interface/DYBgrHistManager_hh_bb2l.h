#ifndef hhAnalysis_bbww_DYBgrHistManager_hh_bb2l_h
#define hhAnalysis_bbww_DYBgrHistManager_hh_bb2l_h

/** \class DYBgrHistManager_hh_bb2l_h
 *
 * Book and fill histograms that are used as inputs to compute the weights
 * for the data-driven Drell-Yan background estimation,
 * cf. Section 9.2 of AN-2020/119 v6.
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h" // HistManagerBase

class DYBgrHistManager_hh_bb2l
  : public HistManagerBase
{
public:
  DYBgrHistManager_hh_bb2l(const edm::ParameterSet & cfg);
  ~DYBgrHistManager_hh_bb2l() {}

  /// book and fill histograms
  void
  bookHistograms(TFileDirectory & dir) override;

  void
  fillHistograms(double HT, double selJetAK8_Hbb_msoftdrop, bool isBoosted, int numBJets_medium, double evtWeight);

 private:
  TH1 * histogram_resolved_2b_HT_;
  TH1 * histogram_resolved_1b_HT_;
  TH1 * histogram_resolved_0b_HT_;

  TH1 * histogram_boosted_ge1b_msoftdrop_;
  TH1 * histogram_boosted_0b_msoftdrop_;
};

#endif
