from collections import OrderedDict as OD

# file generated at 2018-10-31 22:57:51 with the following command:
# create_dictionary.py -m python/samples/metaDict_2017_hh.py -p /hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples -Z zeroes.txt -z zombies.txt -N samples_2017 -E 2017 -o python/samples -g hhAnalyzeSamples_2017_hh.py -M

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
  ("fsize_local",                     846701817), # 846.70MB, avg file size 423.35MB
  ("fsize_db",                        18070036516), # 18.07GB, avg file size 1.29GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_300_hh_2b2v"),
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
  ("fsize_local",                     904336198), # 904.34MB, avg file size 452.17MB
  ("fsize_db",                        18927275912), # 18.93GB, avg file size 996.17MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_350_hh_2b2v"),
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
  ("fsize_local",                     330539197), # 330.54MB, avg file size 330.54MB
  ("fsize_db",                        6827583120), # 6.83GB, avg file size 682.76MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_400_hh_2b2v"),
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
  ("fsize_local",                     376897400), # 376.90MB, avg file size 376.90MB
  ("fsize_db",                        7423075893), # 7.42GB, avg file size 571.01MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_750_hh_2b2v"),
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
  ("fsize_local",                     943400082), # 943.40MB, avg file size 943.40MB
  ("fsize_db",                        22186460848), # 22.19GB, avg file size 1.85GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_1_hh_2b2v"),
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
  ("fsize_local",                     1038588585), # 1.04GB, avg file size 1.04GB
  ("fsize_db",                        21257341288), # 21.26GB, avg file size 1.25GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_sm_hh_2b2v"),
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
  ("fsize_local",                     1167201412), # 1.17GB, avg file size 1.17GB
  ("fsize_db",                        23088598268), # 23.09GB, avg file size 1.36GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_2_hh_2b2v"),
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
  ("fsize_local",                     1019117774), # 1.02GB, avg file size 1.02GB
  ("fsize_db",                        20768532098), # 20.77GB, avg file size 1.22GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_3_hh_2b2v"),
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
  ("fsize_local",                     1025075067), # 1.03GB, avg file size 1.03GB
  ("fsize_db",                        21440735341), # 21.44GB, avg file size 1.13GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_7_hh_2b2v"),
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
  ("fsize_local",                     1138388848), # 1.14GB, avg file size 1.14GB
  ("fsize_db",                        22534822736), # 22.53GB, avg file size 1.19GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_9_hh_2b2v"),
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
  ("fsize_local",                     1040477245), # 1.04GB, avg file size 1.04GB
  ("fsize_db",                        21561540290), # 21.56GB, avg file size 937.46MB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_12_hh_2b2v"),
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
  ("fsize_local",                     1132714197), # 1.13GB, avg file size 1.13GB
  ("fsize_db",                        24640211831), # 24.64GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_250_hh_2b2t"),
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
  ("fsize_local",                     1111493068), # 1.11GB, avg file size 1.11GB
  ("fsize_db",                        24012313674), # 24.01GB, avg file size 1.33GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_260_hh_2b2t"),
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
  ("fsize_local",                     1114484028), # 1.11GB, avg file size 1.11GB
  ("fsize_db",                        23968184441), # 23.97GB, avg file size 1.41GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_270_hh_2b2t"),
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
  ("fsize_local",                     1174322626), # 1.17GB, avg file size 1.17GB
  ("fsize_db",                        25138262751), # 25.14GB, avg file size 1.09GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_280_hh_2b2t"),
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
  ("fsize_local",                     900196991), # 900.20MB, avg file size 900.20MB
  ("fsize_db",                        19012035463), # 19.01GB, avg file size 1.27GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_300_hh_2b2t"),
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
  ("fsize_local",                     947307037), # 947.31MB, avg file size 947.31MB
  ("fsize_db",                        19447040410), # 19.45GB, avg file size 1.77GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_350_hh_2b2t"),
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
  ("fsize_local",                     330329953), # 330.33MB, avg file size 330.33MB
  ("fsize_db",                        6609409571), # 6.61GB, avg file size 944.20MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_400_hh_2b2t"),
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
  ("fsize_local",                     1023471515), # 1.02GB, avg file size 1.02GB
  ("fsize_db",                        20167217854), # 20.17GB, avg file size 1.26GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_450_hh_2b2t"),
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
  ("fsize_local",                     1017391241), # 1.02GB, avg file size 1.02GB
  ("fsize_db",                        19708690689), # 19.71GB, avg file size 1.79GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_500_hh_2b2t"),
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
  ("fsize_local",                     1077746204), # 1.08GB, avg file size 1.08GB
  ("fsize_db",                        20644816504), # 20.64GB, avg file size 1.59GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_550_hh_2b2t"),
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
  ("fsize_local",                     733202768), # 733.20MB, avg file size 733.20MB
  ("fsize_db",                        13957904944), # 13.96GB, avg file size 1.16GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_600_hh_2b2t"),
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
  ("fsize_local",                     744548143), # 744.55MB, avg file size 744.55MB
  ("fsize_db",                        14016331858), # 14.02GB, avg file size 2.00GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_650_hh_2b2t"),
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
  ("fsize_local",                     755158741), # 755.16MB, avg file size 755.16MB
  ("fsize_db",                        14253263609), # 14.25GB, avg file size 1.10GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_700_hh_2b2t"),
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
  ("fsize_local",                     382675957), # 382.68MB, avg file size 382.68MB
  ("fsize_db",                        7146269195), # 7.15GB, avg file size 1.02GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_750_hh_2b2t"),
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
  ("fsize_local",                     771981312), # 771.98MB, avg file size 771.98MB
  ("fsize_db",                        14420020815), # 14.42GB, avg file size 1.31GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_800_hh_2b2t"),
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
  ("fsize_local",                     777766865), # 777.77MB, avg file size 777.77MB
  ("fsize_db",                        14617490096), # 14.62GB, avg file size 1.04GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_850_hh_2b2t"),
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
  ("fsize_local",                     392596036), # 392.60MB, avg file size 392.60MB
  ("fsize_db",                        7382733082), # 7.38GB, avg file size 671.16MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_900_hh_2b2t"),
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
  ("fsize_local",                     397142290), # 397.14MB, avg file size 397.14MB
  ("fsize_db",                        7364574553), # 7.36GB, avg file size 1.05GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_1000_hh_2b2t"),
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
  ("fsize_local",                     202539710), # 202.54MB, avg file size 202.54MB
  ("fsize_db",                        7497237044), # 7.50GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_1250_hh_2b2t"),
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
  ("fsize_local",                     405936742), # 405.94MB, avg file size 405.94MB
  ("fsize_db",                        7582428905), # 7.58GB, avg file size 1.52GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_1500_hh_2b2t"),
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
  ("fsize_local",                     406755061), # 406.76MB, avg file size 406.76MB
  ("fsize_db",                        7802866732), # 7.80GB, avg file size 650.24MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_1750_hh_2b2t"),
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
  ("fsize_local",                     406632343), # 406.63MB, avg file size 406.63MB
  ("fsize_db",                        7810715378), # 7.81GB, avg file size 710.07MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_2000_hh_2b2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                  : [        50000, ],
    'CountFullWeighted'                      : [        49349,        49346,        49349, ],
    'CountWeighted'                          : [        49349,        49346,        49349, ],
    'CountFullWeightedNoPU'                  : [        49368, ],
    'CountWeightedNoPU'                      : [        49368, ],
    'CountWeightedLHEWeightScale'            : [            0, ],
    'CountWeightedLHEWeightScaleNoPU'        : [            0, ],
    'CountFullWeightedLHEWeightScale'        : [            0, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [            0, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     204547393), # 204.55MB, avg file size 204.55MB
  ("fsize_db",                        7943092984), # 7.94GB, avg file size 992.89MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_3000_hh_2b2t"),
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
  ("fsize_local",                     543767894), # 543.77MB, avg file size 543.77MB
  ("fsize_db",                        13445383362), # 13.45GB, avg file size 896.36MB
  ("use_it",                          False),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_260_hh_2b2t_noncorr"),
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
  ("fsize_local",                     1050365125), # 1.05GB, avg file size 525.18MB
  ("fsize_db",                        25493703953), # 25.49GB, avg file size 849.79MB
  ("use_it",                          False),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_300_hh_2b2t_noncorr"),
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
  ("fsize_local",                     666934864), # 666.93MB, avg file size 666.93MB
  ("fsize_db",                        15628942112), # 15.63GB, avg file size 1.56GB
  ("use_it",                          False),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_350_hh_2b2t_noncorr"),
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
  ("fsize_local",                     657316414), # 657.32MB, avg file size 657.32MB
  ("fsize_db",                        14938047142), # 14.94GB, avg file size 829.89MB
  ("use_it",                          False),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_400_hh_2b2t_noncorr"),
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
  ("fsize_local",                     251876140), # 251.88MB, avg file size 251.88MB
  ("fsize_db",                        5476096947), # 5.48GB, avg file size 608.46MB
  ("use_it",                          False),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_450_hh_2b2t_noncorr"),
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
  ("fsize_local",                     264769540), # 264.77MB, avg file size 264.77MB
  ("fsize_db",                        5508412042), # 5.51GB, avg file size 1.84GB
  ("use_it",                          False),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_500_hh_2b2t_noncorr"),
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
  ("fsize_local",                     274915090), # 274.92MB, avg file size 274.92MB
  ("fsize_db",                        5599595099), # 5.60GB, avg file size 933.27MB
  ("use_it",                          False),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_550_hh_2b2t_noncorr"),
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
  ("fsize_local",                     282234741), # 282.23MB, avg file size 282.23MB
  ("fsize_db",                        5851929979), # 5.85GB, avg file size 390.13MB
  ("use_it",                          False),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_600_hh_2b2t_noncorr"),
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
  ("fsize_local",                     289183764), # 289.18MB, avg file size 289.18MB
  ("fsize_db",                        5741157480), # 5.74GB, avg file size 1.15GB
  ("use_it",                          False),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_650_hh_2b2t_noncorr"),
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
  ("fsize_local",                     305561042), # 305.56MB, avg file size 305.56MB
  ("fsize_db",                        5935488747), # 5.94GB, avg file size 989.25MB
  ("use_it",                          False),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_900_hh_2b2t_noncorr"),
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
  ("fsize_local",                     870713323), # 870.71MB, avg file size 870.71MB
  ("fsize_db",                        20317409524), # 20.32GB, avg file size 781.44MB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_0_hh_2b2t"),
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
  ("fsize_local",                     710432579), # 710.43MB, avg file size 710.43MB
  ("fsize_db",                        16551491719), # 16.55GB, avg file size 827.57MB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_1_hh_2b2t"),
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
  ("fsize_local",                     1014351304), # 1.01GB, avg file size 1.01GB
  ("fsize_db",                        22555887148), # 22.56GB, avg file size 2.51GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_2_hh_2b2t"),
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
  ("fsize_local",                     1196281886), # 1.20GB, avg file size 1.20GB
  ("fsize_db",                        23834632407), # 23.83GB, avg file size 993.11MB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_2_1_hh_2b2t"),
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
  ("fsize_local",                     1039350509), # 1.04GB, avg file size 519.68MB
  ("fsize_db",                        22237635973), # 22.24GB, avg file size 1.39GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1p5_1_1_hh_2b2t"),
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
  ("fsize_local",                     770036919), # 770.04MB, avg file size 770.04MB
  ("fsize_db",                        16744243710), # 16.74GB, avg file size 2.39GB
  ("use_it",                          False),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_sm_hh_2b2t_noncorr"),
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
  ("fsize_local",                     834846447), # 834.85MB, avg file size 417.42MB
  ("fsize_db",                        17143512092), # 17.14GB, avg file size 902.29MB
  ("use_it",                          False),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_2_hh_2b2t_noncorr"),
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
  ("fsize_local",                     759491569), # 759.49MB, avg file size 759.49MB
  ("fsize_db",                        16412066873), # 16.41GB, avg file size 1.64GB
  ("use_it",                          False),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_3_hh_2b2t_noncorr"),
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
  ("fsize_local",                     730504432), # 730.50MB, avg file size 730.50MB
  ("fsize_db",                        15927663185), # 15.93GB, avg file size 1.14GB
  ("use_it",                          False),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_4_hh_2b2t_noncorr"),
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
  ("fsize_local",                     781863260), # 781.86MB, avg file size 781.86MB
  ("fsize_db",                        16886128095), # 16.89GB, avg file size 1.06GB
  ("use_it",                          False),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_5_hh_2b2t_noncorr"),
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
  ("fsize_local",                     693148642), # 693.15MB, avg file size 693.15MB
  ("fsize_db",                        15020276347), # 15.02GB, avg file size 1.88GB
  ("use_it",                          False),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_6_hh_2b2t_noncorr"),
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
  ("fsize_local",                     748547127), # 748.55MB, avg file size 748.55MB
  ("fsize_db",                        16320639861), # 16.32GB, avg file size 2.04GB
  ("use_it",                          False),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_7_hh_2b2t_noncorr"),
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
  ("fsize_local",                     689341061), # 689.34MB, avg file size 689.34MB
  ("fsize_db",                        14970008942), # 14.97GB, avg file size 1.15GB
  ("use_it",                          False),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_8_hh_2b2t_noncorr"),
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
  ("fsize_local",                     809553384), # 809.55MB, avg file size 809.55MB
  ("fsize_db",                        16547476913), # 16.55GB, avg file size 919.30MB
  ("use_it",                          False),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_9_hh_2b2t_noncorr"),
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
  ("fsize_local",                     749227921), # 749.23MB, avg file size 749.23MB
  ("fsize_db",                        16293634924), # 16.29GB, avg file size 1.81GB
  ("use_it",                          False),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_10_hh_2b2t_noncorr"),
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
  ("fsize_local",                     753421082), # 753.42MB, avg file size 753.42MB
  ("fsize_db",                        16430762018), # 16.43GB, avg file size 1.37GB
  ("use_it",                          False),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_11_hh_2b2t_noncorr"),
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
  ("fsize_local",                     746440941), # 746.44MB, avg file size 746.44MB
  ("fsize_db",                        16173950628), # 16.17GB, avg file size 1.47GB
  ("use_it",                          False),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_12_hh_2b2t_noncorr"),
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
  ("fsize_local",                     1022257818), # 1.02GB, avg file size 1.02GB
  ("fsize_db",                        20440095707), # 20.44GB, avg file size 1.14GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_sm_hh_2b2t"),
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
  ("fsize_local",                     1164929152), # 1.16GB, avg file size 1.16GB
  ("fsize_db",                        22130629455), # 22.13GB, avg file size 1.58GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_2_hh_2b2t"),
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
  ("fsize_local",                     1070813223), # 1.07GB, avg file size 1.07GB
  ("fsize_db",                        21371438091), # 21.37GB, avg file size 971.43MB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_3_hh_2b2t"),
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
  ("fsize_local",                     1047152916), # 1.05GB, avg file size 1.05GB
  ("fsize_db",                        21451946375), # 21.45GB, avg file size 1.02GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_4_hh_2b2t"),
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
  ("fsize_local",                     984349601), # 984.35MB, avg file size 984.35MB
  ("fsize_db",                        20190349511), # 20.19GB, avg file size 1.26GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_7_hh_2b2t"),
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
    'Count'                                  : [       350000, ],
    'CountFullWeighted'                      : [       349950,       349964,       349936, ],
    'CountWeighted'                          : [       349950,       349964,       349936, ],
    'CountFullWeightedNoPU'                  : [       349946, ],
    'CountWeightedNoPU'                      : [       349946, ],
    'CountWeightedLHEWeightScale'            : [       454493,       418999,       387650,       379695,       349950,       323686,       322197,       296884,       274550, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       454495,       418996,       387643,       379702,       349946,       323682,       322204,       296885,       274547, ],
    'CountFullWeightedLHEWeightScale'        : [       454493,       418999,       387650,       379695,       349950,       323686,       322197,       296884,       274550, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       454495,       418996,       387643,       379702,       349946,       323682,       322204,       296885,       274547, ],
  }),
  ("nof_tree_events",                 350000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1048927947), # 1.05GB, avg file size 1.05GB
  ("fsize_db",                        22924430937), # 22.92GB, avg file size 1.27GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_9_hh_2b2t"),
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
  ("fsize_local",                     1044774786), # 1.04GB, avg file size 1.04GB
  ("fsize_db",                        21176117597), # 21.18GB, avg file size 2.12GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct30_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_12_hh_2b2t"),
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

