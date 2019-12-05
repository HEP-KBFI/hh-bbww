#include "hhAnalysis/bbww/interface/MEMOutput_hh_bb1l.h" // MEMOutput_hh_bb1l

#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h" // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetBase.h" // RecoJetBase

MEMOutput_hh_bb1l::MEMOutput_hh_bb1l()
  : lepton_eta_(0.)
  , lepton_phi_(0.)
  , wjet1_eta_(0.)
  , wjet1_phi_(0.)
  , wjet1_isReconstructed_(false)
  , wjet2_eta_(0.)
  , wjet2_phi_(0.)
  , wjet2_isReconstructed_(false)
  , bjet1_eta_(0.)
  , bjet1_phi_(0.)
  , bjet1_isReconstructed_(false)
  , bjet2_eta_(0.)
  , bjet2_phi_(0.)
  , bjet2_isReconstructed_(false)
  , type_(-1)
  , weight_signal_(-1.)
  , weightErr_signal_(-1.)
  , weight_background_(-1.)
  , weightErr_background_(-1.)
  , LR_(-1.)
  , LRErr_(-1.)
  , Score_(-1.)
  , cpuTime_(-1.)
  , realTime_(-1.)
  , isValid_(0)
  , errorFlag_(0)
{}

void
MEMOutput_hh_bb1l::fillInputs(const RecoLepton * lepton,
                              const RecoJetBase * wjet1,
			      const RecoJetBase * wjet2,
			      const RecoJetBase * bjet1,
			      const RecoJetBase * bjet2)
{
  lepton_eta_              = lepton -> eta();
  lepton_phi_              = lepton -> phi();
  if ( wjet1 ) 
  {
    wjet1_eta_             = wjet1 -> eta();
    wjet1_phi_             = wjet1 -> phi();
    wjet1_isReconstructed_ = true;
  }
  if ( wjet2 ) 
  {    
    wjet2_eta_             = wjet2 -> eta();
    wjet2_phi_             = wjet2 -> phi();
    wjet2_isReconstructed_ = true;
  }
  if ( bjet1 ) 
  {
    bjet1_eta_             = bjet1 -> eta();
    bjet1_phi_             = bjet1 -> phi();
    bjet1_isReconstructed_ = true;
  }
  if ( bjet2 ) 
  {    
    bjet2_eta_             = bjet2 -> eta();
    bjet2_phi_             = bjet2 -> phi();
    bjet2_isReconstructed_ = true;
  }
  if      (  bjet1_isReconstructed_ && bjet2_isReconstructed_  &&  wjet1_isReconstructed_ && wjet2_isReconstructed_  ) type_ = 0;
  else if ( (bjet1_isReconstructed_ || bjet2_isReconstructed_) &&  wjet1_isReconstructed_ && wjet2_isReconstructed_  ) type_ = 1;
  else if (  bjet1_isReconstructed_ && bjet2_isReconstructed_  && (wjet1_isReconstructed_ || wjet2_isReconstructed_) ) type_ = 2;
  else if ( (bjet1_isReconstructed_ || bjet2_isReconstructed_) && (wjet1_isReconstructed_ || wjet2_isReconstructed_) ) type_ = 3;
  else assert(0);
}

std::ostream& operator<<(std::ostream& stream,
                         const MEMOutput_hh_bb1l& memOutput)
{
  stream   << "<MEMOutput (hh_bb1l)>:\n"
              " "                << memOutput.eventInfo_          << "\n"
              " lepton:"
              " eta = "          << memOutput.lepton_eta_     << ","
              " phi = "          << memOutput.lepton_phi_     << "\n";
  stream << " jet from W->jj #1:";
  if ( memOutput.wjet1_isReconstructed_ )
  {                    
    stream << " eta = "          << memOutput.wjet1_eta_          << ","
              " phi = "          << memOutput.wjet1_phi_          << "\n";
  } else {
    stream << " N/A \n";
  }
  stream   << " jet from W->jj #2:";
  if ( memOutput.wjet2_isReconstructed_ )
  {                    
    stream << " eta = "          << memOutput.wjet2_eta_          << ","
              " phi = "          << memOutput.wjet2_phi_          << "\n";
  } else {
    stream << " N/A \n";
  }
  stream << " b-jet #1:";
  if ( memOutput.bjet1_isReconstructed_ )
  {                    
    stream << " eta = "          << memOutput.bjet1_eta_          << ","
              " phi = "          << memOutput.bjet1_phi_          << "\n";
  } else {
    stream << " N/A \n";
  }
  stream   << " b-jet #2:";
  if ( memOutput.bjet2_isReconstructed_ )
  {                    
    stream << " eta = "          << memOutput.bjet2_eta_          << ","
              " phi = "          << memOutput.bjet2_phi_          << "\n";
  } else {
    stream << " N/A \n";
  }
  stream   << " type = "         << memOutput.type()              << "\n"
              " weights:\n"
              "  signal = "      << memOutput.weight_signal()     << "\n"
              "  background = "  << memOutput.weight_background() << "\n"
              " weights_Err:\n"
              "  signal_Err = "      << memOutput.weightErr_signal()     << "\n"
              "  background_Err = "  << memOutput.weightErr_background() << "\n"
              " LR = "           << memOutput.LR()                << "\n"
              " LRErr = "                 << memOutput.LRErr()                << "\n"
              " Score = "                 << memOutput.Score()                << "\n"
              " isValid = "      << memOutput.isValid()           << "\n"
              " errorFlag = "    << memOutput.errorFlag()         << "\n"
              " cpuTime = "      << memOutput.cpuTime()           << "\n"
              " realTime = "     << memOutput.realTime()          << "\n";
  return stream;
}
