import FWCore.ParameterSet.Config as cms
import os

from tthAnalysis.HiggsToTauTau.configs.recommendedMEtFilters_cfi import *
from tthAnalysis.HiggsToTauTau.configs.EvtYieldHistManager_cfi import *

process = cms.PSet()

process.fwliteInput = cms.PSet(
    fileNames = cms.vstring(),
    maxEvents = cms.int32(-1),
    outputEvery = cms.uint32(100000)
)

process.fwliteOutput = cms.PSet(
    fileName = cms.string('')
)

process.testMEM_hh_bb1l = cms.PSet(
    treeName = cms.string('Events'),

    maxSelEvents = cms.int32(1000),

    process = cms.string(''),
    histogramDir = cms.string(''),
    era = cms.string('2017'),

    triggers_1e = cms.vstring(
        'HLT_Ele32_WPTight_Gsf',
        'HLT_Ele35_WPTight_Gsf'
    ),
    use_triggers_1e = cms.bool(True),
    triggers_1mu = cms.vstring(
        'HLT_IsoMu24',
        'HLT_IsoMu27'
    ),
    use_triggers_1mu = cms.bool(True),
    
    apply_offline_e_trigger_cuts_1e = cms.bool(True),
    apply_offline_e_trigger_cuts_1mu = cms.bool(True),
    
    electronSelection = cms.string('Tight'),
    muonSelection = cms.string('Tight'),
    leptonChargeSelection = cms.string('OS'),

    central_or_shift = cms.string(''),
    apply_genWeight = cms.bool(True),
    apply_hlt_filter = cms.bool(False),
    apply_met_filters = cms.bool(True),
    cfgMEtFilter = cms.PSet(),

    branchName_electrons = cms.string('Electron'),
    branchName_muons = cms.string('Muon'),
    branchName_hadTaus = cms.string('Tau'),
    branchName_jets_ak4 = cms.string('Jet'),
    branchName_jets_ak8_Hbb = cms.string('FatJet'),
    branchName_subjets_ak8_Hbb = cms.string('SubJet'),
    #branchName_jets_ak8_Wjj = cms.string('FatJetAK8LS'),
    #branchName_subjets_ak8_Wjj = cms.string('SubJetAK8LS'),
    branchName_jets_ak8_Wjj = cms.string('FatJet'),
    branchName_subjets_ak8_Wjj = cms.string('SubJet'),
    branchName_met = cms.string('MET'),
    
    branchName_genLeptons = cms.string('GenLep'),
    branchName_genNeutrinos = cms.string('GenNu'),
    branchName_genJets = cms.string('GenJet'),

    branchName_genBJets = cms.string('GenBQuarkFromTop'),
    branchName_genWBosons = cms.string('GenVbosons'),
    branchName_genWJets = cms.string('GenWZQuark'),
    
    # branches specific to HH signal
    branchName_genParticlesFromHiggs = cms.string('GenHiggsDaughters'),

    # branches specific to ttbar background
    branchName_genLeptonsFromTop = cms.string('GenLepFromTop'),
    branchName_genNeutrinosFromTop = cms.string('GenNuFromTop'),
    branchName_genBQuarksFromTop = cms.string('GenBQuarkFromTop'),
    branchName_genLightQuarksFromTop = cms.string('GenQuarkFromTop'), # used for generator-level matching of jets from W->jj decays

    genMatchingOption = cms.int32(1),
    
    selEventsFileName_input = cms.string(''),
    selEventsFileName_output = cms.string(''),

    hasLHE = cms.bool(True),
    isDEBUG = cms.bool(False),
    tHweights = cms.VPSet(),
)

process_value = "$PROCESS"
genMatchingOption_value = $GENMATCHINGOPTION
if process_value == "signal":
    inputFiles = [
        "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_sm_hh_2b2v/0000/tree_1.root"
    ]
elif process_value == "background":
    inputFiles = [
        "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov24_woPresel_nom_all/ntuples/TTJets_SingleLeptFromT/0000/tree_1.root",
        #"/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov24_woPresel_nom_all/ntuples/TTJets_SingleLeptFromT/0000/tree_2.root",
        #"/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov24_woPresel_nom_all/ntuples/TTJets_SingleLeptFromT/0000/tree_3.root",
        #"/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov24_woPresel_nom_all/ntuples/TTJets_SingleLeptFromT/0000/tree_4.root",
        #"/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov24_woPresel_nom_all/ntuples/TTJets_SingleLeptFromT/0000/tree_5.root",
        "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov24_woPresel_nom_all/ntuples/TTJets_SingleLeptFromTbar/0000/tree_1.root",
        #"/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov24_woPresel_nom_all/ntuples/TTJets_SingleLeptFromTbar/0000/tree_2.root",
        #"/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov24_woPresel_nom_all/ntuples/TTJets_SingleLeptFromTbar/0000/tree_3.root",
        #"/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov24_woPresel_nom_all/ntuples/TTJets_SingleLeptFromTbar/0000/tree_4.root",
        #"/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov24_woPresel_nom_all/ntuples/TTJets_SingleLeptFromTbar/0000/tree_5.root",        
    ]
else:
    raise ValueError("Invalid Configuration parameter 'process' = %s !!" % process_value)
process.fwliteInput.fileNames = cms.vstring(inputFiles)
process.fwliteOutput.fileName = cms.string("testMEM_hh_bb1l_%s_genMatchOpt%i.root" % (process_value, genMatchingOption_value))
process.testMEM_hh_bb1l.process = cms.string(process_value)
process.testMEM_hh_bb1l.histogramDir = cms.string('%s_genMatchOpt%i' % (process_value, genMatchingOption_value))
process.testMEM_hh_bb1l.genMatchingOption = cms.int32(genMatchingOption_value)
