from hhAnalysis.bbww.samples.hhAnalyzeSamples_2017 import samples_2017 as samples

for sample_name, sample_info in samples_2017.items():

  if not isinstance(sample_info, OD):
    continue

  if sample_info["type"] == "data":
    sample_info["use_it"] = False
