from collections import OrderedDict as OD

# file generated at 2020-03-15 14:37:09 with the following command:
# find_samples.py -V -i ../../tthAnalysis/NanoAOD/test/datasets/txt/datasets_ttbar_mc_2018_RunIIAutumn18MiniAOD.txt -m python/samples/metaDict_2018_ttbar.py -s ../../tthAnalysis/NanoAOD/test/datasets/txt/sum_datasets_ttbar_2018_RunIIAutumn18MiniAOD.txt

meta_dictionary = OD()


### event sums

sum_events = { 
  ("TTTo2L2Nu_hdampDOWN", "TTTo2L2Nu_hdampDOWN_ext1"),
  ("TTTo2L2Nu_hdampUP", "TTTo2L2Nu_hdampUP_ext1"),
  ("TTTo2L2Nu_ueDown", "TTTo2L2Nu_ueDown_ext1"),
  ("TTTo2L2Nu_ueUp", "TTTo2L2Nu_ueUp_ext1"),
  ("TTTo2L2Nu_erdON", "TTTo2L2Nu_erdON_ext1"),
  ("TTTo2L2Nu_mtop169p5", "TTTo2L2Nu_mtop169p5_ext1"),
  ("TTToSemiLeptonic_mtop169p5", "TTToSemiLeptonic_mtop169p5_ext1"),
  ("TTTo2L2Nu_mtop175p5", "TTTo2L2Nu_mtop175p5_ext1"),
  ("TTToSemiLeptonic_mtop175p5", "TTToSemiLeptonic_mtop175p5_ext1"),
}


meta_dictionary["/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_hdampDown"),
  ("process_name_specific", "TTTo2L2Nu_hdampDOWN"),
  ("nof_db_events",         5458000),
  ("nof_db_files",          158),
  ("fsize_db",              289530779054),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 289.53GB; nevents: 5.46M; release: 10_2_5; last modified: 2019-02-10 05:36:37"),
])

meta_dictionary["/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_hdampDown"),
  ("process_name_specific", "TTTo2L2Nu_hdampDOWN_ext1"),
  ("nof_db_events",         9952000),
  ("nof_db_files",          264),
  ("fsize_db",              527737712006),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 527.74GB; nevents: 9.95M; release: 10_2_5; last modified: 2020-03-02 19:40:17"),
])

meta_dictionary["/TTToSemiLeptonic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_hdampDown"),
  ("process_name_specific", "TTToSemiLeptonic_hdampDOWN"),
  ("nof_db_events",         25904000),
  ("nof_db_files",          695),
  ("fsize_db",              1388433897628),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.39TB; nevents: 25.90M; release: 10_2_5; last modified: 2019-02-18 15:17:08"),
])

meta_dictionary["/TTToHadronic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_hdampDown"),
  ("process_name_specific", "TTToHadronic_hdampDOWN"),
  ("nof_db_events",         26425000),
  ("nof_db_files",          729),
  ("fsize_db",              1432904122912),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.43TB; nevents: 26.43M; release: 10_2_5; last modified: 2018-12-31 01:52:42"),
])

meta_dictionary["/TTTo2L2Nu_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_hdampUp"),
  ("process_name_specific", "TTTo2L2Nu_hdampUP"),
  ("nof_db_events",         5260000),
  ("nof_db_files",          148),
  ("fsize_db",              280579235973),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 280.58GB; nevents: 5.26M; release: 10_2_5; last modified: 2018-12-10 17:55:54"),
])

meta_dictionary["/TTTo2L2Nu_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_hdampUp"),
  ("process_name_specific", "TTTo2L2Nu_hdampUP_ext1"),
  ("nof_db_events",         9903000),
  ("nof_db_files",          314),
  ("fsize_db",              529852266703),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 529.85GB; nevents: 9.90M; release: 10_2_5; last modified: 2020-03-02 00:54:35"),
])

