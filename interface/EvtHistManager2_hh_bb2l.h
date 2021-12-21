#ifndef hhAnalysis_bbww_EvtHistManager2_hh_bb2l_h
#define hhAnalysis_bbww_EvtHistManager2_hh_bb2l_h

/** \class EvtHistManager2_hh_bb2l
 *
 * Book and fill histograms for event-level quantities in the dilepton category
 * of the HH->bbWW analysis
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h" // HistManagerBase
#include "hhAnalysis/bbwwMEM/interface/MEMResult.h" // MEMbbwwAlgoDilepton

// forward declarations
class MEMOutput_hh_bb2l;

class EvtHistManager2_hh_bb2l
  : public HistManagerBase
{
public:
  EvtHistManager2_hh_bb2l(const edm::ParameterSet & cfg);
  ~EvtHistManager2_hh_bb2l() {}

  /// book and fill histograms
  void
  bookHistograms(TFileDirectory & dir) override;

  void
  fillHistograms(int numElectrons,
                 int numMuons,
                 int numJets,
                 int numBJets_loose,
                 int numBJets_medium, 
                 double HT,
		 double STMET,            
                 double m_Hbb, double dR_Hbb, double dPhi_Hbb, double pT_Hbb,
                 double m_ll, double dR_ll, double dPhi_ll, double pT_ll,
                 double m_HHvis, double m_HH, double m_HH_analytic,
                 double m_HH_hme, double hmeCpuTime,
                 double vbf_jet1_pt, double vbf_jet1_eta, double vbf_jet2_pt, double vbf_jet2_eta, double vbf_m_jj, double vbf_dEta_jj,
                 double evtWeight);

  const TH1 *
  getHistogram_EventCounter() const;

 private:
  TH1 * histogram_numElectrons_;
  TH1 * histogram_numMuons_;
  TH1 * histogram_numJets_;
  TH1 * histogram_numBJets_loose_;
  TH1 * histogram_numBJets_medium_;

  TH1 * histogram_HT_;
  TH1 * histogram_STMET_;

  TH1 * histogram_m_Hbb_;
  TH1 * histogram_dR_Hbb_;
  TH1 * histogram_dPhi_Hbb_;
  TH1 * histogram_pT_Hbb_;

  TH1 * histogram_m_ll_;
  TH1 * histogram_dR_ll_;
  TH1 * histogram_dPhi_ll_;
  TH1 * histogram_dEta_ll_;
  TH1 * histogram_pT_ll_;

  TH1 * histogram_m_HH_hme_;
  TH1* histogram_m_HH_analytic_;
  TH1 * histogram_hmeCpuTime_;
  TH1 * histogram_m_HH_;
  TH1 * histogram_m_HHvis_;

  TH1 * histogram_vbf_jet1_pt_;
  TH1 * histogram_vbf_jet1_eta_;
  TH1 * histogram_vbf_jet2_pt_;
  TH1 * histogram_vbf_jet2_eta_;
  TH1 * histogram_vbf_m_jj_;
  TH1 * histogram_vbf_dEta_jj_;

  TH1 * histogram_EventCounter_;

  int option_; // flag to enable/disable booking & filling of MEM histograms
};

#endif
