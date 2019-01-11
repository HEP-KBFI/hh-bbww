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
  elif era == "2018":
    from hhAnalysis.bbww.samples.hhAnalyzeSamples_2018 import samples_2018 as samples
  else:
    raise ValueError("Invalid era: %s" % era)
elif mode == "forBDTtraining":
  if era == "2016":
    from hhAnalysis.bbww.samples.hhAnalyzeSamples_2016_BDT import samples_2016 as samples
  elif era == "2017":
    from hhAnalysis.bbww.samples.hhAnalyzeSamples_2017_BDT import samples_2017 as samples
  elif era == "2018":
    from hhAnalysis.bbww.samples.hhAnalyzeSamples_2018_BDT import samples_2018 as samples
  else:
    raise ValueError("Invalid era: %s" % era)
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
  hadTau_mva_wp_veto  = "dR03mvaTight"
elif era == "2017":
  hadTau_mva_wp_veto  = "dR03mvaMedium"
elif era == "2018":
  raise ValueError("Implement me!")
else:
  raise ValueError("Invalid era: %s" % era)


self.categories = []
    for type_bb_and_leptons in [
      "bb1l",    "2bM1l",    "1bM1bL1l",  "1bM1l",
      "bb1e",    "2bM1e",    "1bM1bL1e",  "1bM1e",
      "bb1mu",   "2bM1mu",   "1bM1bL1mu", "1bM1mu" ]:
      for type_Hbb in [ "", "_resolvedHbb", "_boostedHbb" ]:
        for type_Wjj in [ "", "_resolvedWjj", "_boostedWjj_lowPurity", "_boostedWjj_highPurity" ]:
          if (type_Hbb == "" and type_Wjj != "") or (type_Hbb != "" and type_Wjj == ""):
            continue
          for type_vbf in [ "", "_vbf", "_nonvbf" ]:
            self.categories.append("hh_%s%s%s%s" % (type_bb_and_leptons, type_Hbb, type_Wjj, type_vbf))
    self.category_inclusive = "hh_bb1l"

