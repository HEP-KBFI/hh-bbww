from collections import OrderedDict as OD

# file generated at 2020-10-20 23:30:04 with the following command:
# find_samples.py -V -i ../../tthAnalysis/NanoAOD/test/datasets/txt/datasets_ttbar_mc_2017_RunIIFall17MiniAODv2.txt -m python/samples/metaDict_2017_ttbar.py -s ../../tthAnalysis/NanoAOD/test/datasets/txt/sum_datasets_ttbar_2017_RunIIFall17MiniAODv2.txt -c python/samples/sampleLocations_2017_nanoAOD_ttbar.txt

meta_dictionary = OD()


### event sums

sum_events = { 
  ("TTTo2L2Nu_hdampDOWN", "TTTo2L2Nu_hdampDOWN_ext1", "TTTo2L2Nu_hdampDOWN_ext2"),
  ("TTTo2L2Nu_hdampUP", "TTTo2L2Nu_hdampUP_ext1", "TTTo2L2Nu_hdampUP_ext2"),
  ("TTTo2L2Nu_ueDown", "TTTo2L2Nu_ueDown_ext1", "TTTo2L2Nu_ueDown_ext2"),
  ("TTTo2L2Nu_ueUp", "TTTo2L2Nu_ueUp_ext1", "TTTo2L2Nu_ueUp_ext2"),
  ("TTTo2L2Nu_QCDbased", "TTTo2L2Nu_QCDbased_ext1"),
  ("TTTo2L2Nu_GluonMove", "TTTo2L2Nu_GluonMove_ext1", "TTTo2L2Nu_GluonMove_ext2"),
  ("TTTo2L2Nu_erdON", "TTTo2L2Nu_erdON_ext1", "TTTo2L2Nu_erdON_ext2"),
  ("TTTo2L2Nu_mtop166p5", "TTTo2L2Nu_mtop166p5_PSweights"),
  ("TTToSemiLeptonic_mtop166p5", "TTToSemiLeptonic_mtop166p5_PSweights"),
  ("TTToHadronic_mtop166p5", "TTToHadronic_mtop166p5_PSweights"),
  ("TTTo2L2Nu_mtop169p5", "TTTo2L2Nu_mtop169p5_ext1", "TTTo2L2Nu_mtop169p5_ext2"),
  ("TTToSemiLeptonic_mtop169p5", "TTToSemiLeptonic_mtop169p5_ext1"),
  ("TTTo2L2Nu_mtop173p5", "TTTo2L2Nu_mtop173p5_ext1"),
  ("TTTo2L2Nu_mtop175p5", "TTTo2L2Nu_mtop175p5_ext1", "TTTo2L2Nu_mtop175p5_ext2"),
  ("TTToSemiLeptonic_mtop175p5", "TTToSemiLeptonic_mtop175p5_ext1"),
  ("TTTo2L2Nu_mtop178p5", "TTTo2L2Nu_mtop178p5_PSweights"),
  ("TTToSemiLeptonic_mtop178p5", "TTToSemiLeptonic_mtop178p5_PSweights"),
}


meta_dictionary["/TTTo2L2Nu_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTTo2L2Nu_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "TT_hdampDown"),
  ("process_name_specific", "TTTo2L2Nu_hdampDOWN"),
  ("nof_db_events",         5476459),
  ("nof_db_files",          85),
  ("fsize_db",              291527855740),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 291.53GB; nevents: 5.48M; release: 9_4_7; last modified: 2018-10-13 06:11:24"),
])

meta_dictionary["/TTTo2L2Nu_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTTo2L2Nu_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1"),
  ("sample_category",       "TT_hdampDown"),
  ("process_name_specific", "TTTo2L2Nu_hdampDOWN_ext1"),
  ("nof_db_events",         9963000),
  ("nof_db_files",          254),
  ("fsize_db",              534340304188),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 534.34GB; nevents: 9.96M; release: 9_4_7; last modified: 2020-02-27 06:58:09"),
])

meta_dictionary["/TTTo2L2Nu_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext2-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Oct17_TTTo2L2Nu_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext2-v2"),
  ("sample_category",       "TT_hdampDown"),
  ("process_name_specific", "TTTo2L2Nu_hdampDOWN_ext2"),
  ("nof_db_events",         29618000),
  ("nof_db_files",          740),
  ("fsize_db",              1797154233436),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "96.06%; status: VALID; size: 1.80TB; nevents: 29.62M; release: 9_4_7; last modified: 2020-10-14 23:02:27"),
])

