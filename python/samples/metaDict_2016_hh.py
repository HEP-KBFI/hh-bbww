from collections import OrderedDict as OD

# file generated at 2021-02-07 13:53:25 with the following command:
# find_samples.py -V -i ../../tthAnalysis/NanoAOD/test/datasets/txt/datasets_hh_bbww_mc_2016_RunIISummer16MiniAODv3.txt -m python/samples/metaDict_2016_hh.py -s ../../tthAnalysis/NanoAOD/test/datasets/txt/sum_datasets_hh_bbww_2016_RunIISummer16MiniAODv3.txt -c python/samples/sampleLocations_2016_nanoAOD_hh_bbww.txt

meta_dictionary = OD()


### event sums

sum_events = { 
  ("signal_ggf_spin0_900_hh_2b2t", "signal_ggf_spin0_900_hh_2b2t_PSWeights"),
  ("signal_vbf_nonresonant_1_0_1_hh_2b2t_dipoleRecoilOff", "signal_vbf_nonresonant_1_0_1_hh_2b2t_dipoleRecoilOff_ext1"),
  ("signal_ggf_nonresonant_node_sm_hh_2b2v", "signal_ggf_nonresonant_node_box_hh_2b2v", "signal_ggf_nonresonant_node_1_hh_2b2v", "signal_ggf_nonresonant_node_2_hh_2b2v", "signal_ggf_nonresonant_node_3_hh_2b2v", "signal_ggf_nonresonant_node_4_hh_2b2v", "signal_ggf_nonresonant_node_5_hh_2b2v", "signal_ggf_nonresonant_node_6_hh_2b2v", "signal_ggf_nonresonant_node_7_hh_2b2v", "signal_ggf_nonresonant_node_8_hh_2b2v", "signal_ggf_nonresonant_node_9_hh_2b2v", "signal_ggf_nonresonant_node_10_hh_2b2v", "signal_ggf_nonresonant_node_11_hh_2b2v", "signal_ggf_nonresonant_node_12_hh_2b2v"),
  ("signal_ggf_nonresonant_node_sm_hh_2b2v_sl_PSWeights", "signal_ggf_nonresonant_node_1_hh_2b2v_sl_PSWeights", "signal_ggf_nonresonant_node_2_hh_2b2v_sl_PSWeights", "signal_ggf_nonresonant_node_3_hh_2b2v_sl_PSWeights", "signal_ggf_nonresonant_node_4_hh_2b2v_sl_PSWeights", "signal_ggf_nonresonant_node_5_hh_2b2v_sl", "signal_ggf_nonresonant_node_6_hh_2b2v_sl_PSWeights", "signal_ggf_nonresonant_node_7_hh_2b2v_sl", "signal_ggf_nonresonant_node_8_hh_2b2v_sl_PSWeights", "signal_ggf_nonresonant_node_9_hh_2b2v_sl", "signal_ggf_nonresonant_node_10_hh_2b2v_sl_PSWeights", "signal_ggf_nonresonant_node_11_hh_2b2v_sl_PSWeights", "signal_ggf_nonresonant_node_12_hh_2b2v_sl_PSWeights"),
  ("signal_ggf_nonresonant_node_sm_hh_2b2t", "signal_ggf_nonresonant_node_box_hh_2b2t", "signal_ggf_nonresonant_node_1_hh_2b2t", "signal_ggf_nonresonant_node_2_hh_2b2t", "signal_ggf_nonresonant_node_3_hh_2b2t", "signal_ggf_nonresonant_node_4_hh_2b2t", "signal_ggf_nonresonant_node_5_hh_2b2t", "signal_ggf_nonresonant_node_6_hh_2b2t", "signal_ggf_nonresonant_node_7_hh_2b2t", "signal_ggf_nonresonant_node_8_hh_2b2t", "signal_ggf_nonresonant_node_9_hh_2b2t", "signal_ggf_nonresonant_node_10_hh_2b2t", "signal_ggf_nonresonant_node_11_hh_2b2t", "signal_ggf_nonresonant_node_12_hh_2b2t", "signal_ggf_nonresonant_node_13_hh_2b2t"),
}


meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-260_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToRadionToHHTo2B2VTo2L2Nu_M-260_narrow_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_260_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_260_hh_2b2v"),
  ("nof_db_events",         299998),
  ("nof_db_files",          4),
  ("fsize_db",              11821300223),
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 15.07GB; nevents: 299.12k; release: 9_4_9; last modified: 2019-03-03 19:51:10"),
])

meta_dictionary["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_1_hh_bbvv"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_1_hh_2b2v_dipoleRecoilOff"),
  ("nof_db_events",         398999),
  ("nof_db_files",          18),
  ("fsize_db",              18513625499),
  ("xsection",              4.773e-05),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 18.51GB; nevents: 399.00k; release: 9_4_9; last modified: 2020-10-05 18:52:44"),
])

meta_dictionary["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_2_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct19_VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_2_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_2_hh_bbvv"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_2_hh_2b2v_dipoleRecoilOff"),
  ("nof_db_events",         396799),
  ("nof_db_files",          26),
  ("fsize_db",              19203455679),
  ("xsection",              3.9562e-05),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 19.20GB; nevents: 396.80k; release: 9_4_9; last modified: 2020-10-18 08:02:16"),
])

meta_dictionary["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_2_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFHHTo2B2VTo2L2Nu_CV_1_C2V_2_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94"),
  ("sample_category",       "signal_vbf_nonresonant_1_2_1_hh_bbvv"),
  ("process_name_specific", "signal_vbf_nonresonant_1_2_1_hh_2b2v_dipoleRecoilOff"),
  ("nof_db_events",         399200),
  ("nof_db_files",          25),
  ("fsize_db",              20560010155),
  ("xsection",              0.000398001),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.56GB; nevents: 399.20k; release: 9_4_9; last modified: 2020-10-10 06:50:35"),
])

meta_dictionary["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_0_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_0_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_0_hh_bbvv"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_0_hh_2b2v_dipoleRecoilOff"),
  ("nof_db_events",         399999),
  ("nof_db_files",          24),
  ("fsize_db",              18665186777),
  ("xsection",              0.000126972),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 18.67GB; nevents: 400.00k; release: 9_4_9; last modified: 2020-10-05 19:15:01"),
])

meta_dictionary["/VBFHHTo2B2VTo2L2Nu_CV_1_5_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFHHTo2B2VTo2L2Nu_CV_1_5_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_"),
  ("sample_category",       "signal_vbf_nonresonant_1p5_1_1_hh_bbvv"),
  ("process_name_specific", "signal_vbf_nonresonant_1p5_1_1_hh_2b2v_dipoleRecoilOff"),
  ("nof_db_events",         398799),
  ("nof_db_files",          15),
  ("fsize_db",              19328505325),
  ("xsection",              0.001834377),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 19.33GB; nevents: 398.80k; release: 9_4_9; last modified: 2020-09-28 12:13:10"),
])

meta_dictionary["/VBFHHTo2B2VTo2L2Nu_CV_0_5_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFHHTo2B2VTo2L2Nu_CV_0_5_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_"),
  ("sample_category",       "signal_vbf_nonresonant_0p5_1_1_hh_bbvv"),
  ("process_name_specific", "signal_vbf_nonresonant_0p5_1_1_hh_2b2v_dipoleRecoilOff"),
  ("nof_db_events",         399097),
  ("nof_db_files",          24),
  ("fsize_db",              20226758825),
  ("xsection",              0.000300811),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.23GB; nevents: 399.10k; release: 9_4_9; last modified: 2020-10-08 12:52:01"),
])

