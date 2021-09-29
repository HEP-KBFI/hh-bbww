import logging
import re

from hhAnalysis.multilepton.configs.analyzeConfig_hh import *
from tthAnalysis.HiggsToTauTau.jobTools import create_if_not_exists
from tthAnalysis.HiggsToTauTau.analysisTools import initDict, getKey, create_cfg, createFile, generateInputFileList

def getHistogramDir(category, apply_jetSmearing, apply_metSmearing):
  histogramDir = category
  if apply_jetSmearing:
    histogramDir += "_jetSmearingEnabled"
  else:
    histogramDir += "_jetSmearingDisabled"
  if apply_metSmearing:
    histogramDir += "_metSmearingEnabled"
  else:
    histogramDir += "_metSmearingDisabled"  
  return histogramDir

class analyzeConfig_hh_bbwwMEM_singlelepton(analyzeConfig_hh):
  """Configuration metadata needed to run analysis in a single go.

  Sets up a folder structure by defining full path names; no directory creation is delegated here.

  Args specific to analyzeConfig_hh_bbwwMEM_singlelepton:
    None.

  See $CMSSW_BASE/src/tthAnalysis/HiggsToTauTau/python/analyzeConfig.py
  for documentation of further Args.

  """
  def __init__(self,
        configDir,
        outputDir,
        executable_analyze,
        cfgFile_analyze,
        samples,
        max_jobs_per_sample,
        apply_jetSmearing_options,
        apply_metSmearing_options,
        max_files_per_job,
        era,
        check_output_files,
        running_method,
        num_parallel_jobs,
        select_rle_output = False,
        verbose           = False,
        isDebug           = False,
        rle_select        = '',
        use_home          = True,
      ):
    analyzeConfig_hh.__init__(self,
      configDir             = configDir,
      outputDir             = outputDir,
      executable_analyze    = executable_analyze,
      channel               = "hh_bbwwMEM_singlelepton",
      samples               = samples,
      jet_cleaning_by_index = False,
      gen_matching_by_index = False,
      central_or_shifts     = [ "central" ],
      max_files_per_job     = max_files_per_job,
      era                   = era,
      use_lumi              = False,
      lumi                  = 1.,
      check_output_files    = check_output_files,
      running_method        = running_method,
      num_parallel_jobs     = num_parallel_jobs,
      histograms_to_fit     = [],
      triggers              = [],
      lep_mva_wp            = "hh_multilepton",
      verbose               = verbose,
      isDebug               = isDebug,
      use_home              = use_home,
      template_dir          = os.path.join(os.getenv('CMSSW_BASE'), 'src', 'hhAnalysis', 'bbwwMEMPerformanceStudies', 'test', 'templates')
    )
    self.max_jobs_per_sample = max_jobs_per_sample
    self.apply_jetSmearing_options = apply_jetSmearing_options
    self.apply_metSmearing_options = apply_metSmearing_options
    self.cfgFile_analyze = os.path.join(self.template_dir, cfgFile_analyze)
    self.select_rle_output = select_rle_output
    self.rle_select = rle_select
    self.evtCategory_inclusive = "hh_bbwwMEM_singlelepton"
    self.make_dependency_hadd_stage2 = "phony_hadd_stage1"

  def createCfg_analyze(self, jobOptions, sample_info):
    """Create python configuration file for the analyze_hh_bbwwMEM_singlelepton executable (analysis code)

    Args:
      inputFiles: list of input files (Ntuples)
      outputFile: output file of the job -- a ROOT file containing histogram
      process: either `TT` or `signal`
    """

    jobOptions['histogramDir'] = getHistogramDir(self.evtCategory_inclusive, jobOptions['apply_jetSmearing'], jobOptions['apply_metSmearing'])
    lines = super(analyzeConfig_hh_bbwwMEM_singlelepton, self).createCfg_analyze(jobOptions, sample_info,
      additionalJobOptions = [ "apply_jetSmearing", "apply_metSmearing", "maxSelEvents", "skipSelEvents" ])
    create_cfg(self.cfgFile_analyze, jobOptions['cfgFile_modified'], lines)

  def create(self):
    """Creates all necessary config files and runs the complete analysis workfow -- either locally or on the batch system
    """
    for sample_name, sample_info in self.samples.items():
      if not sample_info["use_it"]:
        continue
      process_name = sample_info["process_name_specific"]
      key_dir = getKey(process_name)
      for dir_type in [ DKEY_CFGS, DKEY_HIST, DKEY_LOGS, DKEY_RLES, DKEY_SYNC ]:
        initDict(self.dirs, [ key_dir, dir_type ])
        if dir_type in [ DKEY_CFGS, DKEY_LOGS ]:
          self.dirs[key_dir][dir_type] = os.path.join(self.configDir, dir_type, self.channel, process_name)
        else:
          self.dirs[key_dir][dir_type] = os.path.join(self.outputDir, dir_type, self.channel, process_name)
    for dir_type in [ DKEY_CFGS, DKEY_SCRIPTS, DKEY_HIST, DKEY_LOGS, DKEY_DCRD, DKEY_PLOT, DKEY_HADD_RT, DKEY_SYNC ]:
      initDict(self.dirs, [ dir_type ])
      if dir_type in [ DKEY_CFGS, DKEY_SCRIPTS, DKEY_LOGS, DKEY_DCRD, DKEY_PLOT, DKEY_HADD_RT ]:
        self.dirs[dir_type] = os.path.join(self.configDir, dir_type, self.channel)
      else:
        self.dirs[dir_type] = os.path.join(self.outputDir, dir_type, self.channel)
    for key in self.dirs.keys():
      if type(self.dirs[key]) == dict:
        for dir_type in self.dirs[key].keys():
          create_if_not_exists(self.dirs[key][dir_type])
      else:
        create_if_not_exists(self.dirs[key])

    inputFileLists = {}
    for sample_name, sample_info in self.samples.items():
      if not sample_info["use_it"]:
        continue
      logging.info("Checking input files for sample %s" % sample_info["process_name_specific"])
      inputFileLists[sample_name] = generateInputFileList(sample_info, self.max_files_per_job)

    for apply_jetSmearing in self.apply_jetSmearing_options:
      jetSmearingLabel = None
      if apply_jetSmearing:
        jetSmearingLabel = "jetSmearingEnabled"
      else:
        jetSmearingLabel = "jetSmearingDisabled"
      for apply_metSmearing in self.apply_metSmearing_options:
        metSmearingLabel = None
        if apply_metSmearing:
          metSmearingLabel = "metSmearingEnabled"
        else:
          metSmearingLabel = "metSmearingDisabled"
        for sample_name, sample_info in self.samples.items():
          if not sample_info["use_it"]:
            continue
          process_name = sample_info["process_name_specific"]
          isSignal = True if process_name.find("signal") != -1 else False
          logging.info("Creating configuration files to run '%s' for sample %s" % (self.executable_analyze, process_name))
          sample_category = sample_info["sample_category"]

          inputFileList = inputFileLists[sample_name]
          numJobsPerFile = None
          if   sample_info["process_name_specific"] == "signal_ggf_nonresonant_node_sm_hh_2b2v_sl_PSWeights":
            numJobsPerFile = 1000
          elif sample_info["process_name_specific"] == "signal_ggf_nonresonant_cHHH1_hh_2b2v_sl":
            numJobsPerFile = 400
          elif sample_info["process_name_specific"] == "TTJets_SingleLeptFromT" or \
               sample_info["process_name_specific"] == "TTJets_SingleLeptFromTbar":
            numJobsPerFile = 100
          elif sample_info["process_name_specific"] == "TTJets_SingleLeptFromT_ext1" or \
               sample_info["process_name_specific"] == "TTJets_SingleLeptFromTbar_ext1":
            numJobsPerFile = 100
          elif sample_info["process_name_specific"] == "TTToSemiLeptonic": 
            numJobsPerFile = 20
          else:
            raise ValueError("Invalid sample: %s" % sample_info["process_name_specific"])
          numJobs = numJobsPerFile*len(inputFileList.keys())
          if numJobs > self.max_jobs_per_sample:
            print("Processing of full sample would require submission of %i jobs. Restricting the number of jobs to %i." % (numJobs, self.max_jobs_per_sample))
            numJobs = self.max_jobs_per_sample
          for jobId in range(1, numJobs + 1):
            
            ntupleId = ((jobId - 1)/numJobsPerFile) + 1
            maxSelEvents = 250
            skipSelEvents = maxSelEvents*((jobId - 1) % numJobsPerFile)

            # build config files for executing analysis code
            key_dir = getKey(process_name)
            key_analyze_job = getKey(process_name, jetSmearingLabel, metSmearingLabel, jobId)
            ntupleFiles = inputFileList[ntupleId]
            if len(ntupleFiles) == 0:
              logging.warning("No input ntuples for %s --> skipping job !!" % (key_analyze_job))
              continue

            cfgFile_modified_path = os.path.join(self.dirs[key_dir][DKEY_CFGS], "analyze_%s_%s_%s_%s_%i_cfg.py" % (self.channel, process_name, jetSmearingLabel, metSmearingLabel, jobId))
            histogramFile_path = os.path.join(self.dirs[key_dir][DKEY_HIST], "analyze_%s_%s_%s_%s_%i.root" % (self.channel, process_name, jetSmearingLabel, metSmearingLabel, jobId))
            logFile_path = os.path.join(self.dirs[key_dir][DKEY_LOGS], "analyze_%s_%s_%s_%s_%i.log" % (self.channel, process_name, jetSmearingLabel, metSmearingLabel, jobId))
            rleOutputFile_path = os.path.join(self.dirs[key_dir][DKEY_RLES], "rle_%s_%s_%s_%s_%i.txt" % (self.channel, process_name, jetSmearingLabel, metSmearingLabel, jobId)) \
                                 if self.select_rle_output else ""
            self.jobOptions_analyze[key_analyze_job] = {
              'ntupleFiles'              : ntupleFiles,
              'cfgFile_modified'         : cfgFile_modified_path,
              'histogramFile'            : histogramFile_path,
              'logFile'                  : logFile_path,
              'selEventsFileName_output' : rleOutputFile_path,
              'apply_jetSmearing'        : apply_jetSmearing,
              'apply_metSmearing'        : apply_metSmearing,
              'maxSelEvents'             : maxSelEvents,
              'skipSelEvents'            : skipSelEvents
            }
            self.createCfg_analyze(self.jobOptions_analyze[key_analyze_job], sample_info)

            # initialize input and output file names for hadd_stage1
            key_hadd_stage1 = getKey(process_name, jetSmearingLabel, metSmearingLabel)
            if not key_hadd_stage1 in self.inputFiles_hadd_stage1:
              self.inputFiles_hadd_stage1[key_hadd_stage1] = []
            self.inputFiles_hadd_stage1[key_hadd_stage1].append(self.jobOptions_analyze[key_analyze_job]['histogramFile'])
            self.outputFile_hadd_stage1[key_hadd_stage1] = os.path.join(self.dirs[DKEY_HIST], "histograms_harvested_stage1_%s_%s_%s_%s.root" % \
              (self.channel, process_name, jetSmearingLabel, metSmearingLabel))

          # add output files of hadd_stage1 to list of input files for hadd_stage2
          key_hadd_stage1 = getKey(process_name, jetSmearingLabel, metSmearingLabel)
          key_hadd_stage2 = getKey("")
          if not key_hadd_stage2 in self.inputFiles_hadd_stage2:
            self.inputFiles_hadd_stage2[key_hadd_stage2] = []
          self.inputFiles_hadd_stage2[key_hadd_stage2].append(self.outputFile_hadd_stage1[key_hadd_stage1])
          self.outputFile_hadd_stage2[key_hadd_stage2] = os.path.join(self.dirs[DKEY_HIST], "histograms_harvested_stage2_%s.root" % self.channel)

    if self.is_sbatch:
      logging.info("Creating script for submitting '%s' jobs to batch system" % self.executable_analyze)
      self.sbatchFile_analyze = os.path.join(self.dirs[DKEY_SCRIPTS], "sbatch_analyze_%s.py" % self.channel)
      self.createScript_sbatch_analyze(self.executable_analyze, self.sbatchFile_analyze, self.jobOptions_analyze)

    logging.info("Creating Makefile")
    lines_makefile = []
    self.addToMakefile_analyze(lines_makefile)
    self.addToMakefile_hadd_stage1(lines_makefile)
    self.addToMakefile_hadd_stage2(lines_makefile)
    self.targets.extend(self.outputFile_hadd_stage2.values())
    self.createMakefile(lines_makefile)

    logging.info("Done")

    return self.num_jobs
