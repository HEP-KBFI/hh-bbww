#!/usr/bin/env python
import os, logging, sys, getpass
from collections import OrderedDict as OD
from hhAnalysis.bbww.configs.analyzeConfig_hh_bb1l import analyzeConfig_hh_bb1l
from tthAnalysis.HiggsToTauTau.jobTools import query_yes_no
from tthAnalysis.HiggsToTauTau.analysisSettings import systematics
from tthAnalysis.HiggsToTauTau.runConfig import tthAnalyzeParser, filter_samples

# E.g.: ./tthAnalyzeRun_hh_bb1l.py -v 2017Dec13 -m default -e 2017

mode_choices     = [ 'default', 'forBDTtraining' ]
sys_choices      = [ 'full' ] + systematics.an_extended_opts_hh
systematics.full = systematics.an_extended_hh

parser = tthAnalyzeParser()
parser.add_modes(mode_choices)
parser.add_sys(sys_choices)
parser.add_preselect()
parser.add_nonnominal()
parser.add_tau_id_wp()
parser.add_hlt_filter()
parser.add_files_per_job()
parser.add_use_home()
parser.add_lep_mva_wp()
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
hlt_filter        = args.hlt_filter
files_per_job     = args.files_per_job
use_home          = args.use_home
lep_mva_wp        = args.lep_mva_wp

# Use the arguments
central_or_shifts = []
for systematic_label in systematics_label:
  for central_or_shift in getattr(systematics, systematic_label):
    if central_or_shift not in central_or_shifts:
      central_or_shifts.append(central_or_shift)

if mode == "default":
  if era == "2016":
    from hhAnalysis.bbww.samples.hhAnalyzeSamples_2016 import samples_2016 as samples
  elif era == "2017":
    from hhAnalysis.bbww.samples.hhAnalyzeSamples_2017 import samples_2017 as samples
    from tthAnalysis.HiggsToTauTau.samples.stitch_2017 import samples_to_stitch_2017 as samples_to_stitch
  elif era == "2018":
    from hhAnalysis.bbww.samples.hhAnalyzeSamples_2018 import samples_2018 as samples
  else:
    raise ValueError("Invalid era: %s" % era)

  # [*] use binned DY samples in BDT training                                                                                                                                                               
  dy_samples_inclusive = []
  dy_samples_binned = []
  for sample_set in samples_to_stitch:
    for sample_key, sample_value in sample_set.items():
      if sample_key == 'inclusive':
        dy_inclusive_samples = list(filter(lambda sample_name: sample_name.startswith('DY'), sample_value['samples']))
        dy_samples_inclusive.extend(dy_inclusive_samples)
      else:
        for sample_binned_value in sample_value:
          dy_binned_samples = list(
            filter(lambda sample_name: sample_name.startswith('DY'), sample_binned_value['samples']))
          dy_samples_binned.extend(dy_binned_samples)
  wjets_samples_inclusive = []
  wjets_samples_binned = []
  for sample_set in samples_to_stitch:
    for sample_key, sample_value in sample_set.items():
      if sample_key == 'inclusive':
        wjets_inclusive_samples = list(filter(lambda sample_name: sample_name.startswith('W'), sample_value['samples']))
        wjets_samples_inclusive.extend(wjets_inclusive_samples)
      else:
        for sample_binned_value in sample_value:
          wjets_binned_samples = list(
            filter(lambda sample_name: sample_name.startswith('W'), sample_binned_value['samples']))
          wjets_samples_binned.extend(wjets_binned_samples)

  for sample_name, sample_info in samples.items():
    if sample_name == 'sum_events': continue
    if sample_info["process_name_specific"] in [
      "TTTo2L2Nu_PSweights", "TTToSemiLeptonic_PSweights", "TTToHadronic_PSweights",
    ]:
      # Use non-PSweights samples for the analysis to estimate the irreducible ttbar background                                                                                                             
      sample_info["use_it"] = False
    elif sample_info["process_name_specific"] in dy_samples_binned or sample_info["process_name_specific"] in wjets_samples_binned:
      sample_info["use_it"] = False  # [*]                                                                                                                                                                  
    elif sample_info["process_name_specific"] in dy_samples_inclusive or sample_info["process_name_specific"] in wjets_samples_inclusive:
      sample_info["use_it"] = True  # [*]                  