meta_dictionary["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFHHTo2B2VTo2L2Nu_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94"),
  ("sample_category",       "signal_vbf_nonresonant_1_0_1_hh_bbvv"),
  ("process_name_specific", "signal_vbf_nonresonant_1_0_1_hh_2b2v_dipoleRecoilOff"),
  ("nof_db_events",         396800),
  ("nof_db_files",          24),
  ("fsize_db",              19702706677),
  ("xsection",              0.000753069),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 19.70GB; nevents: 396.80k; release: 9_4_9; last modified: 2020-10-05 19:18:46"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_SM_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2019Oct05_GluGluToHHTo2B2VTo2L2Nu_node_SM_13TeV-madgraph-v2__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_node_sm_hh_2b2v"),
  ("nof_db_events",         299999),
  ("nof_db_files",          5),
  ("fsize_db",              13376661186),
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
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
  ("xsection",              0.027654),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.03GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-08 04:50:00"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_cHHH0_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct31_GluGluToHHTo2B2VTo2L2Nu_node_cHHH0_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptoti"),
  ("sample_category",       "signal_ggf_nonresonant_cHHH0_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_cHHH0_hh_2b2v"),
  ("nof_db_events",         399999),
  ("nof_db_files",          44),
  ("fsize_db",              16972955311),
  ("xsection",              0.001928162),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.97GB; nevents: 400.00k; release: 9_4_9; last modified: 2020-10-26 01:00:45"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_cHHH1_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct17_GluGluToHHTo2B2VTo2L2Nu_node_cHHH1_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptoti"),
  ("sample_category",       "signal_ggf_nonresonant_cHHH1_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_cHHH1_hh_2b2v"),
  ("nof_db_events",         396798),
  ("nof_db_files",          89),
  ("fsize_db",              17674000555),
  ("xsection",              0.000858569),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 17.67GB; nevents: 396.80k; release: 9_4_9; last modified: 2020-10-13 20:45:52"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_cHHH2p45_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToHHTo2B2VTo2L2Nu_node_cHHH2p45_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asympt"),
  ("sample_category",       "signal_ggf_nonresonant_cHHH2p45_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_cHHH2p45_hh_2b2v"),
  ("nof_db_events",         398400),
  ("nof_db_files",          25),
  ("fsize_db",              16864768372),
  ("xsection",              0.000362916),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.86GB; nevents: 398.40k; release: 9_4_9; last modified: 2020-09-27 14:11:53"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_cHHH5_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToHHTo2B2VTo2L2Nu_node_cHHH5_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptoti"),
  ("sample_category",       "signal_ggf_nonresonant_cHHH5_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_cHHH5_hh_2b2v"),
  ("nof_db_events",         394800),
  ("nof_db_files",          42),
  ("fsize_db",              16232250597),
  ("xsection",              0.002521218),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.23GB; nevents: 394.80k; release: 9_4_9; last modified: 2020-10-05 19:07:08"),
])

meta_dictionary["/GluGluToHHTo2B2WToLNu2J_node_SM_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToHHTo2B2WToLNu2J_node_SM_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_node_sm_hh_2b2v_sl_PSWeights"),
  ("nof_db_events",         299996),
  ("nof_db_files",          26),
  ("fsize_db",              13854390389),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.85GB; nevents: 300.00k; release: 9_4_9; last modified: 2020-10-05 19:07:40"),
])

meta_dictionary["/GluGluToHHTo2B2WToLNu2J_node_1_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToHHTo2B2WToLNu2J_node_1_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_node_1_hh_2b2v_sl_PSWeights"),
  ("nof_db_events",         297895),
  ("nof_db_files",          19),
  ("fsize_db",              13390936467),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.39GB; nevents: 297.89k; release: 9_4_9; last modified: 2020-10-05 19:03:00"),
])

meta_dictionary["/GluGluToHHTo2B2WToLNu2J_node_2_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToHHTo2B2WToLNu2J_node_2_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_node_2_hh_2b2v_sl_PSWeights"),
  ("nof_db_events",         298398),
  ("nof_db_files",          22),
  ("fsize_db",              14956599323),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.96GB; nevents: 298.40k; release: 9_4_9; last modified: 2020-10-03 06:21:59"),
])

meta_dictionary["/GluGluToHHTo2B2WToLNu2J_node_3_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct31_GluGluToHHTo2B2WToLNu2J_node_3_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_node_3_hh_2b2v_sl_PSWeights"),
  ("nof_db_events",         287898),
  ("nof_db_files",          20),
  ("fsize_db",              13260878078),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.26GB; nevents: 287.90k; release: 9_4_9; last modified: 2020-10-26 01:21:31"),
])

meta_dictionary["/GluGluToHHTo2B2WToLNu2J_node_4_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToHHTo2B2WToLNu2J_node_4_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_node_4_hh_2b2v_sl_PSWeights"),
  ("nof_db_events",         293698),
  ("nof_db_files",          20),
  ("fsize_db",              13281373082),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.28GB; nevents: 293.70k; release: 9_4_9; last modified: 2020-10-05 19:15:46"),
])

meta_dictionary["/GluGluToHHTo2B2WToLNu2J_node_5_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToHHTo2B2WToLNu2J_node_5_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_node_5_hh_2b2v_sl"),
  ("nof_db_events",         299098),
  ("nof_db_files",          19),
  ("fsize_db",              14447245371),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.45GB; nevents: 299.10k; release: 9_4_9; last modified: 2020-10-05 19:14:31"),
])

meta_dictionary["/GluGluToHHTo2B2WToLNu2J_node_6_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToHHTo2B2WToLNu2J_node_6_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_node_6_hh_2b2v_sl_PSWeights"),
  ("nof_db_events",         298896),
  ("nof_db_files",          16),
  ("fsize_db",              13518884270),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.52GB; nevents: 298.90k; release: 9_4_9; last modified: 2020-10-05 18:50:24"),
])

meta_dictionary["/GluGluToHHTo2B2WToLNu2J_node_7_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToHHTo2B2WToLNu2J_node_7_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_node_7_hh_2b2v_sl"),
  ("nof_db_events",         298398),
  ("nof_db_files",          18),
  ("fsize_db",              13451681242),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.45GB; nevents: 298.40k; release: 9_4_9; last modified: 2020-10-05 18:56:45"),
])

meta_dictionary["/GluGluToHHTo2B2WToLNu2J_node_8_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToHHTo2B2WToLNu2J_node_8_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_node_8_hh_2b2v_sl_PSWeights"),
  ("nof_db_events",         298899),
  ("nof_db_files",          19),
  ("fsize_db",              13370755539),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.37GB; nevents: 298.90k; release: 9_4_9; last modified: 2020-10-03 06:02:43"),
])

meta_dictionary["/GluGluToHHTo2B2WToLNu2J_node_9_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToHHTo2B2WToLNu2J_node_9_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_node_9_hh_2b2v_sl"),
  ("nof_db_events",         299996),
  ("nof_db_files",          21),
  ("fsize_db",              14367121107),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.37GB; nevents: 300.00k; release: 9_4_9; last modified: 2020-10-08 12:52:31"),
])

meta_dictionary["/GluGluToHHTo2B2WToLNu2J_node_10_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct19_GluGluToHHTo2B2WToLNu2J_node_10_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_node_10_hh_2b2v_sl_PSWeights"),
  ("nof_db_events",         299998),
  ("nof_db_files",          17),
  ("fsize_db",              13467941180),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.47GB; nevents: 300.00k; release: 9_4_9; last modified: 2020-10-05 18:51:44"),
])

meta_dictionary["/GluGluToHHTo2B2WToLNu2J_node_11_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToHHTo2B2WToLNu2J_node_11_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_node_11_hh_2b2v_sl_PSWeights"),
  ("nof_db_events",         298398),
  ("nof_db_files",          18),
  ("fsize_db",              13629128068),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.63GB; nevents: 298.40k; release: 9_4_9; last modified: 2020-09-26 07:16:02"),
])

meta_dictionary["/GluGluToHHTo2B2WToLNu2J_node_12_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToHHTo2B2WToLNu2J_node_12_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_node_12_hh_2b2v_sl_PSWeights"),
  ("nof_db_events",         295397),
  ("nof_db_files",          18),
  ("fsize_db",              13215460281),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.22GB; nevents: 295.40k; release: 9_4_9; last modified: 2020-10-05 19:01:26"),
])

meta_dictionary["/GluGluToHHTo2B2VLNu2J_node_cHHH0_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct31_GluGluToHHTo2B2VLNu2J_node_cHHH0_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_"),
  ("sample_category",       "signal_ggf_nonresonant_cHHH0_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_cHHH0_hh_2b2v_sl"),
  ("nof_db_events",         398394),
  ("nof_db_files",          26),
  ("fsize_db",              16886138632),
  ("xsection",              0.0076246),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.89GB; nevents: 398.39k; release: 9_4_9; last modified: 2020-10-23 14:48:58"),
])

meta_dictionary["/GluGluToHHTo2B2VLNu2J_node_cHHH1_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToHHTo2B2VLNu2J_node_cHHH1_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_"),
  ("sample_category",       "signal_ggf_nonresonant_cHHH1_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_cHHH1_hh_2b2v_sl"),
  ("nof_db_events",         398998),
  ("nof_db_files",          43),
  ("fsize_db",              17448307042),
  ("xsection",              0.00339506),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 17.45GB; nevents: 399.00k; release: 9_4_9; last modified: 2020-09-28 14:13:29"),
])

meta_dictionary["/GluGluToHHTo2B2VLNu2J_node_cHHH2p45_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct17_GluGluToHHTo2B2VLNu2J_node_cHHH2p45_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptot"),
  ("sample_category",       "signal_ggf_nonresonant_cHHH2p45_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_cHHH2p45_hh_2b2v_sl"),
  ("nof_db_events",         391395),
  ("nof_db_files",          23),
  ("fsize_db",              16836087533),
  ("xsection",              0.00143508),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.84GB; nevents: 391.39k; release: 9_4_9; last modified: 2020-10-17 08:01:41"),
])

