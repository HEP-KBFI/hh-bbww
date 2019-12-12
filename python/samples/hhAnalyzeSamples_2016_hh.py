from collections import OrderedDict as OD

# file generated at 2019-12-09 04:47:39 with the following command:
# create_dictionary.py -m python/samples/metaDict_2016_hh.py -p /hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples -N samples_2016 -E 2016 -o python/samples -g hhAnalyzeSamples_2016_hh.py -M

samples_2016 = OD()
samples_2016["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-260_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_260_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_260_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299998, ],
    'CountWeighted'                                              : [       300004,       299995,       300046, ],
    'CountWeightedLHEWeightScale'                                : [       305752,       300004,       292733,       305752,       300004,       292733,       305752,       300004,       292733, ],
    'CountWeightedL1PrefireNom'                                  : [       295862,       295852,       295898, ],
    'CountWeightedL1Prefire'                                     : [       295862,       294761,       296959, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       301503,       295861,       288717,       301503,       295861,       288717,       301503,       295861,       288717, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     915607895), # 915.61MB, avg file size 915.61MB
  ("fsize_db",                        11821300223), # 11.82GB, avg file size 2.96GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_260_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-270_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_270_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_270_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       294629, ],
    'CountWeighted'                                              : [       294641,       294646,       294624, ],
    'CountWeightedLHEWeightScale'                                : [       301127,       294639,       286780,       301127,       294639,       286780,       301127,       294639,       286780, ],
    'CountWeightedL1PrefireNom'                                  : [       290405,       290402,       290404, ],
    'CountWeightedL1Prefire'                                     : [       290405,       289282,       291520, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       296772,       290402,       282690,       296772,       290402,       282690,       296772,       290402,       282690, ],
  }),
  ("nof_tree_events",                 294629),
  ("nof_db_events",                   294629),
  ("fsize_local",                     909837438), # 909.84MB, avg file size 909.84MB
  ("fsize_db",                        11694604529), # 11.69GB, avg file size 3.90GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_270_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-300_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_300_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_300_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       299984,       299961,       300056, ],
    'CountWeightedLHEWeightScale'                                : [       308988,       299983,       290128,       308988,       299983,       290128,       308988,       299983,       290128, ],
    'CountWeightedL1PrefireNom'                                  : [       295359,       295339,       295414, ],
    'CountWeightedL1Prefire'                                     : [       295359,       294145,       296569, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       304182,       295356,       285680,       304182,       295356,       285680,       304182,       295356,       285680, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     957199789), # 957.20MB, avg file size 957.20MB
  ("fsize_db",                        12121761327), # 12.12GB, avg file size 3.03GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_300_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-350_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_350_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_350_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       295149, ],
    'CountWeighted'                                              : [       295268,       295216,       295146, ],
    'CountWeightedLHEWeightScale'                                : [       307330,       295247,       282815,       307330,       295247,       282815,       307330,       295247,       282815, ],
    'CountWeightedL1PrefireNom'                                  : [       290107,       290071,       290036, ],
    'CountWeightedL1Prefire'                                     : [       290107,       288787,       291419, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       301961,       290093,       277947,       301961,       290093,       277947,       301961,       290093,       277947, ],
  }),
  ("nof_tree_events",                 295149),
  ("nof_db_events",                   295149),
  ("fsize_local",                     988236417), # 988.24MB, avg file size 988.24MB
  ("fsize_db",                        12270587874), # 12.27GB, avg file size 2.45GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_350_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-400_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_400_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_400_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299997, ],
    'CountWeighted'                                              : [       300074,       299993,       300004, ],
    'CountWeightedLHEWeightScale'                                : [       315263,       300072,       285213,       315263,       300072,       285213,       315263,       300072,       285213, ],
    'CountWeightedL1PrefireNom'                                  : [       294387,       294337,       294358, ],
    'CountWeightedL1Prefire'                                     : [       294387,       292946,       295825, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       309275,       294384,       279875,       309275,       294384,       279875,       309275,       294384,       279875, ],
  }),
  ("nof_tree_events",                 299997),
  ("nof_db_events",                   299997),
  ("fsize_local",                     1043365593), # 1.04GB, avg file size 1.04GB
  ("fsize_db",                        12763369067), # 12.76GB, avg file size 3.19GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_400_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-450_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_450_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_450_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       296256, ],
    'CountWeighted'                                              : [       296242,       296282,       296272, ],
    'CountWeightedLHEWeightScale'                                : [       313768,       296240,       279794,       313768,       296240,       279794,       313768,       296240,       279794, ],
    'CountWeightedL1PrefireNom'                                  : [       290340,       290360,       290358, ],
    'CountWeightedL1Prefire'                                     : [       290340,       288851,       291825, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       307458,       290337,       274249,       307458,       290337,       274249,       307458,       290337,       274249, ],
  }),
  ("nof_tree_events",                 296256),
  ("nof_db_events",                   296256),
  ("fsize_local",                     1065495437), # 1.07GB, avg file size 1.07GB
  ("fsize_db",                        12817875328), # 12.82GB, avg file size 3.20GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_450_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-500_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_500_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_500_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       299965,       299952,       299983, ],
    'CountWeightedLHEWeightScale'                                : [       319918,       299965,       281656,       319918,       299965,       281656,       319918,       299965,       281656, ],
    'CountWeightedL1PrefireNom'                                  : [       293749,       293736,       293771, ],
    'CountWeightedL1Prefire'                                     : [       293749,       292193,       295309, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       313224,       293747,       275849,       313224,       293747,       275849,       313224,       293747,       275849, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1111014186), # 1.11GB, avg file size 1.11GB
  ("fsize_db",                        13281765633), # 13.28GB, avg file size 2.66GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_500_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-550_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_550_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_550_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       299981,       300021,       300062, ],
    'CountWeightedLHEWeightScale'                                : [       321842,       299978,       280187,       321842,       299978,       280187,       321842,       299978,       280187, ],
    'CountWeightedL1PrefireNom'                                  : [       293497,       293506,       293557, ],
    'CountWeightedL1Prefire'                                     : [       293497,       291885,       295106, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       314824,       293494,       274163,       314824,       293494,       274163,       314824,       293494,       274163, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1138886757), # 1.14GB, avg file size 1.14GB
  ("fsize_db",                        13529956556), # 13.53GB, avg file size 2.71GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_550_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-600_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_600_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_600_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       299980,       299991,       300035, ],
    'CountWeightedLHEWeightScale'                                : [       323626,       299979,       278866,       323626,       299979,       278866,       323626,       299979,       278866, ],
    'CountWeightedL1PrefireNom'                                  : [       293316,       293319,       293347, ],
    'CountWeightedL1Prefire'                                     : [       293316,       291665,       294968, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       316378,       293314,       272699,       316378,       293314,       272699,       316378,       293314,       272699, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1161076284), # 1.16GB, avg file size 1.16GB
  ("fsize_db",                        13674104858), # 13.67GB, avg file size 3.42GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_600_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-650_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_650_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_650_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       299538, ],
    'CountWeighted'                                              : [       299467,       299550,       299598, ],
    'CountWeightedLHEWeightScale'                                : [       324727,       299466,       277246,       324727,       299466,       277246,       324727,       299466,       277246, ],
    'CountWeightedL1PrefireNom'                                  : [       292651,       292703,       292723, ],
    'CountWeightedL1Prefire'                                     : [       292651,       290968,       294337, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       317254,       292648,       270942,       317254,       292648,       270942,       317254,       292648,       270942, ],
  }),
  ("nof_tree_events",                 299538),
  ("nof_db_events",                   299538),
  ("fsize_local",                     1177903392), # 1.18GB, avg file size 1.18GB
  ("fsize_db",                        13997216210), # 14.00GB, avg file size 2.80GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_650_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-750_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_750_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_750_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       298727, ],
    'CountWeighted'                                              : [       298779,       298723,       298729, ],
    'CountWeightedLHEWeightScale'                                : [       326694,       298769,       274381,       326694,       298769,       274381,       326694,       298769,       274381, ],
    'CountWeightedL1PrefireNom'                                  : [       291625,       291585,       291608, ],
    'CountWeightedL1Prefire'                                     : [       291625,       289880,       293371, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       318846,       291617,       267862,       318846,       291617,       267862,       318846,       291617,       267862, ],
  }),
  ("nof_tree_events",                 298727),
  ("nof_db_events",                   298727),
  ("fsize_local",                     1200865535), # 1.20GB, avg file size 1.20GB
  ("fsize_db",                        13966996917), # 13.97GB, avg file size 4.66GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_750_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-800_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_800_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_800_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       299705, ],
    'CountWeighted'                                              : [       299677,       299776,       299777, ],
    'CountWeightedLHEWeightScale'                                : [       329029,       299674,       274337,       329029,       299674,       274337,       329029,       299674,       274337, ],
    'CountWeightedL1PrefireNom'                                  : [       292537,       292584,       292603, ],
    'CountWeightedL1Prefire'                                     : [       292537,       290793,       294282, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       321133,       292534,       267826,       321133,       292534,       267826,       321133,       292534,       267826, ],
  }),
  ("nof_tree_events",                 299705),
  ("nof_db_events",                   299705),
  ("fsize_local",                     1214494817), # 1.21GB, avg file size 1.21GB
  ("fsize_db",                        14140095303), # 14.14GB, avg file size 4.71GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_800_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-900_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_900_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_900_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       298733, ],
    'CountWeighted'                                              : [       298741,       298821,       298716, ],
    'CountWeightedLHEWeightScale'                                : [       330287,       298739,       271774,       330287,       298739,       271774,       330287,       298739,       271774, ],
    'CountWeightedL1PrefireNom'                                  : [       291481,       291511,       291477, ],
    'CountWeightedL1Prefire'                                     : [       291481,       289718,       293248, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       322219,       291478,       265201,       322219,       291478,       265201,       322219,       291478,       265201, ],
  }),
  ("nof_tree_events",                 298733),
  ("nof_db_events",                   298733),
  ("fsize_local",                     1226394118), # 1.23GB, avg file size 1.23GB
  ("fsize_db",                        14389658695), # 14.39GB, avg file size 4.80GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_900_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-1000_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1000_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_1000_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       300033,       299944,       299984, ],
    'CountWeightedLHEWeightScale'                                : [       333750,       300033,       271427,       333750,       300033,       271427,       333750,       300033,       271427, ],
    'CountWeightedL1PrefireNom'                                  : [       292565,       292502,       292547, ],
    'CountWeightedL1Prefire'                                     : [       292565,       290763,       294373, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       325422,       292563,       264713,       325422,       292563,       264713,       325422,       292563,       264713, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1245432426), # 1.25GB, avg file size 1.25GB
  ("fsize_db",                        14685031472), # 14.69GB, avg file size 3.67GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1000_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-260_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_260_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_260_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       299904,       300065,       300024, ],
    'CountWeightedLHEWeightScale'                                : [       305771,       299904,       292706,       305771,       299904,       292706,       305771,       299904,       292706, ],
    'CountWeightedL1PrefireNom'                                  : [       295626,       295715,       295712, ],
    'CountWeightedL1Prefire'                                     : [       295626,       294482,       296761, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       301339,       295625,       288522,       301339,       295625,       288522,       301339,       295625,       288522, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     931936565), # 931.94MB, avg file size 931.94MB
  ("fsize_db",                        12205401208), # 12.21GB, avg file size 4.07GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_260_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-270_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_270_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_270_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       299993,       299993,       300024, ],
    'CountWeightedLHEWeightScale'                                : [       306610,       299992,       292026,       306610,       299992,       292026,       306610,       299992,       292026, ],
    'CountWeightedL1PrefireNom'                                  : [       295584,       295582,       295613, ],
    'CountWeightedL1Prefire'                                     : [       295584,       294420,       296744, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       302071,       295582,       287763,       302071,       295582,       287763,       302071,       295582,       287763, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     943570614), # 943.57MB, avg file size 943.57MB
  ("fsize_db",                        12216222977), # 12.22GB, avg file size 4.07GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_270_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-300_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_300_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_300_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       300075,       299971,       300036, ],
    'CountWeightedLHEWeightScale'                                : [       308996,       300054,       290112,       308996,       300054,       290112,       308996,       300054,       290112, ],
    'CountWeightedL1PrefireNom'                                  : [       295218,       295147,       295208, ],
    'CountWeightedL1Prefire'                                     : [       295218,       293963,       296471, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       303985,       295204,       285481,       303985,       295204,       285481,       303985,       295204,       285481, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     980911276), # 980.91MB, avg file size 980.91MB
  ("fsize_db",                        12432044182), # 12.43GB, avg file size 4.14GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_300_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-350_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_350_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_350_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       299953,       300004,       300078, ],
    'CountWeightedLHEWeightScale'                                : [       312408,       299952,       287449,       312408,       299952,       287449,       312408,       299952,       287449, ],
    'CountWeightedL1PrefireNom'                                  : [       294676,       294706,       294756, ],
    'CountWeightedL1Prefire'                                     : [       294676,       293321,       296027, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       306842,       294674,       282415,       306842,       294674,       282415,       306842,       294674,       282415, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1031086945), # 1.03GB, avg file size 1.03GB
  ("fsize_db",                        12931701996), # 12.93GB, avg file size 3.23GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_350_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-400_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_400_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_400_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       300026,       299989,       299948, ],
    'CountWeightedLHEWeightScale'                                : [       315235,       300020,       285238,       315235,       300020,       285238,       315235,       300020,       285238, ],
    'CountWeightedL1PrefireNom'                                  : [       294522,       294496,       294484, ],
    'CountWeightedL1Prefire'                                     : [       294522,       293134,       295914, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       309408,       294517,       280059,       309408,       294517,       280059,       309408,       294517,       280059, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1075110513), # 1.08GB, avg file size 1.08GB
  ("fsize_db",                        13138610285), # 13.14GB, avg file size 4.38GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_400_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-450_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_450_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_450_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       299961,       300060,       299988, ],
    'CountWeightedLHEWeightScale'                                : [       317714,       299961,       283327,       317714,       299961,       283327,       317714,       299961,       283327, ],
    'CountWeightedL1PrefireNom'                                  : [       294275,       294316,       294309, ],
    'CountWeightedL1Prefire'                                     : [       294275,       292852,       295700, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       311622,       294274,       277986,       311622,       294274,       277986,       311622,       294274,       277986, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1114371165), # 1.11GB, avg file size 1.11GB
  ("fsize_db",                        13501491108), # 13.50GB, avg file size 3.38GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_450_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-500_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_500_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_500_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       300033,       299950,       299932, ],
    'CountWeightedLHEWeightScale'                                : [       319897,       300031,       281654,       319897,       300031,       281654,       319897,       300031,       281654, ],
    'CountWeightedL1PrefireNom'                                  : [       294236,       294175,       294180, ],
    'CountWeightedL1Prefire'                                     : [       294236,       292797,       295670, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       313673,       294233,       276265,       313673,       294233,       276265,       313673,       294233,       276265, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1148478936), # 1.15GB, avg file size 1.15GB
  ("fsize_db",                        13733577571), # 13.73GB, avg file size 4.58GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_500_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-550_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_550_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_550_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       300017,       300029,       299980, ],
    'CountWeightedLHEWeightScale'                                : [       321864,       300010,       280186,       321864,       300010,       280186,       321864,       300010,       280186, ],
    'CountWeightedL1PrefireNom'                                  : [       294119,       294115,       294102, ],
    'CountWeightedL1Prefire'                                     : [       294119,       292663,       295571, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       315485,       294113,       274720,       315485,       294113,       274720,       315485,       294113,       274720, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1175444901), # 1.18GB, avg file size 1.18GB
  ("fsize_db",                        13919729330), # 13.92GB, avg file size 4.64GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_550_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-600_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_600_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_600_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       299969,       300036,       299992, ],
    'CountWeightedLHEWeightScale'                                : [       323617,       299968,       278860,       323617,       299968,       278860,       323617,       299968,       278860, ],
    'CountWeightedL1PrefireNom'                                  : [       294145,       294176,       294165, ],
    'CountWeightedL1Prefire'                                     : [       294145,       292711,       295582, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       317272,       294142,       273471,       317272,       294142,       273471,       317272,       294142,       273471, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1197032988), # 1.20GB, avg file size 1.20GB
  ("fsize_db",                        14074430864), # 14.07GB, avg file size 4.69GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_600_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-650_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_650_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_650_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                      : [       298806, ],
    'CountWeighted'                                              : [       298810,       298869,       298784, ],
    'CountWeightedLHEWeightScale'                                : [       323946,       298800,       276575,       323946,       298800,       276575,       323946,       298800,       276575, ],
    'CountWeightedL1PrefireNom'                                  : [       292959,       292990,       292955, ],
    'CountWeightedL1Prefire'                                     : [       292959,       291527,       294393, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       317559,       292951,       271188,       317559,       292951,       271188,       317559,       292951,       271188, ],
  }),
  ("nof_tree_events",                 298806),
  ("nof_db_events",                   298806),
  ("fsize_local",                     1207883657), # 1.21GB, avg file size 1.21GB
  ("fsize_db",                        14346261466), # 14.35GB, avg file size 2.39GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_650_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-700_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_700_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_700_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       300047,       299947,       299948, ],
    'CountWeightedLHEWeightScale'                                : [       326704,       300039,       276567,       326704,       300039,       276567,       326704,       300039,       276567, ],
    'CountWeightedL1PrefireNom'                                  : [       294197,       294140,       294137, ],
    'CountWeightedL1Prefire'                                     : [       294197,       292775,       295623, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       320316,       294191,       271221,       320316,       294191,       271221,       320316,       294191,       271221, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1224308205), # 1.22GB, avg file size 1.22GB
  ("fsize_db",                        14636315935), # 14.64GB, avg file size 4.88GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_700_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-800_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_800_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_800_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       300031,       299922,       299915, ],
    'CountWeightedLHEWeightScale'                                : [       329351,       300024,       274606,       329351,       300024,       274606,       329351,       300024,       274606, ],
    'CountWeightedL1PrefireNom'                                  : [       294263,       294188,       294190, ],
    'CountWeightedL1Prefire'                                     : [       294263,       292859,       295665, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       323004,       294256,       269359,       323004,       294256,       269359,       323004,       294256,       269359, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1241995680), # 1.24GB, avg file size 1.24GB
  ("fsize_db",                        14673528101), # 14.67GB, avg file size 3.67GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_800_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-900_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_900_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_900_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       299984,       299965,       300006, ],
    'CountWeightedLHEWeightScale'                                : [       331710,       299979,       272939,       331710,       299979,       272939,       331710,       299979,       272939, ],
    'CountWeightedL1PrefireNom'                                  : [       294246,       294229,       294266, ],
    'CountWeightedL1Prefire'                                     : [       294246,       292851,       295643, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       325332,       294242,       267728,       325332,       294242,       267728,       325332,       294242,       267728, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1254097244), # 1.25GB, avg file size 1.25GB
  ("fsize_db",                        15011560063), # 15.01GB, avg file size 5.00GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_900_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1000_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1000_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_1000_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       299118, ],
    'CountWeighted'                                              : [       299112,       299138,       299190, ],
    'CountWeightedLHEWeightScale'                                : [       332789,       299108,       270645,       332789,       299108,       270645,       332789,       299108,       270645, ],
    'CountWeightedL1PrefireNom'                                  : [       293385,       293388,       293456, ],
    'CountWeightedL1Prefire'                                     : [       293385,       291999,       294776, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       326394,       293381,       265477,       326394,       293381,       265477,       326394,       293381,       265477, ],
  }),
  ("nof_tree_events",                 299118),
  ("nof_db_events",                   299118),
  ("fsize_local",                     1259806974), # 1.26GB, avg file size 1.26GB
  ("fsize_db",                        15065557472), # 15.07GB, avg file size 5.02GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_1000_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_1_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_1_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_1_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       300021,       300025,       299979, ],
    'CountWeightedLHEWeightScale'                                : [       326212,       300021,       277737,       326212,       300021,       277737,       326212,       300021,       277737, ],
    'CountWeightedL1PrefireNom'                                  : [       288365,       288365,       288355, ],
    'CountWeightedL1Prefire'                                     : [       288365,       285462,       291269, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       313353,       288362,       267104,       313353,       288362,       267104,       313353,       288362,       267104, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1079218069), # 1.08GB, avg file size 1.08GB
  ("fsize_db",                        12626803802), # 12.63GB, avg file size 4.21GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_1_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_2_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_2_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_2_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       300041,       299894,       299993, ],
    'CountWeightedLHEWeightScale'                                : [       324928,       300041,       278756,       324928,       300041,       278756,       324928,       300041,       278756, ],
    'CountWeightedL1PrefireNom'                                  : [       285211,       285159,       285210, ],
    'CountWeightedL1Prefire'                                     : [       285211,       281653,       288788, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       308640,       285208,       265199,       308640,       285208,       265199,       308640,       285208,       265199, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1138738995), # 1.14GB, avg file size 1.14GB
  ("fsize_db",                        13505935893), # 13.51GB, avg file size 2.25GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_2_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_2_C3_1_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_2_1_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_2_1_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       299951,       299977,       299991, ],
    'CountWeightedLHEWeightScale'                                : [       338116,       299951,       269640,       338116,       299951,       269640,       338116,       299951,       269640, ],
    'CountWeightedL1PrefireNom'                                  : [       287335,       287331,       287364, ],
    'CountWeightedL1Prefire'                                     : [       287335,       284341,       290344, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       323762,       287333,       258353,       323762,       287333,       258353,       323762,       287333,       258353, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1236320703), # 1.24GB, avg file size 1.24GB
  ("fsize_db",                        14484771487), # 14.48GB, avg file size 2.41GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_2_1_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_0_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_0_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_0_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       300040,       299904,       299954, ],
    'CountWeightedLHEWeightScale'                                : [       322426,       300037,       280507,       322426,       300037,       280507,       322426,       300037,       280507, ],
    'CountWeightedL1PrefireNom'                                  : [       289896,       289851,       289858, ],
    'CountWeightedL1Prefire'                                     : [       289896,       287342,       292448, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       311374,       289892,       271175,       311374,       289892,       271175,       311374,       289892,       271175, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1078441240), # 1.08GB, avg file size 1.08GB
  ("fsize_db",                        13033305340), # 13.03GB, avg file size 3.26GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_0_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2VTo2L2Nu_CV_1_5_C2V_1_C3_1_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1p5_1_1_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_nonresonant_1p5_1_1_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       299402, ],
    'CountWeighted'                                              : [       299408,       299349,       299474, ],
    'CountWeightedLHEWeightScale'                                : [       329955,       299404,       274211,       329955,       299404,       274211,       329955,       299404,       274211, ],
    'CountWeightedL1PrefireNom'                                  : [       287829,       287800,       287858, ],
    'CountWeightedL1Prefire'                                     : [       287829,       284997,       290670, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       317007,       287825,       263748,       317007,       287825,       263748,       317007,       287825,       263748, ],
  }),
  ("nof_tree_events",                 299402),
  ("nof_db_events",                   299402),
  ("fsize_local",                     1153496527), # 1.15GB, avg file size 1.15GB
  ("fsize_db",                        13628421160), # 13.63GB, avg file size 2.73GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1p5_1_1_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2VTo2L2Nu_CV_0_5_C2V_1_C3_1_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_0p5_1_1_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_nonresonant_0p5_1_1_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       297179, ],
    'CountWeighted'                                              : [       297192,       297162,       297150, ],
    'CountWeightedLHEWeightScale'                                : [       332159,       297190,       269009,       332159,       297190,       269009,       332159,       297190,       269009, ],
    'CountWeightedL1PrefireNom'                                  : [       285149,       285125,       285143, ],
    'CountWeightedL1Prefire'                                     : [       285149,       282270,       288046, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       318568,       285146,       258219,       318568,       285146,       258219,       318568,       285146,       258219, ],
  }),
  ("nof_tree_events",                 297179),
  ("nof_db_events",                   297179),
  ("fsize_local",                     1203746726), # 1.20GB, avg file size 1.20GB
  ("fsize_db",                        14044768795), # 14.04GB, avg file size 2.81GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_0p5_1_1_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2VTo2L2Nu_node_SM_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_sm_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       300033,       300016,       300032, ],
    'CountWeightedLHEWeightScale'                                : [       384360,       362836,       342661,       317828,       300033,       283287,       267195,       252189,       238119, ],
    'CountWeightedL1PrefireNom'                                  : [       293947,       293931,       293955, ],
    'CountWeightedL1Prefire'                                     : [       293947,       292418,       295476, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       376518,       355501,       335784,       311339,       293945,       277599,       261737,       247082,       233336, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1100933765), # 1.10GB, avg file size 1.10GB
  ("fsize_db",                        13376661186), # 13.38GB, avg file size 2.68GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_sm_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2VTo2L2Nu_node_box_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_box_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       300022,       300043,       299976, ],
    'CountWeightedLHEWeightScale'                                : [       382913,       363713,       345315,       315873,       300021,       284793,       265024,       251680,       238903, ],
    'CountWeightedL1PrefireNom'                                  : [       294254,       294257,       294234, ],
    'CountWeightedL1Prefire'                                     : [       294254,       292796,       295708, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       375496,       356736,       338742,       309751,       294251,       279369,       259882,       246844,       234350, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1074561726), # 1.07GB, avg file size 1.07GB
  ("fsize_db",                        13225066454), # 13.23GB, avg file size 4.41GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_box_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2VTo2L2Nu_node_1_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_1_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       299988,       299979,       299983, ],
    'CountWeightedLHEWeightScale'                                : [       385630,       362179,       340639,       319540,       299985,       282078,       269129,       252597,       237448, ],
    'CountWeightedL1PrefireNom'                                  : [       293862,       293845,       293868, ],
    'CountWeightedL1Prefire'                                     : [       293862,       292326,       295392, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       377671,       354790,       333759,       312931,       293859,       276370,       263552,       247424,       232635, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1120232946), # 1.12GB, avg file size 1.12GB
  ("fsize_db",                        13519407617), # 13.52GB, avg file size 3.38GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_1_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2VTo2L2Nu_node_2_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v3/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_2_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [         8218, ],
    'CountWeighted'                                              : [         8217,         8217,         8216, ],
    'CountWeightedLHEWeightScale'                                : [        10753,         9812,         9002,         9008,         8216,         7536,         7657,         6982,         6402, ],
    'CountWeightedL1PrefireNom'                                  : [         8033,         8033,         8033, ],
    'CountWeightedL1Prefire'                                     : [         8033,         7988,         8078, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        10511,         9594,         8803,         8805,         8033,         7369,         7484,         6826,         6260, ],
  }),
  ("nof_tree_events",                 8218),
  ("nof_db_events",                   300000),
  ("fsize_local",                     34619685), # 34.62MB, avg file size 34.62MB
  ("fsize_db",                        14649063726), # 14.65GB, avg file size 3.66GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_2_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2VTo2L2Nu_node_3_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_3_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       299998, ],
    'CountWeighted'                                              : [       300064,       299964,       299935, ],
    'CountWeightedLHEWeightScale'                                : [       385312,       362284,       340998,       319130,       300063,       282325,       268658,       252512,       237609, ],
    'CountWeightedL1PrefireNom'                                  : [       293906,       293840,       293838, ],
    'CountWeightedL1Prefire'                                     : [       293906,       292368,       295441, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       377371,       354891,       334095,       312545,       293904,       276604,       263109,       247349,       232791, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1115759803), # 1.12GB, avg file size 1.12GB
  ("fsize_db",                        13601999029), # 13.60GB, avg file size 4.53GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_3_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2VTo2L2Nu_node_4_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_4_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       299999,       299997,       299937, ],
    'CountWeightedLHEWeightScale'                                : [       383461,       363426,       344402,       316597,       299999,       284257,       265828,       251857,       238612, ],
    'CountWeightedL1PrefireNom'                                  : [       294120,       294113,       294089, ],
    'CountWeightedL1Prefire'                                     : [       294120,       292637,       295604, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       375882,       356312,       337717,       310331,       294118,       278735,       260562,       246918,       233973, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1083834941), # 1.08GB, avg file size 1.08GB
  ("fsize_db",                        13322107044), # 13.32GB, avg file size 4.44GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_4_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2VTo2L2Nu_node_5_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_5_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       300070,       299942,       299966, ],
    'CountWeightedLHEWeightScale'                                : [       389049,       360182,       334601,       324158,       300066,       278608,       274285,       253766,       235614, ],
    'CountWeightedL1PrefireNom'                                  : [       293483,       293413,       293417, ],
    'CountWeightedL1Prefire'                                     : [       293483,       291863,       295104, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       380472,       352324,       327365,       317000,       293479,       272574,       268222,       248213,       230504, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1169181383), # 1.17GB, avg file size 1.17GB
  ("fsize_db",                        14057961060), # 14.06GB, avg file size 3.51GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_5_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2VTo2L2Nu_node_6_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_6_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       299982,       300015,       300052, ],
    'CountWeightedLHEWeightScale'                                : [       382864,       363876,       345732,       315757,       299975,       284964,       264893,       251616,       238949, ],
    'CountWeightedL1PrefireNom'                                  : [       294384,       294395,       294439, ],
    'CountWeightedL1Prefire'                                     : [       294384,       292964,       295801, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       375641,       357093,       339354,       309787,       294378,       279696,       259876,       246906,       234523, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1073142494), # 1.07GB, avg file size 1.07GB
  ("fsize_db",                        13143785774), # 13.14GB, avg file size 3.29GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_6_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2VTo2L2Nu_node_7_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_7_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299997, ],
    'CountWeighted'                                              : [       300016,       300034,       300044, ],
    'CountWeightedLHEWeightScale'                                : [       379147,       366135,       352540,       310691,       300011,       288830,       259242,       250294,       240959, ],
    'CountWeightedL1PrefireNom'                                  : [       295004,       295007,       295027, ],
    'CountWeightedL1Prefire'                                     : [       295004,       293710,       296294, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       372765,       360033,       346711,       305458,       295000,       284051,       254870,       246115,       236969, ],
  }),
  ("nof_tree_events",                 299997),
  ("nof_db_events",                   299997),
  ("fsize_local",                     1006532843), # 1.01GB, avg file size 1.01GB
  ("fsize_db",                        12803480606), # 12.80GB, avg file size 3.20GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_7_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2VTo2L2Nu_node_8_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_8_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       299935,       300002,       299950, ],
    'CountWeightedLHEWeightScale'                                : [       385549,       362240,       340804,       319407,       299933,       282171,       268970,       252556,       237496, ],
    'CountWeightedL1PrefireNom'                                  : [       293816,       293851,       293819, ],
    'CountWeightedL1Prefire'                                     : [       293816,       292272,       295351, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       377570,       354829,       333900,       312787,       293813,       276444,       263385,       247372,       232668, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1116937397), # 1.12GB, avg file size 1.12GB
  ("fsize_db",                        13552950610), # 13.55GB, avg file size 4.52GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_8_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2VTo2L2Nu_node_9_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_9_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       299998, ],
    'CountWeighted'                                              : [       299948,       299999,       300001, ],
    'CountWeightedLHEWeightScale'                                : [       387741,       360881,       336742,       322413,       299947,       279874,       272333,       253346,       236307, ],
    'CountWeightedL1PrefireNom'                                  : [       293479,       293502,       293523, ],
    'CountWeightedL1Prefire'                                     : [       293479,       291872,       295084, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       379282,       353084,       329529,       315369,       293478,       273871,       266377,       247860,       231233, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1154146966), # 1.15GB, avg file size 1.15GB
  ("fsize_db",                        13997106004), # 14.00GB, avg file size 4.67GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_9_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2VTo2L2Nu_node_10_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_10_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299998, ],
    'CountWeighted'                                              : [       300030,       300073,       299939, ],
    'CountWeightedLHEWeightScale'                                : [       379916,       365713,       351256,       311718,       300017,       288079,       260389,       250543,       240548, ],
    'CountWeightedL1PrefireNom'                                  : [       294894,       294912,       294837, ],
    'CountWeightedL1Prefire'                                     : [       294894,       293571,       296206, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       373357,       359477,       345325,       306327,       294884,       283204,       255879,       246256,       236474, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1017744925), # 1.02GB, avg file size 1.02GB
  ("fsize_db",                        12822566212), # 12.82GB, avg file size 3.21GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_10_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2VTo2L2Nu_node_11_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_11_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       299364, ],
    'CountWeighted'                                              : [       299375,       299296,       299377, ],
    'CountWeightedLHEWeightScale'                                : [       382107,       363097,       344966,       315152,       299374,       284330,       264406,       251084,       238419, ],
    'CountWeightedL1PrefireNom'                                  : [       293816,       293770,       293821, ],
    'CountWeightedL1Prefire'                                     : [       293816,       292409,       295223, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       374948,       356379,       338649,       309233,       293814,       279114,       259432,       246420,       234035, ],
  }),
  ("nof_tree_events",                 299364),
  ("nof_db_events",                   299364),
  ("fsize_local",                     1068832186), # 1.07GB, avg file size 1.07GB
  ("fsize_db",                        13315340669), # 13.32GB, avg file size 2.66GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_11_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2VTo2L2Nu_node_12_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_12_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299997, ],
    'CountWeighted'                                              : [       300048,       300034,       300039, ],
    'CountWeightedLHEWeightScale'                                : [       380853,       365029,       349247,       313042,       300047,       286992,       261866,       250923,       240025, ],
    'CountWeightedL1PrefireNom'                                  : [       294675,       294645,       294693, ],
    'CountWeightedL1Prefire'                                     : [       294675,       293305,       296046, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       373999,       358527,       343073,       307402,       294673,       281914,       257144,       246443,       235775, ],
  }),
  ("nof_tree_events",                 299997),
  ("nof_db_events",                   299997),
  ("fsize_local",                     1036927945), # 1.04GB, avg file size 1.04GB
  ("fsize_db",                        13025018010), # 13.03GB, avg file size 3.26GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_12_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-250_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_250_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_250_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [        50000, ],
    'CountWeighted'                                              : [        50000,        49996,        49996, ],
    'CountWeightedLHEWeightScale'                                : [        50807,        50000,        48908,        50807,        50000,        48908,        50807,        50000,        48908, ],
    'CountWeightedL1PrefireNom'                                  : [        49295,        49288,        49296, ],
    'CountWeightedL1Prefire'                                     : [        49295,        49105,        49482, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        50084,        49295,        48223,        50084,        49295,        48223,        50084,        49295,        48223, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     153902985), # 153.90MB, avg file size 153.90MB
  ("fsize_db",                        1962681716), # 1.96GB, avg file size 1.96GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-260_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_260_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_260_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [        50000, ],
    'CountWeighted'                                              : [        49999,        49996,        50001, ],
    'CountWeightedLHEWeightScale'                                : [        50955,        49999,        48787,        50955,        49999,        48787,        50955,        49999,        48787, ],
    'CountWeightedL1PrefireNom'                                  : [        49279,        49275,        49284, ],
    'CountWeightedL1Prefire'                                     : [        49279,        49087,        49470, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        50216,        49279,        48091,        50216,        49279,        48091,        50216,        49279,        48091, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     155620591), # 155.62MB, avg file size 155.62MB
  ("fsize_db",                        1978376178), # 1.98GB, avg file size 1.98GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_260_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-270_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_270_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_270_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [        50000, ],
    'CountWeighted'                                              : [        49996,        50003,        49997, ],
    'CountWeightedLHEWeightScale'                                : [        51103,        49996,        48669,        51103,        49996,        48669,        51103,        49996,        48669, ],
    'CountWeightedL1PrefireNom'                                  : [        49240,        49246,        49239, ],
    'CountWeightedL1Prefire'                                     : [        49240,        49039,        49440, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        50322,        49240,        47938,        50322,        49240,        47938,        50322,        49240,        47938, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     157583132), # 157.58MB, avg file size 157.58MB
  ("fsize_db",                        1992599467), # 1.99GB, avg file size 1.99GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_270_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-280_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_280_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_280_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [        49600, ],
    'CountWeighted'                                              : [        49606,        49598,        49603, ],
    'CountWeightedLHEWeightScale'                                : [        50828,        49606,        48175,        50828,        49606,        48175,        50828,        49606,        48175, ],
    'CountWeightedL1PrefireNom'                                  : [        48846,        48836,        48848, ],
    'CountWeightedL1Prefire'                                     : [        48846,        48645,        49045, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        50045,        48846,        47444,        50045,        48846,        47444,        50045,        48846,        47444, ],
  }),
  ("nof_tree_events",                 49600),
  ("nof_db_events",                   49600),
  ("fsize_local",                     158122687), # 158.12MB, avg file size 158.12MB
  ("fsize_db",                        1985262651), # 1.99GB, avg file size 1.99GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_280_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-300_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_300_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_300_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                      : [       450000, ],
    'CountWeighted'                                              : [       450044,       450016,       449954, ],
    'CountWeightedLHEWeightScale'                                : [       463472,       450044,       435231,       463472,       450044,       435231,       463472,       450044,       435231, ],
    'CountWeightedL1PrefireNom'                                  : [       442708,       442678,       442676, ],
    'CountWeightedL1Prefire'                                     : [       442708,       440790,       444624, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       455872,       442708,       428202,       455872,       442708,       428202,       455872,       442708,       428202, ],
  }),
  ("nof_tree_events",                 450000),
  ("nof_db_events",                   450000),
  ("fsize_local",                     1453836552), # 1.45GB, avg file size 1.45GB
  ("fsize_db",                        18335508201), # 18.34GB, avg file size 2.62GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_300_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-320_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_320_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_320_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        50000, ],
    'CountWeighted'                                              : [        49996,        50003,        49999, ],
    'CountWeightedLHEWeightScale'                                : [        51731,        49996,        48171,        51731,        49996,        48171,        51731,        49996,        48171, ],
    'CountWeightedL1PrefireNom'                                  : [        49146,        49150,        49147, ],
    'CountWeightedL1Prefire'                                     : [        49146,        48924,        49367, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        50842,        49146,        47357,        50842,        49146,        47357,        50842,        49146,        47357, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     166253440), # 166.25MB, avg file size 166.25MB
  ("fsize_db",                        2102297139), # 2.10GB, avg file size 1.05GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_320_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-340_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_340_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_340_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [        48000, ],
    'CountWeighted'                                              : [        47997,        48001,        47999, ],
    'CountWeightedLHEWeightScale'                                : [        49881,        47997,        46073,        49881,        47997,        46073,        49881,        47997,        46073, ],
    'CountWeightedL1PrefireNom'                                  : [        47132,        47135,        47132, ],
    'CountWeightedL1Prefire'                                     : [        47132,        46908,        47356, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        48973,        47132,        45247,        48973,        47132,        45247,        48973,        47132,        45247, ],
  }),
  ("nof_tree_events",                 48000),
  ("nof_db_events",                   48000),
  ("fsize_local",                     162565505), # 162.57MB, avg file size 162.57MB
  ("fsize_db",                        1955847184), # 1.96GB, avg file size 1.96GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_340_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-350_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_350_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_350_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [        50000, ],
    'CountWeighted'                                              : [        49989,        49992,        50002, ],
    'CountWeightedLHEWeightScale'                                : [        52062,        49989,        47913,        52062,        49989,        47913,        52062,        49989,        47913, ],
    'CountWeightedL1PrefireNom'                                  : [        49091,        49091,        49100, ],
    'CountWeightedL1Prefire'                                     : [        49091,        48858,        49323, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        51114,        49091,        47054,        51114,        49091,        47054,        51114,        49091,        47054, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     171102326), # 171.10MB, avg file size 171.10MB
  ("fsize_db",                        2167356346), # 2.17GB, avg file size 2.17GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_350_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-400_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_400_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_400_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       250000, ],
    'CountWeighted'                                              : [       249983,       250020,       249980, ],
    'CountWeightedLHEWeightScale'                                : [       262684,       249983,       237709,       262684,       249983,       237709,       262684,       249983,       237709, ],
    'CountWeightedL1PrefireNom'                                  : [       245061,       245069,       245069, ],
    'CountWeightedL1Prefire'                                     : [       245061,       243805,       246312, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       257459,       245061,       233056,       257459,       245061,       233056,       257459,       245061,       233056, ],
  }),
  ("nof_tree_events",                 250000),
  ("nof_db_events",                   250000),
  ("fsize_local",                     885041635), # 885.04MB, avg file size 885.04MB
  ("fsize_db",                        10749996877), # 10.75GB, avg file size 3.58GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_400_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-450_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_450_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_450_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        99600, ],
    'CountWeighted'                                              : [        99611,        99595,        99636, ],
    'CountWeightedLHEWeightScale'                                : [       105485,        99611,        94063,       105485,        99611,        94063,       105485,        99611,        94063, ],
    'CountWeightedL1PrefireNom'                                  : [        97512,        97510,        97521, ],
    'CountWeightedL1Prefire'                                     : [        97512,        96986,        98039, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       103247,        97512,        92101,       103247,        97512,        92101,       103247,        97512,        92101, ],
  }),
  ("nof_tree_events",                 99600),
  ("nof_db_events",                   99600),
  ("fsize_local",                     366408279), # 366.41MB, avg file size 366.41MB
  ("fsize_db",                        4411305292), # 4.41GB, avg file size 2.21GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_450_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-500_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_500_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_500_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        99200, ],
    'CountWeighted'                                              : [        99207,        99186,        99212, ],
    'CountWeightedLHEWeightScale'                                : [       105773,        99207,        93134,       105773,        99207,        93134,       105773,        99207,        93134, ],
    'CountWeightedL1PrefireNom'                                  : [        97028,        97014,        97036, ],
    'CountWeightedL1Prefire'                                     : [        97028,        96484,        97572, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       103437,        97028,        91106,       103437,        97028,        91106,       103437,        97028,        91106, ],
  }),
  ("nof_tree_events",                 99200),
  ("nof_db_events",                   99200),
  ("fsize_local",                     376520029), # 376.52MB, avg file size 376.52MB
  ("fsize_db",                        4435751146), # 4.44GB, avg file size 2.22GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-550_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_550_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_550_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [       100021,       100011,        99974, ],
    'CountWeightedLHEWeightScale'                                : [       107278,       100021,        93402,       107278,       100021,        93402,       107278,       100021,        93402, ],
    'CountWeightedL1PrefireNom'                                  : [        97768,        97759,        97745, ],
    'CountWeightedL1Prefire'                                     : [        97768,        97209,        98328, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       104851,        97768,        91320,       104851,        97768,        91320,       104851,        97768,        91320, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     389850769), # 389.85MB, avg file size 389.85MB
  ("fsize_db",                        4499327267), # 4.50GB, avg file size 2.25GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_550_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-600_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_600_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_600_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [       100010,        99997,       100001, ],
    'CountWeightedLHEWeightScale'                                : [       107866,       100010,        92956,       107866,       100010,        92956,       107866,       100010,        92956, ],
    'CountWeightedL1PrefireNom'                                  : [        97653,        97646,        97647, ],
    'CountWeightedL1Prefire'                                     : [        97653,        97071,        98235, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       105311,        97653,        90783,       105311,        97653,        90783,       105311,        97653,        90783, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     398434663), # 398.43MB, avg file size 398.43MB
  ("fsize_db",                        4581235338), # 4.58GB, avg file size 2.29GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_600_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-650_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_650_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_650_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99992,        99998,       100030, ],
    'CountWeightedLHEWeightScale'                                : [       108413,        99992,        92554,       108413,        99992,        92554,       108413,        99992,        92554, ],
    'CountWeightedL1PrefireNom'                                  : [        97623,        97623,        97646, ],
    'CountWeightedL1Prefire'                                     : [        97623,        97039,        98208, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       105820,        97623,        90372,       105820,        97623,        90372,       105820,        97623,        90372, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     405555601), # 405.56MB, avg file size 405.56MB
  ("fsize_db",                        4742625025), # 4.74GB, avg file size 2.37GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_650_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-800_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_800_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_800_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99993,        99993,       100006, ],
    'CountWeightedLHEWeightScale'                                : [       109795,        99993,        91539,       109795,        99993,        91539,       109795,        99993,        91539, ],
    'CountWeightedL1PrefireNom'                                  : [        97490,        97485,        97500, ],
    'CountWeightedL1Prefire'                                     : [        97490,        96879,        98100, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       107022,        97490,        89256,       107022,        97490,        89256,       107022,        97490,        89256, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     421749136), # 421.75MB, avg file size 421.75MB
  ("fsize_db",                        4845795202), # 4.85GB, avg file size 2.42GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_800_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-900_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_900_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_900_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99992,        99984,        99972, ],
    'CountWeightedLHEWeightScale'                                : [       110555,        99992,        90983,       110555,        99992,        90983,       110555,        99992,        90983, ],
    'CountWeightedL1PrefireNom'                                  : [        97455,        97446,        97450, ],
    'CountWeightedL1Prefire'                                     : [        97455,        96837,        98073, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       107730,        97455,        88682,       107730,        97455,        88682,       107730,        97455,        88682, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     429634672), # 429.63MB, avg file size 429.63MB
  ("fsize_db",                        4858199935), # 4.86GB, avg file size 2.43GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_900_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-250_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_250_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_250_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [        50000, ],
    'CountWeighted'                                              : [        50000,        49994,        49998, ],
    'CountWeightedLHEWeightScale'                                : [        50810,        50000,        48905,        50810,        50000,        48905,        50810,        50000,        48905, ],
    'CountWeightedL1PrefireNom'                                  : [        49278,        49274,        49278, ],
    'CountWeightedL1Prefire'                                     : [        49278,        49086,        49469, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        50071,        49278,        48204,        50071,        49278,        48204,        50071,        49278,        48204, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     155698433), # 155.70MB, avg file size 155.70MB
  ("fsize_db",                        1970267888), # 1.97GB, avg file size 1.97GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-260_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_260_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_260_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [        50000, ],
    'CountWeighted'                                              : [        49995,        50005,        50003, ],
    'CountWeightedLHEWeightScale'                                : [        50954,        49995,        48790,        50954,        49995,        48790,        50954,        49995,        48790, ],
    'CountWeightedL1PrefireNom'                                  : [        49245,        49251,        49250, ],
    'CountWeightedL1Prefire'                                     : [        49245,        49046,        49443, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        50181,        49245,        48062,        50181,        49245,        48062,        50181,        49245,        48062, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     157791576), # 157.79MB, avg file size 157.79MB
  ("fsize_db",                        2021288641), # 2.02GB, avg file size 2.02GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_260_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-270_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_270_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_270_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [        50000, ],
    'CountWeighted'                                              : [        49997,        50002,        50001, ],
    'CountWeightedLHEWeightScale'                                : [        51100,        49997,        48672,        51100,        49997,        48672,        51100,        49997,        48672, ],
    'CountWeightedL1PrefireNom'                                  : [        49210,        49212,        49213, ],
    'CountWeightedL1Prefire'                                     : [        49210,        49002,        49417, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        50288,        49210,        47910,        50288,        49210,        47910,        50288,        49210,        47910, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     160212733), # 160.21MB, avg file size 160.21MB
  ("fsize_db",                        2049006927), # 2.05GB, avg file size 2.05GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_270_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-280_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_280_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_280_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [        50000, ],
    'CountWeighted'                                              : [        49996,        49999,        49995, ],
    'CountWeightedLHEWeightScale'                                : [        51238,        49996,        48559,        51238,        49996,        48559,        51238,        49996,        48559, ],
    'CountWeightedL1PrefireNom'                                  : [        49188,        49191,        49188, ],
    'CountWeightedL1Prefire'                                     : [        49188,        48977,        49399, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        50403,        49188,        47780,        50403,        49188,        47780,        50403,        49188,        47780, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     162163729), # 162.16MB, avg file size 162.16MB
  ("fsize_db",                        2024724980), # 2.02GB, avg file size 2.02GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_280_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-300_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_300_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_300_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       447400, ],
    'CountWeighted'                                              : [       447444,       447398,       447345, ],
    'CountWeightedLHEWeightScale'                                : [       460790,       447444,       432712,       460790,       447444,       432712,       460790,       447444,       432712, ],
    'CountWeightedL1PrefireNom'                                  : [       439952,       439915,       439906, ],
    'CountWeightedL1Prefire'                                     : [       439952,       438009,       441889, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       453024,       439952,       425540,       453024,       439952,       425540,       453024,       439952,       425540, ],
  }),
  ("nof_tree_events",                 447400),
  ("nof_db_events",                   447400),
  ("fsize_local",                     1476029701), # 1.48GB, avg file size 1.48GB
  ("fsize_db",                        18368864093), # 18.37GB, avg file size 3.67GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_300_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-320_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_320_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_320_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [        50000, ],
    'CountWeighted'                                              : [        49992,        49994,        50001, ],
    'CountWeightedLHEWeightScale'                                : [        51729,        49992,        48169,        51729,        49992,        48169,        51729,        49992,        48169, ],
    'CountWeightedL1PrefireNom'                                  : [        49131,        49130,        49140, ],
    'CountWeightedL1Prefire'                                     : [        49131,        48908,        49354, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        50828,        49131,        47344,        50828,        49131,        47344,        50828,        49131,        47344, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     170283362), # 170.28MB, avg file size 170.28MB
  ("fsize_db",                        2056109122), # 2.06GB, avg file size 2.06GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_320_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-340_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_340_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_340_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [        50000, ],
    'CountWeighted'                                              : [        49996,        50010,        50000, ],
    'CountWeightedLHEWeightScale'                                : [        51958,        49996,        47993,        51958,        49996,        47993,        51958,        49996,        47993, ],
    'CountWeightedL1PrefireNom'                                  : [        49106,        49112,        49110, ],
    'CountWeightedL1Prefire'                                     : [        49106,        48878,        49334, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        51023,        49106,        47144,        51023,        49106,        47144,        51023,        49106,        47144, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     173597421), # 173.60MB, avg file size 173.60MB
  ("fsize_db",                        2082210498), # 2.08GB, avg file size 2.08GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_340_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-350_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_350_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_350_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [        50000, ],
    'CountWeighted'                                              : [        50002,        49996,        50006, ],
    'CountWeightedLHEWeightScale'                                : [        52061,        50002,        47912,        52061,        50002,        47912,        52061,        50002,        47912, ],
    'CountWeightedL1PrefireNom'                                  : [        49102,        49097,        49107, ],
    'CountWeightedL1Prefire'                                     : [        49102,        48872,        49332, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        51116,        49102,        47058,        51116,        49102,        47058,        51116,        49102,        47058, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     175601760), # 175.60MB, avg file size 175.60MB
  ("fsize_db",                        2097870831), # 2.10GB, avg file size 2.10GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_350_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-400_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_400_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_400_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       250000, ],
    'CountWeighted'                                              : [       250027,       249951,       250001, ],
    'CountWeightedLHEWeightScale'                                : [       262682,       250027,       237714,       262682,       250027,       237714,       262682,       250027,       237714, ],
    'CountWeightedL1PrefireNom'                                  : [       245201,       245153,       245192, ],
    'CountWeightedL1Prefire'                                     : [       245201,       243988,       246417, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       257573,       245201,       233171,       257573,       245201,       233171,       257573,       245201,       233171, ],
  }),
  ("nof_tree_events",                 250000),
  ("nof_db_events",                   250000),
  ("fsize_local",                     910604117), # 910.60MB, avg file size 910.60MB
  ("fsize_db",                        10695129460), # 10.70GB, avg file size 3.57GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_400_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-450_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_450_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_450_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99997,        99974,       100016, ],
    'CountWeightedLHEWeightScale'                                : [       105906,        99997,        94447,       105906,        99997,        94447,       105906,        99997,        94447, ],
    'CountWeightedL1PrefireNom'                                  : [        98026,        98009,        98042, ],
    'CountWeightedL1Prefire'                                     : [        98026,        97533,        98520, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       103796,        98026,        92599,       103796,        98026,        92599,       103796,        98026,        92599, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     379736824), # 379.74MB, avg file size 379.74MB
  ("fsize_db",                        4416939298), # 4.42GB, avg file size 2.21GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_450_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-500_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_500_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_500_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99994,       100014,        99986, ],
    'CountWeightedLHEWeightScale'                                : [       106625,        99994,        93895,       106625,        99994,        93895,       106625,        99994,        93895, ],
    'CountWeightedL1PrefireNom'                                  : [        97987,        97994,        97989, ],
    'CountWeightedL1Prefire'                                     : [        97987,        97489,        98486, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       104463,        97987,        92023,       104463,        97987,        92023,       104463,        97987,        92023, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     392457820), # 392.46MB, avg file size 392.46MB
  ("fsize_db",                        4450805287), # 4.45GB, avg file size 4.45GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-550_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_550_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_550_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99997,       100036,        99986, ],
    'CountWeightedLHEWeightScale'                                : [       107293,        99997,        93392,       107293,        99997,        93392,       107293,        99997,        93392, ],
    'CountWeightedL1PrefireNom'                                  : [        97953,        97974,        97950, ],
    'CountWeightedL1Prefire'                                     : [        97953,        97448,        98456, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       105077,        97953,        91497,       105077,        97953,        91497,       105077,        97953,        91497, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     402732234), # 402.73MB, avg file size 402.73MB
  ("fsize_db",                        4675550080), # 4.68GB, avg file size 2.34GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_550_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-600_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_600_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_600_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [       100041,        99977,       100007, ],
    'CountWeightedLHEWeightScale'                                : [       107872,       100041,        92954,       107872,       100041,        92954,       107872,       100041,        92954, ],
    'CountWeightedL1PrefireNom'                                  : [        97987,        97942,        97971, ],
    'CountWeightedL1Prefire'                                     : [        97987,        97487,        98488, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       105652,        97987,        91073,       105652,        97987,        91073,       105652,        97987,        91073, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     410835671), # 410.84MB, avg file size 410.84MB
  ("fsize_db",                        4653469892), # 4.65GB, avg file size 2.33GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_600_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-650_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_650_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_650_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99985,       100024,       100008, ],
    'CountWeightedLHEWeightScale'                                : [       108412,        99985,        92550,       108412,        99985,        92550,       108412,        99985,        92550, ],
    'CountWeightedL1PrefireNom'                                  : [        97966,        97988,        97981, ],
    'CountWeightedL1Prefire'                                     : [        97966,        97469,        98461, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       106199,        97966,        90689,       106199,        97966,        90689,       106199,        97966,        90689, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     418307404), # 418.31MB, avg file size 418.31MB
  ("fsize_db",                        4740249400), # 4.74GB, avg file size 2.37GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_650_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-750_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_750_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_750_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [       100009,       100005,       100023, ],
    'CountWeightedLHEWeightScale'                                : [       109361,       100009,        91849,       109361,       100009,        91849,       109361,       100009,        91849, ],
    'CountWeightedL1PrefireNom'                                  : [        98030,        98027,        98041, ],
    'CountWeightedL1Prefire'                                     : [        98030,        97549,        98513, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       107185,        98030,        90046,       107185,        98030,        90046,       107185,        98030,        90046, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     428223144), # 428.22MB, avg file size 428.22MB
  ("fsize_db",                        4895097500), # 4.90GB, avg file size 2.45GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-800_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_800_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_800_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [       100006,        99986,        99991, ],
    'CountWeightedLHEWeightScale'                                : [       109785,       100006,        91539,       109785,       100006,        91539,       109785,       100006,        91539, ],
    'CountWeightedL1PrefireNom'                                  : [        98032,        98015,        98026, ],
    'CountWeightedL1Prefire'                                     : [        98032,        97549,        98513, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       107606,        98032,        89743,       107606,        98032,        89743,       107606,        98032,        89743, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     432557272), # 432.56MB, avg file size 432.56MB
  ("fsize_db",                        4784663508), # 4.78GB, avg file size 4.78GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_800_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2Tau_CV_1_C2V_1_C3_0_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_0_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_0_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       296060, ],
    'CountWeighted'                                              : [       296005,       296109,       296124, ],
    'CountWeightedLHEWeightScale'                                : [       318163,       296004,       276840,       318163,       296004,       276840,       318163,       296004,       276840, ],
    'CountWeightedL1PrefireNom'                                  : [       285770,       285793,       285815, ],
    'CountWeightedL1Prefire'                                     : [       285770,       283176,       288361, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       306934,       285767,       267373,       306934,       285767,       267373,       306934,       285767,       267373, ],
  }),
  ("nof_tree_events",                 296060),
  ("nof_db_events",                   296060),
  ("fsize_local",                     1068985358), # 1.07GB, avg file size 1.07GB
  ("fsize_db",                        12663197291), # 12.66GB, avg file size 2.53GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_0_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2Tau_CV_1_C2V_1_C3_1_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_1_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_1_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       300036,       299990,       300041, ],
    'CountWeightedLHEWeightScale'                                : [       326180,       300035,       277763,       326180,       300035,       277763,       326180,       300035,       277763, ],
    'CountWeightedL1PrefireNom'                                  : [       287830,       287815,       287835, ],
    'CountWeightedL1Prefire'                                     : [       287830,       284799,       290877, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       312728,       287827,       266641,       312728,       287827,       266641,       312728,       287827,       266641, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1085303448), # 1.09GB, avg file size 1.09GB
  ("fsize_db",                        12708206493), # 12.71GB, avg file size 3.18GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_1_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2Tau_CV_1_C2V_1_C3_2_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_2_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_2_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       257175, ],
    'CountWeighted'                                              : [       257204,       257167,       257150, ],
    'CountWeightedLHEWeightScale'                                : [       278651,       257202,       238891,       278651,       257202,       238891,       278651,       257202,       238891, ],
    'CountWeightedL1PrefireNom'                                  : [       244168,       244161,       244146, ],
    'CountWeightedL1Prefire'                                     : [       244168,       241034,       247319, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       264317,       244165,       226977,       264317,       244165,       226977,       264317,       244165,       226977, ],
  }),
  ("nof_tree_events",                 257175),
  ("nof_db_events",                   257175),
  ("fsize_local",                     981483762), # 981.48MB, avg file size 981.48MB
  ("fsize_db",                        11297192364), # 11.30GB, avg file size 2.82GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_2_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2Tau_CV_1_C2V_2_C3_1_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_2_1_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_2_1_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       300021,       299918,       300020, ],
    'CountWeightedLHEWeightScale'                                : [       338031,       300019,       269697,       338031,       300019,       269697,       338031,       300019,       269697, ],
    'CountWeightedL1PrefireNom'                                  : [       287115,       287070,       287125, ],
    'CountWeightedL1Prefire'                                     : [       287115,       284056,       290193, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       323403,       287112,       258189,       323403,       287112,       258189,       323403,       287112,       258189, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1266802846), # 1.27GB, avg file size 1.27GB
  ("fsize_db",                        14237299312), # 14.24GB, avg file size 2.85GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_2_1_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2Tau_CV_1_5_C2V_1_C3_1_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1p5_1_1_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1p5_1_1_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299322, ],
    'CountWeighted'                                              : [       299228,       299338,       299324, ],
    'CountWeightedLHEWeightScale'                                : [       330039,       299228,       274012,       330039,       299228,       274012,       330039,       299228,       274012, ],
    'CountWeightedL1PrefireNom'                                  : [       287288,       287320,       287320, ],
    'CountWeightedL1Prefire'                                     : [       287288,       284354,       290227, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       316611,       287285,       263163,       316611,       287285,       263163,       316611,       287285,       263163, ],
  }),
  ("nof_tree_events",                 299322),
  ("nof_db_events",                   299322),
  ("fsize_local",                     1171498050), # 1.17GB, avg file size 1.17GB
  ("fsize_db",                        13394462193), # 13.39GB, avg file size 3.35GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1p5_1_1_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2Tau_CV_0_5_C2V_1_C3_1_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_0p5_1_1_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_0p5_1_1_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       300035,       300021,       299998, ],
    'CountWeightedLHEWeightScale'                                : [       335098,       300027,       271701,       335098,       300027,       271701,       335098,       300027,       271701, ],
    'CountWeightedL1PrefireNom'                                  : [       287484,       287474,       287476, ],
    'CountWeightedL1Prefire'                                     : [       287484,       284487,       290502, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       320955,       287479,       260467,       320955,       287479,       260467,       320955,       287479,       260467, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1240139430), # 1.24GB, avg file size 1.24GB
  ("fsize_db",                        13698968263), # 13.70GB, avg file size 3.42GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_0p5_1_1_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2Tau_node_SM_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_sm_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       300010,       299984,       300018, ],
    'CountWeightedLHEWeightScale'                                : [       384326,       362835,       342679,       317799,       300007,       283310,       267174,       252190,       238143, ],
    'CountWeightedL1PrefireNom'                                  : [       293734,       293721,       293734, ],
    'CountWeightedL1Prefire'                                     : [       293734,       292156,       295310, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       376219,       355255,       335576,       311092,       293730,       277434,       261533,       246915,       233201, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1128510216), # 1.13GB, avg file size 564.26MB
  ("fsize_db",                        13013254769), # 13.01GB, avg file size 4.34GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_sm_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2Tau_node_box_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_box_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       277140, ],
    'CountWeighted'                                              : [       277141,       277152,       277124, ],
    'CountWeightedLHEWeightScale'                                : [       353745,       336001,       318999,       291807,       277137,       263092,       244831,       232504,       220700, ],
    'CountWeightedL1PrefireNom'                                  : [       271541,       271531,       271544, ],
    'CountWeightedL1Prefire'                                     : [       271541,       270120,       272956, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       346528,       329216,       312611,       285849,       271536,       257819,       239829,       227802,       216274, ],
  }),
  ("nof_tree_events",                 277140),
  ("nof_db_events",                   277140),
  ("fsize_local",                     1017050247), # 1.02GB, avg file size 508.53MB
  ("fsize_db",                        11969129912), # 11.97GB, avg file size 3.99GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_box_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2Tau_node_2_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_2_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       291000, ],
    'CountWeighted'                                              : [       291008,       291000,       290998, ],
    'CountWeightedLHEWeightScale'                                : [       371670,       352736,       334726,       306701,       291007,       276078,       257424,       244188,       231621, ],
    'CountWeightedL1PrefireNom'                                  : [       285180,       285166,       285177, ],
    'CountWeightedL1Prefire'                                     : [       285180,       283704,       286650, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       364148,       345687,       328107,       300484,       285178,       270608,       252197,       239292,       227025, ],
  }),
  ("nof_tree_events",                 291000),
  ("nof_db_events",                   291000),
  ("fsize_local",                     1074889033), # 1.07GB, avg file size 537.44MB
  ("fsize_db",                        12693181737), # 12.69GB, avg file size 4.23GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_2_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2Tau_node_9_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_9_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       299988,       299994,       300008, ],
    'CountWeightedLHEWeightScale'                                : [       380810,       365080,       349381,       312975,       299966,       287063,       261794,       250909,       240060, ],
    'CountWeightedL1PrefireNom'                                  : [       294391,       294389,       294411, ],
    'CountWeightedL1Prefire'                                     : [       294391,       292960,       295821, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       373632,       358272,       342922,       307070,       294375,       281750,       256850,       246220,       235613, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1060134798), # 1.06GB, avg file size 530.07MB
  ("fsize_db",                        12554774019), # 12.55GB, avg file size 4.18GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_9_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2Tau_node_10_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_10_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       300015,       300000,       299986, ],
    'CountWeightedLHEWeightScale'                                : [       382021,       364307,       347067,       314637,       300007,       285767,       263646,       251349,       239399, ],
    'CountWeightedL1PrefireNom'                                  : [       294151,       294135,       294142, ],
    'CountWeightedL1Prefire'                                     : [       294151,       292662,       295636, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       374491,       357201,       340358,       308429,       294144,       280237,       258440,       246437,       234763, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1083254668), # 1.08GB, avg file size 541.63MB
  ("fsize_db",                        12953354252), # 12.95GB, avg file size 3.24GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_10_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2Tau_node_11_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_11_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       300003,       299983,       299962, ],
    'CountWeightedLHEWeightScale'                                : [       384467,       362941,       342915,       317930,       300001,       283344,       267336,       252167,       238093, ],
    'CountWeightedL1PrefireNom'                                  : [       293845,       293836,       293818, ],
    'CountWeightedL1Prefire'                                     : [       293845,       292300,       295390, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       376488,       355512,       335977,       311316,       293841,       277597,       261762,       246980,       233253, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1129934012), # 1.13GB, avg file size 564.97MB
  ("fsize_db",                        13042878478), # 13.04GB, avg file size 4.35GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_11_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2Tau_node_12_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_12_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       298800, ],
    'CountWeighted'                                              : [       298741,       298816,       298793, ],
    'CountWeightedLHEWeightScale'                                : [       385318,       359966,       336994,       319937,       298736,       279663,       269923,       252028,       235837, ],
    'CountWeightedL1PrefireNom'                                  : [       292411,       292449,       292447, ],
    'CountWeightedL1Prefire'                                     : [       292411,       290831,       293991, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       377047,       352321,       329903,       313059,       292405,       273769,       264114,       246663,       230862, ],
  }),
  ("nof_tree_events",                 298800),
  ("nof_db_events",                   298800),
  ("fsize_local",                     1177472552), # 1.18GB, avg file size 588.74MB
  ("fsize_db",                        13370108309), # 13.37GB, avg file size 4.46GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_12_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2Tau_node_13_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_13_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       299963,       300002,       299986, ],
    'CountWeightedLHEWeightScale'                                : [       388568,       360323,       335114,       323568,       299958,       278971,       273631,       253666,       235856, ],
    'CountWeightedL1PrefireNom'                                  : [       293102,       293120,       293116, ],
    'CountWeightedL1Prefire'                                     : [       293102,       291400,       294803, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       379586,       352068,       327493,       316083,       293098,       272623,       267298,       247847,       230486, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1208431539), # 1.21GB, avg file size 604.22MB
  ("fsize_db",                        13600771777), # 13.60GB, avg file size 4.53GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Dec08_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_13_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["sum_events"] = [
  [ 'signal_ggf_nonresonant_node_sm_hh_2b2t',          'signal_ggf_nonresonant_node_box_hh_2b2t',         'signal_ggf_nonresonant_node_2_hh_2b2t',           'signal_ggf_nonresonant_node_9_hh_2b2t',           'signal_ggf_nonresonant_node_10_hh_2b2t',          'signal_ggf_nonresonant_node_11_hh_2b2t',          'signal_ggf_nonresonant_node_12_hh_2b2t',          'signal_ggf_nonresonant_node_13_hh_2b2t',           ],
  [ 'signal_ggf_nonresonant_node_sm_hh_2b2v',          'signal_ggf_nonresonant_node_box_hh_2b2v',         'signal_ggf_nonresonant_node_1_hh_2b2v',           'signal_ggf_nonresonant_node_2_hh_2b2v',           'signal_ggf_nonresonant_node_3_hh_2b2v',           'signal_ggf_nonresonant_node_4_hh_2b2v',           'signal_ggf_nonresonant_node_5_hh_2b2v',           'signal_ggf_nonresonant_node_6_hh_2b2v',           'signal_ggf_nonresonant_node_7_hh_2b2v',           'signal_ggf_nonresonant_node_8_hh_2b2v',           'signal_ggf_nonresonant_node_9_hh_2b2v',           'signal_ggf_nonresonant_node_10_hh_2b2v',          'signal_ggf_nonresonant_node_11_hh_2b2v',          'signal_ggf_nonresonant_node_12_hh_2b2v',           ],
]

