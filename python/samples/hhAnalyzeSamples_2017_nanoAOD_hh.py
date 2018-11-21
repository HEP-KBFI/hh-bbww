from collections import OrderedDict as OD

# file generated at 2018-11-13 22:16:21 with the following command:
# create_dictionary.py -m python/samples/metaDict_2017_hh.py -p python/samples/sampleLocations_hh_2017.txt -Z zeroes.txt -z zombies.txt -N samples_2017 -E 2017 -o python/samples -g hhAnalyzeSamples_2017_nanoAOD_hh.py -M

samples_2017 = OD()
samples_2017["/VBFToRadionToHHTo2B2VTo2L2Nu_M-300_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_300_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_spin0_300_hh_2b2v"),
  ("nof_files",                       13),
  ("nof_db_files",                    14),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 279999),
  ("nof_db_events",                   279999),
  ("fsize_local",                     688782350), # 688.78MB, avg file size 52.98MB
  ("fsize_db",                        18070036516), # 18.07GB, avg file size 1.29GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep14_take2/VBFToRadionToHHTo2B2VTo2L2Nu_M-300_narrow_13TeV-madgraph/NanoProduction_v2_2018Sep14_take2_VBFToRadionToHHTo2B2VTo2L2Nu_M-300_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/180914_140805"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2VTo2L2Nu_M-350_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_350_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_spin0_350_hh_2b2v"),
  ("nof_files",                       13),
  ("nof_db_files",                    19),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 285000),
  ("nof_db_events",                   285000),
  ("fsize_local",                     731388774), # 731.39MB, avg file size 56.26MB
  ("fsize_db",                        18927275912), # 18.93GB, avg file size 996.17MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Oct26/VBFToRadionToHHTo2B2VTo2L2Nu_M-350_narrow_13TeV-madgraph/NanoProduction_v2_2018Oct26_VBFToRadionToHHTo2B2VTo2L2Nu_M-350_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/181026_113109"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2VTo2L2Nu_M-400_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_400_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_spin0_400_hh_2b2v"),
  ("nof_files",                       3),
  ("nof_db_files",                    10),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     262521872), # 262.52MB, avg file size 87.51MB
  ("fsize_db",                        6827583120), # 6.83GB, avg file size 682.76MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep14_take2/VBFToRadionToHHTo2B2VTo2L2Nu_M-400_narrow_13TeV-madgraph/NanoProduction_v2_2018Sep14_take2_VBFToRadionToHHTo2B2VTo2L2Nu_M-400_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/180914_141011"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2VTo2L2Nu_M-750_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_750_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_spin0_750_hh_2b2v"),
  ("nof_files",                       3),
  ("nof_db_files",                    13),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     300677665), # 300.68MB, avg file size 100.23MB
  ("fsize_db",                        7423075893), # 7.42GB, avg file size 571.01MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep14_take2/VBFToRadionToHHTo2B2VTo2L2Nu_M-750_narrow_13TeV-madgraph/NanoProduction_v2_2018Sep14_take2_VBFToRadionToHHTo2B2VTo2L2Nu_M-750_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/180914_141219"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_250_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_250_hh_2b2v"),
  ("nof_files",                       8),
  ("nof_db_files",                    14),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     601754962), # 601.75MB, avg file size 75.22MB
  ("fsize_db",                        20842533885), # 20.84GB, avg file size 1.49GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2VTo2L2Nu_M-250_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2VTo2L2Nu_M-250_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_r/181101_082539"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])


samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-260_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_260_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_260_hh_2b2v"),
  ("nof_files",                       8),
  ("nof_db_files",                    17),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     642059002), # 642.06MB, avg file size 80.26MB
  ("fsize_db",                        20086379241), # 20.09GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov13/GluGluToRadionToHHTo2B2VTo2L2Nu_M-260_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov13_GluGluToRadionToHHTo2B2VTo2L2Nu_M-260_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_r/181113_191203"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-270_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_270_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_270_hh_2b2v"),
  ("nof_files",                       8),
  ("nof_db_files",                    19),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 388000),
  ("nof_db_events",                   388000),
  ("fsize_local",                     629181031), # 629.18MB, avg file size 78.65MB
  ("fsize_db",                        19501546911), # 19.50GB, avg file size 1.03GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2VTo2L2Nu_M-270_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2VTo2L2Nu_M-270_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_r/181101_083456"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-280_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_280_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_280_hh_2b2v"),
  ("nof_files",                       8),
  ("nof_db_files",                    14),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 384000),
  ("nof_db_events",                   384000),
  ("fsize_local",                     595883068), # 595.88MB, avg file size 74.49MB
  ("fsize_db",                        20165336883), # 20.17GB, avg file size 1.44GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2VTo2L2Nu_M-280_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2VTo2L2Nu_M-280_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_r/181101_083708"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-320_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_320_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_320_hh_2b2v"),
  ("nof_files",                       6),
  ("nof_db_files",                    20),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     507257915), # 507.26MB, avg file size 84.54MB
  ("fsize_db",                        15538010606), # 15.54GB, avg file size 776.90MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2VTo2L2Nu_M-320_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2VTo2L2Nu_M-320_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_r/181101_083919"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-350_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_350_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_350_hh_2b2v"),
  ("nof_files",                       6),
  ("nof_db_files",                    12),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     522775069), # 522.78MB, avg file size 87.13MB
  ("fsize_db",                        15654716885), # 15.65GB, avg file size 1.30GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2VTo2L2Nu_M-350_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2VTo2L2Nu_M-350_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_r/181101_084126"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-400_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_400_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_400_hh_2b2v"),
  ("nof_files",                       6),
  ("nof_db_files",                    16),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 292000),
  ("nof_db_events",                   292000),
  ("fsize_local",                     533138888), # 533.14MB, avg file size 88.86MB
  ("fsize_db",                        15536600053), # 15.54GB, avg file size 971.04MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/GluGluToRadionToHHTo2B2VTo2L2Nu_M-400_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Sep26_GluGluToRadionToHHTo2B2VTo2L2Nu_M-400_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_r/180926_132010"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-450_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_450_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_450_hh_2b2v"),
  ("nof_files",                       6),
  ("nof_db_files",                    20),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     570782054), # 570.78MB, avg file size 95.13MB
  ("fsize_db",                        16296871303), # 16.30GB, avg file size 814.84MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2VTo2L2Nu_M-450_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2VTo2L2Nu_M-450_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_r/181101_084508"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_500_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_500_hh_2b2v"),
  ("nof_files",                       4),
  ("nof_db_files",                    12),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     395421108), # 395.42MB, avg file size 98.86MB
  ("fsize_db",                        10964750047), # 10.96GB, avg file size 913.73MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2VTo2L2Nu_M-500_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2VTo2L2Nu_M-500_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_r/181101_084712"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-600_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_600_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_600_hh_2b2v"),
  ("nof_files",                       4),
  ("nof_db_files",                    9),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     416288732), # 416.29MB, avg file size 104.07MB
  ("fsize_db",                        11169462986), # 11.17GB, avg file size 1.24GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2VTo2L2Nu_M-600_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2VTo2L2Nu_M-600_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_r/181101_084845"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-650_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_650_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_650_hh_2b2v"),
  ("nof_files",                       4),
  ("nof_db_files",                    12),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     424617035), # 424.62MB, avg file size 106.15MB
  ("fsize_db",                        11395262580), # 11.40GB, avg file size 949.61MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2VTo2L2Nu_M-650_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2VTo2L2Nu_M-650_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_r/181101_085056"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-700_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_700_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_700_hh_2b2v"),
  ("nof_files",                       4),
  ("nof_db_files",                    8),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     432038247), # 432.04MB, avg file size 108.01MB
  ("fsize_db",                        11438629863), # 11.44GB, avg file size 1.43GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2VTo2L2Nu_M-700_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2VTo2L2Nu_M-700_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_r/181101_085309"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_750_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_750_hh_2b2v"),
  ("nof_files",                       4),
  ("nof_db_files",                    11),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     424474498), # 424.47MB, avg file size 106.12MB
  ("fsize_db",                        11931037531), # 11.93GB, avg file size 1.08GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2VTo2L2Nu_M-750_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2VTo2L2Nu_M-750_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_r/181101_085515"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-800_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_800_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_800_hh_2b2v"),
  ("nof_files",                       4),
  ("nof_db_files",                    15),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 197000),
  ("nof_db_events",                   197000),
  ("fsize_local",                     423638150), # 423.64MB, avg file size 105.91MB
  ("fsize_db",                        11877663068), # 11.88GB, avg file size 791.84MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2VTo2L2Nu_M-800_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2VTo2L2Nu_M-800_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_r/181101_085721"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-850_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_850_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_850_hh_2b2v"),
  ("nof_files",                       4),
  ("nof_db_files",                    15),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     434774492), # 434.77MB, avg file size 108.69MB
  ("fsize_db",                        12127308050), # 12.13GB, avg file size 808.49MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/GluGluToRadionToHHTo2B2VTo2L2Nu_M-850_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Sep26_GluGluToRadionToHHTo2B2VTo2L2Nu_M-850_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_r/180926_132538"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-900_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_900_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_900_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    11),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     225396966), # 225.40MB, avg file size 112.70MB
  ("fsize_db",                        5935911198), # 5.94GB, avg file size 539.63MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2VTo2L2Nu_M-900_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2VTo2L2Nu_M-900_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_r/181101_090208"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-1000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1000_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_1000_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    7),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     228922576), # 228.92MB, avg file size 114.46MB
  ("fsize_db",                        5930718483), # 5.93GB, avg file size 847.25MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/GluGluToRadionToHHTo2B2VTo2L2Nu_M-1000_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Sep26_GluGluToRadionToHHTo2B2VTo2L2Nu_M-1000_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_/180926_132852"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-1250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1250_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_1250_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    8),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     227958808), # 227.96MB, avg file size 113.98MB
  ("fsize_db",                        6224151597), # 6.22GB, avg file size 778.02MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2VTo2L2Nu_M-1250_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2VTo2L2Nu_M-1250_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_/181101_090657"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-1500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1500_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_1500_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    12),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 99998),
  ("nof_db_events",                   99998),
  ("fsize_local",                     238302794), # 238.30MB, avg file size 119.15MB
  ("fsize_db",                        6171310375), # 6.17GB, avg file size 514.28MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2VTo2L2Nu_M-1500_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2VTo2L2Nu_M-1500_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_/181101_090901"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-1750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1750_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_1750_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    10),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     232252652), # 232.25MB, avg file size 116.13MB
  ("fsize_db",                        6356319473), # 6.36GB, avg file size 635.63MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2VTo2L2Nu_M-1750_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2VTo2L2Nu_M-1750_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_/181101_091110"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-2000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_2000_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_2000_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    8),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     243334292), # 243.33MB, avg file size 121.67MB
  ("fsize_db",                        6172348486), # 6.17GB, avg file size 771.54MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2VTo2L2Nu_M-2000_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2VTo2L2Nu_M-2000_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_/181101_091315"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-2500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_2500_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_2500_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    13),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 97000),
  ("nof_db_events",                   97000),
  ("fsize_local",                     229998197), # 230.00MB, avg file size 115.00MB
  ("fsize_db",                        6425534542), # 6.43GB, avg file size 494.27MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2VTo2L2Nu_M-2500_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2VTo2L2Nu_M-2500_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_/181101_091526"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-3000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_3000_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_3000_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    11),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 97999),
  ("nof_db_events",                   97999),
  ("fsize_local",                     233888195), # 233.89MB, avg file size 116.94MB
  ("fsize_db",                        6497731845), # 6.50GB, avg file size 590.70MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2VTo2L2Nu_M-3000_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2VTo2L2Nu_M-3000_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_/181101_091732"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_1_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_1_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_1_hh_2b2v"),
  ("nof_files",                       8),
  ("nof_db_files",                    12),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 399996),
  ("nof_db_events",                   399996),
  ("fsize_local",                     722153064), # 722.15MB, avg file size 90.27MB
  ("fsize_db",                        22186460848), # 22.19GB, avg file size 1.85GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Oct28/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_1_13TeV-madgraph/NanoProduction_v2_2018Oct28_VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_1_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/181027_224534"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2VTo2L2Nu_node_SM_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_node_sm_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_sm_hh_2b2v"),
  ("nof_files",                       8),
  ("nof_db_files",                    17),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 388999),
  ("nof_db_events",                   388999),
  ("fsize_local",                     789254840), # 789.25MB, avg file size 98.66MB
  ("fsize_db",                        21257341288), # 21.26GB, avg file size 1.25GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Oct28/GluGluToHHTo2B2VTo2L2Nu_node_SM_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Oct28_GluGluToHHTo2B2VTo2L2Nu_node_SM_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/181027_224746"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2VTo2L2Nu_node_2_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_node_2_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_2_hh_2b2v"),
  ("nof_files",                       8),
  ("nof_db_files",                    17),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     886316211), # 886.32MB, avg file size 110.79MB
  ("fsize_db",                        23088598268), # 23.09GB, avg file size 1.36GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Oct28/GluGluToHHTo2B2VTo2L2Nu_node_2_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Oct28_GluGluToHHTo2B2VTo2L2Nu_node_2_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/181027_224953"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2VTo2L2Nu_node_3_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_node_3_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_3_hh_2b2v"),
  ("nof_files",                       8),
  ("nof_db_files",                    17),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 380000),
  ("nof_db_events",                   380000),
  ("fsize_local",                     774597689), # 774.60MB, avg file size 96.82MB
  ("fsize_db",                        20768532098), # 20.77GB, avg file size 1.22GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Oct28/GluGluToHHTo2B2VTo2L2Nu_node_3_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Oct28_GluGluToHHTo2B2VTo2L2Nu_node_3_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/181027_225158"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2VTo2L2Nu_node_7_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_node_7_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_7_hh_2b2v"),
  ("nof_files",                       8),
  ("nof_db_files",                    19),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 392999),
  ("nof_db_events",                   392999),
  ("fsize_local",                     779893857), # 779.89MB, avg file size 97.49MB
  ("fsize_db",                        21440735341), # 21.44GB, avg file size 1.13GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Oct28/GluGluToHHTo2B2VTo2L2Nu_node_7_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Oct28_GluGluToHHTo2B2VTo2L2Nu_node_7_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/181027_225331"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2VTo2L2Nu_node_9_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_node_9_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_9_hh_2b2v"),
  ("nof_files",                       8),
  ("nof_db_files",                    19),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 386999),
  ("nof_db_events",                   386999),
  ("fsize_local",                     862077561), # 862.08MB, avg file size 107.76MB
  ("fsize_db",                        22534822736), # 22.53GB, avg file size 1.19GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Oct28/GluGluToHHTo2B2VTo2L2Nu_node_9_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Oct28_GluGluToHHTo2B2VTo2L2Nu_node_9_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/181027_225535"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2VTo2L2Nu_node_12_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_node_12_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_12_hh_2b2v"),
  ("nof_files",                       9),
  ("nof_db_files",                    23),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     794367529), # 794.37MB, avg file size 88.26MB
  ("fsize_db",                        21561540290), # 21.56GB, avg file size 937.46MB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Oct28/GluGluToHHTo2B2VTo2L2Nu_node_12_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Oct28_GluGluToHHTo2B2VTo2L2Nu_node_12_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/181027_225747"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-250_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_250_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_250_hh_2b2t"),
  ("nof_files",                       8),
  ("nof_db_files",                    23),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     888781574), # 888.78MB, avg file size 111.10MB
  ("fsize_db",                        24640211831), # 24.64GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Oct26/VBFToRadionToHHTo2B2Tau_M-250_narrow_13TeV-madgraph/NanoProduction_v2_2018Oct26_VBFToRadionToHHTo2B2Tau_M-250_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/181026_122108"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-260_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_260_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_260_hh_2b2t"),
  ("nof_files",                       8),
  ("nof_db_files",                    18),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 388000),
  ("nof_db_events",                   388000),
  ("fsize_local",                     872819902), # 872.82MB, avg file size 109.10MB
  ("fsize_db",                        24012313674), # 24.01GB, avg file size 1.33GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/VBFToRadionToHHTo2B2Tau_M-260_narrow_13TeV-madgraph/NanoProduction_v2_2018Sep26_VBFToRadionToHHTo2B2Tau_M-260_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_150132"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-270_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_270_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_270_hh_2b2t"),
  ("nof_files",                       8),
  ("nof_db_files",                    17),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 384000),
  ("nof_db_events",                   384000),
  ("fsize_local",                     874955304), # 874.96MB, avg file size 109.37MB
  ("fsize_db",                        23968184441), # 23.97GB, avg file size 1.41GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/VBFToRadionToHHTo2B2Tau_M-270_narrow_13TeV-madgraph/NanoProduction_v2_2018Sep26_VBFToRadionToHHTo2B2Tau_M-270_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/180926_150515"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-280_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_280_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_280_hh_2b2t"),
  ("nof_files",                       8),
  ("nof_db_files",                    23),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     920488020), # 920.49MB, avg file size 115.06MB
  ("fsize_db",                        25138262751), # 25.14GB, avg file size 1.09GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/VBFToRadionToHHTo2B2Tau_M-280_narrow_13TeV-madgraph/NanoProduction_v2_2018Sep26_VBFToRadionToHHTo2B2Tau_M-280_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_150854"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-300_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_300_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_300_hh_2b2t"),
  ("nof_files",                       6),
  ("nof_db_files",                    15),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     705839041), # 705.84MB, avg file size 117.64MB
  ("fsize_db",                        19012035463), # 19.01GB, avg file size 1.27GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Oct26/VBFToRadionToHHTo2B2Tau_M-300_narrow_13TeV-madgraph/NanoProduction_v2_2018Oct26_VBFToRadionToHHTo2B2Tau_M-300_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/181026_122316"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-350_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_350_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_350_hh_2b2t"),
  ("nof_files",                       6),
  ("nof_db_files",                    11),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     741458833), # 741.46MB, avg file size 123.58MB
  ("fsize_db",                        19447040410), # 19.45GB, avg file size 1.77GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/VBFToRadionToHHTo2B2Tau_M-350_narrow_13TeV-madgraph/NanoProduction_v2_2018Sep26_VBFToRadionToHHTo2B2Tau_M-350_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/180926_151218"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-400_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_400_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_400_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    7),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     257800602), # 257.80MB, avg file size 128.90MB
  ("fsize_db",                        6609409571), # 6.61GB, avg file size 944.20MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/VBFToRadionToHHTo2B2Tau_M-400_narrow_13TeV-madgraph/NanoProduction_v2_2018Sep26_VBFToRadionToHHTo2B2Tau_M-400_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/180926_151525"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-450_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_450_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_450_hh_2b2t"),
  ("nof_files",                       6),
  ("nof_db_files",                    16),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     800415422), # 800.42MB, avg file size 133.40MB
  ("fsize_db",                        20167217854), # 20.17GB, avg file size 1.26GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/VBFToRadionToHHTo2B2Tau_M-450_narrow_13TeV-madgraph/NanoProduction_v2_2018Sep26_VBFToRadionToHHTo2B2Tau_M-450_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_151850"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-500_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_500_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_500_hh_2b2t"),
  ("nof_files",                       7),
  ("nof_db_files",                    11),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 290000),
  ("nof_db_events",                   290000),
  ("fsize_local",                     799446933), # 799.45MB, avg file size 114.21MB
  ("fsize_db",                        19708690689), # 19.71GB, avg file size 1.79GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/VBFToRadionToHHTo2B2Tau_M-500_narrow_13TeV-madgraph/NanoProduction_v2_2018Sep26_VBFToRadionToHHTo2B2Tau_M-500_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_152200"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-550_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_550_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_550_hh_2b2t"),
  ("nof_files",                       6),
  ("nof_db_files",                    13),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     844315066), # 844.32MB, avg file size 140.72MB
  ("fsize_db",                        20644816504), # 20.64GB, avg file size 1.59GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/VBFToRadionToHHTo2B2Tau_M-550_narrow_13TeV-madgraph/NanoProduction_v2_2018Sep26_VBFToRadionToHHTo2B2Tau_M-550_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_152458"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-600_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_600_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_600_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    12),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     574103352), # 574.10MB, avg file size 143.53MB
  ("fsize_db",                        13957904944), # 13.96GB, avg file size 1.16GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/VBFToRadionToHHTo2B2Tau_M-600_narrow_13TeV-madgraph/NanoProduction_v2_2018Sep26_VBFToRadionToHHTo2B2Tau_M-600_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_152728"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-650_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_650_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_650_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    7),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     583449868), # 583.45MB, avg file size 145.86MB
  ("fsize_db",                        14016331858), # 14.02GB, avg file size 2.00GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/VBFToRadionToHHTo2B2Tau_M-650_narrow_13TeV-madgraph/NanoProduction_v2_2018Sep26_VBFToRadionToHHTo2B2Tau_M-650_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_153024"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-700_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_700_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_700_hh_2b2t"),
  ("nof_files",                       5),
  ("nof_db_files",                    13),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     595639418), # 595.64MB, avg file size 119.13MB
  ("fsize_db",                        14253263609), # 14.25GB, avg file size 1.10GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/VBFToRadionToHHTo2B2Tau_M-700_narrow_13TeV-madgraph/NanoProduction_v2_2018Sep26_VBFToRadionToHHTo2B2Tau_M-700_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_153433"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-750_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_750_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_750_hh_2b2t"),
  ("nof_files",                       3),
  ("nof_db_files",                    7),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     302962315), # 302.96MB, avg file size 100.99MB
  ("fsize_db",                        7146269195), # 7.15GB, avg file size 1.02GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/VBFToRadionToHHTo2B2Tau_M-750_narrow_13TeV-madgraph/NanoProduction_v2_2018Sep26_VBFToRadionToHHTo2B2Tau_M-750_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/180926_153839"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-800_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_800_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_800_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    11),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     607048134), # 607.05MB, avg file size 151.76MB
  ("fsize_db",                        14420020815), # 14.42GB, avg file size 1.31GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/VBFToRadionToHHTo2B2Tau_M-800_narrow_13TeV-madgraph/NanoProduction_v2_2018Sep26_VBFToRadionToHHTo2B2Tau_M-800_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_154240"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-850_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_850_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_850_hh_2b2t"),
  ("nof_files",                       5),
  ("nof_db_files",                    14),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     614983259), # 614.98MB, avg file size 123.00MB
  ("fsize_db",                        14617490096), # 14.62GB, avg file size 1.04GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/VBFToRadionToHHTo2B2Tau_M-850_narrow_13TeV-madgraph/NanoProduction_v2_2018Sep26_VBFToRadionToHHTo2B2Tau_M-850_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_154621"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-900_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_900_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_900_hh_2b2t"),
  ("nof_files",                       3),
  ("nof_db_files",                    11),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     311742460), # 311.74MB, avg file size 103.91MB
  ("fsize_db",                        7382733082), # 7.38GB, avg file size 671.16MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/VBFToRadionToHHTo2B2Tau_M-900_narrow_13TeV-madgraph/NanoProduction_v2_2018Sep26_VBFToRadionToHHTo2B2Tau_M-900_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_154951"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-1000_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_1000_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_1000_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    7),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     313616209), # 313.62MB, avg file size 156.81MB
  ("fsize_db",                        7364574553), # 7.36GB, avg file size 1.05GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/VBFToRadionToHHTo2B2Tau_M-1000_narrow_13TeV-madgraph/NanoProduction_v2_2018Sep26_VBFToRadionToHHTo2B2Tau_M-1000_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_155304"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-1250_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_1250_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_1250_hh_2b2t"),
  ("nof_files",                       3),
  ("nof_db_files",                    7),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     163163393), # 163.16MB, avg file size 54.39MB
  ("fsize_db",                        7497237044), # 7.50GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/VBFToRadionToHHTo2B2Tau_M-1250_narrow_13TeV-madgraph/NanoProduction_v2_2018Sep26_VBFToRadionToHHTo2B2Tau_M-1250_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_155638"),
        ("selection", "*"),
        ("blacklist", [1]),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-1500_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_1500_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_1500_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    5),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     324576045), # 324.58MB, avg file size 162.29MB
  ("fsize_db",                        7582428905), # 7.58GB, avg file size 1.52GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/VBFToRadionToHHTo2B2Tau_M-1500_narrow_13TeV-madgraph/NanoProduction_v2_2018Sep26_VBFToRadionToHHTo2B2Tau_M-1500_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_155957"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-1750_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_1750_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_1750_hh_2b2t"),
  ("nof_files",                       3),
  ("nof_db_files",                    12),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     329912211), # 329.91MB, avg file size 109.97MB
  ("fsize_db",                        7802866732), # 7.80GB, avg file size 650.24MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/VBFToRadionToHHTo2B2Tau_M-1750_narrow_13TeV-madgraph/NanoProduction_v2_2018Sep26_VBFToRadionToHHTo2B2Tau_M-1750_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_160320"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-2000_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_2000_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_2000_hh_2b2t"),
  ("nof_files",                       3),
  ("nof_db_files",                    11),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     331174553), # 331.17MB, avg file size 110.39MB
  ("fsize_db",                        7810715378), # 7.81GB, avg file size 710.07MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/VBFToRadionToHHTo2B2Tau_M-2000_narrow_13TeV-madgraph/NanoProduction_v2_2018Sep26_VBFToRadionToHHTo2B2Tau_M-2000_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_160636"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-3000_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_3000_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_3000_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    8),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     330979161), # 330.98MB, avg file size 165.49MB
  ("fsize_db",                        7943092984), # 7.94GB, avg file size 992.89MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov14/VBFToRadionToHHTo2B2Tau_M-3000_narrow_13TeV-madgraph/NanoProduction_v2_2018Nov14_VBFToRadionToHHTo2B2Tau_M-3000_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/181114_092640"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-260_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_260_hh_bbtt_noncorr"),
  ("process_name_specific",           "signal_ggf_spin0_260_hh_2b2t_noncorr"),
  ("nof_files",                       6),
  ("nof_db_files",                    15),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 270000),
  ("nof_db_events",                   270000),
  ("fsize_local",                     425455617), # 425.46MB, avg file size 70.91MB
  ("fsize_db",                        13445383362), # 13.45GB, avg file size 896.36MB
  ("use_it",                          False),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/GluGluToRadionToHHTo2B2Tau_M-260_narrow_13TeV-madgraph/NanoProduction_v2_2018Sep26_GluGluToRadionToHHTo2B2Tau_M-260_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_140829"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-270_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_270_hh_bbtt_noncorr"),
  ("process_name_specific",           "signal_ggf_spin0_270_hh_2b2t_noncorr"),
  ("nof_files",                       6),
  ("nof_db_files",                    15),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     475907629), # 475.91MB, avg file size 79.32MB
  ("fsize_db",                        15004164477), # 15.00GB, avg file size 1.00GB
  ("use_it",                          False),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2Tau_M-270_narrow_13TeV-madgraph/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2Tau_M-270_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/181101_091908"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-300_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_300_hh_bbtt_noncorr"),
  ("process_name_specific",           "signal_ggf_spin0_300_hh_2b2t_noncorr"),
  ("nof_files",                       11),
  ("nof_db_files",                    30),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 500000),
  ("nof_db_events",                   500000),
  ("fsize_local",                     819517729), # 819.52MB, avg file size 74.50MB
  ("fsize_db",                        25493703953), # 25.49GB, avg file size 849.79MB
  ("use_it",                          False),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/GluGluToRadionToHHTo2B2Tau_M-300_narrow_13TeV-madgraph/NanoProduction_v2_2018Sep26_GluGluToRadionToHHTo2B2Tau_M-300_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_141706"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-350_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_350_hh_bbtt_noncorr"),
  ("process_name_specific",           "signal_ggf_spin0_350_hh_2b2t_noncorr"),
  ("nof_files",                       6),
  ("nof_db_files",                    10),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     518909960), # 518.91MB, avg file size 86.48MB
  ("fsize_db",                        15628942112), # 15.63GB, avg file size 1.56GB
  ("use_it",                          False),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/GluGluToRadionToHHTo2B2Tau_M-350_narrow_13TeV-madgraph/NanoProduction_v2_2018Sep26_GluGluToRadionToHHTo2B2Tau_M-350_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_142125"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-400_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_400_hh_bbtt_noncorr"),
  ("process_name_specific",           "signal_ggf_spin0_400_hh_2b2t_noncorr"),
  ("nof_files",                       6),
  ("nof_db_files",                    18),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 278000),
  ("nof_db_events",                   278000),
  ("fsize_local",                     509796890), # 509.80MB, avg file size 84.97MB
  ("fsize_db",                        14938047142), # 14.94GB, avg file size 829.89MB
  ("use_it",                          False),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/GluGluToRadionToHHTo2B2Tau_M-400_narrow_13TeV-madgraph/NanoProduction_v2_2018Sep26_GluGluToRadionToHHTo2B2Tau_M-400_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_142716"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-450_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_450_hh_bbtt_noncorr"),
  ("process_name_specific",           "signal_ggf_spin0_450_hh_2b2t_noncorr"),
  ("nof_files",                       2),
  ("nof_db_files",                    9),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     193590153), # 193.59MB, avg file size 96.80MB
  ("fsize_db",                        5476096947), # 5.48GB, avg file size 608.46MB
  ("use_it",                          False),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/GluGluToRadionToHHTo2B2Tau_M-450_narrow_13TeV-madgraph/NanoProduction_v2_2018Sep26_GluGluToRadionToHHTo2B2Tau_M-450_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_143204"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-500_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_500_hh_bbtt_noncorr"),
  ("process_name_specific",           "signal_ggf_spin0_500_hh_2b2t_noncorr"),
  ("nof_files",                       2),
  ("nof_db_files",                    3),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     202376664), # 202.38MB, avg file size 101.19MB
  ("fsize_db",                        5508412042), # 5.51GB, avg file size 1.84GB
  ("use_it",                          False),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/GluGluToRadionToHHTo2B2Tau_M-500_narrow_13TeV-madgraph/NanoProduction_v2_2018Sep26_GluGluToRadionToHHTo2B2Tau_M-500_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_143604"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-550_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_550_hh_bbtt_noncorr"),
  ("process_name_specific",           "signal_ggf_spin0_550_hh_2b2t_noncorr"),
  ("nof_files",                       2),
  ("nof_db_files",                    6),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     210242463), # 210.24MB, avg file size 105.12MB
  ("fsize_db",                        5599595099), # 5.60GB, avg file size 933.27MB
  ("use_it",                          False),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/GluGluToRadionToHHTo2B2Tau_M-550_narrow_13TeV-madgraph/NanoProduction_v2_2018Sep26_GluGluToRadionToHHTo2B2Tau_M-550_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_143933"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-600_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_600_hh_bbtt_noncorr"),
  ("process_name_specific",           "signal_ggf_spin0_600_hh_2b2t_noncorr"),
  ("nof_files",                       2),
  ("nof_db_files",                    15),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     215809942), # 215.81MB, avg file size 107.90MB
  ("fsize_db",                        5851929979), # 5.85GB, avg file size 390.13MB
  ("use_it",                          False),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/GluGluToRadionToHHTo2B2Tau_M-600_narrow_13TeV-madgraph/NanoProduction_v2_2018Sep26_GluGluToRadionToHHTo2B2Tau_M-600_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_144347"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-650_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_650_hh_bbtt_noncorr"),
  ("process_name_specific",           "signal_ggf_spin0_650_hh_2b2t_noncorr"),
  ("nof_files",                       2),
  ("nof_db_files",                    5),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     220438708), # 220.44MB, avg file size 110.22MB
  ("fsize_db",                        5741157480), # 5.74GB, avg file size 1.15GB
  ("use_it",                          False),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/GluGluToRadionToHHTo2B2Tau_M-650_narrow_13TeV-madgraph/NanoProduction_v2_2018Sep26_GluGluToRadionToHHTo2B2Tau_M-650_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_144838"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-900_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_900_hh_bbtt_noncorr"),
  ("process_name_specific",           "signal_ggf_spin0_900_hh_2b2t_noncorr"),
  ("nof_files",                       3),
  ("nof_db_files",                    6),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     236599811), # 236.60MB, avg file size 78.87MB
  ("fsize_db",                        5935488747), # 5.94GB, avg file size 989.25MB
  ("use_it",                          False),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/GluGluToRadionToHHTo2B2Tau_M-900_narrow_13TeV-madgraph/NanoProduction_v2_2018Sep26_GluGluToRadionToHHTo2B2Tau_M-900_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_145259"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_250_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_250_hh_2b2t"),
  ("nof_files",                       8),
  ("nof_db_files",                    17),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 390000),
  ("nof_db_events",                   390000),
  ("fsize_local",                     577643614), # 577.64MB, avg file size 72.21MB
  ("fsize_db",                        20093492648), # 20.09GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2Tau_M-250_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2Tau_M-250_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realis/181101_092114"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-260_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_260_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_260_hh_2b2t"),
  ("nof_files",                       8),
  ("nof_db_files",                    18),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 360000),
  ("nof_db_events",                   360000),
  ("fsize_local",                     571127598), # 571.13MB, avg file size 71.39MB
  ("fsize_db",                        17758553715), # 17.76GB, avg file size 986.59MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2Tau_M-260_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2Tau_M-260_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realis/181101_092248"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-270_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_270_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_270_hh_2b2t"),
  ("nof_files",                       8),
  ("nof_db_files",                    16),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 392000),
  ("nof_db_events",                   392000),
  ("fsize_local",                     624983441), # 624.98MB, avg file size 78.12MB
  ("fsize_db",                        19361033085), # 19.36GB, avg file size 1.21GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2Tau_M-270_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2Tau_M-270_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realis/181101_092459"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-280_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_280_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_280_hh_2b2t"),
  ("nof_files",                       9),
  ("nof_db_files",                    23),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 398000),
  ("nof_db_events",                   398000),
  ("fsize_local",                     609062461), # 609.06MB, avg file size 67.67MB
  ("fsize_db",                        20704800616), # 20.70GB, avg file size 900.21MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/GluGluToRadionToHHTo2B2Tau_M-280_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Sep26_GluGluToRadionToHHTo2B2Tau_M-280_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realis/180926_141325"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-300_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_300_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_300_hh_2b2t"),
  ("nof_files",                       6),
  ("nof_db_files",                    22),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     490085875), # 490.09MB, avg file size 81.68MB
  ("fsize_db",                        15151937781), # 15.15GB, avg file size 688.72MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2Tau_M-300_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2Tau_M-300_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realis/181101_092841"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-320_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_320_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_320_hh_2b2t"),
  ("nof_files",                       6),
  ("nof_db_files",                    13),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     500026223), # 500.03MB, avg file size 83.34MB
  ("fsize_db",                        15215406969), # 15.22GB, avg file size 1.17GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2Tau_M-320_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2Tau_M-320_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realis/181101_093045"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-350_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_350_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_350_hh_2b2t"),
  ("nof_files",                       6),
  ("nof_db_files",                    14),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     514130271), # 514.13MB, avg file size 85.69MB
  ("fsize_db",                        15430234358), # 15.43GB, avg file size 1.10GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2Tau_M-350_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2Tau_M-350_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realis/181101_093309"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-400_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_400_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_400_hh_2b2t"),
  ("nof_files",                       6),
  ("nof_db_files",                    16),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 296000),
  ("nof_db_events",                   296000),
  ("fsize_local",                     533030898), # 533.03MB, avg file size 88.84MB
  ("fsize_db",                        15540706594), # 15.54GB, avg file size 971.29MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2Tau_M-400_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2Tau_M-400_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realis/181101_093446"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-450_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_450_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_450_hh_2b2t"),
  ("nof_files",                       6),
  ("nof_db_files",                    18),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 272000),
  ("nof_db_events",                   272000),
  ("fsize_local",                     513697480), # 513.70MB, avg file size 85.62MB
  ("fsize_db",                        14544281532), # 14.54GB, avg file size 808.02MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2Tau_M-450_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2Tau_M-450_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realis/181101_093655"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_500_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_500_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    12),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 190000),
  ("nof_db_events",                   190000),
  ("fsize_local",                     374999801), # 375.00MB, avg file size 93.75MB
  ("fsize_db",                        10300681960), # 10.30GB, avg file size 858.39MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2Tau_M-500_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2Tau_M-500_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realis/181101_093836"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-550_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_550_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_550_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    11),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     406901872), # 406.90MB, avg file size 101.73MB
  ("fsize_db",                        10884541416), # 10.88GB, avg file size 989.50MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2Tau_M-550_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2Tau_M-550_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realis/181101_094042"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-600_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_600_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_600_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    12),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     417532384), # 417.53MB, avg file size 104.38MB
  ("fsize_db",                        11044936345), # 11.04GB, avg file size 920.41MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2Tau_M-600_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2Tau_M-600_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realis/181101_094222"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-650_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_650_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_650_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    15),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 188000),
  ("nof_db_events",                   188000),
  ("fsize_local",                     403224305), # 403.22MB, avg file size 100.81MB
  ("fsize_db",                        10510514184), # 10.51GB, avg file size 700.70MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2Tau_M-650_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2Tau_M-650_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realis/181101_094432"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-700_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_700_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_700_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    8),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     435915209), # 435.92MB, avg file size 108.98MB
  ("fsize_db",                        11214998225), # 11.21GB, avg file size 1.40GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2Tau_M-700_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2Tau_M-700_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realis/181101_094728"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_750_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_750_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    12),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 196000),
  ("nof_db_events",                   196000),
  ("fsize_local",                     421907924), # 421.91MB, avg file size 105.48MB
  ("fsize_db",                        11545737081), # 11.55GB, avg file size 962.14MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2Tau_M-750_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2Tau_M-750_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realis/181101_095008"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-800_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_800_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_800_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    10),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     437935732), # 437.94MB, avg file size 109.48MB
  ("fsize_db",                        11819983411), # 11.82GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov05/GluGluToRadionToHHTo2B2Tau_M-800_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov05_GluGluToRadionToHHTo2B2Tau_M-800_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realis/181105_204009"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-850_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_850_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_850_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    15),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 192000),
  ("nof_db_events",                   192000),
  ("fsize_local",                     425324177), # 425.32MB, avg file size 106.33MB
  ("fsize_db",                        11490975329), # 11.49GB, avg file size 766.07MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2Tau_M-850_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2Tau_M-850_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realis/181101_095454"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-900_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_900_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_900_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    7),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 95000),
  ("nof_db_events",                   95000),
  ("fsize_local",                     218649052), # 218.65MB, avg file size 109.32MB
  ("fsize_db",                        5517036529), # 5.52GB, avg file size 788.15MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2Tau_M-900_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2Tau_M-900_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realis/181101_095704"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-1000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1000_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_1000_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    9),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     234769701), # 234.77MB, avg file size 117.38MB
  ("fsize_db",                        5887358169), # 5.89GB, avg file size 654.15MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2Tau_M-1000_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2Tau_M-1000_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_reali/181101_095948"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-1250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1250_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_1250_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    9),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     233514622), # 233.51MB, avg file size 116.76MB
  ("fsize_db",                        6210975535), # 6.21GB, avg file size 690.11MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2Tau_M-1250_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2Tau_M-1250_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_reali/181101_100206"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-1500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1500_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_1500_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    4),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     242595569), # 242.60MB, avg file size 121.30MB
  ("fsize_db",                        5949909431), # 5.95GB, avg file size 1.49GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2Tau_M-1500_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2Tau_M-1500_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_reali/181101_100418"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-1750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1750_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_1750_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    11),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     236078075), # 236.08MB, avg file size 118.04MB
  ("fsize_db",                        6303523737), # 6.30GB, avg file size 573.05MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov05/GluGluToRadionToHHTo2B2Tau_M-1750_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov05_GluGluToRadionToHHTo2B2Tau_M-1750_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_reali/181105_204232"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-2000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_2000_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_2000_hh_2b2t"),
  ("nof_files",                       3),
  ("nof_db_files",                    6),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 92000),
  ("nof_db_events",                   92000),
  ("fsize_local",                     229150619), # 229.15MB, avg file size 76.38MB
  ("fsize_db",                        5565938746), # 5.57GB, avg file size 927.66MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2Tau_M-2000_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2Tau_M-2000_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_reali/181101_100848"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-2500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_2500_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_2500_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    11),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     237918875), # 237.92MB, avg file size 118.96MB
  ("fsize_db",                        6456631366), # 6.46GB, avg file size 586.97MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/GluGluToRadionToHHTo2B2Tau_M-2500_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Sep26_GluGluToRadionToHHTo2B2Tau_M-2500_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_reali/180926_145741"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-3000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_3000_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_3000_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    8),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     238547840), # 238.55MB, avg file size 119.27MB
  ("fsize_db",                        6431618251), # 6.43GB, avg file size 803.95MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Nov01/GluGluToRadionToHHTo2B2Tau_M-3000_narrow_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Nov01_GluGluToRadionToHHTo2B2Tau_M-3000_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_reali/181101_101408"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/VBFHHTo2B2Tau_CV_1_C2V_1_C3_0_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_0_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_0_hh_2b2t"),
  ("nof_files",                       9),
  ("nof_db_files",                    26),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 369000),
  ("nof_db_events",                   369000),
  ("fsize_local",                     663282738), # 663.28MB, avg file size 73.70MB
  ("fsize_db",                        20317409524), # 20.32GB, avg file size 781.44MB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/VBFHHTo2B2Tau_CV_1_C2V_1_C3_0_13TeV-madgraph/NanoProduction_v2_2018Sep26_VBFHHTo2B2Tau_CV_1_C2V_1_C3_0_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_161927"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/VBFHHTo2B2Tau_CV_1_C2V_1_C3_1_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_1_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_1_hh_2b2t"),
  ("nof_files",                       6),
  ("nof_db_files",                    20),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     535651288), # 535.65MB, avg file size 89.28MB
  ("fsize_db",                        16551491719), # 16.55GB, avg file size 827.57MB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/VBFHHTo2B2Tau_CV_1_C2V_1_C3_1_13TeV-madgraph/NanoProduction_v2_2018Sep26_VBFHHTo2B2Tau_CV_1_C2V_1_C3_1_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/180926_162201"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/VBFHHTo2B2Tau_CV_1_C2V_1_C3_2_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_2_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_2_hh_2b2t"),
  ("nof_files",                       8),
  ("nof_db_files",                    9),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     764528243), # 764.53MB, avg file size 95.57MB
  ("fsize_db",                        22555887148), # 22.56GB, avg file size 2.51GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/VBFHHTo2B2Tau_CV_1_C2V_1_C3_2_13TeV-madgraph/NanoProduction_v2_2018Sep26_VBFHHTo2B2Tau_CV_1_C2V_1_C3_2_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_162515"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/VBFHHTo2B2Tau_CV_1_C2V_2_C3_1_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_2_1_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_2_1_hh_2b2t"),
  ("nof_files",                       9),
  ("nof_db_files",                    24),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     901461462), # 901.46MB, avg file size 100.16MB
  ("fsize_db",                        23834632407), # 23.83GB, avg file size 993.11MB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/VBFHHTo2B2Tau_CV_1_C2V_2_C3_1_13TeV-madgraph/NanoProduction_v2_2018Sep26_VBFHHTo2B2Tau_CV_1_C2V_2_C3_1_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_162807"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/VBFHHTo2B2Tau_CV_1_5_C2V_1_C3_1_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1p5_1_1_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1p5_1_1_hh_2b2t"),
  ("nof_files",                       11),
  ("nof_db_files",                    16),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 392000),
  ("nof_db_events",                   392000),
  ("fsize_local",                     791201242), # 791.20MB, avg file size 71.93MB
  ("fsize_db",                        22237635973), # 22.24GB, avg file size 1.39GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Oct28/VBFHHTo2B2Tau_CV_1_5_C2V_1_C3_1_13TeV-madgraph/NanoProduction_v2_2018Oct28_VBFHHTo2B2Tau_CV_1_5_C2V_1_C3_1_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/181027_230119"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2Tau_node_SM_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_node_sm_hh_bbtt_noncorr"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_sm_hh_2b2t_noncorr"),
  ("nof_files",                       6),
  ("nof_db_files",                    7),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     615617263), # 615.62MB, avg file size 102.60MB
  ("fsize_db",                        16744243710), # 16.74GB, avg file size 2.39GB
  ("use_it",                          False),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/GluGluToHHTo2B2Tau_node_SM_13TeV-madgraph/NanoProduction_v2_2018Sep26_GluGluToHHTo2B2Tau_node_SM_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_133333"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2Tau_node_2_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_node_2_hh_bbtt_noncorr"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_2_hh_2b2t_noncorr"),
  ("nof_files",                       15),
  ("nof_db_files",                    19),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 295000),
  ("nof_db_events",                   295000),
  ("fsize_local",                     692083633), # 692.08MB, avg file size 46.14MB
  ("fsize_db",                        17143512092), # 17.14GB, avg file size 902.29MB
  ("use_it",                          False),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Oct28/GluGluToHHTo2B2Tau_node_2_13TeV-madgraph/NanoProduction_v2_2018Oct28_GluGluToHHTo2B2Tau_node_2_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/181027_230321"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2Tau_node_3_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_node_3_hh_bbtt_noncorr"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_3_hh_2b2t_noncorr"),
  ("nof_files",                       6),
  ("nof_db_files",                    10),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 294000),
  ("nof_db_events",                   294000),
  ("fsize_local",                     606863786), # 606.86MB, avg file size 101.14MB
  ("fsize_db",                        16412066873), # 16.41GB, avg file size 1.64GB
  ("use_it",                          False),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/GluGluToHHTo2B2Tau_node_3_13TeV-madgraph/NanoProduction_v2_2018Sep26_GluGluToHHTo2B2Tau_node_3_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_133725"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2Tau_node_4_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_node_4_hh_bbtt_noncorr"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_4_hh_2b2t_noncorr"),
  ("nof_files",                       6),
  ("nof_db_files",                    14),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 293000),
  ("nof_db_events",                   293000),
  ("fsize_local",                     585768091), # 585.77MB, avg file size 97.63MB
  ("fsize_db",                        15927663185), # 15.93GB, avg file size 1.14GB
  ("use_it",                          False),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/GluGluToHHTo2B2Tau_node_4_13TeV-madgraph/NanoProduction_v2_2018Sep26_GluGluToHHTo2B2Tau_node_4_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_134051"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2Tau_node_5_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_node_5_hh_bbtt_noncorr"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_5_hh_2b2t_noncorr"),
  ("nof_files",                       7),
  ("nof_db_files",                    16),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     627204890), # 627.20MB, avg file size 89.60MB
  ("fsize_db",                        16886128095), # 16.89GB, avg file size 1.06GB
  ("use_it",                          False),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/GluGluToHHTo2B2Tau_node_5_13TeV-madgraph/NanoProduction_v2_2018Sep26_GluGluToHHTo2B2Tau_node_5_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_134453"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2Tau_node_6_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_node_6_hh_bbtt_noncorr"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_6_hh_2b2t_noncorr"),
  ("nof_files",                       6),
  ("nof_db_files",                    8),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 277000),
  ("nof_db_events",                   277000),
  ("fsize_local",                     556201012), # 556.20MB, avg file size 92.70MB
  ("fsize_db",                        15020276347), # 15.02GB, avg file size 1.88GB
  ("use_it",                          False),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/GluGluToHHTo2B2Tau_node_6_13TeV-madgraph/NanoProduction_v2_2018Sep26_GluGluToHHTo2B2Tau_node_6_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_134919"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2Tau_node_7_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_node_7_hh_bbtt_noncorr"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_7_hh_2b2t_noncorr"),
  ("nof_files",                       6),
  ("nof_db_files",                    8),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     599791565), # 599.79MB, avg file size 99.97MB
  ("fsize_db",                        16320639861), # 16.32GB, avg file size 2.04GB
  ("use_it",                          False),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/GluGluToHHTo2B2Tau_node_7_13TeV-madgraph/NanoProduction_v2_2018Sep26_GluGluToHHTo2B2Tau_node_7_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_135244"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2Tau_node_8_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_node_8_hh_bbtt_noncorr"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_8_hh_2b2t_noncorr"),
  ("nof_files",                       6),
  ("nof_db_files",                    13),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 277000),
  ("nof_db_events",                   277000),
  ("fsize_local",                     553576515), # 553.58MB, avg file size 92.26MB
  ("fsize_db",                        14970008942), # 14.97GB, avg file size 1.15GB
  ("use_it",                          False),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/GluGluToHHTo2B2Tau_node_8_13TeV-madgraph/NanoProduction_v2_2018Sep26_GluGluToHHTo2B2Tau_node_8_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_135611"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2Tau_node_9_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_node_9_hh_bbtt_noncorr"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_9_hh_2b2t_noncorr"),
  ("nof_files",                       6),
  ("nof_db_files",                    18),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 282000),
  ("nof_db_events",                   282000),
  ("fsize_local",                     644537523), # 644.54MB, avg file size 107.42MB
  ("fsize_db",                        16547476913), # 16.55GB, avg file size 919.30MB
  ("use_it",                          False),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Oct26/GluGluToHHTo2B2Tau_node_9_13TeV-madgraph/NanoProduction_v2_2018Oct26_GluGluToHHTo2B2Tau_node_9_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/181026_115455"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2Tau_node_10_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_node_10_hh_bbtt_noncorr"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_10_hh_2b2t_noncorr"),
  ("nof_files",                       6),
  ("nof_db_files",                    9),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     600045464), # 600.05MB, avg file size 100.01MB
  ("fsize_db",                        16293634924), # 16.29GB, avg file size 1.81GB
  ("use_it",                          False),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/GluGluToHHTo2B2Tau_node_10_13TeV-madgraph/NanoProduction_v2_2018Sep26_GluGluToHHTo2B2Tau_node_10_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_135920"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2Tau_node_11_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_node_11_hh_bbtt_noncorr"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_11_hh_2b2t_noncorr"),
  ("nof_files",                       6),
  ("nof_db_files",                    12),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     602918650), # 602.92MB, avg file size 100.49MB
  ("fsize_db",                        16430762018), # 16.43GB, avg file size 1.37GB
  ("use_it",                          False),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/GluGluToHHTo2B2Tau_node_11_13TeV-madgraph/NanoProduction_v2_2018Sep26_GluGluToHHTo2B2Tau_node_11_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_140250"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2Tau_node_12_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_node_12_hh_bbtt_noncorr"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_12_hh_2b2t_noncorr"),
  ("nof_files",                       6),
  ("nof_db_files",                    11),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     598024848), # 598.02MB, avg file size 99.67MB
  ("fsize_db",                        16173950628), # 16.17GB, avg file size 1.47GB
  ("use_it",                          False),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/GluGluToHHTo2B2Tau_node_12_13TeV-madgraph/NanoProduction_v2_2018Sep26_GluGluToHHTo2B2Tau_node_12_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_140527"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2Tau_node_SM_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_node_sm_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_sm_hh_2b2t"),
  ("nof_files",                       8),
  ("nof_db_files",                    18),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 380000),
  ("nof_db_events",                   380000),
  ("fsize_local",                     767892405), # 767.89MB, avg file size 95.99MB
  ("fsize_db",                        20440095707), # 20.44GB, avg file size 1.14GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Oct28/GluGluToHHTo2B2Tau_node_SM_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Oct28_GluGluToHHTo2B2Tau_node_SM_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/181027_230553"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2Tau_node_2_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_node_2_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_2_hh_2b2t"),
  ("nof_files",                       8),
  ("nof_db_files",                    14),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 392000),
  ("nof_db_events",                   392000),
  ("fsize_local",                     873935868), # 873.94MB, avg file size 109.24MB
  ("fsize_db",                        22130629455), # 22.13GB, avg file size 1.58GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Oct28/GluGluToHHTo2B2Tau_node_2_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Oct28_GluGluToHHTo2B2Tau_node_2_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/181027_230753"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2Tau_node_3_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_node_3_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_3_hh_2b2t"),
  ("nof_files",                       8),
  ("nof_db_files",                    22),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 396000),
  ("nof_db_events",                   396000),
  ("fsize_local",                     802652614), # 802.65MB, avg file size 100.33MB
  ("fsize_db",                        21371438091), # 21.37GB, avg file size 971.43MB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Oct28/GluGluToHHTo2B2Tau_node_3_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Oct28_GluGluToHHTo2B2Tau_node_3_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/181027_230958"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2Tau_node_4_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_node_4_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_4_hh_2b2t"),
  ("nof_files",                       8),
  ("nof_db_files",                    21),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     786317335), # 786.32MB, avg file size 98.29MB
  ("fsize_db",                        21451946375), # 21.45GB, avg file size 1.02GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Oct28/GluGluToHHTo2B2Tau_node_4_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Oct28_GluGluToHHTo2B2Tau_node_4_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/181027_231206"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2Tau_node_7_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_node_7_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_7_hh_2b2t"),
  ("nof_files",                       8),
  ("nof_db_files",                    16),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 376000),
  ("nof_db_events",                   376000),
  ("fsize_local",                     740478096), # 740.48MB, avg file size 92.56MB
  ("fsize_db",                        20190349511), # 20.19GB, avg file size 1.26GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Oct28/GluGluToHHTo2B2Tau_node_7_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Oct28_GluGluToHHTo2B2Tau_node_7_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/181027_231412"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2Tau_node_9_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_node_9_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_9_hh_2b2t"),
  ("nof_files",                       8),
  ("nof_db_files",                    18),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     895520935), # 895.52MB, avg file size 111.94MB
  ("fsize_db",                        22924430937), # 22.92GB, avg file size 1.27GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Oct28/GluGluToHHTo2B2Tau_node_9_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Oct28_GluGluToHHTo2B2Tau_node_9_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/181027_231612"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2Tau_node_12_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_node_12_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_12_hh_2b2t"),
  ("nof_files",                       8),
  ("nof_db_files",                    10),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     784412953), # 784.41MB, avg file size 98.05MB
  ("fsize_db",                        21176117597), # 21.18GB, avg file size 2.12GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Oct28/GluGluToHHTo2B2Tau_node_12_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Oct28_GluGluToHHTo2B2Tau_node_12_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/181027_231810"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["sum_events"] = [
]

