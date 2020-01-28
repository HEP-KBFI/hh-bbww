from collections import OrderedDict as OD

# file generated at 2020-01-28 22:04:01 with the following command:
# create_dictionary.py -m python/samples/metaDict_2016_hh_sync.py -p /hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nonNom_hh_bbww_sync/ntuples -N samples_2016 -E 2016 -o python/samples -g hhAnalyzeSamples_2016_sync.py -M

samples_2016 = OD()
samples_2016["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-750_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal"),
  ("process_name_specific",           "signal_ggf_spin0_750_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [       144981, ],
    'CountWeighted'                                              : [       144965,       144991,       144983, ],
    'CountWeightedLHEWeightScale'                                : [       158551,       144964,       133141,       158551,       144964,       133141,       158551,       144964,       133141, ],
    'CountWeightedLHEEnvelope'                                   : [       158551,       133141, ],
    'CountWeightedL1PrefireNom'                                  : [       141520,       141532,       141529, ],
    'CountWeightedL1Prefire'                                     : [       141520,       140677,       142365, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       154751,       141519,       129993,       154751,       141519,       129993,       154751,       141519,       129993, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                       : [       154751,       129993, ],
  }),
  ("nof_tree_events",                 144981),
  ("nof_db_events",                   298727),
  ("fsize_local",                     600707214), # 600.71MB, avg file size 600.71MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan28_woPresel_nonNom_hh_bbww_sync/ntuples/signal_ggf_spin0_750_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
]

