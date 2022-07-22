from tthAnalysis.HiggsToTauTau.analysisSettings import systematics

class FakeRate_bbww_e_shape(object):
    br_low_pt  = [ "CMS_ttHl_FRe_shape_br_low_ptUp", "CMS_ttHl_FRe_shape_br_low_ptDown"   ]
    br_mid_pt  = [ "CMS_ttHl_FRe_shape_br_mid_ptUp", "CMS_ttHl_FRe_shape_br_mid_ptDown"   ]
    br_high_pt = [ "CMS_ttHl_FRe_shape_br_high_ptUp", "CMS_ttHl_FRe_shape_br_high_ptDown" ]
    ee_low_pt  = [ "CMS_ttHl_FRe_shape_ee_low_ptUp", "CMS_ttHl_FRe_shape_ee_low_ptDown"   ]
    ee_mid_pt  = [ "CMS_ttHl_FRe_shape_ee_mid_ptUp", "CMS_ttHl_FRe_shape_ee_mid_ptDown"   ]
    ee_high_pt = [ "CMS_ttHl_FRe_shape_ee_high_ptUp", "CMS_ttHl_FRe_shape_ee_high_ptDown" ]

    full = br_low_pt + br_mid_pt + br_high_pt + ee_low_pt + ee_mid_pt + ee_high_pt

class FakeRate_bbww_m_shape(object):
    br_low_pt  = [ "CMS_ttHl_FRm_shape_br_low_ptUp", "CMS_ttHl_FRm_shape_br_low_ptDown"   ]
    br_mid_pt  = [ "CMS_ttHl_FRm_shape_br_mid_ptUp", "CMS_ttHl_FRm_shape_br_mid_ptDown"   ]
    br_high_pt = [ "CMS_ttHl_FRm_shape_br_high_ptUp", "CMS_ttHl_FRm_shape_br_high_ptDown" ]
    ee_low_pt  = [ "CMS_ttHl_FRm_shape_ee_low_ptUp", "CMS_ttHl_FRm_shape_ee_low_ptDown"   ]
    ee_mid_pt  = [ "CMS_ttHl_FRm_shape_ee_mid_ptUp", "CMS_ttHl_FRm_shape_ee_mid_ptDown"   ]
    ee_high_pt = [ "CMS_ttHl_FRm_shape_ee_high_ptUp", "CMS_ttHl_FRm_shape_ee_high_ptDown" ]

    full = br_low_pt + br_mid_pt + br_high_pt + ee_low_pt + ee_mid_pt + ee_high_pt

class systematics_bbww(systematics):
  bbww_FR_shape = FakeRate_bbww_e_shape.full + FakeRate_bbww_m_shape.full
  tth_FR_shape = systematics.FRe_shape + systematics.FRm_shape
  an_full_hh_bbww = systematics.central + systematics.JES + systematics.JER + systematics.leptonIDSF + \
                    systematics.UnclusteredEn + systematics.btag + systematics.FRe_shape + systematics.FRm_shape + \
                    systematics.lhe + systematics.triggerSF + systematics.PU + systematics.DYMCNormScaleFactors + \
                    systematics.L1PreFiring + systematics.partonShower + systematics.ttbar + systematics.AK8 + \
                    systematics.pileupJetID + systematics.topPtReweighting + systematics.leptonIDSF_hh_recomp + \
                    systematics.mcClosure + systematics.ttbar + systematics.pdf + systematics.LHEVpt + \
                    systematics.subjetBtag # + systematics.pdf_mem
  an_opts_hh_bbww = [
    "central", "JES", "JER", "leptonIDSF", "UnclusteredEn", "btag", "FRe_shape", "FRm_shape", "lhe", "triggerSF", "PU",
    "DYMCNormScaleFactors", "L1PreFiring", "partonShower", "AK8", "pileupJetID", "topPtReweighting",
    "leptonIDSF_hh_recomp", systematics.mcClosure_str, "ttbar", "pdf", "LHEVpt", "subjetBtag", # "pdf_mem"
  ]
  an_internal_hh_bbww = systematics.central + systematics.leptonIDSF + systematics.btag + systematics.lhe + \
                        systematics.triggerSF + systematics.PU + systematics.L1PreFiring + systematics.FRe_shape + \
                        systematics.FRm_shape + systematics.DYMCNormScaleFactors + systematics.topPtReweighting + \
                        systematics.partonShower + systematics.leptonIDSF_hh_recomp + systematics.pileupJetID + \
                        systematics.pdf + systematics.pdf_mem + systematics.LHEVpt + systematics.subjetBtag

class systematics_bbww_dl(systematics_bbww):
  pass

class systematics_bbww_sl(systematics_bbww):
  systematics_bbww.an_full_hh_bbww += systematics.tauES
  systematics_bbww.an_opts_hh_bbww.extend([ "tauES" ])
