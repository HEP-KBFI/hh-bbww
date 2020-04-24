from collections import OrderedDict as OD

# file generated at 2020-04-24 12:45:56 with the following command:
# create_dictionary.py -m python/samples/metaDict_2017_hh_sync_ttbar.py -p /hdfs/local/snandan/ttHNtupleProduction/2017/2020Apr22_woPresel_nonNom_hh_bbww_sync_ttbar/ntuples -N samples_2017 -E 2017 -o python/samples -g hhAnalyzeSamples_2017_sync_ttbar_test.py -M

samples_2017 = OD()
samples_2017["/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "background"),
  ("process_name_specific",           "TTTo2L2Nu_PSweights"),
  ("nof_files",                       1),
  ("nof_db_files",                    1056),
  ("nof_events",                      {
    'Count'                                                                          : [        47260, ],
    'CountWeighted'                                                                  : [        46895,        46903,        46893, ],
    'CountWeightedLHEWeightScale'                                                    : [        52897,        51919,        51278,        48096,        46895,        45975,        43511,        42230,        41179, ],
    'CountWeightedLHEEnvelope'                                                       : [        57140,        38401, ],
    'CountWeightedPSWeight'                                                          : [        46940,        46923,        66370,        46837,        46836,        29310, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [       472580,       472575,       472580,       472580,       472328,       472324, ],
    'CountWeightedL1PrefireNom'                                                      : [        45516,        45520,        45515, ],
    'CountWeightedL1Prefire'                                                         : [        45516,        45178,        45846, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [        51308,        50372,        49762,        46668,        45515,        44633,        42231,        40998,        39987, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [        55435,        37282, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [        45569,        45534,        64407,        45446,        45478,        28461, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [       458543,       458539,       458543,       458543,       458305,       458300, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [        46930,        46935,        46923, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [        47024,        47031,        47014, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [        46963,        46968,        46956, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [        47080,        47087,        47070, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [        46973,        46978,        46965, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [        47123,        47131,        47114, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [        52941,        51967,        51331,        48121,        46928,        46014,        43523,        42251,        41207, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [        53054,        52083,        51450,        48210,        47023,        46112,        43592,        42327,        41288, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [        52978,        52002,        51366,        48155,        46961,        46045,        43555,        42281,        41235, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [        53116,        52143,        51510,        48268,        47078,        46166,        43647,        42378,        41338, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [        52993,        52018,        51381,        48165,        46971,        46056,        43560,        42287,        41243, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [        53174,        52200,        51566,        48311,        47122,        46210,        43680,        42413,        41373, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [        57164,        38450, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [        57264,        38548, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [        57205,        38475, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [        57335,        38591, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [        57217,        38485, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [        57387,        38631, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [        46973,        46959,        66404,        46868,        46872,        29345, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [        47068,        47056,        66525,        46961,        46970,        29419, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [        47006,        46991,        66451,        46901,        46905,        29365, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [        47124,        47111,        66605,        47017,        47025,        29452, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [        47016,        47001,        66462,        46911,        46915,        29373, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [        47168,        47155,        66660,        47061,        47068,        29484, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [       472811,       472806,       472811,       472811,       472561,       472556, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [       473677,       473673,       473677,       473677,       473427,       473423, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [       473147,       473142,       473147,       473147,       472896,       472892, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [       474258,       474253,       474258,       474258,       474008,       474003, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [       473239,       473234,       473239,       473239,       472988,       472984, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [       474676,       474672,       474676,       474676,       474426,       474422, ],
    'CountWeightedL1PrefireNomTOP16011TopPtRwgtSF'                                   : [        45560,        45563,        45555, ],
    'CountWeightedL1PrefireNomTOP16011TopPtRwgtSFSquared'                            : [        45662,        45667,        45655, ],
    'CountWeightedL1PrefireNomLinearTopPtRwgtSF'                                     : [        45591,        45594,        45586, ],
    'CountWeightedL1PrefireNomLinearTopPtRwgtSFSquared'                              : [        45714,        45719,        45708, ],
    'CountWeightedL1PrefireNomQuadraticTopPtRwgtSF'                                  : [        45603,        45606,        45598, ],
    'CountWeightedL1PrefireNomQuadraticTopPtRwgtSFSquared'                           : [        45761,        45767,        45754, ],
    'CountWeightedL1PrefireTOP16011TopPtRwgtSF'                                      : [        45560,        45223,        45887, ],
    'CountWeightedL1PrefireTOP16011TopPtRwgtSFSquared'                               : [        45662,        45327,        45988, ],
    'CountWeightedL1PrefireLinearTopPtRwgtSF'                                        : [        45591,        45254,        45919, ],
    'CountWeightedL1PrefireLinearTopPtRwgtSFSquared'                                 : [        45714,        45378,        46041, ],
    'CountWeightedL1PrefireQuadraticTopPtRwgtSF'                                     : [        45603,        45266,        45930, ],
    'CountWeightedL1PrefireQuadraticTopPtRwgtSFSquared'                              : [        45761,        45426,        46088, ],
    'CountWeightedLHEWeightScaleL1PrefireNomTOP16011TopPtRwgtSF'                     : [        51364,        50431,        49825,        46705,        45558,        44681,        42252,        41028,        40023, ],
    'CountWeightedLHEWeightScaleL1PrefireNomTOP16011TopPtRwgtSFSquared'              : [        51487,        50556,        49953,        46802,        45660,        44786,        42330,        41111,        40111, ],
    'CountWeightedLHEWeightScaleL1PrefireNomLinearTopPtRwgtSF'                       : [        51398,        50465,        49859,        46737,        45589,        44710,        42282,        41056,        40050, ],
    'CountWeightedLHEWeightScaleL1PrefireNomLinearTopPtRwgtSFSquared'                : [        51545,        50613,        50009,        46857,        45713,        44837,        42381,        41160,        40158, ],
    'CountWeightedLHEWeightScaleL1PrefireNomQuadraticTopPtRwgtSF'                    : [        51416,        50482,        49875,        46748,        45601,        44723,        42289,        41064,        40059, ],
    'CountWeightedLHEWeightScaleL1PrefireNomQuadraticTopPtRwgtSFSquared'             : [        51606,        50673,        50068,        46903,        45760,        44885,        42417,        41197,        40196, ],
    'CountWeightedLHEEnvelopeL1PrefireNomTOP16011TopPtRwgtSF'                        : [        55472,        37339, ],
    'CountWeightedLHEEnvelopeL1PrefireNomTOP16011TopPtRwgtSFSquared'                 : [        55583,        37444, ],
    'CountWeightedLHEEnvelopeL1PrefireNomLinearTopPtRwgtSF'                          : [        55511,        37362, ],
    'CountWeightedLHEEnvelopeL1PrefireNomLinearTopPtRwgtSFSquared'                   : [        55649,        37483, ],
    'CountWeightedLHEEnvelopeL1PrefireNomQuadraticTopPtRwgtSF'                       : [        55526,        37374, ],
    'CountWeightedLHEEnvelopeL1PrefireNomQuadraticTopPtRwgtSFSquared'                : [        55706,        37526, ],
    'CountWeightedPSWeightL1PrefireNomTOP16011TopPtRwgtSF'                           : [        45612,        45580,        64456,        45487,        45524,        28502, ],
    'CountWeightedPSWeightL1PrefireNomTOP16011TopPtRwgtSFSquared'                    : [        45715,        45684,        64588,        45588,        45628,        28580, ],
    'CountWeightedPSWeightL1PrefireNomLinearTopPtRwgtSF'                             : [        45643,        45610,        64500,        45518,        45554,        28520, ],
    'CountWeightedPSWeightL1PrefireNomLinearTopPtRwgtSFSquared'                      : [        45767,        45736,        64663,        45641,        45681,        28611, ],
    'CountWeightedPSWeightL1PrefireNomQuadraticTopPtRwgtSF'                          : [        45655,        45622,        64514,        45530,        45567,        28530, ],
    'CountWeightedPSWeightL1PrefireNomQuadraticTopPtRwgtSFSquared'                   : [        45815,        45784,        64724,        45688,        45727,        28645, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNomTOP16011TopPtRwgtSF'             : [       458888,       458884,       458888,       458888,       458650,       458646, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNomTOP16011TopPtRwgtSFSquared'      : [       459840,       459836,       459840,       459840,       459603,       459598, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNomLinearTopPtRwgtSF'               : [       459206,       459202,       459206,       459206,       458968,       458964, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNomLinearTopPtRwgtSFSquared'        : [       460388,       460384,       460388,       460388,       460150,       460146, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNomQuadraticTopPtRwgtSF'            : [       459317,       459312,       459317,       459317,       459078,       459074, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNomQuadraticTopPtRwgtSFSquared'     : [       460842,       460838,       460842,       460842,       460604,       460600, ],
  }),
  ("nof_tree_events",                 47260),
  ("nof_db_events",                   69155808),
  ("fsize_local",                     218229643), # 218.23MB, avg file size 218.23MB
  ("fsize_db",                        3693271643807), # 3.69TB, avg file size 3.50GB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2017/2020Apr22_woPresel_nonNom_hh_bbww_sync_ttbar/ntuples/TTTo2L2Nu_PSweights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
]

