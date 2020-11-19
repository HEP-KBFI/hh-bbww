#ifndef hhAnalysis_bbww_MEMHistManager_hh_bb2l_h
#define hhAnalysis_bbww_MEMHistManager_hh_bb2l_h

/** \class MEMHistManager_hh_bb2l
 *
 * Book and fill histograms of quantities computed by the matrix-element method (MEM) in the dilepton category
 * of the HH->bbWW analysis
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h" // HistManagerBase
#include "hhAnalysis/bbwwMEM/interface/MEMResult.h" // MEMbbwwAlgoDilepton

// forward declarations
class MEMOutput_hh_bb2l;

class MEMHistManager_hh_bb2l
  : public HistManagerBase
{
public:
  MEMHistManager_hh_bb2l(const edm::ParameterSet & cfg);
  ~MEMHistManager_hh_bb2l() {}

  /// book and fill histograms
  void
  bookHistograms(TFileDirectory & dir) override;

  void
  fillHistograms(const MEMOutput_hh_bb2l * const memResult,
                 //const MEMOutput_hh_bb2l * const memResult_missingBJet,
                 double evtWeight);

  void
  fillHistograms(const MEMbbwwResultDilepton * const memResult,
                 double memCpuTime,
                 //const MEMbbwwResultDilepton * const memResult_missingBJet,
                 //double memCpuTime_missingBJet,
                 double evtWeight);

 private:
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
};

#endif
