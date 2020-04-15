from collections import OrderedDict as OD

# file generated at 2020-04-15 16:23:39 with the following command:
# create_dictionary.py -m python/samples/metaDict_2017_hh.py -p /hdfs/local/acaan/addMEM/2017/addMEM_hh_bb2l_03April20_BDT_nom/final_ntuples/hh_bb2l -N samples_2017 -E 2017 -o python/samples -g hhAnalyzeSamples_2017_hh_MEM_bb2l_BDT.py -M

samples_2017 = OD()
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
  ("nof_tree_events",                 157057),
  ("nof_db_events",                   388999),
  ("fsize_local",                     662725041), # 662.73MB, avg file size 662.73MB
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
        ("path",      "/hdfs/local/acaan/addMEM/2017/addMEM_hh_bb2l_03April20_BDT_nom/final_ntuples/hh_bb2l/signal_ggf_nonresonant_node_sm_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 162103),
  ("nof_db_events",                   400000),
  ("fsize_local",                     711578893), # 711.58MB, avg file size 711.58MB
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
        ("path",      "/hdfs/local/acaan/addMEM/2017/addMEM_hh_bb2l_03April20_BDT_nom/final_ntuples/hh_bb2l/signal_ggf_nonresonant_node_2_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 153779),
  ("nof_db_events",                   380000),
  ("fsize_local",                     650622451), # 650.62MB, avg file size 650.62MB
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
        ("path",      "/hdfs/local/acaan/addMEM/2017/addMEM_hh_bb2l_03April20_BDT_nom/final_ntuples/hh_bb2l/signal_ggf_nonresonant_node_3_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 157706),
  ("nof_db_events",                   392999),
  ("fsize_local",                     658014745), # 658.01MB, avg file size 658.01MB
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
        ("path",      "/hdfs/local/acaan/addMEM/2017/addMEM_hh_bb2l_03April20_BDT_nom/final_ntuples/hh_bb2l/signal_ggf_nonresonant_node_7_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 156107),
  ("nof_db_events",                   386999),
  ("fsize_local",                     693067396), # 693.07MB, avg file size 693.07MB
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
        ("path",      "/hdfs/local/acaan/addMEM/2017/addMEM_hh_bb2l_03April20_BDT_nom/final_ntuples/hh_bb2l/signal_ggf_nonresonant_node_9_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 161535),
  ("nof_db_events",                   400000),
  ("fsize_local",                     671579056), # 671.58MB, avg file size 671.58MB
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
        ("path",      "/hdfs/local/acaan/addMEM/2017/addMEM_hh_bb2l_03April20_BDT_nom/final_ntuples/hh_bb2l/signal_ggf_nonresonant_node_12_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 462986),
  ("nof_db_events",                   779989),
  ("fsize_local",                     1781019289), # 1.78GB, avg file size 890.51MB
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
        ("path",      "/hdfs/local/acaan/addMEM/2017/addMEM_hh_bb2l_03April20_BDT_nom/final_ntuples/hh_bb2l/signal_ggf_nonresonant_node_sm_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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

