from tthAnalysis.HiggsToTauTau.analysisSettings import systematics

class systematics_bbww(systematics):
  an_full_hh_bbww = systematics.central + systematics.JES + systematics.JER + systematics.leptonIDSF + \
                    systematics.UnclusteredEn + systematics.btag + systematics.FRe_shape + systematics.FRm_shape + \
                    systematics.lhe + systematics.triggerSF + systematics.PU + systematics.DYMCNormScaleFactors + \
                    systematics.L1PreFiring + systematics.partonShower + systematics.AK8 + \
                    systematics.pileupJetID + systematics.topPtReweighting + systematics.leptonIDSF_hh_recomp + \
                    systematics.mcClosure + systematics.ttbar + systematics.pdf
  an_opts_hh_bbww = [
    "central", "JES", "JER", "leptonIDSF", "UnclusteredEn", "btag", "FRe_shape", "FRm_shape", "lhe", "triggerSF", "PU",
    "DYMCNormScaleFactors", "L1PreFiring", "partonShower", "AK8", "pileupJetID", "topPtReweighting",
    "leptonIDSF_hh_recomp", systematics.mcClosure_str, "ttbar", "pdf",
  ]
  an_internal_hh_bbww = systematics.central + systematics.leptonIDSF + systematics.btag + systematics.lhe + \
                        systematics.triggerSF + systematics.PU + systematics.L1PreFiring + systematics.FRe_shape + \
                        systematics.FRm_shape + systematics.DYMCNormScaleFactors + systematics.topPtReweighting + \
                        systematics.partonShower + systematics.leptonIDSF_hh_recomp + systematics.pileupJetID + \
                        systematics.pdf + systematics.pdf_mem

class systematics_bbww_dl(systematics_bbww):
  pass

class systematics_bbww_sl(systematics_bbww):
  systematics_bbww.an_full_hh_bbww += systematics.tauES
  systematics_bbww.an_opts_hh_bbww.extend([ "tauES" ])
