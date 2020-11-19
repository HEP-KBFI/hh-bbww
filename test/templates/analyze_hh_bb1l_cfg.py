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
            xmlFileName_even = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_bdt_odd_half_model_resolved_nonres.xml'), ## "BDT .xml -> Odd train:Even test" to be used for even evt no.
            xmlFileName_odd = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_bdt_even_half_model_resolved_nonres.xml'), ## "BDT .xml -> Even train:Odd test" to be used for odd evt no.
            inputVariables = cms.vstring(
                'lep_pt', 'bjet1_pt', 'bjet2_pt', 'met', 'm_Hbb_regCorr',
                'dR_Hbb', 'pT_Hbb', 'm_Wjj', 'dR_Hww', 'pT_Hww',
                'Smin_Hww', 'dR_b1lep', 'dR_b2lep', 'pT_HH', 'mT_W',
                'mT_top_2particle', 'mindr_lep1_jet', 'avg_dr_jet_central', 'mbb_loose', 'mbb_medium',
                'dR_HH', 'cosThetaS_HH', 'mht', 'jpaScore', 'bjet1_btagCSV',
                'wjet1_btagCSV', 'vbf_m_jj', 'vbf_dEta_jj',
                'SM', 'BM1', 'BM2', 'BM3', 'BM4', 'BM5', 'BM6', 'BM7', 'BM8', 'BM9', 'BM10', 'BM11', 'BM12'
            )
        ),
        nonresonant_boosted = cms.PSet(
            xmlFileName_even = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_bdt_odd_half_model_boosted_nonres.xml'), ## "BDT .xml -> Odd train:Even test" to be used for even evt no.
            xmlFileName_odd = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_bdt_even_half_model_boosted_nonres.xml'), ## "BDT .xml -> Even train:Odd test" to be used for odd evt no.
            inputVariables = cms.vstring(
                'bjet2_pt', 'met', 'm_Hbb', 'dR_Hbb', 'm_HHvis',
                'pT_HH', 'mT_W', 'mindr_lep1_jet', 'avg_dr_jet_central', 'mbb_loose',
                'mbb_medium', 'tau21_Hbb', 'numJets', 'numBJets_loose', 'numBJets_medium', 
                'lep_pt', 'Smin_Hww', 'dR_b1lep', 'pT_Hww', 'mT_top_2particle', 
                'pT_Hbb', 'dR_Wjj', 'cosThetaS_HH', 'bjet1_btagCSV', 
                'wjet1_btagCSV', 'vbf_m_jj', 'vbf_dEta_jj',
                'SM', 'BM1', 'BM2', 'BM3', 'BM4', 'BM5', 'BM6', 'BM7', 'BM8', ##'BM9', 'BM10', 'BM11', 'BM12'
            )
        )
    ),
    LBN = cms.PSet(
        resonant_spin2_resolved = cms.PSet(

        ),
        resonant_spin2_boosted = cms.PSet(

        ),
        resonant_spin0_resolved = cms.PSet(
            pbFileName_even = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/multiclass_DNN_wlbn_for_bb1l_resolved_odd_data_res_spin0.pb'), ## "LBN .pb -> Odd train:Even test" to be used for even evt no.
            pbFileName_odd = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/multiclass_DNN_wlbn_for_bb1l_resolved_even_data_res_spin0.pb'), ## "LBN .pb -> Even train:Odd test" to be used for odd evt no.
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
            classes = cms.vstring('HH', 'TT', 'W', 'DY', 'ST', 'Other')
        ),
        resonant_spin0_boosted = cms.PSet(
            pbFileName_even = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/multiclass_DNN_wlbn_for_bb1l_boosted_odd_data_res_spin0.pb'), ## "LBN .pb -> Odd train:Even test" to be used for even evt no.
            pbFileName_odd = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/multiclass_DNN_wlbn_for_bb1l_boosted_even_data_res_spin0.pb'), ## "LBN .pb -> Even train:Odd test" to be used for odd evt no.
            ll_inputVariables = cms.vstring(
                'bjet1', 'bjet2', 'wjet1', 'wjet2', 'lep'
            ),
            hl_inputVariables = cms.vstring(
                'mht', 'HT', 'm_Hbb', 'jpaScore', 'm_Wjj', 
                'dR_HH', 'mbb_loose', 'mbb_medium', 'numJets', 'numBJets_medium', 
                'numBJets_medium', 'dR_b1lep', 'pT_HH', 'm_HH_B2G_18_008', 'mT_W', 
                'mT_top_2particle', 'mindr_lep1_jet', 'avg_dr_jet_central', 'mll_loose', 'bjet2_pt', 
                'leadFwdJet_pt', 'numLeptons', 'tau21_Hbb', 'vbf_m_jj', 'vbf_dEta_jj', 
                'bjet1_btagCSV', 'wjet1_btagCSV', 'gen_mHH'
            ),
            classes = cms.vstring('HH', 'TT', 'W', 'DY', 'ST', 'Other')
        ),
        nonresonant_resolved = cms.PSet(
            pbFileName_even = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/multiclass_DNN_wlbn_for_bb1l_resolved_odd_data_nonres.pb'), ## "LBN .pb -> Odd train:Even test" to be used for even evt no.
            pbFileName_odd = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/multiclass_DNN_wlbn_for_bb1l_resolved_even_data_nonres.pb'), ## "LBN .pb -> Even train:Odd test" to be used for odd evt no.
            ll_inputVariables = cms.vstring(
                'bjet1', 'bjet2', 'wjet1', 'wjet2', 'lep'
            ),
            hl_inputVariables = cms.vstring(
                'met', 'm_Hbb', 'eta_Hbb', 'jpaScore', 'm_Wjj', 
                'Smin_Hww', 'dR_HH', 'mbb_loose', 'mbb_medium', 'numJets', 
                'numBJets_loose', 'numBJets_medium', 'pT_Hww', 'dR_b1lep', 'pT_HHvis', 
                'm_HH', 'm_HH_B2G_18_008', 'mT_W', 'mindr_lep1_jet', 'avg_dr_jet_central', 
                'mll_loose', 'cosThetaS_WW', 'cosThetaS_HH', 'leadFwdJet_pt', 'vbf_m_jj', 
                'vbf_dEta_jj', 'bjet1_btagCSV', 'wjet1_btagCSV',
                'SM', 'BM1', 'BM2', 'BM3', 'BM4', 'BM5', 'BM6', 'BM7', 'BM8', 'BM9', 'BM10', 'BM11', 'BM12'
            ),
            classes = cms.vstring('HH', 'TT', 'W', 'DY', 'ST', 'Other')
        ),
        nonresonant_boosted = cms.PSet(
            pbFileName_even = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/multiclass_DNN_wlbn_for_bb1l_boosted_odd_data_nonres.pb'), ## "LBN .pb -> Odd train:Even test" to be used for even evt no.
            pbFileName_odd = cms.string('hhAnalysis/bbww/data/BDT_hh_bb1l/multiclass_DNN_wlbn_for_bb1l_boosted_even_data_nonres.pb'), ## "LBN .pb -> Even train:Odd test" to be used for odd evt no.
            ll_inputVariables = cms.vstring(
                'bjet1', 'bjet2', 'wjet1', 'wjet2', 'lep'
            ),
            hl_inputVariables = cms.vstring(
                'mht', 'HT', 'm_Hbb', 'jpaScore', 'm_Wjj', 
                'dR_HH', 'mbb_loose', 'mbb_medium', 'numJets', 'numBJets_medium', 
                'numBJets_medium', 'dR_b1lep', 'pT_HH', 'm_HH_B2G_18_008', 'mT_W', 
                'mT_top_2particle', 'mindr_lep1_jet', 'avg_dr_jet_central', 'mll_loose', 'bjet2_pt', 
                'leadFwdJet_pt', 'numLeptons', 'tau21_Hbb', 'vbf_m_jj', 'vbf_dEta_jj', 
                'bjet1_btagCSV', 'wjet1_btagCSV',
                'SM', 'BM1', 'BM2', 'BM3', 'BM4', 'BM5', 'BM6', 'BM7', 'BM8', 'BM9', 'BM10', 'BM11', 'BM12'
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

#----------------------------------------------------------------------------------------------------
# CV: temporary work-around; 
#     neccessary because Saswati has not finished BDT and LBN training for resonant HH signal yet
process.analyze_hh_bb1l.BDT.resonant_spin2_resolved = process.analyze_hh_bb1l.BDT.nonresonant_resolved
process.analyze_hh_bb1l.BDT.resonant_spin2_boosted  = process.analyze_hh_bb1l.BDT.nonresonant_boosted
process.analyze_hh_bb1l.BDT.resonant_spin0_resolved = process.analyze_hh_bb1l.BDT.nonresonant_resolved
process.analyze_hh_bb1l.BDT.resonant_spin0_boosted  = process.analyze_hh_bb1l.BDT.nonresonant_boosted
process.analyze_hh_bb1l.LBN.resonant_spin2_resolved = process.analyze_hh_bb1l.LBN.nonresonant_resolved
process.analyze_hh_bb1l.LBN.resonant_spin2_boosted  = process.analyze_hh_bb1l.LBN.nonresonant_boosted
##process.analyze_hh_bb1l.LBN.resonant_spin0_resolved = process.analyze_hh_bb1l.LBN.nonresonant_resolved
##process.analyze_hh_bb1l.LBN.resonant_spin0_boosted  = process.analyze_hh_bb1l.LBN.nonresonant_boosted
##process.fwliteInput.maxEvents = cms.int32(10000)
##process.fwliteInput.outputEvery = cms.uint32(1000)
#----------------------------------------------------------------------------------------------------
