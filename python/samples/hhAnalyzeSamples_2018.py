from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2018_base import samples_2018 as samples_2018_bkg
from hhAnalysis.bbww.samples.hhAnalyzeSamples_2018_hh import samples_2018 as samples_2018_hh

samples_2018_ttbar = None
try:
  from hhAnalysis.bbww.samples.hhAnalyzeSamples_2018_ttbar import samples_2018 as samples_2018_ttbar
except ImportError:
  pass

from hhAnalysis.multilepton.samples.reclassifySamples import reclassifySamples
samples_2018 = reclassifySamples(samples_2018_hh, samples_2018_bkg, samples_2018_ttbar)