meta_dictionary["/GluGluToHHTo2B2VLNu2J_node_cHHH5_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct31_GluGluToHHTo2B2VLNu2J_node_cHHH5_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_"),
  ("sample_category",       "signal_ggf_nonresonant_cHHH5_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_cHHH5_hh_2b2v_sl"),
  ("nof_db_events",         396596),
  ("nof_db_files",          41),
  ("fsize_db",              16437001616),
  ("xsection",              0.00996974),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.44GB; nevents: 396.60k; release: 9_4_9; last modified: 2020-10-20 18:01:45"),
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

meta_dictionary["/GluGluToRadionToHHTo2B2VToLNu2J_M-650_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToRadionToHHTo2B2VToLNu2J_M-650_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "signal_ggf_spin0_650_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_650_hh_2b2v_sl"),
  ("nof_db_events",         299997),
  ("nof_db_files",          5),
  ("fsize_db",              14421548407),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.42GB; nevents: 300.00k; release: 9_4_9; last modified: 2019-03-03 22:57:20"),
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

meta_dictionary["/VBFHHTo2B2WToLNu2J_CV_1_C2V_1_C3_0_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFHHTo2B2WToLNu2J_CV_1_C2V_1_C3_0_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_0_hh_bbvv_sl"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_0_hh_2b2v_sl_dipoleRecoilOff"),
  ("nof_db_events",         398999),
  ("nof_db_files",          13),
  ("fsize_db",              18635165335),
  ("xsection",              0.000502091),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 18.64GB; nevents: 399.00k; release: 9_4_9; last modified: 2020-10-05 18:57:55"),
])

meta_dictionary["/VBFHHTo2B2WToLNu2J_CV_1_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFHHTo2B2WToLNu2J_CV_1_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_1_hh_bbvv_sl"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_1_hh_2b2v_sl_dipoleRecoilOff"),
  ("nof_db_events",         399998),
  ("nof_db_files",          23),
  ("fsize_db",              18828525571),
  ("xsection",              0.000188741),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 18.83GB; nevents: 400.00k; release: 9_4_9; last modified: 2020-10-08 12:54:02"),
])

meta_dictionary["/VBFHHTo2B2WToLNu2J_CV_1_C2V_1_C3_2_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFHHTo2B2WToLNu2J_CV_1_C2V_1_C3_2_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_2_hh_bbvv_sl"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_2_hh_2b2v_sl_dipoleRecoilOff"),
  ("nof_db_events",         395494),
  ("nof_db_files",          24),
  ("fsize_db",              19284295734),
  ("xsection",              0.000156443),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 19.28GB; nevents: 395.49k; release: 9_4_9; last modified: 2020-09-29 06:02:25"),
])

meta_dictionary["/VBFHHTo2B2WToLNu2J_CV_1_C2V_2_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFHHTo2B2WToLNu2J_CV_1_C2V_2_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94"),
  ("sample_category",       "signal_vbf_nonresonant_1_2_1_hh_bbvv_sl"),
  ("process_name_specific", "signal_vbf_nonresonant_1_2_1_hh_2b2v_sl_dipoleRecoilOff"),
  ("nof_db_events",         398193),
  ("nof_db_files",          20),
  ("fsize_db",              20938124623),
  ("xsection",              0.001573824),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.94GB; nevents: 398.19k; release: 9_4_9; last modified: 2020-09-28 20:11:15"),
])

meta_dictionary["/VBFHHTo2B2WToLNu2J_CV_0_5_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFHHTo2B2WToLNu2J_CV_0_5_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_"),
  ("sample_category",       "signal_vbf_nonresonant_0p5_1_1_hh_bbvv_sl"),
  ("process_name_specific", "signal_vbf_nonresonant_0p5_1_1_hh_2b2v_sl_dipoleRecoilOff"),
  ("nof_db_events",         399994),
  ("nof_db_files",          8),
  ("fsize_db",              20402821916),
  ("xsection",              0.001189508),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.40GB; nevents: 399.99k; release: 9_4_9; last modified: 2020-10-03 06:36:40"),
])

meta_dictionary["/VBFHHTo2B2WToLNu2J_CV_1_5_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct31_VBFHHTo2B2WToLNu2J_CV_1_5_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_"),
  ("sample_category",       "signal_vbf_nonresonant_1p5_1_1_hh_bbvv_sl"),
  ("process_name_specific", "signal_vbf_nonresonant_1p5_1_1_hh_2b2v_sl_dipoleRecoilOff"),
  ("nof_db_events",         395494),
  ("nof_db_files",          24),
  ("fsize_db",              19666709618),
  ("xsection",              0.007253737),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 19.67GB; nevents: 395.49k; release: 9_4_9; last modified: 2020-10-26 01:08:20"),
])