meta_dictionary["/TTToSemiLeptonic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTToSemiLeptonic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2"),
  ("sample_category",       "TT_hdampDown"),
  ("process_name_specific", "TTToSemiLeptonic_hdampDOWN"),
  ("nof_db_events",         26849863),
  ("nof_db_files",          505),
  ("fsize_db",              1453196831832),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 1.45TB; nevents: 26.85M; release: 9_4_7; last modified: 2019-06-26 09:57:46"),
])

meta_dictionary["/TTToHadronic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTToHadronic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v"),
  ("sample_category",       "TT_hdampDown"),
  ("process_name_specific", "TTToHadronic_hdampDOWN"),
  ("nof_db_events",         27117982),
  ("nof_db_files",          418),
  ("fsize_db",              1492982332867),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "97.44%; status: VALID; size: 1.49TB; nevents: 27.12M; release: 9_4_7; last modified: 2018-07-24 00:07:50"),
])

meta_dictionary["/TTTo2L2Nu_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Apr22_TTTo2L2Nu_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "TT_hdampUp"),
  ("process_name_specific", "TTTo2L2Nu_hdampUP"),
  ("nof_db_events",         3288128),
  ("nof_db_files",          67),
  ("fsize_db",              176301752654),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 176.30GB; nevents: 3.29M; release: 9_4_7; last modified: 2019-03-05 13:12:52"),
])

meta_dictionary["/TTTo2L2Nu_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTTo2L2Nu_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1"),
  ("sample_category",       "TT_hdampUp"),
  ("process_name_specific", "TTTo2L2Nu_hdampUP_ext1"),
  ("nof_db_events",         9872999),
  ("nof_db_files",          252),
  ("fsize_db",              532196934554),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 532.20GB; nevents: 9.87M; release: 9_4_7; last modified: 2020-02-16 07:36:24"),
])

meta_dictionary["/TTTo2L2Nu_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext2-v2/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_hdampUp"),
  ("process_name_specific", "TTTo2L2Nu_hdampUP_ext2"),
  ("nof_db_events",         25797000),
  ("nof_db_files",          541),
  ("fsize_db",              1502993272816),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: PRODUCTION; size: 1.50TB; nevents: 25.80M; release: 9_4_7; last modified: 2020-10-07 05:16:00"),
])

meta_dictionary["/TTToSemiLeptonic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTToSemiLeptonic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14"),
  ("sample_category",       "TT_hdampUp"),
  ("process_name_specific", "TTToSemiLeptonic_hdampUP"),
  ("nof_db_events",         23977012),
  ("nof_db_files",          348),
  ("fsize_db",              1303431143623),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 1.30TB; nevents: 23.98M; release: 9_4_6_patch1; last modified: 2018-10-06 02:51:39"),
])

meta_dictionary["/TTToHadronic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTToHadronic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2"),
  ("sample_category",       "TT_hdampUp"),
  ("process_name_specific", "TTToHadronic_hdampUP"),
  ("nof_db_events",         27260880),
  ("nof_db_files",          489),
  ("fsize_db",              1509180190914),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "95.26%; status: VALID; size: 1.51TB; nevents: 27.26M; release: 9_4_7; last modified: 2018-10-06 23:47:15"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "TT_ueDown"),
  ("process_name_specific", "TTTo2L2Nu_ueDown"),
  ("nof_db_events",         5500000),
  ("nof_db_files",          86),
  ("fsize_db",              292849978936),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 292.85GB; nevents: 5.50M; release: 9_4_6_patch1; last modified: 2018-09-19 07:44:18"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1"),
  ("sample_category",       "TT_ueDown"),
  ("process_name_specific", "TTTo2L2Nu_ueDown_ext1"),
  ("nof_db_events",         9609000),
  ("nof_db_files",          246),
  ("fsize_db",              515372873445),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "94.85%; status: VALID; size: 515.37GB; nevents: 9.61M; release: 9_4_7; last modified: 2020-02-21 17:04:50"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext2-v2/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_ueDown"),
  ("process_name_specific", "TTTo2L2Nu_ueDown_ext2"),
  ("nof_db_events",         23766000),
  ("nof_db_files",          558),
  ("fsize_db",              1441739612615),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: PRODUCTION; size: 1.44TB; nevents: 23.77M; release: 9_4_7; last modified: 2020-10-09 10:13:15"),
])

meta_dictionary["/TTToSemiLeptonic_TuneCP5down_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTToSemiLeptonic_TuneCP5down_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2"),
  ("sample_category",       "TT_ueDown"),
  ("process_name_specific", "TTToSemiLeptonic_ueDown"),
  ("nof_db_events",         22911672),
  ("nof_db_files",          330),
  ("fsize_db",              1238638894281),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 1.24TB; nevents: 22.91M; release: 9_4_6_patch1; last modified: 2019-09-10 05:06:15"),
])

