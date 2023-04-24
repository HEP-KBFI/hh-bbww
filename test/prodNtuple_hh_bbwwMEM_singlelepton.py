#!/usr/bin/env python
import os, logging, sys, getpass
from collections import OrderedDict as OD
from hhAnalysis.bbww.configs.prodNtupleConfig_hh_bbwwMEM_singlelepton import prodNtupleConfig_hh_bbwwMEM_singlelepton
from tthAnalysis.HiggsToTauTau.jobTools import query_yes_no
from tthAnalysis.HiggsToTauTau.analysisSettings import systematics, get_lumi
from tthAnalysis.HiggsToTauTau.runConfig import tthAnalyzeParser, filter_samples
from tthAnalysis.HiggsToTauTau.common import logging, load_samples_hh_bbww as load_samples, load_samples_stitched

# E.g.: ./prodNtuple_hh_bbwwMEM_singlelepton.py -v 2021Sep10 -e 2016

parser = tthAnalyzeParser()
parser.add_preselect()
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
keep_logs          = args.keep_logs

# Additional arguments
use_preselected   = args.use_preselected
rle_select        = os.path.expanduser(args.rle_select)
files_per_job     = args.files_per_job
use_home          = args.use_home

samples = load_samples(era, suffix = "preselected" if use_preselected else "")
samples = load_samples_stitched(samples, era, [ 'dy_nlo', 'wjets' ])
for sample_name, sample_info in samples.items():
  if sample_name == 'sum_events':
    continue
  if sample_info["process_name_specific"].find("signal_ggf_nonresonant_node_sm_hh_2b2v_sl") != -1: # HH signal sample @ LO 
    sample_info["sample_category"] = "signal_lo"
    sample_info["use_it"] = True
  elif sample_info["process_name_specific"].find("signal_ggf_nonresonant_cHHH1_hh_2b2v_sl") != -1: # HH signal sample @ NLO
    vetoes = [
      "duplicate",
    ]
    isVeto = False
    for veto in vetoes:
      if sample_info["process_name_specific"].find(veto) != -1:
        isVeto = True
    sample_info["sample_category"] = "signal_nlo"
    sample_info["use_it"] = True
  elif sample_info["process_name_specific"].find("TTJets_SingleLeptFromT")         != -1 or \
       sample_info["process_name_specific"].find("TTJets_SingleLeptFromTbar")      != -1 or \
       sample_info["process_name_specific"].find("TTJets_SingleLeptFromT_ext1")    != -1 or \
       sample_info["process_name_specific"].find("TTJets_SingleLeptFromTbar_ext1") != -1:          # ttbar background sample @ LO
    sample_info["sample_category"] = "background_lo"
    sample_info["use_it"] = True
  elif sample_info["process_name_specific"] == "TTToSemiLeptonic":                                 # ttbar background sample @ NLO
    sample_info["sample_category"] = "background_nlo"
    sample_info["use_it"] = True
  else:
    sample_info["use_it"] = False

if __name__ == '__main__':
  logging.basicConfig(
    stream = sys.stdout,
    level  = logging.INFO,
    format = '%(asctime)s - %(levelname)s: %(message)s',
  )

  if sample_filter:
    samples = filter_samples(samples, sample_filter)

  analysis = prodNtupleConfig_hh_bbwwMEM_singlelepton(
    configDir = os.path.join("/scratch/persistent", getpass.getuser(), "hhAnalysis", era, version),
    localDir  = os.path.join("/home",               getpass.getuser(), "hhAnalysis", era, version),
    outputDir = os.path.join("/local",              getpass.getuser(), "hhAnalysis", era, version),
    executable_analyze                    = "produceMEMNtuple_hh_bb1l",
    cfgFile_analyze                       = "produceMEMNtuple_hh_bb1l_cfg.py",
    samples                               = samples,
    max_jobs_per_sample                   = 100, # CV: use for tests
    ##max_jobs_per_sample                   = 10000, # CV: use for full production
    max_files_per_job                     = files_per_job,
    era                                   = era,
    check_output_files                    = check_output_files,
    running_method                        = running_method,
    num_parallel_jobs                     = num_parallel_jobs,
    select_rle_output                     = True,
    isDebug                               = debug,
    rle_select                            = rle_select,
    use_home                              = use_home,
    keep_logs                             = keep_logs,
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
