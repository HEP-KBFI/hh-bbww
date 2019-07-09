from collections import OrderedDict as OD

# file generated at 2019-07-10 02:39:35 with the following command:
# find_samples.py -V -i ../../tthAnalysis/NanoAOD/test/datasets/txt/datasets_hh_bbww_sync_2016_RunIISummer16MiniAODv3.txt -m python/samples/metaDict_2016_hh_sync.py

meta_dictionary = OD()


### event sums

sum_events = { 
}


meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-750_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "signal"),
  ("process_name_specific", "signal_ggf_spin0_750_hh_2b2v"),
  ("nof_db_events",         298727),
  ("nof_db_files",          3),
  ("fsize_db",              13966996917),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 13.97GB; nevents: 298.73k; release: 9_4_9; last modified: 2019-03-03 06:58:24"),
])


# event statistics by sample category:
# signal: 298.73k

