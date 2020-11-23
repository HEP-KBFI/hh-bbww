from collections import OrderedDict as OD

# file generated at 2020-11-22 14:07:28 with the following command:
# find_samples.py -V -i ../../tthAnalysis/NanoAOD/test/datasets/txt/datasets_hh_bbww_mc_2018_RunIIAutumn18MiniAOD.txt -m python/samples/metaDict_2018_hh.py -s ../../tthAnalysis/NanoAOD/test/datasets/txt/sum_datasets_hh_bbww_2018_RunIIAutumn18MiniAOD.txt -c python/samples/sampleLocations_2018_nanoAOD_hh_bbww.txt

meta_dictionary = OD()


### event sums

sum_events = { 
  ("signal_vbf_nonresonant_1_0_1_hh_2b2t_dipoleRecoilOff", "signal_vbf_nonresonant_1_0_1_hh_2b2t_dipoleRecoilOff_ext1"),
  ("signal_ggf_nonresonant_node_sm_hh_2b2v", "signal_ggf_nonresonant_node_1_hh_2b2v", "signal_ggf_nonresonant_node_2_hh_2b2v", "signal_ggf_nonresonant_node_3_hh_2b2v", "signal_ggf_nonresonant_node_4_hh_2b2v", "signal_ggf_nonresonant_node_5_hh_2b2v", "signal_ggf_nonresonant_node_6_hh_2b2v", "signal_ggf_nonresonant_node_7_hh_2b2v", "signal_ggf_nonresonant_node_8_hh_2b2v", "signal_ggf_nonresonant_node_9_hh_2b2v", "signal_ggf_nonresonant_node_10_hh_2b2v", "signal_ggf_nonresonant_node_11_hh_2b2v", "signal_ggf_nonresonant_node_12_hh_2b2v"),
  ("signal_ggf_nonresonant_node_sm_hh_2b2v_sl", "signal_ggf_nonresonant_node_2_hh_2b2v_sl", "signal_ggf_nonresonant_node_3_hh_2b2v_sl", "signal_ggf_nonresonant_node_4_hh_2b2v_sl", "signal_ggf_nonresonant_node_5_hh_2b2v_sl", "signal_ggf_nonresonant_node_6_hh_2b2v_sl", "signal_ggf_nonresonant_node_7_hh_2b2v_sl", "signal_ggf_nonresonant_node_8_hh_2b2v_sl", "signal_ggf_nonresonant_node_9_hh_2b2v_sl", "signal_ggf_nonresonant_node_10_hh_2b2v_sl", "signal_ggf_nonresonant_node_11_hh_2b2v_sl", "signal_ggf_nonresonant_node_12_hh_2b2v_sl"),
  ("signal_ggf_nonresonant_node_sm_hh_2b2t", "signal_ggf_nonresonant_node_2_hh_2b2t", "signal_ggf_nonresonant_node_3_hh_2b2t", "signal_ggf_nonresonant_node_4_hh_2b2t", "signal_ggf_nonresonant_node_5_hh_2b2t", "signal_ggf_nonresonant_node_6_hh_2b2t", "signal_ggf_nonresonant_node_7_hh_2b2t", "signal_ggf_nonresonant_node_8_hh_2b2t", "signal_ggf_nonresonant_node_9_hh_2b2t", "signal_ggf_nonresonant_node_10_hh_2b2t", "signal_ggf_nonresonant_node_11_hh_2b2t", "signal_ggf_nonresonant_node_12_hh_2b2t"),
}


meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2VTo2L2Nu_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_250_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_250_hh_2b2v"),
  ("nof_db_events",         400000),
  ("nof_db_files",          17),
  ("fsize_db",              21769417420),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.77GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-16 03:00:22"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2VTo2L2Nu_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_260_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_260_hh_2b2v"),
  ("nof_db_events",         399997),
  ("nof_db_files",          14),
  ("fsize_db",              20956744775),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.96GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-14 14:47:05"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2VTo2L2Nu_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_270_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_270_hh_2b2v"),
  ("nof_db_events",         399998),
  ("nof_db_files",          17),
  ("fsize_db",              21109891474),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.11GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-12 00:51:04"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2VTo2L2Nu_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_280_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_280_hh_2b2v"),
  ("nof_db_events",         400000),
  ("nof_db_files",          16),
  ("fsize_db",              21992399506),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.99GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-16 03:15:57"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2VTo2L2Nu_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_300_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_300_hh_2b2v"),
  ("nof_db_events",         300000),
  ("nof_db_files",          16),
  ("fsize_db",              16130523073),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.13GB; nevents: 300.00k; release: 10_2_5; last modified: 2020-09-14 11:44:31"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2VTo2L2Nu_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_320_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_320_hh_2b2v"),
  ("nof_db_events",         300000),
  ("nof_db_files",          13),
  ("fsize_db",              16290185653),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.29GB; nevents: 300.00k; release: 10_2_5; last modified: 2020-09-14 04:53:54"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2VTo2L2Nu_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_350_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_350_hh_2b2v"),
  ("nof_db_events",         299999),
  ("nof_db_files",          12),
  ("fsize_db",              16256170207),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.26GB; nevents: 300.00k; release: 10_2_5; last modified: 2020-09-16 03:08:51"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2VTo2L2Nu_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_400_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_400_hh_2b2v"),
  ("nof_db_events",         300000),
  ("nof_db_files",          15),
  ("fsize_db",              17394059503),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 17.39GB; nevents: 300.00k; release: 10_2_5; last modified: 2020-09-12 13:09:03"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2VTo2L2Nu_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_500_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_500_hh_2b2v"),
  ("nof_db_events",         300000),
  ("nof_db_files",          13),
  ("fsize_db",              17471951247),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 17.47GB; nevents: 300.00k; release: 10_2_5; last modified: 2020-09-15 02:42:40"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2VTo2L2Nu_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_550_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_550_hh_2b2v"),
  ("nof_db_events",         300000),
  ("nof_db_files",          8),
  ("fsize_db",              18211430509),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 18.21GB; nevents: 300.00k; release: 10_2_5; last modified: 2020-09-16 05:58:38"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2VTo2L2Nu_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_600_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_600_hh_2b2v"),
  ("nof_db_events",         200000),
  ("nof_db_files",          7),
  ("fsize_db",              12311761166),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.31GB; nevents: 200.00k; release: 10_2_5; last modified: 2020-09-14 08:47:44"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2VTo2L2Nu_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_650_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_650_hh_2b2v"),
  ("nof_db_events",         199999),
  ("nof_db_files",          12),
  ("fsize_db",              12454041911),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.45GB; nevents: 200.00k; release: 10_2_5; last modified: 2020-09-11 04:53:59"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2VTo2L2Nu_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_700_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_700_hh_2b2v"),
  ("nof_db_events",         200000),
  ("nof_db_files",          13),
  ("fsize_db",              12555546335),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.56GB; nevents: 200.00k; release: 10_2_5; last modified: 2020-09-16 03:20:37"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2VTo2L2Nu_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_750_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_750_hh_2b2v"),
  ("nof_db_events",         199999),
  ("nof_db_files",          14),
  ("fsize_db",              13006707251),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.01GB; nevents: 200.00k; release: 10_2_5; last modified: 2020-09-15 22:02:55"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2VTo2L2Nu_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_800_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_800_hh_2b2v"),
  ("nof_db_events",         199998),
  ("nof_db_files",          14),
  ("fsize_db",              13089476147),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.09GB; nevents: 200.00k; release: 10_2_5; last modified: 2020-09-11 22:56:22"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2VTo2L2Nu_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_850_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_850_hh_2b2v"),
  ("nof_db_events",         199997),
  ("nof_db_files",          13),
  ("fsize_db",              13167424036),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.17GB; nevents: 200.00k; release: 10_2_5; last modified: 2020-09-16 06:04:05"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2VTo2L2Nu_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_900_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_900_hh_2b2v"),
  ("nof_db_events",         199999),
  ("nof_db_files",          12),
  ("fsize_db",              12520224790),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.52GB; nevents: 200.00k; release: 10_2_5; last modified: 2020-09-12 06:53:42"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2VTo2L2Nu_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin0_1000_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_1000_hh_2b2v"),
  ("nof_db_events",         99999),
  ("nof_db_files",          9),
  ("fsize_db",              6339783437),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.34GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-09-16 05:59:19"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2VTo2L2Nu_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin0_1250_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_1250_hh_2b2v"),
  ("nof_db_events",         100000),
  ("nof_db_files",          6),
  ("fsize_db",              6214334271),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.21GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-09-14 16:04:09"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2VTo2L2Nu_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin0_1500_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_1500_hh_2b2v"),
  ("nof_db_events",         100000),
  ("nof_db_files",          8),
  ("fsize_db",              6217807927),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.22GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-10-07 13:53:28"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2VTo2L2Nu_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin0_1750_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_1750_hh_2b2v"),
  ("nof_db_events",         100000),
  ("nof_db_files",          9),
  ("fsize_db",              6399858338),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.40GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-09-18 15:36:09"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2VTo2L2Nu_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin0_2000_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_2000_hh_2b2v"),
  ("nof_db_events",         99998),
  ("nof_db_files",          8),
  ("fsize_db",              6250048572),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.25GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-09-16 03:17:12"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2VTo2L2Nu_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin0_2500_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_2500_hh_2b2v"),
  ("nof_db_events",         100000),
  ("nof_db_files",          12),
  ("fsize_db",              6648889879),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.65GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-09-25 07:15:27"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2VTo2L2Nu_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin0_3000_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_3000_hh_2b2v"),
  ("nof_db_events",         100000),
  ("nof_db_files",          10),
  ("fsize_db",              6767988851),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.77GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-10-07 15:53:39"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_ggf_spin2_250_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_250_hh_2b2v"),
  ("nof_db_events",         399998),
  ("nof_db_files",          12),
  ("fsize_db",              21099457960),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.10GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-14 17:42:10"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_ggf_spin2_260_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_260_hh_2b2v"),
  ("nof_db_events",         400000),
  ("nof_db_files",          20),
  ("fsize_db",              21222151277),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.22GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-14 13:04:35"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_ggf_spin2_270_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_270_hh_2b2v"),
  ("nof_db_events",         400000),
  ("nof_db_files",          17),
  ("fsize_db",              21635602520),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.64GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-14 16:00:14"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_ggf_spin2_280_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_280_hh_2b2v"),
  ("nof_db_events",         399998),
  ("nof_db_files",          12),
  ("fsize_db",              21492020096),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.49GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-15 21:54:10"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_ggf_spin2_300_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_300_hh_2b2v"),
  ("nof_db_events",         299999),
  ("nof_db_files",          14),
  ("fsize_db",              16166482441),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.17GB; nevents: 300.00k; release: 10_2_5; last modified: 2020-09-11 22:57:48"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_ggf_spin2_320_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_320_hh_2b2v"),
  ("nof_db_events",         299998),
  ("nof_db_files",          12),
  ("fsize_db",              16707306428),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.71GB; nevents: 300.00k; release: 10_2_5; last modified: 2020-09-16 03:10:16"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_ggf_spin2_350_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_350_hh_2b2v"),
  ("nof_db_events",         300000),
  ("nof_db_files",          12),
  ("fsize_db",              17008053450),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 17.01GB; nevents: 300.00k; release: 10_2_5; last modified: 2020-09-15 02:48:00"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_ggf_spin2_400_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_400_hh_2b2v"),
  ("nof_db_events",         300000),
  ("nof_db_files",          15),
  ("fsize_db",              17452430860),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 17.45GB; nevents: 300.00k; release: 10_2_5; last modified: 2020-09-16 05:56:22"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_ggf_spin2_450_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_450_hh_2b2v"),
  ("nof_db_events",         300000),
  ("nof_db_files",          8),
  ("fsize_db",              18286814735),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 18.29GB; nevents: 300.00k; release: 10_2_5; last modified: 2020-09-16 03:15:47"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_ggf_spin2_500_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_500_hh_2b2v"),
  ("nof_db_events",         299999),
  ("nof_db_files",          10),
  ("fsize_db",              18029238407),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 18.03GB; nevents: 300.00k; release: 10_2_5; last modified: 2020-09-14 23:39:23"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_ggf_spin2_550_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_550_hh_2b2v"),
  ("nof_db_events",         300000),
  ("nof_db_files",          11),
  ("fsize_db",              17868443167),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 17.87GB; nevents: 300.00k; release: 10_2_5; last modified: 2020-09-15 02:38:29"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_ggf_spin2_600_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_600_hh_2b2v"),
  ("nof_db_events",         200000),
  ("nof_db_files",          11),
  ("fsize_db",              12265654789),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.27GB; nevents: 200.00k; release: 10_2_5; last modified: 2020-09-16 03:21:40"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_ggf_spin2_650_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_650_hh_2b2v"),
  ("nof_db_events",         200000),
  ("nof_db_files",          7),
  ("fsize_db",              12362249390),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.36GB; nevents: 200.00k; release: 10_2_5; last modified: 2020-09-16 03:20:52"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_ggf_spin2_700_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_700_hh_2b2v"),
  ("nof_db_events",         200000),
  ("nof_db_files",          10),
  ("fsize_db",              12213272084),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.21GB; nevents: 200.00k; release: 10_2_5; last modified: 2020-09-16 03:03:52"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_ggf_spin2_750_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_750_hh_2b2v"),
  ("nof_db_events",         199999),
  ("nof_db_files",          12),
  ("fsize_db",              12949339827),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.95GB; nevents: 200.00k; release: 10_2_5; last modified: 2020-09-15 21:59:55"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_ggf_spin2_800_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_800_hh_2b2v"),
  ("nof_db_events",         199999),
  ("nof_db_files",          8),
  ("fsize_db",              12584995133),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.58GB; nevents: 200.00k; release: 10_2_5; last modified: 2020-09-16 05:57:07"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_ggf_spin2_850_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_850_hh_2b2v"),
  ("nof_db_events",         197000),
  ("nof_db_files",          7),
  ("fsize_db",              13202094182),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.20GB; nevents: 197.00k; release: 10_2_5; last modified: 2020-09-14 10:07:50"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_ggf_spin2_900_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_900_hh_2b2v"),
  ("nof_db_events",         199999),
  ("nof_db_files",          11),
  ("fsize_db",              13510236979),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.51GB; nevents: 200.00k; release: 10_2_5; last modified: 2020-09-15 02:44:24"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_reali"),
  ("sample_category",       "signal_ggf_spin2_1000_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_1000_hh_2b2v"),
  ("nof_db_events",         90000),
  ("nof_db_files",          2),
  ("fsize_db",              5575990858),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 5.58GB; nevents: 90.00k; release: 10_2_5; last modified: 2020-09-23 10:49:00"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_reali"),
  ("sample_category",       "signal_ggf_spin2_1250_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_1250_hh_2b2v"),
  ("nof_db_events",         100000),
  ("nof_db_files",          5),
  ("fsize_db",              6322077799),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.32GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-09-18 02:47:24"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_reali"),
  ("sample_category",       "signal_ggf_spin2_1500_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_1500_hh_2b2v"),
  ("nof_db_events",         100000),
  ("nof_db_files",          10),
  ("fsize_db",              6498665132),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.50GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-09-16 23:19:05"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_reali"),
  ("sample_category",       "signal_ggf_spin2_1750_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_1750_hh_2b2v"),
  ("nof_db_events",         100000),
  ("nof_db_files",          10),
  ("fsize_db",              7054399734),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 7.05GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-09-14 23:38:38"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_reali"),
  ("sample_category",       "signal_ggf_spin2_2000_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_2000_hh_2b2v"),
  ("nof_db_events",         100000),
  ("nof_db_files",          7),
  ("fsize_db",              6472017019),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.47GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-09-16 03:17:32"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_reali"),
  ("sample_category",       "signal_ggf_spin2_2500_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_2500_hh_2b2v"),
  ("nof_db_events",         99999),
  ("nof_db_files",          7),
  ("fsize_db",              6553856520),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.55GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-09-16 05:57:57"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct31_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_reali"),
  ("sample_category",       "signal_ggf_spin2_3000_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin2_3000_hh_2b2v"),
  ("nof_db_events",         100000),
  ("nof_db_files",          6),
  ("fsize_db",              6743129991),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.74GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-10-26 01:21:21"),
])

