from collections import OrderedDict as OD

# file generated at 2019-07-07 19:37:57 with the following command:
# find_samples.py -V -i ../../tthAnalysis/NanoAOD/test/datasets/txt/datasets_hh_bbww_mc_2017_RunIIFall17MiniAODv2.txt -m python/samples/metaDict_2017_hh.py -s ../../tthAnalysis/NanoAOD/test/datasets/txt/sum_datasets_hh_bbww_2017_RunIIFall17MiniAODv2.txt -c python/samples/sampleLocations_2017_nanoAOD_hh_bbww.txt

meta_dictionary = OD()


### event sums

sum_events = { 
  ("signal_ggf_nonresonant_node_sm_hh_2b2v", "signal_ggf_nonresonant_node_2_hh_2b2v", "signal_ggf_nonresonant_node_3_hh_2b2v", "signal_ggf_nonresonant_node_7_hh_2b2v", "signal_ggf_nonresonant_node_9_hh_2b2v", "signal_ggf_nonresonant_node_12_hh_2b2v"),
  ("signal_ggf_nonresonant_node_sm_hh_2b2t", "signal_ggf_nonresonant_node_2_hh_2b2t", "signal_ggf_nonresonant_node_3_hh_2b2t", "signal_ggf_nonresonant_node_4_hh_2b2t", "signal_ggf_nonresonant_node_7_hh_2b2t", "signal_ggf_nonresonant_node_9_hh_2b2t", "signal_ggf_nonresonant_node_12_hh_2b2t"),
}


meta_dictionary["/VBFToRadionToHHTo2B2VTo2L2Nu_M-300_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_VBFToRadionToHHTo2B2VTo2L2Nu_M-300_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2"),
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

meta_dictionary["/VBFToRadionToHHTo2B2VTo2L2Nu_M-350_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_VBFToRadionToHHTo2B2VTo2L2Nu_M-350_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2"),
  ("sample_category",       "signal_vbf_spin0_350_hh_bbvv"),
  ("process_name_specific", "signal_vbf_spin0_350_hh_2b2v"),
  ("nof_db_events",         285000),
  ("nof_db_files",          19),
  ("fsize_db",              18927275912),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 18.93GB; nevents: 285.00k; release: 9_4_6_patch1; last modified: 2018-10-13 06:27:57"),
])

