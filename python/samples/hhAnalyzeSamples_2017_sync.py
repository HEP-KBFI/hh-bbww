from collections import OrderedDict as OD

# file generated at 2019-05-02 02:39:07 with the following command:
# create_dictionary.py -m python/samples/metaDict_2017_hh_sync.py -p /hdfs/local/karl/ttHNtupleProduction/2017/2019May02_woPresel_nonNom_hh_bbww_sync/ntuples -N samples_2017 -E 2017 -o python/samples -g hhAnalyzeSamples_2017_sync.py -M

samples_2017 = OD()
samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal"),
  ("process_name_specific",           "signal_ggf_spin0_750_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                            : [        52000, ],
    'CountWeighted'                                    : [        51972,        51953,        51984, ],
    'CountWeightedNoPU'                                : [        51992, ],
    'CountFullWeighted'                                : [        51972,        51953,        51984, ],
    'CountFullWeightedNoPU'                            : [        51992, ],
    'CountWeightedLHEWeightScale'                      : [        56911,        59494,        58770,        64740,        56911,        51972,        54215,        53585,        58770,        51972,        47663,        49619,        49071,        53585,        47663,        56911,        59494,        58770,        64740,        56911,        54215,        53585,        58770,        51972,        47663,        49619,        49071,        53585,        47663,        56911,        59494,        58770,        64740,        56911,        51972,        54215,        53585,        58770,        51972,        47663,        49619,        49071,        53585,        47663, ],
    'CountWeightedLHEWeightScaleNoPU'                  : [        56914,        59506,        58782,        64754,        56914,        51992,        54226,        53595,        58782,        51992,        47668,        49629,        49081,        53595,        47668,        56914,        59506,        58782,        64754,        56914,        54226,        53595,        58782,        51992,        47668,        49629,        49081,        53595,        47668,        56914,        59506,        58782,        64754,        56914,        51992,        54226,        53595,        58782,        51992,        47668,        49629,        49081,        53595,        47668, ],
    'CountFullWeightedLHEWeightScale'                  : [        56911,        59494,        58770,        64740,        56911,        51972,        54215,        53585,        58770,        51972,        47663,        49619,        49071,        53585,        47663,        56911,        59494,        58770,        64740,        56911,        54215,        53585,        58770,        51972,        47663,        49619,        49071,        53585,        47663,        56911,        59494,        58770,        64740,        56911,        51972,        54215,        53585,        58770,        51972,        47663,        49619,        49071,        53585,        47663, ],
    'CountFullWeightedLHEWeightScaleNoPU'              : [        56914,        59506,        58782,        64754,        56914,        51992,        54226,        53595,        58782,        51992,        47668,        49629,        49081,        53595,        47668,        56914,        59506,        58782,        64754,        56914,        54226,        53595,        58782,        51992,        47668,        49629,        49081,        53595,        47668,        56914,        59506,        58782,        64754,        56914,        51992,        54226,        53595,        58782,        51992,        47668,        49629,        49081,        53595,        47668, ],
    'CountWeightedL1PrefireNom'                        : [        50011,        49988,        50026, ],
    'CountWeightedL1Prefire'                           : [        50011,        49562,        50455, ],
    'CountWeightedNoPUL1PrefireNom'                    : [        50031, ],
    'CountFullWeightedL1PrefireNom'                    : [        50011,        49988,        50026, ],
    'CountFullWeightedL1Prefire'                       : [        50011,        49562,        50455, ],
    'CountFullWeightedNoPUL1PrefireNom'                : [        50031, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'          : [        54751,        57192,        56509,        62232,        54751,        50011,        52131,        51536,        56509,        50011,        45872,        47723,        47205,        51536,        45872,        54751,        57192,        56509,        62232,        54751,        52131,        51536,        56509,        50011,        45872,        47723,        47205,        51536,        45872,        54751,        57192,        56509,        62232,        54751,        50011,        52131,        51536,        56509,        50011,        45872,        47723,        47205,        51536,        45872, ],
    'CountWeightedLHEWeightScaleNoPUL1PrefireNom'      : [        54759,        57207,        56523,        62248,        54759,        50031,        52145,        51549,        56523,        50031,        45881,        47735,        47217,        51549,        45881,        54759,        57207,        56523,        62248,        54759,        52145,        51549,        56523,        50031,        45881,        47735,        47217,        51549,        45881,        54759,        57207,        56523,        62248,        54759,        50031,        52145,        51549,        56523,        50031,        45881,        47735,        47217,        51549,        45881, ],
    'CountFullWeightedLHEWeightScaleL1PrefireNom'      : [        54751,        57192,        56509,        62232,        54751,        50011,        52131,        51536,        56509,        50011,        45872,        47723,        47205,        51536,        45872,        54751,        57192,        56509,        62232,        54751,        52131,        51536,        56509,        50011,        45872,        47723,        47205,        51536,        45872,        54751,        57192,        56509,        62232,        54751,        50011,        52131,        51536,        56509,        50011,        45872,        47723,        47205,        51536,        45872, ],
    'CountFullWeightedLHEWeightScaleNoPUL1PrefireNom'  : [        54759,        57207,        56523,        62248,        54759,        50031,        52145,        51549,        56523,        50031,        45881,        47735,        47217,        51549,        45881,        54759,        57207,        56523,        62248,        54759,        52145,        51549,        56523,        50031,        45881,        47735,        47217,        51549,        45881,        54759,        57207,        56523,        62248,        54759,        50031,        52145,        51549,        56523,        50031,        45881,        47735,        47217,        51549,        45881, ],
  }),
  ("nof_tree_events",                 52000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     203322842), # 203.32MB, avg file size 203.32MB
  ("fsize_db",                        11931037531), # 11.93GB, avg file size 1.08GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019May02_woPresel_nonNom_hh_bbww_sync/ntuples/signal_ggf_spin0_750_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
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