meta_dictionary["/VBFHHTo2B2WToLNu2J_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFHHTo2B2WToLNu2J_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94"),
  ("sample_category",       "signal_vbf_nonresonant_1_0_1_hh_bbvv_sl"),
  ("process_name_specific", "signal_vbf_nonresonant_1_0_1_hh_2b2v_sl_dipoleRecoilOff"),
  ("nof_db_events",         399096),
  ("nof_db_files",          27),
  ("fsize_db",              20236728193),
  ("xsection",              0.002977884),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.24GB; nevents: 399.10k; release: 9_4_9; last modified: 2020-10-05 18:50:34"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToRadionToHHTo2B2Tau_M-250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymp"),
  ("sample_category",       "signal_vbf_spin0_250_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_250_hh_2b2t"),
  ("nof_db_events",         399200),
  ("nof_db_files",          6),
  ("fsize_db",              21299446883),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.30GB; nevents: 399.20k; release: 9_4_9; last modified: 2020-09-16 05:59:59"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-260_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToRadionToHHTo2B2Tau_M-260_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymp"),
  ("sample_category",       "signal_vbf_spin0_260_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_260_hh_2b2t"),
  ("nof_db_events",         395000),
  ("nof_db_files",          5),
  ("fsize_db",              21209489911),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.21GB; nevents: 395.00k; release: 9_4_9; last modified: 2020-09-14 18:59:16"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-270_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToRadionToHHTo2B2Tau_M-270_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymp"),
  ("sample_category",       "signal_vbf_spin0_270_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_270_hh_2b2t"),
  ("nof_db_events",         395700),
  ("nof_db_files",          7),
  ("fsize_db",              21337721793),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.34GB; nevents: 395.70k; release: 9_4_9; last modified: 2020-09-18 00:14:53"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-280_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToRadionToHHTo2B2Tau_M-280_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymp"),
  ("sample_category",       "signal_vbf_spin0_280_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_280_hh_2b2t"),
  ("nof_db_events",         396400),
  ("nof_db_files",          5),
  ("fsize_db",              21531514022),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.53GB; nevents: 396.40k; release: 9_4_9; last modified: 2020-09-16 03:13:07"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-300_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToRadionToHHTo2B2Tau_M-300_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymp"),
  ("sample_category",       "signal_vbf_spin0_300_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_300_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          5),
  ("fsize_db",              16521214810),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.52GB; nevents: 300.00k; release: 9_4_9; last modified: 2020-09-17 03:16:32"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-320_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToRadionToHHTo2B2Tau_M-320_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymp"),
  ("sample_category",       "signal_vbf_spin0_320_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_320_hh_2b2t"),
  ("nof_db_events",         299200),
  ("nof_db_files",          5),
  ("fsize_db",              16662151278),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.66GB; nevents: 299.20k; release: 9_4_9; last modified: 2020-09-16 05:59:49"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-350_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToRadionToHHTo2B2Tau_M-350_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymp"),
  ("sample_category",       "signal_vbf_spin0_350_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_350_hh_2b2t"),
  ("nof_db_events",         298000),
  ("nof_db_files",          8),
  ("fsize_db",              16908533930),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.91GB; nevents: 298.00k; release: 9_4_9; last modified: 2020-09-25 19:23:44"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-400_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToRadionToHHTo2B2Tau_M-400_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymp"),
  ("sample_category",       "signal_vbf_spin0_400_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_400_hh_2b2t"),
  ("nof_db_events",         298400),
  ("nof_db_files",          5),
  ("fsize_db",              17255325259),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 17.26GB; nevents: 298.40k; release: 9_4_9; last modified: 2020-09-16 03:15:27"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-450_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToRadionToHHTo2B2Tau_M-450_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymp"),
  ("sample_category",       "signal_vbf_spin0_450_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_450_hh_2b2t"),
  ("nof_db_events",         298400),
  ("nof_db_files",          3),
  ("fsize_db",              17580406855),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 17.58GB; nevents: 298.40k; release: 9_4_9; last modified: 2020-09-14 17:45:40"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToRadionToHHTo2B2Tau_M-500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymp"),
  ("sample_category",       "signal_vbf_spin0_500_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_500_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          3),
  ("fsize_db",              17956939093),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 17.96GB; nevents: 300.00k; release: 9_4_9; last modified: 2020-09-14 23:44:13"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-550_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToRadionToHHTo2B2Tau_M-550_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymp"),
  ("sample_category",       "signal_vbf_spin0_550_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_550_hh_2b2t"),
  ("nof_db_events",         299300),
  ("nof_db_files",          6),
  ("fsize_db",              18237199185),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 18.24GB; nevents: 299.30k; release: 9_4_9; last modified: 2020-09-16 03:19:52"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-600_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToRadionToHHTo2B2Tau_M-600_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymp"),
  ("sample_category",       "signal_vbf_spin0_600_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_600_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          5),
  ("fsize_db",              12377694096),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.38GB; nevents: 200.00k; release: 9_4_9; last modified: 2020-09-16 03:13:52"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-650_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToRadionToHHTo2B2Tau_M-650_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymp"),
  ("sample_category",       "signal_vbf_spin0_650_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_650_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          4),
  ("fsize_db",              12477486812),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.48GB; nevents: 200.00k; release: 9_4_9; last modified: 2020-09-14 11:44:56"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-700_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToRadionToHHTo2B2Tau_M-700_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymp"),
  ("sample_category",       "signal_vbf_spin0_700_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_700_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          3),
  ("fsize_db",              12617931333),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.62GB; nevents: 200.00k; release: 9_4_9; last modified: 2020-09-13 12:44:02"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct19_VBFToRadionToHHTo2B2Tau_M-750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymp"),
  ("sample_category",       "signal_vbf_spin0_750_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_750_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          4),
  ("fsize_db",              12763317309),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.76GB; nevents: 200.00k; release: 9_4_9; last modified: 2020-09-15 14:43:01"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-800_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToRadionToHHTo2B2Tau_M-800_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymp"),
  ("sample_category",       "signal_vbf_spin0_800_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_800_hh_2b2t"),
  ("nof_db_events",         199300),
  ("nof_db_files",          4),
  ("fsize_db",              12855127044),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.86GB; nevents: 199.30k; release: 9_4_9; last modified: 2020-09-15 21:52:45"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-850_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToRadionToHHTo2B2Tau_M-850_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymp"),
  ("sample_category",       "signal_vbf_spin0_850_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_850_hh_2b2t"),
  ("nof_db_events",         199400),
  ("nof_db_files",          5),
  ("fsize_db",              12962982116),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.96GB; nevents: 199.40k; release: 9_4_9; last modified: 2020-09-15 14:46:31"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-900_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToRadionToHHTo2B2Tau_M-900_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymp"),
  ("sample_category",       "signal_vbf_spin0_900_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_900_hh_2b2t"),
  ("nof_db_events",         199600),
  ("nof_db_files",          4),
  ("fsize_db",              13038158901),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.04GB; nevents: 199.60k; release: 9_4_9; last modified: 2020-09-16 03:01:23"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-1000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToRadionToHHTo2B2Tau_M-1000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asym"),
  ("sample_category",       "signal_vbf_spin0_1000_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_1000_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          3),
  ("fsize_db",              6644043956),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.64GB; nevents: 100.00k; release: 9_4_9; last modified: 2020-09-16 03:15:37"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-1250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToRadionToHHTo2B2Tau_M-1250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asym"),
  ("sample_category",       "signal_vbf_spin0_1250_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_1250_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          3),
  ("fsize_db",              6799676332),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.80GB; nevents: 100.00k; release: 9_4_9; last modified: 2020-09-16 03:07:46"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-1500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToRadionToHHTo2B2Tau_M-1500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asym"),
  ("sample_category",       "signal_vbf_spin0_1500_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_1500_hh_2b2t"),
  ("nof_db_events",         99700),
  ("nof_db_files",          4),
  ("fsize_db",              6898339776),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.90GB; nevents: 99.70k; release: 9_4_9; last modified: 2020-09-16 02:57:42"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-1750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToRadionToHHTo2B2Tau_M-1750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asym"),
  ("sample_category",       "signal_vbf_spin0_1750_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_1750_hh_2b2t"),
  ("nof_db_events",         99500),
  ("nof_db_files",          1),
  ("fsize_db",              6898552202),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.90GB; nevents: 99.50k; release: 9_4_9; last modified: 2020-09-16 05:58:59"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-2000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToRadionToHHTo2B2Tau_M-2000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asym"),
  ("sample_category",       "signal_vbf_spin0_2000_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_2000_hh_2b2t"),
  ("nof_db_events",         99600),
  ("nof_db_files",          1),
  ("fsize_db",              6975912136),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.98GB; nevents: 99.60k; release: 9_4_9; last modified: 2020-09-15 02:37:59"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-3000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToRadionToHHTo2B2Tau_M-3000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asym"),
  ("sample_category",       "signal_vbf_spin0_3000_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_3000_hh_2b2t"),
  ("nof_db_events",         99600),
  ("nof_db_files",          3),
  ("fsize_db",              7186439272),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 7.19GB; nevents: 99.60k; release: 9_4_9; last modified: 2020-09-16 03:08:21"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToBulkGravitonToHHTo2B2Tau_M-250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2"),
  ("sample_category",       "signal_vbf_spin2_250_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_250_hh_2b2t"),
  ("nof_db_events",         399300),
  ("nof_db_files",          5),
  ("fsize_db",              21665085461),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.67GB; nevents: 399.30k; release: 9_4_9; last modified: 2020-09-16 03:09:46"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-260_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToBulkGravitonToHHTo2B2Tau_M-260_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2"),
  ("sample_category",       "signal_vbf_spin2_260_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_260_hh_2b2t"),
  ("nof_db_events",         399000),
  ("nof_db_files",          6),
  ("fsize_db",              19965168763),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 19.97GB; nevents: 399.00k; release: 9_4_9; last modified: 2020-09-16 06:03:20"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-270_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToBulkGravitonToHHTo2B2Tau_M-270_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2"),
  ("sample_category",       "signal_vbf_spin2_270_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_270_hh_2b2t"),
  ("nof_db_events",         399100),
  ("nof_db_files",          7),
  ("fsize_db",              19965470447),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 19.97GB; nevents: 399.10k; release: 9_4_9; last modified: 2020-09-16 03:02:47"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-280_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToBulkGravitonToHHTo2B2Tau_M-280_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2"),
  ("sample_category",       "signal_vbf_spin2_280_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_280_hh_2b2t"),
  ("nof_db_events",         399200),
  ("nof_db_files",          6),
  ("fsize_db",              19918920031),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 19.92GB; nevents: 399.20k; release: 9_4_9; last modified: 2020-09-18 00:11:52"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-300_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToBulkGravitonToHHTo2B2Tau_M-300_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2"),
  ("sample_category",       "signal_vbf_spin2_300_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_300_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          5),
  ("fsize_db",              14933126905),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.93GB; nevents: 300.00k; release: 9_4_9; last modified: 2020-09-16 02:58:52"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-320_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToBulkGravitonToHHTo2B2Tau_M-320_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2"),
  ("sample_category",       "signal_vbf_spin2_320_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_320_hh_2b2t"),
  ("nof_db_events",         299000),
  ("nof_db_files",          5),
  ("fsize_db",              14844734816),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.84GB; nevents: 299.00k; release: 9_4_9; last modified: 2020-09-16 03:05:11"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-350_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToBulkGravitonToHHTo2B2Tau_M-350_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2"),
  ("sample_category",       "signal_vbf_spin2_350_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_350_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          7),
  ("fsize_db",              14849340648),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.85GB; nevents: 300.00k; release: 9_4_9; last modified: 2020-10-10 11:50:52"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-400_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToBulkGravitonToHHTo2B2Tau_M-400_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2"),
  ("sample_category",       "signal_vbf_spin2_400_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_400_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          3),
  ("fsize_db",              14759908108),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.76GB; nevents: 300.00k; release: 9_4_9; last modified: 2020-09-13 22:04:32"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-450_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToBulkGravitonToHHTo2B2Tau_M-450_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2"),
  ("sample_category",       "signal_vbf_spin2_450_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_450_hh_2b2t"),
  ("nof_db_events",         295800),
  ("nof_db_files",          3),
  ("fsize_db",              14543528828),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.54GB; nevents: 295.80k; release: 9_4_9; last modified: 2020-09-14 10:07:45"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToBulkGravitonToHHTo2B2Tau_M-500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2"),
  ("sample_category",       "signal_vbf_spin2_500_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_500_hh_2b2t"),
  ("nof_db_events",         299100),
  ("nof_db_files",          5),
  ("fsize_db",              14761989473),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.76GB; nevents: 299.10k; release: 9_4_9; last modified: 2020-09-16 03:12:32"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-600_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToBulkGravitonToHHTo2B2Tau_M-600_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2"),
  ("sample_category",       "signal_vbf_spin2_600_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_600_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          4),
  ("fsize_db",              9898141934),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 9.90GB; nevents: 200.00k; release: 9_4_9; last modified: 2020-09-16 03:01:32"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-650_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToBulkGravitonToHHTo2B2Tau_M-650_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2"),
  ("sample_category",       "signal_vbf_spin2_650_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_650_hh_2b2t"),
  ("nof_db_events",         197300),
  ("nof_db_files",          3),
  ("fsize_db",              9750259439),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 9.75GB; nevents: 197.30k; release: 9_4_9; last modified: 2020-09-14 06:45:58"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-700_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToBulkGravitonToHHTo2B2Tau_M-700_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2"),
  ("sample_category",       "signal_vbf_spin2_700_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_700_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          5),
  ("fsize_db",              9931172424),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 9.93GB; nevents: 200.00k; release: 9_4_9; last modified: 2020-09-16 02:59:22"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct17_VBFToBulkGravitonToHHTo2B2Tau_M-750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2"),
  ("sample_category",       "signal_vbf_spin2_750_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_750_hh_2b2t"),
  ("nof_db_events",         198000),
  ("nof_db_files",          5),
  ("fsize_db",              9850444030),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 9.85GB; nevents: 198.00k; release: 9_4_9; last modified: 2020-09-15 22:00:25"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-850_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToBulkGravitonToHHTo2B2Tau_M-850_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2"),
  ("sample_category",       "signal_vbf_spin2_850_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_850_hh_2b2t"),
  ("nof_db_events",         197200),
  ("nof_db_files",          5),
  ("fsize_db",              9850192498),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 9.85GB; nevents: 197.20k; release: 9_4_9; last modified: 2020-09-15 22:03:30"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-900_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToBulkGravitonToHHTo2B2Tau_M-900_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2"),
  ("sample_category",       "signal_vbf_spin2_900_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_900_hh_2b2t"),
  ("nof_db_events",         199100),
  ("nof_db_files",          4),
  ("fsize_db",              9914302589),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 9.91GB; nevents: 199.10k; release: 9_4_9; last modified: 2020-09-16 13:48:54"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-1000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToBulkGravitonToHHTo2B2Tau_M-1000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun"),
  ("sample_category",       "signal_vbf_spin2_1000_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_1000_hh_2b2t"),
  ("nof_db_events",         99200),
  ("nof_db_files",          3),
  ("fsize_db",              4992199922),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 4.99GB; nevents: 99.20k; release: 9_4_9; last modified: 2020-09-16 03:11:41"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-1200_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToBulkGravitonToHHTo2B2Tau_M-1200_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun"),
  ("sample_category",       "signal_vbf_spin2_1200_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_1200_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          3),
  ("fsize_db",              5054132277),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 5.05GB; nevents: 100.00k; release: 9_4_9; last modified: 2020-09-14 19:08:50"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-1750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToBulkGravitonToHHTo2B2Tau_M-1750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun"),
  ("sample_category",       "signal_vbf_spin2_1750_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_1750_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          3),
  ("fsize_db",              5078291014),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 5.08GB; nevents: 100.00k; release: 9_4_9; last modified: 2020-09-15 14:36:31"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-2000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFToBulkGravitonToHHTo2B2Tau_M-2000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun"),
  ("sample_category",       "signal_vbf_spin2_2000_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_2000_hh_2b2t"),
  ("nof_db_events",         99300),
  ("nof_db_files",          3),
  ("fsize_db",              5051593636),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 5.05GB; nevents: 99.30k; release: 9_4_9; last modified: 2020-09-16 03:00:37"),
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

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-700_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToRadionToHHTo2B2Tau_M-700_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_as"),
  ("sample_category",       "signal_ggf_spin0_700_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_700_hh_2b2t"),
  ("nof_db_events",         199000),
  ("nof_db_files",          3),
  ("fsize_db",              9589956271),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 9.59GB; nevents: 199.00k; release: 9_4_9; last modified: 2020-09-14 06:47:54"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToRadionToHHTo2B2Tau_M-750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_as"),
  ("sample_category",       "signal_ggf_spin0_750_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_750_hh_2b2t"),
  ("nof_db_events",         198200),
  ("nof_db_files",          4),
  ("fsize_db",              9653223921),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 9.65GB; nevents: 198.20k; release: 9_4_9; last modified: 2020-09-16 02:58:12"),
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

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-850_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToRadionToHHTo2B2Tau_M-850_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_as"),
  ("sample_category",       "signal_ggf_spin0_850_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_850_hh_2b2t"),
  ("nof_db_events",         199100),
  ("nof_db_files",          6),
  ("fsize_db",              9884082889),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 9.88GB; nevents: 199.10k; release: 9_4_9; last modified: 2020-09-15 22:02:31"),
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

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-900_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToRadionToHHTo2B2Tau_M-900_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_as"),
  ("sample_category",       "signal_ggf_spin0_900_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_900_hh_2b2t_PSWeights"),
  ("nof_db_events",         200000),
  ("nof_db_files",          5),
  ("fsize_db",              9988346129),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 9.99GB; nevents: 200.00k; release: 9_4_9; last modified: 2020-09-15 02:40:20"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-1000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToRadionToHHTo2B2Tau_M-1000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_a"),
  ("sample_category",       "signal_ggf_spin0_1000_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_1000_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          3),
  ("fsize_db",              5075552784),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 5.08GB; nevents: 100.00k; release: 9_4_9; last modified: 2020-09-16 05:59:34"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-1250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToRadionToHHTo2B2Tau_M-1250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_a"),
  ("sample_category",       "signal_ggf_spin0_1250_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_1250_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          1),
  ("fsize_db",              5140097093),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 5.14GB; nevents: 100.00k; release: 9_4_9; last modified: 2020-09-14 15:59:44"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-1500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToRadionToHHTo2B2Tau_M-1500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_a"),
  ("sample_category",       "signal_ggf_spin0_1500_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_1500_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          3),
  ("fsize_db",              5315508364),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 5.32GB; nevents: 100.00k; release: 9_4_9; last modified: 2020-09-15 21:52:40"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-1750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToRadionToHHTo2B2Tau_M-1750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_a"),
  ("sample_category",       "signal_ggf_spin0_1750_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_1750_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          1),
  ("fsize_db",              5358389208),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 5.36GB; nevents: 100.00k; release: 9_4_9; last modified: 2020-09-16 03:04:36"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-2000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToRadionToHHTo2B2Tau_M-2000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_a"),
  ("sample_category",       "signal_ggf_spin0_2000_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_2000_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          2),
  ("fsize_db",              5409168825),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 5.41GB; nevents: 100.00k; release: 9_4_9; last modified: 2020-09-13 20:45:07"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-2500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToRadionToHHTo2B2Tau_M-2500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_a"),
  ("sample_category",       "signal_ggf_spin0_2500_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_2500_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          1),
  ("fsize_db",              5464121471),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 5.46GB; nevents: 100.00k; release: 9_4_9; last modified: 2020-09-13 14:43:38"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-3000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToRadionToHHTo2B2Tau_M-3000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_a"),
  ("sample_category",       "signal_ggf_spin0_3000_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_3000_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          3),
  ("fsize_db",              5545454639),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 5.55GB; nevents: 100.00k; release: 9_4_9; last modified: 2020-09-16 03:07:17"),
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

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-700_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToBulkGravitonToHHTo2B2Tau_M-700_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcR"),
  ("sample_category",       "signal_ggf_spin2_700_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_700_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          4),
  ("fsize_db",              10228456255),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 10.23GB; nevents: 200.00k; release: 9_4_9; last modified: 2020-09-16 03:12:27"),
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

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-850_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToBulkGravitonToHHTo2B2Tau_M-850_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcR"),
  ("sample_category",       "signal_ggf_spin2_850_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_850_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          4),
  ("fsize_db",              10438711009),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 10.44GB; nevents: 200.00k; release: 9_4_9; last modified: 2020-09-15 21:57:20"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-900_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToBulkGravitonToHHTo2B2Tau_M-900_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcR"),
  ("sample_category",       "signal_ggf_spin2_900_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_900_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          4),
  ("fsize_db",              10490939882),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 10.49GB; nevents: 200.00k; release: 9_4_9; last modified: 2020-09-16 03:02:02"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-1000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToBulkGravitonToHHTo2B2Tau_M-1000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mc"),
  ("sample_category",       "signal_ggf_spin2_1000_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_1000_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          3),
  ("fsize_db",              5306653973),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 5.31GB; nevents: 100.00k; release: 9_4_9; last modified: 2020-09-14 19:05:40"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-1250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToBulkGravitonToHHTo2B2Tau_M-1250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mc"),
  ("sample_category",       "signal_ggf_spin2_1250_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_1250_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          3),
  ("fsize_db",              5407629175),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 5.41GB; nevents: 100.00k; release: 9_4_9; last modified: 2020-09-16 20:01:01"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-1500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToBulkGravitonToHHTo2B2Tau_M-1500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mc"),
  ("sample_category",       "signal_ggf_spin2_1500_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_1500_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          1),
  ("fsize_db",              5408366589),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 5.41GB; nevents: 100.00k; release: 9_4_9; last modified: 2020-09-13 16:00:13"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-1750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToBulkGravitonToHHTo2B2Tau_M-1750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mc"),
  ("sample_category",       "signal_ggf_spin2_1750_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_1750_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          1),
  ("fsize_db",              5424783618),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 5.42GB; nevents: 100.00k; release: 9_4_9; last modified: 2020-09-14 22:10:40"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-2000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToBulkGravitonToHHTo2B2Tau_M-2000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mc"),
  ("sample_category",       "signal_ggf_spin2_2000_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_2000_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          1),
  ("fsize_db",              5460445376),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 5.46GB; nevents: 100.00k; release: 9_4_9; last modified: 2020-09-13 12:41:16"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-2500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToBulkGravitonToHHTo2B2Tau_M-2500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mc"),
  ("sample_category",       "signal_ggf_spin2_2500_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_2500_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          3),
  ("fsize_db",              5576170410),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 5.58GB; nevents: 100.00k; release: 9_4_9; last modified: 2020-09-16 13:39:39"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-3000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToBulkGravitonToHHTo2B2Tau_M-3000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mc"),
  ("sample_category",       "signal_ggf_spin2_3000_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_3000_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          1),
  ("fsize_db",              5581992893),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 5.58GB; nevents: 100.00k; release: 9_4_9; last modified: 2020-09-13 12:43:54"),
])

meta_dictionary["/VBFHHTo2B2Tau_CV_1_C2V_1_C3_0_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFHHTo2B2Tau_CV_1_C2V_1_C3_0_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcR"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_0_hh_bbtt"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_0_hh_2b2t_dipoleRecoilOff"),
  ("nof_db_events",         993600),
  ("nof_db_files",          39),
  ("fsize_db",              45541341311),
  ("xsection",              0.000335439),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 45.54GB; nevents: 993.60k; release: 9_4_9; last modified: 2020-09-28 00:11:05"),
])

