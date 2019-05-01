#!/usr/bin/env python

from hhAnalysis.bbww.configs.analyzeConfig_hh_bb1l import analyzeConfig_hh_bb1l
from tthAnalysis.HiggsToTauTau.jobTools import query_yes_no
from tthAnalysis.HiggsToTauTau.analysisSettings import systematics, get_lumi
from tthAnalysis.HiggsToTauTau.runConfig import tthAnalyzeParser, filter_samples
from tthAnalysis.HiggsToTauTau.common import logging, load_samples_hh_bbww as load_samples

import os
import sys
import getpass
import importlib

# E.g.: ./test/tthAnalyzeRun_hh_bb1l.py -v 2017Dec13 -m default -e 2017

mode_choices     = [ 'default', 'forBDTtraining' ]
sys_choices      = [ 'full' ] + systematics.an_extended_opts_hh
systematics.full = systematics.an_extended_hh

parser = tthAnalyzeParser()
parser.add_modes(mode_choices)
parser.add_sys(sys_choices)
parser.add_preselect()
parser.add_nonnominal()
parser.add_tau_id_wp()
parser.add_hlt_filter()
parser.add_files_per_job() 
parser.add_use_home()
parser.add_lep_mva_wp()
args = parser.parse_args()

# Common arguments
era                = args.era
version            = args.version
dry_run            = args.dry_run
no_exec            = args.no_exec
auto_exec          = args.auto_exec
check_output_files = not args.not_check_input_files
debug              = args.debug
sample_filter      = args.filter
num_parallel_jobs  = args.num_parallel_jobs
running_method     = args.running_method

# Additional arguments
mode              = args.mode
systematics_label = args.systematics
use_preselected   = args.use_preselected
use_nonnominal    = args.original_central
hlt_filter        = args.hlt_filter
files_per_job     = args.files_per_job
use_home          = args.use_home
lep_mva_wp        = args.lep_mva_wp

# Use the arguments
central_or_shifts = []

for systematic_label in systematics_label:
  for central_or_shift in getattr(systematics, systematic_label):
    if central_or_shift not in central_or_shifts:
      central_or_shifts.append(central_or_shift)
lumi = get_lumi(era)

samples_to_stitch = getattr(
  importlib.import_module("tthAnalysis.HiggsToTauTau.samples.stitch_{}".format(era)),
  "samples_to_stitch_{}".format(era)
)

if mode == "default":
  samples = load_samples(era)

  # [*] use binned DY samples in BDT training
  dy_samples_inclusive = []
  dy_samples_binned = []
  for sample_set in samples_to_stitch:
    for sample_key, sample_value in sample_set.items():
      if sample_key == 'inclusive':
        dy_inclusive_samples = list(filter(lambda sample_name: sample_name.startswith('DY'), sample_value['samples']))
        dy_samples_inclusive.extend(dy_inclusive_samples)
      else:
        for sample_binned_value in sample_value:
          dy_binned_samples = list(
            filter(lambda sample_name: sample_name.startswith('DY'), sample_binned_value['samples']))
          dy_samples_binned.extend(dy_binned_samples)

  wjets_samples_inclusive = []
  wjets_samples_binned = []
  for sample_set in samples_to_stitch:
    for sample_key, sample_value in sample_set.items():
      if sample_key == 'inclusive':
        wjets_inclusive_samples = list(filter(lambda sample_name: sample_name.startswith('W'), sample_value['samples']))
        wjets_samples_inclusive.extend(wjets_inclusive_samples)
      else:
        for sample_binned_value in sample_value:
          wjets_binned_samples = list(
            filter(lambda sample_name: sample_name.startswith('W'), sample_binned_value['samples']))
          wjets_samples_binned.extend(wjets_binned_samples)

  for sample_name, sample_info in samples.items():
    if sample_name == 'sum_events': continue
    if sample_info["process_name_specific"] in [
      "TTTo2L2Nu_PSweights", "TTToSemiLeptonic_PSweights", "TTToHadronic_PSweights",
    ]:
      # Use non-PSweights samples for the analysis to estimate the irreducible ttbar background
      sample_info["use_it"] = False
    elif sample_info["process_name_specific"] in dy_samples_binned or sample_info["process_name_specific"] in wjets_samples_binned:
      sample_info["use_it"] = False  # [*]                                                                                                                                                                  
    elif sample_info["process_name_specific"] in dy_samples_inclusive or sample_info["process_name_specific"] in wjets_samples_inclusive:
      sample_info["use_it"] = True  # [*]                  

