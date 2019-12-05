from collections import OrderedDict as OD

# file generated at 2019-08-31 14:21:33 with the following command:
# create_dictionary.py -m python/samples/metaDict_2016_hh.py -p /hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples -N samples_2016 -E 2016 -o python/samples -g hhAnalyzeSamples_2016_hh.py -M

samples_2016 = OD()
samples_2016["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-260_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_260_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_260_hh_2b2v"),
  ("nof_files",                       7),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299998, ],
    'CountWeighted'                                              : [       299991,       300001,       299996, ],
    'CountWeightedLHEWeightScale'                                : [       305748,       299990,       292716,       305748,       299990,       292716,       305748,       299990,       292716, ],
    'CountWeightedL1PrefireNom'                                  : [       295856,       295853,       295867, ],
    'CountWeightedL1Prefire'                                     : [       295856,       294751,       296952, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       301501,       295855,       288705,       301501,       295855,       288705,       301501,       295855,       288705, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1955716624), # 1.96GB, avg file size 279.39MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_260_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       6),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       294629, ],
    'CountWeighted'                                              : [       294618,       294629,       294620, ],
    'CountWeightedLHEWeightScale'                                : [       301144,       294613,       286790,       301144,       294613,       286790,       301144,       294613,       286790, ],
    'CountWeightedL1PrefireNom'                                  : [       290391,       290390,       290400, ],
    'CountWeightedL1Prefire'                                     : [       290391,       289269,       291506, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       296785,       290387,       282698,       296785,       290387,       282698,       296785,       290387,       282698, ],
  }),
  ("nof_tree_events",                 294629),
  ("nof_db_events",                   294629),
  ("fsize_local",                     1937433156), # 1.94GB, avg file size 322.91MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_270_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       7),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       299976,       300011,       299986, ],
    'CountWeightedLHEWeightScale'                                : [       308997,       299974,       290135,       308997,       299974,       290135,       308997,       299974,       290135, ],
    'CountWeightedL1PrefireNom'                                  : [       295355,       295367,       295368, ],
    'CountWeightedL1Prefire'                                     : [       295355,       294140,       296564, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       304188,       295352,       285687,       304188,       295352,       285687,       304188,       295352,       285687, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     2029019431), # 2.03GB, avg file size 289.86MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_300_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       6),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       295149, ],
    'CountWeighted'                                              : [       295171,       295187,       295154, ],
    'CountWeightedLHEWeightScale'                                : [       307331,       295167,       282819,       307331,       295167,       282819,       307331,       295167,       282819, ],
    'CountWeightedL1PrefireNom'                                  : [       290046,       290056,       290037, ],
    'CountWeightedL1Prefire'                                     : [       290046,       288729,       291360, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       301962,       290043,       277950,       301962,       290043,       277950,       301962,       290043,       277950, ],
  }),
  ("nof_tree_events",                 295149),
  ("nof_db_events",                   295149),
  ("fsize_local",                     2079998398), # 2.08GB, avg file size 346.67MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_350_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       7),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299997, ],
    'CountWeighted'                                              : [       299972,       300051,       300035, ],
    'CountWeightedLHEWeightScale'                                : [       315272,       299968,       285216,       315272,       299968,       285216,       315272,       299968,       285216, ],
    'CountWeightedL1PrefireNom'                                  : [       294328,       294367,       294373, ],
    'CountWeightedL1Prefire'                                     : [       294328,       292888,       295765, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       309281,       294324,       279877,       309281,       294324,       279877,       309281,       294324,       279877, ],
  }),
  ("nof_tree_events",                 299997),
  ("nof_db_events",                   299997),
  ("fsize_local",                     2182396173), # 2.18GB, avg file size 311.77MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_400_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       6),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       296256, ],
    'CountWeighted'                                              : [       296262,       296254,       296249, ],
    'CountWeightedLHEWeightScale'                                : [       313766,       296257,       279780,       313766,       296257,       279780,       313766,       296257,       279780, ],
    'CountWeightedL1PrefireNom'                                  : [       290349,       290343,       290343, ],
    'CountWeightedL1Prefire'                                     : [       290349,       288861,       291838, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       307457,       290344,       274237,       307457,       290344,       274237,       307457,       290344,       274237, ],
  }),
  ("nof_tree_events",                 296256),
  ("nof_db_events",                   296256),
  ("fsize_local",                     2218634182), # 2.22GB, avg file size 369.77MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_450_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       7),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       299950,       300002,       299978, ],
    'CountWeightedLHEWeightScale'                                : [       319914,       299949,       281656,       319914,       299949,       281656,       319914,       299949,       281656, ],
    'CountWeightedL1PrefireNom'                                  : [       293745,       293764,       293769, ],
    'CountWeightedL1Prefire'                                     : [       293745,       292185,       295304, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       313220,       293743,       275849,       313220,       293743,       275849,       313220,       293743,       275849, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     2298314860), # 2.30GB, avg file size 328.33MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_500_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       7),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       300007,       300016,       299972, ],
    'CountWeightedLHEWeightScale'                                : [       321840,       300001,       280193,       321840,       300001,       280193,       321840,       300001,       280193, ],
    'CountWeightedL1PrefireNom'                                  : [       293512,       293503,       293506, ],
    'CountWeightedL1Prefire'                                     : [       293512,       291901,       295123, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       314825,       293507,       274168,       314825,       293507,       274168,       314825,       293507,       274168, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     2347744537), # 2.35GB, avg file size 335.39MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_550_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       7),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       299995,       300030,       300013, ],
    'CountWeightedLHEWeightScale'                                : [       323615,       299993,       278857,       323615,       299993,       278857,       323615,       299993,       278857, ],
    'CountWeightedL1PrefireNom'                                  : [       293326,       293344,       293336, ],
    'CountWeightedL1Prefire'                                     : [       293326,       291676,       294976, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       316370,       293323,       272692,       316370,       293323,       272692,       316370,       293323,       272692, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     2381823244), # 2.38GB, avg file size 340.26MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_600_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       6),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       299538, ],
    'CountWeighted'                                              : [       299519,       299532,       299518, ],
    'CountWeightedLHEWeightScale'                                : [       324729,       299516,       277235,       324729,       299516,       277235,       324729,       299516,       277235, ],
    'CountWeightedL1PrefireNom'                                  : [       292682,       292692,       292677, ],
    'CountWeightedL1Prefire'                                     : [       292682,       291000,       294368, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       317254,       292679,       270936,       317254,       292679,       270936,       317254,       292679,       270936, ],
  }),
  ("nof_tree_events",                 299538),
  ("nof_db_events",                   299538),
  ("fsize_local",                     2407750832), # 2.41GB, avg file size 401.29MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_650_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       6),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       298727, ],
    'CountWeighted'                                              : [       298718,       298712,       298710, ],
    'CountWeightedLHEWeightScale'                                : [       326696,       298715,       274384,       326696,       298715,       274384,       326696,       298715,       274384, ],
    'CountWeightedL1PrefireNom'                                  : [       291590,       291576,       291598, ],
    'CountWeightedL1Prefire'                                     : [       291590,       289848,       293333, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       318847,       291587,       267865,       318847,       291587,       267865,       318847,       291587,       267865, ],
  }),
  ("nof_tree_events",                 298727),
  ("nof_db_events",                   298727),
  ("fsize_local",                     2446184519), # 2.45GB, avg file size 407.70MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_750_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       6),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       299705, ],
    'CountWeighted'                                              : [       299692,       299706,       299696, ],
    'CountWeightedLHEWeightScale'                                : [       329030,       299687,       274355,       329030,       299687,       274355,       329030,       299687,       274355, ],
    'CountWeightedL1PrefireNom'                                  : [       292545,       292542,       292557, ],
    'CountWeightedL1Prefire'                                     : [       292545,       290802,       294292, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       321133,       292541,       267838,       321133,       292541,       267838,       321133,       292541,       267838, ],
  }),
  ("nof_tree_events",                 299705),
  ("nof_db_events",                   299705),
  ("fsize_local",                     2470660446), # 2.47GB, avg file size 411.78MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_800_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       6),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       298733, ],
    'CountWeighted'                                              : [       298766,       298748,       298715, ],
    'CountWeightedLHEWeightScale'                                : [       330291,       298763,       271777,       330291,       298763,       271777,       330291,       298763,       271777, ],
    'CountWeightedL1PrefireNom'                                  : [       291493,       291473,       291477, ],
    'CountWeightedL1Prefire'                                     : [       291493,       289730,       293258, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       322221,       291490,       265203,       322221,       291490,       265203,       322221,       291490,       265203, ],
  }),
  ("nof_tree_events",                 298733),
  ("nof_db_events",                   298733),
  ("fsize_local",                     2490428684), # 2.49GB, avg file size 415.07MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_900_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       7),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       300041,       300008,       299994, ],
    'CountWeightedLHEWeightScale'                                : [       333764,       300040,       271434,       333764,       300040,       271434,       333764,       300040,       271434, ],
    'CountWeightedL1PrefireNom'                                  : [       292570,       292540,       292553, ],
    'CountWeightedL1Prefire'                                     : [       292570,       290764,       294375, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       325429,       292567,       264718,       325429,       292567,       264718,       325429,       292567,       264718, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     2525999201), # 2.53GB, avg file size 360.86MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1000_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       6),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       299972,       299983,       299948, ],
    'CountWeightedLHEWeightScale'                                : [       305772,       299972,       292713,       305772,       299972,       292713,       305772,       299972,       292713, ],
    'CountWeightedL1PrefireNom'                                  : [       295666,       295666,       295661, ],
    'CountWeightedL1Prefire'                                     : [       295666,       294521,       296805, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       301340,       295664,       288527,       301340,       295664,       288527,       301340,       295664,       288527, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1982773313), # 1.98GB, avg file size 330.46MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_260_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       7),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       299944,       299967,       300037, ],
    'CountWeightedLHEWeightScale'                                : [       306611,       299941,       292027,       306611,       299941,       292027,       306611,       299941,       292027, ],
    'CountWeightedL1PrefireNom'                                  : [       295557,       295564,       295620, ],
    'CountWeightedL1Prefire'                                     : [       295557,       294393,       296713, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       302072,       295553,       287763,       302072,       295553,       287763,       302072,       295553,       287763, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     2003201812), # 2.00GB, avg file size 286.17MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_270_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       6),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       299981,       300010,       300001, ],
    'CountWeightedLHEWeightScale'                                : [       309003,       299981,       290128,       309003,       299981,       290128,       309003,       299981,       290128, ],
    'CountWeightedL1PrefireNom'                                  : [       295161,       295172,       295183, ],
    'CountWeightedL1Prefire'                                     : [       295161,       293906,       296412, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       303990,       295159,       285494,       303990,       295159,       285494,       303990,       295159,       285494, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     2071934600), # 2.07GB, avg file size 345.32MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_300_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       7),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       300014,       299993,       299980, ],
    'CountWeightedLHEWeightScale'                                : [       312403,       300013,       287447,       312403,       300013,       287447,       312403,       300013,       287447, ],
    'CountWeightedL1PrefireNom'                                  : [       294715,       294699,       294693, ],
    'CountWeightedL1Prefire'                                     : [       294715,       293362,       296065, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       306838,       294713,       282413,       306838,       294713,       282413,       306838,       294713,       282413, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     2161004366), # 2.16GB, avg file size 308.71MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_350_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       7),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       300003,       300007,       300044, ],
    'CountWeightedLHEWeightScale'                                : [       315231,       299996,       285248,       315231,       299996,       285248,       315231,       299996,       285248, ],
    'CountWeightedL1PrefireNom'                                  : [       294509,       294505,       294543, ],
    'CountWeightedL1Prefire'                                     : [       294509,       293121,       295896, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       309405,       294503,       280067,       309405,       294503,       280067,       309405,       294503,       280067, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     2236801945), # 2.24GB, avg file size 319.54MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_400_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       7),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       300001,       300017,       300016, ],
    'CountWeightedLHEWeightScale'                                : [       317715,       300000,       283335,       317715,       300000,       283335,       317715,       300000,       283335, ],
    'CountWeightedL1PrefireNom'                                  : [       294298,       294290,       294327, ],
    'CountWeightedL1Prefire'                                     : [       294298,       292873,       295724, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       311624,       294296,       277991,       311624,       294296,       277991,       311624,       294296,       277991, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     2302654765), # 2.30GB, avg file size 328.95MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_450_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       6),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       300010,       299991,       299995, ],
    'CountWeightedLHEWeightScale'                                : [       319906,       300007,       281662,       319906,       300007,       281662,       319906,       300007,       281662, ],
    'CountWeightedL1PrefireNom'                                  : [       294220,       294198,       294220, ],
    'CountWeightedL1Prefire'                                     : [       294220,       292783,       295657, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       313679,       294217,       276271,       313679,       294217,       276271,       313679,       294217,       276271, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     2360207626), # 2.36GB, avg file size 393.37MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_500_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       7),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       300015,       299988,       299996, ],
    'CountWeightedLHEWeightScale'                                : [       321858,       300008,       280187,       321858,       300008,       280187,       321858,       300008,       280187, ],
    'CountWeightedL1PrefireNom'                                  : [       294116,       294090,       294112, ],
    'CountWeightedL1Prefire'                                     : [       294116,       292661,       295571, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       315481,       294110,       274721,       315481,       294110,       274721,       315481,       294110,       274721, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     2401853713), # 2.40GB, avg file size 343.12MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_550_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       7),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       300015,       300014,       299983, ],
    'CountWeightedLHEWeightScale'                                : [       323622,       300014,       278859,       323622,       300014,       278859,       323622,       300014,       278859, ],
    'CountWeightedL1PrefireNom'                                  : [       294175,       294163,       294162, ],
    'CountWeightedL1Prefire'                                     : [       294175,       292738,       295611, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       317275,       294172,       273471,       317275,       294172,       273471,       317275,       294172,       273471, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     2435396283), # 2.44GB, avg file size 347.91MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_600_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       6),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                      : [       298806, ],
    'CountWeighted'                                              : [       298792,       298795,       298783, ],
    'CountWeightedLHEWeightScale'                                : [       323946,       298776,       276557,       323946,       298776,       276557,       323946,       298776,       276557, ],
    'CountWeightedL1PrefireNom'                                  : [       292949,       292941,       292957, ],
    'CountWeightedL1Prefire'                                     : [       292949,       291516,       294382, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       317559,       292937,       271175,       317559,       292937,       271175,       317559,       292937,       271175, ],
  }),
  ("nof_tree_events",                 298806),
  ("nof_db_events",                   298806),
  ("fsize_local",                     2450826769), # 2.45GB, avg file size 408.47MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_650_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       7),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       299971,       300020,       300031, ],
    'CountWeightedLHEWeightScale'                                : [       326723,       299961,       276554,       326723,       299961,       276554,       326723,       299961,       276554, ],
    'CountWeightedL1PrefireNom'                                  : [       294153,       294184,       294189, ],
    'CountWeightedL1Prefire'                                     : [       294153,       292728,       295577, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       320330,       294145,       271211,       320330,       294145,       271211,       320330,       294145,       271211, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     2481533245), # 2.48GB, avg file size 354.50MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_700_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       7),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       300007,       299988,       300010, ],
    'CountWeightedLHEWeightScale'                                : [       329372,       299998,       274604,       329372,       299998,       274604,       329372,       299998,       274604, ],
    'CountWeightedL1PrefireNom'                                  : [       294246,       294229,       294251, ],
    'CountWeightedL1Prefire'                                     : [       294246,       292841,       295652, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       323016,       294239,       269359,       323016,       294239,       269359,       323016,       294239,       269359, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     2512477001), # 2.51GB, avg file size 358.93MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_800_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       7),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       299989,       300026,       300037, ],
    'CountWeightedLHEWeightScale'                                : [       331696,       299984,       272920,       331696,       299984,       272920,       331696,       299984,       272920, ],
    'CountWeightedL1PrefireNom'                                  : [       294252,       294267,       294286, ],
    'CountWeightedL1Prefire'                                     : [       294252,       292854,       295647, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       325322,       294247,       267714,       325322,       294247,       267714,       325322,       294247,       267714, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     2533290174), # 2.53GB, avg file size 361.90MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_900_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       6),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       299118, ],
    'CountWeighted'                                              : [       299102,       299147,       299124, ],
    'CountWeightedLHEWeightScale'                                : [       332783,       299096,       270651,       332783,       299096,       270651,       332783,       299096,       270651, ],
    'CountWeightedL1PrefireNom'                                  : [       293382,       293390,       293417, ],
    'CountWeightedL1Prefire'                                     : [       293382,       291994,       294768, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       326389,       293376,       265481,       326389,       293376,       265481,       326389,       293376,       265481, ],
  }),
  ("nof_tree_events",                 299118),
  ("nof_db_events",                   299118),
  ("fsize_local",                     2540535687), # 2.54GB, avg file size 423.42MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_1000_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       7),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       299980,       300004,       299967, ],
    'CountWeightedLHEWeightScale'                                : [       326212,       299979,       277737,       326212,       299979,       277737,       326212,       299979,       277737, ],
    'CountWeightedL1PrefireNom'                                  : [       288350,       288359,       288345, ],
    'CountWeightedL1Prefire'                                     : [       288350,       285450,       291257, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       313351,       288347,       267107,       313351,       288347,       267107,       313351,       288347,       267107, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     2323021800), # 2.32GB, avg file size 331.86MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_1_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       7),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       299983,       299972,       300008, ],
    'CountWeightedLHEWeightScale'                                : [       324927,       299981,       278756,       324927,       299981,       278756,       324927,       299981,       278756, ],
    'CountWeightedL1PrefireNom'                                  : [       285194,       285179,       285213, ],
    'CountWeightedL1Prefire'                                     : [       285194,       281635,       288771, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       308640,       285191,       265199,       308640,       285191,       265199,       308640,       285191,       265199, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     2426810764), # 2.43GB, avg file size 346.69MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_2_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       7),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       300008,       300018,       299967, ],
    'CountWeightedLHEWeightScale'                                : [       338115,       300007,       269641,       338115,       300007,       269641,       338115,       300007,       269641, ],
    'CountWeightedL1PrefireNom'                                  : [       287357,       287343,       287357, ],
    'CountWeightedL1Prefire'                                     : [       287357,       284359,       290371, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       323760,       287355,       258355,       323760,       287355,       258355,       323760,       287355,       258355, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     2540797947), # 2.54GB, avg file size 362.97MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_2_1_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       6),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       300028,       300037,       300007, ],
    'CountWeightedLHEWeightScale'                                : [       322426,       300021,       280508,       322426,       300021,       280508,       322426,       300021,       280508, ],
    'CountWeightedL1PrefireNom'                                  : [       289891,       289901,       289873, ],
    'CountWeightedL1Prefire'                                     : [       289891,       287342,       292442, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       311374,       289885,       271176,       311374,       289885,       271176,       311374,       289885,       271176, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     2319455149), # 2.32GB, avg file size 386.58MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_0_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       6),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       299402, ],
    'CountWeighted'                                              : [       299407,       299389,       299372, ],
    'CountWeightedLHEWeightScale'                                : [       329956,       299400,       274212,       329956,       299400,       274212,       329956,       299400,       274212, ],
    'CountWeightedL1PrefireNom'                                  : [       287828,       287814,       287822, ],
    'CountWeightedL1Prefire'                                     : [       287828,       284995,       290670, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       317006,       287823,       263750,       317006,       287823,       263750,       317006,       287823,       263750, ],
  }),
  ("nof_tree_events",                 299402),
  ("nof_db_events",                   299402),
  ("fsize_local",                     2419069726), # 2.42GB, avg file size 403.18MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1p5_1_1_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       6),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       297179, ],
    'CountWeighted'                                              : [       297202,       297168,       297163, ],
    'CountWeightedLHEWeightScale'                                : [       332157,       297196,       269009,       332157,       297196,       269009,       332157,       297196,       269009, ],
    'CountWeightedL1PrefireNom'                                  : [       285152,       285129,       285152, ],
    'CountWeightedL1Prefire'                                     : [       285152,       282270,       288048, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       318568,       285147,       258219,       318568,       285147,       258219,       318568,       285147,       258219, ],
  }),
  ("nof_tree_events",                 297179),
  ("nof_db_events",                   297179),
  ("fsize_local",                     2488213928), # 2.49GB, avg file size 414.70MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_0p5_1_1_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       7),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       299955,       299960,       299961, ],
    'CountWeightedLHEWeightScale'                                : [       384363,       362837,       342658,       317826,       299953,       283290,       267195,       252187,       238122, ],
    'CountWeightedL1PrefireNom'                                  : [       293903,       293899,       293914, ],
    'CountWeightedL1Prefire'                                     : [       293903,       292379,       295426, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       376522,       355501,       335781,       311338,       293900,       277602,       261738,       247082,       233338, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     2279153271), # 2.28GB, avg file size 325.59MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_sm_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       7),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       300048,       299987,       300006, ],
    'CountWeightedLHEWeightScale'                                : [       382919,       363715,       345313,       315872,       300046,       284794,       265024,       251681,       238906, ],
    'CountWeightedL1PrefireNom'                                  : [       294267,       294223,       294253, ],
    'CountWeightedL1Prefire'                                     : [       294267,       292809,       295725, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       375502,       356738,       338741,       309749,       294265,       279369,       259883,       246847,       234352, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     2234011039), # 2.23GB, avg file size 319.14MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_box_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       7),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       300000,       300011,       299987, ],
    'CountWeightedLHEWeightScale'                                : [       385636,       362173,       340637,       319540,       299995,       282077,       269128,       252599,       237450, ],
    'CountWeightedL1PrefireNom'                                  : [       293866,       293862,       293870, ],
    'CountWeightedL1Prefire'                                     : [       293866,       292332,       295398, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       377674,       354786,       333758,       312931,       293862,       276368,       263552,       247427,       232636, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     2306506277), # 2.31GB, avg file size 329.50MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_1_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [         8218, ],
    'CountWeighted'                                              : [         8217,         8217,         8216, ],
    'CountWeightedLHEWeightScale'                                : [        10753,         9812,         9002,         9008,         8216,         7536,         7657,         6982,         6402, ],
    'CountWeightedL1PrefireNom'                                  : [         8033,         8033,         8033, ],
    'CountWeightedL1Prefire'                                     : [         8033,         7988,         8078, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        10511,         9594,         8803,         8805,         8033,         7369,         7484,         6826,         6260, ],
  }),
  ("nof_tree_events",                 8218),
  ("nof_db_events",                   8218),
  ("fsize_local",                     67884023), # 67.88MB, avg file size 67.88MB
  ("fsize_db",                        452565251), # 452.57MB, avg file size 452.57MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_2_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       7),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       299998, ],
    'CountWeighted'                                              : [       299996,       300019,       299972, ],
    'CountWeightedLHEWeightScale'                                : [       385317,       362285,       340996,       319127,       299994,       282326,       268659,       252515,       237611, ],
    'CountWeightedL1PrefireNom'                                  : [       293868,       293872,       293859, ],
    'CountWeightedL1Prefire'                                     : [       293868,       292330,       295401, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       377376,       354891,       334093,       312542,       293865,       276604,       263111,       247351,       232791, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     2300612641), # 2.30GB, avg file size 328.66MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_3_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       7),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       299974,       299984,       299999, ],
    'CountWeightedLHEWeightScale'                                : [       383465,       363423,       344402,       316596,       299973,       284259,       265825,       251857,       238613, ],
    'CountWeightedL1PrefireNom'                                  : [       294105,       294106,       294127, ],
    'CountWeightedL1Prefire'                                     : [       294105,       292624,       295589, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       375885,       356312,       337718,       310331,       294103,       278736,       260560,       246917,       233973, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     2248461752), # 2.25GB, avg file size 321.21MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_4_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       7),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       300006,       299988,       299981, ],
    'CountWeightedLHEWeightScale'                                : [       389054,       360182,       334599,       324157,       300000,       278610,       274285,       253769,       235617, ],
    'CountWeightedL1PrefireNom'                                  : [       293447,       293437,       293426, ],
    'CountWeightedL1Prefire'                                     : [       293447,       291828,       295066, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       380477,       352323,       327363,       317001,       293443,       272575,       268221,       248216,       230506, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     2384936381), # 2.38GB, avg file size 340.71MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_5_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       7),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       299993,       300019,       300000, ],
    'CountWeightedLHEWeightScale'                                : [       382868,       363875,       345731,       315755,       299984,       284965,       264895,       251611,       238948, ],
    'CountWeightedL1PrefireNom'                                  : [       294392,       294398,       294406, ],
    'CountWeightedL1Prefire'                                     : [       294392,       292972,       295809, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       375644,       357093,       339353,       309785,       294385,       279697,       259879,       246904,       234524, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     2227674181), # 2.23GB, avg file size 318.24MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_6_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       7),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299997, ],
    'CountWeighted'                                              : [       300009,       299972,       300023, ],
    'CountWeightedLHEWeightScale'                                : [       379151,       366137,       352539,       310692,       300000,       288828,       259243,       250295,       240960, ],
    'CountWeightedL1PrefireNom'                                  : [       295000,       294971,       295010, ],
    'CountWeightedL1Prefire'                                     : [       295000,       293705,       296288, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       372769,       360034,       346710,       305457,       294993,       284050,       254872,       246117,       236970, ],
  }),
  ("nof_tree_events",                 299997),
  ("nof_db_events",                   299997),
  ("fsize_local",                     2107202677), # 2.11GB, avg file size 301.03MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_7_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       7),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       299968,       299990,       300001, ],
    'CountWeightedLHEWeightScale'                                : [       385552,       362236,       340803,       319408,       299964,       282172,       268971,       252559,       237497, ],
    'CountWeightedL1PrefireNom'                                  : [       293834,       293846,       293848, ],
    'CountWeightedL1Prefire'                                     : [       293834,       292294,       295372, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       377572,       354826,       333898,       312785,       293830,       276445,       263386,       247376,       232669, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     2302029136), # 2.30GB, avg file size 328.86MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_8_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       7),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       299998, ],
    'CountWeighted'                                              : [       299962,       299991,       300005, ],
    'CountWeightedLHEWeightScale'                                : [       387745,       360880,       336742,       322412,       299960,       279873,       272333,       253346,       236307, ],
    'CountWeightedL1PrefireNom'                                  : [       293490,       293494,       293524, ],
    'CountWeightedL1Prefire'                                     : [       293490,       291881,       295095, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       379286,       353084,       329529,       315369,       293487,       273871,       266377,       247861,       231234, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     2361691068), # 2.36GB, avg file size 337.38MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_9_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       7),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299998, ],
    'CountWeighted'                                              : [       300002,       300004,       300022, ],
    'CountWeightedLHEWeightScale'                                : [       379918,       365719,       351257,       311719,       299989,       288075,       260390,       250546,       240550, ],
    'CountWeightedL1PrefireNom'                                  : [       294874,       294870,       294887, ],
    'CountWeightedL1Prefire'                                     : [       294874,       293553,       296189, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       373360,       359481,       345324,       306329,       294865,       283201,       255880,       246259,       236475, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     2127702857), # 2.13GB, avg file size 303.96MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_10_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       6),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       299364, ],
    'CountWeighted'                                              : [       299354,       299404,       299391, ],
    'CountWeightedLHEWeightScale'                                : [       382111,       363097,       344965,       315151,       299351,       284332,       264408,       251088,       238419, ],
    'CountWeightedL1PrefireNom'                                  : [       293808,       293835,       293828, ],
    'CountWeightedL1Prefire'                                     : [       293808,       292397,       295214, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       374951,       356378,       338649,       309233,       293805,       279114,       259433,       246423,       234036, ],
  }),
  ("nof_tree_events",                 299364),
  ("nof_db_events",                   299364),
  ("fsize_local",                     2217657490), # 2.22GB, avg file size 369.61MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_11_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       7),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299997, ],
    'CountWeighted'                                              : [       300005,       300026,       299970, ],
    'CountWeightedLHEWeightScale'                                : [       380861,       365032,       349245,       313043,       300003,       286992,       261866,       250925,       240026, ],
    'CountWeightedL1PrefireNom'                                  : [       294649,       294639,       294652, ],
    'CountWeightedL1Prefire'                                     : [       294649,       293279,       296017, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       374005,       358526,       343071,       307403,       294647,       281915,       257145,       246446,       235776, ],
  }),
  ("nof_tree_events",                 299997),
  ("nof_db_events",                   299997),
  ("fsize_local",                     2164033420), # 2.16GB, avg file size 309.15MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_12_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeighted'                                              : [        50000,        49998,        50001, ],
    'CountWeightedLHEWeightScale'                                : [        50807,        50000,        48908,        50807,        50000,        48908,        50807,        50000,        48908, ],
    'CountWeightedL1PrefireNom'                                  : [        49295,        49289,        49300, ],
    'CountWeightedL1Prefire'                                     : [        49295,        49105,        49482, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        50084,        49295,        48223,        50084,        49295,        48223,        50084,        49295,        48223, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     333337377), # 333.34MB, avg file size 333.34MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeighted'                                              : [        49999,        49996,        49998, ],
    'CountWeightedLHEWeightScale'                                : [        50955,        49999,        48787,        50955,        49999,        48787,        50955,        49999,        48787, ],
    'CountWeightedL1PrefireNom'                                  : [        49279,        49276,        49282, ],
    'CountWeightedL1Prefire'                                     : [        49279,        49087,        49470, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        50216,        49279,        48091,        50216,        49279,        48091,        50216,        49279,        48091, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     336722297), # 336.72MB, avg file size 336.72MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_260_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeighted'                                              : [        49996,        50002,        50000, ],
    'CountWeightedLHEWeightScale'                                : [        51103,        49996,        48669,        51103,        49996,        48669,        51103,        49996,        48669, ],
    'CountWeightedL1PrefireNom'                                  : [        49240,        49246,        49241, ],
    'CountWeightedL1Prefire'                                     : [        49240,        49039,        49440, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        50322,        49240,        47938,        50322,        49240,        47938,        50322,        49240,        47938, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     340152119), # 340.15MB, avg file size 340.15MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_270_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeighted'                                              : [        49606,        49597,        49596, ],
    'CountWeightedLHEWeightScale'                                : [        50828,        49606,        48175,        50828,        49606,        48175,        50828,        49606,        48175, ],
    'CountWeightedL1PrefireNom'                                  : [        48846,        48835,        48845, ],
    'CountWeightedL1Prefire'                                     : [        48846,        48645,        49045, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        50045,        48846,        47444,        50045,        48846,        47444,        50045,        48846,        47444, ],
  }),
  ("nof_tree_events",                 49600),
  ("nof_db_events",                   49600),
  ("fsize_local",                     340979452), # 340.98MB, avg file size 340.98MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_280_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       9),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                      : [       450000, ],
    'CountWeighted'                                              : [       449941,       449983,       449953, ],
    'CountWeightedLHEWeightScale'                                : [       463473,       449941,       435219,       463473,       449941,       435219,       463473,       449941,       435219, ],
    'CountWeightedL1PrefireNom'                                  : [       442649,       442658,       442678, ],
    'CountWeightedL1Prefire'                                     : [       442649,       440730,       444557, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       455873,       442649,       428194,       455873,       442649,       428194,       455873,       442649,       428194, ],
  }),
  ("nof_tree_events",                 450000),
  ("nof_db_events",                   450000),
  ("fsize_local",                     3151760551), # 3.15GB, avg file size 350.20MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_300_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeighted'                                              : [        49996,        50002,        50001, ],
    'CountWeightedLHEWeightScale'                                : [        51731,        49996,        48171,        51731,        49996,        48171,        51731,        49996,        48171, ],
    'CountWeightedL1PrefireNom'                                  : [        49146,        49150,        49147, ],
    'CountWeightedL1Prefire'                                     : [        49146,        48924,        49367, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        50842,        49146,        47357,        50842,        49146,        47357,        50842,        49146,        47357, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     355641984), # 355.64MB, avg file size 355.64MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_320_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeighted'                                              : [        47997,        48000,        48000, ],
    'CountWeightedLHEWeightScale'                                : [        49881,        47997,        46073,        49881,        47997,        46073,        49881,        47997,        46073, ],
    'CountWeightedL1PrefireNom'                                  : [        47132,        47135,        47132, ],
    'CountWeightedL1Prefire'                                     : [        47132,        46908,        47356, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        48973,        47132,        45247,        48973,        47132,        45247,        48973,        47132,        45247, ],
  }),
  ("nof_tree_events",                 48000),
  ("nof_db_events",                   48000),
  ("fsize_local",                     346931845), # 346.93MB, avg file size 346.93MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_340_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeighted'                                              : [        49989,        50003,        49997, ],
    'CountWeightedLHEWeightScale'                                : [        52062,        49989,        47913,        52062,        49989,        47913,        52062,        49989,        47913, ],
    'CountWeightedL1PrefireNom'                                  : [        49091,        49097,        49098, ],
    'CountWeightedL1Prefire'                                     : [        49091,        48858,        49323, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        51114,        49091,        47054,        51114,        49091,        47054,        51114,        49091,        47054, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     364447810), # 364.45MB, avg file size 364.45MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_350_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       5),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       250000, ],
    'CountWeighted'                                              : [       249990,       250001,       249981, ],
    'CountWeightedLHEWeightScale'                                : [       262685,       249990,       237714,       262685,       249990,       237714,       262685,       249990,       237714, ],
    'CountWeightedL1PrefireNom'                                  : [       245065,       245059,       245068, ],
    'CountWeightedL1Prefire'                                     : [       245065,       243810,       246316, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       257459,       245065,       233060,       257459,       245065,       233060,       257459,       245065,       233060, ],
  }),
  ("nof_tree_events",                 250000),
  ("nof_db_events",                   250000),
  ("fsize_local",                     1881255265), # 1.88GB, avg file size 376.25MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_400_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        99600, ],
    'CountWeighted'                                              : [        99613,        99601,        99594, ],
    'CountWeightedLHEWeightScale'                                : [       105479,        99613,        94068,       105479,        99613,        94068,       105479,        99613,        94068, ],
    'CountWeightedL1PrefireNom'                                  : [        97513,        97513,        97497, ],
    'CountWeightedL1Prefire'                                     : [        97513,        96987,        98039, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       103243,        97513,        92104,       103243,        97513,        92104,       103243,        97513,        92104, ],
  }),
  ("nof_tree_events",                 99600),
  ("nof_db_events",                   99600),
  ("fsize_local",                     771650296), # 771.65MB, avg file size 385.83MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_450_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        99200, ],
    'CountWeighted'                                              : [        99201,        99203,        99205, ],
    'CountWeightedLHEWeightScale'                                : [       105782,        99201,        93135,       105782,        99201,        93135,       105782,        99201,        93135, ],
    'CountWeightedL1PrefireNom'                                  : [        97025,        97024,        97031, ],
    'CountWeightedL1Prefire'                                     : [        97025,        96481,        97568, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       103443,        97025,        91108,       103443,        97025,        91108,       103443,        97025,        91108, ],
  }),
  ("nof_tree_events",                 99200),
  ("nof_db_events",                   99200),
  ("fsize_local",                     787809288), # 787.81MB, avg file size 393.90MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99995,        99994,        99995, ],
    'CountWeightedLHEWeightScale'                                : [       107273,        99995,        93404,       107273,        99995,        93404,       107273,        99995,        93404, ],
    'CountWeightedL1PrefireNom'                                  : [        97754,        97750,        97756, ],
    'CountWeightedL1Prefire'                                     : [        97754,        97195,        98313, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       104847,        97754,        91322,       104847,        97754,        91322,       104847,        97754,        91322, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     811103090), # 811.10MB, avg file size 405.55MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_550_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [       100001,        99983,       100003, ],
    'CountWeightedLHEWeightScale'                                : [       107872,       100001,        92955,       107872,       100001,        92955,       107872,       100001,        92955, ],
    'CountWeightedL1PrefireNom'                                  : [        97649,        97638,        97648, ],
    'CountWeightedL1Prefire'                                     : [        97649,        97068,        98231, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       105315,        97649,        90783,       105315,        97649,        90783,       105315,        97649,        90783, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     825943009), # 825.94MB, avg file size 412.97MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_600_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99997,        99997,        99979, ],
    'CountWeightedLHEWeightScale'                                : [       108410,        99997,        92556,       108410,        99997,        92556,       108410,        99997,        92556, ],
    'CountWeightedL1PrefireNom'                                  : [        97626,        97622,        97619, ],
    'CountWeightedL1Prefire'                                     : [        97626,        97040,        98212, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       105818,        97626,        90373,       105818,        97626,        90373,       105818,        97626,        90373, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     837779992), # 837.78MB, avg file size 418.89MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_650_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [       100006,       100009,        99996, ],
    'CountWeightedLHEWeightScale'                                : [       109789,       100006,        91539,       109789,       100006,        91539,       109789,       100006,        91539, ],
    'CountWeightedL1PrefireNom'                                  : [        97496,        97493,        97493, ],
    'CountWeightedL1Prefire'                                     : [        97496,        96885,        98107, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       107018,        97496,        89256,       107018,        97496,        89256,       107018,        97496,        89256, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     865546272), # 865.55MB, avg file size 432.77MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_800_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99997,        99997,        99997, ],
    'CountWeightedLHEWeightScale'                                : [       110550,        99997,        90983,       110550,        99997,        90983,       110550,        99997,        90983, ],
    'CountWeightedL1PrefireNom'                                  : [        97458,        97453,        97462, ],
    'CountWeightedL1Prefire'                                     : [        97458,        96841,        98076, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       107727,        97458,        88682,       107727,        97458,        88682,       107727,        97458,        88682, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     879957725), # 879.96MB, avg file size 439.98MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_900_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeighted'                                              : [        50000,        49993,        50005, ],
    'CountWeightedLHEWeightScale'                                : [        50810,        50000,        48905,        50810,        50000,        48905,        50810,        50000,        48905, ],
    'CountWeightedL1PrefireNom'                                  : [        49278,        49273,        49282, ],
    'CountWeightedL1Prefire'                                     : [        49278,        49086,        49469, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        50071,        49278,        48204,        50071,        49278,        48204,        50071,        49278,        48204, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     337136044), # 337.14MB, avg file size 337.14MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeighted'                                              : [        49995,        49995,        50002, ],
    'CountWeightedLHEWeightScale'                                : [        50954,        49995,        48790,        50954,        49995,        48790,        50954,        49995,        48790, ],
    'CountWeightedL1PrefireNom'                                  : [        49245,        49245,        49249, ],
    'CountWeightedL1Prefire'                                     : [        49245,        49046,        49443, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        50181,        49245,        48062,        50181,        49245,        48062,        50181,        49245,        48062, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     340555565), # 340.56MB, avg file size 340.56MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_260_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeighted'                                              : [        49997,        50005,        49997, ],
    'CountWeightedLHEWeightScale'                                : [        51100,        49997,        48672,        51100,        49997,        48672,        51100,        49997,        48672, ],
    'CountWeightedL1PrefireNom'                                  : [        49210,        49215,        49211, ],
    'CountWeightedL1Prefire'                                     : [        49210,        49002,        49417, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        50288,        49210,        47910,        50288,        49210,        47910,        50288,        49210,        47910, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     345405745), # 345.41MB, avg file size 345.41MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_270_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeighted'                                              : [        49996,        49988,        50001, ],
    'CountWeightedLHEWeightScale'                                : [        51238,        49996,        48559,        51238,        49996,        48559,        51238,        49996,        48559, ],
    'CountWeightedL1PrefireNom'                                  : [        49188,        49184,        49192, ],
    'CountWeightedL1Prefire'                                     : [        49188,        48977,        49399, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        50403,        49188,        47780,        50403,        49188,        47780,        50403,        49188,        47780, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     348755692), # 348.76MB, avg file size 348.76MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_280_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       9),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       447400, ],
    'CountWeighted'                                              : [       447416,       447398,       447400, ],
    'CountWeightedLHEWeightScale'                                : [       460787,       447416,       432711,       460787,       447416,       432711,       460787,       447416,       432711, ],
    'CountWeightedL1PrefireNom'                                  : [       439939,       439919,       439936, ],
    'CountWeightedL1Prefire'                                     : [       439939,       437994,       441875, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       453019,       439939,       425539,       453019,       439939,       425539,       453019,       439939,       425539, ],
  }),
  ("nof_tree_events",                 447400),
  ("nof_db_events",                   447400),
  ("fsize_local",                     3185615233), # 3.19GB, avg file size 353.96MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_300_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeighted'                                              : [        49992,        49997,        49992, ],
    'CountWeightedLHEWeightScale'                                : [        51729,        49992,        48169,        51729,        49992,        48169,        51729,        49992,        48169, ],
    'CountWeightedL1PrefireNom'                                  : [        49131,        49131,        49135, ],
    'CountWeightedL1Prefire'                                     : [        49131,        48908,        49354, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        50828,        49131,        47344,        50828,        49131,        47344,        50828,        49131,        47344, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     362758930), # 362.76MB, avg file size 362.76MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_320_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeighted'                                              : [        49996,        49998,        49994, ],
    'CountWeightedLHEWeightScale'                                : [        51958,        49996,        47993,        51958,        49996,        47993,        51958,        49996,        47993, ],
    'CountWeightedL1PrefireNom'                                  : [        49106,        49105,        49107, ],
    'CountWeightedL1Prefire'                                     : [        49106,        48878,        49334, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        51023,        49106,        47144,        51023,        49106,        47144,        51023,        49106,        47144, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     368331410), # 368.33MB, avg file size 368.33MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_340_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeighted'                                              : [        50002,        50001,        49996, ],
    'CountWeightedLHEWeightScale'                                : [        52061,        50002,        47912,        52061,        50002,        47912,        52061,        50002,        47912, ],
    'CountWeightedL1PrefireNom'                                  : [        49102,        49100,        49102, ],
    'CountWeightedL1Prefire'                                     : [        49102,        48872,        49332, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        51116,        49102,        47058,        51116,        49102,        47058,        51116,        49102,        47058, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     371788359), # 371.79MB, avg file size 371.79MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_350_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       5),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       250000, ],
    'CountWeighted'                                              : [       250003,       250032,       249995, ],
    'CountWeightedLHEWeightScale'                                : [       262692,       250003,       237711,       262692,       250003,       237711,       262692,       250003,       237711, ],
    'CountWeightedL1PrefireNom'                                  : [       245187,       245200,       245185, ],
    'CountWeightedL1Prefire'                                     : [       245187,       243972,       246401, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       257580,       245187,       233171,       257580,       245187,       233171,       257580,       245187,       233171, ],
  }),
  ("nof_tree_events",                 250000),
  ("nof_db_events",                   250000),
  ("fsize_local",                     1923569760), # 1.92GB, avg file size 384.71MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_400_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [       100005,       100005,        99995, ],
    'CountWeightedLHEWeightScale'                                : [       105907,       100005,        94447,       105907,       100005,        94447,       105907,       100005,        94447, ],
    'CountWeightedL1PrefireNom'                                  : [        98031,        98027,        98029, ],
    'CountWeightedL1Prefire'                                     : [        98031,        97537,        98525, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       103796,        98031,        92599,       103796,        98031,        92599,       103796,        98031,        92599, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     792544723), # 792.54MB, avg file size 396.27MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_450_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       2),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99990,        99993,        99997, ],
    'CountWeightedLHEWeightScale'                                : [       106626,        99990,        93894,       106626,        99990,        93894,       106626,        99990,        93894, ],
    'CountWeightedL1PrefireNom'                                  : [        97986,        97980,        97995, ],
    'CountWeightedL1Prefire'                                     : [        97986,        97487,        98484, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       104463,        97986,        92023,       104463,        97986,        92023,       104463,        97986,        92023, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     814427755), # 814.43MB, avg file size 407.21MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99998,        99999,       100011, ],
    'CountWeightedLHEWeightScale'                                : [       107288,        99998,        93394,       107288,        99998,        93394,       107288,        99998,        93394, ],
    'CountWeightedL1PrefireNom'                                  : [        97954,        97953,        97964, ],
    'CountWeightedL1Prefire'                                     : [        97954,        97450,        98458, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       105074,        97954,        91499,       105074,        97954,        91499,       105074,        97954,        91499, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     831489218), # 831.49MB, avg file size 415.74MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_550_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [       100003,       100002,        99994, ],
    'CountWeightedLHEWeightScale'                                : [       107869,       100003,        92955,       107869,       100003,        92955,       107869,       100003,        92955, ],
    'CountWeightedL1PrefireNom'                                  : [        97963,        97958,        97964, ],
    'CountWeightedL1Prefire'                                     : [        97963,        97464,        98463, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       105650,        97963,        91075,       105650,        97963,        91075,       105650,        97963,        91075, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     843886577), # 843.89MB, avg file size 421.94MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_600_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99998,       100015,       100007, ],
    'CountWeightedLHEWeightScale'                                : [       108413,        99998,        92553,       108413,        99998,        92553,       108413,        99998,        92553, ],
    'CountWeightedL1PrefireNom'                                  : [        97974,        97983,        97981, ],
    'CountWeightedL1Prefire'                                     : [        97974,        97477,        98470, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       106200,        97974,        90691,       106200,        97974,        90691,       106200,        97974,        90691, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     856488649), # 856.49MB, avg file size 428.24MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_650_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99998,       100005,       100003, ],
    'CountWeightedLHEWeightScale'                                : [       109359,        99998,        91852,       109359,        99998,        91852,       109359,        99998,        91852, ],
    'CountWeightedL1PrefireNom'                                  : [        98024,        98027,        98028, ],
    'CountWeightedL1Prefire'                                     : [        98024,        97541,        98506, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       107184,        98024,        90049,       107184,        98024,        90049,       107184,        98024,        90049, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     873575001), # 873.58MB, avg file size 436.79MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       2),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99989,       100004,        99979, ],
    'CountWeightedLHEWeightScale'                                : [       109785,        99989,        91541,       109785,        99989,        91541,       109785,        99989,        91541, ],
    'CountWeightedL1PrefireNom'                                  : [        98021,        98026,        98020, ],
    'CountWeightedL1Prefire'                                     : [        98021,        97539,        98502, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       107606,        98021,        89744,       107606,        98021,        89744,       107606,        98021,        89744, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     881320034), # 881.32MB, avg file size 440.66MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_800_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       6),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       296060, ],
    'CountWeighted'                                              : [       296057,       296058,       296082, ],
    'CountWeightedLHEWeightScale'                                : [       318162,       296055,       276838,       318162,       296055,       276838,       318162,       296055,       276838, ],
    'CountWeightedL1PrefireNom'                                  : [       285786,       285776,       285802, ],
    'CountWeightedL1Prefire'                                     : [       285786,       283196,       288380, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       306933,       285783,       267372,       306933,       285783,       267372,       306933,       285783,       267372, ],
  }),
  ("nof_tree_events",                 296060),
  ("nof_db_events",                   296060),
  ("fsize_local",                     2344444544), # 2.34GB, avg file size 390.74MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_0_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       7),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       300014,       299981,       299948, ],
    'CountWeightedLHEWeightScale'                                : [       326180,       300012,       277763,       326180,       300012,       277763,       326180,       300012,       277763, ],
    'CountWeightedL1PrefireNom'                                  : [       287826,       287812,       287806, ],
    'CountWeightedL1Prefire'                                     : [       287826,       284793,       290866, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       312728,       287822,       266643,       312728,       287822,       266643,       312728,       287822,       266643, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     2383786632), # 2.38GB, avg file size 340.54MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_1_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       6),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       257175, ],
    'CountWeighted'                                              : [       257178,       257191,       257165, ],
    'CountWeightedLHEWeightScale'                                : [       278653,       257175,       238891,       278653,       257175,       238891,       278653,       257175,       238891, ],
    'CountWeightedL1PrefireNom'                                  : [       244163,       244169,       244148, ],
    'CountWeightedL1Prefire'                                     : [       244163,       241028,       247314, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       264318,       244160,       226977,       264318,       244160,       226977,       264318,       244160,       226977, ],
  }),
  ("nof_tree_events",                 257175),
  ("nof_db_events",                   257175),
  ("fsize_local",                     2133602952), # 2.13GB, avg file size 355.60MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_2_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       7),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       299983,       300013,       299988, ],
    'CountWeightedLHEWeightScale'                                : [       338031,       299979,       269699,       338031,       299979,       269699,       338031,       299979,       269699, ],
    'CountWeightedL1PrefireNom'                                  : [       287103,       287111,       287110, ],
    'CountWeightedL1Prefire'                                     : [       287103,       284044,       290176, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       323403,       287099,       258190,       323403,       287099,       258190,       323403,       287099,       258190, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     2636540334), # 2.64GB, avg file size 376.65MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_2_1_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       6),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       299322, ],
    'CountWeighted'                                              : [       299362,       299301,       299321, ],
    'CountWeightedLHEWeightScale'                                : [       330037,       299361,       274012,       330037,       299361,       274012,       330037,       299361,       274012, ],
    'CountWeightedL1PrefireNom'                                  : [       287332,       287309,       287319, ],
    'CountWeightedL1Prefire'                                     : [       287332,       284400,       290275, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       316609,       287330,       263163,       316609,       287330,       263163,       316609,       287330,       263163, ],
  }),
  ("nof_tree_events",                 299322),
  ("nof_db_events",                   299322),
  ("fsize_local",                     2495422246), # 2.50GB, avg file size 415.90MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1p5_1_1_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       7),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       300004,       299957,       299985, ],
    'CountWeightedLHEWeightScale'                                : [       335097,       299995,       271703,       335097,       299995,       271703,       335097,       299995,       271703, ],
    'CountWeightedL1PrefireNom'                                  : [       287472,       287449,       287471, ],
    'CountWeightedL1Prefire'                                     : [       287472,       284475,       290488, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       320954,       287467,       260469,       320954,       287467,       260469,       320954,       287467,       260469, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     2601918609), # 2.60GB, avg file size 371.70MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2019Aug30_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_0p5_1_1_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  [ 'signal_ggf_nonresonant_node_sm_hh_2b2v',          'signal_ggf_nonresonant_node_box_hh_2b2v',         'signal_ggf_nonresonant_node_1_hh_2b2v',           'signal_ggf_nonresonant_node_2_hh_2b2v',           'signal_ggf_nonresonant_node_3_hh_2b2v',           'signal_ggf_nonresonant_node_4_hh_2b2v',           'signal_ggf_nonresonant_node_5_hh_2b2v',           'signal_ggf_nonresonant_node_6_hh_2b2v',           'signal_ggf_nonresonant_node_7_hh_2b2v',           'signal_ggf_nonresonant_node_8_hh_2b2v',           'signal_ggf_nonresonant_node_9_hh_2b2v',           'signal_ggf_nonresonant_node_10_hh_2b2v',          'signal_ggf_nonresonant_node_11_hh_2b2v',          'signal_ggf_nonresonant_node_12_hh_2b2v',           ],
]

