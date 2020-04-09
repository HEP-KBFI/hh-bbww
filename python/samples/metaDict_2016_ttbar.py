from collections import OrderedDict as OD

# file generated at 2020-04-09 20:16:34 with the following command:
# find_samples.py -V -i ../../tthAnalysis/NanoAOD/test/datasets/txt/datasets_ttbar_mc_2016_RunIISummer16MiniAODv3.txt -m python/samples/metaDict_2016_ttbar.py -s ../../tthAnalysis/NanoAOD/test/datasets/txt/sum_datasets_ttbar_2016_RunIISummer16MiniAODv3.txt -c python/samples/sampleLocations_2016_nanoAOD_ttbar.txt

meta_dictionary = OD()


### event sums

sum_events = { 
  ("TTTo2L2Nu_hdampDOWN", "TTTo2L2Nu_hdampDOWN_ext1"),
  ("TTTo2L2Nu_hdampUP", "TTTo2L2Nu_hdampUP_ext1"),
  ("TTTo2L2Nu_ueDown", "TTTo2L2Nu_ueDown_ext1"),
  ("TTTo2L2Nu_ueUp", "TTTo2L2Nu_ueUp_ext1"),
  ("TTTo2L2Nu_erdON", "TTTo2L2Nu_erdON_ext1"),
}


meta_dictionary["/TTTo2L2Nu_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Mar31_TTTo2L2Nu_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1"),
  ("sample_category",       "TT_hdampDown"),
  ("process_name_specific", "TTTo2L2Nu_hdampDOWN"),
  ("nof_db_events",         9963900),
  ("nof_db_files",          143),
  ("fsize_db",              440499394219),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 440.50GB; nevents: 9.96M; release: 9_4_9; last modified: 2020-01-09 12:35:35"),
])

meta_dictionary["/TTTo2L2Nu_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Mar31_TTTo2L2Nu_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1"),
  ("sample_category",       "TT_hdampDown"),
  ("process_name_specific", "TTTo2L2Nu_hdampDOWN_ext1"),
  ("nof_db_events",         4944800),
  ("nof_db_files",          112),
  ("fsize_db",              218167419681),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 218.17GB; nevents: 4.94M; release: 9_4_9; last modified: 2020-02-18 19:40:33"),
])

meta_dictionary["/TTToSemiLeptonic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Mar31_TTToSemiLeptonic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1"),
  ("sample_category",       "TT_hdampDown"),
  ("process_name_specific", "TTToSemiLeptonic_hdampDOWN"),
  ("nof_db_events",         29818400),
  ("nof_db_files",          414),
  ("fsize_db",              1348075651578),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "86.29%; status: VALID; size: 1.35TB; nevents: 29.82M; release: 9_4_9; last modified: 2020-02-08 10:12:20"),
])

meta_dictionary["/TTToHadronic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Mar31_TTToHadronic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"),
  ("sample_category",       "TT_hdampDown"),
  ("process_name_specific", "TTToHadronic_hdampDOWN"),
  ("nof_db_events",         28900700),
  ("nof_db_files",          411),
  ("fsize_db",              1338002370689),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "89.77%; status: VALID; size: 1.34TB; nevents: 28.90M; release: 9_4_9; last modified: 2020-03-18 13:51:40"),
])

meta_dictionary["/TTTo2L2Nu_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Mar31_TTTo2L2Nu_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1"),
  ("sample_category",       "TT_hdampUp"),
  ("process_name_specific", "TTTo2L2Nu_hdampUP"),
  ("nof_db_events",         9923800),
  ("nof_db_files",          143),
  ("fsize_db",              440216123353),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 440.22GB; nevents: 9.92M; release: 9_4_9; last modified: 2020-02-15 17:46:58"),
])

meta_dictionary["/TTTo2L2Nu_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Mar31_TTTo2L2Nu_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1"),
  ("sample_category",       "TT_hdampUp"),
  ("process_name_specific", "TTTo2L2Nu_hdampUP_ext1"),
  ("nof_db_events",         4965300),
  ("nof_db_files",          93),
  ("fsize_db",              220079948375),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "54.0%; status: VALID; size: 220.08GB; nevents: 4.97M; release: 9_4_9; last modified: 2020-02-28 23:21:34"),
])

