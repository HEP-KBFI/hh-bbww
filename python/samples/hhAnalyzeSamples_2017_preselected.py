from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2017_preselected_base import samples_2017 as samples_2017_bkg
from hhAnalysis.bbww.samples.hhAnalyzeSamples_2017_hh_preselected import samples_2017 as samples_2017_hh
from hhAnalysis.bbww.samples.hhAnalyzeSamples_2017_ttbar_preselected import samples_2017 as samples_2017_ttbar

from hhAnalysis.bbww.samples.reclassifySamples import reclassifySamples
samples_2017 = reclassifySamples(samples_2017_hh, samples_2017_bkg, samples_2017_ttbar)
