from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2017_base import samples_2017 as samples_2017_bkg
from hhAnalysis.bbww.samples.hhAnalyzeSamples_2017_hh import samples_2017 as samples_2017_hh

from hhAnalysis.multilepton.samples.reclassifySamples import reclassifySamples
samples_2017 = reclassifySamples(samples_2017_hh, samples_2017_bkg)