meta_dictionary["/VBFToRadionToHHTo2B2VTo2L2Nu_M-400_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_VBFToRadionToHHTo2B2VTo2L2Nu_M-400_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2"),
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
  ("crab_string",           "2017v2_2019Jun17_VBFToRadionToHHTo2B2VTo2L2Nu_M-750_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2"),
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

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo2B2VTo2L2Nu_M-250_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14"),
  ("sample_category",       "signal_ggf_spin0_250_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_250_hh_2b2v"),
  ("nof_db_events",         399998),
  ("nof_db_files",          14),
  ("fsize_db",              20842533885),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 20.84GB; nevents: 400.00k; release: 9_4_7; last modified: 2018-10-07 09:16:29"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-260_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo2B2VTo2L2Nu_M-260_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14"),
  ("sample_category",       "signal_ggf_spin0_260_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_260_hh_2b2v"),
  ("nof_db_events",         400000),
  ("nof_db_files",          17),
  ("fsize_db",              20086379241),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 20.09GB; nevents: 400.00k; release: 9_4_7; last modified: 2018-10-04 17:01:17"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-270_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo2B2VTo2L2Nu_M-270_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14"),
  ("sample_category",       "signal_ggf_spin0_270_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_270_hh_2b2v"),
  ("nof_db_events",         388000),
  ("nof_db_files",          19),
  ("fsize_db",              19501546911),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 19.50GB; nevents: 388.00k; release: 9_4_7; last modified: 2018-10-06 15:07:10"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-280_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2VTo2L2Nu_M-280_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14"),
  ("sample_category",       "signal_ggf_spin0_280_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_280_hh_2b2v"),
  ("nof_db_events",         384000),
  ("nof_db_files",          14),
  ("fsize_db",              20165336883),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 20.17GB; nevents: 384.00k; release: 9_4_7; last modified: 2018-10-06 03:15:09"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-320_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2VTo2L2Nu_M-320_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14"),
  ("sample_category",       "signal_ggf_spin0_320_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_320_hh_2b2v"),
  ("nof_db_events",         299996),
  ("nof_db_files",          20),
  ("fsize_db",              15538010606),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 15.54GB; nevents: 300.00k; release: 9_4_7; last modified: 2018-10-13 05:54:17"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-350_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2VTo2L2Nu_M-350_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14"),
  ("sample_category",       "signal_ggf_spin0_350_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_350_hh_2b2v"),
  ("nof_db_events",         300000),
  ("nof_db_files",          12),
  ("fsize_db",              15654716885),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 15.65GB; nevents: 300.00k; release: 9_4_7; last modified: 2018-10-08 08:54:59"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-400_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2VTo2L2Nu_M-400_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14"),
  ("sample_category",       "signal_ggf_spin0_400_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_400_hh_2b2v"),
  ("nof_db_events",         292000),
  ("nof_db_files",          16),
  ("fsize_db",              15536600053),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 15.54GB; nevents: 292.00k; release: 9_4_7; last modified: 2018-09-19 14:04:09"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-450_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2VTo2L2Nu_M-450_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14"),
  ("sample_category",       "signal_ggf_spin0_450_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_450_hh_2b2v"),
  ("nof_db_events",         299999),
  ("nof_db_files",          20),
  ("fsize_db",              16296871303),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 16.30GB; nevents: 300.00k; release: 9_4_7; last modified: 2018-10-15 07:11:44"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2VTo2L2Nu_M-500_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14"),
  ("sample_category",       "signal_ggf_spin0_500_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_500_hh_2b2v"),
  ("nof_db_events",         200000),
  ("nof_db_files",          12),
  ("fsize_db",              10964750047),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 10.96GB; nevents: 200.00k; release: 9_4_7; last modified: 2018-10-06 03:13:03"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-600_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2VTo2L2Nu_M-600_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14"),
  ("sample_category",       "signal_ggf_spin0_600_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_600_hh_2b2v"),
  ("nof_db_events",         199998),
  ("nof_db_files",          9),
  ("fsize_db",              11169462986),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.17GB; nevents: 200.00k; release: 9_4_7; last modified: 2018-10-05 15:39:31"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-650_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2VTo2L2Nu_M-650_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14"),
  ("sample_category",       "signal_ggf_spin0_650_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_650_hh_2b2v"),
  ("nof_db_events",         200000),
  ("nof_db_files",          12),
  ("fsize_db",              11395262580),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.40GB; nevents: 200.00k; release: 9_4_7; last modified: 2018-10-07 00:13:42"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-700_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2VTo2L2Nu_M-700_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14"),
  ("sample_category",       "signal_ggf_spin0_700_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_700_hh_2b2v"),
  ("nof_db_events",         199998),
  ("nof_db_files",          8),
  ("fsize_db",              11438629863),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.44GB; nevents: 200.00k; release: 9_4_7; last modified: 2018-10-06 03:23:28"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2VTo2L2Nu_M-750_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14"),
  ("sample_category",       "signal_ggf_spin0_750_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_750_hh_2b2v"),
  ("nof_db_events",         200000),
  ("nof_db_files",          11),
  ("fsize_db",              11931037531),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.93GB; nevents: 200.00k; release: 9_4_7; last modified: 2018-10-06 03:20:04"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-800_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2VTo2L2Nu_M-800_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14"),
  ("sample_category",       "signal_ggf_spin0_800_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_800_hh_2b2v"),
  ("nof_db_events",         197000),
  ("nof_db_files",          15),
  ("fsize_db",              11877663068),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.88GB; nevents: 197.00k; release: 9_4_7; last modified: 2018-10-07 00:11:27"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-850_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2VTo2L2Nu_M-850_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14"),
  ("sample_category",       "signal_ggf_spin0_850_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_850_hh_2b2v"),
  ("nof_db_events",         199999),
  ("nof_db_files",          15),
  ("fsize_db",              12127308050),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 12.13GB; nevents: 200.00k; release: 9_4_7; last modified: 2018-09-19 07:40:54"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-900_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2VTo2L2Nu_M-900_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14"),
  ("sample_category",       "signal_ggf_spin0_900_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_900_hh_2b2v"),
  ("nof_db_events",         100000),
  ("nof_db_files",          11),
  ("fsize_db",              5935911198),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 5.94GB; nevents: 100.00k; release: 9_4_7; last modified: 2018-10-05 15:42:45"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-1000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2VTo2L2Nu_M-1000_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_1000_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_1000_hh_2b2v"),
  ("nof_db_events",         100000),
  ("nof_db_files",          7),
  ("fsize_db",              5930718483),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 5.93GB; nevents: 100.00k; release: 9_4_7; last modified: 2018-09-19 07:41:34"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-1250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2VTo2L2Nu_M-1250_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_1250_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_1250_hh_2b2v"),
  ("nof_db_events",         100000),
  ("nof_db_files",          8),
  ("fsize_db",              6224151597),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 6.22GB; nevents: 100.00k; release: 9_4_7; last modified: 2018-10-06 14:52:05"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-1500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2VTo2L2Nu_M-1500_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_1500_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_1500_hh_2b2v"),
  ("nof_db_events",         99998),
  ("nof_db_files",          12),
  ("fsize_db",              6171310375),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 6.17GB; nevents: 100.00k; release: 9_4_7; last modified: 2018-10-06 14:47:55"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-1750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2VTo2L2Nu_M-1750_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_1750_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_1750_hh_2b2v"),
  ("nof_db_events",         100000),
  ("nof_db_files",          10),
  ("fsize_db",              6356319473),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 6.36GB; nevents: 100.00k; release: 9_4_7; last modified: 2018-10-07 00:29:09"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-2000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2VTo2L2Nu_M-2000_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_2000_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_2000_hh_2b2v"),
  ("nof_db_events",         100000),
  ("nof_db_files",          8),
  ("fsize_db",              6172348486),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 6.17GB; nevents: 100.00k; release: 9_4_7; last modified: 2018-10-05 06:52:07"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-2500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2VTo2L2Nu_M-2500_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_2500_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_2500_hh_2b2v"),
  ("nof_db_events",         97000),
  ("nof_db_files",          13),
  ("fsize_db",              6425534542),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 6.43GB; nevents: 97.00k; release: 9_4_7; last modified: 2018-10-07 00:08:21"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-3000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2VTo2L2Nu_M-3000_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_3000_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_3000_hh_2b2v"),
  ("nof_db_events",         97999),
  ("nof_db_files",          11),
  ("fsize_db",              6497731845),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 6.50GB; nevents: 98.00k; release: 9_4_7; last modified: 2018-10-06 23:58:11"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-250_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realist"),
  ("sample_category",       "signal_ggf_spin2_250_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_250_hh_2b2v"),
  ("nof_db_events",         399997),
  ("nof_db_files",          23),
  ("fsize_db",              20041115926),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 20.04GB; nevents: 400.00k; release: 9_4_7; last modified: 2019-04-12 15:14:25"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-260_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-260_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realist"),
  ("sample_category",       "signal_ggf_spin2_260_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_260_hh_2b2v"),
  ("nof_db_events",         399997),
  ("nof_db_files",          21),
  ("fsize_db",              20202072552),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 20.20GB; nevents: 400.00k; release: 9_4_7; last modified: 2019-04-13 15:33:40"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-270_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-270_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realist"),
  ("sample_category",       "signal_ggf_spin2_270_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_270_hh_2b2v"),
  ("nof_db_events",         400000),
  ("nof_db_files",          22),
  ("fsize_db",              20268702810),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 20.27GB; nevents: 400.00k; release: 9_4_7; last modified: 2019-03-27 09:00:48"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-280_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-280_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realist"),
  ("sample_category",       "signal_ggf_spin2_280_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_280_hh_2b2v"),
  ("nof_db_events",         399995),
  ("nof_db_files",          31),
  ("fsize_db",              20542842010),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 20.54GB; nevents: 400.00k; release: 9_4_7; last modified: 2019-03-24 06:41:11"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-300_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-300_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realist"),
  ("sample_category",       "signal_ggf_spin2_300_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_300_hh_2b2v"),
  ("nof_db_events",         399998),
  ("nof_db_files",          26),
  ("fsize_db",              20998766588),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 21.00GB; nevents: 400.00k; release: 9_4_7; last modified: 2019-03-27 00:22:57"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-320_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-320_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realist"),
  ("sample_category",       "signal_ggf_spin2_320_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_320_hh_2b2v"),
  ("nof_db_events",         293998),
  ("nof_db_files",          17),
  ("fsize_db",              15577989269),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 15.58GB; nevents: 294.00k; release: 9_4_7; last modified: 2019-03-31 22:54:31"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-350_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-350_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realist"),
  ("sample_category",       "signal_ggf_spin2_350_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_350_hh_2b2v"),
  ("nof_db_events",         281999),
  ("nof_db_files",          18),
  ("fsize_db",              15217194365),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 15.22GB; nevents: 282.00k; release: 9_4_7; last modified: 2019-05-31 23:25:29"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-400_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-400_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realist"),
  ("sample_category",       "signal_ggf_spin2_400_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_400_hh_2b2v"),
  ("nof_db_events",         298000),
  ("nof_db_files",          20),
  ("fsize_db",              16133391096),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 16.13GB; nevents: 298.00k; release: 9_4_7; last modified: 2019-05-22 05:12:32"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-450_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-450_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realist"),
  ("sample_category",       "signal_ggf_spin2_450_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_450_hh_2b2v"),
  ("nof_db_events",         300000),
  ("nof_db_files",          19),
  ("fsize_db",              16485829471),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 16.49GB; nevents: 300.00k; release: 9_4_7; last modified: 2019-04-07 21:09:39"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-500_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realist"),
  ("sample_category",       "signal_ggf_spin2_500_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_500_hh_2b2v"),
  ("nof_db_events",         200000),
  ("nof_db_files",          21),
  ("fsize_db",              11497248581),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.50GB; nevents: 200.00k; release: 9_4_7; last modified: 2019-05-29 05:30:25"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-550_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-550_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realist"),
  ("sample_category",       "signal_ggf_spin2_550_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_550_hh_2b2v"),
  ("nof_db_events",         200000),
  ("nof_db_files",          17),
  ("fsize_db",              11543534297),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.54GB; nevents: 200.00k; release: 9_4_7; last modified: 2019-04-11 21:07:03"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-600_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-600_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realist"),
  ("sample_category",       "signal_ggf_spin2_600_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_600_hh_2b2v"),
  ("nof_db_events",         192000),
  ("nof_db_files",          15),
  ("fsize_db",              11191273021),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.19GB; nevents: 192.00k; release: 9_4_7; last modified: 2019-05-26 15:59:22"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-650_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-650_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realist"),
  ("sample_category",       "signal_ggf_spin2_650_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_650_hh_2b2v"),
  ("nof_db_events",         200000),
  ("nof_db_files",          22),
  ("fsize_db",              11871616225),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.87GB; nevents: 200.00k; release: 9_4_7; last modified: 2019-03-16 01:36:24"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-700_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-700_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realist"),
  ("sample_category",       "signal_ggf_spin2_700_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_700_hh_2b2v"),
  ("nof_db_events",         199998),
  ("nof_db_files",          18),
  ("fsize_db",              11820942716),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.82GB; nevents: 200.00k; release: 9_4_7; last modified: 2019-04-21 19:52:47"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-750_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realist"),
  ("sample_category",       "signal_ggf_spin2_750_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_750_hh_2b2v"),
  ("nof_db_events",         198000),
  ("nof_db_files",          15),
  ("fsize_db",              11778577981),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.78GB; nevents: 198.00k; release: 9_4_7; last modified: 2019-04-10 10:51:35"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-800_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-800_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realist"),
  ("sample_category",       "signal_ggf_spin2_800_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_800_hh_2b2v"),
  ("nof_db_events",         200000),
  ("nof_db_files",          20),
  ("fsize_db",              11967660431),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.97GB; nevents: 200.00k; release: 9_4_7; last modified: 2019-03-27 00:26:37"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-850_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-850_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realist"),
  ("sample_category",       "signal_ggf_spin2_850_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_850_hh_2b2v"),
  ("nof_db_events",         200000),
  ("nof_db_files",          15),
  ("fsize_db",              12348394332),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 12.35GB; nevents: 200.00k; release: 9_4_7; last modified: 2019-03-15 16:51:13"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-900_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-900_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realist"),
  ("sample_category",       "signal_ggf_spin2_900_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_900_hh_2b2v"),
  ("nof_db_events",         99999),
  ("nof_db_files",          9),
  ("fsize_db",              6022388849),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 6.02GB; nevents: 100.00k; release: 9_4_7; last modified: 2019-04-03 11:32:26"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1000_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realis"),
  ("sample_category",       "signal_ggf_spin2_1000_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_1000_hh_2b2v"),
  ("nof_db_events",         99999),
  ("nof_db_files",          10),
  ("fsize_db",              6101733672),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 6.10GB; nevents: 100.00k; release: 9_4_7; last modified: 2019-02-19 08:53:26"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1250_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realis"),
  ("sample_category",       "signal_ggf_spin2_1250_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_1250_hh_2b2v"),
  ("nof_db_events",         100000),
  ("nof_db_files",          7),
  ("fsize_db",              6305015701),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 6.31GB; nevents: 100.00k; release: 9_4_7; last modified: 2019-03-18 15:44:31"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1500_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realis"),
  ("sample_category",       "signal_ggf_spin2_1500_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_1500_hh_2b2v"),
  ("nof_db_events",         100000),
  ("nof_db_files",          15),
  ("fsize_db",              6512057209),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 6.51GB; nevents: 100.00k; release: 9_4_7; last modified: 2019-03-19 15:28:44"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1750_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realis"),
  ("sample_category",       "signal_ggf_spin2_1750_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_1750_hh_2b2v"),
  ("nof_db_events",         99999),
  ("nof_db_files",          12),
  ("fsize_db",              6489134095),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 6.49GB; nevents: 100.00k; release: 9_4_7; last modified: 2019-03-23 13:48:05"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-2000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-2000_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realis"),
  ("sample_category",       "signal_ggf_spin2_2000_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_2000_hh_2b2v"),
  ("nof_db_events",         100000),
  ("nof_db_files",          11),
  ("fsize_db",              6328288934),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 6.33GB; nevents: 100.00k; release: 9_4_7; last modified: 2019-04-11 22:59:11"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-2500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-2500_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realis"),
  ("sample_category",       "signal_ggf_spin2_2500_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_2500_hh_2b2v"),
  ("nof_db_events",         98000),
  ("nof_db_files",          13),
  ("fsize_db",              6377937593),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 6.38GB; nevents: 98.00k; release: 9_4_7; last modified: 2019-03-24 17:28:25"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-3000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-3000_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realis"),
  ("sample_category",       "signal_ggf_spin2_3000_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_3000_hh_2b2v"),
  ("nof_db_events",         99999),
  ("nof_db_files",          12),
  ("fsize_db",              6547475897),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 6.55GB; nevents: 100.00k; release: 9_4_7; last modified: 2019-05-21 20:48:47"),
])

