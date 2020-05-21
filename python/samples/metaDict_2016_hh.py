from collections import OrderedDict as OD

# file generated at 2020-05-21 15:07:30 with the following command:
# find_samples.py -V -i ../../tthAnalysis/NanoAOD/test/datasets/txt/datasets_hh_bbww_mc_2016_RunIISummer16MiniAODv3.txt -m python/samples/metaDict_2016_hh.py -s ../../tthAnalysis/NanoAOD/test/datasets/txt/sum_datasets_hh_bbww_2016_RunIISummer16MiniAODv3.txt -c python/samples/sampleLocations_2016_nanoAOD_hh_bbww.txt

meta_dictionary = OD()


### event sums

sum_events = { 
  ("signal_ggf_nonresonant_node_sm_hh_2b2v", "signal_ggf_nonresonant_node_box_hh_2b2v", "signal_ggf_nonresonant_node_1_hh_2b2v", "signal_ggf_nonresonant_node_2_hh_2b2v", "signal_ggf_nonresonant_node_3_hh_2b2v", "signal_ggf_nonresonant_node_4_hh_2b2v", "signal_ggf_nonresonant_node_5_hh_2b2v", "signal_ggf_nonresonant_node_6_hh_2b2v", "signal_ggf_nonresonant_node_7_hh_2b2v", "signal_ggf_nonresonant_node_8_hh_2b2v", "signal_ggf_nonresonant_node_9_hh_2b2v", "signal_ggf_nonresonant_node_10_hh_2b2v", "signal_ggf_nonresonant_node_11_hh_2b2v", "signal_ggf_nonresonant_node_12_hh_2b2v"),
  ("signal_ggf_nonresonant_node_sm_hh_2b2v_sl", "signal_ggf_nonresonant_node_box_hh_2b2v_sl", "signal_ggf_nonresonant_node_1_hh_2b2v_sl", "signal_ggf_nonresonant_node_2_hh_2b2v_sl", "signal_ggf_nonresonant_node_3_hh_2b2v_sl", "signal_ggf_nonresonant_node_4_hh_2b2v_sl", "signal_ggf_nonresonant_node_5_hh_2b2v_sl", "signal_ggf_nonresonant_node_6_hh_2b2v_sl", "signal_ggf_nonresonant_node_7_hh_2b2v_sl", "signal_ggf_nonresonant_node_8_hh_2b2v_sl", "signal_ggf_nonresonant_node_9_hh_2b2v_sl", "signal_ggf_nonresonant_node_10_hh_2b2v_sl", "signal_ggf_nonresonant_node_11_hh_2b2v_sl", "signal_ggf_nonresonant_node_12_hh_2b2v_sl"),
  ("signal_ggf_nonresonant_node_sm_hh_2b2t", "signal_ggf_nonresonant_node_box_hh_2b2t", "signal_ggf_nonresonant_node_2_hh_2b2t", "signal_ggf_nonresonant_node_9_hh_2b2t", "signal_ggf_nonresonant_node_10_hh_2b2t", "signal_ggf_nonresonant_node_11_hh_2b2t", "signal_ggf_nonresonant_node_12_hh_2b2t", "signal_ggf_nonresonant_node_13_hh_2b2t"),
}


meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-260_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToRadionToHHTo2B2VTo2L2Nu_M-260_narrow_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_260_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_260_hh_2b2v"),
  ("nof_db_events",         299998),
  ("nof_db_files",          4),
  ("fsize_db",              11821300223),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.82GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-02 02:43:18"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-270_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToRadionToHHTo2B2VTo2L2Nu_M-270_narrow_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_270_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_270_hh_2b2v"),
  ("nof_db_events",         294629),
  ("nof_db_files",          3),
  ("fsize_db",              11694604529),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.69GB; nevents: 294.63k; release: 9_4_9; last modified: 2019-03-02 18:57:03"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-300_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToRadionToHHTo2B2VTo2L2Nu_M-300_narrow_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_300_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_300_hh_2b2v"),
  ("nof_db_events",         300000),
  ("nof_db_files",          4),
  ("fsize_db",              12121761327),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.12GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-02-28 09:18:27"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-350_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToRadionToHHTo2B2VTo2L2Nu_M-350_narrow_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_350_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_350_hh_2b2v"),
  ("nof_db_events",         295149),
  ("nof_db_files",          5),
  ("fsize_db",              12270587874),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.27GB; nevents: 295.15k; release: 9_4_9; last modified: 2019-03-08 17:41:33"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-400_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToRadionToHHTo2B2VTo2L2Nu_M-400_narrow_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_400_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_400_hh_2b2v"),
  ("nof_db_events",         299997),
  ("nof_db_files",          4),
  ("fsize_db",              12763369067),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.76GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-09 00:51:17"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-450_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToRadionToHHTo2B2VTo2L2Nu_M-450_narrow_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_450_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_450_hh_2b2v"),
  ("nof_db_events",         296256),
  ("nof_db_files",          4),
  ("fsize_db",              12817875328),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.82GB; nevents: 296.26k; release: 9_4_9; last modified: 2019-03-08 17:40:30"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-500_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToRadionToHHTo2B2VTo2L2Nu_M-500_narrow_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_500_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_500_hh_2b2v"),
  ("nof_db_events",         300000),
  ("nof_db_files",          5),
  ("fsize_db",              13281765633),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.28GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-01 15:31:45"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-550_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToRadionToHHTo2B2VTo2L2Nu_M-550_narrow_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_550_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_550_hh_2b2v"),
  ("nof_db_events",         299999),
  ("nof_db_files",          5),
  ("fsize_db",              13529956556),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.53GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-02 09:18:04"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-600_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToRadionToHHTo2B2VTo2L2Nu_M-600_narrow_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_600_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_600_hh_2b2v"),
  ("nof_db_events",         299999),
  ("nof_db_files",          4),
  ("fsize_db",              13674104858),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.67GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-03 00:03:16"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-650_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToRadionToHHTo2B2VTo2L2Nu_M-650_narrow_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_650_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_650_hh_2b2v"),
  ("nof_db_events",         299538),
  ("nof_db_files",          5),
  ("fsize_db",              13997216210),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.00GB; nevents: 299.54k; release: 9_4_9; last modified: 2019-03-03 12:00:50"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-750_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToRadionToHHTo2B2VTo2L2Nu_M-750_narrow_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_750_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_750_hh_2b2v"),
  ("nof_db_events",         298727),
  ("nof_db_files",          3),
  ("fsize_db",              13966996917),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.97GB; nevents: 298.73k; release: 9_4_9; last modified: 2019-03-03 06:58:24"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-800_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToRadionToHHTo2B2VTo2L2Nu_M-800_narrow_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_800_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_800_hh_2b2v"),
  ("nof_db_events",         299705),
  ("nof_db_files",          3),
  ("fsize_db",              14140095303),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.14GB; nevents: 299.70k; release: 9_4_9; last modified: 2019-03-12 21:42:38"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-900_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToRadionToHHTo2B2VTo2L2Nu_M-900_narrow_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_900_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_900_hh_2b2v"),
  ("nof_db_events",         298733),
  ("nof_db_files",          3),
  ("fsize_db",              14389658695),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.39GB; nevents: 298.73k; release: 9_4_9; last modified: 2019-02-28 21:01:17"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-1000_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToRadionToHHTo2B2VTo2L2Nu_M-1000_narrow_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_1000_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_1000_hh_2b2v"),
  ("nof_db_events",         299999),
  ("nof_db_files",          4),
  ("fsize_db",              14685031472),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.69GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-03 05:04:25"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-260_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-260_narrow_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_260_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_260_hh_2b2v"),
  ("nof_db_events",         300000),
  ("nof_db_files",          3),
  ("fsize_db",              12205401208),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.21GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-06 04:53:36"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-270_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-270_narrow_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_270_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_270_hh_2b2v"),
  ("nof_db_events",         300000),
  ("nof_db_files",          3),
  ("fsize_db",              12216222977),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.22GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-03 03:38:55"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-300_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-300_narrow_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_300_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_300_hh_2b2v"),
  ("nof_db_events",         299999),
  ("nof_db_files",          3),
  ("fsize_db",              12432044182),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.43GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-03 15:07:06"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-350_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-350_narrow_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_350_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_350_hh_2b2v"),
  ("nof_db_events",         300000),
  ("nof_db_files",          4),
  ("fsize_db",              12931701996),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.93GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-03 12:01:11"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-400_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-400_narrow_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_400_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_400_hh_2b2v"),
  ("nof_db_events",         300000),
  ("nof_db_files",          3),
  ("fsize_db",              13138610285),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.14GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-06 04:55:06"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-450_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-450_narrow_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_450_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_450_hh_2b2v"),
  ("nof_db_events",         299999),
  ("nof_db_files",          4),
  ("fsize_db",              13501491108),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.50GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-03 11:59:28"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-500_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-500_narrow_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_500_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_500_hh_2b2v"),
  ("nof_db_events",         299999),
  ("nof_db_files",          3),
  ("fsize_db",              13733577571),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.73GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-04 08:51:30"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-550_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-550_narrow_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_550_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_550_hh_2b2v"),
  ("nof_db_events",         299999),
  ("nof_db_files",          3),
  ("fsize_db",              13919729330),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.92GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-02 13:13:34"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-600_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-600_narrow_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_600_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_600_hh_2b2v"),
  ("nof_db_events",         299999),
  ("nof_db_files",          3),
  ("fsize_db",              14074430864),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.07GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-04 19:08:14"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-650_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-650_narrow_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_650_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_650_hh_2b2v"),
  ("nof_db_events",         298806),
  ("nof_db_files",          6),
  ("fsize_db",              14346261466),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.35GB; nevents: 298.81k; release: 9_4_9; last modified: 2019-03-05 02:36:04"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-700_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-700_narrow_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_700_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_700_hh_2b2v"),
  ("nof_db_events",         299999),
  ("nof_db_files",          3),
  ("fsize_db",              14636315935),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.64GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-04 08:52:55"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-800_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-800_narrow_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_800_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_800_hh_2b2v"),
  ("nof_db_events",         299999),
  ("nof_db_files",          4),
  ("fsize_db",              14673528101),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.67GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-08 02:00:13"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-900_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-900_narrow_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_900_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_900_hh_2b2v"),
  ("nof_db_events",         299999),
  ("nof_db_files",          3),
  ("fsize_db",              15011560063),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 15.01GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-07 04:33:04"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1000_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1000_narrow_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_1000_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_1000_hh_2b2v"),
  ("nof_db_events",         299118),
  ("nof_db_files",          3),
  ("fsize_db",              15065557472),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 15.07GB; nevents: 299.12k; release: 9_4_9; last modified: 2019-03-03 19:51:10"),
])

meta_dictionary["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_1_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_1_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_1_hh_bbvv"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_1_hh_2b2v"),
  ("nof_db_events",         300000),
  ("nof_db_files",          3),
  ("fsize_db",              12626803802),
  ("xsection",              4.55695e-05),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.63GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-03 08:44:06"),
])

meta_dictionary["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_2_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_2_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_2_hh_bbvv"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_2_hh_2b2v"),
  ("nof_db_events",         300000),
  ("nof_db_files",          6),
  ("fsize_db",              13505935893),
  ("xsection",              3.75655e-05),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.51GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-11 11:48:25"),
])

meta_dictionary["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_2_C3_1_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_VBFHHTo2B2VTo2L2Nu_CV_1_C2V_2_C3_1_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_vbf_nonresonant_1_2_1_hh_bbvv"),
  ("process_name_specific", "signal_vbf_nonresonant_1_2_1_hh_2b2v"),
  ("nof_db_events",         300000),
  ("nof_db_files",          6),
  ("fsize_db",              14484771487),
  ("xsection",              0.0003753816),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.48GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-09 09:58:43"),
])

meta_dictionary["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_0_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_0_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_0_hh_bbvv"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_0_hh_2b2v"),
  ("nof_db_events",         299999),
  ("nof_db_files",          4),
  ("fsize_db",              13033305340),
  ("xsection",              0.0001216848),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.03GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-03 06:57:00"),
])

meta_dictionary["/VBFHHTo2B2VTo2L2Nu_CV_1_5_C2V_1_C3_1_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_VBFHHTo2B2VTo2L2Nu_CV_1_5_C2V_1_C3_1_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_vbf_nonresonant_1p5_1_1_hh_bbvv"),
  ("process_name_specific", "signal_vbf_nonresonant_1p5_1_1_hh_2b2v"),
  ("nof_db_events",         299402),
  ("nof_db_files",          5),
  ("fsize_db",              13628421160),
  ("xsection",              0.0017430382),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.63GB; nevents: 299.40k; release: 9_4_9; last modified: 2019-03-11 15:03:07"),
])

