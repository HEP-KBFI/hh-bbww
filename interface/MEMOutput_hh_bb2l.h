#ifndef hhAnalysis_bbww_MEMOutput_hh_bb2l_h
#define hhAnalysis_bbww_MEMOutput_hh_bb2l_h

#include "tthAnalysis/HiggsToTauTau/interface/EventInfo.h" // EventInfo

#include <Rtypes.h> // Int_t, Float_t

#include <iostream>

// forward declarations
class RecoLepton;
class RecoJetBase;

class MEMOutput_hh_bb2l
{
public:
  MEMOutput_hh_bb2l();
  ~MEMOutput_hh_bb2l() {}

  /**
   * @brief Funtions to access data-members
   * @return Values of data-members
   */
  inline Int_t type()                   const { return type_; }
  inline Float_t weight_signal()        const { return weight_signal_; }
  inline Float_t weightErr_signal()     const { return weightErr_signal_; }
  inline Float_t weight_background()    const { return weight_background_; }
  inline Float_t weightErr_background() const { return weightErr_background_; }
  inline Float_t LR()                   const { return LR_; }
  inline Float_t LRErr()                const { return LRErr_; }
  inline Float_t Score()                const { return Score_; }
  inline Float_t cpuTime()              const { return cpuTime_; }
  inline Float_t realTime()             const { return realTime_; }
  inline Int_t isValid()                const { return isValid_; }
  inline Int_t errorFlag()              const { return errorFlag_; }

  inline bool is_initialized() const { return eventInfo_.is_initialized(); }

  friend class MEMInterface_hh_bb2l;
  friend class MEMOutputReader_hh_bb2l;
  friend class EvtHistManager_hh_bb2l;

  void
  fillInputs(const RecoLepton * leadLepton,
             const RecoLepton * subleadLepton,
             const RecoJetBase * bjet1,
	     const RecoJetBase * bjet2);

  EventInfo eventInfo_;
  Float_t leadLepton_eta_;
  Float_t leadLepton_phi_;
  Float_t subleadLepton_eta_;
  Float_t subleadLepton_phi_;
  Float_t bjet1_eta_;
  Float_t bjet1_phi_;
  bool bjet1_isReconstructed_;
  Float_t bjet2_eta_;
  Float_t bjet2_phi_;
  bool bjet2_isReconstructed_;
protected:
  Int_t type_; // either 0 (fully reconstructed H->bb decay) or 1 (one b-jet from H->bb decay not reconstructed)
  Float_t weight_signal_; // HH->bbWW signal
  Float_t weightErr_signal_; // HH->bbWW signal
  Float_t weight_background_; // tt+jets background (dilepton)
  Float_t weightErr_background_; // tt+jets background (dilepton)
  Float_t LR_;
  Float_t LRErr_;
  Float_t Score_;
  Float_t cpuTime_;
  Float_t realTime_;
  Int_t isValid_;
  Int_t errorFlag_;
};

std::ostream& operator<<(std::ostream& stream,
                         const MEMOutput_hh_bb2l& memOutput);

#endif // MEMOutput_hh_bb2l_h
