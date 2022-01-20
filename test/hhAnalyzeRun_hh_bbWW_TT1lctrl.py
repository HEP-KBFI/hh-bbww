#!/usr/bin/env python

from hhAnalysis.bbww.configs.analyzeConfig_hh_bbWW_TT1lctrl import analyzeConfig_hh_bbWW_TT1lctrl
from tthAnalysis.HiggsToTauTau.jobTools import query_yes_no
from tthAnalysis.HiggsToTauTau.analysisSettings import systematics, get_lumi
from tthAnalysis.HiggsToTauTau.runConfig import tthAnalyzeParser, filter_samples
from tthAnalysis.HiggsToTauTau.common import logging, load_samples_hh_bbww as load_samples, load_samples_stitched

import os
import sys
import getpass

# E.g.: ./test/tthAnalyzeRun_hh_bbWW_TT1lctrl.py -v 2017Dec13 -m default -e 2017

mode_choices     = [ 'default' ]
sys_choices      = [ 'full', 'internal' ] + systematics.an_opts_hh_bbww
systematics.full = systematics.an_tth
systematics.internal = systematics.an_internal_no_mem

parser = tthAnalyzeParser()
parser.add_modes(mode_choices)
parser.add_sys(sys_choices)
parser.add_preselect()
parser.add_lep_mva_wp(default_wp = 'hh_multilepton')
parser.add_nonnominal()
parser.add_tau_id_wp()
parser.add_hlt_filter()
parser.add_files_per_job(files_per_job = 8)
parser.add_use_home()
parser.add_stitched([ 'dy_nlo', 'wjets' ])
parser.add_jet_cleaning('by_dr')
parser.add_gen_matching()
parser.enable_regrouped_jerc(default = 'jes')
parser.add_split_trigger_sys()
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
lep_mva_wp        = args.lep_mva_wp
hlt_filter        = args.hlt_filter
files_per_job     = args.files_per_job
use_home          = args.use_home
use_stitched      = args.use_stitched
jet_cleaning      = args.jet_cleaning
gen_matching      = args.gen_matching
regroup_jerc      = args.enable_regrouped_jerc
split_trigger_sys = args.split_trigger_sys

if lep_mva_wp != "hh_multilepton" and use_preselected:
  raise RuntimeError("Cannot use skimmed samples while tightening the prompt lepton MVA cut")

if regroup_jerc:
  if 'full' not in systematics_label:
    raise RuntimeError("Regrouped JEC or split JER was enabled but not running with full systematics")
  if regroup_jerc == 'both':
    systematics.full.extend(systematics.JEC_regrouped + systematics.JER_split)
  elif regroup_jerc == 'jes':
    systematics.full.extend(systematics.JEC_regrouped)
  elif regroup_jerc == 'jer':
    systematics.full.extend(systematics.JER_split)
  else:
    raise RuntimeError("Invalid choice: %s" % regroup_jerc)
if split_trigger_sys == 'yes':
  for trigger_sys in systematics.triggerSF:
    del systematics.internal[systematics.internal.index(trigger_sys)]
    del systematics.full[systematics.full.index(trigger_sys)]
if split_trigger_sys in [ 'yes', 'both' ]:
  systematics.internal.extend(systematics.triggerSF_2lss)
  systematics.full.extend(systematics.triggerSF_2lss)

# Use the arguments
central_or_shifts = []
for systematic_label in systematics_label:
  for central_or_shift in getattr(systematics, systematic_label):
    if central_or_shift not in central_or_shifts:
      central_or_shifts.append(central_or_shift)
lumi = get_lumi(era)
jet_cleaning_by_index = (jet_cleaning == 'by_index')
gen_matching_by_index = (gen_matching == 'by_index')

if mode == "default":
  samples = load_samples(era, suffix = "preselected_sl" if use_preselected else "")
else:
  raise ValueError("Internal logic error")

samples = load_samples_stitched(samples, era, use_stitched)

blacklisted_categories = []
for sample_name, sample_info in samples.items():
  if sample_name == 'sum_events':
    continue
  if sample_name.startswith(('/DoubleMuon/', '/DoubleEG/', '/MuonEG/', '/Tau/')):
    sample_info["use_it"] = False
  if sample_info["process_name_specific"].startswith('signal') and 'hh' in sample_info["process_name_specific"]:
    sample_info["use_it"] = False
  if sample_info["sample_category"] in blacklisted_categories:
    sample_info["use_it"] = False

if __name__ == '__main__':
  logging.info(
    "Running the jobs with the following systematic uncertainties enabled: %s" % \
    ', '.join(central_or_shifts)
  )

  if sample_filter:
    samples = filter_samples(samples, sample_filter)

  analysis = analyzeConfig_hh_bbWW_TT1lctrl(
    configDir = os.path.join("/scratch-persistent", getpass.getuser(), "hhAnalysis", era, version),
    localDir  = os.path.join("/home",               getpass.getuser(), "hhAnalysis", era, version),
    outputDir = os.path.join("/hdfs/local",         getpass.getuser(), "hhAnalysis", era, version),
    executable_analyze                    = "analyze_hh_bbWW_TT1lctrl",
    cfgFile_analyze                       = "analyze_hh_bbWW_TT1lctrl_cfg.py",
    samples                               = samples,
    applyFakeRateWeights                  = "enabled",
    central_or_shifts                     = central_or_shifts,
    lep_mva_wp                            = lep_mva_wp,
    jet_cleaning_by_index                 = jet_cleaning_by_index,
    gen_matching_by_index                 = gen_matching_by_index,
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
