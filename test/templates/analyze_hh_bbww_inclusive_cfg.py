import FWCore.ParameterSet.Config as cms
import os

from tthAnalysis.HiggsToTauTau.configs.recommendedMEtFilters_cfi import *
from tthAnalysis.HiggsToTauTau.configs.EvtYieldHistManager_cfi import *

process = cms.PSet()

process.fwliteInput = cms.PSet(
    fileNames = cms.vstring(),
    maxEvents = cms.int32(-1),
    outputEvery = cms.uint32(1000)
)

process.fwliteOutput = cms.PSet(
    fileName = cms.string('')
)

process.analyze_hh_bbww_inclusive = cms.PSet(
    treeName = cms.string('Events'),
    process = cms.string('signal'),
    era = cms.string('2017'),

    triggers_1e = cms.vstring(),
    triggers_2e = cms.vstring(),
    triggers_1mu = cms.vstring(),
    triggers_2mu = cms.vstring(),
    triggers_1e1mu = cms.vstring(),

    use_triggers_1e = cms.bool(True),
    use_triggers_2e = cms.bool(True),
    use_triggers_1mu = cms.bool(True),
    use_triggers_2mu = cms.bool(True),
    use_triggers_1e1mu = cms.bool(True),

    apply_offline_e_trigger_cuts_1e = cms.bool(True),
    apply_offline_e_trigger_cuts_2e = cms.bool(True),
    apply_offline_e_trigger_cuts_1mu = cms.bool(True),
    apply_offline_e_trigger_cuts_2mu = cms.bool(True),
    apply_offline_e_trigger_cuts_1e1mu = cms.bool(True),

    isMC = cms.bool(True),
    central_or_shift = cms.string('central'),

    branchName_electrons = cms.string('Electron'),
    branchName_muons = cms.string('Muon'),
    branchName_jets = cms.string('Jet'),
    branchName_fatJets = cms.string('FatJet'),
    branchName_subJets = cms.string('SubJet'),
    branchName_fatJetsLS = cms.string('FatJetAK8LSLoose'),
    branchName_subJetsLS = cms.string('SubJetAK8LSLoose'),
    branchName_met = cms.string('MET'),

    selEventsFileName_input = cms.string(''),
    isDEBUG = cms.bool(False),
    useNonNominal = cms.bool(False),

    genMatchingByIndex = cms.bool(True),
    jetCleaningByIndex = cms.bool(False),

    syncNtuple = cms.PSet(
        tree = cms.string('syncTree'),
        output = cms.string('inclusive.root'),
        requireGenMatching = cms.bool(False),
    ),
    tHweights = cms.VPSet(),
)
