import os

from tthAnalysis.HiggsToTauTau.configs.addMEMConfig import *
from tthAnalysis.HiggsToTauTau.analysisTools import create_cfg

class addMEMConfig_hh_bb1l(addMEMConfig):

  def __init__(self,
        treeName,
        outputDir,
        cfgDir,
        executable_addMEM,
        samples,
        era,
        check_output_files,
        leptonSelection,
        running_method,
        max_files_per_job,
        mem_integrations_per_job,
        max_mem_integrations,
        max_jobs_per_sample,
        num_parallel_jobs,
        isDebug,
        central_or_shift,
        lep_mva_wp,
        jet_cleaning_by_index,
        dry_run,
        use_nonnominal,
        use_home,
        method_mem,
        submission_cmd = None,
        pool_id = '',
      ):
    addMEMConfig.__init__(self,
      treeName                 = treeName,
      outputDir                = outputDir,
      cfgDir                   = cfgDir,
      executable_addMEM        = executable_addMEM,
      samples                  = samples,
      era                      = era,
      check_output_files       = check_output_files,
      running_method           = running_method,
      max_files_per_job        = max_files_per_job,
      mem_integrations_per_job = mem_integrations_per_job,
      max_mem_integrations     = max_mem_integrations,
      max_jobs_per_sample      = max_jobs_per_sample,
      num_parallel_jobs        = num_parallel_jobs,
      leptonSelection          = leptonSelection,
      hadTauSelection          = "undefined|undefined",
      jet_cleaning_by_index    = jet_cleaning_by_index,
      integration_choice       = '',
      dry_run                  = dry_run,
      use_nonnominal           = use_nonnominal,
      use_home                 = use_home,
      channel                  = "hh_bb1l",
      lep_mva_wp               = lep_mva_wp,
      submission_cmd           = submission_cmd,
      pool_id                  = pool_id,
    )

    self.template_dir = os.path.join(
      os.getenv('CMSSW_BASE'), 'src', 'hhAnalysis', 'bbww', 'test', 'templates'
    )
    logging.info("Templates directory is: {templateDir}".format(templateDir = self.template_dir))
    self.cfgFile_addMEM_original = os.path.join(self.template_dir, "addMEM_hh_bb1l_cfg.py")
    #self.maxPermutations_branchName = "maxPermutations_addMEM_%s_lep%s" % (self.channel, self.leptonSelection)
    #print("WARNING: Temporarily using maxPermutations_branchName = '%s' for DEBUGging purposes. This is not the correct branch !!" % self.maxPermutations_branchName)
    self.maxPermutations_branchName = ""
    print("WARNING: Temporarily setting maxPermutations_branchName = '' for DEBUGging purposes. This may significantly increase the computing time per job !!")
    self.isDebug = isDebug
    self.central_or_shift = central_or_shift
    self.method_mem = method_mem

  def createCfg_addMEM(self, inputFiles, startRange, endRange, outputFile, era, process, isMC, cfgFile_modified, whitelist = []):
    """Create python configuration file for the addMEM_hh_bb1l executable (MEM code)

    Args:
      inputFile: list of input files (Ntuples)
      outputFile: output file of the job
    """

    '''Let's assume that the following configuration options remain constant at all times and need not be modified
    - process.fwliteInput.outputEvery
    - process.addMEM_hh_bb1l.branchName_electrons
    - process.addMEM_hh_bb1l.branchName_muons
    - process.addMEM_hh_bb1l.branchName_jets_ak4
    - process.addMEM_hh_bb1l.branchName_jets_ak8
    - process.addMEM_hh_bb1l.branchName_subjets_ak8
    - process.addMEM_hh_bb1l.branchName_jets
    - process.addMEM_hh_bb1l.branchName_met
    '''

    lines = []
    skipEvents = startRange
    maxEvents = endRange - startRange
    lines.append("process.fwliteInput.fileNames = cms.vstring(%s)" % inputFiles)
    lines.append("process.fwliteInput.skipEvents = cms.uint32(%s)" % skipEvents)
    lines.append("process.fwliteInput.maxEvents = cms.int32(%s)" % maxEvents)
    lines.append("process.fwliteOutput.fileName = cms.string('%s')" % os.path.basename(outputFile))
    lines.append("process.addMEM_hh_bb1l.era = cms.string('%s')" % era)
    if skipEvents > 0:
      lines.append("process.addMEM_hh_bb1l.copy_histograms = cms.vstring()")
    lines.append("process.addMEM_hh_bb1l.leptonSelection = cms.string('%s')" % self.leptonSelection)
    lines.append("process.addMEM_hh_bb1l.process = cms.string('%s')" % process)
    lines.append("process.addMEM_hh_bb1l.isMC = cms.bool(%s)" % isMC)
    lines.append("process.addMEM_hh_bb1l.isDEBUG = cms.bool(%s)" % self.isDebug)
    lines.append("process.addMEM_hh_bb1l.central_or_shift_mem = cms.vstring(%s)" % self.central_or_shift)
    lines.append("process.addMEM_hh_bb1l.dryRun = cms.bool(%s)" % self.dry_run)
    lines.append("process.addMEM_hh_bb1l.useNonNominal = cms.bool(%s)" % self.use_nonnominal)
    lines.append("process.addMEM_hh_bb1l.method_mem = cms.bool(%s)" % self.method_mem)
    lines.append("process.addMEM_hh_bb1l.branchName_maxPermutations_addMEM = cms.string('%s')" % self.maxPermutations_branchName)
    lines.append("process.addMEM_hh_bb1l.lep_mva_wp = cms.string('%s')" % self.lep_mva_wp)
    lines.append("process.addMEM_hh_bb1l.lep_mva_cut_mu = cms.double(%s)" % self.lep_mva_cut_mu)
    lines.append("process.addMEM_hh_bb1l.lep_mva_cut_e = cms.double(%s)" % self.lep_mva_cut_e)

    create_cfg(self.cfgFile_addMEM_original, cfgFile_modified, lines)
