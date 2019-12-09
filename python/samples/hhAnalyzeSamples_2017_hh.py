from collections import OrderedDict as OD

# file generated at 2019-12-09 14:05:23 with the following command:
# create_dictionary.py -m python/samples/metaDict_2017_hh.py -p /hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples -N samples_2017 -E 2017 -o python/samples -g hhAnalyzeSamples_2017_hh.py -M

samples_2017 = OD()
samples_2017["/VBFToRadionToHHTo2B2VTo2L2Nu_M-300_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_300_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_spin0_300_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                      : [       279999, ],
    'CountWeighted'                                              : [       279966,       279957,       279952, ],
    'CountWeightedL1PrefireNom'                                  : [       271088,       271075,       271091, ],
    'CountWeightedL1Prefire'                                     : [       271088,       268963,       273162, ],
  }),
  ("nof_tree_events",                 279999),
  ("nof_db_events",                   279999),
  ("fsize_local",                     1263419728), # 1.26GB, avg file size 1.26GB
  ("fsize_db",                        18070036516), # 18.07GB, avg file size 1.29GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_300_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2VTo2L2Nu_M-350_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_350_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_spin0_350_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                      : [       285000, ],
    'CountWeighted'                                              : [       284952,       284993,       285008, ],
    'CountWeightedL1PrefireNom'                                  : [       275532,       275548,       275570, ],
    'CountWeightedL1Prefire'                                     : [       275532,       273285,       277729, ],
  }),
  ("nof_tree_events",                 285000),
  ("nof_db_events",                   285000),
  ("fsize_local",                     1336545415), # 1.34GB, avg file size 1.34GB
  ("fsize_db",                        18927275912), # 18.93GB, avg file size 996.17MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_350_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99987,        99954,        99965, ],
    'CountWeightedL1PrefireNom'                                  : [        96485,        96461,        96473, ],
    'CountWeightedL1Prefire'                                     : [        96485,        95659,        97293, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     483914479), # 483.91MB, avg file size 483.91MB
  ("fsize_db",                        6827583120), # 6.83GB, avg file size 682.76MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_400_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99975,        99989,        99968, ],
    'CountWeightedL1PrefireNom'                                  : [        95941,        95946,        95939, ],
    'CountWeightedL1Prefire'                                     : [        95941,        95012,        96859, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     538612750), # 538.61MB, avg file size 538.61MB
  ("fsize_db",                        7423075893), # 7.42GB, avg file size 571.01MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_750_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       399998, ],
    'CountWeighted'                                              : [       399935,       399980,       399905, ],
    'CountWeightedL1PrefireNom'                                  : [       392877,       392882,       392868, ],
    'CountWeightedL1Prefire'                                     : [       392877,       391022,       394642, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     1219523012), # 1.22GB, avg file size 1.22GB
  ("fsize_db",                        20842533885), # 20.84GB, avg file size 1.49GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_250_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-260_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_260_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_260_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                      : [       400000, ],
    'CountWeighted'                                              : [       400019,       399949,       400035, ],
    'CountWeightedLHEWeightScale'                                : [       406265,       399994,       391182,       406265,       399994,       391182,       406265,       399994,       391182, ],
    'CountWeightedL1PrefireNom'                                  : [       392487,       392430,       392499, ],
    'CountWeightedL1Prefire'                                     : [       392487,       390536,       394350, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       398575,       392468,       383856,       398575,       392468,       383856,       398575,       392468,       383856, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1220805184), # 1.22GB, avg file size 1.22GB
  ("fsize_db",                        20086379241), # 20.09GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_260_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       388000, ],
    'CountWeighted'                                              : [       387938,       387981,       388042, ],
    'CountWeightedLHEWeightScale'                                : [       395280,       387938,       378437,       395280,       387938,       378437,       395280,       387938,       378437, ],
    'CountWeightedL1PrefireNom'                                  : [       380324,       380343,       380400, ],
    'CountWeightedL1Prefire'                                     : [       380324,       378365,       382204, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       387468,       380324,       371034,       387468,       380324,       371034,       387468,       380324,       371034, ],
  }),
  ("nof_tree_events",                 388000),
  ("nof_db_events",                   388000),
  ("fsize_local",                     1197859959), # 1.20GB, avg file size 1.20GB
  ("fsize_db",                        19501546911), # 19.50GB, avg file size 1.03GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_270_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       384000, ],
    'CountWeighted'                                              : [       383961,       383999,       384009, ],
    'CountWeightedL1PrefireNom'                                  : [       376110,       376120,       376153, ],
    'CountWeightedL1Prefire'                                     : [       376110,       374101,       378036, ],
  }),
  ("nof_tree_events",                 384000),
  ("nof_db_events",                   384000),
  ("fsize_local",                     1210332805), # 1.21GB, avg file size 1.21GB
  ("fsize_db",                        20165336883), # 20.17GB, avg file size 1.44GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_280_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       299996, ],
    'CountWeighted'                                              : [       299979,       299953,       300001, ],
    'CountWeightedLHEWeightScale'                                : [       309821,       299979,       289309,       309821,       299979,       289309,       309821,       299979,       289309, ],
    'CountWeightedL1PrefireNom'                                  : [       293003,       292966,       293031, ],
    'CountWeightedL1Prefire'                                     : [       293003,       291267,       294687, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       302568,       293003,       282615,       302568,       293003,       282615,       302568,       293003,       282615, ],
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     974124507), # 974.12MB, avg file size 974.12MB
  ("fsize_db",                        15538010606), # 15.54GB, avg file size 776.90MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_320_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       299964,       299940,       299938, ],
    'CountWeightedLHEWeightScale'                                : [       312013,       299964,       287641,       312013,       299964,       287641,       312013,       299964,       287641, ],
    'CountWeightedL1PrefireNom'                                  : [       292297,       292277,       292284, ],
    'CountWeightedL1Prefire'                                     : [       292297,       290420,       294126, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       303972,       292297,       280326,       303972,       292297,       280326,       303972,       292297,       280326, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     999304391), # 999.30MB, avg file size 999.30MB
  ("fsize_db",                        15654716885), # 15.65GB, avg file size 1.30GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_350_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       292000, ],
    'CountWeighted'                                              : [       292013,       291998,       291916, ],
    'CountWeightedLHEWeightScale'                                : [       306718,       292013,       277666,       306718,       292013,       277666,       306718,       292013,       277666, ],
    'CountWeightedL1PrefireNom'                                  : [       283788,       283772,       283731, ],
    'CountWeightedL1Prefire'                                     : [       283788,       281813,       285718, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       298033,       283788,       269897,       298033,       283788,       269897,       298033,       283788,       269897, ],
  }),
  ("nof_tree_events",                 292000),
  ("nof_db_events",                   292000),
  ("fsize_local",                     1009907558), # 1.01GB, avg file size 1.01GB
  ("fsize_db",                        15536600053), # 15.54GB, avg file size 971.04MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_400_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       299934,       299939,       299943, ],
    'CountWeightedLHEWeightScale'                                : [       317770,       299934,       283225,       317770,       299934,       283225,       317770,       299934,       283225, ],
    'CountWeightedL1PrefireNom'                                  : [       290855,       290842,       290873, ],
    'CountWeightedL1Prefire'                                     : [       290855,       288702,       292966, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       308073,       290855,       274692,       308073,       290855,       274692,       308073,       290855,       274692, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1070492577), # 1.07GB, avg file size 1.07GB
  ("fsize_db",                        16296871303), # 16.30GB, avg file size 814.84MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_450_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       200008,       200006,       199959, ],
    'CountWeightedLHEWeightScale'                                : [       213378,       200008,       187623,       213378,       200008,       187623,       213378,       200008,       187623, ],
    'CountWeightedL1PrefireNom'                                  : [       193663,       193647,       193654, ],
    'CountWeightedL1Prefire'                                     : [       193663,       192177,       195127, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       206580,       193663,       181721,       206580,       193663,       181721,       206580,       193663,       181721, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     732702273), # 732.70MB, avg file size 732.70MB
  ("fsize_db",                        10964750047), # 10.96GB, avg file size 913.73MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_500_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       199998, ],
    'CountWeighted'                                              : [       199989,       199981,       199981, ],
    'CountWeightedLHEWeightScale'                                : [       215943,       199989,       185665,       215943,       199989,       185665,       215943,       199989,       185665, ],
    'CountWeightedL1PrefireNom'                                  : [       192977,       192970,       192964, ],
    'CountWeightedL1Prefire'                                     : [       192977,       191358,       194581, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       208331,       192977,       179194,       208331,       192977,       179194,       208331,       192977,       179194, ],
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     763788509), # 763.79MB, avg file size 763.79MB
  ("fsize_db",                        11169462986), # 11.17GB, avg file size 1.24GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_600_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199940,       199980,       199955, ],
    'CountWeightedLHEWeightScale'                                : [       217043,       199940,       184822,       217043,       199940,       184822,       217043,       199940,       184822, ],
    'CountWeightedL1PrefireNom'                                  : [       192823,       192822,       192862, ],
    'CountWeightedL1Prefire'                                     : [       192823,       191178,       194447, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       209263,       192823,       178267,       209263,       192823,       178267,       209263,       192823,       178267, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     775677631), # 775.68MB, avg file size 775.68MB
  ("fsize_db",                        11395262580), # 11.40GB, avg file size 949.61MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_650_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       199998, ],
    'CountWeighted'                                              : [       199996,       199963,       199971, ],
    'CountWeightedLHEWeightScale'                                : [       218047,       199995,       184041,       218047,       199995,       184041,       218047,       199995,       184041, ],
    'CountWeightedL1PrefireNom'                                  : [       192656,       192645,       192634, ],
    'CountWeightedL1Prefire'                                     : [       192656,       190971,       194319, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       210006,       192656,       177335,       210006,       192656,       177335,       210006,       192656,       177335, ],
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     784748696), # 784.75MB, avg file size 784.75MB
  ("fsize_db",                        11438629863), # 11.44GB, avg file size 1.43GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_700_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       200016,       200001,       199923, ],
    'CountWeightedL1PrefireNom'                                  : [       192575,       192550,       192534, ],
    'CountWeightedL1Prefire'                                     : [       192575,       190871,       194257, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     798496809), # 798.50MB, avg file size 798.50MB
  ("fsize_db",                        11931037531), # 11.93GB, avg file size 1.08GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_750_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       197000, ],
    'CountWeighted'                                              : [       197020,       196971,       196973, ],
    'CountWeightedL1PrefireNom'                                  : [       189485,       189442,       189464, ],
    'CountWeightedL1Prefire'                                     : [       189485,       187769,       191180, ],
  }),
  ("nof_tree_events",                 197000),
  ("nof_db_events",                   197000),
  ("fsize_local",                     793258382), # 793.26MB, avg file size 793.26MB
  ("fsize_db",                        11877663068), # 11.88GB, avg file size 791.84MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_800_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       199999, ],
    'CountWeighted'                                              : [       199946,       199952,       199972, ],
    'CountWeightedL1PrefireNom'                                  : [       192203,       192189,       192235, ],
    'CountWeightedL1Prefire'                                     : [       192203,       190441,       193951, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     810747694), # 810.75MB, avg file size 810.75MB
  ("fsize_db",                        12127308050), # 12.13GB, avg file size 808.49MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_850_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99978,        99995,        99942, ],
    'CountWeightedLHEWeightScale'                                : [       110667,        99978,        90811,       110667,        99978,        90811,       110667,        99978,        90811, ],
    'CountWeightedL1PrefireNom'                                  : [        96039,        96047,        96021, ],
    'CountWeightedL1Prefire'                                     : [        96039,        95148,        96923, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       106281,        96039,        87251,       106281,        96039,        87251,       106281,        96039,        87251, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     404571066), # 404.57MB, avg file size 404.57MB
  ("fsize_db",                        5935911198), # 5.94GB, avg file size 539.63MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_900_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99965,        99969,        99961, ],
    'CountWeightedLHEWeightScale'                                : [       111333,        99963,        90330,       111333,        99963,        90330,       111333,        99963,        90330, ],
    'CountWeightedL1PrefireNom'                                  : [        95947,        95940,        95956, ],
    'CountWeightedL1Prefire'                                     : [        95947,        95039,        96846, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       106832,        95946,        86712,       106832,        95946,        86712,       106832,        95946,        86712, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     408877629), # 408.88MB, avg file size 408.88MB
  ("fsize_db",                        5930718483), # 5.93GB, avg file size 847.25MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1000_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99979,        99986,        99962, ],
    'CountWeightedL1PrefireNom'                                  : [        95853,        95848,        95849, ],
    'CountWeightedL1Prefire'                                     : [        95853,        94930,        96770, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     418065550), # 418.07MB, avg file size 418.07MB
  ("fsize_db",                        6224151597), # 6.22GB, avg file size 778.02MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1250_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [        99998, ],
    'CountWeighted'                                              : [        99963,        99953,        99949, ],
    'CountWeightedLHEWeightScale'                                : [       113887,        99962,        88509,       113887,        99962,        88509,       113887,        99962,        88509, ],
    'CountWeightedL1PrefireNom'                                  : [        95735,        95723,        95733, ],
    'CountWeightedL1Prefire'                                     : [        95735,        94796,        96668, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       109058,        95734,        84783,       109058,        95734,        84783,       109058,        95734,        84783, ],
  }),
  ("nof_tree_events",                 99998),
  ("nof_db_events",                   99998),
  ("fsize_local",                     413367533), # 413.37MB, avg file size 413.37MB
  ("fsize_db",                        6171310375), # 6.17GB, avg file size 514.28MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1500_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99974,        99938,        99965, ],
    'CountWeightedL1PrefireNom'                                  : [        95609,        95589,        95592, ],
    'CountWeightedL1Prefire'                                     : [        95609,        94644,        96567, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     417238546), # 417.24MB, avg file size 417.24MB
  ("fsize_db",                        6356319473), # 6.36GB, avg file size 635.63MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1750_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99926,        99919,        99947, ],
    'CountWeightedLHEWeightScale'                                : [       115690,        99925,        87204,       115690,        99925,        87204,       115690,        99925,        87204, ],
    'CountWeightedL1PrefireNom'                                  : [        95545,        95531,        95562, ],
    'CountWeightedL1Prefire'                                     : [        95545,        94578,        96508, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       110603,        95544,        83388,       110603,        95544,        83388,       110603,        95544,        83388, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     415269302), # 415.27MB, avg file size 415.27MB
  ("fsize_db",                        6172348486), # 6.17GB, avg file size 771.54MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_2000_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [        97000, ],
    'CountWeighted'                                              : [        96874,        96884,        96862, ],
    'CountWeightedL1PrefireNom'                                  : [        92494,        92487,        92506, ],
    'CountWeightedL1Prefire'                                     : [        92494,        91537,        93452, ],
  }),
  ("nof_tree_events",                 97000),
  ("nof_db_events",                   97000),
  ("fsize_local",                     407647077), # 407.65MB, avg file size 407.65MB
  ("fsize_db",                        6425534542), # 6.43GB, avg file size 494.27MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_2500_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [        97999, ],
    'CountWeighted'                                              : [        97755,        97737,        97747, ],
    'CountWeightedL1PrefireNom'                                  : [        93312,        93294,        93315, ],
    'CountWeightedL1Prefire'                                     : [        93312,        92346,        94278, ],
  }),
  ("nof_tree_events",                 97999),
  ("nof_db_events",                   97999),
  ("fsize_local",                     413379812), # 413.38MB, avg file size 413.38MB
  ("fsize_db",                        6497731845), # 6.50GB, avg file size 590.70MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_3000_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_250_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_250_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                      : [       399997, ],
    'CountWeighted'                                              : [       399935,       400016,       399956, ],
    'CountWeightedLHEWeightScale'                                : [       404892,       399929,       392226,       404892,       399929,       392226,       404892,       399929,       392226, ],
    'CountWeightedL1PrefireNom'                                  : [       392393,       392444,       392422, ],
    'CountWeightedL1Prefire'                                     : [       392393,       390447,       394259, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       397210,       392388,       384858,       397210,       392388,       384858,       397210,       392388,       384858, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     1224608357), # 1.22GB, avg file size 1.22GB
  ("fsize_db",                        20041115926), # 20.04GB, avg file size 871.35MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_250_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-260_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_260_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_260_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                      : [       399997, ],
    'CountWeighted'                                              : [       399964,       400009,       400036, ],
    'CountWeightedLHEWeightScale'                                : [       406237,       399963,       391183,       406237,       399963,       391183,       406237,       399963,       391183, ],
    'CountWeightedL1PrefireNom'                                  : [       392111,       392118,       392186, ],
    'CountWeightedL1Prefire'                                     : [       392111,       390089,       394044, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       398210,       392108,       383531,       398210,       392108,       383531,       398210,       392108,       383531, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     1239574702), # 1.24GB, avg file size 1.24GB
  ("fsize_db",                        20202072552), # 20.20GB, avg file size 962.00MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_260_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-270_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_270_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_270_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                      : [       400000, ],
    'CountWeighted'                                              : [       400051,       399949,       400006, ],
    'CountWeightedLHEWeightScale'                                : [       407495,       400051,       390161,       407495,       400051,       390161,       407495,       400051,       390161, ],
    'CountWeightedL1PrefireNom'                                  : [       391839,       391745,       391840, ],
    'CountWeightedL1Prefire'                                     : [       391839,       389746,       393839, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       399109,       391839,       382216,       399109,       391839,       382216,       399109,       391839,       382216, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1256658338), # 1.26GB, avg file size 1.26GB
  ("fsize_db",                        20268702810), # 20.27GB, avg file size 921.30MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_270_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-280_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_280_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_280_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    31),
  ("nof_events",                      {
    'Count'                                                      : [       399995, ],
    'CountWeighted'                                              : [       400029,       399942,       399946, ],
    'CountWeightedLHEWeightScale'                                : [       408733,       400028,       389180,       408733,       400028,       389180,       408733,       400028,       389180, ],
    'CountWeightedL1PrefireNom'                                  : [       391535,       391454,       391494, ],
    'CountWeightedL1Prefire'                                     : [       391535,       389393,       393594, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       400015,       391533,       380977,       400015,       391533,       380977,       400015,       391533,       380977, ],
  }),
  ("nof_tree_events",                 399995),
  ("nof_db_events",                   399995),
  ("fsize_local",                     1273499522), # 1.27GB, avg file size 1.27GB
  ("fsize_db",                        20542842010), # 20.54GB, avg file size 662.67MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_280_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-300_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_300_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_300_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    26),
  ("nof_events",                      {
    'Count'                                                      : [       399998, ],
    'CountWeighted'                                              : [       400014,       399966,       400007, ],
    'CountWeightedLHEWeightScale'                                : [       411013,       400014,       387362,       411013,       400014,       387362,       411013,       400014,       387362, ],
    'CountWeightedL1PrefireNom'                                  : [       390814,       390773,       390821, ],
    'CountWeightedL1Prefire'                                     : [       390814,       388527,       393031, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       401504,       390814,       378515,       401504,       390814,       378515,       401504,       390814,       378515, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     1301780507), # 1.30GB, avg file size 1.30GB
  ("fsize_db",                        20998766588), # 21.00GB, avg file size 807.64MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_300_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-320_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_320_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_320_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                      : [       293998, ],
    'CountWeighted'                                              : [       293950,       293937,       293988, ],
    'CountWeightedLHEWeightScale'                                : [       303633,       293950,       283520,       303633,       293950,       283520,       303633,       293950,       283520, ],
    'CountWeightedL1PrefireNom'                                  : [       286900,       286879,       286937, ],
    'CountWeightedL1Prefire'                                     : [       286900,       285170,       288586, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       296287,       286899,       276749,       296287,       286899,       276749,       296287,       286899,       276749, ],
  }),
  ("nof_tree_events",                 293998),
  ("nof_db_events",                   293998),
  ("fsize_local",                     977552027), # 977.55MB, avg file size 977.55MB
  ("fsize_db",                        15577989269), # 15.58GB, avg file size 916.35MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_320_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-350_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_350_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_350_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                      : [       281999, ],
    'CountWeighted'                                              : [       281964,       281967,       281961, ],
    'CountWeightedLHEWeightScale'                                : [       293260,       281963,       270389,       293260,       281963,       270389,       293260,       281963,       270389, ],
    'CountWeightedL1PrefireNom'                                  : [       274729,       274703,       274748, ],
    'CountWeightedL1Prefire'                                     : [       274729,       272981,       276437, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       285668,       274728,       263486,       285668,       274728,       263486,       285668,       274728,       263486, ],
  }),
  ("nof_tree_events",                 281999),
  ("nof_db_events",                   281999),
  ("fsize_local",                     964588935), # 964.59MB, avg file size 964.59MB
  ("fsize_db",                        15217194365), # 15.22GB, avg file size 845.40MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_350_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-400_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_400_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_400_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                      : [       298000, ],
    'CountWeighted'                                              : [       297937,       298017,       298003, ],
    'CountWeightedLHEWeightScale'                                : [       313030,       297937,       283380,       313030,       297937,       283380,       313030,       297937,       283380, ],
    'CountWeightedL1PrefireNom'                                  : [       289718,       289765,       289773, ],
    'CountWeightedL1Prefire'                                     : [       289718,       287766,       291640, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       304312,       289718,       275597,       304312,       289718,       275597,       304312,       289718,       275597, ],
  }),
  ("nof_tree_events",                 298000),
  ("nof_db_events",                   298000),
  ("fsize_local",                     1059425920), # 1.06GB, avg file size 1.06GB
  ("fsize_db",                        16133391096), # 16.13GB, avg file size 806.67MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_400_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-450_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_450_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_450_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       299911,       299927,       299942, ],
    'CountWeightedLHEWeightScale'                                : [       317757,       299911,       283222,       317757,       299911,       283222,       317757,       299911,       283222, ],
    'CountWeightedL1PrefireNom'                                  : [       291241,       291239,       291278, ],
    'CountWeightedL1Prefire'                                     : [       291241,       289213,       293245, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       308485,       291241,       275077,       308485,       291241,       275077,       308485,       291241,       275077, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1102292114), # 1.10GB, avg file size 1.10GB
  ("fsize_db",                        16485829471), # 16.49GB, avg file size 867.68MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_450_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_500_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_500_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199968,       199967,       199975, ],
    'CountWeightedLHEWeightScale'                                : [       213383,       199968,       187657,       213383,       199968,       187657,       213383,       199968,       187657, ],
    'CountWeightedL1PrefireNom'                                  : [       194075,       194062,       194084, ],
    'CountWeightedL1Prefire'                                     : [       194075,       192703,       195426, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       207038,       194075,       182158,       207038,       194075,       182158,       207038,       194075,       182158, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     756482707), # 756.48MB, avg file size 756.48MB
  ("fsize_db",                        11497248581), # 11.50GB, avg file size 547.49MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_500_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-550_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_550_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_550_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199971,       199977,       199960, ],
    'CountWeightedLHEWeightScale'                                : [       214738,       199970,       186599,       214738,       199970,       186599,       214738,       199970,       186599, ],
    'CountWeightedL1PrefireNom'                                  : [       194087,       194092,       194073, ],
    'CountWeightedL1Prefire'                                     : [       194087,       192725,       195428, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       208364,       194086,       181141,       208364,       194086,       181141,       208364,       194086,       181141, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     773188072), # 773.19MB, avg file size 773.19MB
  ("fsize_db",                        11543534297), # 11.54GB, avg file size 679.03MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_550_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-600_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_600_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_600_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                      : [       192000, ],
    'CountWeighted'                                              : [       191970,       191962,       191942, ],
    'CountWeightedLHEWeightScale'                                : [       207287,       191970,       178226,       207287,       191970,       178226,       207287,       191970,       178226, ],
    'CountWeightedL1PrefireNom'                                  : [       186268,       186262,       186254, ],
    'CountWeightedL1Prefire'                                     : [       186268,       184954,       187566, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       201088,       186268,       172966,       201088,       186268,       172966,       201088,       186268,       172966, ],
  }),
  ("nof_tree_events",                 192000),
  ("nof_db_events",                   192000),
  ("fsize_local",                     755218369), # 755.22MB, avg file size 755.22MB
  ("fsize_db",                        11191273021), # 11.19GB, avg file size 746.08MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_600_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-650_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_650_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_650_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       200017,       200006,       199949, ],
    'CountWeightedLHEWeightScale'                                : [       217035,       200017,       184833,       217035,       200017,       184833,       217035,       200017,       184833, ],
    'CountWeightedL1PrefireNom'                                  : [       194033,       194006,       194011, ],
    'CountWeightedL1Prefire'                                     : [       194033,       192660,       195385, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       210512,       194033,       179347,       210512,       194033,       179347,       210512,       194033,       179347, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     797721258), # 797.72MB, avg file size 797.72MB
  ("fsize_db",                        11871616225), # 11.87GB, avg file size 539.62MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_650_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-700_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_700_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_700_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                      : [       199998, ],
    'CountWeighted'                                              : [       199972,       199965,       199953, ],
    'CountWeightedLHEWeightScale'                                : [       218037,       199972,       184075,       218037,       199972,       184075,       218037,       199972,       184075, ],
    'CountWeightedL1PrefireNom'                                  : [       194058,       194042,       194052, ],
    'CountWeightedL1Prefire'                                     : [       194058,       192703,       195393, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       211544,       194058,       178659,       211544,       194058,       178659,       211544,       194058,       178659, ],
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     805228469), # 805.23MB, avg file size 805.23MB
  ("fsize_db",                        11820942716), # 11.82GB, avg file size 656.72MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_700_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_750_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_750_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                      : [       198000, ],
    'CountWeighted'                                              : [       197954,       197934,       197956, ],
    'CountWeightedLHEWeightScale'                                : [       216760,       197954,       181572,       216760,       197954,       181572,       216760,       197954,       181572, ],
    'CountWeightedL1PrefireNom'                                  : [       192060,       192034,       192075, ],
    'CountWeightedL1Prefire'                                     : [       192060,       190711,       193389, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       210256,       192060,       176182,       210256,       192060,       176182,       210256,       192060,       176182, ],
  }),
  ("nof_tree_events",                 198000),
  ("nof_db_events",                   198000),
  ("fsize_local",                     802616059), # 802.62MB, avg file size 802.62MB
  ("fsize_db",                        11778577981), # 11.78GB, avg file size 785.24MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_750_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-800_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_800_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_800_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199949,       199989,       199985, ],
    'CountWeightedLHEWeightScale'                                : [       219797,       199949,       182727,       219797,       199949,       182727,       219797,       199949,       182727, ],
    'CountWeightedL1PrefireNom'                                  : [       194069,       194077,       194104, ],
    'CountWeightedL1Prefire'                                     : [       194069,       192727,       195395, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       213290,       194069,       177379,       213290,       194069,       177379,       213290,       194069,       177379, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     815035699), # 815.04MB, avg file size 815.04MB
  ("fsize_db",                        11967660431), # 11.97GB, avg file size 598.38MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_800_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-850_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_850_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_850_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199954,       199962,       199948, ],
    'CountWeightedL1PrefireNom'                                  : [       194010,       194009,       194008, ],
    'CountWeightedL1Prefire'                                     : [       194010,       192655,       195344, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     826205597), # 826.21MB, avg file size 826.21MB
  ("fsize_db",                        12348394332), # 12.35GB, avg file size 823.23MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_850_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-900_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_900_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_900_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                      : [        99999, ],
    'CountWeighted'                                              : [        99997,       100009,        99973, ],
    'CountWeightedLHEWeightScale'                                : [       110561,        99997,        90970,       110561,        99997,        90970,       110561,        99997,        90970, ],
    'CountWeightedL1PrefireNom'                                  : [        97143,        97146,        97134, ],
    'CountWeightedL1Prefire'                                     : [        97143,        96492,        97785, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       107386,        97143,        88386,       107386,        97143,        88386,       107386,        97143,        88386, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     412875096), # 412.88MB, avg file size 412.88MB
  ("fsize_db",                        6022388849), # 6.02GB, avg file size 669.15MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_900_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1000_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_1000_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                      : [        99999, ],
    'CountWeighted'                                              : [        99971,        99973,        99979, ],
    'CountWeightedLHEWeightScale'                                : [       111340,        99971,        90330,       111340,        99971,        90330,       111340,        99971,        90330, ],
    'CountWeightedL1PrefireNom'                                  : [        97084,        97086,        97091, ],
    'CountWeightedL1Prefire'                                     : [        97084,        96427,        97733, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       108110,        97084,        87730,       108110,        97084,        87730,       108110,        97084,        87730, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     414441072), # 414.44MB, avg file size 414.44MB
  ("fsize_db",                        6101733672), # 6.10GB, avg file size 610.17MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_1000_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1250_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_1250_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99945,        99986,        99981, ],
    'CountWeightedL1PrefireNom'                                  : [        97069,        97099,        97092, ],
    'CountWeightedL1Prefire'                                     : [        97069,        96418,        97713, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     419761632), # 419.76MB, avg file size 419.76MB
  ("fsize_db",                        6305015701), # 6.31GB, avg file size 900.72MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_1250_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1500_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_1500_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99945,        99933,        99931, ],
    'CountWeightedL1PrefireNom'                                  : [        97062,        97049,        97057, ],
    'CountWeightedL1Prefire'                                     : [        97062,        96409,        97707, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     415331280), # 415.33MB, avg file size 415.33MB
  ("fsize_db",                        6512057209), # 6.51GB, avg file size 434.14MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_1500_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1750_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_1750_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                      : [        99999, ],
    'CountWeighted'                                              : [        99939,        99936,        99959, ],
    'CountWeightedL1PrefireNom'                                  : [        97022,        97012,        97042, ],
    'CountWeightedL1Prefire'                                     : [        97022,        96359,        97674, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     414653563), # 414.65MB, avg file size 414.65MB
  ("fsize_db",                        6489134095), # 6.49GB, avg file size 540.76MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_1750_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-2000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_2000_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_2000_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99905,        99912,        99890, ],
    'CountWeightedLHEWeightScale'                                : [       115680,        99905,        87185,       115680,        99905,        87185,       115680,        99905,        87185, ],
    'CountWeightedL1PrefireNom'                                  : [        96938,        96927,        96937, ],
    'CountWeightedL1Prefire'                                     : [        96938,        96264,        97600, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       112243,        96938,        84593,       112243,        96938,        84593,       112243,        96938,        84593, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     412228780), # 412.23MB, avg file size 412.23MB
  ("fsize_db",                        6328288934), # 6.33GB, avg file size 575.30MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_2000_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-2500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_2500_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_2500_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                      : [        98000, ],
    'CountWeighted'                                              : [        97879,        97879,        97873, ],
    'CountWeightedLHEWeightScale'                                : [       114845,        97879,        84387,       114845,        97879,        84387,       114845,        97879,        84387, ],
    'CountWeightedL1PrefireNom'                                  : [        94939,        94941,        94937, ],
    'CountWeightedL1Prefire'                                     : [        94939,        94272,        95597, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       111397,        94939,        81852,       111397,        94939,        81852,       111397,        94939,        81852, ],
  }),
  ("nof_tree_events",                 98000),
  ("nof_db_events",                   98000),
  ("fsize_local",                     406138422), # 406.14MB, avg file size 406.14MB
  ("fsize_db",                        6377937593), # 6.38GB, avg file size 490.61MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_2500_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-3000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_3000_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_3000_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                      : [        99999, ],
    'CountWeighted'                                              : [        99816,        99796,        99803, ],
    'CountWeightedLHEWeightScale'                                : [       118531,        99813,        85118,       118531,        99813,        85118,       118531,        99813,        85118, ],
    'CountWeightedL1PrefireNom'                                  : [        96842,        96829,        96835, ],
    'CountWeightedL1Prefire'                                     : [        96842,        96164,        97510, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       115008,        96840,        82584,       115008,        96840,        82584,       115008,        96840,        82584, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     416164231), # 416.16MB, avg file size 416.16MB
  ("fsize_db",                        6547475897), # 6.55GB, avg file size 545.62MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_3000_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       399996, ],
    'CountWeighted'                                              : [       396340,       396381,       396247, ],
    'CountWeightedL1PrefireNom'                                  : [       370950,       370920,       370958, ],
    'CountWeightedL1Prefire'                                     : [       370950,       365058,       376795, ],
  }),
  ("nof_tree_events",                 399996),
  ("nof_db_events",                   399996),
  ("fsize_local",                     1476716934), # 1.48GB, avg file size 1.48GB
  ("fsize_db",                        22186460848), # 22.19GB, avg file size 1.85GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_1_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2VTo2L2Nu_node_SM_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_sm_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                      : [       388999, ],
    'CountWeighted'                                              : [       388918,       388934,       388956, ],
    'CountWeightedLHEWeightScale'                                : [       497857,       469962,       443757,       412133,       388917,       367196,       347077,       327484,       309123, ],
    'CountWeightedL1PrefireNom'                                  : [       377192,       377195,       377223, ],
    'CountWeightedL1Prefire'                                     : [       377192,       374412,       379920, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       482707,       455800,       430505,       399571,       377190,       356213,       336486,       317591,       299866, ],
  }),
  ("nof_tree_events",                 388999),
  ("nof_db_events",                   388999),
  ("fsize_local",                     1408527718), # 1.41GB, avg file size 1.41GB
  ("fsize_db",                        21257341288), # 21.26GB, avg file size 1.25GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_sm_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2VTo2L2Nu_node_2_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_2_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                      : [       400000, ],
    'CountWeighted'                                              : [       399921,       399896,       399913, ],
    'CountWeightedLHEWeightScale'                                : [       519620,       478804,       442924,       434231,       399913,       369767,       368607,       339314,       313624, ],
    'CountWeightedL1PrefireNom'                                  : [       386217,       386154,       386257, ],
    'CountWeightedL1Prefire'                                     : [       386217,       383056,       389340, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       501649,       462453,       427971,       419169,       386211,       357248,       355792,       327666,       302978, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1540735933), # 1.54GB, avg file size 1.54GB
  ("fsize_db",                        23088598268), # 23.09GB, avg file size 1.36GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_2_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2VTo2L2Nu_node_3_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_3_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                      : [       380000, ],
    'CountWeighted'                                              : [       379987,       379939,       379928, ],
    'CountWeightedLHEWeightScale'                                : [       486418,       459049,       433324,       402701,       379984,       358622,       339154,       319943,       301945, ],
    'CountWeightedL1PrefireNom'                                  : [       368403,       368352,       368387, ],
    'CountWeightedL1Prefire'                                     : [       368403,       365666,       371091, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       471483,       445078,       420248,       390319,       368400,       347787,       328713,       310190,       292811, ],
  }),
  ("nof_tree_events",                 380000),
  ("nof_db_events",                   380000),
  ("fsize_local",                     1380962429), # 1.38GB, avg file size 1.38GB
  ("fsize_db",                        20768532098), # 20.77GB, avg file size 1.22GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_3_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2VTo2L2Nu_node_7_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_7_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                      : [       392999, ],
    'CountWeighted'                                              : [       392988,       392955,       392950, ],
    'CountWeightedLHEWeightScale'                                : [       501191,       475874,       451526,       413936,       392988,       372835,       347914,       330263,       313308, ],
    'CountWeightedL1PrefireNom'                                  : [       381547,       381492,       381552, ],
    'CountWeightedL1Prefire'                                     : [       381547,       378818,       384220, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       486493,       462037,       438498,       401786,       381547,       362066,       337691,       320642,       304253, ],
  }),
  ("nof_tree_events",                 392999),
  ("nof_db_events",                   392999),
  ("fsize_local",                     1399561971), # 1.40GB, avg file size 1.40GB
  ("fsize_db",                        21440735341), # 21.44GB, avg file size 1.13GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_7_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2VTo2L2Nu_node_9_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_9_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                      : [       386999, ],
    'CountWeighted'                                              : [       386971,       387035,       386950, ],
    'CountWeightedLHEWeightScale'                                : [       502561,       463311,       428628,       419856,       386971,       357905,       356285,       328279,       303581, ],
    'CountWeightedL1PrefireNom'                                  : [       373627,       373656,       373629, ],
    'CountWeightedL1Prefire'                                     : [       373627,       370549,       376666, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       485101,       447362,       413999,       405249,       373627,       345673,       343873,       316952,       293191, ],
  }),
  ("nof_tree_events",                 386999),
  ("nof_db_events",                   386999),
  ("fsize_local",                     1501665835), # 1.50GB, avg file size 1.50GB
  ("fsize_db",                        22534822736), # 22.53GB, avg file size 1.19GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_9_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2VTo2L2Nu_node_12_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_12_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                      : [       400000, ],
    'CountWeighted'                                              : [       400046,       400024,       399942, ],
    'CountWeightedLHEWeightScale'                                : [       509929,       484450,       459890,       421060,       400046,       379661,       353841,       336073,       318991, ],
    'CountWeightedL1PrefireNom'                                  : [       388458,       388426,       388425, ],
    'CountWeightedL1Prefire'                                     : [       388458,       385696,       391168, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       495081,       470464,       446720,       408785,       388458,       368777,       343515,       326355,       309836, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1421187307), # 1.42GB, avg file size 1.42GB
  ("fsize_db",                        21561540290), # 21.56GB, avg file size 937.46MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_12_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       400000, ],
    'CountWeighted'                                              : [       399998,       399994,       399941, ],
    'CountWeightedL1PrefireNom'                                  : [       388473,       388438,       388469, ],
    'CountWeightedL1Prefire'                                     : [       388473,       385652,       391199, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1706351497), # 1.71GB, avg file size 1.71GB
  ("fsize_db",                        24640211831), # 24.64GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       388000, ],
    'CountWeighted'                                              : [       387905,       387946,       387983, ],
    'CountWeightedL1PrefireNom'                                  : [       376423,       376438,       376483, ],
    'CountWeightedL1Prefire'                                     : [       376423,       373629,       379144, ],
  }),
  ("nof_tree_events",                 388000),
  ("nof_db_events",                   388000),
  ("fsize_local",                     1674414392), # 1.67GB, avg file size 1.67GB
  ("fsize_db",                        24012313674), # 24.01GB, avg file size 1.33GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_260_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       384000, ],
    'CountWeighted'                                              : [       383955,       383965,       383899, ],
    'CountWeightedL1PrefireNom'                                  : [       372436,       372415,       372423, ],
    'CountWeightedL1Prefire'                                     : [       372436,       369639,       375152, ],
  }),
  ("nof_tree_events",                 384000),
  ("nof_db_events",                   384000),
  ("fsize_local",                     1677027001), # 1.68GB, avg file size 1.68GB
  ("fsize_db",                        23968184441), # 23.97GB, avg file size 1.41GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_270_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       400000, ],
    'CountWeighted'                                              : [       399942,       400003,       399967, ],
    'CountWeightedL1PrefireNom'                                  : [       387697,       387701,       387736, ],
    'CountWeightedL1Prefire'                                     : [       387697,       384729,       390579, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1764958335), # 1.76GB, avg file size 1.76GB
  ("fsize_db",                        25138262751), # 25.14GB, avg file size 1.09GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_280_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       299949,       299971,       299986, ],
    'CountWeightedL1PrefireNom'                                  : [       290365,       290363,       290413, ],
    'CountWeightedL1Prefire'                                     : [       290365,       288064,       292613, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1349232941), # 1.35GB, avg file size 1.35GB
  ("fsize_db",                        19012035463), # 19.01GB, avg file size 1.27GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_300_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       299951,       299941,       299974, ],
    'CountWeightedL1PrefireNom'                                  : [       289689,       289677,       289703, ],
    'CountWeightedL1Prefire'                                     : [       289689,       287253,       292074, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1405735922), # 1.41GB, avg file size 1.41GB
  ("fsize_db",                        19447040410), # 19.45GB, avg file size 1.77GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_350_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99975,        99972,        99987, ],
    'CountWeightedL1PrefireNom'                                  : [        96346,        96342,        96357, ],
    'CountWeightedL1Prefire'                                     : [        96346,        95493,        97185, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     484784041), # 484.78MB, avg file size 484.78MB
  ("fsize_db",                        6609409571), # 6.61GB, avg file size 944.20MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_400_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-450_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_450_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_450_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       299959,       299970,       299951, ],
    'CountWeightedL1PrefireNom'                                  : [       288844,       288826,       288860, ],
    'CountWeightedL1Prefire'                                     : [       288844,       286237,       291406, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1494385799), # 1.49GB, avg file size 747.19MB
  ("fsize_db",                        20167217854), # 20.17GB, avg file size 1.26GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_450_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       290000, ],
    'CountWeighted'                                              : [       289988,       289936,       289906, ],
    'CountWeightedL1PrefireNom'                                  : [       278902,       278852,       278879, ],
    'CountWeightedL1Prefire'                                     : [       278902,       276315,       281443, ],
  }),
  ("nof_tree_events",                 290000),
  ("nof_db_events",                   290000),
  ("fsize_local",                     1476280643), # 1.48GB, avg file size 1.48GB
  ("fsize_db",                        19708690689), # 19.71GB, avg file size 1.79GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-550_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_550_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_550_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       299931,       299901,       299925, ],
    'CountWeightedL1PrefireNom'                                  : [       288217,       288174,       288240, ],
    'CountWeightedL1Prefire'                                     : [       288217,       285489,       290900, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1558900426), # 1.56GB, avg file size 779.45MB
  ("fsize_db",                        20644816504), # 20.64GB, avg file size 1.59GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_550_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199908,       199904,       199912, ],
    'CountWeightedL1PrefireNom'                                  : [       192024,       192010,       192035, ],
    'CountWeightedL1Prefire'                                     : [       192024,       190193,       193828, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1055071083), # 1.06GB, avg file size 1.06GB
  ("fsize_db",                        13957904944), # 13.96GB, avg file size 1.16GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_600_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199961,       199968,       199906, ],
    'CountWeightedL1PrefireNom'                                  : [       191776,       191763,       191758, ],
    'CountWeightedL1Prefire'                                     : [       191776,       189883,       193642, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1069842043), # 1.07GB, avg file size 1.07GB
  ("fsize_db",                        14016331858), # 14.02GB, avg file size 2.00GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_650_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199903,       199932,       199911, ],
    'CountWeightedL1PrefireNom'                                  : [       191637,       191647,       191645, ],
    'CountWeightedL1Prefire'                                     : [       191637,       189725,       193523, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1084365019), # 1.08GB, avg file size 1.08GB
  ("fsize_db",                        14253263609), # 14.25GB, avg file size 1.10GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_700_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99924,        99962,        99957, ],
    'CountWeightedL1PrefireNom'                                  : [        95751,        95766,        95774, ],
    'CountWeightedL1Prefire'                                     : [        95751,        94791,        96699, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     548046618), # 548.05MB, avg file size 548.05MB
  ("fsize_db",                        7146269195), # 7.15GB, avg file size 1.02GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199915,       199922,       199927, ],
    'CountWeightedL1PrefireNom'                                  : [       191447,       191447,       191459, ],
    'CountWeightedL1Prefire'                                     : [       191447,       189502,       193369, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1104870040), # 1.10GB, avg file size 1.10GB
  ("fsize_db",                        14420020815), # 14.42GB, avg file size 1.31GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_800_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199873,       199865,       199882, ],
    'CountWeightedL1PrefireNom'                                  : [       191404,       191393,       191414, ],
    'CountWeightedL1Prefire'                                     : [       191404,       189461,       193326, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1112254573), # 1.11GB, avg file size 1.11GB
  ("fsize_db",                        14617490096), # 14.62GB, avg file size 1.04GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_850_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99939,        99918,        99928, ],
    'CountWeightedL1PrefireNom'                                  : [        95667,        95643,        95670, ],
    'CountWeightedL1Prefire'                                     : [        95667,        94689,        96634, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     560696219), # 560.70MB, avg file size 560.70MB
  ("fsize_db",                        7382733082), # 7.38GB, avg file size 671.16MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_900_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99923,        99922,        99919, ],
    'CountWeightedL1PrefireNom'                                  : [        95624,        95620,        95622, ],
    'CountWeightedL1Prefire'                                     : [        95624,        94638,        96597, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     566024867), # 566.02MB, avg file size 566.02MB
  ("fsize_db",                        7364574553), # 7.36GB, avg file size 1.05GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_1000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99896,        99880,        99893, ],
    'CountWeightedL1PrefireNom'                                  : [        95402,        95396,        95402, ],
    'CountWeightedL1Prefire'                                     : [        95402,        94380,        96413, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     572570737), # 572.57MB, avg file size 572.57MB
  ("fsize_db",                        7497237044), # 7.50GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_1250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99830,        99839,        99832, ],
    'CountWeightedL1PrefireNom'                                  : [        95322,        95334,        95315, ],
    'CountWeightedL1Prefire'                                     : [        95322,        94301,        96336, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     574057612), # 574.06MB, avg file size 574.06MB
  ("fsize_db",                        7582428905), # 7.58GB, avg file size 1.52GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_1500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99719,        99735,        99741, ],
    'CountWeightedL1PrefireNom'                                  : [        95139,        95146,        95148, ],
    'CountWeightedL1Prefire'                                     : [        95139,        94105,        96167, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     574127296), # 574.13MB, avg file size 574.13MB
  ("fsize_db",                        7802866732), # 7.80GB, avg file size 650.24MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_1750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99675,        99681,        99659, ],
    'CountWeightedL1PrefireNom'                                  : [        95001,        94999,        95001, ],
    'CountWeightedL1Prefire'                                     : [        95001,        93947,        96046, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     572648342), # 572.65MB, avg file size 572.65MB
  ("fsize_db",                        7810715378), # 7.81GB, avg file size 710.07MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_2000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        98787,        98819,        98810, ],
    'CountWeightedL1PrefireNom'                                  : [        94042,        94052,        94066, ],
    'CountWeightedL1Prefire'                                     : [        94042,        92985,        95094, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     572481800), # 572.48MB, avg file size 572.48MB
  ("fsize_db",                        7943092984), # 7.94GB, avg file size 992.89MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_3000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-250_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_250_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_250_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                      : [       386000, ],
    'CountWeighted'                                              : [       380711,       380684,       380654, ],
    'CountWeightedLHEWeightScale'                                : [       418477,       382051,       351705,       416983,       380711,       350495,       415816,       379664,       349551, ],
    'CountWeightedL1PrefireNom'                                  : [       351680,       351624,       351702, ],
    'CountWeightedL1Prefire'                                     : [       351680,       345403,       357976, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       386173,       352974,       325316,       384728,       351678,       324146,       383600,       350666,       323233, ],
  }),
  ("nof_tree_events",                 386000),
  ("nof_db_events",                   386000),
  ("fsize_local",                     1664239445), # 1.66GB, avg file size 1.66GB
  ("fsize_db",                        23569723909), # 23.57GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-260_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_260_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_260_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                      : [       400000, ],
    'CountWeighted'                                              : [       396138,       396210,       396124, ],
    'CountWeightedLHEWeightScale'                                : [       425618,       397454,       372943,       424175,       396138,       371737,       423058,       395121,       370804, ],
    'CountWeightedL1PrefireNom'                                  : [       369736,       369732,       369757, ],
    'CountWeightedL1Prefire'                                     : [       369736,       363831,       375627, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       396678,       371010,       348593,       395281,       369736,       347424,       394200,       368750,       346521, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1599479238), # 1.60GB, avg file size 1.60GB
  ("fsize_db",                        22974833125), # 22.97GB, avg file size 1.21GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_260_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-270_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_270_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_270_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                      : [       400000, ],
    'CountWeighted'                                              : [       396176,       396169,       396177, ],
    'CountWeightedLHEWeightScale'                                : [       425826,       397469,       372790,       424408,       396175,       371605,       423310,       395176,       370689, ],
    'CountWeightedL1PrefireNom'                                  : [       369669,       369630,       369702, ],
    'CountWeightedL1Prefire'                                     : [       369669,       363737,       375586, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       396770,       370920,       348351,       395398,       369667,       347203,       394336,       368700,       346316, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1601296312), # 1.60GB, avg file size 1.60GB
  ("fsize_db",                        22808220732), # 22.81GB, avg file size 1.20GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_270_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-280_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_280_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_280_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                      : [       400000, ],
    'CountWeighted'                                              : [       396168,       396205,       396164, ],
    'CountWeightedLHEWeightScale'                                : [       426095,       397392,       372446,       424750,       396167,       371325,       423708,       395219,       370458, ],
    'CountWeightedL1PrefireNom'                                  : [       369680,       369657,       369721, ],
    'CountWeightedL1Prefire'                                     : [       369680,       363745,       375598, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       397049,       370864,       348028,       395747,       369678,       346942,       394739,       368761,       346102, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1603803792), # 1.60GB, avg file size 1.60GB
  ("fsize_db",                        22983626173), # 22.98GB, avg file size 1.21GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_280_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-300_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_300_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_300_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                      : [       282000, ],
    'CountWeighted'                                              : [       279385,       279307,       279385, ],
    'CountWeightedLHEWeightScale'                                : [       300913,       280205,       262165,       300009,       279384,       261415,       299307,       278746,       260833, ],
    'CountWeightedL1PrefireNom'                                  : [       260494,       260430,       260526, ],
    'CountWeightedL1Prefire'                                     : [       260494,       256264,       264710, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       280220,       261288,       244794,       279344,       260493,       244067,       278666,       259876,       243504, ],
  }),
  ("nof_tree_events",                 282000),
  ("nof_db_events",                   282000),
  ("fsize_local",                     1133502327), # 1.13GB, avg file size 1.13GB
  ("fsize_db",                        15951259391), # 15.95GB, avg file size 839.54MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_300_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-320_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_320_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_320_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       297163,       297090,       297116, ],
    'CountWeightedLHEWeightScale'                                : [       320676,       297966,       278290,       319787,       297162,       277558,       319097,       296536,       276989, ],
    'CountWeightedL1PrefireNom'                                  : [       276816,       276758,       276832, ],
    'CountWeightedL1Prefire'                                     : [       276816,       272256,       281359, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       298343,       277588,       259591,       297488,       276814,       258885,       296824,       276212,       258338, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1209170903), # 1.21GB, avg file size 1.21GB
  ("fsize_db",                        17224376684), # 17.22GB, avg file size 1.01GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_320_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-350_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_350_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_350_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       297244,       297241,       297247, ],
    'CountWeightedLHEWeightScale'                                : [       321677,       297993,       277648,       320847,       297243,       276968,       320201,       296661,       276438, ],
    'CountWeightedL1PrefireNom'                                  : [       276729,       276694,       276755, ],
    'CountWeightedL1Prefire'                                     : [       276729,       272130,       281318, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       299102,       277449,       258780,       298305,       276728,       258126,       297684,       276168,       257617, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1211954372), # 1.21GB, avg file size 1.21GB
  ("fsize_db",                        16911146727), # 16.91GB, avg file size 1.06GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_350_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-400_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_400_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_400_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                      : [       292000, ],
    'CountWeighted'                                              : [       289082,       289007,       289038, ],
    'CountWeightedLHEWeightScale'                                : [       314301,       289648,       268560,       313669,       289080,       268047,       313177,       288637,       267646, ],
    'CountWeightedL1PrefireNom'                                  : [       268541,       268476,       268569, ],
    'CountWeightedL1Prefire'                                     : [       268541,       263946,       273125, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       291657,       269085,       249782,       291049,       268538,       249287,       290575,       268112,       248901, ],
  }),
  ("nof_tree_events",                 292000),
  ("nof_db_events",                   292000),
  ("fsize_local",                     1185599308), # 1.19GB, avg file size 1.19GB
  ("fsize_db",                        16538417486), # 16.54GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_400_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-450_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_450_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_450_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       297031,       296940,       296861, ],
    'CountWeightedLHEWeightScale'                                : [       324809,       297551,       274418,       324224,       297027,       273945,       323766,       296616,       273576, ],
    'CountWeightedL1PrefireNom'                                  : [       275420,       275359,       275384, ],
    'CountWeightedL1Prefire'                                     : [       275420,       270596,       280232, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       300898,       275922,       254770,       300334,       275418,       254315,       299894,       275023,       253959, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1225242877), # 1.23GB, avg file size 1.23GB
  ("fsize_db",                        16984173640), # 16.98GB, avg file size 808.77MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_450_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-500_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_500_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_500_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       296817,       296853,       296840, ],
    'CountWeightedLHEWeightScale'                                : [       326340,       297263,       272948,       325839,       296817,       272548,       325446,       296467,       272234, ],
    'CountWeightedL1PrefireNom'                                  : [       274894,       274871,       274933, ],
    'CountWeightedL1Prefire'                                     : [       274894,       269994,       279785, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       301934,       275325,       253037,       301451,       274894,       252651,       301073,       274557,       252349, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1233131985), # 1.23GB, avg file size 1.23GB
  ("fsize_db",                        16980250583), # 16.98GB, avg file size 1.54GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-600_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_600_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_600_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       197637,       197650,       197618, ],
    'CountWeightedLHEWeightScale'                                : [       219587,       197814,       179948,       219387,       197637,       179790,       219230,       197498,       179666, ],
    'CountWeightedL1PrefireNom'                                  : [       182291,       182286,       182297, ],
    'CountWeightedL1Prefire'                                     : [       182291,       178871,       185707, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       202356,       182460,       166105,       202166,       182291,       165954,       202016,       182159,       165836, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     832507226), # 832.51MB, avg file size 832.51MB
  ("fsize_db",                        11350421129), # 11.35GB, avg file size 1.03GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_600_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-650_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_650_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_650_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                      : [       197000, ],
    'CountWeighted'                                              : [       194681,       194620,       194614, ],
    'CountWeightedLHEWeightScale'                                : [       217393,       194844,       176394,       217205,       194679,       176247,       217057,       194548,       176131, ],
    'CountWeightedL1PrefireNom'                                  : [       179001,       178982,       178971, ],
    'CountWeightedL1Prefire'                                     : [       179001,       175525,       182477, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       199759,       179158,       162337,       199579,       178999,       162195,       199437,       178874,       162084, ],
  }),
  ("nof_tree_events",                 197000),
  ("nof_db_events",                   197000),
  ("fsize_local",                     824912550), # 824.91MB, avg file size 824.91MB
  ("fsize_db",                        11416936121), # 11.42GB, avg file size 1.04GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_650_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-700_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_700_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_700_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       197261,       197246,       197256, ],
    'CountWeightedLHEWeightScale'                                : [       221433,       197396,       178003,       221273,       197255,       177878,       221147,       197144,       177779, ],
    'CountWeightedL1PrefireNom'                                  : [       181140,       181088,       181186, ],
    'CountWeightedL1Prefire'                                     : [       181140,       177567,       184722, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       203172,       181271,       163576,       203019,       181136,       163457,       202899,       181030,       163363, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     842056467), # 842.06MB, avg file size 842.06MB
  ("fsize_db",                        11593555122), # 11.59GB, avg file size 966.13MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_700_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-750_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_750_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_750_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       197207,       197194,       197247, ],
    'CountWeightedLHEWeightScale'                                : [       222484,       197324,       177159,       222350,       197207,       177056,       222245,       197115,       176974, ],
    'CountWeightedL1PrefireNom'                                  : [       180670,       180647,       180708, ],
    'CountWeightedL1Prefire'                                     : [       180670,       177017,       184333, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       203682,       180783,       162413,       203554,       180670,       162313,       203453,       180582,       162235, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     846065020), # 846.07MB, avg file size 846.07MB
  ("fsize_db",                        11489097788), # 11.49GB, avg file size 2.30GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-850_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_850_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_850_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       196919,       196885,       196894, ],
    'CountWeightedLHEWeightScale'                                : [       224088,       197016,       175475,       223978,       196919,       175391,       223891,       196843,       175324, ],
    'CountWeightedL1PrefireNom'                                  : [       179908,       179858,       179926, ],
    'CountWeightedL1Prefire'                                     : [       179908,       176163,       183665, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       204638,       180000,       160432,       204533,       179908,       160351,       204449,       179835,       160287, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     852438338), # 852.44MB, avg file size 852.44MB
  ("fsize_db",                        11469515493), # 11.47GB, avg file size 1.43GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_850_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-900_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_900_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_900_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        98347,        98370,        98369, ],
    'CountWeightedLHEWeightScale'                                : [       112494,        98389,        87322,       112442,        98343,        87282,       112401,        98308,        87251, ],
    'CountWeightedL1PrefireNom'                                  : [        89724,        89720,        89740, ],
    'CountWeightedL1Prefire'                                     : [        89724,        87828,        91630, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       102560,        89766,        79708,       102511,        89722,        79670,       102471,        89688,        79640, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     428087135), # 428.09MB, avg file size 428.09MB
  ("fsize_db",                        5871346880), # 5.87GB, avg file size 489.28MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_900_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-1000_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_1000_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_1000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        98141,        98138,        98153, ],
    'CountWeightedLHEWeightScale'                                : [       113171,        98179,        86498,       113127,        98141,        86465,       113093,        98112,        86439, ],
    'CountWeightedL1PrefireNom'                                  : [        89117,        89099,        89132, ],
    'CountWeightedL1Prefire'                                     : [        89117,        87145,        91098, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       102713,        89153,        78586,       102671,        89117,        78554,       102638,        89089,        78529, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     430740900), # 430.74MB, avg file size 430.74MB
  ("fsize_db",                        5935760871), # 5.94GB, avg file size 494.65MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_1000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-1750_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_1750_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_1750_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        96184,        96181,        96147, ],
    'CountWeightedLHEWeightScale'                                : [       116927,        96197,        81030,       116911,        96183,        81018,       116897,        96172,        81008, ],
    'CountWeightedL1PrefireNom'                                  : [        86077,        86056,        86088, ],
    'CountWeightedL1Prefire'                                     : [        86077,        83936,        88250, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       104632,        86089,        72544,       104616,        86077,        72533,       104604,        86066,        72524, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     423480922), # 423.48MB, avg file size 423.48MB
  ("fsize_db",                        5865706342), # 5.87GB, avg file size 651.75MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_1750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-2000_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_2000_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_2000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        95168,        95195,        95174, ],
    'CountWeightedLHEWeightScale'                                : [       117499,        95175,        79172,       117490,        95168,        79166,       117483,        95162,        79161, ],
    'CountWeightedL1PrefireNom'                                  : [        84767,        84776,        84769, ],
    'CountWeightedL1Prefire'                                     : [        84767,        82580,        86989, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       104637,        84772,        70525,       104629,        84766,        70520,       104622,        84760,        70515, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     420304026), # 420.30MB, avg file size 420.30MB
  ("fsize_db",                        6015024771), # 6.02GB, avg file size 601.50MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_2000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       390000, ],
    'CountWeighted'                                              : [       390069,       389998,       389980, ],
    'CountWeightedL1PrefireNom'                                  : [       382746,       382675,       382704, ],
    'CountWeightedL1Prefire'                                     : [       382746,       380832,       384560, ],
  }),
  ("nof_tree_events",                 390000),
  ("nof_db_events",                   390000),
  ("fsize_local",                     1182142184), # 1.18GB, avg file size 1.18GB
  ("fsize_db",                        20093492648), # 20.09GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       360000, ],
    'CountWeighted'                                              : [       359964,       360000,       359999, ],
    'CountWeightedLHEWeightScale'                                : [       365610,       359961,       352043,       365610,       359961,       352043,       365610,       359961,       352043, ],
    'CountWeightedL1PrefireNom'                                  : [       352839,       352857,       352876, ],
    'CountWeightedL1Prefire'                                     : [       352839,       351000,       354604, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       358325,       352837,       345110,       358325,       352837,       345110,       358325,       352837,       345110, ],
  }),
  ("nof_tree_events",                 360000),
  ("nof_db_events",                   360000),
  ("fsize_local",                     1093573923), # 1.09GB, avg file size 1.09GB
  ("fsize_db",                        17758553715), # 17.76GB, avg file size 986.59MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_260_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       392000, ],
    'CountWeighted'                                              : [       392036,       391971,       392016, ],
    'CountWeightedLHEWeightScale'                                : [       399342,       392022,       382349,       399342,       392022,       382349,       399342,       392022,       382349, ],
    'CountWeightedL1PrefireNom'                                  : [       383961,       383909,       383959, ],
    'CountWeightedL1Prefire'                                     : [       383961,       381892,       385944, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       391084,       383950,       374534,       391084,       383950,       374534,       391084,       383950,       374534, ],
  }),
  ("nof_tree_events",                 392000),
  ("nof_db_events",                   392000),
  ("fsize_local",                     1204083984), # 1.20GB, avg file size 1.20GB
  ("fsize_db",                        19361033085), # 19.36GB, avg file size 1.21GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_270_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       398000, ],
    'CountWeighted'                                              : [       397935,       397980,       397961, ],
    'CountWeightedL1PrefireNom'                                  : [       389352,       389368,       389382, ],
    'CountWeightedL1Prefire'                                     : [       389352,       387171,       391453, ],
  }),
  ("nof_tree_events",                 398000),
  ("nof_db_events",                   398000),
  ("fsize_local",                     1247995549), # 1.25GB, avg file size 1.25GB
  ("fsize_db",                        20704800616), # 20.70GB, avg file size 900.21MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_280_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       300049,       299930,       299959, ],
    'CountWeightedLHEWeightScale'                                : [       308237,       300049,       290522,       308237,       300049,       290522,       308237,       300049,       290522, ],
    'CountWeightedL1PrefireNom'                                  : [       293089,       292994,       293046, ],
    'CountWeightedL1Prefire'                                     : [       293089,       291347,       294770, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       301062,       293089,       283845,       301062,       293089,       283845,       301062,       293089,       283845, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     950248847), # 950.25MB, avg file size 950.25MB
  ("fsize_db",                        15151937781), # 15.15GB, avg file size 688.72MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_300_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       299962,       299954,       299997, ],
    'CountWeightedLHEWeightScale'                                : [       309838,       299962,       289298,       309838,       299962,       289298,       309838,       299962,       289298, ],
    'CountWeightedL1PrefireNom'                                  : [       292505,       292492,       292539, ],
    'CountWeightedL1Prefire'                                     : [       292505,       290662,       294301, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       302075,       292505,       282141,       302075,       292505,       282141,       302075,       292505,       282141, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     970403834), # 970.40MB, avg file size 970.40MB
  ("fsize_db",                        15215406969), # 15.22GB, avg file size 1.17GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_320_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       299995,       300043,       299941, ],
    'CountWeightedLHEWeightScale'                                : [       311982,       299993,       287611,       311982,       299993,       287611,       311982,       299993,       287611, ],
    'CountWeightedL1PrefireNom'                                  : [       291873,       291886,       291857, ],
    'CountWeightedL1Prefire'                                     : [       291873,       289896,       293797, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       303481,       291870,       279881,       303481,       291870,       279881,       303481,       291870,       279881, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     996697840), # 996.70MB, avg file size 996.70MB
  ("fsize_db",                        15430234358), # 15.43GB, avg file size 1.10GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_350_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       296000, ],
    'CountWeighted'                                              : [       296027,       295915,       295984, ],
    'CountWeightedLHEWeightScale'                                : [       310901,       296027,       281469,       310901,       296027,       281469,       310901,       296027,       281469, ],
    'CountWeightedL1PrefireNom'                                  : [       287270,       287195,       287248, ],
    'CountWeightedL1Prefire'                                     : [       287270,       285176,       289316, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       301663,       287270,       273209,       301663,       287270,       273209,       301663,       287270,       273209, ],
  }),
  ("nof_tree_events",                 296000),
  ("nof_db_events",                   296000),
  ("fsize_local",                     1023211313), # 1.02GB, avg file size 1.02GB
  ("fsize_db",                        15540706594), # 15.54GB, avg file size 971.29MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_400_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       272000, ],
    'CountWeighted'                                              : [       271995,       271937,       271996, ],
    'CountWeightedLHEWeightScale'                                : [       288103,       271995,       256804,       288103,       271995,       256804,       288103,       271995,       256804, ],
    'CountWeightedL1PrefireNom'                                  : [       263477,       263418,       263507, ],
    'CountWeightedL1Prefire'                                     : [       263477,       261464,       265458, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       279032,       263477,       248822,       279032,       263477,       248822,       279032,       263477,       248822, ],
  }),
  ("nof_tree_events",                 272000),
  ("nof_db_events",                   272000),
  ("fsize_local",                     973261808), # 973.26MB, avg file size 973.26MB
  ("fsize_db",                        14544281532), # 14.54GB, avg file size 808.02MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_450_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       190000, ],
    'CountWeighted'                                              : [       189995,       190029,       190021, ],
    'CountWeightedLHEWeightScale'                                : [       202729,       189995,       178272,       202729,       189995,       178272,       202729,       189995,       178272, ],
    'CountWeightedL1PrefireNom'                                  : [       183623,       183648,       183634, ],
    'CountWeightedL1Prefire'                                     : [       183623,       182135,       185093, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       195888,       183623,       172331,       195888,       183623,       172331,       195888,       183623,       172331, ],
  }),
  ("nof_tree_events",                 190000),
  ("nof_db_events",                   190000),
  ("fsize_local",                     699379981), # 699.38MB, avg file size 699.38MB
  ("fsize_db",                        10300681960), # 10.30GB, avg file size 858.39MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199975,       199951,       200000, ],
    'CountWeightedLHEWeightScale'                                : [       214726,       199975,       186581,       214726,       199975,       186581,       214726,       199975,       186581, ],
    'CountWeightedL1PrefireNom'                                  : [       192936,       192910,       192956, ],
    'CountWeightedL1Prefire'                                     : [       192936,       191299,       194551, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       207117,       192936,       180053,       207117,       192936,       180053,       207117,       192936,       180053, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     755716096), # 755.72MB, avg file size 755.72MB
  ("fsize_db",                        10884541416), # 10.88GB, avg file size 989.50MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_550_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199983,       199972,       199941, ],
    'CountWeightedLHEWeightScale'                                : [       215954,       199982,       185647,       215954,       199982,       185647,       215954,       199982,       185647, ],
    'CountWeightedL1PrefireNom'                                  : [       192691,       192676,       192684, ],
    'CountWeightedL1Prefire'                                     : [       192691,       191004,       194357, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       208030,       192689,       178922,       208030,       192689,       178922,       208030,       192689,       178922, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     771728616), # 771.73MB, avg file size 771.73MB
  ("fsize_db",                        11044936345), # 11.04GB, avg file size 920.41MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_600_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       188000, ],
    'CountWeighted'                                              : [       187980,       187931,       187961, ],
    'CountWeightedLHEWeightScale'                                : [       204025,       187980,       173735,       204025,       187980,       173735,       204025,       187980,       173735, ],
    'CountWeightedL1PrefireNom'                                  : [       180909,       180857,       180920, ],
    'CountWeightedL1Prefire'                                     : [       180909,       179283,       182514, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       196304,       180909,       167239,       196304,       180909,       167239,       196304,       180909,       167239, ],
  }),
  ("nof_tree_events",                 188000),
  ("nof_db_events",                   188000),
  ("fsize_local",                     739481308), # 739.48MB, avg file size 739.48MB
  ("fsize_db",                        10510514184), # 10.51GB, avg file size 700.70MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_650_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199919,       200015,       199967, ],
    'CountWeightedLHEWeightScale'                                : [       218058,       199919,       184085,       218058,       199919,       184085,       218058,       199919,       184085, ],
    'CountWeightedL1PrefireNom'                                  : [       192226,       192267,       192272, ],
    'CountWeightedL1Prefire'                                     : [       192226,       190462,       193972, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       209587,       192226,       177014,       209587,       192226,       177014,       209587,       192226,       177014, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     798445478), # 798.45MB, avg file size 798.45MB
  ("fsize_db",                        11214998225), # 11.21GB, avg file size 1.40GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_700_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       196000, ],
    'CountWeighted'                                              : [       195945,       195987,       195992, ],
    'CountWeightedL1PrefireNom'                                  : [       188193,       188207,       188231, ],
    'CountWeightedL1Prefire'                                     : [       188193,       186425,       189946, ],
  }),
  ("nof_tree_events",                 196000),
  ("nof_db_events",                   196000),
  ("fsize_local",                     799414521), # 799.41MB, avg file size 799.41MB
  ("fsize_db",                        11545737081), # 11.55GB, avg file size 962.14MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-800_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_800_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_800_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199954,       199983,       199978, ],
    'CountWeightedL1PrefireNom'                                  : [       191983,       191996,       192001, ],
    'CountWeightedL1Prefire'                                     : [       191983,       190171,       193781, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     824650411), # 824.65MB, avg file size 824.65MB
  ("fsize_db",                        11819983411), # 11.82GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_800_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       192000, ],
    'CountWeighted'                                              : [       191971,       191959,       191946, ],
    'CountWeightedL1PrefireNom'                                  : [       184232,       184202,       184240, ],
    'CountWeightedL1Prefire'                                     : [       184232,       182472,       185973, ],
  }),
  ("nof_tree_events",                 192000),
  ("nof_db_events",                   192000),
  ("fsize_local",                     799057328), # 799.06MB, avg file size 799.06MB
  ("fsize_db",                        11490975329), # 11.49GB, avg file size 766.07MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_850_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [        95000, ],
    'CountWeighted'                                              : [        94980,        94979,        94981, ],
    'CountWeightedLHEWeightScale'                                : [       105134,        94980,        86280,       105134,        94980,        86280,       105134,        94980,        86280, ],
    'CountWeightedL1PrefireNom'                                  : [        91044,        91041,        91048, ],
    'CountWeightedL1Prefire'                                     : [        91044,        90156,        91927, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       100747,        91044,        82723,       100747,        91044,        82723,       100747,        91044,        82723, ],
  }),
  ("nof_tree_events",                 95000),
  ("nof_db_events",                   95000),
  ("fsize_local",                     395908546), # 395.91MB, avg file size 395.91MB
  ("fsize_db",                        5517036529), # 5.52GB, avg file size 788.15MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_900_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-1000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1000_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_1000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99979,        99992,        99979, ],
    'CountWeightedLHEWeightScale'                                : [       111332,        99979,        90326,       111332,        99979,        90326,       111332,        99979,        90326, ],
    'CountWeightedL1PrefireNom'                                  : [        95771,        95775,        95776, ],
    'CountWeightedL1Prefire'                                     : [        95771,        94826,        96708, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       106622,        95771,        86545,       106622,        95771,        86545,       106622,        95771,        86545, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     423136587), # 423.14MB, avg file size 423.14MB
  ("fsize_db",                        5887358169), # 5.89GB, avg file size 654.15MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99970,        99975,        99983, ],
    'CountWeightedL1PrefireNom'                                  : [        95597,        95599,        95609, ],
    'CountWeightedL1Prefire'                                     : [        95597,        94622,        96568, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     434118100), # 434.12MB, avg file size 434.12MB
  ("fsize_db",                        6210975535), # 6.21GB, avg file size 690.11MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99965,        99967,        99948, ],
    'CountWeightedLHEWeightScale'                                : [       113902,        99965,        88519,       113902,        99965,        88519,       113902,        99965,        88519, ],
    'CountWeightedL1PrefireNom'                                  : [        95493,        95493,        95482, ],
    'CountWeightedL1Prefire'                                     : [        95493,        94504,        96479, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       108786,        95492,        84575,       108786,        95492,        84575,       108786,        95492,        84575, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     424605319), # 424.61MB, avg file size 424.61MB
  ("fsize_db",                        5949909431), # 5.95GB, avg file size 1.49GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-1750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1750_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_1750_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99940,        99944,        99946, ],
    'CountWeightedL1PrefireNom'                                  : [        95395,        95386,        95406, ],
    'CountWeightedL1Prefire'                                     : [        95395,        94391,        96394, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     424659682), # 424.66MB, avg file size 424.66MB
  ("fsize_db",                        6303523737), # 6.30GB, avg file size 573.05MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [        92000, ],
    'CountWeighted'                                              : [        91915,        91911,        91908, ],
    'CountWeightedLHEWeightScale'                                : [       106418,        91911,        80211,       106418,        91911,        80211,       106418,        91911,        80211, ],
    'CountWeightedL1PrefireNom'                                  : [        87674,        87669,        87669, ],
    'CountWeightedL1Prefire'                                     : [        87674,        86742,        88603, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       101496,        87672,        76520,       101496,        87672,        76520,       101496,        87672,        76520, ],
  }),
  ("nof_tree_events",                 92000),
  ("nof_db_events",                   92000),
  ("fsize_local",                     386005443), # 386.01MB, avg file size 386.01MB
  ("fsize_db",                        5565938746), # 5.57GB, avg file size 927.66MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_2000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99871,        99888,        99880, ],
    'CountWeightedL1PrefireNom'                                  : [        95234,        95235,        95249, ],
    'CountWeightedL1Prefire'                                     : [        95234,        94221,        96247, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     420966050), # 420.97MB, avg file size 420.97MB
  ("fsize_db",                        6456631366), # 6.46GB, avg file size 586.97MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_2500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99737,        99746,        99744, ],
    'CountWeightedL1PrefireNom'                                  : [        95002,        95000,        95022, ],
    'CountWeightedL1Prefire'                                     : [        95002,        93975,        96030, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     420510414), # 420.51MB, avg file size 420.51MB
  ("fsize_db",                        6431618251), # 6.43GB, avg file size 803.95MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_3000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2Tau_M-250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_250_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_250_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                      : [       400000, ],
    'CountWeighted'                                              : [       399948,       399972,       399986, ],
    'CountWeightedLHEWeightScale'                                : [       404905,       399948,       392245,       404905,       399948,       392245,       404905,       399948,       392245, ],
    'CountWeightedL1PrefireNom'                                  : [       392102,       392102,       392143, ],
    'CountWeightedL1Prefire'                                     : [       392102,       390074,       394044, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       396901,       392102,       384576,       396901,       392102,       384576,       396901,       392102,       384576, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1217244282), # 1.22GB, avg file size 1.22GB
  ("fsize_db",                        20195673518), # 20.20GB, avg file size 878.07MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2Tau_M-260_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_260_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_260_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                      : [       384000, ],
    'CountWeighted'                                              : [       383963,       383923,       383971, ],
    'CountWeightedLHEWeightScale'                                : [       390007,       383963,       375523,       390007,       383963,       375523,       390007,       383963,       375523, ],
    'CountWeightedL1PrefireNom'                                  : [       376052,       376016,       376063, ],
    'CountWeightedL1Prefire'                                     : [       376052,       374024,       377991, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       381915,       376052,       367818,       381915,       376052,       367818,       381915,       376052,       367818, ],
  }),
  ("nof_tree_events",                 384000),
  ("nof_db_events",                   384000),
  ("fsize_local",                     1186195270), # 1.19GB, avg file size 1.19GB
  ("fsize_db",                        19164112451), # 19.16GB, avg file size 1.13GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_260_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2Tau_M-270_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_270_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_270_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                      : [       390000, ],
    'CountWeighted'                                              : [       389995,       389981,       389966, ],
    'CountWeightedLHEWeightScale'                                : [       397347,       389995,       380395,       397347,       389995,       380395,       397347,       389995,       380395, ],
    'CountWeightedL1PrefireNom'                                  : [       381607,       381567,       381608, ],
    'CountWeightedL1Prefire'                                     : [       381607,       379475,       383652, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       388743,       381607,       372261,       388743,       381607,       372261,       388743,       381607,       372261, ],
  }),
  ("nof_tree_events",                 390000),
  ("nof_db_events",                   390000),
  ("fsize_local",                     1219791821), # 1.22GB, avg file size 1.22GB
  ("fsize_db",                        19739699313), # 19.74GB, avg file size 1.10GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_270_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2Tau_M-280_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_280_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_280_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                      : [       379000, ],
    'CountWeighted'                                              : [       378993,       378961,       378972, ],
    'CountWeightedLHEWeightScale'                                : [       387251,       378993,       368745,       387251,       378993,       368745,       387251,       378993,       368745, ],
    'CountWeightedL1PrefireNom'                                  : [       370464,       370422,       370469, ],
    'CountWeightedL1Prefire'                                     : [       370464,       368319,       372531, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       378486,       370464,       360502,       378486,       370464,       360502,       378486,       370464,       360502, ],
  }),
  ("nof_tree_events",                 379000),
  ("nof_db_events",                   379000),
  ("fsize_local",                     1200284431), # 1.20GB, avg file size 1.20GB
  ("fsize_db",                        19359006495), # 19.36GB, avg file size 967.95MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_280_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2tau_M-300_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_300_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_300_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    33),
  ("nof_events",                      {
    'Count'                                                      : [        40000, ],
    'CountWeighted'                                              : [        39995,        39996,        39997, ],
    'CountWeightedLHEWeightScale'                                : [        41097,        39995,        38736,        41097,        39995,        38736,        41097,        39995,        38736, ],
    'CountWeightedL1PrefireNom'                                  : [        39100,        39100,        39103, ],
    'CountWeightedL1Prefire'                                     : [        39100,        38876,        39316, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        40171,        39100,        37875,        40171,        39100,        37875,        40171,        39100,        37875, ],
  }),
  ("nof_tree_events",                 40000),
  ("nof_db_events",                   981549),
  ("fsize_local",                     129383848), # 129.38MB, avg file size 129.38MB
  ("fsize_db",                        50466696906), # 50.47GB, avg file size 1.53GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_300_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2Tau_M-350_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_350_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_350_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       300007,       299984,       300004, ],
    'CountWeightedLHEWeightScale'                                : [       312006,       300007,       287645,       312006,       300007,       287645,       312006,       300007,       287645, ],
    'CountWeightedL1PrefireNom'                                  : [       291985,       291967,       291984, ],
    'CountWeightedL1Prefire'                                     : [       291985,       290052,       293879, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       303603,       291985,       280010,       303603,       291985,       280010,       303603,       291985,       280010, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1023160418), # 1.02GB, avg file size 1.02GB
  ("fsize_db",                        15849336173), # 15.85GB, avg file size 2.26GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_350_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2Tau_M-400_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_400_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_400_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       299926,       299960,       299987, ],
    'CountWeightedLHEWeightScale'                                : [       315132,       299926,       285254,       315132,       299926,       285254,       315132,       299926,       285254, ],
    'CountWeightedL1PrefireNom'                                  : [       291312,       291324,       291358, ],
    'CountWeightedL1Prefire'                                     : [       291312,       289277,       293320, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       305983,       291312,       277109,       305983,       291312,       277109,       305983,       291312,       277109, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1067911254), # 1.07GB, avg file size 1.07GB
  ("fsize_db",                        16220410321), # 16.22GB, avg file size 1.08GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_400_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2Tau_M-450_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_450_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_450_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       299992,       299950,       299950, ],
    'CountWeightedLHEWeightScale'                                : [       317772,       299992,       283219,       317772,       299992,       283219,       317772,       299992,       283219, ],
    'CountWeightedL1PrefireNom'                                  : [       291008,       290959,       290999, ],
    'CountWeightedL1Prefire'                                     : [       291008,       288907,       293077, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       308184,       291008,       274810,       308184,       291008,       274810,       308184,       291008,       274810, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1106689268), # 1.11GB, avg file size 1.11GB
  ("fsize_db",                        16455015197), # 16.46GB, avg file size 1.03GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_450_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2Tau_M-500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_500_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_500_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       200002,       199984,       199951, ],
    'CountWeightedLHEWeightScale'                                : [       213369,       200002,       187635,       213369,       200002,       187635,       213369,       200002,       187635, ],
    'CountWeightedL1PrefireNom'                                  : [       193804,       193789,       193779, ],
    'CountWeightedL1Prefire'                                     : [       193804,       192372,       195216, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       206712,       193804,       181871,       206712,       193804,       181871,       206712,       193804,       181871, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     761500486), # 761.50MB, avg file size 761.50MB
  ("fsize_db",                        11098842678), # 11.10GB, avg file size 1.39GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2Tau_M-550_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_550_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_550_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                      : [       192000, ],
    'CountWeighted'                                              : [       191978,       191998,       191975, ],
    'CountWeightedLHEWeightScale'                                : [       206148,       191978,       179138,       206148,       191978,       179138,       206148,       191978,       179138, ],
    'CountWeightedL1PrefireNom'                                  : [       186069,       186074,       186080, ],
    'CountWeightedL1Prefire'                                     : [       186069,       184707,       187412, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       199749,       186069,       173662,       199749,       186069,       173662,       199749,       186069,       173662, ],
  }),
  ("nof_tree_events",                 192000),
  ("nof_db_events",                   192000),
  ("fsize_local",                     751440904), # 751.44MB, avg file size 751.44MB
  ("fsize_db",                        10855478264), # 10.86GB, avg file size 775.39MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_550_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2Tau_M-600_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_600_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_600_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199998,       199999,       199969, ],
    'CountWeightedLHEWeightScale'                                : [       215960,       199998,       185683,       215960,       199998,       185683,       215960,       199998,       185683, ],
    'CountWeightedL1PrefireNom'                                  : [       193878,       193869,       193875, ],
    'CountWeightedL1Prefire'                                     : [       193878,       192469,       195266, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       209300,       193878,       180040,       209300,       193878,       180040,       209300,       193878,       180040, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     799079966), # 799.08MB, avg file size 799.08MB
  ("fsize_db",                        11487024358), # 11.49GB, avg file size 675.71MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_600_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2Tau_M-650_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_650_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_650_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                      : [       188000, ],
    'CountWeighted'                                              : [       187974,       187960,       187970, ],
    'CountWeightedLHEWeightScale'                                : [       204001,       187973,       173747,       204001,       187973,       173747,       204001,       187973,       173747, ],
    'CountWeightedL1PrefireNom'                                  : [       182149,       182129,       182161, ],
    'CountWeightedL1Prefire'                                     : [       182149,       180814,       183466, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       197632,       182147,       168395,       197632,       182147,       168395,       197632,       182147,       168395, ],
  }),
  ("nof_tree_events",                 188000),
  ("nof_db_events",                   188000),
  ("fsize_local",                     764224082), # 764.22MB, avg file size 764.22MB
  ("fsize_db",                        10754684541), # 10.75GB, avg file size 768.19MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_650_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2Tau_M-750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_750_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_750_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199984,       199981,       199952, ],
    'CountWeightedLHEWeightScale'                                : [       218959,       199982,       183379,       218959,       199982,       183379,       218959,       199982,       183379, ],
    'CountWeightedL1PrefireNom'                                  : [       193809,       193791,       193804, ],
    'CountWeightedL1Prefire'                                     : [       193809,       192400,       195199, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       212155,       193807,       177751,       212155,       193807,       177751,       212155,       193807,       177751, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     833099050), # 833.10MB, avg file size 833.10MB
  ("fsize_db",                        11547164401), # 11.55GB, avg file size 888.24MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2Tau_M-800_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_800_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_800_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                      : [       192000, ],
    'CountWeighted'                                              : [       191956,       191945,       191972, ],
    'CountWeightedLHEWeightScale'                                : [       210982,       191956,       175452,       210982,       191956,       175452,       210982,       191956,       175452, ],
    'CountWeightedL1PrefireNom'                                  : [       186175,       186158,       186192, ],
    'CountWeightedL1Prefire'                                     : [       186175,       184856,       187479, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       204586,       186175,       170193,       204586,       186175,       170193,       204586,       186175,       170193, ],
  }),
  ("nof_tree_events",                 192000),
  ("nof_db_events",                   192000),
  ("fsize_local",                     806716952), # 806.72MB, avg file size 806.72MB
  ("fsize_db",                        11179122535), # 11.18GB, avg file size 1.02GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_800_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       369000, ],
    'CountWeighted'                                              : [       365800,       365894,       365880, ],
    'CountWeightedL1PrefireNom'                                  : [       344775,       344772,       344848, ],
    'CountWeightedL1Prefire'                                     : [       344775,       339838,       349657, ],
  }),
  ("nof_tree_events",                 369000),
  ("nof_db_events",                   369000),
  ("fsize_local",                     1356426779), # 1.36GB, avg file size 1.36GB
  ("fsize_db",                        20317409524), # 20.32GB, avg file size 781.44MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_0_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       297139,       297153,       297192, ],
    'CountWeightedL1PrefireNom'                                  : [       277516,       277506,       277540, ],
    'CountWeightedL1Prefire'                                     : [       277516,       272964,       282033, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1108209353), # 1.11GB, avg file size 1.11GB
  ("fsize_db",                        16551491719), # 16.55GB, avg file size 827.57MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_1_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       400000, ],
    'CountWeighted'                                              : [       396242,       396300,       396267, ],
    'CountWeightedL1PrefireNom'                                  : [       363531,       363512,       363578, ],
    'CountWeightedL1Prefire'                                     : [       363531,       356197,       370859, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1551721390), # 1.55GB, avg file size 1.55GB
  ("fsize_db",                        22555887148), # 22.56GB, avg file size 2.51GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_2_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
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
    'Count'                                                      : [       400000, ],
    'CountWeighted'                                              : [       392905,       392917,       392980, ],
    'CountWeightedL1PrefireNom'                                  : [       364734,       364695,       364803, ],
    'CountWeightedL1Prefire'                                     : [       364734,       358513,       370966, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1711785514), # 1.71GB, avg file size 1.71GB
  ("fsize_db",                        23834632407), # 23.83GB, avg file size 993.11MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_2_1_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFHHTo2B2Tau_CV_1_5_C2V_1_C3_1_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1p5_1_1_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1p5_1_1_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                      : [       392000, ],
    'CountWeighted'                                              : [       386922,       387034,       386937, ],
    'CountWeightedL1PrefireNom'                                  : [       361216,       361241,       361248, ],
    'CountWeightedL1Prefire'                                     : [       361216,       355369,       367040, ],
  }),
  ("nof_tree_events",                 392000),
  ("nof_db_events",                   392000),
  ("fsize_local",                     1555673155), # 1.56GB, avg file size 1.56GB
  ("fsize_db",                        22237635973), # 22.24GB, avg file size 1.39GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1p5_1_1_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2Tau_node_SM_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_sm_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                      : [       380000, ],
    'CountWeighted'                                              : [       380005,       379962,       380039, ],
    'CountWeightedLHEWeightScale'                                : [       486390,       459104,       433467,       402655,       380003,       358695,       339105,       319932,       301971, ],
    'CountWeightedL1PrefireNom'                                  : [       367952,       367906,       367987, ],
    'CountWeightedL1Prefire'                                     : [       367952,       365108,       370746, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       470847,       444579,       419883,       389768,       367949,       347435,       328236,       309786,       292481, ],
  }),
  ("nof_tree_events",                 380000),
  ("nof_db_events",                   380000),
  ("fsize_local",                     1382403221), # 1.38GB, avg file size 1.38GB
  ("fsize_db",                        20440095707), # 20.44GB, avg file size 1.14GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_sm_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2Tau_node_2_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_2_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                      : [       392000, ],
    'CountWeighted'                                              : [       392000,       391922,       391981, ],
    'CountWeightedLHEWeightScale'                                : [       509246,       469269,       434113,       425550,       392000,       362403,       361237,       332538,       307370, ],
    'CountWeightedL1PrefireNom'                                  : [       377804,       377736,       377805, ],
    'CountWeightedL1Prefire'                                     : [       377804,       374542,       381018, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       490647,       452347,       418639,       409966,       377804,       349450,       347976,       320488,       296357, ],
  }),
  ("nof_tree_events",                 392000),
  ("nof_db_events",                   392000),
  ("fsize_local",                     1534351331), # 1.53GB, avg file size 1.53GB
  ("fsize_db",                        22130629455), # 22.13GB, avg file size 1.58GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_2_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2Tau_node_3_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_3_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                      : [       396000, ],
    'CountWeighted'                                              : [       396011,       395854,       396019, ],
    'CountWeightedLHEWeightScale'                                : [       506923,       478366,       451560,       419680,       396003,       373716,       353457,       333432,       314657, ],
    'CountWeightedL1PrefireNom'                                  : [       383324,       383203,       383347, ],
    'CountWeightedL1Prefire'                                     : [       383324,       380331,       386257, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       490559,       463075,       437248,       406115,       383318,       361858,       342021,       322750,       304662, ],
  }),
  ("nof_tree_events",                 396000),
  ("nof_db_events",                   396000),
  ("fsize_local",                     1446379624), # 1.45GB, avg file size 1.45GB
  ("fsize_db",                        21371438091), # 21.37GB, avg file size 971.43MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_3_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2Tau_node_4_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_4_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                      : [       400000, ],
    'CountWeighted'                                              : [       399990,       399952,       399974, ],
    'CountWeightedLHEWeightScale'                                : [       510036,       484402,       459732,       421208,       399990,       379554,       354002,       336103,       318934, ],
    'CountWeightedL1PrefireNom'                                  : [       387769,       387734,       387767, ],
    'CountWeightedL1Prefire'                                     : [       387769,       384859,       390615, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       494330,       469627,       445826,       408222,       387769,       368062,       343078,       325834,       309266, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1426246102), # 1.43GB, avg file size 1.43GB
  ("fsize_db",                        21451946375), # 21.45GB, avg file size 1.02GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_4_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2Tau_node_7_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_7_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                      : [       376000, ],
    'CountWeighted'                                              : [       375979,       375921,       376006, ],
    'CountWeightedLHEWeightScale'                                : [       479495,       455283,       432003,       396004,       375979,       356709,       332838,       315959,       299750, ],
    'CountWeightedL1PrefireNom'                                  : [       364480,       364428,       364509, ],
    'CountWeightedL1Prefire'                                     : [       364480,       361744,       367161, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       464718,       441380,       418918,       383790,       364480,       345894,       322564,       306293,       290656, ],
  }),
  ("nof_tree_events",                 376000),
  ("nof_db_events",                   376000),
  ("fsize_local",                     1341288876), # 1.34GB, avg file size 1.34GB
  ("fsize_db",                        20190349511), # 20.19GB, avg file size 1.26GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_7_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2Tau_node_9_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_9_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                      : [       400000, ],
    'CountWeighted'                                              : [       399981,       399864,       399967, ],
    'CountWeightedLHEWeightScale'                                : [       519421,       478877,       443039,       433940,       399981,       369934,       368229,       339294,       313779, ],
    'CountWeightedL1PrefireNom'                                  : [       385405,       385304,       385421, ],
    'CountWeightedL1Prefire'                                     : [       385405,       382052,       388719, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       500358,       461461,       427065,       417991,       385405,       356577,       354678,       326927,       302436, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1577174770), # 1.58GB, avg file size 1.58GB
  ("fsize_db",                        22924430937), # 22.92GB, avg file size 1.27GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_9_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2Tau_node_12_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_12_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                      : [       400000, ],
    'CountWeighted'                                              : [       399989,       400042,       399952, ],
    'CountWeightedLHEWeightScale'                                : [       509963,       484459,       459890,       421090,       399989,       379656,       353864,       336081,       318979, ],
    'CountWeightedL1PrefireNom'                                  : [       387785,       387792,       387776, ],
    'CountWeightedL1Prefire'                                     : [       387785,       384879,       390626, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       494284,       469697,       445988,       408130,       387783,       368169,       342963,       325823,       309322, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1424016568), # 1.42GB, avg file size 1.42GB
  ("fsize_db",                        21176117597), # 21.18GB, avg file size 2.12GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_12_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["sum_events"] = [
  [ 'signal_ggf_nonresonant_node_sm_hh_2b2v',          'signal_ggf_nonresonant_node_2_hh_2b2v',           'signal_ggf_nonresonant_node_3_hh_2b2v',           'signal_ggf_nonresonant_node_7_hh_2b2v',           'signal_ggf_nonresonant_node_9_hh_2b2v',           'signal_ggf_nonresonant_node_12_hh_2b2v',           ],
  [ 'signal_ggf_nonresonant_node_sm_hh_2b2t',          'signal_ggf_nonresonant_node_2_hh_2b2t',           'signal_ggf_nonresonant_node_3_hh_2b2t',           'signal_ggf_nonresonant_node_4_hh_2b2t',           'signal_ggf_nonresonant_node_7_hh_2b2t',           'signal_ggf_nonresonant_node_9_hh_2b2t',           'signal_ggf_nonresonant_node_12_hh_2b2t',           ],
]