meta_dictionary["/VBFHHTo2B2VTo2L2Nu_CV_0_5_C2V_1_C3_1_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_VBFHHTo2B2VTo2L2Nu_CV_0_5_C2V_1_C3_1_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_vbf_nonresonant_0p5_1_1_hh_bbvv"),
  ("process_name_specific", "signal_vbf_nonresonant_0p5_1_1_hh_2b2v"),
  ("nof_db_events",         297179),
  ("nof_db_files",          5),
  ("fsize_db",              14044768795),
  ("xsection",              0.0002857708),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.04GB; nevents: 297.18k; release: 9_4_9; last modified: 2019-03-02 19:00:23"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_SM_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToHHTo2B2VTo2L2Nu_node_SM_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_node_sm_hh_2b2v"),
  ("nof_db_events",         299999),
  ("nof_db_files",          5),
  ("fsize_db",              13376661186),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.38GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-06 06:38:51"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_box_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToHHTo2B2VTo2L2Nu_node_box_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_node_box_hh_2b2v"),
  ("nof_db_events",         299999),
  ("nof_db_files",          3),
  ("fsize_db",              13225066454),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.23GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-05 05:40:35"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_1_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToHHTo2B2VTo2L2Nu_node_1_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_node_1_hh_2b2v"),
  ("nof_db_events",         299999),
  ("nof_db_files",          4),
  ("fsize_db",              13519407617),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.52GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-03 13:37:58"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_2_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v3/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToHHTo2B2VTo2L2Nu_node_2_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v3"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_node_2_hh_2b2v"),
  ("nof_db_events",         300000),
  ("nof_db_files",          4),
  ("fsize_db",              14649063726),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.65GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-07-23 18:39:16"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_3_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToHHTo2B2VTo2L2Nu_node_3_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_node_3_hh_2b2v"),
  ("nof_db_events",         299998),
  ("nof_db_files",          3),
  ("fsize_db",              13601999029),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.60GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-12 21:44:58"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_4_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToHHTo2B2VTo2L2Nu_node_4_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_node_4_hh_2b2v"),
  ("nof_db_events",         299999),
  ("nof_db_files",          3),
  ("fsize_db",              13322107044),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.32GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-10 11:45:26"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_5_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToHHTo2B2VTo2L2Nu_node_5_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_node_5_hh_2b2v"),
  ("nof_db_events",         299999),
  ("nof_db_files",          4),
  ("fsize_db",              14057961060),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.06GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-03 19:48:50"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_6_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToHHTo2B2VTo2L2Nu_node_6_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_node_6_hh_2b2v"),
  ("nof_db_events",         299999),
  ("nof_db_files",          4),
  ("fsize_db",              13143785774),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.14GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-03 03:36:40"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_7_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToHHTo2B2VTo2L2Nu_node_7_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_node_7_hh_2b2v"),
  ("nof_db_events",         299997),
  ("nof_db_files",          4),
  ("fsize_db",              12803480606),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.80GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-02 18:57:43"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_8_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToHHTo2B2VTo2L2Nu_node_8_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_node_8_hh_2b2v"),
  ("nof_db_events",         299999),
  ("nof_db_files",          3),
  ("fsize_db",              13552950610),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.55GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-02 13:13:05"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_9_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToHHTo2B2VTo2L2Nu_node_9_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_node_9_hh_2b2v"),
  ("nof_db_events",         299998),
  ("nof_db_files",          3),
  ("fsize_db",              13997106004),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.00GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-11 16:47:40"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_10_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToHHTo2B2VTo2L2Nu_node_10_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_node_10_hh_2b2v"),
  ("nof_db_events",         299998),
  ("nof_db_files",          4),
  ("fsize_db",              12822566212),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.82GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-11 16:49:01"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_11_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToHHTo2B2VTo2L2Nu_node_11_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_node_11_hh_2b2v"),
  ("nof_db_events",         299364),
  ("nof_db_files",          5),
  ("fsize_db",              13315340669),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.32GB; nevents: 299.36k; release: 9_4_9; last modified: 2019-03-07 07:39:02"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_12_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct07_GluGluToHHTo2B2VTo2L2Nu_node_12_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_node_12_hh_2b2v"),
  ("nof_db_events",         299997),
  ("nof_db_files",          4),
  ("fsize_db",              13025018010),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.03GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-08 04:50:00"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_node_SM_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToRadionToHHTo2B2WToLNu2J_node_SM_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_node_sm_hh_2b2v_sl"),
  ("nof_db_events",         299996),
  ("nof_db_files",          4),
  ("fsize_db",              13758086324),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.76GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-04 04:51:57"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_node_box_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToRadionToHHTo2B2WToLNu2J_node_box_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_node_box_hh_2b2v_sl"),
  ("nof_db_events",         299998),
  ("nof_db_files",          5),
  ("fsize_db",              13554966138),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.55GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-19 18:29:37"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_node-1_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToRadionToHHTo2B2WToLNu2J_node-1_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_node_1_hh_2b2v_sl"),
  ("nof_db_events",         299994),
  ("nof_db_files",          6),
  ("fsize_db",              14226816913),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.23GB; nevents: 299.99k; release: 9_4_9; last modified: 2019-03-06 20:40:18"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_node-2_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToRadionToHHTo2B2WToLNu2J_node-2_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_node_2_hh_2b2v_sl"),
  ("nof_db_events",         299996),
  ("nof_db_files",          5),
  ("fsize_db",              15065193278),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 15.07GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-02 18:56:32"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_node-3_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToRadionToHHTo2B2WToLNu2J_node-3_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_node_3_hh_2b2v_sl"),
  ("nof_db_events",         299201),
  ("nof_db_files",          4),
  ("fsize_db",              14042794496),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.04GB; nevents: 299.20k; release: 9_4_9; last modified: 2019-03-03 05:05:41"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_node-4_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToRadionToHHTo2B2WToLNu2J_node-4_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_node_4_hh_2b2v_sl"),
  ("nof_db_events",         299998),
  ("nof_db_files",          5),
  ("fsize_db",              13734345217),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.73GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-05 14:42:35"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_node-5_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToRadionToHHTo2B2WToLNu2J_node-5_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_node_5_hh_2b2v_sl"),
  ("nof_db_events",         299996),
  ("nof_db_files",          6),
  ("fsize_db",              14660310040),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.66GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-05 22:47:07"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_node-6_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToRadionToHHTo2B2WToLNu2J_node-6_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_node_6_hh_2b2v_sl"),
  ("nof_db_events",         299999),
  ("nof_db_files",          3),
  ("fsize_db",              13255677867),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.26GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-04 03:48:21"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_node-7_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToRadionToHHTo2B2WToLNu2J_node-7_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_node_7_hh_2b2v_sl"),
  ("nof_db_events",         299998),
  ("nof_db_files",          4),
  ("fsize_db",              12941536315),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.94GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-04 12:01:34"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_node-8_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToRadionToHHTo2B2WToLNu2J_node-8_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_node_8_hh_2b2v_sl"),
  ("nof_db_events",         299996),
  ("nof_db_files",          5),
  ("fsize_db",              14190505186),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.19GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-07 16:43:30"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_node-9_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToRadionToHHTo2B2WToLNu2J_node-9_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_node_9_hh_2b2v_sl"),
  ("nof_db_events",         299591),
  ("nof_db_files",          5),
  ("fsize_db",              14339474676),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.34GB; nevents: 299.59k; release: 9_4_9; last modified: 2019-03-03 06:54:13"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_node-10_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToRadionToHHTo2B2WToLNu2J_node-10_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_node_10_hh_2b2v_sl"),
  ("nof_db_events",         299997),
  ("nof_db_files",          5),
  ("fsize_db",              13151222527),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.15GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-06 12:41:08"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_node-11_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToRadionToHHTo2B2WToLNu2J_node-11_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_node_11_hh_2b2v_sl"),
  ("nof_db_events",         299994),
  ("nof_db_files",          6),
  ("fsize_db",              13676249855),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.68GB; nevents: 299.99k; release: 9_4_9; last modified: 2019-03-06 02:00:49"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_node-12_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToRadionToHHTo2B2WToLNu2J_node-12_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_node_12_hh_2b2v_sl"),
  ("nof_db_events",         299994),
  ("nof_db_files",          4),
  ("fsize_db",              13168943933),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.17GB; nevents: 299.99k; release: 9_4_9; last modified: 2019-03-13 16:54:18"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_M-250_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToRadionToHHTo2B2WToLNu2J_M-250_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_250_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_250_hh_2b2v_sl"),
  ("nof_db_events",         299997),
  ("nof_db_files",          5),
  ("fsize_db",              12143344410),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.14GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-02 19:00:58"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_M-260_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToRadionToHHTo2B2WToLNu2J_M-260_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_260_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_260_hh_2b2v_sl"),
  ("nof_db_events",         299402),
  ("nof_db_files",          5),
  ("fsize_db",              12033567447),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.03GB; nevents: 299.40k; release: 9_4_9; last modified: 2019-03-07 16:43:40"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_M-270_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToRadionToHHTo2B2WToLNu2J_M-270_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_270_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_270_hh_2b2v_sl"),
  ("nof_db_events",         299995),
  ("nof_db_files",          5),
  ("fsize_db",              12073887370),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.07GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-06 14:01:22"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_M-300_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToRadionToHHTo2B2WToLNu2J_M-300_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_300_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_300_hh_2b2v_sl"),
  ("nof_db_events",         299996),
  ("nof_db_files",          4),
  ("fsize_db",              12250780111),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.25GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-08 01:59:58"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_M-350_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToRadionToHHTo2B2WToLNu2J_M-350_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_350_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_350_hh_2b2v_sl"),
  ("nof_db_events",         299998),
  ("nof_db_files",          5),
  ("fsize_db",              12822147007),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.82GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-03 03:40:44"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_M-400_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToRadionToHHTo2B2WToLNu2J_M-400_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_400_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_400_hh_2b2v_sl"),
  ("nof_db_events",         300000),
  ("nof_db_files",          5),
  ("fsize_db",              13147855533),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.15GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-03 21:31:27"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_M-450_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToRadionToHHTo2B2WToLNu2J_M-450_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_450_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_450_hh_2b2v_sl"),
  ("nof_db_events",         292028),
  ("nof_db_files",          4),
  ("fsize_db",              13118198421),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.12GB; nevents: 292.03k; release: 9_4_9; last modified: 2019-03-03 05:01:11"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_M-500_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToRadionToHHTo2B2WToLNu2J_M-500_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_500_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_500_hh_2b2v_sl"),
  ("nof_db_events",         299997),
  ("nof_db_files",          5),
  ("fsize_db",              13799384403),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.80GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-03 08:45:47"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_M-550_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToRadionToHHTo2B2WToLNu2J_M-550_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_550_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_550_hh_2b2v_sl"),
  ("nof_db_events",         299996),
  ("nof_db_files",          4),
  ("fsize_db",              13970691602),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.97GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-06 14:00:20"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_M-600_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToRadionToHHTo2B2WToLNu2J_M-600_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_600_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_600_hh_2b2v_sl"),
  ("nof_db_events",         299999),
  ("nof_db_files",          5),
  ("fsize_db",              14217239886),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.22GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-03 13:37:02"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_M-700_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToRadionToHHTo2B2WToLNu2J_M-700_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_700_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_700_hh_2b2v_sl"),
  ("nof_db_events",         299998),
  ("nof_db_files",          4),
  ("fsize_db",              14467187735),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.47GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-03 06:51:01"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_M-800_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToRadionToHHTo2B2WToLNu2J_M-800_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_800_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_800_hh_2b2v_sl"),
  ("nof_db_events",         299999),
  ("nof_db_files",          5),
  ("fsize_db",              14975865562),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.98GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-03 01:43:48"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_M-900_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToRadionToHHTo2B2WToLNu2J_M-900_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_900_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_900_hh_2b2v_sl"),
  ("nof_db_events",         300000),
  ("nof_db_files",          4),
  ("fsize_db",              15010963358),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 15.01GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-14 14:01:29"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_M-1000_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToRadionToHHTo2B2WToLNu2J_M-1000_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_1000_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_1000_hh_2b2v_sl"),
  ("nof_db_events",         299469),
  ("nof_db_files",          5),
  ("fsize_db",              15303436616),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 15.30GB; nevents: 299.47k; release: 9_4_9; last modified: 2019-03-03 11:59:24"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-250_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-250_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_250_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_250_hh_2b2v_sl"),
  ("nof_db_events",         299998),
  ("nof_db_files",          5),
  ("fsize_db",              12270543882),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.27GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-03 16:41:42"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-260_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-260_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_260_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_260_hh_2b2v_sl"),
  ("nof_db_events",         300000),
  ("nof_db_files",          4),
  ("fsize_db",              12407686965),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.41GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-08 00:29:06"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-270_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-270_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_270_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_270_hh_2b2v_sl"),
  ("nof_db_events",         299231),
  ("nof_db_files",          5),
  ("fsize_db",              12387077839),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.39GB; nevents: 299.23k; release: 9_4_9; last modified: 2019-03-03 12:02:11"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-300_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-300_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_300_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_300_hh_2b2v_sl"),
  ("nof_db_events",         299998),
  ("nof_db_files",          4),
  ("fsize_db",              12692339481),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.69GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-07 21:41:37"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-350_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-350_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1"),
  ("sample_category",       "signal_ggf_spin2_350_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_350_hh_2b2v_sl"),
  ("nof_db_events",         299402),
  ("nof_db_files",          4),
  ("fsize_db",              13215909741),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.22GB; nevents: 299.40k; release: 9_4_9; last modified: 2018-10-12 05:20:11"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-400_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-400_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_400_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_400_hh_2b2v_sl"),
  ("nof_db_events",         299993),
  ("nof_db_files",          4),
  ("fsize_db",              13636388128),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.64GB; nevents: 299.99k; release: 9_4_9; last modified: 2019-03-03 05:05:26"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-450_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-450_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_450_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_450_hh_2b2v_sl"),
  ("nof_db_events",         299998),
  ("nof_db_files",          5),
  ("fsize_db",              13995682190),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.00GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-02 23:57:30"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-500_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-500_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_500_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_500_hh_2b2v_sl"),
  ("nof_db_events",         299999),
  ("nof_db_files",          4),
  ("fsize_db",              14208882340),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.21GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-05 22:44:51"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-550_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-550_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_550_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_550_hh_2b2v_sl"),
  ("nof_db_events",         299995),
  ("nof_db_files",          4),
  ("fsize_db",              14478664969),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.48GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-04 19:04:19"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-600_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-600_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_600_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_600_hh_2b2v_sl"),
  ("nof_db_events",         299995),
  ("nof_db_files",          4),
  ("fsize_db",              14654413374),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.65GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-06 12:39:54"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-650_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-650_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_650_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_650_hh_2b2v_sl"),
  ("nof_db_events",         299997),
  ("nof_db_files",          5),
  ("fsize_db",              14989654961),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.99GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-06 00:39:35"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-700_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-700_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_700_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_700_hh_2b2v_sl"),
  ("nof_db_events",         299995),
  ("nof_db_files",          5),
  ("fsize_db",              15100949761),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 15.10GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-02 02:50:05"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-800_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-800_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_800_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_800_hh_2b2v_sl"),
  ("nof_db_events",         299998),
  ("nof_db_files",          6),
  ("fsize_db",              15643527631),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 15.64GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-07 16:42:44"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-900_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-900_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_900_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_900_hh_2b2v_sl"),
  ("nof_db_events",         299999),
  ("nof_db_files",          6),
  ("fsize_db",              15836490873),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 15.84GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-05 07:04:38"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-1000_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec11_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-1000_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_1000_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_1000_hh_2b2v_sl"),
  ("nof_db_events",         299997),
  ("nof_db_files",          5),
  ("fsize_db",              15848133420),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 15.85GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-14 22:49:19"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-250_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-250_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_250_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_250_hh_2b2t"),
  ("nof_db_events",         50000),
  ("nof_db_files",          1),
  ("fsize_db",              1962681716),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 1.96GB; nevents: 50.00k; release: 9_4_9; last modified: 2019-05-11 05:06:43"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-260_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-260_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_260_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_260_hh_2b2t"),
  ("nof_db_events",         50000),
  ("nof_db_files",          1),
  ("fsize_db",              1978376178),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 1.98GB; nevents: 50.00k; release: 9_4_9; last modified: 2019-04-29 16:50:10"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-270_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-270_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_270_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_270_hh_2b2t"),
  ("nof_db_events",         50000),
  ("nof_db_files",          1),
  ("fsize_db",              1992599467),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 1.99GB; nevents: 50.00k; release: 9_4_9; last modified: 2019-05-11 00:12:26"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-280_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-280_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_280_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_280_hh_2b2t"),
  ("nof_db_events",         49600),
  ("nof_db_files",          1),
  ("fsize_db",              1985262651),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 1.99GB; nevents: 49.60k; release: 9_4_9; last modified: 2019-05-11 00:12:40"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-300_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-300_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1"),
  ("sample_category",       "signal_ggf_spin0_300_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_300_hh_2b2t"),
  ("nof_db_events",         450000),
  ("nof_db_files",          7),
  ("fsize_db",              18335508201),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 18.34GB; nevents: 450.00k; release: 9_4_9; last modified: 2019-01-28 05:00:42"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-320_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-320_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_320_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_320_hh_2b2t"),
  ("nof_db_events",         50000),
  ("nof_db_files",          2),
  ("fsize_db",              2102297139),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 2.10GB; nevents: 50.00k; release: 9_4_9; last modified: 2019-05-02 10:54:45"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-340_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-340_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_340_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_340_hh_2b2t"),
  ("nof_db_events",         48000),
  ("nof_db_files",          1),
  ("fsize_db",              1955847184),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 1.96GB; nevents: 48.00k; release: 9_4_9; last modified: 2019-05-11 00:06:45"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-350_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-350_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_350_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_350_hh_2b2t"),
  ("nof_db_events",         50000),
  ("nof_db_files",          1),
  ("fsize_db",              2167356346),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 2.17GB; nevents: 50.00k; release: 9_4_9; last modified: 2019-05-04 03:00:42"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-400_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-400_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1"),
  ("sample_category",       "signal_ggf_spin0_400_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_400_hh_2b2t"),
  ("nof_db_events",         250000),
  ("nof_db_files",          3),
  ("fsize_db",              10749996877),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 10.75GB; nevents: 250.00k; release: 9_4_9; last modified: 2019-01-26 12:53:29"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-450_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-450_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_450_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_450_hh_2b2t"),
  ("nof_db_events",         99600),
  ("nof_db_files",          2),
  ("fsize_db",              4411305292),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 4.41GB; nevents: 99.60k; release: 9_4_9; last modified: 2019-04-30 00:46:43"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-500_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-500_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_500_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_500_hh_2b2t"),
  ("nof_db_events",         99200),
  ("nof_db_files",          2),
  ("fsize_db",              4435751146),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 4.44GB; nevents: 99.20k; release: 9_4_9; last modified: 2019-04-29 11:59:17"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-550_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-550_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_550_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_550_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          2),
  ("fsize_db",              4499327267),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 4.50GB; nevents: 100.00k; release: 9_4_9; last modified: 2019-04-30 00:51:58"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-600_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-600_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_600_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_600_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          2),
  ("fsize_db",              4581235338),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 4.58GB; nevents: 100.00k; release: 9_4_9; last modified: 2019-05-11 00:09:40"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-650_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-650_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_650_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_650_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          2),
  ("fsize_db",              4742625025),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 4.74GB; nevents: 100.00k; release: 9_4_9; last modified: 2019-08-08 18:19:25"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-800_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-800_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_800_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_800_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          2),
  ("fsize_db",              4845795202),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 4.85GB; nevents: 100.00k; release: 9_4_9; last modified: 2019-05-04 01:20:30"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-900_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-900_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_900_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_900_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          2),
  ("fsize_db",              4858199935),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 4.86GB; nevents: 100.00k; release: 9_4_9; last modified: 2019-05-04 02:59:01"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-250_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToBulkGravitonToHHTo2B2Tau_M-250_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_250_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_250_hh_2b2t"),
  ("nof_db_events",         50000),
  ("nof_db_files",          1),
  ("fsize_db",              1970267888),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 1.97GB; nevents: 50.00k; release: 9_4_9; last modified: 2019-02-22 03:36:40"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-260_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToBulkGravitonToHHTo2B2Tau_M-260_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_260_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_260_hh_2b2t"),
  ("nof_db_events",         50000),
  ("nof_db_files",          1),
  ("fsize_db",              2021288641),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 2.02GB; nevents: 50.00k; release: 9_4_9; last modified: 2019-02-21 20:49:44"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-270_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToBulkGravitonToHHTo2B2Tau_M-270_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_270_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_270_hh_2b2t"),
  ("nof_db_events",         50000),
  ("nof_db_files",          1),
  ("fsize_db",              2049006927),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 2.05GB; nevents: 50.00k; release: 9_4_9; last modified: 2019-02-21 18:46:15"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-280_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToBulkGravitonToHHTo2B2Tau_M-280_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_280_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_280_hh_2b2t"),
  ("nof_db_events",         50000),
  ("nof_db_files",          1),
  ("fsize_db",              2024724980),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 2.02GB; nevents: 50.00k; release: 9_4_9; last modified: 2019-02-20 09:50:39"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-300_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToBulkGravitonToHHTo2B2Tau_M-300_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1"),
  ("sample_category",       "signal_ggf_spin2_300_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_300_hh_2b2t"),
  ("nof_db_events",         447400),
  ("nof_db_files",          5),
  ("fsize_db",              18368864093),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 18.37GB; nevents: 447.40k; release: 9_4_9; last modified: 2019-02-01 17:46:12"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-320_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToBulkGravitonToHHTo2B2Tau_M-320_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_320_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_320_hh_2b2t"),
  ("nof_db_events",         50000),
  ("nof_db_files",          1),
  ("fsize_db",              2056109122),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 2.06GB; nevents: 50.00k; release: 9_4_9; last modified: 2019-02-21 18:45:45"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-340_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToBulkGravitonToHHTo2B2Tau_M-340_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_340_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_340_hh_2b2t"),
  ("nof_db_events",         50000),
  ("nof_db_files",          1),
  ("fsize_db",              2082210498),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 2.08GB; nevents: 50.00k; release: 9_4_9; last modified: 2019-02-20 05:44:38"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-350_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToBulkGravitonToHHTo2B2Tau_M-350_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_350_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_350_hh_2b2t"),
  ("nof_db_events",         50000),
  ("nof_db_files",          1),
  ("fsize_db",              2097870831),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 2.10GB; nevents: 50.00k; release: 9_4_9; last modified: 2019-02-21 18:49:55"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-400_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToBulkGravitonToHHTo2B2Tau_M-400_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1"),
  ("sample_category",       "signal_ggf_spin2_400_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_400_hh_2b2t"),
  ("nof_db_events",         250000),
  ("nof_db_files",          3),
  ("fsize_db",              10695129460),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 10.70GB; nevents: 250.00k; release: 9_4_9; last modified: 2019-02-01 17:46:27"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-450_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToBulkGravitonToHHTo2B2Tau_M-450_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_450_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_450_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          2),
  ("fsize_db",              4416939298),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 4.42GB; nevents: 100.00k; release: 9_4_9; last modified: 2019-02-22 11:00:58"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-500_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToBulkGravitonToHHTo2B2Tau_M-500_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_500_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_500_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          1),
  ("fsize_db",              4450805287),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 4.45GB; nevents: 100.00k; release: 9_4_9; last modified: 2019-04-21 22:12:52"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-550_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToBulkGravitonToHHTo2B2Tau_M-550_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_550_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_550_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          2),
  ("fsize_db",              4675550080),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 4.68GB; nevents: 100.00k; release: 9_4_9; last modified: 2019-02-21 16:52:53"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-600_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToBulkGravitonToHHTo2B2Tau_M-600_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_600_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_600_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          2),
  ("fsize_db",              4653469892),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 4.65GB; nevents: 100.00k; release: 9_4_9; last modified: 2019-02-21 22:46:19"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-650_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToBulkGravitonToHHTo2B2Tau_M-650_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_650_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_650_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          2),
  ("fsize_db",              4740249400),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 4.74GB; nevents: 100.00k; release: 9_4_9; last modified: 2019-02-22 04:50:26"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-750_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToBulkGravitonToHHTo2B2Tau_M-750_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_750_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_750_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          2),
  ("fsize_db",              4895097500),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 4.90GB; nevents: 100.00k; release: 9_4_9; last modified: 2019-05-02 03:01:57"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-800_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToBulkGravitonToHHTo2B2Tau_M-800_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin2_800_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_800_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          1),
  ("fsize_db",              4784663508),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 4.78GB; nevents: 100.00k; release: 9_4_9; last modified: 2019-02-22 00:38:43"),
])

