import FWCore.ParameterSet.Config as cms

from hhAnalysis.bbww.makePlots_mcClosure_cfg import process

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
    )
])
