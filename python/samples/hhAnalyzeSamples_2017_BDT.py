from hhAnalysis.bbww.samples.hhAnalyzeSamples_2017_bkg import samples_2017

for sample_name, sample_info in samples_2017.items():
  if sample_name == 'sum_events':
    continue
  if sample_info["process_name_specific"] in [
        "TTZJets_LO",
        "TTWJets_LO",
        "TTTo2L2Nu",
        "TTTo2L2Nu_PSweights",
        "TTToSemiLeptonic",
        "TTToSemiLeptonic_PSweights",
        "TTToHadronic",
        "TTToHadronic_PSweights",
      ]:
    sample_info["use_it"] = True
  else:
    sample_info["use_it"] = False
