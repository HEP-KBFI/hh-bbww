from collections import OrderedDict as OD

# file generated at 2020-12-26 01:40:05 with the following command:
# create_dictionary.py -m python/samples/metaDict_2016_hh_sync.py -p /hdfs/local/karl/ttHNtupleProduction/2016/2020Dec25_woPresel_nonNom_hh_bbww_sync_hh_multilepton/ntuples -N samples_2016 -E 2016 -o python/samples -g hhAnalyzeSamples_2016_sync.py -M

samples_2016 = OD()
samples_2016["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-750_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal"),
  ("process_name_specific",           "signal_ggf_spin0_750_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 144981, ],
    'CountWeighted'                                                                  : [ 1.44964547e+05, 1.44991250e+05, 1.44983062e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.58550844e+05, 1.44964047e+05, 1.33141203e+05, 1.58550844e+05, 1.44964047e+05, 1.33141203e+05, 1.58550844e+05, 1.44964047e+05, 1.33141203e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.58550844e+05, 1.33141203e+05, ],
    'CountWeightedFull'                                                              : [ 1.44964547e+05, 1.44991250e+05, 1.44983062e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.58550844e+05, 1.44964047e+05, 1.33141203e+05, 1.58550844e+05, 1.44964047e+05, 1.33141203e+05, 1.58550844e+05, 1.44964047e+05, 1.33141203e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.58550844e+05, 1.33141203e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.41520266e+05, 1.41532484e+05, 1.41529125e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.41520266e+05, 1.40676516e+05, 1.42364781e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.54750859e+05, 1.41519188e+05, 1.29993133e+05, 1.54750859e+05, 1.41519188e+05, 1.29993133e+05, 1.54750859e+05, 1.41519188e+05, 1.29993133e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.54750859e+05, 1.29993133e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 1.41520266e+05, 1.41532484e+05, 1.41529125e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 1.41520266e+05, 1.40676516e+05, 1.42364781e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.54750859e+05, 1.41519188e+05, 1.29993133e+05, 1.54750859e+05, 1.41519188e+05, 1.29993133e+05, 1.54750859e+05, 1.41519188e+05, 1.29993133e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.54750859e+05, 1.29993133e+05, ],
  }),
  ("nof_tree_events",                 144981),
  ("nof_db_events",                   298727),
  ("fsize_local",                     850426487), # 850.43MB, avg file size 850.43MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Dec25_woPresel_nonNom_hh_bbww_sync_hh_multilepton/ntuples/signal_ggf_spin0_750_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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

