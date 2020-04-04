#!/usr/bin/env python

from hhAnalysis.bbww.configs.analyzeConfig_hadWTagger import analyzeConfig_hadWTagger
from tthAnalysis.HiggsToTauTau.jobTools import query_yes_no
from tthAnalysis.HiggsToTauTau.analysisSettings import systematics, get_lumi
from tthAnalysis.HiggsToTauTau.runConfig import tthAnalyzeParser, filter_samples
from tthAnalysis.HiggsToTauTau.common import logging, load_samples_hh_bbww as load_samples

import os
import sys
import getpass

# E.g.: ./test/tthAnalyzeRun_hadTopTagger.py -v 2019Dec09 -m default -e 2017

mode_choices     = [ 'default', 'forBDTtraining' ]
sys_choices      = [ 'full' ] + systematics.an_opts_hh_bbww
systematics.full = systematics.an_hh_bbww

parser = tthAnalyzeParser()
parser.add_modes(mode_choices)
parser.add_sys(sys_choices)
parser.add_rle_select()
parser.add_files_per_job() 
parser.add_use_home()
parser.add_jet_cleaning('by_dr')
args = parser.parse_args()

# Common arguments
era                = args.era
version            = args.version
no_exec            = args.no_exec
auto_exec          = args.auto_exec
check_output_files = not args.not_check_input_files
debug              = args.debug
sample_filter      = args.filter
num_parallel_jobs  = args.num_parallel_jobs
running_method     = args.running_method

# Additional arguments
mode              = args.mode
rle_select        = os.path.expanduser(args.rle_select)
files_per_job     = args.files_per_job
use_home          = args.use_home
jet_cleaning      = args.jet_cleaning

lumi = get_lumi(era)
jet_cleaning_by_index = (jet_cleaning == 'by_index')

if mode == "default":
  samples = load_samples(era)
elif mode == "forBDTtraining":
  samples = load_samples(era, suffix = "BDT")
else:
  raise ValueError("Internal logic error")

blacklisted_categories = []
for sample_name, sample_info in samples.items():
  if sample_name == 'sum_events':
    continue
  if sample_info["sample_category"] in blacklisted_categories:
    sample_info["use_it"] = False
    continue
  if sample_name.startswith(('/MuonEG/', '/Tau/')):
    sample_info["use_it"] = False
  if sample_name.startswith(('/TTToSemiLeptonic')):
    sample_info["use_it"] = True
  if sample_name.startswith(('/GluGluToHHTo2B2WToLNu2J_node_SM')):
    sample_info["use_it"] = True

if __name__ == '__main__':

  if sample_filter:
    samples = filter_samples(samples, sample_filter)

  analysis = analyzeConfig_hadWTagger(
    configDir = os.path.join("/home",       getpass.getuser(), "hhAnalysis", era, version),
    outputDir = os.path.join("/hdfs/local", getpass.getuser(), "hhAnalysis", era, version),
    executable_analyze                    = "analyze_hadWTagger",
    cfgFile_analyze                       = "analyze_hadWTagger_cfg.py",
    samples                               = samples,
    central_or_shifts                     = [ "central" ],
    jet_cleaning_by_index                 = jet_cleaning_by_index,
    max_files_per_job                     = files_per_job,
    era                                   = era,
    use_lumi                              = True,
    lumi                                  = lumi,
    check_output_files                    = check_output_files,
    running_method                        = running_method,
    num_parallel_jobs                     = num_parallel_jobs,
    isDebug                               = debug,
    use_home                              = use_home,
    submission_cmd                        = sys.argv,
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