meta_dictionary["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_1_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_1_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_1_hh_bbvv"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_1_hh_2b2v"),
  ("nof_db_events",         399996),
  ("nof_db_files",          12),
  ("fsize_db",              22186460848),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 22.19GB; nevents: 400.00k; release: 9_4_7; last modified: 2018-10-04 12:17:37"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_SM_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToHHTo2B2VTo2L2Nu_node_SM_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_node_sm_hh_2b2v"),
  ("nof_db_events",         388999),
  ("nof_db_files",          17),
  ("fsize_db",              21257341288),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 21.26GB; nevents: 389.00k; release: 9_4_7; last modified: 2018-10-06 14:38:29"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_2_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToHHTo2B2VTo2L2Nu_node_2_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_node_2_hh_2b2v"),
  ("nof_db_events",         400000),
  ("nof_db_files",          17),
  ("fsize_db",              23088598268),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 23.09GB; nevents: 400.00k; release: 9_4_7; last modified: 2018-10-07 19:46:00"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_3_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToHHTo2B2VTo2L2Nu_node_3_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_node_3_hh_2b2v"),
  ("nof_db_events",         380000),
  ("nof_db_files",          17),
  ("fsize_db",              20768532098),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 20.77GB; nevents: 380.00k; release: 9_4_7; last modified: 2018-10-05 06:29:29"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_7_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToHHTo2B2VTo2L2Nu_node_7_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_node_7_hh_2b2v"),
  ("nof_db_events",         392999),
  ("nof_db_files",          19),
  ("fsize_db",              21440735341),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 21.44GB; nevents: 393.00k; release: 9_4_7; last modified: 2018-10-06 23:56:37"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_9_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToHHTo2B2VTo2L2Nu_node_9_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_node_9_hh_2b2v"),
  ("nof_db_events",         386999),
  ("nof_db_files",          19),
  ("fsize_db",              22534822736),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 22.53GB; nevents: 387.00k; release: 9_4_7; last modified: 2018-10-05 15:38:37"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_12_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToHHTo2B2VTo2L2Nu_node_12_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_node_12_hh_2b2v"),
  ("nof_db_events",         400000),
  ("nof_db_files",          23),
  ("fsize_db",              21561540290),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 21.56GB; nevents: 400.00k; release: 9_4_7; last modified: 2018-10-15 05:25:20"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-250_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_VBFToRadionToHHTo2B2Tau_M-250_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_spin0_250_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_250_hh_2b2t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          23),
  ("fsize_db",              24640211831),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 24.64GB; nevents: 400.00k; release: 9_4_7; last modified: 2018-10-15 05:13:26"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-260_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_VBFToRadionToHHTo2B2Tau_M-260_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_spin0_260_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_260_hh_2b2t"),
  ("nof_db_events",         388000),
  ("nof_db_files",          18),
  ("fsize_db",              24012313674),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 24.01GB; nevents: 388.00k; release: 9_4_7; last modified: 2018-09-07 04:31:39"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-270_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_VBFToRadionToHHTo2B2Tau_M-270_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2"),
  ("sample_category",       "signal_vbf_spin0_270_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_270_hh_2b2t"),
  ("nof_db_events",         384000),
  ("nof_db_files",          17),
  ("fsize_db",              23968184441),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 23.97GB; nevents: 384.00k; release: 9_4_7; last modified: 2018-08-28 23:32:32"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-280_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_VBFToRadionToHHTo2B2Tau_M-280_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_spin0_280_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_280_hh_2b2t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          23),
  ("fsize_db",              25138262751),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 25.14GB; nevents: 400.00k; release: 9_4_7; last modified: 2018-08-12 16:19:09"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-300_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_VBFToRadionToHHTo2B2Tau_M-300_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2"),
  ("sample_category",       "signal_vbf_spin0_300_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_300_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          15),
  ("fsize_db",              19012035463),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 19.01GB; nevents: 300.00k; release: 9_4_6_patch1; last modified: 2018-10-13 06:13:55"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-350_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_VBFToRadionToHHTo2B2Tau_M-350_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2"),
  ("sample_category",       "signal_vbf_spin0_350_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_350_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          11),
  ("fsize_db",              19447040410),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 19.45GB; nevents: 300.00k; release: 9_4_6_patch1; last modified: 2018-09-07 18:55:13"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-400_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_VBFToRadionToHHTo2B2Tau_M-400_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2"),
  ("sample_category",       "signal_vbf_spin0_400_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_400_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          7),
  ("fsize_db",              6609409571),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 6.61GB; nevents: 100.00k; release: 9_4_6_patch1; last modified: 2018-06-18 11:36:21"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-450_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "signal_vbf_spin0_450_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_450_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          16),
  ("fsize_db",              20167217854),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 20.17GB; nevents: 300.00k; release: 9_4_7; last modified: 2018-09-07 17:39:56"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-500_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_VBFToRadionToHHTo2B2Tau_M-500_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_spin0_500_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_500_hh_2b2t"),
  ("nof_db_events",         290000),
  ("nof_db_files",          11),
  ("fsize_db",              19708690689),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 19.71GB; nevents: 290.00k; release: 9_4_7; last modified: 2018-09-22 09:38:10"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-550_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_VBFToRadionToHHTo2B2Tau_M-550_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_spin0_550_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_550_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          13),
  ("fsize_db",              20644816504),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 20.64GB; nevents: 300.00k; release: 9_4_7; last modified: 2018-08-12 16:26:56"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-600_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_VBFToRadionToHHTo2B2Tau_M-600_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_spin0_600_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_600_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          12),
  ("fsize_db",              13957904944),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 13.96GB; nevents: 200.00k; release: 9_4_7; last modified: 2018-06-29 11:31:36"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-650_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_VBFToRadionToHHTo2B2Tau_M-650_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_spin0_650_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_650_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          7),
  ("fsize_db",              14016331858),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 14.02GB; nevents: 200.00k; release: 9_4_7; last modified: 2018-06-18 01:33:19"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-700_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_VBFToRadionToHHTo2B2Tau_M-700_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_spin0_700_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_700_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          13),
  ("fsize_db",              14253263609),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 14.25GB; nevents: 200.00k; release: 9_4_7; last modified: 2018-07-24 00:07:03"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-750_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_VBFToRadionToHHTo2B2Tau_M-750_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2"),
  ("sample_category",       "signal_vbf_spin0_750_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_750_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          7),
  ("fsize_db",              7146269195),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 7.15GB; nevents: 100.00k; release: 9_4_6_patch1; last modified: 2018-07-24 01:35:08"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-800_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_VBFToRadionToHHTo2B2Tau_M-800_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_spin0_800_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_800_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          11),
  ("fsize_db",              14420020815),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 14.42GB; nevents: 200.00k; release: 9_4_7; last modified: 2018-06-21 13:33:44"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-850_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_VBFToRadionToHHTo2B2Tau_M-850_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_spin0_850_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_850_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          14),
  ("fsize_db",              14617490096),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 14.62GB; nevents: 200.00k; release: 9_4_7; last modified: 2018-07-24 01:30:14"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-900_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_VBFToRadionToHHTo2B2Tau_M-900_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_spin0_900_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_900_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          11),
  ("fsize_db",              7382733082),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 7.38GB; nevents: 100.00k; release: 9_4_7; last modified: 2018-07-22 14:46:14"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-1000_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_VBFToRadionToHHTo2B2Tau_M-1000_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_spin0_1000_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_1000_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          7),
  ("fsize_db",              7364574553),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 7.36GB; nevents: 100.00k; release: 9_4_7; last modified: 2018-06-23 12:47:54"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-1250_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_VBFToRadionToHHTo2B2Tau_M-1250_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_spin0_1250_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_1250_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          7),
  ("fsize_db",              7497237044),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 7.50GB; nevents: 100.00k; release: 9_4_7; last modified: 2018-07-22 14:45:24"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-1500_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_VBFToRadionToHHTo2B2Tau_M-1500_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_spin0_1500_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_1500_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          5),
  ("fsize_db",              7582428905),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 7.58GB; nevents: 100.00k; release: 9_4_7; last modified: 2018-06-17 16:32:38"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-1750_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_VBFToRadionToHHTo2B2Tau_M-1750_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_spin0_1750_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_1750_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          12),
  ("fsize_db",              7802866732),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 7.80GB; nevents: 100.00k; release: 9_4_7; last modified: 2018-07-24 00:05:16"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-2000_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_VBFToRadionToHHTo2B2Tau_M-2000_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_spin0_2000_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_2000_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          11),
  ("fsize_db",              7810715378),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 7.81GB; nevents: 100.00k; release: 9_4_7; last modified: 2018-08-01 23:50:22"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-3000_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_VBFToRadionToHHTo2B2Tau_M-3000_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_spin0_3000_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_3000_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          8),
  ("fsize_db",              7943092984),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 7.94GB; nevents: 100.00k; release: 9_4_7; last modified: 2018-06-15 22:53:34"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-250_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_VBFToBulkGravitonToHHTo2B2Tau_M-250_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_spin2_250_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_250_hh_2b2t"),
  ("nof_db_events",         386000),
  ("nof_db_files",          22),
  ("fsize_db",              23569723909),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 23.57GB; nevents: 386.00k; release: 9_4_7; last modified: 2018-10-07 00:10:22"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-260_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_VBFToBulkGravitonToHHTo2B2Tau_M-260_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_spin2_260_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_260_hh_2b2t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          19),
  ("fsize_db",              22974833125),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 22.97GB; nevents: 400.00k; release: 9_4_7; last modified: 2018-10-06 14:53:58"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-270_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_VBFToBulkGravitonToHHTo2B2Tau_M-270_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_spin2_270_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_270_hh_2b2t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          19),
  ("fsize_db",              22808220732),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 22.81GB; nevents: 400.00k; release: 9_4_7; last modified: 2018-10-15 04:15:09"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-280_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_VBFToBulkGravitonToHHTo2B2Tau_M-280_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_spin2_280_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_280_hh_2b2t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          19),
  ("fsize_db",              22983626173),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 22.98GB; nevents: 400.00k; release: 9_4_7; last modified: 2018-10-15 05:05:51"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-300_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_VBFToBulkGravitonToHHTo2B2Tau_M-300_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_spin2_300_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_300_hh_2b2t"),
  ("nof_db_events",         282000),
  ("nof_db_files",          19),
  ("fsize_db",              15951259391),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 15.95GB; nevents: 282.00k; release: 9_4_7; last modified: 2018-10-04 16:58:05"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-320_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_VBFToBulkGravitonToHHTo2B2Tau_M-320_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_spin2_320_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_320_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          17),
  ("fsize_db",              17224376684),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 17.22GB; nevents: 300.00k; release: 9_4_7; last modified: 2018-10-21 07:08:07"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-350_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_VBFToBulkGravitonToHHTo2B2Tau_M-350_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_spin2_350_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_350_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          16),
  ("fsize_db",              16911146727),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 16.91GB; nevents: 300.00k; release: 9_4_7; last modified: 2018-10-06 14:54:34"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-400_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_VBFToBulkGravitonToHHTo2B2Tau_M-400_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_spin2_400_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_400_hh_2b2t"),
  ("nof_db_events",         292000),
  ("nof_db_files",          14),
  ("fsize_db",              16538417486),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 16.54GB; nevents: 292.00k; release: 9_4_7; last modified: 2018-10-06 03:07:55"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-450_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_VBFToBulkGravitonToHHTo2B2Tau_M-450_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_spin2_450_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_450_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          21),
  ("fsize_db",              16984173640),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 16.98GB; nevents: 300.00k; release: 9_4_7; last modified: 2018-10-15 06:48:49"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-500_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_VBFToBulkGravitonToHHTo2B2Tau_M-500_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_spin2_500_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_500_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          11),
  ("fsize_db",              16980250583),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 16.98GB; nevents: 300.00k; release: 9_4_7; last modified: 2018-10-05 06:25:59"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-600_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_VBFToBulkGravitonToHHTo2B2Tau_M-600_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_spin2_600_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_600_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          11),
  ("fsize_db",              11350421129),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.35GB; nevents: 200.00k; release: 9_4_7; last modified: 2018-10-05 06:36:51"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-650_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_VBFToBulkGravitonToHHTo2B2Tau_M-650_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_spin2_650_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_650_hh_2b2t"),
  ("nof_db_events",         197000),
  ("nof_db_files",          11),
  ("fsize_db",              11416936121),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.42GB; nevents: 197.00k; release: 9_4_7; last modified: 2018-10-05 15:45:09"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-700_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_VBFToBulkGravitonToHHTo2B2Tau_M-700_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_spin2_700_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_700_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          12),
  ("fsize_db",              11593555122),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.59GB; nevents: 200.00k; release: 9_4_7; last modified: 2018-10-05 06:57:15"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-750_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_VBFToBulkGravitonToHHTo2B2Tau_M-750_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_spin2_750_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_750_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          5),
  ("fsize_db",              11489097788),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.49GB; nevents: 200.00k; release: 9_4_7; last modified: 2018-10-08 08:48:13"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-850_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_VBFToBulkGravitonToHHTo2B2Tau_M-850_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_spin2_850_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_850_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          8),
  ("fsize_db",              11469515493),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.47GB; nevents: 200.00k; release: 9_4_7; last modified: 2018-10-15 04:25:15"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-900_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_VBFToBulkGravitonToHHTo2B2Tau_M-900_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_spin2_900_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_900_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          12),
  ("fsize_db",              5871346880),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 5.87GB; nevents: 100.00k; release: 9_4_7; last modified: 2018-10-06 15:02:53"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-1000_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_VBFToBulkGravitonToHHTo2B2Tau_M-1000_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_spin2_1000_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_1000_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          12),
  ("fsize_db",              5935760871),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 5.94GB; nevents: 100.00k; release: 9_4_7; last modified: 2018-10-06 03:03:38"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-1750_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_VBFToBulkGravitonToHHTo2B2Tau_M-1750_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_spin2_1750_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_1750_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          9),
  ("fsize_db",              5865706342),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 5.87GB; nevents: 100.00k; release: 9_4_7; last modified: 2018-10-06 14:45:25"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-2000_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_VBFToBulkGravitonToHHTo2B2Tau_M-2000_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_spin2_2000_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_2000_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          10),
  ("fsize_db",              6015024771),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 6.02GB; nevents: 100.00k; release: 9_4_7; last modified: 2018-10-15 04:40:56"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2Tau_M-250_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_250_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_250_hh_2b2t"),
  ("nof_db_events",         390000),
  ("nof_db_files",          17),
  ("fsize_db",              20093492648),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 20.09GB; nevents: 390.00k; release: 9_4_7; last modified: 2018-10-05 06:33:49"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-260_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2Tau_M-260_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_260_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_260_hh_2b2t"),
  ("nof_db_events",         360000),
  ("nof_db_files",          18),
  ("fsize_db",              17758553715),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 17.76GB; nevents: 360.00k; release: 9_4_7; last modified: 2018-10-27 17:57:38"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-270_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2Tau_M-270_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_270_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_270_hh_2b2t"),
  ("nof_db_events",         392000),
  ("nof_db_files",          16),
  ("fsize_db",              19361033085),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 19.36GB; nevents: 392.00k; release: 9_4_7; last modified: 2018-10-06 02:49:04"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-280_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo2B2Tau_M-280_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_280_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_280_hh_2b2t"),
  ("nof_db_events",         398000),
  ("nof_db_files",          23),
  ("fsize_db",              20704800616),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 20.70GB; nevents: 398.00k; release: 9_4_7; last modified: 2018-09-22 09:36:33"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-300_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2Tau_M-300_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_300_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_300_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          22),
  ("fsize_db",              15151937781),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 15.15GB; nevents: 300.00k; release: 9_4_7; last modified: 2018-10-15 06:54:56"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-320_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2Tau_M-320_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_320_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_320_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          13),
  ("fsize_db",              15215406969),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 15.22GB; nevents: 300.00k; release: 9_4_7; last modified: 2018-10-07 19:28:16"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-350_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2Tau_M-350_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_350_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_350_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          14),
  ("fsize_db",              15430234358),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 15.43GB; nevents: 300.00k; release: 9_4_7; last modified: 2018-10-15 06:59:41"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-400_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2Tau_M-400_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_400_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_400_hh_2b2t"),
  ("nof_db_events",         296000),
  ("nof_db_files",          16),
  ("fsize_db",              15540706594),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 15.54GB; nevents: 296.00k; release: 9_4_7; last modified: 2018-10-05 06:26:55"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-450_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2Tau_M-450_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_450_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_450_hh_2b2t"),
  ("nof_db_events",         272000),
  ("nof_db_files",          18),
  ("fsize_db",              14544281532),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 14.54GB; nevents: 272.00k; release: 9_4_7; last modified: 2018-10-22 14:06:37"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2Tau_M-500_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_500_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_500_hh_2b2t"),
  ("nof_db_events",         190000),
  ("nof_db_files",          12),
  ("fsize_db",              10300681960),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 10.30GB; nevents: 190.00k; release: 9_4_7; last modified: 2018-10-15 05:26:22"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-550_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2Tau_M-550_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_550_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_550_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          11),
  ("fsize_db",              10884541416),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 10.88GB; nevents: 200.00k; release: 9_4_7; last modified: 2018-10-05 06:43:39"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-600_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2Tau_M-600_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_600_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_600_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          12),
  ("fsize_db",              11044936345),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.04GB; nevents: 200.00k; release: 9_4_7; last modified: 2018-10-15 05:21:54"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-650_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2Tau_M-650_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_650_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_650_hh_2b2t"),
  ("nof_db_events",         188000),
  ("nof_db_files",          15),
  ("fsize_db",              10510514184),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 10.51GB; nevents: 188.00k; release: 9_4_7; last modified: 2018-10-06 14:50:47"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-700_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2Tau_M-700_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_700_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_700_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          8),
  ("fsize_db",              11214998225),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.21GB; nevents: 200.00k; release: 9_4_7; last modified: 2018-10-07 10:42:58"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2Tau_M-750_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_750_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_750_hh_2b2t"),
  ("nof_db_events",         196000),
  ("nof_db_files",          12),
  ("fsize_db",              11545737081),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.55GB; nevents: 196.00k; release: 9_4_7; last modified: 2018-10-06 23:55:15"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-800_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2Tau_M-800_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_800_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_800_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          10),
  ("fsize_db",              11819983411),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.82GB; nevents: 200.00k; release: 9_4_7; last modified: 2018-10-13 06:16:59"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-850_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2Tau_M-850_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_850_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_850_hh_2b2t"),
  ("nof_db_events",         192000),
  ("nof_db_files",          15),
  ("fsize_db",              11490975329),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.49GB; nevents: 192.00k; release: 9_4_7; last modified: 2018-10-06 14:38:59"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-900_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2Tau_M-900_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_900_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_900_hh_2b2t"),
  ("nof_db_events",         95000),
  ("nof_db_files",          7),
  ("fsize_db",              5517036529),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 5.52GB; nevents: 95.00k; release: 9_4_7; last modified: 2018-10-05 16:02:54"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-1000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2Tau_M-1000_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_1000_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_1000_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          9),
  ("fsize_db",              5887358169),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 5.89GB; nevents: 100.00k; release: 9_4_7; last modified: 2018-10-07 00:28:33"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-1250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2Tau_M-1250_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_1250_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_1250_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          9),
  ("fsize_db",              6210975535),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 6.21GB; nevents: 100.00k; release: 9_4_7; last modified: 2018-10-06 23:59:19"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-1500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2Tau_M-1500_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_1500_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_1500_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          4),
  ("fsize_db",              5949909431),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 5.95GB; nevents: 100.00k; release: 9_4_7; last modified: 2018-10-06 02:51:22"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-1750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2Tau_M-1750_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_1750_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_1750_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          11),
  ("fsize_db",              6303523737),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 6.30GB; nevents: 100.00k; release: 9_4_7; last modified: 2018-10-15 05:29:10"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-2000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2Tau_M-2000_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_2000_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_2000_hh_2b2t"),
  ("nof_db_events",         92000),
  ("nof_db_files",          6),
  ("fsize_db",              5565938746),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 5.57GB; nevents: 92.00k; release: 9_4_7; last modified: 2018-10-04 16:59:28"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-2500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2Tau_M-2500_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_2500_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_2500_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          11),
  ("fsize_db",              6456631366),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 6.46GB; nevents: 100.00k; release: 9_4_7; last modified: 2018-09-21 02:53:21"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-3000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToRadionToHHTo2B2Tau_M-3000_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_3000_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_3000_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          8),
  ("fsize_db",              6431618251),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 6.43GB; nevents: 100.00k; release: 9_4_7; last modified: 2018-10-06 03:26:36"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToBulkGravitonToHHTo2B2Tau_M-250_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_250_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_250_hh_2b2t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          23),
  ("fsize_db",              20195673518),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 20.20GB; nevents: 400.00k; release: 9_4_7; last modified: 2018-10-15 07:02:41"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-260_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToBulkGravitonToHHTo2B2Tau_M-260_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_260_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_260_hh_2b2t"),
  ("nof_db_events",         384000),
  ("nof_db_files",          17),
  ("fsize_db",              19164112451),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 19.16GB; nevents: 384.00k; release: 9_4_7; last modified: 2018-10-06 23:53:19"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-270_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToBulkGravitonToHHTo2B2Tau_M-270_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_270_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_270_hh_2b2t"),
  ("nof_db_events",         390000),
  ("nof_db_files",          18),
  ("fsize_db",              19739699313),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 19.74GB; nevents: 390.00k; release: 9_4_7; last modified: 2018-10-06 02:54:05"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-280_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToBulkGravitonToHHTo2B2Tau_M-280_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_280_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_280_hh_2b2t"),
  ("nof_db_events",         379000),
  ("nof_db_files",          20),
  ("fsize_db",              19359006495),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 19.36GB; nevents: 379.00k; release: 9_4_7; last modified: 2018-10-06 02:59:02"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2tau_M-300_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToBulkGravitonToHHTo2B2tau_M-300_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin2_300_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_300_hh_2b2t"),
  ("nof_db_events",         981549),
  ("nof_db_files",          33),
  ("fsize_db",              50466696906),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 50.47GB; nevents: 981.55k; release: 9_4_6_patch1,9_4_7; last modified: 2018-04-20 01:01:32"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-350_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToBulkGravitonToHHTo2B2Tau_M-350_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_350_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_350_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          7),
  ("fsize_db",              15849336173),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 15.85GB; nevents: 300.00k; release: 9_4_7; last modified: 2018-10-06 23:54:42"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-400_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToBulkGravitonToHHTo2B2Tau_M-400_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_400_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_400_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          15),
  ("fsize_db",              16220410321),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 16.22GB; nevents: 300.00k; release: 9_4_7; last modified: 2018-09-19 07:52:13"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-450_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToBulkGravitonToHHTo2B2Tau_M-450_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_450_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_450_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          16),
  ("fsize_db",              16455015197),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 16.46GB; nevents: 300.00k; release: 9_4_7; last modified: 2018-10-06 23:49:08"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToBulkGravitonToHHTo2B2Tau_M-500_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_500_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_500_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          8),
  ("fsize_db",              11098842678),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.10GB; nevents: 200.00k; release: 9_4_7; last modified: 2018-10-05 15:51:52"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-550_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToBulkGravitonToHHTo2B2Tau_M-550_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_550_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_550_hh_2b2t"),
  ("nof_db_events",         192000),
  ("nof_db_files",          14),
  ("fsize_db",              10855478264),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 10.86GB; nevents: 192.00k; release: 9_4_7; last modified: 2018-10-04 16:56:34"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-600_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToBulkGravitonToHHTo2B2Tau_M-600_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_600_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_600_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          17),
  ("fsize_db",              11487024358),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.49GB; nevents: 200.00k; release: 9_4_7; last modified: 2018-10-18 09:35:09"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-650_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToBulkGravitonToHHTo2B2Tau_M-650_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_650_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_650_hh_2b2t"),
  ("nof_db_events",         188000),
  ("nof_db_files",          14),
  ("fsize_db",              10754684541),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 10.75GB; nevents: 188.00k; release: 9_4_7; last modified: 2018-10-17 12:55:13"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToBulkGravitonToHHTo2B2Tau_M-750_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_750_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_750_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          13),
  ("fsize_db",              11547164401),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.55GB; nevents: 200.00k; release: 9_4_7; last modified: 2018-10-15 05:14:00"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-800_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToBulkGravitonToHHTo2B2Tau_M-800_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_800_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_800_hh_2b2t"),
  ("nof_db_events",         192000),
  ("nof_db_files",          11),
  ("fsize_db",              11179122535),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.18GB; nevents: 192.00k; release: 9_4_7; last modified: 2018-10-04 16:45:48"),
])

