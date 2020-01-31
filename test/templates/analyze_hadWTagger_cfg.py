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

process.analyze_hadWTagger = cms.PSet(
    treeName = cms.string('Events'),

    process = cms.string(''),
    histogramDir = cms.string(''),
    era = cms.string(''),

    leptonSelection = cms.string(''),

    isMC = cms.bool(True),
    lumiScale = cms.VPSet(),
    apply_genWeight = cms.bool(True),

    branchName_electrons = cms.string('Electron'),
    branchName_muons = cms.string('Muon'),
    branchName_jets_ak4 = cms.string('Jet'),
    branchName_jets_ak8 = cms.string('FatJet'),
    branchName_subjets_ak8 = cms.string('SubJet'),
    branchName_met = cms.string('MET'),

    branchName_genLeptons = cms.string('GenLep'),
    branchName_genJets = cms.string('GenJet'),
    branchName_genBJets = cms.string('GenBQuarkFromTop'),
    branchName_genWBosons = cms.string('GenVbosons'),
    branchName_genWJets = cms.string('GenWZQuark'),

    jetCleaningByIndex = cms.bool(False),

    selEventsFileName_input = cms.string(''),

    isDEBUG = cms.bool(False),
    hasLHE = cms.bool(True),

    hhWeight_cfg = cms.PSet(
        denominator_file = cms.string(''),
        klScan_file = cms.string('hhAnalysis/multilepton/data/kl_scan.dat'),
        ktScan_file = cms.string(''),
        coefFile = cms.string('HHStatAnalysis/AnalyticalModels/data/coefficientsByBin_extended_3M_costHHSim_19-4.txt'),
        histtitle = cms.string(''),
        isDEBUG = cms.bool(False),
        do_scan = cms.bool(True),
        do_ktscan = cms.bool(False),
        apply_rwgt = cms.bool(False),
    ),
)
