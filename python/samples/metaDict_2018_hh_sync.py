from collections import OrderedDict as OD

# file generated at 2019-07-10 02:39:51 with the following command:
# find_samples.py -V -i ../../tthAnalysis/NanoAOD/test/datasets/txt/datasets_hh_bbww_sync_2018_RunIIAutumn18MiniAOD.txt -m python/samples/metaDict_2018_hh_sync.py

meta_dictionary = OD()


### event sums

sum_events = { 
}


meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "signal"),
  ("process_name_specific", "signal_ggf_spin0_750_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          10),
  ("fsize_db",              11645634056),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.65GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-06-01 01:25:21"),
])


# event statistics by sample category:
# signal: 200.00k

