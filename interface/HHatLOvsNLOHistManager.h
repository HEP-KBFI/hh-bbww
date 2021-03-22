#ifndef hhAnalysis_bbww_HHatLOvsNLOHistManager_h
#define hhAnalysis_bbww_HHatLOvsNLOHistManager_h

/** \class EvtHistManager_hh_bbWW_Wctrl
 *
 * Book and fill histograms for validating the reweighting of the LO HH MC samples
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h" // HistManagerBase
#include "tthAnalysis/HiggsToTauTau/interface/Particle.h"        // Particle::LorentzVector

class HHatLOvsNLOHistManager
  : public HistManagerBase
{
public:
  HHatLOvsNLOHistManager(const edm::ParameterSet & cfg);
  ~HHatLOvsNLOHistManager() {}

  /// book and fill histograms
  void
  bookHistograms(TFileDirectory & dir) override;

  void
  fillHistograms(const Particle::LorentzVector & genHBosonP4_lead,
                 const Particle::LorentzVector & genHBosonP4_sublead,
		 double evtWeight,
                 double hhWeight);

 private:
  TH1* histogram_genHBoson_lead_pt_;
  TH1* histogram_genHBoson_lead_eta_;
  TH1* histogram_genHBoson_sublead_pt_;
  TH1* histogram_genHBoson_sublead_eta_;

  TH1* histogram_genHH_mass_;
  TH1* histogram_genHH_pt_;
  TH1* histogram_genHH_absCosThetaStar_;

  //TH2* histogram_HHReweight_vs_genHH_mass_;
};

#endif