meta_dictionary["/VBFHHTo2B2Tau_CV_1_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFHHTo2B2Tau_CV_1_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcR"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_1_hh_bbtt"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_1_hh_2b2t_dipoleRecoilOff"),
  ("nof_db_events",         1996000),
  ("nof_db_files",          17),
  ("fsize_db",              90436757989),
  ("xsection",              0.00025219),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 90.44GB; nevents: 2.00M; release: 9_4_9; last modified: 2020-09-13 22:01:47"),
])

meta_dictionary["/VBFHHTo2B2Tau_CV_1_C2V_1_C3_2_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFHHTo2B2Tau_CV_1_C2V_1_C3_2_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcR"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_2_hh_bbtt"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_2_hh_2b2t_dipoleRecoilOff"),
  ("nof_db_events",         998000),
  ("nof_db_files",          9),
  ("fsize_db",              46741447242),
  ("xsection",              0.000104517),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 46.74GB; nevents: 998.00k; release: 9_4_9; last modified: 2020-09-14 17:42:45"),
])

meta_dictionary["/VBFHHTo2B2Tau_CV_1_C2V_2_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFHHTo2B2Tau_CV_1_C2V_2_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcR"),
  ("sample_category",       "signal_vbf_nonresonant_1_2_1_hh_bbtt"),
  ("process_name_specific", "signal_vbf_nonresonant_1_2_1_hh_2b2t_dipoleRecoilOff"),
  ("nof_db_events",         1996000),
  ("nof_db_files",          19),
  ("fsize_db",              99308407017),
  ("xsection",              0.001051448),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 99.31GB; nevents: 2.00M; release: 9_4_9; last modified: 2020-09-14 02:45:53"),
])

