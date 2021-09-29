#!/usr/bin/env python
import os, logging, sys, getpass
from collections import OrderedDict as OD
from hhAnalysis.bbwwMEMPerformanceStudies.configs.analyzeConfig_hh_bbwwMEM_singlelepton import analyzeConfig_hh_bbwwMEM_singlelepton
from tthAnalysis.HiggsToTauTau.jobTools import query_yes_no
from tthAnalysis.HiggsToTauTau.analysisSettings import systematics, get_lumi
from tthAnalysis.HiggsToTauTau.runConfig import tthAnalyzeParser, filter_samples

# E.g.: ./hhAnalyzeRun_bbwwMEM_singlelepton.py -v 2021May17 -e 2016

parser = tthAnalyzeParser()
parser.add_rle_select()
parser.add_files_per_job(1) # CV: need to reduce number of Ntuple files processed per job, as computation of MEM takes considerable time
parser.add_use_home()
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
rle_select        = os.path.expanduser(args.rle_select)
files_per_job     = args.files_per_job
use_home          = args.use_home

if era == "2016":
  from hhAnalysis.bbwwMEMPerformanceStudies.samples.hhAnalyzeSamples_singlelepton_2016 import samples_2016 as samples
else:
  print("Please use '2016' era, as the LO SM HH signal MC samples for the '2017' and '2018' eras are affected by a coupling bug!")
  print(" c.f. https://indico.cern.ch/event/996685/contributions/4251752/attachments/2198363/3717406/HH_bbWW_LOtoNLOreweighting_2021Mar01.pdf")
  ValueError("Aborting.")

if __name__ == '__main__':
  logging.basicConfig(
    stream = sys.stdout,
    level  = logging.INFO,
    format = '%(asctime)s - %(levelname)s: %(message)s',
  )

  if sample_filter:
    samples = filter_samples(samples, sample_filter)

  analysis = analyzeConfig_hh_bbwwMEM_singlelepton(
    configDir = os.path.join("/home",       getpass.getuser(), "hhAnalysis", era, version),
    outputDir = os.path.join("/hdfs/local", getpass.getuser(), "hhAnalysis", era, version),
    executable_analyze                    = "analyze_hh_bbwwMEM_singlelepton",
    cfgFile_analyze                       = "analyze_hh_bbwwMEM_singlelepton_cfg.py",
    samples                               = samples,
    ##max_jobs_per_sample                   = 1000,
    max_jobs_per_sample                   = 100,
    apply_jetSmearing_options             = [ True, False ],
    apply_metSmearing_options             = [ True, False ],
    max_files_per_job                     = files_per_job,
    era                                   = era,
    check_output_files                    = check_output_files,
    running_method                        = running_method,
    num_parallel_jobs                     = num_parallel_jobs,
    select_rle_output                     = True,
    isDebug                               = debug,
    rle_select                            = rle_select,
    use_home                              = use_home,
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