meta_dictionary["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_1_hh_bbvv"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_1_hh_2b2v_dipoleRecoilOff"),
  ("nof_db_events",         399998),
  ("nof_db_files",          20),
  ("fsize_db",              23660265098),
  ("xsection",              4.55695e-05),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.66GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-26 05:17:03"),
])

meta_dictionary["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_1_dipoleRecoilOn-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Nov18_VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_1_dipoleRecoilOn-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realist"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_1_hh_bbvv_dipoleRecoilOn"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_1_hh_2b2v_dipoleRecoilOn"),
  ("nof_db_events",         399999),
  ("nof_db_files",          19),
  ("fsize_db",              23019095049),
  ("xsection",              4.55695e-05),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.02GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-28 08:13:36"),
])

meta_dictionary["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_2_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_2_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_2_hh_bbvv"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_2_hh_2b2v_dipoleRecoilOff"),
  ("nof_db_events",         395997),
  ("nof_db_files",          19),
  ("fsize_db",              24106383775),
  ("xsection",              3.75655e-05),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 24.11GB; nevents: 396.00k; release: 10_2_5; last modified: 2020-09-29 06:04:14"),
])

meta_dictionary["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_2_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo2B2VTo2L2Nu_CV_1_C2V_2_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_vbf_nonresonant_1_2_1_hh_bbvv"),
  ("process_name_specific", "signal_vbf_nonresonant_1_2_1_hh_2b2v_dipoleRecoilOff"),
  ("nof_db_events",         400000),
  ("nof_db_files",          21),
  ("fsize_db",              26601674546),
  ("xsection",              0.0003753816),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 26.60GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-25 19:23:49"),
])

meta_dictionary["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_2_C3_1_dipoleRecoilOn-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Nov18_VBFHHTo2B2VTo2L2Nu_CV_1_C2V_2_C3_1_dipoleRecoilOn-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realist"),
  ("sample_category",       "signal_vbf_nonresonant_1_2_1_hh_bbvv_dipoleRecoilOn"),
  ("process_name_specific", "signal_vbf_nonresonant_1_2_1_hh_2b2v_dipoleRecoilOn"),
  ("nof_db_events",         399997),
  ("nof_db_files",          22),
  ("fsize_db",              25257880512),
  ("xsection",              0.0003753816),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 25.26GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-30 05:12:51"),
])

meta_dictionary["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_0_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_0_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_0_hh_bbvv"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_0_hh_2b2v_dipoleRecoilOff"),
  ("nof_db_events",         399999),
  ("nof_db_files",          19),
  ("fsize_db",              23615969861),
  ("xsection",              0.0001216848),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.62GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-29 05:05:19"),
])

meta_dictionary["/VBFHHTo2B2VTo2L2Nu_CV_1_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo2B2VTo2L2Nu_CV_1_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_real"),
  ("sample_category",       "signal_vbf_nonresonant_1p5_1_1_hh_bbvv"),
  ("process_name_specific", "signal_vbf_nonresonant_1p5_1_1_hh_2b2v_dipoleRecoilOff"),
  ("nof_db_events",         399999),
  ("nof_db_files",          10),
  ("fsize_db",              25237710585),
  ("xsection",              0.0017430382),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 25.24GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-23 10:50:45"),
])

meta_dictionary["/VBFHHTo2B2VTo2L2Nu_CV_0_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo2B2VTo2L2Nu_CV_0_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_real"),
  ("sample_category",       "signal_vbf_nonresonant_0p5_1_1_hh_bbvv"),
  ("process_name_specific", "signal_vbf_nonresonant_0p5_1_1_hh_2b2v_dipoleRecoilOff"),
  ("nof_db_events",         399999),
  ("nof_db_files",          10),
  ("fsize_db",              25513228160),
  ("xsection",              0.0002857708),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 25.51GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-25 19:26:19"),
])

meta_dictionary["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo2B2VTo2L2Nu_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_vbf_nonresonant_1_0_1_hh_bbvv"),
  ("process_name_specific", "signal_vbf_nonresonant_1_0_1_hh_2b2v_dipoleRecoilOff"),
  ("nof_db_events",         399999),
  ("nof_db_files",          12),
  ("fsize_db",              25638125950),
  ("xsection",              0.0007149609),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 25.64GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-24 14:21:19"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_SM_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo2B2VTo2L2Nu_node_SM_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_node_sm_hh_2b2v"),
  ("nof_db_events",         399998),
  ("nof_db_files",          15),
  ("fsize_db",              23207192931),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.21GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-16 03:08:56"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo2B2VTo2L2Nu_node_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_node_1_hh_2b2v"),
  ("nof_db_events",         399999),
  ("nof_db_files",          15),
  ("fsize_db",              22964320188),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 22.96GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-13 19:02:37"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_2_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo2B2VTo2L2Nu_node_2_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_node_2_hh_2b2v"),
  ("nof_db_events",         399999),
  ("nof_db_files",          17),
  ("fsize_db",              25245646410),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 25.25GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-16 13:41:39"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_3_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo2B2VTo2L2Nu_node_3_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_node_3_hh_2b2v"),
  ("nof_db_events",         399998),
  ("nof_db_files",          16),
  ("fsize_db",              22826714259),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 22.83GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-16 03:07:01"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_4_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo2B2VTo2L2Nu_node_4_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_node_4_hh_2b2v"),
  ("nof_db_events",         399999),
  ("nof_db_files",          17),
  ("fsize_db",              23101309698),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.10GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-13 12:40:36"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_5_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo2B2VTo2L2Nu_node_5_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_node_5_hh_2b2v"),
  ("nof_db_events",         399997),
  ("nof_db_files",          15),
  ("fsize_db",              23707187679),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.71GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-16 05:58:54"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo2B2VTo2L2Nu_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_node_6_hh_2b2v"),
  ("nof_db_events",         399998),
  ("nof_db_files",          17),
  ("fsize_db",              23050645194),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.05GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-15 02:43:20"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_7_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo2B2VTo2L2Nu_node_7_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_node_7_hh_2b2v"),
  ("nof_db_events",         399997),
  ("nof_db_files",          12),
  ("fsize_db",              23799450196),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.80GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-16 07:35:19"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_8_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo2B2VTo2L2Nu_node_8_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_node_8_hh_2b2v"),
  ("nof_db_events",         399999),
  ("nof_db_files",          17),
  ("fsize_db",              22468004114),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 22.47GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-16 13:47:09"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_9_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo2B2VTo2L2Nu_node_9_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_node_9_hh_2b2v"),
  ("nof_db_events",         399999),
  ("nof_db_files",          21),
  ("fsize_db",              25032953842),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 25.03GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-13 23:38:51"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_10_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo2B2VTo2L2Nu_node_10_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_node_10_hh_2b2v"),
  ("nof_db_events",         400000),
  ("nof_db_files",          16),
  ("fsize_db",              23040806113),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.04GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-14 06:46:19"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_11_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo2B2VTo2L2Nu_node_11_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_node_11_hh_2b2v"),
  ("nof_db_events",         399998),
  ("nof_db_files",          17),
  ("fsize_db",              23065514169),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.07GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-14 08:45:28"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_12_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo2B2VTo2L2Nu_node_12_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_node_12_hh_2b2v"),
  ("nof_db_events",         400000),
  ("nof_db_files",          19),
  ("fsize_db",              23515520244),
  ("xsection",              0.026422),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.52GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-13 22:01:22"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_cHHH0_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo2B2VTo2L2Nu_node_cHHH0_TuneCP5_PSWeights_13TeV-powheg-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_nonresonant_cHHH0_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_cHHH0_hh_2b2v"),
  ("nof_db_events",         383098),
  ("nof_db_files",          23),
  ("fsize_db",              19461973427),
  ("xsection",              0.00176969),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 19.46GB; nevents: 383.10k; release: 10_2_5; last modified: 2020-03-06 14:14:03"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_cHHH1_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo2B2VTo2L2Nu_node_cHHH1_TuneCP5_PSWeights_13TeV-powheg-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_nonresonant_cHHH1_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_cHHH1_hh_2b2v"),
  ("nof_db_events",         399998),
  ("nof_db_files",          27),
  ("fsize_db",              20612880655),
  ("xsection",              0.00078807),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.61GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-03-20 09:46:18"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_cHHH2p45_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo2B2VTo2L2Nu_node_cHHH2p45_TuneCP5_PSWeights_13TeV-powheg-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_nonresonant_cHHH2p45_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_cHHH2p45_hh_2b2v"),
  ("nof_db_events",         399998),
  ("nof_db_files",          17),
  ("fsize_db",              20453536548),
  ("xsection",              0.00033379),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.45GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-02-21 18:54:06"),
])

meta_dictionary["/GluGluToHHTo2B2VTo2L2Nu_node_cHHH5_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo2B2VTo2L2Nu_node_cHHH5_TuneCP5_PSWeights_13TeV-powheg-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_nonresonant_cHHH5_hh_bbvv"),
  ("process_name_specific", "signal_ggf_nonresonant_cHHH5_hh_2b2v"),
  ("nof_db_events",         399999),
  ("nof_db_files",          20),
  ("fsize_db",              19750514425),
  ("xsection",              0.00232827),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 19.75GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-03-14 01:54:05"),
])