meta_dictionary["/VBFHHTo2B2Tau_CV_1_C2V_1_C3_0_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_VBFHHTo2B2Tau_CV_1_C2V_1_C3_0_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_0_hh_bbtt"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_0_hh_2b2t"),
  ("nof_db_events",         296060),
  ("nof_db_files",          5),
  ("fsize_db",              12663197291),
  ("xsection",              0.0003364547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.66GB; nevents: 296.06k; release: 9_4_9; last modified: 2019-03-06 12:40:23"),
])

meta_dictionary["/VBFHHTo2B2Tau_CV_1_C2V_1_C3_1_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_VBFHHTo2B2Tau_CV_1_C2V_1_C3_1_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_1_hh_bbtt"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_1_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          4),
  ("fsize_db",              12708206493),
  ("xsection",              0.0001260006),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.71GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-05 22:43:04"),
])

meta_dictionary["/VBFHHTo2B2Tau_CV_1_C2V_1_C3_2_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_VBFHHTo2B2Tau_CV_1_C2V_1_C3_2_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_2_hh_bbtt"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_2_hh_2b2t"),
  ("nof_db_events",         257175),
  ("nof_db_files",          4),
  ("fsize_db",              11297192364),
  ("xsection",              0.0001038674),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.30GB; nevents: 257.18k; release: 9_4_9; last modified: 2019-03-13 20:51:33"),
])

