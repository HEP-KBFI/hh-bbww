from hhAnalysis.bbww.samples.hhAnalyzeSamples_2018 import samples_2018

bdt_samples = [
  "TTTo2L2Nu",
  "TTTo2L2Nu_PSweights",
  "TTToSemiLeptonic",
  "TTToSemiLeptonic_PSweights",
  "ST_s-channel_4f_leptonDecays",
  "ST_tWll",
  "ST_t-channel_antitop_4f_inclusiveDecays",
  "ST_s-channel_4f_leptonDecays_PSweights",
  "ST_tW_antitop_5f_inclusiveDecays_ext1",
  "ST_tW_top_5f_inclusiveDecays_ext1",
  "ST_t-channel_top_4f_inclusiveDecays",
  "ST_t-channel_antitop_4f_inclusiveDecays_PSweights"
]

for sample_name, sample_info in samples_2018.items():
  if sample_name == 'sum_events': continue
  sample_info["use_it"] = sample_info["process_name_specific"] in bdt_samples or\
                          'signal' in sample_info["process_name_specific"]