meta_dictionary["/GluGluToHHTo2B2WToLNu2J_node_SM_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo2B2WToLNu2J_node_SM_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_node_sm_hh_2b2v_sl"),
  ("nof_db_events",         399993),
  ("nof_db_files",          20),
  ("fsize_db",              23965435053),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.97GB; nevents: 399.99k; release: 10_2_5; last modified: 2020-09-10 05:21:23"),
])

meta_dictionary["/GluGluToHHTo2B2WToLNu2J_node_2_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo2B2WToLNu2J_node_2_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_node_2_hh_2b2v_sl"),
  ("nof_db_events",         396995),
  ("nof_db_files",          22),
  ("fsize_db",              25251888315),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 25.25GB; nevents: 397.00k; release: 10_2_5; last modified: 2020-09-06 05:57:03"),
])

meta_dictionary["/GluGluToHHTo2B2WToLNu2J_node_3_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo2B2WToLNu2J_node_3_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_node_3_hh_2b2v_sl"),
  ("nof_db_events",         393994),
  ("nof_db_files",          23),
  ("fsize_db",              23680187086),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.68GB; nevents: 393.99k; release: 10_2_5; last modified: 2020-09-11 11:00:45"),
])

meta_dictionary["/GluGluToHHTo2B2WToLNu2J_node_4_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo2B2WToLNu2J_node_4_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_node_4_hh_2b2v_sl"),
  ("nof_db_events",         399996),
  ("nof_db_files",          23),
  ("fsize_db",              23798532201),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.80GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-06 05:56:38"),
])

meta_dictionary["/GluGluToHHTo2B2WToLNu2J_node_5_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo2B2WToLNu2J_node_5_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_node_5_hh_2b2v_sl"),
  ("nof_db_events",         399995),
  ("nof_db_files",          19),
  ("fsize_db",              24105158990),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 24.11GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-10 05:22:23"),
])

meta_dictionary["/GluGluToHHTo2B2WToLNu2J_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo2B2WToLNu2J_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_node_6_hh_2b2v_sl"),
  ("nof_db_events",         399997),
  ("nof_db_files",          25),
  ("fsize_db",              23790005587),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.79GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-11 14:51:41"),
])

meta_dictionary["/GluGluToHHTo2B2WToLNu2J_node_7_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo2B2WToLNu2J_node_7_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_node_7_hh_2b2v_sl"),
  ("nof_db_events",         399997),
  ("nof_db_files",          26),
  ("fsize_db",              23886773869),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.89GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-08 22:06:23"),
])

meta_dictionary["/GluGluToHHTo2B2WToLNu2J_node_8_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo2B2WToLNu2J_node_8_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_node_8_hh_2b2v_sl"),
  ("nof_db_events",         395996),
  ("nof_db_files",          19),
  ("fsize_db",              22673829945),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 22.67GB; nevents: 396.00k; release: 10_2_5; last modified: 2020-09-07 03:52:04"),
])

meta_dictionary["/GluGluToHHTo2B2WToLNu2J_node_9_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo2B2WToLNu2J_node_9_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_node_9_hh_2b2v_sl"),
  ("nof_db_events",         399994),
  ("nof_db_files",          24),
  ("fsize_db",              25258622692),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 25.26GB; nevents: 399.99k; release: 10_2_5; last modified: 2020-09-11 11:02:40"),
])

meta_dictionary["/GluGluToHHTo2B2WToLNu2J_node_10_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo2B2WToLNu2J_node_10_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_node_10_hh_2b2v_sl"),
  ("nof_db_events",         399996),
  ("nof_db_files",          17),
  ("fsize_db",              23115766015),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.12GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-07 01:52:08"),
])

meta_dictionary["/GluGluToHHTo2B2WToLNu2J_node_11_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo2B2WToLNu2J_node_11_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_node_11_hh_2b2v_sl"),
  ("nof_db_events",         399997),
  ("nof_db_files",          21),
  ("fsize_db",              23137065319),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.14GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-11 11:00:50"),
])

meta_dictionary["/GluGluToHHTo2B2WToLNu2J_node_12_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo2B2WToLNu2J_node_12_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_node_12_hh_2b2v_sl"),
  ("nof_db_events",         399993),
  ("nof_db_files",          21),
  ("fsize_db",              21463230841),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.46GB; nevents: 399.99k; release: 10_2_5; last modified: 2020-09-13 10:49:38"),
])

meta_dictionary["/GluGluToHHTo2B2VLNu2J_node_cHHH0_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo2B2VLNu2J_node_cHHH0_TuneCP5_PSWeights_13TeV-powheg-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_nonresonant_cHHH0_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_cHHH0_hh_2b2v_sl"),
  ("nof_db_events",         399997),
  ("nof_db_files",          22),
  ("fsize_db",              20383479586),
  ("xsection",              0.00732418),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.38GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-03-13 01:11:05"),
])

meta_dictionary["/GluGluToHHTo2B2VLNu2J_node_cHHH1_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo2B2VLNu2J_node_cHHH1_TuneCP5_PSWeights_13TeV-powheg-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_nonresonant_cHHH1_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_cHHH1_hh_2b2v_sl"),
  ("nof_db_events",         391398),
  ("nof_db_files",          21),
  ("fsize_db",              20213187246),
  ("xsection",              0.00326156),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.21GB; nevents: 391.40k; release: 10_2_5; last modified: 2020-03-20 05:08:41"),
])

meta_dictionary["/GluGluToHHTo2B2VLNu2J_node_cHHH2p45_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo2B2VLNu2J_node_cHHH2p45_TuneCP5_PSWeights_13TeV-powheg-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_nonresonant_cHHH2p45_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_cHHH2p45_hh_2b2v_sl"),
  ("nof_db_events",         383096),
  ("nof_db_files",          25),
  ("fsize_db",              19867289750),
  ("xsection",              0.00138144),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 19.87GB; nevents: 383.10k; release: 10_2_5; last modified: 2020-03-13 18:52:49"),
])

