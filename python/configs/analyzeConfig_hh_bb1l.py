import logging
import re
from datetime import datetime

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
        apply_hadTauVeto,
        hadTau_mva_wp_veto,
        applyFakeRateWeights,
        central_or_shifts,
        lep_mva_wp,
        jet_cleaning_by_index,
        gen_matching_by_index,
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
        do_sync           = False,
        isDebug           = False,
        rle_select        = '',
        use_nonnominal    = False,
        hlt_filter        = False,
        use_home          = False,
        submission_cmd    = None,
        second_bdt        = False,
        doDataMCPlots     = False,
      ):
    analyzeConfig_hh.__init__(self,
      configDir             = configDir,
      outputDir             = outputDir,
      executable_analyze    = executable_analyze,
      channel               = "hh_bb1l",
      samples               = samples,
      jet_cleaning_by_index = jet_cleaning_by_index,
      gen_matching_by_index = gen_matching_by_index,
      central_or_shifts     = central_or_shifts,
      max_files_per_job     = max_files_per_job,
      era                   = era,
      use_lumi              = use_lumi,
      lumi                  = lumi,
      check_output_files    = check_output_files,
      running_method        = running_method,
      num_parallel_jobs     = num_parallel_jobs,
      histograms_to_fit     = histograms_to_fit,
      triggers              = [ '1e', '1mu' ],
      lep_mva_wp            = lep_mva_wp,
      verbose               = verbose,
      dry_run               = dry_run,
      do_sync               = do_sync,
      isDebug               = isDebug,
      use_home              = use_home,
      template_dir          = os.path.join(os.getenv('CMSSW_BASE'), 'src', 'hhAnalysis', 'bbww', 'test', 'templates'),
      submission_cmd        = submission_cmd,
      apply_pileupJetID     = 'loose',
    )

    self.lepton_selections = [ "Tight", "Fakeable" ]
    self.lepton_frWeights = [ "enabled", "disabled" ]
    self.apply_hadTauVeto = apply_hadTauVeto
    self.hadTau_mva_wp_veto = hadTau_mva_wp_veto
    self.applyFakeRateWeights = applyFakeRateWeights

    self.apply_leptonGenMatching = True
    if self.run_mcClosure:
      self.lepton_selections.extend([ "Fakeable_mcClosure_e", "Fakeable_mcClosure_m" ])
    self.central_or_shifts_fr = systematics.FRe_shape + systematics.FRm_shape
    self.pruneSystematics()
    self.internalizeSystematics()

    self.executable_addBackgrounds = executable_addBackgrounds
    self.executable_addFakes = executable_addFakes

    self.nonfake_backgrounds = self.get_nonfake_backgrounds(split_vh = False, split_th = False, split_ST = True)

    self.cfgFile_analyze = os.path.join(self.template_dir, cfgFile_analyze)
    self.prep_dcard_signals = []
    for sample_name, sample_info in self.samples.items():
      if not sample_info["use_it"]:
        continue
      sample_category = sample_info["sample_category"]
      if sample_category.startswith("signal"):
        self.prep_dcard_signals.append(sample_category)
    self.make_plots_backgrounds = self.get_makeplots_backgrounds()
    self.cfgFile_make_plots = os.path.join(self.template_dir, "makePlots_hh_bb1l_cfg.py")
    self.cfgFile_make_plots_mcClosure = os.path.join(self.template_dir, "makePlots_mcClosure_hh_bb1l_cfg.py")

    self.select_rle_output = select_rle_output
    self.rle_select = rle_select
    self.use_nonnominal = use_nonnominal
    self.hlt_filter = hlt_filter

    self.evtCategories = evtCategories
    self.evtCategory_inclusive = "hh_bb1l"
    if not self.evtCategory_inclusive in self.evtCategories:
      self.evtCategories.append(self.evtCategory_inclusive)
    self.second_bdt = second_bdt
    self.doDataMCPlots = doDataMCPlots
  def set_BDT_training(self):
    """Run analysis for the purpose of preparing event list files for BDT training.
    """
    self.lepton_selections = [ "Tight" ]
    self.lepton_frWeights = [ "disabled" ]
    self.isBDTtraining = True

  def accept_systematics(self, central_or_shift, is_mc, lepton_selection, sample_info):
    if central_or_shift != "central":
      isFR_shape_shift = (central_or_shift in self.central_or_shifts_fr)
      if not ((lepton_selection == "Fakeable" and isFR_shape_shift) or lepton_selection == "Tight"):
        return False
      if isFR_shape_shift and lepton_selection == "Tight":
        return False
      if not is_mc and not isFR_shape_shift:
        return False
      if not self.accept_central_or_shift(central_or_shift, sample_info):
        return False
    return True

  def createCfg_analyze(self, jobOptions, sample_info, lepton_selection):
    """Create python configuration file for the analyze_hh_bb1l executable (analysis code)

    Args:
      inputFiles: list of input files (Ntuples)
      outputFile: output file of the job -- a ROOT file containing histogram
      process: either `TT`, `TTW`, `TTZ`, `DY`, `Rares`, `data_obs`, or `signal`
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

  def addToMakefile_backgrounds_from_data(self, lines_makefile, make_target = "phony_addFakes", make_dependency = "phony_copyHistograms"):
    self.addToMakefile_addBackgrounds(lines_makefile, "phony_addBackgrounds", make_dependency, self.sbatchFile_addBackgrounds, self.jobOptions_addBackgrounds)
    self.addToMakefile_hadd_stage1_5(lines_makefile, "phony_hadd_stage1_5", "phony_addBackgrounds")
    self.addToMakefile_addBackgrounds(lines_makefile, "phony_addBackgrounds_sum", "phony_hadd_stage1_5", self.sbatchFile_addBackgrounds_sum, self.jobOptions_addBackgrounds_sum)
    self.addToMakefile_addFakes(lines_makefile, "phony_addFakes", "phony_hadd_stage1_5")
    if make_target != "phony_addFakes":
      lines_makefile.append("%s: %s" % (make_target, "phony_addFakes"))
      lines_makefile.append("")
    self.make_dependency_hadd_stage2 = " ".join([ "phony_addBackgrounds_sum", make_target ])

  def create(self):
    """Creates all necessary config files and runs the complete analysis workfow -- either locally or on the batch system
    """

    for sample_name, sample_info in self.samples.items():
      if self.isBDTtraining and sample_info["sample_category"] == 'data_obs' :
        sample_info["use_it"] = False
      if not sample_info["use_it"]:
        continue
      sample_category = sample_info["sample_category"]
      is_mc = (sample_info["type"] == "mc")
      process_name = sample_info["process_name_specific"]

      logging.info("Building dictionaries for sample %s..." % process_name)
      for lepton_selection in self.lepton_selections:
        for lepton_frWeight in self.lepton_frWeights:
          if lepton_frWeight == "enabled" and not lepton_selection.startswith("Fakeable"):
            continue
          if lepton_frWeight == "disabled" and not lepton_selection in [ "Tight", "forBDTtraining" ]:
            continue

          lepton_selection_and_frWeight = get_lepton_selection_and_frWeight(lepton_selection, lepton_frWeight)
          central_or_shift_extensions = ["", "hadd", "copyHistograms", "addBackgrounds"]
          central_or_shift_dedicated = self.central_or_shifts if self.runTHweights(sample_info) else self.central_or_shifts_external
          central_or_shifts_extended = central_or_shift_extensions + central_or_shift_dedicated
          for central_or_shift_or_dummy in central_or_shifts_extended:
            process_name_extended = [ process_name, "hadd" ]
            for process_name_or_dummy in process_name_extended:
              if process_name_or_dummy in [ "hadd" ] and central_or_shift_or_dummy != "":
                continue
              evtcategories_extended = [""]
              evtcategories_extended.extend(self.evtCategories)
              if central_or_shift_or_dummy in [ "hadd", "copyHistograms", "addBackgrounds" ] and process_name_or_dummy in [ "hadd" ]:
                continue

              if central_or_shift_or_dummy not in central_or_shift_extensions and not self.accept_systematics(
                  central_or_shift_or_dummy, is_mc, lepton_selection, sample_info
              ):
                continue

              key_dir = getKey(process_name_or_dummy, lepton_selection_and_frWeight, central_or_shift_or_dummy)
              for dir_type in [ DKEY_CFGS, DKEY_HIST, DKEY_LOGS, DKEY_RLES, DKEY_SYNC ]:
                if dir_type == DKEY_SYNC and not self.do_sync:
                  continue
                initDict(self.dirs, [ key_dir, dir_type ])
                if dir_type in [ DKEY_CFGS, DKEY_LOGS ]:
                  self.dirs[key_dir][dir_type] = os.path.join(self.configDir, dir_type, self.channel,
                                                              "_".join([ lepton_selection_and_frWeight ]), process_name_or_dummy, central_or_shift_or_dummy)
                else:
                  self.dirs[key_dir][dir_type] = os.path.join(self.outputDir, dir_type, self.channel,
                                                              "_".join([ lepton_selection_and_frWeight ]), process_name_or_dummy)

    for subdirectory in [ "addBackgrounds", "addBackgroundLeptonFakes", "prepareDatacards", "addSystFakeRates", "makePlots" ]:
      key_dir = getKey(subdirectory)
      for dir_type in [ DKEY_CFGS, DKEY_HIST, DKEY_LOGS, DKEY_DCRD, DKEY_PLOT ]:
        initDict(self.dirs, [ key_dir, dir_type ])
        if dir_type in [ DKEY_CFGS, DKEY_LOGS, DKEY_DCRD, DKEY_PLOT ]:
          self.dirs[key_dir][dir_type] = os.path.join(self.configDir, dir_type, self.channel, subdirectory)
        else:
          self.dirs[key_dir][dir_type] = os.path.join(self.outputDir, dir_type, self.channel, subdirectory)
    for dir_type in [ DKEY_CFGS, DKEY_SCRIPTS, DKEY_HIST, DKEY_LOGS, DKEY_DCRD, DKEY_PLOT, DKEY_HADD_RT, DKEY_SYNC ]:
      if dir_type == DKEY_SYNC and not self.do_sync:
        continue
      initDict(self.dirs, [ dir_type ])
      if dir_type in [ DKEY_CFGS, DKEY_SCRIPTS, DKEY_LOGS, DKEY_DCRD, DKEY_PLOT, DKEY_HADD_RT ]:
        self.dirs[dir_type] = os.path.join(self.configDir, dir_type, self.channel)
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
          if not sample_info["use_it"]:
            continue
          process_name = sample_info["process_name_specific"]
          logging.info("Creating configuration files to run '%s' for sample %s" % (self.executable_analyze, process_name))
          inputFileList = inputFileLists[sample_name]

          sample_category = sample_info["sample_category"]
          is_mc = (sample_info["type"] == "mc")
          use_th_weights = self.runTHweights(sample_info)

          central_or_shift_dedicated = self.central_or_shifts if use_th_weights else self.central_or_shifts_external
          for central_or_shift in central_or_shift_dedicated:
            if not self.accept_systematics(
                central_or_shift, is_mc, lepton_selection, sample_info
            ):
              continue

            central_or_shifts_local = []
            if central_or_shift == "central" and not use_th_weights:
              for central_or_shift_local in self.central_or_shifts_internal:
                if self.accept_systematics(
                    central_or_shift_local, is_mc, lepton_selection, sample_info
                ):
                  central_or_shifts_local.append(central_or_shift_local)

            logging.info(" ... for '%s' and systematic uncertainty option '%s'" % (lepton_selection_and_frWeight, central_or_shift))

            # build config files for executing analysis code
            key_analyze_dir = getKey(process_name, lepton_selection_and_frWeight, central_or_shift)

            for jobId in inputFileList.keys():
              analyze_job_tuple = (process_name, lepton_selection_and_frWeight, central_or_shift, jobId)
              key_analyze_job = getKey(*analyze_job_tuple)
              ntupleFiles = inputFileList[jobId]
              if len(ntupleFiles) == 0:
                logging.warning("No input ntuples for %s --> skipping job !!" % (key_analyze_job))
                continue

              syncOutput = ''
              syncTree = ''
              if self.do_sync:
                mcClosure_match = mcClosure_regex.match(lepton_selection_and_frWeight)
                if lepton_selection_and_frWeight == 'Tight':
                  syncOutput = os.path.join(self.dirs[key_analyze_dir][DKEY_SYNC], '%s_%s_SR.root' % (self.channel, central_or_shift))
                  syncTree = 'syncTree_%s_SR' % self.channel.replace('_', '')
                elif lepton_selection_and_frWeight == 'Fakeable_wFakeRateWeights':
                  syncOutput = os.path.join(self.dirs[key_analyze_dir][DKEY_SYNC], '%s_%s_Fake.root' % (self.channel, central_or_shift))
                  syncTree = 'syncTree_%s_Fake' % self.channel.replace('_', '')
                elif mcClosure_match:
                  mcClosure_type = mcClosure_match.group('type')
                  syncOutput = os.path.join(self.dirs[key_analyze_dir][DKEY_SYNC], '%s_%s_mcClosure_%s.root' % (self.channel, central_or_shift, mcClosure_type))
                  syncTree = 'syncTree_%s_mcClosure_%s' % (self.channel.replace('_', ''), mcClosure_type)
                else:
                  continue
              if syncTree and central_or_shift != "central":
                syncTree = os.path.join(central_or_shift, syncTree)
              syncRLE = ''
              if self.do_sync and self.rle_select:
                syncRLE = self.rle_select % syncTree
                if not os.path.isfile(syncRLE):
                  logging.warning("Input RLE file for the sync is missing: %s; skipping the job" % syncRLE)
                  continue
              if syncOutput:
                self.inputFiles_sync['sync'].append(syncOutput)

              cfgFile_modified_path = os.path.join(self.dirs[key_analyze_dir][DKEY_CFGS], "analyze_%s_%s_%s_%i_cfg.py" % analyze_job_tuple)
              histogramFile_path = os.path.join(self.dirs[key_analyze_dir][DKEY_HIST], "analyze_%s_%s_%s_%i.root" % analyze_job_tuple)
              logFile_path = os.path.join(self.dirs[key_analyze_dir][DKEY_LOGS], "analyze_%s_%s_%s_%i.log" % analyze_job_tuple)
              rleOutputFile_path = os.path.join(self.dirs[key_analyze_dir][DKEY_RLES], "rle_%s_%s_%s_%i.txt" % analyze_job_tuple) \
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
                'apply_leptonGenMatching'  : self.apply_leptonGenMatching,
                'apply_hadTauVeto'         : self.apply_hadTauVeto,
                'hadTauSelection_veto'     : self.hadTau_mva_wp_veto,
                'applyFakeRateWeights'     : applyFakeRateWeights,
                'apply_pileupJetID'        : self.apply_pileupJetID,
                'central_or_shift'         : central_or_shift,
                'central_or_shifts_local'  : central_or_shifts_local,
                'evtCategories'            : self.evtCategories,
                'selectBDT'                : self.isBDTtraining,
                'secondBDT'                : self.second_bdt,
                'doDataMCPlots'            : self.doDataMCPlots,
                'syncOutput'               : syncOutput,
                'syncTree'                 : syncTree,
                'syncRLE'                  : syncRLE,
                'apply_hlt_filter'         : self.hlt_filter,
                'useNonNominal'            : self.use_nonnominal,
                'fillGenEvtHistograms'     : True,
                'useAssocJetBtag'          : self.do_sync,
              }
              self.createCfg_analyze(self.jobOptions_analyze[key_analyze_job], sample_info, lepton_selection)

              # initialize input and output file names for hadd_stage1
              key_hadd_stage1_dir = getKey(process_name, lepton_selection_and_frWeight, "hadd")
              hadd_stage1_job_tuple = (process_name, lepton_selection_and_frWeight)
              key_hadd_stage1_job = getKey(*hadd_stage1_job_tuple)
              if not key_hadd_stage1_job in self.inputFiles_hadd_stage1:
                self.inputFiles_hadd_stage1[key_hadd_stage1_job] = []
              self.inputFiles_hadd_stage1[key_hadd_stage1_job].append(self.jobOptions_analyze[key_analyze_job]['histogramFile'])
              self.outputFile_hadd_stage1[key_hadd_stage1_job] = os.path.join(self.dirs[key_hadd_stage1_dir][DKEY_HIST], "hadd_stage1_%s_%s.root" % hadd_stage1_job_tuple)

          if self.isBDTtraining or self.do_sync:
            continue

          #----------------------------------------------------------------------------
          # split hadd_stage1 files into separate files, one for each event category
          for category in self.evtCategories:
            key_hadd_stage1_job = getKey(process_name, lepton_selection_and_frWeight)
            key_copyHistograms_dir = getKey(process_name, lepton_selection_and_frWeight, "copyHistograms")
            copyHistograms_job_tuple = (category, process_name, lepton_selection_and_frWeight)
            key_copyHistograms_job = getKey(*copyHistograms_job_tuple)
            cfgFile_modified = os.path.join(self.dirs[key_copyHistograms_dir][DKEY_CFGS], "copyHistograms_%s_%s_%s_cfg.py" % copyHistograms_job_tuple)
            outputFile = os.path.join(self.dirs[key_copyHistograms_dir][DKEY_HIST], "copyHistograms_%s_%s_%s.root" % copyHistograms_job_tuple)
            self.jobOptions_copyHistograms[key_copyHistograms_job] = {
              'inputFile' : self.outputFile_hadd_stage1[key_hadd_stage1_job],
              'cfgFile_modified' : cfgFile_modified,
              'outputFile' : outputFile,
              'logFile' : os.path.join(self.dirs[key_copyHistograms_dir][DKEY_LOGS], os.path.basename(cfgFile_modified).replace("_cfg.py", ".log")),
              'categories' :[ category + "_" + lepton_selection_and_frWeight ],
            }
            self.createCfg_copyHistograms(self.jobOptions_copyHistograms[key_copyHistograms_job])
          #----------------------------------------------------------------------------

          # add output files of copyHistograms jobs to list of input files for hadd_stage1_5
          for category in self.evtCategories:
            key_copyHistograms_job = getKey(category, process_name, lepton_selection_and_frWeight)
            key_hadd_stage1_5_dir = getKey("hadd", lepton_selection_and_frWeight)
            hadd_stage1_5_job_tuple = (category, lepton_selection_and_frWeight)
            key_hadd_stage1_5_job = getKey(*hadd_stage1_5_job_tuple)
            if not key_hadd_stage1_5_job in self.inputFiles_hadd_stage1_5:
              self.inputFiles_hadd_stage1_5[key_hadd_stage1_5_job] = []
            self.inputFiles_hadd_stage1_5[key_hadd_stage1_5_job].append(self.jobOptions_copyHistograms[key_copyHistograms_job]['outputFile'])
            self.outputFile_hadd_stage1_5[key_hadd_stage1_5_job] = os.path.join(self.dirs[key_hadd_stage1_5_dir][DKEY_HIST],
                                                                        "hadd_stage1_5_%s_%s.root" % hadd_stage1_5_job_tuple)

        if self.isBDTtraining or self.do_sync:
          continue

        for category in self.evtCategories:
          # sum fake background contributions for the total of all MC sample
          # input processes: TT_fake, TTW_fake, TTWW_fake, ...
          # output process: fakes_mc
          key_hadd_stage1_5_job = getKey(category, lepton_selection_and_frWeight)
          key_addBackgrounds_dir = getKey("addBackgrounds")
          addBackgrounds_job_fakes_tuple = ("fakes_mc", category, lepton_selection_and_frWeight)
          key_addBackgrounds_job_fakes = getKey(*addBackgrounds_job_fakes_tuple)
          sample_categories = []
          sample_categories.extend(self.nonfake_backgrounds)
          processes_input = []
          for sample_category in sample_categories:
            processes_input.append("%s_fake" % sample_category)
          self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_fakes] = {
            'inputFile' : self.outputFile_hadd_stage1_5[key_hadd_stage1_5_job],
            'cfgFile_modified' : os.path.join(self.dirs[key_addBackgrounds_dir][DKEY_CFGS], "addBackgrounds_%s_%s_%s_cfg.py" % addBackgrounds_job_fakes_tuple),
            'outputFile' : os.path.join(self.dirs[key_addBackgrounds_dir][DKEY_HIST], "addBackgrounds_%s_%s_%s.root" % addBackgrounds_job_fakes_tuple),
            'logFile' : os.path.join(self.dirs[key_addBackgrounds_dir][DKEY_LOGS], "addBackgrounds_%s_%s_%s.log" % addBackgrounds_job_fakes_tuple),
            'categories' : [ getHistogramDir(category, lepton_selection, lepton_frWeight) ],
            'processes_input' : processes_input,
            'process_output' : "fakes_mc"
          }
          self.createCfg_addBackgrounds(self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_fakes])

          # sum conversion background contributions for the total of all MC sample
          # input processes: TT_Convs, TTW_Convs, TTWW_Convs, ...
          # output process: Convs
          addBackgrounds_job_Convs_tuple = ("Convs", category, lepton_selection)
          key_addBackgrounds_job_Convs = getKey(*addBackgrounds_job_Convs_tuple)
          sample_categories = []
          sample_categories.extend(self.nonfake_backgrounds)
          processes_input = []
          for sample_category in self.convs_backgrounds:
            processes_input.append("%s_Convs" % sample_category)
          self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_Convs] = {
            'inputFile' : self.outputFile_hadd_stage1_5[key_hadd_stage1_5_job],
            'cfgFile_modified' : os.path.join(self.dirs[key_addBackgrounds_dir][DKEY_CFGS], "addBackgrounds_%s_%s_%s_cfg.py" % addBackgrounds_job_Convs_tuple),
            'outputFile' : os.path.join(self.dirs[key_addBackgrounds_dir][DKEY_HIST], "addBackgrounds_%s_%s_%s.root" % addBackgrounds_job_Convs_tuple),
            'logFile' : os.path.join(self.dirs[key_addBackgrounds_dir][DKEY_LOGS], "addBackgrounds_%s_%s_%s.log" % addBackgrounds_job_Convs_tuple),
            'categories' : [ getHistogramDir(category, lepton_selection, lepton_frWeight) ],
            'processes_input' : processes_input,
            'process_output' : "Convs"
          }
          self.createCfg_addBackgrounds(self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_Convs])

          # sum signal contributions from gluon fusion and VBF HH production,
          # separately for "nonfake" and "fake" contributions
          genMatch_categories = [ "nonfake", "fake" ]
          for genMatch_category in genMatch_categories:
            for signal_base, signal_input in self.signal_io.items():
              addBackgrounds_job_signal_tuple = (category, lepton_selection, signal_base, genMatch_category)
              key_addBackgrounds_job_signal = getKey(*addBackgrounds_job_signal_tuple)
              if key_addBackgrounds_job_signal in self.jobOptions_addBackgrounds_sum.keys():
                continue
              processes_input = signal_input
              process_output = signal_base
              if genMatch_category == "fake":
                processes_input = [ process_input + "_fake" for process_input in processes_input ]
                process_output += "_fake"
              self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_signal] = {
                'inputFile' : self.outputFile_hadd_stage1_5[key_hadd_stage1_5_job],
                'cfgFile_modified' : os.path.join(self.dirs[key_addBackgrounds_dir][DKEY_CFGS], "addBackgrounds_%s_%s_%s_%s_cfg.py" % addBackgrounds_job_signal_tuple),
                'outputFile' : os.path.join(self.dirs[key_addBackgrounds_dir][DKEY_HIST], "addBackgrounds_%s_%s_%s_%s.root" % addBackgrounds_job_signal_tuple),
                'logFile' : os.path.join(self.dirs[key_addBackgrounds_dir][DKEY_LOGS], "addBackgrounds_%s_%s_%s_%s.log" % addBackgrounds_job_signal_tuple),
                'categories' : [ getHistogramDir(category, lepton_selection, lepton_frWeight) ],
                'processes_input' : processes_input,
                'process_output' : process_output
              }
              self.createCfg_addBackgrounds(self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_signal])
              key_hadd_stage2_job = getKey(category, lepton_selection_and_frWeight)
              if not key_hadd_stage2_job in self.inputFiles_hadd_stage2:
                self.inputFiles_hadd_stage2[key_hadd_stage2_job] = []
              if lepton_selection == "Tight":
                self.inputFiles_hadd_stage2[key_hadd_stage2_job].append(self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_signal]['outputFile'])

          # initialize input and output file names for hadd_stage2
          key_hadd_stage1_5_job = getKey(category, lepton_selection_and_frWeight)
          key_hadd_stage2_dir = getKey("hadd", lepton_selection_and_frWeight)
          hadd_stage2_job_tuple = (category, lepton_selection_and_frWeight)
          key_hadd_stage2_job = getKey(*hadd_stage2_job_tuple)
          if not key_hadd_stage2_job in self.inputFiles_hadd_stage2:
            self.inputFiles_hadd_stage2[key_hadd_stage2_job] = []
          if lepton_selection == "Tight":
            self.inputFiles_hadd_stage2[key_hadd_stage2_job].append(self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_fakes]['outputFile'])
            self.inputFiles_hadd_stage2[key_hadd_stage2_job].append(self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_Convs]['outputFile'])
          self.inputFiles_hadd_stage2[key_hadd_stage2_job].append(self.outputFile_hadd_stage1_5[key_hadd_stage1_5_job])
          self.outputFile_hadd_stage2[key_hadd_stage2_job] = os.path.join(self.dirs[key_hadd_stage2_dir][DKEY_HIST],
                                                                          "hadd_stage2_%s_%s.root" % hadd_stage2_job_tuple)

    if self.isBDTtraining or self.do_sync:
      if self.is_sbatch:
        logging.info("Creating script for submitting '%s' jobs to batch system" % self.executable_analyze)
        self.sbatchFile_analyze = os.path.join(self.dirs[DKEY_SCRIPTS], "sbatch_analyze_%s.py" % self.channel)
        if self.isBDTtraining:
          self.createScript_sbatch_analyze(self.executable_analyze, self.sbatchFile_analyze, self.jobOptions_analyze)
        elif self.do_sync:
          self.createScript_sbatch_syncNtuple(self.executable_analyze, self.sbatchFile_analyze, self.jobOptions_analyze)
      logging.info("Creating Makefile")
      lines_makefile = []
      if self.isBDTtraining:
        self.addToMakefile_analyze(lines_makefile)
        self.addToMakefile_hadd_stage1(lines_makefile)
      elif self.do_sync:
        self.addToMakefile_syncNtuple(lines_makefile)
        outputFile_sync_path = os.path.join(self.outputDir, DKEY_SYNC, '%s.root' % self.channel)
        self.outputFile_sync['sync'] = outputFile_sync_path
        self.addToMakefile_hadd_sync(lines_makefile)
      else:
        raise ValueError("Internal logic error")
      self.targets.extend(self.phoniesToAdd)
      self.addToMakefile_validate(lines_makefile)
      self.createMakefile(lines_makefile)
      logging.info("Done.")
      return self.num_jobs

    logging.info("Creating configuration files to run 'addBackgroundFakes'")
    for category in self.evtCategories:
      key_hadd_stage1_5_job = getKey(category, get_lepton_selection_and_frWeight("Fakeable", "enabled"))
      key_addFakes_dir = getKey("addBackgroundLeptonFakes")
      addFakes_job_tuple = (category)
      key_addFakes_job = getKey("data_fakes", *addFakes_job_tuple)
      self.jobOptions_addFakes[key_addFakes_job] = {
        'inputFile' : self.outputFile_hadd_stage1_5[key_hadd_stage1_5_job],
        'cfgFile_modified' : os.path.join(self.dirs[key_addFakes_dir][DKEY_CFGS], "addBackgroundLeptonFakes_%s_cfg.py" % addFakes_job_tuple),
          'outputFile' : os.path.join(self.dirs[key_addFakes_dir][DKEY_HIST], "addBackgroundLeptonFakes_%s.root" % addFakes_job_tuple),
          'logFile' : os.path.join(self.dirs[key_addFakes_dir][DKEY_LOGS], "addBackgroundLeptonFakes_%s.log" % addFakes_job_tuple),
          'category_signal' : getHistogramDir(category, "Tight", "disabled"),
          'category_sideband' : getHistogramDir(category, "Fakeable", "enabled")
        }
      self.createCfg_addFakes(self.jobOptions_addFakes[key_addFakes_job])
      key_hadd_stage2_job = getKey(category, get_lepton_selection_and_frWeight("Tight", "disabled"))
      self.inputFiles_hadd_stage2[key_hadd_stage2_job].append(self.jobOptions_addFakes[key_addFakes_job]['outputFile'])

    logging.info("Creating configuration files to run 'prepareDatacards'")
    histogramsToFit = self.histograms_to_fit.keys()
    for category in self.evtCategories:
      for histogramToFit in histogramsToFit:
        logging.info(" ...  for category %s, histogram %s" % (category, histogramToFit))

        prep_dcard_HH = set()
        for sample_name, sample_info in self.samples.items():
          if not sample_info["use_it"]:
            continue
          sample_category = sample_info["sample_category"]
          if sample_category.startswith("signal"):
            sample_category = sample_info["sample_category_hh"]
            doAdd = False
            if "BDTOutput" in histogramToFit or "MVAOutput" in histogramToFit:
              if ("SM" in histogramToFit or "BM" in histogramToFit) and 'nonresonant' in sample_category:
                doAdd = True
              startpos = histogramToFit.find("MVAOutput_") + len("MVAOutput_")
              endpos = histogramToFit.find("_", startpos)
              massPoint = histogramToFit[startpos:endpos]
              if "spin0" in histogramToFit and "spin0" in sample_category and "_%s_" % massPoint in sample_category:
                doAdd = True
              if "spin2" in histogramToFit and "spin2" in sample_category and "_%s_" % massPoint in sample_category:
                doAdd = True
            else:
              doAdd = True
            if doAdd:
              if "bbvv" in sample_category:
                prep_dcard_HH.add(sample_category.replace("bbvv", "bbzz"))
                prep_dcard_HH.add(sample_category.replace("bbvv", "bbww"))
              elif "bbtt" in sample_category:
                prep_dcard_HH.add(sample_category)
              else:
                raise ValueError("Failed to identify relevant HH decay mode(s) for 'sample_category' = %s !!" % sample_category)
        prep_dcard_HH = list(prep_dcard_HH)
        prep_dcard_H = []
        prep_dcard_other_nonfake_backgrounds = []
        for process in self.nonfake_backgrounds:
          if process in [ "VH", "WH", "ZH", "TH", "TTH", "TTWH", "TTZH", "ggH", "qqH" ]:
            prep_dcard_H.append("%s_hww" % process)
            prep_dcard_H.append("%s_hzz" % process)
            prep_dcard_H.append("%s_htt" % process)
            prep_dcard_H.append("%s_hbb" % process)
          else:
            prep_dcard_other_nonfake_backgrounds.append(process)
        self.prep_dcard_processesToCopy = [ "data_obs" ] + prep_dcard_HH + prep_dcard_H + prep_dcard_other_nonfake_backgrounds + [ "Convs", "data_fakes", "fakes_mc" ]

        key_hadd_stage2_job = getKey(category, get_lepton_selection_and_frWeight("Tight", "disabled"))
        key_prep_dcard_dir = getKey("prepareDatacards")
        prep_dcard_job_tuple = (self.channel, category, histogramToFit)
        key_prep_dcard_job = getKey(category, histogramToFit)
        # CV: Temporary workaround to implement event categories 
        #     implemented in hhAnalysis/bbww/src/EventCategory_hh_bb2l_BDT.cc and hhAnalysis/bbww/src/EventCategory_hh_bb2l_LBN.cc
        #     The datacard extraction for these event categories needs to be implemented more properly later !!
        histogramDir_modified = None
        histogramToFit_modified = None
        cfgFile_modified = None
        datacardFile = None
        datacardCategory = None
        if histogramToFit.find("/") != -1:
          histogramDir_modified = getHistogramDir(category, "Tight", "disabled") + "/" + histogramToFit[:histogramToFit.rfind("/")]
          histogramDir_modified = histogramDir_modified.replace("/$PROCESS", "")
          histogramToFit_modified = histogramToFit[histogramToFit.rfind("/") + 1:]
          # CV: propagate histogram (re)binning options
          self.histograms_to_fit[histogramToFit_modified] = self.histograms_to_fit[histogramToFit]
          suffix = "%s_%s_%s" % (self.channel, category, histogramToFit.replace("/$PROCESS", "").replace("/", "_"))
          cfgFile_modified = os.path.join(self.dirs[key_prep_dcard_dir][DKEY_CFGS], "prepareDatacards_%s_cfg.py" % suffix)
          datacardFile = os.path.join(self.dirs[key_prep_dcard_dir][DKEY_DCRD], "prepareDatacards_%s.root" % suffix)
          datacardCategory = histogramToFit[:histogramToFit.rfind("/$PROCESS")]
          datacardCategory = category + "_" + datacardCategory[datacardCategory.rfind("/") + 1:]
        else:
          histogramDir_modified = getHistogramDir(category, "Tight", "disabled")
          histogramToFit_modified = histogramToFit           
          cfgFile_modified = os.path.join(self.dirs[key_prep_dcard_dir][DKEY_CFGS], "prepareDatacards_%s_%s_%s_cfg.py" % prep_dcard_job_tuple)
          datacardFile = os.path.join(self.dirs[key_prep_dcard_dir][DKEY_DCRD], "prepareDatacards_%s_%s_%s.root" % prep_dcard_job_tuple)
          datacardCategory = category
        self.jobOptions_prep_dcard[key_prep_dcard_job] = {
          'inputFile' : self.outputFile_hadd_stage2[key_hadd_stage2_job],
          'cfgFile_modified' : cfgFile_modified,
          'datacardFile' : datacardFile,
          'histogramDir' : histogramDir_modified,
          'histogramToFit' : histogramToFit_modified,
          'category' : datacardCategory
        }
        self.createCfg_prep_dcard(self.jobOptions_prep_dcard[key_prep_dcard_job])
        # add shape templates for the following systematic uncertainties:
        #  - 'CMS_ttHl_Clos_norm_e'
        #  - 'CMS_ttHl_Clos_shape_e'
        #  - 'CMS_ttHl_Clos_norm_m'
        #  - 'CMS_ttHl_Clos_shape_m'
        key_add_syst_fakerate_dir = getKey("addSystFakeRates")
        add_syst_fakerate_job_tuple = (self.channel, category, histogramToFit)
        key_add_syst_fakerate_job = getKey(category, histogramToFit)
        outputFile = None
        if histogramToFit.find("/") != -1:
          suffix = "%s_%s_%s" % (self.channel, category, histogramToFit.replace("/$PROCESS", "").replace("/", "_"))
          cfgFile_modified = os.path.join(self.dirs[key_add_syst_fakerate_dir][DKEY_CFGS], "addSystFakeRates_%s.py" % suffix)
          outputFile = os.path.join(self.dirs[key_add_syst_fakerate_dir][DKEY_DCRD], "addSystFakeRates_%s.root" % suffix)
        else:
          cfgFile_modified = os.path.join(self.dirs[key_add_syst_fakerate_dir][DKEY_CFGS], "addSystFakeRates_%s_%s_%s_cfg.py" % add_syst_fakerate_job_tuple)
          outputFile = os.path.join(self.dirs[key_add_syst_fakerate_dir][DKEY_DCRD], "addSystFakeRates_%s_%s_%s.root" % add_syst_fakerate_job_tuple)
        self.jobOptions_add_syst_fakerate[key_add_syst_fakerate_job] = {
          'inputFile' : self.jobOptions_prep_dcard[key_prep_dcard_job]['datacardFile'],
          'cfgFile_modified' : cfgFile_modified,
          'outputFile' : outputFile,
          'category' : datacardCategory,
          'histogramToFit' : histogramToFit_modified,
          'plots_outputFileName' : os.path.join(self.dirs[key_add_syst_fakerate_dir][DKEY_PLOT], "addSystFakeRates.png")
        }
        for lepton_type in [ 'e', 'm' ]:
          lepton_mcClosure = "Fakeable_mcClosure_%s" % lepton_type
          if lepton_mcClosure not in self.lepton_selections:
            continue
          lepton_selection_and_frWeight = get_lepton_selection_and_frWeight(lepton_mcClosure, "enabled")
          key_addBackgrounds_job_fakes = getKey("fakes_mc", category, lepton_selection_and_frWeight)
          histogramDir_nominal = histogramDir_modified
          histogramDir_mcClosure = self.mcClosure_dir[lepton_mcClosure]
          histogramDir_mcClosure = histogramDir_mcClosure.replace(self.evtCategory_inclusive, category)
          if histogramToFit.find("/") != -1:
            histogramDir_mcClosure = histogramDir_mcClosure + "/" + histogramToFit[:histogramToFit.rfind("/")]
            histogramDir_mcClosure = histogramDir_mcClosure.replace("/$PROCESS", "fakes_mc")
          else:
            histogramDir_nominal = histogramDir_nominal + "/sel/evt/fakes_mc"
            histogramDir_mcClosure = histogramDir_mcClosure + "/sel/evt/fakes_mc"
          self.jobOptions_add_syst_fakerate[key_add_syst_fakerate_job].update({
            'add_Clos_%s' % lepton_type : ("Fakeable_mcClosure_%s" % lepton_type) in self.lepton_selections,
            'inputFile_nominal_%s' % lepton_type : self.outputFile_hadd_stage2[key_hadd_stage2_job],
            'histogramName_nominal_%s' % lepton_type : "%s/%s" % (histogramDir_nominal, histogramToFit_modified),
            'inputFile_mcClosure_%s' % lepton_type : self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_fakes]['outputFile'],
            'histogramName_mcClosure_%s' % lepton_type : "%s/%s" % (histogramDir_mcClosure, histogramToFit_modified)
          })
        self.createCfg_add_syst_fakerate(self.jobOptions_add_syst_fakerate[key_add_syst_fakerate_job])

    logging.info("Creating configuration files to run 'makePlots'")
    key_hadd_stage2_job = getKey(self.evtCategory_inclusive, get_lepton_selection_and_frWeight("Tight", "disabled"))
    key_makePlots_dir = getKey("makePlots")
    key_makePlots_job = getKey('')
    self.jobOptions_make_plots[key_makePlots_job] = {
        'executable' : self.executable_make_plots,
        'inputFile' : self.outputFile_hadd_stage2[key_hadd_stage2_job],
        'cfgFile_modified' : os.path.join(self.dirs[key_makePlots_dir][DKEY_CFGS], "makePlots_%s_cfg.py" % self.channel),
        'outputFile' : os.path.join(self.dirs[key_makePlots_dir][DKEY_PLOT], "makePlots_%s.png" % self.channel),
        'histogramDir' : getHistogramDir(self.evtCategory_inclusive, "Tight", "disabled"),
        'label' : '1l',
        'make_plots_backgrounds' : self.make_plots_backgrounds
      }
    self.createCfg_makePlots(self.jobOptions_make_plots[key_makePlots_job])
    if "Fakeable_mcClosure" in self.lepton_selections: #TODO
        key_hadd_stage2_job = getKey(self.evtCategory_inclusive, get_lepton_selection_and_frWeight("Tight", "disabled"))
        key_makePlots_job = getKey('')
        self.jobOptions_make_plots[key_makePlots_job] = {
          'executable' : self.executable_make_plots_mcClosure,
          'inputFile' : self.outputFile_hadd_stage2[key_hadd_stage2_job],
          'cfgFile_modified' : os.path.join(self.dirs[key_makePlots_dir][DKEY_CFGS], "makePlots_mcClosure_%s_cfg.py" % self.channel),
          'outputFile' : os.path.join(self.dirs[key_makePlots_dir][DKEY_PLOT], "makePlots_mcClosure_%s.png" % self.channel)
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
    self.addToMakefile_copyHistograms(lines_makefile, make_target = "phony_copyHistograms", make_dependency = "phony_hadd_stage1")
    self.addToMakefile_backgrounds_from_data(lines_makefile, make_dependency = "phony_copyHistograms")
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
    self.addToMakefile_validate(lines_makefile)
    self.createMakefile(lines_makefile)

    logging.info("Done")

    return self.num_jobs