meta_dictionary["/VBFHHTo2B2Tau_CV_1_5_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFHHTo2B2Tau_CV_1_5_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_m"),
  ("sample_category",       "signal_vbf_nonresonant_1p5_1_1_hh_bbtt"),
  ("process_name_specific", "signal_vbf_nonresonant_1p5_1_1_hh_2b2t_dipoleRecoilOff"),
  ("nof_db_events",         995500),
  ("nof_db_files",          11),
  ("fsize_db",              47063460066),
  ("xsection",              0.004846112),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 47.06GB; nevents: 995.50k; release: 9_4_9; last modified: 2020-09-13 19:06:22"),
])

meta_dictionary["/VBFHHTo2B2Tau_CV_0_5_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFHHTo2B2Tau_CV_0_5_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_m"),
  ("sample_category",       "signal_vbf_nonresonant_0p5_1_1_hh_bbtt"),
  ("process_name_specific", "signal_vbf_nonresonant_0p5_1_1_hh_2b2t_dipoleRecoilOff"),
  ("nof_db_events",         999000),
  ("nof_db_files",          17),
  ("fsize_db",              49082808579),
  ("xsection",              0.000794692),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 49.08GB; nevents: 999.00k; release: 9_4_9; last modified: 2020-09-14 22:09:25"),
])

meta_dictionary["/VBFHHTo2B2Tau_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFHHTo2B2Tau_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcR/201011_182949"),
  ("sample_category",       "signal_vbf_nonresonant_1_0_1_hh_bbtt"),
  ("process_name_specific", "signal_vbf_nonresonant_1_0_1_hh_2b2t_dipoleRecoilOff"),
  ("nof_db_events",         1998600),
  ("nof_db_files",          19),
  ("fsize_db",              95935612009),
  ("xsection",              0.00198948),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 95.94GB; nevents: 2.00M; release: 9_4_9; last modified: 2020-09-14 08:45:18"),
])

meta_dictionary["/VBFHHTo2B2Tau_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_VBFHHTo2B2Tau_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcR/201011_183101"),
  ("sample_category",       "signal_vbf_nonresonant_1_0_1_hh_bbtt"),
  ("process_name_specific", "signal_vbf_nonresonant_1_0_1_hh_2b2t_dipoleRecoilOff_ext1"),
  ("nof_db_events",         496500),
  ("nof_db_files",          27),
  ("fsize_db",              24277893809),
  ("xsection",              0.00198948),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 24.28GB; nevents: 496.50k; release: 9_4_9; last modified: 2020-08-17 17:16:10"),
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

meta_dictionary["/GluGluToHHTo2B2Tau_node_1_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToHHTo2B2Tau_node_1_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_1_hh_2b2t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          7),
  ("fsize_db",              17178531370),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 17.18GB; nevents: 400.00k; release: 9_4_9; last modified: 2020-09-16 03:03:02"),
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

meta_dictionary["/GluGluToHHTo2B2Tau_node_3_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToHHTo2B2Tau_node_3_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_3_hh_2b2t"),
  ("nof_db_events",         396700),
  ("nof_db_files",          6),
  ("fsize_db",              17304942771),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 17.30GB; nevents: 396.70k; release: 9_4_9; last modified: 2020-09-16 03:17:57"),
])

meta_dictionary["/GluGluToHHTo2B2Tau_node_4_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToHHTo2B2Tau_node_4_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_4_hh_2b2t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          6),
  ("fsize_db",              17171599807),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 17.17GB; nevents: 400.00k; release: 9_4_9; last modified: 2020-09-16 03:19:27"),
])

meta_dictionary["/GluGluToHHTo2B2Tau_node_5_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToHHTo2B2Tau_node_5_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_5_hh_2b2t"),
  ("nof_db_events",         394500),
  ("nof_db_files",          6),
  ("fsize_db",              18014461194),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 18.01GB; nevents: 394.50k; release: 9_4_9; last modified: 2020-09-16 03:15:17"),
])