meta_dictionary["/TTToSemiLeptonic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Mar31_TTToSemiLeptonic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1"),
  ("sample_category",       "TT_hdampUp"),
  ("process_name_specific", "TTToSemiLeptonic_hdampUP"),
  ("nof_db_events",         29671272),
  ("nof_db_files",          385),
  ("fsize_db",              1349067910706),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "10.4%; status: VALID; size: 1.35TB; nevents: 29.67M; release: 9_4_9; last modified: 2020-02-07 13:32:59"),
])

meta_dictionary["/TTToHadronic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Mar31_TTToHadronic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1"),
  ("sample_category",       "TT_hdampUp"),
  ("process_name_specific", "TTToHadronic_hdampUP"),
  ("nof_db_events",         28695100),
  ("nof_db_files",          396),
  ("fsize_db",              1337128214755),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "42.36%; status: VALID; size: 1.34TB; nevents: 28.70M; release: 9_4_9; last modified: 2020-01-16 21:45:00"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Mar31_TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1"),
  ("sample_category",       "TT_ueDown"),
  ("process_name_specific", "TTTo2L2Nu_ueDown"),
  ("nof_db_events",         9414200),
  ("nof_db_files",          136),
  ("fsize_db",              414089278252),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "95.79%; status: VALID; size: 414.09GB; nevents: 9.41M; release: 9_4_9; last modified: 2020-03-03 17:41:09"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Mar31_TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1"),
  ("sample_category",       "TT_ueDown"),
  ("process_name_specific", "TTTo2L2Nu_ueDown_ext1"),
  ("nof_db_events",         4952600),
  ("nof_db_files",          95),
  ("fsize_db",              217895870557),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 217.90GB; nevents: 4.95M; release: 9_4_9; last modified: 2020-03-02 23:52:11"),
])

meta_dictionary["/TTToSemiLeptonic_TuneCP5down_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Mar31_TTToSemiLeptonic_TuneCP5down_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1"),
  ("sample_category",       "TT_ueDown"),
  ("process_name_specific", "TTToSemiLeptonic_ueDown"),
  ("nof_db_events",         28951700),
  ("nof_db_files",          415),
  ("fsize_db",              1305952192284),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "77.24%; status: VALID; size: 1.31TB; nevents: 28.95M; release: 9_4_9; last modified: 2020-03-19 01:45:07"),
])

meta_dictionary["/TTToHadronic_TuneCP5down_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Mar31_TTToHadronic_TuneCP5down_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1"),
  ("sample_category",       "TT_ueDown"),
  ("process_name_specific", "TTToHadronic_ueDown"),
  ("nof_db_events",         27921200),
  ("nof_db_files",          372),
  ("fsize_db",              1289925205797),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "97.97%; status: VALID; size: 1.29TB; nevents: 27.92M; release: 9_4_9; last modified: 2020-03-18 15:55:46"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Mar31_TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1"),
  ("sample_category",       "TT_ueUp"),
  ("process_name_specific", "TTTo2L2Nu_ueUp"),
  ("nof_db_events",         9851000),
  ("nof_db_files",          144),
  ("fsize_db",              436397875157),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "80.81%; status: VALID; size: 436.40GB; nevents: 9.85M; release: 9_4_9; last modified: 2020-02-27 02:29:17"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Mar31_TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1"),
  ("sample_category",       "TT_ueUp"),
  ("process_name_specific", "TTTo2L2Nu_ueUp_ext1"),
  ("nof_db_events",         4987600),
  ("nof_db_files",          79),
  ("fsize_db",              220909282587),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 220.91GB; nevents: 4.99M; release: 9_4_9; last modified: 2020-02-13 09:02:27"),
])

meta_dictionary["/TTToSemiLeptonic_TuneCP5up_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Mar31_TTToSemiLeptonic_TuneCP5up_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1"),
  ("sample_category",       "TT_ueUp"),
  ("process_name_specific", "TTToSemiLeptonic_ueUp"),
  ("nof_db_events",         29239200),
  ("nof_db_files",          360),
  ("fsize_db",              1326440207303),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "0.34%; status: VALID; size: 1.33TB; nevents: 29.24M; release: 9_4_9; last modified: 2020-03-03 17:41:30"),
])

