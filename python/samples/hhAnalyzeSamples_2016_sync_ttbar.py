from collections import OrderedDict as OD

# file generated at 2020-04-24 12:43:46 with the following command:
# create_dictionary.py -m python/samples/metaDict_2016_hh_sync_ttbar.py -p /hdfs/local/snandan/ttHNtupleProduction/2016/2020Apr22_woPresel_nonNom_hh_bbww_sync_ttbar/ntuples -N samples_2016 -E 2016 -o python/samples -g hhAnalyzeSamples_2016_sync_ttbar_test.py -M

samples_2016 = OD()
samples_2016["/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "background"),
  ("process_name_specific",           "TTTo2L2Nu"),
  ("nof_files",                       1),
  ("nof_db_files",                    778),
  ("nof_events",                      {
    'Count'                                                                          : [        47200, ],
    'CountWeighted'                                                                  : [        46755,        46759,        46765, ],
    'CountWeightedLHEWeightScale'                                                    : [        52623,        51779,        51251,        47856,        46755,        45923,        43300,        42099,        41116, ],
    'CountWeightedLHEEnvelope'                                                       : [        56877,        38343, ],
    'CountWeightedPSWeight'                                                          : [        46802,        46711,        66201,        46720,        46747,        29239, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [       472019,       472014,       472019,       472019,       471722,       471716, ],
    'CountWeightedL1PrefireNom'                                                      : [        45874,        45872,        45885, ],
    'CountWeightedL1Prefire'                                                         : [        45874,        45645,        46102, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [        51605,        50787,        50278,        46943,        45873,        45063,        42483,        41312,        40353, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [        55785,        37627, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [        45921,        45823,        64942,        45835,        45876,        28700, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [       463035,       463030,       463035,       463035,       462744,       462739, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [        46796,        46794,        46801, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [        46895,        46891,        46900, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [        46830,        46827,        46834, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [        46951,        46948,        46957, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [        46842,        46840,        46847, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [        47000,        46995,        47007, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [        52671,        51831,        51308,        47885,        46795,        45966,        43316,        42124,        41147, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [        52788,        51951,        51431,        47978,        46893,        46068,        43389,        42203,        41232, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [        52708,        51867,        51343,        47920,        46828,        45998,        43348,        42154,        41176, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [        52852,        52013,        51491,        48037,        46950,        46123,        43444,        42255,        41282, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [        52726,        51886,        51360,        47932,        46841,        46010,        43356,        42163,        41185, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [        52916,        52075,        51552,        48086,        46998,        46171,        43482,        42294,        41321, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [        56910,        38392, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [        57018,        38490, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [        56952,        38418, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [        57090,        38534, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [        56968,        38430, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [        57150,        38578, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [        46842,        46745,        66231,        46753,        46787,        29279, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [        46942,        46841,        66348,        46847,        46887,        29356, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [        46875,        46779,        66279,        46786,        46818,        29298, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [        46998,        46898,        66431,        46904,        46942,        29389, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [        46887,        46792,        66293,        46798,        46830,        29308, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [        47049,        46948,        66492,        46952,        46989,        29425, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [       472254,       472249,       472254,       472254,       471960,       471955, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [       473148,       473142,       473148,       473148,       472858,       472852, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [       472596,       472590,       472596,       472596,       472301,       472296, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [       473734,       473728,       473734,       473734,       473442,       473437, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [       472709,       472703,       472709,       472709,       472415,       472409, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [       474201,       474196,       474201,       474201,       473911,       473905, ],
    'CountWeightedL1PrefireNomTOP16011TopPtRwgtSF'                                   : [        45918,        45913,        45926, ],
    'CountWeightedL1PrefireNomTOP16011TopPtRwgtSFSquared'                            : [        46020,        46013,        46029, ],
    'CountWeightedL1PrefireNomLinearTopPtRwgtSF'                                     : [        45950,        45945,        45959, ],
    'CountWeightedL1PrefireNomLinearTopPtRwgtSFSquared'                              : [        46075,        46068,        46084, ],
    'CountWeightedL1PrefireNomQuadraticTopPtRwgtSF'                                  : [        45964,        45958,        45973, ],
    'CountWeightedL1PrefireNomQuadraticTopPtRwgtSFSquared'                           : [        46125,        46118,        46136, ],
    'CountWeightedL1PrefireTOP16011TopPtRwgtSF'                                      : [        45918,        45691,        46145, ],
    'CountWeightedL1PrefireTOP16011TopPtRwgtSFSquared'                               : [        46020,        45793,        46246, ],
    'CountWeightedL1PrefireLinearTopPtRwgtSF'                                        : [        45950,        45722,        46177, ],
    'CountWeightedL1PrefireLinearTopPtRwgtSFSquared'                                 : [        46075,        45847,        46301, ],
    'CountWeightedL1PrefireQuadraticTopPtRwgtSF'                                     : [        45964,        45736,        46190, ],
    'CountWeightedL1PrefireQuadraticTopPtRwgtSFSquared'                              : [        46125,        45898,        46352, ],
    'CountWeightedLHEWeightScaleL1PrefireNomTOP16011TopPtRwgtSF'                     : [        51659,        50845,        50340,        46979,        45917,        45110,        42503,        41340,        40388, ],
    'CountWeightedLHEWeightScaleL1PrefireNomTOP16011TopPtRwgtSFSquared'              : [        51781,        50969,        50467,        47075,        46018,        45216,        42581,        41424,        40476, ],
    'CountWeightedLHEWeightScaleL1PrefireNomLinearTopPtRwgtSF'                       : [        51695,        50880,        50374,        47012,        45949,        45141,        42534,        41370,        40416, ],
    'CountWeightedLHEWeightScaleL1PrefireNomLinearTopPtRwgtSFSquared'                : [        51843,        51029,        50525,        47132,        46073,        45269,        42634,        41474,        40524, ],
    'CountWeightedLHEWeightScaleL1PrefireNomQuadraticTopPtRwgtSF'                    : [        51715,        50899,        50392,        47026,        45962,        45155,        42544,        41380,        40426, ],
    'CountWeightedLHEWeightScaleL1PrefireNomQuadraticTopPtRwgtSFSquared'             : [        51909,        51094,        50588,        47184,        46124,        45319,        42674,        41515,        40566, ],
    'CountWeightedLHEEnvelopeL1PrefireNomTOP16011TopPtRwgtSF'                        : [        55825,        37680, ],
    'CountWeightedLHEEnvelopeL1PrefireNomTOP16011TopPtRwgtSFSquared'                 : [        55938,        37781, ],
    'CountWeightedLHEEnvelopeL1PrefireNomLinearTopPtRwgtSF'                          : [        55865,        37705, ],
    'CountWeightedLHEEnvelopeL1PrefireNomLinearTopPtRwgtSFSquared'                   : [        56008,        37823, ],
    'CountWeightedLHEEnvelopeL1PrefireNomQuadraticTopPtRwgtSF'                       : [        55883,        37718, ],
    'CountWeightedLHEEnvelopeL1PrefireNomQuadraticTopPtRwgtSFSquared'                : [        56070,        37869, ],
    'CountWeightedPSWeightL1PrefireNomTOP16011TopPtRwgtSF'                           : [        45965,        45863,        64980,        45873,        45921,        28742, ],
    'CountWeightedPSWeightL1PrefireNomTOP16011TopPtRwgtSFSquared'                    : [        46069,        45963,        65104,        45971,        46025,        28822, ],
    'CountWeightedPSWeightL1PrefireNomLinearTopPtRwgtSF'                             : [        45997,        45895,        65027,        45905,        45952,        28761, ],
    'CountWeightedPSWeightL1PrefireNomLinearTopPtRwgtSFSquared'                      : [        46123,        46018,        65184,        46026,        46078,        28853, ],
    'CountWeightedPSWeightL1PrefireNomQuadraticTopPtRwgtSF'                          : [        46011,        45909,        65043,        45918,        45965,        28772, ],
    'CountWeightedPSWeightL1PrefireNomQuadraticTopPtRwgtSFSquared'                   : [        46175,        46069,        65247,        46076,        46128,        28891, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNomTOP16011TopPtRwgtSF'             : [       463335,       463329,       463335,       463335,       463047,       463042, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNomTOP16011TopPtRwgtSFSquared'      : [       464271,       464265,       464271,       464271,       463987,       463982, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNomLinearTopPtRwgtSF'               : [       463668,       463663,       463668,       463668,       463381,       463375, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNomLinearTopPtRwgtSFSquared'        : [       464840,       464834,       464840,       464840,       464555,       464549, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNomQuadraticTopPtRwgtSF'            : [       463795,       463790,       463795,       463795,       463509,       463503, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNomQuadraticTopPtRwgtSFSquared'     : [       465329,       465324,       465329,       465329,       465046,       465040, ],
  }),
  ("nof_tree_events",                 47200),
  ("nof_db_events",                   67926800),
  ("fsize_local",                     216251097), # 216.25MB, avg file size 216.25MB
  ("fsize_db",                        2988515757147), # 2.99TB, avg file size 3.84GB
  ("use_it",                          True),
  ("xsection",                        88.4),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2020Apr22_woPresel_nonNom_hh_bbww_sync_ttbar/ntuples/TTTo2L2Nu"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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