meta_dictionary["/TTToHadronic_TuneCP5down_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTToHadronic_TuneCP5down_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2"),
  ("sample_category",       "TT_ueDown"),
  ("process_name_specific", "TTToHadronic_ueDown"),
  ("nof_db_events",         27252808),
  ("nof_db_files",          460),
  ("fsize_db",              1500092628149),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 1.50TB; nevents: 27.25M; release: 9_4_7; last modified: 2018-10-14 23:45:37"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Apr22_TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "TT_ueUp"),
  ("process_name_specific", "TTTo2L2Nu_ueUp"),
  ("nof_db_events",         5500000),
  ("nof_db_files",          87),
  ("fsize_db",              294673644731),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 294.67GB; nevents: 5.50M; release: 9_4_7; last modified: 2018-07-22 15:47:57"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1"),
  ("sample_category",       "TT_ueUp"),
  ("process_name_specific", "TTTo2L2Nu_ueUp_ext1"),
  ("nof_db_events",         9992000),
  ("nof_db_files",          239),
  ("fsize_db",              539036705125),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 539.04GB; nevents: 9.99M; release: 9_4_7; last modified: 2020-02-26 18:49:34"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext2-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Oct13_TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext2-v2"),
  ("sample_category",       "TT_ueUp"),
  ("process_name_specific", "TTTo2L2Nu_ueUp_ext2"),
  ("nof_db_events",         29890000),
  ("nof_db_files",          762),
  ("fsize_db",              1824390970121),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "91.84%; status: VALID; size: 1.82TB; nevents: 29.89M; release: 9_4_7; last modified: 2020-10-12 10:43:40"),
])

meta_dictionary["/TTToSemiLeptonic_TuneCP5up_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTToSemiLeptonic_TuneCP5up_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2"),
  ("sample_category",       "TT_ueUp"),
  ("process_name_specific", "TTToSemiLeptonic_ueUp"),
  ("nof_db_events",         20122010),
  ("nof_db_files",          330),
  ("fsize_db",              1095057474309),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "96.55%; status: VALID; size: 1.10TB; nevents: 20.12M; release: 9_4_7; last modified: 2018-10-05 15:40:45"),
])

meta_dictionary["/TTToHadronic_TuneCP5up_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTToHadronic_TuneCP5up_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "TT_ueUp"),
  ("process_name_specific", "TTToHadronic_ueUp"),
  ("nof_db_events",         27108792),
  ("nof_db_files",          469),
  ("fsize_db",              1500611986746),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 1.50TB; nevents: 27.11M; release: 9_4_7; last modified: 2018-10-07 19:42:45"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTTo2L2Nu_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "TT_QCDbased"),
  ("process_name_specific", "TTTo2L2Nu_QCDbased"),
  ("nof_db_events",         5500000),
  ("nof_db_files",          143),
  ("fsize_db",              299508226429),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 299.51GB; nevents: 5.50M; release: 9_4_7; last modified: 2020-02-14 12:04:56"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTTo2L2Nu_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1"),
  ("sample_category",       "TT_QCDbased"),
  ("process_name_specific", "TTTo2L2Nu_QCDbased_ext1"),
  ("nof_db_events",         9999000),
  ("nof_db_files",          274),
  ("fsize_db",              544472722769),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 544.47GB; nevents: 10.00M; release: 9_4_7; last modified: 2020-03-15 18:52:06"),
])

meta_dictionary["/TTToSemiLeptonic_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTToSemiLeptonic_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "TT_QCDbased"),
  ("process_name_specific", "TTToSemiLeptonic_QCDbased"),
  ("nof_db_events",         27125000),
  ("nof_db_files",          546),
  ("fsize_db",              1498188372333),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 1.50TB; nevents: 27.12M; release: 9_4_7; last modified: 2020-03-06 19:02:04"),
])

meta_dictionary["/TTToHadronic_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTToHadronic_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "TT_QCDbased"),
  ("process_name_specific", "TTToHadronic_QCDbased"),
  ("nof_db_events",         27341000),
  ("nof_db_files",          537),
  ("fsize_db",              1534244543624),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "99.64%; status: VALID; size: 1.53TB; nevents: 27.34M; release: 9_4_7; last modified: 2020-03-10 08:58:23"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTTo2L2Nu_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "TT_GluonMove"),
  ("process_name_specific", "TTTo2L2Nu_GluonMove"),
  ("nof_db_events",         5461000),
  ("nof_db_files",          139),
  ("fsize_db",              294536631445),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 294.54GB; nevents: 5.46M; release: 9_4_7; last modified: 2020-03-20 16:53:16"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTTo2L2Nu_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1"),
  ("sample_category",       "TT_GluonMove"),
  ("process_name_specific", "TTTo2L2Nu_GluonMove_ext1"),
  ("nof_db_events",         9818000),
  ("nof_db_files",          258),
  ("fsize_db",              530494659584),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 530.49GB; nevents: 9.82M; release: 9_4_7; last modified: 2020-03-30 00:11:27"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext2-v2/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_GluonMove"),
  ("process_name_specific", "TTTo2L2Nu_GluonMove_ext2"),
  ("nof_db_events",         27981000),
  ("nof_db_files",          679),
  ("fsize_db",              1633463218129),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: PRODUCTION; size: 1.63TB; nevents: 27.98M; release: 9_4_7; last modified: 2020-10-09 10:06:37"),
])