meta_dictionary["/VBFHHTo2B2Tau_CV_1_C2V_1_C3_0_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_VBFHHTo2B2Tau_CV_1_C2V_1_C3_0_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_0_hh_bbtt"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_0_hh_2b2t"),
  ("nof_db_events",         369000),
  ("nof_db_files",          26),
  ("fsize_db",              20317409524),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 20.32GB; nevents: 369.00k; release: 9_4_7; last modified: 2018-09-13 02:51:21"),
])

meta_dictionary["/VBFHHTo2B2Tau_CV_1_C2V_1_C3_1_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_VBFHHTo2B2Tau_CV_1_C2V_1_C3_1_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_1_hh_bbtt"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_1_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          20),
  ("fsize_db",              16551491719),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 16.55GB; nevents: 300.00k; release: 9_4_6_patch1; last modified: 2018-08-12 16:18:02"),
])

meta_dictionary["/VBFHHTo2B2Tau_CV_1_C2V_1_C3_2_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_VBFHHTo2B2Tau_CV_1_C2V_1_C3_2_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_2_hh_bbtt"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_2_hh_2b2t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          9),
  ("fsize_db",              22555887148),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 22.56GB; nevents: 400.00k; release: 9_4_7; last modified: 2018-08-15 01:15:08"),
])

