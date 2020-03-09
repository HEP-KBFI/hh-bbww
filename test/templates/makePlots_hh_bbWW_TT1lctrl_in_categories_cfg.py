import FWCore.ParameterSet.Config as cms

from hhAnalysis.bbww.configs.makePlots_cfi import process

process.makePlots.processSignal = cms.string("")

process.makePlots.distributions.extend([
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/hadTop_pt'),
        xAxisTitle = cms.string('p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/lepTop_pt'),
        xAxisTitle = cms.string('p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/mT'),
        xAxisTitle = cms.string('m_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dm_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/jetAK8_Wjj_dR_lepton'),
        xAxisTitle = cms.string('#Delta R'),
        yAxisTitle = cms.string('dN/d#Delta R')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/mtt'),
        xAxisTitle = cms.string('m_{tt} [GeV]'),
        yAxisTitle = cms.string('dN/dm_{tt} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/HT'),
        xAxisTitle = cms.string('H_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dH_{T} [1/GeV]')
    )
])

process.makePlots.labelOnTop = cms.string("CMS Simulation")