meta_dictionary["/GluGluToHHTo2B2VLNu2J_node_cHHH5_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo2B2VLNu2J_node_cHHH5_TuneCP5_PSWeights_13TeV-powheg-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_nonresonant_cHHH5_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_nonresonant_cHHH5_hh_2b2v_sl"),
  ("nof_db_events",         390197),
  ("nof_db_files",          21),
  ("fsize_db",              19251007287),
  ("xsection",              0.00963593),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 19.25GB; nevents: 390.20k; release: 10_2_5; last modified: 2020-03-06 14:18:28"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2WToLNu2J_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_250_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_250_hh_2b2v_sl"),
  ("nof_db_events",         399995),
  ("nof_db_files",          22),
  ("fsize_db",              22058910739),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 22.06GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-08 16:54:08"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2WToLNu2J_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_260_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_260_hh_2b2v_sl"),
  ("nof_db_events",         399998),
  ("nof_db_files",          20),
  ("fsize_db",              21381399216),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.38GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-10 05:19:03"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2WToLNu2J_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_270_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_270_hh_2b2v_sl"),
  ("nof_db_events",         399996),
  ("nof_db_files",          19),
  ("fsize_db",              21536125803),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.54GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-10 05:19:43"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2WToLNu2J_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_280_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_280_hh_2b2v_sl"),
  ("nof_db_events",         399997),
  ("nof_db_files",          16),
  ("fsize_db",              21876567017),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.88GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-10 05:19:13"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2WToLNu2J_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_300_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_300_hh_2b2v_sl"),
  ("nof_db_events",         299997),
  ("nof_db_files",          15),
  ("fsize_db",              16041315443),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.04GB; nevents: 300.00k; release: 10_2_5; last modified: 2020-09-08 16:54:57"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2WToLNu2J_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_320_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_320_hh_2b2v_sl"),
  ("nof_db_events",         299999),
  ("nof_db_files",          17),
  ("fsize_db",              16244875503),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.24GB; nevents: 300.00k; release: 10_2_5; last modified: 2020-09-10 05:17:23"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2WToLNu2J_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_350_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_350_hh_2b2v_sl"),
  ("nof_db_events",         299997),
  ("nof_db_files",          15),
  ("fsize_db",              16512381924),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.51GB; nevents: 300.00k; release: 10_2_5; last modified: 2020-09-06 11:55:50"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2WToLNu2J_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_400_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_400_hh_2b2v_sl"),
  ("nof_db_events",         299998),
  ("nof_db_files",          18),
  ("fsize_db",              16931027309),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.93GB; nevents: 300.00k; release: 10_2_5; last modified: 2020-09-10 11:12:32"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2WToLNu2J_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_450_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_450_hh_2b2v_sl"),
  ("nof_db_events",         299998),
  ("nof_db_files",          18),
  ("fsize_db",              17783509618),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 17.78GB; nevents: 300.00k; release: 10_2_5; last modified: 2020-09-11 11:01:31"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2WToLNu2J_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_500_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_500_hh_2b2v_sl"),
  ("nof_db_events",         299996),
  ("nof_db_files",          19),
  ("fsize_db",              16531068338),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.53GB; nevents: 300.00k; release: 10_2_5; last modified: 2020-09-17 05:12:22"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2WToLNu2J_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_550_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_550_hh_2b2v_sl"),
  ("nof_db_events",         257999),
  ("nof_db_files",          13),
  ("fsize_db",              14331323976),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.33GB; nevents: 258.00k; release: 10_2_5; last modified: 2020-09-23 11:01:31"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2WToLNu2J_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_600_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_600_hh_2b2v_sl"),
  ("nof_db_events",         199998),
  ("nof_db_files",          14),
  ("fsize_db",              11343834815),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.34GB; nevents: 200.00k; release: 10_2_5; last modified: 2020-09-14 04:49:43"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2WToLNu2J_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_650_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_650_hh_2b2v_sl"),
  ("nof_db_events",         199997),
  ("nof_db_files",          20),
  ("fsize_db",              12597153145),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.60GB; nevents: 200.00k; release: 10_2_5; last modified: 2020-09-09 13:52:36"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2WToLNu2J_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_700_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_700_hh_2b2v_sl"),
  ("nof_db_events",         199999),
  ("nof_db_files",          12),
  ("fsize_db",              11558773806),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.56GB; nevents: 200.00k; release: 10_2_5; last modified: 2020-09-13 12:49:50"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2WToLNu2J_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_750_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_750_hh_2b2v_sl"),
  ("nof_db_events",         199999),
  ("nof_db_files",          20),
  ("fsize_db",              13168839827),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.17GB; nevents: 200.00k; release: 10_2_5; last modified: 2020-09-11 11:01:49"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2WToLNu2J_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_800_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_800_hh_2b2v_sl"),
  ("nof_db_events",         199998),
  ("nof_db_files",          21),
  ("fsize_db",              13271821657),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.27GB; nevents: 200.00k; release: 10_2_5; last modified: 2020-09-11 11:02:25"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2WToLNu2J_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_850_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_850_hh_2b2v_sl"),
  ("nof_db_events",         199998),
  ("nof_db_files",          10),
  ("fsize_db",              12193797346),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.19GB; nevents: 200.00k; release: 10_2_5; last modified: 2020-09-12 19:02:39"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2WToLNu2J_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin0_900_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_900_hh_2b2v_sl"),
  ("nof_db_events",         199999),
  ("nof_db_files",          9),
  ("fsize_db",              13081114484),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.08GB; nevents: 200.00k; release: 10_2_5; last modified: 2020-09-10 13:03:36"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2WToLNu2J_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin0_1000_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_1000_hh_2b2v_sl"),
  ("nof_db_events",         100000),
  ("nof_db_files",          9),
  ("fsize_db",              6078455015),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.08GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-09-11 11:00:40"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2WToLNu2J_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin0_1250_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_1250_hh_2b2v_sl"),
  ("nof_db_events",         99999),
  ("nof_db_files",          5),
  ("fsize_db",              6906320482),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.91GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-09-09 15:49:12"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2WToLNu2J_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin0_1500_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_1500_hh_2b2v_sl"),
  ("nof_db_events",         99998),
  ("nof_db_files",          9),
  ("fsize_db",              6245064826),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.25GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-09-13 17:43:22"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2WToLNu2J_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin0_1750_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_1750_hh_2b2v_sl"),
  ("nof_db_events",         99999),
  ("nof_db_files",          10),
  ("fsize_db",              6519894990),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.52GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-09-11 12:58:03"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2WToLNu2J_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin0_2000_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_2000_hh_2b2v_sl"),
  ("nof_db_events",         99999),
  ("nof_db_files",          7),
  ("fsize_db",              7295615609),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 7.30GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-09-09 05:48:32"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2WToLNu2J_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin0_2500_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_2500_hh_2b2v_sl"),
  ("nof_db_events",         100000),
  ("nof_db_files",          8),
  ("fsize_db",              6648523383),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.65GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-09-23 21:51:36"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2WToLNu2J_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2WToLNu2J_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin0_3000_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin0_3000_hh_2b2v_sl"),
  ("nof_db_events",         99998),
  ("nof_db_files",          12),
  ("fsize_db",              6813110549),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.81GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-09-14 02:45:54"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_ggf_spin2_250_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_250_hh_2b2v_sl"),
  ("nof_db_events",         399995),
  ("nof_db_files",          10),
  ("fsize_db",              19971775045),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 19.97GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-12 08:57:23"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_ggf_spin2_260_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_260_hh_2b2v_sl"),
  ("nof_db_events",         399996),
  ("nof_db_files",          15),
  ("fsize_db",              20198243316),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.20GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-14 01:02:15"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_ggf_spin2_270_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_270_hh_2b2v_sl"),
  ("nof_db_events",         399994),
  ("nof_db_files",          16),
  ("fsize_db",              20152896070),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.15GB; nevents: 399.99k; release: 10_2_5; last modified: 2020-09-14 11:48:27"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_ggf_spin2_280_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_280_hh_2b2v_sl"),
  ("nof_db_events",         393998),
  ("nof_db_files",          20),
  ("fsize_db",              20247168170),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.25GB; nevents: 394.00k; release: 10_2_5; last modified: 2020-09-13 16:03:39"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_ggf_spin2_300_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_300_hh_2b2v_sl"),
  ("nof_db_events",         299996),
  ("nof_db_files",          14),
  ("fsize_db",              15383217059),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 15.38GB; nevents: 300.00k; release: 10_2_5; last modified: 2020-09-13 19:03:52"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_ggf_spin2_320_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_320_hh_2b2v_sl"),
  ("nof_db_events",         299999),
  ("nof_db_files",          14),
  ("fsize_db",              15558724573),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 15.56GB; nevents: 300.00k; release: 10_2_5; last modified: 2020-09-13 10:47:24"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_ggf_spin2_350_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_350_hh_2b2v_sl"),
  ("nof_db_events",         299998),
  ("nof_db_files",          12),
  ("fsize_db",              15844168810),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 15.84GB; nevents: 300.00k; release: 10_2_5; last modified: 2020-09-12 04:58:50"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_ggf_spin2_400_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_400_hh_2b2v_sl"),
  ("nof_db_events",         294999),
  ("nof_db_files",          16),
  ("fsize_db",              16131673901),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.13GB; nevents: 295.00k; release: 10_2_5; last modified: 2020-09-13 17:43:35"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_ggf_spin2_450_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_450_hh_2b2v_sl"),
  ("nof_db_events",         299999),
  ("nof_db_files",          16),
  ("fsize_db",              16748440441),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.75GB; nevents: 300.00k; release: 10_2_5; last modified: 2020-09-11 06:57:50"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_ggf_spin2_500_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_500_hh_2b2v_sl"),
  ("nof_db_events",         299996),
  ("nof_db_files",          10),
  ("fsize_db",              16947221880),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.95GB; nevents: 300.00k; release: 10_2_5; last modified: 2020-09-13 10:52:04"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_ggf_spin2_550_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_550_hh_2b2v_sl"),
  ("nof_db_events",         299996),
  ("nof_db_files",          18),
  ("fsize_db",              18422901680),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 18.42GB; nevents: 300.00k; release: 10_2_5; last modified: 2020-09-11 11:01:20"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_ggf_spin2_600_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_600_hh_2b2v_sl"),
  ("nof_db_events",         199999),
  ("nof_db_files",          13),
  ("fsize_db",              11639973909),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.64GB; nevents: 200.00k; release: 10_2_5; last modified: 2020-09-13 10:48:02"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_ggf_spin2_650_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_650_hh_2b2v_sl"),
  ("nof_db_events",         175996),
  ("nof_db_files",          14),
  ("fsize_db",              10417424944),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 10.42GB; nevents: 176.00k; release: 10_2_5; last modified: 2020-09-23 10:59:01"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_ggf_spin2_700_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_700_hh_2b2v_sl"),
  ("nof_db_events",         200000),
  ("nof_db_files",          11),
  ("fsize_db",              13025859591),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.03GB; nevents: 200.00k; release: 10_2_5; last modified: 2020-09-10 22:51:20"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_ggf_spin2_750_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_750_hh_2b2v_sl"),
  ("nof_db_events",         199995),
  ("nof_db_files",          12),
  ("fsize_db",              11864616665),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.86GB; nevents: 200.00k; release: 10_2_5; last modified: 2020-09-11 12:56:38"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_ggf_spin2_800_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_800_hh_2b2v_sl"),
  ("nof_db_events",         199995),
  ("nof_db_files",          13),
  ("fsize_db",              12088855279),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.09GB; nevents: 200.00k; release: 10_2_5; last modified: 2020-09-14 06:45:08"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_ggf_spin2_850_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_850_hh_2b2v_sl"),
  ("nof_db_events",         189999),
  ("nof_db_files",          13),
  ("fsize_db",              11961368588),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.96GB; nevents: 190.00k; release: 10_2_5; last modified: 2020-09-13 10:50:26"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_ggf_spin2_900_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_900_hh_2b2v_sl"),
  ("nof_db_events",         199998),
  ("nof_db_files",          11),
  ("fsize_db",              13700391957),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.70GB; nevents: 200.00k; release: 10_2_5; last modified: 2020-09-10 13:01:56"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_reali"),
  ("sample_category",       "signal_ggf_spin2_1000_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_1000_hh_2b2v_sl"),
  ("nof_db_events",         100000),
  ("nof_db_files",          9),
  ("fsize_db",              6254656704),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.25GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-09-13 06:46:41"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_reali"),
  ("sample_category",       "signal_ggf_spin2_1250_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_1250_hh_2b2v_sl"),
  ("nof_db_events",         99998),
  ("nof_db_files",          8),
  ("fsize_db",              6492023211),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.49GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-09-12 15:07:56"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_reali"),
  ("sample_category",       "signal_ggf_spin2_1500_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_1500_hh_2b2v_sl"),
  ("nof_db_events",         99999),
  ("nof_db_files",          11),
  ("fsize_db",              7056320162),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 7.06GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-09-10 14:58:49"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_reali"),
  ("sample_category",       "signal_ggf_spin2_1750_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_1750_hh_2b2v_sl"),
  ("nof_db_events",         99999),
  ("nof_db_files",          10),
  ("fsize_db",              7084354114),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 7.08GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-09-10 14:58:26"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_reali"),
  ("sample_category",       "signal_ggf_spin2_2000_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_2000_hh_2b2v_sl"),
  ("nof_db_events",         100000),
  ("nof_db_files",          12),
  ("fsize_db",              6452776971),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.45GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-09-10 22:51:10"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_reali"),
  ("sample_category",       "signal_ggf_spin2_2500_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_2500_hh_2b2v_sl"),
  ("nof_db_events",         99999),
  ("nof_db_files",          6),
  ("fsize_db",              7464949682),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 7.46GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-09-09 05:50:38"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_reali"),
  ("sample_category",       "signal_ggf_spin2_3000_hh_bbvv_sl"),
  ("process_name_specific", "signal_ggf_spin2_3000_hh_2b2v_sl"),
  ("nof_db_events",         99999),
  ("nof_db_files",          10),
  ("fsize_db",              6593140153),
  ("xsection",              0.109352),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.59GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-09-14 19:07:35"),
])

meta_dictionary["/VBFHHTo2B2WToLNu2J_CV_1_C2V_1_C3_0_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo2B2WToLNu2J_CV_1_C2V_1_C3_0_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_0_hh_bbvv_sl"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_0_hh_2b2v_sl_dipoleRecoilOff"),
  ("nof_db_events",         399995),
  ("nof_db_files",          25),
  ("fsize_db",              24143504881),
  ("xsection",              0.0005036125),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 24.14GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-27 21:11:51"),
])

meta_dictionary["/VBFHHTo2B2WToLNu2J_CV_1_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo2B2WToLNu2J_CV_1_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_1_hh_bbvv_sl"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_1_hh_2b2v_sl_dipoleRecoilOff"),
  ("nof_db_events",         399997),
  ("nof_db_files",          21),
  ("fsize_db",              24125629826),
  ("xsection",              0.0001886003),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 24.13GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-25 19:25:04"),
])

meta_dictionary["/VBFHHTo2B2WToLNu2J_CV_1_C2V_1_C3_1_dipoleRecoilOn-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Nov20_VBFHHTo2B2WToLNu2J_CV_1_C2V_1_C3_1_dipoleRecoilOn-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realist"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_1_hh_bbvv_sl_dipoleRecoilOn"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_1_hh_2b2v_sl_dipoleRecoilOn"),
  ("nof_db_events",         399996),
  ("nof_db_files",          21),
  ("fsize_db",              23463936206),
  ("xsection",              0.0001886003),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.46GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-27 03:17:30"),
])

meta_dictionary["/VBFHHTo2B2WToLNu2J_CV_1_C2V_1_C3_2_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo2B2WToLNu2J_CV_1_C2V_1_C3_2_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_2_hh_bbvv_sl"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_2_hh_2b2v_sl_dipoleRecoilOff"),
  ("nof_db_events",         399990),
  ("nof_db_files",          19),
  ("fsize_db",              24881949087),
  ("xsection",              0.0001554708),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 24.88GB; nevents: 399.99k; release: 10_2_5; last modified: 2020-09-29 09:02:19"),
])

meta_dictionary["/VBFHHTo2B2WToLNu2J_CV_1_C2V_2_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo2B2WToLNu2J_CV_1_C2V_2_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_vbf_nonresonant_1_2_1_hh_bbvv_sl"),
  ("process_name_specific", "signal_vbf_nonresonant_1_2_1_hh_2b2v_sl_dipoleRecoilOff"),
  ("nof_db_events",         399996),
  ("nof_db_files",          22),
  ("fsize_db",              26833952115),
  ("xsection",              0.0015535777),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 26.83GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-26 13:23:15"),
])

meta_dictionary["/VBFHHTo2B2WToLNu2J_CV_1_C2V_2_C3_1_dipoleRecoilOn-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Nov18_VBFHHTo2B2WToLNu2J_CV_1_C2V_2_C3_1_dipoleRecoilOn-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realist"),
  ("sample_category",       "signal_vbf_nonresonant_1_2_1_hh_bbvv_sl_dipoleRecoilOn"),
  ("process_name_specific", "signal_vbf_nonresonant_1_2_1_hh_2b2v_sl_dipoleRecoilOn"),
  ("nof_db_events",         399997),
  ("nof_db_files",          23),
  ("fsize_db",              25537439336),
  ("xsection",              0.0015535777),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 25.54GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-27 03:18:41"),
])

meta_dictionary["/VBFHHTo2B2WToLNu2J_CV_0_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo2B2WToLNu2J_CV_0_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_real"),
  ("sample_category",       "signal_vbf_nonresonant_0p5_1_1_hh_bbvv_sl"),
  ("process_name_specific", "signal_vbf_nonresonant_0p5_1_1_hh_2b2v_sl_dipoleRecoilOff"),
  ("nof_db_events",         400000),
  ("nof_db_files",          20),
  ("fsize_db",              26407229036),
  ("xsection",              0.0011827091),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 26.41GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-27 03:16:55"),
])

meta_dictionary["/VBFHHTo2B2WToLNu2J_CV_1_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo2B2WToLNu2J_CV_1_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_real"),
  ("sample_category",       "signal_vbf_nonresonant_1p5_1_1_hh_bbvv_sl"),
  ("process_name_specific", "signal_vbf_nonresonant_1p5_1_1_hh_2b2v_sl_dipoleRecoilOff"),
  ("nof_db_events",         399999),
  ("nof_db_files",          19),
  ("fsize_db",              24759957662),
  ("xsection",              0.007213847),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 24.76GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-29 07:02:17"),
])