meta_dictionary["/TTToSemiLeptonic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_hdampUp"),
  ("process_name_specific", "TTToSemiLeptonic_hdampUP"),
  ("nof_db_events",         26964000),
  ("nof_db_files",          567),
  ("fsize_db",              1451857443237),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.45TB; nevents: 26.96M; release: 10_2_5; last modified: 2018-12-22 17:00:39"),
])

meta_dictionary["/TTToHadronic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_hdampUp"),
  ("process_name_specific", "TTToHadronic_hdampUP"),
  ("nof_db_events",         24965000),
  ("nof_db_files",          690),
  ("fsize_db",              1360863997866),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.36TB; nevents: 24.96M; release: 10_2_5; last modified: 2019-02-23 11:54:24"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5down_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_ueDown"),
  ("process_name_specific", "TTTo2L2Nu_ueDown"),
  ("nof_db_events",         4954000),
  ("nof_db_files",          145),
  ("fsize_db",              262841944418),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 262.84GB; nevents: 4.95M; release: 10_2_5; last modified: 2019-02-16 16:43:42"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5down_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_ueDown"),
  ("process_name_specific", "TTTo2L2Nu_ueDown_ext1"),
  ("nof_db_events",         9816000),
  ("nof_db_files",          269),
  ("fsize_db",              520405915636),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 520.41GB; nevents: 9.82M; release: 10_2_5; last modified: 2020-03-03 17:41:24"),
])

meta_dictionary["/TTToSemiLeptonic_TuneCP5down_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_ueDown"),
  ("process_name_specific", "TTToSemiLeptonic_ueDown"),
  ("nof_db_events",         20483000),
  ("nof_db_files",          536),
  ("fsize_db",              1097359681757),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.10TB; nevents: 20.48M; release: 10_2_5; last modified: 2019-02-21 11:37:35"),
])

meta_dictionary["/TTToHadronic_TuneCP5down_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_ueDown"),
  ("process_name_specific", "TTToHadronic_ueDown"),
  ("nof_db_events",         26675000),
  ("nof_db_files",          702),
  ("fsize_db",              1446376287651),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.45TB; nevents: 26.68M; release: 10_2_5; last modified: 2019-02-16 22:31:42"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_ueUp"),
  ("process_name_specific", "TTTo2L2Nu_ueUp"),
  ("nof_db_events",         5446000),
  ("nof_db_files",          165),
  ("fsize_db",              290745204567),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 290.75GB; nevents: 5.45M; release: 10_2_5; last modified: 2019-02-16 22:30:24"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_ueUp"),
  ("process_name_specific", "TTTo2L2Nu_ueUp_ext1"),
  ("nof_db_events",         9968000),
  ("nof_db_files",          294),
  ("fsize_db",              532049001268),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 532.05GB; nevents: 9.97M; release: 10_2_5; last modified: 2020-02-28 23:21:29"),
])

meta_dictionary["/TTToSemiLeptonic_TuneCP5up_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_ueUp"),
  ("process_name_specific", "TTToSemiLeptonic_ueUp"),
  ("nof_db_events",         26948000),
  ("nof_db_files",          722),
  ("fsize_db",              1452588033030),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.45TB; nevents: 26.95M; release: 10_2_5; last modified: 2019-02-05 03:58:15"),
])

meta_dictionary["/TTToHadronic_TuneCP5up_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_ueUp"),
  ("process_name_specific", "TTToHadronic_ueUp"),
  ("nof_db_events",         23488000),
  ("nof_db_files",          634),
  ("fsize_db",              1281254369472),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.28TB; nevents: 23.49M; release: 10_2_5; last modified: 2019-01-27 12:50:05"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5CR1_QCDbased_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_QCDbased"),
  ("process_name_specific", "TTTo2L2Nu_QCDbased"),
  ("nof_db_events",         14756000),
  ("nof_db_files",          353),
  ("fsize_db",              790811976585),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 790.81GB; nevents: 14.76M; release: 10_2_5; last modified: 2020-02-15 00:49:45"),
])

