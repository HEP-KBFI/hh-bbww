from collections import OrderedDict as OD

# file generated at 2019-05-02 01:40:57 with the following command:
# find_samples.py -V -i ../../tthAnalysis/NanoAOD/test/datasets/txt/datasets_hh_bbww_sync_2017_RunIIFall17MiniAODv2.txt -m python/samples/metaDict_2017_hh_sync.py

meta_dictionary = OD()


### event sums

sum_events = { 
}


meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "signal"),
  ("process_name_specific", "signal_ggf_spin0_750_hh_2b2v"),
  ("nof_db_events",         200000),
  ("nof_db_files",          11),
  ("fsize_db",              11931037531),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.93GB; nevents: 200.00k; release: 9_4_7; last modified: 2018-10-06 03:20:04"),
])


# event statistics by sample category:
# signal: 200.00k

