#!/usr/bin/env python

from hhAnalysis.bbww.configs.addMEMConfig_hh_bb2l import addMEMConfig_hh_bb2l
from tthAnalysis.HiggsToTauTau.jobTools import query_yes_no
from tthAnalysis.HiggsToTauTau.analysisSettings import systematics
from tthAnalysis.HiggsToTauTau.runConfig import tthAnalyzeParser, filter_samples
from tthAnalysis.HiggsToTauTau.common import logging, load_samples_hh_bbww as load_samples

import os
import sys
import getpass

sys_choices          = [ 'full' ] + systematics.an_addMEM_opts
max_mem_integrations = 10000000
systematics.full     = systematics.an_addMEM
mode_choices = {
  'default' : 'full',
  'BDT'     : 'small',
  'sync'    : 'full',
}

parser = tthAnalyzeParser(isAddMEM = True)
parser.add_modes(mode_choices.keys())
parser.add_preselect()
parser.add_nonnominal()
parser.add_use_home(False)
parser.add_sys(sys_choices)
parser.add_argument('-shme', '--systematics-hme',
  type = str, nargs = '+', dest = 'systematics_hme', metavar = 'mode', choices = sys_choices, default = sys_choices ,
  required = False,
  help = 'R|Systematic uncertainties for HME method (choices: %s)' % tthAnalyzeParser.cat(sys_choices),
)
parser.add_argument('-n', '--max-mem-integrations',
  type = int, dest = 'max_mem_integrations', metavar = 'integer', default = max_mem_integrations,
  required = False,
  help = 'R|Maximum number of input files per one job (default: %i)' % max_mem_integrations
)
parser.add_argument('-mem', '--method-mem',
  type = bool, dest = 'method_mem', metavar = 'MEM method', default = True, required = False,
  help = 'R|Run MEM'
)
parser.add_argument('-hme', '--method-hme',
  type = bool, dest = 'method_hme', metavar = 'HME method', default = False, required = False,
  help = 'R|Run HME'
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
mode                  = args.mode
systematics_label     = args.systematics
systematics_label_hme = args.systematics_hme
use_preselected       = args.use_preselected
use_nonnominal        = args.original_central
use_home              = args.use_home

# Custom arguments
max_mem_integrations = args.max_mem_integrations
method_mem           = args.method_mem
method_hme           = args.method_hme

# Use the arguments
central_or_shifts = []
for systematic_label in systematics_label:
  for central_or_shift in getattr(systematics, systematic_label):
    if central_or_shift not in central_or_shifts:
      central_or_shifts.append(central_or_shift)
central_or_shifts_hme = []
for systematic_label_hme in systematics_label_hme:
  for central_or_shift in getattr(systematics, systematic_label_hme):
    if central_or_shift not in central_or_shifts_hme:
      central_or_shifts_hme.append(central_or_shift)

version = "%s_%s_%s" % (
  version, mode, 'nonNom' if use_nonnominal else 'nom'
)

if mode == "default":
  samples = load_samples(era, suffix = "preselected" if use_preselected else "")
elif mode == "BDT":
  if use_preselected:
    raise ValueError("Producing Ntuples for BDT training from preselected Ntuples makes no sense!")
  samples = load_samples(era, suffix = "BDT")
elif mode == "sync":
  samples = load_samples(era, suffix = "sync")
else:
  raise ValueError("Invalid mode: %s" % mode)

if __name__ == '__main__':
  logging.basicConfig(
    stream = sys.stdout,
    level  = logging.DEBUG,
    format = '%(asctime)s - %(levelname)s: %(message)s'
  )

  logging.info(
    "Running the jobs with the following systematic uncertainties enabled: %s" % \
    ', '.join(central_or_shifts)
  )
  if not use_preselected:
    logging.warning('Running the analysis on fully inclusive samples!')

  if sample_filter:
    samples = filter_samples(samples, sample_filter)

  addMEMProduction = addMEMConfig_hh_bb2l(
    treeName                 = 'Events',
    outputDir                = os.path.join("/hdfs/local", getpass.getuser(), "addMEM", era, version),
    cfgDir                   = os.path.join("/home",       getpass.getuser(), "addMEM", era, version),
    executable_addMEM        = "addMEM_hh_bb2l",
    samples                  = samples,
    era                      = era,
    check_output_files       = check_output_files,
    running_method           = running_method,
    max_files_per_job        = 1, # so that we'd have 1-1 correspondence b/w input and output files
    mem_integrations_per_job = 50,
    max_mem_integrations     = max_mem_integrations, # use -1 if you don't want to limit the nof MEM integrations
    num_parallel_jobs        = num_parallel_jobs,
    leptonSelection          = "Fakeable",
    isDebug                  = debug,
    central_or_shift         = central_or_shifts,
    central_or_shift_hme     = central_or_shifts_hme,
    dry_run                  = dry_run,
    use_nonnominal           = use_nonnominal,
    use_home                 = use_home,
    method_mem               = method_mem,
    method_hme               = method_hme,
  )

  goodToGo = addMEMProduction.create()

  if goodToGo:
    if auto_exec:
      run_addMEMProduction = True
    elif no_exec:
      run_addMEMProduction = False
    else:
      run_addMEMProduction = query_yes_no("Start jobs ?")
    if run_addMEMProduction:
      addMEMProduction.run()
