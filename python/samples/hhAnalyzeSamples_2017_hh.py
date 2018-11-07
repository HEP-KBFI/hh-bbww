from collections import OrderedDict as OD

# file generated at 2018-11-07 11:59:22 with the following command:
# create_dictionary.py -m python/samples/metaDict_2017_hh.py -p /hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples -Z zeroes.txt -z zombies.txt -N samples_2017 -E 2017 -o python/samples -g hhAnalyzeSamples_2017_hh.py -M

samples_2017 = OD()
samples_2017["/VBFToRadionToHHTo2B2VTo2L2Nu_M-300_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_300_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_spin0_300_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                  : [       279999, ],
    'CountFullWeighted'                      : [       279979,       279964,       279946, ],
    'CountWeighted'                          : [       279979,       279964,       279946, ],
    'CountFullWeightedNoPU'                  : [       279963, ],
    'CountWeightedNoPU'                      : [       279963, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 279999),
  ("nof_db_events",                   279999),
  ("fsize_local",                     845868591), # 845.87MB, avg file size 422.93MB
  ("fsize_db",                        18070036516), # 18.07GB, avg file size 1.29GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_300_hh_2b2v"),
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
  ("nof_files",                       2),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                  : [       285000, ],
    'CountFullWeighted'                      : [       284965,       284957,       284987, ],
    'CountWeighted'                          : [       284965,       284957,       284987, ],
    'CountFullWeightedNoPU'                  : [       284962, ],
    'CountWeightedNoPU'                      : [       284962, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 285000),
  ("nof_db_events",                   285000),
  ("fsize_local",                     903176015), # 903.18MB, avg file size 451.59MB
  ("fsize_db",                        18927275912), # 18.93GB, avg file size 996.17MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_350_hh_2b2v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                  : [       100000, ],
    'CountFullWeighted'                      : [        99974,        99971,        99969, ],
    'CountWeighted'                          : [        99974,        99971,        99969, ],
    'CountFullWeightedNoPU'                  : [        99978, ],
    'CountWeightedNoPU'                      : [        99978, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     330032630), # 330.03MB, avg file size 330.03MB
  ("fsize_db",                        6827583120), # 6.83GB, avg file size 682.76MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_400_hh_2b2v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                  : [       100000, ],
    'CountFullWeighted'                      : [        99964,        99966,        99964, ],
    'CountWeighted'                          : [        99964,        99966,        99964, ],
    'CountFullWeightedNoPU'                  : [        99970, ],
    'CountWeightedNoPU'                      : [        99970, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     375587682), # 375.59MB, avg file size 375.59MB
  ("fsize_db",                        7423075893), # 7.42GB, avg file size 571.01MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_750_hh_2b2v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                  : [       399998, ],
    'CountFullWeighted'                      : [       399994,       399955,       399996, ],
    'CountWeighted'                          : [       399994,       399955,       399996, ],
    'CountFullWeightedNoPU'                  : [       399972, ],
    'CountWeightedNoPU'                      : [       399972, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     794787560), # 794.79MB, avg file size 794.79MB
  ("fsize_db",                        20842533885), # 20.84GB, avg file size 1.49GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_250_hh_2b2v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                  : [       388000, ],
    'CountFullWeighted'                      : [       387971,       387988,       388053, ],
    'CountWeighted'                          : [       387971,       387988,       388053, ],
    'CountFullWeightedNoPU'                  : [       387972, ],
    'CountWeightedNoPU'                      : [       387972, ],
    'CountWeightedLHEWeightScale'            : [       395291,       387971,       378436,       395291,       387971,       378436,       395291,       387971,       378436, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       395257,       387972,       378431,       395257,       387972,       378431,       395257,       387972,       378431, ],
    'CountFullWeightedLHEWeightScale'        : [       395291,       387971,       378436,       395291,       387971,       378436,       395291,       387971,       378436, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       395257,       387972,       378431,       395257,       387972,       378431,       395257,       387972,       378431, ],
  }),
  ("nof_tree_events",                 388000),
  ("nof_db_events",                   388000),
  ("fsize_local",                     854033982), # 854.03MB, avg file size 854.03MB
  ("fsize_db",                        19501546911), # 19.50GB, avg file size 1.03GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_270_hh_2b2v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                  : [       384000, ],
    'CountFullWeighted'                      : [       383977,       383948,       383964, ],
    'CountWeighted'                          : [       383977,       383948,       383964, ],
    'CountFullWeightedNoPU'                  : [       383986, ],
    'CountWeightedNoPU'                      : [       383986, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 384000),
  ("nof_db_events",                   384000),
  ("fsize_local",                     885741081), # 885.74MB, avg file size 885.74MB
  ("fsize_db",                        20165336883), # 20.17GB, avg file size 1.44GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_280_hh_2b2v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                  : [       299996, ],
    'CountFullWeighted'                      : [       299966,       300000,       300001, ],
    'CountWeighted'                          : [       299966,       300000,       300001, ],
    'CountFullWeightedNoPU'                  : [       299980, ],
    'CountWeightedNoPU'                      : [       299980, ],
    'CountWeightedLHEWeightScale'            : [       309821,       299966,       289300,       309821,       299966,       289300,       309821,       299966,       289300, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       309827,       299980,       289295,       309827,       299980,       289295,       309827,       299980,       289295, ],
    'CountFullWeightedLHEWeightScale'        : [       309821,       299966,       289300,       309821,       299966,       289300,       309821,       299966,       289300, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       309827,       299980,       289295,       309827,       299980,       289295,       309827,       299980,       289295, ],
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     691241958), # 691.24MB, avg file size 691.24MB
  ("fsize_db",                        15538010606), # 15.54GB, avg file size 776.90MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_320_hh_2b2v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                  : [       300000, ],
    'CountFullWeighted'                      : [       300001,       299976,       299988, ],
    'CountWeighted'                          : [       300001,       299976,       299988, ],
    'CountFullWeightedNoPU'                  : [       299988, ],
    'CountWeightedNoPU'                      : [       299988, ],
    'CountWeightedLHEWeightScale'            : [       312000,       300001,       287638,       312000,       300001,       287638,       312000,       300001,       287638, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       312006,       299988,       287639,       312006,       299988,       287639,       312006,       299988,       287639, ],
    'CountFullWeightedLHEWeightScale'        : [       312000,       300001,       287638,       312000,       300001,       287638,       312000,       300001,       287638, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       312006,       299988,       287639,       312006,       299988,       287639,       312006,       299988,       287639, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     710087168), # 710.09MB, avg file size 710.09MB
  ("fsize_db",                        15654716885), # 15.65GB, avg file size 1.30GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_350_hh_2b2v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                  : [       292000, ],
    'CountFullWeighted'                      : [       291989,       291996,       291978, ],
    'CountWeighted'                          : [       291989,       291996,       291978, ],
    'CountFullWeightedNoPU'                  : [       291982, ],
    'CountWeightedNoPU'                      : [       291982, ],
    'CountWeightedLHEWeightScale'            : [       306715,       291989,       277660,       306715,       291989,       277660,       306715,       291989,       277660, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       306731,       291982,       277639,       306731,       291982,       277639,       306731,       291982,       277639, ],
    'CountFullWeightedLHEWeightScale'        : [       306715,       291989,       277660,       306715,       291989,       277660,       306715,       291989,       277660, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       306731,       291982,       277639,       306731,       291982,       277639,       306731,       291982,       277639, ],
  }),
  ("nof_tree_events",                 292000),
  ("nof_db_events",                   292000),
  ("fsize_local",                     829008576), # 829.01MB, avg file size 829.01MB
  ("fsize_db",                        15536600053), # 15.54GB, avg file size 971.04MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_400_hh_2b2v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                  : [       299999, ],
    'CountFullWeighted'                      : [       299954,       299967,       299956, ],
    'CountWeighted'                          : [       299954,       299967,       299956, ],
    'CountFullWeightedNoPU'                  : [       299975, ],
    'CountWeightedNoPU'                      : [       299975, ],
    'CountWeightedLHEWeightScale'            : [       317771,       299954,       283232,       317771,       299954,       283232,       317771,       299954,       283232, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       317745,       299975,       283249,       317745,       299975,       283249,       317745,       299975,       283249, ],
    'CountFullWeightedLHEWeightScale'        : [       317771,       299954,       283232,       317771,       299954,       283232,       317771,       299954,       283232, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       317745,       299975,       283249,       317745,       299975,       283249,       317745,       299975,       283249, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     779171732), # 779.17MB, avg file size 779.17MB
  ("fsize_db",                        16296871303), # 16.30GB, avg file size 814.84MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_450_hh_2b2v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                  : [       200000, ],
    'CountFullWeighted'                      : [       199971,       199978,       199974, ],
    'CountWeighted'                          : [       199971,       199978,       199974, ],
    'CountFullWeightedNoPU'                  : [       199984, ],
    'CountWeightedNoPU'                      : [       199984, ],
    'CountWeightedLHEWeightScale'            : [       213378,       199971,       187644,       213378,       199971,       187644,       213378,       199971,       187644, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       213348,       199984,       187675,       213348,       199984,       187675,       213348,       199984,       187675, ],
    'CountFullWeightedLHEWeightScale'        : [       213378,       199971,       187644,       213378,       199971,       187644,       213378,       199971,       187644, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       213348,       199984,       187675,       213348,       199984,       187675,       213348,       199984,       187675, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     612600986), # 612.60MB, avg file size 612.60MB
  ("fsize_db",                        10964750047), # 10.96GB, avg file size 913.73MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_500_hh_2b2v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                  : [       199998, ],
    'CountFullWeighted'                      : [       199985,       199983,       199962, ],
    'CountWeighted'                          : [       199985,       199983,       199962, ],
    'CountFullWeightedNoPU'                  : [       199980, ],
    'CountWeightedNoPU'                      : [       199980, ],
    'CountWeightedLHEWeightScale'            : [       215953,       199985,       185669,       215953,       199985,       185669,       215953,       199985,       185669, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       216004,       199980,       185639,       216004,       199980,       185639,       216004,       199980,       185639, ],
    'CountFullWeightedLHEWeightScale'        : [       215953,       199985,       185669,       215953,       199985,       185669,       215953,       199985,       185669, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       216004,       199980,       185639,       216004,       199980,       185639,       216004,       199980,       185639, ],
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     571505235), # 571.51MB, avg file size 571.51MB
  ("fsize_db",                        11169462986), # 11.17GB, avg file size 1.24GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_600_hh_2b2v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                  : [       200000, ],
    'CountFullWeighted'                      : [       199972,       199956,       199973, ],
    'CountWeighted'                          : [       199972,       199956,       199973, ],
    'CountFullWeightedNoPU'                  : [       199970, ],
    'CountWeightedNoPU'                      : [       199970, ],
    'CountWeightedLHEWeightScale'            : [       217060,       199972,       184822,       217060,       199972,       184822,       217060,       199972,       184822, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       217019,       199970,       184768,       217019,       199970,       184768,       217019,       199970,       184768, ],
    'CountFullWeightedLHEWeightScale'        : [       217060,       199972,       184822,       217060,       199972,       184822,       217060,       199972,       184822, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       217019,       199970,       184768,       217019,       199970,       184768,       217019,       199970,       184768, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     583072032), # 583.07MB, avg file size 583.07MB
  ("fsize_db",                        11395262580), # 11.40GB, avg file size 949.61MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_650_hh_2b2v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                  : [       199998, ],
    'CountFullWeighted'                      : [       199965,       199972,       199973, ],
    'CountWeighted'                          : [       199965,       199972,       199973, ],
    'CountFullWeightedNoPU'                  : [       199976, ],
    'CountWeightedNoPU'                      : [       199976, ],
    'CountWeightedLHEWeightScale'            : [       218042,       199965,       184050,       218042,       199965,       184050,       218042,       199965,       184050, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       218018,       199976,       184051,       218018,       199976,       184051,       218018,       199976,       184051, ],
    'CountFullWeightedLHEWeightScale'        : [       218042,       199965,       184050,       218042,       199965,       184050,       218042,       199965,       184050, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       218018,       199976,       184051,       218018,       199976,       184051,       218018,       199976,       184051, ],
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     592867356), # 592.87MB, avg file size 592.87MB
  ("fsize_db",                        11438629863), # 11.44GB, avg file size 1.43GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_700_hh_2b2v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                  : [       200000, ],
    'CountFullWeighted'                      : [       199955,       199993,       199963, ],
    'CountWeighted'                          : [       199955,       199993,       199963, ],
    'CountFullWeightedNoPU'                  : [       199976, ],
    'CountWeightedNoPU'                      : [       199976, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     565992590), # 565.99MB, avg file size 565.99MB
  ("fsize_db",                        11931037531), # 11.93GB, avg file size 1.08GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_750_hh_2b2v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                  : [       197000, ],
    'CountFullWeighted'                      : [       196973,       196965,       196978, ],
    'CountWeighted'                          : [       196973,       196965,       196978, ],
    'CountFullWeightedNoPU'                  : [       196976, ],
    'CountWeightedNoPU'                      : [       196976, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 197000),
  ("nof_db_events",                   197000),
  ("fsize_local",                     564431204), # 564.43MB, avg file size 564.43MB
  ("fsize_db",                        11877663068), # 11.88GB, avg file size 791.84MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_800_hh_2b2v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                  : [       199999, ],
    'CountFullWeighted'                      : [       199987,       199975,       199985, ],
    'CountWeighted'                          : [       199987,       199975,       199985, ],
    'CountFullWeightedNoPU'                  : [       199973, ],
    'CountWeightedNoPU'                      : [       199973, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     578337415), # 578.34MB, avg file size 578.34MB
  ("fsize_db",                        12127308050), # 12.13GB, avg file size 808.49MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_850_hh_2b2v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                  : [       100000, ],
    'CountFullWeighted'                      : [        99978,        99991,        99983, ],
    'CountWeighted'                          : [        99978,        99991,        99983, ],
    'CountFullWeightedNoPU'                  : [        99980, ],
    'CountWeightedNoPU'                      : [        99980, ],
    'CountWeightedLHEWeightScale'            : [       110660,        99978,        90815,       110660,        99978,        90815,       110660,        99978,        90815, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       110644,        99980,        90803,       110644,        99980,        90803,       110644,        99980,        90803, ],
    'CountFullWeightedLHEWeightScale'        : [       110660,        99978,        90815,       110660,        99978,        90815,       110660,        99978,        90815, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       110644,        99980,        90803,       110644,        99980,        90803,       110644,        99980,        90803, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     309165103), # 309.17MB, avg file size 309.17MB
  ("fsize_db",                        5935911198), # 5.94GB, avg file size 539.63MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_900_hh_2b2v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                  : [       100000, ],
    'CountFullWeighted'                      : [        99974,        99984,        99975, ],
    'CountWeighted'                          : [        99974,        99984,        99975, ],
    'CountFullWeightedNoPU'                  : [        99974, ],
    'CountWeightedNoPU'                      : [        99974, ],
    'CountWeightedLHEWeightScale'            : [       111335,        99972,        90332,       111335,        99972,        90332,       111335,        99972,        90332, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       111324,        99974,        90324,       111324,        99974,        90324,       111324,        99974,        90324, ],
    'CountFullWeightedLHEWeightScale'        : [       111335,        99972,        90332,       111335,        99972,        90332,       111335,        99972,        90332, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       111324,        99974,        90324,       111324,        99974,        90324,       111324,        99974,        90324, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     347799072), # 347.80MB, avg file size 347.80MB
  ("fsize_db",                        5930718483), # 5.93GB, avg file size 847.25MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1000_hh_2b2v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                  : [       100000, ],
    'CountFullWeighted'                      : [        99972,        99976,        99979, ],
    'CountWeighted'                          : [        99972,        99976,        99979, ],
    'CountFullWeightedNoPU'                  : [        99974, ],
    'CountWeightedNoPU'                      : [        99974, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     302634412), # 302.63MB, avg file size 302.63MB
  ("fsize_db",                        6224151597), # 6.22GB, avg file size 778.02MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1250_hh_2b2v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                  : [        99998, ],
    'CountFullWeighted'                      : [        99946,        99954,        99947, ],
    'CountWeighted'                          : [        99946,        99954,        99947, ],
    'CountFullWeightedNoPU'                  : [        99954, ],
    'CountWeightedNoPU'                      : [        99954, ],
    'CountWeightedLHEWeightScale'            : [       113888,        99945,        88512,       113888,        99945,        88512,       113888,        99945,        88512, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       113883,        99954,        88523,       113883,        99954,        88523,       113883,        99954,        88523, ],
    'CountFullWeightedLHEWeightScale'        : [       113888,        99945,        88512,       113888,        99945,        88512,       113888,        99945,        88512, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       113883,        99954,        88523,       113883,        99954,        88523,       113883,        99954,        88523, ],
  }),
  ("nof_tree_events",                 99998),
  ("nof_db_events",                   99998),
  ("fsize_local",                     321318944), # 321.32MB, avg file size 321.32MB
  ("fsize_db",                        6171310375), # 6.17GB, avg file size 514.28MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1500_hh_2b2v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                  : [       100000, ],
    'CountFullWeighted'                      : [        99968,        99952,        99950, ],
    'CountWeighted'                          : [        99968,        99952,        99950, ],
    'CountFullWeightedNoPU'                  : [        99958, ],
    'CountWeightedNoPU'                      : [        99958, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     305552471), # 305.55MB, avg file size 305.55MB
  ("fsize_db",                        6356319473), # 6.36GB, avg file size 635.63MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1750_hh_2b2v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                  : [       100000, ],
    'CountFullWeighted'                      : [        99924,        99923,        99923, ],
    'CountWeighted'                          : [        99924,        99923,        99923, ],
    'CountFullWeightedNoPU'                  : [        99932, ],
    'CountWeightedNoPU'                      : [        99932, ],
    'CountWeightedLHEWeightScale'            : [       115683,        99922,        87203,       115683,        99922,        87203,       115683,        99922,        87203, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       115709,        99932,        87211,       115709,        99932,        87211,       115709,        99932,        87211, ],
    'CountFullWeightedLHEWeightScale'        : [       115683,        99922,        87203,       115683,        99922,        87203,       115683,        99922,        87203, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       115709,        99932,        87211,       115709,        99932,        87211,       115709,        99932,        87211, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     325861060), # 325.86MB, avg file size 325.86MB
  ("fsize_db",                        6172348486), # 6.17GB, avg file size 771.54MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_2000_hh_2b2v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                  : [        97000, ],
    'CountFullWeighted'                      : [        96875,        96876,        96869, ],
    'CountWeighted'                          : [        96875,        96876,        96869, ],
    'CountFullWeightedNoPU'                  : [        96882, ],
    'CountWeightedNoPU'                      : [        96882, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 97000),
  ("nof_db_events",                   97000),
  ("fsize_local",                     300110110), # 300.11MB, avg file size 300.11MB
  ("fsize_db",                        6425534542), # 6.43GB, avg file size 494.27MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_2500_hh_2b2v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                  : [        97999, ],
    'CountFullWeighted'                      : [        97747,        97741,        97747, ],
    'CountWeighted'                          : [        97747,        97741,        97747, ],
    'CountFullWeightedNoPU'                  : [        97747, ],
    'CountWeightedNoPU'                      : [        97747, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 97999),
  ("nof_db_events",                   97999),
  ("fsize_local",                     304688614), # 304.69MB, avg file size 304.69MB
  ("fsize_db",                        6497731845), # 6.50GB, avg file size 590.70MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_3000_hh_2b2v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                  : [       399996, ],
    'CountFullWeighted'                      : [       396328,       396290,       396289, ],
    'CountWeighted'                          : [       396328,       396290,       396289, ],
    'CountFullWeightedNoPU'                  : [       396286, ],
    'CountWeightedNoPU'                      : [       396286, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 399996),
  ("nof_db_events",                   399996),
  ("fsize_local",                     942609717), # 942.61MB, avg file size 942.61MB
  ("fsize_db",                        22186460848), # 22.19GB, avg file size 1.85GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_1_hh_2b2v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                  : [       388999, ],
    'CountFullWeighted'                      : [       388904,       388969,       388938, ],
    'CountWeighted'                          : [       388904,       388969,       388938, ],
    'CountFullWeightedNoPU'                  : [       388947, ],
    'CountWeightedNoPU'                      : [       388947, ],
    'CountWeightedLHEWeightScale'            : [       497857,       469950,       443755,       412134,       388903,       367196,       347078,       327485,       309123, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       497861,       469950,       443754,       412140,       388947,       367195,       347081,       327488,       309123, ],
    'CountFullWeightedLHEWeightScale'        : [       497857,       469950,       443755,       412134,       388903,       367196,       347078,       327485,       309123, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       497861,       469950,       443754,       412140,       388947,       367195,       347081,       327488,       309123, ],
  }),
  ("nof_tree_events",                 388999),
  ("nof_db_events",                   388999),
  ("fsize_local",                     1036975675), # 1.04GB, avg file size 1.04GB
  ("fsize_db",                        21257341288), # 21.26GB, avg file size 1.25GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_sm_hh_2b2v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                  : [       400000, ],
    'CountFullWeighted'                      : [       399901,       399925,       399896, ],
    'CountWeighted'                          : [       399901,       399925,       399896, ],
    'CountFullWeightedNoPU'                  : [       399896, ],
    'CountWeightedNoPU'                      : [       399896, ],
    'CountWeightedLHEWeightScale'            : [       519619,       478796,       442926,       434234,       399896,       369769,       368608,       339312,       313622, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       519603,       478793,       442933,       434215,       399896,       369771,       368592,       339306,       313622, ],
    'CountFullWeightedLHEWeightScale'        : [       519619,       478796,       442926,       434234,       399896,       369769,       368608,       339312,       313622, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       519603,       478793,       442933,       434215,       399896,       369771,       368592,       339306,       313622, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1163792688), # 1.16GB, avg file size 1.16GB
  ("fsize_db",                        23088598268), # 23.09GB, avg file size 1.36GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_2_hh_2b2v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                  : [       380000, ],
    'CountFullWeighted'                      : [       379957,       379971,       379981, ],
    'CountWeighted'                          : [       379957,       379971,       379981, ],
    'CountFullWeightedNoPU'                  : [       379964, ],
    'CountWeightedNoPU'                      : [       379964, ],
    'CountWeightedLHEWeightScale'            : [       486421,       459035,       433321,       402703,       379955,       358625,       339150,       319952,       301946, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       486416,       459039,       433331,       402697,       379964,       358630,       339142,       319950,       301948, ],
    'CountFullWeightedLHEWeightScale'        : [       486421,       459035,       433321,       402703,       379955,       358625,       339150,       319952,       301946, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       486416,       459039,       433331,       402697,       379964,       358630,       339142,       319950,       301948, ],
  }),
  ("nof_tree_events",                 380000),
  ("nof_db_events",                   380000),
  ("fsize_local",                     1147378820), # 1.15GB, avg file size 1.15GB
  ("fsize_db",                        20768532098), # 20.77GB, avg file size 1.22GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_3_hh_2b2v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                  : [       392999, ],
    'CountFullWeighted'                      : [       392987,       392922,       392965, ],
    'CountWeighted'                          : [       392987,       392922,       392965, ],
    'CountFullWeightedNoPU'                  : [       392969, ],
    'CountWeightedNoPU'                      : [       392969, ],
    'CountWeightedLHEWeightScale'            : [       501196,       475867,       451527,       413940,       392987,       372836,       347915,       330257,       313310, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       501195,       475857,       451517,       413941,       392969,       372830,       347918,       330259,       313307, ],
    'CountFullWeightedLHEWeightScale'        : [       501196,       475867,       451527,       413940,       392987,       372836,       347915,       330257,       313310, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       501195,       475857,       451517,       413941,       392969,       372830,       347918,       330259,       313307, ],
  }),
  ("nof_tree_events",                 392999),
  ("nof_db_events",                   392999),
  ("fsize_local",                     1165381468), # 1.17GB, avg file size 1.17GB
  ("fsize_db",                        21440735341), # 21.44GB, avg file size 1.13GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_7_hh_2b2v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                  : [       386999, ],
    'CountFullWeighted'                      : [       386956,       386943,       386977, ],
    'CountWeighted'                          : [       386956,       386943,       386977, ],
    'CountFullWeightedNoPU'                  : [       386951, ],
    'CountWeightedNoPU'                      : [       386951, ],
    'CountWeightedLHEWeightScale'            : [       502560,       463300,       428630,       419860,       386956,       357906,       356284,       328285,       303580, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       502549,       463303,       428640,       419846,       386951,       357915,       356269,       328279,       303583, ],
    'CountFullWeightedLHEWeightScale'        : [       502560,       463300,       428630,       419860,       386956,       357906,       356284,       328285,       303580, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       502549,       463303,       428640,       419846,       386951,       357915,       356269,       328279,       303583, ],
  }),
  ("nof_tree_events",                 386999),
  ("nof_db_events",                   386999),
  ("fsize_local",                     1135512073), # 1.14GB, avg file size 1.14GB
  ("fsize_db",                        22534822736), # 22.53GB, avg file size 1.19GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_9_hh_2b2v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                  : [       400000, ],
    'CountFullWeighted'                      : [       399954,       400001,       399951, ],
    'CountWeighted'                          : [       399954,       400001,       399951, ],
    'CountFullWeightedNoPU'                  : [       399970, ],
    'CountWeightedNoPU'                      : [       399970, ],
    'CountWeightedLHEWeightScale'            : [       509934,       484440,       459891,       421067,       399954,       379659,       353843,       336080,       318989, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       509935,       484442,       459895,       421068,       399970,       379663,       353843,       336081,       318990, ],
    'CountFullWeightedLHEWeightScale'        : [       509934,       484440,       459891,       421067,       399954,       379659,       353843,       336080,       318989, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       509935,       484442,       459895,       421068,       399970,       379663,       353843,       336081,       318990, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1039160320), # 1.04GB, avg file size 1.04GB
  ("fsize_db",                        21561540290), # 21.56GB, avg file size 937.46MB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_12_hh_2b2v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                  : [       400000, ],
    'CountFullWeighted'                      : [       399942,       399970,       399958, ],
    'CountWeighted'                          : [       399942,       399970,       399958, ],
    'CountFullWeightedNoPU'                  : [       399966, ],
    'CountWeightedNoPU'                      : [       399966, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1132682564), # 1.13GB, avg file size 1.13GB
  ("fsize_db",                        24640211831), # 24.64GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_250_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                  : [       388000, ],
    'CountFullWeighted'                      : [       387937,       387955,       387914, ],
    'CountWeighted'                          : [       387937,       387955,       387914, ],
    'CountFullWeightedNoPU'                  : [       387954, ],
    'CountWeightedNoPU'                      : [       387954, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 388000),
  ("nof_db_events",                   388000),
  ("fsize_local",                     1111462945), # 1.11GB, avg file size 1.11GB
  ("fsize_db",                        24012313674), # 24.01GB, avg file size 1.33GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_260_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                  : [       384000, ],
    'CountFullWeighted'                      : [       383971,       383961,       383921, ],
    'CountWeighted'                          : [       383971,       383961,       383921, ],
    'CountFullWeightedNoPU'                  : [       383960, ],
    'CountWeightedNoPU'                      : [       383960, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 384000),
  ("nof_db_events",                   384000),
  ("fsize_local",                     1240952543), # 1.24GB, avg file size 1.24GB
  ("fsize_db",                        23968184441), # 23.97GB, avg file size 1.41GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_270_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                  : [       400000, ],
    'CountFullWeighted'                      : [       399943,       399959,       399966, ],
    'CountWeighted'                          : [       399943,       399959,       399966, ],
    'CountFullWeightedNoPU'                  : [       399954, ],
    'CountWeightedNoPU'                      : [       399954, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1308951446), # 1.31GB, avg file size 1.31GB
  ("fsize_db",                        25138262751), # 25.14GB, avg file size 1.09GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_280_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                  : [       300000, ],
    'CountFullWeighted'                      : [       299983,       299986,       299943, ],
    'CountWeighted'                          : [       299983,       299986,       299943, ],
    'CountFullWeightedNoPU'                  : [       299962, ],
    'CountWeightedNoPU'                      : [       299962, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     900174799), # 900.17MB, avg file size 900.17MB
  ("fsize_db",                        19012035463), # 19.01GB, avg file size 1.27GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_300_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                  : [       300000, ],
    'CountFullWeighted'                      : [       299967,       299971,       299946, ],
    'CountWeighted'                          : [       299967,       299971,       299946, ],
    'CountFullWeightedNoPU'                  : [       299960, ],
    'CountWeightedNoPU'                      : [       299960, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     947286120), # 947.29MB, avg file size 947.29MB
  ("fsize_db",                        19447040410), # 19.45GB, avg file size 1.77GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_350_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                  : [       100000, ],
    'CountFullWeighted'                      : [        99978,        99966,        99973, ],
    'CountWeighted'                          : [        99978,        99966,        99973, ],
    'CountFullWeightedNoPU'                  : [        99976, ],
    'CountWeightedNoPU'                      : [        99976, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     330323821), # 330.32MB, avg file size 330.32MB
  ("fsize_db",                        6609409571), # 6.61GB, avg file size 944.20MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_400_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                  : [       300000, ],
    'CountFullWeighted'                      : [       299959,       299962,       299954, ],
    'CountWeighted'                          : [       299959,       299962,       299954, ],
    'CountFullWeightedNoPU'                  : [       299950, ],
    'CountWeightedNoPU'                      : [       299950, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1023453986), # 1.02GB, avg file size 1.02GB
  ("fsize_db",                        20167217854), # 20.17GB, avg file size 1.26GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_450_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                  : [       290000, ],
    'CountFullWeighted'                      : [       289934,       289931,       289943, ],
    'CountWeighted'                          : [       289934,       289931,       289943, ],
    'CountFullWeightedNoPU'                  : [       289940, ],
    'CountWeightedNoPU'                      : [       289940, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 290000),
  ("nof_db_events",                   290000),
  ("fsize_local",                     1017376355), # 1.02GB, avg file size 1.02GB
  ("fsize_db",                        19708690689), # 19.71GB, avg file size 1.79GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_500_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                  : [       300000, ],
    'CountFullWeighted'                      : [       299931,       299894,       299913, ],
    'CountWeighted'                          : [       299931,       299894,       299913, ],
    'CountFullWeightedNoPU'                  : [       299916, ],
    'CountWeightedNoPU'                      : [       299916, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1077726595), # 1.08GB, avg file size 1.08GB
  ("fsize_db",                        20644816504), # 20.64GB, avg file size 1.59GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_550_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                  : [       200000, ],
    'CountFullWeighted'                      : [       199908,       199918,       199906, ],
    'CountWeighted'                          : [       199908,       199918,       199906, ],
    'CountFullWeightedNoPU'                  : [       199924, ],
    'CountWeightedNoPU'                      : [       199924, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     796899252), # 796.90MB, avg file size 796.90MB
  ("fsize_db",                        13957904944), # 13.96GB, avg file size 1.16GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_600_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                  : [       200000, ],
    'CountFullWeighted'                      : [       199961,       199953,       199941, ],
    'CountWeighted'                          : [       199961,       199953,       199941, ],
    'CountFullWeightedNoPU'                  : [       199948, ],
    'CountWeightedNoPU'                      : [       199948, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     806078483), # 806.08MB, avg file size 806.08MB
  ("fsize_db",                        14016331858), # 14.02GB, avg file size 2.00GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_650_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                  : [       200000, ],
    'CountFullWeighted'                      : [       199912,       199938,       199937, ],
    'CountWeighted'                          : [       199912,       199938,       199937, ],
    'CountFullWeightedNoPU'                  : [       199934, ],
    'CountWeightedNoPU'                      : [       199934, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     825348589), # 825.35MB, avg file size 825.35MB
  ("fsize_db",                        14253263609), # 14.25GB, avg file size 1.10GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_700_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                  : [       100000, ],
    'CountFullWeighted'                      : [        99941,        99942,        99942, ],
    'CountWeighted'                          : [        99941,        99942,        99942, ],
    'CountFullWeightedNoPU'                  : [        99946, ],
    'CountWeightedNoPU'                      : [        99946, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     382668177), # 382.67MB, avg file size 382.67MB
  ("fsize_db",                        7146269195), # 7.15GB, avg file size 1.02GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_750_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                  : [       200000, ],
    'CountFullWeighted'                      : [       199915,       199919,       199916, ],
    'CountWeighted'                          : [       199915,       199919,       199916, ],
    'CountFullWeightedNoPU'                  : [       199912, ],
    'CountWeightedNoPU'                      : [       199912, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     771964179), # 771.96MB, avg file size 771.96MB
  ("fsize_db",                        14420020815), # 14.42GB, avg file size 1.31GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_800_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                  : [       200000, ],
    'CountFullWeighted'                      : [       199873,       199867,       199874, ],
    'CountWeighted'                          : [       199873,       199867,       199874, ],
    'CountFullWeightedNoPU'                  : [       199864, ],
    'CountWeightedNoPU'                      : [       199864, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     777750532), # 777.75MB, avg file size 777.75MB
  ("fsize_db",                        14617490096), # 14.62GB, avg file size 1.04GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_850_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                  : [       100000, ],
    'CountFullWeighted'                      : [        99936,        99933,        99922, ],
    'CountWeighted'                          : [        99936,        99933,        99922, ],
    'CountFullWeightedNoPU'                  : [        99938, ],
    'CountWeightedNoPU'                      : [        99938, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     392587958), # 392.59MB, avg file size 392.59MB
  ("fsize_db",                        7382733082), # 7.38GB, avg file size 671.16MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_900_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                  : [       100000, ],
    'CountFullWeighted'                      : [        99923,        99927,        99916, ],
    'CountWeighted'                          : [        99923,        99927,        99916, ],
    'CountFullWeightedNoPU'                  : [        99926, ],
    'CountWeightedNoPU'                      : [        99926, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     434155587), # 434.16MB, avg file size 434.16MB
  ("fsize_db",                        7364574553), # 7.36GB, avg file size 1.05GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_1000_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                  : [        50000, ],
    'CountFullWeighted'                      : [        49939,        49937,        49937, ],
    'CountWeighted'                          : [        49939,        49937,        49937, ],
    'CountFullWeightedNoPU'                  : [        49940, ],
    'CountWeightedNoPU'                      : [        49940, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     220503563), # 220.50MB, avg file size 220.50MB
  ("fsize_db",                        7497237044), # 7.50GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_1250_hh_2b2t"),
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