elif mode == "forBDTtraining":
  if era == "2016":
    from hhAnalysis.bbww.samples.hhAnalyzeSamples_2016_BDT import samples_2016 as samples
  elif era == "2017":
    from hhAnalysis.bbww.samples.hhAnalyzeSamples_2017_BDT import samples_2017 as samples
    from tthAnalysis.HiggsToTauTau.samples.stitch_2017 import samples_to_stitch_2017 as samples_to_stitch
  elif era == "2018":
    from hhAnalysis.bbww.samples.hhAnalyzeSamples_2018_BDT import samples_2018 as samples
  else:
    raise ValueError("Invalid era: %s" % era)

   # [*] use binned DY samples in BDT training                                                                                                                                                               
  dy_samples_inclusive = []
  dy_samples_binned = []
  for sample_set in samples_to_stitch:
    for sample_key, sample_value in sample_set.items():
      if sample_key == 'inclusive':
        dy_inclusive_samples = list(filter(lambda sample_name: sample_name.startswith('DY'), sample_value['samples']))
        dy_samples_inclusive.extend(dy_inclusive_samples)
      else:
        for sample_binned_value in sample_value:
          dy_binned_samples = list(
            filter(lambda sample_name: sample_name.startswith('DY'), sample_binned_value['samples'])
          )
          dy_samples_binned.extend(dy_binned_samples)

  wjets_samples_inclusive = []
  wjets_samples_binned = []
  for sample_set in samples_to_stitch:
    for sample_key, sample_value in sample_set.items():
      if sample_key == 'inclusive':
        wjets_inclusive_samples = list(filter(lambda sample_name: sample_name.startswith('W'), sample_value['samples']))
        wjets_samples_inclusive.extend(wjets_inclusive_samples)
      else:
        for sample_binned_value in sample_value:
          wjets_binned_samples = list(
            filter(lambda sample_name: sample_name.startswith('W'), sample_binned_value['samples'])
          )
          wjets_samples_binned.extend(wjets_binned_samples)

  for sample_name, sample_info in samples.items():
    if sample_name == 'sum_events': continue
    if sample_info["process_name_specific"] in [
      "TTTo2L2Nu", "TTToSemiLeptonic", "TTToHadronic",
    ]:
        # Use PSweights samples only for BDT training                                                                                                                                                         
      sample_info["use_it"] = False
    elif sample_info["process_name_specific"] in dy_samples_binned or sample_info["process_name_specific"] in wjets_samples_binned:
      sample_info["use_it"] = True  # [*]
    elif sample_info["process_name_specific"] in dy_samples_inclusive or sample_info["process_name_specific"] in wjets_samples_inclusive:
      sample_info["use_it"] = False  # [*]        
else:
  raise ValueError("Internal logic error")



if era == "2016":
  from tthAnalysis.HiggsToTauTau.analysisSettings import lumi_2016 as lumi
elif era == "2017":
  from tthAnalysis.HiggsToTauTau.analysisSettings import lumi_2017 as lumi
elif era == "2018":
  from tthAnalysis.HiggsToTauTau.analysisSettings import lumi_2018 as lumi
else:
  raise ValueError("Invalid era: %s" % era)

if era == "2016":
  #hadTau_mva_wp_veto  = "dR03mvaTight"
  hadTau_mva_wp  = "dR03mvaTight"
elif era == "2017":
  #hadTau_mva_wp_veto  = "dR03mvaMedium"
  hadTau_mva_wp  = "dR03mvaMedium"
elif era == "2018":
  raise ValueError("Implement me!")
else:
  raise ValueError("Invalid era: %s" % era)

if __name__ == '__main__':
  logging.basicConfig(
    stream = sys.stdout,
    level  = logging.INFO,
    format = '%(asctime)s - %(levelname)s: %(message)s',
  )

  logging.info(
    "Running the jobs with the following systematic uncertainties enabled: %s" % \
    ', '.join(central_or_shifts)
  )
  if not use_preselected:
    logging.warning('Running the analysis on fully inclusive samples!')

  if sample_filter:
    samples = filter_samples(samples, sample_filter)

  if args.tau_id_wp:
    logging.info("Changing tau ID working point: %s -> %s" % (hadTau_mva_wp , args.tau_id_wp))
    #hadTau_mva_wp_veto = args.tau_id_wp
    hadTau_mva_wp = args.tau_id_wp

  analysis = analyzeConfig_hh_bb1l(
    configDir = os.path.join("/home",       getpass.getuser(), "hhAnalysis", era, version),
    outputDir = os.path.join("/hdfs/local", getpass.getuser(), "hhAnalysis", era, version),
    executable_analyze                    = "analyze_hh_bb1l",
    cfgFile_analyze                       = "analyze_hh_bb1l_cfg.py",
    samples                               = samples,
    lep_mva_wp                            = lep_mva_wp,
    apply_hadTauVeto                      = False,
    hadTau_mva_wp_veto                    = hadTau_mva_wp,
    applyFakeRateWeights                  = "enabled",
    central_or_shifts                     = central_or_shifts,
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
      "STMET"                             : {},
      "MVAOutput_350"                     : {},
      "MVAOutput_400"                     : {},
      "MVAOutput_750"                     : {}
    },
    select_rle_output                     = True,
    dry_run                               = dry_run,
    isDebug                               = debug,
    use_nonnominal                        = use_nonnominal,
    hlt_filter                            = hlt_filter,
    use_home                              = use_home,
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
