import FWCore.ParameterSet.Config as cms

from hhAnalysis.bbww.configs.makePlots_cfi import process

process.makePlots.distributions.extend([
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/m_ltau'),
        xAxisTitle = cms.string('m_{l#tau} [GeV]'),
        yAxisTitle = cms.string('dN/dm_{l#tau} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/dR_ltau"),
        xAxisTitle = cms.string("#Delta R_{l#tau}"),
        yAxisTitle = cms.string("dN/d#Delta R_{l#tau}")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/dPhi_ltau"),
        xAxisTitle = cms.string("#Delta#phi_{l#tau}"),
        yAxisTitle = cms.string("dN/d#Delta#phi_{l#tau}")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/m_Hww"),
        xAxisTitle = cms.string("m_{l#tau+MET} [GeV]"),
        yAxisTitle = cms.string("dN/dm_{l#tau+MET} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/pT_Hww"),
        xAxisTitle = cms.string("p_{T}^{l#tau+MET} [GeV]"),
        yAxisTitle = cms.string("dN/dp_{T}^{l#tau+MET} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/m_Hbb"),
        xAxisTitle = cms.string("m_{bb} [GeV]"),
        yAxisTitle = cms.string("dN/dm_{bb} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/pT_Hbb"),
        xAxisTitle = cms.string("p_{T}^{bb} [GeV]"),
        yAxisTitle = cms.string("dN/dp_{T}^{bb} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/dR_Hbb"),
        xAxisTitle = cms.string("#Delta R^{bb} [GeV]"),
        yAxisTitle = cms.string("dN/d#Delta R^{bb} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/m_HHvis"),
        xAxisTitle = cms.string("m_{HH}^{vis} [GeV]"),
        yAxisTitle = cms.string("dN/dm_{HH}^{vis} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/m_HH"),
        xAxisTitle = cms.string("m_{HH} [GeV]"),
        yAxisTitle = cms.string("dN/dm_{HH} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/pT_HH"),
        xAxisTitle = cms.string("p_{T}^{HH} [GeV]"),
        yAxisTitle = cms.string("dN/dp_{T}^{HH} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/vbf_jet1_pt"),
        xAxisTitle = cms.string("leading VBF jet p_{T} [GeV]"),
        yAxisTitle = cms.string("dN/dp_{T} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/vbf_jet1_eta"),
        xAxisTitle = cms.string("leading VBF jet #eta"),
        yAxisTitle = cms.string("dN/d#eta [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/vbf_jet2_pt"),
        xAxisTitle = cms.string("subleading VBF jet p_{T} [GeV]"),
        yAxisTitle = cms.string("dN/dp_{T} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/vbf_jet2_eta"),
        xAxisTitle = cms.string("subleading VBF jet #eta"),
        yAxisTitle = cms.string("dN/d#eta [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/vbf_m_jj"),
        xAxisTitle = cms.string("VBF jet m_{jj} [GeV]"),
        yAxisTitle = cms.string("dN/dm_{jj} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/vbf_dEta_jj"),
        xAxisTitle = cms.string("VBF jet #Delta#eta_{jj} [GeV]"),
        yAxisTitle = cms.string("dN/d#Delta#eta_{jj}")
    )
])
