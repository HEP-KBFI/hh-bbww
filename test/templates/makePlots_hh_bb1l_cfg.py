import FWCore.ParameterSet.Config as cms

from hhAnalysis.bbww.configs.makePlots_cfi import process

process.makePlots.distributions.extend([
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/m_Wjj"),
        xAxisTitle = cms.string("m_{jj} [GeV]"),
        yAxisTitle = cms.string("dN/dm_{jj} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/dR_Wjj"),
        xAxisTitle = cms.string("#Delta R_{jj}"),
        yAxisTitle = cms.string("dN/d#Delta R_{jj}")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/pT_Wjj"),
        xAxisTitle = cms.string("p_{T}^{jj} [GeV]"),
        yAxisTitle = cms.string("dN/dp_{T}^{jj} [1/GeV]")
    ),    
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/dR_Hww"),
        xAxisTitle = cms.string("#Delta R_{WW}"),
        yAxisTitle = cms.string("dN/d#Delta R_{WW}")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/pT_Hww"),
        xAxisTitle = cms.string("p_{T}^{WW} [GeV]"),
        yAxisTitle = cms.string("dN/dp_{T}^{WW} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/Smin_Hww"),
        xAxisTitle = cms.string("S_{min}^{WW} [GeV]"),
        yAxisTitle = cms.string("dN/dS_{min}^{WW} [1/GeV]")
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
        histogramName = cms.string("sel/evt/$PROCESS/m_HH_B2G_18_008"),
        xAxisTitle = cms.string("m_{HH} (B2G-18-008) [GeV]"),
        yAxisTitle = cms.string("dN/dm_{HH} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/pT_HH"),
        xAxisTitle = cms.string("p_{T}^{HH} [GeV]"),
        yAxisTitle = cms.string("dN/dp_{T}^{HH} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/dR_HH"),
        xAxisTitle = cms.string("#Delta R^{HH} [GeV]"),
        yAxisTitle = cms.string("dN/d#Delta R^{HH} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/Smin_HH"),
        xAxisTitle = cms.string("S_{min}^{HH} [GeV]"),
        yAxisTitle = cms.string("dN/dS_{min}^{HH} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/mT_W"),
        xAxisTitle = cms.string("m_{T}^{W} [GeV]"),
        yAxisTitle = cms.string("dN/dm_{T}^{W} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/mT_top_3particle"),
        xAxisTitle = cms.string("m_{T}^{top} [GeV]"),
        yAxisTitle = cms.string("dN/dm_{T}^{top} [1/GeV]")
    ),
##    cms.PSet(
##        histogramName = cms.string("sel/evt/$PROCESS/mvaOutput_Hj_tagger"),
##        xAxisTitle = cms.string("MVA Discriminant Hj Tagger"),
##        yAxisTitle = cms.string("dN/dMVA")
##    ),
##    cms.PSet(
##        histogramName = cms.string("sel/evt/$PROCESS/mvaOutput_Hjj_tagger"),
##        xAxisTitle = cms.string("MVA Discriminant Hjj Tagger"),
##        yAxisTitle = cms.string("dN/dMVA")
##    ),
##     cms.PSet(
##         histogramName = cms.string("sel/evt/$PROCESS/vbf_jet1_pt"),
##         xAxisTitle = cms.string("leading VBF jet p_{T} [GeV]"),
##         yAxisTitle = cms.string("dN/dp_{T} [1/GeV]")
##     ),
##     cms.PSet(
##         histogramName = cms.string("sel/evt/$PROCESS/vbf_jet1_eta"),
##         xAxisTitle = cms.string("leading VBF jet #eta"),
##         yAxisTitle = cms.string("dN/d#eta [1/GeV]")
##     ),
##     cms.PSet(
##         histogramName = cms.string("sel/evt/$PROCESS/vbf_jet2_pt"),
##         xAxisTitle = cms.string("subleading VBF jet p_{T} [GeV]"),
##         yAxisTitle = cms.string("dN/dp_{T} [1/GeV]")
##     ),
##     cms.PSet(
##         histogramName = cms.string("sel/evt/$PROCESS/vbf_jet2_eta"),
##         xAxisTitle = cms.string("subleading VBF jet #eta"),
##         yAxisTitle = cms.string("dN/d#eta [1/GeV]")
##     ),
##     cms.PSet(
##         histogramName = cms.string("sel/evt/$PROCESS/vbf_m_jj"),
##         xAxisTitle = cms.string("VBF jet m_{jj} [GeV]"),
##         yAxisTitle = cms.string("dN/dm_{jj} [1/GeV]")
##     ),
##     cms.PSet(
##         histogramName = cms.string("sel/evt/$PROCESS/vbf_dEta_jj"),
##         xAxisTitle = cms.string("VBF jet #Delta#eta_{jj} [GeV]"),
##         yAxisTitle = cms.string("dN/d#Delta#eta_{jj}")
##     ),
    cms.PSet(
           histogramName = cms.string("sel/evtYield/$PROCESS/evtYield"),
           xAxisTitle = cms.string("Run Period"),
           yAxisTitle = cms.string("Events / 1 fb^{-1}"),
           divideByBinWidth = cms.bool(False)
    )
])