samples_2017["/VBFToRadionToHHTo2B2Tau_M-1500_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_1500_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_1500_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                  : [       100000, ],
    'CountFullWeighted'                      : [        99830,        99841,        99825, ],
    'CountWeighted'                          : [        99830,        99841,        99825, ],
    'CountFullWeightedNoPU'                  : [        99836, ],
    'CountWeightedNoPU'                      : [        99836, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     405857304), # 405.86MB, avg file size 405.86MB
  ("fsize_db",                        7582428905), # 7.58GB, avg file size 1.52GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_1500_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                  : [       100000, ],
    'CountFullWeighted'                      : [        99730,        99732,        99723, ],
    'CountWeighted'                          : [        99730,        99732,        99723, ],
    'CountFullWeightedNoPU'                  : [        99732, ],
    'CountWeightedNoPU'                      : [        99732, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     406608595), # 406.61MB, avg file size 406.61MB
  ("fsize_db",                        7802866732), # 7.80GB, avg file size 650.24MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_1750_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                  : [       100000, ],
    'CountFullWeighted'                      : [        99672,        99674,        99658, ],
    'CountWeighted'                          : [        99672,        99674,        99658, ],
    'CountFullWeightedNoPU'                  : [        99678, ],
    'CountWeightedNoPU'                      : [        99678, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     406410301), # 406.41MB, avg file size 406.41MB
  ("fsize_db",                        7810715378), # 7.81GB, avg file size 710.07MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_2000_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                  : [       270000, ],
    'CountFullWeighted'                      : [       269983,       269992,       269976, ],
    'CountWeighted'                          : [       269983,       269992,       269976, ],
    'CountFullWeightedNoPU'                  : [       269976, ],
    'CountWeightedNoPU'                      : [       269976, ],
    'CountWeightedLHEWeightScale'            : [       274201,       269983,       264030,       274201,       269983,       264030,       274201,       269983,       264030, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       274183,       269976,       264046,       274183,       269976,       264046,       274183,       269976,       264046, ],
    'CountFullWeightedLHEWeightScale'        : [       274201,       269983,       264030,       274201,       269983,       264030,       274201,       269983,       264030, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       274183,       269976,       264046,       274183,       269976,       264046,       274183,       269976,       264046, ],
  }),
  ("nof_tree_events",                 270000),
  ("nof_db_events",                   270000),
  ("fsize_local",                     543728368), # 543.73MB, avg file size 543.73MB
  ("fsize_db",                        13445383362), # 13.45GB, avg file size 896.36MB
  ("use_it",                          False),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_260_hh_2b2t_noncorr"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                  : [       300000, ],
    'CountFullWeighted'                      : [       299963,       299984,       299999, ],
    'CountWeighted'                          : [       299963,       299984,       299999, ],
    'CountFullWeightedNoPU'                  : [       299980, ],
    'CountWeightedNoPU'                      : [       299980, ],
    'CountWeightedLHEWeightScale'            : [       305634,       299963,       292607,       305634,       299963,       292607,       305634,       299963,       292607, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       305612,       299980,       292604,       305612,       299980,       292604,       305612,       299980,       292604, ],
    'CountFullWeightedLHEWeightScale'        : [       305634,       299963,       292607,       305634,       299963,       292607,       305634,       299963,       292607, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       305612,       299980,       292604,       305612,       299980,       292604,       305612,       299980,       292604, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     609816370), # 609.82MB, avg file size 609.82MB
  ("fsize_db",                        15004164477), # 15.00GB, avg file size 1.00GB
  ("use_it",                          False),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_270_hh_2b2t_noncorr"),
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
  ("nof_files",                       2),
  ("nof_db_files",                    30),
  ("nof_events",                      {
    'Count'                                  : [       500000, ],
    'CountFullWeighted'                      : [       500007,       499919,       499969, ],
    'CountWeighted'                          : [       500007,       499919,       499969, ],
    'CountFullWeightedNoPU'                  : [       499966, ],
    'CountWeightedNoPU'                      : [       499966, ],
    'CountWeightedLHEWeightScale'            : [       513735,       500002,       484215,       513735,       500002,       484215,       513735,       500002,       484215, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       513734,       499966,       484184,       513734,       499966,       484184,       513734,       499966,       484184, ],
    'CountFullWeightedLHEWeightScale'        : [       513735,       500002,       484215,       513735,       500002,       484215,       513735,       500002,       484215, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       513734,       499966,       484184,       513734,       499966,       484184,       513734,       499966,       484184, ],
  }),
  ("nof_tree_events",                 500000),
  ("nof_db_events",                   500000),
  ("fsize_local",                     1050276614), # 1.05GB, avg file size 525.14MB
  ("fsize_db",                        25493703953), # 25.49GB, avg file size 849.79MB
  ("use_it",                          False),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_300_hh_2b2t_noncorr"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                  : [       300000, ],
    'CountFullWeighted'                      : [       299981,       299979,       299979, ],
    'CountWeighted'                          : [       299981,       299979,       299979, ],
    'CountFullWeightedNoPU'                  : [       299978, ],
    'CountWeightedNoPU'                      : [       299978, ],
    'CountWeightedLHEWeightScale'            : [       311977,       299981,       287627,       311977,       299981,       287627,       311977,       299981,       287627, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       311995,       299978,       287630,       311995,       299978,       287630,       311995,       299978,       287630, ],
    'CountFullWeightedLHEWeightScale'        : [       311977,       299981,       287627,       311977,       299981,       287627,       311977,       299981,       287627, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       311995,       299978,       287630,       311995,       299978,       287630,       311995,       299978,       287630, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     666877300), # 666.88MB, avg file size 666.88MB
  ("fsize_db",                        15628942112), # 15.63GB, avg file size 1.56GB
  ("use_it",                          False),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_350_hh_2b2t_noncorr"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                  : [       278000, ],
    'CountFullWeighted'                      : [       277972,       277982,       277977, ],
    'CountWeighted'                          : [       277972,       277982,       277977, ],
    'CountFullWeightedNoPU'                  : [       277978, ],
    'CountWeightedNoPU'                      : [       277978, ],
    'CountWeightedLHEWeightScale'            : [       292013,       277972,       264343,       292013,       277972,       264343,       292013,       277972,       264343, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       292025,       277978,       264320,       292025,       277978,       264320,       292025,       277978,       264320, ],
    'CountFullWeightedLHEWeightScale'        : [       292013,       277972,       264343,       292013,       277972,       264343,       292013,       277972,       264343, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       292025,       277978,       264320,       292025,       277978,       264320,       292025,       277978,       264320, ],
  }),
  ("nof_tree_events",                 278000),
  ("nof_db_events",                   278000),
  ("fsize_local",                     746250407), # 746.25MB, avg file size 746.25MB
  ("fsize_db",                        14938047142), # 14.94GB, avg file size 829.89MB
  ("use_it",                          False),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_400_hh_2b2t_noncorr"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                  : [       100000, ],
    'CountFullWeighted'                      : [        99996,        99995,       100008, ],
    'CountWeighted'                          : [        99996,        99995,       100008, ],
    'CountFullWeightedNoPU'                  : [        99996, ],
    'CountWeightedNoPU'                      : [        99996, ],
    'CountWeightedLHEWeightScale'            : [       105934,        99996,        94415,       105934,        99996,        94415,       105934,        99996,        94415, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       105924,        99996,        94417,       105924,        99996,        94417,       105924,        99996,        94417, ],
    'CountFullWeightedLHEWeightScale'        : [       105934,        99996,        94415,       105934,        99996,        94415,       105934,        99996,        94415, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       105924,        99996,        94417,       105924,        99996,        94417,       105924,        99996,        94417, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     285542209), # 285.54MB, avg file size 285.54MB
  ("fsize_db",                        5476096947), # 5.48GB, avg file size 608.46MB
  ("use_it",                          False),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_450_hh_2b2t_noncorr"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                  : [       100000, ],
    'CountFullWeighted'                      : [        99982,        99985,        99982, ],
    'CountWeighted'                          : [        99982,        99985,        99982, ],
    'CountFullWeightedNoPU'                  : [        99990, ],
    'CountWeightedNoPU'                      : [        99990, ],
    'CountWeightedLHEWeightScale'            : [       106680,        99982,        93816,       106680,        99982,        93816,       106680,        99982,        93816, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       106669,        99990,        93839,       106669,        99990,        93839,       106669,        99990,        93839, ],
    'CountFullWeightedLHEWeightScale'        : [       106680,        99982,        93816,       106680,        99982,        93816,       106680,        99982,        93816, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       106669,        99990,        93839,       106669,        99990,        93839,       106669,        99990,        93839, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     264742297), # 264.74MB, avg file size 264.74MB
  ("fsize_db",                        5508412042), # 5.51GB, avg file size 1.84GB
  ("use_it",                          False),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_500_hh_2b2t_noncorr"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                  : [       100000, ],
    'CountFullWeighted'                      : [        99991,        99995,        99993, ],
    'CountWeighted'                          : [        99991,        99995,        99993, ],
    'CountFullWeightedNoPU'                  : [        99994, ],
    'CountWeightedNoPU'                      : [        99994, ],
    'CountWeightedLHEWeightScale'            : [       107366,        99991,        93302,       107366,        99991,        93302,       107366,        99991,        93302, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       107360,        99994,        93312,       107360,        99994,        93312,       107360,        99994,        93312, ],
    'CountFullWeightedLHEWeightScale'        : [       107366,        99991,        93302,       107366,        99991,        93302,       107366,        99991,        93302, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       107360,        99994,        93312,       107360,        99994,        93312,       107360,        99994,        93312, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     274878696), # 274.88MB, avg file size 274.88MB
  ("fsize_db",                        5599595099), # 5.60GB, avg file size 933.27MB
  ("use_it",                          False),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_550_hh_2b2t_noncorr"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                  : [       100000, ],
    'CountFullWeighted'                      : [        99997,        99985,        99990, ],
    'CountWeighted'                          : [        99997,        99985,        99990, ],
    'CountFullWeightedNoPU'                  : [        99996, ],
    'CountWeightedNoPU'                      : [        99996, ],
    'CountWeightedLHEWeightScale'            : [       107976,        99996,        92832,       107976,        99996,        92832,       107976,        99996,        92832, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       108006,        99996,        92826,       108006,        99996,        92826,       108006,        99996,        92826, ],
    'CountFullWeightedLHEWeightScale'        : [       107976,        99996,        92832,       107976,        99996,        92832,       107976,        99996,        92832, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       108006,        99996,        92826,       108006,        99996,        92826,       108006,        99996,        92826, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     314424137), # 314.42MB, avg file size 314.42MB
  ("fsize_db",                        5851929979), # 5.85GB, avg file size 390.13MB
  ("use_it",                          False),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_600_hh_2b2t_noncorr"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                  : [       100000, ],
    'CountFullWeighted'                      : [        99976,        99971,        99971, ],
    'CountWeighted'                          : [        99976,        99971,        99971, ],
    'CountFullWeightedNoPU'                  : [        99984, ],
    'CountWeightedNoPU'                      : [        99984, ],
    'CountWeightedLHEWeightScale'            : [       108515,        99976,        92403,       108515,        99976,        92403,       108515,        99976,        92403, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       108506,        99984,        92385,       108506,        99984,        92385,       108506,        99984,        92385, ],
    'CountFullWeightedLHEWeightScale'        : [       108515,        99976,        92403,       108515,        99976,        92403,       108515,        99976,        92403, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       108506,        99984,        92385,       108506,        99984,        92385,       108506,        99984,        92385, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     289137801), # 289.14MB, avg file size 289.14MB
  ("fsize_db",                        5741157480), # 5.74GB, avg file size 1.15GB
  ("use_it",                          False),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_650_hh_2b2t_noncorr"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                  : [       100000, ],
    'CountFullWeighted'                      : [        99985,        99984,        99992, ],
    'CountWeighted'                          : [        99985,        99984,        99992, ],
    'CountFullWeightedNoPU'                  : [        99986, ],
    'CountWeightedNoPU'                      : [        99986, ],
    'CountWeightedLHEWeightScale'            : [       110666,        99985,        90825,       110666,        99985,        90825,       110666,        99985,        90825, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       110652,        99986,        90818,       110652,        99986,        90818,       110652,        99986,        90818, ],
    'CountFullWeightedLHEWeightScale'        : [       110666,        99985,        90825,       110666,        99985,        90825,       110666,        99985,        90825, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       110652,        99986,        90818,       110652,        99986,        90818,       110652,        99986,        90818, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     305485125), # 305.49MB, avg file size 305.49MB
  ("fsize_db",                        5935488747), # 5.94GB, avg file size 989.25MB
  ("use_it",                          False),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_900_hh_2b2t_noncorr"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                  : [       390000, ],
    'CountFullWeighted'                      : [       389993,       389964,       389965, ],
    'CountWeighted'                          : [       389993,       389964,       389965, ],
    'CountFullWeightedNoPU'                  : [       389982, ],
    'CountWeightedNoPU'                      : [       389982, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 390000),
  ("nof_db_events",                   390000),
  ("fsize_local",                     775042873), # 775.04MB, avg file size 775.04MB
  ("fsize_db",                        20093492648), # 20.09GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_250_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                  : [       360000, ],
    'CountFullWeighted'                      : [       360008,       359949,       360005, ],
    'CountWeighted'                          : [       360008,       359949,       360005, ],
    'CountFullWeightedNoPU'                  : [       359972, ],
    'CountWeightedNoPU'                      : [       359972, ],
    'CountWeightedLHEWeightScale'            : [       365606,       360003,       352045,       365606,       360003,       352045,       365606,       360003,       352045, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       365576,       359972,       352072,       365576,       359972,       352072,       365576,       359972,       352072, ],
    'CountFullWeightedLHEWeightScale'        : [       365606,       360003,       352045,       365606,       360003,       352045,       365606,       360003,       352045, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       365576,       359972,       352072,       365576,       359972,       352072,       365576,       359972,       352072, ],
  }),
  ("nof_tree_events",                 360000),
  ("nof_db_events",                   360000),
  ("fsize_local",                     785747974), # 785.75MB, avg file size 785.75MB
  ("fsize_db",                        17758553715), # 17.76GB, avg file size 986.59MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_260_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                  : [       392000, ],
    'CountFullWeighted'                      : [       391981,       391995,       391958, ],
    'CountWeighted'                          : [       391981,       391995,       391958, ],
    'CountFullWeightedNoPU'                  : [       391982, ],
    'CountWeightedNoPU'                      : [       391982, ],
    'CountWeightedLHEWeightScale'            : [       399356,       391971,       382358,       399356,       391971,       382358,       399356,       391971,       382358, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       399329,       391982,       382354,       399329,       391982,       382354,       399329,       391982,       382354, ],
    'CountFullWeightedLHEWeightScale'        : [       399356,       391971,       382358,       399356,       391971,       382358,       399356,       391971,       382358, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       399329,       391982,       382354,       399329,       391982,       382354,       399329,       391982,       382354, ],
  }),
  ("nof_tree_events",                 392000),
  ("nof_db_events",                   392000),
  ("fsize_local",                     862169172), # 862.17MB, avg file size 862.17MB
  ("fsize_db",                        19361033085), # 19.36GB, avg file size 1.21GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_270_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                  : [       398000, ],
    'CountFullWeighted'                      : [       397999,       397948,       397964, ],
    'CountWeighted'                          : [       397999,       397948,       397964, ],
    'CountFullWeightedNoPU'                  : [       397994, ],
    'CountWeightedNoPU'                      : [       397994, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 398000),
  ("nof_db_events",                   398000),
  ("fsize_local",                     900892840), # 900.89MB, avg file size 900.89MB
  ("fsize_db",                        20704800616), # 20.70GB, avg file size 900.21MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_280_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                  : [       300000, ],
    'CountFullWeighted'                      : [       299979,       299983,       299981, ],
    'CountWeighted'                          : [       299979,       299983,       299981, ],
    'CountFullWeightedNoPU'                  : [       299976, ],
    'CountWeightedNoPU'                      : [       299976, ],
    'CountWeightedLHEWeightScale'            : [       308250,       299979,       290521,       308250,       299979,       290521,       308250,       299979,       290521, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       308245,       299976,       290500,       308245,       299976,       290500,       308245,       299976,       290500, ],
    'CountFullWeightedLHEWeightScale'        : [       308250,       299979,       290521,       308250,       299979,       290521,       308250,       299979,       290521, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       308245,       299976,       290500,       308245,       299976,       290500,       308245,       299976,       290500, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     677039986), # 677.04MB, avg file size 677.04MB
  ("fsize_db",                        15151937781), # 15.15GB, avg file size 688.72MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_300_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                  : [       300000, ],
    'CountFullWeighted'                      : [       299988,       299984,       300010, ],
    'CountWeighted'                          : [       299988,       299984,       300010, ],
    'CountFullWeightedNoPU'                  : [       299988, ],
    'CountWeightedNoPU'                      : [       299988, ],
    'CountWeightedLHEWeightScale'            : [       309834,       299988,       289297,       309834,       299988,       289297,       309834,       299988,       289297, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       309840,       299988,       289299,       309840,       299988,       289299,       309840,       299988,       289299, ],
    'CountFullWeightedLHEWeightScale'        : [       309834,       299988,       289297,       309834,       299988,       289297,       309834,       299988,       289297, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       309840,       299988,       289299,       309840,       299988,       289299,       309840,       299988,       289299, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     690919278), # 690.92MB, avg file size 690.92MB
  ("fsize_db",                        15215406969), # 15.22GB, avg file size 1.17GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_320_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                  : [       300000, ],
    'CountFullWeighted'                      : [       299969,       299976,       300024, ],
    'CountWeighted'                          : [       299969,       299976,       300024, ],
    'CountFullWeightedNoPU'                  : [       299978, ],
    'CountWeightedNoPU'                      : [       299978, ],
    'CountWeightedLHEWeightScale'            : [       311994,       299965,       287628,       311994,       299965,       287628,       311994,       299965,       287628, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       312001,       299978,       287626,       312001,       299978,       287626,       312001,       299978,       287626, ],
    'CountFullWeightedLHEWeightScale'        : [       311994,       299965,       287628,       311994,       299965,       287628,       311994,       299965,       287628, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       312001,       299978,       287626,       312001,       299978,       287626,       312001,       299978,       287626, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     709951340), # 709.95MB, avg file size 709.95MB
  ("fsize_db",                        15430234358), # 15.43GB, avg file size 1.10GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_350_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                  : [       296000, ],
    'CountFullWeighted'                      : [       295988,       295999,       295982, ],
    'CountWeighted'                          : [       295988,       295999,       295982, ],
    'CountFullWeightedNoPU'                  : [       295978, ],
    'CountWeightedNoPU'                      : [       295978, ],
    'CountWeightedLHEWeightScale'            : [       310924,       295988,       281455,       310924,       295988,       281455,       310924,       295988,       281455, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       310933,       295978,       281433,       310933,       295978,       281433,       310933,       295978,       281433, ],
    'CountFullWeightedLHEWeightScale'        : [       310924,       295988,       281455,       310924,       295988,       281455,       310924,       295988,       281455, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       310933,       295978,       281433,       310933,       295978,       281433,       310933,       295978,       281433, ],
  }),
  ("nof_tree_events",                 296000),
  ("nof_db_events",                   296000),
  ("fsize_local",                     736554649), # 736.55MB, avg file size 736.55MB
  ("fsize_db",                        15540706594), # 15.54GB, avg file size 971.29MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_400_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                  : [       272000, ],
    'CountFullWeighted'                      : [       271972,       271973,       271985, ],
    'CountWeighted'                          : [       271972,       271973,       271985, ],
    'CountFullWeightedNoPU'                  : [       271980, ],
    'CountWeightedNoPU'                      : [       271980, ],
    'CountWeightedLHEWeightScale'            : [       288106,       271972,       256806,       288106,       271972,       256806,       288106,       271972,       256806, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       288088,       271980,       256818,       288088,       271980,       256818,       288088,       271980,       256818, ],
    'CountFullWeightedLHEWeightScale'        : [       288106,       271972,       256806,       288106,       271972,       256806,       288106,       271972,       256806, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       288088,       271980,       256818,       288088,       271980,       256818,       288088,       271980,       256818, ],
  }),
  ("nof_tree_events",                 272000),
  ("nof_db_events",                   272000),
  ("fsize_local",                     709911081), # 709.91MB, avg file size 709.91MB
  ("fsize_db",                        14544281532), # 14.54GB, avg file size 808.02MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_450_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                  : [       190000, ],
    'CountFullWeighted'                      : [       189982,       189985,       189978, ],
    'CountWeighted'                          : [       189982,       189985,       189978, ],
    'CountFullWeightedNoPU'                  : [       189992, ],
    'CountWeightedNoPU'                      : [       189992, ],
    'CountWeightedLHEWeightScale'            : [       202730,       189982,       178264,       202730,       189982,       178264,       202730,       189982,       178264, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       202691,       189992,       178297,       202691,       189992,       178297,       202691,       189992,       178297, ],
    'CountFullWeightedLHEWeightScale'        : [       202730,       189982,       178264,       202730,       189982,       178264,       202730,       189982,       178264, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       202691,       189992,       178297,       202691,       189992,       178297,       202691,       189992,       178297, ],
  }),
  ("nof_tree_events",                 190000),
  ("nof_db_events",                   190000),
  ("fsize_local",                     519314570), # 519.31MB, avg file size 519.31MB
  ("fsize_db",                        10300681960), # 10.30GB, avg file size 858.39MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_500_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                  : [       200000, ],
    'CountFullWeighted'                      : [       200009,       199974,       199972, ],
    'CountWeighted'                          : [       200009,       199974,       199972, ],
    'CountFullWeightedNoPU'                  : [       199990, ],
    'CountWeightedNoPU'                      : [       199990, ],
    'CountWeightedLHEWeightScale'            : [       214727,       200009,       186593,       214727,       200009,       186593,       214727,       200009,       186593, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       214725,       199990,       186623,       214725,       199990,       186623,       214725,       199990,       186623, ],
    'CountFullWeightedLHEWeightScale'        : [       214727,       200009,       186593,       214727,       200009,       186593,       214727,       200009,       186593, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       214725,       199990,       186623,       214725,       199990,       186623,       214725,       199990,       186623, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     565072523), # 565.07MB, avg file size 565.07MB
  ("fsize_db",                        10884541416), # 10.88GB, avg file size 989.50MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_550_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                  : [       200000, ],
    'CountFullWeighted'                      : [       199977,       199980,       199985, ],
    'CountWeighted'                          : [       199977,       199980,       199985, ],
    'CountFullWeightedNoPU'                  : [       199980, ],
    'CountWeightedNoPU'                      : [       199980, ],
    'CountWeightedLHEWeightScale'            : [       215967,       199976,       185658,       215967,       199976,       185658,       215967,       199976,       185658, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       216010,       199980,       185634,       216010,       199980,       185634,       216010,       199980,       185634, ],
    'CountFullWeightedLHEWeightScale'        : [       215967,       199976,       185658,       215967,       199976,       185658,       215967,       199976,       185658, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       216010,       199980,       185634,       216010,       199980,       185634,       216010,       199980,       185634, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     654477683), # 654.48MB, avg file size 654.48MB
  ("fsize_db",                        11044936345), # 11.04GB, avg file size 920.41MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_600_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                  : [       188000, ],
    'CountFullWeighted'                      : [       187974,       187955,       187962, ],
    'CountWeighted'                          : [       187974,       187955,       187962, ],
    'CountFullWeightedNoPU'                  : [       187966, ],
    'CountWeightedNoPU'                      : [       187966, ],
    'CountWeightedLHEWeightScale'            : [       204011,       187974,       173732,       204011,       187974,       173732,       204011,       187974,       173732, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       203990,       187966,       173681,       203990,       187966,       173681,       203990,       187966,       173681, ],
    'CountFullWeightedLHEWeightScale'        : [       204011,       187974,       173732,       204011,       187974,       173732,       204011,       187974,       173732, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       203990,       187966,       173681,       203990,       187966,       173681,       203990,       187966,       173681, ],
  }),
  ("nof_tree_events",                 188000),
  ("nof_db_events",                   188000),
  ("fsize_local",                     560187048), # 560.19MB, avg file size 560.19MB
  ("fsize_db",                        10510514184), # 10.51GB, avg file size 700.70MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_650_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                  : [       200000, ],
    'CountFullWeighted'                      : [       199982,       199996,       199971, ],
    'CountWeighted'                          : [       199982,       199996,       199971, ],
    'CountFullWeightedNoPU'                  : [       199982, ],
    'CountWeightedNoPU'                      : [       199982, ],
    'CountWeightedLHEWeightScale'            : [       218065,       199982,       184069,       218065,       199982,       184069,       218065,       199982,       184069, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       218020,       199982,       184060,       218020,       199982,       184060,       218020,       199982,       184060, ],
    'CountFullWeightedLHEWeightScale'        : [       218065,       199982,       184069,       218065,       199982,       184069,       218065,       199982,       184069, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       218020,       199982,       184060,       218020,       199982,       184060,       218020,       199982,       184060, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     606450952), # 606.45MB, avg file size 606.45MB
  ("fsize_db",                        11214998225), # 11.21GB, avg file size 1.40GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_700_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                  : [       196000, ],
    'CountFullWeighted'                      : [       195991,       195984,       195976, ],
    'CountWeighted'                          : [       195991,       195984,       195976, ],
    'CountFullWeightedNoPU'                  : [       195978, ],
    'CountWeightedNoPU'                      : [       195978, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 196000),
  ("nof_db_events",                   196000),
  ("fsize_local",                     571743741), # 571.74MB, avg file size 571.74MB
  ("fsize_db",                        11545737081), # 11.55GB, avg file size 962.14MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_750_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                  : [       192000, ],
    'CountFullWeighted'                      : [       191971,       191954,       191964, ],
    'CountWeighted'                          : [       191971,       191954,       191964, ],
    'CountFullWeightedNoPU'                  : [       191972, ],
    'CountWeightedNoPU'                      : [       191972, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 192000),
  ("nof_db_events",                   192000),
  ("fsize_local",                     575272965), # 575.27MB, avg file size 575.27MB
  ("fsize_db",                        11490975329), # 11.49GB, avg file size 766.07MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_850_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                  : [        95000, ],
    'CountFullWeighted'                      : [        94984,        94980,        94987, ],
    'CountWeighted'                          : [        94984,        94980,        94987, ],
    'CountFullWeightedNoPU'                  : [        94988, ],
    'CountWeightedNoPU'                      : [        94988, ],
    'CountWeightedLHEWeightScale'            : [       105125,        94984,        86286,       105125,        94984,        86286,       105125,        94984,        86286, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       105112,        94988,        86276,       105112,        94988,        86276,       105112,        94988,        86276, ],
    'CountFullWeightedLHEWeightScale'        : [       105125,        94984,        86286,       105125,        94984,        86286,       105125,        94984,        86286, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       105112,        94988,        86276,       105112,        94988,        86276,       105112,        94988,        86276, ],
  }),
  ("nof_tree_events",                 95000),
  ("nof_db_events",                   95000),
  ("fsize_local",                     304622618), # 304.62MB, avg file size 304.62MB
  ("fsize_db",                        5517036529), # 5.52GB, avg file size 788.15MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_900_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                  : [       100000, ],
    'CountFullWeighted'                      : [        99978,        99974,        99973, ],
    'CountWeighted'                          : [        99978,        99974,        99973, ],
    'CountFullWeightedNoPU'                  : [        99980, ],
    'CountWeightedNoPU'                      : [        99980, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     316593459), # 316.59MB, avg file size 316.59MB
  ("fsize_db",                        6210975535), # 6.21GB, avg file size 690.11MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1250_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                  : [       100000, ],
    'CountFullWeighted'                      : [        99967,        99959,        99962, ],
    'CountWeighted'                          : [        99967,        99959,        99962, ],
    'CountFullWeightedNoPU'                  : [        99960, ],
    'CountWeightedNoPU'                      : [        99960, ],
    'CountWeightedLHEWeightScale'            : [       113904,        99967,        88518,       113904,        99967,        88518,       113904,        99967,        88518, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       113892,        99960,        88527,       113892,        99960,        88527,       113892,        99960,        88527, ],
    'CountFullWeightedLHEWeightScale'        : [       113904,        99967,        88518,       113904,        99967,        88518,       113904,        99967,        88518, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       113892,        99960,        88527,       113892,        99960,        88527,       113892,        99960,        88527, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     333166478), # 333.17MB, avg file size 333.17MB
  ("fsize_db",                        5949909431), # 5.95GB, avg file size 1.49GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1500_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                  : [        92000, ],
    'CountFullWeighted'                      : [        91903,        91915,        91922, ],
    'CountWeighted'                          : [        91903,        91915,        91922, ],
    'CountFullWeightedNoPU'                  : [        91916, ],
    'CountWeightedNoPU'                      : [        91916, ],
    'CountWeightedLHEWeightScale'            : [       106421,        91903,        80211,       106421,        91903,        80211,       106421,        91903,        80211, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       106432,        91916,        80212,       106432,        91916,        80212,       106432,        91916,        80212, ],
    'CountFullWeightedLHEWeightScale'        : [       106421,        91903,        80211,       106421,        91903,        80211,       106421,        91903,        80211, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       106432,        91916,        80212,       106432,        91916,        80212,       106432,        91916,        80212, ],
  }),
  ("nof_tree_events",                 92000),
  ("nof_db_events",                   92000),
  ("fsize_local",                     306608947), # 306.61MB, avg file size 306.61MB
  ("fsize_db",                        5565938746), # 5.57GB, avg file size 927.66MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_2000_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                  : [       100000, ],
    'CountFullWeighted'                      : [        99880,        99886,        99879, ],
    'CountWeighted'                          : [        99880,        99886,        99879, ],
    'CountFullWeightedNoPU'                  : [        99886, ],
    'CountWeightedNoPU'                      : [        99886, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     314129203), # 314.13MB, avg file size 314.13MB
  ("fsize_db",                        6456631366), # 6.46GB, avg file size 586.97MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_2500_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                  : [       100000, ],
    'CountFullWeighted'                      : [        99744,        99745,        99748, ],
    'CountWeighted'                          : [        99744,        99745,        99748, ],
    'CountFullWeightedNoPU'                  : [        99752, ],
    'CountWeightedNoPU'                      : [        99752, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     314557700), # 314.56MB, avg file size 314.56MB
  ("fsize_db",                        6431618251), # 6.43GB, avg file size 803.95MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_3000_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    26),
  ("nof_events",                      {
    'Count'                                  : [       369000, ],
    'CountFullWeighted'                      : [       365816,       365852,       365813, ],
    'CountWeighted'                          : [       365816,       365852,       365813, ],
    'CountFullWeightedNoPU'                  : [       365860, ],
    'CountWeightedNoPU'                      : [       365860, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 369000),
  ("nof_db_events",                   369000),
  ("fsize_local",                     980888038), # 980.89MB, avg file size 980.89MB
  ("fsize_db",                        20317409524), # 20.32GB, avg file size 781.44MB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_0_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                  : [       300000, ],
    'CountFullWeighted'                      : [       297176,       297174,       297144, ],
    'CountWeighted'                          : [       297176,       297174,       297144, ],
    'CountFullWeightedNoPU'                  : [       297188, ],
    'CountWeightedNoPU'                      : [       297188, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     710417241), # 710.42MB, avg file size 710.42MB
  ("fsize_db",                        16551491719), # 16.55GB, avg file size 827.57MB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_1_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                  : [       400000, ],
    'CountFullWeighted'                      : [       396298,       396304,       396290, ],
    'CountWeighted'                          : [       396298,       396304,       396290, ],
    'CountFullWeightedNoPU'                  : [       396316, ],
    'CountWeightedNoPU'                      : [       396316, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1014331885), # 1.01GB, avg file size 1.01GB
  ("fsize_db",                        22555887148), # 22.56GB, avg file size 2.51GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_2_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    24),
  ("nof_events",                      {
    'Count'                                  : [       400000, ],
    'CountFullWeighted'                      : [       392981,       392950,       392972, ],
    'CountWeighted'                          : [       392981,       392950,       392972, ],
    'CountFullWeightedNoPU'                  : [       392958, ],
    'CountWeightedNoPU'                      : [       392958, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1196162966), # 1.20GB, avg file size 1.20GB
  ("fsize_db",                        23834632407), # 23.83GB, avg file size 993.11MB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_2_1_hh_2b2t"),
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
  ("nof_files",                       2),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                  : [       392000, ],
    'CountFullWeighted'                      : [       387001,       387015,       386964, ],
    'CountWeighted'                          : [       387001,       387015,       386964, ],
    'CountFullWeightedNoPU'                  : [       387028, ],
    'CountWeightedNoPU'                      : [       387028, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 392000),
  ("nof_db_events",                   392000),
  ("fsize_local",                     1039297458), # 1.04GB, avg file size 519.65MB
  ("fsize_db",                        22237635973), # 22.24GB, avg file size 1.39GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1p5_1_1_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                  : [       300000, ],
    'CountFullWeighted'                      : [       299958,       299918,       299951, ],
    'CountWeighted'                          : [       299958,       299918,       299951, ],
    'CountFullWeightedNoPU'                  : [       299956, ],
    'CountWeightedNoPU'                      : [       299956, ],
    'CountWeightedLHEWeightScale'            : [       383981,       362415,       342177,       317876,       299948,       283150,       267704,       252559,       238375, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       383979,       362418,       342188,       317873,       299956,       283158,       267699,       252562,       238381, ],
    'CountFullWeightedLHEWeightScale'        : [       383981,       362415,       342177,       317876,       299948,       283150,       267704,       252559,       238375, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       383979,       362418,       342188,       317873,       299956,       283158,       267699,       252562,       238381, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     874743936), # 874.74MB, avg file size 874.74MB
  ("fsize_db",                        16744243710), # 16.74GB, avg file size 2.39GB
  ("use_it",                          False),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_sm_hh_2b2t_noncorr"),
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
  ("nof_files",                       2),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                  : [       295000, ],
    'CountFullWeighted'                      : [       294932,       294932,       294929, ],
    'CountWeighted'                          : [       294932,       294932,       294929, ],
    'CountFullWeightedNoPU'                  : [       294934, ],
    'CountWeightedNoPU'                      : [       294934, ],
    'CountWeightedLHEWeightScale'            : [       383200,       353125,       326694,       320219,       294932,       272724,       271818,       250235,       231306, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       383218,       353131,       326689,       320237,       294934,       272721,       271835,       250243,       231306, ],
    'CountFullWeightedLHEWeightScale'        : [       383200,       353125,       326694,       320219,       294932,       272724,       271818,       250235,       231306, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       383218,       353131,       326689,       320237,       294934,       272721,       271835,       250243,       231306, ],
  }),
  ("nof_tree_events",                 295000),
  ("nof_db_events",                   295000),
  ("fsize_local",                     939114083), # 939.11MB, avg file size 469.56MB
  ("fsize_db",                        17143512092), # 17.14GB, avg file size 902.29MB
  ("use_it",                          False),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_2_hh_2b2t_noncorr"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                  : [       294000, ],
    'CountFullWeighted'                      : [       293981,       293976,       293965, ],
    'CountWeighted'                          : [       293981,       293976,       293965, ],
    'CountFullWeightedNoPU'                  : [       293976, ],
    'CountWeightedNoPU'                      : [       293976, ],
    'CountWeightedLHEWeightScale'            : [       376345,       355164,       335277,       311563,       293980,       277474,       262388,       247540,       233615, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       376346,       355160,       335268,       311567,       293976,       277468,       262392,       247541,       233611, ],
    'CountFullWeightedLHEWeightScale'        : [       376345,       355164,       335277,       311563,       293980,       277474,       262388,       247540,       233615, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       376346,       355160,       335268,       311567,       293976,       277468,       262392,       247541,       233611, ],
  }),
  ("nof_tree_events",                 294000),
  ("nof_db_events",                   294000),
  ("fsize_local",                     759400363), # 759.40MB, avg file size 759.40MB
  ("fsize_db",                        16412066873), # 16.41GB, avg file size 1.64GB
  ("use_it",                          False),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_3_hh_2b2t_noncorr"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                  : [       293000, ],
    'CountFullWeighted'                      : [       292975,       292942,       292956, ],
    'CountWeighted'                          : [       292975,       292942,       292956, ],
    'CountFullWeightedNoPU'                  : [       292974, ],
    'CountWeightedNoPU'                      : [       292974, ],
    'CountWeightedLHEWeightScale'            : [       373617,       354805,       336718,       308554,       292970,       278003,       259329,       246203,       233601, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       373623,       354802,       336713,       308559,       292974,       278002,       259333,       246206,       233599, ],
    'CountFullWeightedLHEWeightScale'        : [       373617,       354805,       336718,       308554,       292970,       278003,       259329,       246203,       233601, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       373623,       354802,       336713,       308559,       292974,       278002,       259333,       246206,       233599, ],
  }),
  ("nof_tree_events",                 293000),
  ("nof_db_events",                   293000),
  ("fsize_local",                     730424339), # 730.42MB, avg file size 730.42MB
  ("fsize_db",                        15927663185), # 15.93GB, avg file size 1.14GB
  ("use_it",                          False),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_4_hh_2b2t_noncorr"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                  : [       300000, ],
    'CountFullWeighted'                      : [       299952,       299959,       299937, ],
    'CountWeighted'                          : [       299952,       299959,       299937, ],
    'CountFullWeightedNoPU'                  : [       299964, ],
    'CountWeightedNoPU'                      : [       299964, ],
    'CountWeightedLHEWeightScale'            : [       384732,       361982,       340855,       318884,       299950,       282398,       268823,       252820,       237981, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       384722,       361992,       340880,       318872,       299964,       282415,       268807,       252820,       237990, ],
    'CountFullWeightedLHEWeightScale'        : [       384732,       361982,       340855,       318884,       299950,       282398,       268823,       252820,       237981, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       384722,       361992,       340880,       318872,       299964,       282415,       268807,       252820,       237990, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     886988763), # 886.99MB, avg file size 886.99MB
  ("fsize_db",                        16886128095), # 16.89GB, avg file size 1.06GB
  ("use_it",                          False),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_5_hh_2b2t_noncorr"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                  : [       277000, ],
    'CountFullWeighted'                      : [       276950,       276984,       277001, ],
    'CountWeighted'                          : [       276950,       276984,       277001, ],
    'CountFullWeightedNoPU'                  : [       276982, ],
    'CountWeightedNoPU'                      : [       276982, ],
    'CountWeightedLHEWeightScale'            : [       353378,       335351,       318069,       291908,       276948,       262684,       245383,       232817,       220778, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       353369,       335348,       318068,       291901,       276982,       262683,       245377,       232814,       220776, ],
    'CountFullWeightedLHEWeightScale'        : [       353378,       335351,       318069,       291908,       276948,       262684,       245383,       232817,       220778, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       353369,       335348,       318068,       291901,       276982,       262683,       245377,       232814,       220776, ],
  }),
  ("nof_tree_events",                 277000),
  ("nof_db_events",                   277000),
  ("fsize_local",                     693073086), # 693.07MB, avg file size 693.07MB
  ("fsize_db",                        15020276347), # 15.02GB, avg file size 1.88GB
  ("use_it",                          False),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_6_hh_2b2t_noncorr"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                  : [       300000, ],
    'CountFullWeighted'                      : [       299948,       299971,       299974, ],
    'CountWeighted'                          : [       299948,       299971,       299974, ],
    'CountFullWeightedNoPU'                  : [       299980, ],
    'CountWeightedNoPU'                      : [       299980, ],
    'CountWeightedLHEWeightScale'            : [       382582,       363263,       344699,       315965,       299946,       284620,       265563,       252101,       239175, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       382585,       363264,       344699,       315973,       299980,       284620,       265569,       252104,       239175, ],
    'CountFullWeightedLHEWeightScale'        : [       382582,       363263,       344699,       315965,       299946,       284620,       265563,       252101,       239175, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       382585,       363264,       344699,       315973,       299980,       284620,       265569,       252104,       239175, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     851443921), # 851.44MB, avg file size 851.44MB
  ("fsize_db",                        16320639861), # 16.32GB, avg file size 2.04GB
  ("use_it",                          False),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_7_hh_2b2t_noncorr"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                  : [       277000, ],
    'CountFullWeighted'                      : [       276997,       277003,       276980, ],
    'CountWeighted'                          : [       276997,       277003,       276980, ],
    'CountFullWeightedNoPU'                  : [       276984, ],
    'CountWeightedNoPU'                      : [       276984, ],
    'CountWeightedLHEWeightScale'            : [       353155,       335478,       318459,       291614,       276993,       262905,       245061,       232743,       220893, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       353153,       335479,       318463,       291612,       276984,       262909,       245058,       232742,       220896, ],
    'CountFullWeightedLHEWeightScale'        : [       353155,       335478,       318459,       291614,       276993,       262905,       245061,       232743,       220893, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       353153,       335479,       318463,       291612,       276984,       262909,       245058,       232742,       220896, ],
  }),
  ("nof_tree_events",                 277000),
  ("nof_db_events",                   277000),
  ("fsize_local",                     689262265), # 689.26MB, avg file size 689.26MB
  ("fsize_db",                        14970008942), # 14.97GB, avg file size 1.15GB
  ("use_it",                          False),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_8_hh_2b2t_noncorr"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                  : [       282000, ],
    'CountFullWeighted'                      : [       281944,       281934,       281939, ],
    'CountWeighted'                          : [       281944,       281934,       281939, ],
    'CountFullWeightedNoPU'                  : [       281950, ],
    'CountWeightedNoPU'                      : [       281950, ],
    'CountWeightedLHEWeightScale'            : [       366172,       337591,       312351,       305900,       281944,       260801,       259570,       239186,       221204, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       366181,       337596,       312351,       305909,       281950,       260801,       259578,       239191,       221204, ],
    'CountFullWeightedLHEWeightScale'        : [       366172,       337591,       312351,       305900,       281944,       260801,       259570,       239186,       221204, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       366181,       337596,       312351,       305909,       281950,       260801,       259578,       239191,       221204, ],
  }),
  ("nof_tree_events",                 282000),
  ("nof_db_events",                   282000),
  ("fsize_local",                     809394153), # 809.39MB, avg file size 809.39MB
  ("fsize_db",                        16547476913), # 16.55GB, avg file size 919.30MB
  ("use_it",                          False),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_9_hh_2b2t_noncorr"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                  : [       300000, ],
    'CountFullWeighted'                      : [       299983,       299966,       299994, ],
    'CountWeighted'                          : [       299983,       299966,       299994, ],
    'CountFullWeightedNoPU'                  : [       299982, ],
    'CountWeightedNoPU'                      : [       299982, ],
    'CountWeightedLHEWeightScale'            : [       382602,       363263,       344685,       315991,       299980,       284610,       265589,       252109,       239168, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       382601,       363262,       344686,       315990,       299982,       284612,       265586,       252108,       239168, ],
    'CountFullWeightedLHEWeightScale'        : [       382602,       363263,       344685,       315991,       299980,       284610,       265589,       252109,       239168, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       382601,       363262,       344686,       315990,       299982,       284612,       265586,       252108,       239168, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     749101964), # 749.10MB, avg file size 749.10MB
  ("fsize_db",                        16293634924), # 16.29GB, avg file size 1.81GB
  ("use_it",                          False),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_10_hh_2b2t_noncorr"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                  : [       300000, ],
    'CountFullWeighted'                      : [       299980,       299981,       299964, ],
    'CountWeighted'                          : [       299980,       299981,       299964, ],
    'CountFullWeightedNoPU'                  : [       299978, ],
    'CountWeightedNoPU'                      : [       299978, ],
    'CountWeightedLHEWeightScale'            : [       382827,       363106,       344238,       316304,       299978,       284358,       265939,       252184,       239039, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       382836,       363107,       344233,       316313,       299978,       284357,       265946,       252188,       239036, ],
    'CountFullWeightedLHEWeightScale'        : [       382827,       363106,       344238,       316304,       299978,       284358,       265939,       252184,       239039, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       382836,       363107,       344233,       316313,       299978,       284357,       265946,       252188,       239036, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     753345837), # 753.35MB, avg file size 753.35MB
  ("fsize_db",                        16430762018), # 16.43GB, avg file size 1.37GB
  ("use_it",                          False),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_11_hh_2b2t_noncorr"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                  : [       300000, ],
    'CountFullWeighted'                      : [       299999,       299986,       299997, ],
    'CountWeighted'                          : [       299999,       299986,       299997, ],
    'CountFullWeightedNoPU'                  : [       299982, ],
    'CountWeightedNoPU'                      : [       299982, ],
    'CountWeightedLHEWeightScale'            : [       382464,       363340,       344927,       315809,       299999,       284749,       265390,       252062,       239243, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       382459,       363340,       344929,       315805,       299982,       284751,       265385,       252063,       239245, ],
    'CountFullWeightedLHEWeightScale'        : [       382464,       363340,       344927,       315809,       299999,       284749,       265390,       252062,       239243, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       382459,       363340,       344929,       315805,       299982,       284751,       265385,       252063,       239245, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     850486125), # 850.49MB, avg file size 850.49MB
  ("fsize_db",                        16173950628), # 16.17GB, avg file size 1.47GB
  ("use_it",                          False),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_12_hh_2b2t_noncorr"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                  : [       380000, ],
    'CountFullWeighted'                      : [       379946,       379965,       379927, ],
    'CountWeighted'                          : [       379946,       379965,       379927, ],
    'CountFullWeightedNoPU'                  : [       379966, ],
    'CountWeightedNoPU'                      : [       379966, ],
    'CountWeightedLHEWeightScale'            : [       486393,       459088,       433470,       402657,       379945,       358692,       339105,       319933,       301971, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       486392,       459086,       433469,       402657,       379966,       358693,       339102,       319932,       301972, ],
    'CountFullWeightedLHEWeightScale'        : [       486393,       459088,       433470,       402657,       379945,       358692,       339105,       319933,       301971, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       486392,       459086,       433469,       402657,       379966,       358693,       339102,       319932,       301972, ],
  }),
  ("nof_tree_events",                 380000),
  ("nof_db_events",                   380000),
  ("fsize_local",                     1153107778), # 1.15GB, avg file size 1.15GB
  ("fsize_db",                        20440095707), # 20.44GB, avg file size 1.14GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_sm_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                  : [       392000, ],
    'CountFullWeighted'                      : [       391950,       391910,       391945, ],
    'CountWeighted'                          : [       391950,       391910,       391945, ],
    'CountFullWeightedNoPU'                  : [       391922, ],
    'CountWeightedNoPU'                      : [       391922, ],
    'CountWeightedLHEWeightScale'            : [       509244,       469255,       434114,       425552,       391950,       362404,       361235,       332540,       307372, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       509240,       469251,       434111,       425550,       391922,       362402,       361233,       332538,       307370, ],
    'CountFullWeightedLHEWeightScale'        : [       509244,       469255,       434114,       425552,       391950,       362404,       361235,       332540,       307372, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       509240,       469251,       434111,       425550,       391922,       362402,       361233,       332538,       307370, ],
  }),
  ("nof_tree_events",                 392000),
  ("nof_db_events",                   392000),
  ("fsize_local",                     1164835134), # 1.16GB, avg file size 1.16GB
  ("fsize_db",                        22130629455), # 22.13GB, avg file size 1.58GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_2_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                  : [       396000, ],
    'CountFullWeighted'                      : [       395969,       395973,       395942, ],
    'CountWeighted'                          : [       395969,       395973,       395942, ],
    'CountFullWeightedNoPU'                  : [       395972, ],
    'CountWeightedNoPU'                      : [       395972, ],
    'CountWeightedLHEWeightScale'            : [       506928,       478364,       451555,       419687,       395960,       373719,       353457,       333432,       314656, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       506927,       478372,       451563,       419684,       395972,       373724,       353452,       333434,       314660, ],
    'CountFullWeightedLHEWeightScale'        : [       506928,       478364,       451555,       419687,       395960,       373719,       353457,       333432,       314656, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       506927,       478372,       451563,       419684,       395972,       373724,       353452,       333434,       314660, ],
  }),
  ("nof_tree_events",                 396000),
  ("nof_db_events",                   396000),
  ("fsize_local",                     1070788408), # 1.07GB, avg file size 1.07GB
  ("fsize_db",                        21371438091), # 21.37GB, avg file size 971.43MB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_3_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                  : [       400000, ],
    'CountFullWeighted'                      : [       399937,       399963,       399975, ],
    'CountWeighted'                          : [       399937,       399963,       399975, ],
    'CountFullWeightedNoPU'                  : [       399972, ],
    'CountWeightedNoPU'                      : [       399972, ],
    'CountWeightedLHEWeightScale'            : [       510037,       484392,       459726,       421210,       399937,       379557,       354002,       336110,       318929, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       510039,       484395,       459734,       421209,       399972,       379564,       354003,       336116,       318933, ],
    'CountFullWeightedLHEWeightScale'        : [       510037,       484392,       459726,       421210,       399937,       379557,       354002,       336110,       318929, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       510039,       484395,       459734,       421209,       399972,       379564,       354003,       336116,       318933, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1185781678), # 1.19GB, avg file size 1.19GB
  ("fsize_db",                        21451946375), # 21.45GB, avg file size 1.02GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_4_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                  : [       376000, ],
    'CountFullWeighted'                      : [       375960,       375960,       375946, ],
    'CountWeighted'                          : [       375960,       375960,       375946, ],
    'CountFullWeightedNoPU'                  : [       375962, ],
    'CountWeightedNoPU'                      : [       375962, ],
    'CountWeightedLHEWeightScale'            : [       479495,       455275,       432003,       396009,       375960,       356707,       332839,       315958,       299753, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       479493,       455272,       432001,       396009,       375962,       356708,       332840,       315960,       299753, ],
    'CountFullWeightedLHEWeightScale'        : [       479495,       455275,       432003,       396009,       375960,       356707,       332839,       315958,       299753, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       479493,       455272,       432001,       396009,       375962,       356708,       332840,       315960,       299753, ],
  }),
  ("nof_tree_events",                 376000),
  ("nof_db_events",                   376000),
  ("fsize_local",                     984326868), # 984.33MB, avg file size 984.33MB
  ("fsize_db",                        20190349511), # 20.19GB, avg file size 1.26GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_7_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                  : [       400000, ],
    'CountFullWeighted'                      : [       399960,       399943,       399944, ],
    'CountWeighted'                          : [       399960,       399943,       399944, ],
    'CountFullWeightedNoPU'                  : [       399946, ],
    'CountWeightedNoPU'                      : [       399946, ],
    'CountWeightedLHEWeightScale'            : [       519431,       478865,       443040,       433945,       399960,       369935,       368231,       339302,       313776, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       519435,       478862,       443030,       433954,       399946,       369929,       368240,       339303,       313773, ],
    'CountFullWeightedLHEWeightScale'        : [       519431,       478865,       443040,       433945,       399960,       369935,       368231,       339302,       313776, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       519435,       478862,       443030,       433954,       399946,       369929,       368240,       339303,       313773, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1330016811), # 1.33GB, avg file size 1.33GB
  ("fsize_db",                        22924430937), # 22.92GB, avg file size 1.27GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_9_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                  : [       400000, ],
    'CountFullWeighted'                      : [       399933,       399990,       399944, ],
    'CountWeighted'                          : [       399933,       399990,       399944, ],
    'CountFullWeightedNoPU'                  : [       399976, ],
    'CountWeightedNoPU'                      : [       399976, ],
    'CountWeightedLHEWeightScale'            : [       509966,       484451,       459887,       421093,       399932,       379653,       353864,       336085,       318982, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       509967,       484451,       459886,       421092,       399976,       379655,       353864,       336086,       318982, ],
    'CountFullWeightedLHEWeightScale'        : [       509966,       484451,       459887,       421093,       399932,       379653,       353864,       336085,       318982, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       509967,       484451,       459886,       421092,       399976,       379655,       353864,       336086,       318982, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1044749225), # 1.04GB, avg file size 1.04GB
  ("fsize_db",                        21176117597), # 21.18GB, avg file size 2.12GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_12_hh_2b2t"),
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