meta_dictionary["/VBFHHTo2B2Tau_CV_1_C2V_2_C3_1_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "signal_vbf_nonresonant_1_2_1_hh_bbtt"),
  ("process_name_specific", "signal_vbf_nonresonant_1_2_1_hh_2b2t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          24),
  ("fsize_db",              23834632407),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 23.83GB; nevents: 400.00k; release: 9_4_7; last modified: 2018-08-14 13:44:14"),
])

meta_dictionary["/VBFHHTo2B2Tau_CV_1_5_C2V_1_C3_1_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_VBFHHTo2B2Tau_CV_1_5_C2V_1_C3_1_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2"),
  ("sample_category",       "signal_vbf_nonresonant_1p5_1_1_hh_bbtt"),
  ("process_name_specific", "signal_vbf_nonresonant_1p5_1_1_hh_2b2t"),
  ("nof_db_events",         392000),
  ("nof_db_files",          16),
  ("fsize_db",              22237635973),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 22.24GB; nevents: 392.00k; release: 9_4_7; last modified: 2018-10-16 23:07:57"),
])

meta_dictionary["/GluGluToHHTo2B2Tau_node_SM_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToHHTo2B2Tau_node_SM_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_sm_hh_2b2t"),
  ("nof_db_events",         380000),
  ("nof_db_files",          18),
  ("fsize_db",              20440095707),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 20.44GB; nevents: 380.00k; release: 9_4_7; last modified: 2018-10-20 02:00:18"),
])

