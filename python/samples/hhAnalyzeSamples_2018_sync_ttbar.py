from collections import OrderedDict as OD

# file generated at 2020-05-24 15:05:27 with the following command:
# create_dictionary.py -m python/samples/metaDict_2018_hh_sync_ttbar.py -p /hdfs/local/karl/ttHNtupleProduction/2018/2020May24_woPresel_nonNom_hh_bbww_sync_ttbar/ntuples -N samples_2018 -E 2018 -o python/samples -g hhAnalyzeSamples_2018_sync_ttbar.py -M

samples_2018 = OD()
samples_2018["/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "background"),
  ("process_name_specific",           "TTTo2L2Nu"),
  ("nof_files",                       1),
  ("nof_db_files",                    968),
  ("nof_events",                      {
    'Count'                                                                          : [        50000, ],
    'CountWeighted'                                                                  : [        49625,        49617,        49617, ],
    'CountWeightedLHEWeightScale'                                                    : [        55992,        55004,        54351,        50850,        49621,        48669,        45972,        44649,        43555, ],
    'CountWeightedLHEEnvelope'                                                       : [        60470,        40640, ],
    'CountWeightedPSWeight'                                                          : [        49621,        49433,        70261,        49630,        49821,        31088, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [       499936,       499929,       499936,       499936,       499683,       499677, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [        49653,        49652,        49655, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [        49751,        49750,        49751, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [        49689,        49688,        49691, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [        49812,        49812,        49813, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [        49705,        49704,        49707, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [        49869,        49868,        49870, ],
    'CountWeightedHighPtTopPtRwgtSF'                                                 : [        49701,        49699,        49703, ],
    'CountWeightedHighPtTopPtRwgtSFSquared'                                          : [        49835,        49834,        49836, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [        56029,        55051,        54406,        50869,        49651,        48709,        45978,        44667,        43584, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [        56142,        55171,        54534,        50958,        49749,        48815,        46047,        44746,        43671, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [        56070,        55090,        54444,        50907,        49688,        48744,        46013,        44700,        43615, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [        56212,        55238,        54599,        51023,        49811,        48874,        46107,        44803,        43725, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [        56092,        55111,        54466,        50922,        49703,        48761,        46023,        44712,        43628, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [        56283,        55309,        54669,        51079,        49867,        48932,        46151,        44849,        43772, ],
    'CountWeightedLHEWeightScaleHighPtTopPtRwgtSF'                                   : [        56086,        55104,        54456,        50921,        49699,        48754,        46025,        44710,        43624, ],
    'CountWeightedLHEWeightScaleHighPtTopPtRwgtSFSquared'                            : [        56243,        55265,        54622,        51049,        49833,        48893,        46129,        44821,        43741, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [        60490,        40689, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [        60592,        40791, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [        60536,        40716, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [        60671,        40838, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [        60555,        40732, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [        60739,        40889, ],
    'CountWeightedLHEEnvelopeHighPtTopPtRwgtSF'                                      : [        60553,        40723, ],
    'CountWeightedLHEEnvelopeHighPtTopPtRwgtSFSquared'                               : [        60704,        40852, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [        49653,        49463,        70280,        49659,        49850,        31127, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [        49752,        49559,        70393,        49755,        49947,        31206, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [        49689,        49499,        70332,        49695,        49887,        31148, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [        49813,        49621,        70485,        49817,        50010,        31241, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [        49705,        49514,        70351,        49712,        49903,        31160, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [        49869,        49676,        70557,        49875,        50067,        31282, ],
    'CountWeightedPSWeightHighPtTopPtRwgtSF'                                         : [        49699,        49510,        70352,        49708,        49900,        31153, ],
    'CountWeightedPSWeightHighPtTopPtRwgtSFSquared'                                  : [        49834,        49642,        70521,        49842,        50035,        31253, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [       500128,       500122,       500128,       500128,       499881,       499874, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [       501032,       501025,       501032,       501032,       500788,       500781, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [       500501,       500495,       500501,       500501,       500252,       500246, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [       501669,       501663,       501669,       501669,       501424,       501418, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [       500656,       500650,       500656,       500656,       500408,       500402, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [       502231,       502224,       502231,       502231,       501986,       501980, ],
    'CountWeightedPSWeightOriginalXWGTUPHighPtTopPtRwgtSF'                           : [       500631,       500625,       500631,       500631,       500382,       500376, ],
    'CountWeightedPSWeightOriginalXWGTUPHighPtTopPtRwgtSFSquared'                    : [       501916,       501910,       501916,       501916,       501670,       501664, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   64310000),
  ("fsize_local",                     228260608), # 228.26MB, avg file size 228.26MB
  ("fsize_db",                        3413760837047), # 3.41TB, avg file size 3.53GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May24_woPresel_nonNom_hh_bbww_sync_ttbar/ntuples/TTTo2L2Nu"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["sum_events"] = [
]