meta_dictionary["/GluGluToHHTo2B2Tau_node_6_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct31_GluGluToHHTo2B2Tau_node_6_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_6_hh_2b2t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          7),
  ("fsize_db",              17277119464),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 17.28GB; nevents: 400.00k; release: 9_4_9; last modified: 2020-10-26 01:22:16"),
])

meta_dictionary["/GluGluToHHTo2B2Tau_node_7_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToHHTo2B2Tau_node_7_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_7_hh_2b2t"),
  ("nof_db_events",         397000),
  ("nof_db_files",          5),
  ("fsize_db",              17033242389),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 17.03GB; nevents: 397.00k; release: 9_4_9; last modified: 2020-09-16 16:54:00"),
])

meta_dictionary["/GluGluToHHTo2B2Tau_node_8_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToHHTo2B2Tau_node_8_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_8_hh_2b2t"),
  ("nof_db_events",         398900),
  ("nof_db_files",          5),
  ("fsize_db",              16954806742),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.95GB; nevents: 398.90k; release: 9_4_9; last modified: 2020-09-16 03:07:21"),
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

meta_dictionary["/GluGluToHHTo2B2Tau_node_cHHH0_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToHHTo2B2Tau_node_cHHH0_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-"),
  ("sample_category",       "signal_ggf_nonresonant_cHHH0_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_cHHH0_hh_2b2t"),
  ("nof_db_events",         947200),
  ("nof_db_files",          33),
  ("fsize_db",              38664951189),
  ("xsection",              0.00509388),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 38.66GB; nevents: 947.20k; release: 9_4_9; last modified: 2020-09-03 07:12:54"),
])

meta_dictionary["/GluGluToHHTo2B2Tau_node_cHHH1_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct11_GluGluToHHTo2B2Tau_node_cHHH1_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-"),
  ("sample_category",       "signal_ggf_nonresonant_cHHH1_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_cHHH1_hh_2b2t"),
  ("nof_db_events",         999400),
  ("nof_db_files",          29),
  ("fsize_db",              41235766334),
  ("xsection",              0.00226819),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 41.24GB; nevents: 999.40k; release: 9_4_9; last modified: 2020-08-29 10:23:02"),
])

meta_dictionary["/GluGluToHHTo2B2Tau_node_cHHH2p45_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct19_GluGluToHHTo2B2Tau_node_cHHH2p45_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_"),
  ("sample_category",       "signal_ggf_nonresonant_cHHH2p45_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_cHHH2p45_hh_2b2t"),
  ("nof_db_events",         951000),
  ("nof_db_files",          31),
  ("fsize_db",              39424683698),
  ("xsection",              0.00095876),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 39.42GB; nevents: 951.00k; release: 9_4_9; last modified: 2020-08-29 10:22:50"),
])

meta_dictionary["/GluGluToHHTo2B2Tau_node_cHHH5_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Oct17_GluGluToHHTo2B2Tau_node_cHHH5_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-"),
  ("sample_category",       "signal_ggf_nonresonant_cHHH5_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_cHHH5_hh_2b2t"),
  ("nof_db_events",         984200),
  ("nof_db_files",          28),
  ("fsize_db",              38800257105),
  ("xsection",              0.00666064),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 38.80GB; nevents: 984.20k; release: 9_4_9; last modified: 2020-08-22 05:08:29"),
])


