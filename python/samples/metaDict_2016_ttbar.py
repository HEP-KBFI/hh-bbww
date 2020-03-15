from collections import OrderedDict as OD

# file generated at 2020-03-15 14:30:04 with the following command:
# find_samples.py -V -i ../../tthAnalysis/NanoAOD/test/datasets/txt/datasets_ttbar_mc_2016_RunIISummer16MiniAODv3.txt -m python/samples/metaDict_2016_ttbar.py -s ../../tthAnalysis/NanoAOD/test/datasets/txt/sum_datasets_ttbar_2016_RunIISummer16MiniAODv3.txt

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
  ("crab_string",           ""),
  ("sample_category",       "TT_hdampDown"),
  ("process_name_specific", "TTTo2L2Nu_hdampDOWN"),
  ("nof_db_events",         9963900),
  ("nof_db_files",          143),
  ("fsize_db",              440499394219),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 440.50GB; nevents: 9.96M; release: 9_4_9; last modified: 2020-01-09 12:35:35"),
])

meta_dictionary["/TTTo2L2Nu_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_hdampDown"),
  ("process_name_specific", "TTTo2L2Nu_hdampDOWN_ext1"),
  ("nof_db_events",         4944800),
  ("nof_db_files",          112),
  ("fsize_db",              218167419681),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 218.17GB; nevents: 4.94M; release: 9_4_9; last modified: 2020-02-18 19:40:33"),
])

meta_dictionary["/TTToSemiLeptonic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_hdampDown"),
  ("process_name_specific", "TTToSemiLeptonic_hdampDOWN"),
  ("nof_db_events",         29818400),
  ("nof_db_files",          414),
  ("fsize_db",              1348075651578),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.35TB; nevents: 29.82M; release: 9_4_9; last modified: 2020-02-08 10:12:20"),
])

meta_dictionary["/TTToHadronic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_hdampDown"),
  ("process_name_specific", "TTToHadronic_hdampDOWN"),
  ("nof_db_events",         28900700),
  ("nof_db_files",          411),
  ("fsize_db",              1338002370689),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: PRODUCTION; size: 1.34TB; nevents: 28.90M; release: 9_4_9; last modified: 2020-01-26 03:33:58"),
])

meta_dictionary["/TTTo2L2Nu_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_hdampUp"),
  ("process_name_specific", "TTTo2L2Nu_hdampUP"),
  ("nof_db_events",         9923800),
  ("nof_db_files",          143),
  ("fsize_db",              440216123353),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 440.22GB; nevents: 9.92M; release: 9_4_9; last modified: 2020-02-15 17:46:58"),
])

meta_dictionary["/TTTo2L2Nu_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_hdampUp"),
  ("process_name_specific", "TTTo2L2Nu_hdampUP_ext1"),
  ("nof_db_events",         4965300),
  ("nof_db_files",          93),
  ("fsize_db",              220079948375),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 220.08GB; nevents: 4.97M; release: 9_4_9; last modified: 2020-02-28 23:21:34"),
])

meta_dictionary["/TTToSemiLeptonic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_hdampUp"),
  ("process_name_specific", "TTToSemiLeptonic_hdampUP"),
  ("nof_db_events",         29671272),
  ("nof_db_files",          385),
  ("fsize_db",              1349067910706),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.35TB; nevents: 29.67M; release: 9_4_9; last modified: 2020-02-07 13:32:59"),
])

meta_dictionary["/TTToHadronic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_hdampUp"),
  ("process_name_specific", "TTToHadronic_hdampUP"),
  ("nof_db_events",         28695100),
  ("nof_db_files",          396),
  ("fsize_db",              1337128214755),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.34TB; nevents: 28.70M; release: 9_4_9; last modified: 2020-01-16 21:45:00"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_ueDown"),
  ("process_name_specific", "TTTo2L2Nu_ueDown"),
  ("nof_db_events",         9414200),
  ("nof_db_files",          136),
  ("fsize_db",              414089278252),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 414.09GB; nevents: 9.41M; release: 9_4_9; last modified: 2020-03-03 17:41:09"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_ueDown"),
  ("process_name_specific", "TTTo2L2Nu_ueDown_ext1"),
  ("nof_db_events",         4952600),
  ("nof_db_files",          95),
  ("fsize_db",              217895870557),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 217.90GB; nevents: 4.95M; release: 9_4_9; last modified: 2020-03-02 23:52:11"),
])