meta_dictionary["/TTToSemiLeptonic_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTToSemiLeptonic_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "TT_GluonMove"),
  ("process_name_specific", "TTToSemiLeptonic_GluonMove"),
  ("nof_db_events",         27409000),
  ("nof_db_files",          639),
  ("fsize_db",              1502331258937),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 1.50TB; nevents: 27.41M; release: 9_4_7; last modified: 2020-03-21 23:47:42"),
])

meta_dictionary["/TTToHadronic_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTToHadronic_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "TT_GluonMove"),
  ("process_name_specific", "TTToHadronic_GluonMove"),
  ("nof_db_events",         27469000),
  ("nof_db_files",          602),
  ("fsize_db",              1530584055949),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 1.53TB; nevents: 27.47M; release: 9_4_7; last modified: 2020-03-20 03:45:21"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "TT_erdON"),
  ("process_name_specific", "TTTo2L2Nu_erdON"),
  ("nof_db_events",         5092000),
  ("nof_db_files",          162),
  ("fsize_db",              274704284910),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 274.70GB; nevents: 5.09M; release: 9_4_7; last modified: 2019-07-12 23:47:31"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1"),
  ("sample_category",       "TT_erdON"),
  ("process_name_specific", "TTTo2L2Nu_erdON_ext1"),
  ("nof_db_events",         9966000),
  ("nof_db_files",          235),
  ("fsize_db",              541613889407),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 541.61GB; nevents: 9.97M; release: 9_4_7; last modified: 2020-03-21 14:49:47"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext2-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Oct17_TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext2-v2"),
  ("sample_category",       "TT_erdON"),
  ("process_name_specific", "TTTo2L2Nu_erdON_ext2"),
  ("nof_db_events",         29352000),
  ("nof_db_files",          756),
  ("fsize_db",              1709100793154),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "94.21%; status: VALID; size: 1.71TB; nevents: 29.35M; release: 9_4_7; last modified: 2020-10-13 23:44:24"),
])

meta_dictionary["/TTToSemiLeptonic_TuneCP5_erdON_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Apr22_TTToSemiLeptonic_TuneCP5_erdON_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "TT_erdON"),
  ("process_name_specific", "TTToSemiLeptonic_erdON"),
  ("nof_db_events",         27292000),
  ("nof_db_files",          658),
  ("fsize_db",              1492517947810),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 1.49TB; nevents: 27.29M; release: 9_4_7; last modified: 2019-05-27 20:25:09"),
])

meta_dictionary["/TTToHadronic_TuneCP5_erdON_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTToHadronic_TuneCP5_erdON_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3"),
  ("sample_category",       "TT_erdON"),
  ("process_name_specific", "TTToHadronic_erdON"),
  ("nof_db_events",         26893000),
  ("nof_db_files",          457),
  ("fsize_db",              1491456606989),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 1.49TB; nevents: 26.89M; release: 9_4_7; last modified: 2019-09-27 02:10:05"),
])

meta_dictionary["/TTTo2L2Nu_mtop166p5_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTTo2L2Nu_mtop166p5_TuneCP5_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2"),
  ("sample_category",       "TT_mtop166p5"),
  ("process_name_specific", "TTTo2L2Nu_mtop166p5"),
  ("nof_db_events",         2430849),
  ("nof_db_files",          51),
  ("fsize_db",              129108353493),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "96.0%; status: VALID; size: 129.11GB; nevents: 2.43M; release: 9_4_6_patch1; last modified: 2018-10-06 03:26:04"),
])

meta_dictionary["/TTTo2L2Nu_mtop166p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTTo2L2Nu_mtop166p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2"),
  ("sample_category",       "TT_mtop166p5"),
  ("process_name_specific", "TTTo2L2Nu_mtop166p5_PSweights"),
  ("nof_db_events",         2500000),
  ("nof_db_files",          42),
  ("fsize_db",              132728814159),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 132.73GB; nevents: 2.50M; release: 9_4_6_patch1; last modified: 2018-10-18 09:18:16"),
])

