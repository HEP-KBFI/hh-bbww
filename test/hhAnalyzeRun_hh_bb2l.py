#!/usr/bin/env python

from hhAnalysis.bbww.configs.analyzeConfig_hh_bb2l import analyzeConfig_hh_bb2l, DEFAULT_AK8_CORR
from hhAnalysis.bbww.analysisSettings import systematics_bbww_dl as systematics
from tthAnalysis.HiggsToTauTau.jobTools import query_yes_no
from tthAnalysis.HiggsToTauTau.analysisSettings import get_lumi
from tthAnalysis.HiggsToTauTau.runConfig import tthAnalyzeParser, filter_samples
from tthAnalysis.HiggsToTauTau.common import logging, load_samples_hh_bbww as load_samples, load_samples_stitched
from hhAnalysis.multilepton.common import get_histograms_to_fit

import os
import sys
import getpass

# E.g.: ./test/hhAnalyzeRun_hh_bb2l.py -v 2017Dec13 -M LBN -m default -e 2017

dyBgr_defaults   = [ "disabled", "applyWeights_data", "applyWeights_mc" ] # CV: use this to apply data-driven DY background estimation
dyBgr_choices    = dyBgr_defaults + [ "compWeights" ] # CV: use 'compWeights' to compute inputs for data-driven DY background estimation
training_choices = [ 'BDT', 'LBN' ]
signal_choices   = [ 'nonres', 'spin0', 'spin2' ]
mode_choices     = [
  'default', 'wMEM', 'forBDTtraining', 'forBDTtraining_wMEM', 'hh_sync', 'hh_sync_wMEM',
  'ttbar_sync', 'ttbar_sync_wMEM',
]
sys_choices      = [ 'full', 'internal', 'pdf_mem' ] + systematics.an_opts_hh_bbww + [ 'MEM_bb2l' ]
systematics.full = systematics.an_full_hh_bbww
systematics.internal = systematics.an_internal_hh_bbww

