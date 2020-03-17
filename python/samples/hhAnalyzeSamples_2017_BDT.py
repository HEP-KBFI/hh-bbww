from hhAnalysis.bbww.samples.hhAnalyzeSamples_2017 import samples_2017

bdt_samples = [
  "signal_ggf_nonresonant_node_sm_hh_2b2v",
  "signal_ggf_nonresonant_node_2_hh_2b2v",
  "signal_ggf_nonresonant_node_3_hh_2b2v",
  "signal_ggf_nonresonant_node_7_hh_2b2v",
  "signal_ggf_nonresonant_node_9_hh_2b2v",
  "signal_ggf_nonresonant_node_12_hh_2b2v",
  "signal_ggf_nonresonant_node_sm_hh_2b2v_sl",
  "TTTo2L2Nu",
  "TTTo2L2Nu_PSweights",
  #"TTToSemiLeptonic",
  #"TTToSemiLeptonic_PSweights"
]

for sample_name, sample_info in samples_2017.items():
  if sample_name == 'sum_events': continue
  sample_info["use_it"] = sample_info["process_name_specific"] in bdt_samples