meta_dictionary["/VBFHHTo2B2WToLNu2J_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo2B2WToLNu2J_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realis"),
  ("sample_category",       "signal_vbf_nonresonant_1_0_1_hh_bbvv_sl"),
  ("process_name_specific", "signal_vbf_nonresonant_1_0_1_hh_2b2v_sl_dipoleRecoilOff"),
  ("nof_db_events",         399995),
  ("nof_db_files",          20),
  ("fsize_db",              25812987479),
  ("xsection",              0.0029590341),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 25.81GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-27 09:13:19"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_VBFToRadionToHHTo2B2Tau_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_vbf_spin0_250_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_250_hh_2b2t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          16),
  ("fsize_db",              24201103622),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 24.20GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-05-21 18:24:29"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_VBFToRadionToHHTo2B2Tau_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_vbf_spin0_260_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_260_hh_2b2t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          21),
  ("fsize_db",              24429994840),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 24.43GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-03-28 14:24:59"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_VBFToRadionToHHTo2B2Tau_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_vbf_spin0_270_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_270_hh_2b2t"),
  ("nof_db_events",         384000),
  ("nof_db_files",          17),
  ("fsize_db",              23560021919),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.56GB; nevents: 384.00k; release: 10_2_5; last modified: 2019-04-15 06:11:27"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_VBFToRadionToHHTo2B2Tau_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_vbf_spin0_280_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_280_hh_2b2t"),
  ("nof_db_events",         378000),
  ("nof_db_files",          23),
  ("fsize_db",              23422801619),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.42GB; nevents: 378.00k; release: 10_2_5; last modified: 2019-04-29 08:27:47"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_VBFToRadionToHHTo2B2Tau_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_vbf_spin0_300_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_300_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          15),
  ("fsize_db",              18779481578),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 18.78GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-06-02 00:53:21"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_VBFToRadionToHHTo2B2Tau_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_vbf_spin0_320_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_320_hh_2b2t"),
  ("nof_db_events",         268000),
  ("nof_db_files",          17),
  ("fsize_db",              16443985477),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.44GB; nevents: 268.00k; release: 10_2_5; last modified: 2019-05-28 21:52:02"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_VBFToRadionToHHTo2B2Tau_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_vbf_spin0_350_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_350_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          18),
  ("fsize_db",              19234659018),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 19.23GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-04-15 18:08:54"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_VBFToRadionToHHTo2B2Tau_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_vbf_spin0_400_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_400_hh_2b2t"),
  ("nof_db_events",         284000),
  ("nof_db_files",          12),
  ("fsize_db",              18538011629),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 18.54GB; nevents: 284.00k; release: 10_2_5; last modified: 2019-05-06 05:49:08"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_VBFToRadionToHHTo2B2Tau_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_vbf_spin0_450_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_450_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          14),
  ("fsize_db",              19880260071),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 19.88GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-05-11 16:18:32"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_VBFToRadionToHHTo2B2Tau_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_vbf_spin0_500_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_500_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          14),
  ("fsize_db",              20164079086),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.16GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-05-10 23:06:01"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_VBFToRadionToHHTo2B2Tau_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_vbf_spin0_550_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_550_hh_2b2t"),
  ("nof_db_events",         292000),
  ("nof_db_files",          18),
  ("fsize_db",              20001572830),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.00GB; nevents: 292.00k; release: 10_2_5; last modified: 2019-04-16 06:53:05"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_VBFToRadionToHHTo2B2Tau_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_vbf_spin0_600_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_600_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          10),
  ("fsize_db",              13832525612),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.83GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-05-05 16:54:08"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_VBFToRadionToHHTo2B2Tau_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_vbf_spin0_650_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_650_hh_2b2t"),
  ("nof_db_events",         192000),
  ("nof_db_files",          15),
  ("fsize_db",              13520238121),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.52GB; nevents: 192.00k; release: 10_2_5; last modified: 2019-05-12 13:33:40"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_VBFToRadionToHHTo2B2Tau_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_vbf_spin0_700_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_700_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          12),
  ("fsize_db",              14128746298),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.13GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-05-17 07:24:35"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Nov24_VBFToRadionToHHTo2B2Tau_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_vbf_spin0_750_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_750_hh_2b2t"),
  ("nof_db_events",         192000),
  ("nof_db_files",          10),
  ("fsize_db",              13657644591),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.66GB; nevents: 192.00k; release: 10_2_5; last modified: 2019-05-11 00:07:30"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Nov24_VBFToRadionToHHTo2B2Tau_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_vbf_spin0_800_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_800_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          17),
  ("fsize_db",              14483792512),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.48GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-04-21 19:51:52"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFToRadionToHHTo2B2Tau_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin0_850_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_850_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          8),
  ("fsize_db",              15269843874),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 15.27GB; nevents: 200.00k; release: 10_2_5; last modified: 2020-09-15 21:52:29"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_VBFToRadionToHHTo2B2Tau_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_vbf_spin0_900_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_900_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          19),
  ("fsize_db",              14720486395),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.72GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-05-01 09:30:27"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_VBFToRadionToHHTo2B2Tau_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_vbf_spin0_1000_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_1000_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          12),
  ("fsize_db",              7497593534),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 7.50GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-04-21 19:40:11"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_VBFToRadionToHHTo2B2Tau_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_vbf_spin0_1250_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_1250_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          10),
  ("fsize_db",              7602021628),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 7.60GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-04-17 20:21:08"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Nov24_VBFToRadionToHHTo2B2Tau_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_vbf_spin0_1500_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_1500_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          9),
  ("fsize_db",              7687388828),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 7.69GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-05-29 23:31:29"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Nov24_VBFToRadionToHHTo2B2Tau_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_vbf_spin0_1750_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_1750_hh_2b2t"),
  ("nof_db_events",         91000),
  ("nof_db_files",          8),
  ("fsize_db",              7052793193),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 7.05GB; nevents: 91.00k; release: 10_2_5; last modified: 2019-05-21 20:57:07"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_VBFToRadionToHHTo2B2Tau_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_vbf_spin0_2000_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_2000_hh_2b2t"),
  ("nof_db_events",         84000),
  ("nof_db_files",          12),
  ("fsize_db",              6693361558),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.69GB; nevents: 84.00k; release: 10_2_5; last modified: 2019-04-17 14:52:09"),
])

meta_dictionary["/VBFToRadionToHHTo2B2Tau_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_VBFToRadionToHHTo2B2Tau_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_vbf_spin0_3000_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin0_3000_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          13),
  ("fsize_db",              8103387579),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 8.10GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-04-13 15:39:10"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_VBFToBulkGravitonToHHTo2B2Tau_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_vbf_spin2_250_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_250_hh_2b2t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          16),
  ("fsize_db",              24231856380),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 24.23GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-05-10 23:10:25"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_VBFToBulkGravitonToHHTo2B2Tau_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_vbf_spin2_260_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_260_hh_2b2t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          25),
  ("fsize_db",              22967054769),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 22.97GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-05-02 03:00:13"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_VBFToBulkGravitonToHHTo2B2Tau_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_vbf_spin2_270_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_270_hh_2b2t"),
  ("nof_db_events",         384000),
  ("nof_db_files",          25),
  ("fsize_db",              21814983036),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.81GB; nevents: 384.00k; release: 10_2_5; last modified: 2019-04-15 02:11:11"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_VBFToBulkGravitonToHHTo2B2Tau_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_vbf_spin2_280_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_280_hh_2b2t"),
  ("nof_db_events",         356000),
  ("nof_db_files",          18),
  ("fsize_db",              20210387059),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.21GB; nevents: 356.00k; release: 10_2_5; last modified: 2019-05-29 18:35:14"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_VBFToBulkGravitonToHHTo2B2Tau_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_vbf_spin2_300_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_300_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          19),
  ("fsize_db",              17244807583),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 17.24GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-05-29 13:34:37"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_VBFToBulkGravitonToHHTo2B2Tau_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_vbf_spin2_320_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_320_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          18),
  ("fsize_db",              17220173981),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 17.22GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-04-21 19:38:49"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_VBFToBulkGravitonToHHTo2B2Tau_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_vbf_spin2_350_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_350_hh_2b2t"),
  ("nof_db_events",         290000),
  ("nof_db_files",          19),
  ("fsize_db",              16301770062),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.30GB; nevents: 290.00k; release: 10_2_5; last modified: 2019-04-14 14:32:34"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_VBFToBulkGravitonToHHTo2B2Tau_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_vbf_spin2_400_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_400_hh_2b2t"),
  ("nof_db_events",         284000),
  ("nof_db_files",          12),
  ("fsize_db",              16196623550),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.20GB; nevents: 284.00k; release: 10_2_5; last modified: 2019-05-06 09:50:56"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_VBFToBulkGravitonToHHTo2B2Tau_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_vbf_spin2_450_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_450_hh_2b2t"),
  ("nof_db_events",         295000),
  ("nof_db_files",          20),
  ("fsize_db",              16589766784),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.59GB; nevents: 295.00k; release: 10_2_5; last modified: 2019-04-14 18:35:56"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_VBFToBulkGravitonToHHTo2B2Tau_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_vbf_spin2_500_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_500_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          13),
  ("fsize_db",              16882301821),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.88GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-05-12 13:30:59"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_VBFToBulkGravitonToHHTo2B2Tau_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_vbf_spin2_600_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_600_hh_2b2t"),
  ("nof_db_events",         192000),
  ("nof_db_files",          13),
  ("fsize_db",              11104772663),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.10GB; nevents: 192.00k; release: 10_2_5; last modified: 2019-04-12 19:39:35"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_VBFToBulkGravitonToHHTo2B2Tau_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_vbf_spin2_650_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_650_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          11),
  ("fsize_db",              11488161488),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.49GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-04-22 23:58:25"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_VBFToBulkGravitonToHHTo2B2Tau_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_vbf_spin2_700_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_700_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          12),
  ("fsize_db",              11488642680),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.49GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-04-15 18:12:13"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_VBFToBulkGravitonToHHTo2B2Tau_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_vbf_spin2_750_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_750_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          14),
  ("fsize_db",              11534875410),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.53GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-04-28 03:05:42"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_VBFToBulkGravitonToHHTo2B2Tau_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_vbf_spin2_850_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_850_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          10),
  ("fsize_db",              11437184170),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.44GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-04-30 13:04:07"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_VBFToBulkGravitonToHHTo2B2Tau_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_vbf_spin2_900_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_900_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          7),
  ("fsize_db",              11390511587),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.39GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-04-30 00:51:05"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_VBFToBulkGravitonToHHTo2B2Tau_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-"),
  ("sample_category",       "signal_vbf_spin2_1000_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_1000_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          9),
  ("fsize_db",              5853097024),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 5.85GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-05-16 02:03:45"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-1200_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_VBFToBulkGravitonToHHTo2B2Tau_M-1200_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-"),
  ("sample_category",       "signal_vbf_spin2_1200_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_1200_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          3),
  ("fsize_db",              5865949865),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 5.87GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-05-03 07:04:06"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_VBFToBulkGravitonToHHTo2B2Tau_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-"),
  ("sample_category",       "signal_vbf_spin2_1750_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_1750_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          7),
  ("fsize_db",              5885960863),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 5.89GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-05-01 15:28:37"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2B2Tau_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_VBFToBulkGravitonToHHTo2B2Tau_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-"),
  ("sample_category",       "signal_vbf_spin2_2000_hh_bbtt"),
  ("process_name_specific", "signal_vbf_spin2_2000_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          9),
  ("fsize_db",              6034285592),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.03GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-04-11 11:28:47"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToRadionToHHTo2B2Tau_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_spin0_250_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_250_hh_2b2t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          12),
  ("fsize_db",              20240174056),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.24GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-05-10 23:40:14"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToRadionToHHTo2B2Tau_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_spin0_260_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_260_hh_2b2t"),
  ("nof_db_events",         384000),
  ("nof_db_files",          19),
  ("fsize_db",              18565212926),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 18.57GB; nevents: 384.00k; release: 10_2_5; last modified: 2019-04-21 19:37:57"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToRadionToHHTo2B2Tau_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_spin0_270_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_270_hh_2b2t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          19),
  ("fsize_db",              19438730085),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 19.44GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-04-21 19:43:36"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToRadionToHHTo2B2Tau_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_spin0_280_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_280_hh_2b2t"),
  ("nof_db_events",         394000),
  ("nof_db_files",          19),
  ("fsize_db",              20152836915),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.15GB; nevents: 394.00k; release: 10_2_5; last modified: 2019-04-15 02:11:42"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToRadionToHHTo2B2Tau_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_spin0_300_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_300_hh_2b2t"),
  ("nof_db_events",         282000),
  ("nof_db_files",          11),
  ("fsize_db",              13926261523),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.93GB; nevents: 282.00k; release: 10_2_5; last modified: 2019-05-02 21:11:15"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToRadionToHHTo2B2Tau_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_spin0_320_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_320_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          16),
  ("fsize_db",              15016611273),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 15.02GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-04-21 19:39:41"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-340_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo2B2Tau_M-340_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_340_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_340_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          15),
  ("fsize_db",              16764677713),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.76GB; nevents: 300.00k; release: 10_2_5; last modified: 2020-09-14 04:54:19"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToRadionToHHTo2B2Tau_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_spin0_350_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_350_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          15),
  ("fsize_db",              15183250113),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 15.18GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-06-05 16:46:06"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToRadionToHHTo2B2Tau_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_spin0_400_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_400_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          15),
  ("fsize_db",              15498531412),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 15.50GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-04-14 20:35:57"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToRadionToHHTo2B2Tau_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_spin0_450_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_450_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          18),
  ("fsize_db",              15806279456),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 15.81GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-05-30 04:23:12"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToRadionToHHTo2B2Tau_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_spin0_500_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_500_hh_2b2t"),
  ("nof_db_events",         279000),
  ("nof_db_files",          10),
  ("fsize_db",              14816439731),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.82GB; nevents: 279.00k; release: 10_2_5; last modified: 2019-05-17 22:22:31"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToRadionToHHTo2B2Tau_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_spin0_550_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_550_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          19),
  ("fsize_db",              16251104941),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.25GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-04-26 06:19:34"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToRadionToHHTo2B2Tau_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_spin0_600_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_600_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          15),
  ("fsize_db",              11015984538),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.02GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-04-15 02:10:17"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToRadionToHHTo2B2Tau_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_spin0_650_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_650_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          8),
  ("fsize_db",              10969933314),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 10.97GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-05-05 15:15:55"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToRadionToHHTo2B2Tau_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_spin0_700_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_700_hh_2b2t"),
  ("nof_db_events",         190000),
  ("nof_db_files",          15),
  ("fsize_db",              10693708527),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 10.69GB; nevents: 190.00k; release: 10_2_5; last modified: 2019-05-06 18:31:11"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToRadionToHHTo2B2Tau_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_spin0_750_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_750_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          10),
  ("fsize_db",              11645634056),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.65GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-06-01 01:25:21"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToRadionToHHTo2B2Tau_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_spin0_800_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_800_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          12),
  ("fsize_db",              11769076433),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.77GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-05-06 09:54:07"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToRadionToHHTo2B2Tau_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_spin0_850_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_850_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          11),
  ("fsize_db",              11808552400),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.81GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-04-21 08:43:28"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToRadionToHHTo2B2Tau_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_spin0_900_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_900_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          7),
  ("fsize_db",              11388868653),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.39GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-05-01 02:19:55"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToRadionToHHTo2B2Tau_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_spin0_1000_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_1000_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          6),
  ("fsize_db",              5818152628),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 5.82GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-05-01 02:16:29"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToRadionToHHTo2B2Tau_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_spin0_1250_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_1250_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          10),
  ("fsize_db",              6226646883),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.23GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-05-29 13:36:02"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToRadionToHHTo2B2Tau_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_spin0_1500_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_1500_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          5),
  ("fsize_db",              5941935179),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 5.94GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-05-04 15:00:17"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToRadionToHHTo2B2Tau_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_spin0_1750_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_1750_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          11),
  ("fsize_db",              6337929130),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.34GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-04-13 15:35:06"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToRadionToHHTo2B2Tau_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_spin0_2000_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_2000_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          8),
  ("fsize_db",              6150409100),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.15GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-04-10 08:57:18"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToRadionToHHTo2B2Tau_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_spin0_2500_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_2500_hh_2b2t"),
  ("nof_db_events",         75000),
  ("nof_db_files",          8),
  ("fsize_db",              4884205812),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 4.88GB; nevents: 75.00k; release: 10_2_5; last modified: 2019-05-01 19:56:22"),
])

