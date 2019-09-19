#ifndef hhAnalysis_bbww_HMEOutput_hh_bb2l_h
#define hhAnalysis_bbww_HMEOutput_hh_bb2l_h

#include "tthAnalysis/HiggsToTauTau/interface/EventInfo.h" // EventInfo

#include <Rtypes.h> // Int_t, Float_t

#include <iostream>

// forward declarations
class RecoLepton;
class RecoJetBase;

class HMEOutput_hh_bb2l
{
public:
  HMEOutput_hh_bb2l();
  ~HMEOutput_hh_bb2l() {}

  /**
   * @brief Funtions to access data-members
   * @return Values of data-members
   */
  inline Int_t type()                const { return type_; }
  inline Float_t m_HH_hme()     const { return m_HH_hme_; }
  inline Float_t cpuTime()           const { return cpuTime_; }
  inline Float_t realTime()          const { return realTime_; }
  inline Int_t isValid()             const { return isValid_; }
  inline Int_t errorFlag()           const { return errorFlag_; }

  inline bool is_initialized() const { return eventInfo_.is_initialized(); }

  friend class HMEInterface_hh_bb2l;
  friend class HMEOutputReader_hh_bb2l;

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
  Float_t m_HH_hme_; // HH->bbWW signal
  Float_t cpuTime_;
  Float_t realTime_;
  Int_t isValid_;
  Int_t errorFlag_;
};

std::ostream& operator<<(std::ostream& stream,
                         const HMEOutput_hh_bb2l& hmeOutput);

#endif // MEMOutput_hh_bb2l_h
