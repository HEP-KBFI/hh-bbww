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
    outputEvery = cms.uint32(1000)
)

process.fwliteOutput = cms.PSet(
    fileName = cms.string('')
)

process.analyze_hh_HHatLOvsNLO = cms.PSet(
    treeName = cms.string('Events'),

    process = cms.string(''),
    histogramDir = cms.string(''),
    era = cms.string(''),

    isMC = cms.bool(True),
    central_or_shift = cms.string(''),
    lumiScale = cms.VPSet(),
    ref_genWeight = cms.double(0.),
    apply_genWeight = cms.bool(True),
    apply_topPtReweighting = cms.string(''),

    branchName_genHBosons = cms.string('GenHiggs'),

    gen_mHH = cms.vdouble(250,260,270,280,300,350,400,450,500,550,600,650,700,750,800,850,900,1000),
    nonRes_BMs = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),

    isDEBUG = cms.bool(False),
    hasLHE = cms.bool(True),
    hasPS = cms.bool(False),
    apply_LHE_nom = cms.bool(False),

    evtWeight = cms.PSet(
        apply = cms.bool(False),
        histogramFile = cms.string(''),
        histogramName = cms.string(''),
        branchNameXaxis = cms.string(''),
        branchNameYaxis = cms.string(''),
        branchTypeXaxis = cms.string(''),
        branchTypeYaxis = cms.string(''),
    ),
    hhWeight_cfg = hhWeight,

    leptonFakeRateWeight = cms.PSet()
)

