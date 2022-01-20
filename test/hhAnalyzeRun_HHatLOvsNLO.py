#!/usr/bin/env python

from hhAnalysis.bbww.configs.analyzeConfig_HHatLOvsNLO import analyzeConfig_HHatLOvsNLO
from tthAnalysis.HiggsToTauTau.jobTools import query_yes_no
from tthAnalysis.HiggsToTauTau.analysisSettings import get_lumi
from tthAnalysis.HiggsToTauTau.runConfig import tthAnalyzeParser, filter_samples
from tthAnalysis.HiggsToTauTau.common import logging, load_samples_hh_bbww as load_samples, \
  load_samples_hh_multilepton as load_samples_multilepton, load_samples_stitched

import os
import sys
import getpass

# E.g.: ./test/tthAnalyzeRun_HHatLOvsNLO.py -v 2021Mar21 -m default -e 2017

mode_choices = [ 'bbww', 'multilepton' ]

parser = tthAnalyzeParser()
parser.add_modes(mode_choices, default = 'bbww')
parser.add_preselect(use_preselected = False)
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
use_preselected   = args.use_preselected
files_per_job     = args.files_per_job
use_home          = args.use_home

lumi = get_lumi(era)

load_samples_func = None
if mode == 'bbww':
  load_samples_func = load_samples
elif mode == 'multilepton':
  load_samples_func = load_samples_multilepton
else:
  assert(False)

samples = load_samples_func(era, suffix = "preselected" if use_preselected else "")

for sample_name, sample_info in samples.items():
  if sample_name == 'sum_events':
    continue
  if not 'signal_ggf_nonresonant' in sample_info['sample_category']:
    sample_info["use_it"] = False

if __name__ == '__main__':
  if not use_preselected:
    logging.warning('Running the analysis on fully inclusive samples!')

  if sample_filter:
    samples = filter_samples(samples, sample_filter)

  analysis = analyzeConfig_HHatLOvsNLO(
    configDir = os.path.join("/scratch-persistent", getpass.getuser(), "hhAnalysis", era, version),
    localDir  = os.path.join("/home",               getpass.getuser(), "hhAnalysis", era, version),
    outputDir = os.path.join("/hdfs/local",         getpass.getuser(), "hhAnalysis", era, version),
    executable_analyze = "analyze_HHatLOvsNLO",
    cfgFile_analyze    = "analyze_HHatLOvsNLO_cfg.py",
    samples            = samples,
    max_files_per_job  = files_per_job,
    era                = era,
    use_lumi           = True,
    lumi               = lumi,
    check_output_files = check_output_files,
    running_method     = running_method,
    num_parallel_jobs  = num_parallel_jobs,
    dry_run            = dry_run,
    isDebug            = debug,
    use_home           = use_home,
    submission_cmd     = sys.argv,
  )

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
