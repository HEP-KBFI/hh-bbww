import FWCore.ParameterSet.Config as cms

from hhAnalysis.bbww.configs.makePlots_cfi import process

process.makePlots.distributions.extend([
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/m_ll"),
        xAxisTitle = cms.string("m_{ll} [GeV]"),
        yAxisTitle = cms.string("dN/dm_{ll} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/pT_ll"),
        xAxisTitle = cms.string("p_{T}^{ll} [GeV]"),
        yAxisTitle = cms.string("dN/p_{T}^{ll} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/m_Hbb"),
        xAxisTitle = cms.string("m_{bb} [GeV]"),
        yAxisTitle = cms.string("dN/dm_{bb} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/pT_Hbb"),
        xAxisTitle = cms.string("p_{T}^{bb} [GeV]"),
        yAxisTitle = cms.string("dN/p_{T}^{bb} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/dR_Hbb"),
        xAxisTitle = cms.string("#Delta R^{bb} [GeV]"),
        yAxisTitle = cms.string("dN/#Delta R^{bb} [1/GeV]")
    ),
])