parser = tthAnalyzeParser(max_help_position = 60)
parser.add_modes(mode_choices)
parser.add_sys(sys_choices)
parser.add_preselect()
parser.add_rle_select()
parser.add_lep_mva_wp(default_wp = 'hh_multilepton')
parser.add_nonnominal()
parser.add_hlt_filter()
parser.add_files_per_job()
parser.add_use_home()
parser.add_sideband(default_choice = 'disabled')
parser.add_tau_id() # compatibility with sync Ntuple workflow, otherwise ignored
parser.add_jet_cleaning('by_dr')
parser.add_gen_matching()
parser.enable_regrouped_jerc(default = 'jes_all', include_ak8 = True)
parser.add_split_trigger_sys(default = 'yes') # yes = keep only the flavor-dependent variations of the SF
parser.add_blacklist()
parser.add_argument('-dy', '--dy-background',
  type = str, nargs = '+', dest = 'dy', metavar = 'method', choices = dyBgr_choices, default = dyBgr_defaults, required = False,
  help = 'R|DY background estimation',
)
parser.add_argument('-hme', '--hmeBr',
  dest = 'add_hmeBr', action = 'store_true',
  help = 'R|add hme branch'
)
parser.add_argument('-M', '--training-method',
  type = str, nargs = '+', dest = 'training_method', metavar = 'method', choices = training_choices, required = True,
  help = 'R|Fill histograms for either or both of the methods: %s' % tthAnalyzeParser.cat(training_choices),
)
parser.add_argument('-F', '--fill-spin',
  type = str, nargs = '+', dest = 'fill_spin', metavar = 'spin', choices = signal_choices, required = False, default = [ 'nonres' ],
  help = 'R|Fill histograms for any of the following methods: %s' % tthAnalyzeParser.cat(signal_choices),
)
parser.add_argument('-iac', '--ignore-ak8-corrections',
  type = str, dest = 'ignore_ak8_corrections', metavar = 'correction', nargs = '+', choices = DEFAULT_AK8_CORR, default = [ 'PUPPI' ],
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
keep_logs          = args.keep_logs

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
sideband          = args.sideband
jet_cleaning      = args.jet_cleaning
gen_matching      = args.gen_matching
regroup_jerc      = args.enable_regrouped_jerc
split_trigger_sys = args.split_trigger_sys
use_blacklist     = args.use_blacklist
add_hmeBr         = args.add_hmeBr
doDataMCPlots     = True
dyBgr_options     = args.dy
training_method   = args.training_method
fill_spin         = args.fill_spin
ignore_ak8_corrections = args.ignore_ak8_corrections

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

fillHistograms_BDT = 'BDT' in training_method
fillHistograms_LBN = 'LBN' in training_method

fillHistograms_resonant = 'nonres' in fill_spin
fillHistograms_spin0    = 'spin0' in fill_spin
fillHistograms_spin2    = 'spin2' in fill_spin

blacklist = []
if use_blacklist:
  blacklist.append('postproc')
  if use_preselected:
    blacklist.append('skimmed_bbww')

# the Ntuples that currently have the MEM scores are computed with fakebale lepton selection
if add_hmeBr:
  #hmebranch = "{}_lep{}".format(HMEbranch_base, "Loose" if "forBDTtraining" in mode else "Fakeable")
  hmebranch = "{}_lepFakeable".format(HMEbranch_base)
if "wMEM" in mode:
  #MEMbranch = '{}_lep{}'.format(MEMbranch_base, "Loose" if "forBDTtraining" in mode else "Fakeable")
  MEMbranch = '{}_lepFakeable'.format(MEMbranch_base)

if mode == "default":
  samples = load_samples(era, suffix = "preselected" if use_preselected else "")
  samples = load_samples_stitched(samples, era, [ 'dy_nlo', 'wjets' ])
elif mode == "wMEM":
  if not use_preselected:
    raise ValueError("MEM branches can be read only from preselected Ntuples")
  samples = load_samples(era, suffix = MEMsample_base)
elif mode == "forBDTtraining":
  if use_preselected:
    raise ValueError("Producing Ntuples for BDT training from preselected Ntuples makes no sense!")
  fillHistograms_BDT = False
  fillHistograms_LBN = False
  samples = load_samples(era)
  samples = load_samples_stitched(samples, era, [ 'dy_nlo', 'wjets' ])
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

if not do_sync:
  for sample_name, sample_info in samples.items():
    if sample_name == 'sum_events':
      continue
    if fillHistograms_resonant and 'spin' in sample_info['process_name_specific']:
      sample_info["use_it"] = False
    if fillHistograms_spin0 and 'nonres' in sample_info['process_name_specific']:
      sample_info["use_it"] = False
    if fillHistograms_spin2 and 'nonres' in sample_info['process_name_specific']:
      sample_info["use_it"] = False
histograms_to_fit = {
  "EventCounter" : {}
}
masspoints = [ 250., 260., 270., 280., 300., 350., 400., 450., 500., 550., 600., 650., 700., 750., 800., 850., 900., 1000. ]
if fill_spin in ['spin0', 'spin2']:
  for masspoint in masspoints:
    # CV: add histograms for BDT-based extraction of resonant HH signal,
    #     using the categories defined in hhAnalysis/bbww/src/EventCategory_hh_bb2l_BDT.cc
    if fillHistograms_BDT:
      categories = [ "boosted", "resolved_2b", "resolved_1b" ]
      for category in categories:
        histograms_to_fit.update({ "sel/datacard/BDT/%s/$PROCESS/MVAOutput_%0.0f_%s" % (category, masspoint, fill_spin) : {} })
    # CV: add histograms for extraction of resonant HH signal based on Lorentz-Boost-Network (LBN),
    #     using the categories defined in hhAnalysis/bbww/src/EventCategory_hh_bb2l_LBN.cc
    if fillHistograms_LBN:
      categories = [
        "HH_boosted", "HH_resolved_2b", "HH_resolved_1b",
        "TT_resolved",
        "DY_resolved",
        "Other"
      ]
      for category in categories:
        histograms_to_fit.update({ "sel/datacard/LBN/%s/$PROCESS/MVAOutput_%0.0f_%s" % (category, masspoint, fill_spin) : {} })
if fillHistograms_resonant:
  bmNames = get_histograms_to_fit().keys()
  for bmName in bmNames:
    if 'spin' in bmName: continue
    if 'SM' not in bmName: continue
    if 'EventCounter' in bmName: continue
    if fillHistograms_BDT:
      categories = [ "boosted", "resolved_2b_vbf", "resolved_2b_nonvbf", "resolved_1b" ]
      for category in categories:
        histograms_to_fit.update({ "sel/datacard/BDT/%s/$PROCESS/%s" % (category, bmName) : {} })
    if fillHistograms_LBN:
      categories = [
        "HH_resolved_2b_vbf", "HH_resolved_2b_nonvbf",
        "TT_resolved",
        "DY_resolved",
        "Other"
      ]
      for category in categories:
        histograms_to_fit.update({ "sel/datacard/LBN/%s/$PROCESS/%s" % (category, bmName) : {} })
        histograms_to_fit.update({ "sel/datacard/wmem_LBN/%s/$PROCESS/%s" % (category, bmName) : {} })

if sideband == 'disabled':
  chargeSumSelections = [ "OS" ]
elif sideband == 'enabled':
  chargeSumSelections = [ "OS", "SS" ]
elif sideband == 'only':
  chargeSumSelections = [ "SS" ]
else:
  raise ValueError("Invalid choice for the sideband: %s" % sideband)

if not dyBgr_options:
  raise RuntimeError("DY background option cannot be empty")
if do_sync:
  logging.warning("Disabling DY background option")
  dyBgr_options = [ 'disabled' ]
if "compWeights" in dyBgr_options and len(dyBgr_options) > 1:
  raise RuntimeError("Cannot use 'compWeights' with other options: %s" % ', '.join(dyBgr_options))

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
    configDir = os.path.join("/scratch-persistent", getpass.getuser(), "hhAnalysis", era, version),
    localDir  = os.path.join("/home",               getpass.getuser(), "hhAnalysis", era, version),
    outputDir = os.path.join("/hdfs/local",         getpass.getuser(), "hhAnalysis", era, version),
    executable_analyze                    = "analyze2_hh_bb2l",
    cfgFile_analyze                       = "analyze_hh_bb2l_cfg.py",
    samples                               = samples,
    fillHistograms_BDT                    = fillHistograms_BDT,
    fillHistograms_LBN                    = fillHistograms_LBN,
    fillHistograms_resonant               = fillHistograms_resonant,
    fillHistograms_spin0                  = fillHistograms_spin0,
    fillHistograms_spin2                  = fillHistograms_spin2,
    MEMbranch                             = MEMbranch,
    hmebranch                             = hmebranch,
    lepton_charge_selections              = chargeSumSelections,
    applyFakeRateWeights                  = "enabled",
    central_or_shifts                     = central_or_shifts,
    lep_mva_wp                            = lep_mva_wp,
    dyBgr_options                         = dyBgr_options,
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
    executable_addDYBgr                   = "addBackgroundLeptonFlips2", # CV: use addBackgroundLeptonFlips executable from ttH analysis !!
    executable_compDYBgrWeights           = "compDYBgrWeights",
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
    keep_logs                             = keep_logs,
    blacklist                             = blacklist,
    disable_ak8_corr                      = ignore_ak8_corrections,
    submission_cmd                        = sys.argv,
    ttbar_based_mcClosure                 = True,
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
