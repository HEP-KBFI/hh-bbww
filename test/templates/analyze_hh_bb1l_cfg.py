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
    apply_genPhotonFilter = cms.string("disabled"),

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
    branchName_vertex = cms.string('PV'),

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
    branchName_genProxyPhotons = cms.string('GenPhotonCandidate'),
    branchName_genFromHardProcess = cms.string('GenIsHardProcess'),
    branchName_genTauFromV = cms.string('GenTauFromV'),
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
    usejpa = cms.bool(False),
    hhSignalScaleFactor = cms.double(0.),

    fillHistograms_BDT = cms.bool(True),
    BDT = cms.PSet(
        resonant_spin2_resolved = cms.PSet(

        ),
        resonant_spin2_boosted = cms.PSet(

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
            xmlFileName_even = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_bdt_odd_half_model_resolved_nonres_X_era.xml'), ## "BDT .xml -> Odd train:Even test" to be used for even evt no.
            xmlFileName_odd = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_bdt_even_half_model_resolved_nonres_X_era.xml'), ## "BDT .xml -> Even train:Odd test" to be used for odd evt no.
            inputVariables = cms.vstring(
            'dR_b1lep', 'mindr_lep1_jet', 'm_Hbb_regCorr', 'bjet1_btagCSV',
            'bjet1_pt', 'jpaScore', 'mT_W', 'dR_b2lep', 'lep_pt',
            'met', 'mht', 'm_HHvis', 'pT_HH',
            'wjet1_pt', 'mT_top_2particle', 'pT_Hbb', 'mbb_medium',
            'avg_dr_jet_central', 'mbb_loose', 'dR_Hbb', 'leadFwdJet_pt',
            'lep_e', "Smin_Hww", "dR_HH", "dPhi_HHvis",
            'bjet1_e', 'wjet2_pt'
            )
        ),
        nonresonant_boosted = cms.PSet(
            xmlFileName_even = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_bdt_odd_half_model_boosted_nonres_X_era.xml'), ## "BDT .xml -> Odd train:Even test" to be used for even evt no.
            xmlFileName_odd = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_bdt_even_half_model_boosted_nonres_X_era.xml'), ## "BDT .xml -> Even train:Odd test" to be used for odd evt no.
            inputVariables = cms.vstring(
                'mindr_lep1_jet', 'm_Hbb', 'mbb_medium',
                'bjet2_btagCSV', 'tau21_Hbb', 'mht', 'mbb_loose',
                'jpaScore', 'bjet1_btagCSV', 'met', 'lep_pt', 'dR_b1lep',
                'pT_Hbb', 'pT_HH', 'leadFwdJet_pt', 'avg_dr_jet_central', 'dPhi_HHvis',
                'wjet1_pt', 'mT_W', 'mT_top_2particle', 'dR_Hbb',
                'lep_e', 'mll_loose', 'bjet2_pt',
                'Smin_HH', 'lep_eta', 'Smin_Hww'
            )
        )
    ),
    fillHistograms_LBN = cms.bool(True),
    LBN = cms.PSet(
        resonant_spin2_resolved = cms.PSet(
            pbFileName_even = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/multiclass_DNN_wlbn_for_bb1l_resolved_odd_data_res_X_era.pb'), ## "LBN .pb -> Odd train:Even test" to be used for even evt no.
            pbFileName_odd = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/multiclass_DNN_wlbn_for_bb1l_resolved_even_data_res_X_era.pb'), ## "LBN .pb -> Even train:Odd test" to be used for odd evt no.
            ll_inputVariables = cms.vstring(
                'bjet1', 'bjet2', 'wjet1', 'wjet2', 'lep'
            ),
            hl_inputVariables = cms.vstring(
                'numJets', 'bjet1_btagCSV', 'pT_Hbb', 'mindr_lep1_jet',
                'HT', 'lepPairCharge_loose', 'mT_W', 'dR_Hbb', 'mll_loose',
                'bjet2_btagCSV', 'avg_dr_jet_central', 'mbb_medium',
                'numBJets_loose', 'pT_HH', 'm_Hbb_regCorr', 'met_LD',
                'mT_top_3particle', 'dPhi_HHvis', 'dR_b2lep', 'numJetsForward',
                'lep_pt', 'wjet1_btagCSV', 'wjet2_btagCSV', 'selLepton_type', 'dR_b1lep', 'gen_mHH'
            ),
            classes = cms.vstring('HH', 'TT', 'ST', 'W', 'H', 'Other')

        ),
        resonant_spin2_boosted = cms.PSet(
            pbFileName_even = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/multiclass_DNN_wlbn_for_bb1l_boosted_odd_data_res_X_era.pb'), ## "LBN .pb -> Odd train:Even test" to be used for even evt no.
            pbFileName_odd = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/multiclass_DNN_wlbn_for_bb1l_boosted_even_data_res_X_era.pb'), ## "LBN .pb -> Even train:Odd test" to be used for odd evt no.
            ll_inputVariables = cms.vstring(
                'bjet1', 'bjet2', 'wjet1', 'wjet2', 'lep'
            ),
            hl_inputVariables = cms.vstring(
                'numJets', 'numBJets_medium', 'wjet1_btagCSV', 'mindr_lep1_jet',
                'tau21_Hbb', 'm_Hbb', 'wjet2_btagCSV', 'bjet2_btagCSV',
                'bjet1_btagCSV', 'mll_loose', 'numBJets_loose', 'mbb_medium',
                'pT_Hbb', 'lepPairCharge_loose', 'lep_pt', 'met', 'mT_W',
                'HT', 'mbb_loose', 'dR_Hbb', 'avg_dr_jet_central', 'dPhi_HHvis',
                'dPhi_Hww', 'pT_Hww', 'numJetsForward', 'gen_mHH'
            ),
            classes = cms.vstring('HH', 'TT', 'ST', 'W', 'H', 'Other')
        ),
        resonant_spin0_resolved = cms.PSet(
            pbFileName_even = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/multiclass_DNN_wlbn_for_bb1l_resolved_odd_data_res_X_era.pb'), ## "LBN .pb -> Odd train:Even test" to be used for even evt no.
            pbFileName_odd = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/multiclass_DNN_wlbn_for_bb1l_resolved_even_data_res_X_era.pb'), ## "LBN .pb -> Even train:Odd test" to be used for odd evt no.
            ll_inputVariables = cms.vstring(
                'bjet1', 'bjet2', 'wjet1', 'wjet2', 'lep'
            ),
            hl_inputVariables = cms.vstring(
                'numJets', 'bjet1_btagCSV', 'bjet2_btagCSV', 'mindr_lep1_jet',
                'pT_Hbb', 'm_Hbb_regCorr', 'dR_Hbb', 'mT_W', 'HT',
                'lepPairType_loose', 'lep_pt', 'pT_HH', 'mll_loose',
                'avg_dr_jet_central', 'met', 'wjet2_btagCSV', 'numBJets_loose',
                'mbb_medium', 'dR_b1lep', 'mT_top_2particle', 'mjj_highestpt',
                'numJetsForward', 'wjet1_btagCSV', 'dR_b2lep', 'pT_HHvis', 'gen_mHH'
            ),
            classes = cms.vstring('HH', 'TT', 'ST', 'W', 'H', 'Other')
        ),
        resonant_spin0_boosted = cms.PSet(
            pbFileName_even = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/multiclass_DNN_wlbn_for_bb1l_boosted_odd_data_res_X_era.pb'), ## "LBN .pb -> Odd train:Even test" to be used for even evt no.
            pbFileName_odd = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/multiclass_DNN_wlbn_for_bb1l_boosted_even_data_res_X_era.pb'), ## "LBN .pb -> Even train:Odd test" to be used for odd evt no.
            ll_inputVariables = cms.vstring(
                'bjet1', 'bjet2', 'wjet1', 'wjet2', 'lep'
            ),
            hl_inputVariables = cms.vstring(
                'numJets', 'numBJets_medium', 'wjet1_btagCSV',
                'mindr_lep1_jet', 'tau21_Hbb', 'wjet2_btagCSV',
                'm_Hbb', 'bjet1_btagCSV', 'bjet2_btagCSV',
                'lepPairCharge_loose', 'HT', 'mbb_medium', 'mll_loose',
                'met', 'lep_pt', 'pT_Hbb', 'avg_dr_jet_central',
                'numBJets_loose', 'dR_Hbb', 'mbb_loose', 'pT_HHvis',
                'dPhi_HHvis', 'm_HH_B2G_18_008', 'mT_top_3particle', 'numJetsForward', 'gen_mHH'
            ),
            classes = cms.vstring('HH', 'TT', 'ST', 'W', 'H', 'Other')
        ),
        nonresonant_resolved = cms.PSet(
            pbFileName_even = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/multiclass_DNN_wlbn_for_bb1l_resolved_odd_data_nonres_X_era.pb'), ## "LBN .pb -> Odd train:Even test" to be used for even evt no.
            pbFileName_odd = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/multiclass_DNN_wlbn_for_bb1l_resolved_even_data_nonres_X_era.pb'), ## "LBN .pb -> Even train:Odd test" to be used for odd evt no.
            ll_inputVariables = cms.vstring(
                'bjet1', 'bjet2', 'wjet1', 'wjet2', 'lep'
            ),
            hl_inputVariables = cms.vstring(
                'bjet1_btagCSV', 'mll_loose', 'numJets',
                'pT_Hbb', 'met', 'mindr_lep1_jet', 'mT_W',
                'bjet2_btagCSV', 'HT', 'selLepton_type',
                'dR_b2lep', 'dR_Hbb', 'mjj_highestpt',
                'mT_top_3particle', 'avg_dr_jet_central',
                'lep_pt', 'mht', 'dPhi_HHvis', 'mbb_medium',
                'm_Hbb_regCorr', 'leadFwdJet_pt', 'numBJets_loose', 'mbb_loose'
            ),
            classes = cms.vstring('HH', 'TT', 'ST', 'W', 'DY', 'Other')
        ),
        nonresonant_boosted = cms.PSet(
            pbFileName_even = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/multiclass_DNN_wlbn_for_bb1l_boosted_odd_data_nonres_X_era.pb'), ## "LBN .pb -> Odd train:Even test" to be used for even evt no.
            pbFileName_odd = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/multiclass_DNN_wlbn_for_bb1l_boosted_even_data_nonres_X_era.pb'), ## "LBN .pb -> Even train:Odd test" to be used for odd evt no.
            ll_inputVariables = cms.vstring(
                'bjet1', 'bjet2', 'wjet1', 'wjet2', 'lep'
            ),
            hl_inputVariables = cms.vstring(
                'numJets', 'wjet1_btagCSV', 'tau21_Hbb', 'm_Hbb',
                'mll_loose', 'numBJets_medium', 'mindr_lep1_jet',
                'bjet1_btagCSV', 'bjet2_btagCSV', 'pT_Hbb',
                'wjet2_btagCSV', 'met', 'HT', 'mT_W', 
                'mbb_loose', 'lep_pt', 'dR_b1lep', 'dPhi_HHvis', 
                'avg_dr_jet_central', 'dR_Hbb', 'mbb_medium', 'numBJets_loose',
                'pT_HH', 'pT_Wjj', 'm_HHvis', 'selLepton_type', 'dR_Wjj', 
                'pT_Hww', 'numJetsForward', 'Smin_Hww', 'mT_top_3particle', 'pT_HHvis'
            ),
            classes = cms.vstring('HH', 'TT', 'ST', 'W', 'DY', 'Other')
        )
    ),
    gen_mHH = cms.vdouble(250,260,270,280,300,320,350,400,450,500,550,600,650,700,750,800,850,900,1000), ## Set the signal mass range used in the BDT .pkl/.xml/.pb files
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

    hasPDF = cms.bool(False),
    pdfSettings = cms.PSet(
        lhaid = cms.uint32(0),
        norm = cms.vdouble(),
    ),

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
    blacklist = cms.PSet(
        inputFileNames = cms.vstring(),
        sampleName = cms.string(''),
    ),

    apply_LHEVpt_rwgt = cms.bool(False),
)

