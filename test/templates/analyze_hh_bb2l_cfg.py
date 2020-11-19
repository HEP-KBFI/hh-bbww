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
    run_hme           = cms.bool(False),
    cfgMEtFilter = cms.PSet(),
    triggerWhiteList = cms.PSet(),

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
    branchName_genJets = cms.string('GenJet'),
    branchName_genHiggses = cms.string('GenHiggs'),

    branchName_muonGenMatch = cms.string('MuonGenMatch'),
    branchName_electronGenMatch = cms.string('ElectronGenMatch'),
    branchName_hadTauGenMatch = cms.string('TauGenMatch'),
    branchName_jetGenMatch = cms.string('JetGenMatch'),

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

    fillHistograms_BDT = cms.bool(False),
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
            xmlFileName_even = cms.string(''), ## "BDT .xml -> Odd train:Even test" to be used for even evt no.
            xmlFileName_odd = cms.string(''), ## "BDT .xml -> Even train:Odd test" to be used for odd evt no.
            inputVariables = cms.vstring(
                '', '', '', '', '',
                '', '', '', '', '',
                '', '', '', '', ''
            )
        ),
        nonresonant_boosted = cms.PSet(
            xmlFileName_even = cms.string(''), ## "BDT .xml -> Odd train:Even test" to be used for even evt no.
            xmlFileName_odd = cms.string(''), ## "BDT .xml -> Even train:Odd test" to be used for odd evt no.
            inputVariables = cms.vstring(
                '', '', '', '', '',
                '', '', '', '', '',
                '', '', '', '', ''
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
        nonresonant_boosted = cms.PSet(
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
        )
    ),
    gen_mHH = cms.vdouble(250,260,270,280,300,350,400,450,500,550,600,650,700,750,800,850,900,1000), ## Set the signal mass range used in the BDT .pkl/.xml/.pb files
    nonRes_BMs = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),

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
