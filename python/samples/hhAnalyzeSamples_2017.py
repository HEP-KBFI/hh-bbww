from hhAnalysis.multilepton.samples.hhAnalyzeSamples_2017_bkg import samples_2017 as samples_2017_bkg
from hhAnalysis.bbww.samples.hhAnalyzeSamples_2017_hh import samples_2017 as samples_2017_hh
from hhAnalysis.multilepton.samples.hhAnalyzeSamples_2017_wjets import samples_2017 as samples_2017_wjets

import collections
import itertools
import copy

sum_events_hh  = copy.deepcopy(samples_2017_hh['sum_events'])
sum_events_bkg = copy.deepcopy(samples_2017_bkg['sum_events'])
sum_events_wjets = copy.deepcopy(samples_2017_wjets['sum_events'])

del samples_2017_hh['sum_events']
del samples_2017_bkg['sum_events']
del samples_2017_wjets['sum_events']

samples_2017 = collections.OrderedDict(itertools.chain(
  samples_2017_bkg.items(), samples_2017_hh.items(), samples_2017_wjets.items()
))

samples_2017['sum_events'] = sum_events_hh + sum_events_bkg

from collections import OrderedDict as OD

for sample_name, sample_info in samples_2017.items():

  if not isinstance(sample_info, OD):
    continue

  if 'CountWeightedLHEWeightScale' in sample_info["nof_events"] and \
      sample_info["nof_events"]['CountWeightedLHEWeightScale'] == [ 0 ]:
    sample_info["has_LHE"] = False

  if sample_info["process_name_specific"].startswith('signal') and 'hh' in sample_info["process_name_specific"]:
    sample_info["use_it"] = 'noncorr' not in sample_info["process_name_specific"] # temp: enable resonant samples only

  if sample_name.startswith('/ZZ'):
    sample_info["sample_category"] = "ZZ"
  elif sample_name.startswith('/WZ'):
    sample_info["sample_category"] = "WZ"
  elif sample_name.startswith('/WW'):
    sample_info["sample_category"] = "WW"
  elif sample_name.startswith('/DY') and sample_name.find('JetsToLL') != -1 and sample_name.find('JetsToLL') < 10:
    sample_info["sample_category"] = "DY"
  elif sample_name.startswith('/W') and sample_name.find('JetsToLNu') != -1 and sample_name.find('JetsToLNu') < 10:
    sample_info["sample_category"] = "W"
  elif sample_name.startswith('/ttH'):
    sample_info["sample_category"] = "TTH"

  if sample_info["sample_category"] == "Rares":
    sample_info["sample_category"] = "Other"
  if sample_info["sample_category"] in [ "tHq", "tHW" ]:
    sample_info["sample_category"] = "TH"

  ##if sample_name in samples_2017_wjets:
  ##  sample_info["use_it"] = False

