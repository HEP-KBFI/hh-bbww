from hhAnalysis.bbww.samples.tthAnalyzeSamples_2017_hh_MEM_bb2l_BDT import samples_2017 as samples_2017_bkg
from hhAnalysis.bbww.samples.hhAnalyzeSamples_2017_hh_MEM_bb2l_BDT import samples_2017 as samples_2017_hh

from collections import OrderedDict as OD
for sample_name, sample_info in samples_2017_bkg.items():
  if not isinstance(sample_info, OD):
    continue
  sample_info["xsection"] *= sample_info["nof_events"]["Count"][0] / sample_info["nof_tree_events"]
for sample_name, sample_info in samples_2017_hh.items():
  if not isinstance(sample_info, OD):
    continue
  sample_info["xsection"] *= sample_info["nof_events"]["Count"][0] / sample_info["nof_tree_events"]

from hhAnalysis.bbww.samples.reclassifySamples import reclassifySamples
samples_2017 = reclassifySamples(samples_2017_hh, samples_2017_bkg)