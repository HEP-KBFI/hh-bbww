#include "hhAnalysis/bbww/interface/HMEOutput_hh_bb2l.h" // MEMOutput_hh_bb2l

#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h" // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetBase.h" // RecoJetBase

HMEOutput_hh_bb2l::HMEOutput_hh_bb2l()
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
  , m_HH_hme_(-1.)
  , cpuTime_(-1.)
  , realTime_(-1.)
  , isValid_(0)
  , errorFlag_(0)
{}

void
HMEOutput_hh_bb2l::fillInputs(const RecoLepton * leadLepton,
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
                         const HMEOutput_hh_bb2l& hmeOutput)
{
  stream   << "<HMEOutput (hh_bb2l)>:\n"
              " "                << hmeOutput.eventInfo_          << "\n"
              " leading lepton:"
              " eta = "          << hmeOutput.leadLepton_eta_     << ","
              " phi = "          << hmeOutput.leadLepton_phi_     << "\n"
              " subleading lepton:"
              " eta = "          << hmeOutput.subleadLepton_eta_  << ","
              " phi = "          << hmeOutput.subleadLepton_phi_  << "\n"
              " b-jet #1:";
  if ( hmeOutput.bjet1_isReconstructed_ )
  {                    
    stream << " eta = "          << hmeOutput.bjet1_eta_          << ","
              " phi = "          << hmeOutput.bjet1_phi_          << "\n";
  } else {
    stream << " N/A \n";
  }
  stream   << " b-jet #2:";
  if ( hmeOutput.bjet2_isReconstructed_ )
  {                    
    stream << " eta = "          << hmeOutput.bjet2_eta_          << ","
              " phi = "          << hmeOutput.bjet2_phi_          << "\n";
  } else {
    stream << " N/A \n";
  }
  stream   << " type = "         << hmeOutput.type()              << "\n"
              " m_HH_hme:\n"
              "  signal = "      << hmeOutput.m_HH_hme()     << "\n"
              " isValid = "      << hmeOutput.isValid()           << "\n"
              " errorFlag = "    << hmeOutput.errorFlag()         << "\n"
              " cpuTime = "      << hmeOutput.cpuTime()           << "\n"
              " realTime = "     << hmeOutput.realTime()          << "\n";
  return stream;
}