elif mode == "forBDTtraining":
  samples = load_samples(era, suffix = "BDT")

   # [*] use binned DY samples in BDT training
  dy_samples_inclusive = []
  dy_samples_binned = []
  for sample_set in samples_to_stitch:
    for sample_key, sample_value in sample_set.items():
      if sample_key == 'inclusive':
        dy_inclusive_samples = list(filter(lambda sample_name: sample_name.startswith('DY'), sample_value['samples']))
        dy_samples_inclusive.extend(dy_inclusive_samples)
      else:
        for sample_binned_value in sample_value:
          dy_binned_samples = list(
            filter(lambda sample_name: sample_name.startswith('DY'), sample_binned_value['samples'])
          )
          dy_samples_binned.extend(dy_binned_samples)

  wjets_samples_inclusive = []
  wjets_samples_binned = []
  for sample_set in samples_to_stitch:
    for sample_key, sample_value in sample_set.items():
      if sample_key == 'inclusive':
        wjets_inclusive_samples = list(filter(lambda sample_name: sample_name.startswith('W'), sample_value['samples']))
        wjets_samples_inclusive.extend(wjets_inclusive_samples)
      else:
        for sample_binned_value in sample_value:
          wjets_binned_samples = list(
            filter(lambda sample_name: sample_name.startswith('W'), sample_binned_value['samples'])
          )
          wjets_samples_binned.extend(wjets_binned_samples)

  for sample_name, sample_info in samples.items():
    if sample_name == 'sum_events': continue
    if sample_info["process_name_specific"] in [
      "TTTo2L2Nu", "TTToSemiLeptonic", "TTToHadronic",
    ]:
      # Use PSweights samples only for BDT training
      sample_info["use_it"] = False
    elif sample_info["process_name_specific"] in dy_samples_binned or sample_info["process_name_specific"] in wjets_samples_binned:
      sample_info["use_it"] = True  # [*]
    elif sample_info["process_name_specific"] in dy_samples_inclusive or sample_info["process_name_specific"] in wjets_samples_inclusive:
      sample_info["use_it"] = False  # [*]        
else:
  raise ValueError("Internal logic error")