meta_dictionary["/VBFHHTo2B2Tau_CV_1_C2V_2_C3_1_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_VBFHHTo2B2Tau_CV_1_C2V_2_C3_1_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_vbf_nonresonant_1_2_1_hh_bbtt"),
  ("process_name_specific", "signal_vbf_nonresonant_1_2_1_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          5),
  ("fsize_db",              14237299312),
  ("xsection",              0.0010379183),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.24GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-07 05:55:50"),
])

meta_dictionary["/VBFHHTo2B2Tau_CV_1_5_C2V_1_C3_1_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_VBFHHTo2B2Tau_CV_1_5_C2V_1_C3_1_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_vbf_nonresonant_1p5_1_1_hh_bbtt"),
  ("process_name_specific", "signal_vbf_nonresonant_1p5_1_1_hh_2b2t"),
  ("nof_db_events",         299322),
  ("nof_db_files",          4),
  ("fsize_db",              13394462193),
  ("xsection",              0.0048194459),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.39GB; nevents: 299.32k; release: 9_4_9; last modified: 2019-03-05 22:46:44"),
])

meta_dictionary["/VBFHHTo2B2Tau_CV_0_5_C2V_1_C3_1_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_VBFHHTo2B2Tau_CV_0_5_C2V_1_C3_1_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_vbf_nonresonant_0p5_1_1_hh_bbtt"),
  ("process_name_specific", "signal_vbf_nonresonant_0p5_1_1_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          4),
  ("fsize_db",              13698968263),
  ("xsection",              0.0007901474),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.70GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-05 02:33:26"),
])

