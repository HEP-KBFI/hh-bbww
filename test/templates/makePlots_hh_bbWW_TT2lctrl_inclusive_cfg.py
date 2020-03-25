import FWCore.ParameterSet.Config as cms

from hhAnalysis.bbww.configs.makePlots_cfi import process

process.makePlots.processSignal = cms.string("")

process.makePlots.distributions = cms.VPSet(
    cms.PSet(
        histogramName = cms.string('sel/electron/$PROCESS/pt'),
        xMin = cms.double(25.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('e p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/electron/$PROCESS/eta'),
        xAxisTitle = cms.string('e #eta'),
        yAxisTitle = cms.string('dN/d#eta')
    ),
    cms.PSet(
        histogramName = cms.string('sel/muon/$PROCESS/pt'),
        xMin = cms.double(25.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('#mu p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/muon/$PROCESS/eta'),
        xAxisTitle = cms.string('#mu #eta'),
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
        histogramName = cms.string('sel/evt/$PROCESS/top_pt'),
        xAxisTitle = cms.string('p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/antiTop_pt'),
        xAxisTitle = cms.string('p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/m_ll'),
        xAxisTitle = cms.string('m_{ll} [GeV]'),
        yAxisTitle = cms.string('dN/dm_{ll} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/mtt'),
        xAxisTitle = cms.string('m_{tt} [GeV]'),
        yAxisTitle = cms.string('dN/dm_{tt} [1/GeV]')
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
        histogramName = cms.string("sel/triggers_1mu/$PROCESS/hltPathCounter"),
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
