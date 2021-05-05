import FWCore.ParameterSet.Config as cms
import os

from tthAnalysis.HiggsToTauTau.configs.recommendedMEtFilters_cfi import *
from tthAnalysis.HiggsToTauTau.configs.EvtYieldHistManager_cfi import *
from tthAnalysis.HiggsToTauTau.configs.hhWeight_cfi import hhWeight
from tthAnalysis.HiggsToTauTau.analysisSettings import *

process = cms.PSet()

process.fwliteInput = cms.PSet(
    fileNames = cms.vstring(),
    maxEvents = cms.int32(-1),
    outputEvery = cms.uint32(100000)
)

process.fwliteOutput = cms.PSet(
    fileName = cms.string('')
)

process.analyze_hh_bb2l = cms.PSet(
    treeName = cms.string('Events'),

    process = cms.string(''),
    histogramDir = cms.string(''),
    era = cms.string(''),

    triggers_1e = cms.vstring(),
    use_triggers_1e = cms.bool(True),
    triggers_2e = cms.vstring(),
    use_triggers_2e = cms.bool(True),
    triggers_1mu = cms.vstring(),
    use_triggers_1mu = cms.bool(True),
    triggers_2mu = cms.vstring(),
    use_triggers_2mu = cms.bool(True),
    triggers_1e1mu = cms.vstring(),
    use_triggers_1e1mu = cms.bool(True),

    apply_offline_e_trigger_cuts_1e = cms.bool(True),
    apply_offline_e_trigger_cuts_2e = cms.bool(True),
    apply_offline_e_trigger_cuts_1mu = cms.bool(True),
    apply_offline_e_trigger_cuts_2mu = cms.bool(True),
    apply_offline_e_trigger_cuts_1e1mu = cms.bool(True),

    electronSelection = cms.string(''),
    muonSelection = cms.string(''),
    apply_leptonGenMatching = cms.bool(True),
    leptonChargeSelection = cms.string(''),

    dyBgr_option = cms.string('disabled'),

    apply_pileupJetID = cms.string(''),

    applyFakeRateWeights = cms.string(""),
    leptonFakeRateWeight = cms.PSet(
        inputFileName = cms.string(""),
        histogramName_e = cms.string(""),
        histogramName_mu = cms.string(""),
        era = cms.string(""),
        applyNonClosureCorrection = cms.bool(True),
    ),

    evtCategories = cms.vstring(), # CV: "inclusive" event category is added automatically

    isMC = cms.bool(True),
    central_or_shift = cms.string(''),
    lumiScale = cms.VPSet(),
    ref_genWeight = cms.double(0.),
    apply_genWeight = cms.bool(True),
    apply_DYMCReweighting = cms.bool(False),
    apply_DYMCNormScaleFactors = cms.bool(False),
    apply_topPtReweighting = cms.string(''),
    apply_l1PreFireWeight = cms.bool(True),
    apply_hlt_filter = cms.bool(False),
    apply_met_filters = cms.bool(True),
    run_hme = cms.bool(False),
    cfgMEtFilter = cms.PSet(),
    triggerWhiteList = cms.PSet(),
    apply_genPhotonFilter = cms.string("disabled"),
    
    fillGenEvtHistograms = cms.bool(False),
    cfgEvtYieldHistManager = cms.PSet(),

    branchName_electrons = cms.string('Electron'),
    branchName_muons = cms.string('Muon'),
    branchName_jets_ak4 = cms.string('Jet'),
    branchName_jets_ak8 = cms.string('FatJet'),
    branchName_subjets_ak8 = cms.string('SubJet'),
    branchName_met = cms.string('MET'),

    branchName_genLeptons = cms.string('GenLep'),
    branchName_genHadTaus = cms.string('GenVisTau'),
    branchName_genPhotons = cms.string('GenPhoton'),
    branchName_genProxyPhotons = cms.string('GenPhotonCandidate'),
    branchName_genFromHardProcess = cms.string('GenIsHardProcess'),
    branchName_genJets = cms.string('GenJet'),
    branchName_genHiggses = cms.string('GenHiggs'),

    branchName_muonGenMatch = cms.string('MuonGenMatch'),
    branchName_electronGenMatch = cms.string('ElectronGenMatch'),
    branchName_hadTauGenMatch = cms.string('TauGenMatch'),
    branchName_jetGenMatch = cms.string('JetGenMatch'),
    branchName_vertex = cms.string('PV'),

    redoGenMatching = cms.bool(False),
    genMatchingByIndex = cms.bool(True),
    jetCleaningByIndex = cms.bool(True),

    branchName_genBJets = cms.string('GenBQuarkFromTop'),
    branchName_genWBosons = cms.string('GenVbosons'),

    branchName_memOutput = cms.string(''),
    branchName_hmeOutput = cms.string(''),

    selEventsFileName_input = cms.string(''),
    selEventsFileName_output = cms.string(''),
    selectBDT = cms.bool(False),

    fillHistograms_BDT = cms.bool(True),
    BDT = cms.PSet(
        resonant_spin2_resolved = cms.PSet(
            xmlFileName_even = cms.string(''), ## "BDT .xml -> Odd train:Even test" to be used for even evt no.
            xmlFileName_odd = cms.string(''), ## "BDT .xml -> Even train:Odd test" to be used for odd evt no.
            inputVariables = cms.vstring(
                '', '', '', '', '',
                '', '', '', '', '',
                '', '', '', '', ''
            )
        ),
        resonant_spin2_boosted = cms.PSet(
            xmlFileName_even = cms.string(''), ## "BDT .xml -> Odd train:Even test" to be used for even evt no.
            xmlFileName_odd = cms.string(''), ## "BDT .xml -> Even train:Odd test" to be used for odd evt no.
            inputVariables = cms.vstring(
                '', '', '', '', '',
                '', '', '', '', '',
                '', '', '', '', ''
            )
        ),
        resonant_spin0_resolved = cms.PSet(
            xmlFileName_even = cms.string(''), ## "BDT .xml -> Odd train:Even test" to be used for even evt no.
            xmlFileName_odd = cms.string(''), ## "BDT .xml -> Even train:Odd test" to be used for odd evt no.
            inputVariables = cms.vstring(
                '', '', '', '', '',
                '', '', '', '', '',
                '', '', '', '', ''
            )
        ),
        resonant_spin0_boosted = cms.PSet(
            xmlFileName_even = cms.string(''), ## "BDT .xml -> Odd train:Even test" to be used for even evt no.
            xmlFileName_odd = cms.string(''), ## "BDT .xml -> Even train:Odd test" to be used for odd evt no.
            inputVariables = cms.vstring(
                '', '', '', '', '',
                '', '', '', '', '',
                '', '', '', '', ''
            )
        ),
        nonresonant_resolved = cms.PSet(
            xmlFileName_even = cms.string('hhAnalysis/bbww/data/BDT_hh_bb2l/bb2l_bdt_odd_half_model_resolved_nonres_BM_era.xml'), ## "BDT .xml -> Odd train:Even test" to be used for even evt no.
            xmlFileName_odd = cms.string('hhAnalysis/bbww/data/BDT_hh_bb2l/bb2l_bdt_even_half_model_resolved_nonres_BM_era.xml'), ## "BDT .xml -> Even train:Odd test" to be used for odd evt no.
            inputVariables = cms.vstring(
                'm_Hbb_regCorr', 'm_ll', 'Smin_Hww', 'mbb_loose', 'm_HHvis',
                'dR_ll', 'logTopness_publishedChi2', 'mT2_top_2particle', 'mht', 'logTopness_fixedChi2',
                'mbb_medium', 'pT_HH', 'logHiggsness_fixedChi2', 'pT_Hbb', 'pT_Hww',
                'lep2_pt', 'dR_Hbb', 'dPhi_Hbb', 'pT_ll', 'met_pt_proj'
            )
        ),
        nonresonant_boosted = cms.PSet(
            xmlFileName_even = cms.string('hhAnalysis/bbww/data/BDT_hh_bb2l/bb2l_bdt_odd_half_model_boosted_nonres_BM_era.xml'), ## "BDT .xml -> Odd train:Even test" to be used for even evt no.
            xmlFileName_odd = cms.string('hhAnalysis/bbww/data/BDT_hh_bb2l/bb2l_bdt_odd_half_model_boosted_nonres_BM_era.xml'), ## "BDT .xml -> Even train:Odd test" to be used for odd evt no.
            inputVariables = cms.vstring(
                'm_ll', 'm_Hbb', 'mbb_loose', 'dR_ll', 'mbb_medium',
                'Smin_Hww', 'mindr_lep1_jet', 'max_dPhi_lepMEt', 'dR_Hbb', 'tau21_Hbb',
                'STMET', 'pT_HH', 'bjet2_pt', 'avg_dr_jet_central', 'lep1_e',
                'mht', 'm_HHvis', 'pT_ll', 'dPhi_HH', 'logHiggsness_fixedChi2', 'dPhi_HHvis',
                'lep2_pt', 'eta_HHvis', 'dR_b1lep2', 'logTopness_fixedChi2'
            )
        )
    ),
    fillHistograms_LBN = cms.bool(False),
    LBN = cms.PSet(
        resonant_spin2_resolved = cms.PSet(
            pbFileName_even = cms.string(''), ## "LBN .pb -> Odd train:Even test" to be used for even evt no.
            pbFileName_odd = cms.string(''), ## "LBN .pb -> Even train:Odd test" to be used for odd evt no.
            ll_inputVariables = cms.vstring(
                'bjet1', 'bjet2', 'lep1', 'lep2'
            ),
            hl_inputVariables = cms.vstring(
                '', '', '', '', '',
                '', '', '', '', '',
                '', '', '', '', ''
            ),
            classes = cms.vstring('HH', 'TT', 'W', 'DY', 'ST', 'Other')
        ),
        resonant_spin2_boosted = cms.PSet(
            pbFileName_even = cms.string(''), ## "LBN .pb -> Odd train:Even test" to be used for even evt no.
            pbFileName_odd = cms.string(''), ## "LBN .pb -> Even train:Odd test" to be used for odd evt no.
            ll_inputVariables = cms.vstring(
                'bjet1', 'bjet2', 'lep1', 'lep2'
            ),
            hl_inputVariables = cms.vstring(
                '', '', '', '', '',
                '', '', '', '', '',
                '', '', '', '', ''
            ),
            classes = cms.vstring('HH', 'TT', 'W', 'DY', 'ST', 'Other')
        ),
        resonant_spin0_resolved = cms.PSet(
            pbFileName_even = cms.string(''), ## "LBN .pb -> Odd train:Even test" to be used for even evt no.
            pbFileName_odd = cms.string(''), ## "LBN .pb -> Even train:Odd test" to be used for odd evt no.
            ll_inputVariables = cms.vstring(
                'bjet1', 'bjet2', 'lep1', 'lep2'
            ),
            hl_inputVariables = cms.vstring(
                '', '', '', '', '',
                '', '', '', '', '',
                '', '', '', '', ''
            ),
            classes = cms.vstring('HH', 'TT', 'W', 'DY', 'ST', 'Other')
        ),
        resonant_spin0_boosted = cms.PSet(
            pbFileName_even = cms.string(''), ## "LBN .pb -> Odd train:Even test" to be used for even evt no.
            pbFileName_odd = cms.string(''), ## "LBN .pb -> Even train:Odd test" to be used for odd evt no.
            ll_inputVariables = cms.vstring(
                'bjet1', 'bjet2', 'lep1', 'lep2'
            ),
            hl_inputVariables = cms.vstring(
                '', '', '', '', '',
                '', '', '', '', '',
                '', '', '', '', ''
            ),
            classes = cms.vstring('HH', 'TT', 'W', 'DY', 'ST', 'Other')
        ),
        nonresonant_resolved = cms.PSet(
            pbFileName_even = cms.string('hhAnalysis/bbww/data/BDT_hh_bb2l/multiclass_DNN_wlbn_for_bb2l_resolved_odd_data_nonres_X_era.pb'), ## "LBN .pb -> Odd train:Even test" to be used for even evt no.
            pbFileName_odd = cms.string('hhAnalysis/bbww/data/BDT_hh_bb2l/multiclass_DNN_wlbn_for_bb2l_resolved_even_data_nonres_X_era.pb'), ## "LBN .pb -> Even train:Odd test" to be used for odd evt no.
            ll_inputVariables = cms.vstring(
                'bjet1', 'bjet2', 'lep1', 'lep2'
            ),
            hl_inputVariables = cms.vstring(
                'm_Hbb_regCorr', 'Smin_Hww', 'm_HHvis', 'dR_ll',\
                'logTopness_publishedChi2', 'mT2_top_2particle',\
                'mht', 'logTopness_fixedChi2', 'pT_HH', 'logHiggsness_fixedChi2',\
                'pT_Hbb', 'pT_Hww', 'lep2_pt', 'dR_Hbb', 'pT_ll',\
                'met_pt_proj', 'mjj_highestpt', 'mjj_closeToH', 'HT'
            ),
            classes = cms.vstring('HH', 'TT', 'ST', 'Other', 'DY')
        ),
        nonresonant_boosted = cms.PSet(
            pbFileName_even = cms.string('hhAnalysis/bbww/data/BDT_hh_bb2l/multiclass_DNN_wlbn_for_bb2l_boosted_odd_data_nonres_X_era.pb'), ## "LBN .pb -> Odd train:Even test" to be used for even evt no.
            pbFileName_odd = cms.string('hhAnalysis/bbww/data/BDT_hh_bb2l/multiclass_DNN_wlbn_for_bb2l_boosted_even_data_nonres_X_era.pb'), ## "LBN .pb -> Even train:Odd test" to be used for odd evt no.
            ll_inputVariables = cms.vstring(
                'bjet1', 'bjet2', 'lep1', 'lep2'
            ),
            hl_inputVariables = cms.vstring(
                'm_ll', 'm_Hbb', 'dR_ll', 'Smin_Hww', 'mindr_lep1_jet',\
                'max_dPhi_lepMEt', 'dR_Hbb', 'tau21_Hbb', 'STMET',\
                'pT_HH', 'bjet2_pt', 'avg_dr_jet_central', 'mht',\
                'pT_ll', 'dPhi_HH', 'logHiggsness_fixedChi2', 'dPhi_HHvis',\
                'lep2_pt', 'eta_HHvis', 'dR_b1lep2', 'logTopness_fixedChi2', 'HT'
            ),
            classes = cms.vstring('HH', 'TT', 'ST', 'Other', 'DY')
        )
    ),
    gen_mHH = cms.vdouble(250,260,270,280,300,350,400,450,500,550,600,650,700),#750,800,850,900,1000), ## Set the signal mass range used in the BDT .pkl/.xml/.pb files
    nonRes_BMs = cms.vstring(),

    fillHistograms_nonresonant = cms.bool(True),
    fillHistograms_resonant_spin0 = cms.bool(False),
    fillHistograms_resonant_spin2 = cms.bool(False),

    syncNtuple = cms.PSet(
        tree = cms.string(''),
        output = cms.string(''),
        requireGenMatching = cms.bool(False),
    ),
    useNonNominal = cms.bool(False),
    isDEBUG = cms.bool(False),
    hasLHE = cms.bool(True),
    hasPS = cms.bool(False),
    apply_LHE_nom = cms.bool(False),
    useObjectMultiplicity = cms.bool(False),

    evtWeight = cms.PSet(
        apply = cms.bool(False),
        histogramFile = cms.string(''),
        histogramName = cms.string(''),
        branchNameXaxis = cms.string(''),
        branchNameYaxis = cms.string(''),
        branchTypeXaxis = cms.string(''),
        branchTypeYaxis = cms.string(''),
    ),
    tHweights = cms.VPSet(),
    hhWeight_cfg = hhWeight,
)

process.analyze_hh_bb2l.BDT.resonant_spin2_resolved = process.analyze_hh_bb2l.BDT.nonresonant_resolved
process.analyze_hh_bb2l.BDT.resonant_spin2_boosted  = process.analyze_hh_bb2l.BDT.nonresonant_boosted
process.analyze_hh_bb2l.BDT.resonant_spin0_resolved = process.analyze_hh_bb2l.BDT.nonresonant_resolved
process.analyze_hh_bb2l.BDT.resonant_spin0_boosted  = process.analyze_hh_bb2l.BDT.nonresonant_boosted
process.analyze_hh_bb2l.LBN.resonant_spin2_resolved = process.analyze_hh_bb2l.LBN.nonresonant_resolved
process.analyze_hh_bb2l.LBN.resonant_spin2_boosted  = process.analyze_hh_bb2l.LBN.nonresonant_boosted
process.analyze_hh_bb2l.LBN.resonant_spin0_resolved = process.analyze_hh_bb2l.LBN.nonresonant_resolved
process.analyze_hh_bb2l.LBN.resonant_spin0_boosted  = process.analyze_hh_bb2l.LBN.nonresonant_boosted
