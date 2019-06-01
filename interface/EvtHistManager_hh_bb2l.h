#ifndef hhAnalysis_bbww_EvtHistManager_hh_bb2l_h
#define hhAnalysis_bbww_EvtHistManager_hh_bb2l_h

/** \class EvtHistManager_hh_bb2l
 *
 * Book and fill histograms for event-level quantities in the dilepton category
 * of the HH->bbWW analysis
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h" // HistManagerBase

#include "hhAnalysis/bbwwMEM/interface/MEMResult.h" // MEMbbwwResultDilepton

class EvtHistManager_hh_bb2l
  : public HistManagerBase
{
public:
  EvtHistManager_hh_bb2l(const edm::ParameterSet & cfg);
  ~EvtHistManager_hh_bb2l() {}

  /// book and fill histograms
  void
  bookHistograms(TFileDirectory & dir) override;

  void
  fillHistograms(int numElectrons,
                 int numMuons,
                 int numJets,
                 int numBJets_loose,
                 int numBJets_medium,
		 const MEMbbwwResultDilepton* memResult, double memCpuTime,
		 const MEMbbwwResultDilepton* memResult_missingBJet, double memCpuTime_missingBJet,
		 double mvaoutput300, double mvaoutput400, double mvaoutput750,
		 double mvaoutputnohiggnessnotopness300, double mvaoutputnohiggnessnotopness400, double mvaoutputnohiggnessnotopness750,
		 double mvaoutput_bb2l_node3, double mvaoutput_bb2l_node7, double mvaoutput_bb2l_sm,
		 double evtWeight);

  const TH1 *
  getHistogram_EventCounter() const;

  /// flag to enable/disable booking & filling of MEM histograms
  enum { kOption_undefined, kOption_memDisabled, kOption_memEnabled };

 private:
  TH1 * histogram_numElectrons_;
  TH1 * histogram_numMuons_;
  TH1 * histogram_numJets_;
  TH1 * histogram_numBJets_loose_;
  TH1 * histogram_numBJets_medium_;

  TH1 * histogram_log_memProb_signal_;
  TH1 * histogram_log_memProbErr_signal_;
  TH1 * histogram_log_memProb_background_;
  TH1 * histogram_log_memProbErr_background_;
  TH1 * histogram_memLR_;
  TH1 * histogram_log_memLR_div_Err_;
  TH1 * histogram_memScore_;
  TH1 * histogram_memCpuTime_;

  TH1 * histogram_log_memProb_signal_missingBJet_;
  TH1 * histogram_log_memProbErr_signal_missingBJet_;
  TH1 * histogram_log_memProb_background_missingBJet_;
  TH1 * histogram_log_memProbErr_background_missingBJet_;
  TH1 * histogram_memLR_missingBJet_;
  TH1 * histogram_log_memLR_div_Err_missingBJet_;
  TH1 * histogram_memScore_missingBJet_;
  TH1 * histogram_memCpuTime_missingBJet_;

  TH1 * histogram_MVAOutput300_;
  TH1 * histogram_MVAOutput400_;
  TH1 * histogram_MVAOutput750_;
  TH1 * histogram_MVAOutputnohiggnessnotopness300_;
  TH1 * histogram_MVAOutputnohiggnessnotopness400_;
  TH1 * histogram_MVAOutputnohiggnessnotopness750_;
  TH1 * histogram_MVAOutputnode3_;
  TH1 * histogram_MVAOutputnode7_;
  TH1 * histogram_MVAOutputsm_;


  TH1 * histogram_EventCounter_;

  int option_; // flag to enable/disable booking & filling of MEM histograms
};

#endif
