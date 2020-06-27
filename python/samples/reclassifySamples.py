from hhAnalysis.multilepton.samples.reclassifySamples import reclassifySamples as reclassifySamples_multilepton

def reclassifySamples(samples_era_hh, samples_era_bkg, samples_era_ttbar = None):

  # reuse the sample classification defined in HH multilepton analysis
  samples = reclassifySamples_multilepton(samples_era_hh, samples_era_bkg, samples_era_ttbar)

  from collections import OrderedDict as OD

  for sample_name, sample_info in samples.items():

    if not isinstance(sample_info, OD):
      continue

    process_name = sample_info["process_name_specific"]

    if process_name == "TTToHadronic" and "RunIIFall17MiniAODv2" in sample_name:
      # disable TTToHadronic 2017 sample because it does not have PS weights
      # see also https://gitlab.cern.ch/cms-hh-bbww/cms-hh-to-bbww/-/commit/fbeeb76bdf52256700d929f0ae123917957510fd
      sample_info["use_it"] = False

    if process_name.startswith((
          "TTZToQQ", "TTWJetsToQQ", "HZJ_HToWW", "WminusH_HToBB_WToLNu", "WplusH_HToBB_WToLNu",
          "DYToLL_0J", "DYToLL_1J", "DYToLL_2J",
        )):
      # https://gitlab.cern.ch/cms-hh-bbww/cms-hh-to-bbww/-/commit/bfb0a15b40f0b404c3ab8e79c1a1d415d07d343a
      sample_info["use_it"] = True

    if process_name.startswith("DYJetsToLL_M-50_amcatnloFXFX"):
      # disable the inclusive NLO DY sample -> use exclusive samples temporarily
      sample_info["use_it"] = False

  return samples
