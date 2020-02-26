#ifndef hhAnalysis_bbww_comp_metP4_B2G_18_008_h
#define hhAnalysis_bbww_comp_metP4_B2G_18_008_h

#include "tthAnalysis/HiggsToTauTau/interface/Particle.h" // Particle::LorentzVector

// compute four-vector of neutrino produced in H->WW*->jj lnu decay,
// using Higgs boson mass constraint, as described in Section 3.4.2 of AN-2018/058 (v4)
Particle::LorentzVector comp_metP4_B2G_18_008(const Particle::LorentzVector& visP4, double metPx, double metPy, double mH);

#endif
