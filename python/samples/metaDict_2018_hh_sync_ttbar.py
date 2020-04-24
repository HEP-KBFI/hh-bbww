from collections import OrderedDict as OD

# file generated at 2020-04-23 11:45:23 with the following command:
# find_samples.py -V -i ../../tthAnalysis/NanoAOD/test/datasets/txt/datasets_ttbar_sync_2018_RunIIAutumn18MiniAOD.txt -m python/samples/metaDict_2018_hh_sync_ttbar.py

meta_dictionary = OD()


### event sums

sum_events = { 
}


meta_dictionary["/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "background"),
  ("process_name_specific", "TTTo2L2Nu"),
  ("nof_db_events",         64310000),
  ("nof_db_files",          968),
  ("fsize_db",              3413760837047),
  ("xsection",              88.4),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 3.41TB; nevents: 64.31M; release: 10_2_5; last modified: 2018-11-21 18:44:43"),
])


# event statistics by sample category:
# background: 64.31M