meta_dictionary["/GluGluToHHTo2B2Tau_node_2_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToHHTo2B2Tau_node_2_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_2_hh_2b2t"),
  ("nof_db_events",         392000),
  ("nof_db_files",          14),
  ("fsize_db",              22130629455),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 22.13GB; nevents: 392.00k; release: 9_4_7; last modified: 2018-10-05 06:46:31"),
])

meta_dictionary["/GluGluToHHTo2B2Tau_node_3_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToHHTo2B2Tau_node_3_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_3_hh_2b2t"),
  ("nof_db_events",         396000),
  ("nof_db_files",          22),
  ("fsize_db",              21371438091),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 21.37GB; nevents: 396.00k; release: 9_4_7; last modified: 2018-10-07 19:39:40"),
])

meta_dictionary["/GluGluToHHTo2B2Tau_node_4_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToHHTo2B2Tau_node_4_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_4_hh_2b2t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          21),
  ("fsize_db",              21451946375),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 21.45GB; nevents: 400.00k; release: 9_4_7; last modified: 2018-10-15 06:43:44"),
])

meta_dictionary["/GluGluToHHTo2B2Tau_node_7_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToHHTo2B2Tau_node_7_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_7_hh_2b2t"),
  ("nof_db_events",         376000),
  ("nof_db_files",          16),
  ("fsize_db",              20190349511),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 20.19GB; nevents: 376.00k; release: 9_4_7; last modified: 2018-10-06 23:57:14"),
])

