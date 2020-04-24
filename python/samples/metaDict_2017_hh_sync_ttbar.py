from collections import OrderedDict as OD

# file generated at 2020-04-23 11:44:33 with the following command:
# find_samples.py -V -i ../../tthAnalysis/NanoAOD/test/datasets/txt/datasets_ttbar_sync_2017_RunIIFall17MiniAODv2.txt -m python/samples/metaDict_2017_hh_sync_ttbar.py

meta_dictionary = OD()


### event sums

sum_events = { 
}


meta_dictionary["/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "background"),
  ("process_name_specific", "TTTo2L2Nu_PSweights"),
  ("nof_db_events",         69155808),
  ("nof_db_files",          1056),
  ("fsize_db",              3693271643807),
  ("xsection",              88.4),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 3.69TB; nevents: 69.16M; release: 9_4_7; last modified: 2018-11-25 13:11:01"),
])


# event statistics by sample category:
# background: 69.16M