meta_dictionary["/GluGluToRadionToHHTo2B2Tau_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToRadionToHHTo2B2Tau_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_spin0_3000_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin0_3000_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          10),
  ("fsize_db",              6520354346),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.52GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-05-04 15:04:42"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToBulkGravitonToHHTo2B2Tau_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_250_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_250_hh_2b2t"),
  ("nof_db_events",         380000),
  ("nof_db_files",          18),
  ("fsize_db",              18890989806),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 18.89GB; nevents: 380.00k; release: 10_2_5; last modified: 2019-04-26 06:20:41"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToBulkGravitonToHHTo2B2Tau_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_260_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_260_hh_2b2t"),
  ("nof_db_events",         382000),
  ("nof_db_files",          16),
  ("fsize_db",              19066503700),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 19.07GB; nevents: 382.00k; release: 10_2_5; last modified: 2019-05-11 05:07:30"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToBulkGravitonToHHTo2B2Tau_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_270_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_270_hh_2b2t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          16),
  ("fsize_db",              19893232081),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 19.89GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-04-14 08:40:25"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToBulkGravitonToHHTo2B2Tau_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_280_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_280_hh_2b2t"),
  ("nof_db_events",         380000),
  ("nof_db_files",          18),
  ("fsize_db",              18844045494),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 18.84GB; nevents: 380.00k; release: 10_2_5; last modified: 2019-04-17 20:26:05"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToBulkGravitonToHHTo2B2Tau_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_300_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_300_hh_2b2t"),
  ("nof_db_events",         276000),
  ("nof_db_files",          18),
  ("fsize_db",              14039003672),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.04GB; nevents: 276.00k; release: 10_2_5; last modified: 2019-04-30 23:50:46"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToBulkGravitonToHHTo2B2Tau_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_320_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_320_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          18),
  ("fsize_db",              15463954444),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 15.46GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-04-21 19:46:51"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-340_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo2B2Tau_M-340_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin2_340_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_340_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          13),
  ("fsize_db",              17118223925),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 17.12GB; nevents: 300.00k; release: 10_2_5; last modified: 2020-09-14 16:02:54"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToBulkGravitonToHHTo2B2Tau_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_350_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_350_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          18),
  ("fsize_db",              15655389694),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 15.66GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-05-14 04:41:32"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToBulkGravitonToHHTo2B2Tau_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_400_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_400_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          16),
  ("fsize_db",              15930702282),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 15.93GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-05-26 18:41:54"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToBulkGravitonToHHTo2B2Tau_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_450_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_450_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          13),
  ("fsize_db",              16108935179),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.11GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-05-06 09:54:46"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToBulkGravitonToHHTo2B2Tau_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_500_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_500_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          17),
  ("fsize_db",              16548626128),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.55GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-05-28 19:44:58"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToBulkGravitonToHHTo2B2Tau_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_550_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_550_hh_2b2t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          20),
  ("fsize_db",              16747172547),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.75GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-04-18 00:30:11"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToBulkGravitonToHHTo2B2Tau_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_600_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_600_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          12),
  ("fsize_db",              11160601240),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.16GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-04-30 00:51:26"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToBulkGravitonToHHTo2B2Tau_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_650_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_650_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          13),
  ("fsize_db",              11334272905),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.33GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-04-21 19:42:55"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToBulkGravitonToHHTo2B2Tau_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_700_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_700_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          16),
  ("fsize_db",              11442662705),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.44GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-04-21 19:50:46"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToBulkGravitonToHHTo2B2Tau_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_750_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_750_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          11),
  ("fsize_db",              11419024777),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.42GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-04-14 20:33:47"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToBulkGravitonToHHTo2B2Tau_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_800_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_800_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          14),
  ("fsize_db",              11703560456),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.70GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-04-22 23:57:45"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToBulkGravitonToHHTo2B2Tau_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_850_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_850_hh_2b2t"),
  ("nof_db_events",         190000),
  ("nof_db_files",          14),
  ("fsize_db",              11594437357),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.59GB; nevents: 190.00k; release: 10_2_5; last modified: 2019-04-15 14:07:03"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToBulkGravitonToHHTo2B2Tau_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_900_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_900_hh_2b2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          17),
  ("fsize_db",              12299683201),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.30GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-04-21 19:52:36"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToBulkGravitonToHHTo2B2Tau_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin2_1000_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_1000_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          6),
  ("fsize_db",              5950106308),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 5.95GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-04-30 00:55:12"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToBulkGravitonToHHTo2B2Tau_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin2_1250_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_1250_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          8),
  ("fsize_db",              6272333626),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.27GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-05-29 13:37:02"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToBulkGravitonToHHTo2B2Tau_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin2_1500_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_1500_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          6),
  ("fsize_db",              6259371847),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.26GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-05-04 21:09:00"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToBulkGravitonToHHTo2B2Tau_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin2_1750_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_1750_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          7),
  ("fsize_db",              6307435165),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.31GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-04-21 19:44:08"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToBulkGravitonToHHTo2B2Tau_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin2_2000_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_2000_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          11),
  ("fsize_db",              6220782071),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.22GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-05-29 23:27:25"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToBulkGravitonToHHTo2B2Tau_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin2_2500_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_2500_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          10),
  ("fsize_db",              6340415904),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.34GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-05-29 08:37:47"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2B2Tau_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToBulkGravitonToHHTo2B2Tau_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin2_3000_hh_bbtt"),
  ("process_name_specific", "signal_ggf_spin2_3000_hh_2b2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          8),
  ("fsize_db",              6287076693),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.29GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-04-21 19:51:57"),
])

meta_dictionary["/VBFHHTo2B2Tau_CV_1_C2V_1_C3_0_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo2B2Tau_CV_1_C2V_1_C3_0_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_0_hh_bbtt"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_0_hh_2b2t_dipoleRecoilOff"),
  ("nof_db_events",         1000000),
  ("nof_db_files",          26),
  ("fsize_db",              57894125585),
  ("xsection",              0.0003364547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 57.89GB; nevents: 1.00M; release: 10_2_5; last modified: 2020-09-14 13:03:00"),
])

meta_dictionary["/VBFHHTo2B2Tau_CV_1_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo2B2Tau_CV_1_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_1_hh_bbtt"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_1_hh_2b2t_dipoleRecoilOff"),
  ("nof_db_events",         2000000),
  ("nof_db_files",          48),
  ("fsize_db",              116165471521),
  ("xsection",              0.0001260006),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 116.17GB; nevents: 2.00M; release: 10_2_5; last modified: 2020-09-16 05:58:37"),
])

meta_dictionary["/VBFHHTo2B2Tau_CV_1_C2V_1_C3_1_dipoleRecoilOn-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Nov18_VBFHHTo2B2Tau_CV_1_C2V_1_C3_1_dipoleRecoilOn-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_1_hh_bbtt_dipoleRecoilOn"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_1_hh_2b2t_dipoleRecoilOn"),
  ("nof_db_events",         1000000),
  ("nof_db_files",          27),
  ("fsize_db",              56478823992),
  ("xsection",              0.0001260006),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 56.48GB; nevents: 1.00M; release: 10_2_5; last modified: 2020-09-14 19:07:55"),
])

meta_dictionary["/VBFHHTo2B2Tau_CV_1_C2V_1_C3_2_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo2B2Tau_CV_1_C2V_1_C3_2_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_2_hh_bbtt"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_2_hh_2b2t_dipoleRecoilOff"),
  ("nof_db_events",         997000),
  ("nof_db_files",          29),
  ("fsize_db",              60946852926),
  ("xsection",              0.0001038674),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 60.95GB; nevents: 997.00k; release: 10_2_5; last modified: 2020-09-15 14:41:41"),
])

meta_dictionary["/VBFHHTo2B2Tau_CV_1_C2V_2_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo2B2Tau_CV_1_C2V_2_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_vbf_nonresonant_1_2_1_hh_bbtt"),
  ("process_name_specific", "signal_vbf_nonresonant_1_2_1_hh_2b2t_dipoleRecoilOff"),
  ("nof_db_events",         1996000),
  ("nof_db_files",          56),
  ("fsize_db",              126966878305),
  ("xsection",              0.0010379183),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 126.97GB; nevents: 2.00M; release: 10_2_5; last modified: 2020-09-15 21:53:00"),
])

meta_dictionary["/VBFHHTo2B2Tau_CV_1_C2V_2_C3_1_dipoleRecoilOn-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Nov18_VBFHHTo2B2Tau_CV_1_C2V_2_C3_1_dipoleRecoilOn-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v1"),
  ("sample_category",       "signal_vbf_nonresonant_1_2_1_hh_bbtt_dipoleRecoilOn"),
  ("process_name_specific", "signal_vbf_nonresonant_1_2_1_hh_2b2t_dipoleRecoilOn"),
  ("nof_db_events",         1000000),
  ("nof_db_files",          29),
  ("fsize_db",              63322680009),
  ("xsection",              0.0010379183),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 63.32GB; nevents: 1.00M; release: 10_2_5; last modified: 2020-09-13 22:05:07"),
])

meta_dictionary["/VBFHHTo2B2Tau_CV_1_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo2B2Tau_CV_1_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic"),
  ("sample_category",       "signal_vbf_nonresonant_1p5_1_1_hh_bbtt"),
  ("process_name_specific", "signal_vbf_nonresonant_1p5_1_1_hh_2b2t_dipoleRecoilOff"),
  ("nof_db_events",         1000000),
  ("nof_db_files",          32),
  ("fsize_db",              61833260146),
  ("xsection",              0.0048194459),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 61.83GB; nevents: 1.00M; release: 10_2_5; last modified: 2020-09-15 14:43:06"),
])

