#!/usr/bin/env python

from hhAnalysis.bbww.configs.analyzeConfig_hh_bb2l import analyzeConfig_hh_bb2l
from tthAnalysis.HiggsToTauTau.jobTools import query_yes_no
from tthAnalysis.HiggsToTauTau.analysisSettings import systematics, get_lumi
from tthAnalysis.HiggsToTauTau.runConfig import tthAnalyzeParser, filter_samples
from tthAnalysis.HiggsToTauTau.common import logging, load_samples_hh_bbww as load_samples, load_samples_stitched

import os
import sys
import getpass
import importlib

# E.g.: ./test/tthAnalyzeRun_hh_bb2l.py -v 2017Dec13 -m default -e 2017

mode_choices     = [
  'default', 'wMEM', 'forBDTtraining', 'forBDTtraining_wMEM', 'hh_sync', 'hh_sync_wMEM',
  'ttbar_sync', 'ttbar_sync_wMEM',
]
sys_choices      = [ 'full', 'internal' ] + systematics.an_opts_hh_bbww + [ 'MEM_bb2l' ]
systematics.full = systematics.an_hh_bbww
systematics.internal = systematics.an_internal_no_mem

parser = tthAnalyzeParser()
parser.add_modes(mode_choices)
parser.add_sys(sys_choices)
parser.add_preselect()
parser.add_rle_select()
parser.add_nonnominal()
parser.add_hlt_filter()
parser.add_files_per_job(5) # CV: need to reduce number of Ntuple files processed per job, as computation of HH mass with HME algorithm takes considerable time
parser.add_use_home()
parser.add_sideband(default_choice = 'enabled')
parser.add_tau_id() # compatibility with sync Ntuple workflow, otherwise ignored
parser.add_jet_cleaning('by_dr')
parser.add_gen_matching()
parser.enable_regrouped_jerc()
parser.add_split_trigger_sys()
parser.add_argument('-hme', '--hmeBr',
  dest = 'add_hmeBr', action = 'store_true',
  help = 'R|add hme branch'
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
sideband          = args.sideband
jet_cleaning      = args.jet_cleaning
gen_matching      = args.gen_matching
regroup_jerc      = args.enable_regrouped_jerc
split_trigger_sys = args.split_trigger_sys
add_hmeBr            =args.add_hmeBr

if regroup_jerc:
  if 'full' not in systematics_label:
    raise RuntimeError("Regrouped JEC or split JER was enabled but not running with full systematics")
  systematics.full.extend(systematics.JEC_regrouped + systematics.JER_split)
if split_trigger_sys == 'yes':
  for trigger_sys in systematics.triggerSF:
    del systematics.internal[systematics.internal.index(trigger_sys)]
    del systematics.full[systematics.full.index(trigger_sys)]
if split_trigger_sys in [ 'yes', 'both' ]:
  systematics.internal.extend(systematics.triggerSF_2lss)
  systematics.full.extend(systematics.triggerSF_2lss)

# Use the arguments
if "wMEM" in mode:
  systematics.full += systematics.MEM_bb2l
  systematics.internal += systematics.MEM_bb2l
central_or_shifts = []
for systematic_label in systematics_label:
  for central_or_shift in getattr(systematics, systematic_label):
    if central_or_shift not in central_or_shifts:
      if central_or_shift in systematics.MEM_bb2l and "MEM" not in mode:
        continue
      central_or_shifts.append(central_or_shift)

do_sync = 'sync' in mode
lumi = get_lumi(era)
jet_cleaning_by_index = (jet_cleaning == 'by_index')
gen_matching_by_index = (gen_matching == 'by_index')

MEMbranch = ''
hmebranch = ''
MEMbranch_base = "memObjects_hh_bb2l"
HMEbranch_base = "hmeObjects_hh_bb2l"
MEMsample_base = "addMEM_hh_bb2l"

# the Ntuples that currently have the MEM scores are computed with fakebale lepton selection
if add_hmeBr:
  #hmebranch = "{}_lep{}".format(HMEbranch_base, "Loose" if "forBDTtraining" in mode else "Fakeable")
  hmebranch = "{}_lepFakeable".format(HMEbranch_base)
if "wMEM" in mode:
  #MEMbranch = '{}_lep{}'.format(MEMbranch_base, "Loose" if "forBDTtraining" in mode else "Fakeable")
  MEMbranch = '{}_lepFakeable'.format(MEMbranch_base)

if mode == "default":
  samples = load_samples(era, suffix = "preselected" if use_preselected else "")
elif mode == "wMEM":
  if not use_preselected:
    raise ValueError("MEM branches can be read only from preselected Ntuples")
  samples = load_samples(era, suffix = MEMsample_base)
elif mode == "forBDTtraining":
  if use_preselected:
    raise ValueError("Producing Ntuples for BDT training from preselected Ntuples makes no sense!")
  samples = load_samples(era, suffix = "BDT")
  samples = load_samples_stitched(samples, era, load_dy = True, load_wjets = True)
elif mode == "forBDTtraining_wMEM":
  if use_preselected:
    raise ValueError("Producing Ntuples for BDT training from preselected Ntuples makes no sense!")
  samples = load_samples(era, suffix = "MEM_bb2l_BDT")
elif mode == "hh_sync_wMEM":
  if not use_preselected:
    raise ValueError("MEM branches can be read only from preselected Ntuples")
  samples = load_samples(era, suffix = "{}_sync{}".format(MEMsample_base, '' if use_nonnominal else "_nom"))
elif mode == "hh_sync":
  samples = load_samples(era, suffix = "sync")
elif mode == "ttbar_sync_wMEM":
  if not use_preselected:
    raise ValueError("MEM branches can be read only from preselected Ntuples")
  samples = load_samples(era, suffix = "{}_sync_ttbar{}".format(MEMsample_base, '' if use_nonnominal else "_nom"))
elif mode == "ttbar_sync":
  samples = load_samples(era, suffix = "sync_ttbar")
else:
  raise ValueError("Internal logic error")


for sample_name, sample_info in samples.items():
  if sample_name == 'sum_events':
    continue
  if "CHH" in sample_name:
    sample_info["use_it"] = False

evtCategories = None
"""
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
"""
evtCategories = []

if sideband == 'disabled':
  chargeSumSelections = [ "OS" ]
elif sideband == 'enabled':
  chargeSumSelections = [ "OS", "SS" ]
elif sideband == 'only':
  chargeSumSelections = [ "SS" ]
else:
  raise ValueError("Invalid choice for the sideband: %s" % sideband)

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
    MEMbranch                             = MEMbranch,
    hmebranch                             = hmebranch,
    lepton_charge_selections              = chargeSumSelections,
    applyFakeRateWeights                  = "enabled",
    central_or_shifts                     = central_or_shifts,
    jet_cleaning_by_index                 = jet_cleaning_by_index,
    gen_matching_by_index                 = gen_matching_by_index,
    evtCategories                         = evtCategories,
    max_files_per_job                     = files_per_job,
    era                                   = era,
    use_lumi                              = True,
    lumi                                  = lumi,
    check_output_files                    = check_output_files,
    running_method                        = running_method,
    num_parallel_jobs                     = num_parallel_jobs,
    executable_addSysTT                   = "addSysTT",
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
      "MVAOutputnohiggnessnotopness_750"  : {},
      ###
      "SM_plainVars_noHH_ee_MHH1_lowMbb"    : {},
      "SM_plainVars_noHH_em_MHH1_lowMbb"    : {},
      "SM_plainVars_noHH_mm_MHH1_lowMbb"    : {},
      "SM_plainVars_noHH_ee_MHH2_lowMbb"    : {},
      "SM_plainVars_noHH_em_MHH2_lowMbb"    : {},
      "SM_plainVars_noHH_mm_MHH2_lowMbb"    : {},
      "SM_plainVars_noHH_ee_MHH3_lowMbb"    : {},
      "SM_plainVars_noHH_em_MHH3_lowMbb"    : {},
      "SM_plainVars_noHH_mm_MHH3_lowMbb"    : {},
      "SM_plainVars_noHH_ee_MHH4_lowMbb"    : {},
      "SM_plainVars_noHH_em_MHH4_lowMbb"    : {},
      "SM_plainVars_noHH_mm_MHH4_lowMbb"    : {},
      "SM_plainVars_noHH_ee_MHH5_lowMbb"    : {},
      "SM_plainVars_noHH_em_MHH5_lowMbb"    : {},
      "SM_plainVars_noHH_mm_MHH5_lowMbb"    : {},
      "SM_plainVars_noHH_ee_MHH1_medMbb"    : {},
      "SM_plainVars_noHH_em_MHH1_medMbb"    : {},
      "SM_plainVars_noHH_mm_MHH1_medMbb"    : {},
      "SM_plainVars_noHH_ee_MHH2_medMbb"    : {},
      "SM_plainVars_noHH_em_MHH2_medMbb"    : {},
      "SM_plainVars_noHH_mm_MHH2_medMbb"    : {},
      "SM_plainVars_noHH_ee_MHH3_medMbb"    : {},
      "SM_plainVars_noHH_em_MHH3_medMbb"    : {},
      "SM_plainVars_noHH_mm_MHH3_medMbb"    : {},
      "SM_plainVars_noHH_ee_MHH4_medMbb"    : {},
      "SM_plainVars_noHH_em_MHH4_medMbb"    : {},
      "SM_plainVars_noHH_mm_MHH4_medMbb"    : {},
      "SM_plainVars_noHH_ee_MHH5_medMbb"    : {},
      "SM_plainVars_noHH_em_MHH5_medMbb"    : {},
      "SM_plainVars_noHH_mm_MHH5_medMbb"    : {},
      "SM_plainVars_noHH_ee_MHH1_highMbb"    : {},
      "SM_plainVars_noHH_em_MHH1_highMbb"    : {},
      "SM_plainVars_noHH_mm_MHH1_highMbb"    : {},
      "SM_plainVars_noHH_ee_MHH2_highMbb"    : {},
      "SM_plainVars_noHH_em_MHH2_highMbb"    : {},
      "SM_plainVars_noHH_mm_MHH2_highMbb"    : {},
      "SM_plainVars_noHH_ee_MHH3_highMbb"    : {},
      "SM_plainVars_noHH_em_MHH3_highMbb"    : {},
      "SM_plainVars_noHH_mm_MHH3_highMbb"    : {},
      "SM_plainVars_noHH_ee_MHH4_highMbb"    : {},
      "SM_plainVars_noHH_em_MHH4_highMbb"    : {},
      "SM_plainVars_noHH_mm_MHH4_highMbb"    : {},
      "SM_plainVars_noHH_ee_MHH5_highMbb"    : {},
      "SM_plainVars_noHH_em_MHH5_highMbb"    : {},
      "SM_plainVars_noHH_mm_MHH5_highMbb"    : {},
      ###
      "SM_plainVars_noHH_withbb_ee_MHH1"    : {},
      "SM_plainVars_noHH_withbb_em_MHH1"    : {},
      "SM_plainVars_noHH_withbb_mm_MHH1"    : {},
      "SM_plainVars_noHH_withbb_ee_MHH2"    : {},
      "SM_plainVars_noHH_withbb_em_MHH2"    : {},
      "SM_plainVars_noHH_withbb_mm_MHH2"    : {},
      "SM_plainVars_noHH_withbb_ee_MHH3"    : {},
      "SM_plainVars_noHH_withbb_em_MHH3"    : {},
      "SM_plainVars_noHH_withbb_mm_MHH3"    : {},
      "SM_plainVars_noHH_withbb_ee_MHH4"    : {},
      "SM_plainVars_noHH_withbb_em_MHH4"    : {},
      "SM_plainVars_noHH_withbb_mm_MHH4"    : {},
      "SM_plainVars_noHH_withbb_ee_MHH5"    : {},
      "SM_plainVars_noHH_withbb_em_MHH5"    : {},
      "SM_plainVars_noHH_withbb_mm_MHH5"    : {},
      #####
      "SM_plainVars_Xness_nocat"    : {},
      "SM_plainVars_nocat"    : {},
      "SM_plainVars_noHH_withbb_nocat"    : {},
      "SM_plainVars_noHH_nocat"    : {},
      ##  ///////////
      "SM_plainVars_Xness_ee"    : {},
      "SM_plainVars_Xness_em"    : {},
      "SM_plainVars_Xness_mm"    : {},
      "SM_plainVars_ee"    : {},
      "SM_plainVars_em"    : {},
      "SM_plainVars_mm"    : {},
    },
    select_rle_output                     = True,
    dry_run                               = dry_run,
    do_sync                               = do_sync,
    isDebug                               = debug,
    rle_select                            = rle_select,
    use_nonnominal                        = use_nonnominal,
    hlt_filter                            = hlt_filter,
    use_home                              = use_home,
    submission_cmd                        = sys.argv,
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
