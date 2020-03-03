from collections import OrderedDict as OD

# file generated at 2020-03-03 10:42:57 with the following command:
# create_dictionary.py -m python/samples/metaDict_2016_hh.py -p /hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples -N samples_2016 -E 2016 -o python/samples -g hhAnalyzeSamples_2016_hh.py -M

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
    'CountWeightedLHEEnvelope'                                   : [       305752,       292733, ],
    'CountWeightedL1PrefireNom'                                  : [       295862,       295852,       295898, ],
    'CountWeightedL1Prefire'                                     : [       295862,       294761,       296959, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       301503,       295861,       288717,       301503,       295861,       288717,       301503,       295861,       288717, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       301503,       288717, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     971364660), # 971.36MB, avg file size 971.36MB
  ("fsize_db",                        11821300223), # 11.82GB, avg file size 2.96GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_260_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       301127,       286780, ],
    'CountWeightedL1PrefireNom'                                  : [       290405,       290402,       290404, ],
    'CountWeightedL1Prefire'                                     : [       290405,       289282,       291520, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       296772,       290402,       282690,       296772,       290402,       282690,       296772,       290402,       282690, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       296772,       282690, ],
  }),
  ("nof_tree_events",                 294629),
  ("nof_db_events",                   294629),
  ("fsize_local",                     964729343), # 964.73MB, avg file size 964.73MB
  ("fsize_db",                        11694604529), # 11.69GB, avg file size 3.90GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_270_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       308988,       290128, ],
    'CountWeightedL1PrefireNom'                                  : [       295359,       295339,       295414, ],
    'CountWeightedL1Prefire'                                     : [       295359,       294145,       296569, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       304182,       295356,       285680,       304182,       295356,       285680,       304182,       295356,       285680, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       304182,       285680, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1014924297), # 1.01GB, avg file size 1.01GB
  ("fsize_db",                        12121761327), # 12.12GB, avg file size 3.03GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_300_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       307330,       282815, ],
    'CountWeightedL1PrefireNom'                                  : [       290107,       290071,       290036, ],
    'CountWeightedL1Prefire'                                     : [       290107,       288787,       291419, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       301961,       290093,       277947,       301961,       290093,       277947,       301961,       290093,       277947, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       301961,       277947, ],
  }),
  ("nof_tree_events",                 295149),
  ("nof_db_events",                   295149),
  ("fsize_local",                     1047114226), # 1.05GB, avg file size 1.05GB
  ("fsize_db",                        12270587874), # 12.27GB, avg file size 2.45GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_350_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       315263,       285213, ],
    'CountWeightedL1PrefireNom'                                  : [       294387,       294337,       294358, ],
    'CountWeightedL1Prefire'                                     : [       294387,       292946,       295825, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       309275,       294384,       279875,       309275,       294384,       279875,       309275,       294384,       279875, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       309275,       279875, ],
  }),
  ("nof_tree_events",                 299997),
  ("nof_db_events",                   299997),
  ("fsize_local",                     1105836388), # 1.11GB, avg file size 1.11GB
  ("fsize_db",                        12763369067), # 12.76GB, avg file size 3.19GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_400_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       313768,       279794, ],
    'CountWeightedL1PrefireNom'                                  : [       290340,       290360,       290358, ],
    'CountWeightedL1Prefire'                                     : [       290340,       288851,       291825, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       307458,       290337,       274249,       307458,       290337,       274249,       307458,       290337,       274249, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       307458,       274249, ],
  }),
  ("nof_tree_events",                 296256),
  ("nof_db_events",                   296256),
  ("fsize_local",                     1129068755), # 1.13GB, avg file size 1.13GB
  ("fsize_db",                        12817875328), # 12.82GB, avg file size 3.20GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_450_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       319918,       281656, ],
    'CountWeightedL1PrefireNom'                                  : [       293749,       293736,       293771, ],
    'CountWeightedL1Prefire'                                     : [       293749,       292193,       295309, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       313224,       293747,       275849,       313224,       293747,       275849,       313224,       293747,       275849, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       313224,       275849, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1173701274), # 1.17GB, avg file size 1.17GB
  ("fsize_db",                        13281765633), # 13.28GB, avg file size 2.66GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_500_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       321842,       280187, ],
    'CountWeightedL1PrefireNom'                                  : [       293497,       293506,       293557, ],
    'CountWeightedL1Prefire'                                     : [       293497,       291885,       295106, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       314824,       293494,       274163,       314824,       293494,       274163,       314824,       293494,       274163, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       314824,       274163, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1202235452), # 1.20GB, avg file size 1.20GB
  ("fsize_db",                        13529956556), # 13.53GB, avg file size 2.71GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_550_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       323626,       278866, ],
    'CountWeightedL1PrefireNom'                                  : [       293316,       293319,       293347, ],
    'CountWeightedL1Prefire'                                     : [       293316,       291665,       294968, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       316378,       293314,       272699,       316378,       293314,       272699,       316378,       293314,       272699, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       316378,       272699, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1224979622), # 1.22GB, avg file size 1.22GB
  ("fsize_db",                        13674104858), # 13.67GB, avg file size 3.42GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_600_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       324727,       277246, ],
    'CountWeightedL1PrefireNom'                                  : [       292651,       292703,       292723, ],
    'CountWeightedL1Prefire'                                     : [       292651,       290968,       294337, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       317254,       292648,       270942,       317254,       292648,       270942,       317254,       292648,       270942, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       317254,       270942, ],
  }),
  ("nof_tree_events",                 299538),
  ("nof_db_events",                   299538),
  ("fsize_local",                     1241787311), # 1.24GB, avg file size 1.24GB
  ("fsize_db",                        13997216210), # 14.00GB, avg file size 2.80GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_650_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       326694,       274381, ],
    'CountWeightedL1PrefireNom'                                  : [       291625,       291585,       291608, ],
    'CountWeightedL1Prefire'                                     : [       291625,       289880,       293371, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       318846,       291617,       267862,       318846,       291617,       267862,       318846,       291617,       267862, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       318846,       267862, ],
  }),
  ("nof_tree_events",                 298727),
  ("nof_db_events",                   298727),
  ("fsize_local",                     1264679596), # 1.26GB, avg file size 1.26GB
  ("fsize_db",                        13966996917), # 13.97GB, avg file size 4.66GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_750_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       329029,       274337, ],
    'CountWeightedL1PrefireNom'                                  : [       292537,       292584,       292603, ],
    'CountWeightedL1Prefire'                                     : [       292537,       290793,       294282, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       321133,       292534,       267826,       321133,       292534,       267826,       321133,       292534,       267826, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       321133,       267826, ],
  }),
  ("nof_tree_events",                 299705),
  ("nof_db_events",                   299705),
  ("fsize_local",                     1278781851), # 1.28GB, avg file size 1.28GB
  ("fsize_db",                        14140095303), # 14.14GB, avg file size 4.71GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_800_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       330287,       271774, ],
    'CountWeightedL1PrefireNom'                                  : [       291481,       291511,       291477, ],
    'CountWeightedL1Prefire'                                     : [       291481,       289718,       293248, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       322219,       291478,       265201,       322219,       291478,       265201,       322219,       291478,       265201, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       322219,       265201, ],
  }),
  ("nof_tree_events",                 298733),
  ("nof_db_events",                   298733),
  ("fsize_local",                     1290530638), # 1.29GB, avg file size 1.29GB
  ("fsize_db",                        14389658695), # 14.39GB, avg file size 4.80GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_900_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       333750,       271427, ],
    'CountWeightedL1PrefireNom'                                  : [       292565,       292502,       292547, ],
    'CountWeightedL1Prefire'                                     : [       292565,       290763,       294373, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       325422,       292563,       264713,       325422,       292563,       264713,       325422,       292563,       264713, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       325422,       264713, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1310243147), # 1.31GB, avg file size 1.31GB
  ("fsize_db",                        14685031472), # 14.69GB, avg file size 3.67GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1000_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       305771,       292706, ],
    'CountWeightedL1PrefireNom'                                  : [       295626,       295715,       295712, ],
    'CountWeightedL1Prefire'                                     : [       295626,       294482,       296761, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       301339,       295625,       288522,       301339,       295625,       288522,       301339,       295625,       288522, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       301339,       288522, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     988627933), # 988.63MB, avg file size 988.63MB
  ("fsize_db",                        12205401208), # 12.21GB, avg file size 4.07GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_260_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       306610,       292026, ],
    'CountWeightedL1PrefireNom'                                  : [       295584,       295582,       295613, ],
    'CountWeightedL1Prefire'                                     : [       295584,       294420,       296744, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       302071,       295582,       287763,       302071,       295582,       287763,       302071,       295582,       287763, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       302071,       287763, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1000066089), # 1.00GB, avg file size 1.00GB
  ("fsize_db",                        12216222977), # 12.22GB, avg file size 4.07GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_270_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       308996,       290112, ],
    'CountWeightedL1PrefireNom'                                  : [       295218,       295147,       295208, ],
    'CountWeightedL1Prefire'                                     : [       295218,       293963,       296471, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       303985,       295204,       285481,       303985,       295204,       285481,       303985,       295204,       285481, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       303985,       285481, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1039492933), # 1.04GB, avg file size 1.04GB
  ("fsize_db",                        12432044182), # 12.43GB, avg file size 4.14GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_300_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       312408,       287449, ],
    'CountWeightedL1PrefireNom'                                  : [       294676,       294706,       294756, ],
    'CountWeightedL1Prefire'                                     : [       294676,       293321,       296027, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       306842,       294674,       282415,       306842,       294674,       282415,       306842,       294674,       282415, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       306842,       282415, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1093054274), # 1.09GB, avg file size 1.09GB
  ("fsize_db",                        12931701996), # 12.93GB, avg file size 3.23GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_350_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       315235,       285238, ],
    'CountWeightedL1PrefireNom'                                  : [       294522,       294496,       294484, ],
    'CountWeightedL1Prefire'                                     : [       294522,       293134,       295914, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       309408,       294517,       280059,       309408,       294517,       280059,       309408,       294517,       280059, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       309408,       280059, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1139309559), # 1.14GB, avg file size 1.14GB
  ("fsize_db",                        13138610285), # 13.14GB, avg file size 4.38GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_400_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       317714,       283327, ],
    'CountWeightedL1PrefireNom'                                  : [       294275,       294316,       294309, ],
    'CountWeightedL1Prefire'                                     : [       294275,       292852,       295700, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       311622,       294274,       277986,       311622,       294274,       277986,       311622,       294274,       277986, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       311622,       277986, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1176728046), # 1.18GB, avg file size 1.18GB
  ("fsize_db",                        13501491108), # 13.50GB, avg file size 3.38GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_450_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       319897,       281654, ],
    'CountWeightedL1PrefireNom'                                  : [       294236,       294175,       294180, ],
    'CountWeightedL1Prefire'                                     : [       294236,       292797,       295670, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       313673,       294233,       276265,       313673,       294233,       276265,       313673,       294233,       276265, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       313673,       276265, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1211406338), # 1.21GB, avg file size 1.21GB
  ("fsize_db",                        13733577571), # 13.73GB, avg file size 4.58GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_500_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       321864,       280186, ],
    'CountWeightedL1PrefireNom'                                  : [       294119,       294115,       294102, ],
    'CountWeightedL1Prefire'                                     : [       294119,       292663,       295571, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       315485,       294113,       274720,       315485,       294113,       274720,       315485,       294113,       274720, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       315485,       274720, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1239506832), # 1.24GB, avg file size 1.24GB
  ("fsize_db",                        13919729330), # 13.92GB, avg file size 4.64GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_550_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       323617,       278860, ],
    'CountWeightedL1PrefireNom'                                  : [       294145,       294176,       294165, ],
    'CountWeightedL1Prefire'                                     : [       294145,       292711,       295582, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       317272,       294142,       273471,       317272,       294142,       273471,       317272,       294142,       273471, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       317272,       273471, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1260577689), # 1.26GB, avg file size 1.26GB
  ("fsize_db",                        14074430864), # 14.07GB, avg file size 4.69GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_600_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       323946,       276575, ],
    'CountWeightedL1PrefireNom'                                  : [       292959,       292990,       292955, ],
    'CountWeightedL1Prefire'                                     : [       292959,       291527,       294393, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       317559,       292951,       271188,       317559,       292951,       271188,       317559,       292951,       271188, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       317559,       271188, ],
  }),
  ("nof_tree_events",                 298806),
  ("nof_db_events",                   298806),
  ("fsize_local",                     1271559247), # 1.27GB, avg file size 1.27GB
  ("fsize_db",                        14346261466), # 14.35GB, avg file size 2.39GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_650_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       326704,       276567, ],
    'CountWeightedL1PrefireNom'                                  : [       294197,       294140,       294137, ],
    'CountWeightedL1Prefire'                                     : [       294197,       292775,       295623, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       320316,       294191,       271221,       320316,       294191,       271221,       320316,       294191,       271221, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       320316,       271221, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1288402794), # 1.29GB, avg file size 1.29GB
  ("fsize_db",                        14636315935), # 14.64GB, avg file size 4.88GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_700_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       329351,       274606, ],
    'CountWeightedL1PrefireNom'                                  : [       294263,       294188,       294190, ],
    'CountWeightedL1Prefire'                                     : [       294263,       292859,       295665, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       323004,       294256,       269359,       323004,       294256,       269359,       323004,       294256,       269359, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       323004,       269359, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1306486123), # 1.31GB, avg file size 1.31GB
  ("fsize_db",                        14673528101), # 14.67GB, avg file size 3.67GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_800_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       331710,       272939, ],
    'CountWeightedL1PrefireNom'                                  : [       294246,       294229,       294266, ],
    'CountWeightedL1Prefire'                                     : [       294246,       292851,       295643, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       325332,       294242,       267728,       325332,       294242,       267728,       325332,       294242,       267728, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       325332,       267728, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1318731119), # 1.32GB, avg file size 1.32GB
  ("fsize_db",                        15011560063), # 15.01GB, avg file size 5.00GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_900_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       332789,       270645, ],
    'CountWeightedL1PrefireNom'                                  : [       293385,       293388,       293456, ],
    'CountWeightedL1Prefire'                                     : [       293385,       291999,       294776, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       326394,       293381,       265477,       326394,       293381,       265477,       326394,       293381,       265477, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       326394,       265477, ],
  }),
  ("nof_tree_events",                 299118),
  ("nof_db_events",                   299118),
  ("fsize_local",                     1324082847), # 1.32GB, avg file size 1.32GB
  ("fsize_db",                        15065557472), # 15.07GB, avg file size 5.02GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_1000_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       328773,       275221, ],
    'CountWeightedL1PrefireNom'                                  : [       288365,       288365,       288355, ],
    'CountWeightedL1Prefire'                                     : [       288365,       285462,       291269, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       313353,       288362,       267104,       313353,       288362,       267104,       313353,       288362,       267104, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       315864,       264636, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1145755665), # 1.15GB, avg file size 1.15GB
  ("fsize_db",                        12626803802), # 12.63GB, avg file size 4.21GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_1_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       327207,       276516, ],
    'CountWeightedL1PrefireNom'                                  : [       285211,       285159,       285210, ],
    'CountWeightedL1Prefire'                                     : [       285211,       281653,       288788, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       308640,       285208,       265199,       308640,       285208,       265199,       308640,       285208,       265199, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       310866,       263010, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1208335475), # 1.21GB, avg file size 1.21GB
  ("fsize_db",                        13505935893), # 13.51GB, avg file size 2.25GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_2_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       339274,       268509, ],
    'CountWeightedL1PrefireNom'                                  : [       287335,       287331,       287364, ],
    'CountWeightedL1Prefire'                                     : [       287335,       284341,       290344, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       323762,       287333,       258353,       323762,       287333,       258353,       323762,       287333,       258353, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       324897,       257245, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1302540037), # 1.30GB, avg file size 1.30GB
  ("fsize_db",                        14484771487), # 14.48GB, avg file size 2.41GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_2_1_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       325875,       277109, ],
    'CountWeightedL1PrefireNom'                                  : [       289896,       289851,       289858, ],
    'CountWeightedL1Prefire'                                     : [       289896,       287342,       292448, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       311374,       289892,       271175,       311374,       289892,       271175,       311374,       289892,       271175, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       314761,       267836, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1144668171), # 1.14GB, avg file size 1.14GB
  ("fsize_db",                        13033305340), # 13.03GB, avg file size 3.26GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_0_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       332124,       272079, ],
    'CountWeightedL1PrefireNom'                                  : [       287829,       287800,       287858, ],
    'CountWeightedL1Prefire'                                     : [       287829,       284997,       290670, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       317007,       287825,       263748,       317007,       287825,       263748,       317007,       287825,       263748, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       319137,       261654, ],
  }),
  ("nof_tree_events",                 299402),
  ("nof_db_events",                   299402),
  ("fsize_local",                     1221178819), # 1.22GB, avg file size 1.22GB
  ("fsize_db",                        13628421160), # 13.63GB, avg file size 2.73GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1p5_1_1_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       333634,       267566, ],
    'CountWeightedL1PrefireNom'                                  : [       285149,       285125,       285143, ],
    'CountWeightedL1Prefire'                                     : [       285149,       282270,       288046, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       318568,       285146,       258219,       318568,       285146,       258219,       318568,       285146,       258219, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       320014,       256805, ],
  }),
  ("nof_tree_events",                 297179),
  ("nof_db_events",                   297179),
  ("fsize_local",                     1269108971), # 1.27GB, avg file size 1.27GB
  ("fsize_db",                        14044768795), # 14.04GB, avg file size 2.81GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_0p5_1_1_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       384360,       238119, ],
    'CountWeightedL1PrefireNom'                                  : [       293947,       293931,       293955, ],
    'CountWeightedL1Prefire'                                     : [       293947,       292418,       295476, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       376518,       355501,       335784,       311339,       293945,       277599,       261737,       247082,       233336, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       376518,       233336, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1163567601), # 1.16GB, avg file size 1.16GB
  ("fsize_db",                        13376661186), # 13.38GB, avg file size 2.68GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_sm_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       382913,       238903, ],
    'CountWeightedL1PrefireNom'                                  : [       294254,       294257,       294234, ],
    'CountWeightedL1Prefire'                                     : [       294254,       292796,       295708, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       375496,       356736,       338742,       309751,       294251,       279369,       259882,       246844,       234350, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       375496,       234350, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1136370826), # 1.14GB, avg file size 1.14GB
  ("fsize_db",                        13225066454), # 13.23GB, avg file size 4.41GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_box_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       385630,       237448, ],
    'CountWeightedL1PrefireNom'                                  : [       293862,       293845,       293868, ],
    'CountWeightedL1Prefire'                                     : [       293862,       292326,       295392, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       377671,       354790,       333759,       312931,       293859,       276370,       263552,       247424,       232635, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       377671,       232635, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1182342548), # 1.18GB, avg file size 1.18GB
  ("fsize_db",                        13519407617), # 13.52GB, avg file size 3.38GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_1_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [        10753,         6402, ],
    'CountWeightedL1PrefireNom'                                  : [         8033,         8033,         8033, ],
    'CountWeightedL1Prefire'                                     : [         8033,         7988,         8078, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        10511,         9594,         8803,         8805,         8033,         7369,         7484,         6826,         6260, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [        10511,         6260, ],
  }),
  ("nof_tree_events",                 8218),
  ("nof_db_events",                   300000),
  ("fsize_local",                     36387251), # 36.39MB, avg file size 36.39MB
  ("fsize_db",                        14649063726), # 14.65GB, avg file size 3.66GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_2_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       385312,       237609, ],
    'CountWeightedL1PrefireNom'                                  : [       293906,       293840,       293838, ],
    'CountWeightedL1Prefire'                                     : [       293906,       292368,       295441, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       377371,       354891,       334095,       312545,       293904,       276604,       263109,       247349,       232791, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       377371,       232791, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1178571169), # 1.18GB, avg file size 1.18GB
  ("fsize_db",                        13601999029), # 13.60GB, avg file size 4.53GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_3_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       383461,       238612, ],
    'CountWeightedL1PrefireNom'                                  : [       294120,       294113,       294089, ],
    'CountWeightedL1Prefire'                                     : [       294120,       292637,       295604, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       375882,       356312,       337717,       310331,       294118,       278735,       260562,       246918,       233973, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       375882,       233973, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1145911658), # 1.15GB, avg file size 1.15GB
  ("fsize_db",                        13322107044), # 13.32GB, avg file size 4.44GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_4_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       389049,       235614, ],
    'CountWeightedL1PrefireNom'                                  : [       293483,       293413,       293417, ],
    'CountWeightedL1Prefire'                                     : [       293483,       291863,       295104, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       380472,       352324,       327365,       317000,       293479,       272574,       268222,       248213,       230504, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       380472,       230504, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1232178331), # 1.23GB, avg file size 1.23GB
  ("fsize_db",                        14057961060), # 14.06GB, avg file size 3.51GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_5_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       382864,       238949, ],
    'CountWeightedL1PrefireNom'                                  : [       294384,       294395,       294439, ],
    'CountWeightedL1Prefire'                                     : [       294384,       292964,       295801, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       375641,       357093,       339354,       309787,       294378,       279696,       259876,       246906,       234523, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       375641,       234523, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1133968271), # 1.13GB, avg file size 1.13GB
  ("fsize_db",                        13143785774), # 13.14GB, avg file size 3.29GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_6_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       379147,       240959, ],
    'CountWeightedL1PrefireNom'                                  : [       295004,       295007,       295027, ],
    'CountWeightedL1Prefire'                                     : [       295004,       293710,       296294, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       372765,       360033,       346711,       305458,       295000,       284051,       254870,       246115,       236969, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       372765,       236969, ],
  }),
  ("nof_tree_events",                 299997),
  ("nof_db_events",                   299997),
  ("fsize_local",                     1066229823), # 1.07GB, avg file size 1.07GB
  ("fsize_db",                        12803480606), # 12.80GB, avg file size 3.20GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_7_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       385549,       237496, ],
    'CountWeightedL1PrefireNom'                                  : [       293816,       293851,       293819, ],
    'CountWeightedL1Prefire'                                     : [       293816,       292272,       295351, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       377570,       354829,       333900,       312787,       293813,       276444,       263385,       247372,       232668, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       377570,       232668, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1179082253), # 1.18GB, avg file size 1.18GB
  ("fsize_db",                        13552950610), # 13.55GB, avg file size 4.52GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_8_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       387741,       236307, ],
    'CountWeightedL1PrefireNom'                                  : [       293479,       293502,       293523, ],
    'CountWeightedL1Prefire'                                     : [       293479,       291872,       295084, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       379282,       353084,       329529,       315369,       293478,       273871,       266377,       247860,       231233, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       379282,       231233, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1217299339), # 1.22GB, avg file size 1.22GB
  ("fsize_db",                        13997106004), # 14.00GB, avg file size 4.67GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_9_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       379916,       240548, ],
    'CountWeightedL1PrefireNom'                                  : [       294894,       294912,       294837, ],
    'CountWeightedL1Prefire'                                     : [       294894,       293571,       296206, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       373357,       359477,       345325,       306327,       294884,       283204,       255879,       246256,       236474, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       373357,       236474, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1078274120), # 1.08GB, avg file size 1.08GB
  ("fsize_db",                        12822566212), # 12.82GB, avg file size 3.21GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_10_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       382107,       238419, ],
    'CountWeightedL1PrefireNom'                                  : [       293816,       293770,       293821, ],
    'CountWeightedL1Prefire'                                     : [       293816,       292409,       295223, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       374948,       356379,       338649,       309233,       293814,       279114,       259432,       246420,       234035, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       374948,       234035, ],
  }),
  ("nof_tree_events",                 299364),
  ("nof_db_events",                   299364),
  ("fsize_local",                     1129131809), # 1.13GB, avg file size 1.13GB
  ("fsize_db",                        13315340669), # 13.32GB, avg file size 2.66GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_11_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       380853,       240025, ],
    'CountWeightedL1PrefireNom'                                  : [       294675,       294645,       294693, ],
    'CountWeightedL1Prefire'                                     : [       294675,       293305,       296046, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       373999,       358527,       343073,       307402,       294673,       281914,       257144,       246443,       235775, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       373999,       235775, ],
  }),
  ("nof_tree_events",                 299997),
  ("nof_db_events",                   299997),
  ("fsize_local",                     1098724730), # 1.10GB, avg file size 1.10GB
  ("fsize_db",                        13025018010), # 13.03GB, avg file size 3.26GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_12_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_node_SM_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_sm_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299996, ],
    'CountWeighted'                                              : [       299973,       299945,       299933, ],
    'CountWeightedLHEWeightScale'                                : [       384329,       362833,       342671,       317803,       299971,       283298,       267179,       252181,       238129, ],
    'CountWeightedLHEEnvelope'                                   : [       384329,       238129, ],
    'CountWeightedL1PrefireNom'                                  : [       293881,       293857,       293877, ],
    'CountWeightedL1Prefire'                                     : [       293881,       292339,       295424, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       376449,       355462,       335762,       311283,       293878,       277583,       261692,       247052,       233323, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       376449,       233323, ],
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     1203583107), # 1.20GB, avg file size 1.20GB
  ("fsize_db",                        13758086324), # 13.76GB, avg file size 3.44GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_sm_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_node_box_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_box_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       299998, ],
    'CountWeighted'                                              : [       300025,       300008,       299989, ],
    'CountWeightedLHEWeightScale'                                : [       382906,       363726,       345344,       315857,       300022,       284809,       264999,       251669,       238905, ],
    'CountWeightedLHEEnvelope'                                   : [       382906,       238905, ],
    'CountWeightedL1PrefireNom'                                  : [       294212,       294192,       294196, ],
    'CountWeightedL1Prefire'                                     : [       294212,       292733,       295690, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       375434,       356698,       338726,       309687,       294209,       279346,       259819,       246798,       234320, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       375434,       234320, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1171711221), # 1.17GB, avg file size 1.17GB
  ("fsize_db",                        13554966138), # 13.55GB, avg file size 2.71GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_box_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_node-1_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_1_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                      : [       299994, ],
    'CountWeighted'                                              : [       299978,       299939,       300005, ],
    'CountWeightedLHEWeightScale'                                : [       385637,       362145,       340580,       319563,       299968,       282047,       269163,       252604,       237438, ],
    'CountWeightedLHEEnvelope'                                   : [       385637,       237438, ],
    'CountWeightedL1PrefireNom'                                  : [       293771,       293742,       293797, ],
    'CountWeightedL1Prefire'                                     : [       293771,       292212,       295329, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       377570,       354662,       333614,       312865,       293764,       276266,       263511,       247364,       232562, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       377570,       232562, ],
  }),
  ("nof_tree_events",                 299994),
  ("nof_db_events",                   299994),
  ("fsize_local",                     1222872669), # 1.22GB, avg file size 1.22GB
  ("fsize_db",                        14226816913), # 14.23GB, avg file size 2.37GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_1_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_node-2_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_2_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       299996, ],
    'CountWeighted'                                              : [       299933,       299951,       300041, ],
    'CountWeightedLHEWeightScale'                                : [       392378,       358371,       329047,       328595,       299933,       275355,       279230,       254841,       233845, ],
    'CountWeightedLHEEnvelope'                                   : [       392378,       233845, ],
    'CountWeightedL1PrefireNom'                                  : [       293046,       293044,       293118, ],
    'CountWeightedL1Prefire'                                     : [       293046,       291346,       294742, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       383258,       350124,       321538,       320945,       293044,       269060,       272719,       248961,       228492, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       383258,       228492, ],
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     1311325821), # 1.31GB, avg file size 1.31GB
  ("fsize_db",                        15065193278), # 15.07GB, avg file size 3.01GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_2_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_node-3_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_3_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299201, ],
    'CountWeighted'                                              : [       299174,       299202,       299284, ],
    'CountWeightedLHEWeightScale'                                : [       384293,       361320,       340088,       318285,       299174,       281574,       267947,       251843,       236973, ],
    'CountWeightedLHEEnvelope'                                   : [       384293,       236973, ],
    'CountWeightedL1PrefireNom'                                  : [       292998,       293001,       293076, ],
    'CountWeightedL1Prefire'                                     : [       292998,       291435,       294556, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       376276,       353857,       333122,       311636,       292996,       275799,       262345,       246629,       232110, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       376276,       232110, ],
  }),
  ("nof_tree_events",                 299201),
  ("nof_db_events",                   299201),
  ("fsize_local",                     1216775380), # 1.22GB, avg file size 1.22GB
  ("fsize_db",                        14042794496), # 14.04GB, avg file size 3.51GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_3_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_node-4_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_4_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       299998, ],
    'CountWeighted'                                              : [       299999,       300102,       299972, ],
    'CountWeightedLHEWeightScale'                                : [       383460,       363429,       344410,       316587,       299991,       284261,       265816,       251845,       238616, ],
    'CountWeightedLHEEnvelope'                                   : [       383460,       238616, ],
    'CountWeightedL1PrefireNom'                                  : [       294075,       294127,       294064, ],
    'CountWeightedL1Prefire'                                     : [       294075,       292567,       295579, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       375816,       356258,       337674,       310270,       294069,       278696,       260506,       246869,       233938, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       375816,       233938, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1183922595), # 1.18GB, avg file size 1.18GB
  ("fsize_db",                        13734345217), # 13.73GB, avg file size 2.75GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_4_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_node-5_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_5_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                      : [       299996, ],
    'CountWeighted'                                              : [       299940,       299978,       299994, ],
    'CountWeightedLHEWeightScale'                                : [       389003,       360215,       334692,       324087,       299938,       278656,       274200,       253745,       235637, ],
    'CountWeightedLHEEnvelope'                                   : [       389003,       235637, ],
    'CountWeightedL1PrefireNom'                                  : [       293316,       293330,       293359, ],
    'CountWeightedL1Prefire'                                     : [       293316,       291666,       294965, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       380303,       352245,       327354,       316827,       293313,       272537,       268050,       248113,       230455, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       380303,       230455, ],
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     1273628513), # 1.27GB, avg file size 1.27GB
  ("fsize_db",                        14660310040), # 14.66GB, avg file size 2.44GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_5_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_node-6_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_6_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       299978,       299944,       299985, ],
    'CountWeightedLHEWeightScale'                                : [       382838,       363872,       345748,       315737,       299977,       284980,       264878,       251607,       238964, ],
    'CountWeightedLHEEnvelope'                                   : [       382838,       238964, ],
    'CountWeightedL1PrefireNom'                                  : [       294365,       294338,       294379, ],
    'CountWeightedL1Prefire'                                     : [       294365,       292934,       295793, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       375589,       357070,       339354,       309743,       294362,       279698,       259842,       246884,       234525, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       375589,       234525, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1169420514), # 1.17GB, avg file size 1.17GB
  ("fsize_db",                        13255677867), # 13.26GB, avg file size 4.42GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_6_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_node-7_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_7_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299998, ],
    'CountWeighted'                                              : [       299984,       299953,       299921, ],
    'CountWeightedLHEWeightScale'                                : [       379175,       366134,       352515,       310721,       299977,       288811,       259266,       250295,       240946, ],
    'CountWeightedLHEEnvelope'                                   : [       379175,       240946, ],
    'CountWeightedL1PrefireNom'                                  : [       294945,       294912,       294920, ],
    'CountWeightedL1Prefire'                                     : [       294945,       293635,       296247, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       372741,       359981,       346637,       305442,       294939,       283992,       254860,       246083,       236922, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       372741,       236922, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1088077079), # 1.09GB, avg file size 1.09GB
  ("fsize_db",                        12941536315), # 12.94GB, avg file size 3.24GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_7_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_node-8_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_8_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       299996, ],
    'CountWeighted'                                              : [       299985,       299970,       299951, ],
    'CountWeightedLHEWeightScale'                                : [       385526,       362243,       340829,       319384,       299984,       282186,       268944,       252551,       237503, ],
    'CountWeightedLHEEnvelope'                                   : [       385526,       237503, ],
    'CountWeightedL1PrefireNom'                                  : [       293810,       293797,       293791, ],
    'CountWeightedL1Prefire'                                     : [       293810,       292255,       295361, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       377501,       354791,       333891,       312722,       293807,       276429,       263325,       247338,       232650, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       377501,       232650, ],
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     1217947259), # 1.22GB, avg file size 1.22GB
  ("fsize_db",                        14190505186), # 14.19GB, avg file size 2.84GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_8_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_node-9_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_9_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       299591, ],
    'CountWeighted'                                              : [       299526,       299558,       299612, ],
    'CountWeightedLHEWeightScale'                                : [       387195,       360412,       336343,       321937,       299525,       279522,       271916,       252987,       235996, ],
    'CountWeightedLHEEnvelope'                                   : [       387195,       235996, ],
    'CountWeightedL1PrefireNom'                                  : [       293026,       293034,       293080, ],
    'CountWeightedL1Prefire'                                     : [       293026,       291396,       294647, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       378679,       352565,       329081,       314847,       293024,       273480,       265922,       247464,       230889, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       378679,       230889, ],
  }),
  ("nof_tree_events",                 299591),
  ("nof_db_events",                   299591),
  ("fsize_local",                     1257699393), # 1.26GB, avg file size 1.26GB
  ("fsize_db",                        14339474676), # 14.34GB, avg file size 2.87GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_9_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_node-10_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_10_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       299997, ],
    'CountWeighted'                                              : [       300052,       300009,       299942, ],
    'CountWeightedLHEWeightScale'                                : [       379838,       365750,       351368,       311636,       300049,       288144,       260296,       250528,       240589, ],
    'CountWeightedLHEEnvelope'                                   : [       379838,       240589, ],
    'CountWeightedL1PrefireNom'                                  : [       294961,       294930,       294897, ],
    'CountWeightedL1Prefire'                                     : [       294961,       293646,       296264, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       373351,       359580,       345502,       306302,       294957,       283323,       255833,       246286,       236557, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       373351,       236557, ],
  }),
  ("nof_tree_events",                 299997),
  ("nof_db_events",                   299997),
  ("fsize_local",                     1100156287), # 1.10GB, avg file size 1.10GB
  ("fsize_db",                        13151222527), # 13.15GB, avg file size 2.63GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_10_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_node-11_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_11_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                      : [       299994, ],
    'CountWeighted'                                              : [       300052,       299968,       299994, ],
    'CountWeightedLHEWeightScale'                                : [       382925,       363853,       345678,       315830,       300051,       284920,       264976,       251618,       238913, ],
    'CountWeightedLHEEnvelope'                                   : [       382925,       238913, ],
    'CountWeightedL1PrefireNom'                                  : [       294401,       294351,       294374, ],
    'CountWeightedL1Prefire'                                     : [       294401,       292973,       295831, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       375670,       357050,       339281,       309830,       294399,       279638,       259934,       246890,       234475, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       375670,       234475, ],
  }),
  ("nof_tree_events",                 299994),
  ("nof_db_events",                   299994),
  ("fsize_local",                     1164265566), # 1.16GB, avg file size 1.16GB
  ("fsize_db",                        13676249855), # 13.68GB, avg file size 2.28GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_11_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_node-12_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_12_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299994, ],
    'CountWeighted'                                              : [       299966,       299991,       299988, ],
    'CountWeightedLHEWeightScale'                                : [       380877,       365021,       349212,       313069,       299965,       286967,       261892,       250925,       240010, ],
    'CountWeightedLHEEnvelope'                                   : [       380877,       240010, ],
    'CountWeightedL1PrefireNom'                                  : [       294578,       294579,       294601, ],
    'CountWeightedL1Prefire'                                     : [       294578,       293184,       295960, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       373958,       358456,       342984,       307377,       294576,       281845,       257125,       246405,       235722, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       373958,       235722, ],
  }),
  ("nof_tree_events",                 299994),
  ("nof_db_events",                   299994),
  ("fsize_local",                     1126659434), # 1.13GB, avg file size 1.13GB
  ("fsize_db",                        13168943933), # 13.17GB, avg file size 3.29GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_12_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_M-250_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_250_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_250_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       299997, ],
    'CountWeighted'                                              : [       299987,       300030,       300044, ],
    'CountWeightedLHEWeightScale'                                : [       304877,       299987,       293426,       304877,       299987,       293426,       304877,       299987,       293426, ],
    'CountWeightedLHEEnvelope'                                   : [       304877,       293426, ],
    'CountWeightedL1PrefireNom'                                  : [       296017,       296035,       296064, ],
    'CountWeightedL1Prefire'                                     : [       296017,       294948,       297078, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       300809,       296016,       289563,       300809,       296016,       289563,       300809,       296016,       289563, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       300809,       289563, ],
  }),
  ("nof_tree_events",                 299997),
  ("nof_db_events",                   299997),
  ("fsize_local",                     968757064), # 968.76MB, avg file size 968.76MB
  ("fsize_db",                        12143344410), # 12.14GB, avg file size 2.43GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_250_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_M-260_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_260_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_260_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       299402, ],
    'CountWeighted'                                              : [       299421,       299326,       299384, ],
    'CountWeightedLHEWeightScale'                                : [       305157,       299420,       292140,       305157,       299420,       292140,       305157,       299420,       292140, ],
    'CountWeightedLHEEnvelope'                                   : [       305157,       292140, ],
    'CountWeightedL1PrefireNom'                                  : [       295292,       295227,       295271, ],
    'CountWeightedL1Prefire'                                     : [       295292,       294184,       296381, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       300925,       295289,       288134,       300925,       295289,       288134,       300925,       295289,       288134, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       300925,       288134, ],
  }),
  ("nof_tree_events",                 299402),
  ("nof_db_events",                   299402),
  ("fsize_local",                     979791293), # 979.79MB, avg file size 979.79MB
  ("fsize_db",                        12033567447), # 12.03GB, avg file size 2.41GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_260_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_M-270_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_270_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_270_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       299995, ],
    'CountWeighted'                                              : [       299992,       299997,       299974, ],
    'CountWeightedLHEWeightScale'                                : [       306633,       299991,       291998,       306633,       299991,       291998,       306633,       299991,       291998, ],
    'CountWeightedLHEEnvelope'                                   : [       306633,       291998, ],
    'CountWeightedL1PrefireNom'                                  : [       295721,       295718,       295713, ],
    'CountWeightedL1Prefire'                                     : [       295721,       294582,       296852, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       302232,       295719,       287868,       302232,       295719,       287868,       302232,       295719,       287868, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       302232,       287868, ],
  }),
  ("nof_tree_events",                 299995),
  ("nof_db_events",                   299995),
  ("fsize_local",                     995930356), # 995.93MB, avg file size 995.93MB
  ("fsize_db",                        12073887370), # 12.07GB, avg file size 2.41GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_270_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_M-300_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_300_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_300_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299996, ],
    'CountWeighted'                                              : [       299997,       300016,       299963, ],
    'CountWeightedLHEWeightScale'                                : [       308979,       299996,       290154,       308979,       299996,       290154,       308979,       299996,       290154, ],
    'CountWeightedLHEEnvelope'                                   : [       308979,       290154, ],
    'CountWeightedL1PrefireNom'                                  : [       295356,       295367,       295329, ],
    'CountWeightedL1Prefire'                                     : [       295356,       294133,       296573, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       304159,       295354,       285691,       304159,       295354,       285691,       304159,       295354,       285691, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       304159,       285691, ],
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     1033987695), # 1.03GB, avg file size 1.03GB
  ("fsize_db",                        12250780111), # 12.25GB, avg file size 3.06GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_300_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_M-350_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_350_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_350_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       299998, ],
    'CountWeighted'                                              : [       299963,       299967,       300028, ],
    'CountWeightedLHEWeightScale'                                : [       312387,       299963,       287463,       312387,       299963,       287463,       312387,       299963,       287463, ],
    'CountWeightedLHEEnvelope'                                   : [       312387,       287463, ],
    'CountWeightedL1PrefireNom'                                  : [       294710,       294696,       294771, ],
    'CountWeightedL1Prefire'                                     : [       294710,       293350,       296071, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       306855,       294709,       282451,       306855,       294709,       282451,       306855,       294709,       282451, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       306855,       282451, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1092679985), # 1.09GB, avg file size 1.09GB
  ("fsize_db",                        12822147007), # 12.82GB, avg file size 2.56GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_350_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_M-400_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_400_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_400_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       300043,       300016,       300049, ],
    'CountWeightedLHEWeightScale'                                : [       315244,       300043,       285256,       315244,       300043,       285256,       315244,       300043,       285256, ],
    'CountWeightedLHEEnvelope'                                   : [       315244,       285256, ],
    'CountWeightedL1PrefireNom'                                  : [       294366,       294338,       294383, ],
    'CountWeightedL1Prefire'                                     : [       294366,       292914,       295812, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       309250,       294365,       279908,       309250,       294365,       279908,       309250,       294365,       279908, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       309250,       279908, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1141421424), # 1.14GB, avg file size 1.14GB
  ("fsize_db",                        13147855533), # 13.15GB, avg file size 2.63GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_400_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_M-450_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_450_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_450_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       292028, ],
    'CountWeighted'                                              : [       292002,       292031,       292061, ],
    'CountWeightedLHEWeightScale'                                : [       309283,       292001,       275798,       309283,       292001,       275798,       309283,       292001,       275798, ],
    'CountWeightedLHEEnvelope'                                   : [       309283,       275798, ],
    'CountWeightedL1PrefireNom'                                  : [       286164,       286170,       286206, ],
    'CountWeightedL1Prefire'                                     : [       286164,       284680,       287649, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       303034,       286162,       270308,       303034,       286162,       270308,       303034,       286162,       270308, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       303034,       270308, ],
  }),
  ("nof_tree_events",                 292028),
  ("nof_db_events",                   292028),
  ("fsize_local",                     1152439009), # 1.15GB, avg file size 1.15GB
  ("fsize_db",                        13118198421), # 13.12GB, avg file size 3.28GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_450_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_M-500_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_500_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_500_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       299997, ],
    'CountWeighted'                                              : [       299986,       300030,       299913, ],
    'CountWeightedLHEWeightScale'                                : [       319913,       299986,       281668,       319913,       299986,       281668,       319913,       299986,       281668, ],
    'CountWeightedLHEEnvelope'                                   : [       319913,       281668, ],
    'CountWeightedL1PrefireNom'                                  : [       293638,       293660,       293592, ],
    'CountWeightedL1Prefire'                                     : [       293638,       292040,       295232, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       313081,       293637,       275737,       313081,       293637,       275737,       313081,       293637,       275737, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       313081,       275737, ],
  }),
  ("nof_tree_events",                 299997),
  ("nof_db_events",                   299997),
  ("fsize_local",                     1223191868), # 1.22GB, avg file size 1.22GB
  ("fsize_db",                        13799384403), # 13.80GB, avg file size 2.76GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_500_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_M-550_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_550_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_550_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299996, ],
    'CountWeighted'                                              : [       300055,       299982,       299985, ],
    'CountWeightedLHEWeightScale'                                : [       321848,       300055,       280185,       321848,       300055,       280185,       321848,       300055,       280185, ],
    'CountWeightedLHEEnvelope'                                   : [       321848,       280185, ],
    'CountWeightedL1PrefireNom'                                  : [       293490,       293447,       293454, ],
    'CountWeightedL1Prefire'                                     : [       293490,       291852,       295126, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       314777,       293488,       274117,       314777,       293488,       274117,       314777,       293488,       274117, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       314777,       274117, ],
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     1255407515), # 1.26GB, avg file size 1.26GB
  ("fsize_db",                        13970691602), # 13.97GB, avg file size 3.49GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_550_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_M-600_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_600_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_600_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       300036,       300028,       300051, ],
    'CountWeightedLHEWeightScale'                                : [       323625,       300028,       278845,       323625,       300028,       278845,       323625,       300028,       278845, ],
    'CountWeightedLHEEnvelope'                                   : [       323625,       278845, ],
    'CountWeightedL1PrefireNom'                                  : [       293189,       293185,       293203, ],
    'CountWeightedL1Prefire'                                     : [       293189,       291494,       294889, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       316204,       293182,       272542,       316204,       293182,       272542,       316204,       293182,       272542, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       316204,       272542, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1281619693), # 1.28GB, avg file size 1.28GB
  ("fsize_db",                        14217239886), # 14.22GB, avg file size 2.84GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_600_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_M-700_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_700_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_700_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299998, ],
    'CountWeighted'                                              : [       299993,       299940,       300040, ],
    'CountWeightedLHEWeightScale'                                : [       326693,       299992,       276553,       326693,       299992,       276553,       326693,       299992,       276553, ],
    'CountWeightedLHEEnvelope'                                   : [       326693,       276553, ],
    'CountWeightedL1PrefireNom'                                  : [       292892,       292858,       292921, ],
    'CountWeightedL1Prefire'                                     : [       292892,       291138,       294642, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       318912,       292890,       270042,       318912,       292890,       270042,       318912,       292890,       270042, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       318912,       270042, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1317238793), # 1.32GB, avg file size 1.32GB
  ("fsize_db",                        14467187735), # 14.47GB, avg file size 3.62GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_700_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_M-800_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_800_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_800_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       300039,       299921,       299937, ],
    'CountWeightedLHEWeightScale'                                : [       329331,       300037,       274610,       329331,       300037,       274610,       329331,       300037,       274610, ],
    'CountWeightedLHEEnvelope'                                   : [       329331,       274610, ],
    'CountWeightedL1PrefireNom'                                  : [       292684,       292616,       292634, ],
    'CountWeightedL1Prefire'                                     : [       292684,       290890,       294485, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       321238,       292681,       267932,       321238,       292681,       267932,       321238,       292681,       267932, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       321238,       267932, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1339396456), # 1.34GB, avg file size 1.34GB
  ("fsize_db",                        14975865562), # 14.98GB, avg file size 3.00GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_800_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_M-900_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_900_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_900_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       299926,       299943,       300018, ],
    'CountWeightedLHEWeightScale'                                : [       331702,       299925,       272913,       331702,       299925,       272913,       331702,       299925,       272913, ],
    'CountWeightedLHEEnvelope'                                   : [       331702,       272913, ],
    'CountWeightedL1PrefireNom'                                  : [       292413,       292422,       292468, ],
    'CountWeightedL1Prefire'                                     : [       292413,       290576,       294250, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       323309,       292411,       266087,       323309,       292411,       266087,       323309,       292411,       266087, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       323309,       266087, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1353094908), # 1.35GB, avg file size 1.35GB
  ("fsize_db",                        15010963358), # 15.01GB, avg file size 3.75GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_900_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_M-1000_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1000_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_1000_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       299469, ],
    'CountWeighted'                                              : [       299441,       299493,       299482, ],
    'CountWeightedLHEWeightScale'                                : [       333192,       299439,       270989,       333192,       299439,       270989,       333192,       299439,       270989, ],
    'CountWeightedLHEEnvelope'                                   : [       333192,       270989, ],
    'CountWeightedL1PrefireNom'                                  : [       291879,       291901,       291909, ],
    'CountWeightedL1Prefire'                                     : [       291879,       290038,       293720, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       324710,       291877,       264156,       324710,       291877,       264156,       324710,       291877,       264156, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       324710,       264156, ],
  }),
  ("nof_tree_events",                 299469),
  ("nof_db_events",                   299469),
  ("fsize_local",                     1358245074), # 1.36GB, avg file size 1.36GB
  ("fsize_db",                        15303436616), # 15.30GB, avg file size 3.06GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1000_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-250_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_250_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_250_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       299998, ],
    'CountWeighted'                                              : [       299982,       300054,       300019, ],
    'CountWeightedLHEWeightScale'                                : [       304803,       299967,       293479,       304803,       299967,       293479,       304803,       299967,       293479, ],
    'CountWeightedLHEEnvelope'                                   : [       304803,       293479, ],
    'CountWeightedL1PrefireNom'                                  : [       295870,       295908,       295903, ],
    'CountWeightedL1Prefire'                                     : [       295870,       294770,       296963, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       300590,       295859,       289472,       300590,       295859,       289472,       300590,       295859,       289472, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       300590,       289472, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     984637742), # 984.64MB, avg file size 984.64MB
  ("fsize_db",                        12270543882), # 12.27GB, avg file size 2.45GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_250_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-260_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_260_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_260_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       300001,       300019,       300032, ],
    'CountWeightedLHEWeightScale'                                : [       305778,       299998,       292707,       305778,       299998,       292707,       305778,       299998,       292707, ],
    'CountWeightedLHEEnvelope'                                   : [       305778,       292707, ],
    'CountWeightedL1PrefireNom'                                  : [       295711,       295717,       295736, ],
    'CountWeightedL1Prefire'                                     : [       295711,       294571,       296845, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       301375,       295707,       288549,       301375,       295707,       288549,       301375,       295707,       288549, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       301375,       288549, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1000854776), # 1.00GB, avg file size 1.00GB
  ("fsize_db",                        12407686965), # 12.41GB, avg file size 3.10GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_260_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-270_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_270_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_270_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       299231, ],
    'CountWeighted'                                              : [       299186,       299234,       299213, ],
    'CountWeightedLHEWeightScale'                                : [       305822,       299184,       291288,       305822,       299184,       291288,       305822,       299184,       291288, ],
    'CountWeightedLHEEnvelope'                                   : [       305822,       291288, ],
    'CountWeightedL1PrefireNom'                                  : [       294793,       294811,       294816, ],
    'CountWeightedL1Prefire'                                     : [       294793,       293624,       295956, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       301279,       294790,       287023,       301279,       294790,       287023,       301279,       294790,       287023, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       301279,       287023, ],
  }),
  ("nof_tree_events",                 299231),
  ("nof_db_events",                   299231),
  ("fsize_local",                     1013980253), # 1.01GB, avg file size 1.01GB
  ("fsize_db",                        12387077839), # 12.39GB, avg file size 2.48GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_270_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-300_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_300_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_300_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299998, ],
    'CountWeighted'                                              : [       300016,       300023,       300035, ],
    'CountWeightedLHEWeightScale'                                : [       308977,       300016,       290135,       308977,       300016,       290135,       308977,       300016,       290135, ],
    'CountWeightedLHEEnvelope'                                   : [       308977,       290135, ],
    'CountWeightedL1PrefireNom'                                  : [       295191,       295190,       295218, ],
    'CountWeightedL1Prefire'                                     : [       295191,       293934,       296448, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       303980,       295189,       285511,       303980,       295189,       285511,       303980,       295189,       285511, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       303980,       285511, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1059941277), # 1.06GB, avg file size 1.06GB
  ("fsize_db",                        12692339481), # 12.69GB, avg file size 3.17GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_300_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-350_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_350_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_350_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299402, ],
    'CountWeighted'                                              : [       299391,       299361,       299428, ],
    'CountWeightedLHEWeightScale'                                : [       311775,       299391,       286878,       311775,       299391,       286878,       311775,       299391,       286878, ],
    'CountWeightedLHEEnvelope'                                   : [       311775,       286878, ],
    'CountWeightedL1PrefireNom'                                  : [       294081,       294057,       294105, ],
    'CountWeightedL1Prefire'                                     : [       294081,       292709,       295447, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       306189,       294079,       281823,       306189,       294079,       281823,       306189,       294079,       281823, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       306189,       281823, ],
  }),
  ("nof_tree_events",                 299402),
  ("nof_db_events",                   299402),
  ("fsize_local",                     1122943739), # 1.12GB, avg file size 1.12GB
  ("fsize_db",                        13215909741), # 13.22GB, avg file size 3.30GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_350_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-400_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_400_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_400_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299993, ],
    'CountWeighted'                                              : [       300003,       299967,       300004, ],
    'CountWeightedLHEWeightScale'                                : [       315255,       300003,       285219,       315255,       300003,       285219,       315255,       300003,       285219, ],
    'CountWeightedLHEEnvelope'                                   : [       315255,       285219, ],
    'CountWeightedL1PrefireNom'                                  : [       294441,       294423,       294439, ],
    'CountWeightedL1Prefire'                                     : [       294441,       293026,       295853, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       309352,       294439,       279979,       309352,       294439,       279979,       309352,       294439,       279979, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       309352,       279979, ],
  }),
  ("nof_tree_events",                 299993),
  ("nof_db_events",                   299993),
  ("fsize_local",                     1178519304), # 1.18GB, avg file size 1.18GB
  ("fsize_db",                        13636388128), # 13.64GB, avg file size 3.41GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_400_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-450_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_450_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_450_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       299998, ],
    'CountWeighted'                                              : [       300061,       300090,       300009, ],
    'CountWeightedLHEWeightScale'                                : [       317722,       300060,       283332,       317722,       300060,       283332,       317722,       300060,       283332, ],
    'CountWeightedLHEEnvelope'                                   : [       317722,       283332, ],
    'CountWeightedL1PrefireNom'                                  : [       294234,       294247,       294201, ],
    'CountWeightedL1Prefire'                                     : [       294234,       292772,       295692, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       311517,       294233,       277893,       311517,       294233,       277893,       311517,       294233,       277893, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       311517,       277893, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1226147787), # 1.23GB, avg file size 1.23GB
  ("fsize_db",                        13995682190), # 14.00GB, avg file size 2.80GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_450_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-500_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_500_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_500_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       300073,       299948,       299979, ],
    'CountWeightedLHEWeightScale'                                : [       319930,       300053,       281658,       319930,       300053,       281658,       319930,       300053,       281658, ],
    'CountWeightedLHEEnvelope'                                   : [       319930,       281658, ],
    'CountWeightedL1PrefireNom'                                  : [       294142,       294064,       294085, ],
    'CountWeightedL1Prefire'                                     : [       294142,       292663,       295618, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       313568,       294127,       276158,       313568,       294127,       276158,       313568,       294127,       276158, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       313568,       276158, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1267379192), # 1.27GB, avg file size 1.27GB
  ("fsize_db",                        14208882340), # 14.21GB, avg file size 3.55GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_500_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-550_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_550_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_550_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299995, ],
    'CountWeighted'                                              : [       300072,       300042,       300025, ],
    'CountWeightedLHEWeightScale'                                : [       321860,       300070,       280176,       321860,       300070,       280176,       321860,       300070,       280176, ],
    'CountWeightedLHEEnvelope'                                   : [       321860,       280176, ],
    'CountWeightedL1PrefireNom'                                  : [       294073,       294048,       294055, ],
    'CountWeightedL1Prefire'                                     : [       294073,       292592,       295552, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       315398,       294071,       274641,       315398,       294071,       274641,       315398,       294071,       274641, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       315398,       274641, ],
  }),
  ("nof_tree_events",                 299995),
  ("nof_db_events",                   299995),
  ("fsize_local",                     1298641618), # 1.30GB, avg file size 1.30GB
  ("fsize_db",                        14478664969), # 14.48GB, avg file size 3.62GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_550_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-600_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_600_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_600_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299995, ],
    'CountWeighted'                                              : [       299952,       300021,       299984, ],
    'CountWeightedLHEWeightScale'                                : [       323629,       299949,       278844,       323629,       299949,       278844,       323629,       299949,       278844, ],
    'CountWeightedLHEEnvelope'                                   : [       323629,       278844, ],
    'CountWeightedL1PrefireNom'                                  : [       294022,       294057,       294044, ],
    'CountWeightedL1Prefire'                                     : [       294022,       292552,       295488, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       317156,       294019,       273354,       317156,       294019,       273354,       317156,       294019,       273354, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       317156,       273354, ],
  }),
  ("nof_tree_events",                 299995),
  ("nof_db_events",                   299995),
  ("fsize_local",                     1323062072), # 1.32GB, avg file size 1.32GB
  ("fsize_db",                        14654413374), # 14.65GB, avg file size 3.66GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_600_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-650_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_650_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_650_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       299997, ],
    'CountWeighted'                                              : [       299999,       299969,       300002, ],
    'CountWeightedLHEWeightScale'                                : [       325220,       299990,       277678,       325220,       299990,       277678,       325220,       299990,       277678, ],
    'CountWeightedLHEEnvelope'                                   : [       325220,       277678, ],
    'CountWeightedL1PrefireNom'                                  : [       294116,       294076,       294140, ],
    'CountWeightedL1Prefire'                                     : [       294116,       292670,       295565, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       318794,       294109,       272263,       318794,       294109,       272263,       318794,       294109,       272263, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       318794,       272263, ],
  }),
  ("nof_tree_events",                 299997),
  ("nof_db_events",                   299997),
  ("fsize_local",                     1341006344), # 1.34GB, avg file size 1.34GB
  ("fsize_db",                        14989654961), # 14.99GB, avg file size 3.00GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_650_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-700_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_700_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_700_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       299995, ],
    'CountWeighted'                                              : [       299979,       299990,       299945, ],
    'CountWeightedLHEWeightScale'                                : [       326709,       299979,       276576,       326709,       299979,       276576,       326709,       299979,       276576, ],
    'CountWeightedLHEEnvelope'                                   : [       326709,       276576, ],
    'CountWeightedL1PrefireNom'                                  : [       293984,       293986,       293974, ],
    'CountWeightedL1Prefire'                                     : [       293984,       292512,       295454, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       320129,       293982,       271068,       320129,       293982,       271068,       320129,       293982,       271068, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       320129,       271068, ],
  }),
  ("nof_tree_events",                 299995),
  ("nof_db_events",                   299995),
  ("fsize_local",                     1352550082), # 1.35GB, avg file size 1.35GB
  ("fsize_db",                        15100949761), # 15.10GB, avg file size 3.02GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_700_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-800_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_800_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_800_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                      : [       299998, ],
    'CountWeighted'                                              : [       299962,       300054,       299991, ],
    'CountWeightedLHEWeightScale'                                : [       329360,       299961,       274621,       329360,       299961,       274621,       329360,       299961,       274621, ],
    'CountWeightedLHEEnvelope'                                   : [       329360,       274621, ],
    'CountWeightedL1PrefireNom'                                  : [       294051,       294102,       294072, ],
    'CountWeightedL1Prefire'                                     : [       294051,       292604,       295495, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       322817,       294049,       269222,       322817,       294049,       269222,       322817,       294049,       269222, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       322817,       269222, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1366084221), # 1.37GB, avg file size 1.37GB
  ("fsize_db",                        15643527631), # 15.64GB, avg file size 2.61GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_800_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-900_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_900_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_900_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       300047,       299968,       300037, ],
    'CountWeightedLHEWeightScale'                                : [       331689,       300042,       272952,       331689,       300042,       272952,       331689,       300042,       272952, ],
    'CountWeightedLHEEnvelope'                                   : [       331689,       272952, ],
    'CountWeightedL1PrefireNom'                                  : [       294209,       294159,       294203, ],
    'CountWeightedL1Prefire'                                     : [       294209,       292795,       295626, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       325221,       294204,       267671,       325221,       294204,       267671,       325221,       294204,       267671, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       325221,       267671, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1372721171), # 1.37GB, avg file size 1.37GB
  ("fsize_db",                        15836490873), # 15.84GB, avg file size 2.64GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_900_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-1000_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1000_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_1000_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       299997, ],
    'CountWeighted'                                              : [       300052,       299919,       300029, ],
    'CountWeightedLHEWeightScale'                                : [       333739,       300051,       271429,       333739,       300051,       271429,       333739,       300051,       271429, ],
    'CountWeightedLHEEnvelope'                                   : [       333739,       271429, ],
    'CountWeightedL1PrefireNom'                                  : [       294227,       294130,       294224, ],
    'CountWeightedL1Prefire'                                     : [       294227,       292821,       295638, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       327265,       294225,       266194,       327265,       294225,       266194,       327265,       294225,       266194, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       327265,       266194, ],
  }),
  ("nof_tree_events",                 299997),
  ("nof_db_events",                   299997),
  ("fsize_local",                     1375172118), # 1.38GB, avg file size 1.38GB
  ("fsize_db",                        15848133420), # 15.85GB, avg file size 3.17GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_1000_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [        50807,        48908, ],
    'CountWeightedL1PrefireNom'                                  : [        49295,        49288,        49296, ],
    'CountWeightedL1Prefire'                                     : [        49295,        49105,        49482, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        50084,        49295,        48223,        50084,        49295,        48223,        50084,        49295,        48223, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [        50084,        48223, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     163772411), # 163.77MB, avg file size 163.77MB
  ("fsize_db",                        1962681716), # 1.96GB, avg file size 1.96GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [        50955,        48787, ],
    'CountWeightedL1PrefireNom'                                  : [        49279,        49275,        49284, ],
    'CountWeightedL1Prefire'                                     : [        49279,        49087,        49470, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        50216,        49279,        48091,        50216,        49279,        48091,        50216,        49279,        48091, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [        50216,        48091, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     165687164), # 165.69MB, avg file size 165.69MB
  ("fsize_db",                        1978376178), # 1.98GB, avg file size 1.98GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_260_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [        51103,        48669, ],
    'CountWeightedL1PrefireNom'                                  : [        49240,        49246,        49239, ],
    'CountWeightedL1Prefire'                                     : [        49240,        49039,        49440, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        50322,        49240,        47938,        50322,        49240,        47938,        50322,        49240,        47938, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [        50322,        47938, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     167665815), # 167.67MB, avg file size 167.67MB
  ("fsize_db",                        1992599467), # 1.99GB, avg file size 1.99GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_270_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [        50828,        48175, ],
    'CountWeightedL1PrefireNom'                                  : [        48846,        48836,        48848, ],
    'CountWeightedL1Prefire'                                     : [        48846,        48645,        49045, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        50045,        48846,        47444,        50045,        48846,        47444,        50045,        48846,        47444, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [        50045,        47444, ],
  }),
  ("nof_tree_events",                 49600),
  ("nof_db_events",                   49600),
  ("fsize_local",                     168286887), # 168.29MB, avg file size 168.29MB
  ("fsize_db",                        1985262651), # 1.99GB, avg file size 1.99GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_280_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       463472,       435231, ],
    'CountWeightedL1PrefireNom'                                  : [       442708,       442678,       442676, ],
    'CountWeightedL1Prefire'                                     : [       442708,       440790,       444624, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       455872,       442708,       428202,       455872,       442708,       428202,       455872,       442708,       428202, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       455872,       428202, ],
  }),
  ("nof_tree_events",                 450000),
  ("nof_db_events",                   450000),
  ("fsize_local",                     1545967907), # 1.55GB, avg file size 1.55GB
  ("fsize_db",                        18335508201), # 18.34GB, avg file size 2.62GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_300_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [        51731,        48171, ],
    'CountWeightedL1PrefireNom'                                  : [        49146,        49150,        49147, ],
    'CountWeightedL1Prefire'                                     : [        49146,        48924,        49367, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        50842,        49146,        47357,        50842,        49146,        47357,        50842,        49146,        47357, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [        50842,        47357, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     176512587), # 176.51MB, avg file size 176.51MB
  ("fsize_db",                        2102297139), # 2.10GB, avg file size 1.05GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_320_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [        49881,        46073, ],
    'CountWeightedL1PrefireNom'                                  : [        47132,        47135,        47132, ],
    'CountWeightedL1Prefire'                                     : [        47132,        46908,        47356, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        48973,        47132,        45247,        48973,        47132,        45247,        48973,        47132,        45247, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [        48973,        45247, ],
  }),
  ("nof_tree_events",                 48000),
  ("nof_db_events",                   48000),
  ("fsize_local",                     172491483), # 172.49MB, avg file size 172.49MB
  ("fsize_db",                        1955847184), # 1.96GB, avg file size 1.96GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_340_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [        52062,        47913, ],
    'CountWeightedL1PrefireNom'                                  : [        49091,        49091,        49100, ],
    'CountWeightedL1Prefire'                                     : [        49091,        48858,        49323, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        51114,        49091,        47054,        51114,        49091,        47054,        51114,        49091,        47054, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [        51114,        47054, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     181404447), # 181.40MB, avg file size 181.40MB
  ("fsize_db",                        2167356346), # 2.17GB, avg file size 2.17GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_350_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       262684,       237709, ],
    'CountWeightedL1PrefireNom'                                  : [       245061,       245069,       245069, ],
    'CountWeightedL1Prefire'                                     : [       245061,       243805,       246312, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       257459,       245061,       233056,       257459,       245061,       233056,       257459,       245061,       233056, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       257459,       233056, ],
  }),
  ("nof_tree_events",                 250000),
  ("nof_db_events",                   250000),
  ("fsize_local",                     938812261), # 938.81MB, avg file size 938.81MB
  ("fsize_db",                        10749996877), # 10.75GB, avg file size 3.58GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_400_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       105485,        94063, ],
    'CountWeightedL1PrefireNom'                                  : [        97512,        97510,        97521, ],
    'CountWeightedL1Prefire'                                     : [        97512,        96986,        98039, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       103247,        97512,        92101,       103247,        97512,        92101,       103247,        97512,        92101, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       103247,        92101, ],
  }),
  ("nof_tree_events",                 99600),
  ("nof_db_events",                   99600),
  ("fsize_local",                     388371315), # 388.37MB, avg file size 388.37MB
  ("fsize_db",                        4411305292), # 4.41GB, avg file size 2.21GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_450_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       105773,        93134, ],
    'CountWeightedL1PrefireNom'                                  : [        97028,        97014,        97036, ],
    'CountWeightedL1Prefire'                                     : [        97028,        96484,        97572, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       103437,        97028,        91106,       103437,        97028,        91106,       103437,        97028,        91106, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       103437,        91106, ],
  }),
  ("nof_tree_events",                 99200),
  ("nof_db_events",                   99200),
  ("fsize_local",                     398659165), # 398.66MB, avg file size 398.66MB
  ("fsize_db",                        4435751146), # 4.44GB, avg file size 2.22GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       107278,        93402, ],
    'CountWeightedL1PrefireNom'                                  : [        97768,        97759,        97745, ],
    'CountWeightedL1Prefire'                                     : [        97768,        97209,        98328, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       104851,        97768,        91320,       104851,        97768,        91320,       104851,        97768,        91320, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       104851,        91320, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     412217458), # 412.22MB, avg file size 412.22MB
  ("fsize_db",                        4499327267), # 4.50GB, avg file size 2.25GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_550_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       107866,        92956, ],
    'CountWeightedL1PrefireNom'                                  : [        97653,        97646,        97647, ],
    'CountWeightedL1Prefire'                                     : [        97653,        97071,        98235, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       105311,        97653,        90783,       105311,        97653,        90783,       105311,        97653,        90783, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       105311,        90783, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     420489722), # 420.49MB, avg file size 420.49MB
  ("fsize_db",                        4581235338), # 4.58GB, avg file size 2.29GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_600_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       108413,        92554, ],
    'CountWeightedL1PrefireNom'                                  : [        97623,        97623,        97646, ],
    'CountWeightedL1Prefire'                                     : [        97623,        97039,        98208, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       105820,        97623,        90372,       105820,        97623,        90372,       105820,        97623,        90372, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       105820,        90372, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     427883085), # 427.88MB, avg file size 427.88MB
  ("fsize_db",                        4742625025), # 4.74GB, avg file size 2.37GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_650_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       109795,        91539, ],
    'CountWeightedL1PrefireNom'                                  : [        97490,        97485,        97500, ],
    'CountWeightedL1Prefire'                                     : [        97490,        96879,        98100, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       107022,        97490,        89256,       107022,        97490,        89256,       107022,        97490,        89256, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       107022,        89256, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     444686870), # 444.69MB, avg file size 444.69MB
  ("fsize_db",                        4845795202), # 4.85GB, avg file size 2.42GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_800_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       110555,        90983, ],
    'CountWeightedL1PrefireNom'                                  : [        97455,        97446,        97450, ],
    'CountWeightedL1Prefire'                                     : [        97455,        96837,        98073, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       107730,        97455,        88682,       107730,        97455,        88682,       107730,        97455,        88682, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       107730,        88682, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     452775744), # 452.78MB, avg file size 452.78MB
  ("fsize_db",                        4858199935), # 4.86GB, avg file size 2.43GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_900_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [        50810,        48905, ],
    'CountWeightedL1PrefireNom'                                  : [        49278,        49274,        49278, ],
    'CountWeightedL1Prefire'                                     : [        49278,        49086,        49469, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        50071,        49278,        48204,        50071,        49278,        48204,        50071,        49278,        48204, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [        50071,        48204, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     165740192), # 165.74MB, avg file size 165.74MB
  ("fsize_db",                        1970267888), # 1.97GB, avg file size 1.97GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [        50954,        48790, ],
    'CountWeightedL1PrefireNom'                                  : [        49245,        49251,        49250, ],
    'CountWeightedL1Prefire'                                     : [        49245,        49046,        49443, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        50181,        49245,        48062,        50181,        49245,        48062,        50181,        49245,        48062, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [        50181,        48062, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     167933538), # 167.93MB, avg file size 167.93MB
  ("fsize_db",                        2021288641), # 2.02GB, avg file size 2.02GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_260_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [        51100,        48672, ],
    'CountWeightedL1PrefireNom'                                  : [        49210,        49212,        49213, ],
    'CountWeightedL1Prefire'                                     : [        49210,        49002,        49417, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        50288,        49210,        47910,        50288,        49210,        47910,        50288,        49210,        47910, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [        50288,        47910, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     170433911), # 170.43MB, avg file size 170.43MB
  ("fsize_db",                        2049006927), # 2.05GB, avg file size 2.05GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_270_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [        51238,        48559, ],
    'CountWeightedL1PrefireNom'                                  : [        49188,        49191,        49188, ],
    'CountWeightedL1Prefire'                                     : [        49188,        48977,        49399, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        50403,        49188,        47780,        50403,        49188,        47780,        50403,        49188,        47780, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [        50403,        47780, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     172594682), # 172.59MB, avg file size 172.59MB
  ("fsize_db",                        2024724980), # 2.02GB, avg file size 2.02GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_280_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       460790,       432712, ],
    'CountWeightedL1PrefireNom'                                  : [       439952,       439915,       439906, ],
    'CountWeightedL1Prefire'                                     : [       439952,       438009,       441889, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       453024,       439952,       425540,       453024,       439952,       425540,       453024,       439952,       425540, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       453024,       425540, ],
  }),
  ("nof_tree_events",                 447400),
  ("nof_db_events",                   447400),
  ("fsize_local",                     1568136133), # 1.57GB, avg file size 1.57GB
  ("fsize_db",                        18368864093), # 18.37GB, avg file size 3.67GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_300_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [        51729,        48169, ],
    'CountWeightedL1PrefireNom'                                  : [        49131,        49130,        49140, ],
    'CountWeightedL1Prefire'                                     : [        49131,        48908,        49354, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        50828,        49131,        47344,        50828,        49131,        47344,        50828,        49131,        47344, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [        50828,        47344, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     180660770), # 180.66MB, avg file size 180.66MB
  ("fsize_db",                        2056109122), # 2.06GB, avg file size 2.06GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_320_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [        51958,        47993, ],
    'CountWeightedL1PrefireNom'                                  : [        49106,        49112,        49110, ],
    'CountWeightedL1Prefire'                                     : [        49106,        48878,        49334, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        51023,        49106,        47144,        51023,        49106,        47144,        51023,        49106,        47144, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [        51023,        47144, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     184090741), # 184.09MB, avg file size 184.09MB
  ("fsize_db",                        2082210498), # 2.08GB, avg file size 2.08GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_340_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [        52061,        47912, ],
    'CountWeightedL1PrefireNom'                                  : [        49102,        49097,        49107, ],
    'CountWeightedL1Prefire'                                     : [        49102,        48872,        49332, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        51116,        49102,        47058,        51116,        49102,        47058,        51116,        49102,        47058, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [        51116,        47058, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     186206591), # 186.21MB, avg file size 186.21MB
  ("fsize_db",                        2097870831), # 2.10GB, avg file size 2.10GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_350_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       262682,       237714, ],
    'CountWeightedL1PrefireNom'                                  : [       245201,       245153,       245192, ],
    'CountWeightedL1Prefire'                                     : [       245201,       243988,       246417, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       257573,       245201,       233171,       257573,       245201,       233171,       257573,       245201,       233171, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       257573,       233171, ],
  }),
  ("nof_tree_events",                 250000),
  ("nof_db_events",                   250000),
  ("fsize_local",                     966034785), # 966.03MB, avg file size 966.03MB
  ("fsize_db",                        10695129460), # 10.70GB, avg file size 3.57GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_400_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       105906,        94447, ],
    'CountWeightedL1PrefireNom'                                  : [        98026,        98009,        98042, ],
    'CountWeightedL1Prefire'                                     : [        98026,        97533,        98520, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       103796,        98026,        92599,       103796,        98026,        92599,       103796,        98026,        92599, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       103796,        92599, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     401975696), # 401.98MB, avg file size 401.98MB
  ("fsize_db",                        4416939298), # 4.42GB, avg file size 2.21GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_450_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       106625,        93895, ],
    'CountWeightedL1PrefireNom'                                  : [        97987,        97994,        97989, ],
    'CountWeightedL1Prefire'                                     : [        97987,        97489,        98486, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       104463,        97987,        92023,       104463,        97987,        92023,       104463,        97987,        92023, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       104463,        92023, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     414396426), # 414.40MB, avg file size 414.40MB
  ("fsize_db",                        4450805287), # 4.45GB, avg file size 4.45GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       107293,        93392, ],
    'CountWeightedL1PrefireNom'                                  : [        97953,        97974,        97950, ],
    'CountWeightedL1Prefire'                                     : [        97953,        97448,        98456, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       105077,        97953,        91497,       105077,        97953,        91497,       105077,        97953,        91497, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       105077,        91497, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     424905786), # 424.91MB, avg file size 424.91MB
  ("fsize_db",                        4675550080), # 4.68GB, avg file size 2.34GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_550_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       107872,        92954, ],
    'CountWeightedL1PrefireNom'                                  : [        97987,        97942,        97971, ],
    'CountWeightedL1Prefire'                                     : [        97987,        97487,        98488, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       105652,        97987,        91073,       105652,        97987,        91073,       105652,        97987,        91073, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       105652,        91073, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     433148367), # 433.15MB, avg file size 433.15MB
  ("fsize_db",                        4653469892), # 4.65GB, avg file size 2.33GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_600_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       108412,        92550, ],
    'CountWeightedL1PrefireNom'                                  : [        97966,        97988,        97981, ],
    'CountWeightedL1Prefire'                                     : [        97966,        97469,        98461, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       106199,        97966,        90689,       106199,        97966,        90689,       106199,        97966,        90689, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       106199,        90689, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     440896870), # 440.90MB, avg file size 440.90MB
  ("fsize_db",                        4740249400), # 4.74GB, avg file size 2.37GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_650_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       109361,        91849, ],
    'CountWeightedL1PrefireNom'                                  : [        98030,        98027,        98041, ],
    'CountWeightedL1Prefire'                                     : [        98030,        97549,        98513, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       107185,        98030,        90046,       107185,        98030,        90046,       107185,        98030,        90046, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       107185,        90046, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     450945891), # 450.95MB, avg file size 450.95MB
  ("fsize_db",                        4895097500), # 4.90GB, avg file size 2.45GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       109785,        91539, ],
    'CountWeightedL1PrefireNom'                                  : [        98032,        98015,        98026, ],
    'CountWeightedL1Prefire'                                     : [        98032,        97549,        98513, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       107606,        98032,        89743,       107606,        98032,        89743,       107606,        98032,        89743, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       107606,        89743, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     455177974), # 455.18MB, avg file size 455.18MB
  ("fsize_db",                        4784663508), # 4.78GB, avg file size 4.78GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_800_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       321592,       273455, ],
    'CountWeightedL1PrefireNom'                                  : [       285770,       285793,       285815, ],
    'CountWeightedL1Prefire'                                     : [       285770,       283176,       288361, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       306934,       285767,       267373,       306934,       285767,       267373,       306934,       285767,       267373, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       310302,       264048, ],
  }),
  ("nof_tree_events",                 296060),
  ("nof_db_events",                   296060),
  ("fsize_local",                     1137950701), # 1.14GB, avg file size 1.14GB
  ("fsize_db",                        12663197291), # 12.66GB, avg file size 2.53GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_0_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       328763,       275224, ],
    'CountWeightedL1PrefireNom'                                  : [       287830,       287815,       287835, ],
    'CountWeightedL1Prefire'                                     : [       287830,       284799,       290877, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       312728,       287827,       266641,       312728,       287827,       266641,       312728,       287827,       266641, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       315260,       264151, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1155686692), # 1.16GB, avg file size 1.16GB
  ("fsize_db",                        12708206493), # 12.71GB, avg file size 3.18GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_1_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       280628,       236948, ],
    'CountWeightedL1PrefireNom'                                  : [       244168,       244161,       244146, ],
    'CountWeightedL1Prefire'                                     : [       244168,       241034,       247319, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       264317,       244165,       226977,       264317,       244165,       226977,       264317,       244165,       226977, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       266244,       225081, ],
  }),
  ("nof_tree_events",                 257175),
  ("nof_db_events",                   257175),
  ("fsize_local",                     1042948220), # 1.04GB, avg file size 1.04GB
  ("fsize_db",                        11297192364), # 11.30GB, avg file size 2.82GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_2_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       339162,       268596, ],
    'CountWeightedL1PrefireNom'                                  : [       287115,       287070,       287125, ],
    'CountWeightedL1Prefire'                                     : [       287115,       284056,       290193, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       323403,       287112,       258189,       323403,       287112,       258189,       323403,       287112,       258189, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       324510,       257111, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1338091626), # 1.34GB, avg file size 1.34GB
  ("fsize_db",                        14237299312), # 14.24GB, avg file size 2.85GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_2_1_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       332139,       271947, ],
    'CountWeightedL1PrefireNom'                                  : [       287288,       287320,       287320, ],
    'CountWeightedL1Prefire'                                     : [       287288,       284354,       290227, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       316611,       287285,       263163,       316611,       287285,       263163,       316611,       287285,       263163, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       318667,       261143, ],
  }),
  ("nof_tree_events",                 299322),
  ("nof_db_events",                   299322),
  ("fsize_local",                     1241791493), # 1.24GB, avg file size 1.24GB
  ("fsize_db",                        13394462193), # 13.39GB, avg file size 3.35GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1p5_1_1_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       336636,       270193, ],
    'CountWeightedL1PrefireNom'                                  : [       287484,       287474,       287476, ],
    'CountWeightedL1Prefire'                                     : [       287484,       284487,       290502, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       320955,       287479,       260467,       320955,       287479,       260467,       320955,       287479,       260467, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       322461,       258991, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1311241239), # 1.31GB, avg file size 1.31GB
  ("fsize_db",                        13698968263), # 13.70GB, avg file size 3.42GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_0p5_1_1_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       384326,       238143, ],
    'CountWeightedL1PrefireNom'                                  : [       293734,       293721,       293734, ],
    'CountWeightedL1Prefire'                                     : [       293734,       292156,       295310, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       376219,       355255,       335576,       311092,       293730,       277434,       261533,       246915,       233201, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       376219,       233201, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1195416920), # 1.20GB, avg file size 597.71MB
  ("fsize_db",                        13013254769), # 13.01GB, avg file size 4.34GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_sm_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       353745,       220700, ],
    'CountWeightedL1PrefireNom'                                  : [       271541,       271531,       271544, ],
    'CountWeightedL1Prefire'                                     : [       271541,       270120,       272956, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       346528,       329216,       312611,       285849,       271536,       257819,       239829,       227802,       216274, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       346528,       216274, ],
  }),
  ("nof_tree_events",                 277140),
  ("nof_db_events",                   277140),
  ("fsize_local",                     1078261347), # 1.08GB, avg file size 539.13MB
  ("fsize_db",                        11969129912), # 11.97GB, avg file size 3.99GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_box_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       371670,       231621, ],
    'CountWeightedL1PrefireNom'                                  : [       285180,       285166,       285177, ],
    'CountWeightedL1Prefire'                                     : [       285180,       283704,       286650, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       364148,       345687,       328107,       300484,       285178,       270608,       252197,       239292,       227025, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       364148,       227025, ],
  }),
  ("nof_tree_events",                 291000),
  ("nof_db_events",                   291000),
  ("fsize_local",                     1138857976), # 1.14GB, avg file size 569.43MB
  ("fsize_db",                        12693181737), # 12.69GB, avg file size 4.23GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_2_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       380810,       240060, ],
    'CountWeightedL1PrefireNom'                                  : [       294391,       294389,       294411, ],
    'CountWeightedL1Prefire'                                     : [       294391,       292960,       295821, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       373632,       358272,       342922,       307070,       294375,       281750,       256850,       246220,       235613, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       373632,       235613, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1124759914), # 1.12GB, avg file size 562.38MB
  ("fsize_db",                        12554774019), # 12.55GB, avg file size 4.18GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_9_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       382021,       239399, ],
    'CountWeightedL1PrefireNom'                                  : [       294151,       294135,       294142, ],
    'CountWeightedL1Prefire'                                     : [       294151,       292662,       295636, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       374491,       357201,       340358,       308429,       294144,       280237,       258440,       246437,       234763, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       374491,       234763, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1149084463), # 1.15GB, avg file size 574.54MB
  ("fsize_db",                        12953354252), # 12.95GB, avg file size 3.24GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_10_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       384467,       238093, ],
    'CountWeightedL1PrefireNom'                                  : [       293845,       293836,       293818, ],
    'CountWeightedL1Prefire'                                     : [       293845,       292300,       295390, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       376488,       355512,       335977,       311316,       293841,       277597,       261762,       246980,       233253, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       376488,       233253, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1197029703), # 1.20GB, avg file size 598.51MB
  ("fsize_db",                        13042878478), # 13.04GB, avg file size 4.35GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_11_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       385318,       235837, ],
    'CountWeightedL1PrefireNom'                                  : [       292411,       292449,       292447, ],
    'CountWeightedL1Prefire'                                     : [       292411,       290831,       293991, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       377047,       352321,       329903,       313059,       292405,       273769,       264114,       246663,       230862, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       377047,       230862, ],
  }),
  ("nof_tree_events",                 298800),
  ("nof_db_events",                   298800),
  ("fsize_local",                     1242849789), # 1.24GB, avg file size 621.42MB
  ("fsize_db",                        13370108309), # 13.37GB, avg file size 4.46GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_12_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEEnvelope'                                   : [       388568,       235856, ],
    'CountWeightedL1PrefireNom'                                  : [       293102,       293120,       293116, ],
    'CountWeightedL1Prefire'                                     : [       293102,       291400,       294803, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       379586,       352068,       327493,       316083,       293098,       272623,       267298,       247847,       230486, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       379586,       230486, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1274722076), # 1.27GB, avg file size 637.36MB
  ("fsize_db",                        13600771777), # 13.60GB, avg file size 4.53GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_13_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  [ 'signal_ggf_nonresonant_node_sm_hh_2b2v_sl',       'signal_ggf_nonresonant_node_box_hh_2b2v_sl',      'signal_ggf_nonresonant_node_1_hh_2b2v_sl',        'signal_ggf_nonresonant_node_2_hh_2b2v_sl',        'signal_ggf_nonresonant_node_3_hh_2b2v_sl',        'signal_ggf_nonresonant_node_4_hh_2b2v_sl',        'signal_ggf_nonresonant_node_5_hh_2b2v_sl',        'signal_ggf_nonresonant_node_6_hh_2b2v_sl',        'signal_ggf_nonresonant_node_7_hh_2b2v_sl',        'signal_ggf_nonresonant_node_8_hh_2b2v_sl',        'signal_ggf_nonresonant_node_9_hh_2b2v_sl',        'signal_ggf_nonresonant_node_10_hh_2b2v_sl',       'signal_ggf_nonresonant_node_11_hh_2b2v_sl',       'signal_ggf_nonresonant_node_12_hh_2b2v_sl',        ],
]

