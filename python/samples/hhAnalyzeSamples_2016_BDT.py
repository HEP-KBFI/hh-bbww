from hhAnalysis.bbww.samples.hhAnalyzeSamples_2016 import samples_2016

bdt_samples = [
  "signal_ggf_nonresonant_node_sm_hh_2b2v",
  "signal_ggf_nonresonant_node_box_hh_2b2v",
  "signal_ggf_nonresonant_node_1_hh_2b2v",
  "signal_ggf_nonresonant_node_2_hh_2b2v",
  "signal_ggf_nonresonant_node_3_hh_2b2v",
  "signal_ggf_nonresonant_node_4_hh_2b2v",
  "signal_ggf_nonresonant_node_5_hh_2b2v",
  "signal_ggf_nonresonant_node_6_hh_2b2v",
  "signal_ggf_nonresonant_node_7_hh_2b2v",
  "signal_ggf_nonresonant_node_8_hh_2b2v",
  "signal_ggf_nonresonant_node_9_hh_2b2v",
  "signal_ggf_nonresonant_node_10_hh_2b2v",
  "signal_ggf_nonresonant_node_11_hh_2b2v",
  "signal_ggf_nonresonant_node_12_hh_2b2v",
  "signal_ggf_nonresonant_node_sm_hh_2b2v_sl",
  "signal_ggf_nonresonant_node_box_hh_2b2v_sl",
  "signal_ggf_nonresonant_node_1_hh_2b2v_sl",
  "signal_ggf_nonresonant_node_2_hh_2b2v_sl",
  "signal_ggf_nonresonant_node_3_hh_2b2v_sl",
  "signal_ggf_nonresonant_node_4_hh_2b2v_sl",
  "signal_ggf_nonresonant_node_5_hh_2b2v_sl",
  "signal_ggf_nonresonant_node_6_hh_2b2v_sl",
  "signal_ggf_nonresonant_node_7_hh_2b2v_sl",
  "signal_ggf_nonresonant_node_8_hh_2b2v_sl",
  "signal_ggf_nonresonant_node_9_hh_2b2v_sl",
  "signal_ggf_nonresonant_node_10_hh_2b2v_sl",
  "signal_ggf_nonresonant_node_11_hh_2b2v_sl",
  "signal_ggf_nonresonant_node_12_hh_2b2v_sl",
  "TTTo2L2Nu"
  "signal_ggf_spin0_300_hh_2b2v_sl",
  "signal_ggf_spin0_400_hh_2b2v_sl",
  "signal_ggf_spin0_500_hh_2b2v_sl",
  "signal_ggf_spin0_900_hh_2b2v_sl",
  "signal_ggf_spin0_1000_hh_2b2v_sl",
  "signal_ggf_spin0_300_hh_2b2v",
  "signal_ggf_spin0_400_hh_2b2v",
  "signal_ggf_spin0_500_hh_2b2v",
  "signal_ggf_spin0_900_hh_2b2v",
  "signal_ggf_spin0_1000_hh_2b2v",
  "TTToSemiLeptonic"
]

for sample_name, sample_info in samples_2016.items():
  if sample_name == 'sum_events': continue
  sample_info["use_it"] = sample_info["process_name_specific"] in bdt_samples
