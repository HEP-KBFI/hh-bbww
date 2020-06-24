#!/usr/bin/env python

from hhAnalysis.bbww.configs.analyzeConfig_hh_bb1l import analyzeConfig_hh_bb1l
from tthAnalysis.HiggsToTauTau.jobTools import query_yes_no
from tthAnalysis.HiggsToTauTau.analysisSettings import systematics, get_lumi
from tthAnalysis.HiggsToTauTau.runConfig import tthAnalyzeParser, filter_samples
from tthAnalysis.HiggsToTauTau.common import logging, load_samples_hh_bbww as load_samples, load_samples_stitched

import os
import sys
import getpass
import importlib

# E.g.: ./test/tthAnalyzeRun_hh_bb1l.py -v 2017Dec13 -m default -e 2017

mode_choices     = [ 'default', 'forBDTtraining', 'hh_sync', 'ttbar_sync' ]
sys_choices      = [ 'full', 'internal' ] + systematics.an_opts_hh_bbww
systematics.full = systematics.an_hh_bbww
systematics.internal = systematics.an_internal_no_mem

parser = tthAnalyzeParser()
parser.add_modes(mode_choices)
parser.add_sys(sys_choices)
parser.add_preselect() # effectively ignored, but needed by sync Ntuple workflow
parser.add_rle_select()
parser.add_nonnominal()
parser.add_tau_id_wp()
parser.add_hlt_filter()
parser.add_files_per_job()
parser.add_use_home()
parser.add_tau_id()
parser.add_jet_cleaning('by_dr')
parser.add_gen_matching()
parser.enable_regrouped_jerc()
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
rle_select        = os.path.expanduser(args.rle_select)
use_nonnominal    = args.original_central
hlt_filter        = args.hlt_filter
files_per_job     = args.files_per_job
use_home          = args.use_home
tau_id            = args.tau_id
jet_cleaning      = args.jet_cleaning
gen_matching      = args.gen_matching
regroup_jerc      = args.enable_regrouped_jerc
split_trigger_sys = args.split_trigger_sys

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
central_or_shifts = []

for systematic_label in systematics_label:
  for central_or_shift in getattr(systematics, systematic_label):
    if central_or_shift not in central_or_shifts:
      central_or_shifts.append(central_or_shift)

do_sync = 'sync' in mode
lumi = get_lumi(era)
jet_cleaning_by_index = (jet_cleaning == 'by_index')
gen_matching_by_index = (gen_matching == 'by_index')

if "sync" not in mode:
  samples_to_stitch = getattr(
    importlib.import_module("tthAnalysis.HiggsToTauTau.samples.stitch"),
    "samples_to_stitch_{}".format(era)
  )

if mode == "default":
  samples = load_samples(era)
elif mode == "forBDTtraining":
  samples = load_samples(era, suffix = "BDT")
  samples = load_samples_stitched(samples, era, load_dy = True, load_wjets = True)
elif mode == "hh_sync":
  samples = load_samples(era, suffix = "sync")
elif mode == "ttbar_sync":
  samples = load_samples(era, suffix = "sync_ttbar")
else:
  raise ValueError("Internal logic error")

if mode == "default" and len(central_or_shifts) <= 1:
  evtCategories = []
else:
  evtCategories = []


hadTauWP_veto_map = {
  'dR03mva' : 'Medium',
  'deepVSj' : 'Medium',
}
hadTau_selection_veto = tau_id + hadTauWP_veto_map[tau_id]