meta_dictionary["/TTToSemiLeptonic_TuneCP5down_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_ueDown"),
  ("process_name_specific", "TTToSemiLeptonic_ueDown"),
  ("nof_db_events",         28497700),
  ("nof_db_files",          399),
  ("fsize_db",              1285392016857),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: PRODUCTION; size: 1.29TB; nevents: 28.50M; release: 9_4_9; last modified: 2019-12-17 20:46:14"),
])

meta_dictionary["/TTToHadronic_TuneCP5down_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_ueDown"),
  ("process_name_specific", "TTToHadronic_ueDown"),
  ("nof_db_events",         27873700),
  ("nof_db_files",          371),
  ("fsize_db",              1287732920696),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: PRODUCTION; size: 1.29TB; nevents: 27.87M; release: 9_4_9; last modified: 2019-12-11 04:48:09"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_ueUp"),
  ("process_name_specific", "TTTo2L2Nu_ueUp"),
  ("nof_db_events",         9851000),
  ("nof_db_files",          144),
  ("fsize_db",              436397875157),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 436.40GB; nevents: 9.85M; release: 9_4_9; last modified: 2020-02-27 02:29:17"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_ueUp"),
  ("process_name_specific", "TTTo2L2Nu_ueUp_ext1"),
  ("nof_db_events",         4987600),
  ("nof_db_files",          79),
  ("fsize_db",              220909282587),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 220.91GB; nevents: 4.99M; release: 9_4_9; last modified: 2020-02-13 09:02:27"),
])

meta_dictionary["/TTToSemiLeptonic_TuneCP5up_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_ueUp"),
  ("process_name_specific", "TTToSemiLeptonic_ueUp"),
  ("nof_db_events",         29239200),
  ("nof_db_files",          360),
  ("fsize_db",              1326440207303),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.33TB; nevents: 29.24M; release: 9_4_9; last modified: 2020-03-03 17:41:30"),
])

meta_dictionary["/TTToHadronic_TuneCP5up_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_ueUp"),
  ("process_name_specific", "TTToHadronic_ueUp"),
  ("nof_db_events",         27939400),
  ("nof_db_files",          400),
  ("fsize_db",              1300075329090),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: PRODUCTION; size: 1.30TB; nevents: 27.94M; release: 9_4_9; last modified: 2019-12-16 04:25:29"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_QCDbased"),
  ("process_name_specific", "TTTo2L2Nu_QCDbased"),
  ("nof_db_events",         14846400),
  ("nof_db_files",          186),
  ("fsize_db",              663165284807),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 663.17GB; nevents: 14.85M; release: 9_4_9; last modified: 2020-02-22 07:46:17"),
])

meta_dictionary["/TTToSemiLeptonic_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_QCDbased"),
  ("process_name_specific", "TTToSemiLeptonic_QCDbased"),
  ("nof_db_events",         28718400),
  ("nof_db_files",          428),
  ("fsize_db",              1317068289434),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: PRODUCTION; size: 1.32TB; nevents: 28.72M; release: 9_4_9; last modified: 2020-01-29 16:13:35"),
])

meta_dictionary["/TTToHadronic_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_QCDbased"),
  ("process_name_specific", "TTToHadronic_QCDbased"),
  ("nof_db_events",         25102200),
  ("nof_db_files",          301),
  ("fsize_db",              1177063813417),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: PRODUCTION; size: 1.18TB; nevents: 25.10M; release: 9_4_9; last modified: 2020-01-28 15:08:39"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_GluonMove"),
  ("process_name_specific", "TTTo2L2Nu_GluonMove"),
  ("nof_db_events",         12127000),
  ("nof_db_files",          193),
  ("fsize_db",              536687854163),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: PRODUCTION; size: 536.69GB; nevents: 12.13M; release: 9_4_9; last modified: 2020-01-24 00:07:28"),
])

meta_dictionary["/TTToSemiLeptonic_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_GluonMove"),
  ("process_name_specific", "TTToSemiLeptonic_GluonMove"),
  ("nof_db_events",         25638900),
  ("nof_db_files",          313),
  ("fsize_db",              1160985967313),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: PRODUCTION; size: 1.16TB; nevents: 25.64M; release: 9_4_9; last modified: 2020-01-29 05:47:48"),
])

