#!/usr/bin/env python

from hhAnalysis.bbww.configs.analyzeConfig_hh_bb1l import analyzeConfig_hh_bb1l
from hhAnalysis.bbww.analysisSettings import systematics_bbww_sl as systematics
from tthAnalysis.HiggsToTauTau.jobTools import query_yes_no
from tthAnalysis.HiggsToTauTau.analysisSettings import get_lumi
from tthAnalysis.HiggsToTauTau.runConfig import tthAnalyzeParser, filter_samples
from tthAnalysis.HiggsToTauTau.common import logging, load_samples_hh_bbww as load_samples, load_samples_stitched
from hhAnalysis.multilepton.common import get_histograms_to_fit

import os
import sys
import getpass
import importlib

# E.g.: ./test/tthAnalyzeRun_hh_bb1l.py -v 2017Dec13 -m default -e 2017

training_choices = [ 'BDT', 'LBN' ]
signal_choices   = [ 'nonres', 'spin0', 'spin2' ]
mode_choices     = [ 'default', 'forBDTtraining', 'hh_sync', 'ttbar_sync' ]
sys_choices      = [ 'full', 'internal' ] + systematics.an_opts_hh_bbww
systematics.full = systematics.an_full_hh_bbww
systematics.internal = systematics.an_internal_hh_bbww