meta_dictionary["/VBFHHTo2B2Tau_CV_0_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo2B2Tau_CV_0_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic"),
  ("sample_category",       "signal_vbf_nonresonant_0p5_1_1_hh_bbtt"),
  ("process_name_specific", "signal_vbf_nonresonant_0p5_1_1_hh_2b2t_dipoleRecoilOff"),
  ("nof_db_events",         992000),
  ("nof_db_files",          29),
  ("fsize_db",              62115882584),
  ("xsection",              0.0007901474),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 62.12GB; nevents: 992.00k; release: 10_2_5; last modified: 2020-09-17 00:55:01"),
])

meta_dictionary["/VBFHHTo2B2Tau_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo2B2Tau_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v/201012_142237"),
  ("sample_category",       "signal_vbf_nonresonant_1_0_1_hh_bbtt"),
  ("process_name_specific", "signal_vbf_nonresonant_1_0_1_hh_2b2t_dipoleRecoilOff"),
  ("nof_db_events",         1997000),
  ("nof_db_files",          55),
  ("fsize_db",              125408556263),
  ("xsection",              0.0019768862),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 125.41GB; nevents: 2.00M; release: 10_2_5; last modified: 2020-09-16 15:36:42"),
])

meta_dictionary["/VBFHHTo2B2Tau_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo2B2Tau_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v/201012_142346"),
  ("sample_category",       "signal_vbf_nonresonant_1_0_1_hh_bbtt"),
  ("process_name_specific", "signal_vbf_nonresonant_1_0_1_hh_2b2t_dipoleRecoilOff_ext1"),
  ("nof_db_events",         500000),
  ("nof_db_files",          15),
  ("fsize_db",              31415804608),
  ("xsection",              0.0019768862),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 31.42GB; nevents: 500.00k; release: 10_2_5; last modified: 2020-08-15 12:30:34"),
])

meta_dictionary["/GluGluToHHTo2B2Tau_node_SM_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToHHTo2B2Tau_node_SM_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_sm_hh_2b2t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          22),
  ("fsize_db",              21797059213),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.80GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-05-30 11:38:11"),
])

meta_dictionary["/GluGluToHHTo2B2Tau_node_2_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToHHTo2B2Tau_node_2_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_2_hh_2b2t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          25),
  ("fsize_db",              22516257623),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 22.52GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-04-27 06:50:19"),
])

meta_dictionary["/GluGluToHHTo2B2Tau_node_3_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToHHTo2B2Tau_node_3_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_3_hh_2b2t"),
  ("nof_db_events",         385000),
  ("nof_db_files",          16),
  ("fsize_db",              20832150345),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.83GB; nevents: 385.00k; release: 10_2_5; last modified: 2019-04-23 00:03:20"),
])

meta_dictionary["/GluGluToHHTo2B2Tau_node_4_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToHHTo2B2Tau_node_4_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_4_hh_2b2t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          21),
  ("fsize_db",              21196927455),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.20GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-05-11 16:20:01"),
])

meta_dictionary["/GluGluToHHTo2B2Tau_node_5_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToHHTo2B2Tau_node_5_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_5_hh_2b2t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          17),
  ("fsize_db",              21769316911),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.77GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-06-05 17:04:58"),
])

meta_dictionary["/GluGluToHHTo2B2Tau_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToHHTo2B2Tau_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_6_hh_2b2t"),
  ("nof_db_events",         388000),
  ("nof_db_files",          25),
  ("fsize_db",              20580880747),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.58GB; nevents: 388.00k; release: 10_2_5; last modified: 2019-04-24 22:34:17"),
])

meta_dictionary["/GluGluToHHTo2B2Tau_node_7_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToHHTo2B2Tau_node_7_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_7_hh_2b2t"),
  ("nof_db_events",         345000),
  ("nof_db_files",          20),
  ("fsize_db",              18385644793),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 18.39GB; nevents: 345.00k; release: 10_2_5; last modified: 2019-05-24 21:04:00"),
])

meta_dictionary["/GluGluToHHTo2B2Tau_node_8_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToHHTo2B2Tau_node_8_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_8_hh_2b2t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          15),
  ("fsize_db",              20868493058),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.87GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-05-04 21:04:16"),
])

meta_dictionary["/GluGluToHHTo2B2Tau_node_9_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToHHTo2B2Tau_node_9_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_9_hh_2b2t"),
  ("nof_db_events",         395000),
  ("nof_db_files",          19),
  ("fsize_db",              22426425741),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 22.43GB; nevents: 395.00k; release: 10_2_5; last modified: 2019-06-13 14:00:42"),
])

meta_dictionary["/GluGluToHHTo2B2Tau_node_10_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToHHTo2B2Tau_node_10_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_10_hh_2b2t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          23),
  ("fsize_db",              21245748310),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.25GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-04-23 00:00:20"),
])

meta_dictionary["/GluGluToHHTo2B2Tau_node_11_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToHHTo2B2Tau_node_11_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_11_hh_2b2t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          12),
  ("fsize_db",              20943410362),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.94GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-05-04 15:01:57"),
])

meta_dictionary["/GluGluToHHTo2B2Tau_node_12_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2019Oct06_GluGluToHHTo2B2Tau_node_12_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_12_hh_2b2t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          23),
  ("fsize_db",              21011506973),
  ("xsection",              0.073056),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.01GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-04-26 06:23:27"),
])

meta_dictionary["/GluGluToHHTo2B2Tau_node_cHHH0_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo2B2Tau_node_cHHH0_TuneCP5_PSWeights_13TeV-powheg-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_nonresonant_cHHH0_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_cHHH0_hh_2b2t"),
  ("nof_db_events",         1000000),
  ("nof_db_files",          34),
  ("fsize_db",              49487397386),
  ("xsection",              0.00489315),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 49.49GB; nevents: 1.00M; release: 10_2_5; last modified: 2020-03-13 18:56:29"),
])

meta_dictionary["/GluGluToHHTo2B2Tau_node_cHHH1_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo2B2Tau_node_cHHH1_TuneCP5_PSWeights_13TeV-powheg-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_nonresonant_cHHH1_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_cHHH1_hh_2b2t"),
  ("nof_db_events",         1000000),
  ("nof_db_files",          34),
  ("fsize_db",              50081318436),
  ("xsection",              0.00217899),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 50.08GB; nevents: 1.00M; release: 10_2_5; last modified: 2020-03-15 05:46:32"),
])

meta_dictionary["/GluGluToHHTo2B2Tau_node_cHHH2p45_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo2B2Tau_node_cHHH2p45_TuneCP5_PSWeights_13TeV-powheg-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_nonresonant_cHHH2p45_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_cHHH2p45_hh_2b2t"),
  ("nof_db_events",         1000000),
  ("nof_db_files",          39),
  ("fsize_db",              50271035315),
  ("xsection",              0.00092291),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 50.27GB; nevents: 1.00M; release: 10_2_5; last modified: 2020-03-15 05:47:22"),
])

meta_dictionary["/GluGluToHHTo2B2Tau_node_cHHH5_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo2B2Tau_node_cHHH5_TuneCP5_PSWeights_13TeV-powheg-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_nonresonant_cHHH5_hh_bbtt"),
  ("process_name_specific", "signal_ggf_nonresonant_cHHH5_hh_2b2t"),
  ("nof_db_events",         1000000),
  ("nof_db_files",          35),
  ("fsize_db",              48318284793),
  ("xsection",              0.00643758),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 48.32GB; nevents: 1.00M; release: 10_2_5; last modified: 2020-03-13 18:56:38"),
])


