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

process.analyze_hh_bb1l = cms.PSet(
    treeName = cms.string('Events'),

    process = cms.string(''),
    histogramDir = cms.string(''),
    era = cms.string(''),

    triggers_1e = cms.vstring(),
    use_triggers_1e = cms.bool(True),
    triggers_1mu = cms.vstring(),
    use_triggers_1mu = cms.bool(True),

    apply_offline_e_trigger_cuts_1e = cms.bool(True),
    apply_offline_e_trigger_cuts_1mu = cms.bool(True),

    electronSelection = cms.string(''),
    muonSelection = cms.string(''),
    apply_leptonGenMatching = cms.bool(True),

    apply_hadTauVeto = cms.bool(True),
    hadTauSelection_veto = cms.string('deepVSjMedium'),
    
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
    apply_topPtReweighting = cms.string(''),
    apply_l1PreFireWeight = cms.bool(True),
    apply_hlt_filter = cms.bool(False),
    apply_met_filters = cms.bool(True),
    cfgMEtFilter = cms.PSet(),
    triggerWhiteList = cms.PSet(),

    fillGenEvtHistograms = cms.bool(False),
    cfgEvtYieldHistManager = cms.PSet(),

    branchName_electrons = cms.string('Electron'),
    branchName_muons = cms.string('Muon'),
    branchName_hadTaus = cms.string('Tau'),
    branchName_jets_ak4 = cms.string('Jet'),
    branchName_jets_ak8 = cms.string('FatJet'),
    branchName_subjets_ak8 = cms.string('SubJet'),
    branchName_jets_ak8LS = cms.string('FatJetAK8LSLoose'),
    branchName_subjets_ak8LS = cms.string('SubJetAK8LSLoose'),
    branchName_met = cms.string('MET'),

    #branchName_memOutput = cms.string('memObjects_hh_bb1l_lepTight'),
    #branchName_memOutput_missingBJet = cms.string('memObjects_hh_bb1l_lepTight_missingBJet'),
    #branchName_memOutput_missingHadWJet = cms.string('memObjects_hh_bb1l_lepTight_missingHadWJet'),
    branchName_memOutput = cms.string(''),
    branchName_memOutput_missingBJet = cms.string(''),
    branchName_memOutput_missingHadWJet = cms.string(''),

    branchName_muonGenMatch = cms.string('MuonGenMatch'),
    branchName_electronGenMatch = cms.string('ElectronGenMatch'),
    branchName_hadTauGenMatch = cms.string('TauGenMatch'),
    branchName_jetGenMatch = cms.string('JetGenMatch'),

    branchName_genLeptons = cms.string('GenLep'),
    branchName_genHadTaus = cms.string('GenVisTau'),
    branchName_genPhotons = cms.string('GenPhoton'),
    branchName_genJets = cms.string('GenJet'),

    redoGenMatching = cms.bool(False),
    genMatchingByIndex = cms.bool(True),
    jetCleaningByIndex = cms.bool(True),

    branchName_genBJets = cms.string('GenBQuarkFromTop'),
    branchName_genParticlesFromHiggs = cms.string('GenHiggsDaughters'),
    branchName_genWBosons = cms.string('GenVbosons'),
    branchName_genWJets = cms.string('GenWZQuark'),

    branchName_genLeptonsFromTop = cms.string('GenLepFromTop'),
    branchName_genNeutrinosFromTop = cms.string('GenNuFromTop'),
    branchName_genBJetsFromTop = cms.string('GenBQuarkFromTop'),
    branchName_genWJetsFromTop = cms.string('GenQuarkFromTop'),

    selEventsFileName_input = cms.string(''),
    selEventsFileName_output = cms.string(''),
    selectBDT = cms.bool(False),

    gen_mHH = cms.vdouble(250,260,270,280,300,350,400,450,500,550,600,650,700,750,800,850,900,1000), ## Set the signal mass range used in the BDT .pkl/.xml/.pb files
    mvaInfo_res = cms.PSet(
        BDT_xml_FileName_even_spin2 = cms.string('hhAnalysis/multilepton/data/1l_3tau_odd_half_model_spin2.xml'), ## "BDT .xml -> Odd train:Even test" to be used for even evt no.
        BDT_xml_FileName_odd_spin2 = cms.string('hhAnalysis/multilepton/data/1l_3tau_even_half_model_spin2.xml'), ## "BDT .xml -> Even train:Odd test" to be used for odd evt no.
        fitFunctionFileName_spin2 = cms.string('hhAnalysis/multilepton/data/1l_3tau_TProfile_signal_fit_func_spin2.root'),  ## File contaning the fitted TF1s
        inputVars_spin2 = cms.vstring(
            'diHiggsVisMass', 'diHiggsMass', 'dr_lep_tau1', 'dr_lep_tau2',
            'dr_lep_tau3', 'dr_tau1_tau2', 'dr_tau1_tau3', 'dr_tau2_tau3',
            'mT_lep', 'gen_mHH'
        ),
        BDT_xml_FileName_even_spin0 = cms.string('hhAnalysis/multilepton/data/1l_3tau_odd_half_model_spin0.xml'),
        BDT_xml_FileName_odd_spin0 = cms.string('hhAnalysis/multilepton/data/1l_3tau_even_half_model_spin0.xml'),
        fitFunctionFileName_spin0 = cms.string('hhAnalysis/multilepton/data/1l_3tau_TProfile_signal_fit_func_spin0.root'),
        inputVars_spin0 = cms.vstring(
            'diHiggsVisMass', 'diHiggsMass', 'dr_lep_tau1', 'dr_lep_tau2',
            'dr_lep_tau3', 'dr_tau1_tau2', 'dr_tau1_tau3', 'dr_tau2_tau3',
            'mT_lep', 'gen_mHH'
        ),
    ),
    nonRes_BMs = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
    mvaInfo_nonres = cms.PSet(
        BDT_xml_FileName_even_nonres = cms.string('hhAnalysis/multilepton/data/1l_3tau_odd_model_nonres.xml'),
        BDT_xml_FileName_odd_nonres = cms.string('hhAnalysis/multilepton/data/1l_3tau_even_model_nonres.xml'),
        inputVars_nonres = cms.vstring(
            'lep_pt', 'lep_phi', 'tau1_pt', 'tau2_pt', 'tau3_pt', 'met', 'diHiggsVisMass',
            'diHiggsMass', 'dr_lep_tau3', 'dr_tau1_tau2', 'dr_tau1_tau3', 'dr_tau2_tau3',
            'm_lep_tau1', 'pt_HH_recoil', 'mT_lep',
            'SM', 'BM1', 'BM2', 'BM3', 'BM4', 'BM5', 'BM6', 'BM7', 'BM8', 'BM9', 'BM10', 'BM11', 'BM12'
        ), ## No Need to add BM indices they will be added for the  non-reso case on the fly
    ),

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
