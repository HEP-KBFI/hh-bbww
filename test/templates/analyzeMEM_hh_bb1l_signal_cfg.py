import FWCore.ParameterSet.Config as cms
import os

process = cms.PSet()

process.fwliteInput = cms.PSet(
    fileNames = cms.vstring(),
    maxEvents = cms.int32(-1),
    outputEvery = cms.uint32(100000)
)

process.fwliteOutput = cms.PSet(
    fileName = cms.string('analyzeMEM_hh_bb1l_signal.root')
)

process.analyzeMEM_hh_bb1l = cms.PSet(
    treeName = cms.string('Events'),

    process = cms.string('signal_ggf_nonresonant_node_sm_hh_2b2v'),
    histogramDir = cms.string('signal'),
    era = cms.string('2017'),

    apply_genWeight = cms.bool(True),

    branchName_electrons = cms.string('Electron'),
    branchName_muons = cms.string('Muon'),
    branchName_jets_ak4 = cms.string('Jet'),
    branchName_jets_ak8_Hbb = cms.string('FatJet'),
    branchName_subjets_ak8_Hbb = cms.string('SubJet'),
    branchName_jets_ak8_Wjj = cms.string('FatJetAK8LSLoose'),
    branchName_subjets_ak8_Wjj = cms.string('SubJetAK8LSLoose'),
    branchName_met = cms.string('MET'),

    branchName_memOutput = cms.string('memObjects_hh_bb1l_lepTight'),
    branchName_memOutput_missingBJet = cms.string('memObjects_hh_bb1l_lepTight_missingBJet'),
    branchName_memOutput_missingHadWJet = cms.string('memObjects_hh_bb1l_lepTight_missingHadWJet'),
    branchName_memOutput_missingBJet_and_HadWJet = cms.string('memObjects_hh_bb1l_lepTight_missingBJet_and_HadWJet'),

    branchName_genLeptons = cms.string('GenLep'),
    branchName_genBJets = cms.string('GenHiggsDaughters'), 
    branchName_genWJets = cms.string('GenWZQuark'),

    isDEBUG = cms.bool(False)
)

inputFilePath = "/hdfs/local/veelken/addMEM/2017/DEBUG_default_nom/ntuples/hh_bb1l/signal_ggf_nonresonant_node_sm_hh_2b2v"
maxInputFiles = 50
zombie_files = []
import os
def getInputFiles(inputFilePath):
    inputFiles = []
    files_and_subdirectories = os.listdir(inputFilePath)
    for file_or_subdirectory in files_and_subdirectories:
        if file_or_subdirectory in zombie_files:
            continue
        file_or_subdirectory = os.path.join(inputFilePath, file_or_subdirectory)
        if os.path.isfile(file_or_subdirectory):
            if file_or_subdirectory.endswith(".root"):
                inputFiles.append(file_or_subdirectory)
        if os.path.isdir(file_or_subdirectory):
            inputFiles.extend(getInputFiles(file_or_subdirectory))
    return inputFiles
inputFiles = getInputFiles(inputFilePath)
process.fwliteInput.fileNames = cms.vstring(inputFiles[0:maxInputFiles])
print "inputFiles = ", process.fwliteInput.fileNames