meta_dictionary["/TTToSemiLeptonic_TuneCP5CR1_QCDbased_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_QCDbased"),
  ("process_name_specific", "TTToSemiLeptonic_QCDbased"),
  ("nof_db_events",         26692000),
  ("nof_db_files",          647),
  ("fsize_db",              1447222516848),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.45TB; nevents: 26.69M; release: 10_2_5; last modified: 2020-02-14 01:44:55"),
])

meta_dictionary["/TTToHadronic_TuneCP5CR1_QCDbased_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_QCDbased"),
  ("process_name_specific", "TTToHadronic_QCDbased"),
  ("nof_db_events",         16378000),
  ("nof_db_files",          431),
  ("fsize_db",              899011042984),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: PRODUCTION; size: 899.01GB; nevents: 16.38M; release: 10_2_5; last modified: 2020-02-12 01:32:58"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5CR2_GluonMove_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_GluonMove"),
  ("process_name_specific", "TTTo2L2Nu_GluonMove"),
  ("nof_db_events",         14958000),
  ("nof_db_files",          388),
  ("fsize_db",              795939500565),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 795.94GB; nevents: 14.96M; release: 10_2_5; last modified: 2020-03-15 10:56:25"),
])

meta_dictionary["/TTToSemiLeptonic_TuneCP5CR2_GluonMove_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_GluonMove"),
  ("process_name_specific", "TTToSemiLeptonic_GluonMove"),
  ("nof_db_events",         23445000),
  ("nof_db_files",          582),
  ("fsize_db",              1260584939068),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: PRODUCTION; size: 1.26TB; nevents: 23.45M; release: 10_2_5; last modified: 2020-02-12 12:56:21"),
])

meta_dictionary["/TTToHadronic_TuneCP5CR2_GluonMove_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_GluonMove"),
  ("process_name_specific", "TTToHadronic_GluonMove"),
  ("nof_db_events",         23798000),
  ("nof_db_files",          592),
  ("fsize_db",              1294306785998),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: PRODUCTION; size: 1.29TB; nevents: 23.80M; release: 10_2_5; last modified: 2020-02-13 16:06:52"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_erdON"),
  ("process_name_specific", "TTTo2L2Nu_erdON"),
  ("nof_db_events",         3738000),
  ("nof_db_files",          118),
  ("fsize_db",              199297633071),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 199.30GB; nevents: 3.74M; release: 10_2_5; last modified: 2019-06-06 19:53:08"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_erdON"),
  ("process_name_specific", "TTTo2L2Nu_erdON_ext1"),
  ("nof_db_events",         9530000),
  ("nof_db_files",          264),
  ("fsize_db",              507664025011),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 507.66GB; nevents: 9.53M; release: 10_2_5; last modified: 2020-02-24 21:21:45"),
])

meta_dictionary["/TTToSemiLeptonic_TuneCP5_erdON_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_erdON"),
  ("process_name_specific", "TTToSemiLeptonic_erdON"),
  ("nof_db_events",         26290000),
  ("nof_db_files",          717),
  ("fsize_db",              1416312432622),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.42TB; nevents: 26.29M; release: 10_2_5; last modified: 2019-03-28 22:16:15"),
])

meta_dictionary["/TTToHadronic_TuneCP5_erdON_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_erdON"),
  ("process_name_specific", "TTToHadronic_erdON"),
  ("nof_db_events",         27486000),
  ("nof_db_files",          799),
  ("fsize_db",              1499579994365),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.50TB; nevents: 27.49M; release: 10_2_5; last modified: 2019-04-04 05:42:22"),
])

meta_dictionary["/TTTo2L2Nu_mtop166p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_mtop166p5"),
  ("process_name_specific", "TTTo2L2Nu_mtop166p5"),
  ("nof_db_events",         2500000),
  ("nof_db_files",          76),
  ("fsize_db",              132230601699),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 132.23GB; nevents: 2.50M; release: 10_2_5; last modified: 2019-02-15 09:47:19"),
])

meta_dictionary["/TTToSemiLeptonic_mtop166p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_mtop166p5"),
  ("process_name_specific", "TTToSemiLeptonic_mtop166p5"),
  ("nof_db_events",         9767000),
  ("nof_db_files",          254),
  ("fsize_db",              521600331561),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 521.60GB; nevents: 9.77M; release: 10_2_5; last modified: 2019-02-02 00:25:04"),
])