meta_dictionary["/TTToSemiLeptonic_mtop166p5_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTToSemiLeptonic_mtop166p5_TuneCP5_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2"),
  ("sample_category",       "TT_mtop166p5"),
  ("process_name_specific", "TTToSemiLeptonic_mtop166p5"),
  ("nof_db_events",         9940122),
  ("nof_db_files",          148),
  ("fsize_db",              536119573228),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 536.12GB; nevents: 9.94M; release: 9_4_7; last modified: 2018-10-17 12:16:08"),
])

meta_dictionary["/TTToSemiLeptonic_mtop166p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTToSemiLeptonic_mtop166p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2"),
  ("sample_category",       "TT_mtop166p5"),
  ("process_name_specific", "TTToSemiLeptonic_mtop166p5_PSweights"),
  ("nof_db_events",         9553066),
  ("nof_db_files",          147),
  ("fsize_db",              515058612689),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 515.06GB; nevents: 9.55M; release: 9_4_7; last modified: 2018-10-17 11:09:45"),
])

meta_dictionary["/TTToHadronic_mtop166p5_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTToHadronic_mtop166p5_TuneCP5_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2"),
  ("sample_category",       "TT_mtop166p5"),
  ("process_name_specific", "TTToHadronic_mtop166p5"),
  ("nof_db_events",         9694576),
  ("nof_db_files",          186),
  ("fsize_db",              532391268393),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "97.96%; status: VALID; size: 532.39GB; nevents: 9.69M; release: 9_4_7; last modified: 2018-10-04 12:16:11"),
])

meta_dictionary["/TTToHadronic_mtop166p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTToHadronic_mtop166p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v"),
  ("sample_category",       "TT_mtop166p5"),
  ("process_name_specific", "TTToHadronic_mtop166p5_PSweights"),
  ("nof_db_events",         10000000),
  ("nof_db_files",          177),
  ("fsize_db",              548417838778),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "98.02%; status: VALID; size: 548.42GB; nevents: 10.00M; release: 9_4_7; last modified: 2018-10-17 11:09:20"),
])

meta_dictionary["/TTTo2L2Nu_mtop169p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTTo2L2Nu_mtop169p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "TT_mtop169p5"),
  ("process_name_specific", "TTTo2L2Nu_mtop169p5"),
  ("nof_db_events",         4955578),
  ("nof_db_files",          76),
  ("fsize_db",              263959681021),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 263.96GB; nevents: 4.96M; release: 9_4_6_patch1; last modified: 2018-05-18 12:06:55"),
])

meta_dictionary["/TTTo2L2Nu_mtop169p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTTo2L2Nu_mtop169p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1"),
  ("sample_category",       "TT_mtop169p5"),
  ("process_name_specific", "TTTo2L2Nu_mtop169p5_ext1"),
  ("nof_db_events",         9674000),
  ("nof_db_files",          232),
  ("fsize_db",              518706712218),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 518.71GB; nevents: 9.67M; release: 9_4_7; last modified: 2020-02-12 05:46:02"),
])

meta_dictionary["/TTTo2L2Nu_mtop169p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext2-v2/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_mtop169p5"),
  ("process_name_specific", "TTTo2L2Nu_mtop169p5_ext2"),
  ("nof_db_events",         29190000),
  ("nof_db_files",          601),
  ("fsize_db",              1691547863971),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.69TB; nevents: 29.19M; release: 9_4_7; last modified: 2020-10-19 21:01:50"),
])

meta_dictionary["/TTToSemiLeptonic_mtop169p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTToSemiLeptonic_mtop169p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v"),
  ("sample_category",       "TT_mtop169p5"),
  ("process_name_specific", "TTToSemiLeptonic_mtop169p5"),
  ("nof_db_events",         18802372),
  ("nof_db_files",          280),
  ("fsize_db",              1016431882420),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "92.06%; status: VALID; size: 1.02TB; nevents: 18.80M; release: 9_4_7; last modified: 2018-10-15 06:48:16"),
])

meta_dictionary["/TTToSemiLeptonic_mtop169p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTToSemiLeptonic_mtop169p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-"),
  ("sample_category",       "TT_mtop169p5"),
  ("process_name_specific", "TTToSemiLeptonic_mtop169p5_ext1"),
  ("nof_db_events",         9858000),
  ("nof_db_files",          257),
  ("fsize_db",              537017483165),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 537.02GB; nevents: 9.86M; release: 9_4_7; last modified: 2020-02-27 06:57:20"),
])

