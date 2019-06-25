#!/usr/bin/env python

from hhAnalysis.bbww.configs.analyzeConfig_hh_bb1l1tau import analyzeConfig_hh_bb1l1tau
from tthAnalysis.HiggsToTauTau.jobTools import query_yes_no
from tthAnalysis.HiggsToTauTau.analysisSettings import systematics, get_lumi
from tthAnalysis.HiggsToTauTau.runConfig import tthAnalyzeParser, filter_samples
from tthAnalysis.HiggsToTauTau.common import logging, load_samples_hh_bbww as load_samples

import os
import sys
import getpass

# E.g.: ./test/tthAnalyzeRun_hh_bb1l1tau.py -v 2017Dec13 -m default -e 2017

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

# Use the arguments
central_or_shifts = []
for systematic_label in systematics_label:
  for central_or_shift in getattr(systematics, systematic_label):
    if central_or_shift not in central_or_shifts:
      central_or_shifts.append(central_or_shift)
lumi = get_lumi(era)

if mode == "default":
  samples = load_samples(era)
elif mode == "forBDTtraining":
  samples = load_samples(era, suffix = "BDT")
else:
  raise ValueError("Internal logic error")

if mode == "default" and len(central_or_shifts) <= 1:
  evtCategories = [
    "hh_bb1l1tau", "hh_bb1l1tau_resolvedHbb", "hh_bb1l1tau_resolvedHbb_vbf", "hh_bb1l1tau_resolvedHbb_nonvbf", "hh_bb1l1tau_boostedHbb", "hh_bb1l1tau_vbf", "hh_bb1l1tau_nonvbf",
    "hh_2bM1l1tau", "hh_2bM1l1tau_resolvedHbb", "hh_2bM1l1tau_resolvedHbb_nonvbf", "hh_2bM1l1tau_nonvbf",
    "hh_1bM1bL1l1tau", "hh_1bM1bL1l1tau_resolvedHbb", "hh_1bM1bL1l1tau_resolvedHbb_nonvbf", "hh_1bM1bL1l1tau_nonvbf",
    "hh_1bM1l1tau", "hh_1bM1l1tau_resolvedHbb", "hh_1bM1l1tau_resolvedHbb_nonvbf", "hh_1bM1l1tau_nonvbf",
    "hh_bb1e1tau", "hh_bb1e1tau_resolvedHbb", "hh_bb1e1tau_resolvedHbb_vbf", "hh_bb1e1tau_resolvedHbb_nonvbf", "hh_bb1e1tau_boostedHbb", "hh_bb1e1tau_vbf", "hh_bb1e1tau_nonvbf",
    "hh_2bM1e1tau", "hh_2bM1e1tau_resolvedHbb", "hh_2bM1e1tau_resolvedHbb_nonvbf", "hh_2bM1e1tau_nonvbf",
    "hh_1bM1bL1e1tau", "hh_1bM1bL1e1tau_resolvedHbb", "hh_1bM1bL1e1tau_resolvedHbb_nonvbf", "hh_1bM1bL1e1tau_nonvbf",
    "hh_1bM1e1tau", "hh_1bM1e1tau_resolvedHbb", "hh_1bM1e1tau_resolvedHbb_nonvbf", "hh_1bM1e1tau_nonvbf",
    "hh_bb1mu1tau", "hh_bb1mu1tau_resolvedHbb", "hh_bb1mu1tau_resolvedHbb_vbf", "hh_bb1mu1tau_resolvedHbb_nonvbf", "hh_bb1mu1tau_boostedHbb", "hh_bb1mu1tau_vbf", "hh_bb1mu1tau_nonvbf",
    "hh_2bM1mu1tau", "hh_2bM1mu1tau_resolvedHbb", "hh_2bM1mu1tau_resolvedHbb_nonvbf", "hh_2bM1mu1tau_nonvbf",
    "hh_1bM1bL1mu1tau", "hh_1bM1bL1mu1tau_resolvedHbb", "hh_1bM1bL1mu1tau_resolvedHbb_nonvbf", "hh_1bM1bL1mu1tau_nonvbf",
    "hh_1bM1mu1tau", "hh_1bM1mu1tau_resolvedHbb", "hh_1bM1mu1tau_resolvedHbb_nonvbf", "hh_1bM1mu1tau_nonvbf"
  ]
else:
  evtCategories = []

hadTau_mva_wp = "dR03mvaMedium"

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
    logging.info("Changing tau ID working point: %s -> %s" % (hadTau_mva_wp , args.tau_id_wp))
    hadTau_mva_wp = args.tau_id_wp

  analysis = analyzeConfig_hh_bb1l1tau(
    configDir = os.path.join("/home",       getpass.getuser(), "hhAnalysis", era, version),
    outputDir = os.path.join("/hdfs/local", getpass.getuser(), "hhAnalysis", era, version),
    executable_analyze                    = "analyze_hh_bb1l1tau",
    cfgFile_analyze                       = "analyze_hh_bb1l1tau_cfg.py",
    samples                               = samples,
    hadTau_mva_wp                         = hadTau_mva_wp,
    chargeSumSelections                   = [ "OS", "SS" ],
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
      "STMET"                             : {}
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
