import FWCore.ParameterSet.Config as cms
import os

process = cms.PSet()

process.fwliteInput = cms.PSet(
    fileNames = cms.vstring(),
    #maxEvents = cms.int32(-1),
    maxEvents = cms.int32(110000),
    outputEvery = cms.uint32(100000)
)

process.fwliteOutput = cms.PSet(
    fileName = cms.string('analyzeMEM_hh_bb1l_signal.root')
)

process.analyzeMEM_hh_bb1l = cms.PSet(
    treeName = cms.string('Events'),

    process = cms.string('signal_ggf_nonresonant_hh_bbvv_sl'),
    histogramDir = cms.string('signal'),
    era = cms.string('2017'),

    hasLHE = cms.bool(True),
    apply_genWeight = cms.bool(True),

    branchName_electrons = cms.string('Electron'),
    branchName_muons = cms.string('Muon'),
    branchName_jets_ak4 = cms.string('Jet'),
    branchName_jets_ak8 = cms.string('FatJet'),
    branchName_subjets_ak8 = cms.string('SubJet'),
    branchName_jets_ak8LS = cms.string('FatJetAK8LSLoose'),
    branchName_subjets_ak8LS = cms.string('SubJetAK8LSLoose'),
    branchName_met = cms.string('MET'),
    branchName_vertex = cms.string('PV'),

    branchName_memOutput = cms.string('memObjects_hh_bb1l_lepFakeable_central'),
    branchName_memOutput_missingBJet = cms.string('memObjects_hh_bb1l_lepFakeable_missingBJet_central'),
    branchName_memOutput_missingHadWJet = cms.string('memObjects_hh_bb1l_lepFakeable_missingHadWJet_central'),
    #branchName_memOutput = cms.string(''),
    #branchName_memOutput_missingBJet = cms.string(''),
    #branchName_memOutput_missingHadWJet = cms.string(''),

    branchNames_genParticles = cms.PSet(
        # branches specific to HH->bbWW signal events
        branchName_genLeptons = cms.string('GenLep'),
        branchName_genNeutrinos = cms.string('GenNu'),
        branchName_genParticlesFromHiggs = cms.string('GenHiggsDaughters'),
        branchName_genWJets = cms.string('GenWZQuark'),
        
        # branches specific to tt+jets background events   
        branchName_genLeptonsFromTop = cms.string('GenLepFromTop'),
        branchName_genNeutrinosFromTop = cms.string('GenNuFromTop'),
        branchName_genBJetsFromTop = cms.string('GenBQuarkFromTop'),
        branchName_genWJetsFromTop = cms.string('GenQuarkFromTop'),
    ),

    jetCleaningByIndex = cms.bool(False),

    isDEBUG = cms.bool(False)
)

#inputFilePath = "/local/karl/ttHNtupleProduction/2017/2019Dec16_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_sm_hh_2b2v_sl/0000"
#maxInputFiles = 50
#zombie_files = []
#import os
#def getInputFiles(inputFilePath):
#    inputFiles = []
#    files_and_subdirectories = os.listdir(inputFilePath)
#    for file_or_subdirectory in files_and_subdirectories:
#        if file_or_subdirectory in zombie_files:
#            continue
#        file_or_subdirectory = os.path.join(inputFilePath, file_or_subdirectory)
#        if os.path.isfile(file_or_subdirectory):
#            if file_or_subdirectory.endswith(".root"):
#                inputFiles.append(file_or_subdirectory)
#        if os.path.isdir(file_or_subdirectory):
#            inputFiles.extend(getInputFiles(file_or_subdirectory))
#    return inputFiles
#inputFiles = getInputFiles(inputFilePath)
#process.fwliteInput.fileNames = cms.vstring(inputFiles[0:maxInputFiles])
inputFiles = [ 
  "/local/veelken/addMEM/2017/2020Feb27sl_default_nom/final_ntuples/hh_bb1l/signal_ggf_nonresonant_node_sm_hh_2b2v_sl/0000/signal_ggf_nonresonant_node_sm_hh_2b2v_sl_final.root"
]
process.fwliteInput.fileNames = cms.vstring(inputFiles)
print "inputFiles = ", process.fwliteInput.fileNames
