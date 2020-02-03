#!/usr/bin/env python

from hhAnalysis.bbww.configs.analyzeConfig_hh_bbww_inclusive import analyzeConfig_hh_bbww_inclusive
from tthAnalysis.HiggsToTauTau.jobTools import query_yes_no
from tthAnalysis.HiggsToTauTau.analysisSettings import systematics
from tthAnalysis.HiggsToTauTau.runConfig import tthAnalyzeParser, filter_samples
from tthAnalysis.HiggsToTauTau.common import logging, load_samples_hh_bbww as load_samples

import os
import sys
import getpass

# E.g. to run: ./test/hhAnalyzeRun_inclusive.py -v 2017Dec13 -e 2017 -o syncTree

sys_choices      = [ "full" ] + systematics.an_inclusive_opts
systematics.full = systematics.an_inclusive

parser = tthAnalyzeParser()
parser.add_sys(sys_choices)
parser.add_rle_select()
parser.add_nonnominal()
parser.add_use_home()
parser.add_tau_id() # compatibility with sync Ntuple workflow, otherwise ignored
parser.add_jet_cleaning()
parser.add_gen_matching()
parser.enable_regrouped_jec()
parser.add_argument('-o', '--output-tree',
  type = str, dest = 'output_tree', metavar = 'name', default = 'syncTree', required = False,
  help = 'R|Output TTree name',
)
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
running_method     = args.running_method

# Additional arguments
rle_select        = os.path.expanduser(args.rle_select)
systematics_label = args.systematics
use_nonnominal    = args.original_central
use_home          = args.use_home
jet_cleaning      = args.jet_cleaning
gen_matching      = args.gen_matching
regroup_jec       = args.enable_regrouped_jec

if regroup_jec:
  if 'full' not in systematics_label:
    raise RuntimeError("Regrouped JEC was enabled but not running with full systematics")
  systematics.full.extend(systematics.JEC_regrouped)

# Custom arguments
output_tree = args.output_tree

# Use the arguments
central_or_shifts = []
for systematic_label in systematics_label:
  for central_or_shift in getattr(systematics, systematic_label):
    if central_or_shift not in central_or_shifts:
      central_or_shifts.append(central_or_shift)
jet_cleaning_by_index = (jet_cleaning == 'by_index')
gen_matching_by_index = (gen_matching == 'by_index')

if use_nonnominal:
  samples = load_samples(era, suffix = "sync")
else:
  raise ValueError("Implement me!")

if __name__ == '__main__':
  logging.basicConfig(
    stream = sys.stdout,
    level  = logging.INFO,
    format = '%(asctime)s - %(levelname)s: %(message)s',
  )

  if sample_filter:
    samples = filter_samples(samples, sample_filter)

  logging.info(
    "Running the jobs with the following systematic uncertainties enabled: %s" % \
    ', '.join(central_or_shifts)
  )

  configDir = os.path.join("/home",       getpass.getuser(), "hhAnalysis", era, version)
  outputDir = os.path.join("/hdfs/local", getpass.getuser(), "hhAnalysis", era, version)

  analysis = analyzeConfig_hh_bbww_inclusive(
    configDir               = configDir,
    outputDir               = outputDir,
    executable_analyze      = "analyze_hh_bbww_inclusive",
    cfgFile_analyze         = "analyze_hh_bbww_inclusive_cfg.py",
    samples                 = samples,
    era                     = era,
    output_tree             = output_tree,
    check_output_files      = check_output_files,
    running_method          = running_method,
    dry_run                 = dry_run,
    isDebug                 = debug,
    rle_select              = rle_select,
    central_or_shifts       = central_or_shifts,
    jet_cleaning_by_index   = jet_cleaning_by_index,
    gen_matching_by_index   = gen_matching_by_index,
    use_nonnominal          = use_nonnominal,
    use_home                = use_home,
    submission_cmd          = sys.argv,
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
