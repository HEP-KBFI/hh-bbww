import FWCore.ParameterSet.Config as cms

process = cms.PSet()

process.fwliteInput = cms.PSet(
    fileNames = cms.vstring(''),
    skipEvents = cms.uint32(0),
    maxEvents = cms.int32(-1),
    outputEvery = cms.uint32(1)
)

process.fwliteOutput = cms.PSet(
    fileName = cms.string('')
)

process.addMEM_hh_bb1l = cms.PSet(
    treeName = cms.string('Events'),

    era = cms.string(''),
    isMC = cms.bool(True),

    leptonSelection = cms.string(''),

    branchName_electrons = cms.string('Electron'),
    branchName_muons = cms.string('Muon'),
    branchName_jets_ak4 = cms.string('Jet'),
    branchName_jets_ak8 = cms.string('FatJet'),
    branchName_subjets_ak8 = cms.string('SubJet'),
    branchName_met = cms.string('MET'),

    copy_all_branches = cms.bool(True),
    copy_histograms = cms.vstring('Count.*'),

    selEventsFileName_input = cms.string(''),
    isDEBUG = cms.bool(False),
    readGenObjects = cms.bool(True),
    isForBDTtraining = cms.bool(False),

    central_or_shift = cms.vstring(),
    jetCleaningByIndex = cms.bool(True),
    useNonNominal = cms.bool(False),
    dryRun = cms.bool(False),
)
