from hhAnalysis.bbww.samples.hhAnalyzeSamples_2017 import samples_2017 as samples

from collections import OrderedDict as OD

for sample_name, sample_info in samples.items():

  if not isinstance(sample_info, OD):
    continue

  if sample_info["type"] == "data":
    sample_info["use_it"] = False
