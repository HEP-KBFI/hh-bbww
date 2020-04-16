from collections import OrderedDict as OD

# file generated at 2020-04-15 14:22:09 with the following command:
# create_dictionary.py -m python/samples/metaDict_2017_hh.py -p /hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples -N samples_2017 -E 2017 -o python/samples -g hhAnalyzeSamples_2017_hh.py -M

samples_2017 = OD()
samples_2017["/VBFToRadionToHHTo2B2VTo2L2Nu_M-300_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_300_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_spin0_300_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [       279999, ],
    'CountWeighted'                                                                  : [       279966,       279957,       279952, ],
    'CountWeightedLHEEnvelope'                                                       : [       279966,       279966, ],
    'CountWeightedL1PrefireNom'                                                      : [       271088,       271075,       271091, ],
    'CountWeightedL1Prefire'                                                         : [       271088,       268963,       273162, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       271088,       271088, ],
  }),
  ("nof_tree_events",                 279999),
  ("nof_db_events",                   279999),
  ("fsize_local",                     1542355298), # 1.54GB, avg file size 1.54GB
  ("fsize_db",                        18070036516), # 18.07GB, avg file size 1.29GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_300_hh_2b2v"),
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
    'Count'                                                                          : [       285000, ],
    'CountWeighted'                                                                  : [       284952,       284993,       285008, ],
    'CountWeightedLHEEnvelope'                                                       : [       284952,       284952, ],
    'CountWeightedL1PrefireNom'                                                      : [       275532,       275548,       275570, ],
    'CountWeightedL1Prefire'                                                         : [       275532,       273285,       277729, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       275532,       275532, ],
  }),
  ("nof_tree_events",                 285000),
  ("nof_db_events",                   285000),
  ("fsize_local",                     1642759596), # 1.64GB, avg file size 1.64GB
  ("fsize_db",                        18927275912), # 18.93GB, avg file size 996.17MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_350_hh_2b2v"),
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
    'Count'                                                                          : [       100000, ],
    'CountWeighted'                                                                  : [        99987,        99954,        99965, ],
    'CountWeightedLHEEnvelope'                                                       : [        99987,        99987, ],
    'CountWeightedL1PrefireNom'                                                      : [        96485,        96461,        96473, ],
    'CountWeightedL1Prefire'                                                         : [        96485,        95659,        97293, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [        96485,        96485, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     597362467), # 597.36MB, avg file size 597.36MB
  ("fsize_db",                        6827583120), # 6.83GB, avg file size 682.76MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_400_hh_2b2v"),
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
    'Count'                                                                          : [       100000, ],
    'CountWeighted'                                                                  : [        99975,        99989,        99968, ],
    'CountWeightedLHEEnvelope'                                                       : [        99975,        99975, ],
    'CountWeightedL1PrefireNom'                                                      : [        95941,        95946,        95939, ],
    'CountWeightedL1Prefire'                                                         : [        95941,        95012,        96859, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [        95941,        95941, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     672658348), # 672.66MB, avg file size 672.66MB
  ("fsize_db",                        7423075893), # 7.42GB, avg file size 571.01MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_750_hh_2b2v"),
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
    'Count'                                                                          : [       399998, ],
    'CountWeighted'                                                                  : [       399935,       399980,       399905, ],
    'CountWeightedLHEEnvelope'                                                       : [       399935,       399935, ],
    'CountWeightedL1PrefireNom'                                                      : [       392877,       392882,       392868, ],
    'CountWeightedL1Prefire'                                                         : [       392877,       391022,       394642, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       392877,       392877, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     1393068280), # 1.39GB, avg file size 1.39GB
  ("fsize_db",                        20842533885), # 20.84GB, avg file size 1.49GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_250_hh_2b2v"),
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
    'Count'                                                                          : [       400000, ],
    'CountWeighted'                                                                  : [       400019,       399949,       400035, ],
    'CountWeightedLHEWeightScale'                                                    : [       406265,       399994,       391182,       406265,       399994,       391182,       406265,       399994,       391182, ],
    'CountWeightedLHEEnvelope'                                                       : [       406265,       391182, ],
    'CountWeightedL1PrefireNom'                                                      : [       392487,       392430,       392499, ],
    'CountWeightedL1Prefire'                                                         : [       392487,       390536,       394350, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       398575,       392468,       383856,       398575,       392468,       383856,       398575,       392468,       383856, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       398575,       383856, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1403651445), # 1.40GB, avg file size 1.40GB
  ("fsize_db",                        20086379241), # 20.09GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_260_hh_2b2v"),
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
    'Count'                                                                          : [       388000, ],
    'CountWeighted'                                                                  : [       387938,       387981,       388042, ],
    'CountWeightedLHEWeightScale'                                                    : [       395280,       387938,       378437,       395280,       387938,       378437,       395280,       387938,       378437, ],
    'CountWeightedLHEEnvelope'                                                       : [       395280,       378437, ],
    'CountWeightedL1PrefireNom'                                                      : [       380324,       380343,       380400, ],
    'CountWeightedL1Prefire'                                                         : [       380324,       378365,       382204, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       387468,       380324,       371034,       387468,       380324,       371034,       387468,       380324,       371034, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       387468,       371034, ],
  }),
  ("nof_tree_events",                 388000),
  ("nof_db_events",                   388000),
  ("fsize_local",                     1383507283), # 1.38GB, avg file size 1.38GB
  ("fsize_db",                        19501546911), # 19.50GB, avg file size 1.03GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_270_hh_2b2v"),
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
    'Count'                                                                          : [       384000, ],
    'CountWeighted'                                                                  : [       383961,       383999,       384009, ],
    'CountWeightedLHEEnvelope'                                                       : [       383961,       383961, ],
    'CountWeightedL1PrefireNom'                                                      : [       376110,       376120,       376153, ],
    'CountWeightedL1Prefire'                                                         : [       376110,       374101,       378036, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       376110,       376110, ],
  }),
  ("nof_tree_events",                 384000),
  ("nof_db_events",                   384000),
  ("fsize_local",                     1396375457), # 1.40GB, avg file size 1.40GB
  ("fsize_db",                        20165336883), # 20.17GB, avg file size 1.44GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_280_hh_2b2v"),
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
    'Count'                                                                          : [       299996, ],
    'CountWeighted'                                                                  : [       299979,       299953,       300001, ],
    'CountWeightedLHEWeightScale'                                                    : [       309821,       299979,       289309,       309821,       299979,       289309,       309821,       299979,       289309, ],
    'CountWeightedLHEEnvelope'                                                       : [       309821,       289309, ],
    'CountWeightedL1PrefireNom'                                                      : [       293003,       292966,       293031, ],
    'CountWeightedL1Prefire'                                                         : [       293003,       291267,       294687, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       302568,       293003,       282615,       302568,       293003,       282615,       302568,       293003,       282615, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       302568,       282615, ],
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     1141656518), # 1.14GB, avg file size 1.14GB
  ("fsize_db",                        15538010606), # 15.54GB, avg file size 776.90MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_320_hh_2b2v"),
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
    'Count'                                                                          : [       300000, ],
    'CountWeighted'                                                                  : [       299964,       299940,       299938, ],
    'CountWeightedLHEWeightScale'                                                    : [       312013,       299964,       287641,       312013,       299964,       287641,       312013,       299964,       287641, ],
    'CountWeightedLHEEnvelope'                                                       : [       312013,       287641, ],
    'CountWeightedL1PrefireNom'                                                      : [       292297,       292277,       292284, ],
    'CountWeightedL1Prefire'                                                         : [       292297,       290420,       294126, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       303972,       292297,       280326,       303972,       292297,       280326,       303972,       292297,       280326, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       303972,       280326, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1178826708), # 1.18GB, avg file size 1.18GB
  ("fsize_db",                        15654716885), # 15.65GB, avg file size 1.30GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_350_hh_2b2v"),
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
    'Count'                                                                          : [       292000, ],
    'CountWeighted'                                                                  : [       292013,       291998,       291916, ],
    'CountWeightedLHEWeightScale'                                                    : [       306718,       292013,       277666,       306718,       292013,       277666,       306718,       292013,       277666, ],
    'CountWeightedLHEEnvelope'                                                       : [       306718,       277666, ],
    'CountWeightedL1PrefireNom'                                                      : [       283788,       283772,       283731, ],
    'CountWeightedL1Prefire'                                                         : [       283788,       281813,       285718, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       298033,       283788,       269897,       298033,       283788,       269897,       298033,       283788,       269897, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       298033,       269897, ],
  }),
  ("nof_tree_events",                 292000),
  ("nof_db_events",                   292000),
  ("fsize_local",                     1202876535), # 1.20GB, avg file size 1.20GB
  ("fsize_db",                        15536600053), # 15.54GB, avg file size 971.04MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_400_hh_2b2v"),
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
    'Count'                                                                          : [       299999, ],
    'CountWeighted'                                                                  : [       299934,       299939,       299943, ],
    'CountWeightedLHEWeightScale'                                                    : [       317770,       299934,       283225,       317770,       299934,       283225,       317770,       299934,       283225, ],
    'CountWeightedLHEEnvelope'                                                       : [       317770,       283225, ],
    'CountWeightedL1PrefireNom'                                                      : [       290855,       290842,       290873, ],
    'CountWeightedL1Prefire'                                                         : [       290855,       288702,       292966, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       308073,       290855,       274692,       308073,       290855,       274692,       308073,       290855,       274692, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       308073,       274692, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1283200553), # 1.28GB, avg file size 1.28GB
  ("fsize_db",                        16296871303), # 16.30GB, avg file size 814.84MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_450_hh_2b2v"),
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
    'Count'                                                                          : [       200000, ],
    'CountWeighted'                                                                  : [       200008,       200006,       199959, ],
    'CountWeightedLHEWeightScale'                                                    : [       213378,       200008,       187623,       213378,       200008,       187623,       213378,       200008,       187623, ],
    'CountWeightedLHEEnvelope'                                                       : [       213378,       187623, ],
    'CountWeightedL1PrefireNom'                                                      : [       193663,       193647,       193654, ],
    'CountWeightedL1Prefire'                                                         : [       193663,       192177,       195127, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       206580,       193663,       181721,       206580,       193663,       181721,       206580,       193663,       181721, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       206580,       181721, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     881837195), # 881.84MB, avg file size 881.84MB
  ("fsize_db",                        10964750047), # 10.96GB, avg file size 913.73MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_500_hh_2b2v"),
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
    'Count'                                                                          : [       199998, ],
    'CountWeighted'                                                                  : [       199989,       199981,       199981, ],
    'CountWeightedLHEWeightScale'                                                    : [       215943,       199989,       185665,       215943,       199989,       185665,       215943,       199989,       185665, ],
    'CountWeightedLHEEnvelope'                                                       : [       215943,       185665, ],
    'CountWeightedL1PrefireNom'                                                      : [       192977,       192970,       192964, ],
    'CountWeightedL1Prefire'                                                         : [       192977,       191358,       194581, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       208331,       192977,       179194,       208331,       192977,       179194,       208331,       192977,       179194, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       208331,       179194, ],
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     927233398), # 927.23MB, avg file size 927.23MB
  ("fsize_db",                        11169462986), # 11.17GB, avg file size 1.24GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_600_hh_2b2v"),
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
    'Count'                                                                          : [       200000, ],
    'CountWeighted'                                                                  : [       199940,       199980,       199955, ],
    'CountWeightedLHEWeightScale'                                                    : [       217043,       199940,       184822,       217043,       199940,       184822,       217043,       199940,       184822, ],
    'CountWeightedLHEEnvelope'                                                       : [       217043,       184822, ],
    'CountWeightedL1PrefireNom'                                                      : [       192823,       192822,       192862, ],
    'CountWeightedL1Prefire'                                                         : [       192823,       191178,       194447, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       209263,       192823,       178267,       209263,       192823,       178267,       209263,       192823,       178267, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       209263,       178267, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     942915017), # 942.92MB, avg file size 942.92MB
  ("fsize_db",                        11395262580), # 11.40GB, avg file size 949.61MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_650_hh_2b2v"),
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
    'Count'                                                                          : [       199998, ],
    'CountWeighted'                                                                  : [       199996,       199963,       199971, ],
    'CountWeightedLHEWeightScale'                                                    : [       218047,       199995,       184041,       218047,       199995,       184041,       218047,       199995,       184041, ],
    'CountWeightedLHEEnvelope'                                                       : [       218047,       184041, ],
    'CountWeightedL1PrefireNom'                                                      : [       192656,       192645,       192634, ],
    'CountWeightedL1Prefire'                                                         : [       192656,       190971,       194319, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       210006,       192656,       177335,       210006,       192656,       177335,       210006,       192656,       177335, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       210006,       177335, ],
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     954533681), # 954.53MB, avg file size 954.53MB
  ("fsize_db",                        11438629863), # 11.44GB, avg file size 1.43GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_700_hh_2b2v"),
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
    'Count'                                                                          : [       200000, ],
    'CountWeighted'                                                                  : [       200016,       200001,       199923, ],
    'CountWeightedLHEEnvelope'                                                       : [       200016,       200016, ],
    'CountWeightedL1PrefireNom'                                                      : [       192575,       192550,       192534, ],
    'CountWeightedL1Prefire'                                                         : [       192575,       190871,       194257, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       192575,       192575, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     969801833), # 969.80MB, avg file size 969.80MB
  ("fsize_db",                        11931037531), # 11.93GB, avg file size 1.08GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_750_hh_2b2v"),
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
    'Count'                                                                          : [       197000, ],
    'CountWeighted'                                                                  : [       197020,       196971,       196973, ],
    'CountWeightedLHEEnvelope'                                                       : [       197020,       197020, ],
    'CountWeightedL1PrefireNom'                                                      : [       189485,       189442,       189464, ],
    'CountWeightedL1Prefire'                                                         : [       189485,       187769,       191180, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       189485,       189485, ],
  }),
  ("nof_tree_events",                 197000),
  ("nof_db_events",                   197000),
  ("fsize_local",                     964094143), # 964.09MB, avg file size 964.09MB
  ("fsize_db",                        11877663068), # 11.88GB, avg file size 791.84MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_800_hh_2b2v"),
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
    'Count'                                                                          : [       199999, ],
    'CountWeighted'                                                                  : [       199946,       199952,       199972, ],
    'CountWeightedLHEEnvelope'                                                       : [       199946,       199946, ],
    'CountWeightedL1PrefireNom'                                                      : [       192203,       192189,       192235, ],
    'CountWeightedL1Prefire'                                                         : [       192203,       190441,       193951, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       192203,       192203, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     985929109), # 985.93MB, avg file size 985.93MB
  ("fsize_db",                        12127308050), # 12.13GB, avg file size 808.49MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_850_hh_2b2v"),
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
    'Count'                                                                          : [       100000, ],
    'CountWeighted'                                                                  : [        99978,        99995,        99942, ],
    'CountWeightedLHEWeightScale'                                                    : [       110667,        99978,        90811,       110667,        99978,        90811,       110667,        99978,        90811, ],
    'CountWeightedLHEEnvelope'                                                       : [       110667,        90811, ],
    'CountWeightedL1PrefireNom'                                                      : [        96039,        96047,        96021, ],
    'CountWeightedL1Prefire'                                                         : [        96039,        95148,        96923, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       106281,        96039,        87251,       106281,        96039,        87251,       106281,        96039,        87251, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       106281,        87251, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     493482159), # 493.48MB, avg file size 493.48MB
  ("fsize_db",                        5935911198), # 5.94GB, avg file size 539.63MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_900_hh_2b2v"),
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
    'Count'                                                                          : [       100000, ],
    'CountWeighted'                                                                  : [        99965,        99969,        99961, ],
    'CountWeightedLHEWeightScale'                                                    : [       111333,        99963,        90330,       111333,        99963,        90330,       111333,        99963,        90330, ],
    'CountWeightedLHEEnvelope'                                                       : [       111334,        90329, ],
    'CountWeightedL1PrefireNom'                                                      : [        95947,        95940,        95956, ],
    'CountWeightedL1Prefire'                                                         : [        95947,        95039,        96846, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       106832,        95946,        86712,       106832,        95946,        86712,       106832,        95946,        86712, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       106833,        86712, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     499211970), # 499.21MB, avg file size 499.21MB
  ("fsize_db",                        5930718483), # 5.93GB, avg file size 847.25MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1000_hh_2b2v"),
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
    'Count'                                                                          : [       100000, ],
    'CountWeighted'                                                                  : [        99979,        99986,        99962, ],
    'CountWeightedLHEEnvelope'                                                       : [        99979,        99979, ],
    'CountWeightedL1PrefireNom'                                                      : [        95853,        95848,        95849, ],
    'CountWeightedL1Prefire'                                                         : [        95853,        94930,        96770, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [        95853,        95853, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     510651963), # 510.65MB, avg file size 510.65MB
  ("fsize_db",                        6224151597), # 6.22GB, avg file size 778.02MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1250_hh_2b2v"),
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
    'Count'                                                                          : [        99998, ],
    'CountWeighted'                                                                  : [        99963,        99953,        99949, ],
    'CountWeightedLHEWeightScale'                                                    : [       113887,        99962,        88509,       113887,        99962,        88509,       113887,        99962,        88509, ],
    'CountWeightedLHEEnvelope'                                                       : [       113887,        88508, ],
    'CountWeightedL1PrefireNom'                                                      : [        95735,        95723,        95733, ],
    'CountWeightedL1Prefire'                                                         : [        95735,        94796,        96668, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       109058,        95734,        84783,       109058,        95734,        84783,       109058,        95734,        84783, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       109058,        84782, ],
  }),
  ("nof_tree_events",                 99998),
  ("nof_db_events",                   99998),
  ("fsize_local",                     508711053), # 508.71MB, avg file size 508.71MB
  ("fsize_db",                        6171310375), # 6.17GB, avg file size 514.28MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1500_hh_2b2v"),
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
    'Count'                                                                          : [       100000, ],
    'CountWeighted'                                                                  : [        99974,        99938,        99965, ],
    'CountWeightedLHEEnvelope'                                                       : [        99974,        99974, ],
    'CountWeightedL1PrefireNom'                                                      : [        95609,        95589,        95592, ],
    'CountWeightedL1Prefire'                                                         : [        95609,        94644,        96567, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [        95609,        95609, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     513819685), # 513.82MB, avg file size 513.82MB
  ("fsize_db",                        6356319473), # 6.36GB, avg file size 635.63MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1750_hh_2b2v"),
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
    'Count'                                                                          : [       100000, ],
    'CountWeighted'                                                                  : [        99926,        99919,        99947, ],
    'CountWeightedLHEWeightScale'                                                    : [       115690,        99925,        87204,       115690,        99925,        87204,       115690,        99925,        87204, ],
    'CountWeightedLHEEnvelope'                                                       : [       115698,        87198, ],
    'CountWeightedL1PrefireNom'                                                      : [        95545,        95531,        95562, ],
    'CountWeightedL1Prefire'                                                         : [        95545,        94578,        96508, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       110603,        95544,        83388,       110603,        95544,        83388,       110603,        95544,        83388, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       110611,        83383, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     514063142), # 514.06MB, avg file size 514.06MB
  ("fsize_db",                        6172348486), # 6.17GB, avg file size 771.54MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_2000_hh_2b2v"),
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
    'Count'                                                                          : [        97000, ],
    'CountWeighted'                                                                  : [        96874,        96884,        96862, ],
    'CountWeightedLHEEnvelope'                                                       : [        96874,        96874, ],
    'CountWeightedL1PrefireNom'                                                      : [        92494,        92487,        92506, ],
    'CountWeightedL1Prefire'                                                         : [        92494,        91537,        93452, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [        92494,        92494, ],
  }),
  ("nof_tree_events",                 97000),
  ("nof_db_events",                   97000),
  ("fsize_local",                     504894131), # 504.89MB, avg file size 504.89MB
  ("fsize_db",                        6425534542), # 6.43GB, avg file size 494.27MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_2500_hh_2b2v"),
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
    'Count'                                                                          : [        97999, ],
    'CountWeighted'                                                                  : [        97755,        97737,        97747, ],
    'CountWeightedLHEEnvelope'                                                       : [        97755,        97755, ],
    'CountWeightedL1PrefireNom'                                                      : [        93312,        93294,        93315, ],
    'CountWeightedL1Prefire'                                                         : [        93312,        92346,        94278, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [        93312,        93312, ],
  }),
  ("nof_tree_events",                 97999),
  ("nof_db_events",                   97999),
  ("fsize_local",                     513003671), # 513.00MB, avg file size 513.00MB
  ("fsize_db",                        6497731845), # 6.50GB, avg file size 590.70MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_3000_hh_2b2v"),
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
    'Count'                                                                          : [       399997, ],
    'CountWeighted'                                                                  : [       399935,       400016,       399956, ],
    'CountWeightedLHEWeightScale'                                                    : [       404892,       399929,       392226,       404892,       399929,       392226,       404892,       399929,       392226, ],
    'CountWeightedLHEEnvelope'                                                       : [       404892,       392226, ],
    'CountWeightedL1PrefireNom'                                                      : [       392393,       392444,       392422, ],
    'CountWeightedL1Prefire'                                                         : [       392393,       390447,       394259, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       397210,       392388,       384858,       397210,       392388,       384858,       397210,       392388,       384858, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       397210,       384858, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     1409967891), # 1.41GB, avg file size 1.41GB
  ("fsize_db",                        20041115926), # 20.04GB, avg file size 871.35MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_250_hh_2b2v"),
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
    'Count'                                                                          : [       399997, ],
    'CountWeighted'                                                                  : [       399964,       400009,       400036, ],
    'CountWeightedLHEWeightScale'                                                    : [       406237,       399963,       391183,       406237,       399963,       391183,       406237,       399963,       391183, ],
    'CountWeightedLHEEnvelope'                                                       : [       406237,       391183, ],
    'CountWeightedL1PrefireNom'                                                      : [       392111,       392118,       392186, ],
    'CountWeightedL1Prefire'                                                         : [       392111,       390089,       394044, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       398210,       392108,       383531,       398210,       392108,       383531,       398210,       392108,       383531, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       398210,       383531, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     1433311582), # 1.43GB, avg file size 1.43GB
  ("fsize_db",                        20202072552), # 20.20GB, avg file size 962.00MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_260_hh_2b2v"),
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
    'Count'                                                                          : [       400000, ],
    'CountWeighted'                                                                  : [       400051,       399949,       400006, ],
    'CountWeightedLHEWeightScale'                                                    : [       407495,       400051,       390161,       407495,       400051,       390161,       407495,       400051,       390161, ],
    'CountWeightedLHEEnvelope'                                                       : [       407495,       390161, ],
    'CountWeightedL1PrefireNom'                                                      : [       391839,       391745,       391840, ],
    'CountWeightedL1Prefire'                                                         : [       391839,       389746,       393839, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       399109,       391839,       382216,       399109,       391839,       382216,       399109,       391839,       382216, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       399109,       382216, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1458129105), # 1.46GB, avg file size 1.46GB
  ("fsize_db",                        20268702810), # 20.27GB, avg file size 921.30MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_270_hh_2b2v"),
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
    'Count'                                                                          : [       399995, ],
    'CountWeighted'                                                                  : [       400029,       399942,       399946, ],
    'CountWeightedLHEWeightScale'                                                    : [       408733,       400028,       389180,       408733,       400028,       389180,       408733,       400028,       389180, ],
    'CountWeightedLHEEnvelope'                                                       : [       408733,       389180, ],
    'CountWeightedL1PrefireNom'                                                      : [       391535,       391454,       391494, ],
    'CountWeightedL1Prefire'                                                         : [       391535,       389393,       393594, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       400015,       391533,       380977,       400015,       391533,       380977,       400015,       391533,       380977, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       400015,       380977, ],
  }),
  ("nof_tree_events",                 399995),
  ("nof_db_events",                   399995),
  ("fsize_local",                     1482716868), # 1.48GB, avg file size 1.48GB
  ("fsize_db",                        20542842010), # 20.54GB, avg file size 662.67MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_280_hh_2b2v"),
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
    'Count'                                                                          : [       399998, ],
    'CountWeighted'                                                                  : [       400014,       399966,       400007, ],
    'CountWeightedLHEWeightScale'                                                    : [       411013,       400014,       387362,       411013,       400014,       387362,       411013,       400014,       387362, ],
    'CountWeightedLHEEnvelope'                                                       : [       411013,       387362, ],
    'CountWeightedL1PrefireNom'                                                      : [       390814,       390773,       390821, ],
    'CountWeightedL1Prefire'                                                         : [       390814,       388527,       393031, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       401504,       390814,       378515,       401504,       390814,       378515,       401504,       390814,       378515, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       401504,       378515, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     1527627493), # 1.53GB, avg file size 1.53GB
  ("fsize_db",                        20998766588), # 21.00GB, avg file size 807.64MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_300_hh_2b2v"),
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
    'Count'                                                                          : [       293998, ],
    'CountWeighted'                                                                  : [       293950,       293937,       293988, ],
    'CountWeightedLHEWeightScale'                                                    : [       303633,       293950,       283520,       303633,       293950,       283520,       303633,       293950,       283520, ],
    'CountWeightedLHEEnvelope'                                                       : [       303633,       283519, ],
    'CountWeightedL1PrefireNom'                                                      : [       286900,       286879,       286937, ],
    'CountWeightedL1Prefire'                                                         : [       286900,       285170,       288586, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       296287,       286899,       276749,       296287,       286899,       276749,       296287,       286899,       276749, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       296287,       276749, ],
  }),
  ("nof_tree_events",                 293998),
  ("nof_db_events",                   293998),
  ("fsize_local",                     1153759751), # 1.15GB, avg file size 1.15GB
  ("fsize_db",                        15577989269), # 15.58GB, avg file size 916.35MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_320_hh_2b2v"),
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
    'Count'                                                                          : [       281999, ],
    'CountWeighted'                                                                  : [       281964,       281967,       281961, ],
    'CountWeightedLHEWeightScale'                                                    : [       293260,       281963,       270389,       293260,       281963,       270389,       293260,       281963,       270389, ],
    'CountWeightedLHEEnvelope'                                                       : [       293260,       270388, ],
    'CountWeightedL1PrefireNom'                                                      : [       274729,       274703,       274748, ],
    'CountWeightedL1Prefire'                                                         : [       274729,       272981,       276437, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       285668,       274728,       263486,       285668,       274728,       263486,       285668,       274728,       263486, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       285668,       263486, ],
  }),
  ("nof_tree_events",                 281999),
  ("nof_db_events",                   281999),
  ("fsize_local",                     1147413751), # 1.15GB, avg file size 1.15GB
  ("fsize_db",                        15217194365), # 15.22GB, avg file size 845.40MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_350_hh_2b2v"),
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
    'Count'                                                                          : [       298000, ],
    'CountWeighted'                                                                  : [       297937,       298017,       298003, ],
    'CountWeightedLHEWeightScale'                                                    : [       313030,       297937,       283380,       313030,       297937,       283380,       313030,       297937,       283380, ],
    'CountWeightedLHEEnvelope'                                                       : [       313031,       283380, ],
    'CountWeightedL1PrefireNom'                                                      : [       289718,       289765,       289773, ],
    'CountWeightedL1Prefire'                                                         : [       289718,       287766,       291640, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       304312,       289718,       275597,       304312,       289718,       275597,       304312,       289718,       275597, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       304313,       275597, ],
  }),
  ("nof_tree_events",                 298000),
  ("nof_db_events",                   298000),
  ("fsize_local",                     1271144466), # 1.27GB, avg file size 1.27GB
  ("fsize_db",                        16133391096), # 16.13GB, avg file size 806.67MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_400_hh_2b2v"),
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
    'Count'                                                                          : [       300000, ],
    'CountWeighted'                                                                  : [       299911,       299927,       299942, ],
    'CountWeightedLHEWeightScale'                                                    : [       317757,       299911,       283222,       317757,       299911,       283222,       317757,       299911,       283222, ],
    'CountWeightedLHEEnvelope'                                                       : [       317757,       283222, ],
    'CountWeightedL1PrefireNom'                                                      : [       291241,       291239,       291278, ],
    'CountWeightedL1Prefire'                                                         : [       291241,       289213,       293245, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       308485,       291241,       275077,       308485,       291241,       275077,       308485,       291241,       275077, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       308485,       275076, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1329758066), # 1.33GB, avg file size 1.33GB
  ("fsize_db",                        16485829471), # 16.49GB, avg file size 867.68MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_450_hh_2b2v"),
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
    'Count'                                                                          : [       200000, ],
    'CountWeighted'                                                                  : [       199968,       199967,       199975, ],
    'CountWeightedLHEWeightScale'                                                    : [       213383,       199968,       187657,       213383,       199968,       187657,       213383,       199968,       187657, ],
    'CountWeightedLHEEnvelope'                                                       : [       213383,       187657, ],
    'CountWeightedL1PrefireNom'                                                      : [       194075,       194062,       194084, ],
    'CountWeightedL1Prefire'                                                         : [       194075,       192703,       195426, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       207038,       194075,       182158,       207038,       194075,       182158,       207038,       194075,       182158, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       207038,       182158, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     917461285), # 917.46MB, avg file size 917.46MB
  ("fsize_db",                        11497248581), # 11.50GB, avg file size 547.49MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_500_hh_2b2v"),
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
    'Count'                                                                          : [       200000, ],
    'CountWeighted'                                                                  : [       199971,       199977,       199960, ],
    'CountWeightedLHEWeightScale'                                                    : [       214738,       199970,       186599,       214738,       199970,       186599,       214738,       199970,       186599, ],
    'CountWeightedLHEEnvelope'                                                       : [       214738,       186599, ],
    'CountWeightedL1PrefireNom'                                                      : [       194087,       194092,       194073, ],
    'CountWeightedL1Prefire'                                                         : [       194087,       192725,       195428, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       208364,       194086,       181141,       208364,       194086,       181141,       208364,       194086,       181141, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       208364,       181141, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     941303853), # 941.30MB, avg file size 941.30MB
  ("fsize_db",                        11543534297), # 11.54GB, avg file size 679.03MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_550_hh_2b2v"),
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
    'Count'                                                                          : [       192000, ],
    'CountWeighted'                                                                  : [       191970,       191962,       191942, ],
    'CountWeightedLHEWeightScale'                                                    : [       207287,       191970,       178226,       207287,       191970,       178226,       207287,       191970,       178226, ],
    'CountWeightedLHEEnvelope'                                                       : [       207287,       178226, ],
    'CountWeightedL1PrefireNom'                                                      : [       186268,       186262,       186254, ],
    'CountWeightedL1Prefire'                                                         : [       186268,       184954,       187566, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       201088,       186268,       172966,       201088,       186268,       172966,       201088,       186268,       172966, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       201088,       172966, ],
  }),
  ("nof_tree_events",                 192000),
  ("nof_db_events",                   192000),
  ("fsize_local",                     922032674), # 922.03MB, avg file size 922.03MB
  ("fsize_db",                        11191273021), # 11.19GB, avg file size 746.08MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_600_hh_2b2v"),
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
    'Count'                                                                          : [       200000, ],
    'CountWeighted'                                                                  : [       200017,       200006,       199949, ],
    'CountWeightedLHEWeightScale'                                                    : [       217035,       200017,       184833,       217035,       200017,       184833,       217035,       200017,       184833, ],
    'CountWeightedLHEEnvelope'                                                       : [       217035,       184833, ],
    'CountWeightedL1PrefireNom'                                                      : [       194033,       194006,       194011, ],
    'CountWeightedL1Prefire'                                                         : [       194033,       192660,       195385, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       210512,       194033,       179347,       210512,       194033,       179347,       210512,       194033,       179347, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       210512,       179347, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     974105433), # 974.11MB, avg file size 974.11MB
  ("fsize_db",                        11871616225), # 11.87GB, avg file size 539.62MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_650_hh_2b2v"),
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
    'Count'                                                                          : [       199998, ],
    'CountWeighted'                                                                  : [       199972,       199965,       199953, ],
    'CountWeightedLHEWeightScale'                                                    : [       218037,       199972,       184075,       218037,       199972,       184075,       218037,       199972,       184075, ],
    'CountWeightedLHEEnvelope'                                                       : [       218037,       184075, ],
    'CountWeightedL1PrefireNom'                                                      : [       194058,       194042,       194052, ],
    'CountWeightedL1Prefire'                                                         : [       194058,       192703,       195393, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       211544,       194058,       178659,       211544,       194058,       178659,       211544,       194058,       178659, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       211544,       178659, ],
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     982447761), # 982.45MB, avg file size 982.45MB
  ("fsize_db",                        11820942716), # 11.82GB, avg file size 656.72MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_700_hh_2b2v"),
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
    'Count'                                                                          : [       198000, ],
    'CountWeighted'                                                                  : [       197954,       197934,       197956, ],
    'CountWeightedLHEWeightScale'                                                    : [       216760,       197954,       181572,       216760,       197954,       181572,       216760,       197954,       181572, ],
    'CountWeightedLHEEnvelope'                                                       : [       216760,       181572, ],
    'CountWeightedL1PrefireNom'                                                      : [       192060,       192034,       192075, ],
    'CountWeightedL1Prefire'                                                         : [       192060,       190711,       193389, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       210256,       192060,       176182,       210256,       192060,       176182,       210256,       192060,       176182, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       210256,       176182, ],
  }),
  ("nof_tree_events",                 198000),
  ("nof_db_events",                   198000),
  ("fsize_local",                     979880511), # 979.88MB, avg file size 979.88MB
  ("fsize_db",                        11778577981), # 11.78GB, avg file size 785.24MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_750_hh_2b2v"),
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
    'Count'                                                                          : [       200000, ],
    'CountWeighted'                                                                  : [       199949,       199989,       199985, ],
    'CountWeightedLHEWeightScale'                                                    : [       219797,       199949,       182727,       219797,       199949,       182727,       219797,       199949,       182727, ],
    'CountWeightedLHEEnvelope'                                                       : [       219797,       182727, ],
    'CountWeightedL1PrefireNom'                                                      : [       194069,       194077,       194104, ],
    'CountWeightedL1Prefire'                                                         : [       194069,       192727,       195395, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       213290,       194069,       177379,       213290,       194069,       177379,       213290,       194069,       177379, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       213290,       177379, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     995548134), # 995.55MB, avg file size 995.55MB
  ("fsize_db",                        11967660431), # 11.97GB, avg file size 598.38MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_800_hh_2b2v"),
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
    'Count'                                                                          : [       200000, ],
    'CountWeighted'                                                                  : [       199954,       199962,       199948, ],
    'CountWeightedLHEEnvelope'                                                       : [       199954,       199954, ],
    'CountWeightedL1PrefireNom'                                                      : [       194010,       194009,       194008, ],
    'CountWeightedL1Prefire'                                                         : [       194010,       192655,       195344, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       194010,       194010, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1007441071), # 1.01GB, avg file size 1.01GB
  ("fsize_db",                        12348394332), # 12.35GB, avg file size 823.23MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_850_hh_2b2v"),
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
    'Count'                                                                          : [        99999, ],
    'CountWeighted'                                                                  : [        99997,       100009,        99973, ],
    'CountWeightedLHEWeightScale'                                                    : [       110561,        99997,        90970,       110561,        99997,        90970,       110561,        99997,        90970, ],
    'CountWeightedLHEEnvelope'                                                       : [       110561,        90970, ],
    'CountWeightedL1PrefireNom'                                                      : [        97143,        97146,        97134, ],
    'CountWeightedL1Prefire'                                                         : [        97143,        96492,        97785, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       107386,        97143,        88386,       107386,        97143,        88386,       107386,        97143,        88386, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       107386,        88386, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     504379029), # 504.38MB, avg file size 504.38MB
  ("fsize_db",                        6022388849), # 6.02GB, avg file size 669.15MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_900_hh_2b2v"),
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
    'Count'                                                                          : [        99999, ],
    'CountWeighted'                                                                  : [        99971,        99973,        99979, ],
    'CountWeightedLHEWeightScale'                                                    : [       111340,        99971,        90330,       111340,        99971,        90330,       111340,        99971,        90330, ],
    'CountWeightedLHEEnvelope'                                                       : [       111340,        90330, ],
    'CountWeightedL1PrefireNom'                                                      : [        97084,        97086,        97091, ],
    'CountWeightedL1Prefire'                                                         : [        97084,        96427,        97733, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       108110,        97084,        87730,       108110,        97084,        87730,       108110,        97084,        87730, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       108110,        87730, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     506790427), # 506.79MB, avg file size 506.79MB
  ("fsize_db",                        6101733672), # 6.10GB, avg file size 610.17MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_1000_hh_2b2v"),
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
    'Count'                                                                          : [       100000, ],
    'CountWeighted'                                                                  : [        99945,        99986,        99981, ],
    'CountWeightedLHEEnvelope'                                                       : [        99945,        99945, ],
    'CountWeightedL1PrefireNom'                                                      : [        97069,        97099,        97092, ],
    'CountWeightedL1Prefire'                                                         : [        97069,        96418,        97713, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [        97069,        97069, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     514808490), # 514.81MB, avg file size 514.81MB
  ("fsize_db",                        6305015701), # 6.31GB, avg file size 900.72MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_1250_hh_2b2v"),
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
    'Count'                                                                          : [       100000, ],
    'CountWeighted'                                                                  : [        99945,        99933,        99931, ],
    'CountWeightedLHEEnvelope'                                                       : [        99945,        99945, ],
    'CountWeightedL1PrefireNom'                                                      : [        97062,        97049,        97057, ],
    'CountWeightedL1Prefire'                                                         : [        97062,        96409,        97707, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [        97062,        97062, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     511759708), # 511.76MB, avg file size 511.76MB
  ("fsize_db",                        6512057209), # 6.51GB, avg file size 434.14MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_1500_hh_2b2v"),
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
    'Count'                                                                          : [        99999, ],
    'CountWeighted'                                                                  : [        99939,        99936,        99959, ],
    'CountWeightedLHEEnvelope'                                                       : [        99939,        99939, ],
    'CountWeightedL1PrefireNom'                                                      : [        97022,        97012,        97042, ],
    'CountWeightedL1Prefire'                                                         : [        97022,        96359,        97674, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [        97022,        97022, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     512368023), # 512.37MB, avg file size 512.37MB
  ("fsize_db",                        6489134095), # 6.49GB, avg file size 540.76MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_1750_hh_2b2v"),
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
    'Count'                                                                          : [       100000, ],
    'CountWeighted'                                                                  : [        99905,        99912,        99890, ],
    'CountWeightedLHEWeightScale'                                                    : [       115680,        99905,        87185,       115680,        99905,        87185,       115680,        99905,        87185, ],
    'CountWeightedLHEEnvelope'                                                       : [       115683,        87182, ],
    'CountWeightedL1PrefireNom'                                                      : [        96938,        96927,        96937, ],
    'CountWeightedL1Prefire'                                                         : [        96938,        96264,        97600, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       112243,        96938,        84593,       112243,        96938,        84593,       112243,        96938,        84593, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       112246,        84590, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     511499249), # 511.50MB, avg file size 511.50MB
  ("fsize_db",                        6328288934), # 6.33GB, avg file size 575.30MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_2000_hh_2b2v"),
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
    'Count'                                                                          : [        98000, ],
    'CountWeighted'                                                                  : [        97879,        97879,        97873, ],
    'CountWeightedLHEWeightScale'                                                    : [       114845,        97879,        84387,       114845,        97879,        84387,       114845,        97879,        84387, ],
    'CountWeightedLHEEnvelope'                                                       : [       114845,        84386, ],
    'CountWeightedL1PrefireNom'                                                      : [        94939,        94941,        94937, ],
    'CountWeightedL1Prefire'                                                         : [        94939,        94272,        95597, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       111397,        94939,        81852,       111397,        94939,        81852,       111397,        94939,        81852, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       111398,        81852, ],
  }),
  ("nof_tree_events",                 98000),
  ("nof_db_events",                   98000),
  ("fsize_local",                     505361623), # 505.36MB, avg file size 505.36MB
  ("fsize_db",                        6377937593), # 6.38GB, avg file size 490.61MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_2500_hh_2b2v"),
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
    'Count'                                                                          : [        99999, ],
    'CountWeighted'                                                                  : [        99816,        99796,        99803, ],
    'CountWeightedLHEWeightScale'                                                    : [       118531,        99813,        85118,       118531,        99813,        85118,       118531,        99813,        85118, ],
    'CountWeightedLHEEnvelope'                                                       : [       118532,        85117, ],
    'CountWeightedL1PrefireNom'                                                      : [        96842,        96829,        96835, ],
    'CountWeightedL1Prefire'                                                         : [        96842,        96164,        97510, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       115008,        96840,        82584,       115008,        96840,        82584,       115008,        96840,        82584, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       115008,        82583, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     518743389), # 518.74MB, avg file size 518.74MB
  ("fsize_db",                        6547475897), # 6.55GB, avg file size 545.62MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_3000_hh_2b2v"),
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
    'Count'                                                                          : [       399996, ],
    'CountWeighted'                                                                  : [       396340,       396381,       396247, ],
    'CountWeightedLHEEnvelope'                                                       : [       396340,       396340, ],
    'CountWeightedL1PrefireNom'                                                      : [       370950,       370920,       370958, ],
    'CountWeightedL1Prefire'                                                         : [       370950,       365058,       376795, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       370950,       370950, ],
  }),
  ("nof_tree_events",                 399996),
  ("nof_db_events",                   399996),
  ("fsize_local",                     1722789667), # 1.72GB, avg file size 1.72GB
  ("fsize_db",                        22186460848), # 22.19GB, avg file size 1.85GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_1_hh_2b2v"),
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
    'Count'                                                                          : [       388999, ],
    'CountWeighted'                                                                  : [       388918,       388934,       388956, ],
    'CountWeightedLHEWeightScale'                                                    : [       497857,       469962,       443757,       412133,       388917,       367196,       347077,       327484,       309123, ],
    'CountWeightedLHEEnvelope'                                                       : [       497857,       309122, ],
    'CountWeightedL1PrefireNom'                                                      : [       377192,       377195,       377223, ],
    'CountWeightedL1Prefire'                                                         : [       377192,       374412,       379920, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       482707,       455800,       430505,       399571,       377190,       356213,       336486,       317591,       299866, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       482707,       299866, ],
  }),
  ("nof_tree_events",                 388999),
  ("nof_db_events",                   388999),
  ("fsize_local",                     1684463228), # 1.68GB, avg file size 1.68GB
  ("fsize_db",                        21257341288), # 21.26GB, avg file size 1.25GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_sm_hh_2b2v"),
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
    'Count'                                                                          : [       400000, ],
    'CountWeighted'                                                                  : [       399921,       399896,       399913, ],
    'CountWeightedLHEWeightScale'                                                    : [       519620,       478804,       442924,       434231,       399913,       369767,       368607,       339314,       313624, ],
    'CountWeightedLHEEnvelope'                                                       : [       519620,       313624, ],
    'CountWeightedL1PrefireNom'                                                      : [       386217,       386154,       386257, ],
    'CountWeightedL1Prefire'                                                         : [       386217,       383056,       389340, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       501649,       462453,       427971,       419169,       386211,       357248,       355792,       327666,       302978, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       501649,       302977, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1863194554), # 1.86GB, avg file size 1.86GB
  ("fsize_db",                        23088598268), # 23.09GB, avg file size 1.36GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_2_hh_2b2v"),
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
    'Count'                                                                          : [       380000, ],
    'CountWeighted'                                                                  : [       379987,       379939,       379928, ],
    'CountWeightedLHEWeightScale'                                                    : [       486418,       459049,       433324,       402701,       379984,       358622,       339154,       319943,       301945, ],
    'CountWeightedLHEEnvelope'                                                       : [       486418,       301945, ],
    'CountWeightedL1PrefireNom'                                                      : [       368403,       368352,       368387, ],
    'CountWeightedL1Prefire'                                                         : [       368403,       365666,       371091, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       471483,       445078,       420248,       390319,       368400,       347787,       328713,       310190,       292811, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       471483,       292811, ],
  }),
  ("nof_tree_events",                 380000),
  ("nof_db_events",                   380000),
  ("fsize_local",                     1652581125), # 1.65GB, avg file size 1.65GB
  ("fsize_db",                        20768532098), # 20.77GB, avg file size 1.22GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_3_hh_2b2v"),
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
    'Count'                                                                          : [       392999, ],
    'CountWeighted'                                                                  : [       392988,       392955,       392950, ],
    'CountWeightedLHEWeightScale'                                                    : [       501191,       475874,       451526,       413936,       392988,       372835,       347914,       330263,       313308, ],
    'CountWeightedLHEEnvelope'                                                       : [       501191,       313308, ],
    'CountWeightedL1PrefireNom'                                                      : [       381547,       381492,       381552, ],
    'CountWeightedL1Prefire'                                                         : [       381547,       378818,       384220, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       486493,       462037,       438498,       401786,       381547,       362066,       337691,       320642,       304253, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       486493,       304253, ],
  }),
  ("nof_tree_events",                 392999),
  ("nof_db_events",                   392999),
  ("fsize_local",                     1670386242), # 1.67GB, avg file size 1.67GB
  ("fsize_db",                        21440735341), # 21.44GB, avg file size 1.13GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_7_hh_2b2v"),
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
    'Count'                                                                          : [       386999, ],
    'CountWeighted'                                                                  : [       386971,       387035,       386950, ],
    'CountWeightedLHEWeightScale'                                                    : [       502561,       463311,       428628,       419856,       386971,       357905,       356285,       328279,       303581, ],
    'CountWeightedLHEEnvelope'                                                       : [       502581,       303561, ],
    'CountWeightedL1PrefireNom'                                                      : [       373627,       373656,       373629, ],
    'CountWeightedL1Prefire'                                                         : [       373627,       370549,       376666, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       485101,       447362,       413999,       405249,       373627,       345673,       343873,       316952,       293191, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       485121,       293172, ],
  }),
  ("nof_tree_events",                 386999),
  ("nof_db_events",                   386999),
  ("fsize_local",                     1819557376), # 1.82GB, avg file size 1.82GB
  ("fsize_db",                        22534822736), # 22.53GB, avg file size 1.19GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_9_hh_2b2v"),
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
    'Count'                                                                          : [       400000, ],
    'CountWeighted'                                                                  : [       400046,       400024,       399942, ],
    'CountWeightedLHEWeightScale'                                                    : [       509929,       484450,       459890,       421060,       400046,       379661,       353841,       336073,       318991, ],
    'CountWeightedLHEEnvelope'                                                       : [       509929,       318991, ],
    'CountWeightedL1PrefireNom'                                                      : [       388458,       388426,       388425, ],
    'CountWeightedL1Prefire'                                                         : [       388458,       385696,       391168, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       495081,       470464,       446720,       408785,       388458,       368777,       343515,       326355,       309836, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       495081,       309836, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1695517111), # 1.70GB, avg file size 1.70GB
  ("fsize_db",                        21561540290), # 21.56GB, avg file size 937.46MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_12_hh_2b2v"),
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