meta_dictionary["/GluGluToHHTo2B2Tau_node_SM_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec04_GluGluToHHTo2B2Tau_node_SM_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_sm_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          3),
  ("fsize_db",              13013254769),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.01GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-05-11 05:06:37"),
])

meta_dictionary["/GluGluToHHTo2B2Tau_node_box_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec04_GluGluToHHTo2B2Tau_node_box_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_box_hh_2b2t"),
  ("nof_db_events",         277140),
  ("nof_db_files",          3),
  ("fsize_db",              11969129912),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.97GB; nevents: 277.14k; release: 9_4_9; last modified: 2019-05-04 17:00:35"),
])

meta_dictionary["/GluGluToHHTo2B2Tau_node_2_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec04_GluGluToHHTo2B2Tau_node_2_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_2_hh_2b2t"),
  ("nof_db_events",         291000),
  ("nof_db_files",          3),
  ("fsize_db",              12693181737),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.69GB; nevents: 291.00k; release: 9_4_9; last modified: 2019-04-30 00:47:28"),
])

meta_dictionary["/GluGluToHHTo2B2Tau_node_9_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec04_GluGluToHHTo2B2Tau_node_9_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_9_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          3),
  ("fsize_db",              12554774019),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.55GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-05-02 21:10:53"),
])

