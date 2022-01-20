from hhAnalysis.multilepton.configs.analyzeConfig_hh import *

from tthAnalysis.HiggsToTauTau.jobTools import create_if_not_exists
from tthAnalysis.HiggsToTauTau.analysisTools import initDict, getKey, create_cfg, createFile, generateInputFileList
from tthAnalysis.HiggsToTauTau.common import logging
from hhAnalysis.multilepton.common import is_nonresonant

import re
import collections
import copy

class analyzeConfig_HHatLOvsNLO(analyzeConfig_hh):
  """Configuration metadata needed to run analysis in a single go.

  Sets up a folder structure by defining full path names; no directory creation is delegated here.

  Args specific to analyzeConfig_HHatLOvsNLO:
    None.

  See $CMSSW_BASE/src/tthAnalysis/HiggsToTauTau/python/analyzeConfig.py
  for documentation of further Args.

  """
  def __init__(self,
        configDir,
        localDir,
        outputDir,
        executable_analyze,
        cfgFile_analyze,
        samples,
        max_files_per_job,
        era,
        use_lumi,
        lumi,
        check_output_files,
        running_method,
        num_parallel_jobs,
        verbose           = False,
        dry_run           = False,
        do_sync           = False,
        isDebug           = False,
        use_home          = False,
        keep_logs         = False,
        submission_cmd    = None,
      ):
    analyzeConfig_hh.__init__(self,
      configDir             = configDir,
      localDir              = localDir,
      outputDir             = outputDir,
      executable_analyze    = executable_analyze,
      channel               = "hh_HHatLOvsNLO",
      samples               = samples,
      jet_cleaning_by_index = None,
      gen_matching_by_index = None,
      central_or_shifts     = [ "central", ],
      max_files_per_job     = max_files_per_job,
      era                   = era,
      use_lumi              = use_lumi,
      lumi                  = lumi,
      check_output_files    = check_output_files,
      running_method        = running_method,
      num_parallel_jobs     = num_parallel_jobs,
      histograms_to_fit     = None,
      triggers              = [],
      verbose               = verbose,
      dry_run               = dry_run,
      isDebug               = isDebug,
      use_home              = use_home,
      keep_logs             = keep_logs,
      template_dir          = os.path.join(os.getenv('CMSSW_BASE'), 'src', 'hhAnalysis', 'bbww', 'test', 'templates'),
      submission_cmd        = submission_cmd,
    )

    self.cfgFile_analyze = os.path.join(self.template_dir, cfgFile_analyze)
    self.inputFiles_hadd_stage2 = {}
    self.outputFile_hadd_stage2 = {}

  def createCfg_analyze(self, jobOptions, sample_info):
    """Create python configuration file for the analyze_HHatLOvsNLO executable (analysis code)

    Args:
      inputFiles: list of input files (Ntuples)
      outputFile: output file of the job -- a ROOT file containing histogram
      process: either `TT`, `TTW`, `TTZ`, `EWK`, `Rares`, `data_obs`, or `signal`
      is_mc: flag indicating whether job runs on MC (True) or data (False)
      lumi_scale: event weight (= xsection * luminosity / number of events)
      central_or_shift: either 'central' or one of the systematic uncertainties defined in $CMSSW_BASE/src/hhAnalysis/multilepton/bin/analyze_hh_bb2l.cc
    """

    jobOptions['histogramDir'] = "analyze_HHatLOvsNLO"

    if is_nonresonant(sample_info["sample_category"]) or self.do_sync:
      jobOptions['hhWeight_cfg.denominator_file'] = 'hhAnalysis/bbww/data/denom_{}{}.root'.format(self.era, '_sync' if self.do_sync else '')
      jobOptions['hhWeight_cfg.histtitle'] = sample_info["sample_category"]

    lines = super(analyzeConfig_HHatLOvsNLO, self).createCfg_analyze(jobOptions, sample_info)
    create_cfg(self.cfgFile_analyze, jobOptions['cfgFile_modified'], lines)

  def create(self):
    """Creates all necessary config files and runs the complete analysis workfow -- either locally or on the batch system
    """
    for sample_name, sample_info in self.samples.items():
      if not sample_info["use_it"]:
        continue

      sample_category = sample_info["sample_category"]
      is_mc = (sample_info["type"] == "mc")
      process_name = sample_info["process_name_specific"]

      logging.info("Building dictionaries for sample %s..." % process_name)
      central_or_shifts_extended = [ "", "hadd" ]
      for central_or_shift_or_dummy in central_or_shifts_extended:
        process_name_extended = [ process_name, "hadd" ]
        for process_name_or_dummy in process_name_extended:
          if process_name_or_dummy in [ "hadd" ] and central_or_shift_or_dummy != "":
            continue
          key_dir = getKey(process_name_or_dummy, central_or_shift_or_dummy)
          for dir_type in [ DKEY_CFGS, DKEY_HIST, DKEY_LOGS ]:
            initDict(self.dirs, [ key_dir, dir_type ])
            if dir_type in [ DKEY_CFGS, DKEY_LOGS ]:
              self.dirs[key_dir][dir_type] = os.path.join(self.get_dir_type(dir_type), dir_type, self.channel,
                                                          process_name_or_dummy)
            else :
              self.dirs[key_dir][dir_type] = os.path.join(self.outputDir, dir_type, self.channel,
                                                          process_name_or_dummy)
    key_dir = "hadd"
    for dir_type in [ DKEY_CFGS, DKEY_SCRIPTS, DKEY_HIST, DKEY_LOGS, DKEY_DCRD, DKEY_HADD_RT ]:
      initDict(self.dirs, [ key_dir, dir_type ])
      if dir_type in [ DKEY_CFGS, DKEY_SCRIPTS, DKEY_LOGS, DKEY_DCRD, DKEY_HADD_RT ]:
        self.dirs[dir_type] = os.path.join(self.get_dir_type(dir_type), dir_type, self.channel)
      else:
        self.dirs[dir_type] = os.path.join(self.outputDir, dir_type, self.channel)

    numDirectories = 0
    for key in self.dirs.keys():
      if type(self.dirs[key]) == dict:
        numDirectories += len(self.dirs[key])
      else:
        numDirectories += 1
    logging.info("Creating directory structure (numDirectories = %i)" % numDirectories)
    numDirectories_created = 0;
    frac = 1
    for key in self.dirs.keys():
      if type(self.dirs[key]) == dict:
        for dir_type in self.dirs[key].keys():
          create_if_not_exists(self.dirs[key][dir_type])
        numDirectories_created += len(self.dirs[key])
      else:
        create_if_not_exists(self.dirs[key])
        numDirectories_created = numDirectories_created + 1
      while 100*numDirectories_created >= frac*numDirectories:
        logging.info(" %i%% completed" % frac)
        frac = frac + 1
    logging.info("Done.")

    inputFileLists = {}
    for sample_name, sample_info in self.samples.items():
      if not sample_info["use_it"]:
        continue
      logging.info("Checking input files for sample %s" % sample_info["process_name_specific"])
      inputFileLists[sample_name] = generateInputFileList(sample_info, self.max_files_per_job)

    for sample_name, sample_info in self.samples.items():
      if not sample_info["use_it"]:
        continue
      for sumHH_lo_option in [ "sumBMs", "singleBM" ]: 
        if "cHHH" in sample_info["sample_category"] and sumHH_lo_option == "sumBMs":
          continue

        process_name = sample_info["process_name_specific"]
        logging.info("Creating configuration files to run '%s' for sample %s" % (self.executable_analyze, process_name))
        inputFileList = inputFileLists[sample_name]

        sample_info_tmp = copy.deepcopy(sample_info)
        if sumHH_lo_option == "singleBM" and not "cHHH" in sample_info_tmp["sample_category"]:
          for bmName in [ "node_sm", "node_1", "node_2", "node_3", "node_4", "node_5", "node_6", "node_7", "node_8", "node_9", "node_10", "node_11", "node_12" ]:
            if bmName in process_name:
              sample_category = "%s_%s" % (sample_info["sample_category"], bmName)
              sample_info_tmp["sample_category"] = sample_category
        
        sample_category = sample_info["sample_category"]
        is_mc = (sample_info["type"] == "mc")

        # build config files for executing analysis code
        key_analyze_dir = getKey(process_name)
  
        for jobId in inputFileList.keys():

          analyze_job_tuple = (process_name, sumHH_lo_option, jobId)
          key_analyze_job = getKey(*analyze_job_tuple)
          ntupleFiles = inputFileList[jobId]
          if len(ntupleFiles) == 0:
            logging.warning("No input ntuples for %s --> skipping job !!" % (key_analyze_job))
            continue

          cfgFile_modified_path = os.path.join(self.dirs[key_analyze_dir][DKEY_CFGS], "analyze_%s_%s_%i_cfg.py" % analyze_job_tuple)
          logFile_path = os.path.join(self.dirs[key_analyze_dir][DKEY_LOGS], "analyze_%s_%s_%i.log" % analyze_job_tuple)
          histogramFile_path = os.path.join(self.dirs[key_analyze_dir][DKEY_HIST], "analyze_%s_%s_%i.root" % analyze_job_tuple)
          save_dXsec_HHWeightInterfaceNLO = (sumHH_lo_option == "singleBM" and sample_info["sample_category"] == "signal_ggf_nonresonant_cHHH1_hh_bbvv" and jobId == 0)
          self.jobOptions_analyze[key_analyze_job] = {
            'ntupleFiles'                     : ntupleFiles,
            'cfgFile_modified'                : cfgFile_modified_path,
            'histogramFile'                   : histogramFile_path,
            'logFile'                         : logFile_path,
            'process'                         : sample_info_tmp["sample_category"],
            'process_hh'                      : sample_info['sample_category_hh'].replace(sample_info["sample_category"], sample_info_tmp["sample_category"]),
            'hhWeight_cfg.apply_rwgt_lo'      : sumHH_lo_option == "sumBMs",
            'save_dXsec_HHWeightInterfaceNLO' : save_dXsec_HHWeightInterfaceNLO,
          }
          self.createCfg_analyze(self.jobOptions_analyze[key_analyze_job], sample_info_tmp)

          # initialize input and output file names for hadd_stage1
          key_hadd_stage1_dir = getKey(process_name, "hadd")
          hadd_stage1_job_tuple = (process_name, sumHH_lo_option)
          key_hadd_stage1_job = getKey("hadd_stage1", *hadd_stage1_job_tuple)
          if not key_hadd_stage1_job in self.inputFiles_hadd_stage1:
            self.inputFiles_hadd_stage1[key_hadd_stage1_job] = []
          self.inputFiles_hadd_stage1[key_hadd_stage1_job].append(self.jobOptions_analyze[key_analyze_job]['histogramFile'])
          self.outputFile_hadd_stage1[key_hadd_stage1_job] = os.path.join(self.dirs[key_hadd_stage1_dir][DKEY_HIST],
                                                                          "hadd_stage1_%s_%s.root" % hadd_stage1_job_tuple)

          # add output files of hadd_stage1 jobs to list of input files for hadd_stage2
          key_hadd_stage2_dir = getKey("hadd")
          key_hadd_stage2_job = getKey("hadd_stage2")
          if not key_hadd_stage2_job in self.inputFiles_hadd_stage2:
            self.inputFiles_hadd_stage2[key_hadd_stage2_job] = []
          self.inputFiles_hadd_stage2[key_hadd_stage2_job].append(self.outputFile_hadd_stage1[key_hadd_stage1_job])
          self.outputFile_hadd_stage2[key_hadd_stage2_job] = os.path.join(self.dirs[key_hadd_stage2_dir][DKEY_HIST],
                                                                          "hadd_stage2.root")

    if self.is_sbatch:
      logging.info("Creating script for submitting '%s' jobs to batch system" % self.executable_analyze)
      self.sbatchFile_analyze = os.path.join(self.dirs[DKEY_SCRIPTS], "sbatch_analyze_%s.py" % self.channel)
      self.createScript_sbatch_analyze(self.executable_analyze, self.sbatchFile_analyze, self.jobOptions_analyze)

    logging.info("Creating Makefile")
    lines_makefile = []
    self.addToMakefile_analyze(lines_makefile)
    self.addToMakefile_hadd_stage1(lines_makefile)
    self.addToMakefile_hadd_stage2(lines_makefile, make_dependency = "phony_hadd_stage1")
    self.targets.extend([ "phony_hadd_stage2", ])
    ##self.addToMakefile_validate(lines_makefile)
    self.createMakefile(lines_makefile)

    logging.info("Done.")

    return self.num_jobs