samples_2017["/GluGluToHHTo2B2WToLNu2J_node_SM_TuneCP5_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_sm_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    30),
  ("nof_events",                      {
    'Count'                                                                          : [       779989, ],
    'CountWeighted'                                                                  : [       779847,       779874,       779932, ],
    'CountWeightedLHEWeightScale'                                                    : [       998358,       942385,       889796,       826468,       779847,       736295,       696016,       656689,       619854, ],
    'CountWeightedLHEEnvelope'                                                       : [       998358,       619854, ],
    'CountWeightedL1PrefireNom'                                                      : [       756272,       756264,       756337, ],
    'CountWeightedL1Prefire'                                                         : [       756272,       750653,       761777, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       967859,       913899,       863164,       801173,       756272,       714217,       674680,       636783,       601240, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       967859,       601240, ],
  }),
  ("nof_tree_events",                 779989),
  ("nof_db_events",                   779989),
  ("fsize_local",                     3514656195), # 3.51GB, avg file size 1.76GB
  ("fsize_db",                        43860671206), # 43.86GB, avg file size 1.46GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_sm_hh_2b2v_sl"),
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
    'Count'                                                                          : [       400000, ],
    'CountWeighted'                                                                  : [       399998,       399994,       399941, ],
    'CountWeightedLHEEnvelope'                                                       : [       399998,       399998, ],
    'CountWeightedL1PrefireNom'                                                      : [       388473,       388438,       388469, ],
    'CountWeightedL1Prefire'                                                         : [       388473,       385652,       391199, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       388473,       388473, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     2078527881), # 2.08GB, avg file size 2.08GB
  ("fsize_db",                        24640211831), # 24.64GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_250_hh_2b2t"),
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
    'Count'                                                                          : [       388000, ],
    'CountWeighted'                                                                  : [       387905,       387946,       387983, ],
    'CountWeightedLHEEnvelope'                                                       : [       387905,       387905, ],
    'CountWeightedL1PrefireNom'                                                      : [       376423,       376438,       376483, ],
    'CountWeightedL1Prefire'                                                         : [       376423,       373629,       379144, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       376423,       376423, ],
  }),
  ("nof_tree_events",                 388000),
  ("nof_db_events",                   388000),
  ("fsize_local",                     2044590915), # 2.04GB, avg file size 2.04GB
  ("fsize_db",                        24012313674), # 24.01GB, avg file size 1.33GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_260_hh_2b2t"),
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
    'Count'                                                                          : [       384000, ],
    'CountWeighted'                                                                  : [       383955,       383965,       383899, ],
    'CountWeightedLHEEnvelope'                                                       : [       383955,       383955, ],
    'CountWeightedL1PrefireNom'                                                      : [       372436,       372415,       372423, ],
    'CountWeightedL1Prefire'                                                         : [       372436,       369639,       375152, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       372436,       372436, ],
  }),
  ("nof_tree_events",                 384000),
  ("nof_db_events",                   384000),
  ("fsize_local",                     2052513380), # 2.05GB, avg file size 2.05GB
  ("fsize_db",                        23968184441), # 23.97GB, avg file size 1.41GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_270_hh_2b2t"),
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
    'Count'                                                                          : [       400000, ],
    'CountWeighted'                                                                  : [       399942,       400003,       399967, ],
    'CountWeightedLHEEnvelope'                                                       : [       399942,       399942, ],
    'CountWeightedL1PrefireNom'                                                      : [       387697,       387701,       387736, ],
    'CountWeightedL1Prefire'                                                         : [       387697,       384729,       390579, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       387697,       387697, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     2164217288), # 2.16GB, avg file size 2.16GB
  ("fsize_db",                        25138262751), # 25.14GB, avg file size 1.09GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_280_hh_2b2t"),
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
    'Count'                                                                          : [       300000, ],
    'CountWeighted'                                                                  : [       299949,       299971,       299986, ],
    'CountWeightedLHEEnvelope'                                                       : [       299949,       299949, ],
    'CountWeightedL1PrefireNom'                                                      : [       290365,       290363,       290413, ],
    'CountWeightedL1Prefire'                                                         : [       290365,       288064,       292613, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       290365,       290365, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1659631254), # 1.66GB, avg file size 1.66GB
  ("fsize_db",                        19012035463), # 19.01GB, avg file size 1.27GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_300_hh_2b2t"),
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
    'Count'                                                                          : [       300000, ],
    'CountWeighted'                                                                  : [       299951,       299941,       299974, ],
    'CountWeightedLHEEnvelope'                                                       : [       299951,       299951, ],
    'CountWeightedL1PrefireNom'                                                      : [       289689,       289677,       289703, ],
    'CountWeightedL1Prefire'                                                         : [       289689,       287253,       292074, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       289689,       289689, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1741988627), # 1.74GB, avg file size 1.74GB
  ("fsize_db",                        19447040410), # 19.45GB, avg file size 1.77GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_350_hh_2b2t"),
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
    'Count'                                                                          : [       100000, ],
    'CountWeighted'                                                                  : [        99975,        99972,        99987, ],
    'CountWeightedLHEEnvelope'                                                       : [        99975,        99975, ],
    'CountWeightedL1PrefireNom'                                                      : [        96346,        96342,        96357, ],
    'CountWeightedL1Prefire'                                                         : [        96346,        95493,        97185, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [        96346,        96346, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     603471964), # 603.47MB, avg file size 603.47MB
  ("fsize_db",                        6609409571), # 6.61GB, avg file size 944.20MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_400_hh_2b2t"),
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
    'Count'                                                                          : [       300000, ],
    'CountWeighted'                                                                  : [       299959,       299970,       299951, ],
    'CountWeightedLHEEnvelope'                                                       : [       299959,       299959, ],
    'CountWeightedL1PrefireNom'                                                      : [       288844,       288826,       288860, ],
    'CountWeightedL1Prefire'                                                         : [       288844,       286237,       291406, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       288844,       288844, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1865009071), # 1.87GB, avg file size 932.50MB
  ("fsize_db",                        20167217854), # 20.17GB, avg file size 1.26GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_450_hh_2b2t"),
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
    'Count'                                                                          : [       290000, ],
    'CountWeighted'                                                                  : [       289988,       289936,       289906, ],
    'CountWeightedLHEEnvelope'                                                       : [       289988,       289988, ],
    'CountWeightedL1PrefireNom'                                                      : [       278902,       278852,       278879, ],
    'CountWeightedL1Prefire'                                                         : [       278902,       276315,       281443, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       278902,       278902, ],
  }),
  ("nof_tree_events",                 290000),
  ("nof_db_events",                   290000),
  ("fsize_local",                     1848850693), # 1.85GB, avg file size 1.85GB
  ("fsize_db",                        19708690689), # 19.71GB, avg file size 1.79GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_500_hh_2b2t"),
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
    'Count'                                                                          : [       300000, ],
    'CountWeighted'                                                                  : [       299931,       299901,       299925, ],
    'CountWeightedLHEEnvelope'                                                       : [       299931,       299931, ],
    'CountWeightedL1PrefireNom'                                                      : [       288217,       288174,       288240, ],
    'CountWeightedL1Prefire'                                                         : [       288217,       285489,       290900, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       288217,       288217, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1956531477), # 1.96GB, avg file size 978.27MB
  ("fsize_db",                        20644816504), # 20.64GB, avg file size 1.59GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_550_hh_2b2t"),
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
    'Count'                                                                          : [       200000, ],
    'CountWeighted'                                                                  : [       199908,       199904,       199912, ],
    'CountWeightedLHEEnvelope'                                                       : [       199908,       199908, ],
    'CountWeightedL1PrefireNom'                                                      : [       192024,       192010,       192035, ],
    'CountWeightedL1Prefire'                                                         : [       192024,       190193,       193828, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       192024,       192024, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1327509479), # 1.33GB, avg file size 1.33GB
  ("fsize_db",                        13957904944), # 13.96GB, avg file size 1.16GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_600_hh_2b2t"),
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
    'Count'                                                                          : [       200000, ],
    'CountWeighted'                                                                  : [       199961,       199968,       199906, ],
    'CountWeightedLHEEnvelope'                                                       : [       199961,       199961, ],
    'CountWeightedL1PrefireNom'                                                      : [       191776,       191763,       191758, ],
    'CountWeightedL1Prefire'                                                         : [       191776,       189883,       193642, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       191776,       191776, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1346683997), # 1.35GB, avg file size 1.35GB
  ("fsize_db",                        14016331858), # 14.02GB, avg file size 2.00GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_650_hh_2b2t"),
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
    'Count'                                                                          : [       200000, ],
    'CountWeighted'                                                                  : [       199903,       199932,       199911, ],
    'CountWeightedLHEEnvelope'                                                       : [       199903,       199903, ],
    'CountWeightedL1PrefireNom'                                                      : [       191637,       191647,       191645, ],
    'CountWeightedL1Prefire'                                                         : [       191637,       189725,       193523, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       191637,       191637, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1365862947), # 1.37GB, avg file size 1.37GB
  ("fsize_db",                        14253263609), # 14.25GB, avg file size 1.10GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_700_hh_2b2t"),
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
    'Count'                                                                          : [       100000, ],
    'CountWeighted'                                                                  : [        99924,        99962,        99957, ],
    'CountWeightedLHEEnvelope'                                                       : [        99924,        99924, ],
    'CountWeightedL1PrefireNom'                                                      : [        95751,        95766,        95774, ],
    'CountWeightedL1Prefire'                                                         : [        95751,        94791,        96699, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [        95751,        95751, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     690762109), # 690.76MB, avg file size 690.76MB
  ("fsize_db",                        7146269195), # 7.15GB, avg file size 1.02GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_750_hh_2b2t"),
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
    'Count'                                                                          : [       200000, ],
    'CountWeighted'                                                                  : [       199915,       199922,       199927, ],
    'CountWeightedLHEEnvelope'                                                       : [       199915,       199915, ],
    'CountWeightedL1PrefireNom'                                                      : [       191447,       191447,       191459, ],
    'CountWeightedL1Prefire'                                                         : [       191447,       189502,       193369, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       191447,       191447, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1394335914), # 1.39GB, avg file size 1.39GB
  ("fsize_db",                        14420020815), # 14.42GB, avg file size 1.31GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_800_hh_2b2t"),
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
    'Count'                                                                          : [       200000, ],
    'CountWeighted'                                                                  : [       199873,       199865,       199882, ],
    'CountWeightedLHEEnvelope'                                                       : [       199873,       199873, ],
    'CountWeightedL1PrefireNom'                                                      : [       191404,       191393,       191414, ],
    'CountWeightedL1Prefire'                                                         : [       191404,       189461,       193326, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       191404,       191404, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1405042291), # 1.41GB, avg file size 1.41GB
  ("fsize_db",                        14617490096), # 14.62GB, avg file size 1.04GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_850_hh_2b2t"),
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
    'Count'                                                                          : [       100000, ],
    'CountWeighted'                                                                  : [        99939,        99918,        99928, ],
    'CountWeightedLHEEnvelope'                                                       : [        99939,        99939, ],
    'CountWeightedL1PrefireNom'                                                      : [        95667,        95643,        95670, ],
    'CountWeightedL1Prefire'                                                         : [        95667,        94689,        96634, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [        95667,        95667, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     708646544), # 708.65MB, avg file size 708.65MB
  ("fsize_db",                        7382733082), # 7.38GB, avg file size 671.16MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_900_hh_2b2t"),
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
    'Count'                                                                          : [       100000, ],
    'CountWeighted'                                                                  : [        99923,        99922,        99919, ],
    'CountWeightedLHEEnvelope'                                                       : [        99923,        99923, ],
    'CountWeightedL1PrefireNom'                                                      : [        95624,        95620,        95622, ],
    'CountWeightedL1Prefire'                                                         : [        95624,        94638,        96597, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [        95624,        95624, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     717174638), # 717.17MB, avg file size 717.17MB
  ("fsize_db",                        7364574553), # 7.36GB, avg file size 1.05GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_1000_hh_2b2t"),
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
    'Count'                                                                          : [       100000, ],
    'CountWeighted'                                                                  : [        99896,        99880,        99893, ],
    'CountWeightedLHEEnvelope'                                                       : [        99896,        99896, ],
    'CountWeightedL1PrefireNom'                                                      : [        95402,        95396,        95402, ],
    'CountWeightedL1Prefire'                                                         : [        95402,        94380,        96413, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [        95402,        95402, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     726885015), # 726.89MB, avg file size 726.89MB
  ("fsize_db",                        7497237044), # 7.50GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_1250_hh_2b2t"),
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
    'Count'                                                                          : [       100000, ],
    'CountWeighted'                                                                  : [        99830,        99839,        99832, ],
    'CountWeightedLHEEnvelope'                                                       : [        99830,        99830, ],
    'CountWeightedL1PrefireNom'                                                      : [        95322,        95334,        95315, ],
    'CountWeightedL1Prefire'                                                         : [        95322,        94301,        96336, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [        95322,        95322, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     731849421), # 731.85MB, avg file size 731.85MB
  ("fsize_db",                        7582428905), # 7.58GB, avg file size 1.52GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_1500_hh_2b2t"),
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
    'Count'                                                                          : [       100000, ],
    'CountWeighted'                                                                  : [        99719,        99735,        99741, ],
    'CountWeightedLHEEnvelope'                                                       : [        99719,        99719, ],
    'CountWeightedL1PrefireNom'                                                      : [        95139,        95146,        95148, ],
    'CountWeightedL1Prefire'                                                         : [        95139,        94105,        96167, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [        95139,        95139, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     733116360), # 733.12MB, avg file size 733.12MB
  ("fsize_db",                        7802866732), # 7.80GB, avg file size 650.24MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_1750_hh_2b2t"),
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
    'Count'                                                                          : [       100000, ],
    'CountWeighted'                                                                  : [        99675,        99681,        99659, ],
    'CountWeightedLHEEnvelope'                                                       : [        99675,        99675, ],
    'CountWeightedL1PrefireNom'                                                      : [        95001,        94999,        95001, ],
    'CountWeightedL1Prefire'                                                         : [        95001,        93947,        96046, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [        95001,        95001, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     732128274), # 732.13MB, avg file size 732.13MB
  ("fsize_db",                        7810715378), # 7.81GB, avg file size 710.07MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_2000_hh_2b2t"),
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
    'Count'                                                                          : [       100000, ],
    'CountWeighted'                                                                  : [        98787,        98819,        98810, ],
    'CountWeightedLHEEnvelope'                                                       : [        98787,        98787, ],
    'CountWeightedL1PrefireNom'                                                      : [        94042,        94052,        94066, ],
    'CountWeightedL1Prefire'                                                         : [        94042,        92985,        95094, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [        94042,        94042, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     735274599), # 735.27MB, avg file size 735.27MB
  ("fsize_db",                        7943092984), # 7.94GB, avg file size 992.89MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_3000_hh_2b2t"),
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
    'Count'                                                                          : [       386000, ],
    'CountWeighted'                                                                  : [       380711,       380684,       380654, ],
    'CountWeightedLHEWeightScale'                                                    : [       418477,       382051,       351705,       416983,       380711,       350495,       415816,       379664,       349551, ],
    'CountWeightedLHEEnvelope'                                                       : [       420183,       347905, ],
    'CountWeightedL1PrefireNom'                                                      : [       351680,       351624,       351702, ],
    'CountWeightedL1Prefire'                                                         : [       351680,       345403,       357976, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       386173,       352974,       325316,       384728,       351678,       324146,       383600,       350666,       323233, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       387830,       321631, ],
  }),
  ("nof_tree_events",                 386000),
  ("nof_db_events",                   386000),
  ("fsize_local",                     2065891738), # 2.07GB, avg file size 2.07GB
  ("fsize_db",                        23569723909), # 23.57GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_250_hh_2b2t"),
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
    'Count'                                                                          : [       400000, ],
    'CountWeighted'                                                                  : [       396138,       396210,       396124, ],
    'CountWeightedLHEWeightScale'                                                    : [       425618,       397454,       372943,       424175,       396138,       371737,       423058,       395121,       370804, ],
    'CountWeightedLHEEnvelope'                                                       : [       429873,       366639, ],
    'CountWeightedL1PrefireNom'                                                      : [       369736,       369732,       369757, ],
    'CountWeightedL1Prefire'                                                         : [       369736,       363831,       375627, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       396678,       371010,       348593,       395281,       369736,       347424,       394200,       368750,       346521, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       400812,       342473, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1938316917), # 1.94GB, avg file size 1.94GB
  ("fsize_db",                        22974833125), # 22.97GB, avg file size 1.21GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_260_hh_2b2t"),
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
    'Count'                                                                          : [       400000, ],
    'CountWeighted'                                                                  : [       396176,       396169,       396177, ],
    'CountWeightedLHEWeightScale'                                                    : [       425826,       397469,       372790,       424408,       396175,       371605,       423310,       395176,       370689, ],
    'CountWeightedLHEEnvelope'                                                       : [       429940,       366665, ],
    'CountWeightedL1PrefireNom'                                                      : [       369669,       369630,       369702, ],
    'CountWeightedL1Prefire'                                                         : [       369669,       363737,       375586, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       396770,       370920,       348351,       395398,       369667,       347203,       394336,       368700,       346316, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       400768,       342403, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1939642017), # 1.94GB, avg file size 1.94GB
  ("fsize_db",                        22808220732), # 22.81GB, avg file size 1.20GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_270_hh_2b2t"),
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
    'Count'                                                                          : [       400000, ],
    'CountWeighted'                                                                  : [       396168,       396205,       396164, ],
    'CountWeightedLHEWeightScale'                                                    : [       426095,       397392,       372446,       424750,       396167,       371325,       423708,       395219,       370458, ],
    'CountWeightedLHEEnvelope'                                                       : [       430025,       366622, ],
    'CountWeightedL1PrefireNom'                                                      : [       369680,       369657,       369721, ],
    'CountWeightedL1Prefire'                                                         : [       369680,       363745,       375598, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       397049,       370864,       348028,       395747,       369678,       346942,       394739,       368761,       346102, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       400875,       342366, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1941619692), # 1.94GB, avg file size 1.94GB
  ("fsize_db",                        22983626173), # 22.98GB, avg file size 1.21GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_280_hh_2b2t"),
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
    'Count'                                                                          : [       282000, ],
    'CountWeighted'                                                                  : [       279385,       279307,       279385, ],
    'CountWeightedLHEWeightScale'                                                    : [       300913,       280205,       262165,       300009,       279384,       261415,       299307,       278746,       260833, ],
    'CountWeightedLHEEnvelope'                                                       : [       303536,       258278, ],
    'CountWeightedL1PrefireNom'                                                      : [       260494,       260430,       260526, ],
    'CountWeightedL1Prefire'                                                         : [       260494,       256264,       264710, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       280220,       261288,       244794,       279344,       260493,       244067,       278666,       259876,       243504, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       282765,       241023, ],
  }),
  ("nof_tree_events",                 282000),
  ("nof_db_events",                   282000),
  ("fsize_local",                     1370967946), # 1.37GB, avg file size 1.37GB
  ("fsize_db",                        15951259391), # 15.95GB, avg file size 839.54MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_300_hh_2b2t"),
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
    'Count'                                                                          : [       300000, ],
    'CountWeighted'                                                                  : [       297163,       297090,       297116, ],
    'CountWeightedLHEWeightScale'                                                    : [       320676,       297966,       278290,       319787,       297162,       277558,       319097,       296536,       276989, ],
    'CountWeightedLHEEnvelope'                                                       : [       323228,       274509, ],
    'CountWeightedL1PrefireNom'                                                      : [       276816,       276758,       276832, ],
    'CountWeightedL1Prefire'                                                         : [       276816,       272256,       281359, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       298343,       277588,       259591,       297488,       276814,       258885,       296824,       276212,       258338, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       300814,       255934, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1461878010), # 1.46GB, avg file size 1.46GB
  ("fsize_db",                        17224376684), # 17.22GB, avg file size 1.01GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_320_hh_2b2t"),
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
    'Count'                                                                          : [       300000, ],
    'CountWeighted'                                                                  : [       297244,       297241,       297247, ],
    'CountWeightedLHEWeightScale'                                                    : [       321677,       297993,       277648,       320847,       297243,       276968,       320201,       296661,       276438, ],
    'CountWeightedLHEEnvelope'                                                       : [       323927,       274264, ],
    'CountWeightedL1PrefireNom'                                                      : [       276729,       276694,       276755, ],
    'CountWeightedL1Prefire'                                                         : [       276729,       272130,       281318, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       299102,       277449,       258780,       298305,       276728,       258126,       297684,       276168,       257617, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       301277,       255516, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1465376565), # 1.47GB, avg file size 1.47GB
  ("fsize_db",                        16911146727), # 16.91GB, avg file size 1.06GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_350_hh_2b2t"),
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
    'Count'                                                                          : [       292000, ],
    'CountWeighted'                                                                  : [       289082,       289007,       289038, ],
    'CountWeightedLHEWeightScale'                                                    : [       314301,       289648,       268560,       313669,       289080,       268047,       313177,       288637,       267646, ],
    'CountWeightedLHEEnvelope'                                                       : [       316061,       265965, ],
    'CountWeightedL1PrefireNom'                                                      : [       268541,       268476,       268569, ],
    'CountWeightedL1Prefire'                                                         : [       268541,       263946,       273125, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       291657,       269085,       249782,       291049,       268538,       249287,       290575,       268112,       248901, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       293356,       247277, ],
  }),
  ("nof_tree_events",                 292000),
  ("nof_db_events",                   292000),
  ("fsize_local",                     1433808838), # 1.43GB, avg file size 1.43GB
  ("fsize_db",                        16538417486), # 16.54GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_400_hh_2b2t"),
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
    'Count'                                                                          : [       300000, ],
    'CountWeighted'                                                                  : [       297031,       296940,       296861, ],
    'CountWeightedLHEWeightScale'                                                    : [       324809,       297551,       274418,       324224,       297027,       273945,       323766,       296616,       273576, ],
    'CountWeightedLHEEnvelope'                                                       : [       326327,       272144, ],
    'CountWeightedL1PrefireNom'                                                      : [       275420,       275359,       275384, ],
    'CountWeightedL1Prefire'                                                         : [       275420,       270596,       280232, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       300898,       275922,       254770,       300334,       275418,       254315,       299894,       275023,       253959, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       302359,       252578, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1483560095), # 1.48GB, avg file size 1.48GB
  ("fsize_db",                        16984173640), # 16.98GB, avg file size 808.77MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_450_hh_2b2t"),
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
    'Count'                                                                          : [       300000, ],
    'CountWeighted'                                                                  : [       296817,       296853,       296840, ],
    'CountWeightedLHEWeightScale'                                                    : [       326340,       297263,       272948,       325839,       296817,       272548,       325446,       296467,       272234, ],
    'CountWeightedLHEEnvelope'                                                       : [       327645,       271011, ],
    'CountWeightedL1PrefireNom'                                                      : [       274894,       274871,       274933, ],
    'CountWeightedL1Prefire'                                                         : [       274894,       269994,       279785, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       301934,       275325,       253037,       301451,       274894,       252651,       301073,       274557,       252349, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       303182,       251177, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1494669360), # 1.49GB, avg file size 1.49GB
  ("fsize_db",                        16980250583), # 16.98GB, avg file size 1.54GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_500_hh_2b2t"),
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
    'Count'                                                                          : [       200000, ],
    'CountWeighted'                                                                  : [       197637,       197650,       197618, ],
    'CountWeightedLHEWeightScale'                                                    : [       219587,       197814,       179948,       219387,       197637,       179790,       219230,       197498,       179666, ],
    'CountWeightedLHEEnvelope'                                                       : [       220239,       179073, ],
    'CountWeightedL1PrefireNom'                                                      : [       182291,       182286,       182297, ],
    'CountWeightedL1Prefire'                                                         : [       182291,       178871,       185707, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       202356,       182460,       166105,       202166,       182291,       165954,       202016,       182159,       165836, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       202975,       165272, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1011513381), # 1.01GB, avg file size 1.01GB
  ("fsize_db",                        11350421129), # 11.35GB, avg file size 1.03GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_600_hh_2b2t"),
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
    'Count'                                                                          : [       197000, ],
    'CountWeighted'                                                                  : [       194681,       194620,       194614, ],
    'CountWeightedLHEWeightScale'                                                    : [       217393,       194844,       176394,       217205,       194679,       176247,       217057,       194548,       176131, ],
    'CountWeightedLHEEnvelope'                                                       : [       217930,       175655, ],
    'CountWeightedL1PrefireNom'                                                      : [       179001,       178982,       178971, ],
    'CountWeightedL1Prefire'                                                         : [       179001,       175525,       182477, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       199759,       179158,       162337,       199579,       178999,       162195,       199437,       178874,       162084, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       200269,       161631, ],
  }),
  ("nof_tree_events",                 197000),
  ("nof_db_events",                   197000),
  ("fsize_local",                     1003378325), # 1.00GB, avg file size 1.00GB
  ("fsize_db",                        11416936121), # 11.42GB, avg file size 1.04GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_650_hh_2b2t"),
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
    'Count'                                                                          : [       200000, ],
    'CountWeighted'                                                                  : [       197261,       197246,       197256, ],
    'CountWeightedLHEWeightScale'                                                    : [       221433,       197396,       178003,       221273,       197255,       177878,       221147,       197144,       177779, ],
    'CountWeightedLHEEnvelope'                                                       : [       221910,       177363, ],
    'CountWeightedL1PrefireNom'                                                      : [       181140,       181088,       181186, ],
    'CountWeightedL1Prefire'                                                         : [       181140,       177567,       184722, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       203172,       181271,       163576,       203019,       181136,       163457,       202899,       181030,       163363, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       203624,       162966, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1024412252), # 1.02GB, avg file size 1.02GB
  ("fsize_db",                        11593555122), # 11.59GB, avg file size 966.13MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_700_hh_2b2t"),
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
    'Count'                                                                          : [       200000, ],
    'CountWeighted'                                                                  : [       197207,       197194,       197247, ],
    'CountWeightedLHEWeightScale'                                                    : [       222484,       197324,       177159,       222350,       197207,       177056,       222245,       197115,       176974, ],
    'CountWeightedLHEEnvelope'                                                       : [       222891,       176626, ],
    'CountWeightedL1PrefireNom'                                                      : [       180670,       180647,       180708, ],
    'CountWeightedL1Prefire'                                                         : [       180670,       177017,       184333, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       203682,       180783,       162413,       203554,       180670,       162313,       203453,       180582,       162235, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       204069,       161903, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1031260227), # 1.03GB, avg file size 1.03GB
  ("fsize_db",                        11489097788), # 11.49GB, avg file size 2.30GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_750_hh_2b2t"),
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
    'Count'                                                                          : [       200000, ],
    'CountWeighted'                                                                  : [       196919,       196885,       196894, ],
    'CountWeightedLHEWeightScale'                                                    : [       224088,       197016,       175475,       223978,       196919,       175391,       223891,       196843,       175324, ],
    'CountWeightedLHEEnvelope'                                                       : [       224448,       175029, ],
    'CountWeightedL1PrefireNom'                                                      : [       179908,       179858,       179926, ],
    'CountWeightedL1Prefire'                                                         : [       179908,       176163,       183665, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       204638,       180000,       160432,       204533,       179908,       160351,       204449,       179835,       160287, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       204982,       160005, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1039487129), # 1.04GB, avg file size 1.04GB
  ("fsize_db",                        11469515493), # 11.47GB, avg file size 1.43GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_850_hh_2b2t"),
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
    'Count'                                                                          : [       100000, ],
    'CountWeighted'                                                                  : [        98347,        98370,        98369, ],
    'CountWeightedLHEWeightScale'                                                    : [       112494,        98389,        87322,       112442,        98343,        87282,       112401,        98308,        87251, ],
    'CountWeightedLHEEnvelope'                                                       : [       112655,        87122, ],
    'CountWeightedL1PrefireNom'                                                      : [        89724,        89720,        89740, ],
    'CountWeightedL1Prefire'                                                         : [        89724,        87828,        91630, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       102560,        89766,        79708,       102511,        89722,        79670,       102471,        89688,        79640, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       102711,        79518, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     521748804), # 521.75MB, avg file size 521.75MB
  ("fsize_db",                        5871346880), # 5.87GB, avg file size 489.28MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_900_hh_2b2t"),
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
    'Count'                                                                          : [       100000, ],
    'CountWeighted'                                                                  : [        98141,        98138,        98153, ],
    'CountWeightedLHEWeightScale'                                                    : [       113171,        98179,        86498,       113127,        98141,        86465,       113093,        98112,        86439, ],
    'CountWeightedLHEEnvelope'                                                       : [       113321,        86323, ],
    'CountWeightedL1PrefireNom'                                                      : [        89117,        89099,        89132, ],
    'CountWeightedL1Prefire'                                                         : [        89117,        87145,        91098, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       102713,        89153,        78586,       102671,        89117,        78554,       102638,        89089,        78529, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       102854,        78420, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     525090856), # 525.09MB, avg file size 525.09MB
  ("fsize_db",                        5935760871), # 5.94GB, avg file size 494.65MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_1000_hh_2b2t"),
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
    'Count'                                                                          : [       100000, ],
    'CountWeighted'                                                                  : [        96184,        96181,        96147, ],
    'CountWeightedLHEWeightScale'                                                    : [       116927,        96197,        81030,       116911,        96183,        81018,       116897,        96172,        81008, ],
    'CountWeightedLHEEnvelope'                                                       : [       116946,        81031, ],
    'CountWeightedL1PrefireNom'                                                      : [        86077,        86056,        86088, ],
    'CountWeightedL1Prefire'                                                         : [        86077,        83936,        88250, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       104632,        86089,        72544,       104616,        86077,        72533,       104604,        86066,        72524, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       104656,        72535, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     518489517), # 518.49MB, avg file size 518.49MB
  ("fsize_db",                        5865706342), # 5.87GB, avg file size 651.75MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_1750_hh_2b2t"),
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
    'Count'                                                                          : [       100000, ],
    'CountWeighted'                                                                  : [        95168,        95195,        95174, ],
    'CountWeightedLHEWeightScale'                                                    : [       117499,        95175,        79172,       117490,        95168,        79166,       117483,        95162,        79161, ],
    'CountWeightedLHEEnvelope'                                                       : [       117534,        79170, ],
    'CountWeightedL1PrefireNom'                                                      : [        84767,        84776,        84769, ],
    'CountWeightedL1Prefire'                                                         : [        84767,        82580,        86989, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       104637,        84772,        70525,       104629,        84766,        70520,       104622,        84760,        70515, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       104670,        70522, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     514603495), # 514.60MB, avg file size 514.60MB
  ("fsize_db",                        6015024771), # 6.02GB, avg file size 601.50MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_2000_hh_2b2t"),
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
    'Count'                                                                          : [       390000, ],
    'CountWeighted'                                                                  : [       390069,       389998,       389980, ],
    'CountWeightedLHEEnvelope'                                                       : [       390069,       390069, ],
    'CountWeightedL1PrefireNom'                                                      : [       382746,       382675,       382704, ],
    'CountWeightedL1Prefire'                                                         : [       382746,       380832,       384560, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       382746,       382746, ],
  }),
  ("nof_tree_events",                 390000),
  ("nof_db_events",                   390000),
  ("fsize_local",                     1362068630), # 1.36GB, avg file size 1.36GB
  ("fsize_db",                        20093492648), # 20.09GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_250_hh_2b2t"),
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
    'Count'                                                                          : [       360000, ],
    'CountWeighted'                                                                  : [       359964,       360000,       359999, ],
    'CountWeightedLHEWeightScale'                                                    : [       365610,       359961,       352043,       365610,       359961,       352043,       365610,       359961,       352043, ],
    'CountWeightedLHEEnvelope'                                                       : [       365610,       352043, ],
    'CountWeightedL1PrefireNom'                                                      : [       352839,       352857,       352876, ],
    'CountWeightedL1Prefire'                                                         : [       352839,       351000,       354604, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       358325,       352837,       345110,       358325,       352837,       345110,       358325,       352837,       345110, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       358325,       345110, ],
  }),
  ("nof_tree_events",                 360000),
  ("nof_db_events",                   360000),
  ("fsize_local",                     1267357939), # 1.27GB, avg file size 1.27GB
  ("fsize_db",                        17758553715), # 17.76GB, avg file size 986.59MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_260_hh_2b2t"),
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
    'Count'                                                                          : [       392000, ],
    'CountWeighted'                                                                  : [       392036,       391971,       392016, ],
    'CountWeightedLHEWeightScale'                                                    : [       399342,       392022,       382349,       399342,       392022,       382349,       399342,       392022,       382349, ],
    'CountWeightedLHEEnvelope'                                                       : [       399342,       382349, ],
    'CountWeightedL1PrefireNom'                                                      : [       383961,       383909,       383959, ],
    'CountWeightedL1Prefire'                                                         : [       383961,       381892,       385944, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       391084,       383950,       374534,       391084,       383950,       374534,       391084,       383950,       374534, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       391084,       374534, ],
  }),
  ("nof_tree_events",                 392000),
  ("nof_db_events",                   392000),
  ("fsize_local",                     1399303046), # 1.40GB, avg file size 1.40GB
  ("fsize_db",                        19361033085), # 19.36GB, avg file size 1.21GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_270_hh_2b2t"),
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
    'Count'                                                                          : [       398000, ],
    'CountWeighted'                                                                  : [       397935,       397980,       397961, ],
    'CountWeightedLHEEnvelope'                                                       : [       397935,       397935, ],
    'CountWeightedL1PrefireNom'                                                      : [       389352,       389368,       389382, ],
    'CountWeightedL1Prefire'                                                         : [       389352,       387171,       391453, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       389352,       389352, ],
  }),
  ("nof_tree_events",                 398000),
  ("nof_db_events",                   398000),
  ("fsize_local",                     1455365087), # 1.46GB, avg file size 1.46GB
  ("fsize_db",                        20704800616), # 20.70GB, avg file size 900.21MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_280_hh_2b2t"),
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
    'Count'                                                                          : [       300000, ],
    'CountWeighted'                                                                  : [       300049,       299930,       299959, ],
    'CountWeightedLHEWeightScale'                                                    : [       308237,       300049,       290522,       308237,       300049,       290522,       308237,       300049,       290522, ],
    'CountWeightedLHEEnvelope'                                                       : [       308237,       290522, ],
    'CountWeightedL1PrefireNom'                                                      : [       293089,       292994,       293046, ],
    'CountWeightedL1Prefire'                                                         : [       293089,       291347,       294770, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       301062,       293089,       283845,       301062,       293089,       283845,       301062,       293089,       283845, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       301062,       283845, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1117370311), # 1.12GB, avg file size 1.12GB
  ("fsize_db",                        15151937781), # 15.15GB, avg file size 688.72MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_300_hh_2b2t"),
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
    'Count'                                                                          : [       300000, ],
    'CountWeighted'                                                                  : [       299962,       299954,       299997, ],
    'CountWeightedLHEWeightScale'                                                    : [       309838,       299962,       289298,       309838,       299962,       289298,       309838,       299962,       289298, ],
    'CountWeightedLHEEnvelope'                                                       : [       309838,       289298, ],
    'CountWeightedL1PrefireNom'                                                      : [       292505,       292492,       292539, ],
    'CountWeightedL1Prefire'                                                         : [       292505,       290662,       294301, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       302075,       292505,       282141,       302075,       292505,       282141,       302075,       292505,       282141, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       302075,       282141, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1148798557), # 1.15GB, avg file size 1.15GB
  ("fsize_db",                        15215406969), # 15.22GB, avg file size 1.17GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_320_hh_2b2t"),
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
    'Count'                                                                          : [       300000, ],
    'CountWeighted'                                                                  : [       299995,       300043,       299941, ],
    'CountWeightedLHEWeightScale'                                                    : [       311982,       299993,       287611,       311982,       299993,       287611,       311982,       299993,       287611, ],
    'CountWeightedLHEEnvelope'                                                       : [       311982,       287611, ],
    'CountWeightedL1PrefireNom'                                                      : [       291873,       291886,       291857, ],
    'CountWeightedL1Prefire'                                                         : [       291873,       289896,       293797, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       303481,       291870,       279881,       303481,       291870,       279881,       303481,       291870,       279881, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       303481,       279881, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1189578851), # 1.19GB, avg file size 1.19GB
  ("fsize_db",                        15430234358), # 15.43GB, avg file size 1.10GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_350_hh_2b2t"),
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
    'Count'                                                                          : [       296000, ],
    'CountWeighted'                                                                  : [       296027,       295915,       295984, ],
    'CountWeightedLHEWeightScale'                                                    : [       310901,       296027,       281469,       310901,       296027,       281469,       310901,       296027,       281469, ],
    'CountWeightedLHEEnvelope'                                                       : [       310901,       281469, ],
    'CountWeightedL1PrefireNom'                                                      : [       287270,       287195,       287248, ],
    'CountWeightedL1Prefire'                                                         : [       287270,       285176,       289316, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       301663,       287270,       273209,       301663,       287270,       273209,       301663,       287270,       273209, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       301663,       273209, ],
  }),
  ("nof_tree_events",                 296000),
  ("nof_db_events",                   296000),
  ("fsize_local",                     1232417195), # 1.23GB, avg file size 1.23GB
  ("fsize_db",                        15540706594), # 15.54GB, avg file size 971.29MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_400_hh_2b2t"),
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
    'Count'                                                                          : [       272000, ],
    'CountWeighted'                                                                  : [       271995,       271937,       271996, ],
    'CountWeightedLHEWeightScale'                                                    : [       288103,       271995,       256804,       288103,       271995,       256804,       288103,       271995,       256804, ],
    'CountWeightedLHEEnvelope'                                                       : [       288103,       256804, ],
    'CountWeightedL1PrefireNom'                                                      : [       263477,       263418,       263507, ],
    'CountWeightedL1Prefire'                                                         : [       263477,       261464,       265458, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       279032,       263477,       248822,       279032,       263477,       248822,       279032,       263477,       248822, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       279032,       248822, ],
  }),
  ("nof_tree_events",                 272000),
  ("nof_db_events",                   272000),
  ("fsize_local",                     1179256136), # 1.18GB, avg file size 1.18GB
  ("fsize_db",                        14544281532), # 14.54GB, avg file size 808.02MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_450_hh_2b2t"),
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
    'Count'                                                                          : [       190000, ],
    'CountWeighted'                                                                  : [       189995,       190029,       190021, ],
    'CountWeightedLHEWeightScale'                                                    : [       202729,       189995,       178272,       202729,       189995,       178272,       202729,       189995,       178272, ],
    'CountWeightedLHEEnvelope'                                                       : [       202729,       178272, ],
    'CountWeightedL1PrefireNom'                                                      : [       183623,       183648,       183634, ],
    'CountWeightedL1Prefire'                                                         : [       183623,       182135,       185093, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       195888,       183623,       172331,       195888,       183623,       172331,       195888,       183623,       172331, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       195888,       172331, ],
  }),
  ("nof_tree_events",                 190000),
  ("nof_db_events",                   190000),
  ("fsize_local",                     852599591), # 852.60MB, avg file size 852.60MB
  ("fsize_db",                        10300681960), # 10.30GB, avg file size 858.39MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_500_hh_2b2t"),
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
    'Count'                                                                          : [       200000, ],
    'CountWeighted'                                                                  : [       199975,       199951,       200000, ],
    'CountWeightedLHEWeightScale'                                                    : [       214726,       199975,       186581,       214726,       199975,       186581,       214726,       199975,       186581, ],
    'CountWeightedLHEEnvelope'                                                       : [       214726,       186581, ],
    'CountWeightedL1PrefireNom'                                                      : [       192936,       192910,       192956, ],
    'CountWeightedL1Prefire'                                                         : [       192936,       191299,       194551, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       207117,       192936,       180053,       207117,       192936,       180053,       207117,       192936,       180053, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       207117,       180053, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     925203759), # 925.20MB, avg file size 925.20MB
  ("fsize_db",                        10884541416), # 10.88GB, avg file size 989.50MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_550_hh_2b2t"),
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
    'Count'                                                                          : [       200000, ],
    'CountWeighted'                                                                  : [       199983,       199972,       199941, ],
    'CountWeightedLHEWeightScale'                                                    : [       215954,       199982,       185647,       215954,       199982,       185647,       215954,       199982,       185647, ],
    'CountWeightedLHEEnvelope'                                                       : [       215954,       185647, ],
    'CountWeightedL1PrefireNom'                                                      : [       192691,       192676,       192684, ],
    'CountWeightedL1Prefire'                                                         : [       192691,       191004,       194357, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       208030,       192689,       178922,       208030,       192689,       178922,       208030,       192689,       178922, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       208030,       178922, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     947999667), # 948.00MB, avg file size 948.00MB
  ("fsize_db",                        11044936345), # 11.04GB, avg file size 920.41MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_600_hh_2b2t"),
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
    'Count'                                                                          : [       188000, ],
    'CountWeighted'                                                                  : [       187980,       187931,       187961, ],
    'CountWeightedLHEWeightScale'                                                    : [       204025,       187980,       173735,       204025,       187980,       173735,       204025,       187980,       173735, ],
    'CountWeightedLHEEnvelope'                                                       : [       204025,       173735, ],
    'CountWeightedL1PrefireNom'                                                      : [       180909,       180857,       180920, ],
    'CountWeightedL1Prefire'                                                         : [       180909,       179283,       182514, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       196304,       180909,       167239,       196304,       180909,       167239,       196304,       180909,       167239, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       196304,       167239, ],
  }),
  ("nof_tree_events",                 188000),
  ("nof_db_events",                   188000),
  ("fsize_local",                     910547031), # 910.55MB, avg file size 910.55MB
  ("fsize_db",                        10510514184), # 10.51GB, avg file size 700.70MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_650_hh_2b2t"),
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
    'Count'                                                                          : [       200000, ],
    'CountWeighted'                                                                  : [       199919,       200015,       199967, ],
    'CountWeightedLHEWeightScale'                                                    : [       218058,       199919,       184085,       218058,       199919,       184085,       218058,       199919,       184085, ],
    'CountWeightedLHEEnvelope'                                                       : [       218058,       184085, ],
    'CountWeightedL1PrefireNom'                                                      : [       192226,       192267,       192272, ],
    'CountWeightedL1Prefire'                                                         : [       192226,       190462,       193972, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       209587,       192226,       177014,       209587,       192226,       177014,       209587,       192226,       177014, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       209587,       177014, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     982972153), # 982.97MB, avg file size 982.97MB
  ("fsize_db",                        11214998225), # 11.21GB, avg file size 1.40GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_700_hh_2b2t"),
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
    'Count'                                                                          : [       196000, ],
    'CountWeighted'                                                                  : [       195945,       195987,       195992, ],
    'CountWeightedLHEEnvelope'                                                       : [       195945,       195945, ],
    'CountWeightedL1PrefireNom'                                                      : [       188193,       188207,       188231, ],
    'CountWeightedL1Prefire'                                                         : [       188193,       186425,       189946, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       188193,       188193, ],
  }),
  ("nof_tree_events",                 196000),
  ("nof_db_events",                   196000),
  ("fsize_local",                     982820891), # 982.82MB, avg file size 982.82MB
  ("fsize_db",                        11545737081), # 11.55GB, avg file size 962.14MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_750_hh_2b2t"),
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
    'Count'                                                                          : [       200000, ],
    'CountWeighted'                                                                  : [       199954,       199983,       199978, ],
    'CountWeightedLHEEnvelope'                                                       : [       199954,       199954, ],
    'CountWeightedL1PrefireNom'                                                      : [       191983,       191996,       192001, ],
    'CountWeightedL1Prefire'                                                         : [       191983,       190171,       193781, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       191983,       191983, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1014454815), # 1.01GB, avg file size 1.01GB
  ("fsize_db",                        11819983411), # 11.82GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_800_hh_2b2t"),
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
    'Count'                                                                          : [       192000, ],
    'CountWeighted'                                                                  : [       191971,       191959,       191946, ],
    'CountWeightedLHEEnvelope'                                                       : [       191971,       191971, ],
    'CountWeightedL1PrefireNom'                                                      : [       184232,       184202,       184240, ],
    'CountWeightedL1Prefire'                                                         : [       184232,       182472,       185973, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       184232,       184232, ],
  }),
  ("nof_tree_events",                 192000),
  ("nof_db_events",                   192000),
  ("fsize_local",                     983507593), # 983.51MB, avg file size 983.51MB
  ("fsize_db",                        11490975329), # 11.49GB, avg file size 766.07MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_850_hh_2b2t"),
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
    'Count'                                                                          : [        95000, ],
    'CountWeighted'                                                                  : [        94980,        94979,        94981, ],
    'CountWeightedLHEWeightScale'                                                    : [       105134,        94980,        86280,       105134,        94980,        86280,       105134,        94980,        86280, ],
    'CountWeightedLHEEnvelope'                                                       : [       105139,        86276, ],
    'CountWeightedL1PrefireNom'                                                      : [        91044,        91041,        91048, ],
    'CountWeightedL1Prefire'                                                         : [        91044,        90156,        91927, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       100747,        91044,        82723,       100747,        91044,        82723,       100747,        91044,        82723, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       100752,        82719, ],
  }),
  ("nof_tree_events",                 95000),
  ("nof_db_events",                   95000),
  ("fsize_local",                     488791579), # 488.79MB, avg file size 488.79MB
  ("fsize_db",                        5517036529), # 5.52GB, avg file size 788.15MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_900_hh_2b2t"),
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
    'Count'                                                                          : [       100000, ],
    'CountWeighted'                                                                  : [        99979,        99992,        99979, ],
    'CountWeightedLHEWeightScale'                                                    : [       111332,        99979,        90326,       111332,        99979,        90326,       111332,        99979,        90326, ],
    'CountWeightedLHEEnvelope'                                                       : [       111332,        90326, ],
    'CountWeightedL1PrefireNom'                                                      : [        95771,        95775,        95776, ],
    'CountWeightedL1Prefire'                                                         : [        95771,        94826,        96708, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       106622,        95771,        86545,       106622,        95771,        86545,       106622,        95771,        86545, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       106622,        86545, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     522640478), # 522.64MB, avg file size 522.64MB
  ("fsize_db",                        5887358169), # 5.89GB, avg file size 654.15MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1000_hh_2b2t"),
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
    'Count'                                                                          : [       100000, ],
    'CountWeighted'                                                                  : [        99970,        99975,        99983, ],
    'CountWeightedLHEEnvelope'                                                       : [        99970,        99970, ],
    'CountWeightedL1PrefireNom'                                                      : [        95597,        95599,        95609, ],
    'CountWeightedL1Prefire'                                                         : [        95597,        94622,        96568, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [        95597,        95597, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     536313068), # 536.31MB, avg file size 536.31MB
  ("fsize_db",                        6210975535), # 6.21GB, avg file size 690.11MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1250_hh_2b2t"),
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
    'Count'                                                                          : [       100000, ],
    'CountWeighted'                                                                  : [        99965,        99967,        99948, ],
    'CountWeightedLHEWeightScale'                                                    : [       113902,        99965,        88519,       113902,        99965,        88519,       113902,        99965,        88519, ],
    'CountWeightedLHEEnvelope'                                                       : [       113902,        88518, ],
    'CountWeightedL1PrefireNom'                                                      : [        95493,        95493,        95482, ],
    'CountWeightedL1Prefire'                                                         : [        95493,        94504,        96479, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       108786,        95492,        84575,       108786,        95492,        84575,       108786,        95492,        84575, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       108787,        84574, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     527868184), # 527.87MB, avg file size 527.87MB
  ("fsize_db",                        5949909431), # 5.95GB, avg file size 1.49GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1500_hh_2b2t"),
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
    'Count'                                                                          : [       100000, ],
    'CountWeighted'                                                                  : [        99940,        99944,        99946, ],
    'CountWeightedLHEEnvelope'                                                       : [        99940,        99940, ],
    'CountWeightedL1PrefireNom'                                                      : [        95395,        95386,        95406, ],
    'CountWeightedL1Prefire'                                                         : [        95395,        94391,        96394, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [        95395,        95395, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     528961553), # 528.96MB, avg file size 528.96MB
  ("fsize_db",                        6303523737), # 6.30GB, avg file size 573.05MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1750_hh_2b2t"),
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
    'Count'                                                                          : [        92000, ],
    'CountWeighted'                                                                  : [        91915,        91911,        91908, ],
    'CountWeightedLHEWeightScale'                                                    : [       106418,        91911,        80211,       106418,        91911,        80211,       106418,        91911,        80211, ],
    'CountWeightedLHEEnvelope'                                                       : [       106418,        80211, ],
    'CountWeightedL1PrefireNom'                                                      : [        87674,        87669,        87669, ],
    'CountWeightedL1Prefire'                                                         : [        87674,        86742,        88603, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       101496,        87672,        76520,       101496,        87672,        76520,       101496,        87672,        76520, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       101497,        76520, ],
  }),
  ("nof_tree_events",                 92000),
  ("nof_db_events",                   92000),
  ("fsize_local",                     483651531), # 483.65MB, avg file size 483.65MB
  ("fsize_db",                        5565938746), # 5.57GB, avg file size 927.66MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_2000_hh_2b2t"),
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
    'Count'                                                                          : [       100000, ],
    'CountWeighted'                                                                  : [        99871,        99888,        99880, ],
    'CountWeightedLHEEnvelope'                                                       : [        99871,        99871, ],
    'CountWeightedL1PrefireNom'                                                      : [        95234,        95235,        95249, ],
    'CountWeightedL1Prefire'                                                         : [        95234,        94221,        96247, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [        95234,        95234, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     527708691), # 527.71MB, avg file size 527.71MB
  ("fsize_db",                        6456631366), # 6.46GB, avg file size 586.97MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_2500_hh_2b2t"),
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
    'Count'                                                                          : [       100000, ],
    'CountWeighted'                                                                  : [        99737,        99746,        99744, ],
    'CountWeightedLHEEnvelope'                                                       : [        99737,        99737, ],
    'CountWeightedL1PrefireNom'                                                      : [        95002,        95000,        95022, ],
    'CountWeightedL1Prefire'                                                         : [        95002,        93975,        96030, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [        95002,        95002, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     528249731), # 528.25MB, avg file size 528.25MB
  ("fsize_db",                        6431618251), # 6.43GB, avg file size 803.95MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_3000_hh_2b2t"),
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
    'Count'                                                                          : [       400000, ],
    'CountWeighted'                                                                  : [       399948,       399972,       399986, ],
    'CountWeightedLHEWeightScale'                                                    : [       404905,       399948,       392245,       404905,       399948,       392245,       404905,       399948,       392245, ],
    'CountWeightedLHEEnvelope'                                                       : [       404905,       392245, ],
    'CountWeightedL1PrefireNom'                                                      : [       392102,       392102,       392143, ],
    'CountWeightedL1Prefire'                                                         : [       392102,       390074,       394044, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       396901,       392102,       384576,       396901,       392102,       384576,       396901,       392102,       384576, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       396901,       384576, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1410772370), # 1.41GB, avg file size 1.41GB
  ("fsize_db",                        20195673518), # 20.20GB, avg file size 878.07MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_250_hh_2b2t"),
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
    'Count'                                                                          : [       384000, ],
    'CountWeighted'                                                                  : [       383963,       383923,       383971, ],
    'CountWeightedLHEWeightScale'                                                    : [       390007,       383963,       375523,       390007,       383963,       375523,       390007,       383963,       375523, ],
    'CountWeightedLHEEnvelope'                                                       : [       390007,       375523, ],
    'CountWeightedL1PrefireNom'                                                      : [       376052,       376016,       376063, ],
    'CountWeightedL1Prefire'                                                         : [       376052,       374024,       377991, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       381915,       376052,       367818,       381915,       376052,       367818,       381915,       376052,       367818, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       381915,       367818, ],
  }),
  ("nof_tree_events",                 384000),
  ("nof_db_events",                   384000),
  ("fsize_local",                     1380626556), # 1.38GB, avg file size 1.38GB
  ("fsize_db",                        19164112451), # 19.16GB, avg file size 1.13GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_260_hh_2b2t"),
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
    'Count'                                                                          : [       390000, ],
    'CountWeighted'                                                                  : [       389995,       389981,       389966, ],
    'CountWeightedLHEWeightScale'                                                    : [       397347,       389995,       380395,       397347,       389995,       380395,       397347,       389995,       380395, ],
    'CountWeightedLHEEnvelope'                                                       : [       397347,       380395, ],
    'CountWeightedL1PrefireNom'                                                      : [       381607,       381567,       381608, ],
    'CountWeightedL1Prefire'                                                         : [       381607,       379475,       383652, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       388743,       381607,       372261,       388743,       381607,       372261,       388743,       381607,       372261, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       388743,       372261, ],
  }),
  ("nof_tree_events",                 390000),
  ("nof_db_events",                   390000),
  ("fsize_local",                     1427577079), # 1.43GB, avg file size 1.43GB
  ("fsize_db",                        19739699313), # 19.74GB, avg file size 1.10GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_270_hh_2b2t"),
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
    'Count'                                                                          : [       379000, ],
    'CountWeighted'                                                                  : [       378993,       378961,       378972, ],
    'CountWeightedLHEWeightScale'                                                    : [       387251,       378993,       368745,       387251,       378993,       368745,       387251,       378993,       368745, ],
    'CountWeightedLHEEnvelope'                                                       : [       387251,       368745, ],
    'CountWeightedL1PrefireNom'                                                      : [       370464,       370422,       370469, ],
    'CountWeightedL1Prefire'                                                         : [       370464,       368319,       372531, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       378486,       370464,       360502,       378486,       370464,       360502,       378486,       370464,       360502, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       378486,       360502, ],
  }),
  ("nof_tree_events",                 379000),
  ("nof_db_events",                   379000),
  ("fsize_local",                     1411214870), # 1.41GB, avg file size 1.41GB
  ("fsize_db",                        19359006495), # 19.36GB, avg file size 967.95MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_280_hh_2b2t"),
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
    'Count'                                                                          : [        40000, ],
    'CountWeighted'                                                                  : [        39995,        39996,        39997, ],
    'CountWeightedLHEWeightScale'                                                    : [        41097,        39995,        38736,        41097,        39995,        38736,        41097,        39995,        38736, ],
    'CountWeightedLHEEnvelope'                                                       : [        41097,        38736, ],
    'CountWeightedL1PrefireNom'                                                      : [        39100,        39100,        39103, ],
    'CountWeightedL1Prefire'                                                         : [        39100,        38876,        39316, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [        40171,        39100,        37875,        40171,        39100,        37875,        40171,        39100,        37875, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [        40171,        37874, ],
  }),
  ("nof_tree_events",                 40000),
  ("nof_db_events",                   981549),
  ("fsize_local",                     154915548), # 154.92MB, avg file size 154.92MB
  ("fsize_db",                        50466696906), # 50.47GB, avg file size 1.53GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_300_hh_2b2t"),
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
    'Count'                                                                          : [       300000, ],
    'CountWeighted'                                                                  : [       300007,       299984,       300004, ],
    'CountWeightedLHEWeightScale'                                                    : [       312006,       300007,       287645,       312006,       300007,       287645,       312006,       300007,       287645, ],
    'CountWeightedLHEEnvelope'                                                       : [       312006,       287645, ],
    'CountWeightedL1PrefireNom'                                                      : [       291985,       291967,       291984, ],
    'CountWeightedL1Prefire'                                                         : [       291985,       290052,       293879, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       303603,       291985,       280010,       303603,       291985,       280010,       303603,       291985,       280010, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       303603,       280010, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1230381063), # 1.23GB, avg file size 1.23GB
  ("fsize_db",                        15849336173), # 15.85GB, avg file size 2.26GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_350_hh_2b2t"),
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
    'Count'                                                                          : [       300000, ],
    'CountWeighted'                                                                  : [       299926,       299960,       299987, ],
    'CountWeightedLHEWeightScale'                                                    : [       315132,       299926,       285254,       315132,       299926,       285254,       315132,       299926,       285254, ],
    'CountWeightedLHEEnvelope'                                                       : [       315132,       285254, ],
    'CountWeightedL1PrefireNom'                                                      : [       291312,       291324,       291358, ],
    'CountWeightedL1Prefire'                                                         : [       291312,       289277,       293320, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       305983,       291312,       277109,       305983,       291312,       277109,       305983,       291312,       277109, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       305983,       277109, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1296066271), # 1.30GB, avg file size 1.30GB
  ("fsize_db",                        16220410321), # 16.22GB, avg file size 1.08GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_400_hh_2b2t"),
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
    'Count'                                                                          : [       300000, ],
    'CountWeighted'                                                                  : [       299992,       299950,       299950, ],
    'CountWeightedLHEWeightScale'                                                    : [       317772,       299992,       283219,       317772,       299992,       283219,       317772,       299992,       283219, ],
    'CountWeightedLHEEnvelope'                                                       : [       317772,       283219, ],
    'CountWeightedL1PrefireNom'                                                      : [       291008,       290959,       290999, ],
    'CountWeightedL1Prefire'                                                         : [       291008,       288907,       293077, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       308184,       291008,       274810,       308184,       291008,       274810,       308184,       291008,       274810, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       308184,       274810, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1352970540), # 1.35GB, avg file size 1.35GB
  ("fsize_db",                        16455015197), # 16.46GB, avg file size 1.03GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_450_hh_2b2t"),
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
    'Count'                                                                          : [       200000, ],
    'CountWeighted'                                                                  : [       200002,       199984,       199951, ],
    'CountWeightedLHEWeightScale'                                                    : [       213369,       200002,       187635,       213369,       200002,       187635,       213369,       200002,       187635, ],
    'CountWeightedLHEEnvelope'                                                       : [       213369,       187635, ],
    'CountWeightedL1PrefireNom'                                                      : [       193804,       193789,       193779, ],
    'CountWeightedL1Prefire'                                                         : [       193804,       192372,       195216, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       206712,       193804,       181871,       206712,       193804,       181871,       206712,       193804,       181871, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       206712,       181871, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     934915296), # 934.92MB, avg file size 934.92MB
  ("fsize_db",                        11098842678), # 11.10GB, avg file size 1.39GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_500_hh_2b2t"),
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
    'Count'                                                                          : [       192000, ],
    'CountWeighted'                                                                  : [       191978,       191998,       191975, ],
    'CountWeightedLHEWeightScale'                                                    : [       206148,       191978,       179138,       206148,       191978,       179138,       206148,       191978,       179138, ],
    'CountWeightedLHEEnvelope'                                                       : [       206148,       179138, ],
    'CountWeightedL1PrefireNom'                                                      : [       186069,       186074,       186080, ],
    'CountWeightedL1Prefire'                                                         : [       186069,       184707,       187412, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       199749,       186069,       173662,       199749,       186069,       173662,       199749,       186069,       173662, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       199749,       173662, ],
  }),
  ("nof_tree_events",                 192000),
  ("nof_db_events",                   192000),
  ("fsize_local",                     926296631), # 926.30MB, avg file size 926.30MB
  ("fsize_db",                        10855478264), # 10.86GB, avg file size 775.39MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_550_hh_2b2t"),
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
    'Count'                                                                          : [       200000, ],
    'CountWeighted'                                                                  : [       199998,       199999,       199969, ],
    'CountWeightedLHEWeightScale'                                                    : [       215960,       199998,       185683,       215960,       199998,       185683,       215960,       199998,       185683, ],
    'CountWeightedLHEEnvelope'                                                       : [       215960,       185683, ],
    'CountWeightedL1PrefireNom'                                                      : [       193878,       193869,       193875, ],
    'CountWeightedL1Prefire'                                                         : [       193878,       192469,       195266, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       209300,       193878,       180040,       209300,       193878,       180040,       209300,       193878,       180040, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       209300,       180040, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     988260453), # 988.26MB, avg file size 988.26MB
  ("fsize_db",                        11487024358), # 11.49GB, avg file size 675.71MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_600_hh_2b2t"),
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
    'Count'                                                                          : [       188000, ],
    'CountWeighted'                                                                  : [       187974,       187960,       187970, ],
    'CountWeightedLHEWeightScale'                                                    : [       204001,       187973,       173747,       204001,       187973,       173747,       204001,       187973,       173747, ],
    'CountWeightedLHEEnvelope'                                                       : [       204001,       173747, ],
    'CountWeightedL1PrefireNom'                                                      : [       182149,       182129,       182161, ],
    'CountWeightedL1Prefire'                                                         : [       182149,       180814,       183466, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       197632,       182147,       168395,       197632,       182147,       168395,       197632,       182147,       168395, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       197632,       168395, ],
  }),
  ("nof_tree_events",                 188000),
  ("nof_db_events",                   188000),
  ("fsize_local",                     945712223), # 945.71MB, avg file size 945.71MB
  ("fsize_db",                        10754684541), # 10.75GB, avg file size 768.19MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_650_hh_2b2t"),
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
    'Count'                                                                          : [       200000, ],
    'CountWeighted'                                                                  : [       199984,       199981,       199952, ],
    'CountWeightedLHEWeightScale'                                                    : [       218959,       199982,       183379,       218959,       199982,       183379,       218959,       199982,       183379, ],
    'CountWeightedLHEEnvelope'                                                       : [       218959,       183379, ],
    'CountWeightedL1PrefireNom'                                                      : [       193809,       193791,       193804, ],
    'CountWeightedL1Prefire'                                                         : [       193809,       192400,       195199, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       212155,       193807,       177751,       212155,       193807,       177751,       212155,       193807,       177751, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       212155,       177751, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1030303915), # 1.03GB, avg file size 1.03GB
  ("fsize_db",                        11547164401), # 11.55GB, avg file size 888.24MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_750_hh_2b2t"),
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
    'Count'                                                                          : [       192000, ],
    'CountWeighted'                                                                  : [       191956,       191945,       191972, ],
    'CountWeightedLHEWeightScale'                                                    : [       210982,       191956,       175452,       210982,       191956,       175452,       210982,       191956,       175452, ],
    'CountWeightedLHEEnvelope'                                                       : [       210982,       175452, ],
    'CountWeightedL1PrefireNom'                                                      : [       186175,       186158,       186192, ],
    'CountWeightedL1Prefire'                                                         : [       186175,       184856,       187479, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       204586,       186175,       170193,       204586,       186175,       170193,       204586,       186175,       170193, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       204586,       170193, ],
  }),
  ("nof_tree_events",                 192000),
  ("nof_db_events",                   192000),
  ("fsize_local",                     997914058), # 997.91MB, avg file size 997.91MB
  ("fsize_db",                        11179122535), # 11.18GB, avg file size 1.02GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_800_hh_2b2t"),
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
    'Count'                                                                          : [       369000, ],
    'CountWeighted'                                                                  : [       365800,       365894,       365880, ],
    'CountWeightedLHEEnvelope'                                                       : [       365800,       365800, ],
    'CountWeightedL1PrefireNom'                                                      : [       344775,       344772,       344848, ],
    'CountWeightedL1Prefire'                                                         : [       344775,       339838,       349657, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       344775,       344775, ],
  }),
  ("nof_tree_events",                 369000),
  ("nof_db_events",                   369000),
  ("fsize_local",                     1596333739), # 1.60GB, avg file size 1.60GB
  ("fsize_db",                        20317409524), # 20.32GB, avg file size 781.44MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_0_hh_2b2t"),
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
    'Count'                                                                          : [       300000, ],
    'CountWeighted'                                                                  : [       297139,       297153,       297192, ],
    'CountWeightedLHEEnvelope'                                                       : [       297139,       297139, ],
    'CountWeightedL1PrefireNom'                                                      : [       277516,       277506,       277540, ],
    'CountWeightedL1Prefire'                                                         : [       277516,       272964,       282033, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       277516,       277516, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1303257918), # 1.30GB, avg file size 1.30GB
  ("fsize_db",                        16551491719), # 16.55GB, avg file size 827.57MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_1_hh_2b2t"),
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
    'Count'                                                                          : [       400000, ],
    'CountWeighted'                                                                  : [       396242,       396300,       396267, ],
    'CountWeightedLHEEnvelope'                                                       : [       396242,       396242, ],
    'CountWeightedL1PrefireNom'                                                      : [       363531,       363512,       363578, ],
    'CountWeightedL1Prefire'                                                         : [       363531,       356197,       370859, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       363531,       363531, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1849435274), # 1.85GB, avg file size 1.85GB
  ("fsize_db",                        22555887148), # 22.56GB, avg file size 2.51GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_2_hh_2b2t"),
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
    'Count'                                                                          : [       400000, ],
    'CountWeighted'                                                                  : [       392905,       392917,       392980, ],
    'CountWeightedLHEEnvelope'                                                       : [       392905,       392905, ],
    'CountWeightedL1PrefireNom'                                                      : [       364734,       364695,       364803, ],
    'CountWeightedL1Prefire'                                                         : [       364734,       358513,       370966, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       364734,       364734, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     2087508594), # 2.09GB, avg file size 2.09GB
  ("fsize_db",                        23834632407), # 23.83GB, avg file size 993.11MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_2_1_hh_2b2t"),
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
    'Count'                                                                          : [       392000, ],
    'CountWeighted'                                                                  : [       386922,       387034,       386937, ],
    'CountWeightedLHEEnvelope'                                                       : [       386922,       386922, ],
    'CountWeightedL1PrefireNom'                                                      : [       361216,       361241,       361248, ],
    'CountWeightedL1Prefire'                                                         : [       361216,       355369,       367040, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       361216,       361216, ],
  }),
  ("nof_tree_events",                 392000),
  ("nof_db_events",                   392000),
  ("fsize_local",                     1859105546), # 1.86GB, avg file size 1.86GB
  ("fsize_db",                        22237635973), # 22.24GB, avg file size 1.39GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1p5_1_1_hh_2b2t"),
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
    'Count'                                                                          : [       380000, ],
    'CountWeighted'                                                                  : [       380005,       379962,       380039, ],
    'CountWeightedLHEWeightScale'                                                    : [       486390,       459104,       433467,       402655,       380003,       358695,       339105,       319932,       301971, ],
    'CountWeightedLHEEnvelope'                                                       : [       486390,       301970, ],
    'CountWeightedL1PrefireNom'                                                      : [       367952,       367906,       367987, ],
    'CountWeightedL1Prefire'                                                         : [       367952,       365108,       370746, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       470847,       444579,       419883,       389768,       367949,       347435,       328236,       309786,       292481, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       470847,       292481, ],
  }),
  ("nof_tree_events",                 380000),
  ("nof_db_events",                   380000),
  ("fsize_local",                     1670447992), # 1.67GB, avg file size 1.67GB
  ("fsize_db",                        20440095707), # 20.44GB, avg file size 1.14GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_sm_hh_2b2t"),
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
    'Count'                                                                          : [       392000, ],
    'CountWeighted'                                                                  : [       392000,       391922,       391981, ],
    'CountWeightedLHEWeightScale'                                                    : [       509246,       469269,       434113,       425550,       392000,       362403,       361237,       332538,       307370, ],
    'CountWeightedLHEEnvelope'                                                       : [       509246,       307370, ],
    'CountWeightedL1PrefireNom'                                                      : [       377804,       377736,       377805, ],
    'CountWeightedL1Prefire'                                                         : [       377804,       374542,       381018, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       490647,       452347,       418639,       409966,       377804,       349450,       347976,       320488,       296357, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       490647,       296357, ],
  }),
  ("nof_tree_events",                 392000),
  ("nof_db_events",                   392000),
  ("fsize_local",                     1876509127), # 1.88GB, avg file size 1.88GB
  ("fsize_db",                        22130629455), # 22.13GB, avg file size 1.58GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_2_hh_2b2t"),
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
    'Count'                                                                          : [       396000, ],
    'CountWeighted'                                                                  : [       396011,       395854,       396019, ],
    'CountWeightedLHEWeightScale'                                                    : [       506923,       478366,       451560,       419680,       396003,       373716,       353457,       333432,       314657, ],
    'CountWeightedLHEEnvelope'                                                       : [       506923,       314657, ],
    'CountWeightedL1PrefireNom'                                                      : [       383324,       383203,       383347, ],
    'CountWeightedL1Prefire'                                                         : [       383324,       380331,       386257, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       490559,       463075,       437248,       406115,       383318,       361858,       342021,       322750,       304662, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       490560,       304662, ],
  }),
  ("nof_tree_events",                 396000),
  ("nof_db_events",                   396000),
  ("fsize_local",                     1749084041), # 1.75GB, avg file size 1.75GB
  ("fsize_db",                        21371438091), # 21.37GB, avg file size 971.43MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_3_hh_2b2t"),
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
    'Count'                                                                          : [       400000, ],
    'CountWeighted'                                                                  : [       399990,       399952,       399974, ],
    'CountWeightedLHEWeightScale'                                                    : [       510036,       484402,       459732,       421208,       399990,       379554,       354002,       336103,       318934, ],
    'CountWeightedLHEEnvelope'                                                       : [       510036,       318934, ],
    'CountWeightedL1PrefireNom'                                                      : [       387769,       387734,       387767, ],
    'CountWeightedL1Prefire'                                                         : [       387769,       384859,       390615, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       494330,       469627,       445826,       408222,       387769,       368062,       343078,       325834,       309266, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       494330,       309266, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1719811132), # 1.72GB, avg file size 1.72GB
  ("fsize_db",                        21451946375), # 21.45GB, avg file size 1.02GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_4_hh_2b2t"),
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
    'Count'                                                                          : [       376000, ],
    'CountWeighted'                                                                  : [       375979,       375921,       376006, ],
    'CountWeightedLHEWeightScale'                                                    : [       479495,       455283,       432003,       396004,       375979,       356709,       332838,       315959,       299750, ],
    'CountWeightedLHEEnvelope'                                                       : [       479495,       299750, ],
    'CountWeightedL1PrefireNom'                                                      : [       364480,       364428,       364509, ],
    'CountWeightedL1Prefire'                                                         : [       364480,       361744,       367161, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       464718,       441380,       418918,       383790,       364480,       345894,       322564,       306293,       290656, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       464718,       290656, ],
  }),
  ("nof_tree_events",                 376000),
  ("nof_db_events",                   376000),
  ("fsize_local",                     1618088881), # 1.62GB, avg file size 1.62GB
  ("fsize_db",                        20190349511), # 20.19GB, avg file size 1.26GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_7_hh_2b2t"),
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
    'Count'                                                                          : [       400000, ],
    'CountWeighted'                                                                  : [       399981,       399864,       399967, ],
    'CountWeightedLHEWeightScale'                                                    : [       519421,       478877,       443039,       433940,       399981,       369934,       368229,       339294,       313779, ],
    'CountWeightedLHEEnvelope'                                                       : [       519421,       313779, ],
    'CountWeightedL1PrefireNom'                                                      : [       385405,       385304,       385421, ],
    'CountWeightedL1Prefire'                                                         : [       385405,       382052,       388719, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       500358,       461461,       427065,       417991,       385405,       356577,       354678,       326927,       302436, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       500358,       302436, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1934491450), # 1.93GB, avg file size 1.93GB
  ("fsize_db",                        22924430937), # 22.92GB, avg file size 1.27GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_9_hh_2b2t"),
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
    'Count'                                                                          : [       400000, ],
    'CountWeighted'                                                                  : [       399989,       400042,       399952, ],
    'CountWeightedLHEWeightScale'                                                    : [       509963,       484459,       459890,       421090,       399989,       379656,       353864,       336081,       318979, ],
    'CountWeightedLHEEnvelope'                                                       : [       509963,       318979, ],
    'CountWeightedL1PrefireNom'                                                      : [       387785,       387792,       387776, ],
    'CountWeightedL1Prefire'                                                         : [       387785,       384879,       390626, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [       494284,       469697,       445988,       408130,       387783,       368169,       342963,       325823,       309322, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [       494284,       309322, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1717419913), # 1.72GB, avg file size 1.72GB
  ("fsize_db",                        21176117597), # 21.18GB, avg file size 2.12GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_12_hh_2b2t"),
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

