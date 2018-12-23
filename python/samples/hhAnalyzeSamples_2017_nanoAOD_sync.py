from hhAnalysis.bbww.samples.hhAnalyzeSamples_2017_nanoAOD_hh import samples_2017

sync_key = "/GluGluToRadionToHHTo2B2VTo2L2Nu_M-750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"

samples_2017[sync_key]['local_paths'][0]['path'] = '/hdfs/local/karl/sync_ntuples/nanoAODproduction/2018Dec24/signal_ggf_spin0_750_hh_2b2v'
samples_2017[sync_key]['nof_files'] = 1
samples_2017[sync_key]['nof_tree_events'] = 52000

for sample_key in samples_2017:
  if sample_key not in [ sync_key, 'sum_events' ]:
    del samples_2017[sample_key]
