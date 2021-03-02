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
            xmlFileName_even = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_bdt_odd_half_model_resolved_nonres_BM_era.xml'), ## "BDT .xml -> Odd train:Even test" to be used for even evt no.
            xmlFileName_odd = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_bdt_even_half_model_resolved_nonres_BM_era.xml'), ## "BDT .xml -> Even train:Odd test" to be used for odd evt no.
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
            xmlFileName_even = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_bdt_odd_half_model_boosted_nonres_BM_era.xml'), ## "BDT .xml -> Odd train:Even test" to be used for even evt no.
            xmlFileName_odd = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_bdt_even_half_model_boosted_nonres_BM_era.xml'), ## "BDT .xml -> Even train:Odd test" to be used for odd evt no.
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

        ),
        resonant_spin2_boosted = cms.PSet(

        ),
        resonant_spin0_resolved = cms.PSet(
            pbFileName_even = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/multiclass_DNN_wlbn_for_bb1l_resolved_odd_data_res_spin0_%s.pb'), ## "LBN .pb -> Odd train:Even test" to be used for even evt no.
            pbFileName_odd = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/multiclass_DNN_wlbn_for_bb1l_resolved_even_data_res_spin0_%s.pb'), ## "LBN .pb -> Even train:Odd test" to be used for odd evt no.
            ll_inputVariables = cms.vstring(
                'bjet1', 'bjet2', 'wjet1', 'wjet2', 'lep'
            ),
            hl_inputVariables = cms.vstring(
                'met', 'm_Hbb', 'eta_Hbb', 'jpaScore', 'm_Wjj',
                'Smin_Hww', 'dR_HH', 'mbb_loose', 'mbb_medium', 'numJets',
                'numBJets_loose', 'numBJets_medium', 'pT_Hww', 'dR_b1lep', 'pT_HHvis',
                'm_HH', 'm_HH_B2G_18_008', 'mT_W', 'mindr_lep1_jet', 'avg_dr_jet_central',
                'mll_loose', 'cosThetaS_WW', 'cosThetaS_HH', 'leadFwdJet_pt', 'vbf_m_jj',
                'vbf_dEta_jj', 'bjet1_btagCSV', 'wjet1_btagCSV', 'gen_mHH'
            ),
            classes = cms.vstring('HH', 'TT', 'ST', 'Other', 'W', 'DY')
        ),
        resonant_spin0_boosted = cms.PSet(
            pbFileName_even = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/multiclass_DNN_wlbn_for_bb1l_boosted_odd_data_res_spin0_%s.pb'), ## "LBN .pb -> Odd train:Even test" to be used for even evt no.
            pbFileName_odd = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/multiclass_DNN_wlbn_for_bb1l_boosted_even_data_res_spin0_%s.pb'), ## "LBN .pb -> Even train:Odd test" to be used for odd evt no.
            ll_inputVariables = cms.vstring(
                'bjet1', 'bjet2', 'wjet1', 'wjet2', 'lep'
            ),
            hl_inputVariables = cms.vstring(
                'mht', 'HT', 'm_Hbb', 'jpaScore', 'm_Wjj',
                'dR_HH', 'mbb_loose', 'mbb_medium', 'numJets', 'numBJets_medium',
                'numBJets_medium', 'dR_b1lep', 'pT_HH', 'm_HH_B2G_18_008', 'mT_W',
                'mT_top_2particle', 'mindr_lep1_jet', 'avg_dr_jet_central', 'mll_loose', 'bjet2_pt',
                'leadFwdJet_pt', 'numJets', 'tau21_Hbb', 'vbf_m_jj', 'vbf_dEta_jj',
                'bjet1_btagCSV', 'wjet1_btagCSV', 'gen_mHH'
            ),
            classes = cms.vstring('HH', 'TT', 'ST', 'Other', 'W', 'DY')
        ),
        nonresonant_resolved = cms.PSet(
            pbFileName_even = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/multiclass_DNN_wlbn_for_bb1l_resolved_odd_data_nonres_BM_era.pb'), ## "LBN .pb -> Odd train:Even test" to be used for even evt no.
            pbFileName_odd = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/multiclass_DNN_wlbn_for_bb1l_resolved_even_data_nonres_BM_era.pb'), ## "LBN .pb -> Even train:Odd test" to be used for odd evt no.
            ll_inputVariables = cms.vstring(
                'bjet1', 'bjet2', 'wjet1', 'wjet2', 'lep'
            ),
            hl_inputVariables = cms.vstring(
                'bjet2_btagCSV', 'bjet1_btagCSV', 'mT_W', 'mll_loose',
                'jpaScore', 'mindr_lep1_jet', 'pT_HH', 'pT_Hbb', 'met',
                'm_Wjj', 'dR_b1lep', 'leadFwdJet_pt', 'm_Hbb_regCorr',
                'avg_dr_jet_central', 'mht', 'HT', 'm_HH', 'selLepton_type',
                'dPhi_Hbb', 'pT_Hww'
            ),
            classes = cms.vstring('HH', 'TT', 'ST', 'Other', 'W', 'DY')
        ),
        nonresonant_boosted = cms.PSet(
            pbFileName_even = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/multiclass_DNN_wlbn_for_bb1l_boosted_odd_data_nonres_BM_era.pb'), ## "LBN .pb -> Odd train:Even test" to be used for even evt no.
            pbFileName_odd = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/multiclass_DNN_wlbn_for_bb1l_boosted_even_data_nonres_BM_era.pb'), ## "LBN .pb -> Even train:Odd test" to be used for odd evt no.
            ll_inputVariables = cms.vstring(
                'bjet1', 'bjet2', 'wjet1', 'wjet2', 'lep'
            ),
            hl_inputVariables = cms.vstring(
                'jpaScore', 'tau21_Hbb', 'mbb_medium', 'bjet2_btagCSV',
                'bjet1_btagCSV', 'mindr_lep1_jet', 'm_Hbb', 'met',
                'mll_loose', 'mbb_loose', 'mht', 'leadFwdJet_pt',
                'avg_dr_jet_central', 'pT_Hbb', 'pT_HH', 'dR_b1lep',
                'dR_Hbb', 'dPhi_HH', 'Smin_HH', 'mT_W', 'selLepton_type', 'dPhi_HHvis'
            ),
            classes = cms.vstring('HH', 'TT', 'ST', 'Other', 'W', 'DY')
        )
    ),
    gen_mHH = cms.vdouble(250,260,270,280,300,350,400,450,500,550,600,650,700),#750,800,850,900,1000), ## Set the signal mass range used in the BDT .pkl/.xml/.pb files
    nonRes_BMs = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),

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

