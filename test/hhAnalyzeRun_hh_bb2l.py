#!/usr/bin/env python

from hhAnalysis.bbww.configs.analyzeConfig_hh_bb2l import analyzeConfig_hh_bb2l
from tthAnalysis.HiggsToTauTau.jobTools import query_yes_no
from tthAnalysis.HiggsToTauTau.analysisSettings import systematics, get_lumi
from tthAnalysis.HiggsToTauTau.runConfig import tthAnalyzeParser, filter_samples
from tthAnalysis.HiggsToTauTau.common import logging, load_samples_hh_bbww as load_samples

import os
import sys
import getpass
import importlib

# E.g.: ./test/tthAnalyzeRun_hh_bb2l.py -v 2017Dec13 -m default -e 2017

mode_choices     = [ 'default', 'forBDTtraining', 'sync' ]
sys_choices      = [ 'full' ] + systematics.an_extended_opts_hh
systematics.full = systematics.an_extended_hh

parser = tthAnalyzeParser()
parser.add_modes(mode_choices)
parser.add_sys(sys_choices)
parser.add_preselect()
parser.add_rle_select()
parser.add_nonnominal()
parser.add_hlt_filter()
parser.add_files_per_job(5) # CV: need to reduce number of Ntuple files processed per job, as computation of HH mass with HME algorithm takes considerable time
parser.add_use_home()
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
rle_select        = os.path.expanduser(args.rle_select)
use_nonnominal    = args.original_central
hlt_filter        = args.hlt_filter
files_per_job     = args.files_per_job
use_home          = args.use_home

# Use the arguments
central_or_shifts = []
for systematic_label in systematics_label:
  for central_or_shift in getattr(systematics, systematic_label):
    if central_or_shift not in central_or_shifts:
      central_or_shifts.append(central_or_shift)

do_sync = mode.startswith('sync')
lumi = get_lumi(era)

if mode == "default":
  samples_to_stitch = getattr(
    importlib.import_module("tthAnalysis.HiggsToTauTau.samples.stitch_{}".format(era)),
    "samples_to_stitch_{}".format(era)
  )
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

  for sample_name, sample_info in samples.items():
    if sample_name == 'sum_events': continue
    if sample_info["process_name_specific"] in [
      "TTTo2L2Nu_PSweights", "TTToSemiLeptonic_PSweights", "TTToHadronic_PSweights",
    ]:
      # Use non-PSweights samples for the analysis to estimate the irreducible ttbar background
      sample_info["use_it"] = False
    elif sample_info["process_name_specific"] in dy_samples_binned:
      sample_info["use_it"] = False  # [*]
    elif sample_info["process_name_specific"] in dy_samples_inclusive:
      sample_info["use_it"] = True  # [*]

elif mode == "forBDTtraining":
  samples_to_stitch = getattr(
    importlib.import_module("tthAnalysis.HiggsToTauTau.samples.stitch_{}".format(era)),
    "samples_to_stitch_{}".format(era)
  )
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

  for sample_name, sample_info in samples.items():
    if sample_name == 'sum_events': continue
    if sample_info["process_name_specific"] in [
      "TTTo2L2Nu", "TTToSemiLeptonic", "TTToHadronic",
    ]:
      # Use PSweights samples only for BDT training
      sample_info["use_it"] = False
    elif sample_info["process_name_specific"] in dy_samples_binned:
      sample_info["use_it"] = True  # [*]
    elif sample_info["process_name_specific"] in dy_samples_inclusive:
      sample_info["use_it"] = False  # [*]

elif mode == "sync":
  samples = load_samples(era, suffix = "sync")
else:
  raise ValueError("Internal logic error")

