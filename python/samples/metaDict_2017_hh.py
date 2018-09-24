from collections import OrderedDict as OD

# file generated at 2018-09-23 22:44:17 with the following command:
# find_samples.py -V -i /home/karl/CMSSW_9_4_6_patch1/src/tthAnalysis/NanoAOD/test/datasets_hh_2017.txt -m python/samples/metaDict_2017_hh.py -c /hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep14_take2 -v 9_4_0

meta_dictionary = OD()


### event sums

sum_events = { 
}


meta_dictionary["/VBFToRadionToHHTo2B2VTo2L2Nu_M-300_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "NanoProduction_v2_2018Sep14_take2_VBFToRadionToHHTo2B2VTo2L2Nu_M-300_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2"),
  ("sample_category",       "signal_vbf_spin0_300_hh_bbvv"),
  ("process_name_specific", "signal_vbf_spin0_300_hh_2b2v"),
  ("nof_db_events",         279999),
  ("nof_db_files",          14),
  ("fsize_db",              18070036516),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 18.07GB; nevents: 280.00k; release: 9_4_6_patch1; last modified: 2018-09-08 05:03:56"),
])

meta_dictionary["/VBFToRadionToHHTo2B2VTo2L2Nu_M-400_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "NanoProduction_v2_2018Sep14_take2_VBFToRadionToHHTo2B2VTo2L2Nu_M-400_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2"),
  ("sample_category",       "signal_vbf_spin0_400_hh_bbvv"),
  ("process_name_specific", "signal_vbf_spin0_400_hh_2b2v"),
  ("nof_db_events",         100000),
  ("nof_db_files",          10),
  ("fsize_db",              6827583120),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 6.83GB; nevents: 100.00k; release: 9_4_6_patch1; last modified: 2018-07-24 00:07:16"),
])

meta_dictionary["/VBFToRadionToHHTo2B2VTo2L2Nu_M-750_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "NanoProduction_v2_2018Sep14_take2_VBFToRadionToHHTo2B2VTo2L2Nu_M-750_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2"),
  ("sample_category",       "signal_vbf_spin0_750_hh_bbvv"),
  ("process_name_specific", "signal_vbf_spin0_750_hh_2b2v"),
  ("nof_db_events",         100000),
  ("nof_db_files",          13),
  ("fsize_db",              7423075893),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 7.42GB; nevents: 100.00k; release: 9_4_6_patch1; last modified: 2018-07-15 02:59:32"),
])


# event statistics by sample category:
# signal_vbf_spin0_300_hh_bbvv: 280.00k
# signal_vbf_spin0_400_hh_bbvv: 100.00k
# signal_vbf_spin0_750_hh_bbvv: 100.00k