if __name__ == '__main__':
  logging.info(
    "Running the jobs with the following systematic uncertainties enabled: %s" % \
    ', '.join(central_or_shifts)
  )

  if sample_filter:
    samples = filter_samples(samples, sample_filter)

  if args.tau_id_wp:
    logging.info("Changing tau ID working point: %s -> %s" % (hadTau_selection_veto, args.tau_id_wp))
    hadTau_mva_wp_veto = args.tau_id_wp

  analysis = analyzeConfig_hh_bb1l(
    configDir = os.path.join("/home",       getpass.getuser(), "hhAnalysis", era, version),
    outputDir = os.path.join("/hdfs/local", getpass.getuser(), "hhAnalysis", era, version),
    executable_analyze                    = "analyze_hh_bb1l",
    cfgFile_analyze                       = "analyze_hh_bb1l_cfg.py",
    samples                               = samples,
    apply_hadTauVeto                      = False,
    hadTau_mva_wp_veto                    = hadTau_selection_veto,
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
    executable_addBackgrounds             = "addBackgrounds",
    executable_addFakes                   = "addBackgroundLeptonFakes",
    histograms_to_fit                     = {
      "EventCounter"                      : {},
      #"HT"                                : {},
      #"STMET"                             : {},
      #"MVAOutput_350"                     : {},
      #"MVAOutput_400"                     : {},
      #"MVAOutput_750"                     : {},
      "cat_jet_Wjj_Hbb_reco"              : {},
      "cat_jet_one_jet_to_Wjj"            : {},
      "cat_jet_strange"                   : {},
      "cat_jet_Wjj_Hbb_reco_MVA"              : {},
      "cat_jet_one_jet_to_Wjj_MVA"            : {},
      "cat_jet_strange_MVA"                   : {},
      ###
      "cat_jet_2BDT_Wjj_BDT_HbbFat_WjjFat_HP_e"            : {},
      "cat_jet_2BDT_Wjj_BDT_WjjFat_HP_e"            : {},
      "cat_jet_2BDT_Wjj_BDT_HbbFat_WjjFat_LP_e"            : {},
      "cat_jet_2BDT_Wjj_BDT_WjjFat_LP_e"            : {},
      "cat_jet_2BDT_Wjj_BDT_HbbFat_WjjRes_allReco_e"            : {},
      "cat_jet_2BDT_Wjj_BDT_Res_allReco_e"            : {},
      "cat_jet_2BDT_Wjj_BDT_HbbFat_WjjFat_HP_m"            : {},
      "cat_jet_2BDT_Wjj_BDT_WjjFat_HP_m"            : {},
      "cat_jet_2BDT_Wjj_BDT_HbbFat_WjjFat_LP_m"            : {},
      "cat_jet_2BDT_Wjj_BDT_WjjFat_LP_m"            : {},
      "cat_jet_2BDT_Wjj_BDT_HbbFat_WjjRes_allReco_m"            : {},
      "cat_jet_2BDT_Wjj_BDT_Res_allReco_m"            : {},
      "cat_jet_2BDT_Wjj_BDT_HbbFat_WjjRes_MissJet_e"            : {},
      "cat_jet_2BDT_Wjj_BDT_Res_MissWJet_e"            : {},
      "cat_jet_2BDT_Wjj_BDT_HbbFat_WjjRes_MissJet_m"            : {},
      "cat_jet_2BDT_Wjj_BDT_Res_MissWJet_m"            : {},
      "cat_jet_2BDT_Wjj_BDT_Res_MissBJet_m"            : {},
      "cat_jet_2BDT_Wjj_BDT_Res_MissBJet_e"            : {},
      #############
      "cat_jet_2BDT_Wjj_simple_HbbFat_WjjFat_HP_e"            : {},
      "cat_jet_2BDT_Wjj_simple_WjjFat_HP_e"            : {},
      "cat_jet_2BDT_Wjj_simple_HbbFat_WjjFat_LP_e"            : {},
      "cat_jet_2BDT_Wjj_simple_WjjFat_LP_e"            : {},
      "cat_jet_2BDT_Wjj_simple_HbbFat_WjjRes_allReco_e"            : {},
      "cat_jet_2BDT_Wjj_simple_Res_allReco_e"            : {},
      "cat_jet_2BDT_Wjj_simple_HbbFat_WjjFat_HP_m"            : {},
      "cat_jet_2BDT_Wjj_simple_WjjFat_HP_m"            : {},
      "cat_jet_2BDT_Wjj_simple_HbbFat_WjjFat_LP_m"            : {},
      "cat_jet_2BDT_Wjj_simple_WjjFat_LP_m"            : {},
      "cat_jet_2BDT_Wjj_simple_HbbFat_WjjRes_allReco_m"            : {},
      "cat_jet_2BDT_Wjj_simple_Res_allReco_m"            : {},
      "cat_jet_2BDT_Wjj_simple_HbbFat_WjjRes_MissJet_e"            : {},
      "cat_jet_2BDT_Wjj_simple_Res_MissWJet_e"            : {},
      "cat_jet_2BDT_Wjj_simple_HbbFat_WjjRes_MissJet_m"            : {},
      "cat_jet_2BDT_Wjj_simple_Res_MissWJet_m"            : {},
      "cat_jet_2BDT_Wjj_simple_Res_MissBJet_m"            : {},
      "cat_jet_2BDT_Wjj_simple_Res_MissBJet_e"            : {},
      ##############
      "cat_jet_Wjj_BDT_HbbFat_WjjFat_HP_e"            : {},
      "cat_jet_Wjj_BDT_WjjFat_HP_e"            : {},
      "cat_jet_Wjj_BDT_HbbFat_WjjFat_LP_e"            : {},
      "cat_jet_Wjj_BDT_WjjFat_LP_e"            : {},
      "cat_jet_Wjj_BDT_HbbFat_WjjRes_allReco_e"            : {},
      "cat_jet_Wjj_BDT_Res_allReco_e"            : {},
      "cat_jet_Wjj_BDT_HbbFat_WjjFat_HP_m"            : {},
      "cat_jet_Wjj_BDT_WjjFat_HP_m"            : {},
      "cat_jet_Wjj_BDT_HbbFat_WjjFat_LP_m"            : {},
      "cat_jet_Wjj_BDT_WjjFat_LP_m"            : {},
      "cat_jet_Wjj_BDT_HbbFat_WjjRes_allReco_m"            : {},
      "cat_jet_Wjj_BDT_Res_allReco_m"            : {},
      "cat_jet_Wjj_BDT_HbbFat_WjjRes_MissJet_e"            : {},
      "cat_jet_Wjj_BDT_Res_MissWJet_e"            : {},
      "cat_jet_Wjj_BDT_HbbFat_WjjRes_MissJet_m"            : {},
      "cat_jet_Wjj_BDT_Res_MissWJet_m"            : {},
      "cat_jet_Wjj_BDT_Res_MissBJet_m"            : {},
      "cat_jet_Wjj_BDT_Res_MissBJet_e"            : {},
      ##############
      "cat_jet_Wjj_simple_HbbFat_WjjFat_HP_e"            : {},
      "cat_jet_Wjj_simple_WjjFat_HP_e"            : {},
      "cat_jet_Wjj_simple_HbbFat_WjjFat_LP_e"            : {},
      "cat_jet_Wjj_simple_WjjFat_LP_e"            : {},
      "cat_jet_Wjj_simple_HbbFat_WjjRes_allReco_e"            : {},
      "cat_jet_Wjj_simple_Res_allReco_e"            : {},
      "cat_jet_Wjj_simple_HbbFat_WjjFat_HP_m"            : {},
      "cat_jet_Wjj_simple_WjjFat_HP_m"            : {},
      "cat_jet_Wjj_simple_HbbFat_WjjFat_LP_m"            : {},
      "cat_jet_Wjj_simple_WjjFat_LP_m"            : {},
      "cat_jet_Wjj_simple_HbbFat_WjjRes_allReco_m"            : {},
      "cat_jet_Wjj_simple_Res_allReco_m"            : {},
      "cat_jet_Wjj_simple_HbbFat_WjjRes_MissJet_e"            : {},
      "cat_jet_Wjj_simple_Res_MissWJet_e"            : {},
      "cat_jet_Wjj_simple_HbbFat_WjjRes_MissJet_m"            : {},
      "cat_jet_Wjj_simple_Res_MissWJet_m"            : {},
      "cat_jet_Wjj_simple_Res_MissBJet_m"            : {},
      "cat_jet_Wjj_simple_Res_MissBJet_e"            : {},
      ################
      "cat_jet_2BDT_Wjj_BDT_X900GeV_HbbFat_WjjFat_HP_e"       : {},
      "cat_jet_2BDT_Wjj_BDT_X900GeV_WjjFat_HP_e"       : {},
      "cat_jet_2BDT_Wjj_BDT_X900GeV_HbbFat_WjjFat_LP_e"       : {},
      "cat_jet_2BDT_Wjj_BDT_X900GeV_WjjFat_LP_e"       : {},
      "cat_jet_2BDT_Wjj_BDT_X900GeV_HbbFat_WjjRes_allReco_e"       : {},
      "cat_jet_2BDT_Wjj_BDT_X900GeV_Res_allReco_e"       : {},
      "cat_jet_2BDT_Wjj_BDT_X900GeV_HbbFat_WjjFat_HP_m"       : {},
      "cat_jet_2BDT_Wjj_BDT_X900GeV_WjjFat_HP_m"       : {},
      "cat_jet_2BDT_Wjj_BDT_X900GeV_HbbFat_WjjFat_LP_m"       : {},
      "cat_jet_2BDT_Wjj_BDT_X900GeV_WjjFat_LP_m"       : {},
      "cat_jet_2BDT_Wjj_BDT_X900GeV_HbbFat_WjjRes_allReco_m"       : {},
      "cat_jet_2BDT_Wjj_BDT_X900GeV_Res_allReco_m"       : {},
      "cat_jet_2BDT_Wjj_BDT_X900GeV_HbbFat_WjjRes_MissJet_e"       : {},
      "cat_jet_2BDT_Wjj_BDT_X900GeV_Res_MissWJet_e"       : {},
      "cat_jet_2BDT_Wjj_BDT_X900GeV_HbbFat_WjjRes_MissJet_m"       : {},
      "cat_jet_2BDT_Wjj_BDT_X900GeV_Res_MissWJet_m"       : {},
      "cat_jet_2BDT_Wjj_BDT_X900GeV_Res_MissBJet_m"       : {},
      "cat_jet_2BDT_Wjj_BDT_X900GeV_Res_MissBJet_e"       : {},
      ###############
      "cat_jet_2BDT_Wjj_simple_X900GeV_HbbFat_WjjFat_HP_e"       : {},
      "cat_jet_2BDT_Wjj_simple_X900GeV_WjjFat_HP_e"       : {},
      "cat_jet_2BDT_Wjj_simple_X900GeV_HbbFat_WjjFat_LP_e"       : {},
      "cat_jet_2BDT_Wjj_simple_X900GeV_WjjFat_LP_e"       : {},
      "cat_jet_2BDT_Wjj_simple_X900GeV_HbbFat_WjjRes_allReco_e"       : {},
      "cat_jet_2BDT_Wjj_simple_X900GeV_Res_allReco_e"       : {},
      "cat_jet_2BDT_Wjj_simple_X900GeV_HbbFat_WjjFat_HP_m"       : {},
      "cat_jet_2BDT_Wjj_simple_X900GeV_WjjFat_HP_m"       : {},
      "cat_jet_2BDT_Wjj_simple_X900GeV_HbbFat_WjjFat_LP_m"       : {},
      "cat_jet_2BDT_Wjj_simple_X900GeV_WjjFat_LP_m"       : {},
      "cat_jet_2BDT_Wjj_simple_X900GeV_HbbFat_WjjRes_allReco_m"       : {},
      "cat_jet_2BDT_Wjj_simple_X900GeV_Res_allReco_m"       : {},
      "cat_jet_2BDT_Wjj_simple_X900GeV_HbbFat_WjjRes_MissJet_e"       : {},
      "cat_jet_2BDT_Wjj_simple_X900GeV_Res_MissWJet_e"       : {},
      "cat_jet_2BDT_Wjj_simple_X900GeV_HbbFat_WjjRes_MissJet_m"       : {},
      "cat_jet_2BDT_Wjj_simple_X900GeV_Res_MissWJet_m"       : {},
      "cat_jet_2BDT_Wjj_simple_X900GeV_Res_MissBJet_m"       : {},
      "cat_jet_2BDT_Wjj_simple_X900GeV_Res_MissBJet_e"       : {},
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