parser = tthAnalyzeParser()
parser.add_modes(mode_choices)
parser.add_sys(sys_choices)
parser.add_preselect()
parser.add_rle_select()
parser.add_lep_mva_wp(default_wp = 'hh_multilepton')
parser.add_nonnominal()
parser.add_tau_id_wp()
parser.add_hlt_filter()
parser.add_files_per_job(files_per_job = 15)
parser.add_use_home()
parser.add_tau_id()
parser.add_jet_cleaning('by_dr')
parser.add_gen_matching()
parser.enable_regrouped_jerc(default = 'jes_all', include_ak8 = True)
parser.add_split_trigger_sys(default = 'yes') # yes = keep only the flavor-dependent variations of the SF
parser.add_argument('-secondBDT', '--secondBDT',
  dest = 'second_bdt', action = 'store_true',
  help = 'R|doing second_bdt for jpa'
)
parser.add_argument('-doDataMCPlot', '--doDataMCPlot',
  dest = 'doDataMCPlots', action = 'store_true',
  help = 'R| do controlPlots'
)
parser.add_argument('-M', '--training-method',
  type = str, nargs = '+', dest = 'training_method', metavar = 'method', choices = training_choices, required = True,
  help = 'R|Fill histograms for either or both of the methods: %s' % tthAnalyzeParser.cat(training_choices),
)
parser.add_argument('-F', '--fill-spin',
  type = str, nargs = '+', dest = 'fill_spin', metavar = 'spin', choices = signal_choices, required = False, default = [ 'nonres' ],
  help = 'R|Fill histograms for any of the following methods: %s' % tthAnalyzeParser.cat(signal_choices),
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
lep_mva_wp        = args.lep_mva_wp
files_per_job     = args.files_per_job
use_home          = args.use_home
tau_id            = args.tau_id
jet_cleaning      = args.jet_cleaning
gen_matching      = args.gen_matching
regroup_jerc      = args.enable_regrouped_jerc
split_trigger_sys = args.split_trigger_sys
doDataMCPlots     = args.doDataMCPlots
ignore_Wjj_boosted = True
second_bdt         = args.second_bdt
training_method    = args.training_method
fill_spin          = args.fill_spin

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
  elif regroup_jerc == 'jes_ak8':
    systematics.full.extend(systematics.AK8_JEC_regrouped)
  elif regroup_jerc == 'jes_all':
    systematics.full.extend(systematics.JEC_regrouped_ALL)
  elif regroup_jerc == 'all':
    systematics.full.extend(systematics.JEC_regrouped_ALL + systematics.JER_split_ALL)
  else:
    raise RuntimeError("Invalid choice: %s" % regroup_jerc)
if split_trigger_sys == 'yes':
  for trigger_sys in systematics.triggerSF:
    del systematics.internal[systematics.internal.index(trigger_sys)]
    del systematics.full[systematics.full.index(trigger_sys)]
if split_trigger_sys in [ 'yes', 'both' ]:
  systematics.internal.extend(systematics.triggerSF_1l)
  systematics.full.extend(systematics.triggerSF_1l)

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

fillHistograms_BDT = 'BDT' in training_method
fillHistograms_LBN = 'LBN' in training_method

fillHistograms_nonresonant       = 'spin0' not in fill_spin and 'spin2' not in fill_spin
fillHistograms_resonant_spin0    = 'spin0' in fill_spin
fillHistograms_resonant_spin2    = 'spin2' in fill_spin

if "sync" not in mode:
  samples_to_stitch = getattr(
    importlib.import_module("tthAnalysis.HiggsToTauTau.samples.stitch"),
    "samples_to_stitch_{}".format(era)
  )
blacklisted_categories = []
if mode == "default":
  samples = load_samples(era, suffix = "preselected_sl" if use_preselected else "")
  samples = load_samples_stitched(samples, era, [ 'dy_nlo', 'wjets' ])
elif mode == "forBDTtraining":
  samples = load_samples(era)
  if not second_bdt : samples = load_samples_stitched(samples, era, [ 'dy_nlo', 'wjets' ])
  if second_bdt :
    for sample_name, sample_info in samples.items():
      if sample_name == 'sum_events':
        continue
      if sample_info["sample_category"] in blacklisted_categories:
        sample_info["use_it"] = False
        continue
      if sample_name.startswith(('/MuonEG/', '/Tau/')):
        sample_info["use_it"] = False
      if sample_name.startswith(('/TTToSemiLeptonic')) and sample_info["process_name_specific"] in ["TTToSemiLeptonic"]:
        sample_info["use_it"] = True
      elif sample_info['process_name_specific'].find('signal_ggf') != -1 and sample_info['process_name_specific'].find('_sl') != -1:
        sample_info["use_it"] = True
      else :
        sample_info["use_it"] = False
elif mode == "hh_sync":
  samples = load_samples(era, suffix = "sync")
elif mode == "ttbar_sync":
  samples = load_samples(era, suffix = "sync_ttbar")
else:
  raise ValueError("Internal logic error")

histograms_to_fit = {
  "EventCounter" : {}
}
masspoints = [ 250., 260., 270., 280., 300., 350., 400., 450., 500., 550., 600., 650., 700., 750., 800., 850., 900., 1000. ]
if 'spin0' in fill_spin or 'spin2' in fill_spin:
  for spin in fill_spin:
    for masspoint in masspoints:
      # CV: add histograms for BDT-based extraction of resonant HH signal,
      #     using the categories defined in hhAnalysis/bbww/src/EventCategory_hh_bb2l_BDT.cc
      if fillHistograms_BDT:
        categories = [ "boosted", "resolved_2b", "resolved_1b" ]
        for category in categories:
          histograms_to_fit.update({ "sel/datacard/BDT/%s/$PROCESS/MVAOutput_%0.0f_%s" % (category, masspoint, spin) : {} })
          # CV: add histograms for extraction of resonant HH signal based on Lorentz-Boost-Network (LBN),
          #     using the categories defined in hhAnalysis/bbww/src/EventCategory_hh_bb2l_LBN.cc
      if fillHistograms_LBN:
        categories = [
          "HH_boosted", "HH_resolved_2b", "HH_resolved_1b",
          "TT_boosted", "TT_resolved",
          "W_boosted", "W_resolved",
          "H_boosted", "H_resolved_2b", "H_resolved_1b",
          "Other"
        ]
        for category in categories:
          histograms_to_fit.update({ "sel/datacard/LBN/%s/$PROCESS/MVAOutput_%0.0f_%s" % (category, masspoint, spin) : {} })
          if masspoint in [400, 450]:
            histograms_to_fit.update({ "sel/datacard/LBN/%s/$PROCESS/MVAOutput_%0.0f_overlap_%s" % (category, masspoint, spin) : {} })
if 'nonres' in fill_spin:
  bmNames = get_histograms_to_fit().keys()
  for bmName in bmNames:
    if fillHistograms_BDT:
      categories = [ "boosted", "resolved_2b_vbf", "resolved_2b_nonvbf", "resolved_1b" ]
      for category in categories:
        histograms_to_fit.update({ "sel/datacard/BDT/%s/$PROCESS/%s" % (category, bmName) : {} })
    if fillHistograms_LBN:
      categories = [ 
        "HH_boosted", "HH_resolved_2b_vbf", "HH_resolved_2b_nonvbf", "HH_resolved_1b_vbf", "HH_resolved_1b_nonvbf", 
        "TT_boosted", "TT_resolved", 
        "W_boosted", "W_resolved", 
        "DY_boosted", "DY_resolved", 
        "SingleTop_boosted", "SingleTop_resolved", 
        "Other" 
      ]
      for category in categories:
        histograms_to_fit.update({ "sel/datacard/LBN/%s/$PROCESS/%s" % (category, bmName) : {} })

hadTauWP_veto_map = {
  'dR03mva' : 'Medium',
  'deepVSj' : 'Medium',
}
hadTau_selection_veto = tau_id + hadTauWP_veto_map[tau_id]
for sample_name, sample_info in samples.items():
  if sample_name == 'sum_events': continue
  if sample_info["type"] == "data":
    sample_info["use_it"] = sample_name.startswith(("/SingleElectron/", "/SingleMuon/", "/EGamma/"))
  if 'nonres' in fill_spin and 'spin' in sample_info['process_name_specific']:
    sample_info["use_it"] = False
  if 'spin0' in fill_spin and 'nonres' in sample_info['process_name_specific']:
    sample_info["use_it"] = False
  if 'spin2' in fill_spin and 'nonres' in sample_info['process_name_specific']:
    sample_info["use_it"] = False

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
    executable_analyze                    = "analyze2_hh_bb1l",
    cfgFile_analyze                       = "analyze_hh_bb1l_cfg.py",
    samples                               = samples,
    fillHistograms_BDT                    = fillHistograms_BDT,
    fillHistograms_LBN                    = fillHistograms_LBN,
    fillHistograms_nonresonant            = fillHistograms_nonresonant,
    fillHistograms_resonant_spin0         = fillHistograms_resonant_spin0,
    fillHistograms_resonant_spin2         = fillHistograms_resonant_spin2,
    apply_hadTauVeto                      = True,
    hadTau_mva_wp_veto                    = hadTau_selection_veto,
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
    executable_addSysTT                   = "addSysTT2",
    executable_addBackgrounds             = "addBackgrounds2",
    executable_addFakes                   = "addBackgroundLeptonFakes2",
    histograms_to_fit                     = histograms_to_fit,
    max_depth_recursion                   = 5,
    select_rle_output                     = True,
    dry_run                               = dry_run,
    do_sync                               = do_sync,
    isDebug                               = debug,
    rle_select                            = rle_select,
    use_nonnominal                        = use_nonnominal,
    hlt_filter                            = hlt_filter,
    use_home                              = use_home,
    submission_cmd                        = sys.argv,
    second_bdt                            = second_bdt
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