meta_dictionary["/TTToHadronic_TuneCP5up_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Mar31_TTToHadronic_TuneCP5up_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1"),
  ("sample_category",       "TT_ueUp"),
  ("process_name_specific", "TTToHadronic_ueUp"),
  ("nof_db_events",         27939400),
  ("nof_db_files",          400),
  ("fsize_db",              1300075329090),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "94.66%; status: VALID; size: 1.30TB; nevents: 27.94M; release: 9_4_9; last modified: 2020-03-19 01:45:22"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Mar31_TTTo2L2Nu_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1"),
  ("sample_category",       "TT_QCDbased"),
  ("process_name_specific", "TTTo2L2Nu_QCDbased"),
  ("nof_db_events",         14846400),
  ("nof_db_files",          186),
  ("fsize_db",              663165284807),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 663.17GB; nevents: 14.85M; release: 9_4_9; last modified: 2020-02-22 07:46:17"),
])

meta_dictionary["/TTToSemiLeptonic_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Mar31_TTToSemiLeptonic_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1"),
  ("sample_category",       "TT_QCDbased"),
  ("process_name_specific", "TTToSemiLeptonic_QCDbased"),
  ("nof_db_events",         29208200),
  ("nof_db_files",          458),
  ("fsize_db",              1339803390539),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 1.34TB; nevents: 29.21M; release: 9_4_9; last modified: 2020-03-19 01:44:57"),
])

meta_dictionary["/TTToHadronic_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Mar31_TTToHadronic_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1"),
  ("sample_category",       "TT_QCDbased"),
  ("process_name_specific", "TTToHadronic_QCDbased"),
  ("nof_db_events",         27446200),
  ("nof_db_files",          352),
  ("fsize_db",              1287103451975),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "99.66%; status: VALID; size: 1.29TB; nevents: 27.45M; release: 9_4_9; last modified: 2020-03-31 22:01:04"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Mar31_TTTo2L2Nu_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1"),
  ("sample_category",       "TT_GluonMove"),
  ("process_name_specific", "TTTo2L2Nu_GluonMove"),
  ("nof_db_events",         13536900),
  ("nof_db_files",          223),
  ("fsize_db",              599132456619),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: PRODUCTION; size: 599.13GB; nevents: 13.54M; release: 9_4_9; last modified: 2020-01-24 00:07:28"),
])

meta_dictionary["/TTToSemiLeptonic_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Mar31_TTToSemiLeptonic_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1"),
  ("sample_category",       "TT_GluonMove"),
  ("process_name_specific", "TTToSemiLeptonic_GluonMove"),
  ("nof_db_events",         26468200),
  ("nof_db_files",          322),
  ("fsize_db",              1198509880349),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 1.20TB; nevents: 26.47M; release: 9_4_9; last modified: 2020-03-27 13:00:04"),
])

meta_dictionary["/TTToHadronic_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Mar31_TTToHadronic_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1"),
  ("sample_category",       "TT_GluonMove"),
  ("process_name_specific", "TTToHadronic_GluonMove"),
  ("nof_db_events",         28881600),
  ("nof_db_files",          413),
  ("fsize_db",              1342210039307),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 1.34TB; nevents: 28.88M; release: 9_4_9; last modified: 2020-04-01 03:52:25"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5_PSweights_erdON_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Mar31_TTTo2L2Nu_TuneCP5_PSweights_erdON_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1"),
  ("sample_category",       "TT_erdON"),
  ("process_name_specific", "TTTo2L2Nu_erdON"),
  ("nof_db_events",         9725600),
  ("nof_db_files",          215),
  ("fsize_db",              432559736598),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "88.78%; status: VALID; size: 432.56GB; nevents: 9.73M; release: 9_4_9; last modified: 2020-03-03 17:42:14"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5_PSweights_erdON_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Mar31_TTTo2L2Nu_TuneCP5_PSweights_erdON_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1"),
  ("sample_category",       "TT_erdON"),
  ("process_name_specific", "TTTo2L2Nu_erdON_ext1"),
  ("nof_db_events",         4837600),
  ("nof_db_files",          130),
  ("fsize_db",              214453762002),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 214.45GB; nevents: 4.84M; release: 9_4_9; last modified: 2020-03-26 01:50:53"),
])

