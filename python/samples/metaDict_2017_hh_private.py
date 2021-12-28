from collections import OrderedDict as OD

# file generated at 2021-12-28 15:45:39 with the following command:
# find_samples.py -V -i ../../tthAnalysis/NanoAOD/test/datasets/txt/datasets_hh_bbww_mc_2017_RunIIFall17MiniAODv2_private.txt -m python/samples/metaDict_2017_hh_private.py -c python/samples/sampleLocations_2017_nanoAOD_hh_bbww.txt

meta_dictionary = OD()


### event sums

sum_events = { 
}


meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-300_narrow_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2/USER"] =  OD([
  ("crab_string",           "2017v2_2021Dec27_GluGluToRadionToHHTo2B2VTo2L2Nu_M-300_narrow_13TeV-madgraph-pythia8__RunIIFall17MiniAODv2"),
  ("sample_category",       "signal_ggf_spin0_300_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_300_hh_2b2v_private"),
  ("nof_db_events",         292398),
  ("nof_db_files",          731),
  ("fsize_db",              21631420649),
  ("xsection",              0.027654),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "66.66%; status: VALID; size: 21.63GB; nevents: 292.40k; release: 9_4_0; last modified: 2021-12-27 11:27:14"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-550_narrow_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2/USER"] =  OD([
  ("crab_string",           "2017v2_2021Dec27_GluGluToRadionToHHTo2B2VTo2L2Nu_M-550_narrow_13TeV-madgraph-pythia8__RunIIFall17MiniAODv2"),
  ("sample_category",       "signal_ggf_spin0_550_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_550_hh_2b2v_private"),
  ("nof_db_events",         295200),
  ("nof_db_files",          738),
  ("fsize_db",              23948598355),
  ("xsection",              0.027654),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "83.33%; status: VALID; size: 23.95GB; nevents: 295.20k; release: 9_4_0; last modified: 2021-12-27 11:37:03"),
])


# event statistics by sample category:
# signal_ggf_spin0_300_hh_bbvv: 292.40k
# signal_ggf_spin0_550_hh_bbvv: 295.20k