#----------------------------------------------------------------------------------------------------
# CV: temporary work-around; 
#     neccessary because Saswati has not finished BDT and LBN training for resonant HH signal yet
process.analyze_hh_bb1l.BDT.resonant_spin2_resolved = process.analyze_hh_bb1l.BDT.nonresonant_resolved
process.analyze_hh_bb1l.BDT.resonant_spin2_boosted  = process.analyze_hh_bb1l.BDT.nonresonant_boosted
process.analyze_hh_bb1l.BDT.resonant_spin0_resolved = process.analyze_hh_bb1l.BDT.nonresonant_resolved
process.analyze_hh_bb1l.BDT.resonant_spin0_boosted  = process.analyze_hh_bb1l.BDT.nonresonant_boosted
process.analyze_hh_bb1l.LBN.resonant_spin2_resolved = process.analyze_hh_bb1l.LBN.nonresonant_resolved
process.analyze_hh_bb1l.LBN.resonant_spin2_boosted  = process.analyze_hh_bb1l.LBN.nonresonant_boosted
process.analyze_hh_bb1l.LBN.resonant_spin0_resolved = process.analyze_hh_bb1l.LBN.nonresonant_resolved
process.analyze_hh_bb1l.LBN.resonant_spin0_boosted  = process.analyze_hh_bb1l.LBN.nonresonant_boosted
#----------------------------------------------------------------------------------------------------