meta_dictionary["/TTToHadronic_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_GluonMove"),
  ("process_name_specific", "TTToHadronic_GluonMove"),
  ("nof_db_events",         23761000),
  ("nof_db_files",          314),
  ("fsize_db",              1103458992483),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: PRODUCTION; size: 1.10TB; nevents: 23.76M; release: 9_4_9; last modified: 2020-01-28 01:16:35"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5_PSweights_erdON_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_erdON"),
  ("process_name_specific", "TTTo2L2Nu_erdON"),
  ("nof_db_events",         9725600),
  ("nof_db_files",          215),
  ("fsize_db",              432559736598),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 432.56GB; nevents: 9.73M; release: 9_4_9; last modified: 2020-03-03 17:42:14"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5_PSweights_erdON_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_erdON"),
  ("process_name_specific", "TTTo2L2Nu_erdON_ext1"),
  ("nof_db_events",         4775400),
  ("nof_db_files",          127),
  ("fsize_db",              211669902969),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: PRODUCTION; size: 211.67GB; nevents: 4.78M; release: 9_4_9; last modified: 2020-01-22 16:08:22"),
])

meta_dictionary["/TTToSemiLeptonic_TuneCP5_PSweights_erdON_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_erdON"),
  ("process_name_specific", "TTToSemiLeptonic_erdON"),
  ("nof_db_events",         28973400),
  ("nof_db_files",          433),
  ("fsize_db",              1316453559336),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: PRODUCTION; size: 1.32TB; nevents: 28.97M; release: 9_4_9; last modified: 2020-01-22 14:55:16"),
])

meta_dictionary["/TTToHadronic_TuneCP5_PSweights_erdON_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_erdON"),
  ("process_name_specific", "TTToHadronic_erdON"),
  ("nof_db_events",         23957400),
  ("nof_db_files",          369),
  ("fsize_db",              1115641687969),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: PRODUCTION; size: 1.12TB; nevents: 23.96M; release: 9_4_9; last modified: 2020-01-21 03:52:27"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5_PSweights_mtop1695_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_backup_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_mtop169p5"),
  ("process_name_specific", "TTTo2L2Nu_mtop169p5_PSweights_backup"),
  ("nof_db_events",         989200),
  ("nof_db_files",          9),
  ("fsize_db",              43359624747),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: PRODUCTION; size: 43.36GB; nevents: 989.20k; release: 9_4_9; last modified: 2020-02-25 19:42:34"),
])

meta_dictionary["/TTToSemiLeptonic_TuneCP5_PSweights_mtop1695_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_backup_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_mtop169p5"),
  ("process_name_specific", "TTToSemiLeptonic_mtop169p5_PSweights_backup"),
  ("nof_db_events",         2042800),
  ("nof_db_files",          21),
  ("fsize_db",              91708676625),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: PRODUCTION; size: 91.71GB; nevents: 2.04M; release: 9_4_9; last modified: 2020-02-24 22:19:47"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5_PSweights_mtop1755_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_backup_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_mtop175p5"),
  ("process_name_specific", "TTTo2L2Nu_mtop175p5_PSweights_backup"),
  ("nof_db_events",         610400),
  ("nof_db_files",          8),
  ("fsize_db",              26943322663),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: PRODUCTION; size: 26.94GB; nevents: 610.40k; release: 9_4_9; last modified: 2020-03-02 18:59:19"),
])

meta_dictionary["/TTToSemiLeptonic_TuneCP5_PSweights_mtop1755_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_backup_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_mtop175p5"),
  ("process_name_specific", "TTToSemiLeptonic_mtop175p5_PSweights_backup"),
  ("nof_db_events",         591000),
  ("nof_db_files",          7),
  ("fsize_db",              26706453712),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: PRODUCTION; size: 26.71GB; nevents: 591.00k; release: 9_4_9; last modified: 2020-03-07 19:40:08"),
])


# event statistics by sample category:
# TT_hdampDown: 73.63M
# TT_hdampUp:   73.26M
# TT_ueDown:    70.74M
# TT_ueUp:      72.02M
# TT_QCDbased:  68.67M
# TT_GluonMove: 61.53M
# TT_erdON:     67.43M
# TT_mtop169p5: 3.03M
# TT_mtop175p5: 1.20M