meta_dictionary["/TTToHadronic_mtop166p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_mtop166p5"),
  ("process_name_specific", "TTToHadronic_mtop166p5"),
  ("nof_db_events",         9734000),
  ("nof_db_files",          250),
  ("fsize_db",              526069586840),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 526.07GB; nevents: 9.73M; release: 10_2_5; last modified: 2019-02-02 05:43:19"),
])

meta_dictionary["/TTTo2L2Nu_mtop169p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_mtop169p5"),
  ("process_name_specific", "TTTo2L2Nu_mtop169p5"),
  ("nof_db_events",         2490000),
  ("nof_db_files",          53),
  ("fsize_db",              132076601731),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 132.08GB; nevents: 2.49M; release: 10_2_5; last modified: 2019-01-17 22:13:44"),
])

meta_dictionary["/TTTo2L2Nu_mtop169p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_mtop169p5"),
  ("process_name_specific", "TTTo2L2Nu_mtop169p5_ext1"),
  ("nof_db_events",         9550000),
  ("nof_db_files",          253),
  ("fsize_db",              506299241179),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 506.30GB; nevents: 9.55M; release: 10_2_5; last modified: 2020-02-21 17:05:57"),
])

meta_dictionary["/TTToSemiLeptonic_mtop169p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_mtop169p5"),
  ("process_name_specific", "TTToSemiLeptonic_mtop169p5"),
  ("nof_db_events",         18896000),
  ("nof_db_files",          520),
  ("fsize_db",              1012550848073),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.01TB; nevents: 18.90M; release: 10_2_5; last modified: 2018-12-31 20:23:32"),
])

meta_dictionary["/TTToSemiLeptonic_mtop169p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_mtop169p5"),
  ("process_name_specific", "TTToSemiLeptonic_mtop169p5_ext1"),
  ("nof_db_events",         9808000),
  ("nof_db_files",          280),
  ("fsize_db",              525576169428),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 525.58GB; nevents: 9.81M; release: 10_2_5; last modified: 2020-02-23 17:56:06"),
])

meta_dictionary["/TTToHadronic_mtop169p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_mtop169p5"),
  ("process_name_specific", "TTToHadronic_mtop169p5"),
  ("nof_db_events",         19232000),
  ("nof_db_files",          538),
  ("fsize_db",              1043078618010),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.04TB; nevents: 19.23M; release: 10_2_5; last modified: 2019-02-16 09:26:45"),
])

meta_dictionary["/TTTo2L2Nu_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_mtop171p5"),
  ("process_name_specific", "TTTo2L2Nu_mtop171p5"),
  ("nof_db_events",         5896000),
  ("nof_db_files",          169),
  ("fsize_db",              313467865129),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 313.47GB; nevents: 5.90M; release: 10_2_5; last modified: 2019-03-01 09:59:50"),
])

meta_dictionary["/TTToSemiLeptonic_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_mtop171p5"),
  ("process_name_specific", "TTToSemiLeptonic_mtop171p5"),
  ("nof_db_events",         24984000),
  ("nof_db_files",          622),
  ("fsize_db",              1340936158922),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.34TB; nevents: 24.98M; release: 10_2_5; last modified: 2019-02-18 17:53:51"),
])

meta_dictionary["/TTToHadronic_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_mtop171p5"),
  ("process_name_specific", "TTToHadronic_mtop171p5"),
  ("nof_db_events",         24777000),
  ("nof_db_files",          624),
  ("fsize_db",              1346096669828),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.35TB; nevents: 24.78M; release: 10_2_5; last modified: 2019-02-16 15:23:49"),
])

meta_dictionary["/TTTo2L2Nu_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_mtop173p5"),
  ("process_name_specific", "TTTo2L2Nu_mtop173p5"),
  ("nof_db_events",         5732000),
  ("nof_db_files",          158),
  ("fsize_db",              305189066785),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 305.19GB; nevents: 5.73M; release: 10_2_5; last modified: 2019-02-19 21:49:18"),
])