meta_dictionary["/TTToHadronic_mtop169p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTToHadronic_mtop169p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3"),
  ("sample_category",       "TT_mtop169p5"),
  ("process_name_specific", "TTToHadronic_mtop169p5"),
  ("nof_db_events",         18739000),
  ("nof_db_files",          411),
  ("fsize_db",              1035722135319),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 1.04TB; nevents: 18.74M; release: 9_4_6_patch1; last modified: 2018-11-11 06:55:02"),
])

meta_dictionary["/TTTo2L2Nu_mtop171p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTTo2L2Nu_mtop171p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2"),
  ("sample_category",       "TT_mtop171p5"),
  ("process_name_specific", "TTTo2L2Nu_mtop171p5"),
  ("nof_db_events",         5954696),
  ("nof_db_files",          105),
  ("fsize_db",              317838339272),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 317.84GB; nevents: 5.95M; release: 9_4_7; last modified: 2018-10-07 00:37:26"),
])

meta_dictionary["/TTToSemiLeptonic_mtop171p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Apr22_TTToSemiLeptonic_mtop171p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v"),
  ("sample_category",       "TT_mtop171p5"),
  ("process_name_specific", "TTToSemiLeptonic_mtop171p5"),
  ("nof_db_events",         25000000),
  ("nof_db_files",          429),
  ("fsize_db",              1354549562121),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 1.35TB; nevents: 25.00M; release: 9_4_7; last modified: 2018-09-19 03:45:55"),
])

meta_dictionary["/TTToHadronic_mtop171p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTToHadronic_mtop171p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v"),
  ("sample_category",       "TT_mtop171p5"),
  ("process_name_specific", "TTToHadronic_mtop171p5"),
  ("nof_db_events",         23983066),
  ("nof_db_files",          364),
  ("fsize_db",              1323043643849),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "97.1%; status: VALID; size: 1.32TB; nevents: 23.98M; release: 9_4_7; last modified: 2018-10-15 05:34:54"),
])

meta_dictionary["/TTTo2L2Nu_mtop173p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTTo2L2Nu_mtop173p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "TT_mtop173p5"),
  ("process_name_specific", "TTTo2L2Nu_mtop173p5"),
  ("nof_db_events",         6000000),
  ("nof_db_files",          120),
  ("fsize_db",              320956100851),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 320.96GB; nevents: 6.00M; release: 9_4_6_patch1; last modified: 2018-10-04 16:56:15"),
])

meta_dictionary["/TTTo2L2Nu_mtop173p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Oct17_TTTo2L2Nu_mtop173p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2"),
  ("sample_category",       "TT_mtop173p5"),
  ("process_name_specific", "TTTo2L2Nu_mtop173p5_ext1"),
  ("nof_db_events",         14505000),
  ("nof_db_files",          384),
  ("fsize_db",              844237214802),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "96.71%; status: VALID; size: 844.24GB; nevents: 14.51M; release: 9_4_7; last modified: 2020-10-15 12:06:13"),
])

meta_dictionary["/TTToSemiLeptonic_mtop173p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Apr22_TTToSemiLeptonic_mtop173p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2"),
  ("sample_category",       "TT_mtop173p5"),
  ("process_name_specific", "TTToSemiLeptonic_mtop173p5"),
  ("nof_db_events",         24132305),
  ("nof_db_files",          400),
  ("fsize_db",              1310413301099),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 1.31TB; nevents: 24.13M; release: 9_4_7; last modified: 2019-09-09 03:33:47"),
])

meta_dictionary["/TTToHadronic_mtop173p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Apr22_TTToHadronic_mtop173p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3"),
  ("sample_category",       "TT_mtop173p5"),
  ("process_name_specific", "TTToHadronic_mtop173p5"),
  ("nof_db_events",         24373000),
  ("nof_db_files",          529),
  ("fsize_db",              1353482022084),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 1.35TB; nevents: 24.37M; release: 9_4_6_patch1; last modified: 2018-08-13 06:31:39"),
])

meta_dictionary["/TTTo2L2Nu_mtop175p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTTo2L2Nu_mtop175p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "TT_mtop175p5"),
  ("process_name_specific", "TTTo2L2Nu_mtop175p5"),
  ("nof_db_events",         4987400),
  ("nof_db_files",          90),
  ("fsize_db",              267023588385),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 267.02GB; nevents: 4.99M; release: 9_4_6_patch1; last modified: 2018-10-05 15:38:52"),
])

meta_dictionary["/TTTo2L2Nu_mtop175p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTTo2L2Nu_mtop175p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1"),
  ("sample_category",       "TT_mtop175p5"),
  ("process_name_specific", "TTTo2L2Nu_mtop175p5_ext1"),
  ("nof_db_events",         9642000),
  ("nof_db_files",          224),
  ("fsize_db",              520015250773),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 520.02GB; nevents: 9.64M; release: 9_4_7; last modified: 2020-02-18 17:50:28"),
])