# event statistics by sample category:
# signal_ggf_spin0_260_hh_bbvv:               300.00k
# signal_ggf_spin0_270_hh_bbvv:               294.63k
# signal_ggf_spin0_300_hh_bbvv:               300.00k
# signal_ggf_spin0_350_hh_bbvv:               295.15k
# signal_ggf_spin0_400_hh_bbvv:               300.00k
# signal_ggf_spin0_450_hh_bbvv:               296.26k
# signal_ggf_spin0_500_hh_bbvv:               300.00k
# signal_ggf_spin0_550_hh_bbvv:               300.00k
# signal_ggf_spin0_600_hh_bbvv:               300.00k
# signal_ggf_spin0_650_hh_bbvv:               299.54k
# signal_ggf_spin0_750_hh_bbvv:               298.73k
# signal_ggf_spin0_800_hh_bbvv:               299.70k
# signal_ggf_spin0_900_hh_bbvv:               298.73k
# signal_ggf_spin0_1000_hh_bbvv:              300.00k
# signal_ggf_spin2_260_hh_bbvv:               300.00k
# signal_ggf_spin2_270_hh_bbvv:               300.00k
# signal_ggf_spin2_300_hh_bbvv:               300.00k
# signal_ggf_spin2_350_hh_bbvv:               300.00k
# signal_ggf_spin2_400_hh_bbvv:               300.00k
# signal_ggf_spin2_450_hh_bbvv:               300.00k
# signal_ggf_spin2_500_hh_bbvv:               300.00k
# signal_ggf_spin2_550_hh_bbvv:               300.00k
# signal_ggf_spin2_600_hh_bbvv:               300.00k
# signal_ggf_spin2_650_hh_bbvv:               298.81k
# signal_ggf_spin2_700_hh_bbvv:               300.00k
# signal_ggf_spin2_800_hh_bbvv:               300.00k
# signal_ggf_spin2_900_hh_bbvv:               300.00k
# signal_ggf_spin2_1000_hh_bbvv:              299.12k
# signal_vbf_nonresonant_1_1_1_hh_bbvv:       399.00k
# signal_vbf_nonresonant_1_1_2_hh_bbvv:       396.80k
# signal_vbf_nonresonant_1_2_1_hh_bbvv:       399.20k
# signal_vbf_nonresonant_1_1_0_hh_bbvv:       400.00k
# signal_vbf_nonresonant_1p5_1_1_hh_bbvv:     398.80k
# signal_vbf_nonresonant_0p5_1_1_hh_bbvv:     399.10k
# signal_vbf_nonresonant_1_0_1_hh_bbvv:       396.80k
# signal_ggf_nonresonant_hh_bbvv:             4.20M
# signal_ggf_nonresonant_cHHH0_hh_bbvv:       400.00k
# signal_ggf_nonresonant_cHHH1_hh_bbvv:       396.80k
# signal_ggf_nonresonant_cHHH2p45_hh_bbvv:    398.40k
# signal_ggf_nonresonant_cHHH5_hh_bbvv:       394.80k
# signal_ggf_nonresonant_hh_bbvv_sl:          3.87M
# signal_ggf_nonresonant_cHHH0_hh_bbvv_sl:    398.39k
# signal_ggf_nonresonant_cHHH1_hh_bbvv_sl:    399.00k
# signal_ggf_nonresonant_cHHH2p45_hh_bbvv_sl: 391.39k
# signal_ggf_nonresonant_cHHH5_hh_bbvv_sl:    396.60k
# signal_ggf_spin0_250_hh_bbvv_sl:            300.00k
# signal_ggf_spin0_260_hh_bbvv_sl:            299.40k
# signal_ggf_spin0_270_hh_bbvv_sl:            300.00k
# signal_ggf_spin0_300_hh_bbvv_sl:            300.00k
# signal_ggf_spin0_350_hh_bbvv_sl:            300.00k
# signal_ggf_spin0_400_hh_bbvv_sl:            300.00k
# signal_ggf_spin0_450_hh_bbvv_sl:            292.03k
# signal_ggf_spin0_500_hh_bbvv_sl:            300.00k
# signal_ggf_spin0_550_hh_bbvv_sl:            300.00k
# signal_ggf_spin0_600_hh_bbvv_sl:            300.00k
# signal_ggf_spin0_650_hh_bbvv_sl:            300.00k
# signal_ggf_spin0_700_hh_bbvv_sl:            300.00k
# signal_ggf_spin0_800_hh_bbvv_sl:            300.00k
# signal_ggf_spin0_900_hh_bbvv_sl:            300.00k
# signal_ggf_spin0_1000_hh_bbvv_sl:           299.47k
# signal_ggf_spin2_250_hh_bbvv_sl:            300.00k
# signal_ggf_spin2_260_hh_bbvv_sl:            300.00k
# signal_ggf_spin2_270_hh_bbvv_sl:            299.23k
# signal_ggf_spin2_300_hh_bbvv_sl:            300.00k
# signal_ggf_spin2_350_hh_bbvv_sl:            299.40k
# signal_ggf_spin2_400_hh_bbvv_sl:            299.99k
# signal_ggf_spin2_450_hh_bbvv_sl:            300.00k
# signal_ggf_spin2_500_hh_bbvv_sl:            300.00k
# signal_ggf_spin2_550_hh_bbvv_sl:            300.00k
# signal_ggf_spin2_600_hh_bbvv_sl:            300.00k
# signal_ggf_spin2_650_hh_bbvv_sl:            300.00k
# signal_ggf_spin2_700_hh_bbvv_sl:            300.00k
# signal_ggf_spin2_800_hh_bbvv_sl:            300.00k
# signal_ggf_spin2_900_hh_bbvv_sl:            300.00k
# signal_ggf_spin2_1000_hh_bbvv_sl:           300.00k
# signal_vbf_nonresonant_1_1_0_hh_bbvv_sl:    399.00k
# signal_vbf_nonresonant_1_1_1_hh_bbvv_sl:    400.00k
# signal_vbf_nonresonant_1_1_2_hh_bbvv_sl:    395.49k
# signal_vbf_nonresonant_1_2_1_hh_bbvv_sl:    398.19k
# signal_vbf_nonresonant_0p5_1_1_hh_bbvv_sl:  399.99k
# signal_vbf_nonresonant_1p5_1_1_hh_bbvv_sl:  395.49k
# signal_vbf_nonresonant_1_0_1_hh_bbvv_sl:    399.10k
# signal_vbf_spin0_250_hh_bbtt:               399.20k
# signal_vbf_spin0_260_hh_bbtt:               395.00k
# signal_vbf_spin0_270_hh_bbtt:               395.70k
# signal_vbf_spin0_280_hh_bbtt:               396.40k
# signal_vbf_spin0_300_hh_bbtt:               300.00k
# signal_vbf_spin0_320_hh_bbtt:               299.20k
# signal_vbf_spin0_350_hh_bbtt:               298.00k
# signal_vbf_spin0_400_hh_bbtt:               298.40k
# signal_vbf_spin0_450_hh_bbtt:               298.40k
# signal_vbf_spin0_500_hh_bbtt:               300.00k
# signal_vbf_spin0_550_hh_bbtt:               299.30k
# signal_vbf_spin0_600_hh_bbtt:               200.00k
# signal_vbf_spin0_650_hh_bbtt:               200.00k
# signal_vbf_spin0_700_hh_bbtt:               200.00k
# signal_vbf_spin0_750_hh_bbtt:               200.00k
# signal_vbf_spin0_800_hh_bbtt:               199.30k
# signal_vbf_spin0_850_hh_bbtt:               199.40k
# signal_vbf_spin0_900_hh_bbtt:               199.60k
# signal_vbf_spin0_1000_hh_bbtt:              100.00k
# signal_vbf_spin0_1250_hh_bbtt:              100.00k
# signal_vbf_spin0_1500_hh_bbtt:              99.70k
# signal_vbf_spin0_1750_hh_bbtt:              99.50k
# signal_vbf_spin0_2000_hh_bbtt:              99.60k
# signal_vbf_spin0_3000_hh_bbtt:              99.60k
# signal_vbf_spin2_250_hh_bbtt:               399.30k
# signal_vbf_spin2_260_hh_bbtt:               399.00k
# signal_vbf_spin2_270_hh_bbtt:               399.10k
# signal_vbf_spin2_280_hh_bbtt:               399.20k
# signal_vbf_spin2_300_hh_bbtt:               300.00k
# signal_vbf_spin2_320_hh_bbtt:               299.00k
# signal_vbf_spin2_350_hh_bbtt:               300.00k
# signal_vbf_spin2_400_hh_bbtt:               300.00k
# signal_vbf_spin2_450_hh_bbtt:               295.80k
# signal_vbf_spin2_500_hh_bbtt:               299.10k
# signal_vbf_spin2_600_hh_bbtt:               200.00k
# signal_vbf_spin2_650_hh_bbtt:               197.30k
# signal_vbf_spin2_700_hh_bbtt:               200.00k
# signal_vbf_spin2_750_hh_bbtt:               198.00k
# signal_vbf_spin2_850_hh_bbtt:               197.20k
# signal_vbf_spin2_900_hh_bbtt:               199.10k
# signal_vbf_spin2_1000_hh_bbtt:              99.20k
# signal_vbf_spin2_1200_hh_bbtt:              100.00k
# signal_vbf_spin2_1750_hh_bbtt:              100.00k
# signal_vbf_spin2_2000_hh_bbtt:              99.30k
# signal_ggf_spin0_250_hh_bbtt:               50.00k
# signal_ggf_spin0_260_hh_bbtt:               50.00k
# signal_ggf_spin0_270_hh_bbtt:               50.00k
# signal_ggf_spin0_280_hh_bbtt:               49.60k
# signal_ggf_spin0_300_hh_bbtt:               450.00k
# signal_ggf_spin0_320_hh_bbtt:               50.00k
# signal_ggf_spin0_340_hh_bbtt:               48.00k
# signal_ggf_spin0_350_hh_bbtt:               50.00k
# signal_ggf_spin0_400_hh_bbtt:               250.00k
# signal_ggf_spin0_450_hh_bbtt:               99.60k
# signal_ggf_spin0_500_hh_bbtt:               99.20k
# signal_ggf_spin0_550_hh_bbtt:               100.00k
# signal_ggf_spin0_600_hh_bbtt:               100.00k
# signal_ggf_spin0_650_hh_bbtt:               100.00k
# signal_ggf_spin0_700_hh_bbtt:               199.00k
# signal_ggf_spin0_750_hh_bbtt:               198.20k
# signal_ggf_spin0_800_hh_bbtt:               100.00k
# signal_ggf_spin0_850_hh_bbtt:               199.10k
# signal_ggf_spin0_900_hh_bbtt:               300.00k
# signal_ggf_spin0_1000_hh_bbtt:              100.00k
# signal_ggf_spin0_1250_hh_bbtt:              100.00k
# signal_ggf_spin0_1500_hh_bbtt:              100.00k
# signal_ggf_spin0_1750_hh_bbtt:              100.00k
# signal_ggf_spin0_2000_hh_bbtt:              100.00k
# signal_ggf_spin0_2500_hh_bbtt:              100.00k
# signal_ggf_spin0_3000_hh_bbtt:              100.00k
# signal_ggf_spin2_250_hh_bbtt:               50.00k
# signal_ggf_spin2_260_hh_bbtt:               50.00k
# signal_ggf_spin2_270_hh_bbtt:               50.00k
# signal_ggf_spin2_280_hh_bbtt:               50.00k
# signal_ggf_spin2_300_hh_bbtt:               447.40k
# signal_ggf_spin2_320_hh_bbtt:               50.00k
# signal_ggf_spin2_340_hh_bbtt:               50.00k
# signal_ggf_spin2_350_hh_bbtt:               50.00k
# signal_ggf_spin2_400_hh_bbtt:               250.00k
# signal_ggf_spin2_450_hh_bbtt:               100.00k
# signal_ggf_spin2_500_hh_bbtt:               100.00k
# signal_ggf_spin2_550_hh_bbtt:               100.00k
# signal_ggf_spin2_600_hh_bbtt:               100.00k
# signal_ggf_spin2_650_hh_bbtt:               100.00k
# signal_ggf_spin2_700_hh_bbtt:               200.00k
# signal_ggf_spin2_750_hh_bbtt:               100.00k
# signal_ggf_spin2_800_hh_bbtt:               100.00k
# signal_ggf_spin2_850_hh_bbtt:               200.00k
# signal_ggf_spin2_900_hh_bbtt:               200.00k
# signal_ggf_spin2_1000_hh_bbtt:              100.00k
# signal_ggf_spin2_1250_hh_bbtt:              100.00k
# signal_ggf_spin2_1500_hh_bbtt:              100.00k
# signal_ggf_spin2_1750_hh_bbtt:              100.00k
# signal_ggf_spin2_2000_hh_bbtt:              100.00k
# signal_ggf_spin2_2500_hh_bbtt:              100.00k
# signal_ggf_spin2_3000_hh_bbtt:              100.00k
# signal_vbf_nonresonant_1_1_0_hh_bbtt:       993.60k
# signal_vbf_nonresonant_1_1_1_hh_bbtt:       2.00M
# signal_vbf_nonresonant_1_1_2_hh_bbtt:       998.00k
# signal_vbf_nonresonant_1_2_1_hh_bbtt:       2.00M
# signal_vbf_nonresonant_1p5_1_1_hh_bbtt:     995.50k
# signal_vbf_nonresonant_0p5_1_1_hh_bbtt:     999.00k
# signal_vbf_nonresonant_1_0_1_hh_bbtt:       2.50M
# signal_ggf_nonresonant_hh_bbtt:             5.15M
# signal_ggf_nonresonant_cHHH0_hh_bbtt:       947.20k
# signal_ggf_nonresonant_cHHH1_hh_bbtt:       999.40k
# signal_ggf_nonresonant_cHHH2p45_hh_bbtt:    951.00k
# signal_ggf_nonresonant_cHHH5_hh_bbtt:       984.20k