# event statistics by sample category:
# signal_ggf_spin0_250_hh_bbvv:                           400.00k
# signal_ggf_spin0_260_hh_bbvv:                           400.00k
# signal_ggf_spin0_270_hh_bbvv:                           400.00k
# signal_ggf_spin0_280_hh_bbvv:                           400.00k
# signal_ggf_spin0_300_hh_bbvv:                           300.00k
# signal_ggf_spin0_320_hh_bbvv:                           300.00k
# signal_ggf_spin0_350_hh_bbvv:                           300.00k
# signal_ggf_spin0_400_hh_bbvv:                           300.00k
# signal_ggf_spin0_500_hh_bbvv:                           300.00k
# signal_ggf_spin0_550_hh_bbvv:                           300.00k
# signal_ggf_spin0_600_hh_bbvv:                           200.00k
# signal_ggf_spin0_650_hh_bbvv:                           200.00k
# signal_ggf_spin0_700_hh_bbvv:                           200.00k
# signal_ggf_spin0_750_hh_bbvv:                           200.00k
# signal_ggf_spin0_800_hh_bbvv:                           200.00k
# signal_ggf_spin0_850_hh_bbvv:                           200.00k
# signal_ggf_spin0_900_hh_bbvv:                           200.00k
# signal_ggf_spin0_1000_hh_bbvv:                          100.00k
# signal_ggf_spin0_1250_hh_bbvv:                          100.00k
# signal_ggf_spin0_1500_hh_bbvv:                          100.00k
# signal_ggf_spin0_1750_hh_bbvv:                          100.00k
# signal_ggf_spin0_2000_hh_bbvv:                          100.00k
# signal_ggf_spin0_2500_hh_bbvv:                          100.00k
# signal_ggf_spin0_3000_hh_bbvv:                          100.00k
# signal_ggf_spin2_250_hh_bbvv:                           400.00k
# signal_ggf_spin2_260_hh_bbvv:                           400.00k
# signal_ggf_spin2_270_hh_bbvv:                           400.00k
# signal_ggf_spin2_280_hh_bbvv:                           400.00k
# signal_ggf_spin2_300_hh_bbvv:                           300.00k
# signal_ggf_spin2_320_hh_bbvv:                           300.00k
# signal_ggf_spin2_350_hh_bbvv:                           300.00k
# signal_ggf_spin2_400_hh_bbvv:                           300.00k
# signal_ggf_spin2_450_hh_bbvv:                           300.00k
# signal_ggf_spin2_500_hh_bbvv:                           300.00k
# signal_ggf_spin2_550_hh_bbvv:                           300.00k
# signal_ggf_spin2_600_hh_bbvv:                           200.00k
# signal_ggf_spin2_650_hh_bbvv:                           200.00k
# signal_ggf_spin2_700_hh_bbvv:                           200.00k
# signal_ggf_spin2_750_hh_bbvv:                           200.00k
# signal_ggf_spin2_800_hh_bbvv:                           200.00k
# signal_ggf_spin2_850_hh_bbvv:                           197.00k
# signal_ggf_spin2_900_hh_bbvv:                           200.00k
# signal_ggf_spin2_1000_hh_bbvv:                          90.00k
# signal_ggf_spin2_1250_hh_bbvv:                          100.00k
# signal_ggf_spin2_1500_hh_bbvv:                          100.00k
# signal_ggf_spin2_1750_hh_bbvv:                          100.00k
# signal_ggf_spin2_2000_hh_bbvv:                          100.00k
# signal_ggf_spin2_2500_hh_bbvv:                          100.00k
# signal_ggf_spin2_3000_hh_bbvv:                          100.00k
# signal_vbf_nonresonant_1_1_1_hh_bbvv:                   400.00k
# signal_vbf_nonresonant_1_1_1_hh_bbvv_dipoleRecoilOn:    400.00k
# signal_vbf_nonresonant_1_1_2_hh_bbvv:                   396.00k
# signal_vbf_nonresonant_1_2_1_hh_bbvv:                   400.00k
# signal_vbf_nonresonant_1_2_1_hh_bbvv_dipoleRecoilOn:    400.00k
# signal_vbf_nonresonant_1_1_0_hh_bbvv:                   400.00k
# signal_vbf_nonresonant_1p5_1_1_hh_bbvv:                 400.00k
# signal_vbf_nonresonant_0p5_1_1_hh_bbvv:                 400.00k
# signal_vbf_nonresonant_1_0_1_hh_bbvv:                   400.00k
# signal_ggf_nonresonant_hh_bbvv:                         5.20M
# signal_ggf_nonresonant_cHHH0_hh_bbvv:                   383.10k
# signal_ggf_nonresonant_cHHH1_hh_bbvv:                   400.00k
# signal_ggf_nonresonant_cHHH2p45_hh_bbvv:                400.00k
# signal_ggf_nonresonant_cHHH5_hh_bbvv:                   400.00k
# signal_ggf_nonresonant_hh_bbvv_sl:                      4.79M
# signal_ggf_nonresonant_cHHH0_hh_bbvv_sl:                400.00k
# signal_ggf_nonresonant_cHHH1_hh_bbvv_sl:                391.40k
# signal_ggf_nonresonant_cHHH2p45_hh_bbvv_sl:             383.10k
# signal_ggf_nonresonant_cHHH5_hh_bbvv_sl:                390.20k
# signal_ggf_spin0_250_hh_bbvv_sl:                        400.00k
# signal_ggf_spin0_260_hh_bbvv_sl:                        400.00k
# signal_ggf_spin0_270_hh_bbvv_sl:                        400.00k
# signal_ggf_spin0_280_hh_bbvv_sl:                        400.00k
# signal_ggf_spin0_300_hh_bbvv_sl:                        300.00k
# signal_ggf_spin0_320_hh_bbvv_sl:                        300.00k
# signal_ggf_spin0_350_hh_bbvv_sl:                        300.00k
# signal_ggf_spin0_400_hh_bbvv_sl:                        300.00k
# signal_ggf_spin0_450_hh_bbvv_sl:                        300.00k
# signal_ggf_spin0_500_hh_bbvv_sl:                        300.00k
# signal_ggf_spin0_550_hh_bbvv_sl:                        258.00k
# signal_ggf_spin0_600_hh_bbvv_sl:                        200.00k
# signal_ggf_spin0_650_hh_bbvv_sl:                        200.00k
# signal_ggf_spin0_700_hh_bbvv_sl:                        200.00k
# signal_ggf_spin0_750_hh_bbvv_sl:                        200.00k
# signal_ggf_spin0_800_hh_bbvv_sl:                        200.00k
# signal_ggf_spin0_850_hh_bbvv_sl:                        200.00k
# signal_ggf_spin0_900_hh_bbvv_sl:                        200.00k
# signal_ggf_spin0_1000_hh_bbvv_sl:                       100.00k
# signal_ggf_spin0_1250_hh_bbvv_sl:                       100.00k
# signal_ggf_spin0_1500_hh_bbvv_sl:                       100.00k
# signal_ggf_spin0_1750_hh_bbvv_sl:                       100.00k
# signal_ggf_spin0_2000_hh_bbvv_sl:                       100.00k
# signal_ggf_spin0_2500_hh_bbvv_sl:                       100.00k
# signal_ggf_spin0_3000_hh_bbvv_sl:                       100.00k
# signal_ggf_spin2_250_hh_bbvv_sl:                        400.00k
# signal_ggf_spin2_260_hh_bbvv_sl:                        400.00k
# signal_ggf_spin2_270_hh_bbvv_sl:                        399.99k
# signal_ggf_spin2_280_hh_bbvv_sl:                        394.00k
# signal_ggf_spin2_300_hh_bbvv_sl:                        300.00k
# signal_ggf_spin2_320_hh_bbvv_sl:                        300.00k
# signal_ggf_spin2_350_hh_bbvv_sl:                        300.00k
# signal_ggf_spin2_400_hh_bbvv_sl:                        295.00k
# signal_ggf_spin2_450_hh_bbvv_sl:                        300.00k
# signal_ggf_spin2_500_hh_bbvv_sl:                        300.00k
# signal_ggf_spin2_550_hh_bbvv_sl:                        300.00k
# signal_ggf_spin2_600_hh_bbvv_sl:                        200.00k
# signal_ggf_spin2_650_hh_bbvv_sl:                        176.00k
# signal_ggf_spin2_700_hh_bbvv_sl:                        200.00k
# signal_ggf_spin2_750_hh_bbvv_sl:                        200.00k
# signal_ggf_spin2_800_hh_bbvv_sl:                        200.00k
# signal_ggf_spin2_850_hh_bbvv_sl:                        190.00k
# signal_ggf_spin2_900_hh_bbvv_sl:                        200.00k
# signal_ggf_spin2_1000_hh_bbvv_sl:                       100.00k
# signal_ggf_spin2_1250_hh_bbvv_sl:                       100.00k
# signal_ggf_spin2_1500_hh_bbvv_sl:                       100.00k
# signal_ggf_spin2_1750_hh_bbvv_sl:                       100.00k
# signal_ggf_spin2_2000_hh_bbvv_sl:                       100.00k
# signal_ggf_spin2_2500_hh_bbvv_sl:                       100.00k
# signal_ggf_spin2_3000_hh_bbvv_sl:                       100.00k
# signal_vbf_nonresonant_1_1_0_hh_bbvv_sl:                400.00k
# signal_vbf_nonresonant_1_1_1_hh_bbvv_sl:                400.00k
# signal_vbf_nonresonant_1_1_1_hh_bbvv_sl_dipoleRecoilOn: 400.00k
# signal_vbf_nonresonant_1_1_2_hh_bbvv_sl:                399.99k
# signal_vbf_nonresonant_1_2_1_hh_bbvv_sl:                400.00k
# signal_vbf_nonresonant_1_2_1_hh_bbvv_sl_dipoleRecoilOn: 400.00k
# signal_vbf_nonresonant_0p5_1_1_hh_bbvv_sl:              400.00k
# signal_vbf_nonresonant_1p5_1_1_hh_bbvv_sl:              400.00k
# signal_vbf_nonresonant_1_0_1_hh_bbvv_sl:                400.00k
# signal_vbf_spin0_250_hh_bbtt:                           400.00k
# signal_vbf_spin0_260_hh_bbtt:                           400.00k
# signal_vbf_spin0_270_hh_bbtt:                           384.00k
# signal_vbf_spin0_280_hh_bbtt:                           378.00k
# signal_vbf_spin0_300_hh_bbtt:                           300.00k
# signal_vbf_spin0_320_hh_bbtt:                           268.00k
# signal_vbf_spin0_350_hh_bbtt:                           300.00k
# signal_vbf_spin0_400_hh_bbtt:                           284.00k
# signal_vbf_spin0_450_hh_bbtt:                           300.00k
# signal_vbf_spin0_500_hh_bbtt:                           300.00k
# signal_vbf_spin0_550_hh_bbtt:                           292.00k
# signal_vbf_spin0_600_hh_bbtt:                           200.00k
# signal_vbf_spin0_650_hh_bbtt:                           192.00k
# signal_vbf_spin0_700_hh_bbtt:                           200.00k
# signal_vbf_spin0_750_hh_bbtt:                           192.00k
# signal_vbf_spin0_800_hh_bbtt:                           200.00k
# signal_vbf_spin0_850_hh_bbtt:                           200.00k
# signal_vbf_spin0_900_hh_bbtt:                           200.00k
# signal_vbf_spin0_1000_hh_bbtt:                          100.00k
# signal_vbf_spin0_1250_hh_bbtt:                          100.00k
# signal_vbf_spin0_1500_hh_bbtt:                          100.00k
# signal_vbf_spin0_1750_hh_bbtt:                          91.00k
# signal_vbf_spin0_2000_hh_bbtt:                          84.00k
# signal_vbf_spin0_3000_hh_bbtt:                          100.00k
# signal_vbf_spin2_250_hh_bbtt:                           400.00k
# signal_vbf_spin2_260_hh_bbtt:                           400.00k
# signal_vbf_spin2_270_hh_bbtt:                           384.00k
# signal_vbf_spin2_280_hh_bbtt:                           356.00k
# signal_vbf_spin2_300_hh_bbtt:                           300.00k
# signal_vbf_spin2_320_hh_bbtt:                           300.00k
# signal_vbf_spin2_350_hh_bbtt:                           290.00k
# signal_vbf_spin2_400_hh_bbtt:                           284.00k
# signal_vbf_spin2_450_hh_bbtt:                           295.00k
# signal_vbf_spin2_500_hh_bbtt:                           300.00k
# signal_vbf_spin2_600_hh_bbtt:                           192.00k
# signal_vbf_spin2_650_hh_bbtt:                           200.00k
# signal_vbf_spin2_700_hh_bbtt:                           200.00k
# signal_vbf_spin2_750_hh_bbtt:                           200.00k
# signal_vbf_spin2_850_hh_bbtt:                           200.00k
# signal_vbf_spin2_900_hh_bbtt:                           200.00k
# signal_vbf_spin2_1000_hh_bbtt:                          100.00k
# signal_vbf_spin2_1200_hh_bbtt:                          100.00k
# signal_vbf_spin2_1750_hh_bbtt:                          100.00k
# signal_vbf_spin2_2000_hh_bbtt:                          100.00k
# signal_ggf_spin0_250_hh_bbtt:                           400.00k
# signal_ggf_spin0_260_hh_bbtt:                           384.00k
# signal_ggf_spin0_270_hh_bbtt:                           400.00k
# signal_ggf_spin0_280_hh_bbtt:                           394.00k
# signal_ggf_spin0_300_hh_bbtt:                           282.00k
# signal_ggf_spin0_320_hh_bbtt:                           300.00k
# signal_ggf_spin0_340_hh_bbtt:                           300.00k
# signal_ggf_spin0_350_hh_bbtt:                           300.00k
# signal_ggf_spin0_400_hh_bbtt:                           300.00k
# signal_ggf_spin0_450_hh_bbtt:                           300.00k
# signal_ggf_spin0_500_hh_bbtt:                           279.00k
# signal_ggf_spin0_550_hh_bbtt:                           300.00k
# signal_ggf_spin0_600_hh_bbtt:                           200.00k
# signal_ggf_spin0_650_hh_bbtt:                           200.00k
# signal_ggf_spin0_700_hh_bbtt:                           190.00k
# signal_ggf_spin0_750_hh_bbtt:                           200.00k
# signal_ggf_spin0_800_hh_bbtt:                           200.00k
# signal_ggf_spin0_850_hh_bbtt:                           200.00k
# signal_ggf_spin0_900_hh_bbtt:                           200.00k
# signal_ggf_spin0_1000_hh_bbtt:                          100.00k
# signal_ggf_spin0_1250_hh_bbtt:                          100.00k
# signal_ggf_spin0_1500_hh_bbtt:                          100.00k
# signal_ggf_spin0_1750_hh_bbtt:                          100.00k
# signal_ggf_spin0_2000_hh_bbtt:                          100.00k
# signal_ggf_spin0_2500_hh_bbtt:                          75.00k
# signal_ggf_spin0_3000_hh_bbtt:                          100.00k
# signal_ggf_spin2_250_hh_bbtt:                           380.00k
# signal_ggf_spin2_260_hh_bbtt:                           382.00k
# signal_ggf_spin2_270_hh_bbtt:                           400.00k
# signal_ggf_spin2_280_hh_bbtt:                           380.00k
# signal_ggf_spin2_300_hh_bbtt:                           276.00k
# signal_ggf_spin2_320_hh_bbtt:                           300.00k
# signal_ggf_spin2_340_hh_bbtt:                           300.00k
# signal_ggf_spin2_350_hh_bbtt:                           300.00k
# signal_ggf_spin2_400_hh_bbtt:                           300.00k
# signal_ggf_spin2_450_hh_bbtt:                           300.00k
# signal_ggf_spin2_500_hh_bbtt:                           300.00k
# signal_ggf_spin2_550_hh_bbtt:                           300.00k
# signal_ggf_spin2_600_hh_bbtt:                           200.00k
# signal_ggf_spin2_650_hh_bbtt:                           200.00k
# signal_ggf_spin2_700_hh_bbtt:                           200.00k
# signal_ggf_spin2_750_hh_bbtt:                           200.00k
# signal_ggf_spin2_800_hh_bbtt:                           200.00k
# signal_ggf_spin2_850_hh_bbtt:                           190.00k
# signal_ggf_spin2_900_hh_bbtt:                           200.00k
# signal_ggf_spin2_1000_hh_bbtt:                          100.00k
# signal_ggf_spin2_1250_hh_bbtt:                          100.00k
# signal_ggf_spin2_1500_hh_bbtt:                          100.00k
# signal_ggf_spin2_1750_hh_bbtt:                          100.00k
# signal_ggf_spin2_2000_hh_bbtt:                          100.00k
# signal_ggf_spin2_2500_hh_bbtt:                          100.00k
# signal_ggf_spin2_3000_hh_bbtt:                          100.00k
# signal_vbf_nonresonant_1_1_0_hh_bbtt:                   1.00M
# signal_vbf_nonresonant_1_1_1_hh_bbtt:                   2.00M
# signal_vbf_nonresonant_1_1_1_hh_bbtt_dipoleRecoilOn:    1.00M
# signal_vbf_nonresonant_1_1_2_hh_bbtt:                   997.00k
# signal_vbf_nonresonant_1_2_1_hh_bbtt:                   2.00M
# signal_vbf_nonresonant_1_2_1_hh_bbtt_dipoleRecoilOn:    1.00M
# signal_vbf_nonresonant_1p5_1_1_hh_bbtt:                 1.00M
# signal_vbf_nonresonant_0p5_1_1_hh_bbtt:                 992.00k
# signal_vbf_nonresonant_1_0_1_hh_bbtt:                   2.50M
# signal_ggf_nonresonant_hh_bbtt:                         4.71M
# signal_ggf_nonresonant_cHHH0_hh_bbtt:                   1.00M
# signal_ggf_nonresonant_cHHH1_hh_bbtt:                   1.00M
# signal_ggf_nonresonant_cHHH2p45_hh_bbtt:                1.00M
# signal_ggf_nonresonant_cHHH5_hh_bbtt:                   1.00M