meta_dictionary["/TTToSemiLeptonic_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_mtop173p5"),
  ("process_name_specific", "TTToSemiLeptonic_mtop173p5"),
  ("nof_db_events",         23892000),
  ("nof_db_files",          590),
  ("fsize_db",              1285214519655),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.29TB; nevents: 23.89M; release: 10_2_5; last modified: 2019-02-03 09:42:53"),
])

meta_dictionary["/TTToHadronic_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_mtop173p5"),
  ("process_name_specific", "TTToHadronic_mtop173p5"),
  ("nof_db_events",         24854000),
  ("nof_db_files",          674),
  ("fsize_db",              1353828323810),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.35TB; nevents: 24.85M; release: 10_2_5; last modified: 2019-02-18 17:52:18"),
])

meta_dictionary["/TTTo2L2Nu_mtop175p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_mtop175p5"),
  ("process_name_specific", "TTTo2L2Nu_mtop175p5"),
  ("nof_db_events",         4958000),
  ("nof_db_files",          154),
  ("fsize_db",              264638885887),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 264.64GB; nevents: 4.96M; release: 10_2_5; last modified: 2019-02-28 05:40:31"),
])

meta_dictionary["/TTTo2L2Nu_mtop175p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_mtop175p5"),
  ("process_name_specific", "TTTo2L2Nu_mtop175p5_ext1"),
  ("nof_db_events",         9603000),
  ("nof_db_files",          283),
  ("fsize_db",              512657546981),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 512.66GB; nevents: 9.60M; release: 10_2_5; last modified: 2020-02-21 17:03:10"),
])

meta_dictionary["/TTToSemiLeptonic_mtop175p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_mtop175p5"),
  ("process_name_specific", "TTToSemiLeptonic_mtop175p5"),
  ("nof_db_events",         19625000),
  ("nof_db_files",          475),
  ("fsize_db",              1057075927311),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.06TB; nevents: 19.62M; release: 10_2_5; last modified: 2019-01-13 04:17:58"),
])

meta_dictionary["/TTToSemiLeptonic_mtop175p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_mtop175p5"),
  ("process_name_specific", "TTToSemiLeptonic_mtop175p5_ext1"),
  ("nof_db_events",         9773000),
  ("nof_db_files",          254),
  ("fsize_db",              526998400342),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 527.00GB; nevents: 9.77M; release: 10_2_5; last modified: 2020-02-19 04:05:08"),
])

meta_dictionary["/TTToHadronic_mtop175p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_mtop175p5"),
  ("process_name_specific", "TTToHadronic_mtop175p5"),
  ("nof_db_events",         18280000),
  ("nof_db_files",          499),
  ("fsize_db",              997347369283),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 997.35GB; nevents: 18.28M; release: 10_2_5; last modified: 2019-01-20 19:00:50"),
])

meta_dictionary["/TTTo2L2Nu_mtop178p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_mtop178p5"),
  ("process_name_specific", "TTTo2L2Nu_mtop178p5"),
  ("nof_db_events",         2416000),
  ("nof_db_files",          76),
  ("fsize_db",              129329691697),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 129.33GB; nevents: 2.42M; release: 10_2_5; last modified: 2019-02-02 00:25:47"),
])

meta_dictionary["/TTToSemiLeptonic_mtop178p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_mtop178p5"),
  ("process_name_specific", "TTToSemiLeptonic_mtop178p5"),
  ("nof_db_events",         9762000),
  ("nof_db_files",          256),
  ("fsize_db",              528185317770),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 528.19GB; nevents: 9.76M; release: 10_2_5; last modified: 2019-02-18 17:53:27"),
])

meta_dictionary["/TTToHadronic_mtop178p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_mtop178p5"),
  ("process_name_specific", "TTToHadronic_mtop178p5"),
  ("nof_db_events",         9782000),
  ("nof_db_files",          247),
  ("fsize_db",              535678760206),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 535.68GB; nevents: 9.78M; release: 10_2_5; last modified: 2019-02-21 08:30:17"),
])