meta_dictionary["/TTToSemiLeptonic_TuneCP5_PSweights_erdON_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Mar31_TTToSemiLeptonic_TuneCP5_PSweights_erdON_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1"),
  ("sample_category",       "TT_erdON"),
  ("process_name_specific", "TTToSemiLeptonic_erdON"),
  ("nof_db_events",         28973400),
  ("nof_db_files",          433),
  ("fsize_db",              1316453559336),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "34.87%; status: VALID; size: 1.32TB; nevents: 28.97M; release: 9_4_9; last modified: 2020-03-18 13:51:28"),
])

meta_dictionary["/TTToHadronic_TuneCP5_PSweights_erdON_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Mar31_TTToHadronic_TuneCP5_PSweights_erdON_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1"),
  ("sample_category",       "TT_erdON"),
  ("process_name_specific", "TTToHadronic_erdON"),
  ("nof_db_events",         27338000),
  ("nof_db_files",          424),
  ("fsize_db",              1273462459025),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "99.3%; status: VALID; size: 1.27TB; nevents: 27.34M; release: 9_4_9; last modified: 2020-03-27 12:58:49"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5_PSweights_mtop1695_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_backup_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Mar31_TTTo2L2Nu_TuneCP5_PSweights_mtop1695_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_backup_94X_mcRun2_asymptotic_v3-v1"),
  ("sample_category",       "TT_mtop169p5"),
  ("process_name_specific", "TTTo2L2Nu_mtop169p5_PSweights_backup"),
  ("nof_db_events",         1294000),
  ("nof_db_files",          12),
  ("fsize_db",              56723913520),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: PRODUCTION; size: 56.72GB; nevents: 1.29M; release: 9_4_9; last modified: 2020-02-25 19:42:34"),
])

meta_dictionary["/TTToSemiLeptonic_TuneCP5_PSweights_mtop1695_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_backup_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Mar31_TTToSemiLeptonic_TuneCP5_PSweights_mtop1695_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_backup_94X_mcRun2_asymptotic_v3-v1"),
  ("sample_category",       "TT_mtop169p5"),
  ("process_name_specific", "TTToSemiLeptonic_mtop169p5_PSweights_backup"),
  ("nof_db_events",         3197800),
  ("nof_db_files",          32),
  ("fsize_db",              143556579755),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: PRODUCTION; size: 143.56GB; nevents: 3.20M; release: 9_4_9; last modified: 2020-02-24 22:19:47"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5_PSweights_mtop1755_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_backup_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Mar31_TTTo2L2Nu_TuneCP5_PSweights_mtop1755_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_backup_94X_mcRun2_asymptotic_v3-v1"),
  ("sample_category",       "TT_mtop175p5"),
  ("process_name_specific", "TTTo2L2Nu_mtop175p5_PSweights_backup"),
  ("nof_db_events",         2431800),
  ("nof_db_files",          72),
  ("fsize_db",              108213630785),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: PRODUCTION; size: 108.21GB; nevents: 2.43M; release: 9_4_9; last modified: 2020-03-02 18:59:19"),
])

meta_dictionary["/TTToSemiLeptonic_TuneCP5_PSweights_mtop1755_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_backup_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2016v3_2020Mar31_TTToSemiLeptonic_TuneCP5_PSweights_mtop1755_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_backup_94X_mcRun2_asymptotic_v3-v1"),
  ("sample_category",       "TT_mtop175p5"),
  ("process_name_specific", "TTToSemiLeptonic_mtop175p5_PSweights_backup"),
  ("nof_db_events",         2703600),
  ("nof_db_files",          31),
  ("fsize_db",              122243863139),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "96.67%; status: PRODUCTION; size: 122.24GB; nevents: 2.70M; release: 9_4_9; last modified: 2020-03-07 19:40:08"),
])


# event statistics by sample category:
# TT_hdampDown: 73.63M
# TT_hdampUp:   73.26M
# TT_ueDown:    71.24M
# TT_ueUp:      72.02M
# TT_QCDbased:  71.50M
# TT_GluonMove: 68.89M
# TT_erdON:     70.87M
# TT_mtop169p5: 4.49M
# TT_mtop175p5: 5.14M

