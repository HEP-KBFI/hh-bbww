#include "hhAnalysis/bbww/interface/MEMOutput_hh_bb2l.h" // MEMOutput_hh_bb2l

#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h" // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetBase.h" // RecoJetBase

MEMOutput_hh_bb2l::MEMOutput_hh_bb2l()
  : leadLepton_eta_(0.)
  , leadLepton_phi_(0.)
  , subleadLepton_eta_(0.)
  , subleadLepton_phi_(0.)
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
MEMOutput_hh_bb2l::fillInputs(const RecoLepton * leadLepton,
			      const RecoLepton * subleadLepton,
			      const RecoJetBase * bjet1,
			      const RecoJetBase * bjet2)
{
  leadLepton_eta_          = leadLepton -> eta();
  leadLepton_phi_          = leadLepton -> phi();
  subleadLepton_eta_       = subleadLepton -> eta();
  subleadLepton_phi_       = subleadLepton -> phi();
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
  if      ( bjet1_isReconstructed_ && bjet2_isReconstructed_ ) type_ = 0;
  else if ( bjet1_isReconstructed_ || bjet2_isReconstructed_ ) type_ = 1;
  else assert(0);
}

std::ostream& operator<<(std::ostream& stream,
                         const MEMOutput_hh_bb2l& memOutput)
{
  stream   << "<MEMOutput (hh_bb2l)>:\n"
              " "                << memOutput.eventInfo_          << "\n"
              " leading lepton:"
              " eta = "          << memOutput.leadLepton_eta_     << ","
              " phi = "          << memOutput.leadLepton_phi_     << "\n"
              " subleading lepton:"
              " eta = "          << memOutput.subleadLepton_eta_  << ","
              " phi = "          << memOutput.subleadLepton_phi_  << "\n"
              " b-jet #1:";
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