meta_dictionary["/TTTo2L2Nu_widthx0p7_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_widthx0p7"),
  ("process_name_specific", "TTTo2L2Nu_widthx0p7"),
  ("nof_db_events",         4776000),
  ("nof_db_files",          139),
  ("fsize_db",              254087020383),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 254.09GB; nevents: 4.78M; release: 10_2_5; last modified: 2019-03-11 13:41:47"),
])

meta_dictionary["/TTToSemiLeptonic_widthx0p7_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_widthx0p7"),
  ("process_name_specific", "TTToSemiLeptonic_widthx0p7"),
  ("nof_db_events",         19500000),
  ("nof_db_files",          545),
  ("fsize_db",              1048702444808),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.05TB; nevents: 19.50M; release: 10_2_5; last modified: 2019-06-09 05:27:46"),
])

meta_dictionary["/TTTo2L2Nu_widthx0p85_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_widthx0p85"),
  ("process_name_specific", "TTTo2L2Nu_widthx0p85"),
  ("nof_db_events",         4790000),
  ("nof_db_files",          139),
  ("fsize_db",              254834163512),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 254.83GB; nevents: 4.79M; release: 10_2_5; last modified: 2019-03-11 16:49:25"),
])

meta_dictionary["/TTToSemiLeptonic_widthx0p85_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_widthx0p85"),
  ("process_name_specific", "TTToSemiLeptonic_widthx0p85"),
  ("nof_db_events",         19800000),
  ("nof_db_files",          540),
  ("fsize_db",              1064523714546),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.06TB; nevents: 19.80M; release: 10_2_5; last modified: 2019-04-08 23:43:13"),
])

meta_dictionary["/TTTo2L2Nu_widthx1p15_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_widthx1p15"),
  ("process_name_specific", "TTTo2L2Nu_widthx1p15"),
  ("nof_db_events",         584000),
  ("nof_db_files",          23),
  ("fsize_db",              31109535835),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 31.11GB; nevents: 584.00k; release: 10_2_5; last modified: 2019-06-03 21:11:08"),
])

meta_dictionary["/TTToSemiLeptonic_widthx1p15_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_widthx1p15"),
  ("process_name_specific", "TTToSemiLeptonic_widthx1p15"),
  ("nof_db_events",         19137000),
  ("nof_db_files",          546),
  ("fsize_db",              1029146761272),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.03TB; nevents: 19.14M; release: 10_2_5; last modified: 2019-03-25 15:37:03"),
])

meta_dictionary["/TTTo2L2Nu_widthx1p3_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_widthx1p3"),
  ("process_name_specific", "TTTo2L2Nu_widthx1p3"),
  ("nof_db_events",         4796000),
  ("nof_db_files",          157),
  ("fsize_db",              255489886690),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 255.49GB; nevents: 4.80M; release: 10_2_5; last modified: 2019-03-28 16:00:36"),
])

meta_dictionary["/TTToSemiLeptonic_widthx1p3_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_widthx1p3"),
  ("process_name_specific", "TTToSemiLeptonic_widthx1p3"),
  ("nof_db_events",         19260000),
  ("nof_db_files",          549),
  ("fsize_db",              1035758532665),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.04TB; nevents: 19.26M; release: 10_2_5; last modified: 2019-03-25 21:19:06"),
])


# event statistics by sample category:
# TT_hdampDown:  67.74M
# TT_hdampUp:    67.09M
# TT_ueDown:     61.93M
# TT_ueUp:       65.85M
# TT_QCDbased:   57.83M
# TT_GluonMove:  62.20M
# TT_erdON:      67.04M
# TT_mtop166p5:  22.00M
# TT_mtop169p5:  59.98M
# TT_mtop171p5:  55.66M
# TT_mtop173p5:  54.48M
# TT_mtop175p5:  62.24M
# TT_mtop178p5:  21.96M
# TT_widthx0p7:  24.28M
# TT_widthx0p85: 24.59M
# TT_widthx1p15: 19.72M
# TT_widthx1p3:  24.06M