meta_dictionary["/TTTo2L2Nu_mtop175p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext2-v2/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT_mtop175p5"),
  ("process_name_specific", "TTTo2L2Nu_mtop175p5_ext2"),
  ("nof_db_events",         28986000),
  ("nof_db_files",          757),
  ("fsize_db",              1769513184228),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: PRODUCTION; size: 1.77TB; nevents: 28.99M; release: 9_4_7; last modified: 2020-10-09 10:13:19"),
])

meta_dictionary["/TTToSemiLeptonic_mtop175p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTToSemiLeptonic_mtop175p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v"),
  ("sample_category",       "TT_mtop175p5"),
  ("process_name_specific", "TTToSemiLeptonic_mtop175p5"),
  ("nof_db_events",         18651748),
  ("nof_db_files",          307),
  ("fsize_db",              1015022724714),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "96.28%; status: VALID; size: 1.02TB; nevents: 18.65M; release: 9_4_6_patch1; last modified: 2018-10-06 14:34:18"),
])

meta_dictionary["/TTToSemiLeptonic_mtop175p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTToSemiLeptonic_mtop175p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-"),
  ("sample_category",       "TT_mtop175p5"),
  ("process_name_specific", "TTToSemiLeptonic_mtop175p5_ext1"),
  ("nof_db_events",         9858000),
  ("nof_db_files",          237),
  ("fsize_db",              540202026504),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 540.20GB; nevents: 9.86M; release: 9_4_7; last modified: 2020-02-16 20:13:24"),
])

meta_dictionary["/TTToHadronic_mtop175p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Apr22_TTToHadronic_mtop175p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v"),
  ("sample_category",       "TT_mtop175p5"),
  ("process_name_specific", "TTToHadronic_mtop175p5"),
  ("nof_db_events",         19688281),
  ("nof_db_files",          320),
  ("fsize_db",              1090427837791),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 1.09TB; nevents: 19.69M; release: 9_4_7; last modified: 2019-03-22 09:59:36"),
])

meta_dictionary["/TTTo2L2Nu_mtop178p5_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTTo2L2Nu_mtop178p5_TuneCP5_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2"),
  ("sample_category",       "TT_mtop178p5"),
  ("process_name_specific", "TTTo2L2Nu_mtop178p5"),
  ("nof_db_events",         2458584),
  ("nof_db_files",          42),
  ("fsize_db",              132267893447),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 132.27GB; nevents: 2.46M; release: 9_4_7; last modified: 2018-10-17 10:23:44"),
])

meta_dictionary["/TTTo2L2Nu_mtop178p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Apr22_TTTo2L2Nu_mtop178p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2"),
  ("sample_category",       "TT_mtop178p5"),
  ("process_name_specific", "TTTo2L2Nu_mtop178p5_PSweights"),
  ("nof_db_events",         2459510),
  ("nof_db_files",          41),
  ("fsize_db",              132134836816),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 132.13GB; nevents: 2.46M; release: 9_4_7; last modified: 2018-09-19 14:05:51"),
])

meta_dictionary["/TTToSemiLeptonic_mtop178p5_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTToSemiLeptonic_mtop178p5_TuneCP5_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2"),
  ("sample_category",       "TT_mtop178p5"),
  ("process_name_specific", "TTToSemiLeptonic_mtop178p5"),
  ("nof_db_events",         9895825),
  ("nof_db_files",          167),
  ("fsize_db",              540169588879),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 540.17GB; nevents: 9.90M; release: 9_4_7; last modified: 2018-10-05 06:30:48"),
])

meta_dictionary["/TTToSemiLeptonic_mtop178p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTToSemiLeptonic_mtop178p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v"),
  ("sample_category",       "TT_mtop178p5"),
  ("process_name_specific", "TTToSemiLeptonic_mtop178p5_PSweights"),
  ("nof_db_events",         9986177),
  ("nof_db_files",          192),
  ("fsize_db",              545083161451),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 545.08GB; nevents: 9.99M; release: 9_4_7; last modified: 2018-10-06 23:47:01"),
])

meta_dictionary["/TTToHadronic_mtop178p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTToHadronic_mtop178p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2"),
  ("sample_category",       "TT_mtop178p5"),
  ("process_name_specific", "TTToHadronic_mtop178p5"),
  ("nof_db_events",         9960120),
  ("nof_db_files",          195),
  ("fsize_db",              553709620124),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 553.71GB; nevents: 9.96M; release: 9_4_7; last modified: 2019-03-07 07:37:44"),
])

