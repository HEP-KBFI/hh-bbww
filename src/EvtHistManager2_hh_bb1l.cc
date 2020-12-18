#include "hhAnalysis/bbww/interface/EvtHistManager2_hh_bb1l.h"

#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h"          // cmsException()
#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), fillWithOverFlow2d()
#include "hhAnalysis/bbww/interface/JPAInterface.h"                    // get_jpaCategory_string, JPA::Category_resolved, JPA::Category_boosted

#include <TAxis.h> // TAxis
#include <TMath.h> // TMath::Pi()

EvtHistManager2_hh_bb1l::EvtHistManager2_hh_bb1l(const edm::ParameterSet & cfg)
  : HistManagerBase(cfg)
{
  central_or_shiftOptions_["numElectrons"] = { "central" };
  central_or_shiftOptions_["numMuons"] = { "central" };
  central_or_shiftOptions_["numJets"] = { "central" };
  central_or_shiftOptions_["numBJets_loose"] = { "central" };
  central_or_shiftOptions_["numBJets_medium"] = { "central" };
  central_or_shiftOptions_["HT"] = { "central" };
  central_or_shiftOptions_["STMET"] = { "central" };
  central_or_shiftOptions_["m_Hbb"] = { "central" };
  central_or_shiftOptions_["dR_Hbb"] = { "central" };
  central_or_shiftOptions_["dPhi_Hbb"] = { "central" };
  central_or_shiftOptions_["pT_Hbb"] = { "central" };
  central_or_shiftOptions_["m_Wjj"] = { "central" };
  central_or_shiftOptions_["dR_Wjj"] = { "central" };
  central_or_shiftOptions_["dPhi_Wjj"] = { "central" };
  central_or_shiftOptions_["pT_Wjj"] = { "central" };
  central_or_shiftOptions_["dR_Hww"] = { "central" };
  central_or_shiftOptions_["dPhi_Hww"] = { "central" };
  central_or_shiftOptions_["pT_Hww"] = { "central" };
  central_or_shiftOptions_["Smin_Hww"] = { "central" };
  central_or_shiftOptions_["m_HHvis"] = { "*" };
  central_or_shiftOptions_["m_HH"] = { "central" };
  central_or_shiftOptions_["m_HH_B2G_18_008"] = { "*" };
  central_or_shiftOptions_["dR_HH"] = { "central" };
  central_or_shiftOptions_["dPhi_HH"] = { "central" };
  central_or_shiftOptions_["pT_HH"] = { "central" };
  central_or_shiftOptions_["Smin_HH"] = { "central" };
  central_or_shiftOptions_["mT_W"] = { "central" };
  central_or_shiftOptions_["mT_top_2particle"] = { "central" };
  central_or_shiftOptions_["mT_top_3particle"] = { "central" };
  central_or_shiftOptions_["vbf_jet1_pt"] = { "central" };
  central_or_shiftOptions_["vbf_jet1_eta"] = { "central" };
  central_or_shiftOptions_["vbf_jet2_pt"] = { "central" };
  central_or_shiftOptions_["vbf_jet2_eta"] = { "central" };
  central_or_shiftOptions_["vbf_m_jj"] = { "central" };
  central_or_shiftOptions_["vbf_dEta_jj"] = { "central" };
  central_or_shiftOptions_["jpaCategory"] = { "central" };
  central_or_shiftOptions_["evtCategory"] = { "central" };
  central_or_shiftOptions_["EventCounter"] = { "*" };
}

const TH1 *
EvtHistManager2_hh_bb1l::getHistogram_EventCounter() const
{
  return histogram_EventCounter_;
}

