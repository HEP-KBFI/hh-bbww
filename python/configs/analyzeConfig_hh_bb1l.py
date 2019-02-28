import logging
import re

from hhAnalysis.multilepton.configs.analyzeConfig_hh import *
from tthAnalysis.HiggsToTauTau.jobTools import create_if_not_exists
from tthAnalysis.HiggsToTauTau.analysisTools import initDict, getKey, create_cfg, createFile, generateInputFileList

def get_lepton_selection_and_frWeight(lepton_selection, lepton_frWeight):
  lepton_selection_and_frWeight = lepton_selection
  if lepton_selection.startswith("Fakeable"):
    if lepton_frWeight == "enabled":
      lepton_selection_and_frWeight += "_wFakeRateWeights"
    elif lepton_frWeight == "disabled":
      lepton_selection_and_frWeight += "_woFakeRateWeights"
  lepton_selection_and_frWeight = lepton_selection_and_frWeight.replace("|", "_")
  return lepton_selection_and_frWeight

def getHistogramDir(category, lepton_selection, lepton_frWeight):
  histogramDir = category
  histogramDir += "_%s" % lepton_selection
  if lepton_selection.find("Fakeable") != -1:
    if lepton_frWeight == "enabled":
      histogramDir += "_wFakeRateWeights"
    elif lepton_frWeight == "disabled":
      histogramDir += "_woFakeRateWeights"
  return histogramDir

