from hhAnalysis.multilepton.samples.reclassifySamples import reclassifySamples as reclassifySamples_multilepton

def reclassifySamples(samples_era_hh, samples_era_bkg, samples_era_ttbar = None, separate_ST = False):

  # reuse the sample classification defined in HH multilepton analysis
  samples = reclassifySamples_multilepton(samples_era_hh, samples_era_bkg, samples_era_ttbar, separate_th = False)

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
          "DYToLL_0J", "DYToLL_1J", "DYToLL_2J", "ttHJetTo", "ZZTo2L2Q", "WWToLNuQQ",
        )):
      # https://gitlab.cern.ch/cms-hh-bbww/cms-hh-to-bbww/-/commit/bfb0a15b40f0b404c3ab8e79c1a1d415d07d343a
      # https://gitlab.cern.ch/cms-hh-bbww/cms-hh-to-bbww/-/commit/03b8b47e14ca5ebabb61b5d5eb7db9c527847b50
      # https://gitlab.cern.ch/cms-hh-bbww/cms-hh-to-bbww/-/commit/ccd4a39e7d164759e88079f8046add9c77837f29
      # https://gitlab.cern.ch/cms-hh-bbww/cms-hh-to-bbww/-/commit/f89c7e9671c515cb4ee1b70b9edfc73f1e1aa045
      sample_info["use_it"] = True

    if process_name.startswith("DYJetsToLL_M-50_amcatnloFXFX"):
      # disable the inclusive NLO DY sample -> use exclusive samples temporarily
      sample_info["use_it"] = False
    if sample_name.startswith('/ST') and separate_ST :
      sample_info["sample_category"] = "ST"

    if 'dipoleRecoilOn' in sample_info["sample_category"] and sample_info["sample_category"].endswith(('bbvv', 'bbvv_sl', 'bbtt')):
      sample_info["use_it"] = True

  return samples