void
EvtHistManager2_hh_bb1l::bookHistograms(TFileDirectory & dir)
{
  histogram_numElectrons_     = book1D(dir, "numElectrons",       5, -0.5,  +4.5);
  histogram_numMuons_         = book1D(dir, "numMuons",           5, -0.5,  +4.5);
  histogram_numJets_          = book1D(dir, "numJets",           20, -0.5, +19.5);
  histogram_numBJets_loose_   = book1D(dir, "numBJets_loose",    10, -0.5,  +9.5);
  histogram_numBJets_medium_  = book1D(dir, "numBJets_medium",   10, -0.5,  +9.5);

  histogram_HT_               = book1D(dir, "HT",               150,  0., 1500.);
  histogram_STMET_            = book1D(dir, "STMET",            150,  0., 1500.);

  histogram_m_Hbb_            = book1D(dir, "m_Hbb",             40,  0.,  200.);
  histogram_dR_Hbb_           = book1D(dir, "dR_Hbb",           100,  0.,    5.);
  histogram_dPhi_Hbb_         = book1D(dir, "dPhi_Hbb",          36,  0., TMath::Pi());
  histogram_pT_Hbb_           = book1D(dir, "pT_Hbb",           100,  0.,  500.);

  histogram_m_Wjj_            = book1D(dir, "m_Wjj",             40,  0.,  200.);
  histogram_dR_Wjj_           = book1D(dir, "dR_Wjj",           100,  0.,    5.);
  histogram_dPhi_Wjj_         = book1D(dir, "dPhi_Wjj",          36,  0., TMath::Pi());
  histogram_pT_Wjj_           = book1D(dir, "pT_Wjj",           100,  0.,  500.);

  histogram_dR_Hww_           = book1D(dir, "dR_Hww",           100,  0.,    5.);
  histogram_dPhi_Hww_         = book1D(dir, "dPhi_Hww",          36,  0., TMath::Pi());
  histogram_pT_Hww_           = book1D(dir, "pT_Hww",           100,  0.,  500.);
  histogram_Smin_Hww_         = book1D(dir, "Smin_Hww",         100,  0.,  500.);

  histogram_m_HHvis_          = book1D(dir, "m_HHvis",          100,  0., 1000.);
  histogram_m_HH_             = book1D(dir, "m_HH",             150,  0., 1500.);
  histogram_m_HH_B2G_18_008_  = book1D(dir, "m_HH_B2G_18_008",  150,  0., 1500.);
  histogram_dR_HH_            = book1D(dir, "dR_HH",            100,  0.,    5.);
  histogram_dPhi_HH_          = book1D(dir, "dPhi_HH",           36,  0., TMath::Pi());
  histogram_pT_HH_            = book1D(dir, "pT_HH",            100,  0.,  500.);
  histogram_Smin_HH_          = book1D(dir, "Smin_HH",          100,  0., 1000.);

  histogram_mT_W_             = book1D(dir, "mT_W",              40,  0.,  200.);
  histogram_mT_top_2particle_ = book1D(dir, "mT_top_2particle", 100,  0.,  500.);
  histogram_mT_top_3particle_ = book1D(dir, "mT_top_3particle", 100,  0.,  500.);

  histogram_vbf_jet1_pt_      = book1D(dir, "vbf_jet1_pt",       40,  0.,  200.);
  histogram_vbf_jet1_eta_     = book1D(dir, "vbf_jet1_eta",     100, -5.0,  +5.0);
  histogram_vbf_jet2_pt_      = book1D(dir, "vbf_jet2_pt",       40,  0.,  200.);
  histogram_vbf_jet2_eta_     = book1D(dir, "vbf_jet2_eta",     100, -5.0,  +5.0);
  histogram_vbf_m_jj_         = book1D(dir, "vbf_m_jj",         150,  0., 1500.);
  histogram_vbf_dEta_jj_      = book1D(dir, "vbf_dEta_jj",      100,  0.,   10.);

  histogram_jpaCategory_      = book1D(dir, "jpaCategory",       15, -0.5, +14.5);
  if ( histogram_jpaCategory_ ) {
    TAxis* xAxis_jpaCategory = histogram_jpaCategory_->GetXaxis();
    for ( int jpaCategory = (int)JPA::Category_resolved::k2b2W; jpaCategory <= (int)JPA::Category_resolved::k0b; ++jpaCategory )
    {
      int idxBin = xAxis_jpaCategory->FindBin(jpaCategory);
      xAxis_jpaCategory->SetBinLabel(idxBin, get_jpaCategory_string(jpaCategory).data());
    }
    for ( int jpaCategory = (int)JPA::Category_boosted::k2b2W; jpaCategory <= (int)JPA::Category_boosted::k2b0W; ++jpaCategory )
    {
      int idxBin = xAxis_jpaCategory->FindBin(jpaCategory);
      xAxis_jpaCategory->SetBinLabel(idxBin, get_jpaCategory_string(jpaCategory).data());
    }
  }

  histogram_evtCategory_      = book1D(dir, "evtCategory",        4, -0.5,  +3.5);
  if ( histogram_evtCategory_ )
  {
    TAxis* xAxis_evtCategory = histogram_evtCategory_->GetXaxis();
    xAxis_evtCategory->SetBinLabel(1, "Undefined");
    xAxis_evtCategory->SetBinLabel(2, "Resolved 2b");
    xAxis_evtCategory->SetBinLabel(3, "Resolved 1b");
    xAxis_evtCategory->SetBinLabel(4, "Boosted");
  }
  histogram_EventCounter_     = book1D(dir, "EventCounter",       1, -0.5,  +0.5);
}

