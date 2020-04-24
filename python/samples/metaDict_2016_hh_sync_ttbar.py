from collections import OrderedDict as OD

# file generated at 2020-04-23 11:41:57 with the following command:
# find_samples.py -V -i ../../tthAnalysis/NanoAOD/test/datasets/txt/datasets_ttbar_sync_2016_RunIISummer16MiniAODv3.txt -m python/samples/metaDict_2016_hh_sync_ttbar.py

meta_dictionary = OD()


### event sums

sum_events = { 
}


meta_dictionary["/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "background"),
  ("process_name_specific", "TTTo2L2Nu"),
  ("nof_db_events",         67926800),
  ("nof_db_files",          778),
  ("fsize_db",              2988515757147),
  ("xsection",              88.4),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 2.99TB; nevents: 67.93M; release: 9_4_9; last modified: 2019-06-05 16:53:03"),
])


# event statistics by sample category:
# background: 67.93M

