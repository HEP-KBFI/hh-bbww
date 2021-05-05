import FWCore.ParameterSet.Config as cms

from hhAnalysis.bbww.configs.makePlots_cfi import process

process.makePlots.distributions.extend([
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/HT"),
        xAxisTitle = cms.string("HT [GeV]"),
        yAxisTitle = cms.string("dN/dHT [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/met"),
        xAxisTitle = cms.string("met"),
        yAxisTitle = cms.string("dN/dmet")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/lep_pt"),
        xAxisTitle = cms.string("p_{T}^{lep} [GeV]"),
        yAxisTitle = cms.string("dN/dp_{T}^{lep} [1/GeV]")
    ),    
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/dR_Hbb"),
        xAxisTitle = cms.string("#Delta R_{Hbb}"),
        yAxisTitle = cms.string("dN/d#Delta R_{Hbb}")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/pT_Hbb"),
        xAxisTitle = cms.string("p_{T}^{Hbb} [GeV]"),
        yAxisTitle = cms.string("dN/dp_{T}^{Hbb} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/m_Hbb_regCorr"),
        xAxisTitle = cms.string("m_{Hbb}^{regCorr} [GeV]"),
        yAxisTitle = cms.string("dN/dm_{Hbb}^{regCorr} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/pT_Hww"),
        xAxisTitle = cms.string("pT_{Hww} [GeV]"),
        yAxisTitle = cms.string("dN/dpT_{Hww} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/pT_HH"),
        xAxisTitle = cms.string("p_{T}^{HH} [GeV]"),
        yAxisTitle = cms.string("dN/dp_{T}^{HH} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/dR_b1lep"),
        xAxisTitle = cms.string("#Delta R^{b1lep}"),
        yAxisTitle = cms.string("dN/d#Delta R^{b1lep}")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/bjet1_btagCSV"),
        xAxisTitle = cms.string("bjet1_btagCSV"),
        yAxisTitle = cms.string("dN/dbjet1_btagCSV")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/selLepton_type"),
        xAxisTitle = cms.string("selLepton_type"),
        yAxisTitle = cms.string("dN/dselLepton_type")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/m_HH_B2G_18_008"),
        xAxisTitle = cms.string("m_{HH} (B2G-18-008) [GeV]"),
        yAxisTitle = cms.string("dN/dm_{HH} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/mjj_highestpt"),
        xAxisTitle = cms.string("m_{jj}^{highestpt} [GeV]"),
        yAxisTitle = cms.string("dN/dm_{jj}^{highestpt} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/Hbb_lead_px"),
        xAxisTitle = cms.string("Hbb_lead_px"),
        yAxisTitle = cms.string("dN/dHbb_lead_px")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/Hbb_lead_e"),
        xAxisTitle = cms.string("Hbb_lead_e [GeV]"),
        yAxisTitle = cms.string("dN/dHbb_lead_e [1/GeV]")
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