if mode == "default" and len(central_or_shifts) <= 1:
  evtCategories = [
    "hh_bb1l", "hh_bb1l_resolvedHbb_resolvedWjj", "hh_bb1l_resolvedHbb_resolvedWjj_vbf", "hh_bb1l_resolvedHbb_resolvedWjj_nonvbf",
    "hh_bb1l_boostedHbb_resolvedWjj", "hh_bb1l_boostedHbb_boostedWjj_lowPurity", "hh_bb1l_boostedHbb_boostedWjj_highPurity", "hh_bb1l_vbf", "hh_bb1l_nonvbf",
    "hh_2bM1l", "hh_2bM1l_resolvedHbb_resolvedWjj", "hh_2bM1l_resolvedHbb_resolvedWjj_vbf", "hh_2bM1l_resolvedHbb_resolvedWjj_nonvbf",
    "hh_2bM1l_boostedHbb_resolvedWjj", "hh_2bM1l_boostedHbb_boostedWjj_lowPurity", "hh_2bM1l_boostedHbb_boostedWjj_highPurity", "hh_2bM1l_vbf", "hh_2bM1l_nonvbf",
    "hh_1bM1bL1l", "hh_1bM1bL1l_resolvedHbb_resolvedWjj", "hh_1bM1bL1l_resolvedHbb_resolvedWjj_vbf", "hh_1bM1bL1l_resolvedHbb_resolvedWjj_nonvbf",
    "hh_1bM1bL1l_boostedHbb_resolvedWjj", "hh_1bM1bL1l_boostedHbb_boostedWjj_lowPurity", "hh_1bM1bL1l_boostedHbb_boostedWjj_highPurity", "hh_1bM1bL1l_vbf", "hh_1bM1bL1l_nonvbf",
    "hh_1bM1l", "hh_1bM1l_resolvedHbb_resolvedWjj", "hh_1bM1l_resolvedHbb_resolvedWjj_vbf", "hh_1bM1l_resolvedHbb_resolvedWjj_nonvbf",
    "hh_1bM1l_boostedHbb_resolvedWjj", "hh_bb1l_boostedHbb_boostedWjj_lowPurity", "hh_1bM1l_boostedHbb_boostedWjj_highPurity", "hh_1bM1l_vbf", "hh_1bM1l_nonvbf",
    "hh_bb1e", "hh_bb1e_resolvedHbb_resolvedWjj", "hh_bb1e_resolvedHbb_resolvedWjj_vbf", "hh_bb1e_resolvedHbb_resolvedWjj_nonvbf",
    "hh_bb1e_boostedHbb_resolvedWjj", "hh_bb1e_boostedHbb_boostedWjj_lowPurity", "hh_bb1e_boostedHbb_boostedWjj_highPurity", "hh_bb1e_vbf", "hh_bb1e_nonvbf",
    "hh_2bM1e", "hh_2bM1e_resolvedHbb_resolvedWjj", "hh_2bM1e_resolvedHbb_resolvedWjj_vbf", "hh_2bM1e_resolvedHbb_resolvedWjj_nonvbf",
    "hh_2bM1e_boostedHbb_resolvedWjj", "hh_2bM1e_boostedHbb_boostedWjj_lowPurity", "hh_2bM1e_boostedHbb_boostedWjj_highPurity", "hh_2bM1e_vbf", "hh_2bM1e_nonvbf",
    "hh_1bM1bL1e", "hh_1bM1bL1e_resolvedHbb_resolvedWjj", "hh_1bM1bL1e_resolvedHbb_resolvedWjj_vbf", "hh_1bM1bL1e_resolvedHbb_resolvedWjj_nonvbf",
    "hh_1bM1bL1e_boostedHbb_resolvedWjj", "hh_1bM1bL1e_boostedHbb_boostedWjj_lowPurity", "hh_1bM1bL1e_boostedHbb_boostedWjj_highPurity", "hh_1bM1bL1e_vbf", "hh_1bM1bL1e_nonvbf",
    "hh_1bM1e", "hh_1bM1e_resolvedHbb_resolvedWjj", "hh_1bM1e_resolvedHbb_resolvedWjj_vbf", "hh_1bM1e_resolvedHbb_resolvedWjj_nonvbf",
    "hh_1bM1e_boostedHbb_resolvedWjj", "hh_bb1e_boostedHbb_boostedWjj_lowPurity", "hh_1bM1e_boostedHbb_boostedWjj_highPurity", "hh_1bM1e_vbf", "hh_1bM1e_nonvbf",
    "hh_bb1mu", "hh_bb1mu_resolvedHbb_resolvedWjj", "hh_bb1mu_resolvedHbb_resolvedWjj_vbf", "hh_bb1mu_resolvedHbb_resolvedWjj_nonvbf",
    "hh_bb1mu_boostedHbb_resolvedWjj", "hh_bb1mu_boostedHbb_boostedWjj_lowPurity", "hh_bb1mu_boostedHbb_boostedWjj_highPurity", "hh_bb1mu_vbf", "hh_bb1mu_nonvbf",
    "hh_2bM1mu", "hh_2bM1mu_resolvedHbb_resolvedWjj", "hh_2bM1mu_resolvedHbb_resolvedWjj_vbf", "hh_2bM1mu_resolvedHbb_resolvedWjj_nonvbf",
    "hh_2bM1mu_boostedHbb_resolvedWjj", "hh_2bM1mu_boostedHbb_boostedWjj_lowPurity", "hh_2bM1mu_boostedHbb_boostedWjj_highPurity", "hh_2bM1mu_vbf", "hh_2bM1mu_nonvbf",
    "hh_1bM1bL1mu", "hh_1bM1bL1mu_resolvedHbb_resolvedWjj", "hh_1bM1bL1mu_resolvedHbb_resolvedWjj_vbf", "hh_1bM1bL1mu_resolvedHbb_resolvedWjj_nonvbf",
    "hh_1bM1bL1mu_boostedHbb_resolvedWjj", "hh_1bM1bL1mu_boostedHbb_boostedWjj_lowPurity", "hh_1bM1bL1mu_boostedHbb_boostedWjj_highPurity", "hh_1bM1bL1mu_vbf", "hh_1bM1bL1mu_nonvbf",
    "hh_1bM1mu", "hh_1bM1mu_resolvedHbb_resolvedWjj", "hh_1bM1mu_resolvedHbb_resolvedWjj_vbf", "hh_1bM1mu_resolvedHbb_resolvedWjj_nonvbf",
    "hh_1bM1mu_boostedHbb_resolvedWjj", "hh_bb1mu_boostedHbb_boostedWjj_lowPurity", "hh_1bM1mu_boostedHbb_boostedWjj_highPurity", "hh_1bM1mu_vbf", "hh_1bM1mu_nonvbf"
  ]