evtCategories = None
if mode == "default" and len(central_or_shifts) <= 1:
  evtCategories = [
    "hh_bb1l", "hh_bb1l_resolvedHbb_resolvedWjj", "hh_bb1l_resolvedHbb_resolvedWjj_vbf", "hh_bb1l_resolvedHbb_resolvedWjj_nonvbf",
    "hh_bb1l_boostedHbb_resolvedWjj", "hh_bb1l_boostedHbb_boostedWjj_lowPurity", "hh_bb1l_boostedHbb_boostedWjj_highPurity", "hh_bb1l_vbf", "hh_bb1l_nonvbf", 
    "hh_2bM1l", "hh_2bM1l_resolvedHbb_resolvedWjj", "hh_2bM1l_resolvedHbb_resolvedWjj_vbf", "hh_2bM1l_resolvedHbb_resolvedWjj_nonvbf",
    "hh_2bM1l_boostedHbb_resolvedWjj", "hh_2bM1l_boostedHbb_boostedWjj_lowPurity", "hh_2bM1l_boostedHbb_boostedWjj_highPurity", "hh_2bM1l_vbf", "hh_2bM1l_nonvbf", 
    "hh_1bM1bL1l", "hh_1bM1bL1l_resolvedHbb_resolvedWjj", "hh_1bM1bL1l_resolvedHbb_resolvedWjj_vbf", "hh_1bM1bL1l_resolvedHbb_resolvedWjj_nonvbf",
    "hh_1bM1bL1l_boostedHbb_resolvedWjj", "hh_1bM1bL1l_boostedHbb_boostedWjj_lowPurity", "hh_1bM1bL1l_boostedHbb_boostedWjj_highPurity", "hh_1bM1bL1l_vbf", "hh_1bM1bL1l_nonvbf", 
    "hh_1bM1l", "hh_1bM1l_resolvedHbb_resolvedWjj", "hh_1bM1l_resolvedHbb_resolvedWjj_vbf", "hh_1bM1l_resolvedHbb_resolvedWjj_nonvbf",
    "hh_1bM1l_boostedHbb_resolvedWjj", "hh_bb1l_boostedHbb_boostedWjj_lowPurity", "hh_1bM1l_boostedHbb_boostedWjj_highPurity", "hh_1bM1l_vbf", "hh_1bM1l_nonvbf", 
    "hh_bb1e", "hh_bb1e_resolvedHbb_resolvedWjj", "hh_bb1e_resolvedHbb_resolvedWjj_vbf", "hh_bb1e_resolvedHbb_resolvedWjj_nonvbf",
    "hh_bb1e_boostedHbb_resolvedWjj", "hh_bb1e_boostedHbb_boostedWjj_lowPurity", "hh_bb1e_boostedHbb_boostedWjj_highPurity", "hh_bb1e_vbf", "hh_bb1e_nonvbf", 
    "hh_2bM1e", "hh_2bM1e_resolvedHbb_resolvedWjj", "hh_2bM1e_resolvedHbb_resolvedWjj_vbf", "hh_2bM1e_resolvedHbb_resolvedWjj_nonvbf",
    "hh_2bM1e_boostedHbb_resolvedWjj", "hh_2bM1e_boostedHbb_boostedWjj_lowPurity", "hh_2bM1e_boostedHbb_boostedWjj_highPurity", "hh_2bM1e_vbf", "hh_2bM1e_nonvbf", 
    "hh_1bM1bL1e", "hh_1bM1bL1e_resolvedHbb_resolvedWjj", "hh_1bM1bL1e_resolvedHbb_resolvedWjj_vbf", "hh_1bM1bL1e_resolvedHbb_resolvedWjj_nonvbf",
    "hh_1bM1bL1e_boostedHbb_resolvedWjj", "hh_1bM1bL1e_boostedHbb_boostedWjj_lowPurity", "hh_1bM1bL1e_boostedHbb_boostedWjj_highPurity", "hh_1bM1bL1e_vbf", "hh_1bM1bL1e_nonvbf", 
    "hh_1bM1e", "hh_1bM1e_resolvedHbb_resolvedWjj", "hh_1bM1e_resolvedHbb_resolvedWjj_vbf", "hh_1bM1e_resolvedHbb_resolvedWjj_nonvbf",
    "hh_1bM1e_boostedHbb_resolvedWjj", "hh_bb1e_boostedHbb_boostedWjj_lowPurity", "hh_1bM1e_boostedHbb_boostedWjj_highPurity", "hh_1bM1e_vbf", "hh_1bM1e_nonvbf", 
    "hh_bb1mu", "hh_bb1mu_resolvedHbb_resolvedWjj", "hh_bb1mu_resolvedHbb_resolvedWjj_vbf", "hh_bb1mu_resolvedHbb_resolvedWjj_nonvbf",
    "hh_bb1mu_boostedHbb_resolvedWjj", "hh_bb1mu_boostedHbb_boostedWjj_lowPurity", "hh_bb1mu_boostedHbb_boostedWjj_highPurity", "hh_bb1mu_vbf", "hh_bb1mu_nonvbf", 
    "hh_2bM1mu", "hh_2bM1mu_resolvedHbb_resolvedWjj", "hh_2bM1mu_resolvedHbb_resolvedWjj_vbf", "hh_2bM1mu_resolvedHbb_resolvedWjj_nonvbf",
    "hh_2bM1mu_boostedHbb_resolvedWjj", "hh_2bM1mu_boostedHbb_boostedWjj_lowPurity", "hh_2bM1mu_boostedHbb_boostedWjj_highPurity", "hh_2bM1mu_vbf", "hh_2bM1mu_nonvbf", 
    "hh_1bM1bL1mu", "hh_1bM1bL1mu_resolvedHbb_resolvedWjj", "hh_1bM1bL1mu_resolvedHbb_resolvedWjj_vbf", "hh_1bM1bL1mu_resolvedHbb_resolvedWjj_nonvbf",
    "hh_1bM1bL1mu_boostedHbb_resolvedWjj", "hh_1bM1bL1mu_boostedHbb_boostedWjj_lowPurity", "hh_1bM1bL1mu_boostedHbb_boostedWjj_highPurity", "hh_1bM1bL1mu_vbf", "hh_1bM1bL1mu_nonvbf", 
    "hh_1bM1mu", "hh_1bM1mu_resolvedHbb_resolvedWjj", "hh_1bM1mu_resolvedHbb_resolvedWjj_vbf", "hh_1bM1mu_resolvedHbb_resolvedWjj_nonvbf",
    "hh_1bM1mu_boostedHbb_resolvedWjj", "hh_bb1mu_boostedHbb_boostedWjj_lowPurity", "hh_1bM1mu_boostedHbb_boostedWjj_highPurity", "hh_1bM1mu_vbf", "hh_1bM1mu_nonvbf"
  ]
else:
  evtCategories = []

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
    logging.info("Changing tau ID working point: %s -> %s" % (hadTau_mva_wp_veto, args.tau_id_wp))
    hadTau_mva_wp_veto = args.tau_id_wp

  analysis = analyzeConfig_hh_bb1l(
    configDir = os.path.join("/home",       getpass.getuser(), "hhAnalysis", era, version),
    outputDir = os.path.join("/hdfs/local", getpass.getuser(), "hhAnalysis", era, version),
    executable_analyze                    = "analyze_hh_bb1l",
    cfgFile_analyze                       = "analyze_hh_bb1l_cfg.py",
    samples                               = samples,
    lep_mva_wp                            = lep_mva_wp,
    apply_hadTauVeto                      = False,
    hadTau_mva_wp_veto                    = hadTau_mva_wp_veto,
    applyFakeRateWeights                  = "enabled",
    central_or_shifts                     = central_or_shifts,
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
      "HT"                                : {},
      "STMET"                             : {}
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