meta_dictionary["/GluGluToHHTo2B2Tau_node_9_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToHHTo2B2Tau_node_9_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_9_hh_2b2t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          18),
  ("fsize_db",              22924430937),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 22.92GB; nevents: 400.00k; release: 9_4_7; last modified: 2018-10-15 05:05:16"),
])

meta_dictionary["/GluGluToHHTo2B2Tau_node_12_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun16_GluGluToHHTo2B2Tau_node_12_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_12_hh_2b2t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          10),
  ("fsize_db",              21176117597),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 21.18GB; nevents: 400.00k; release: 9_4_7; last modified: 2018-10-08 08:57:04"),
])


# event statistics by sample category:
# signal_vbf_spin0_300_hh_bbvv:           280.00k
# signal_vbf_spin0_350_hh_bbvv:           285.00k
# signal_vbf_spin0_400_hh_bbvv:           100.00k
# signal_vbf_spin0_750_hh_bbvv:           100.00k
# signal_ggf_spin0_250_hh_bbvv:           400.00k
# signal_ggf_spin0_260_hh_bbvv:           400.00k
# signal_ggf_spin0_270_hh_bbvv:           388.00k
# signal_ggf_spin0_280_hh_bbvv:           384.00k
# signal_ggf_spin0_320_hh_bbvv:           300.00k
# signal_ggf_spin0_350_hh_bbvv:           300.00k
# signal_ggf_spin0_400_hh_bbvv:           292.00k
# signal_ggf_spin0_450_hh_bbvv:           300.00k
# signal_ggf_spin0_500_hh_bbvv:           200.00k
# signal_ggf_spin0_600_hh_bbvv:           200.00k
# signal_ggf_spin0_650_hh_bbvv:           200.00k
# signal_ggf_spin0_700_hh_bbvv:           200.00k
# signal_ggf_spin0_750_hh_bbvv:           200.00k
# signal_ggf_spin0_800_hh_bbvv:           197.00k
# signal_ggf_spin0_850_hh_bbvv:           200.00k
# signal_ggf_spin0_900_hh_bbvv:           100.00k
# signal_ggf_spin0_1000_hh_bbvv:          100.00k
# signal_ggf_spin0_1250_hh_bbvv:          100.00k
# signal_ggf_spin0_1500_hh_bbvv:          100.00k
# signal_ggf_spin0_1750_hh_bbvv:          100.00k
# signal_ggf_spin0_2000_hh_bbvv:          100.00k
# signal_ggf_spin0_2500_hh_bbvv:          97.00k
# signal_ggf_spin0_3000_hh_bbvv:          98.00k
# signal_ggf_spin2_250_hh_bbvv:           400.00k
# signal_ggf_spin2_260_hh_bbvv:           400.00k
# signal_ggf_spin2_270_hh_bbvv:           400.00k
# signal_ggf_spin2_280_hh_bbvv:           400.00k
# signal_ggf_spin2_300_hh_bbvv:           400.00k
# signal_ggf_spin2_320_hh_bbvv:           294.00k
# signal_ggf_spin2_350_hh_bbvv:           282.00k
# signal_ggf_spin2_400_hh_bbvv:           298.00k
# signal_ggf_spin2_450_hh_bbvv:           300.00k
# signal_ggf_spin2_500_hh_bbvv:           200.00k
# signal_ggf_spin2_550_hh_bbvv:           200.00k
# signal_ggf_spin2_600_hh_bbvv:           192.00k
# signal_ggf_spin2_650_hh_bbvv:           200.00k
# signal_ggf_spin2_700_hh_bbvv:           200.00k
# signal_ggf_spin2_750_hh_bbvv:           198.00k
# signal_ggf_spin2_800_hh_bbvv:           200.00k
# signal_ggf_spin2_850_hh_bbvv:           200.00k
# signal_ggf_spin2_900_hh_bbvv:           100.00k
# signal_ggf_spin2_1000_hh_bbvv:          100.00k
# signal_ggf_spin2_1250_hh_bbvv:          100.00k
# signal_ggf_spin2_1500_hh_bbvv:          100.00k
# signal_ggf_spin2_1750_hh_bbvv:          100.00k
# signal_ggf_spin2_2000_hh_bbvv:          100.00k
# signal_ggf_spin2_2500_hh_bbvv:          98.00k
# signal_ggf_spin2_3000_hh_bbvv:          100.00k
# signal_vbf_nonresonant_1_1_1_hh_bbvv:   400.00k
# signal_ggf_nonresonant_hh_bbvv:         2.35M
# signal_vbf_spin0_250_hh_bbtt:           400.00k
# signal_vbf_spin0_260_hh_bbtt:           388.00k
# signal_vbf_spin0_270_hh_bbtt:           384.00k
# signal_vbf_spin0_280_hh_bbtt:           400.00k
# signal_vbf_spin0_300_hh_bbtt:           300.00k
# signal_vbf_spin0_350_hh_bbtt:           300.00k
# signal_vbf_spin0_400_hh_bbtt:           100.00k
# signal_vbf_spin0_450_hh_bbtt:           300.00k
# signal_vbf_spin0_500_hh_bbtt:           290.00k
# signal_vbf_spin0_550_hh_bbtt:           300.00k
# signal_vbf_spin0_600_hh_bbtt:           200.00k
# signal_vbf_spin0_650_hh_bbtt:           200.00k
# signal_vbf_spin0_700_hh_bbtt:           200.00k
# signal_vbf_spin0_750_hh_bbtt:           100.00k
# signal_vbf_spin0_800_hh_bbtt:           200.00k
# signal_vbf_spin0_850_hh_bbtt:           200.00k
# signal_vbf_spin0_900_hh_bbtt:           100.00k
# signal_vbf_spin0_1000_hh_bbtt:          100.00k
# signal_vbf_spin0_1250_hh_bbtt:          100.00k
# signal_vbf_spin0_1500_hh_bbtt:          100.00k
# signal_vbf_spin0_1750_hh_bbtt:          100.00k
# signal_vbf_spin0_2000_hh_bbtt:          100.00k
# signal_vbf_spin0_3000_hh_bbtt:          100.00k
# signal_vbf_spin2_250_hh_bbtt:           386.00k
# signal_vbf_spin2_260_hh_bbtt:           400.00k
# signal_vbf_spin2_270_hh_bbtt:           400.00k
# signal_vbf_spin2_280_hh_bbtt:           400.00k
# signal_vbf_spin2_300_hh_bbtt:           282.00k
# signal_vbf_spin2_320_hh_bbtt:           300.00k
# signal_vbf_spin2_350_hh_bbtt:           300.00k
# signal_vbf_spin2_400_hh_bbtt:           292.00k
# signal_vbf_spin2_450_hh_bbtt:           300.00k
# signal_vbf_spin2_500_hh_bbtt:           300.00k
# signal_vbf_spin2_600_hh_bbtt:           200.00k
# signal_vbf_spin2_650_hh_bbtt:           197.00k
# signal_vbf_spin2_700_hh_bbtt:           200.00k
# signal_vbf_spin2_750_hh_bbtt:           200.00k
# signal_vbf_spin2_850_hh_bbtt:           200.00k
# signal_vbf_spin2_900_hh_bbtt:           100.00k
# signal_vbf_spin2_1000_hh_bbtt:          100.00k
# signal_vbf_spin2_1750_hh_bbtt:          100.00k
# signal_vbf_spin2_2000_hh_bbtt:          100.00k
# signal_ggf_spin0_250_hh_bbtt:           390.00k
# signal_ggf_spin0_260_hh_bbtt:           360.00k
# signal_ggf_spin0_270_hh_bbtt:           392.00k
# signal_ggf_spin0_280_hh_bbtt:           398.00k
# signal_ggf_spin0_300_hh_bbtt:           300.00k
# signal_ggf_spin0_320_hh_bbtt:           300.00k
# signal_ggf_spin0_350_hh_bbtt:           300.00k
# signal_ggf_spin0_400_hh_bbtt:           296.00k
# signal_ggf_spin0_450_hh_bbtt:           272.00k
# signal_ggf_spin0_500_hh_bbtt:           190.00k
# signal_ggf_spin0_550_hh_bbtt:           200.00k
# signal_ggf_spin0_600_hh_bbtt:           200.00k
# signal_ggf_spin0_650_hh_bbtt:           188.00k
# signal_ggf_spin0_700_hh_bbtt:           200.00k
# signal_ggf_spin0_750_hh_bbtt:           196.00k
# signal_ggf_spin0_800_hh_bbtt:           200.00k
# signal_ggf_spin0_850_hh_bbtt:           192.00k
# signal_ggf_spin0_900_hh_bbtt:           95.00k
# signal_ggf_spin0_1000_hh_bbtt:          100.00k
# signal_ggf_spin0_1250_hh_bbtt:          100.00k
# signal_ggf_spin0_1500_hh_bbtt:          100.00k
# signal_ggf_spin0_1750_hh_bbtt:          100.00k
# signal_ggf_spin0_2000_hh_bbtt:          92.00k
# signal_ggf_spin0_2500_hh_bbtt:          100.00k
# signal_ggf_spin0_3000_hh_bbtt:          100.00k
# signal_ggf_spin2_250_hh_bbtt:           400.00k
# signal_ggf_spin2_260_hh_bbtt:           384.00k
# signal_ggf_spin2_270_hh_bbtt:           390.00k
# signal_ggf_spin2_280_hh_bbtt:           379.00k
# signal_ggf_spin2_300_hh_bbtt:           981.55k
# signal_ggf_spin2_350_hh_bbtt:           300.00k
# signal_ggf_spin2_400_hh_bbtt:           300.00k
# signal_ggf_spin2_450_hh_bbtt:           300.00k
# signal_ggf_spin2_500_hh_bbtt:           200.00k
# signal_ggf_spin2_550_hh_bbtt:           192.00k
# signal_ggf_spin2_600_hh_bbtt:           200.00k
# signal_ggf_spin2_650_hh_bbtt:           188.00k
# signal_ggf_spin2_750_hh_bbtt:           200.00k
# signal_ggf_spin2_800_hh_bbtt:           192.00k
# signal_vbf_nonresonant_1_1_0_hh_bbtt:   369.00k
# signal_vbf_nonresonant_1_1_1_hh_bbtt:   300.00k
# signal_vbf_nonresonant_1_1_2_hh_bbtt:   400.00k
# signal_vbf_nonresonant_1_2_1_hh_bbtt:   400.00k
# signal_vbf_nonresonant_1p5_1_1_hh_bbtt: 392.00k
# signal_ggf_nonresonant_hh_bbtt:         2.74M