meta_dictionary["/GluGluToHHTo2B2Tau_node_10_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec04_GluGluToHHTo2B2Tau_node_10_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_10_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          4),
  ("fsize_db",              12953354252),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.95GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-05-01 13:30:40"),
])

meta_dictionary["/GluGluToHHTo2B2Tau_node_11_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec04_GluGluToHHTo2B2Tau_node_11_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_11_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          3),
  ("fsize_db",              13042878478),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.04GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-04-30 16:50:41"),
])

meta_dictionary["/GluGluToHHTo2B2Tau_node_12_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec04_GluGluToHHTo2B2Tau_node_12_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_12_hh_2b2t"),
  ("nof_db_events",         298800),
  ("nof_db_files",          3),
  ("fsize_db",              13370108309),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.37GB; nevents: 298.80k; release: 9_4_9; last modified: 2019-04-30 16:54:09"),
])

meta_dictionary["/GluGluToHHTo2B2Tau_node_13_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Dec04_GluGluToHHTo2B2Tau_node_13_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_13_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          3),
  ("fsize_db",              13600771777),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.60GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-01-16 19:50:06"),
])


# event statistics by sample category:
# signal_ggf_spin0_260_hh_bbvv:           300.00k
# signal_ggf_spin0_270_hh_bbvv:           294.63k
# signal_ggf_spin0_300_hh_bbvv:           300.00k
# signal_ggf_spin0_350_hh_bbvv:           295.15k
# signal_ggf_spin0_400_hh_bbvv:           300.00k
# signal_ggf_spin0_450_hh_bbvv:           296.26k
# signal_ggf_spin0_500_hh_bbvv:           300.00k
# signal_ggf_spin0_550_hh_bbvv:           300.00k
# signal_ggf_spin0_600_hh_bbvv:           300.00k
# signal_ggf_spin0_650_hh_bbvv:           299.54k
# signal_ggf_spin0_750_hh_bbvv:           298.73k
# signal_ggf_spin0_800_hh_bbvv:           299.70k
# signal_ggf_spin0_900_hh_bbvv:           298.73k
# signal_ggf_spin0_1000_hh_bbvv:          300.00k
# signal_ggf_spin2_260_hh_bbvv:           300.00k
# signal_ggf_spin2_270_hh_bbvv:           300.00k
# signal_ggf_spin2_300_hh_bbvv:           300.00k
# signal_ggf_spin2_350_hh_bbvv:           300.00k
# signal_ggf_spin2_400_hh_bbvv:           300.00k
# signal_ggf_spin2_450_hh_bbvv:           300.00k
# signal_ggf_spin2_500_hh_bbvv:           300.00k
# signal_ggf_spin2_550_hh_bbvv:           300.00k
# signal_ggf_spin2_600_hh_bbvv:           300.00k
# signal_ggf_spin2_650_hh_bbvv:           298.81k
# signal_ggf_spin2_700_hh_bbvv:           300.00k
# signal_ggf_spin2_800_hh_bbvv:           300.00k
# signal_ggf_spin2_900_hh_bbvv:           300.00k
# signal_ggf_spin2_1000_hh_bbvv:          299.12k
# signal_vbf_nonresonant_1_1_1_hh_bbvv:   300.00k
# signal_vbf_nonresonant_1_1_2_hh_bbvv:   300.00k
# signal_vbf_nonresonant_1_2_1_hh_bbvv:   300.00k
# signal_vbf_nonresonant_1_1_0_hh_bbvv:   300.00k
# signal_vbf_nonresonant_1p5_1_1_hh_bbvv: 299.40k
# signal_vbf_nonresonant_0p5_1_1_hh_bbvv: 297.18k
# signal_ggf_nonresonant_hh_bbvv:         4.20M
# signal_ggf_nonresonant_hh_bbvv_sl:      4.20M
# signal_ggf_spin0_250_hh_bbvv_sl:        300.00k
# signal_ggf_spin0_260_hh_bbvv_sl:        299.40k
# signal_ggf_spin0_270_hh_bbvv_sl:        300.00k
# signal_ggf_spin0_300_hh_bbvv_sl:        300.00k
# signal_ggf_spin0_350_hh_bbvv_sl:        300.00k
# signal_ggf_spin0_400_hh_bbvv_sl:        300.00k
# signal_ggf_spin0_450_hh_bbvv_sl:        292.03k
# signal_ggf_spin0_500_hh_bbvv_sl:        300.00k
# signal_ggf_spin0_550_hh_bbvv_sl:        300.00k
# signal_ggf_spin0_600_hh_bbvv_sl:        300.00k
# signal_ggf_spin0_700_hh_bbvv_sl:        300.00k
# signal_ggf_spin0_800_hh_bbvv_sl:        300.00k
# signal_ggf_spin0_900_hh_bbvv_sl:        300.00k
# signal_ggf_spin0_1000_hh_bbvv_sl:       299.47k
# signal_ggf_spin2_250_hh_bbvv_sl:        300.00k
# signal_ggf_spin2_260_hh_bbvv_sl:        300.00k
# signal_ggf_spin2_270_hh_bbvv_sl:        299.23k
# signal_ggf_spin2_300_hh_bbvv_sl:        300.00k
# signal_ggf_spin2_350_hh_bbvv_sl:        299.40k
# signal_ggf_spin2_400_hh_bbvv_sl:        299.99k
# signal_ggf_spin2_450_hh_bbvv_sl:        300.00k
# signal_ggf_spin2_500_hh_bbvv_sl:        300.00k
# signal_ggf_spin2_550_hh_bbvv_sl:        300.00k
# signal_ggf_spin2_600_hh_bbvv_sl:        300.00k
# signal_ggf_spin2_650_hh_bbvv_sl:        300.00k
# signal_ggf_spin2_700_hh_bbvv_sl:        300.00k
# signal_ggf_spin2_800_hh_bbvv_sl:        300.00k
# signal_ggf_spin2_900_hh_bbvv_sl:        300.00k
# signal_ggf_spin2_1000_hh_bbvv_sl:       300.00k
# signal_ggf_spin0_250_hh_bbtt:           50.00k
# signal_ggf_spin0_260_hh_bbtt:           50.00k
# signal_ggf_spin0_270_hh_bbtt:           50.00k
# signal_ggf_spin0_280_hh_bbtt:           49.60k
# signal_ggf_spin0_300_hh_bbtt:           450.00k
# signal_ggf_spin0_320_hh_bbtt:           50.00k
# signal_ggf_spin0_340_hh_bbtt:           48.00k
# signal_ggf_spin0_350_hh_bbtt:           50.00k
# signal_ggf_spin0_400_hh_bbtt:           250.00k
# signal_ggf_spin0_450_hh_bbtt:           99.60k
# signal_ggf_spin0_500_hh_bbtt:           99.20k
# signal_ggf_spin0_550_hh_bbtt:           100.00k
# signal_ggf_spin0_600_hh_bbtt:           100.00k
# signal_ggf_spin0_650_hh_bbtt:           100.00k
# signal_ggf_spin0_800_hh_bbtt:           100.00k
# signal_ggf_spin0_900_hh_bbtt:           100.00k
# signal_ggf_spin2_250_hh_bbtt:           50.00k
# signal_ggf_spin2_260_hh_bbtt:           50.00k
# signal_ggf_spin2_270_hh_bbtt:           50.00k
# signal_ggf_spin2_280_hh_bbtt:           50.00k
# signal_ggf_spin2_300_hh_bbtt:           447.40k
# signal_ggf_spin2_320_hh_bbtt:           50.00k
# signal_ggf_spin2_340_hh_bbtt:           50.00k
# signal_ggf_spin2_350_hh_bbtt:           50.00k
# signal_ggf_spin2_400_hh_bbtt:           250.00k
# signal_ggf_spin2_450_hh_bbtt:           100.00k
# signal_ggf_spin2_500_hh_bbtt:           100.00k
# signal_ggf_spin2_550_hh_bbtt:           100.00k
# signal_ggf_spin2_600_hh_bbtt:           100.00k
# signal_ggf_spin2_650_hh_bbtt:           100.00k
# signal_ggf_spin2_750_hh_bbtt:           100.00k
# signal_ggf_spin2_800_hh_bbtt:           100.00k
# signal_vbf_nonresonant_1_1_0_hh_bbtt:   296.06k
# signal_vbf_nonresonant_1_1_1_hh_bbtt:   300.00k
# signal_vbf_nonresonant_1_1_2_hh_bbtt:   257.18k
# signal_vbf_nonresonant_1_2_1_hh_bbtt:   300.00k
# signal_vbf_nonresonant_1p5_1_1_hh_bbtt: 299.32k
# signal_vbf_nonresonant_0p5_1_1_hh_bbtt: 300.00k
# signal_ggf_nonresonant_hh_bbtt:         2.37M