class analyzeConfig_hh_bb1l(analyzeConfig_hh):
  """Configuration metadata needed to run analysis in a single go.

  Sets up a folder structure by defining full path names; no directory creation is delegated here.

  Args specific to analyzeConfig_hh_bb1l:
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
        lep_mva_wp,
        apply_hadTauVeto,
        hadTau_mva_wp_veto,
        applyFakeRateWeights,
        central_or_shifts,
        evtCategories,              
        max_files_per_job,
        era,
        use_lumi,
        lumi,
        check_output_files,
        running_method,
        num_parallel_jobs,
        executable_addBackgrounds,
        executable_addFakes,
        histograms_to_fit,
        select_rle_output = False,
        verbose           = False,
        dry_run           = False,
        isDebug           = False,
        use_nonnominal    = False,
        hlt_filter        = False,
        use_home          = True,
      ):
    analyzeConfig_hh.__init__(self,
      configDir          = configDir,
      outputDir          = outputDir,
      executable_analyze = executable_analyze,
      channel            = "hh_bb1l",
      samples            = samples,
      central_or_shifts  = central_or_shifts,
      max_files_per_job  = max_files_per_job,
      era                = era,
      use_lumi           = use_lumi,
      lumi               = lumi,
      check_output_files = check_output_files,
      running_method     = running_method,
      num_parallel_jobs  = num_parallel_jobs,
      histograms_to_fit  = histograms_to_fit,
      triggers           = [ '1e', '1mu', '2e', '2mu', '1e1mu' ],
      lep_mva_wp         = lep_mva_wp,
      verbose            = verbose,
      dry_run            = dry_run,
      isDebug            = isDebug,
      use_home           = use_home,
      template_dir       = os.path.join(os.getenv('CMSSW_BASE'), 'src', 'hhAnalysis', 'bbww', 'test', 'templates')
    )

    self.lepton_selections = [ "Tight", "Fakeable" ]
    self.lepton_frWeights = [ "enabled", "disabled" ]
    self.apply_hadTauVeto = apply_hadTauVeto
    self.hadTau_mva_wp_veto = hadTau_mva_wp_veto
    self.applyFakeRateWeights = applyFakeRateWeights
    run_mcClosure = 'central' not in self.central_or_shifts or len(central_or_shifts) > 1 or self.do_sync
    if self.era != '2017':
      logging.warning('mcClosure for lepton FR not possible for era %s' % self.era)
      run_mcClosure = False
    if run_mcClosure:
      # Run MC closure jobs only if the analysis is run w/ (at least some) systematic uncertainties
      #self.lepton_selections.extend([ "Fakeable_mcClosure_all" ]) #TODO
      pass

    self.lepton_genMatches = [ "1l0g0j", "0l1g0j", "0l0g1j" ]

    self.apply_leptonGenMatching = True
    self.lepton_genMatches_nonfakes = []
    self.lepton_genMatches_conversions = []
    self.lepton_genMatches_fakes = []
    for lepton_genMatch in self.lepton_genMatches:
      if lepton_genMatch.endswith("0g0j"):
        self.lepton_genMatches_nonfakes.append(lepton_genMatch)
      elif lepton_genMatch.endswith("0j"):
        self.lepton_genMatches_conversions.append(lepton_genMatch)
      else:
        self.lepton_genMatches_fakes.append(lepton_genMatch)
    if run_mcClosure:
      self.lepton_selections.extend([ "Fakeable_mcClosure_e", "Fakeable_mcClosure_m" ])

    self.executable_addBackgrounds = executable_addBackgrounds
    self.executable_addFakes = executable_addFakes

    self.nonfake_backgrounds = [ "ZZ", "WZ", "WW", "TT", "TTW", "TTWW", "TTZ", "DY", "W", "Other", "VH", "TTH", "TH" ]

    self.cfgFile_analyze = os.path.join(self.template_dir, cfgFile_analyze)
    self.prep_dcard_processesToCopy = [ "data_obs" ] + self.nonfake_backgrounds + [ "conversions", "fakes_data", "fakes_mc" ]
    self.prep_dcard_signals = []
    for sample_name, sample_info in self.samples.items():
      if not sample_info["use_it"]:
        continue
      sample_category = sample_info["sample_category"]
      if sample_category.startswith("signal"):
        self.prep_dcard_signals.append(sample_category)
    self.make_plots_backgrounds = [ "ZZ", "WZ", "WW", "TT", "TTW", "TTWW", "TTZ", "DY", "W", "Other", "VH", "TTH", "TH" ] + [ "conversions", "fakes_data" ]
    self.cfgFile_make_plots = os.path.join(self.template_dir, "makePlots_hh_bb1l_cfg.py")
    self.cfgFile_make_plots_mcClosure = os.path.join(self.template_dir, "makePlots_mcClosure_hh_bb1l_cfg.py")

    self.select_rle_output = select_rle_output
    self.use_nonnominal = use_nonnominal
    self.hlt_filter = hlt_filter

    self.evtCategories = evtCategories
    self.evtCategory_inclusive = "hh_bb1l"
    if not self.evtCategory_inclusive in self.evtCategories:
      self.evtCategories.append(self.evtCategory_inclusive)

  def set_BDT_training(self):
    """Run analysis for the purpose of preparing event list files for BDT training.
    """
    self.lepton_selections = [ "Tight" ]
    self.lepton_frWeights = [ "disabled" ]
    self.isBDTtraining = True

  def createCfg_analyze(self, jobOptions, sample_info, lepton_selection):
    """Create python configuration file for the analyze_hh_bb1l executable (analysis code)

    Args:
      inputFiles: list of input files (Ntuples)
      outputFile: output file of the job -- a ROOT file containing histogram
      process: either `TT`, `TTW`, `TTZ`, `EWK`, `Rares`, `data_obs`, or `signal`
      is_mc: flag indicating whether job runs on MC (True) or data (False)
      lumi_scale: event weight (= xsection * luminosity / number of events)
      central_or_shift: either 'central' or one of the systematic uncertainties defined in $CMSSW_BASE/src/hhAnalysis/multilepton/bin/analyze_hh_bb1l.cc
    """
    lepton_frWeight = "disabled" if jobOptions['applyFakeRateWeights'] == "disabled" else "enabled"

    jobOptions['histogramDir'] = getHistogramDir(self.evtCategory_inclusive, lepton_selection, lepton_frWeight)
    if 'mcClosure' in lepton_selection:
      self.mcClosure_dir[lepton_selection] = jobOptions['histogramDir']

    self.set_leptonFakeRateWeightHistogramNames(jobOptions['central_or_shift'], lepton_selection)
    jobOptions['leptonFakeRateWeight.inputFileName'] = self.leptonFakeRateWeight_inputFile
    jobOptions['leptonFakeRateWeight.histogramName_e'] = self.leptonFakeRateWeight_histogramName_e
    jobOptions['leptonFakeRateWeight.histogramName_mu'] = self.leptonFakeRateWeight_histogramName_mu

    lines = super(analyzeConfig_hh_bb1l, self).createCfg_analyze(jobOptions, sample_info)
    create_cfg(self.cfgFile_analyze, jobOptions['cfgFile_modified'], lines)

  def addToMakefile_backgrounds_from_data(self, lines_makefile):
    self.addToMakefile_addBackgrounds(lines_makefile, "sbatch_addBackgrounds", self.sbatchFile_addBackgrounds, self.jobOptions_addBackgrounds)
    self.addToMakefile_addBackgrounds(lines_makefile, "sbatch_addBackgrounds_sum", self.sbatchFile_addBackgrounds_sum, self.jobOptions_addBackgrounds_sum)
    #----------------------------------------------------------------------------
    # CV: run hadd_stage1_5 jobs on quasar,
    #     as the memory consumption of hadd_stage1_5 jobs exceeds the memory limit (1.8 Gb) for batch jobs
    ##is_sbatch_bak = self.is_sbatch
    ##self.is_sbatch = False
    ##is_makefile_bak = self.is_makefile
    ##self.is_makefile = True
    ##self.addToMakefile_hadd_stage1_5(lines_makefile, max_input_files_per_job = 2)
    self.addToMakefile_hadd_stage1_5(lines_makefile)
    ##self.is_sbatch = is_sbatch_bak
    ##self.is_makefile = is_makefile_bak
    #----------------------------------------------------------------------------
    self.addToMakefile_addFakes(lines_makefile)

  def create(self):
    """Creates all necessary config files and runs the complete analysis workfow -- either locally or on the batch system
    """

    for sample_name, sample_info in self.samples.items():
      if not sample_info["use_it"] or sample_info["sample_category"] in [ "additional_signal_overlap", "background_data_estimate" ]:
        continue
      process_name = sample_info["process_name_specific"]
      for lepton_selection in self.lepton_selections:
        for lepton_frWeight in self.lepton_frWeights:
          if lepton_frWeight == "enabled" and not lepton_selection.startswith("Fakeable"):
            continue
          lepton_selection_and_frWeight = get_lepton_selection_and_frWeight(lepton_selection, lepton_frWeight)
          key_dir = getKey(process_name, lepton_selection_and_frWeight)
          for dir_type in [ DKEY_CFGS, DKEY_HIST, DKEY_LOGS, DKEY_ROOT, DKEY_RLES, DKEY_SYNC ]:
            initDict(self.dirs, [ key_dir, dir_type ])
            if dir_type in [ DKEY_CFGS, DKEY_LOGS ]:
              self.dirs[key_dir][dir_type] = os.path.join(self.configDir, dir_type, self.channel,
                "_".join([ lepton_selection_and_frWeight ]), process_name)
            else:
              self.dirs[key_dir][dir_type] = os.path.join(self.outputDir, dir_type, self.channel,
                "_".join([ lepton_selection_and_frWeight ]), process_name)
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
      if not sample_info["use_it"] or sample_info["sample_category"] in [ "additional_signal_overlap", "background_data_estimate" ]:
        continue
      logging.info("Checking input files for sample %s" % sample_info["process_name_specific"])
      inputFileLists[sample_name] = generateInputFileList(sample_info, self.max_files_per_job)

    mcClosure_regex = re.compile('Fakeable_mcClosure_(?P<type>m|e)_wFakeRateWeights')
    for lepton_selection in self.lepton_selections:
      electron_selection = lepton_selection
      muon_selection = lepton_selection

      if lepton_selection == "Fakeable_mcClosure_e":
        electron_selection = "Fakeable"
        muon_selection = "Tight"
      elif lepton_selection == "Fakeable_mcClosure_m":
        electron_selection = "Tight"
        muon_selection = "Fakeable"

      for lepton_frWeight in self.lepton_frWeights:
        if lepton_frWeight == "enabled" and not lepton_selection.startswith("Fakeable"):
          continue
        if lepton_frWeight == "disabled" and not lepton_selection in [ "Tight", "forBDTtraining" ]:
          continue
        lepton_selection_and_frWeight = get_lepton_selection_and_frWeight(lepton_selection, lepton_frWeight)

        for sample_name, sample_info in self.samples.items():
          if not sample_info["use_it"] or sample_info["sample_category"] in [ "additional_signal_overlap", "background_data_estimate" ]:
            continue
          process_name = sample_info["process_name_specific"]
          logging.info("Creating configuration files to run '%s' for sample %s" % (self.executable_analyze, process_name))

          sample_category = sample_info["sample_category"]
          is_mc = (sample_info["type"] == "mc")
          is_signal = (sample_category.startswith("signal"))
          for central_or_shift in self.central_or_shifts:

            inputFileList = inputFileLists[sample_name]
            for jobId in inputFileList.keys():
              if central_or_shift != "central":
                isFR_shape_shift = (central_or_shift in systematics.FR_all)
                if not ((lepton_selection == "Fakeable" and isFR_shape_shift) or lepton_selection == "Tight"):
                  continue
                if not is_mc and not isFR_shape_shift:
                  continue

              if central_or_shift in systematics.LHE().hh and not (sample_category.startswith("signal") and sample_info['has_LHE']):
                continue
              if central_or_shift in systematics.LHE().ttH and sample_category != "TTH":
                continue
              if central_or_shift in systematics.LHE().ttW and sample_category != "TTW":
                continue
              if central_or_shift in systematics.LHE().ttZ and sample_category != "TTZ":
                continue
              if central_or_shift in systematics.DYMCReweighting and not ('DYMCReweighting' in sample_info.keys() and sample_info["DYMCReweighting"]):
                continue

              logging.info(" ... for '%s' and systematic uncertainty option '%s'" % (lepton_selection_and_frWeight, central_or_shift))

              # build config files for executing analysis code
              key_dir = getKey(process_name, lepton_selection_and_frWeight)
              key_analyze_job = getKey(process_name, lepton_selection_and_frWeight, central_or_shift, jobId)
              ntupleFiles = inputFileList[jobId]
              if len(ntupleFiles) == 0:
                logging.warning("No input ntuples for %s --> skipping job !!" % (key_analyze_job))
                continue

              cfg_key = getKey(self.channel, process_name, lepton_selection_and_frWeight, central_or_shift, jobId)
              cfgFile_modified_path = os.path.join(self.dirs[key_dir][DKEY_CFGS], "analyze_%s_cfg.py" % cfg_key)
              histogramFile_path = os.path.join(self.dirs[key_dir][DKEY_HIST], "%s.root" % key_analyze_job)
              logFile_path = os.path.join(self.dirs[key_dir][DKEY_LOGS], "analyze_%s.log" % cfg_key)
              rleOutputFile_path = os.path.join(self.dirs[key_dir][DKEY_RLES], "rle_%s.txt" % cfg_key) \
                                   if self.select_rle_output else ""
              applyFakeRateWeights = self.applyFakeRateWeights  \
                if self.isBDTtraining or not lepton_selection == "Tight" \
                else "disabled"

              self.jobOptions_analyze[key_analyze_job] = {
                'ntupleFiles'              : ntupleFiles,
                'cfgFile_modified'         : cfgFile_modified_path,
                'histogramFile'            : histogramFile_path,
                'logFile'                  : logFile_path,
                'selEventsFileName_output' : rleOutputFile_path,
                'electronSelection'        : electron_selection,
                'muonSelection'            : muon_selection,
                'lep_mva_cut'              : self.lep_mva_cut,
                'apply_leptonGenMatching'  : self.apply_leptonGenMatching,
                'apply_hadTauVeto'         : self.apply_hadTauVeto,
                'hadTauSelection_veto'     : self.hadTau_mva_wp_veto,
                'applyFakeRateWeights'     : applyFakeRateWeights,
                'central_or_shift'         : central_or_shift,
                'evtCategories'            : self.evtCategories,
                'selectBDT'                : self.isBDTtraining,
                'apply_hlt_filter'         : self.hlt_filter,
                'useNonNominal'            : self.use_nonnominal,
                'fillGenEvtHistograms'     : True,
              }
              self.createCfg_analyze(self.jobOptions_analyze[key_analyze_job], sample_info, lepton_selection)

              # initialize input and output file names for hadd_stage1
              key_hadd_stage1 = getKey(process_name, lepton_selection_and_frWeight)
              if not key_hadd_stage1 in self.inputFiles_hadd_stage1:
                self.inputFiles_hadd_stage1[key_hadd_stage1] = []
              self.inputFiles_hadd_stage1[key_hadd_stage1].append(self.jobOptions_analyze[key_analyze_job]['histogramFile'])
              self.outputFile_hadd_stage1[key_hadd_stage1] = os.path.join(self.dirs[DKEY_HIST], "histograms_harvested_stage1_%s_%s_%s.root" % \
                (self.channel, process_name, lepton_selection_and_frWeight))

          if self.isBDTtraining:
            continue

          #----------------------------------------------------------------------------
          # split hadd_stage1 files into separate files, one for each event category
          for category in self.evtCategories:
            key_hadd_stage1 = getKey(process_name, lepton_selection_and_frWeight)
            key_copyHistograms = getKey(category, process_name, lepton_selection_and_frWeight)
            cfgFile_modified = os.path.join(self.dirs[DKEY_CFGS], "copyHistograms_%s_%s_%s_%s_cfg.py" % \
              (self.channel, process_name, lepton_selection_and_frWeight, category))
            outputFile = os.path.join(self.dirs[DKEY_HIST], "copyHistograms_%s_%s_%s_%s.root" % \
              (self.channel, process_name, lepton_selection_and_frWeight, category))
            self.jobOptions_copyHistograms[key_copyHistograms] = {
              'inputFile' : self.outputFile_hadd_stage1[key_hadd_stage1],
              'cfgFile_modified' : cfgFile_modified,
              'outputFile' : outputFile,
              'logFile' : os.path.join(self.dirs[DKEY_LOGS], os.path.basename(cfgFile_modified).replace("_cfg.py", ".log")),
              'categories' :[ category ],
            }
            self.createCfg_copyHistograms(self.jobOptions_copyHistograms[key_copyHistograms])
          #----------------------------------------------------------------------------

          if is_mc:
            logging.info("Creating configuration files to run 'addBackgrounds' for sample %s" % process_name)

            sample_categories = [ sample_category ]
            for sample_category in sample_categories:
              # sum non-fake and fake contributions for each MC sample separately
              genMatch_categories = [ "nonfake", "conversions", "fake" ]

              for genMatch_category in genMatch_categories:
                for category in self.evtCategories:
                  key_copyHistograms = getKey(category, process_name, lepton_selection_and_frWeight)
                  key_addBackgrounds_job = None
                  processes_input = None
                  process_output = None
                  cfgFile_modified = None
                  outputFile = None
                  if genMatch_category == "nonfake":
                    # sum non-fake contributions for each MC sample separately
                    # input processes: TT2l0g0j,...
                    # output processes: TT; ...
                    if sample_category.startswith("signal"):
                      lepton_genMatches = []
                      lepton_genMatches.extend(self.lepton_genMatches_nonfakes)
                      lepton_genMatches.extend(self.lepton_genMatches_conversions)
                      processes_input = [ "%s%s" % (sample_category, genMatch) for genMatch in lepton_genMatches ]
                    else:
                      processes_input = [ "%s%s" % (sample_category, genMatch) for genMatch in self.lepton_genMatches_nonfakes ]
                    process_output = sample_category
                    key_addBackgrounds_job = getKey(category, process_name, sample_category, lepton_selection_and_frWeight)
                    cfgFile_modified = os.path.join(self.dirs[DKEY_CFGS], "addBackgrounds_%s_%s_%s_%s_%s_cfg.py" % \
                      (self.channel, process_name, sample_category, lepton_selection_and_frWeight, category))
                    outputFile = os.path.join(self.dirs[DKEY_HIST], "addBackgrounds_%s_%s_%s_%s_%s.root" % \
                      (self.channel, process_name, sample_category, lepton_selection_and_frWeight, category))
                  if genMatch_category == "conversions":
                    # sum conversion background contributions for each MC sample separately
                    # input processes: TT1l1g0j,...
                    # output processes: TT_conversions; ...
                    if not sample_category.startswith("signal"):
                      processes_input = [ "%s%s" % (sample_category, genMatch) for genMatch in self.lepton_genMatches_conversions ]
                    process_output = "%s_conversion" % sample_category
                    key_addBackgrounds_job = getKey(category, process_name, "%s_conversion" % sample_category, lepton_selection_and_frWeight)
                    cfgFile_modified = os.path.join(self.dirs[DKEY_CFGS], "addBackgrounds_%s_%s_conversions_%s_%s_%s_cfg.py" % \
                      (self.channel, process_name, sample_category, lepton_selection_and_frWeight, category))
                    outputFile = os.path.join(self.dirs[DKEY_HIST], "addBackgrounds_%s_%s_conversions_%s_%s_%s.root" % \
                      (self.channel, process_name, sample_category, lepton_selection_and_frWeight, category))
                  elif genMatch_category == "fake":
                    # sum fake background contributions for each MC sample separately
                    # input processes: TT1l1j, TT0l2j; ...
                    # output processes: TT_fake; ...
                    processes_input = [ "%s%s" % (sample_category, genMatch) for genMatch in self.lepton_genMatches_fakes ]
                    process_output = "%s_fake" % sample_category
                    key_addBackgrounds_job = getKey(category, process_name, "%s_fake" % sample_category, lepton_selection_and_frWeight)
                    cfgFile_modified = os.path.join(self.dirs[DKEY_CFGS], "addBackgrounds_%s_%s_fakes_%s_%s_%s_cfg.py" % \
                      (self.channel, process_name, sample_category, lepton_selection_and_frWeight, category))
                    outputFile = os.path.join(self.dirs[DKEY_HIST], "addBackgrounds_%s_%s_fakes_%s_%s_%s.root" % \
                      (self.channel, process_name, sample_category, lepton_selection_and_frWeight, category))
                  if processes_input:
                    logging.info(" ...for genMatch option = '%s'" % genMatch_category)
                    self.jobOptions_addBackgrounds[key_addBackgrounds_job] = {
                      'inputFile' : self.jobOptions_copyHistograms[key_copyHistograms]['inputFile'],
                      'cfgFile_modified' : cfgFile_modified,
                      'outputFile' : outputFile,
                      'logFile' : os.path.join(self.dirs[DKEY_LOGS], os.path.basename(cfgFile_modified).replace("_cfg.py", ".log")),
                      'categories' :[ getHistogramDir(category, lepton_selection, lepton_frWeight) ],
                      'processes_input' : processes_input,
                      'process_output' : process_output
                    }
                    self.createCfg_addBackgrounds(self.jobOptions_addBackgrounds[key_addBackgrounds_job])

                    # initialize input and output file names for hadd_stage1_5
                    key_hadd_stage1_5 = getKey(category, lepton_selection_and_frWeight)
                    if not key_hadd_stage1_5 in self.inputFiles_hadd_stage1_5:
                      self.inputFiles_hadd_stage1_5[key_hadd_stage1_5] = []
                    self.inputFiles_hadd_stage1_5[key_hadd_stage1_5].append(self.jobOptions_addBackgrounds[key_addBackgrounds_job]['outputFile'])
                    self.outputFile_hadd_stage1_5[key_hadd_stage1_5] = os.path.join(self.dirs[DKEY_HIST], "histograms_harvested_stage1_5_%s_%s_%s.root" % \
                      (self.channel, lepton_selection_and_frWeight, category))

          if self.isBDTtraining:
            continue
          # add output files of hadd_stage1 for data to list of input files for hadd_stage1_5
          if not is_mc:
            for category in self.evtCategories:
              key_copyHistograms = getKey(category, process_name, lepton_selection_and_frWeight)
              key_hadd_stage1_5 = getKey(lepton_selection_and_frWeight)
              if not key_hadd_stage1_5 in self.inputFiles_hadd_stage1_5:
                self.inputFiles_hadd_stage1_5[key_hadd_stage1_5] = []
              self.inputFiles_hadd_stage1_5[key_hadd_stage1_5].append(self.jobOptions_copyHistograms[key_copyHistograms]['inputFile'])

        if self.isBDTtraining:
          continue

        for category in self.evtCategories:
          # sum fake background contributions for the total of all MC sample
          # input processes: TT1l0g1j,TT0l1g1j,TT0l0g2j; ...
          # output process: fakes_mc
          key_addBackgrounds_job_fakes = getKey(category, lepton_selection_and_frWeight, "fakes")
          key_hadd_stage1_5 = getKey(category, lepton_selection_and_frWeight)
          sample_categories = []
          sample_categories.extend(self.nonfake_backgrounds)
          processes_input = []
          for sample_category in sample_categories:
            processes_input.append("%s_fake" % sample_category)
          self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_fakes] = {
            'inputFile' : self.outputFile_hadd_stage1_5[key_hadd_stage1_5],
            'cfgFile_modified' : os.path.join(self.dirs[DKEY_CFGS], "addBackgrounds_%s_fakes_mc_%s_%s_cfg.py" % \
              (self.channel, lepton_selection_and_frWeight, category)),
            'outputFile' : os.path.join(self.dirs[DKEY_HIST], "addBackgrounds_%s_fakes_mc_%s_%s.root" % \
              (self.channel, lepton_selection_and_frWeight, category)),
            'logFile' : os.path.join(self.dirs[DKEY_LOGS], "addBackgrounds_%s_fakes_mc_%s_%s.log" % \
              (self.channel, lepton_selection_and_frWeight, category)),
            'categories' : [ getHistogramDir(category, lepton_selection, lepton_frWeight) ],
            'processes_input' : processes_input,
            'process_output' : "fakes_mc"
          }
          self.createCfg_addBackgrounds(self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_fakes])

          # sum conversion background contributions for the total of all MC sample
          # input processes: TT1l1g0j, TT0l2g0j; ...
          # output process: conversions
          key_addBackgrounds_job_conversions = getKey(category, lepton_selection, "conversions")
          sample_categories = []
          sample_categories.extend(self.nonfake_backgrounds)
          processes_input = []
          for sample_category in sample_categories:
            processes_input.append("%s_conversion" % sample_category)
          self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_conversions] = {
            'inputFile' : self.outputFile_hadd_stage1_5[key_hadd_stage1_5],
            'cfgFile_modified' : os.path.join(self.dirs[DKEY_CFGS], "addBackgrounds_%s_conversions_%s_%s_cfg.py" % \
              (self.channel, lepton_selection_and_frWeight, category)),
            'outputFile' : os.path.join(self.dirs[DKEY_HIST], "addBackgrounds_%s_conversions_%s_%s.root" % \
              (self.channel, lepton_selection_and_frWeight, category)),
            'logFile' : os.path.join(self.dirs[DKEY_LOGS], "addBackgrounds_%s_conversions_%s_%s.log" % \
              (self.channel, lepton_selection_and_frWeight, category)),
            'categories' : [ getHistogramDir(category, lepton_selection, lepton_frWeight) ],
            'processes_input' : processes_input,
            'process_output' : "conversions"
          }
          self.createCfg_addBackgrounds(self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_conversions])

          # sum signal contributions from gluon fusion and VBF HH production,
          # separately for "nonfake" and "fake" contributions
          genMatch_categories = [ "nonfake", "fake" ]
          for genMatch_category in genMatch_categories:
            for signal_base, signal_input in self.signal_io.items():
              key_addBackgrounds_job_signal = getKey(category, lepton_selection, signal_base, genMatch_category)
              processes_input = signal_input
              process_output = signal_base
              if genMatch_category == "fake":
                processes_input = [ process_input + "_fake" for process_input in processes_input ]
                process_output += "_fake"
              if key_addBackgrounds_job_signal in self.jobOptions_addBackgrounds_sum.keys():
                continue
              cfg_key = getKey(self.channel, signal_base, genMatch_category, lepton_selection, category)
              self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_signal] = {
                'inputFile' : self.outputFile_hadd_stage1_5[key_hadd_stage1_5],
                'cfgFile_modified' : os.path.join(self.dirs[DKEY_CFGS], "addBackgrounds_%s_cfg.py" % cfg_key),
                'outputFile' : os.path.join(self.dirs[DKEY_HIST], "addBackgrounds_%s.root" % cfg_key),
                'logFile' : os.path.join(self.dirs[DKEY_LOGS], "addBackgrounds_%s.log" % cfg_key),
                'categories' : [ getHistogramDir(category, lepton_selection, lepton_frWeight) ],
                'processes_input' : processes_input,
                'process_output' : process_output
              }
              self.createCfg_addBackgrounds(self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_signal])
              key_hadd_stage2 = getKey(category, lepton_selection_and_frWeight)
              if not key_hadd_stage2 in self.inputFiles_hadd_stage2:
                self.inputFiles_hadd_stage2[key_hadd_stage2] = []
              if lepton_selection == "Tight":
                self.inputFiles_hadd_stage2[key_hadd_stage2].append(self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_signal]['outputFile'])

          # initialize input and output file names for hadd_stage2
          key_hadd_stage2 = getKey(category, lepton_selection_and_frWeight)
          if not key_hadd_stage2 in self.inputFiles_hadd_stage2:
            self.inputFiles_hadd_stage2[key_hadd_stage2] = []
          if lepton_selection == "Tight":
            self.inputFiles_hadd_stage2[key_hadd_stage2].append(self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_fakes]['outputFile'])
            self.inputFiles_hadd_stage2[key_hadd_stage2].append(self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_conversions]['outputFile'])
          key_hadd_stage1_5 = getKey(category, lepton_selection_and_frWeight)
          self.inputFiles_hadd_stage2[key_hadd_stage2].append(self.outputFile_hadd_stage1_5[key_hadd_stage1_5])
          self.outputFile_hadd_stage2[key_hadd_stage2] = os.path.join(self.dirs[DKEY_HIST], "histograms_harvested_stage2_%s_%s_%s.root" % \
            (self.channel, lepton_selection_and_frWeight, category))

    if self.isBDTtraining:
      if self.is_sbatch:
        logging.info("Creating script for submitting '%s' jobs to batch system" % self.executable_analyze)
        self.sbatchFile_analyze = os.path.join(self.dirs[DKEY_SCRIPTS], "sbatch_analyze_%s.py" % self.channel)
        self.createScript_sbatch_analyze(self.executable_analyze, self.sbatchFile_analyze, self.jobOptions_analyze)
      logging.info("Creating Makefile")
      lines_makefile = []
      self.addToMakefile_analyze(lines_makefile)
      self.addToMakefile_hadd_stage1(lines_makefile)
      self.createMakefile(lines_makefile)
      logging.info("Done")
      return self.num_jobs

    logging.info("Creating configuration files to run 'addBackgroundFakes'")
    for category in self.evtCategories:
      key_addFakes_job = getKey(category, "fakes_data")
      key_hadd_stage1_5 = getKey(category, get_lepton_selection_and_frWeight("Fakeable", "enabled"))
      self.jobOptions_addFakes[key_addFakes_job] = {
        'inputFile' : self.outputFile_hadd_stage1_5[key_hadd_stage1_5],
        'cfgFile_modified' : os.path.join(self.dirs[DKEY_CFGS], "addBackgroundLeptonFakes_%s_%s_cfg.py" % (self.channel, category)),
        'outputFile' : os.path.join(self.dirs[DKEY_HIST], "addBackgroundLeptonFakes_%s_%s.root" % (self.channel, category)),
        'logFile' : os.path.join(self.dirs[DKEY_LOGS], "addBackgroundLeptonFakes_%s_%s.log" % (self.channel, category)),
        'category_signal' : getHistogramDir(category, "Tight", "disabled"),
        'category_sideband' : getHistogramDir(category, "Fakeable", "enabled")
      }
      self.createCfg_addFakes(self.jobOptions_addFakes[key_addFakes_job])
      key_hadd_stage2 = getKey(category, get_lepton_selection_and_frWeight("Tight", "disabled"))
      self.inputFiles_hadd_stage2[key_hadd_stage2].append(self.jobOptions_addFakes[key_addFakes_job]['outputFile'])

    logging.info("Creating configuration files to run 'prepareDatacards'")
    for category in self.evtCategories:
      for histogramToFit in self.histograms_to_fit:
        key_prep_dcard_job = getKey(category, histogramToFit)
        key_hadd_stage2 = getKey(category, get_lepton_selection_and_frWeight("Tight", "disabled"))
        self.jobOptions_prep_dcard[key_prep_dcard_job] = {
          'inputFile' : self.outputFile_hadd_stage2[key_hadd_stage2],
          'cfgFile_modified' : os.path.join(self.dirs[DKEY_CFGS], "prepareDatacards_%s_%s_%s_cfg.py" % (self.channel, category, histogramToFit)),
          'datacardFile' : os.path.join(self.dirs[DKEY_DCRD], "prepareDatacards_%s_%s_%s.root" % (self.channel, category, histogramToFit)),
          'histogramDir' : getHistogramDir(category, "Tight", "disabled"),
          'histogramToFit' : histogramToFit
        }
        self.createCfg_prep_dcard(self.jobOptions_prep_dcard[key_prep_dcard_job])
        # add shape templates for the following systematic uncertainties:
        #  - 'CMS_ttHl_Clos_norm_e'
        #  - 'CMS_ttHl_Clos_shape_e'
        #  - 'CMS_ttHl_Clos_norm_m'
        #  - 'CMS_ttHl_Clos_shape_m'
        key_prep_dcard_job = getKey(category, histogramToFit)
        key_hadd_stage2 = getKey(category, get_lepton_selection_and_frWeight("Tight", "disabled"))
        key_add_syst_fakerate_job = getKey(category, histogramToFit)
        self.jobOptions_add_syst_fakerate[key_add_syst_fakerate_job] = {
          'inputFile' : self.jobOptions_prep_dcard[key_prep_dcard_job]['datacardFile'],
          'cfgFile_modified' : os.path.join(self.dirs[DKEY_CFGS], "addSystFakeRates_%s_%s_%s_cfg.py" % \
            (self.channel, category, histogramToFit)),
          'outputFile' : os.path.join(self.dirs[DKEY_DCRD], "addSystFakeRates_%s_%s_%s.root" % \
            (self.channel, category, histogramToFit)),
          'category' : category,
          'histogramToFit' : histogramToFit,
          'plots_outputFileName' : os.path.join(self.dirs[DKEY_PLOT], "addSystFakeRates.png")
        }
        histogramDir_nominal = getHistogramDir(category, "Tight", "disabled")
        for lepton_type in [ 'e', 'm' ]:
          lepton_mcClosure = "Fakeable_mcClosure_%s" % lepton_type
          if lepton_mcClosure not in self.lepton_selections:
            continue
          lepton_selection_and_frWeight = get_lepton_selection_and_frWeight(lepton_mcClosure, "enabled")
          key_addBackgrounds_job_fakes = getKey(category, lepton_selection_and_frWeight, "fakes")
          histogramDir_mcClosure = self.mcClosure_dir[lepton_mcClosure]
          histogramDir_mcClosure = histogramDir_mcClosure.replace(self.evtCategory_inclusive, category)
          self.jobOptions_add_syst_fakerate[key_add_syst_fakerate_job].update({
            'add_Clos_%s' % lepton_type : ("Fakeable_mcClosure_%s" % lepton_type) in self.lepton_selections,
            'inputFile_nominal_%s' % lepton_type : self.outputFile_hadd_stage2[key_hadd_stage2],
            'histogramName_nominal_%s' % lepton_type : "%s/sel/evt/fakes_mc/%s" % (histogramDir_nominal, histogramToFit),
            'inputFile_mcClosure_%s' % lepton_type : self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_fakes]['outputFile'],
            'histogramName_mcClosure_%s' % lepton_type : "%s/sel/evt/fakes_mc/%s" % (histogramDir_mcClosure, histogramToFit)
          })
        self.createCfg_add_syst_fakerate(self.jobOptions_add_syst_fakerate[key_add_syst_fakerate_job])

    logging.info("Creating configuration files to run 'makePlots'")
    key_makePlots_job = getKey('')
    key_hadd_stage2 = getKey(self.evtCategory_inclusive, get_lepton_selection_and_frWeight("Tight", "disabled"))
    self.jobOptions_make_plots[key_makePlots_job] = {
      'executable' : self.executable_make_plots,
      'inputFile' : self.outputFile_hadd_stage2[key_hadd_stage2],
      'cfgFile_modified' : os.path.join(self.dirs[DKEY_CFGS], "makePlots_%s_cfg.py" % self.channel),
      'outputFile' : os.path.join(self.dirs[DKEY_PLOT], "makePlots_%s.png" % self.channel),
      'histogramDir' : getHistogramDir(self.evtCategory_inclusive, "Tight", "disabled"),
      'label' : '1l',
      'make_plots_backgrounds' : self.make_plots_backgrounds
    }
    self.createCfg_makePlots(self.jobOptions_make_plots[key_makePlots_job])
    if "Fakeable_mcClosure" in self.lepton_selections: #TODO
      key_makePlots_job = getKey('')
      key_hadd_stage2 = getKey(self.evtCategory_inclusive, get_lepton_selection_and_frWeight("Tight", "disabled"))
      self.jobOptions_make_plots[key_makePlots_job] = {
        'executable' : self.executable_make_plots_mcClosure,
        'inputFile' : self.outputFile_hadd_stage2[key_hadd_stage2],
        'cfgFile_modified' : os.path.join(self.dirs[DKEY_CFGS], "makePlots_mcClosure_%s_cfg.py" % self.channel),
        'outputFile' : os.path.join(self.dirs[DKEY_PLOT], "makePlots_mcClosure_%s.png" % self.channel)
      }
      self.createCfg_makePlots_mcClosure(self.jobOptions_make_plots[key_makePlots_job])

    if self.is_sbatch:
      logging.info("Creating script for submitting '%s' jobs to batch system" % self.executable_analyze)
      self.sbatchFile_analyze = os.path.join(self.dirs[DKEY_SCRIPTS], "sbatch_analyze_%s.py" % self.channel)
      self.createScript_sbatch_analyze(self.executable_analyze, self.sbatchFile_analyze, self.jobOptions_analyze)
      logging.info("Creating script for submitting '%s' jobs to batch system" % self.executable_copyHistograms)
      self.sbatchFile_copyHistograms = os.path.join(self.dirs[DKEY_SCRIPTS], "sbatch_copyHistograms_%s.py" % self.channel)
      self.createScript_sbatch_copyHistograms(self.executable_copyHistograms, self.sbatchFile_copyHistograms, self.jobOptions_copyHistograms)
      logging.info("Creating script for submitting '%s' jobs to batch system" % self.executable_addBackgrounds)
      self.sbatchFile_addBackgrounds = os.path.join(self.dirs[DKEY_SCRIPTS], "sbatch_addBackgrounds_%s.py" % self.channel)
      self.createScript_sbatch_addBackgrounds(self.executable_addBackgrounds, self.sbatchFile_addBackgrounds, self.jobOptions_addBackgrounds)
      self.sbatchFile_addBackgrounds_sum = os.path.join(self.dirs[DKEY_SCRIPTS], "sbatch_addBackgrounds_sum_%s.py" % self.channel)
      self.createScript_sbatch_addBackgrounds(self.executable_addBackgrounds, self.sbatchFile_addBackgrounds_sum, self.jobOptions_addBackgrounds_sum)
      logging.info("Creating script for submitting '%s' jobs to batch system" % self.executable_addFakes)
      self.sbatchFile_addFakes = os.path.join(self.dirs[DKEY_SCRIPTS], "sbatch_addFakes_%s.py" % self.channel)
      self.createScript_sbatch_addFakes(self.executable_addFakes, self.sbatchFile_addFakes, self.jobOptions_addFakes)

    logging.info("Creating Makefile")
    lines_makefile = []
    self.addToMakefile_analyze(lines_makefile)
    self.addToMakefile_hadd_stage1(lines_makefile)
    self.addToMakefile_copyHistograms(lines_makefile)
    self.addToMakefile_backgrounds_from_data(lines_makefile)
    #----------------------------------------------------------------------------
    # CV: run hadd_stage2 jobs on quasar,
    #     as the memory consumption of hadd_stage2 jobs exceeds the memory limit (1.8 Gb) for batch jobs
    ##is_sbatch_bak = self.is_sbatch
    ##self.is_sbatch = False
    ##is_makefile_bak = self.is_makefile
    ##self.is_makefile = True
    ##self.addToMakefile_hadd_stage2(lines_makefile, max_input_files_per_job = 2)
    self.addToMakefile_hadd_stage2(lines_makefile)
    ##self.is_sbatch = is_sbatch_bak
    ##self.is_makefile = is_makefile_bak
    #----------------------------------------------------------------------------
    self.addToMakefile_prep_dcard(lines_makefile)
    self.addToMakefile_add_syst_fakerate(lines_makefile)
    self.addToMakefile_make_plots(lines_makefile)
    self.createMakefile(lines_makefile)

    logging.info("Done")

    return self.num_jobs
