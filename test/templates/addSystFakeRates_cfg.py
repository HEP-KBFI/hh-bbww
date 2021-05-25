import FWCore.ParameterSet.Config as cms

import os

process = cms.PSet()

process.fwliteInput = cms.PSet(
    fileNames = cms.vstring()
)

process.fwliteOutput = cms.PSet(
    fileName = cms.string('addSystFakeRates.root')
)

process.addSystFakeRates = cms.PSet(

    process = cms.string("data_fakes"),

    histogramToFit = cms.string("mvaOutput_final"),
    xAxisTitle = cms.string("MVA Discriminant"),
    yAxisTitle = cms.string("dN/dMVA"),

    addSyst = cms.VPSet(
        cms.PSet(
            name = cms.string("CMS_ttHl_Clos_e"),
            fakes_mc = cms.PSet(
                inputFileName = cms.string(''),
                histogramName = cms.string(''),
            ),
            mcClosure = cms.PSet(
                inputFileName = cms.string(''),
                histogramName = cms.string(''),
            )
        ),
        cms.PSet(
            name = cms.string("CMS_ttHl_Clos_m"),
            fakes_mc = cms.PSet(
                inputFileName = cms.string(''),
                histogramName = cms.string(''),
            ),
            mcClosure = cms.PSet(
                inputFileName = cms.string(''),
                histogramName = cms.string(''),
            )
        ),
        cms.PSet(
            name = cms.string("CMS_ttHl_Clos_t"),
            fakes_mc = cms.PSet(
                inputFileName = cms.string(''),
                histogramName = cms.string(''),
            ),
            mcClosure = cms.PSet(
                inputFileName = cms.string(''),
                histogramName = cms.string(''),
            )
        )
    ),

    outputFileName = cms.string("addSystFakeRates.png")
)