meta_dictionary["/TTTo2L2Nu_widthx0p7_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTTo2L2Nu_widthx0p7_TuneCP5_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "TT_widthx0p7"),
  ("process_name_specific", "TTTo2L2Nu_widthx0p7"),
  ("nof_db_events",         5000000),
  ("nof_db_files",          149),
  ("fsize_db",              269339051490),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 269.34GB; nevents: 5.00M; release: 9_4_7; last modified: 2018-10-15 06:42:24"),
])

meta_dictionary["/TTToSemiLeptonic_widthx0p7_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTToSemiLeptonic_widthx0p7_TuneCP5_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "TT_widthx0p7"),
  ("process_name_specific", "TTToSemiLeptonic_widthx0p7"),
  ("nof_db_events",         19983000),
  ("nof_db_files",          412),
  ("fsize_db",              1090044678188),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "94.0%; status: VALID; size: 1.09TB; nevents: 19.98M; release: 9_4_7; last modified: 2018-10-16 23:09:29"),
])

meta_dictionary["/TTTo2L2Nu_widthx0p85_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTTo2L2Nu_widthx0p85_TuneCP5_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "TT_widthx0p85"),
  ("process_name_specific", "TTTo2L2Nu_widthx0p85"),
  ("nof_db_events",         4880000),
  ("nof_db_files",          129),
  ("fsize_db",              262546859916),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 262.55GB; nevents: 4.88M; release: 9_4_7; last modified: 2018-10-13 06:03:55"),
])

meta_dictionary["/TTToSemiLeptonic_widthx0p85_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Apr22_TTToSemiLeptonic_widthx0p85_TuneCP5_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "TT_widthx0p85"),
  ("process_name_specific", "TTToSemiLeptonic_widthx0p85"),
  ("nof_db_events",         18499000),
  ("nof_db_files",          417),
  ("fsize_db",              1009682784661),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 1.01TB; nevents: 18.50M; release: 9_4_6_patch1; last modified: 2018-09-07 17:39:32"),
])

meta_dictionary["/TTTo2L2Nu_widthx1p15_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTTo2L2Nu_widthx1p15_TuneCP5_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "TT_widthx1p15"),
  ("process_name_specific", "TTTo2L2Nu_widthx1p15"),
  ("nof_db_events",         4978000),
  ("nof_db_files",          117),
  ("fsize_db",              267654403110),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 267.65GB; nevents: 4.98M; release: 9_4_7; last modified: 2018-11-11 15:08:51"),
])

meta_dictionary["/TTToSemiLeptonic_widthx1p15_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Apr22_TTToSemiLeptonic_widthx1p15_TuneCP5_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "TT_widthx1p15"),
  ("process_name_specific", "TTToSemiLeptonic_widthx1p15"),
  ("nof_db_events",         19989000),
  ("nof_db_files",          419),
  ("fsize_db",              1090831097088),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 1.09TB; nevents: 19.99M; release: 9_4_7; last modified: 2018-10-13 10:21:46"),
])

meta_dictionary["/TTTo2L2Nu_widthx1p3_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTTo2L2Nu_widthx1p3_TuneCP5_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "TT_widthx1p3"),
  ("process_name_specific", "TTTo2L2Nu_widthx1p3"),
  ("nof_db_events",         4947000),
  ("nof_db_files",          112),
  ("fsize_db",              265885976593),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 265.89GB; nevents: 4.95M; release: 9_4_7; last modified: 2018-10-07 09:12:00"),
])

meta_dictionary["/TTToSemiLeptonic_widthx1p3_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2020Mar31_TTToSemiLeptonic_widthx1p3_TuneCP5_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "TT_widthx1p3"),
  ("process_name_specific", "TTToSemiLeptonic_widthx1p3"),
  ("nof_db_events",         19976000),
  ("nof_db_files",          429),
  ("fsize_db",              1091053966172),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 1.09TB; nevents: 19.98M; release: 9_4_7; last modified: 2018-11-11 13:40:57"),
])


# event statistics by sample category:
# TT_hdampDown:  99.03M
# TT_hdampUp:    90.20M
# TT_ueDown:     89.04M
# TT_ueUp:       92.61M
# TT_QCDbased:   69.97M
# TT_GluonMove:  98.14M
# TT_erdON:      98.59M
# TT_mtop166p5:  44.12M
# TT_mtop169p5:  91.22M
# TT_mtop171p5:  54.94M
# TT_mtop173p5:  69.01M
# TT_mtop175p5:  91.81M
# TT_mtop178p5:  34.76M
# TT_widthx0p7:  24.98M
# TT_widthx0p85: 23.38M
# TT_widthx1p15: 24.97M
# TT_widthx1p3:  24.92M