void
EvtHistManager2_hh_bb1l::fillHistograms(int numElectrons,
		 		        int numMuons,
			 	        int numJets,
				        int numBJets_loose,
				        int numBJets_medium,
				        double HT,
				        double STMET,
				        double m_Hbb, double dR_Hbb, double dPhi_Hbb, double pT_Hbb,
				        double m_Wjj, double dR_Wjj, double dPhi_Wjj, double pT_Wjj,
				        double dR_Hww, double dPhi_Hww, double pT_Hww, double Smin_Hww,
				        double m_HHvis, double m_HH, double m_HH_B2G_18_008, double dR_HH, double dPhi_HH, double pT_HH, double Smin_HH,
				        double mT_W, double mT_top_2particle, double mT_top_3particle,
				        double vbf_jet1_pt, double vbf_jet1_eta, double vbf_jet2_pt, double vbf_jet2_eta, double vbf_m_jj, double vbf_dEta_jj,
                                        const JPA& jpa, const RecoJetAK8* selJetAK8_Hbb,
				        double evtWeight)
{
  const double evtWeightErr = 0.;

  fillWithOverFlow(histogram_numElectrons_,     numElectrons,      evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numMuons_,         numMuons,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJets_,          numJets,           evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_loose_,   numBJets_loose,    evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_medium_,  numBJets_medium,   evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_HT_,               HT,                evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_STMET_,            STMET,             evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_m_Hbb_,            m_Hbb,             evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dR_Hbb_,           dR_Hbb,            evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_Hbb_,         dPhi_Hbb,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_Hbb_,           pT_Hbb,            evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_m_Wjj_,            m_Wjj,             evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dR_Wjj_,           dR_Wjj,            evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_Wjj_,         dPhi_Wjj,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_Wjj_,           pT_Wjj,            evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_dR_Hww_,           dR_Hww,            evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_Hww_,         dPhi_Hww,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_Hww_,           pT_Hww,            evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_Smin_Hww_,         Smin_Hww,          evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_m_HHvis_,          m_HHvis,           evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_m_HH_,             m_HH,              evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_m_HH_B2G_18_008_,  m_HH_B2G_18_008,   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dR_HH_,            dR_HH,             evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_HH_,          dPhi_HH,           evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_HH_,            pT_HH,             evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_Smin_HH_,          Smin_HH,           evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_mT_W_,             mT_W,              evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT_top_2particle_, mT_top_2particle,  evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT_top_3particle_, mT_top_3particle,  evtWeight, evtWeightErr);

  if ( vbf_jet1_pt > 0. ) {
    fillWithOverFlow(histogram_vbf_jet1_pt_,    vbf_jet1_pt,       evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_vbf_jet1_eta_,   vbf_jet1_eta,      evtWeight, evtWeightErr);
  }
  if ( vbf_jet2_pt > 0. ) {
    fillWithOverFlow(histogram_vbf_jet2_pt_,    vbf_jet2_pt,       evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_vbf_jet2_eta_,   vbf_jet2_eta,      evtWeight, evtWeightErr);
  }
  fillWithOverFlow(histogram_vbf_m_jj_,         vbf_m_jj,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_vbf_dEta_jj_,      vbf_dEta_jj,       evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_jpaCategory_,      jpa.jpaCategory(), evtWeight, evtWeightErr);
  int evtCategory = 0;
  if      ( selJetAK8_Hbb        ) evtCategory = 3;
  else if ( numBJets_medium >= 2 ) evtCategory = 2;
  else if ( numBJets_medium >= 1 ) evtCategory = 1;
  fillWithOverFlow(histogram_evtCategory_,      evtCategory,       evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_EventCounter_,     0.,                evtWeight, evtWeightErr);
}
