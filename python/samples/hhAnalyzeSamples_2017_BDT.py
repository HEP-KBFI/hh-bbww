from hhAnalysis.bbww.samples.hhAnalyzeSamples_2017 import samples_2017

import re

for sample_name, sample_info in samples_2017.items():
  if sample_name == 'sum_events':
    continue
  if sample_info["process_name_specific"] in [
        #"ttHToNonbb_M125_powheg",
        #"TTZJets_LO",
        #"TTWJets_LO",
        # CV: TT samples without PSweights reserved for building datacards !!
        #"TTTo2L2Nu",
        "TTTo2L2Nu_PSweights",
        #"TTToSemiLeptonic",
        "TTToSemiLeptonic_PSweights",
        #"TTToHadronic",
        "TTToHadronic_PSweights",
      ]:
    sample_info["use_it"] = True
  elif sample_info["process_name_specific"].startswith("signal") and 'hh' in sample_info["process_name_specific"]:
    sample_info["use_it"] = True #'nonresonant' not in sample_info["process_name_specific"] # temp: enable resonant samples only
  elif re.match("WZTo3LNu_(0|1|2|3)Jets.*", sample_info["process_name_specific"]):
    sample_info["use_it"] = True
  #elif re.match("WZTo3LNu_(0|1|2|3)Jets.*", sample_info["process_name_specific"]):
  #  sample_info["use_it"] = True
  else:
    sample_info["use_it"] = False
