#include "hhAnalysis/bbww/interface/HHatLOvsNLOHistManager.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), fillWithOverFlow2d()
#include "tthAnalysis/HiggsToTauTau/interface/mvaInputVariables.h"     // comp_cosThetaStar

HHatLOvsNLOHistManager::HHatLOvsNLOHistManager(const edm::ParameterSet & cfg)
  : HistManagerBase(cfg)
{
  central_or_shiftOptions_["genHBoson_lead_pt"]        = { "central" };
  central_or_shiftOptions_["genHBoson_lead_eta"]       = { "central" };
  central_or_shiftOptions_["genHBoson_sublead_pt"]     = { "central" };
  central_or_shiftOptions_["genHBoson_sublead_eta"]    = { "central" };
  central_or_shiftOptions_["genHH_mass"]               = { "central" };
  central_or_shiftOptions_["genHH_pt"]                 = { "central" };
  central_or_shiftOptions_["genHH_absCosThetaStar"]    = { "central" };
  central_or_shiftOptions_["HHReweight_vs_genHH_mass"] = { "central" };
}

void
HHatLOvsNLOHistManager::bookHistograms(TFileDirectory & dir)
{
  histogram_genHBoson_lead_pt_        = book1D(dir, "genHBoson_lead_pt",        "genHBoson_lead_pt",         50,  0.,  500.);
  histogram_genHBoson_lead_eta_       = book1D(dir, "genHBoson_lead_eta",       "genHBoson_lead_eta",       100, -5.0,  +5.0);
  histogram_genHBoson_sublead_pt_     = book1D(dir, "genHBoson_sublead_pt",     "genHBoson_sublead_pt",      50,  0.,  500.);
  histogram_genHBoson_sublead_eta_    = book1D(dir, "genHBoson_sublead_eta",    "genHBoson_sublead_eta",    100, -5.0,  +5.0);

  int numBins_genHH_mass = 36;
  double binning_genHH_mass[] = {
     250,  270,  290,  310,  330,  350,  370, 390,  410,  430, 
     450,  470,  490,  510,  530,  550,  570, 590,  610,  630, 
     650,  670,  700,  750,  800,  850,  900, 950, 1000, 1100, 
    1200, 1300, 1400, 1500, 1750, 2000, 5000
  };
  histogram_genHH_mass_               = book1D(dir, "genHH_mass",               "genHH_mass",               numBins_genHH_mass, binning_genHH_mass);
  histogram_genHH_pt_                 = book1D(dir, "genHH_pt",                 "genHH_pt",                  50,  0.,  500.);
  histogram_genHH_absCosThetaStar_    = book1D(dir, "genHH_absCosThetaStar",    "genHH_absCosThetaStar",     10,  0.,   +1.);  

  //histogram_HHReweight_vs_genHH_mass_ = book2D(dir, "HHReweight_vs_genHH_mass", "HHReweight_vs_genHH_mass", numBins_genHH_mass, binning_genHH_mass, 200, 0., 2.);
}

void
HHatLOvsNLOHistManager::fillHistograms(const Particle::LorentzVector & genHBosonP4_lead,
                                       const Particle::LorentzVector & genHBosonP4_sublead,
		                       double evtWeight,
                                       double hhWeight)
{
  const double evtWeight_and_hhWeight  = evtWeight*hhWeight;
  const double evtWeightErr = 0.;

  Particle::LorentzVector genHHP4 = genHBosonP4_lead + genHBosonP4_sublead;
  double genHH_mass = genHHP4.mass();
  double genHH_pt = genHHP4.pt();
  double genHH_cosThetaStar = std::fabs(comp_cosThetaStar(genHBosonP4_lead, genHBosonP4_sublead));

  fillWithOverFlow(histogram_genHBoson_lead_pt_, genHBosonP4_lead.pt(), evtWeight_and_hhWeight, evtWeightErr);
  fillWithOverFlow(histogram_genHBoson_lead_eta_, genHBosonP4_lead.eta(), evtWeight_and_hhWeight, evtWeightErr);
  fillWithOverFlow(histogram_genHBoson_sublead_pt_, genHBosonP4_sublead.pt(), evtWeight_and_hhWeight, evtWeightErr);
  fillWithOverFlow(histogram_genHBoson_sublead_eta_, genHBosonP4_sublead.eta(), evtWeight_and_hhWeight, evtWeightErr);

  fillWithOverFlow(histogram_genHH_mass_, genHH_mass, evtWeight_and_hhWeight, evtWeightErr);
  fillWithOverFlow(histogram_genHH_pt_, genHH_pt, evtWeight_and_hhWeight, evtWeightErr);
  fillWithOverFlow(histogram_genHH_absCosThetaStar_, genHH_cosThetaStar, evtWeight_and_hhWeight, evtWeightErr);

  //fillWithOverFlow2d(histogram_HHReweight_vs_genHH_mass_, genHH_mass, hhWeight, evtWeight, evtWeightErr);
}
