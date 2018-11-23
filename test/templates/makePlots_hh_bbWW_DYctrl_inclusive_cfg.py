import FWCore.ParameterSet.Config as cms

from hhAnalysis.bbww.configs.makePlots_cfi import process

process.makePlots.processSignal = cms.string("")

process.makePlots.distributions = cms.VPSet(
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
        histogramName = cms.string("sel/evt/$PROCESS/m_bb"),
        xAxisTitle = cms.string("m_{bb} [GeV]"),
        yAxisTitle = cms.string("dN/dm_{bb} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/pT_bb"),
        xAxisTitle = cms.string("p_{T}^{bb} [GeV]"),
        yAxisTitle = cms.string("dN/p_{T}^{bb} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/dR_bb"),
        xAxisTitle = cms.string("#Delta R^{bb} [GeV]"),
        yAxisTitle = cms.string("dN/#Delta R^{bb} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string('sel/leadElectron/$PROCESS/pt'),
        xMin = cms.double(25.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('leading e p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/leadElectron/$PROCESS/eta'),
        xAxisTitle = cms.string('leading e #eta'),
        yAxisTitle = cms.string('dN/d#eta')
    ),
    cms.PSet(
        histogramName = cms.string('sel/subleadElectron/$PROCESS/pt'),
        xMin = cms.double(15.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('subleading e p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/subleadElectron/$PROCESS/eta'),
        xAxisTitle = cms.string('subleading e #eta'),
        yAxisTitle = cms.string('dN/d#eta')
    ),
    cms.PSet(
        histogramName = cms.string('sel/leadMuon/$PROCESS/pt'),
        xMin = cms.double(25.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('leading #mu p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/leadMuon/$PROCESS/eta'),
        xAxisTitle = cms.string('leading #mu #eta'),
        yAxisTitle = cms.string('dN/d#eta')
    ),
    cms.PSet(
        histogramName = cms.string('sel/subleadMuon/$PROCESS/pt'),
        xMin = cms.double(15.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('subleading #mu p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),    
    cms.PSet(
        histogramName = cms.string('sel/subleadMuon/$PROCESS/eta'),
        xAxisTitle = cms.string('subleading #mu #eta'),
        yAxisTitle = cms.string('dN/d#eta')
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/numJets"),
        xAxisTitle = cms.string("jet Multiplicity"),
        yAxisTitle = cms.string("Events")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/numBJets_loose"),
        xAxisTitle = cms.string("loose b-jet Multiplicity"),
        yAxisTitle = cms.string("Events")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/numBJets_medium"),
        xAxisTitle = cms.string("medium b-jet Multiplicity"),
        yAxisTitle = cms.string("Events")
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/HT'),
        xAxisTitle = cms.string('H_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dH_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string("sel/evtYield/$PROCESS/evtYield"),
        xAxisTitle = cms.string("Run Period"),
        yAxisTitle = cms.string("Events / 1 fb^{-1}")
    ),
    cms.PSet(
        histogramName = cms.string("sel/triggers_1e/$PROCESS/hltPathCounter"),
        xAxisTitle = cms.string("HLT Path"),
        yAxisTitle = cms.string("Events / 1 fb^{-1}")
    ),
    cms.PSet(
        histogramName = cms.string("sel/triggers_2e/$PROCESS/hltPathCounter"),
        xAxisTitle = cms.string("HLT Path"),
        yAxisTitle = cms.string("Events / 1 fb^{-1}")
    ),
    cms.PSet(
        histogramName = cms.string("sel/triggers_1mu/$PROCESS/hltPathCounter"),
        xAxisTitle = cms.string("HLT Path"),
        yAxisTitle = cms.string("Events / 1 fb^{-1}")
    ),
    cms.PSet(
        histogramName = cms.string("sel/triggers_2mu/$PROCESS/hltPathCounter"),
        xAxisTitle = cms.string("HLT Path"),
        yAxisTitle = cms.string("Events / 1 fb^{-1}")
    ),
    cms.PSet(
        histogramName = cms.string("sel/weights/$PROCESS/triggerWeight"),
        xAxisTitle = cms.string("Trigger SF"),
        yAxisTitle = cms.string("Events / 1 fb^{-1}")
    ),
)

process.makePlots.labelOnTop = cms.string("CMS Simulation")
