from collections import OrderedDict as OD

# file generated at 2020-04-28 13:09:50 with the following command:
# create_dictionary.py -m python/samples/metaDict_2018_ttbar.py -p /hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples -N samples_2018 -E 2018 -o python/samples -g hhAnalyzeSamples_2018_ttbar_preselected.py -M

samples_2018 = OD()
samples_2018["/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_hdampDown"),
  ("process_name_specific",           "TTTo2L2Nu_hdampDOWN"),
  ("nof_files",                       2),
  ("nof_db_files",                    158),
  ("nof_events",                      {
    'Count'                                                                          : [      5458000, ],
    'CountWeighted'                                                                  : [      5367993,      5368105,      5368526, ],
    'CountWeightedLHEWeightScale'                                                    : [      6048180,      5943082,      5875950,      5499785,      5367993,      5267473,      4976735,      4834640,      4717736, ],
    'CountWeightedLHEEnvelope'                                                       : [      6601341,      4331016, ],
    'CountWeightedPSWeight'                                                          : [      5368335,      5368396,      7589394,      5368338,      5363409,      3362778, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     54573605,     54573148,     54573660,     54573609,     54545468,     54544904, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      5373825,      5373796,      5373843, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      5386315,      5386286,      5386342, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      5377512,      5377479,      5377534, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      5392606,      5392570,      5392626, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      5379183,      5379149,      5379208, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      5398691,      5398652,      5398722, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [      6054337,      5950129,      5883822,      5504157,      5373825,      5273818,      4979674,      4838751,      4722818, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [      6068409,      5964920,      5899322,      5515806,      5386315,      5287057,      4989273,      4849275,      4734116, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [      6058544,      5954158,      5887717,      5508047,      5377512,      5277344,      4983257,      4842117,      4726012, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [      6075585,      5971783,      5905937,      5522454,      5392606,      5293048,      4995404,      4855024,      4739549, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [      6060754,      5956383,      5889959,      5509630,      5379183,      5279083,      4984390,      4843376,      4727370, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [      6083077,      5979262,      5913442,      5528422,      5398691,      5299243,      5000204,      4860020,      4744702, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [      6605596,      4338508, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [      6618617,      4351569, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [      6610351,      4341232, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [      6626759,      4356172, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [      6612193,      4343021, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [      6633778,      4362006, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      5373862,      5373671,      7594795,      5373664,      5369068,      3368062, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      5386449,      5386019,      7610246,      5386037,      5381758,      3377713, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      5377547,      5377373,      7600193,      5377364,      5372725,      3370218, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      5392722,      5392333,      7619478,      5392343,      5387991,      3381358, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      5379220,      5379025,      7602189,      5379022,      5374397,      3371543, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      5398827,      5398382,      7627322,      5398415,      5394098,      3385766, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     54615452,     54614992,     54615503,     54615452,     54587566,     54587016, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     54724605,     54724145,     54724647,     54724605,     54696954,     54696402, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     54654938,     54654486,     54654993,     54654938,     54627018,     54626464, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     54792032,     54791585,     54792087,     54792036,     54764307,     54763755, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     54670176,     54669724,     54670226,     54670176,     54642265,     54641707, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     54850123,     54849676,     54850174,     54850127,     54822412,     54821859, ],
  }),
  ("nof_tree_events",                 2057374),
  ("nof_db_events",                   5458000),
  ("fsize_local",                     8471481789), # 8.47GB, avg file size 4.24GB
  ("fsize_db",                        289530779054), # 289.53GB, avg file size 1.83GB
  ("use_it",                          False),
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_hdampDOWN"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_hdampDown"),
  ("process_name_specific",           "TTTo2L2Nu_hdampDOWN_ext1"),
  ("nof_files",                       1),
  ("nof_db_files",                    264),
  ("nof_events",                      {
    'Count'                                                                          : [      9952000, ],
    'CountWeighted'                                                                  : [      9788213,      9789154,      9785251, ],
    'CountWeightedLHEWeightScale'                                                    : [     11030324,     10837277,     10713774,     10028487,      9788213,      9603030,      9073600,      8813905,      8600226, ],
    'CountWeightedLHEEnvelope'                                                       : [     12035507,      7898248, ],
    'CountWeightedPSWeight'                                                          : [      9788044,      9789500,     13838771,      9787835,      9778242,      6130522, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     99517152,     99516176,     99517200,     99517152,     99464608,     99463496, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      9797939,      9797901,      9797971, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      9820841,      9820779,      9820925, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      9804649,      9804611,      9804685, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      9832264,      9832208,      9832360, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      9807767,      9807716,      9807821, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      9843532,      9843465,      9843622, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     11041597,     10850207,     10728242,     10036537,      9797939,      9614738,      9079079,      8821548,      8609621, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     11067296,     10877264,     10756614,     10057872,      9820841,      9639006,      9096699,      8840867,      8630367, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     11049255,     10857539,     10735319,     10043618,      9804649,      9621152,      9085598,      8827668,      8615424, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     11080381,     10889754,     10768647,     10069968,      9832264,      9649894,      9107839,      8851310,      8640237, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     11053387,     10861677,     10739476,     10046606,      9807767,      9624383,      9087737,      8830036,      8617970, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     11094255,     10903567,     10782468,     10081028,      9843532,      9661315,      9116747,      8860555,      8649748, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     12043364,      7911999, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     12067193,      7935916, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     12052005,      7916961, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     12082011,      7944290, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     12055454,      7920286, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     12095010,      7955061, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      9798210,      9799265,     13848870,      9797624,      9788668,      6140212, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      9821252,      9821929,     13877265,      9820304,      9811972,      6157866, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      9804909,      9806008,     13858685,      9804354,      9795327,      6144132, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      9832656,      9833401,     13894054,      9831779,      9823312,      6164489, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      9808038,      9809102,     13862475,      9807438,      9798504,      6146577, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      9843966,      9844612,     13908700,      9842976,      9834667,      6172592, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     99586336,     99585352,     99586384,     99586328,     99534248,     99533160, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     99787008,     99786056,     99787064,     99787000,     99735352,     99734264, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     99658240,     99657264,     99658288,     99658240,     99606072,     99604992, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     99909688,     99908736,     99909752,     99909696,     99857872,     99856792, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     99686704,     99685720,     99686752,     99686704,     99634568,     99633496, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    100017240,    100016248,    100017296,    100017240,     99965472,     99964392, ],
  }),
  ("nof_tree_events",                 3751093),
  ("nof_db_events",                   9952000),
  ("fsize_local",                     15446520616), # 15.45GB, avg file size 15.45GB
  ("fsize_db",                        527737712006), # 527.74GB, avg file size 2.00GB
  ("use_it",                          False),
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_hdampDOWN_ext1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTToSemiLeptonic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_hdampDown"),
  ("process_name_specific",           "TTToSemiLeptonic_hdampDOWN"),
  ("nof_files",                       6),
  ("nof_db_files",                    695),
  ("nof_events",                      {
    'Count'                                                                          : [     25904000, ],
    'CountWeighted'                                                                  : [     25476040,     25477040,     25477636, ],
    'CountWeightedLHEWeightScale'                                                    : [     28713229,     28208989,     27885632,     26104145,     25475885,     24994027,     23617820,     22940547,     22383221, ],
    'CountWeightedLHEEnvelope'                                                       : [     31327218,     20558508, ],
    'CountWeightedPSWeight'                                                          : [     25476513,     25476137,     36877145,     25476724,     25432435,     15189175, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    259018018,    259018100,    259018100,    259018018,    259017296,    259017208, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     25502631,     25502498,     25502764, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     25562157,     25562030,     25562329, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     25520089,     25519960,     25520241, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     25591932,     25591764,     25592092, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     25528179,     25528035,     25528338, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     25621169,     25621003,     25621374, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     28742384,     28242561,     27923342,     26124954,     25501861,     25024521,     23631956,     22960352,     22407734, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     28809127,     28312913,     27997263,     26180334,     25561387,     25087733,     23677701,     23010607,     22461760, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     28762316,     28261640,     27941765,     26143382,     25519326,     25041209,     23648916,     22976289,     22422845, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     28843154,     28345418,     28028545,     26211824,     25591137,     25116085,     23706701,     23037790,     22487434, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     28773012,     28272402,     27952627,     26151064,     25527400,     25049639,     23654427,     22982417,     22429442, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     28879127,     28381370,     28064627,     26240503,     25620388,     25145848,     23729772,     23061816,     22512211, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     31347697,     20594140, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     31409759,     20656231, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     31370199,     20607064, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     31448290,     20678047, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     31379167,     20615678, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     31482086,     20706005, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     25502966,     25501410,     36905063,     25502180,     25459711,     15212746, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     25562941,     25560283,     36981785,     25561144,     25520384,     15256057, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     25520397,     25518951,     36931141,     25519694,     25477023,     15222484, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     25592626,     25590167,     37026378,     25590989,     25549876,     15272536, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     25528551,     25527004,     36941361,     25527691,     25485184,     15228477, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     25622018,     25619347,     37065575,     25620068,     25579269,     15292443, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    259211844,    259211926,    259211930,    259211844,    259211124,    259211038, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    259733284,    259733366,    259733370,    259733284,    259732576,    259732478, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    259398640,    259398726,    259398726,    259398640,    259397916,    259397826, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    260052294,    260052380,    260052388,    260052294,    260051580,    260051496, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    259472808,    259472890,    259472894,    259472808,    259472088,    259471990, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    260331724,    260331818,    260331818,    260331724,    260331012,    260330924, ],
  }),
  ("nof_tree_events",                 2348627),
  ("nof_db_events",                   25904000),
  ("fsize_local",                     10376826511), # 10.38GB, avg file size 1.73GB
  ("fsize_db",                        1388433897628), # 1.39TB, avg file size 2.00GB
  ("use_it",                          False),
  ("xsection",                        365.52),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTToSemiLeptonic_hdampDOWN"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTToHadronic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_hdampDown"),
  ("process_name_specific",           "TTToHadronic_hdampDOWN"),
  ("nof_files",                       6),
  ("nof_db_files",                    729),
  ("nof_events",                      {
    'Count'                                                                          : [     26425000, ],
    'CountWeighted'                                                                  : [     25987209,     25988992,     25986817, ],
    'CountWeightedLHEWeightScale'                                                    : [     29287909,     28773082,     28443001,     26628781,     25987102,     25495356,     24093916,     23402635,     22833758, ],
    'CountWeightedLHEEnvelope'                                                       : [     31955032,     20971447, ],
    'CountWeightedPSWeight'                                                          : [     25987457,     25985870,     38406670,     25988798,     25914890,     14787172, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    264227430,    264227542,    264227542,    264227434,    264226221,    264226117, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     26014471,     26014472,     26014487, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     26075047,     26075049,     26075080, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     26032303,     26032317,     26032310, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     26105440,     26105436,     26105455, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     26040508,     26040532,     26040516, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     26135173,     26135195,     26135207, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     29317497,     28807215,     28481357,     26649856,     26013686,     25526320,     24108166,     23422693,     22858607, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     29385434,     28878856,     28556625,     26706191,     26074267,     25590660,     24154659,     23473787,     22913558, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     29337863,     28826704,     28500174,     26668668,     26031519,     25543359,     24125486,     23438972,     22874028, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     29420178,     28912048,     28588580,     26738351,     26104639,     25619620,     24184275,     23501559,     22939781, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     29348689,     28837616,     28511201,     26676441,     26039717,     25551921,     24131057,     23445173,     22880731, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     29456720,     28948593,     28625274,     26767465,     26134376,     25649883,     24207707,     23525985,     22964979, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     31975778,     21007667, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     32038937,     21070859, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     31998770,     21020850, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     32078296,     21093131, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     32007855,     21029580, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     32112653,     21121543, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     26014267,     26011529,     38436522,     26014680,     25942559,     14809612, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     26075250,     26071439,     38517141,     26074736,     26004254,     14851285, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     26032068,     26029433,     38463603,     26032555,     25960213,     14819150, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     26105579,     26101949,     38563464,     26105226,     26034316,     14867420, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     26040317,     26037571,     38474337,     26040696,     25968523,     14824875, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     26135435,     26131539,     38604474,     26134815,     26064251,     14886596, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    264422802,    264422918,    264422918,    264422802,    264421632,    264421520, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    264952704,    264952804,    264952804,    264952700,    264951537,    264951429, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    264613776,    264613896,    264613896,    264613780,    264612605,    264612493, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    265278504,    265278604,    265278604,    265278508,    265277329,    265277229, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    264688934,    264689046,    264689046,    264688930,    264687775,    264687663, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    265562700,    265562812,    265562812,    265562700,    265561541,    265561429, ],
  }),
  ("nof_tree_events",                 319957),
  ("nof_db_events",                   26425000),
  ("fsize_local",                     1463346367), # 1.46GB, avg file size 243.89MB
  ("fsize_db",                        1432904122912), # 1.43TB, avg file size 1.97GB
  ("use_it",                          False),
  ("xsection",                        377.85),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTToHadronic_hdampDOWN"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTTo2L2Nu_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_hdampUp"),
  ("process_name_specific",           "TTTo2L2Nu_hdampUP"),
  ("nof_files",                       1),
  ("nof_db_files",                    148),
  ("nof_events",                      {
    'Count'                                                                          : [      5260000, ],
    'CountWeighted'                                                                  : [      5236541,      5236735,      5236548, ],
    'CountWeightedLHEWeightScale'                                                    : [      5898357,      5796129,      5730682,      5364203,      5236541,      5137461,      4854095,      4715389,      4601385, ],
    'CountWeightedLHEEnvelope'                                                       : [      6334632,      4329688, ],
    'CountWeightedPSWeight'                                                          : [      5236217,      5235933,      7417329,      5235583,      5228588,      3266011, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     52593372,     52592784,     52593388,     52593372,     52562660,     52562048, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      5238662,      5238684,      5238645, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      5248250,      5248260,      5248248, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      5242453,      5242475,      5242435, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      5254736,      5254757,      5254751, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      5243657,      5243661,      5243646, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      5259767,      5259768,      5259781, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [      5902913,      5801016,      5735924,      5366191,      5238662,      5140775,      4854325,      4716554,      4603313, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [      5915155,      5813437,      5748587,      5375260,      5248250,      5150814,      4861033,      4723965,      4611319, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [      5907102,      5805076,      5739895,      5370141,      5242453,      5144428,      4858010,      4720042,      4606655, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [      5922324,      5820397,      5755378,      5382057,      5254736,      5157075,      4867381,      4729977,      4617061, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [      5908902,      5806870,      5741668,      5371278,      5243657,      5145672,      4858691,      4720840,      4607539, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [      5928894,      5826882,      5761805,      5387006,      5259767,      5162136,      4871162,      4733922,      4621118, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [      6337398,      4333439, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [      6348533,      4342803, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [      6342053,      4336432, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [      6356519,      4347930, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [      6343594,      4337568, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [      6362766,      4352374, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      5238967,      5238537,      7418779,      5238169,      5231430,      3269647, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      5248632,      5248015,      7430044,      5247641,      5241142,      3277516, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      5242747,      5242322,      7424332,      5241955,      5235196,      3271844, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      5255114,      5254524,      7439626,      5254153,      5247620,      3281263, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      5243962,      5243513,      7425679,      5243146,      5236417,      3272875, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      5260167,      5259538,      7445999,      5259144,      5252666,      3284996, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     52618424,     52617852,     52618444,     52618428,     52588016,     52587408, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     52706984,     52706416,     52707004,     52706988,     52676840,     52676244, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     52657444,     52656864,     52657460,     52657444,     52626980,     52626368, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     52773948,     52773380,     52773968,     52773948,     52743712,     52743104, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     52669136,     52668564,     52669152,     52669136,     52638700,     52638100, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     52823604,     52823032,     52823616,     52823600,     52793400,     52792792, ],
  }),
  ("nof_tree_events",                 1984865),
  ("nof_db_events",                   5260000),
  ("fsize_local",                     8274190729), # 8.27GB, avg file size 8.27GB
  ("fsize_db",                        280579235973), # 280.58GB, avg file size 1.90GB
  ("use_it",                          False),
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_hdampUP"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTTo2L2Nu_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_hdampUp"),
  ("process_name_specific",           "TTTo2L2Nu_hdampUP_ext1"),
  ("nof_files",                       2),
  ("nof_db_files",                    314),
  ("nof_events",                      {
    'Count'                                                                          : [      9903000, ],
    'CountWeighted'                                                                  : [      9859938,      9858693,      9858806, ],
    'CountWeightedLHEWeightScale'                                                    : [     11106531,     10912567,     10787799,     10101093,      9859938,      9671645,      9140562,      8878363,      8662802, ],
    'CountWeightedLHEEnvelope'                                                       : [     11928660,      8150279, ],
    'CountWeightedPSWeight'                                                          : [      9858042,      9859534,     13968384,      9858802,      9845376,      6148674, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     99028406,     99027286,     99028470,     99028390,     98970056,     98968816, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      9863456,      9863407,      9863439, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      9881524,      9881438,      9881563, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      9870588,      9870541,      9870577, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      9893778,      9893694,      9893820, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      9872872,      9872803,      9872891, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      9903270,      9903157,      9903348, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     11115086,     10921784,     10797694,     10104845,      9863456,      9677938,      9141004,      8880590,      8666490, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     11138118,     10945183,     10821580,     10121925,      9881524,      9696886,      9153660,      8894595,      8681612, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     11122978,     10929424,     10805178,     10112289,      9870588,      9684824,      9147940,      8887180,      8672780, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     11151645,     10958290,     10834378,     10134728,      9893778,      9708679,      9165639,      8905935,      8692417, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     11126412,     10932808,     10808515,     10114454,      9872872,      9687177,      9149268,      8888699,      8674461, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     11164073,     10970528,     10846479,     10144123,      9903270,      9718255,      9172805,      8913407,      8700100, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     11933832,      8157423, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     11954755,      8175117, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     11942594,      8163051, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     11969826,      8184757, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     11945525,      8165202, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     11981617,      8193193, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      9863290,      9864298,     13971351,      9863635,      9851133,      6155535, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      9881522,      9882037,     13992776,      9881479,      9869804,      6170375, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      9870409,      9871455,     13981807,      9870786,      9858207,      6159676, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      9893742,      9894337,     14010814,      9893766,      9881953,      6177438, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      9872708,      9873683,     13984417,      9873046,      9860601,      6161639, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      9903299,      9903732,     14022966,      9903203,      9891676,      6184489, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     99065257,     99064145,     99065321,     99065257,     99007516,     99006284, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     99232837,     99231701,     99232877,     99232821,     99175577,     99174361, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     99138820,     99137700,     99138868,     99138820,     99080975,     99079735, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     99359000,     99357872,     99359048,     99359000,     99301564,     99300348, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     99161159,     99160047,     99161215,     99161159,     99103362,     99102122, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     99452857,     99451737,     99452905,     99452849,     99395500,     99394276, ],
  }),
  ("nof_tree_events",                 3734951),
  ("nof_db_events",                   9903000),
  ("fsize_local",                     15575760678), # 15.58GB, avg file size 7.79GB
  ("fsize_db",                        529852266703), # 529.85GB, avg file size 1.69GB
  ("use_it",                          False),
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_hdampUP_ext1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTToSemiLeptonic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_hdampUp"),
  ("process_name_specific",           "TTToSemiLeptonic_hdampUP"),
  ("nof_files",                       3),
  ("nof_db_files",                    567),
  ("nof_events",                      {
    'Count'                                                                          : [     26764000, ],
    'CountWeighted'                                                                  : [     26645714,     26641598,     26639319, ],
    'CountWeightedLHEWeightScale'                                                    : [     30019951,     29493728,     29154946,     27300352,     26644193,     26137314,     24703008,     23993343,     23410041, ],
    'CountWeightedLHEEnvelope'                                                       : [     32237192,     22029124, ],
    'CountWeightedPSWeight'                                                          : [     26643340,     26645743,     38641011,     26642467,     26584020,     15820114, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    267616872,    267617120,    267617120,    267616872,    267616176,    267615944, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     26656998,     26656933,     26656919, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     26706069,     26705966,     26706093, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     26676189,     26676166,     26676184, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     26739114,     26738985,     26739169, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     26682353,     26682279,     26682316, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     26764622,     26764553,     26764674, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     30043263,     29518887,     29182043,     27310653,     26656163,     26154614,     24704377,     23999623,     23420317, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     30105620,     29582327,     29246844,     27356984,     26705232,     26206081,     24738737,     24037702,     23461425, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     30064551,     29539557,     29202192,     27330751,     26675414,     26173164,     24723123,     24017419,     23437277, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     30142127,     29617714,     29281373,     27391561,     26738303,     26237885,     24771048,     24068278,     23490578, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     30073751,     29548597,     29211176,     27336547,     26681544,     26179492,     24726616,     24021454,     23441751, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     30175542,     29650641,     29313980,     27416750,     26763809,     26263658,     24790297,     24088352,     23511247, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     32251533,     22048566, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     32308338,     22096513, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     32275169,     22063779, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     32349007,     22122558, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     32283048,     22069516, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     32380760,     22145158, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     26657849,     26658951,     38650659,     26655806,     26599587,     15837373, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     26707372,     26707187,     38711379,     26704230,     26649974,     15875114, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     26677044,     26678276,     38679443,     26675104,     26618655,     15848059, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     26740343,     26740346,     38760950,     26737374,     26682713,     15893364, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     26683201,     26684267,     38686722,     26681118,     26624959,     15852960, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     26766010,     26765691,     38794622,     26762738,     26708620,     15911246, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    267738680,    267738904,    267738904,    267738680,    267737976,    267737760, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    268193392,    268193576,    268193584,    268193392,    268192680,    268192456, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    267937032,    267937256,    267937264,    267937032,    267936336,    267936112, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    268533768,    268533992,    268534000,    268533768,    268533072,    268532848, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    267996784,    267996984,    267996992,    267996784,    267996080,    267995840, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    268785976,    268786168,    268786176,    268785976,    268785256,    268785016, ],
  }),
  ("nof_tree_events",                 2439685),
  ("nof_db_events",                   26964000),
  ("fsize_local",                     10900730829), # 10.90GB, avg file size 3.63GB
  ("fsize_db",                        1451857443237), # 1.45TB, avg file size 2.56GB
  ("use_it",                          False),
  ("xsection",                        365.52),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTToSemiLeptonic_hdampUP"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTToHadronic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_hdampUp"),
  ("process_name_specific",           "TTToHadronic_hdampUP"),
  ("nof_files",                       3),
  ("nof_db_files",                    690),
  ("nof_events",                      {
    'Count'                                                                          : [     22365000, ],
    'CountWeighted'                                                                  : [     22266192,     22264359,     22261770, ],
    'CountWeightedLHEWeightScale'                                                    : [     25082834,     24645317,     24364306,     22811294,     22266192,     21842661,     20641679,     20049963,     19563723, ],
    'CountWeightedLHEEnvelope'                                                       : [     26937371,     18408410, ],
    'CountWeightedPSWeight'                                                          : [     22262852,     22265952,     32969683,     22265037,     22196273,     12618208, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    223666710,    223666852,    223666852,    223666710,    223665736,    223665594, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     22275125,     22275186,     22274935, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     22315837,     22315943,     22315693, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     22291178,     22291294,     22291028, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     22343482,     22343580,     22343328, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     22296236,     22296339,     22296106, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     22364697,     22364836,     22364575, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     25102039,     24666075,     24386675,     22819636,     22275125,     21856859,     20642568,     20054975,     19572066, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     25153869,     24718819,     24440601,     22858078,     22315837,     21899592,     20671024,     20086531,     19606178, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     25119820,     24683335,     24403545,     22836435,     22291178,     21872372,     20658238,     20069832,     19586264, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     25184374,     24748396,     24469469,     22886971,     22343482,     21926234,     20698044,     20112126,     19630580, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     25127434,     24690861,     24410989,     22841228,     22296236,     21877625,     20661096,     20073165,     19589956, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     25212183,     24775818,     24496645,     22907916,     22364697,     21947683,     20714001,     20128775,     19647754, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     26949038,     18424439, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     26996211,     18464278, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     26968798,     18437152, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     27030191,     18486069, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     26975288,     18441905, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     27056584,     18504885, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     22274667,     22276831,     32978361,     22275912,     22208865,     12631519, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     22315804,     22317006,     33030578,     22316093,     22250578,     12661180, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     22290729,     22292977,     33002868,     22292047,     22224813,     12640066, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     22343372,     22344751,     33072776,     22343810,     22277948,     12675791, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     22295836,     22297978,     33009124,     22297015,     22229973,     12643899, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     22364722,     22365880,     33101638,     22364907,     22299413,     12689882, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    223728428,    223728562,    223728562,    223728420,    223727446,    223727320, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    224105534,    224105662,    224105662,    224105534,    224104594,    224104428, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    223894548,    223894698,    223894698,    223894548,    223893584,    223893424, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    224390492,    224390628,    224390628,    224390492,    224389542,    224389400, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    223944088,    223944254,    223944254,    223944088,    223943132,    223942988, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    224600448,    224600564,    224600564,    224600448,    224599490,    224599340, ],
  }),
  ("nof_tree_events",                 270919),
  ("nof_db_events",                   24965000),
  ("fsize_local",                     1249260015), # 1.25GB, avg file size 416.42MB
  ("fsize_db",                        1360863997866), # 1.36TB, avg file size 1.97GB
  ("use_it",                          False),
  ("xsection",                        377.85),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTToHadronic_hdampUP"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTTo2L2Nu_TuneCP5down_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_ueDown"),
  ("process_name_specific",           "TTTo2L2Nu_ueDown"),
  ("nof_files",                       1),
  ("nof_db_files",                    145),
  ("nof_events",                      {
    'Count'                                                                          : [      4954000, ],
    'CountWeighted'                                                                  : [      4914246,      4914559,      4914552, ],
    'CountWeightedLHEWeightScale'                                                    : [      5537771,      5441286,      5379254,      5035195,      4914219,      4821523,      4555599,      4425118,      4317874, ],
    'CountWeightedLHEEnvelope'                                                       : [      5985040,      4025438, ],
    'CountWeightedPSWeight'                                                          : [      4914968,      4914851,      6947471,      4913762,      4905937,      3076389, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     49541696,     49541248,     49541696,     49541696,     49515208,     49514764, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      4918284,      4918252,      4918300, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      4928614,      4928563,      4928663, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      4921730,      4921709,      4921755, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      4934520,      4934477,      4934570, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      4923057,      4923035,      4923090, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      4939657,      4939615,      4939705, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [      5542781,      5446920,      5385478,      5038198,      4918129,      4826140,      4557146,      4427688,      4321267, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [      5555002,      5459605,      5398660,      5047856,      4928463,      4837065,      4564779,      4436107,      4330340, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [      5546663,      5450647,      5389108,      5041829,      4921576,      4829461,      4560511,      4430852,      4324281, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [      5561648,      5465980,      5404847,      5054078,      4934366,      4842715,      4570543,      4441535,      4335489, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [      5548526,      5452510,      5390969,      5043085,      4922908,      4830835,      4561337,      4431799,      4325313, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [      5568164,      5472465,      5411306,      5059115,      4939505,      4847932,      4574502,      4445658,      4339747, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [      5988335,      4030789, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [      5999526,      4041313, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [      5992679,      4033431, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [      6006984,      4045808, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [      5994250,      4034762, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [      6013131,      4050538, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      4918924,      4918572,      6950907,      4917543,      4910109,      3080570, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      4929330,      4928761,      6963504,      4927768,      4920701,      3088736, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      4922375,      4922041,      6955953,      4921003,      4913526,      3082588, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      4935217,      4934692,      6972177,      4933694,      4926545,      3092161, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      4923704,      4923354,      6957520,      4922319,      4914896,      3083674, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      4940380,      4939796,      6978787,      4938796,      4931760,      3095919, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     49567668,     49567220,     49567668,     49567668,     49541432,     49540992, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     49661600,     49661176,     49661600,     49661600,     49635576,     49635144, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     49603800,     49603364,     49603800,     49603800,     49577520,     49577084, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     49723356,     49722916,     49723356,     49723356,     49697244,     49696804, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     49616472,     49616032,     49616472,     49616472,     49590212,     49589776, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     49773628,     49773196,     49773628,     49773628,     49747540,     49747108, ],
  }),
  ("nof_tree_events",                 1867796),
  ("nof_db_events",                   4954000),
  ("fsize_local",                     7736533996), # 7.74GB, avg file size 7.74GB
  ("fsize_db",                        262841944418), # 262.84GB, avg file size 1.81GB
  ("use_it",                          False),
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_ueDown"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTTo2L2Nu_TuneCP5down_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_ueDown"),
  ("process_name_specific",           "TTTo2L2Nu_ueDown_ext1"),
  ("nof_files",                       1),
  ("nof_db_files",                    269),
  ("nof_events",                      {
    'Count'                                                                          : [      9816000, ],
    'CountWeighted'                                                                  : [      9738718,      9736236,      9734079, ],
    'CountWeightedLHEWeightScale'                                                    : [     10971489,     10779269,     10655644,      9976666,      9738187,      9551972,      9027206,      8768021,      8554930, ],
    'CountWeightedLHEEnvelope'                                                       : [     11857238,      7975936, ],
    'CountWeightedPSWeight'                                                          : [      9736696,      9735929,     13769582,      9736686,      9725544,      6094236, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     98145640,     98144720,     98145656,     98145640,     98093200,     98092232, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      9743940,      9743959,      9743866, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      9764091,      9764106,      9764010, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      9750815,      9750836,      9750741, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      9775852,      9775855,      9775770, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      9753391,      9753396,      9753321, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      9785917,      9785934,      9785834, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     10981114,     10790054,     10667580,      9982342,      9743640,      9560760,      9029988,      8772788,      8561307, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     11005061,     10814864,     10693294,     10001192,      9763794,      9582018,      9044845,      8789181,      8578952, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     10988846,     10797503,     10674804,      9989562,      9750519,      9567346,      9036675,      8779113,      8567306, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     11018276,     10827580,     10705627,     10013567,      9775557,      9593286,      9056310,      8799994,      8589215, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     10992484,     10801129,     10678426,      9991998,      9753095,      9570017,      9038284,      8780933,      8569298, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     11031090,     10840286,     10718273,     10023471,      9785619,      9603475,      9064065,      8808056,      8597533, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     11863353,      7986275, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     11885157,      8006867, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     11872012,      7991538, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     11900016,      8015817, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     11875084,      7994111, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     11912091,      8025072, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      9744131,      9743011,     13775832,      9743771,      9733372,      6102334, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      9764423,      9762896,     13800278,      9763700,      9753937,      6118325, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      9751002,      9749904,     13785889,      9750661,      9740187,      6106342, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      9776163,      9774701,     13817561,      9775496,      9765602,      6125139, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      9753586,      9752445,     13788886,      9753210,      9742797,      6108467, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      9786270,      9784716,     13830444,      9785509,      9775758,      6132531, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     98211512,     98210592,     98211528,     98211496,     98159520,     98158560, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     98394296,     98393376,     98394312,     98394288,     98342688,     98341744, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     98283192,     98282264,     98283208,     98283192,     98231112,     98230144, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     98517088,     98516176,     98517104,     98517088,     98465336,     98464392, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     98307680,     98306768,     98307704,     98307688,     98255624,     98254672, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     98615264,     98614344,     98615288,     98615264,     98563544,     98562584, ],
  }),
  ("nof_tree_events",                 3704641),
  ("nof_db_events",                   9816000),
  ("fsize_local",                     15344089644), # 15.34GB, avg file size 15.34GB
  ("fsize_db",                        520405915636), # 520.41GB, avg file size 1.93GB
  ("use_it",                          False),
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_ueDown_ext1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTToSemiLeptonic_TuneCP5down_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_ueDown"),
  ("process_name_specific",           "TTToSemiLeptonic_ueDown"),
  ("nof_files",                       5),
  ("nof_db_files",                    536),
  ("nof_events",                      {
    'Count'                                                                          : [     20483000, ],
    'CountWeighted'                                                                  : [     20314116,     20317806,     20316579, ],
    'CountWeightedLHEWeightScale'                                                    : [     22892630,     22492642,     22235659,     20816166,     20314116,     19931926,     18834621,     18294762,     17850787, ],
    'CountWeightedLHEEnvelope'                                                       : [     24740287,     16643365, ],
    'CountWeightedPSWeight'                                                          : [     20316588,     20314202,     29425048,     20315810,     20284283,     12102437, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    204801072,    204801240,    204801240,    204801072,    204800548,    204800376, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     20332021,     20331949,     20332096, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     20374395,     20374300,     20374510, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     20346314,     20346232,     20346383, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     20398849,     20398762,     20398947, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     20351779,     20351687,     20351855, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     20420068,     20419943,     20420199, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     22913087,     22515525,     22260877,     20828410,     20332021,     19950625,     18840849,     18305063,     17864476, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     22963407,     22567643,     22314898,     20868148,     20374395,     19995370,     18872232,     18339609,     17901655, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     22929147,     22531007,     22275906,     20843400,     20346314,     19964347,     18854730,     18318176,     17876953, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     22990881,     22594087,     22340539,     20893869,     20398849,     20018790,     18896079,     18362088,     17922996, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     22936871,     22538669,     22283548,     20848619,     20351779,     19970008,     18858205,     18322080,     17881190, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     23017869,     22620808,     22367111,     20914766,     20420068,     20040247,     18912469,     18379132,     17940523, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     24753518,     16665209, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     24799475,     16708467, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     24771500,     16676153, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     24830327,     16727106, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     24778005,     16681647, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     24855742,     16746607, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     20332725,     20329266,     29439739,     20331097,     20301003,     12118425, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     20375478,     20371055,     29493286,     20373015,     20344317,     12150101, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     20346982,     20343608,     29461097,     20345425,     20315182,     12126390, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     20399871,     20395587,     29529945,     20397538,     20368572,     12163637, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     20352493,     20348974,     29467776,     20350843,     20320788,     12130618, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     20421177,     20416598,     29558058,     20418632,     20390051,     12178334, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    204940634,    204940806,    204940806,    204940634,    204940138,    204939962, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    205325553,    205325729,    205325729,    205325553,    205325054,    205324882, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    205090019,    205090203,    205090203,    205090019,    205089515,    205089347, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    205581189,    205581345,    205581345,    205581185,    205580681,    205580501, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    205142393,    205142561,    205142561,    205142385,    205141885,    205141709, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    205788901,    205789061,    205789061,    205788889,    205788393,    205788229, ],
  }),
  ("nof_tree_events",                 1869537),
  ("nof_db_events",                   20483000),
  ("fsize_local",                     8307845011), # 8.31GB, avg file size 1.66GB
  ("fsize_db",                        1097359681757), # 1.10TB, avg file size 2.05GB
  ("use_it",                          False),
  ("xsection",                        365.52),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTToSemiLeptonic_ueDown"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTToHadronic_TuneCP5down_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_ueDown"),
  ("process_name_specific",           "TTToHadronic_ueDown"),
  ("nof_files",                       6),
  ("nof_db_files",                    702),
  ("nof_events",                      {
    'Count'                                                                          : [     26627000, ],
    'CountWeighted'                                                                  : [     26412258,     26412412,     26413217, ],
    'CountWeightedLHEWeightScale'                                                    : [     29759626,     29238779,     28903786,     27062596,     26412258,     25911479,     24487861,     23785334,     23207615, ],
    'CountWeightedLHEEnvelope'                                                       : [     32163374,     21636106, ],
    'CountWeightedPSWeight'                                                          : [     26412602,     26410262,     39058449,     26411421,     26341937,     15015425, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    266250542,    266250768,    266250768,    266250538,    266249524,    266249310, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     26432422,     26432450,     26432343, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     26487597,     26487649,     26487492, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     26450983,     26451020,     26450922, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     26519364,     26519421,     26519291, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     26458112,     26458142,     26458044, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     26546991,     26547053,     26546891, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     29786324,     29268707,     28936836,     27078513,     26432422,     25935936,     24495893,     23798759,     23225480, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     29851827,     29336638,     29007322,     27130156,     26487597,     25994239,     24536621,     23843689,     23273876, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     29807203,     29288831,     28956376,     27098015,     26450983,     25953762,     24513960,     23815809,     23241701, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     29887564,     29371005,     29040631,     27163614,     26519364,     26024676,     24567647,     23872909,     23301617, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     29817261,     29298843,     28966376,     27104788,     26458112,     25961158,     24518441,     23820882,     23247214, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     29922678,     29405840,     29075321,     27190773,     26546991,     26052650,     24588916,     23895064,     23324432, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     32180675,     21664588, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     32240520,     21720900, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     32204044,     21678829, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     32280636,     21745129, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     32212532,     21685974, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     32313727,     21770514, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     26433557,     26429993,     39079136,     26431318,     26363752,     15034885, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     26489189,     26484441,     39151380,     26485906,     26420113,     15073819, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     26452092,     26448623,     39107407,     26449945,     26382175,     15044793, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     26520915,     26516335,     39199914,     26517781,     26451619,     15090667, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     26459280,     26455643,     39116482,     26456984,     26389468,     15049971, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     26548654,     26543725,     39237629,     26545221,     26479527,     15108754, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    266414674,    266414874,    266414874,    266414674,    266413660,    266413454, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    266916188,    266916396,    266916396,    266916188,    266915156,    266914948, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    266608710,    266608922,    266608922,    266608706,    266607698,    266607490, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    267248166,    267248362,    267248366,    267248162,    267247152,    267246936, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    266676854,    266677044,    266677048,    266676854,    266675836,    266675630, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    267517878,    267518096,    267518096,    267517874,    267516862,    267516636, ],
  }),
  ("nof_tree_events",                 326309),
  ("nof_db_events",                   26675000),
  ("fsize_local",                     1500401508), # 1.50GB, avg file size 250.07MB
  ("fsize_db",                        1446376287651), # 1.45TB, avg file size 2.06GB
  ("use_it",                          False),
  ("xsection",                        377.85),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTToHadronic_ueDown"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_ueUp"),
  ("process_name_specific",           "TTTo2L2Nu_ueUp"),
  ("nof_files",                       1),
  ("nof_db_files",                    165),
  ("nof_events",                      {
    'Count'                                                                          : [      5446000, ],
    'CountWeighted'                                                                  : [      5402764,      5401928,      5402189, ],
    'CountWeightedLHEWeightScale'                                                    : [      6087083,      5980269,      5911723,      5534983,      5402646,      5299368,      5008167,      4864395,      4746205, ],
    'CountWeightedLHEEnvelope'                                                       : [      6577809,      4425606, ],
    'CountWeightedPSWeight'                                                          : [      5401631,      5403697,      7659636,      5401981,      5392784,      3363426, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     54458216,     54457564,     54458248,     54458212,     54423476,     54422760, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      5406042,      5406051,      5406007, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      5417405,      5417435,      5417348, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      5409837,      5409842,      5409791, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      5423885,      5423907,      5423830, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      5411280,      5411284,      5411244, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      5429513,      5429543,      5429454, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [      6092653,      5986501,      5918573,      5538330,      5405874,      5304445,      5009882,      4867207,      4749903, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [      6106162,      6000495,      5933077,      5548967,      5417232,      5316428,      5018271,      4876448,      4759850, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [      6096911,      5990607,      5922560,      5542304,      5409670,      5308078,      5013570,      4870686,      4753221, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [      6113447,      6007506,      5939864,      5555800,      5423721,      5322636,      5024608,      4882417,      4765508, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [      6098970,      5992647,      5924586,      5543680,      5411116,      5309577,      5014472,      4871707,      4754330, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [      6120617,      6014605,      5946932,      5561337,      5429346,      5328328,      5028936,      4886921,      4770144, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [      6581460,      4431474, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [      6593806,      4443044, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [      6586229,      4434387, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [      6601981,      4447988, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [      6587951,      4435834, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [      6608726,      4453164, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      5405988,      5407794,      7663368,      5406094,      5397311,      3368008, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      5417439,      5418993,      7677212,      5417311,      5408901,      3376941, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      5409770,      5411608,      7668927,      5409891,      5401076,      3370209, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      5423907,      5425510,      7686764,      5423827,      5415334,      3380681, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      5411222,      5413027,      7670622,      5411320,      5402544,      3371391, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      5429560,      5431108,      7694001,      5429400,      5421021,      3384785, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     54490672,     54490032,     54490712,     54490672,     54456236,     54455532, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     54593960,     54593328,     54593992,     54593960,     54559780,     54559076, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     54530236,     54529600,     54530280,     54530236,     54495748,     54495040, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     54661704,     54661068,     54661736,     54661704,     54627432,     54626724, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     54543940,     54543304,     54543976,     54543940,     54509492,     54508780, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     54716624,     54715980,     54716660,     54716616,     54682392,     54681688, ],
  }),
  ("nof_tree_events",                 2054647),
  ("nof_db_events",                   5446000),
  ("fsize_local",                     8523245091), # 8.52GB, avg file size 8.52GB
  ("fsize_db",                        290745204567), # 290.75GB, avg file size 1.76GB
  ("use_it",                          False),
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_ueUp"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_ueUp"),
  ("process_name_specific",           "TTTo2L2Nu_ueUp_ext1"),
  ("nof_files",                       1),
  ("nof_db_files",                    294),
  ("nof_events",                      {
    'Count'                                                                          : [      9968000, ],
    'CountWeighted'                                                                  : [      9888755,      9885976,      9886183, ],
    'CountWeightedLHEWeightScale'                                                    : [     11141237,     10946028,     10820653,     10130758,      9888182,      9699908,      9166646,      8903634,      8687284, ],
    'CountWeightedLHEEnvelope'                                                       : [     12040614,      8099357, ],
    'CountWeightedPSWeight'                                                          : [      9887508,      9887875,     14018166,      9886892,      9872847,      6157265, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     99674304,     99673088,     99674368,     99674304,     99611800,     99610448, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      9894609,      9894534,      9894649, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      9914983,      9914893,      9915072, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      9901584,      9901507,      9901628, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      9926944,      9926829,      9927012, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      9904209,      9904148,      9904277, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      9937179,      9937081,      9937284, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     11150913,     10956897,     10832648,     10136454,      9894306,      9708721,      9169403,      8908401,      8693672, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     11175158,     10982016,     10858681,     10155530,      9914693,      9730238,      9184406,      8924962,      8711524, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     11158766,     10964452,     10839988,     10143777,      9901280,      9715426,      9176193,      8914808,      8699780, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     11188584,     10994936,     10871217,     10168101,      9926630,      9741686,      9196069,      8935944,      8721954, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     11162479,     10968155,     10843674,     10146276,      9903909,      9718156,      9177842,      8916674,      8701811, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     11201619,     11007853,     10884071,     10178192,      9936876,      9752064,      9203986,      8944186,      8730428, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     12046717,      8109758, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     12068779,      8130617, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     12055512,      8115113, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     12083853,      8139725, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     12058633,      8117758, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     12096130,      8149159, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      9895008,      9895019,     14024449,      9893985,      9880640,      6165351, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      9915563,      9915186,     14049317,      9914125,      9901413,      6181424, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      9901991,      9902026,     14034692,      9900995,      9887585,      6169407, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      9927481,      9927168,     14066899,      9926121,      9913277,      6188323, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      9904630,      9904631,     14037817,      9903580,      9890275,      6171552, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      9937803,      9937390,     14080156,      9936297,      9923655,      6195773, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     99731416,     99730216,     99731480,     99731416,     99669480,     99668136, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     99916472,     99915312,     99916536,     99916472,     99855016,     99853696, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     99804440,     99803240,     99804512,     99804432,     99742400,     99741072, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    100041256,    100040080,    100041336,    100041256,     99979608,     99978288, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     99829528,     99828328,     99829584,     99829528,     99767536,     99766192, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    100141696,    100140504,    100141752,    100141696,    100080064,    100078760, ],
  }),
  ("nof_tree_events",                 3754595),
  ("nof_db_events",                   9968000),
  ("fsize_local",                     15575665616), # 15.58GB, avg file size 15.58GB
  ("fsize_db",                        532049001268), # 532.05GB, avg file size 1.81GB
  ("use_it",                          False),
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_ueUp_ext1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTToSemiLeptonic_TuneCP5up_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_ueUp"),
  ("process_name_specific",           "TTToSemiLeptonic_ueUp"),
  ("nof_files",                       6),
  ("nof_db_files",                    722),
  ("nof_events",                      {
    'Count'                                                                          : [     26948000, ],
    'CountWeighted'                                                                  : [     26727093,     26732662,     26729133, ],
    'CountWeightedLHEWeightScale'                                                    : [     30117030,     29590856,     29253185,     27387334,     26727093,     26224066,     24781854,     24071617,     23487462, ],
    'CountWeightedLHEEnvelope'                                                       : [     32550760,     21895969, ],
    'CountWeightedPSWeight'                                                          : [     26729933,     26731692,     38796725,     26729414,     26672369,     15846434, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    269478872,    269479036,    269479040,    269478868,    269477536,    269477362, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     26749899,     26749870,     26749918, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     26805165,     26805120,     26805224, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     26768754,     26768730,     26768789, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     26837466,     26837408,     26837495, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     26775795,     26775775,     26775817, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     26865049,     26865009,     26865105, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     30143432,     29620513,     29285978,     27402876,     26749899,     26248225,     24789475,     24084659,     23505010, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     30209137,     29688654,     29356676,     27454608,     26805165,     26306658,     24830192,     24129616,     23553478, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     30164629,     29640937,     29305807,     27422682,     26768754,     26266325,     24807806,     24101974,     23521481, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     30245410,     29723552,     29390496,     27488564,     26837466,     26337568,     24861701,     24159297,     23581645, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     30174620,     29650877,     29315732,     27429361,     26775795,     26273632,     24812206,     24106960,     23526917, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     30280560,     29758405,     29425197,     27515724,     26865049,     26365515,     24882932,     24181422,     23604441, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     32567581,     21924319, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     32627475,     21980864, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     32591315,     21938776, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     32668205,     22005458, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     32599682,     21945877, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     32701259,     22030888, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     26750624,     26751001,     38815883,     26749066,     26694223,     15866951, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     26806356,     26805484,     38886260,     26803768,     26751039,     15908021, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     26769440,     26769942,     38844092,     26767979,     26712896,     15877417, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     26838561,     26837910,     38934698,     26836126,     26782983,     15925820, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     26776541,     26776900,     38852811,     26774939,     26720160,     15882836, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     26866282,     26865329,     38971582,     26863573,     26811022,     15944815, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    269620256,    269620412,    269620416,    269620252,    269618938,    269618762, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    270121616,    270121780,    270121784,    270121616,    270120320,    270120148, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    269817068,    269817232,    269817240,    269817084,    269815772,    269815606, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    270458930,    270459086,    270459096,    270458930,    270457624,    270457450, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    269884572,    269884736,    269884740,    269884568,    269883272,    269883090, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    270728500,    270728658,    270728662,    270728498,    270727212,    270727048, ],
  }),
  ("nof_tree_events",                 2442560),
  ("nof_db_events",                   26948000),
  ("fsize_local",                     10870710799), # 10.87GB, avg file size 1.81GB
  ("fsize_db",                        1452588033030), # 1.45TB, avg file size 2.01GB
  ("use_it",                          False),
  ("xsection",                        365.52),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTToSemiLeptonic_ueUp"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTToHadronic_TuneCP5up_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_ueUp"),
  ("process_name_specific",           "TTToHadronic_ueUp"),
  ("nof_files",                       5),
  ("nof_db_files",                    634),
  ("nof_events",                      {
    'Count'                                                                          : [     23488000, ],
    'CountWeighted'                                                                  : [     23296899,     23298658,     23300092, ],
    'CountWeightedLHEWeightScale'                                                    : [     26254885,     25794961,     25499334,     23873042,     23296899,     22857463,     21600525,     20980840,     20471118, ],
    'CountWeightedLHEEnvelope'                                                       : [     28372317,     19087367, ],
    'CountWeightedPSWeight'                                                          : [     23298718,     23298155,     34523428,     23299187,     23230099,     13185660, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    234887652,    234887688,    234887696,    234887652,    234886204,    234886148, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     23316757,     23316683,     23316869, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     23365115,     23365067,     23365219, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     23333177,     23333080,     23333269, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     23393205,     23393131,     23393307, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     23339348,     23339278,     23339453, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     23417354,     23417291,     23417452, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     26277958,     25820945,     25528121,     23886710,     23316757,     22878755,     21607336,     20992433,     20486649, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     26335300,     25880478,     25589935,     23931934,     23365115,     22929904,     21642993,     21031809,     20529114, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     26296427,     25838731,     25545383,     23903958,     23333177,     22894495,     21623294,     21007496,     20500972, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     26366909,     25910863,     25619370,     23961501,     23393205,     22956790,     21670410,     21057623,     20553602, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     26305189,     25847441,     25554064,     23909829,     23339348,     22900911,     21627171,     21011875,     20505749, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     26397635,     25941336,     25649712,     23985266,     23417354,     22981247,     21689000,     21076991,     20573548, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     28387127,     19112237, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     28439488,     19161669, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     28407792,     19124818, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     28474952,     19183078, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     28415144,     19131044, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     28503858,     19205313, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     23316907,     23315282,     34541418,     23316532,     23249039,     13202492, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     23365650,     23363050,     34604972,     23364418,     23298424,     13236431, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     23333285,     23331773,     34566415,     23332975,     23265275,     13211215, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     23393673,     23391260,     34647877,     23392585,     23326200,     13251269, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     23339515,     23337857,     34574286,     23339099,     23271598,     13215701, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     23417928,     23415226,     34680939,     23416587,     23350605,     13267037, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    235005464,    235005504,    235005512,    235005464,    235004020,    235003976, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    235445304,    235445336,    235445344,    235445304,    235443880,    235443820, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    235176848,    235176884,    235176892,    235176848,    235175392,    235175340, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    235738564,    235738604,    235738608,    235738564,    235737132,    235737084, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    235235768,    235235808,    235235812,    235235768,    235234328,    235234284, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    235974416,    235974456,    235974460,    235974416,    235972996,    235972944, ],
  }),
  ("nof_tree_events",                 283511),
  ("nof_db_events",                   23488000),
  ("fsize_local",                     1304377803), # 1.30GB, avg file size 260.88MB
  ("fsize_db",                        1281254369472), # 1.28TB, avg file size 2.02GB
  ("use_it",                          False),
  ("xsection",                        377.85),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTToHadronic_ueUp"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTTo2L2Nu_TuneCP5CR1_QCDbased_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_QCDbased"),
  ("process_name_specific",           "TTTo2L2Nu_QCDbased"),
  ("nof_files",                       2),
  ("nof_db_files",                    353),
  ("nof_events",                      {
    'Count'                                                                          : [     14756000, ],
    'CountWeighted'                                                                  : [     14640943,     14640662,     14637298, ],
    'CountWeightedLHEWeightScale'                                                    : [     16491819,     16204382,     16020039,     14996915,     14640792,     14360853,     13569928,     13181384,     12862016, ],
    'CountWeightedLHEEnvelope'                                                       : [     17824857,     11990301, ],
    'CountWeightedPSWeight'                                                          : [     14637710,     14638075,     20847863,     14636998,     14613426,      9037427, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    147575340,    147572500,    147575524,    147575336,    147444288,    147441084, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     14648390,     14648389,     14648341, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     14678735,     14678693,     14678730, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     14658702,     14658691,     14658641, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     14696367,     14696337,     14696366, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     14662530,     14662515,     14662469, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     14711419,     14711392,     14711426, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     16506308,     16220695,     16038057,     15005473,     14647939,     14374156,     13574144,     13188621,     12871688, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     16542317,     16258039,     16076828,     15033839,     14678272,     14406213,     13596469,     13213297,     12898302, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     16517897,     16231839,     16048912,     15016287,     14658252,     14384050,     13584172,     13198099,     12880703, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     16562144,     16277107,     16095329,     15052397,     14695935,     14423114,     13613711,     13229529,     12913692, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     16523345,     16237244,     16054300,     15019924,     14662079,     14388028,     13586554,     13200798,     12883657, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     16581341,     16296131,     16114252,     15067218,     14710970,     14438359,     13625297,     13241590,     12926124, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     17834117,     12005882, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     17866954,     12036900, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     17847088,     12013788, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     17889215,     12050343, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     17851643,     12017656, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     17907254,     12064213, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     14648966,     14648679,     20857708,     14647677,     14625536,      9049445, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     14679548,     14678554,     20895107,     14677711,     14656762,      9073182, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     14659252,     14659041,     20872873,     14658032,     14635740,      9055391, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     14697141,     14696272,     20921134,     14695410,     14674222,      9083281, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     14663110,     14662815,     20877376,     14661814,     14639651,      9058530, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     14712256,     14711193,     20940554,     14710359,     14689448,      9094219, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    147637812,    147634996,    147637992,    147637808,    147507840,    147504684, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    147913000,    147910212,    147913164,    147912996,    147783804,    147780672, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    147745536,    147742688,    147745684,    147745520,    147615360,    147612184, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    148097412,    148094616,    148097564,    148097404,    147967860,    147964744, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    147781812,    147778968,    147781984,    147781808,    147651728,    147648572, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    148244308,    148241484,    148244472,    148244304,    148114904,    148111784, ],
  }),
  ("nof_tree_events",                 5604300),
  ("nof_db_events",                   14756000),
  ("fsize_local",                     23325733375), # 23.33GB, avg file size 11.66GB
  ("fsize_db",                        790811976585), # 790.81GB, avg file size 2.24GB
  ("use_it",                          False),
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_QCDbased"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTToSemiLeptonic_TuneCP5CR1_QCDbased_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_QCDbased"),
  ("process_name_specific",           "TTToSemiLeptonic_QCDbased"),
  ("nof_files",                       6),
  ("nof_db_files",                    647),
  ("nof_events",                      {
    'Count'                                                                          : [     26692000, ],
    'CountWeighted'                                                                  : [     26476045,     26475635,     26476385, ],
    'CountWeightedLHEWeightScale'                                                    : [     29831260,     29310177,     28975686,     27126574,     26476045,     25974524,     24545153,     23841765,     23263213, ],
    'CountWeightedLHEEnvelope'                                                       : [     32240140,     21688841, ],
    'CountWeightedPSWeight'                                                          : [     26475308,     26475762,     38577305,     26475284,     26405094,     15566017, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    266924478,    266924626,    266924634,    266924486,    266921688,    266921548, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     26496033,     26496026,     26496020, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     26551526,     26551533,     26551518, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     26514663,     26514646,     26514641, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     26583395,     26583367,     26583378, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     26521730,     26521730,     26521715, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     26610944,     26610940,     26610931, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     29858227,     29340396,     29009065,     27142712,     26496033,     25999250,     24553408,     23855394,     23281307, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     29924058,     29408724,     29079941,     27194680,     26551526,     26057885,     24594405,     23900582,     23329993, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     29879160,     29360569,     29028629,     27162283,     26514663,     26017112,     24571509,     23872482,     23297565, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     29959891,     29443161,     29113311,     27228209,     26583395,     26088388,     24625514,     23929886,     23357786, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     29889166,     29370527,     29038579,     27169007,     26521730,     26024475,     24575966,     23877498,     23303048, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     29994928,     29477913,     29147928,     27255328,     26610944,     26116303,     24646738,     23951984,     23380568, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     32257755,     21717519, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     32317987,     21774083, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     32281186,     21731787, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     32358194,     21798370, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     32289608,     21738908, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     32391185,     21823742, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     26496521,     26495739,     38597415,     26495381,     26427249,     15586618, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     26552518,     26550522,     38668450,     26550248,     26483991,     15627393, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     26515106,     26514444,     38625382,     26514045,     26445685,     15596872, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     26584294,     26582522,     38716451,     26582201,     26515528,     15644813, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     26522258,     26521439,     38634139,     26521037,     26452908,     15602271, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     26612009,     26609909,     38753291,     26609552,     26543338,     15663631, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    267066984,    267067116,    267067120,    267066984,    267064202,    267064038, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    267571074,    267571206,    267571210,    267571074,    267568328,    267568188, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    267261346,    267261494,    267261498,    267261350,    267258564,    267258412, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    267904098,    267904234,    267904238,    267904098,    267901344,    267901196, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    267329100,    267329236,    267329240,    267329104,    267326330,    267326182, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    268172958,    268173102,    268173106,    268172958,    268170214,    268170066, ],
  }),
  ("nof_tree_events",                 2517070),
  ("nof_db_events",                   26692000),
  ("fsize_local",                     11275360666), # 11.28GB, avg file size 1.88GB
  ("fsize_db",                        1447222516848), # 1.45TB, avg file size 2.24GB
  ("use_it",                          False),
  ("xsection",                        365.52),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTToSemiLeptonic_QCDbased"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTToHadronic_TuneCP5CR1_QCDbased_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_QCDbased"),
  ("process_name_specific",           "TTToHadronic_QCDbased"),
  ("nof_files",                       3),
  ("nof_db_files",                    704),
  ("nof_events",                      {
    'Count'                                                                          : [     25150000, ],
    'CountWeighted'                                                                  : [     24947966,     24944539,     24939692, ],
    'CountWeightedLHEWeightScale'                                                    : [     28108393,     27617036,     27301270,     25560271,     24947966,     24473976,     23128235,     22464995,     21919707, ],
    'CountWeightedLHEEnvelope'                                                       : [     30378339,     20435819, ],
    'CountWeightedPSWeight'                                                          : [     24947054,     24947703,     37103039,     24945055,     24856382,     13998458, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    251467148,    251467316,    251467316,    251467148,    251462888,    251462696, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     24965300,     24965478,     24965049, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     25017211,     25017368,     25017025, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     24982854,     24983028,     24982637, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     25047288,     25047421,     25047091, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     24989450,     24989583,     24989237, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     25073005,     25073145,     25072839, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     28133399,     27645066,     27332106,     25575129,     24965300,     24496783,     23135661,     22477503,     21936307, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     28195030,     27708917,     27398324,     25623733,     25017211,     24551548,     23173966,     22519709,     21981771, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     28153154,     27664107,     27350608,     25593591,     24982854,     24513645,     23152754,     22493629,     21951660, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     28228826,     27741451,     27429840,     25655364,     25047288,     24580362,     23203311,     22547381,     22008038, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     28162451,     27673329,     27359825,     25599786,     24989450,     24520467,     23156842,     22498268,     21956747, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     28261564,     27773908,     27462190,     25680668,     25073005,     24606437,     23223124,     22568018,     22029309, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     30394370,     20462567, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     30450534,     20515596, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     30416495,     20476032, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     30488494,     20538527, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     30424281,     20482658, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     30519293,     20562223, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     24966567,     24966075,     37122860,     24963558,     24877099,     14016370, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     25018851,     25017247,     37191580,     25014901,     24930323,     14052456, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     24984117,     24983740,     37149686,     24981176,     24894434,     14025640, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     25048874,     25047451,     37237630,     25045058,     24960002,     14068209, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     24990723,     24990202,     37158016,     24987649,     24901103,     14030381, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     25074729,     25073004,     37272951,     25070639,     24985924,     14084901, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    251634736,    251634896,    251634912,    251634736,    251630540,    251630352, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    252105640,    252105812,    252105812,    252105660,    252101468,    252101268, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    251818272,    251818448,    251818464,    251818280,    251814052,    251813872, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    252419592,    252419768,    252419776,    252419592,    252415416,    252415236, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    251880728,    251880904,    251880904,    251880744,    251876508,    251876324, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    252671176,    252671336,    252671352,    252671176,    252666976,    252666800, ],
  }),
  ("nof_tree_events",                 322654),
  ("nof_db_events",                   27350000),
  ("fsize_local",                     1493610675), # 1.49GB, avg file size 497.87MB
  ("fsize_db",                        1501472608417), # 1.50TB, avg file size 2.13GB
  ("use_it",                          False),
  ("xsection",                        377.85),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTToHadronic_QCDbased"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTTo2L2Nu_TuneCP5CR2_GluonMove_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_GluonMove"),
  ("process_name_specific",           "TTTo2L2Nu_GluonMove"),
  ("nof_files",                       2),
  ("nof_db_files",                    388),
  ("nof_events",                      {
    'Count'                                                                          : [     14958000, ],
    'CountWeighted'                                                                  : [     14838551,     14834774,     14833493, ],
    'CountWeightedLHEWeightScale'                                                    : [     16717884,     16425169,     16236812,     15201833,     14838357,     14554947,     13754849,     13360218,     13035687, ],
    'CountWeightedLHEEnvelope'                                                       : [     18067164,     12153708, ],
    'CountWeightedPSWeight'                                                          : [     14836442,     14837015,     20985732,     14836145,     14820104,      9285008, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    149542568,    149541108,    149542692,    149542568,    149460036,    149458324, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     14847769,     14847915,     14847574, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     14878769,     14878971,     14878575, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     14858184,     14858332,     14858021, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     14896610,     14896822,     14896428, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     14862138,     14862297,     14861988, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     14912027,     14912271,     14911814, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     16732900,     16441964,     16255380,     15210818,     14847313,     14568690,     13759429,     13367819,     13045728, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     16769721,     16480107,     16294910,     15239876,     14878316,     14601410,     13782358,     13393088,     13072924, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     16744625,     16453263,     16266333,     15221778,     14857738,     14578692,     13769568,     13377385,     13054844, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     16789765,     16499402,     16313614,     15258659,     14896138,     14618499,     13799773,     13409475,     13088488, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     16750216,     16458823,     16271870,     15225546,     14861684,     14582780,     13772060,     13380183,     13057892, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     16809387,     16518831,     16332938,     15273848,     14911572,     14634096,     13811675,     13421839,     13101229, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     18076900,     12169724, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     18110526,     12201369, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     18090028,     12177719, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     18133031,     12214962, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     18094732,     12181690, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     18151495,     12229152, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     14848180,     14848209,     20995715,     14847272,     14832269,      9297525, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     14879414,     14878885,     21033436,     14877979,     14863823,      9322066, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     14858583,     14858669,     21010987,     14857732,     14842631,      9303617, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     14897218,     14896781,     21059663,     14895876,     14881579,      9332411, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     14862560,     14862561,     21015637,     14861634,     14846705,      9306866, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     14912694,     14912056,     21079464,     14911197,     14897229,      9343716, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    149661964,    149660504,    149662072,    149661964,    149580076,    149578392, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    149943960,    149942496,    149944064,    149943960,    149862708,    149861040, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    149770800,    149769336,    149770900,    149770800,    149688776,    149687080, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    150130236,    150128772,    150130344,    150130236,    150048772,    150047088, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    149808528,    149807068,    149808656,    149808528,    149726548,    149724856, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    150280864,    150279404,    150280980,    150280864,    150199488,    150197804, ],
  }),
  ("nof_tree_events",                 5661883),
  ("nof_db_events",                   14958000),
  ("fsize_local",                     23473173194), # 23.47GB, avg file size 11.74GB
  ("fsize_db",                        795939500565), # 795.94GB, avg file size 2.05GB
  ("use_it",                          False),
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_GluonMove"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTToSemiLeptonic_TuneCP5CR2_GluonMove_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_GluonMove"),
  ("process_name_specific",           "TTToSemiLeptonic_GluonMove"),
  ("nof_files",                       6),
  ("nof_db_files",                    688),
  ("nof_events",                      {
    'Count'                                                                          : [     27500000, ],
    'CountWeighted'                                                                  : [     27277445,     27275138,     27277252, ],
    'CountWeightedLHEWeightScale'                                                    : [     30733643,     30197083,     29852548,     27947620,     27277445,     26760978,     25288566,     24563867,     23968011, ],
    'CountWeightedLHEEnvelope'                                                       : [     33216517,     22344526, ],
    'CountWeightedPSWeight'                                                          : [     27277864,     27278926,     39508012,     27275415,     27227290,     16246606, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    274989656,    274989846,    274989846,    274989648,    274988794,    274988608, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     27297733,     27297866,     27297577, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     27354519,     27354630,     27354420, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     27316962,     27317084,     27316788, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     27387433,     27387500,     27387313, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     27324237,     27324343,     27324063, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     27415765,     27415847,     27415669, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     30760996,     30227776,     29886488,     27963840,     27297733,     26786029,     25296657,     24577528,     23986250, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     30828453,     30297761,     29959105,     28016994,     27354519,     26846052,     25338525,     24623731,     24036049, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     30782601,     30248599,     29906695,     27984023,     27316962,     26804479,     25315354,     24595175,     24003043, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     30865432,     30333322,     29993563,     28051604,     27387433,     26877537,     25370627,     24653975,     24064755, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     30792886,     30258838,     29916914,     27990937,     27324237,     26812034,     25319905,     24600328,     24008657, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     30901486,     30369100,     30029188,     28079474,     27415765,     26906262,     25392436,     24676693,     24088168, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     33234106,     22373792, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     33295665,     22431830, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     33258304,     22388531, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     33337175,     22456901, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     33266949,     22395839, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     33371128,     22482980, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     27299307,     27299150,     39527791,     27295703,     27249675,     16267931, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     27356602,     27355247,     39599797,     27351835,     27307774,     16310326, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     27318480,     27318440,     39556495,     27314970,     27268747,     16278654, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     27389416,     27388244,     39649067,     27384827,     27340393,     16328547, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     27325824,     27325569,     39565474,     27322145,     27276269,     16284266, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     27417911,     27416307,     39686811,     27412979,     27369237,     16348151, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    275147806,    275147994,    275147994,    275147806,    275146964,    275146756, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    275663616,    275663812,    275663812,    275663616,    275662802,    275662612, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    275348304,    275348492,    275348492,    275348304,    275347456,    275347274, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    276007340,    276007528,    276007528,    276007340,    276006524,    276006328, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    275417708,    275417894,    275417894,    275417716,    275416872,    275416684, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    276283784,    276283970,    276283970,    276283784,    276282950,    276282756, ],
  }),
  ("nof_tree_events",                 2538384),
  ("nof_db_events",                   27500000),
  ("fsize_local",                     11299567535), # 11.30GB, avg file size 1.88GB
  ("fsize_db",                        1478792200960), # 1.48TB, avg file size 2.15GB
  ("use_it",                          False),
  ("xsection",                        365.52),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTToSemiLeptonic_GluonMove"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTToHadronic_TuneCP5CR2_GluonMove_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_GluonMove"),
  ("process_name_specific",           "TTToHadronic_GluonMove"),
  ("nof_files",                       3),
  ("nof_db_files",                    694),
  ("nof_events",                      {
    'Count'                                                                          : [     27388000, ],
    'CountWeighted'                                                                  : [     27166285,     27168252,     27158695, ],
    'CountWeightedLHEWeightScale'                                                    : [     30611040,     30075934,     29732196,     27835442,     27166285,     26652802,     25186612,     24464655,     23870864, ],
    'CountWeightedLHEEnvelope'                                                       : [     33084160,     22253872, ],
    'CountWeightedPSWeight'                                                          : [     27166310,     27163414,     40169351,     27167606,     27089732,     15444729, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    273877712,    273877872,    273877880,    273877728,    273876296,    273876136, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     27187917,     27187793,     27187929, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     27244546,     27244404,     27244624, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     27207017,     27206919,     27207025, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     27277242,     27277129,     27277333, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     27214283,     27214169,     27214300, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     27305422,     27305344,     27305508, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     30638425,     30106591,     29766005,     27851727,     27187917,     26677761,     25194771,     24478341,     23889031, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     30705689,     30176317,     29838299,     27904756,     27244546,     26737522,     25236558,     24524398,     23938609, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     30659908,     30127295,     29786115,     27871808,     27207017,     26696121,     25213384,     24495900,     23905740, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     30742486,     30211700,     29872565,     27939199,     27277242,     26768872,     25268503,     24554507,     23967184, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     30670149,     30137494,     29796269,     27878693,     27214283,     26703604,     25217916,     24501027,     23911319, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     30778371,     30247270,     29907968,     27966937,     27305422,     26797405,     25290223,     24577111,     23990464, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     33101762,     22283071, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     33163074,     22340904, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     33125809,     22297717, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     33204407,     22365851, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     33134432,     22304992, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     33238162,     22391779, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     27187781,     27183438,     40190488,     27187916,     27112270,     15464686, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     27244854,     27239177,     40264645,     27243892,     27170323,     15504686, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     27206857,     27202647,     40219581,     27207097,     27131219,     15474896, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     27277497,     27272040,     40314570,     27276717,     27202697,     15522037, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     27214153,     27209754,     40228764,     27214228,     27138639,     15480175, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     27305813,     27299992,     40353056,     27304714,     27231246,     15540534, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    274027984,    274028144,    274028144,    274027984,    274026576,    274026392, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    274541864,    274542024,    274542024,    274541864,    274540496,    274540312, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    274227816,    274227984,    274227984,    274227824,    274226440,    274226256, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    274884160,    274884344,    274884352,    274884168,    274882800,    274882632, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    274296632,    274296808,    274296816,    274296648,    274295224,    274295048, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    275159384,    275159552,    275159552,    275159384,    275158040,    275157864, ],
  }),
  ("nof_tree_events",                 338783),
  ("nof_db_events",                   27488000),
  ("fsize_local",                     1555314353), # 1.56GB, avg file size 518.44MB
  ("fsize_db",                        1495084288230), # 1.50TB, avg file size 2.15GB
  ("use_it",                          False),
  ("xsection",                        377.85),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTToHadronic_GluonMove"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_erdON"),
  ("process_name_specific",           "TTTo2L2Nu_erdON"),
  ("nof_files",                       1),
  ("nof_db_files",                    118),
  ("nof_events",                      {
    'Count'                                                                          : [      3738000, ],
    'CountWeighted'                                                                  : [      3707759,      3707680,      3707136, ],
    'CountWeightedLHEWeightScale'                                                    : [      4178183,      4105065,      4058144,      3799113,      3707740,      3637654,      3437438,      3338894,      3257846, ],
    'CountWeightedLHEEnvelope'                                                       : [      4515454,      3037319, ],
    'CountWeightedPSWeight'                                                          : [      3707797,      3707259,      5249316,      3707941,      3704871,      2316910, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     37379876,     37379400,     37379900,     37379876,     37357800,     37357276, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      3710691,      3710680,      3710700, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      3718413,      3718405,      3718414, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      3713298,      3713287,      3713308, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      3722871,      3722856,      3722877, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      3714278,      3714258,      3714283, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      3726697,      3726692,      3726700, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [      4181908,      4109248,      4062775,      3801319,      3710578,      3641058,      3438522,      3340747,      3260334, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [      4191066,      4118762,      4072647,      3808525,      3718300,      3649217,      3444206,      3347020,      3267095, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [      4184837,      4112069,      4065514,      3804057,      3713187,      3643566,      3441066,      3343142,      3262608, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [      4196083,      4123585,      4077323,      3813224,      3722757,      3653494,      3448564,      3351126,      3270990, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [      4186215,      4113449,      4066893,      3804971,      3714165,      3644576,      3441668,      3343832,      3263352, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [      4200953,      4128424,      4082139,      3816988,      3726584,      3657371,      3451501,      3354189,      3274145, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [      4517846,      3041298, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [      4526204,      3049188, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [      4521122,      3043295, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [      4531830,      3052592, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [      4522274,      3044280, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [      4536410,      3056117, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      3710716,      3709969,      5251696,      3710707,      3707884,      2320050, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      3718491,      3717556,      5261020,      3718338,      3715756,      2326185, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      3713316,      3712590,      5255528,      3713329,      3710473,      2321567, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      3722953,      3722047,      5267587,      3722818,      3720181,      2328765, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      3714295,      3713551,      5256625,      3714283,      3711444,      2322380, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      3726786,      3725846,      5272428,      3726619,      3724006,      2331589, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     37399900,     37399432,     37399924,     37399900,     37378048,     37377524, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     37469872,     37469408,     37469896,     37469872,     37448192,     37447680, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     37427208,     37426740,     37427232,     37427208,     37405312,     37404792, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     37516556,     37516096,     37516584,     37516556,     37494816,     37494304, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     37436432,     37435964,     37436460,     37436432,     37414560,     37414036, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     37553880,     37553416,     37553912,     37553880,     37532168,     37531648, ],
  }),
  ("nof_tree_events",                 1409152),
  ("nof_db_events",                   3738000),
  ("fsize_local",                     5852185358), # 5.85GB, avg file size 5.85GB
  ("fsize_db",                        199297633071), # 199.30GB, avg file size 1.69GB
  ("use_it",                          False),
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_erdON"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_erdON"),
  ("process_name_specific",           "TTTo2L2Nu_erdON_ext1"),
  ("nof_files",                       1),
  ("nof_db_files",                    264),
  ("nof_events",                      {
    'Count'                                                                          : [      9330000, ],
    'CountWeighted'                                                                  : [      9254487,      9253835,      9253097, ],
    'CountWeightedLHEWeightScale'                                                    : [     10428958,     10246712,     10129661,      9482938,      9253714,      9080083,      8580238,      8334313,      8132060, ],
    'CountWeightedLHEEnvelope'                                                       : [     11270687,      7582045, ],
    'CountWeightedPSWeight'                                                          : [      9255538,      9256027,     13101881,      9254659,      9243476,      5781691, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     93280696,     93279648,     93280744,     93280696,     93225504,     93224376, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      9262385,      9262296,      9262482, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      9281721,      9281620,      9281846, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      9268905,      9268805,      9268987, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      9292857,      9292763,      9292985, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      9271359,      9271260,      9271456, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      9302455,      9302355,      9302609, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     10438314,     10257175,     10141209,      9488533,      9262106,      9088631,      8583074,      8339030,      8138320, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     10461257,     10280977,     10165884,      9506634,      9281446,      9109034,      8597350,      8354776,      8155260, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     10445634,     10264246,     10148064,      9495361,      9268621,      9094877,      8589399,      8345009,      8144006, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     10473785,     10293026,     10177555,      9518359,      9292582,      9119704,      8608228,      8365011,      8164987, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     10449104,     10267686,     10151503,      9497683,      9271077,      9097433,      8590944,      8346756,      8145902, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     10485966,     10305123,     10189606,      9527799,      9302174,      9129446,      8615624,      8372729,      8172938, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     11276768,      7592006, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     11297743,      7611710, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     11284968,      7597000, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     11311793,      7620205, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     11287884,      7599465, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     11323296,      7629040, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      9262895,      9262967,     13108198,      9261666,      9251157,      5789480, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      9282378,      9282077,     13131831,      9280793,      9270955,      5804767, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      9269395,      9269491,     13117749,      9268193,      9257628,      5793283, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      9293497,      9293239,     13148213,      9291977,      9282034,      5811214, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      9271876,      9271907,     13120637,      9270623,      9260172,      5795304, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      9303145,      9302747,     13160568,      9301502,      9291810,      5818243, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     93350608,     93349552,     93350648,     93350608,     93295824,     93294688, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     93526072,     93525024,     93526104,     93526072,     93471696,     93470576, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     93418624,     93417560,     93418664,     93418624,     93363768,     93362624, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     93642552,     93641504,     93642592,     93642552,     93588032,     93586912, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     93442112,     93441064,     93442160,     93442112,     93387312,     93386176, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     93736464,     93735408,     93736496,     93736464,     93682000,     93680864, ],
  }),
  ("nof_tree_events",                 3518053),
  ("nof_db_events",                   9530000),
  ("fsize_local",                     14605184966), # 14.61GB, avg file size 14.61GB
  ("fsize_db",                        507664025011), # 507.66GB, avg file size 1.92GB
  ("use_it",                          False),
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_erdON_ext1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTToSemiLeptonic_TuneCP5_erdON_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_erdON"),
  ("process_name_specific",           "TTToSemiLeptonic_erdON"),
  ("nof_files",                       6),
  ("nof_db_files",                    717),
  ("nof_events",                      {
    'Count'                                                                          : [     25758000, ],
    'CountWeighted'                                                                  : [     25548509,     25548778,     25548072, ],
    'CountWeightedLHEWeightScale'                                                    : [     28789032,     28285767,     27962456,     26178406,     25548509,     25065905,     23686973,     23007854,     22449328, ],
    'CountWeightedLHEEnvelope'                                                       : [     31113344,     20930011, ],
    'CountWeightedPSWeight'                                                          : [     25549424,     25550614,     37038326,     25549863,     25502015,     15189462, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    257580700,    257580824,    257580824,    257580700,    257579360,    257579232, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     25569213,     25569294,     25569114, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     25622384,     25622503,     25622326, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     25587206,     25587293,     25587101, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     25653206,     25653295,     25653107, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     25594055,     25594137,     25593960, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     25679837,     25679930,     25679739, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     28814585,     28314483,     27994229,     26193579,     25569213,     25089406,     23694569,     23020685,     22466474, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     28877710,     28379979,     28062219,     26243349,     25622384,     25145651,     23733810,     23063997,     22513169, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     28834847,     28333995,     28013150,     26212487,     25587206,     25106665,     23712086,     23037204,     22482186, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     28912365,     28413308,     28094492,     26275784,     25653206,     25175131,     23763877,     23092311,     22540029, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     28844524,     28343628,     28022767,     26219003,     25594055,     25113792,     23716392,     23042070,     22487483, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     28946246,     28446896,     28127946,     26301980,     25679837,     25202101,     23784390,     23113674,     22562031, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     31129875,     20957369, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     31187585,     21011667, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     31152541,     20971172, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     31226465,     21035149, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     31160684,     20978055, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     31258365,     21059646, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     25569538,     25569566,     37056491,     25568930,     25522576,     15209389, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     25623188,     25622122,     37123639,     25621545,     25576611,     15249013, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     25587496,     25587625,     37083431,     25586992,     25540467,     15219416, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     25653926,     25653026,     37169877,     25652443,     25607199,     15266048, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     25594407,     25594380,     37091824,     25593764,     25547449,     15224699, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     25680663,     25679454,     37205208,     25678913,     25634081,     15284449, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    257718193,    257718325,    257718325,    257718197,    257716885,    257716761, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    258201589,    258201713,    258201713,    258201593,    258200286,    258200154, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    257906228,    257906364,    257906364,    257906228,    257904912,    257904784, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    258523229,    258523365,    258523365,    258523229,    258521931,    258521803, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    257971817,    257971949,    257971949,    257971817,    257970509,    257970373, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    258783378,    258783498,    258783498,    258783386,    258782064,    258781936, ],
  }),
  ("nof_tree_events",                 2322154),
  ("nof_db_events",                   26290000),
  ("fsize_local",                     10350652700), # 10.35GB, avg file size 1.73GB
  ("fsize_db",                        1416312432622), # 1.42TB, avg file size 1.98GB
  ("use_it",                          False),
  ("xsection",                        365.52),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTToSemiLeptonic_erdON"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTToHadronic_TuneCP5_erdON_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_erdON"),
  ("process_name_specific",           "TTToHadronic_erdON"),
  ("nof_files",                       3),
  ("nof_db_files",                    799),
  ("nof_events",                      {
    'Count'                                                                          : [     22442000, ],
    'CountWeighted'                                                                  : [     22261891,     22256734,     22251290, ],
    'CountWeightedLHEWeightScale'                                                    : [     25082805,     24644905,     24363652,     22807825,     22261891,     21839517,     20636780,     20045404,     19559327, ],
    'CountWeightedLHEEnvelope'                                                       : [     27107503,     18235868, ],
    'CountWeightedPSWeight'                                                          : [     22259786,     22261810,     32947230,     22260880,     22192989,     12628549, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    224354774,    224354934,    224354942,    224354768,    224352526,    224352366, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     22277512,     22277458,     22277552, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     22323952,     22323823,     22324101, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     22293168,     22293127,     22293218, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     22350760,     22350645,     22350900, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     22299124,     22299036,     22299182, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     22373867,     22373698,     22373993, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     25105170,     24669967,     24391357,     22821166,     22277512,     21860027,     20643528,     20056694,     19574305, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     25160255,     24727085,     24450588,     22864633,     22323952,     21909054,     20677797,     20094509,     19615038, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     25122788,     24686954,     24407839,     22837637,     22293168,     21875065,     20658775,     20071070,     19587998, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     25190415,     24756084,     24478713,     22892859,     22350760,     21934749,     20703981,     20119152,     19638434, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     25131144,     24695269,     24416119,     22843259,     22299124,     21881224,     20662469,     20075274,     19592569, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     25219751,     24785196,     24507679,     22915577,     22373867,     21958120,     20721763,     20137687,     19657527, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     27121946,     18259823, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     27172241,     18307229, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     27141685,     18271828, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     27206106,     18327660, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     27148701,     18277765, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     27233743,     18348897, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     22277343,     22278198,     32964529,     22277515,     22211441,     12644935, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     22324146,     22323884,     33025336,     22323418,     22258952,     12677692, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     22292987,     22293966,     32988396,     22293232,     22226942,     12653269, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     22350912,     22350857,     33066285,     22350321,     22285473,     12691866, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     22298951,     22299781,     32995867,     22299076,     22232973,     12657592, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     22374110,     22373728,     33097787,     22373243,     22308781,     12707011, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    224541456,    224541624,    224541624,    224541456,    224539258,    224539074, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    224963100,    224963276,    224963276,    224963100,    224960912,    224960744, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    224705134,    224705294,    224705302,    224705128,    224702904,    224702744, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    225243354,    225243522,    225243530,    225243340,    225241136,    225240976, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    224761436,    224761604,    224761604,    224761422,    224759198,    224759022, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    225468516,    225468692,    225468692,    225468520,    225466320,    225466152, ],
  }),
  ("nof_tree_events",                 267466),
  ("nof_db_events",                   27486000),
  ("fsize_local",                     1229399117), # 1.23GB, avg file size 409.80MB
  ("fsize_db",                        1499579994365), # 1.50TB, avg file size 1.88GB
  ("use_it",                          False),
  ("xsection",                        377.85),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTToHadronic_erdON"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTTo2L2Nu_mtop166p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop166p5"),
  ("process_name_specific",           "TTTo2L2Nu_mtop166p5"),
  ("nof_files",                       1),
  ("nof_db_files",                    76),
  ("nof_events",                      {
    'Count'                                                                          : [      2500000, ],
    'CountWeighted'                                                                  : [      2478827,      2478997,      2478845, ],
    'CountWeightedLHEWeightScale'                                                    : [      2794275,      2746959,      2717218,      2537847,      2478827,      2434148,      2293985,      2230682,      2178687, ],
    'CountWeightedLHEEnvelope'                                                       : [      3020424,      2030657, ],
    'CountWeightedPSWeight'                                                          : [      2479135,      2479543,      3504077,      2478913,      2475521,      1553167, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     25002736,     25002692,     25002780,     25002736,     24995856,     24995728, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      2485320,      2485339,      2485283, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      2494695,      2494710,      2494666, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      2486745,      2486765,      2486709, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      2497085,      2497092,      2497052, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      2488337,      2488351,      2488298, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      2501548,      2501569,      2501515, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [      2801677,      2754572,      2725068,      2543790,      2485320,      2440706,      2298770,      2235845,      2184174, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [      2812563,      2765606,      2736287,      2552933,      2494695,      2450293,      2306470,      2243841,      2192407, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [      2803277,      2756113,      2726557,      2545297,      2486745,      2442073,      2300163,      2237166,      2185423, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [      2815234,      2768168,      2738760,      2555456,      2497085,      2452566,      2308820,      2246044,      2194486, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [      2805263,      2758086,      2728525,      2546860,      2488337,      2443672,      2301423,      2238461,      2186748, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [      2820653,      2773535,      2744105,      2559908,      2501548,      2457051,      2312517,      2249797,      2198278, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [      3027383,      2036830, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [      3038163,      2045514, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [      3029188,      2037914, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [      3041186,      2047305, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [      3031096,      2039351, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [      3046560,      2051248, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      2485444,      2485709,      3511842,      2485135,      2481912,      1558011, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      2494860,      2494992,      3524029,      2494449,      2491399,      1564770, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      2486869,      2487152,      3513952,      2486565,      2483320,      1558828, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      2497236,      2497402,      3527560,      2496844,      2493743,      1566123, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      2488461,      2488727,      3516008,      2488151,      2484909,      1559970, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      2501713,      2501851,      3533488,      2501304,      2498222,      1569233, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     25057224,     25057180,     25057266,     25057224,     25050416,     25050286, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     25146476,     25146430,     25146516,     25146474,     25139718,     25139594, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     25072300,     25072256,     25072340,     25072300,     25065476,     25065350, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     25171656,     25171616,     25171700,     25171656,     25164880,     25164754, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     25087936,     25087892,     25087978,     25087936,     25081118,     25080992, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     25215950,     25215910,     25215994,     25215950,     25209176,     25209050, ],
  }),
  ("nof_tree_events",                 929529),
  ("nof_db_events",                   2500000),
  ("fsize_local",                     3803224792), # 3.80GB, avg file size 3.80GB
  ("fsize_db",                        132230601699), # 132.23GB, avg file size 1.74GB
  ("use_it",                          False),
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_mtop166p5"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTToSemiLeptonic_mtop166p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop166p5"),
  ("process_name_specific",           "TTToSemiLeptonic_mtop166p5"),
  ("nof_files",                       1),
  ("nof_db_files",                    254),
  ("nof_events",                      {
    'Count'                                                                          : [      9767000, ],
    'CountWeighted'                                                                  : [      9687413,      9684322,      9685045, ],
    'CountWeightedLHEWeightScale'                                                    : [     10919511,     10733398,     10616159,      9916204,      9687369,      9509539,      8962604,      8714662,      8511045, ],
    'CountWeightedLHEEnvelope'                                                       : [     11800941,      7934651, ],
    'CountWeightedPSWeight'                                                          : [      9685496,      9686681,     14020142,      9685902,      9665802,      5773865, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     97674400,     97674432,     97674432,     97674400,     97674224,     97674192, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      9710323,      9710341,      9710265, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      9747124,      9747143,      9747074, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      9715854,      9715875,      9715796, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      9756353,      9756387,      9756322, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      9722084,      9722110,      9722034, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      9773856,      9773883,      9773800, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     10948540,     10763332,     10647065,      9939549,      9710025,      9535360,      8981428,      8735057,      8532703, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     10991143,     10806585,     10691093,      9975398,      9746817,      9573008,      9011663,      8766445,      8565029, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     10954749,     10769314,     10652844,      9945391,      9715562,      9540644,      8986860,      8740152,      8537525, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     11001540,     10816526,     10700684,      9985186,      9756062,      9581828,      9020774,      8774969,      8573075, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     10962514,     10777007,     10660513,      9951546,      9721789,      9546931,      8991791,      8745234,      8542735, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     11022727,     10837527,     10721585,     10002621,      9773555,      9599365,      9035270,      8789678,      8587935, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     11828343,      7958910, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     11870612,      7992926, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     11835342,      7963107, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     11882350,      7999869, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     11842837,      7968710, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     11903442,      8015268, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      9710310,      9711080,     14052063,      9710300,      9690851,      5791653, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      9747276,      9747614,     14101622,      9746856,      9727976,      5816598, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      9715836,      9716645,     14060374,      9715850,      9696319,      5794703, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      9756488,      9756919,     14115555,      9756141,      9737100,      5821629, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      9722079,      9722831,     14068736,      9722040,      9702563,      5798913, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      9774034,      9774342,     14139515,      9773551,      9754641,      5833114, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     97896840,     97896872,     97896872,     97896848,     97896656,     97896632, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     98248072,     98248104,     98248104,     98248080,     98247896,     98247872, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     97954984,     97955000,     97955000,     97954984,     97954808,     97954784, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     98345328,     98345344,     98345344,     98345328,     98345168,     98345136, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     98016040,     98016072,     98016072,     98016048,     98015872,     98015848, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     98517960,     98517992,     98517992,     98517960,     98517784,     98517752, ],
  }),
  ("nof_tree_events",                 883914),
  ("nof_db_events",                   9767000),
  ("fsize_local",                     3874343654), # 3.87GB, avg file size 3.87GB
  ("fsize_db",                        521600331561), # 521.60GB, avg file size 2.05GB
  ("use_it",                          False),
  ("xsection",                        365.52),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTToSemiLeptonic_mtop166p5"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTToHadronic_mtop166p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop166p5"),
  ("process_name_specific",           "TTToHadronic_mtop166p5"),
  ("nof_files",                       1),
  ("nof_db_files",                    250),
  ("nof_events",                      {
    'Count'                                                                          : [      9534000, ],
    'CountWeighted'                                                                  : [      9456343,      9452821,      9453493, ],
    'CountWeightedLHEWeightScale'                                                    : [     10658002,     10477493,     10364200,      9678931,      9456343,      9283558,      8748315,      8506954,      8308716, ],
    'CountWeightedLHEEnvelope'                                                       : [     11519501,      7745244, ],
    'CountWeightedPSWeight'                                                          : [      9454623,      9456103,     13975703,      9455032,      9427450,      5379708, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     95329952,     95330032,     95330032,     95329952,     95329784,     95329704, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      9478777,      9478763,      9478723, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      9514636,      9514616,      9514635, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      9484187,      9484166,      9484122, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      9523657,      9523643,      9523652, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      9490238,      9490222,      9490198, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      9540688,      9540668,      9540681, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     10686365,     10506708,     10394336,      9701704,      9478777,      9308681,      8766627,      8526776,      8329771, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     10727998,     10548921,     10437286,      9736661,      9514636,      9345375,      8796075,      8557319,      8361236, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     10692427,     10512532,     10399965,      9707400,      9484187,      9313853,      8771921,      8531748,      8334488, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     10738114,     10558617,     10446641,      9746210,      9523657,      9353970,      8804979,      8565654,      8369101, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     10699988,     10520042,     10407468,      9713368,      9490238,      9319974,      8776714,      8536696,      8339546, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     10758757,     10579098,     10467037,      9763176,      9540688,      9371071,      8819071,      8579954,      8383564, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     11546259,      7768849, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     11587548,      7801966, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     11553091,      7772948, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     11598989,      7808750, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     11560396,      7778408, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     11619547,      7823740, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      9478768,      9479813,     14007864,      9478791,      9452041,      5396165, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      9514795,      9515392,     14057632,      9514431,      9488420,      5419282, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      9484159,      9485257,     14016134,      9484207,      9457383,      5399007, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      9523783,      9524461,     14071488,      9523489,      9497312,      5423990, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      9490233,      9491253,     14024520,      9490229,      9463520,      5402910, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      9540874,      9541398,     14095497,      9540441,      9514536,      5434635, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     95560640,     95560720,     95560720,     95560648,     95560472,     95560400, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     95903056,     95903136,     95903136,     95903056,     95902880,     95902800, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     95617448,     95617536,     95617536,     95617464,     95617296,     95617192, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     95997760,     95997848,     95997848,     95997760,     95997608,     95997520, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     95676760,     95676832,     95676832,     95676760,     95676584,     95676512, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     96165792,     96165872,     96165872,     96165792,     96165632,     96165544, ],
  }),
  ("nof_tree_events",                 115193),
  ("nof_db_events",                   9734000),
  ("fsize_local",                     520505303), # 520.51MB, avg file size 520.51MB
  ("fsize_db",                        526069586840), # 526.07GB, avg file size 2.10GB
  ("use_it",                          False),
  ("xsection",                        377.85),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTToHadronic_mtop166p5"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTTo2L2Nu_mtop169p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop169p5"),
  ("process_name_specific",           "TTTo2L2Nu_mtop169p5"),
  ("nof_files",                       1),
  ("nof_db_files",                    53),
  ("nof_events",                      {
    'Count'                                                                          : [      2490000, ],
    'CountWeighted'                                                                  : [      2469074,      2468788,      2468867, ],
    'CountWeightedLHEWeightScale'                                                    : [      2782949,      2734834,      2704309,      2529088,      2468950,      2423485,      2287277,      2222859,      2169901, ],
    'CountWeightedLHEEnvelope'                                                       : [      3007441,      2023195, ],
    'CountWeightedPSWeight'                                                          : [      2469531,      2470148,      3492236,      2468867,      2465156,      1545009, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     24903108,     24902932,     24903134,     24903108,     24893324,     24893100, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      2473369,      2473404,      2473320, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      2480612,      2480645,      2480580, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      2474935,      2474976,      2474892, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      2483273,      2483304,      2483239, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      2476059,      2476097,      2476008, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      2486775,      2486808,      2486732, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [      2787856,      2740026,      2709777,      2532785,      2473292,      2427905,      2290031,      2226066,      2173483, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [      2796316,      2748686,      2718662,      2539738,      2480538,      2435408,      2295764,      2232147,      2179850, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [      2789623,      2741718,      2711424,      2534440,      2474861,      2429410,      2291560,      2227514,      2174856, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [      2799302,      2751557,      2721435,      2542546,      2483198,      2437955,      2298370,      2234599,      2182170, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [      2791076,      2743166,      2712862,      2535526,      2475983,      2430548,      2292389,      2228382,      2175770, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [      2803623,      2755847,      2725708,      2546018,      2486699,      2441482,      2301188,      2237484,      2185110, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [      3011726,      2027583, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [      3019888,      2034521, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [      3013708,      2028783, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [      3023256,      2036534, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [      3015049,      2029826, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [      3027467,      2039662, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      2473658,      2474179,      3496931,      2472913,      2469293,      1548445, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      2480938,      2481375,      3506135,      2480114,      2476600,      1553834, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      2475226,      2475750,      3499244,      2474483,      2470866,      1549358, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      2483593,      2484044,      3510068,      2482780,      2479253,      1555368, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      2476341,      2476860,      3500659,      2475599,      2471998,      1550191, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      2487094,      2487526,      3514666,      2486268,      2482779,      1557844, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     24935336,     24935164,     24935362,     24935336,     24925656,     24925432, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     25003310,     25003140,     25003336,     25003310,     24993706,     24993484, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     24951844,     24951672,     24951872,     24951844,     24942148,     24941924, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     25031214,     25031040,     25031238,     25031214,     25021582,     25021360, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     24962666,     24962494,     24962690,     24962666,     24952972,     24952752, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     25065516,     25065346,     25065542,     25065516,     25055896,     25055676, ],
  }),
  ("nof_tree_events",                 932589),
  ("nof_db_events",                   2490000),
  ("fsize_local",                     3842025176), # 3.84GB, avg file size 3.84GB
  ("fsize_db",                        132076601731), # 132.08GB, avg file size 2.49GB
  ("use_it",                          False),
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_mtop169p5"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTTo2L2Nu_mtop169p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop169p5"),
  ("process_name_specific",           "TTTo2L2Nu_mtop169p5_ext1"),
  ("nof_files",                       2),
  ("nof_db_files",                    253),
  ("nof_events",                      {
    'Count'                                                                          : [      9550000, ],
    'CountWeighted'                                                                  : [      9471098,      9470970,      9471887, ],
    'CountWeightedLHEWeightScale'                                                    : [     10675723,     10491010,     10373442,      9701162,      9470262,      9295431,      8772934,      8525598,      8322311, ],
    'CountWeightedLHEEnvelope'                                                       : [     11536977,      7759391, ],
    'CountWeightedPSWeight'                                                          : [      9471620,      9470222,     13396011,      9471341,      9460143,      5926147, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     95515144,     95514604,     95515220,     95515144,     95477540,     95476852, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      9487185,      9487241,      9487114, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      9514986,      9515052,      9514914, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      9493230,      9493285,      9493163, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      9525225,      9525290,      9525148, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      9497528,      9497594,      9497463, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      9538681,      9538754,      9538613, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     10694591,     10510916,     10394375,      9715359,      9486890,      9312368,      8783523,      8537908,      8336035, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     10727075,     10544144,     10428448,      9742072,      9514700,      9341156,      8805552,      8561243,      8360464, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     10701392,     10517452,     10400718,      9721718,      9492937,      9318166,      8789422,      8543463,      8341313, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     10738582,     10555192,     10439129,      9752866,      9524935,      9350941,      8815589,      8570682,      8369393, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     10706966,     10522988,     10406234,      9725925,      9497237,      9322540,      8792621,      8546848,      8344831, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     10755194,     10571649,     10455510,      9766230,      9538390,      9364489,      8826462,      8581806,      8380706, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     11553419,      7776251, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     11584760,      7802875, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     11561052,      7780865, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     11597713,      7810638, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     11566212,      7784866, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     11613911,      7822670, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      9487472,      9485644,     13414112,      9486766,      9476168,      5939307, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      9515456,      9513211,     13449504,      9514335,      9504328,      5959976, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      9493501,      9491701,     13422985,      9492835,      9482174,      5942819, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      9525669,      9523482,     13464603,      9524609,      9514486,      5965862, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      9497832,      9495956,     13428449,      9497099,      9486562,      5946031, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      9539185,      9536853,     13482313,      9537999,      9528116,      5975386, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     95635972,     95635424,     95636048,     95635964,     95598724,     95598044, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     95896944,     95896388,     95897016,     95896944,     95859952,     95859256, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     95699280,     95698748,     95699364,     95699280,     95661980,     95661300, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     96004164,     96003636,     96004236,     96004164,     95967072,     95966380, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     95741276,     95740756,     95741348,     95741276,     95704012,     95703320, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     96136720,     96136180,     96136796,     96136720,     96099648,     96098968, ],
  }),
  ("nof_tree_events",                 3575659),
  ("nof_db_events",                   9550000),
  ("fsize_local",                     14725618395), # 14.73GB, avg file size 7.36GB
  ("fsize_db",                        506299241179), # 506.30GB, avg file size 2.00GB
  ("use_it",                          False),
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_mtop169p5_ext1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTToSemiLeptonic_mtop169p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop169p5"),
  ("process_name_specific",           "TTToSemiLeptonic_mtop169p5"),
  ("nof_files",                       2),
  ("nof_db_files",                    520),
  ("nof_events",                      {
    'Count'                                                                          : [     18797000, ],
    'CountWeighted'                                                                  : [     18642541,     18642588,     18642633, ],
    'CountWeightedLHEWeightScale'                                                    : [     21011492,     20649173,     20418763,     19093639,     18642541,     18296903,     17267104,     16781003,     16381382, ],
    'CountWeightedLHEEnvelope'                                                       : [     22708347,     15271880, ],
    'CountWeightedPSWeight'                                                          : [     18642227,     18640843,     27002782,     18643029,     18610147,     11101437, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    187965168,    187965280,    187965280,    187965168,    187964760,    187964656, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     18673483,     18673634,     18673310, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     18728260,     18728406,     18728117, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     18685362,     18685500,     18685189, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     18748373,     18748500,     18748210, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     18693798,     18693907,     18693616, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     18774728,     18774873,     18774575, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     21048762,     20688433,     20460034,     19121641,     18673483,     18330264,     17287986,     16805269,     16408410, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     21112764,     20753883,     20527128,     19174252,     18728260,     18386930,     17331320,     16851179,     16456453, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     21062098,     20701268,     20472489,     19134133,     18685362,     18341648,     17299565,     16816189,     16418781, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     21135383,     20775585,     20548106,     19195457,     18748373,     18406154,     17351052,     16869718,     16474001, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     21073014,     20712103,     20483291,     19142327,     18693798,     18350182,     17305790,     16822776,     16425637, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     21167929,     20807845,     20580239,     19221598,     18774728,     18432697,     17372297,     16891493,     16496147, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     22740757,     15305167, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     22802415,     15357640, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     22755732,     15314226, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     22827865,     15372869, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     22765805,     15322055, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     22859584,     15396466, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     18673384,     18671194,     27040283,     18673507,     18641951,     11125802, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     18728444,     18725456,     27112611,     18727857,     18697519,     11164211, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     18685248,     18683121,     27058088,     18685402,     18653714,     11132379, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     18748502,     18745673,     27142863,     18748047,     18717431,     11175257, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     18693705,     18691470,     27069167,     18693753,     18662223,     11138290, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     18774959,     18771943,     27178674,     18774273,     18744034,     11192874, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    188237832,    188237912,    188237912,    188237832,    188237408,    188237312, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    188751536,    188751624,    188751624,    188751536,    188751128,    188751008, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    188362232,    188362320,    188362320,    188362232,    188361824,    188361728, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    188962304,    188962384,    188962384,    188962304,    188961896,    188961784, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    188444216,    188444304,    188444304,    188444208,    188443808,    188443704, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    189221360,    189221456,    189221456,    189221360,    189220944,    189220872, ],
  }),
  ("nof_tree_events",                 1705041),
  ("nof_db_events",                   18896000),
  ("fsize_local",                     7525899379), # 7.53GB, avg file size 3.76GB
  ("fsize_db",                        1012550848073), # 1.01TB, avg file size 1.95GB
  ("use_it",                          False),
  ("xsection",                        365.52),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTToSemiLeptonic_mtop169p5"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTToSemiLeptonic_mtop169p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop169p5"),
  ("process_name_specific",           "TTToSemiLeptonic_mtop169p5_ext1"),
  ("nof_files",                       1),
  ("nof_db_files",                    280),
  ("nof_events",                      {
    'Count'                                                                          : [      9108000, ],
    'CountWeighted'                                                                  : [      9033886,      9029454,      9033252, ],
    'CountWeightedLHEWeightScale'                                                    : [     10182337,     10006395,      9894438,      9252367,      9033886,      8865880,      8366978,      8131253,      7937501, ],
    'CountWeightedLHEEnvelope'                                                       : [     11003179,      7401256, ],
    'CountWeightedPSWeight'                                                          : [      9034004,      9034494,     13084288,      9033178,      9015758,      5379624, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     91091896,     91091952,     91091952,     91091888,     91091672,     91091616, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      9048682,      9048689,      9048657, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      9075346,      9075345,      9075337, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      9054441,      9054442,      9054401, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      9085089,      9085074,      9085076, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      9058533,      9058517,      9058516, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      9097909,      9097869,      9097913, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     10200494,     10025520,      9914551,      9266075,      9048682,      8882176,      8377248,      8143167,      7950739, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     10231617,     10057351,      9947160,      9291707,      9075346,      8909758,      8398409,      8165564,      7974151, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     10206976,     10031748,      9920574,      9272123,      9054441,      8887680,      8382858,      8148453,      7955748, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     10242582,     10067868,      9957320,      9301978,      9085089,      8919056,      8407942,      8174527,      7982638, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     10212269,     10037012,      9925815,      9276127,      9058533,      8891836,      8385898,      8151663,      7959086, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     10258399,     10083542,      9972917,      9314696,      9097909,      8931953,      8418302,      8185120,      7993400, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     11019030,      7417468, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     11049051,      7442989, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     11026282,      7421868, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     11061369,      7450374, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     11031169,      7425675, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     11076774,      7461847, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      9049231,      9049410,     13102678,      9048057,      9031248,      5391505, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      9076030,      9075855,     13137897,      9074520,      9058272,      5410200, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      9054980,      9055165,     13111284,      9053810,      9036958,      5394693, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      9085746,      9085623,     13152533,      9084284,      9067934,      5415551, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      9059076,      9059177,     13116637,      9057889,      9041118,      5397590, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      9098602,      9098326,     13169889,      9097052,      9080900,      5424145, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     91211344,     91211400,     91211400,     91211344,     91211128,     91211072, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     91461512,     91461568,     91461568,     91461512,     91461304,     91461248, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     91271608,     91271664,     91271664,     91271608,     91271384,     91271344, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     91563592,     91563624,     91563624,     91563592,     91563360,     91563312, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     91311344,     91311392,     91311392,     91311344,     91311128,     91311080, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     91689632,     91689672,     91689672,     91689632,     91689408,     91689368, ],
  }),
  ("nof_tree_events",                 826706),
  ("nof_db_events",                   9808000),
  ("fsize_local",                     3650560450), # 3.65GB, avg file size 3.65GB
  ("fsize_db",                        525576169428), # 525.58GB, avg file size 1.88GB
  ("use_it",                          False),
  ("xsection",                        365.52),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTToSemiLeptonic_mtop169p5_ext1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTToHadronic_mtop169p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop169p5"),
  ("process_name_specific",           "TTToHadronic_mtop169p5"),
  ("nof_files",                       2),
  ("nof_db_files",                    538),
  ("nof_events",                      {
    'Count'                                                                          : [     19032000, ],
    'CountWeighted'                                                                  : [     18875725,     18874491,     18872709, ],
    'CountWeightedLHEWeightScale'                                                    : [     21274185,     20905632,     20670750,     19332995,     18875667,     18523652,     17483890,     16990485,     16584964, ],
    'CountWeightedLHEEnvelope'                                                       : [     22991342,     15462010, ],
    'CountWeightedPSWeight'                                                          : [     18874035,     18875315,     27911949,     18876192,     18819043,     10727346, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    190276304,    190276392,    190276400,    190276304,    190275752,    190275648, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     18906416,     18906376,     18906376, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     18962035,     18961952,     18962085, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     18918398,     18918384,     18918360, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     18982345,     18982307,     18982369, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     18926905,     18926879,     18926899, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     19009016,     19008956,     19009072, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     21312190,     20945630,     20712754,     19361591,     18905831,     18557590,     17505208,     17015220,     16612442, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     21377242,     21012121,     20780824,     19415060,     18961448,     18615128,     17549283,     17061867,     16661234, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     21325667,     20958602,     20725326,     19374202,     18917828,     18569078,     17516918,     17026256,     16622924, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     21400081,     21034042,     20802055,     19436503,     18981770,     18634530,     17569211,     17080590,     16678954, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     21336690,     20969562,     20736273,     19382486,     18926318,     18577746,     17523223,     17032906,     16629884, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     21433002,     21066686,     20834580,     19462935,     19008433,     18661419,     17590721,     17102640,     16701416, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     23024324,     15495918, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     23086940,     15549256, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     23039453,     15505085, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     23112668,     15564631, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     23049655,     15512992, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     23144754,     15588523, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     18905770,     18906307,     27951579,     18907186,     18851236,     10750721, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     18961707,     18961474,     28027123,     18962384,     18907478,     10787669, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     18917757,     18918326,     27969877,     18919217,     18863140,     10757089, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     18981975,     18981876,     28058225,     18982772,     18927618,     10798358, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     18926288,     18926789,     27981355,     18927666,     18871676,     10762769, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     19008743,     19008465,     28095354,     19009351,     18954377,     10815315, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    190593000,    190593080,    190593088,    190593000,    190592440,    190592336, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    191114600,    191114680,    191114688,    191114600,    191114024,    191113928, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    190718800,    190718848,    190718872,    190718800,    190718232,    190718128, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    191327344,    191327424,    191327440,    191327344,    191326784,    191326688, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    190801776,    190801856,    190801864,    190801776,    190801224,    190801136, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    191590240,    191590320,    191590328,    191590240,    191589664,    191589568, ],
  }),
  ("nof_tree_events",                 230280),
  ("nof_db_events",                   19232000),
  ("fsize_local",                     1047591589), # 1.05GB, avg file size 523.80MB
  ("fsize_db",                        1043078618010), # 1.04TB, avg file size 1.94GB
  ("use_it",                          False),
  ("xsection",                        377.85),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTToHadronic_mtop169p5"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTTo2L2Nu_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop171p5"),
  ("process_name_specific",           "TTTo2L2Nu_mtop171p5"),
  ("nof_files",                       1),
  ("nof_db_files",                    169),
  ("nof_events",                      {
    'Count'                                                                          : [      5496000, ],
    'CountWeighted'                                                                  : [      5450640,      5451807,      5450527, ],
    'CountWeightedLHEWeightScale'                                                    : [      6143519,      6036898,      5968875,      5584790,      5450548,      5349375,      5052101,      4908288,      4790073, ],
    'CountWeightedLHEEnvelope'                                                       : [      6638903,      4466404, ],
    'CountWeightedPSWeight'                                                          : [      5451593,      5450818,      7713765,      5451615,      5445382,      3408557, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     54955400,     54954972,     54955432,     54955400,     54928168,     54927676, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      5457395,      5457423,      5457353, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      5470282,      5470313,      5470250, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      5461107,      5461129,      5461061, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      5476613,      5476652,      5476588, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      5462880,      5462908,      5462841, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      5482923,      5482963,      5482888, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [      6150784,      6044807,      5977421,      5589661,      5457228,      5355956,      5055198,      4912465,      4795123, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [      6165989,      6060493,      5993617,      5601848,      5470113,      5369458,      5064982,      4923072,      4806428, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [      6154949,      6048841,      5981317,      5593569,      5460940,      5359521,      5058818,      4915884,      4798374, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [      6173096,      6067343,      6000246,      5608518,      5476446,      5375517,      5071166,      4928908,      4811960, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [      6157345,      6051227,      5983716,      5595249,      5462713,      5361344,      5060011,      4917191,      4799783, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [      6181020,      6075220,      6008095,      5614726,      5482754,      5381915,      5076114,      4934024,      4817213, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [      6644372,      4473553, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [      6658539,      4486404, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [      6649046,      4476404, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [      6666543,      4491225, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [      6651151,      4478120, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [      6674113,      4496965, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      5457494,      5456475,      7719594,      5457310,      5451359,      3414134, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      5470462,      5469235,      7735527,      5470085,      5464413,      3424087, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      5461196,      5460199,      7725042,      5461029,      5455051,      3416288, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      5476785,      5475596,      7744871,      5476435,      5470698,      3427738, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      5462972,      5461959,      7727195,      5462802,      5456837,      3417690, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      5483117,      5481876,      7753028,      5482722,      5477055,      3432304, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     55005584,     55005160,     55005612,     55005584,     54978584,     54978092, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     55124272,     55123848,     55124304,     55124268,     55097456,     55096976, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     55044488,     55044064,     55044524,     55044488,     55017444,     55016956, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     55190480,     55190056,     55190508,     55190480,     55163592,     55163104, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     55061508,     55061080,     55061536,     55061504,     55034476,     55033984, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     55252356,     55251932,     55252384,     55252356,     55225488,     55225000, ],
  }),
  ("nof_tree_events",                 2065629),
  ("nof_db_events",                   5896000),
  ("fsize_local",                     8543891825), # 8.54GB, avg file size 8.54GB
  ("fsize_db",                        313467865129), # 313.47GB, avg file size 1.85GB
  ("use_it",                          False),
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_mtop171p5"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTToSemiLeptonic_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop171p5"),
  ("process_name_specific",           "TTToSemiLeptonic_mtop171p5"),
  ("nof_files",                       5),
  ("nof_db_files",                    622),
  ("nof_events",                      {
    'Count'                                                                          : [     24984000, ],
    'CountWeighted'                                                                  : [     24778581,     24783301,     24777991, ],
    'CountWeightedLHEWeightScale'                                                    : [     27927363,     27440202,     27128077,     25388224,     24778444,     24314573,     22967385,     22312288,     21773678, ],
    'CountWeightedLHEEnvelope'                                                       : [     30180083,     20301659, ],
    'CountWeightedPSWeight'                                                          : [     24781753,     24779572,     35906151,     24780277,     24736580,     14746782, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    249814156,    249814264,    249814264,    249814152,    249813460,    249813340, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     24807421,     24807451,     24807370, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     24866017,     24866061,     24865971, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     24824322,     24824335,     24824254, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     24894817,     24894846,     24894784, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     24832398,     24832424,     24832354, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     24923608,     24923623,     24923574, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     27960266,     27476040,     27166807,     25410402,     24806659,     24344485,     22981536,     22331312,     21796715, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     28029321,     27547282,     27240382,     25465828,     24865258,     24405901,     23026097,     22379643,     21848173, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     27979268,     27494330,     27184549,     25428143,     24823563,     24360677,     22997968,     22346825,     21811464, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     28061726,     27578418,     27270532,     25496178,     24894054,     24433459,     23054256,     22406137,     21873297, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     27990279,     27505283,     27195484,     25435929,     24831639,     24369015,     23003469,     22352838,     21817882, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     28097890,     27614278,     27306253,     25524583,     24922844,     24462544,     23076846,     22429500,     21897243, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     30205106,     20333969, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     30269709,     20392186, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     30226372,     20346904, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     30306088,     20414119, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     30236028,     20354770, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     30340615,     20440310, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     24808554,     24805199,     35934561,     24806127,     24764089,     14770496, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     24867561,     24863132,     36010014,     24864193,     24823773,     14813172, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     24825401,     24822140,     35959833,     24823055,     24780846,     14779880, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     24896305,     24892036,     36053250,     24893075,     24852335,     14829067, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     24833552,     24830144,     35970058,     24831072,     24789093,     14785883, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     24925201,     24920653,     36091825,     24921693,     24881427,     14848706, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    250047460,    250047564,    250047564,    250047460,    250046776,    250046668, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    250586796,    250586892,    250586892,    250586788,    250586104,    250585996, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    250224120,    250224236,    250224236,    250224120,    250223432,    250223308, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    250888120,    250888224,    250888224,    250888116,    250887452,    250887336, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    250302092,    250302192,    250302192,    250302084,    250301400,    250301288, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    251169932,    251170044,    251170044,    251169928,    251169248,    251169136, ],
  }),
  ("nof_tree_events",                 2271667),
  ("nof_db_events",                   24984000),
  ("fsize_local",                     10079274991), # 10.08GB, avg file size 2.02GB
  ("fsize_db",                        1340936158922), # 1.34TB, avg file size 2.16GB
  ("use_it",                          False),
  ("xsection",                        365.52),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTToSemiLeptonic_mtop171p5"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTToHadronic_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop171p5"),
  ("process_name_specific",           "TTToHadronic_mtop171p5"),
  ("nof_files",                       3),
  ("nof_db_files",                    624),
  ("nof_events",                      {
    'Count'                                                                          : [     24777000, ],
    'CountWeighted'                                                                  : [     24582684,     24578743,     24572923, ],
    'CountWeightedLHEWeightScale'                                                    : [     27694948,     27211895,     26902466,     25179316,     24581786,     24113904,     22779312,     22129410,     21595092, ],
    'CountWeightedLHEEnvelope'                                                       : [     29931813,     20132261, ],
    'CountWeightedPSWeight'                                                          : [     24576646,     24573752,     36358263,     24577430,     24508336,     13956577, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    247745884,    247745984,    247745992,    247745884,    247744940,    247744812, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     24603077,     24602979,     24603018, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     24661327,     24661216,     24661371, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     24619794,     24619724,     24619763, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     24689868,     24689760,     24689919, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     24627828,     24627753,     24627827, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     24718409,     24718311,     24718488, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     27727863,     27247639,     26941007,     25201534,     24602325,     24143656,     22793526,     22148454,     21618020, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     27796576,     27318483,     27014085,     25256683,     24660590,     24204655,     22837866,     22196512,     21669118, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     27746650,     27265756,     26958592,     25219104,     24619055,     24159725,     22809808,     22163840,     21632637, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     27828675,     27349313,     27043950,     25286746,     24689117,     24231973,     22865757,     22222767,     21694023, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     27757587,     27276623,     26969427,     25226821,     24627082,     24167971,     22815246,     22169801,     21638999, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     27864568,     27384911,     27079370,     25314914,     24717651,     24260808,     22888164,     22245927,     21717776, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     29956729,     20164533, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     30020906,     20222503, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     29977791,     20177350, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     30056955,     20244229, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     29987377,     20185170, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     30091191,     20270222, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     24603169,     24599272,     36388676,     24602999,     24536307,     13978662, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     24661821,     24656803,     36466669,     24660711,     24596102,     14018691, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     24619873,     24616059,     36414085,     24619760,     24552852,     13987566, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     24690291,     24685462,     36510178,     24689349,     24624277,     14033783, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     24627942,     24623954,     36424643,     24627738,     24561091,     13993195, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     24718944,     24713712,     36549585,     24717749,     24653285,     14052261, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    247977704,    247977824,    247977824,    247977704,    247976760,    247976660, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    248513664,    248513776,    248513776,    248513664,    248512720,    248512612, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    248152636,    248152760,    248152760,    248152636,    248151684,    248151584, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    248812504,    248812612,    248812612,    248812504,    248811568,    248811444, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    248230000,    248230116,    248230116,    248230008,    248229056,    248228932, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    249092124,    249092244,    249092244,    249092124,    249091192,    249091076, ],
  }),
  ("nof_tree_events",                 299093),
  ("nof_db_events",                   24777000),
  ("fsize_local",                     1369023942), # 1.37GB, avg file size 456.34MB
  ("fsize_db",                        1346096669828), # 1.35TB, avg file size 2.16GB
  ("use_it",                          False),
  ("xsection",                        377.85),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTToHadronic_mtop171p5"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTTo2L2Nu_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop173p5"),
  ("process_name_specific",           "TTTo2L2Nu_mtop173p5"),
  ("nof_files",                       1),
  ("nof_db_files",                    158),
  ("nof_events",                      {
    'Count'                                                                          : [      5232000, ],
    'CountWeighted'                                                                  : [      5189308,      5189839,      5189894, ],
    'CountWeightedLHEWeightScale'                                                    : [      5847324,      5744403,      5678107,      5318501,      5189282,      5090998,      4813371,      4674579,      4560313, ],
    'CountWeightedLHEEnvelope'                                                       : [      6319399,      4251665, ],
    'CountWeightedPSWeight'                                                          : [      5189526,      5190000,      7346936,      5190491,      5183417,      3241838, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     52324540,     52323848,     52324540,     52324540,     52291072,     52290384, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      5192527,      5192550,      5192494, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      5201939,      5201949,      5201930, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      5196286,      5196317,      5196258, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      5208394,      5208415,      5208392, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      5197377,      5197404,      5197355, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      5213190,      5213195,      5213187, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [      5850885,      5748633,      5682966,      5320113,      5192370,      5094346,      4813581,      4675891,      4562519, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [      5862141,      5760396,      5695235,      5328804,      5201782,      5104385,      4820274,      4683432,      4570775, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [      5855126,      5752703,      5686927,      5324063,      5196121,      5097957,      4817233,      4679334,      4565802, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [      5869418,      5767379,      5702014,      5335601,      5208240,      5110577,      4826570,      4689361,      4576410, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [      5856762,      5754341,      5688541,      5325088,      5197219,      5099102,      4817835,      4680053,      4566612, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [      5875612,      5773523,      5708120,      5340301,      5213031,      5115440,      4830178,      4693145,      4580326, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [      6320981,      4256053, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [      6330983,      4265954, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [      6325715,      4258936, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [      6339134,      4270881, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [      6327012,      4260085, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [      6344869,      4275345, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      5192181,      5192411,      7348287,      5192943,      5186192,      3245311, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      5201685,      5201688,      7359444,      5202242,      5195811,      3253011, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      5195943,      5196180,      7353803,      5196717,      5189934,      3247507, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      5208135,      5208171,      7368931,      5208723,      5202227,      3256756, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      5197047,      5197254,      7355009,      5197793,      5191042,      3248460, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      5212952,      5212928,      7375008,      5213476,      5207069,      3260327, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     52333444,     52332760,     52333444,     52333440,     52300320,     52299628, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     52417488,     52416816,     52417492,     52417488,     52384608,     52383932, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     52372804,     52372116,     52372804,     52372804,     52339628,     52338936, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     52484936,     52484260,     52484936,     52484932,     52451960,     52451280, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     52383036,     52382356,     52383040,     52383036,     52349868,     52349184, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     52531444,     52530768,     52531444,     52531444,     52498512,     52497828, ],
  }),
  ("nof_tree_events",                 1975496),
  ("nof_db_events",                   5732000),
  ("fsize_local",                     8206214565), # 8.21GB, avg file size 8.21GB
  ("fsize_db",                        305189066785), # 305.19GB, avg file size 1.93GB
  ("use_it",                          False),
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_mtop173p5"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTToSemiLeptonic_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop173p5"),
  ("process_name_specific",           "TTToSemiLeptonic_mtop173p5"),
  ("nof_files",                       5),
  ("nof_db_files",                    590),
  ("nof_events",                      {
    'Count'                                                                          : [     23892000, ],
    'CountWeighted'                                                                  : [     23700254,     23697989,     23699482, ],
    'CountWeightedLHEWeightScale'                                                    : [     26703226,     26232368,     25928704,     24287358,     23699173,     23246881,     21980363,     21345412,     20823192, ],
    'CountWeightedLHEEnvelope'                                                       : [     28859958,     19412689, ],
    'CountWeightedPSWeight'                                                          : [     23699030,     23697404,     34350095,     23699940,     23655068,     14091920, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    238897428,    238897524,    238897528,    238897416,    238896504,    238896380, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     23710425,     23710521,     23710316, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     23752796,     23752920,     23752644, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     23727669,     23727740,     23727538, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     23782380,     23782507,     23782255, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     23732580,     23732648,     23732450, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     23804125,     23804240,     23803974, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     26718747,     26250952,     25950213,     24294015,     23709710,     23261555,     21980700,     21350781,     20832742, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     26769413,     26303943,     26005587,     24333044,     23752087,     23306873,     22010656,     21384698,     20869926, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     26738127,     26269632,     25968350,     24312105,     23726952,     23278097,     21997443,     21366596,     20847786, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     26802683,     26335959,     26036623,     24364160,     23781667,     23335207,     22039502,     21411885,     20895739, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     26745481,     26276953,     25975631,     24316686,     23731857,     23283256,     22000138,     21369815,     20851426, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     26830784,     26363782,     26064313,     24385475,     23803403,     23357269,     22055866,     21429056,     20913527, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     28866321,     19432274, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     28911197,     19477048, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     28887997,     19445496, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     28948510,     19499631, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     28893784,     19450697, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     28974464,     19519937, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     23710386,     23707666,     34357027,     23710349,     23667519,     14106061, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     23753154,     23749374,     34409714,     23752199,     23711249,     14138639, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     23727585,     23724971,     34382725,     23727644,     23684581,     14115678, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     23782676,     23779083,     34453974,     23781868,     23740514,     14155045, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     23732531,     23729818,     34388502,     23732489,     23689648,     14119680, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     23804502,     23800682,     34482648,     23803480,     23762568,     14170276, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    238974812,    238974920,    238974920,    238974812,    238973920,    238973816, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    239352604,    239352696,    239352704,    239352604,    239351700,    239351592, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    239154760,    239154848,    239154852,    239154760,    239153856,    239153744, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    239661540,    239661636,    239661644,    239661540,    239660640,    239660520, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    239201092,    239201188,    239201196,    239201092,    239200188,    239200072, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    239873244,    239873340,    239873348,    239873240,    239872360,    239872248, ],
  }),
  ("nof_tree_events",                 2172864),
  ("nof_db_events",                   23892000),
  ("fsize_local",                     9681169267), # 9.68GB, avg file size 1.94GB
  ("fsize_db",                        1285214519655), # 1.29TB, avg file size 2.18GB
  ("use_it",                          False),
  ("xsection",                        365.52),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTToSemiLeptonic_mtop173p5"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTToHadronic_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop173p5"),
  ("process_name_specific",           "TTToHadronic_mtop173p5"),
  ("nof_files",                       5),
  ("nof_db_files",                    674),
  ("nof_events",                      {
    'Count'                                                                          : [     24804000, ],
    'CountWeighted'                                                                  : [     24606933,     24608188,     24603273, ],
    'CountWeightedLHEWeightScale'                                                    : [     27723380,     27235352,     26920618,     25215201,     24606933,     24135737,     22819778,     22161095,     21619276, ],
    'CountWeightedLHEEnvelope'                                                       : [     29962036,     20155799, ],
    'CountWeightedPSWeight'                                                          : [     24605387,     24605716,     36408951,     24605152,     24530515,     13963722, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    248030580,    248030708,    248030716,    248030580,    248029240,    248029096, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     24617137,     24617129,     24617085, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     24661581,     24661529,     24661538, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     24634977,     24634983,     24634918, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     24692200,     24692202,     24692133, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     24640107,     24640124,     24640046, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     24714853,     24714844,     24714782, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     27740113,     27255226,     26943466,     25222638,     24617137,     24151416,     22820582,     22167086,     21629564, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     27793278,     27310778,     27001451,     25263649,     24661581,     24198873,     22852110,     22202678,     21668515, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     27760167,     27274568,     26962244,     25241368,     24634977,     24168541,     22837926,     22183462,     21645153, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     27827707,     27343912,     27033575,     25295862,     24692200,     24228219,     22881970,     22230827,     21695252, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     27767815,     27282187,     26969859,     25246143,     24640107,     24173952,     22840745,     22186852,     21648978, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     27856906,     27372865,     27062438,     25318055,     24714853,     24251249,     22899034,     22248753,     21713854, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     29969157,     20176622, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     30016237,     20223552, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     29991613,     20190304, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     30054884,     20246914, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     29997670,     20195722, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     30081955,     20268039, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     24617634,     24617020,     36417347,     24616425,     24543276,     13977713, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     24662491,     24660921,     36474204,     24660324,     24588457,     14009957, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     24635453,     24634902,     36444472,     24634316,     24560986,     13987242, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     24693056,     24691635,     36520923,     24691035,     24618828,     14026213, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     24640637,     24640002,     36450701,     24639372,     24566164,     13991182, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     24715839,     24714199,     36551527,     24713534,     24641572,     14041263, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    248102516,    248102652,    248102652,    248102520,    248101176,    248101036, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    248499740,    248499860,    248499860,    248499736,    248498408,    248498280, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    248288796,    248288928,    248288932,    248288796,    248287460,    248287328, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    248819444,    248819572,    248819572,    248819444,    248818128,    248817984, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    248337256,    248337388,    248337388,    248337244,    248335928,    248335776, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    249040208,    249040340,    249040340,    249040204,    249038888,    249038760, ],
  }),
  ("nof_tree_events",                 300666),
  ("nof_db_events",                   24854000),
  ("fsize_local",                     1385744513), # 1.39GB, avg file size 277.15MB
  ("fsize_db",                        1353828323810), # 1.35TB, avg file size 2.01GB
  ("use_it",                          False),
  ("xsection",                        377.85),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTToHadronic_mtop173p5"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTTo2L2Nu_mtop175p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop175p5"),
  ("process_name_specific",           "TTTo2L2Nu_mtop175p5"),
  ("nof_files",                       1),
  ("nof_db_files",                    154),
  ("nof_events",                      {
    'Count'                                                                          : [      4574000, ],
    'CountWeighted'                                                                  : [      4537906,      4537266,      4537771, ],
    'CountWeightedLHEWeightScale'                                                    : [      5111702,      5021044,      4962196,      4651553,      4537893,      4450249,      4211430,      4088468,      3987335, ],
    'CountWeightedLHEEnvelope'                                                       : [      5525110,      3716860, ],
    'CountWeightedPSWeight'                                                          : [      4537801,      4537979,      6426609,      4538021,      4531762,      2832183, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     45734720,     45733916,     45734744,     45734720,     45698608,     45697764, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      4537444,      4537479,      4537393, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      4543103,      4543130,      4543072, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      4540938,      4540973,      4540882, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      4549135,      4549170,      4549100, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      4541376,      4541408,      4541320, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      4552245,      4552286,      4552222, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [      5111841,      5021814,      4963567,      4650215,      4537307,      4450546,      4209088,      4087179,      3986892, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [      5118811,      5029277,      4971516,      4655175,      4542970,      4456818,      4212511,      4091432,      3991825, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [      5115769,      5025603,      4967251,      4653886,      4540800,      4453909,      4212473,      4090385,      3989943, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [      5125586,      5035804,      4977858,      4661512,      4548997,      4462604,      4218392,      4096975,      3997096, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [      5116598,      5026429,      4968083,      4654236,      4541236,      4454398,      4212524,      4090550,      3990194, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [      5129777,      5039968,      4982000,      4664528,      4552107,      4465801,      4220567,      4099336,      3999599, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [      5523167,      3718584, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [      5528733,      3725201, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [      5527567,      3721267, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [      5536325,      3729812, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [      5528051,      3721841, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [      5540028,      3732844, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      4537424,      4537387,      6423972,      4537464,      4531495,      2833554, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      4543168,      4542920,      6430054,      4543020,      4537326,      2838690, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      4540918,      4540894,      6429102,      4540974,      4534977,      2835600, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      4549185,      4548968,      6438918,      4549075,      4543324,      2842194, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      4541351,      4541309,      6429411,      4541388,      4535420,      2836099, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      4552315,      4552056,      6442711,      4552176,      4546480,      2844638, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     45724816,     45724024,     45724844,     45724816,     45689072,     45688240, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     45772472,     45771684,     45772492,     45772472,     45737048,     45736228, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     45761256,     45760460,     45761276,     45761256,     45725452,     45724612, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     45835240,     45834456,     45835264,     45835240,     45799716,     45798888, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     45764992,     45764200,     45765012,     45764992,     45729224,     45728384, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     45865356,     45864572,     45865376,     45865356,     45829904,     45829068, ],
  }),
  ("nof_tree_events",                 1734381),
  ("nof_db_events",                   4958000),
  ("fsize_local",                     7236650812), # 7.24GB, avg file size 7.24GB
  ("fsize_db",                        264638885887), # 264.64GB, avg file size 1.72GB
  ("use_it",                          False),
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_mtop175p5"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTTo2L2Nu_mtop175p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop175p5"),
  ("process_name_specific",           "TTTo2L2Nu_mtop175p5_ext1"),
  ("nof_files",                       1),
  ("nof_db_files",                    283),
  ("nof_events",                      {
    'Count'                                                                          : [      9603000, ],
    'CountWeighted'                                                                  : [      9526485,      9527954,      9526650, ],
    'CountWeightedLHEWeightScale'                                                    : [     10733245,     10542248,     10418091,      9765975,      9526436,      9342287,      8841034,      8582528,      8369892, ],
    'CountWeightedLHEEnvelope'                                                       : [     11599346,      7803858, ],
    'CountWeightedPSWeight'                                                          : [      9526979,      9523921,     13495507,      9526653,      9521157,      5946449, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     96059360,     96057736,     96059440,     96059360,     95983000,     95981240, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      9525647,      9525654,      9525604, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      9537280,      9537281,      9537293, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      9532992,      9533002,      9532953, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      9549974,      9549964,      9549975, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      9533814,      9533825,      9533799, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      9556360,      9556358,      9556389, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     10733184,     10543486,     10420573,      9762933,      9525357,      9342686,      8835989,      8579660,      8368805, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     10747474,     10558795,     10436889,      9773105,      9536983,      9355594,      8843059,      8588455,      8379019, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     10741451,     10551470,     10428326,      9770641,      9532699,      9349743,      8843119,      8586403,      8375236, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     10761758,     10572553,     10450248,      9786444,      9549673,      9367758,      8855394,      8600102,      8390081, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     10743112,     10553135,     10429989,      9771322,      9533523,      9350695,      8843152,      8586670,      8375678, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     10770399,     10581140,     10458788,      9792624,      9556065,      9374337,      8859833,      8604917,      8395186, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     11595025,      7807186, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     11606467,      7820816, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     11604259,      7812845, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     11622438,      7830532, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     11605203,      7813992, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     11630028,      7836770, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      9525920,      9522389,     13489783,      9525307,      9520553,      5949148, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      9537679,      9533707,     13502358,      9536776,      9532744,      5959746, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      9533265,      9529777,     13500540,      9532683,      9527853,      5953451, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      9550353,      9546449,     13520970,      9549494,      9545329,      5967137, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      9534095,      9530563,     13501140,      9533488,      9528752,      5954448, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      9556783,      9552782,     13528847,      9555845,      9551906,      5972140, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     95995656,     95994064,     95995720,     95995656,     95920216,     95918496, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     96093088,     96091528,     96093152,     96093080,     96018280,     96016592, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     96072304,     96070728,     96072376,     96072296,     95996744,     95994992, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     96225344,     96223768,     96225424,     96225344,     96150320,     96148592, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     96079296,     96077720,     96079368,     96079288,     96003768,     96002048, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     96286816,     96285248,     96286896,     96286816,     96211896,     96210176, ],
  }),
  ("nof_tree_events",                 3646124),
  ("nof_db_events",                   9603000),
  ("fsize_local",                     15209272253), # 15.21GB, avg file size 15.21GB
  ("fsize_db",                        512657546981), # 512.66GB, avg file size 1.81GB
  ("use_it",                          False),
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_mtop175p5_ext1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTToSemiLeptonic_mtop175p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop175p5"),
  ("process_name_specific",           "TTToSemiLeptonic_mtop175p5"),
  ("nof_files",                       2),
  ("nof_db_files",                    475),
  ("nof_events",                      {
    'Count'                                                                          : [     19625000, ],
    'CountWeighted'                                                                  : [     19472156,     19469324,     19465207, ],
    'CountWeightedLHEWeightScale'                                                    : [     21929717,     21542111,     21291196,     19954671,     19471488,     19093517,     18065789,     17539489,     17106525, ],
    'CountWeightedLHEEnvelope'                                                       : [     23700894,     15948902, ],
    'CountWeightedPSWeight'                                                          : [     19469329,     19469907,     28227352,     19467186,     19428407,     11567282, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    196239720,    196239864,    196239864,    196239720,    196238984,    196238856, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     19466244,     19466249,     19466162, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     19490282,     19490213,     19490342, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     19481240,     19481229,     19481146, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     19516146,     19516100,     19516172, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     19482978,     19482972,     19482935, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     19529353,     19529297,     19529433, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     21929999,     21545037,     21296592,     19948739,     19465650,     19094553,     18055720,     17533851,     17104467, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     21959604,     21576683,     21330255,     19969844,     19489683,     19121151,     18070380,     17551990,     17125500, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     21946845,     21561290,     21312382,     19964466,     19480626,     19108955,     18070265,     17547595,     17117567, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     21988681,     21604697,     21357455,     19997010,     19515559,     19145960,     18095544,     17575750,     17148069, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     21950303,     21564751,     21315864,     19965916,     19482386,     19110933,     18070370,     17548212,     17118540, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     22006497,     21622386,     21375045,     20009797,     19528756,     19159519,     18104745,     17585701,     17158623, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     23692457,     15955921, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     23716182,     15983967, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     23711276,     15967461, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     23748743,     16003785, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     23713272,     15969823, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     23764455,     16016602, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     19467419,     19467252,     28216674,     19464432,     19427237,     11572266, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     19491829,     19490839,     28244219,     19488011,     19452190,     11592608, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     19482375,     19482287,     28239016,     19479466,     19442121,     11580649, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     19517639,     19516776,     28282874,     19513959,     19477839,     11607004, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     19484189,     19483995,     28240462,     19481154,     19443934,     11582545, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     19530933,     19529911,     28299695,     19527031,     19491181,     11616694, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    196181576,    196181688,    196181688,    196181576,    196180816,    196180696, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    196382248,    196382344,    196382344,    196382248,    196381536,    196381392, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    196337832,    196337968,    196337968,    196337832,    196337104,    196336976, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    196652152,    196652288,    196652288,    196652152,    196651424,    196651288, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    196352904,    196353048,    196353048,    196352904,    196352176,    196352040, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    196779240,    196779376,    196779376,    196779240,    196778496,    196778376, ],
  }),
  ("nof_tree_events",                 1786340),
  ("nof_db_events",                   19625000),
  ("fsize_local",                     7995065109), # 8.00GB, avg file size 4.00GB
  ("fsize_db",                        1057075927311), # 1.06TB, avg file size 2.23GB
  ("use_it",                          False),
  ("xsection",                        365.52),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTToSemiLeptonic_mtop175p5"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTToSemiLeptonic_mtop175p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop175p5"),
  ("process_name_specific",           "TTToSemiLeptonic_mtop175p5_ext1"),
  ("nof_files",                       2),
  ("nof_db_files",                    254),
  ("nof_events",                      {
    'Count'                                                                          : [      9773000, ],
    'CountWeighted'                                                                  : [      9694385,      9695319,      9693707, ],
    'CountWeightedLHEWeightScale'                                                    : [     10921103,     10726990,     10601001,      9937578,      9694056,      9507111,      8997002,      8734203,      8517971, ],
    'CountWeightedLHEEnvelope'                                                       : [     11802822,      7941597, ],
    'CountWeightedPSWeight'                                                          : [      9695000,      9693205,     14056527,      9694141,      9677203,      5760384, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     97721848,     97721892,     97721892,     97721852,     97721436,     97721380, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      9693074,      9693065,      9693073, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      9704630,      9704667,      9704611, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      9700568,      9700565,      9700574, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      9717596,      9717610,      9717565, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      9701354,      9701353,      9701336, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      9723976,      9724032,      9723927, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     10920776,     10727993,     10603242,      9934193,      9692776,      9507218,      8991595,      8730993,      8516586, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     10935061,     10743307,     10619563,      9944291,      9704334,      9520067,      8998512,      8739664,      8526701, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     10929198,     10736128,     10611149,      9942060,      9700277,      9514423,      8998869,      8737877,      8523139, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     10949611,     10757330,     10633181,      9957886,      9717285,      9532491,      9011111,      8751553,      8538015, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     10930824,     10737753,     10612772,      9942686,      9701055,      9515323,      8998844,      8738095,      8523545, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     10958280,     10765927,     10641736,      9964072,      9723681,      9539053,      9015514,      8756343,      8543092, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     11798059,      7944816, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     11809332,      7958500, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     11807483,      7950578, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     11825642,      7968413, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     11808364,      7951686, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     11833232,      7974646, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      9693661,      9691427,     14050512,      9692435,      9676185,      5762656, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      9705393,      9702726,     14063556,      9703793,      9688195,      5772589, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      9701156,      9698942,     14061698,      9699955,      9683637,      5766855, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      9718317,      9715710,     14082925,      9716773,      9701056,      5779798, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      9701948,      9699683,     14062274,      9700701,      9684485,      5767760, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      9724756,      9722020,     14091019,      9723105,      9707580,      5784542, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     97692080,     97692124,     97692124,     97692080,     97691664,     97691624, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     97788472,     97788508,     97788508,     97788472,     97788048,     97788008, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     97770240,     97770280,     97770280,     97770240,     97769824,     97769788, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     97923464,     97923508,     97923508,     97923468,     97923048,     97923008, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     97776920,     97776956,     97776956,     97776920,     97776504,     97776460, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     97984968,     97985008,     97985008,     97984968,     97984556,     97984520, ],
  }),
  ("nof_tree_events",                 891163),
  ("nof_db_events",                   9773000),
  ("fsize_local",                     3989891937), # 3.99GB, avg file size 1.99GB
  ("fsize_db",                        526998400342), # 527.00GB, avg file size 2.07GB
  ("use_it",                          False),
  ("xsection",                        365.52),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTToSemiLeptonic_mtop175p5_ext1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTToHadronic_mtop175p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop175p5"),
  ("process_name_specific",           "TTToHadronic_mtop175p5"),
  ("nof_files",                       2),
  ("nof_db_files",                    499),
  ("nof_events",                      {
    'Count'                                                                          : [     18080000, ],
    'CountWeighted'                                                                  : [     17936817,     17935809,     17933096, ],
    'CountWeightedLHEWeightScale'                                                    : [     20204488,     19846083,     19613696,     18384747,     17936817,     17589440,     16644426,     16158775,     15759124, ],
    'CountWeightedLHEEnvelope'                                                       : [     21836558,     14692086, ],
    'CountWeightedPSWeight'                                                          : [     17935441,     17939287,     26555209,     17936216,     17883296,     10170170, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    180773888,    180773992,    180774024,    180773888,    180772656,    180772528, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     17933676,     17933642,     17933652, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     17955793,     17955757,     17955779, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     17947481,     17947464,     17947487, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     17979639,     17979605,     17979654, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     17949131,     17949052,     17949136, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     17991809,     17991770,     17991823, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     20204606,     19848720,     19618695,     18379157,     17933676,     17590372,     16635040,     16153490,     15757225, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     20231740,     19877806,     19649715,     18398488,     17955793,     17614876,     16648451,     16170163,     15776587, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     20220144,     19863715,     19633258,     18393659,     17947481,     17603647,     16648448,     16166169,     15769298, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     20258576,     19903658,     19674779,     18423556,     17979639,     17637771,     16671674,     16192062,     15797406, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     20223347,     19866920,     19636471,     18394991,     17949131,     17605493,     16648559,     16166733,     15770218, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     20274990,     19919934,     19691015,     18435322,     17991809,     17650255,     16680129,     16201247,     15807123, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     21828619,     14698581, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     21850324,     14724430, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     21845986,     14709212, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     21880376,     14742699, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     21847843,     14711402, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     21894840,     14754512, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     17933643,     17936760,     26545625,     17933715,     17882128,     10174293, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     17956048,     17958434,     26572042,     17955428,     17905022,     10191948, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     17947449,     17950641,     26566636,     17947563,     17895824,     10181691, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     17979852,     17982373,     26608353,     17979342,     17928639,     10204648, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     17949095,     17952209,     26568102,     17949137,     17897561,     10183328, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     17992104,     17994442,     26624413,     17991404,     17941022,     10213079, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    180736688,    180736792,    180736808,    180736672,    180735456,    180735320, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    180921888,    180922008,    180922008,    180921888,    180920688,    180920568, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    180880896,    180881008,    180881024,    180880888,    180879680,    180879536, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    181170200,    181170304,    181170312,    181170200,    181168984,    181168856, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    180894856,    180894976,    180894984,    180894856,    180893632,    180893504, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    181287848,    181287984,    181287984,    181287848,    181286656,    181286512, ],
  }),
  ("nof_tree_events",                 220664),
  ("nof_db_events",                   18280000),
  ("fsize_local",                     1019033179), # 1.02GB, avg file size 509.52MB
  ("fsize_db",                        997347369283), # 997.35GB, avg file size 2.00GB
  ("use_it",                          False),
  ("xsection",                        377.85),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTToHadronic_mtop175p5"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTTo2L2Nu_mtop178p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop178p5"),
  ("process_name_specific",           "TTTo2L2Nu_mtop178p5"),
  ("nof_files",                       1),
  ("nof_db_files",                    76),
  ("nof_events",                      {
    'Count'                                                                          : [      2416000, ],
    'CountWeighted'                                                                  : [      2396629,      2396709,      2396955, ],
    'CountWeightedLHEWeightScale'                                                    : [      2699606,      2651019,      2619153,      2457779,      2396629,      2349540,      2226128,      2160069,      2105617, ],
    'CountWeightedLHEEnvelope'                                                       : [      2917424,      1963318, ],
    'CountWeightedPSWeight'                                                          : [      2396783,      2396341,      3397660,      2396700,      2395001,      1493824, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     24158210,     24157580,     24158238,     24158206,     24132064,     24131376, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      2394429,      2394499,      2394349, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      2395386,      2395476,      2395297, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      2396431,      2396503,      2396355, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      2398870,      2398957,      2398779, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      2396233,      2396311,      2396151, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      2399649,      2399748,      2399550, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [      2697289,      2649066,      2617536,      2454920,      2394429,      2347625,      2222960,      2157497,      2103546, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [      2698674,      2650737,      2619478,      2455470,      2395386,      2348935,      2222915,      2157934,      2104381, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [      2699545,      2651243,      2619652,      2457018,      2396431,      2349552,      2224899,      2159333,      2105294, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [      2702592,      2654516,      2623148,      2459122,      2398870,      2352280,      2226296,      2161124,      2107418, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [      2699509,      2651208,      2619613,      2456781,      2396233,      2349386,      2224540,      2159038,      2105049, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [      2703839,      2655747,      2624366,      2459847,      2399649,      2353106,      2226664,      2161598,      2107969, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [      2913823,      1962503, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [      2914278,      1964341, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [      2916335,      1964053, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [      2918655,      1967021, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [      2916077,      1964003, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [      2919554,      1967905, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      2394466,      2393936,      3393306,      2394320,      2392761,      1493216, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      2395455,      2394843,      3393673,      2395244,      2393819,      1494637, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      2396469,      2395945,      3396235,      2396328,      2394751,      1494391, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      2398932,      2398337,      3398780,      2398728,      2397282,      1496671, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      2396273,      2395743,      3395827,      2396125,      2394577,      1494378, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      2399719,      2399106,      3399610,      2399507,      2398108,      1497395, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     24128948,     24128322,     24128976,     24128944,     24103086,     24102402, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     24133554,     24132938,     24133582,     24133554,     24107924,     24107246, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     24149820,     24149194,     24149850,     24149818,     24123910,     24123228, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     24169792,     24169172,     24169820,     24169788,     24144076,     24143398, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     24147566,     24146944,     24147596,     24147566,     24121674,     24120990, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     24177074,     24176454,     24177102,     24177072,     24151390,     24150710, ],
  }),
  ("nof_tree_events",                 922007),
  ("nof_db_events",                   2416000),
  ("fsize_local",                     3873004252), # 3.87GB, avg file size 3.87GB
  ("fsize_db",                        129329691697), # 129.33GB, avg file size 1.70GB
  ("use_it",                          False),
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_mtop178p5"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTToSemiLeptonic_mtop178p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop178p5"),
  ("process_name_specific",           "TTToSemiLeptonic_mtop178p5"),
  ("nof_files",                       1),
  ("nof_db_files",                    256),
  ("nof_events",                      {
    'Count'                                                                          : [      9762000, ],
    'CountWeighted'                                                                  : [      9685865,      9683141,      9684041, ],
    'CountWeightedLHEWeightScale'                                                    : [     10909570,     10713388,     10584852,      9931823,      9685865,      9494648,      8995458,      8728470,      8508702, ],
    'CountWeightedLHEEnvelope'                                                       : [     11789749,      7933772, ],
    'CountWeightedPSWeight'                                                          : [      9685116,      9684006,     14053885,      9685696,      9670239,      5747816, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     97634672,     97634696,     97634696,     97634672,     97634008,     97633984, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      9675617,      9675633,      9675605, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      9679316,      9679280,      9679379, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      9683731,      9683746,      9683709, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      9693421,      9693377,      9693453, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      9682961,      9682960,      9682949, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      9696612,      9696569,      9696663, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     10899933,     10705297,     10578203,      9919987,      9675617,      9486773,      8982392,      8717885,      8500147, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     10905271,     10711893,     10585955,      9921951,      9679316,      9491948,      8981975,      8719463,      8503382, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     10909051,     10714118,     10586761,      9928476,      9683731,      9494574,      8990250,      8725319,      8507235, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     10921126,     10727172,     10600801,      9936738,      9693421,      9505479,      8995649,      8732395,      8515682, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     10908906,     10713990,     10586654,      9927518,      9682961,      9493939,      8988794,      8724145,      8506282, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     10926157,     10732209,     10605836,      9939660,      9696612,      9508903,      8997140,      8734332,      8517967, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     11774949,      7930297, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     11776571,      7937573, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     11785110,      7936567, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     11794276,      7948419, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     11784088,      7936390, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     11797970,      7952021, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      9675591,      9674011,     14036070,      9675744,      9661164,      5745220, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      9679469,      9677398,     14037789,      9679175,      9665428,      5750454, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      9683683,      9682149,     14048128,      9683867,      9669193,      5749771, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      9693526,      9691553,     14058798,      9693316,      9679362,      5758324, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      9682932,      9681307,     14046507,      9683064,      9668529,      5749721, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      9696765,      9694639,     14062410,      9696450,      9682816,      5761116, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     97499048,     97499072,     97499072,     97499048,     97498400,     97498376, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     97515488,     97515512,     97515512,     97515488,     97514856,     97514848, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     97583360,     97583384,     97583384,     97583360,     97582712,     97582688, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     97662144,     97662160,     97662160,     97662144,     97661496,     97661480, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     97574344,     97574368,     97574368,     97574344,     97573704,     97573680, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     97691784,     97691792,     97691792,     97691784,     97691144,     97691128, ],
  }),
  ("nof_tree_events",                 890456),
  ("nof_db_events",                   9762000),
  ("fsize_local",                     4012570260), # 4.01GB, avg file size 4.01GB
  ("fsize_db",                        528185317770), # 528.19GB, avg file size 2.06GB
  ("use_it",                          False),
  ("xsection",                        365.52),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTToSemiLeptonic_mtop178p5"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTToHadronic_mtop178p5_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop178p5"),
  ("process_name_specific",           "TTToHadronic_mtop178p5"),
  ("nof_files",                       1),
  ("nof_db_files",                    247),
  ("nof_events",                      {
    'Count'                                                                          : [      9782000, ],
    'CountWeighted'                                                                  : [      9703512,      9705681,      9704810, ],
    'CountWeightedLHEWeightScale'                                                    : [     10930939,     10735061,     10607011,      9952082,      9703512,      9515147,      9014403,      8747232,      8527336, ],
    'CountWeightedLHEEnvelope'                                                       : [     11813834,      7950358, ],
    'CountWeightedPSWeight'                                                          : [      9705680,      9706766,     14371884,      9705521,      9673394,      5498443, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     97834080,     97834160,     97834168,     97834080,     97833192,     97833104, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      9695972,      9695931,      9696014, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      9699717,      9699674,      9699752, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      9704129,      9704080,      9704155, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      9713858,      9713816,      9713890, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      9703362,      9703325,      9703392, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      9717104,      9717088,      9717125, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     10921442,     10727020,     10600289,      9940305,      9695972,      9507208,      9001379,      8736641,      8518716, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     10926934,     10733666,     10608037,      9942395,      9699717,      9512357,      9001023,      8738239,      8521937, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     10930589,     10735868,     10608889,      9948832,      9704129,      9515044,      9009262,      8744103,      8525835, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     10942839,     10749015,     10622929,      9957231,      9713858,      9525944,      9014761,      8751218,      8534278, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     10930468,     10735763,     10608800,      9947888,      9703362,      9514425,      9007831,      8742947,      8524897, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     10947927,     10754079,     10627992,      9960200,      9717104,      9529396,      9016308,      8753200,      8536601, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     11799003,      7946960, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     11800652,      7954331, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     11809225,      7953236, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     11818443,      7965199, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     11808233,      7953070, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     11822204,      7968817, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      9696202,      9696772,     14354063,      9695703,      9664348,      5495833, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      9700073,      9700210,     14356241,      9699227,      9668658,      5500727, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      9704333,      9704939,     14366398,      9703859,      9672401,      5500205, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      9714195,      9714411,     14377699,      9713407,      9682629,      5508287, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      9703586,      9704153,     14364793,      9703075,      9671703,      5500148, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      9717474,      9717595,     14381476,      9716596,      9685976,      5510925, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     97699624,     97699704,     97699712,     97699624,     97698752,     97698656, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     97717048,     97717136,     97717136,     97717048,     97716208,     97716120, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     97784168,     97784248,     97784256,     97784168,     97783312,     97783224, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     97863952,     97864032,     97864048,     97863952,     97863104,     97863008, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     97775320,     97775400,     97775400,     97775320,     97774464,     97774352, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     97894096,     97894176,     97894184,     97894096,     97893240,     97893144, ],
  }),
  ("nof_tree_events",                 118479),
  ("nof_db_events",                   9782000),
  ("fsize_local",                     550826924), # 550.83MB, avg file size 550.83MB
  ("fsize_db",                        535678760206), # 535.68GB, avg file size 2.17GB
  ("use_it",                          False),
  ("xsection",                        377.85),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTToHadronic_mtop178p5"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTTo2L2Nu_widthx0p7_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_widthx0p7"),
  ("process_name_specific",           "TTTo2L2Nu_widthx0p7"),
  ("nof_files",                       1),
  ("nof_db_files",                    139),
  ("nof_events",                      {
    'Count'                                                                          : [      4776000, ],
    'CountWeighted'                                                                  : [      4737859,      4737710,      4737817, ],
    'CountWeightedLHEWeightScale'                                                    : [      5338885,      5245364,      5185316,      4854301,      4737778,      4647928,      4392015,      4266112,      4162541, ],
    'CountWeightedLHEEnvelope'                                                       : [      5769706,      3880995, ],
    'CountWeightedPSWeight'                                                          : [      4737923,      4737103,      6706450,      4737318,      4732791,      2960039, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     47754904,     47754472,     47754936,     47754904,     47728380,     47727876, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      4741397,      4741322,      4741469, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      4751375,      4751309,      4751430, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      4744715,      4744635,      4744786, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      4757052,      4756977,      4757105, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      4745991,      4745910,      4746069, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      4762006,      4761937,      4762071, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [      5343745,      5250814,      5191333,      4857238,      4741253,      4652404,      4393546,      4268607,      4165828, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [      5355567,      5263074,      5204060,      4866579,      4751228,      4662946,      4400930,      4276745,      4174590, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [      5347473,      5254405,      5194823,      4860721,      4744571,      4655587,      4396771,      4271650,      4168726, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [      5361946,      5269212,      5210006,      4872557,      4756902,      4668380,      4406470,      4281958,      4179545, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [      5349277,      5256202,      5196619,      4861937,      4745847,      4656919,      4397578,      4272561,      4169719, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [      5368243,      5275466,      5216241,      4877432,      4761861,      4673409,      4410288,      4285940,      4183648, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [      5772896,      3886184, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [      5783708,      3896364, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [      5777068,      3888727, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [      5790868,      3900689, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [      5778586,      3890013, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [      5796804,      3905251, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      4741776,      4740714,      6709778,      4740952,      4736823,      2964103, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      4751853,      4750544,      6721953,      4750805,      4747043,      2971994, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      4745087,      4744044,      6714638,      4744276,      4740112,      2966033, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      4757512,      4756241,      6730296,      4756498,      4752668,      2975274, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      4746380,      4745305,      6716141,      4745539,      4741416,      2967084, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      4762507,      4761165,      6736667,      4761420,      4757682,      2978903, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     47787120,     47786684,     47787152,     47787112,     47760828,     47760328, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     47878048,     47877624,     47878080,     47878048,     47851968,     47851480, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     47821784,     47821356,     47821816,     47821784,     47795448,     47794960, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     47937404,     47936976,     47937444,     47937412,     47911248,     47910760, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     47834072,     47833644,     47834108,     47834076,     47807764,     47807268, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     47986052,     47985628,     47986080,     47986052,     47959920,     47959432, ],
  }),
  ("nof_tree_events",                 1801864),
  ("nof_db_events",                   4776000),
  ("fsize_local",                     7469412706), # 7.47GB, avg file size 7.47GB
  ("fsize_db",                        254087020383), # 254.09GB, avg file size 1.83GB
  ("use_it",                          False),
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_widthx0p7"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTToSemiLeptonic_widthx0p7_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_widthx0p7"),
  ("process_name_specific",           "TTToSemiLeptonic_widthx0p7"),
  ("nof_files",                       4),
  ("nof_db_files",                    545),
  ("nof_events",                      {
    'Count'                                                                          : [     19050000, ],
    'CountWeighted'                                                                  : [     18895705,     18894841,     18894776, ],
    'CountWeightedLHEWeightScale'                                                    : [     21289180,     20917893,     20679357,     19359149,     18895705,     18537453,     17516939,     17015038,     16602366, ],
    'CountWeightedLHEEnvelope'                                                       : [     23008498,     15478494, ],
    'CountWeightedPSWeight'                                                          : [     18895294,     18891954,     27382149,     18894093,     18860086,     11238183, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    190513876,    190513932,    190513932,    190513872,    190513264,    190513212, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     18909351,     18909458,     18909237, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     18948875,     18948998,     18948736, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     18922637,     18922739,     18922538, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     18971607,     18971732,     18971461, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     18927757,     18927863,     18927651, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     18991405,     18991534,     18991311, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     21308381,     20939376,     20703071,     19370582,     18909351,     18554969,     17522701,     17024649,     16615146, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     21355341,     20988050,     20753563,     19407582,     18948875,     18596722,     17551870,     17056818,     16649777, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     21323302,     20953765,     20717026,     19384523,     18922637,     18567723,     17535624,     17036850,     16626744, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     21380881,     21012626,     20777380,     19431496,     18971607,     18618489,     17574051,     17077715,     16669620, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     21330520,     20960946,     20724211,     19389405,     18927757,     18573043,     17538865,     17040508,     16630720, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     21406051,     21037584,     20802245,     19450997,     18991405,     18638558,     17589341,     17093627,     16686005, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     23020989,     15498854, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     23063907,     15539141, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     23037699,     15509035, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     23092593,     15556457, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     23043803,     15514166, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     23116326,     15574663, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     18910276,     18906133,     27396111,     18908353,     18875723,     11253020, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     18950102,     18945159,     27446256,     18947477,     18916089,     11282441, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     18923538,     18919460,     27415961,     18921671,     18888916,     11260421, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     18972775,     18967963,     27480341,     18970263,     18938645,     11295013, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     18928698,     18924527,     27422278,     18926738,     18894138,     11264366, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     18992683,     18987646,     27506674,     18989969,     18958649,     11308693, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    190604156,    190604208,    190604208,    190604148,    190603564,    190603496, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    190962552,    190962608,    190962608,    190962552,    190961956,    190961904, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    190742932,    190742988,    190742988,    190742932,    190742352,    190742284, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    191200188,    191200240,    191200240,    191200184,    191199600,    191199544, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    190791900,    190791956,    190791956,    190791896,    190791308,    190791244, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    191393720,    191393776,    191393776,    191393720,    191393132,    191393076, ],
  }),
  ("nof_tree_events",                 1733789),
  ("nof_db_events",                   19500000),
  ("fsize_local",                     7710687618), # 7.71GB, avg file size 1.93GB
  ("fsize_db",                        1048702444808), # 1.05TB, avg file size 1.92GB
  ("use_it",                          False),
  ("xsection",                        365.52),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTToSemiLeptonic_widthx0p7"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTTo2L2Nu_widthx0p85_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_widthx0p85"),
  ("process_name_specific",           "TTTo2L2Nu_widthx0p85"),
  ("nof_files",                       1),
  ("nof_db_files",                    139),
  ("nof_events",                      {
    'Count'                                                                          : [      4790000, ],
    'CountWeighted'                                                                  : [      4750753,      4750876,      4750773, ],
    'CountWeightedLHEWeightScale'                                                    : [      5352792,      5258705,      5198274,      4868065,      4750710,      4660638,      4405303,      4278719,      4174622, ],
    'CountWeightedLHEEnvelope'                                                       : [      5784890,      3892105, ],
    'CountWeightedPSWeight'                                                          : [      4751241,      4751058,      6724736,      4750222,      4745137,      2968300, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     47910980,     47910448,     47911024,     47910980,     47884320,     47883692, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      4754507,      4754516,      4754509, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      4764459,      4764462,      4764486, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      4757849,      4757844,      4757845, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      4770175,      4770174,      4770190, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      4759137,      4759138,      4759144, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      4775163,      4775139,      4775195, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [      5357628,      5264128,      5204273,      4870942,      4754362,      4665061,      4406751,      4281140,      4177845, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [      5369449,      5276398,      5217003,      4880258,      4764313,      4675580,      4414095,      4289232,      4186567, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [      5361377,      5267754,      5207774,      4874457,      4757703,      4668271,      4410008,      4284206,      4180761, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [      5375877,      5282577,      5222981,      4886278,      4770031,      4681045,      4419676,      4294494,      4191553, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [      5363211,      5269565,      5209589,      4875685,      4758995,      4669610,      4410819,      4285124,      4181761, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [      5382218,      5288870,      5229242,      4891188,      4775016,      4686098,      4423513,      4298481,      4195669, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [      5788050,      3897220, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [      5798863,      3907358, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [      5792253,      3899781, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [      5806086,      3911714, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [      5793799,      3901075, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [      5812051,      3916289, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      4755015,      4754642,      6727985,      4753849,      4749088,      2972321, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      4765040,      4764479,      6740131,      4763709,      4759256,      2980186, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      4758348,      4757988,      6732878,      4757191,      4752402,      2974268, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      4770743,      4770215,      6748528,      4769437,      4764922,      2983496, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      4759649,      4759272,      6734407,      4758470,      4753717,      2975321, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      4775740,      4775165,      6754950,      4774385,      4769972,      2987138, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     47926316,     47925796,     47926356,     47926316,     47899968,     47899356, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     48016652,     48016140,     48016700,     48016652,     47990536,     47989928, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     47961196,     47960680,     47961248,     47961196,     47934804,     47934192, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     48076380,     48075868,     48076428,     48076380,     48050168,     48049568, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     47973416,     47972892,     47973464,     47973416,     47947044,     47946424, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     48124904,     48124384,     48124952,     48124904,     48098720,     48098116, ],
  }),
  ("nof_tree_events",                 1808171),
  ("nof_db_events",                   4790000),
  ("fsize_local",                     7497292545), # 7.50GB, avg file size 7.50GB
  ("fsize_db",                        254834163512), # 254.83GB, avg file size 1.83GB
  ("use_it",                          False),
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_widthx0p85"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTToSemiLeptonic_widthx0p85_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_widthx0p85"),
  ("process_name_specific",           "TTToSemiLeptonic_widthx0p85"),
  ("nof_files",                       3),
  ("nof_db_files",                    540),
  ("nof_events",                      {
    'Count'                                                                          : [     14766000, ],
    'CountWeighted'                                                                  : [     14647556,     14647607,     14646477, ],
    'CountWeightedLHEWeightScale'                                                    : [     16503861,     16214465,     16028180,     15007875,     14647556,     14368687,     13579945,     13190052,     12869324, ],
    'CountWeightedLHEEnvelope'                                                       : [     17836624,     11997932, ],
    'CountWeightedPSWeight'                                                          : [     14647479,     14646201,     21224158,     14645694,     14617400,      8711725, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    147677168,    147677252,    147677252,    147677168,    147676752,    147676656, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     14657818,     14657892,     14657743, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     14688230,     14688295,     14688140, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     14668136,     14668202,     14668062, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     14705887,     14705930,     14705792, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     14672058,     14672117,     14671976, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     14721138,     14721177,     14721067, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     16518436,     16230833,     16046258,     15016515,     14657818,     14382032,     13584217,     13197300,     12879032, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     16554551,     16268290,     16085108,     15044971,     14688230,     14414153,     13606639,     13222039,     12905690, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     16530035,     16242006,     16057102,     15027341,     14668136,     14391934,     13594248,     13206769,     12888044, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     16574387,     16287376,     16103611,     15063554,     14705887,     14431065,     13623870,     13238268,     12921101, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     16535579,     16247518,     16062616,     15031072,     14672058,     14396015,     13596717,     13209560,     12891081, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     16593791,     16306615,     16122770,     15078566,     14721138,     14446523,     13635632,     13250514,     12933712, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     17845904,     12013609, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     17878790,     12044733, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     17858896,     12021507, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     17901083,     12058174, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     17863568,     12025446, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     17919375,     12072192, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     14658867,     14656908,     21234657,     14656484,     14629348,      8723083, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     14689545,     14686879,     21273213,     14686551,     14660469,      8745739, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     14669169,     14667255,     21250067,     14666826,     14639578,      8728828, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     14707158,     14704598,     21299672,     14704265,     14677971,      8755510, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     14673130,     14671102,     21254884,     14670707,     14643610,      8731860, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     14722489,     14719687,     21319912,     14719421,     14693445,      8766066, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    147738620,    147738692,    147738692,    147738616,    147738188,    147738100, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    148014964,    148015036,    148015036,    148014960,    148014540,    148014448, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    147846192,    147846284,    147846284,    147846192,    147845768,    147845680, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    148199268,    148199356,    148199356,    148199272,    148198856,    148198760, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    147883736,    147883808,    147883808,    147883728,    147883296,    147883212, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    148348332,    148348428,    148348428,    148348336,    148347916,    148347828, ],
  }),
  ("nof_tree_events",                 1342723),
  ("nof_db_events",                   19800000),
  ("fsize_local",                     5972116734), # 5.97GB, avg file size 1.99GB
  ("fsize_db",                        1064523714546), # 1.06TB, avg file size 1.97GB
  ("use_it",                          False),
  ("xsection",                        365.52),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTToSemiLeptonic_widthx0p85"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTTo2L2Nu_widthx1p15_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_widthx1p15"),
  ("process_name_specific",           "TTTo2L2Nu_widthx1p15"),
  ("nof_files",                       1),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                                          : [       584000, ],
    'CountWeighted'                                                                  : [       579466,       579468,       579389, ],
    'CountWeightedLHEWeightScale'                                                    : [       652971,       641499,       634073,       593769,       579457,       568390,       537240,       521778,       509074, ],
    'CountWeightedLHEEnvelope'                                                       : [       705713,       474574, ],
    'CountWeightedPSWeight'                                                          : [       579385,       579507,       819515,       579493,       577923,       362131, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [      5839734,      5839666,      5839734,      5839734,      5836344,      5836277, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [       579852,       579881,       579819, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [       581037,       581072,       580997, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [       580261,       580288,       580228, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [       581735,       581770,       581701, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [       580404,       580436,       580369, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [       582317,       582354,       582278, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [       653529,       642131,       634778,       594087,       579835,       568904,       537389,       522052,       509446, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [       654932,       643593,       636303,       595189,       581020,       570161,       538254,       523014,       510489, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [       653985,       642573,       635209,       594513,       580243,       569296,       537787,       522426,       509804, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [       655719,       644350,       637036,       595926,       581717,       570830,       538939,       523658,       511099, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [       654192,       642779,       635413,       594652,       580386,       569444,       537872,       522525,       509912, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [       656461,       645086,       637769,       596496,       582299,       571420,       539380,       524119,       511575, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [       706064,       475179, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [       707343,       476394, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [       706575,       475493, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [       708226,       476929, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [       706744,       475640, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [       708920,       477463, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [       579824,       579908,       819862,       579899,       578389,       362608, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [       581020,       581070,       821300,       581067,       579609,       363552, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [       580230,       580319,       820467,       580310,       578797,       362846, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [       581719,       581773,       822335,       581771,       580308,       363955, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [       580375,       580461,       820634,       580449,       578939,       362964, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [       582305,       582356,       823079,       582342,       580887,       364381, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [      5842839,      5842772,      5842839,      5842839,      5839488,      5839421, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [      5853565,      5853500,      5853565,      5853565,      5850248,      5850182, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [      5847107,      5847040,      5847107,      5847107,      5843751,      5843684, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [      5860881,      5860815,      5860881,      5860881,      5857551,      5857484, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [      5848468,      5848402,      5848468,      5848468,      5845115,      5845048, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [      5866560,      5866495,      5866560,      5866560,      5863236,      5863171, ],
  }),
  ("nof_tree_events",                 220015),
  ("nof_db_events",                   584000),
  ("fsize_local",                     914318170), # 914.32MB, avg file size 914.32MB
  ("fsize_db",                        31109535835), # 31.11GB, avg file size 1.35GB
  ("use_it",                          False),
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_widthx1p15"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTToSemiLeptonic_widthx1p15_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_widthx1p15"),
  ("process_name_specific",           "TTToSemiLeptonic_widthx1p15"),
  ("nof_files",                       2),
  ("nof_db_files",                    546),
  ("nof_events",                      {
    'Count'                                                                          : [     19089000, ],
    'CountWeighted'                                                                  : [     18936427,     18935923,     18933015, ],
    'CountWeightedLHEWeightScale'                                                    : [     21336568,     20962845,     20722574,     19401167,     18936427,     18575827,     17554469,     17050732,     16636459, ],
    'CountWeightedLHEEnvelope'                                                       : [     23058728,     15510719, ],
    'CountWeightedPSWeight'                                                          : [     18934716,     18934739,     27442719,     18934573,     18900998,     11261912, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    190861408,    190861504,    190861504,    190861408,    190860824,    190860728, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     18949203,     18949418,     18948880, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     18988618,     18988899,     18988330, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     18962511,     18962729,     18962229, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     19011453,     19011698,     19011146, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     18967616,     18967818,     18967319, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     19031168,     19031438,     19030878, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     21355522,     20984117,     20746087,     19412429,     18949203,     18593215,     17560117,     17060260,     16649131, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     21402341,     21032664,     20796433,     19449337,     18988618,     18634876,     17589212,     17092346,     16683707, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     21370525,     20998561,     20760108,     19426432,     18962511,     18606008,     17573079,     17072497,     16660773, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     21428009,     21057341,     20820353,     19473347,     19011453,     18656713,     17611478,     17113332,     16703613, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     21377700,     21005703,     20767225,     19431279,     18967616,     18611266,     17576282,     17076102,     16664685, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     21453114,     21082209,     20845125,     19492765,     19031168,     18676673,     17626685,     17129140,     16719897, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     23070975,     15530950, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     23113747,     15571167, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     23087747,     15541175, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     23142547,     15588568, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     23093778,     15546272, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     23166146,     15606719, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     18949581,     18948678,     27456497,     18948622,     18916627,     11276650, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     18989353,     18987515,     27506545,     18987609,     18957005,     11306012, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     18962888,     18962065,     27476420,     18961983,     18929816,     11284082, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     19012111,     19010437,     27540710,     19010507,     18979579,     11318625, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     18968027,     18967094,     27482644,     18967001,     18934971,     11287988, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     19031946,     19030034,     27566902,     19030086,     18999461,     11332255, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    190991928,    190992000,    190992000,    190991928,    190991328,    190991256, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    191349400,    191349480,    191349480,    191349400,    191348816,    191348736, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    191131432,    191131520,    191131520,    191131432,    191130856,    191130776, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    191588064,    191588144,    191588144,    191588064,    191587472,    191587384, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    191179704,    191179776,    191179776,    191179704,    191179088,    191179008, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    191780712,    191780792,    191780792,    191780712,    191780112,    191780040, ],
  }),
  ("nof_tree_events",                 1736053),
  ("nof_db_events",                   19137000),
  ("fsize_local",                     7715895785), # 7.72GB, avg file size 3.86GB
  ("fsize_db",                        1029146761272), # 1.03TB, avg file size 1.88GB
  ("use_it",                          False),
  ("xsection",                        365.52),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTToSemiLeptonic_widthx1p15"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTTo2L2Nu_widthx1p3_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_widthx1p3"),
  ("process_name_specific",           "TTTo2L2Nu_widthx1p3"),
  ("nof_files",                       1),
  ("nof_db_files",                    157),
  ("nof_events",                      {
    'Count'                                                                          : [      4296000, ],
    'CountWeighted'                                                                  : [      4260878,      4262528,      4261854, ],
    'CountWeightedLHEWeightScale'                                                    : [      4802690,      4718185,      4663700,      4366934,      4260815,      4180520,      3951106,      3837496,      3744079, ],
    'CountWeightedLHEEnvelope'                                                       : [      5190134,      3490762, ],
    'CountWeightedPSWeight'                                                          : [      4261706,      4260878,      6030700,      4261277,      4256569,      2663440, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     42958368,     42957984,     42958392,     42958368,     42934596,     42934168, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      4264923,      4264931,      4264926, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      4273875,      4273859,      4273891, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      4267912,      4267922,      4267923, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      4278985,      4278983,      4279000, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      4269075,      4269076,      4269083, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      4283471,      4283454,      4283491, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [      4807018,      4723049,      4669085,      4369529,      4264791,      4184519,      3952443,      3839714,      3747013, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [      4817605,      4734044,      4680511,      4377893,      4273743,      4193980,      3959050,      3847004,      3754872, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [      4810386,      4726290,      4672225,      4372677,      4267782,      4187389,      3955354,      3842458,      3749622, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [      4823370,      4739576,      4685869,      4383285,      4278858,      4198881,      3964049,      3851708,      3759332, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [      4812018,      4727922,      4673856,      4373775,      4268945,      4188606,      3956088,      3843287,      3750525, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [      4829040,      4745219,      4691498,      4387680,      4283341,      4203420,      3967495,      3855305,      3763046, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [      5192972,      3495376, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [      5202675,      3504490, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [      5196744,      3497672, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [      5209142,      3508386, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [      5198124,      3498823, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [      5214508,      3512492, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      4265165,      4264111,      6033601,      4264535,      4260102,      2667079, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      4274195,      4272938,      6044444,      4273362,      4269201,      2674168, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      4268148,      4267111,      6037986,      4267536,      4263074,      2668820, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      4279294,      4278085,      6051989,      4278507,      4274288,      2677131, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      4269317,      4268260,      6039330,      4268683,      4264235,      2669775, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      4283795,      4282540,      6057706,      4282959,      4278764,      2680410, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     42984016,     42983636,     42984036,     42984016,     42960452,     42960040, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     43065248,     43064876,     43065268,     43065248,     43041860,     43041448, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     43015176,     43014800,     43015196,     43015176,     42991576,     42991160, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     43118648,     43118268,     43118664,     43118648,     43095184,     43094768, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     43026088,     43025704,     43026104,     43026088,     43002500,     43002080, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     43162344,     43161968,     43162360,     43162344,     43138912,     43138500, ],
  }),
  ("nof_tree_events",                 1619226),
  ("nof_db_events",                   4796000),
  ("fsize_local",                     6711109674), # 6.71GB, avg file size 6.71GB
  ("fsize_db",                        255489886690), # 255.49GB, avg file size 1.63GB
  ("use_it",                          False),
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_widthx1p3"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/TTToSemiLeptonic_widthx1p3_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_widthx1p3"),
  ("process_name_specific",           "TTToSemiLeptonic_widthx1p3"),
  ("nof_files",                       2),
  ("nof_db_files",                    549),
  ("nof_events",                      {
    'Count'                                                                          : [     19110000, ],
    'CountWeighted'                                                                  : [     18960032,     18957719,     18955746, ],
    'CountWeightedLHEWeightScale'                                                    : [     21359595,     20986276,     20746591,     19421761,     18960032,     18596772,     17572685,     17069048,     16654915, ],
    'CountWeightedLHEEnvelope'                                                       : [     23083200,     15528589, ],
    'CountWeightedPSWeight'                                                          : [     18955130,     18956118,     27471981,     18956032,     18920714,     11274932, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    191088568,    191088624,    191088624,    191088560,    191088000,    191087944, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     18970032,     18969925,     18970071, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     19009566,     19009492,     19009650, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     18983356,     18983249,     18983389, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     19032378,     19032297,     19032448, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     18988399,     18988283,     18988441, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     19052047,     19051944,     19052113, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     21378670,     21007686,     20770280,     19433118,     18970032,     18614283,     17578385,     17078657,     16667687, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     21425602,     21056374,     20820810,     19470089,     19009566,     18656063,     17607539,     17110848,     16702356, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     21393658,     21022126,     20784298,     19447113,     18983356,     18627057,     17591357,     17090897,     16679314, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     21451252,     21081052,     20844710,     19494100,     19032378,     18677902,     17629818,     17131821,     16722263, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     21400792,     21029212,     20791378,     19451887,     18988399,     18632284,     17594505,     17094470,     16683216, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     21476244,     21105843,     20869383,     19513437,     19052047,     18697813,     17644958,     17147580,     16738504, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     23095547,     15548957, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     23138406,     15589306, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     23112318,     15559174, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     23167201,     15606689, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     23118319,     15564225, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     23190756,     15624754, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     18969981,     18970150,     27485880,     18970141,     18936510,     11289796, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     19009839,     19009089,     27536088,     19009263,     18977106,     11319267, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     18983273,     18983541,     27505789,     18983503,     18949712,     11297216, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     19032598,     19032009,     27570271,     19032133,     18999671,     11331884, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     18988343,     18988500,     27512016,     18988501,     18954906,     11301107, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     19052336,     19051504,     27596460,     19051693,     19019639,     11345472, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    191203480,    191203536,    191203536,    191203488,    191202936,    191202880, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    191562496,    191562552,    191562552,    191562496,    191561976,    191561920, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    191342616,    191342680,    191342680,    191342608,    191342064,    191342016, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    191800624,    191800688,    191800688,    191800624,    191800080,    191800008, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    191390448,    191390504,    191390504,    191390448,    191389912,    191389856, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    191992456,    191992496,    191992496,    191992456,    191991912,    191991848, ],
  }),
  ("nof_tree_events",                 1736064),
  ("nof_db_events",                   19260000),
  ("fsize_local",                     7715652994), # 7.72GB, avg file size 3.86GB
  ("fsize_db",                        1035758532665), # 1.04TB, avg file size 1.89GB
  ("use_it",                          False),
  ("xsection",                        365.52),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Apr27_wPresel_nom_hh_bbww_ttbar/ntuples/TTToSemiLeptonic_widthx1p3"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["sum_events"] = [
  [ 'TTTo2L2Nu_hdampDOWN',                             'TTTo2L2Nu_hdampDOWN_ext1',                         ],
  [ 'TTTo2L2Nu_hdampUP',                               'TTTo2L2Nu_hdampUP_ext1',                           ],
  [ 'TTTo2L2Nu_erdON',                                 'TTTo2L2Nu_erdON_ext1',                             ],
  [ 'TTTo2L2Nu_ueDown',                                'TTTo2L2Nu_ueDown_ext1',                            ],
  [ 'TTTo2L2Nu_mtop169p5',                             'TTTo2L2Nu_mtop169p5_ext1',                         ],
  [ 'TTToSemiLeptonic_mtop169p5',                      'TTToSemiLeptonic_mtop169p5_ext1',                  ],
  [ 'TTTo2L2Nu_mtop175p5',                             'TTTo2L2Nu_mtop175p5_ext1',                         ],
  [ 'TTTo2L2Nu_ueUp',                                  'TTTo2L2Nu_ueUp_ext1',                              ],
  [ 'TTToSemiLeptonic_mtop175p5',                      'TTToSemiLeptonic_mtop175p5_ext1',                  ],
]

