import FWCore.ParameterSet.Config as cms

import os

process = cms.PSet()

process.fwliteInput = cms.PSet(
    fileNames = cms.vstring(),
    maxEvents = cms.int32(-1),
    outputEvery = cms.uint32(100000)
)

process.fwliteOutput = cms.PSet(
    fileName = cms.string('')
)

process.compDYBgrWeights = cms.PSet(

    era = cms.string(""),

    processData = cms.string("data_obs"),
    processesToSubtract = cms.vstring(),

    processMC = cms.string("DY"),

    isMC = cms.bool(True),

    outputFilePath = cms.string(""),

    categories = cms.VPSet(
        cms.PSet(
            numerator1 = cms.string("hh_bb2l_DYBgrMR_OS_Tight/sel/dyBgr/%s/resolved_1b_HT"),
            denominator1 = cms.string("hh_bb2l_DYBgrMR_OS_Tight/sel/dyBgr/%s/resolved_0b_HT"),
            weight1 = cms.string("Weight1B"),
            numerator2 = cms.string("hh_bb2l_DYBgrMR_OS_Tight/sel/dyBgr/%s/resolved_2b_HT"),
            denominator2 = cms.string("hh_bb2l_DYBgrMR_OS_Tight/sel/dyBgr/%s/resolved_0b_HT"),
            weight2 = cms.string("Weight2B"),
            outputFileName = cms.string("weight_HT_SF_%s_1D_%s.root")
        ),
        cms.PSet(
            numerator1 = cms.string("hh_bb2l_DYBgrMR_OS_Tight/sel/dyBgr/%s/boosted_ge1b_msoftdrop"),
            denominator1 = cms.string("hh_bb2l_DYBgrMR_OS_Tight/sel/dyBgr/%s/boosted_0b_msoftdrop"),
            weight1 = cms.string("Weight1B"),
            numerator2 = cms.string(""),
            denominator2 = cms.string(""),
            weight2 = cms.string(""),
            outputFileName = cms.string("weight_fatjetsoftDropmass_SF_%s_1D_%s.root")
        )
    )
)
