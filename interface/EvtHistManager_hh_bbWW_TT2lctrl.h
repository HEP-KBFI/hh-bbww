#ifndef hhAnalysis_bbww_EvtHistManager_hh_bbWW_TT2lctrl_h
#define hhAnalysis_bbww_EvtHistManager_hh_bbWW_TT2lctrl_h

/** \class EvtHistManager_hh_bbWW_TT2lctrl
 *
 * Book and fill histograms for event-level quantities in the tt+jets (TT) dilepton control region 
 * of the HH->bbWW analysis
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h"       // HistManagerBase
#include "tthAnalysis/HiggsToTauTau/interface/Particle.h"              // Particle::LorentzVector
#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), fillWithOverFlow2d()

#include <TH1.h>   // TH1
#include <TH2.h>   // TH2
#include <TMath.h> // TMath::Pi()

class EvtHistManager_hh_bbWW_TT2lctrl
  : public HistManagerBase
{
public:
  EvtHistManager_hh_bbWW_TT2lctrl(const edm::ParameterSet & cfg);
  ~EvtHistManager_hh_bbWW_TT2lctrl() {}

  /// book and fill histograms
  void
  bookHistograms(TFileDirectory & dir) override;

  void
  fillHistograms(int numElectrons,
                 int numMuons,
                 int numJets,
                 int numBJets_loose,
                 int numBJets_medium,
                 int numJetsAK8_Hbb,
		 double HT,
		 double STMET,
                 bool isValid_topKinReco, 
                 const Particle::LorentzVector& genMEtP4, const Particle::LorentzVector& metP4,
                 const Particle::LorentzVector& genTopQuarkP4_top, 
                 bool isGenMatched_top_assoc1, const Particle::LorentzVector& topQuarkP4_top_assoc1,
                 bool isGenMatched_top_assoc2, const Particle::LorentzVector& topQuarkP4_top_assoc2,
                 const Particle::LorentzVector& genTopQuarkP4_antitop, 
                 bool isGenMatched_antitop_assoc1, const Particle::LorentzVector& topQuarkP4_antitop_assoc1,
                 bool isGenMatched_antitop_assoc2, const Particle::LorentzVector& topQuarkP4_antitop_assoc2,
		 const Particle::LorentzVector& selLeptonP4_lead, const Particle::LorentzVector& selLeptonP4_sublead,
                 double m_HH_hme,
                 double vbf_m_jj, double vbf_dEta_jj,
		 double evtWeight);

  const TH1 *
  getHistogram_EventCounter() const;

 private:
  TH1 * histogram_numElectrons_;
  TH1 * histogram_numMuons_;
  TH1 * histogram_numHadTaus_;
  TH1 * histogram_numJets_;
  TH1 * histogram_numBJets_loose_;
  TH1 * histogram_numBJets_medium_;
  TH1 * histogram_numJetsAK8_Hbb_; 

  TH1 * histogram_HT_;
  TH1 * histogram_STMET_;

  TH1 * histogram_genMEt_pt_;
  TH1 * histogram_genMEt_eta_;
  TH1 * histogram_genMEt_phi_;
  TH1 * histogram_recMEt_pt_;
  TH1 * histogram_recMEt_eta_;
  TH1 * histogram_recMEt_phi_;
  TH1 * histogram_deltaMEt_eta_;
  TH1 * histogram_deltaMEt_px_;
  TH1 * histogram_deltaMEt_py_;

  TH1 * histogram_genTop_pt_;
  TH1 * histogram_genTop_eta_;
  TH1 * histogram_genTop_phi_;

  TH1 * histogram_genAntiTop_pt_;
  TH1 * histogram_genAntiTop_eta_;
  TH1 * histogram_genAntiTop_phi_;

  TH1 * histogram_genTopPair_mass_;
  TH1 * histogram_genTopPair_pt_;

  struct histogramEntryType
  {
    histogramEntryType(const std::string& association, std::map<std::string, std::vector<std::string>>& central_or_shiftOptions)
      : association_(association)
    {
      central_or_shiftOptions[Form("top_pt_%s", association_.data())] = { "*" };
      central_or_shiftOptions[Form("top_eta_%s", association_.data())] = { "central" };
      central_or_shiftOptions[Form("top_phi_%s", association_.data())] = { "central" };
      central_or_shiftOptions[Form("genTop_pt_vs_top_pt_%s", association_.data())] = { "central" };
      central_or_shiftOptions[Form("deltaTop_pt_%s", association_.data())] = { "central" };
      central_or_shiftOptions[Form("deltaTop_pt_vs_genTop_pt_%s", association_.data())] = { "central" };
      central_or_shiftOptions[Form("deltaTop_eta_%s", association_.data())] = { "central" };
      central_or_shiftOptions[Form("deltaTop_phi_%s", association_.data())] = { "central" };
      central_or_shiftOptions[Form("antiTop_pt_%s", association_.data())] = { "*" };
      central_or_shiftOptions[Form("antiTop_eta_%s", association_.data())] = { "central" };
      central_or_shiftOptions[Form("antiTop_phi_%s", association_.data())] = { "central" };
      central_or_shiftOptions[Form("genAntiTop_pt_vs_antiTop_pt_%s", association_.data())] = { "central" };
      central_or_shiftOptions[Form("deltaAntiTop_pt_%s", association_.data())] = { "central" };
      central_or_shiftOptions[Form("deltaAntiTop_pt_vs_genAntiTop_pt_%s", association_.data())] = { "central" };
      central_or_shiftOptions[Form("deltaAntiTop_eta_%s", association_.data())] = { "central" };
      central_or_shiftOptions[Form("deltaAntiTop_phi_%s", association_.data())] = { "central" };
      central_or_shiftOptions[Form("topPair_mass_%s", association_.data())] = { "central" };
      central_or_shiftOptions[Form("deltaTopPair_mass_vs_genTopPair_mass_%s", association_.data())] = { "central" };
      central_or_shiftOptions[Form("topPair_pt_%s", association_.data())] = { "central" };
      central_or_shiftOptions[Form("deltaTopPair_pt_vs_genTopPair_pt_%s", association_.data())] = { "central" };
    }
    ~histogramEntryType() {}

    void
    bookHistograms(TFileDirectory & dir, HistManagerBase* histManager)
    {
      // CV: binning in top quark pT taken from AN-2015/309 (TOP-16-001)
      int numBins_pt = 6;
      float binning_pt[numBins_pt + 1] = { 0., 65., 125., 200., 290., 400., 550. } ;

      histogram_top_pt_               = histManager->book1D(dir, Form("top_pt_%s", association_.data()),            100,    0.,  500.);
      histogram_top_eta_              = histManager->book1D(dir, Form("top_eta_%s", association_.data()),           100,   -5.,   +5.);
      histogram_top_phi_              = histManager->book1D(dir, Form("top_phi_%s", association_.data()),            36, -TMath::Pi(), +TMath::Pi());
      histogram_genTop_pt_vs_top_pt_  = histManager->book2D(dir, Form("genTop_pt_vs_top_pt_%s", association_.data()), numBins_pt, binning_pt, numBins_pt, binning_pt);
      histogram_deltaTop_pt_          = histManager->book1D(dir, Form("deltaTop_pt_%s", association_.data()),        40, -100., +100.);
      histogram_deltaTop_pt_vs_genTop_pt_ = histManager->book2D(dir, Form("deltaTop_pt_vs_genTop_pt_%s", association_.data()), 10, 0., 250., 30, -75., +75.);
      histogram_deltaTop_eta_         = histManager->book1D(dir, Form("deltaTop_eta_%s", association_.data()),      100,   -5.,   +5.);
      histogram_deltaTop_phi_         = histManager->book1D(dir, Form("deltaTop_phi_%s", association_.data()),       36,    0., 0.2*TMath::Pi());

      histogram_antiTop_pt_           = histManager->book1D(dir, Form("antiTop_pt_%s", association_.data()),        100,    0.,  500.);
      histogram_antiTop_eta_          = histManager->book1D(dir, Form("antiTop_eta_%s", association_.data()),       100,   -5.,   +5.);
      histogram_antiTop_phi_          = histManager->book1D(dir, Form("antiTop_phi_%s", association_.data()),        36, -TMath::Pi(), +TMath::Pi());
      histogram_genAntiTop_pt_vs_antiTop_pt_ = histManager->book2D(dir, Form("genAntiTop_pt_vs_antiTop_pt_%s", association_.data()), numBins_pt, binning_pt, numBins_pt, binning_pt);
      histogram_deltaAntiTop_pt_      = histManager->book1D(dir, Form("deltaAntiTop_pt_%s", association_.data()),    40, -100., +100.);
      histogram_deltaAntiTop_pt_vs_genAntiTop_pt_ = histManager->book2D(dir, Form("deltaAntiTop_pt_vs_genAntiTop_pt_%s", association_.data()), 10, 0., 250., 30, -75., +75.);
      histogram_deltaAntiTop_eta_     = histManager->book1D(dir, Form("deltaAntiTop_eta_%s", association_.data()),  100,   -5.,   +5.);
      histogram_deltaAntiTop_phi_     = histManager->book1D(dir, Form("deltaAntiTop_phi_%s", association_.data()),   36,    0., 0.2*TMath::Pi());

      histogram_topPair_mass_         = histManager->book1D(dir, Form("topPair_mass_%s", association_.data()),      100,    0., 1000.);
      histogram_deltaTopPair_mass_vs_genTopPair_mass_ = histManager->book2D(dir, Form("deltaTopPair_mass_vs_genTopPair_mass_%s", association_.data()), 10, 0., 500., 40, -500, +500.);
      histogram_topPair_pt_           = histManager->book1D(dir, Form("topPair_pt_%s", association_.data()),        100,    0., 1000.);
      histogram_deltaTopPair_pt_vs_genTopPair_pt_ = histManager->book2D(dir, Form("deltaTopPair_pt_vs_genTopPair_pt_%s", association_.data()), 10, 0., 500., 40, -500, +500.);
    }

    void
    fillHistograms(bool isValid_topKinReco, 
                   const Particle::LorentzVector& genTopQuarkP4_top, 
                   bool isGenMatched_top_assoc1, const Particle::LorentzVector& topQuarkP4_top_assoc1,
                   bool isGenMatched_top_assoc2, const Particle::LorentzVector& topQuarkP4_top_assoc2,
                   const Particle::LorentzVector& genTopQuarkP4_antitop, 
                   bool isGenMatched_antitop_assoc1, const Particle::LorentzVector& topQuarkP4_antitop_assoc1,
                   bool isGenMatched_antitop_assoc2, const Particle::LorentzVector& topQuarkP4_antitop_assoc2,
  		   double evtWeight)
    {
      const double evtWeightErr = 0.;

      if ( isValid_topKinReco && (isGenMatched_top_assoc1 || isGenMatched_top_assoc2) && (isGenMatched_antitop_assoc1 || isGenMatched_antitop_assoc2) )
      {
        const Particle::LorentzVector* topQuarkP4_top = nullptr;
        if      ( ( isGenMatched_top_assoc1 && !isGenMatched_top_assoc2 && association_ == "correctAssoc"  ) ||
                  (!isGenMatched_top_assoc1 &&  isGenMatched_top_assoc2 && association_ == "incorrectAssoc") ) topQuarkP4_top = &topQuarkP4_top_assoc1;          
        else if ( (!isGenMatched_top_assoc1 &&  isGenMatched_top_assoc2 && association_ == "correctAssoc"  ) ||
                  ( isGenMatched_top_assoc1 && !isGenMatched_top_assoc2 && association_ == "incorrectAssoc") ) topQuarkP4_top = &topQuarkP4_top_assoc2;
        else assert(0);
        fillWithOverFlow(histogram_top_pt_,           topQuarkP4_top->pt(),      evtWeight, evtWeightErr);
        fillWithOverFlow(histogram_top_eta_,          topQuarkP4_top->eta(),     evtWeight, evtWeightErr);
        fillWithOverFlow(histogram_top_phi_,          topQuarkP4_top->phi(),     evtWeight, evtWeightErr);
        histogram_genTop_pt_vs_top_pt_->Fill(topQuarkP4_top->pt(), genTopQuarkP4_top.pt(), evtWeight);
        double deltaTop_pt = topQuarkP4_top->pt() - genTopQuarkP4_top.pt();
        fillWithOverFlow(histogram_deltaTop_pt_,      deltaTop_pt,               evtWeight, evtWeightErr);
        fillWithOverFlow2d(histogram_deltaTop_pt_vs_genTop_pt_, genTopQuarkP4_top.pt(), deltaTop_pt, evtWeight, evtWeightErr);
        double deltaTop_eta = topQuarkP4_top->eta() - genTopQuarkP4_top.eta();
        fillWithOverFlow(histogram_deltaTop_eta_,     deltaTop_eta,              evtWeight, evtWeightErr);
        double deltaTop_phi = topQuarkP4_top->phi() - genTopQuarkP4_top.phi();
        fillWithOverFlow(histogram_deltaTop_phi_,     deltaTop_phi,              evtWeight, evtWeightErr);

        const Particle::LorentzVector* topQuarkP4_antitop = nullptr;
        if      ( ( isGenMatched_antitop_assoc1 && !isGenMatched_antitop_assoc2 && association_ == "correctAssoc"  ) ||
                  (!isGenMatched_antitop_assoc1 &&  isGenMatched_antitop_assoc2 && association_ == "incorrectAssoc") ) topQuarkP4_antitop = &topQuarkP4_antitop_assoc1;          
        else if ( (!isGenMatched_antitop_assoc1 &&  isGenMatched_antitop_assoc2 && association_ == "correctAssoc"  ) ||
                  ( isGenMatched_antitop_assoc1 && !isGenMatched_antitop_assoc2 && association_ == "incorrectAssoc") ) topQuarkP4_antitop = &topQuarkP4_antitop_assoc2;
        else assert(0);
        fillWithOverFlow(histogram_antiTop_pt_,       topQuarkP4_antitop->pt(),  evtWeight, evtWeightErr);
        fillWithOverFlow(histogram_antiTop_eta_,      topQuarkP4_antitop->eta(), evtWeight, evtWeightErr);
        fillWithOverFlow(histogram_antiTop_phi_,      topQuarkP4_antitop->phi(), evtWeight, evtWeightErr);
        histogram_genAntiTop_pt_vs_antiTop_pt_->Fill(topQuarkP4_antitop->pt(), genTopQuarkP4_antitop.pt(), evtWeight);
        double deltaAntiTop_pt = topQuarkP4_antitop->pt() - genTopQuarkP4_antitop.pt();
        fillWithOverFlow(histogram_deltaAntiTop_pt_,  deltaAntiTop_pt,          evtWeight, evtWeightErr);
        fillWithOverFlow2d(histogram_deltaAntiTop_pt_vs_genAntiTop_pt_, genTopQuarkP4_antitop.pt(), deltaAntiTop_pt, evtWeight, evtWeightErr);
        double deltaAntiTop_eta = topQuarkP4_antitop->eta() - genTopQuarkP4_antitop.eta();
        fillWithOverFlow(histogram_deltaAntiTop_eta_, deltaAntiTop_eta,         evtWeight, evtWeightErr);
        double deltaAntiTop_phi = topQuarkP4_antitop->phi() - genTopQuarkP4_antitop.phi();
        fillWithOverFlow(histogram_deltaAntiTop_phi_, deltaAntiTop_phi,         evtWeight, evtWeightErr);

        Particle::LorentzVector genTopPairP4 = genTopQuarkP4_top + genTopQuarkP4_antitop;
        Particle::LorentzVector topPairP4 = *topQuarkP4_top + *topQuarkP4_antitop;
        fillWithOverFlow(histogram_topPair_mass_,     topPairP4.mass(),         evtWeight, evtWeightErr);
        fillWithOverFlow2d(histogram_deltaTopPair_mass_vs_genTopPair_mass_, genTopPairP4.mass(), topPairP4.mass() - genTopPairP4.mass(), evtWeight, evtWeightErr);
        fillWithOverFlow(histogram_topPair_pt_,       topPairP4.pt(),           evtWeight, evtWeightErr);
        fillWithOverFlow2d(histogram_deltaTopPair_pt_vs_genTopPair_pt_, genTopPairP4.pt(), topPairP4.pt() - genTopPairP4.pt(), evtWeight, evtWeightErr);
      }
    }

    std::string association_;

    TH1 * histogram_top_pt_;
    TH1 * histogram_top_eta_;
    TH1 * histogram_top_phi_;
    TH2 * histogram_genTop_pt_vs_top_pt_;
    TH1 * histogram_deltaTop_pt_;
    TH2 * histogram_deltaTop_pt_vs_genTop_pt_;
    TH1 * histogram_deltaTop_eta_;
    TH1 * histogram_deltaTop_phi_;

    TH1 * histogram_genAntiTop_pt_;
    TH1 * histogram_genAntiTop_eta_;
    TH1 * histogram_genAntiTop_phi_;
    TH1 * histogram_antiTop_pt_;
    TH1 * histogram_antiTop_eta_;
    TH1 * histogram_antiTop_phi_;
    TH2 * histogram_genAntiTop_pt_vs_antiTop_pt_;
    TH1 * histogram_deltaAntiTop_pt_;
    TH2 * histogram_deltaAntiTop_pt_vs_genAntiTop_pt_;
    TH1 * histogram_deltaAntiTop_eta_;
    TH1 * histogram_deltaAntiTop_phi_;
   
    TH1 * histogram_topPair_mass_;
    TH2 * histogram_deltaTopPair_mass_vs_genTopPair_mass_;
    TH1 * histogram_topPair_pt_;
    TH2 * histogram_deltaTopPair_pt_vs_genTopPair_pt_;
  };
  std::vector<std::string> associations_; // { "correctAssoc", "incorrectAssoc" }
  std::map<std::string, histogramEntryType*> histograms_top_and_antiTop_; // key = "correctAssoc" or "incorrectAssoc"

  TH1 * histogram_m_ll_;
  TH1 * histogram_dR_ll_;
  TH1 * histogram_dPhi_ll_;
  TH1 * histogram_dEta_ll_;
  TH1 * histogram_pT_ll_;

  TH1 * histogram_m_HH_hme_;

  TH1 * histogram_vbf_m_jj_;
  TH1 * histogram_vbf_dEta_jj_;

  TH1 * histogram_EventCounter_;
};

#endif