evtCategories = None
if mode == "default" and len(central_or_shifts) <= 1:
  evtCategories = [
    "hh_bb2l", "hh_bb2l_resolvedHbb", "hh_bb2l_resolvedHbb_vbf", "hh_bb2l_resolvedHbb_nonvbf", "hh_bb2l_boostedHbb", "hh_bb2l_vbf", "hh_bb2l_nonvbf",
    "hh_2bM2l", "hh_2bM2l_resolvedHbb", "hh_2bM2l_resolvedHbb_nonvbf", "hh_2bM2l_nonvbf",
    "hh_1bM1bL2l", "hh_1bM1bL2l_resolvedHbb", "hh_1bM1bL2l_resolvedHbb_nonvbf", "hh_1bM1bL2l_nonvbf",
    "hh_1bM2l", "hh_1bM2l_resolvedHbb", "hh_1bM2l_resolvedHbb_nonvbf", "hh_1bM2l_nonvbf",
    "hh_bb2e", "hh_bb2e_resolvedHbb", "hh_bb2e_resolvedHbb_vbf", "hh_bb2e_resolvedHbb_nonvbf", "hh_bb2e_boostedHbb", "hh_bb2e_vbf", "hh_bb2e_nonvbf",
    "hh_2bM2e", "hh_2bM2e_resolvedHbb", "hh_2bM2e_resolvedHbb_nonvbf", "hh_2bM2e_nonvbf",
    "hh_1bM1bL2e", "hh_1bM1bL2e_resolvedHbb", "hh_1bM1bL2e_resolvedHbb_nonvbf", "hh_1bM1bL2e_nonvbf",
    "hh_1bM2e", "hh_1bM2e_resolvedHbb", "hh_1bM2e_resolvedHbb_nonvbf", "hh_1bM2e_nonvbf",
    "hh_bb2mu", "hh_bb2mu_resolvedHbb", "hh_bb2mu_resolvedHbb_vbf", "hh_bb2mu_resolvedHbb_nonvbf", "hh_bb2mu_boostedHbb", "hh_bb2mu_vbf", "hh_bb2mu_nonvbf",
    "hh_2bM2mu", "hh_2bM2mu_resolvedHbb", "hh_2bM2mu_resolvedHbb_nonvbf", "hh_2bM2mu_nonvbf",
    "hh_1bM1bL2mu", "hh_1bM1bL2mu_resolvedHbb", "hh_1bM1bL2mu_resolvedHbb_nonvbf", "hh_1bM1bL2mu_nonvbf",
    "hh_1bM2mu", "hh_1bM2mu_resolvedHbb", "hh_1bM2mu_resolvedHbb_nonvbf", "hh_1bM2mu_nonvbf",
    "hh_bb1e1mu", "hh_bb1e1mu_resolvedHbb", "hh_bb1e1mu_resolvedHbb_vbf", "hh_bb1e1mu_resolvedHbb_nonvbf", "hh_bb1e1mu_boostedHbb", "hh_bb1e1mu_vbf", "hh_bb1e1mu_nonvbf",
    "hh_2bM1e1mu", "hh_2bM1e1mu_resolvedHbb", "hh_2bM1e1mu_resolvedHbb_nonvbf", "hh_2bM1e1mu_nonvbf",
    "hh_1bM1bL1e1mu", "hh_1bM1bL1e1mu_resolvedHbb", "hh_1bM1bL1e1mu_resolvedHbb_nonvbf", "hh_1bM1bL1e1mu_nonvbf",
    "hh_1bM1e1mu", "hh_1bM1e1mu_resolvedHbb", "hh_1bM1e1mu_resolvedHbb_nonvbf", "hh_1bM1e1mu_nonvbf"
  ]
else:
  evtCategories = [
    "hh_bb2l", "hh_bb2l_resolvedHbb", "hh_bb2l_boostedHbb"
  ]

if __name__ == '__main__':
  logging.info(
    "Running the jobs with the following systematic uncertainties enabled: %s" % \
    ', '.join(central_or_shifts)
  )
  if not use_preselected:
    logging.warning('Running the analysis on fully inclusive samples!')

  if sample_filter:
    samples = filter_samples(samples, sample_filter)

  analysis = analyzeConfig_hh_bb2l(
    configDir = os.path.join("/home",       getpass.getuser(), "hhAnalysis", era, version),
    outputDir = os.path.join("/hdfs/local", getpass.getuser(), "hhAnalysis", era, version),
    executable_analyze                    = "analyze_hh_bb2l",
    cfgFile_analyze                       = "analyze_hh_bb2l_cfg.py",
    samples                               = samples,
    lepton_charge_selections              = [ "OS", "SS" ],
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
      "MVAOutput_300"                     : {},
      "MVAOutput_400"                     : {},
      "MVAOutput_750"                     : {},
      "MVAOutputnohiggnessnotopness_300"  : {},
      "MVAOutputnohiggnessnotopness_400"  : {},
      "MVAOutputnohiggnessnotopness_750"  : {}

    },
    select_rle_output                     = True,
    dry_run                               = dry_run,
    do_sync                               = do_sync,
    isDebug                               = debug,
    rle_select                            = rle_select,
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
