import FWCore.ParameterSet.Config as cms

from hhAnalysis.bbww.configs.makePlots_cfi import process

process.makePlots.processSignal = cms.string("")

process.makePlots.distributions.extend([
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/mT'),
        xAxisTitle = cms.string('m_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dm_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/pT_lnu'),
        xAxisTitle = cms.string('p_{T}^{W} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T}^{W} [1/GeV]')
    )
])

process.makePlots.labelOnTop = cms.string("CMS Simulation")