else:
  evtCategories = [
    "hh_bb1l", "hh_bb1l_resolvedHbb_resolvedWjj", "hh_bb1l_boostedHbb_resolvedWjj", "hh_bb1l_boostedHbb_boostedWjj_lowPurity", "hh_bb1l_boostedHbb_boostedWjj_highPurity"
  ]

hadTau_mva_wp_veto = "dR03mvaMedium"

if __name__ == '__main__':
  logging.info(
    "Running the jobs with the following systematic uncertainties enabled: %s" % \
    ', '.join(central_or_shifts)
  )
  if not use_preselected:
    logging.warning('Running the analysis on fully inclusive samples!')

  if sample_filter:
    samples = filter_samples(samples, sample_filter)

  if args.tau_id_wp:
    logging.info("Changing tau ID working point: %s -> %s" % (hadTau_mva_wp_veto, args.tau_id_wp))
    hadTau_mva_wp_veto = args.tau_id_wp

  analysis = analyzeConfig_hh_bb1l(
    configDir = os.path.join("/home",       getpass.getuser(), "hhAnalysis", era, version),
    outputDir = os.path.join("/hdfs/local", getpass.getuser(), "hhAnalysis", era, version),
    executable_analyze                    = "analyze_hh_bb1l",
    cfgFile_analyze                       = "analyze_hh_bb1l_cfg.py",
    samples                               = samples,
    lep_mva_wp                            = lep_mva_wp,
    apply_hadTauVeto                      = False,
    hadTau_mva_wp_veto                    = hadTau_mva_wp_veto,
    applyFakeRateWeights                  = "enabled",
    central_or_shifts                     = central_or_shifts,
    evtCategories                         = evtCategories,
    max_files_per_job                     = files_per_job,
    era                                   = era,
    use_lumi                              = True,
    lumi                                  = lumi,
    check_output_files                    = check_output_files,
    running_method                        = running_method,
    num_parallel_jobs                     = num_parallel_jobs,
    executable_addBackgrounds             = "addBackgrounds",
    executable_addFakes                   = "addBackgroundLeptonFakes",
    histograms_to_fit                     = {
      "EventCounter"                      : {},
      "HT"                                : {},
      "STMET"                             : {},
      "MVAOutput_350"                     : {},
      "MVAOutput_400"                     : {},
      "MVAOutput_750"                     : {}
    },
    select_rle_output                     = True,
    dry_run                               = dry_run,
    isDebug                               = debug,
    use_nonnominal                        = use_nonnominal,
    hlt_filter                            = hlt_filter,
    use_home                              = use_home,
  )

  if mode.find("forBDTtraining") != -1:
    analysis.set_BDT_training()

  job_statistics = analysis.create()
  for job_type, num_jobs in job_statistics.items():
    logging.info(" #jobs of type '%s' = %i" % (job_type, num_jobs))

  if auto_exec:
    run_analysis = True
  elif no_exec:
    run_analysis = False
  else:
    run_analysis = query_yes_no("Start jobs ?")
  if run_analysis:
    analysis.run()
  else:
    sys.exit(0)
