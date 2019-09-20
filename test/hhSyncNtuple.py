#!/usr/bin/env python

import os, logging, sys, getpass

from tthAnalysis.HiggsToTauTau.configs.syncNtupleConfig import syncNtupleConfig
from tthAnalysis.HiggsToTauTau.jobTools import query_yes_no
from tthAnalysis.HiggsToTauTau.runConfig import tthAnalyzeParser
from tthAnalysis.HiggsToTauTau.analysisSettings import systematics

sys_choices     = systematics.an_inclusive_opts
channel_choices = [
  'hh_bbww_inclusive', 'hh_bb2l', 'hh_bb1l'
]

parser = tthAnalyzeParser()
parser.add_rle_select()
parser.add_nonnominal()
parser.add_hlt_filter()
parser.add_tau_id_wp()
parser.add_use_home()
parser.add_sys(sys_choices)
parser.add_argument('-c', '--channels',
  type = str, nargs = '+', dest = 'channels', metavar = 'channel', choices = channel_choices,
  default = channel_choices, required = False,
  help = 'R|Choice of analyses for which the sync Ntuple is used (choices: %s)' % \
         tthAnalyzeParser.cat(channel_choices),
)
parser.add_argument('-o', '--output',
  type = str, dest = 'output', metavar = 'filename', default = 'sync_bbww_Tallinn.root',
  help = 'R|Final output filename',
)
parser.add_argument('-X', '--clean',
  dest = 'clean', action = 'store_true', default = False, help = 'R|Remove all output files',
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
running_method     = args.running_method

# Additional arguments
rle_select        = os.path.expanduser(args.rle_select)
use_nonnominal    = args.original_central
tau_id_wp         = args.tau_id_wp
use_home          = args.use_home
hlt_filter        = args.hlt_filter
systematics_label = args.systematics

# Custom arguments
channels = args.channels
output   = args.output
clean    = args.clean

for systematic_label in systematics_label:
  if systematics_label != 'full':
    if not hasattr(systematics, systematic_label):
      raise ValueError('Invalid option for systematic uncertainty: %s' % systematic_label)

if __name__ == '__main__':
  logging.basicConfig(
    stream = sys.stdout,
    level  = logging.INFO,
    format = '%(asctime)s - %(levelname)s: %(message)s',
  )

  analysis = syncNtupleConfig(
    config_dir = os.path.join("/home",       getpass.getuser(), "hhAnalysis", args.era, args.version),
    output_dir = os.path.join("/hdfs/local", getpass.getuser(), "hhAnalysis", args.era, args.version),
    output_filename    = output,
    version            = version,
    era                = era,
    channels           = channels,
    dry_run            = dry_run,
    check_output_files = check_output_files,
    running_method     = running_method,
    isDebug            = debug,
    rle_select         = rle_select,
    with_mem           = False,
    use_nonnominal     = use_nonnominal,
    hlt_filter         = hlt_filter,
    tau_id_wp          = tau_id_wp,
    use_home           = use_home,
    systematics_label  = systematics_label,
    use_preselected    = False,
    project_dir        = os.path.join(os.getenv('CMSSW_BASE'), 'src', 'hhAnalysis', 'bbww'),
    file_pattern       = 'hhAnalyzeRun_%s.py',
    jet_cleaning       = '',
    gen_matching       = '',
    suffix             = 'bbww',
  )

  job_statistics = analysis.create()

  if auto_exec:
    run_analysis = True
  elif no_exec:
    run_analysis = False
  else:
    run_analysis = query_yes_no("Start jobs ?")
  if run_analysis:
    analysis.run(clean)
  else:
    sys.exit(0)
