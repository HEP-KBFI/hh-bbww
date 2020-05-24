from collections import OrderedDict as OD

# file generated at 2020-05-24 11:17:23 with the following command:
# create_dictionary.py -m python/samples/metaDict_2018_ttbar.py -p /hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples -N samples_2018 -E 2018 -o python/samples -g hhAnalyzeSamples_2018_ttbar_preselected.py -M

samples_2018 = OD()
samples_2018["/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_hdampDown"),
  ("process_name_specific",           "TTTo2L2Nu_hdampDOWN"),
  ("nof_files",                       12),
  ("nof_db_files",                    158),
  ("nof_events",                      {
    'Count'                                                                          : [      5458000, ],
    'CountWeighted'                                                                  : [      5367993,      5368104,      5368526, ],
    'CountWeightedLHEWeightScale'                                                    : [      6048180,      5943082,      5875951,      5499785,      5367993,      5267472,      4976735,      4834639,      4717736, ],
    'CountWeightedLHEEnvelope'                                                       : [      6601341,      4331015, ],
    'CountWeightedPSWeight'                                                          : [      5368335,      5368396,      7589394,      5368339,      5363409,      3362778, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     54573605,     54573147,     54573658,     54573606,     54545468,     54544905, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      5373825,      5373796,      5373843, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      5386314,      5386286,      5386341, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      5377512,      5377479,      5377534, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      5392606,      5392570,      5392626, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      5379183,      5379149,      5379208, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      5398691,      5398652,      5398722, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [      6054337,      5950130,      5883822,      5504157,      5373825,      5273818,      4979675,      4838751,      4722818, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [      6068409,      5964920,      5899322,      5515806,      5386314,      5287058,      4989273,      4849275,      4734117, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [      6058544,      5954158,      5887717,      5508047,      5377512,      5277344,      4983258,      4842117,      4726011, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [      6075584,      5971783,      5905937,      5522454,      5392606,      5293048,      4995404,      4855024,      4739549, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [      6060753,      5956383,      5889960,      5509629,      5379183,      5279083,      4984390,      4843376,      4727370, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [      6083078,      5979261,      5913442,      5528422,      5398691,      5299243,      5000204,      4860020,      4744703, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [      6605596,      4338509, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [      6618617,      4351569, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [      6610352,      4341232, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [      6626759,      4356172, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [      6612193,      4343021, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [      6633779,      4362006, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      5373863,      5373672,      7594795,      5373664,      5369068,      3368062, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      5386448,      5386019,      7610247,      5386037,      5381759,      3377713, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      5377547,      5377373,      7600194,      5377364,      5372725,      3370218, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      5392722,      5392333,      7619479,      5392343,      5387991,      3381359, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      5379220,      5379025,      7602190,      5379021,      5374398,      3371543, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      5398827,      5398382,      7627322,      5398415,      5394098,      3385766, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     54615445,     54614990,     54615496,     54615446,     54587570,     54587010, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     54724597,     54724146,     54724649,     54724598,     54696952,     54696400, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     54654940,     54654486,     54654992,     54654941,     54627018,     54626459, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     54792036,     54791584,     54792088,     54792037,     54764305,     54763750, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     54670174,     54669718,     54670225,     54670175,     54642266,     54641708, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     54850124,     54849672,     54850174,     54850125,     54822411,     54821857, ],
  }),
  ("nof_tree_events",                 2057374),
  ("nof_db_events",                   5458000),
  ("fsize_local",                     8681144954), # 8.68GB, avg file size 723.43MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_hdampDOWN"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       10),
  ("nof_db_files",                    264),
  ("nof_events",                      {
    'Count'                                                                          : [      9952000, ],
    'CountWeighted'                                                                  : [      9788213,      9789155,      9785252, ],
    'CountWeightedLHEWeightScale'                                                    : [     11030324,     10837277,     10713774,     10028487,      9788213,      9603029,      9073599,      8813906,      8600226, ],
    'CountWeightedLHEEnvelope'                                                       : [     12035506,      7898248, ],
    'CountWeightedPSWeight'                                                          : [      9788044,      9789499,     13838771,      9787835,      9778242,      6130523, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     99517153,     99516158,     99517210,     99517153,     99464599,     99463494, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      9797938,      9797902,      9797971, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      9820842,      9820780,      9820925, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      9804650,      9804611,      9804685, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      9832263,      9832209,      9832359, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      9807767,      9807715,      9807821, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      9843532,      9843466,      9843623, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     11041598,     10850207,     10728244,     10036537,      9797938,      9614739,      9079078,      8821547,      8609622, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     11067296,     10877263,     10756614,     10057871,      9820842,      9639007,      9096699,      8840866,      8630367, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     11049253,     10857539,     10735319,     10043618,      9804650,      9621152,      9085597,      8827669,      8615424, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     11080381,     10889754,     10768647,     10069966,      9832263,      9649895,      9107839,      8851310,      8640237, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     11053386,     10861677,     10739477,     10046606,      9807767,      9624383,      9087738,      8830036,      8617971, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     11094255,     10903568,     10782469,     10081027,      9843532,      9661315,      9116747,      8860555,      8649748, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     12043363,      7911999, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     12067192,      7935916, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     12052007,      7916961, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     12082012,      7944291, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     12055454,      7920286, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     12095010,      7955061, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      9798211,      9799265,     13848870,      9797623,      9788669,      6140213, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      9821251,      9821927,     13877265,      9820304,      9811971,      6157866, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      9804909,      9806007,     13858687,      9804353,      9795327,      6144131, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      9832656,      9833401,     13894055,      9831779,      9823313,      6164489, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      9808039,      9809103,     13862474,      9807439,      9798504,      6146577, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      9843966,      9844611,     13908699,      9842976,      9834668,      6172592, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     99586329,     99585347,     99586382,     99586330,     99534258,     99533169, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     99787007,     99786039,     99787060,     99787007,     99735342,     99734267, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     99658238,     99657253,     99658293,     99658238,     99606079,     99604985, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     99909704,     99908727,     99909758,     99909702,     99857883,     99856794, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     99686696,     99685713,     99686750,     99686696,     99634586,     99633494, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    100017235,    100016261,    100017288,    100017234,     99965474,     99964392, ],
  }),
  ("nof_tree_events",                 3751093),
  ("nof_db_events",                   9952000),
  ("fsize_local",                     15810566621), # 15.81GB, avg file size 1.58GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_hdampDOWN_ext1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       54),
  ("nof_db_files",                    695),
  ("nof_events",                      {
    'Count'                                                                          : [     25904000, ],
    'CountWeighted'                                                                  : [     25476039,     25477040,     25477636, ],
    'CountWeightedLHEWeightScale'                                                    : [     28713230,     28208990,     27885630,     26104145,     25475885,     24994027,     23617821,     22940547,     22383221, ],
    'CountWeightedLHEEnvelope'                                                       : [     31327219,     20558508, ],
    'CountWeightedPSWeight'                                                          : [     25476513,     25476137,     36877144,     25476725,     25432435,     15189175, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    259018017,    259018100,    259018102,    259018017,    259017290,    259017202, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     25502630,     25502499,     25502764, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     25562156,     25562030,     25562327, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     25520088,     25519960,     25520241, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     25591932,     25591764,     25592091, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     25528178,     25528036,     25528337, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     25621170,     25621003,     25621374, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     28742384,     28242560,     27923342,     26124955,     25501860,     25024521,     23631957,     22960352,     22407734, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     28809127,     28312914,     27997263,     26180335,     25561387,     25087733,     23677701,     23010607,     22461760, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     28762316,     28261641,     27941765,     26143383,     25519327,     25041209,     23648915,     22976288,     22422845, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     28843153,     28345417,     28028545,     26211824,     25591139,     25116086,     23706701,     23037790,     22487434, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     28773012,     28272401,     27952626,     26151064,     25527399,     25049638,     23654428,     22982416,     22429442, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     28879127,     28381370,     28064627,     26240504,     25620388,     25145848,     23729772,     23061816,     22512210, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     31347697,     20594141, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     31409758,     20656232, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     31370199,     20607064, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     31448291,     20678047, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     31379167,     20615678, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     31482085,     20706004, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     25502966,     25501409,     36905062,     25502180,     25459712,     15212746, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     25562940,     25560283,     36981784,     25561144,     25520384,     15256058, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     25520398,     25518950,     36931140,     25519693,     25477023,     15222484, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     25592627,     25590167,     37026377,     25590989,     25549876,     15272536, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     25528551,     25527004,     36941361,     25527691,     25485185,     15228477, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     25622019,     25619347,     37065575,     25620066,     25579269,     15292442, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    259211850,    259211931,    259211934,    259211849,    259211129,    259211043, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    259733290,    259733373,    259733375,    259733289,    259732580,    259732493, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    259398646,    259398728,    259398730,    259398645,    259397927,    259397840, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    260052300,    260052384,    260052386,    260052299,    260051587,    260051499, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    259472799,    259472884,    259472885,    259472798,    259472084,    259471995, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    260331724,    260331806,    260331809,    260331723,    260331012,    260330924, ],
  }),
  ("nof_tree_events",                 2348627),
  ("nof_db_events",                   25904000),
  ("fsize_local",                     10727775247), # 10.73GB, avg file size 198.66MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTToSemiLeptonic_hdampDOWN"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       53),
  ("nof_db_files",                    729),
  ("nof_events",                      {
    'Count'                                                                          : [     26425000, ],
    'CountWeighted'                                                                  : [     25987208,     25988993,     25986818, ],
    'CountWeightedLHEWeightScale'                                                    : [     29287910,     28773081,     28443001,     26628781,     25987103,     25495356,     24093915,     23402633,     22833758, ],
    'CountWeightedLHEEnvelope'                                                       : [     31955032,     20971446, ],
    'CountWeightedPSWeight'                                                          : [     25987456,     25985870,     38406670,     25988797,     25914890,     14787172, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    264227426,    264227536,    264227536,    264227426,    264226234,    264226123, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     26014471,     26014472,     26014487, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     26075047,     26075048,     26075079, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     26032303,     26032317,     26032309, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     26105441,     26105439,     26105455, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     26040507,     26040532,     26040515, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     26135174,     26135195,     26135207, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     29317498,     28807216,     28481358,     26649854,     26013687,     25526318,     24108166,     23422693,     22858606, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     29385434,     28878854,     28556625,     26706191,     26074268,     25590660,     24154658,     23473788,     22913558, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     29337863,     28826704,     28500174,     26668667,     26031519,     25543360,     24125486,     23438973,     22874029, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     29420180,     28912048,     28588579,     26738350,     26104638,     25619620,     24184274,     23501560,     22939780, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     29348689,     28837616,     28511200,     26676440,     26039717,     25551920,     24131054,     23445173,     22880730, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     29456721,     28948593,     28625274,     26767463,     26134376,     25649884,     24207707,     23525984,     22964979, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     31975777,     21007667, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     32038936,     21070859, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     31998773,     21020850, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     32078297,     21093132, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     32007855,     21029580, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     32112652,     21121544, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     26014266,     26011530,     38436521,     26014680,     25942558,     14809612, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     26075251,     26071438,     38517143,     26074736,     26004255,     14851285, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     26032069,     26029433,     38463602,     26032556,     25960213,     14819150, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     26105579,     26101948,     38563464,     26105226,     26034316,     14867419, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     26040318,     26037571,     38474337,     26040696,     25968523,     14824876, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     26135433,     26131539,     38604476,     26134815,     26064250,     14886596, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    264422813,    264422920,    264422920,    264422813,    264421636,    264421527, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    264952691,    264952797,    264952797,    264952691,    264951526,    264951421, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    264613786,    264613893,    264613893,    264613786,    264612607,    264612498, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    265278506,    265278614,    265278614,    265278507,    265277335,    265277228, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    264688936,    264689045,    264689045,    264688937,    264687757,    264687647, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    265562706,    265562812,    265562812,    265562706,    265561536,    265561428, ],
  }),
  ("nof_tree_events",                 319957),
  ("nof_db_events",                   26425000),
  ("fsize_local",                     1552589967), # 1.55GB, avg file size 29.29MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTToHadronic_hdampDOWN"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       6),
  ("nof_db_files",                    148),
  ("nof_events",                      {
    'Count'                                                                          : [      5260000, ],
    'CountWeighted'                                                                  : [      5236541,      5236735,      5236548, ],
    'CountWeightedLHEWeightScale'                                                    : [      5898357,      5796129,      5730681,      5364203,      5236541,      5137461,      4854094,      4715389,      4601385, ],
    'CountWeightedLHEEnvelope'                                                       : [      6334631,      4329688, ],
    'CountWeightedPSWeight'                                                          : [      5236217,      5235932,      7417329,      5235582,      5228587,      3266010, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     52593365,     52592784,     52593383,     52593366,     52562664,     52562051, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      5238662,      5238684,      5238644, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      5248249,      5248259,      5248248, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      5242453,      5242475,      5242435, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      5254736,      5254757,      5254750, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      5243657,      5243660,      5243646, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      5259767,      5259768,      5259780, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [      5902912,      5801015,      5735923,      5366191,      5238662,      5140775,      4854324,      4716554,      4603313, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [      5915155,      5813437,      5748586,      5375259,      5248249,      5150814,      4861033,      4723965,      4611319, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [      5907102,      5805076,      5739894,      5370141,      5242453,      5144428,      4858010,      4720042,      4606655, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [      5922325,      5820397,      5755378,      5382057,      5254736,      5157075,      4867380,      4729977,      4617060, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [      5908902,      5806869,      5741668,      5371278,      5243657,      5145672,      4858691,      4720840,      4607539, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [      5928895,      5826882,      5761805,      5387006,      5259767,      5162135,      4871162,      4733922,      4621117, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [      6337398,      4333438, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [      6348533,      4342803, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [      6342053,      4336432, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [      6356520,      4347930, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [      6343594,      4337568, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [      6362765,      4352374, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      5238967,      5238537,      7418779,      5238169,      5231430,      3269647, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      5248632,      5248015,      7430043,      5247641,      5241142,      3277515, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      5242748,      5242322,      7424333,      5241955,      5235197,      3271844, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      5255113,      5254523,      7439626,      5254153,      5247620,      3281263, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      5243962,      5243513,      7425679,      5243146,      5236417,      3272875, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      5260167,      5259538,      7445999,      5259144,      5252666,      3284996, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     52618426,     52617851,     52618444,     52618427,     52588016,     52587408, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     52706984,     52706417,     52707000,     52706985,     52676843,     52676244, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     52657444,     52656866,     52657461,     52657444,     52626979,     52626369, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     52773950,     52773380,     52773966,     52773950,     52743706,     52743104, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     52669139,     52668565,     52669156,     52669140,     52638704,     52638098, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     52823602,     52823032,     52823617,     52823602,     52793395,     52792796, ],
  }),
  ("nof_tree_events",                 1984865),
  ("nof_db_events",                   5260000),
  ("fsize_local",                     8472923313), # 8.47GB, avg file size 1.41GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_hdampUP"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       11),
  ("nof_db_files",                    314),
  ("nof_events",                      {
    'Count'                                                                          : [      9903000, ],
    'CountWeighted'                                                                  : [      9859939,      9858692,      9858806, ],
    'CountWeightedLHEWeightScale'                                                    : [     11106530,     10912566,     10787799,     10101093,      9859939,      9671645,      9140563,      8878364,      8662803, ],
    'CountWeightedLHEEnvelope'                                                       : [     11928660,      8150279, ],
    'CountWeightedPSWeight'                                                          : [      9858043,      9859534,     13968383,      9858802,      9845376,      6148674, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     99028407,     99027274,     99028459,     99028401,     98970056,     98968816, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      9863454,      9863408,      9863439, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      9881524,      9881438,      9881563, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      9870588,      9870541,      9870577, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      9893778,      9893695,      9893820, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      9872872,      9872804,      9872892, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      9903271,      9903157,      9903348, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     11115086,     10921784,     10797694,     10104844,      9863454,      9677938,      9141004,      8880590,      8666490, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     11138119,     10945182,     10821581,     10121925,      9881524,      9696886,      9153659,      8894596,      8681611, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     11122977,     10929424,     10805177,     10112289,      9870588,      9684824,      9147940,      8887180,      8672779, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     11151646,     10958290,     10834378,     10134728,      9893778,      9708680,      9165640,      8905935,      8692417, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     11126412,     10932808,     10808515,     10114453,      9872872,      9687178,      9149268,      8888698,      8674461, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     11164073,     10970527,     10846478,     10144123,      9903271,      9718255,      9172805,      8913408,      8700100, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     11933832,      8157423, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     11954756,      8175117, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     11942593,      8163051, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     11969827,      8184757, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     11945526,      8165202, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     11981617,      8193193, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      9863290,      9864299,     13971352,      9863634,      9851133,      6155535, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      9881523,      9882037,     13992778,      9881479,      9869803,      6170374, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      9870408,      9871454,     13981807,      9870786,      9858206,      6159677, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      9893742,      9894337,     14010813,      9893765,      9881953,      6177439, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      9872708,      9873683,     13984418,      9873046,      9860601,      6161639, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      9903298,      9903732,     14022965,      9903203,      9891675,      6184490, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     99065268,     99064148,     99065318,     99065264,     99007518,     99006289, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     99232829,     99231711,     99232877,     99232824,     99175579,     99174360, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     99138827,     99137703,     99138878,     99138822,     99080977,     99079744, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     99358995,     99357877,     99359044,     99358989,     99301557,     99300336, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     99161166,     99160041,     99161214,     99161161,     99103356,     99102120, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     99452852,     99451739,     99452901,     99452851,     99395493,     99394274, ],
  }),
  ("nof_tree_events",                 3734951),
  ("nof_db_events",                   9903000),
  ("fsize_local",                     15943221074), # 15.94GB, avg file size 1.45GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_hdampUP_ext1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       27),
  ("nof_db_files",                    567),
  ("nof_events",                      {
    'Count'                                                                          : [     26764000, ],
    'CountWeighted'                                                                  : [     26645713,     26641597,     26639319, ],
    'CountWeightedLHEWeightScale'                                                    : [     30019952,     29493730,     29154944,     27300351,     26644193,     26137314,     24703008,     23993341,     23410043, ],
    'CountWeightedLHEEnvelope'                                                       : [     32237193,     22029124, ],
    'CountWeightedPSWeight'                                                          : [     26643337,     26645744,     38641013,     26642468,     26584022,     15820114, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    267616879,    267617095,    267617101,    267616878,    267616164,    267615936, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     26656998,     26656931,     26656918, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     26706068,     26705967,     26706093, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     26676188,     26676167,     26676183, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     26739112,     26738982,     26739168, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     26682354,     26682279,     26682315, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     26764623,     26764553,     26764673, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     30043264,     29518888,     29182043,     27310652,     26656163,     26154614,     24704378,     23999622,     23420317, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     30105622,     29582326,     29246844,     27356984,     26705231,     26206079,     24738737,     24037703,     23461425, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     30064550,     29539556,     29202193,     27330751,     26675411,     26173162,     24723122,     24017420,     23437278, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     30142129,     29617715,     29281371,     27391561,     26738302,     26237884,     24771048,     24068277,     23490581, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     30073752,     29548595,     29211176,     27336547,     26681545,     26179491,     24726616,     24021455,     23441751, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     30175542,     29650642,     29313980,     27416749,     26763809,     26263659,     24790296,     24088351,     23511245, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     32251532,     22048567, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     32308341,     22096512, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     32275169,     22063780, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     32349006,     22122557, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     32283048,     22069516, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     32380758,     22145158, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     26657848,     26658950,     38650658,     26655807,     26599586,     15837373, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     26707372,     26707187,     38711380,     26704233,     26649975,     15875114, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     26677045,     26678274,     38679444,     26675103,     26618653,     15848058, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     26740342,     26740346,     38760950,     26737374,     26682713,     15893364, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     26683204,     26684265,     38686723,     26681118,     26624958,     15852960, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     26766008,     26765691,     38794618,     26762736,     26708619,     15911246, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    267738682,    267738895,    267738901,    267738680,    267737982,    267737754, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    268193376,    268193587,    268193592,    268193378,    268192686,    268192459, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    267937035,    267937249,    267937254,    267937036,    267936335,    267936107, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    268533769,    268533984,    268533988,    268533771,    268533075,    268532853, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    267996770,    267996982,    267996988,    267996773,    267996070,    267995841, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    268785955,    268786170,    268786176,    268785954,    268785263,    268785040, ],
  }),
  ("nof_tree_events",                 2439685),
  ("nof_db_events",                   26964000),
  ("fsize_local",                     11223305225), # 11.22GB, avg file size 415.68MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTToSemiLeptonic_hdampUP"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       23),
  ("nof_db_files",                    690),
  ("nof_events",                      {
    'Count'                                                                          : [     22365000, ],
    'CountWeighted'                                                                  : [     22266192,     22264359,     22261769, ],
    'CountWeightedLHEWeightScale'                                                    : [     25082835,     24645316,     24364304,     22811296,     22266192,     21842663,     20641679,     20049963,     19563721, ],
    'CountWeightedLHEEnvelope'                                                       : [     26937373,     18408409, ],
    'CountWeightedPSWeight'                                                          : [     22262852,     22265951,     32969684,     22265038,     22196275,     12618209, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    223666716,    223666858,    223666858,    223666716,    223665730,    223665585, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     22275124,     22275186,     22274934, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     22315839,     22315942,     22315692, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     22291177,     22291295,     22291030, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     22343482,     22343580,     22343328, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     22296236,     22296340,     22296106, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     22364699,     22364835,     22364574, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     25102039,     24666073,     24386676,     22819636,     22275124,     21856859,     20642568,     20054975,     19572066, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     25153871,     24718817,     24440600,     22858078,     22315839,     21899590,     20671023,     20086530,     19606179, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     25119819,     24683334,     24403546,     22836435,     22291177,     21872373,     20658236,     20069833,     19586265, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     25184374,     24748397,     24469468,     22886971,     22343482,     21926233,     20698044,     20112126,     19630580, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     25127434,     24690861,     24410989,     22841228,     22296236,     21877624,     20661096,     20073164,     19589956, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     25212184,     24775816,     24496645,     22907915,     22364699,     21947684,     20714002,     20128774,     19647753, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     26949037,     18424438, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     26996209,     18464277, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     26968798,     18437153, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     27030189,     18486068, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     26975288,     18441905, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     27056584,     18504884, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     22274668,     22276831,     32978361,     22275911,     22208864,     12631520, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     22315804,     22317006,     33030576,     22316092,     22250579,     12661182, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     22290729,     22292976,     33002868,     22292047,     22224813,     12640066, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     22343371,     22344751,     33072776,     22343810,     22277949,     12675791, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     22295836,     22297978,     33009123,     22297015,     22229975,     12643900, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     22364721,     22365880,     33101640,     22364908,     22299413,     12689882, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    223728430,    223728569,    223728569,    223728428,    223727458,    223727317, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    224105537,    224105679,    224105679,    224105537,    224104575,    224104434, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    223894546,    223894688,    223894688,    223894546,    223893569,    223893427, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    224390496,    224390635,    224390635,    224390495,    224389529,    224389386, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    223944102,    223944245,    223944245,    223944103,    223943132,    223942990, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    224600455,    224600593,    224600593,    224600454,    224599490,    224599346, ],
  }),
  ("nof_tree_events",                 270919),
  ("nof_db_events",                   24965000),
  ("fsize_local",                     1315622457), # 1.32GB, avg file size 57.20MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTToHadronic_hdampUP"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       6),
  ("nof_db_files",                    145),
  ("nof_events",                      {
    'Count'                                                                          : [      4954000, ],
    'CountWeighted'                                                                  : [      4914245,      4914558,      4914552, ],
    'CountWeightedLHEWeightScale'                                                    : [      5537771,      5441286,      5379254,      5035194,      4914218,      4821522,      4555599,      4425118,      4317873, ],
    'CountWeightedLHEEnvelope'                                                       : [      5985040,      4025438, ],
    'CountWeightedPSWeight'                                                          : [      4914968,      4914851,      6947471,      4913762,      4905937,      3076389, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     49541691,     49541249,     49541691,     49541691,     49515206,     49514764, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      4918284,      4918252,      4918300, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      4928614,      4928564,      4928663, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      4921729,      4921708,      4921754, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      4934520,      4934477,      4934569, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      4923057,      4923034,      4923089, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      4939656,      4939615,      4939705, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [      5542781,      5446920,      5385477,      5038197,      4918129,      4826140,      4557146,      4427688,      4321267, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [      5555002,      5459605,      5398660,      5047856,      4928462,      4837064,      4564779,      4436107,      4330340, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [      5546663,      5450647,      5389107,      5041829,      4921575,      4829461,      4560511,      4430851,      4324281, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [      5561648,      5465980,      5404847,      5054078,      4934366,      4842715,      4570542,      4441534,      4335489, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [      5548525,      5452510,      5390969,      5043085,      4922908,      4830835,      4561337,      4431798,      4325313, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [      5568164,      5472465,      5411306,      5059114,      4939506,      4847932,      4574501,      4445658,      4339747, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [      5988335,      4030789, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [      5999526,      4041313, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [      5992679,      4033431, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [      6006984,      4045808, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [      5994250,      4034761, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [      6013131,      4050538, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      4918924,      4918572,      6950906,      4917543,      4910109,      3080570, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      4929330,      4928761,      6963504,      4927768,      4920701,      3088736, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      4922375,      4922040,      6955952,      4921003,      4913526,      3082588, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      4935217,      4934692,      6972177,      4933694,      4926545,      3092160, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      4923704,      4923353,      6957520,      4922319,      4914896,      3083674, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      4940380,      4939796,      6978787,      4938796,      4931760,      3095918, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     49567665,     49567227,     49567665,     49567665,     49541432,     49540993, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     49661602,     49661170,     49661602,     49661602,     49635578,     49635143, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     49603803,     49603363,     49603803,     49603803,     49577525,     49577086, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     49723350,     49722916,     49723350,     49723350,     49697242,     49696803, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     49616469,     49616033,     49616469,     49616469,     49590211,     49589772, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     49773628,     49773196,     49773628,     49773628,     49747543,     49747108, ],
  }),
  ("nof_tree_events",                 1867796),
  ("nof_db_events",                   4954000),
  ("fsize_local",                     7922394846), # 7.92GB, avg file size 1.32GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_ueDown"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       10),
  ("nof_db_files",                    269),
  ("nof_events",                      {
    'Count'                                                                          : [      9816000, ],
    'CountWeighted'                                                                  : [      9738718,      9736236,      9734080, ],
    'CountWeightedLHEWeightScale'                                                    : [     10971489,     10779268,     10655645,      9976666,      9738186,      9551973,      9027205,      8768020,      8554930, ],
    'CountWeightedLHEEnvelope'                                                       : [     11857237,      7975936, ],
    'CountWeightedPSWeight'                                                          : [      9736695,      9735929,     13769581,      9736687,      9725544,      6094235, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     98145641,     98144718,     98145665,     98145643,     98093209,     98092239, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      9743941,      9743958,      9743865, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      9764092,      9764106,      9764010, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      9750816,      9750835,      9750741, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      9775852,      9775856,      9775770, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      9753392,      9753395,      9753322, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      9785917,      9785933,      9785833, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     10981114,     10790053,     10667580,      9982342,      9743639,      9560762,      9029988,      8772788,      8561307, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     11005060,     10814865,     10693293,     10001192,      9763793,      9582017,      9044844,      8789181,      8578952, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     10988846,     10797503,     10674803,      9989562,      9750518,      9567346,      9036676,      8779113,      8567306, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     11018276,     10827580,     10705627,     10013568,      9775557,      9593285,      9056311,      8799994,      8589215, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     10992485,     10801128,     10678426,      9991997,      9753095,      9570017,      9038283,      8780934,      8569298, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     11031090,     10840285,     10718272,     10023470,      9785618,      9603475,      9064064,      8808057,      8597534, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     11863353,      7986275, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     11885159,      8006867, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     11872013,      7991538, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     11900015,      8015817, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     11875085,      7994110, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     11912089,      8025072, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      9744132,      9743011,     13775830,      9743770,      9733374,      6102333, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      9764424,      9762896,     13800277,      9763700,      9753937,      6118324, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      9751001,      9749905,     13785888,      9750660,      9740186,      6106341, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      9776163,      9774700,     13817559,      9775497,      9765602,      6125140, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      9753587,      9752445,     13788886,      9753209,      9742797,      6108467, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      9786269,      9784717,     13830442,      9785510,      9775757,      6132530, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     98211500,     98210589,     98211523,     98211501,     98159512,     98158554, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     98394282,     98393379,     98394304,     98394282,     98342686,     98341739, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     98283185,     98282270,     98283209,     98283185,     98231101,     98230138, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     98517086,     98516181,     98517109,     98517087,     98465331,     98464380, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     98307682,     98306769,     98307703,     98307682,     98255630,     98254672, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     98615264,     98614360,     98615285,     98615264,     98563541,     98562590, ],
  }),
  ("nof_tree_events",                 3704641),
  ("nof_db_events",                   9816000),
  ("fsize_local",                     15710662695), # 15.71GB, avg file size 1.57GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_ueDown_ext1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       41),
  ("nof_db_files",                    536),
  ("nof_events",                      {
    'Count'                                                                          : [     20483000, ],
    'CountWeighted'                                                                  : [     20314116,     20317805,     20316579, ],
    'CountWeightedLHEWeightScale'                                                    : [     22892630,     22492643,     22235658,     20816165,     20314116,     19931926,     18834620,     18294763,     17850787, ],
    'CountWeightedLHEEnvelope'                                                       : [     24740287,     16643365, ],
    'CountWeightedPSWeight'                                                          : [     20316587,     20314202,     29425048,     20315812,     20284281,     12102437, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    204801066,    204801236,    204801236,    204801062,    204800553,    204800379, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     20332021,     20331948,     20332095, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     20374394,     20374300,     20374510, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     20346315,     20346233,     20346383, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     20398848,     20398763,     20398947, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     20351780,     20351687,     20351855, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     20420067,     20419942,     20420199, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     22913088,     22515525,     22260877,     20828410,     20332021,     19950625,     18840848,     18305063,     17864476, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     22963406,     22567644,     22314898,     20868149,     20374394,     19995370,     18872230,     18339610,     17901656, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     22929147,     22531008,     22275906,     20843400,     20346315,     19964347,     18854729,     18318176,     17876953, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     22990881,     22594088,     22340539,     20893868,     20398848,     20018791,     18896078,     18362089,     17922996, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     22936871,     22538669,     22283548,     20848620,     20351780,     19970010,     18858205,     18322081,     17881191, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     23017868,     22620808,     22367112,     20914765,     20420067,     20040248,     18912470,     18379131,     17940523, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     24753519,     16665208, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     24799477,     16708468, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     24771500,     16676153, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     24830329,     16727106, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     24778004,     16681648, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     24855742,     16746608, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     20332726,     20329265,     29439740,     20331097,     20301003,     12118424, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     20375478,     20371055,     29493286,     20373015,     20344317,     12150101, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     20346983,     20343607,     29461096,     20345425,     20315182,     12126390, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     20399871,     20395587,     29529945,     20397538,     20368571,     12163637, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     20352492,     20348974,     29467776,     20350844,     20320788,     12130617, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     20421177,     20416599,     29558058,     20418632,     20390052,     12178334, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    204940644,    204940813,    204940813,    204940641,    204940136,    204939964, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    205325559,    205325728,    205325728,    205325558,    205325059,    205324886, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    205090027,    205090196,    205090196,    205090026,    205089520,    205089347, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    205581185,    205581355,    205581355,    205581183,    205580680,    205580508, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    205142389,    205142561,    205142561,    205142388,    205141881,    205141707, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    205788892,    205789062,    205789062,    205788889,    205788393,    205788220, ],
  }),
  ("nof_tree_events",                 1869537),
  ("nof_db_events",                   20483000),
  ("fsize_local",                     8577162506), # 8.58GB, avg file size 209.20MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTToSemiLeptonic_ueDown"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       56),
  ("nof_db_files",                    702),
  ("nof_events",                      {
    'Count'                                                                          : [     26627000, ],
    'CountWeighted'                                                                  : [     26412259,     26412411,     26413217, ],
    'CountWeightedLHEWeightScale'                                                    : [     29759627,     29238779,     28903785,     27062597,     26412259,     25911478,     24487861,     23785334,     23207616, ],
    'CountWeightedLHEEnvelope'                                                       : [     32163374,     21636106, ],
    'CountWeightedPSWeight'                                                          : [     26412601,     26410261,     39058447,     26411422,     26341936,     15015426, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    266250557,    266250767,    266250767,    266250554,    266249529,    266249321, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     26432421,     26432449,     26432342, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     26487596,     26487647,     26487492, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     26450982,     26451020,     26450922, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     26519365,     26519422,     26519290, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     26458113,     26458141,     26458044, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     26546992,     26547053,     26546891, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     29786325,     29268709,     28936836,     27078512,     26432421,     25935936,     24495893,     23798760,     23225480, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     29851828,     29336638,     29007322,     27130156,     26487596,     25994239,     24536621,     23843689,     23273875, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     29807204,     29288830,     28956375,     27098015,     26450982,     25953762,     24513959,     23815809,     23241701, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     29887563,     29371005,     29040632,     27163615,     26519365,     26024676,     24567647,     23872910,     23301616, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     29817261,     29298840,     28966375,     27104789,     26458113,     25961157,     24518440,     23820882,     23247215, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     29922679,     29405840,     29075322,     27190774,     26546992,     26052650,     24588917,     23895064,     23324432, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     32180676,     21664589, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     32240520,     21720899, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     32204045,     21678830, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     32280634,     21745129, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     32212531,     21685974, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     32313726,     21770514, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     26433557,     26429993,     39079137,     26431319,     26363754,     15034885, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     26489190,     26484440,     39151380,     26485906,     26420113,     15073819, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     26452093,     26448623,     39107407,     26449944,     26382174,     15044793, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     26520914,     26516335,     39199914,     26517781,     26451619,     15090667, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     26459282,     26455644,     39116480,     26456983,     26389468,     15049971, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     26548653,     26543726,     39237630,     26545220,     26479526,     15108753, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    266414668,    266414874,    266414874,    266414667,    266413651,    266413439, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    266916182,    266916386,    266916387,    266916180,    266915174,    266914966, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    266608712,    266608920,    266608920,    266608710,    266607695,    266607482, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    267248161,    267248366,    267248367,    267248160,    267247151,    267246940, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    266676852,    266677058,    266677058,    266676850,    266675835,    266675626, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    267517874,    267518081,    267518081,    267517873,    267516864,    267516656, ],
  }),
  ("nof_tree_events",                 326309),
  ("nof_db_events",                   26675000),
  ("fsize_local",                     1592054015), # 1.59GB, avg file size 28.43MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTToHadronic_ueDown"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       6),
  ("nof_db_files",                    165),
  ("nof_events",                      {
    'Count'                                                                          : [      5446000, ],
    'CountWeighted'                                                                  : [      5402764,      5401928,      5402189, ],
    'CountWeightedLHEWeightScale'                                                    : [      6087083,      5980268,      5911723,      5534984,      5402645,      5299368,      5008167,      4864395,      4746205, ],
    'CountWeightedLHEEnvelope'                                                       : [      6577808,      4425606, ],
    'CountWeightedPSWeight'                                                          : [      5401631,      5403697,      7659635,      5401981,      5392783,      3363426, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     54458210,     54457566,     54458246,     54458208,     54423475,     54422757, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      5406042,      5406052,      5406006, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      5417404,      5417435,      5417348, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      5409836,      5409843,      5409790, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      5423884,      5423907,      5423830, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      5411280,      5411284,      5411243, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      5429512,      5429543,      5429454, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [      6092652,      5986500,      5918573,      5538329,      5405874,      5304444,      5009881,      4867207,      4749902, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [      6106162,      6000494,      5933077,      5548967,      5417233,      5316428,      5018271,      4876448,      4759850, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [      6096911,      5990607,      5922559,      5542304,      5409670,      5308078,      5013569,      4870686,      4753221, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [      6113447,      6007506,      5939864,      5555800,      5423720,      5322636,      5024608,      4882417,      4765508, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [      6098971,      5992647,      5924586,      5543680,      5411115,      5309577,      5014472,      4871707,      4754330, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [      6120616,      6014605,      5946931,      5561337,      5429346,      5328327,      5028935,      4886921,      4770144, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [      6581459,      4431474, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [      6593806,      4443043, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [      6586229,      4434387, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [      6601981,      4447988, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [      6587951,      4435834, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [      6608726,      4453164, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      5405987,      5407794,      7663368,      5406094,      5397311,      3368008, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      5417439,      5418992,      7677213,      5417310,      5408901,      3376941, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      5409770,      5411608,      7668927,      5409891,      5401076,      3370209, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      5423907,      5425509,      7686764,      5423827,      5415334,      3380681, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      5411222,      5413027,      7670622,      5411320,      5402544,      3371391, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      5429560,      5431109,      7694001,      5429399,      5421021,      3384785, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     54490673,     54490036,     54490709,     54490672,     54456240,     54455527, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     54593960,     54593323,     54593993,     54593959,     54559779,     54559076, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     54530244,     54529602,     54530281,     54530244,     54495753,     54495041, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     54661702,     54661070,     54661738,     54661702,     54627429,     54626723, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     54543941,     54543304,     54543977,     54543941,     54509488,     54508777, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     54716620,     54715983,     54716653,     54716618,     54682388,     54681685, ],
  }),
  ("nof_tree_events",                 2054647),
  ("nof_db_events",                   5446000),
  ("fsize_local",                     8727049227), # 8.73GB, avg file size 1.45GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_ueUp"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       10),
  ("nof_db_files",                    294),
  ("nof_events",                      {
    'Count'                                                                          : [      9968000, ],
    'CountWeighted'                                                                  : [      9888753,      9885975,      9886184, ],
    'CountWeightedLHEWeightScale'                                                    : [     11141238,     10946028,     10820652,     10130759,      9888183,      9699908,      9166645,      8903633,      8687285, ],
    'CountWeightedLHEEnvelope'                                                       : [     12040615,      8099358, ],
    'CountWeightedPSWeight'                                                          : [      9887508,      9887875,     14018166,      9886892,      9872846,      6157265, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     99674287,     99673082,     99674360,     99674287,     99611805,     99610461, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      9894610,      9894534,      9894649, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      9914984,      9914893,      9915072, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      9901583,      9901508,      9901628, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      9926943,      9926829,      9927013, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      9904210,      9904149,      9904278, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      9937180,      9937081,      9937284, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     11150912,     10956898,     10832648,     10136453,      9894307,      9708722,      9169403,      8908400,      8693671, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     11175158,     10982016,     10858681,     10155530,      9914692,      9730238,      9184405,      8924962,      8711523, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     11158766,     10964452,     10839987,     10143777,      9901279,      9715426,      9176193,      8914807,      8699780, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     11188584,     10994935,     10871217,     10168103,      9926631,      9741687,      9196070,      8935945,      8721954, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     11162480,     10968155,     10843675,     10146276,      9903909,      9718157,      9177843,      8916675,      8701811, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     11201620,     11007854,     10884070,     10178193,      9936876,      9752064,      9203986,      8944187,      8730428, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     12046716,      8109759, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     12068779,      8130618, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     12055512,      8115114, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     12083853,      8139725, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     12058634,      8117757, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     12096130,      8149159, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      9895008,      9895020,     14024450,      9893985,      9880639,      6165350, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      9915562,      9915185,     14049316,      9914125,      9901414,      6181424, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      9901992,      9902026,     14034691,      9900995,      9887584,      6169407, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      9927480,      9927168,     14066899,      9926121,      9913278,      6188323, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      9904630,      9904630,     14037816,      9903579,      9890276,      6171551, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      9937803,      9937389,     14080156,      9936296,      9923655,      6195772, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     99731410,     99730214,     99731479,     99731409,     99669475,     99668149, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     99916474,     99915293,     99916540,     99916473,     99855011,     99853699, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     99804437,     99803241,     99804507,     99804436,     99742400,     99741069, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    100041264,    100040080,    100041331,    100041264,     99979612,     99978292, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     99829524,     99828330,     99829593,     99829523,     99767519,     99766186, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    100141687,    100140503,    100141753,    100141685,    100080069,    100078753, ],
  }),
  ("nof_tree_events",                 3754595),
  ("nof_db_events",                   9968000),
  ("fsize_local",                     15947663391), # 15.95GB, avg file size 1.59GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_ueUp_ext1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       57),
  ("nof_db_files",                    722),
  ("nof_events",                      {
    'Count'                                                                          : [     26948000, ],
    'CountWeighted'                                                                  : [     26727094,     26732661,     26729134, ],
    'CountWeightedLHEWeightScale'                                                    : [     30117030,     29590856,     29253185,     27387335,     26727094,     26224066,     24781855,     24071616,     23487462, ],
    'CountWeightedLHEEnvelope'                                                       : [     32550760,     21895969, ],
    'CountWeightedPSWeight'                                                          : [     26729932,     26731692,     38796725,     26729413,     26672369,     15846434, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    269478862,    269479028,    269479032,    269478863,    269477538,    269477362, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     26749899,     26749871,     26749917, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     26805166,     26805120,     26805225, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     26768753,     26768731,     26768789, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     26837465,     26837409,     26837495, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     26775796,     26775774,     26775817, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     26865048,     26865010,     26865104, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     30143432,     29620513,     29285977,     27402875,     26749899,     26248226,     24789475,     24084658,     23505011, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     30209136,     29688653,     29356677,     27454607,     26805166,     26306659,     24830191,     24129616,     23553478, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     30164629,     29640937,     29305808,     27422681,     26768753,     26266325,     24807805,     24101974,     23521481, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     30245410,     29723554,     29390497,     27488562,     26837465,     26337568,     24861701,     24159298,     23581646, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     30174620,     29650876,     29315730,     27429362,     26775796,     26273634,     24812206,     24106960,     23526917, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     30280561,     29758404,     29425198,     27515724,     26865048,     26365516,     24882931,     24181421,     23604441, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     32567581,     21924320, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     32627475,     21980863, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     32591317,     21938775, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     32668204,     22005458, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     32599683,     21945877, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     32701257,     22030887, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     26750624,     26751001,     38815884,     26749066,     26694223,     15866950, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     26806357,     26805484,     38886261,     26803768,     26751040,     15908021, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     26769439,     26769942,     38844091,     26767978,     26712896,     15877417, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     26838560,     26837911,     38934698,     26836127,     26782982,     15925819, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     26776540,     26776901,     38852811,     26774939,     26720162,     15882836, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     26866282,     26865329,     38971582,     26863573,     26811021,     15944814, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    269620242,    269620405,    269620409,    269620243,    269618935,    269618762, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    270121612,    270121773,    270121777,    270121613,    270120319,    270120148, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    269817082,    269817245,    269817249,    269817082,    269815770,    269815595, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    270458926,    270459088,    270459092,    270458927,    270457627,    270457452, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    269884564,    269884726,    269884729,    269884566,    269883254,    269883080, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    270728507,    270728668,    270728672,    270728509,    270727206,    270727035, ],
  }),
  ("nof_tree_events",                 2442560),
  ("nof_db_events",                   26948000),
  ("fsize_local",                     11237503188), # 11.24GB, avg file size 197.15MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTToSemiLeptonic_ueUp"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       49),
  ("nof_db_files",                    634),
  ("nof_events",                      {
    'Count'                                                                          : [     23488000, ],
    'CountWeighted'                                                                  : [     23296898,     23298658,     23300092, ],
    'CountWeightedLHEWeightScale'                                                    : [     26254885,     25794960,     25499334,     23873043,     23296898,     22857463,     21600525,     20980840,     20471118, ],
    'CountWeightedLHEEnvelope'                                                       : [     28372316,     19087367, ],
    'CountWeightedPSWeight'                                                          : [     23298717,     23298155,     34523428,     23299187,     23230100,     13185660, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    234887653,    234887694,    234887699,    234887653,    234886184,    234886131, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     23316757,     23316684,     23316869, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     23365115,     23365067,     23365219, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     23333177,     23333080,     23333268, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     23393205,     23393131,     23393306, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     23339348,     23339277,     23339452, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     23417354,     23417290,     23417451, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     26277957,     25820945,     25528120,     23886709,     23316757,     22878756,     21607336,     20992432,     20486648, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     26335299,     25880478,     25589935,     23931935,     23365115,     22929905,     21642993,     21031809,     20529114, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     26296427,     25838731,     25545384,     23903957,     23333177,     22894494,     21623294,     21007497,     20500973, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     26366910,     25910863,     25619371,     23961502,     23393205,     22956790,     21670410,     21057623,     20553603, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     26305189,     25847441,     25554064,     23909829,     23339348,     22900911,     21627171,     21011875,     20505749, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     26397635,     25941336,     25649711,     23985264,     23417354,     22981245,     21688999,     21076991,     20573548, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     28387126,     19112237, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     28439488,     19161669, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     28407792,     19124817, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     28474952,     19183079, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     28415144,     19131044, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     28503858,     19205312, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     23316907,     23315283,     34541418,     23316531,     23249039,     13202492, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     23365649,     23363050,     34604971,     23364418,     23298426,     13236432, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     23333286,     23331772,     34566415,     23332976,     23265274,     13211214, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     23393672,     23391261,     34647878,     23392585,     23326201,     13251269, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     23339516,     23337858,     34574284,     23339099,     23271598,     13215700, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     23417928,     23415226,     34680940,     23416586,     23350605,     13267038, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    235005455,    235005496,    235005500,    235005454,    235004007,    235003957, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    235445296,    235445337,    235445341,    235445294,    235443869,    235443818, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    235176840,    235176880,    235176885,    235176839,    235175393,    235175343, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    235738565,    235738606,    235738610,    235738565,    235737131,    235737080, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    235235770,    235235812,    235235817,    235235770,    235234322,    235234272, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    235974425,    235974463,    235974468,    235974424,    235972995,    235972942, ],
  }),
  ("nof_tree_events",                 283511),
  ("nof_db_events",                   23488000),
  ("fsize_local",                     1384891739), # 1.38GB, avg file size 28.26MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTToHadronic_ueUp"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       15),
  ("nof_db_files",                    353),
  ("nof_events",                      {
    'Count'                                                                          : [     14756000, ],
    'CountWeighted'                                                                  : [     14640943,     14640662,     14637298, ],
    'CountWeightedLHEWeightScale'                                                    : [     16491820,     16204382,     16020039,     14996916,     14640792,     14360853,     13569928,     13181384,     12862017, ],
    'CountWeightedLHEEnvelope'                                                       : [     17824856,     11990301, ],
    'CountWeightedPSWeight'                                                          : [     14637709,     14638076,     20847862,     14636998,     14613426,      9037427, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    147575343,    147572490,    147575509,    147575339,    147444278,    147441089, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     14648389,     14648389,     14648340, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     14678734,     14678692,     14678729, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     14658701,     14658691,     14658642, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     14696368,     14696337,     14696365, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     14662529,     14662515,     14662468, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     14711419,     14711391,     14711426, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     16506307,     16220694,     16038056,     15005471,     14647940,     14374157,     13574143,     13188621,     12871688, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     16542316,     16258040,     16076829,     15033839,     14678271,     14406212,     13596468,     13213298,     12898301, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     16517898,     16231839,     16048913,     15016288,     14658251,     14384050,     13584172,     13198098,     12880703, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     16562144,     16277108,     16095329,     15052397,     14695934,     14423112,     13613711,     13229530,     12913692, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     16523343,     16237245,     16054302,     15019923,     14662079,     14388028,     13586553,     13200798,     12883656, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     16581342,     16296131,     16114252,     15067218,     14710968,     14438360,     13625296,     13241588,     12926123, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     17834116,     12005882, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     17866953,     12036900, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     17847090,     12013788, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     17889214,     12050342, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     17851643,     12017656, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     17907254,     12064213, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     14648967,     14648678,     20857706,     14647677,     14625535,      9049445, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     14679549,     14678552,     20895106,     14677711,     14656761,      9073181, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     14659252,     14659041,     20872873,     14658032,     14635740,      9055391, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     14697142,     14696272,     20921136,     14695409,     14674223,      9083282, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     14663111,     14662815,     20877375,     14661814,     14639650,      9058531, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     14712255,     14711194,     20940555,     14710359,     14689449,      9094219, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    147637823,    147634996,    147637986,    147637816,    147507831,    147504679, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    147913003,    147910201,    147913163,    147912997,    147783792,    147780665, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    147745523,    147742695,    147745685,    147745519,    147615345,    147612183, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    148097418,    148094611,    148097578,    148097413,    147967868,    147964735, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    147781808,    147778982,    147781974,    147781802,    147651725,    147648572, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    148244311,    148241504,    148244474,    148244307,    148114909,    148111778, ],
  }),
  ("nof_tree_events",                 5604300),
  ("nof_db_events",                   14756000),
  ("fsize_local",                     23878278046), # 23.88GB, avg file size 1.59GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_QCDbased"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       54),
  ("nof_db_files",                    647),
  ("nof_events",                      {
    'Count'                                                                          : [     26692000, ],
    'CountWeighted'                                                                  : [     26476043,     26475636,     26476385, ],
    'CountWeightedLHEWeightScale'                                                    : [     29831260,     29310176,     28975686,     27126576,     26476043,     25974523,     24545153,     23841766,     23263213, ],
    'CountWeightedLHEEnvelope'                                                       : [     32240141,     21688841, ],
    'CountWeightedPSWeight'                                                          : [     26475308,     26475762,     38577306,     26475284,     26405093,     15566017, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    266924501,    266924640,    266924644,    266924504,    266921677,    266921528, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     26496032,     26496025,     26496020, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     26551526,     26551531,     26551517, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     26514663,     26514643,     26514641, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     26583394,     26583368,     26583378, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     26521731,     26521730,     26521715, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     26610943,     26610939,     26610932, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     29858227,     29340396,     29009065,     27142712,     26496032,     25999249,     24553409,     23855395,     23281307, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     29924058,     29408723,     29079942,     27194680,     26551526,     26057884,     24594404,     23900582,     23329993, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     29879160,     29360567,     29028628,     27162281,     26514663,     26017111,     24571508,     23872481,     23297565, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     29959891,     29443157,     29113311,     27228210,     26583394,     26088388,     24625514,     23929885,     23357786, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     29889166,     29370526,     29038579,     27169006,     26521731,     26024476,     24575966,     23877500,     23303049, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     29994927,     29477912,     29147929,     27255326,     26610943,     26116303,     24646736,     23951984,     23380568, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     32257757,     21717519, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     32317987,     21774084, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     32281184,     21731788, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     32358193,     21798371, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     32289608,     21738907, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     32391185,     21823741, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     26496520,     26495739,     38597415,     26495381,     26427249,     15586618, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     26552518,     26550521,     38668449,     26550248,     26483992,     15627393, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     26515107,     26514444,     38625381,     26514045,     26445684,     15596872, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     26584292,     26582522,     38716449,     26582202,     26515530,     15644813, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     26522260,     26521439,     38634140,     26521036,     26452906,     15602271, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     26612009,     26609909,     38753290,     26609550,     26543337,     15663631, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    267066980,    267067118,    267067123,    267066982,    267064198,    267064052, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    267571069,    267571206,    267571212,    267571071,    267568333,    267568185, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    267261342,    267261480,    267261486,    267261345,    267258557,    267258409, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    267904096,    267904236,    267904240,    267904098,    267901346,    267901198, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    267329106,    267329244,    267329249,    267329108,    267326321,    267326174, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    268172958,    268173096,    268173101,    268172960,    268170207,    268170061, ],
  }),
  ("nof_tree_events",                 2517070),
  ("nof_db_events",                   26692000),
  ("fsize_local",                     11651216738), # 11.65GB, avg file size 215.76MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTToSemiLeptonic_QCDbased"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       26),
  ("nof_db_files",                    704),
  ("nof_events",                      {
    'Count'                                                                          : [     25150000, ],
    'CountWeighted'                                                                  : [     24947966,     24944541,     24939691, ],
    'CountWeightedLHEWeightScale'                                                    : [     28108393,     27617037,     27301268,     25560272,     24947966,     24473975,     23128235,     22464994,     21919705, ],
    'CountWeightedLHEEnvelope'                                                       : [     30378338,     20435819, ],
    'CountWeightedPSWeight'                                                          : [     24947053,     24947704,     37103039,     24945056,     24856382,     13998457, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    251467126,    251467290,    251467299,    251467129,    251462881,    251462695, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     24965301,     24965478,     24965050, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     25017211,     25017368,     25017025, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     24982853,     24983029,     24982637, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     25047288,     25047421,     25047092, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     24989449,     24989583,     24989236, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     25073003,     25073146,     25072839, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     28133398,     27645067,     27332105,     25575129,     24965301,     24496785,     23135661,     22477501,     21936307, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     28195028,     27708917,     27398325,     25623732,     25017211,     24551549,     23173965,     22519708,     21981771, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     28153154,     27664106,     27350605,     25593591,     24982853,     24513644,     23152754,     22493630,     21951658, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     28228828,     27741449,     27429840,     25655364,     25047288,     24580362,     23203311,     22547381,     22008038, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     28162452,     27673331,     27359825,     25599786,     24989449,     24520467,     23156842,     22498268,     21956746, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     28261565,     27773907,     27462190,     25680669,     25073003,     24606438,     23223125,     22568017,     22029309, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     30394371,     20462566, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     30450536,     20515597, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     30416494,     20476033, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     30488495,     20538527, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     30424280,     20482657, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     30519292,     20562224, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     24966567,     24966076,     37122861,     24963558,     24877097,     14016370, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     25018849,     25017248,     37191579,     25014902,     24930322,     14052455, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     24984116,     24983739,     37149684,     24981176,     24894432,     14025639, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     25048875,     25047448,     37237629,     25045059,     24960000,     14068209, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     24990723,     24990202,     37158016,     24987647,     24901105,     14030381, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     25074731,     25073003,     37272952,     25070640,     24985925,     14084901, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    251634737,    251634903,    251634911,    251634738,    251630521,    251630339, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    252105642,    252105807,    252105816,    252105646,    252101465,    252101283, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    251818284,    251818448,    251818458,    251818287,    251814063,    251813880, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    252419610,    252419771,    252419780,    252419613,    252415413,    252415233, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    251880732,    251880895,    251880905,    251880734,    251876519,    251876335, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    252671161,    252671328,    252671336,    252671164,    252666974,    252666790, ],
  }),
  ("nof_tree_events",                 322654),
  ("nof_db_events",                   27350000),
  ("fsize_local",                     1571103240), # 1.57GB, avg file size 60.43MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTToHadronic_QCDbased"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       16),
  ("nof_db_files",                    388),
  ("nof_events",                      {
    'Count'                                                                          : [     14958000, ],
    'CountWeighted'                                                                  : [     14838551,     14834775,     14833493, ],
    'CountWeightedLHEWeightScale'                                                    : [     16717883,     16425170,     16236812,     15201832,     14838358,     14554946,     13754848,     13360219,     13035687, ],
    'CountWeightedLHEEnvelope'                                                       : [     18067163,     12153708, ],
    'CountWeightedPSWeight'                                                          : [     14836442,     14837015,     20985732,     14836144,     14820104,      9285007, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    149542579,    149541111,    149542694,    149542579,    149460020,    149458321, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     14847769,     14847915,     14847574, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     14878770,     14878971,     14878574, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     14858184,     14858331,     14858020, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     14896610,     14896822,     14896427, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     14862139,     14862295,     14861986, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     14912027,     14912271,     14911813, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     16732901,     16441965,     16255379,     15210818,     14847313,     14568688,     13759430,     13367819,     13045728, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     16769719,     16480106,     16294910,     15239876,     14878316,     14601410,     13782358,     13393087,     13072923, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     16744625,     16453263,     16266332,     15221779,     14857738,     14578692,     13769567,     13377385,     13054844, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     16789765,     16499401,     16313613,     15258657,     14896138,     14618500,     13799772,     13409475,     13088488, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     16750216,     16458824,     16271869,     15225543,     14861684,     14582780,     13772059,     13380183,     13057892, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     16809387,     16518830,     16332938,     15273848,     14911571,     14634096,     13811674,     13421839,     13101230, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     18076901,     12169724, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     18110526,     12201369, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     18090027,     12177718, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     18133032,     12214962, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     18094732,     12181689, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     18151494,     12229152, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     14848180,     14848208,     20995716,     14847271,     14832269,      9297525, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     14879415,     14878885,     21033437,     14877979,     14863823,      9322065, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     14858582,     14858669,     21010989,     14857732,     14842630,      9303617, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     14897218,     14896782,     21059661,     14895877,     14881578,      9332410, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     14862561,     14862561,     21015637,     14861633,     14846704,      9306866, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     14912694,     14912056,     21079463,     14911198,     14897229,      9343716, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    149661962,    149660504,    149662075,    149661963,    149580074,    149578392, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    149943948,    149942500,    149944061,    149943949,    149862723,    149861046, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    149770797,    149769339,    149770911,    149770798,    149688779,    149687089, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    150130232,    150128778,    150130346,    150130233,    150048767,    150047082, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    149808516,    149807060,    149808633,    149808516,    149726548,    149724864, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    150280859,    150279410,    150280972,    150280860,    150199484,    150197811, ],
  }),
  ("nof_tree_events",                 5661883),
  ("nof_db_events",                   14958000),
  ("fsize_local",                     24033316057), # 24.03GB, avg file size 1.50GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_GluonMove"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       55),
  ("nof_db_files",                    688),
  ("nof_events",                      {
    'Count'                                                                          : [     27500000, ],
    'CountWeighted'                                                                  : [     27277445,     27275138,     27277254, ],
    'CountWeightedLHEWeightScale'                                                    : [     30733643,     30197082,     29852548,     27947619,     27277445,     26760978,     25288565,     24563867,     23968011, ],
    'CountWeightedLHEEnvelope'                                                       : [     33216517,     22344526, ],
    'CountWeightedPSWeight'                                                          : [     27277864,     27278927,     39508011,     27275414,     27227290,     16246606, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    274989648,    274989843,    274989843,    274989649,    274988798,    274988606, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     27297734,     27297865,     27297575, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     27354519,     27354632,     27354420, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     27316961,     27317085,     27316786, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     27387433,     27387499,     27387313, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     27324235,     27324343,     27324063, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     27415765,     27415847,     27415668, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     30760996,     30227774,     29886487,     27963839,     27297734,     26786030,     25296656,     24577527,     23986252, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     30828453,     30297759,     29959103,     28016995,     27354519,     26846051,     25338526,     24623731,     24036050, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     30782600,     30248600,     29906695,     27984024,     27316961,     26804479,     25315353,     24595175,     24003043, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     30865432,     30333321,     29993562,     28051604,     27387433,     26877536,     25370627,     24653976,     24064755, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     30792886,     30258837,     29916913,     27990935,     27324235,     26812035,     25319905,     24600328,     24008658, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     30901486,     30369100,     30029189,     28079474,     27415765,     26906261,     25392436,     24676693,     24088167, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     33234107,     22373792, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     33295667,     22431830, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     33258304,     22388530, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     33337176,     22456901, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     33266948,     22395839, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     33371127,     22482980, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     27299308,     27299149,     39527791,     27295703,     27249675,     16267931, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     27356604,     27355247,     39599797,     27351835,     27307775,     16310326, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     27318480,     27318439,     39556495,     27314970,     27268747,     16278653, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     27389416,     27388243,     39649067,     27384827,     27340393,     16328546, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     27325823,     27325570,     39565474,     27322144,     27276268,     16284266, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     27417910,     27416307,     39686812,     27412979,     27369236,     16348152, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    275147808,    275147996,    275147996,    275147808,    275146972,    275146783, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    275663616,    275663802,    275663802,    275663616,    275662799,    275662609, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    275348302,    275348494,    275348494,    275348303,    275347466,    275347276, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    276007335,    276007519,    276007519,    276007335,    276006511,    276006322, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    275417717,    275417905,    275417905,    275417717,    275416881,    275416687, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    276283783,    276283967,    276283967,    276283783,    276282952,    276282763, ],
  }),
  ("nof_tree_events",                 2538384),
  ("nof_db_events",                   27500000),
  ("fsize_local",                     11663980075), # 11.66GB, avg file size 212.07MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTToSemiLeptonic_GluonMove"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       29),
  ("nof_db_files",                    694),
  ("nof_events",                      {
    'Count'                                                                          : [     27388000, ],
    'CountWeighted'                                                                  : [     27166284,     27168251,     27158695, ],
    'CountWeightedLHEWeightScale'                                                    : [     30611041,     30075934,     29732196,     27835443,     27166284,     26652802,     25186613,     24464656,     23870863, ],
    'CountWeightedLHEEnvelope'                                                       : [     33084161,     22253872, ],
    'CountWeightedPSWeight'                                                          : [     27166310,     27163413,     40169349,     27167607,     27089733,     15444729, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    273877717,    273877884,    273877888,    273877722,    273876303,    273876132, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     27187917,     27187790,     27187928, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     27244547,     27244404,     27244624, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     27207017,     27206920,     27207026, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     27277242,     27277129,     27277333, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     27214284,     27214169,     27214301, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     27305420,     27305343,     27305507, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     30638423,     30106593,     29766003,     27851726,     27187917,     26677761,     25194771,     24478342,     23889031, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     30705691,     30176319,     29838298,     27904754,     27244547,     26737522,     25236558,     24524396,     23938609, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     30659908,     30127295,     29786116,     27871810,     27207017,     26696122,     25213384,     24495900,     23905739, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     30742487,     30211702,     29872564,     27939198,     27277242,     26768872,     25268502,     24554507,     23967184, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     30670149,     30137493,     29796268,     27878691,     27214284,     26703604,     25217914,     24501030,     23911319, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     30778372,     30247267,     29907968,     27966935,     27305420,     26797405,     25290224,     24577111,     23990464, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     33101762,     22283070, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     33163075,     22340903, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     33125811,     22297718, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     33204409,     22365850, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     33134434,     22304991, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     33238164,     22391780, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     27187781,     27183436,     40190484,     27187918,     27112270,     15464685, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     27244855,     27239175,     40264646,     27243891,     27170323,     15504686, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     27206859,     27202648,     40219581,     27207096,     27131220,     15474897, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     27277498,     27272038,     40314569,     27276718,     27202696,     15522037, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     27214153,     27209754,     40228762,     27214227,     27138639,     15480175, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     27305811,     27299992,     40353054,     27304714,     27231246,     15540535, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    274027975,    274028143,    274028145,    274027978,    274026585,    274026410, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    274541862,    274542029,    274542031,    274541867,    274540492,    274540318, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    274227813,    274227981,    274227983,    274227817,    274226420,    274226246, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    274884180,    274884347,    274884349,    274884183,    274882799,    274882628, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    274296631,    274296798,    274296801,    274296635,    274295234,    274295060, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    275159396,    275159562,    275159564,    275159400,    275158024,    275157853, ],
  }),
  ("nof_tree_events",                 338783),
  ("nof_db_events",                   27488000),
  ("fsize_local",                     1640938376), # 1.64GB, avg file size 56.58MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTToHadronic_GluonMove"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       4),
  ("nof_db_files",                    118),
  ("nof_events",                      {
    'Count'                                                                          : [      3738000, ],
    'CountWeighted'                                                                  : [      3707759,      3707680,      3707136, ],
    'CountWeightedLHEWeightScale'                                                    : [      4178183,      4105065,      4058144,      3799113,      3707740,      3637654,      3437438,      3338894,      3257846, ],
    'CountWeightedLHEEnvelope'                                                       : [      4515454,      3037319, ],
    'CountWeightedPSWeight'                                                          : [      3707797,      3707259,      5249316,      3707941,      3704871,      2316909, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     37379875,     37379399,     37379899,     37379875,     37357799,     37357276, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      3710691,      3710680,      3710699, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      3718413,      3718406,      3718414, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      3713298,      3713287,      3713308, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      3722871,      3722856,      3722877, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      3714278,      3714258,      3714283, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      3726697,      3726692,      3726700, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [      4181908,      4109248,      4062775,      3801319,      3710578,      3641058,      3438522,      3340747,      3260334, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [      4191066,      4118762,      4072646,      3808525,      3718300,      3649216,      3444206,      3347020,      3267095, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [      4184837,      4112069,      4065514,      3804057,      3713187,      3643565,      3441066,      3343142,      3262608, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [      4196083,      4123585,      4077323,      3813224,      3722757,      3653494,      3448564,      3351126,      3270990, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [      4186214,      4113449,      4066893,      3804971,      3714165,      3644576,      3441668,      3343832,      3263352, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [      4200953,      4128424,      4082139,      3816988,      3726584,      3657371,      3451501,      3354189,      3274145, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [      4517846,      3041298, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [      4526204,      3049187, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [      4521122,      3043295, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [      4531830,      3052592, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [      4522274,      3044280, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [      4536410,      3056117, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      3710716,      3709969,      5251695,      3710707,      3707884,      2320050, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      3718490,      3717556,      5261020,      3718338,      3715756,      2326185, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      3713316,      3712590,      5255527,      3713329,      3710473,      2321567, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      3722953,      3722047,      5267587,      3722818,      3720180,      2328765, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      3714296,      3713550,      5256624,      3714283,      3711444,      2322379, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      3726785,      3725846,      5272428,      3726619,      3724006,      2331589, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     37399899,     37399433,     37399925,     37399899,     37378044,     37377523, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     37469870,     37469406,     37469894,     37469869,     37448195,     37447683, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     37427208,     37426739,     37427234,     37427208,     37405313,     37404793, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     37516559,     37516096,     37516585,     37516559,     37494819,     37494302, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     37436434,     37435965,     37436460,     37436434,     37414561,     37414038, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     37553883,     37553417,     37553909,     37553883,     37532166,     37531650, ],
  }),
  ("nof_tree_events",                 1409152),
  ("nof_db_events",                   3738000),
  ("fsize_local",                     5991334050), # 5.99GB, avg file size 1.50GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_erdON"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       10),
  ("nof_db_files",                    264),
  ("nof_events",                      {
    'Count'                                                                          : [      9330000, ],
    'CountWeighted'                                                                  : [      9254487,      9253835,      9253096, ],
    'CountWeightedLHEWeightScale'                                                    : [     10428958,     10246711,     10129661,      9482938,      9253714,      9080082,      8580238,      8334312,      8132059, ],
    'CountWeightedLHEEnvelope'                                                       : [     11270687,      7582045, ],
    'CountWeightedPSWeight'                                                          : [      9255539,      9256027,     13101882,      9254660,      9243477,      5781691, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     93280704,     93279654,     93280748,     93280705,     93225519,     93224382, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      9262386,      9262297,      9262481, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      9281721,      9281620,      9281846, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      9268905,      9268805,      9268987, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      9292857,      9292763,      9292985, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      9271360,      9271260,      9271457, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      9302456,      9302355,      9302609, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     10438314,     10257175,     10141208,      9488532,      9262106,      9088630,      8583074,      8339030,      8138319, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     10461258,     10280977,     10165883,      9506635,      9281445,      9109035,      8597351,      8354775,      8155260, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     10445634,     10264246,     10148064,      9495361,      9268621,      9094877,      8589400,      8345008,      8144006, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     10473785,     10293026,     10177555,      9518360,      9292582,      9119704,      8608228,      8365011,      8164987, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     10449105,     10267686,     10151504,      9497683,      9271077,      9097434,      8590944,      8346756,      8145901, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     10485965,     10305123,     10189605,      9527798,      9302174,      9129446,      8615625,      8372729,      8172938, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     11276768,      7592006, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     11297742,      7611709, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     11284968,      7597000, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     11311793,      7620205, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     11287882,      7599464, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     11323297,      7629040, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      9262895,      9262967,     13108198,      9261666,      9251156,      5789479, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      9282378,      9282075,     13131830,      9280794,      9270956,      5804766, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      9269395,      9269491,     13117749,      9268193,      9257628,      5793283, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      9293497,      9293240,     13148212,      9291977,      9282035,      5811213, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      9271876,      9271907,     13120637,      9270624,      9260171,      5795303, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      9303145,      9302746,     13160569,      9301501,      9291809,      5818243, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     93350599,     93349553,     93350641,     93350600,     93295831,     93294704, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     93526072,     93525027,     93526111,     93526074,     93471696,     93470579, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     93418609,     93417563,     93418653,     93418611,     93363754,     93362625, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     93642546,     93641506,     93642587,     93642548,     93588026,     93586905, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     93442114,     93441069,     93442157,     93442114,     93387309,     93386176, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     93736462,     93735419,     93736502,     93736463,     93681998,     93680876, ],
  }),
  ("nof_tree_events",                 3518053),
  ("nof_db_events",                   9530000),
  ("fsize_local",                     14955348690), # 14.96GB, avg file size 1.50GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_erdON_ext1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       52),
  ("nof_db_files",                    717),
  ("nof_events",                      {
    'Count'                                                                          : [     25758000, ],
    'CountWeighted'                                                                  : [     25548509,     25548778,     25548071, ],
    'CountWeightedLHEWeightScale'                                                    : [     28789033,     28285769,     27962455,     26178407,     25548509,     25065904,     23686973,     23007855,     22449328, ],
    'CountWeightedLHEEnvelope'                                                       : [     31113343,     20930011, ],
    'CountWeightedPSWeight'                                                          : [     25549425,     25550614,     37038325,     25549863,     25502014,     15189462, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    257580693,    257580823,    257580823,    257580693,    257579360,    257579232, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     25569212,     25569293,     25569115, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     25622386,     25622503,     25622325, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     25587205,     25587293,     25587102, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     25653207,     25653295,     25653107, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     25594055,     25594136,     25593959, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     25679837,     25679930,     25679741, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     28814586,     28314483,     27994231,     26193578,     25569212,     25089407,     23694569,     23020684,     22466474, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     28877712,     28379979,     28062218,     26243350,     25622386,     25145650,     23733810,     23063996,     22513170, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     28834845,     28333995,     28013150,     26212489,     25587205,     25106665,     23712085,     23037204,     22482186, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     28912365,     28413307,     28094493,     26275784,     25653207,     25175131,     23763877,     23092310,     22540029, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     28844521,     28343627,     28022766,     26219003,     25594055,     25113793,     23716390,     23042069,     22487483, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     28946244,     28446896,     28127946,     26301979,     25679837,     25202101,     23784390,     23113674,     22562031, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     31129876,     20957369, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     31187585,     21011667, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     31152540,     20971172, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     31226465,     21035149, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     31160685,     20978054, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     31258364,     21059646, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     25569538,     25569567,     37056491,     25568930,     25522576,     15209389, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     25623188,     25622122,     37123640,     25621543,     25576610,     15249013, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     25587497,     25587626,     37083431,     25586992,     25540466,     15219415, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     25653926,     25653027,     37169876,     25652445,     25607200,     15266049, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     25594406,     25594380,     37091823,     25593763,     25547449,     15224698, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     25680664,     25679453,     37205209,     25678914,     25634082,     15284449, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    257718203,    257718332,    257718332,    257718204,    257716885,    257716757, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    258201588,    258201715,    258201716,    258201588,    258200280,    258200154, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    257906228,    257906356,    257906356,    257906228,    257904908,    257904781, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    258523229,    258523357,    258523357,    258523229,    258521921,    258521793, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    257971828,    257971956,    257971956,    257971828,    257970506,    257970377, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    258783371,    258783501,    258783502,    258783372,    258782066,    258781939, ],
  }),
  ("nof_tree_events",                 2322154),
  ("nof_db_events",                   26290000),
  ("fsize_local",                     10690161018), # 10.69GB, avg file size 205.58MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTToSemiLeptonic_erdON"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       23),
  ("nof_db_files",                    799),
  ("nof_events",                      {
    'Count'                                                                          : [     22442000, ],
    'CountWeighted'                                                                  : [     22261891,     22256734,     22251290, ],
    'CountWeightedLHEWeightScale'                                                    : [     25082804,     24644905,     24363651,     22807825,     22261891,     21839519,     20636780,     20045404,     19559328, ],
    'CountWeightedLHEEnvelope'                                                       : [     27107504,     18235868, ],
    'CountWeightedPSWeight'                                                          : [     22259785,     22261808,     32947229,     22260879,     22192989,     12628549, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    224354771,    224354934,    224354938,    224354770,    224352532,    224352356, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     22277513,     22277457,     22277552, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     22323952,     22323824,     22324100, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     22293168,     22293127,     22293217, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     22350760,     22350645,     22350901, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     22299125,     22299035,     22299183, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     22373865,     22373697,     22373993, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     25105171,     24669965,     24391358,     22821166,     22277513,     21860028,     20643528,     20056693,     19574306, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     25160255,     24727084,     24450587,     22864632,     22323952,     21909054,     20677796,     20094509,     19615037, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     25122789,     24686954,     24407838,     22837635,     22293168,     21875064,     20658776,     20071071,     19587998, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     25190414,     24756084,     24478713,     22892860,     22350760,     21934748,     20703982,     20119154,     19638434, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     25131146,     24695268,     24416119,     22843260,     22299125,     21881223,     20662469,     20075273,     19592571, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     25219751,     24785196,     24507678,     22915575,     22373865,     21958122,     20721763,     20137686,     19657528, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     27121949,     18259823, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     27172240,     18307228, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     27141683,     18271827, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     27206105,     18327659, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     27148701,     18277765, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     27233742,     18348897, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     22277341,     22278199,     32964527,     22277515,     22211440,     12644935, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     22324146,     22323884,     33025337,     22323420,     22258953,     12677691, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     22292987,     22293966,     32988394,     22293233,     22226940,     12653268, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     22350912,     22350857,     33066284,     22350321,     22285473,     12691866, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     22298953,     22299780,     32995869,     22299077,     22232973,     12657592, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     22374110,     22373728,     33097785,     22373241,     22308781,     12707011, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    224541458,    224541622,    224541626,    224541461,    224539245,    224539073, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    224963111,    224963272,    224963276,    224963110,    224960918,    224960744, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    224705127,    224705289,    224705293,    224705127,    224702904,    224702730, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    225243341,    225243507,    225243509,    225243342,    225241143,    225240968, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    224761421,    224761584,    224761589,    224761420,    224759203,    224759027, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    225468518,    225468688,    225468690,    225468519,    225466320,    225466145, ],
  }),
  ("nof_tree_events",                 267466),
  ("nof_db_events",                   27486000),
  ("fsize_local",                     1295499415), # 1.30GB, avg file size 56.33MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTToHadronic_erdON"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       3),
  ("nof_db_files",                    76),
  ("nof_events",                      {
    'Count'                                                                          : [      2500000, ],
    'CountWeighted'                                                                  : [      2478827,      2478997,      2478845, ],
    'CountWeightedLHEWeightScale'                                                    : [      2794275,      2746959,      2717217,      2537847,      2478827,      2434148,      2293985,      2230682,      2178686, ],
    'CountWeightedLHEEnvelope'                                                       : [      3020424,      2030657, ],
    'CountWeightedPSWeight'                                                          : [      2479135,      2479543,      3504077,      2478913,      2475521,      1553167, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     25002736,     25002692,     25002780,     25002736,     24995856,     24995727, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      2485320,      2485339,      2485283, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      2494695,      2494710,      2494666, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      2486745,      2486765,      2486709, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      2497085,      2497092,      2497052, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      2488337,      2488351,      2488298, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      2501547,      2501569,      2501515, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [      2801678,      2754572,      2725068,      2543790,      2485320,      2440706,      2298770,      2235845,      2184174, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [      2812563,      2765606,      2736287,      2552933,      2494695,      2450292,      2306470,      2243841,      2192407, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [      2803277,      2756113,      2726556,      2545297,      2486745,      2442073,      2300163,      2237166,      2185423, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [      2815233,      2768168,      2738760,      2555456,      2497085,      2452566,      2308820,      2246043,      2194486, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [      2805263,      2758086,      2728525,      2546860,      2488337,      2443672,      2301423,      2238461,      2186748, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [      2820653,      2773535,      2744105,      2559908,      2501547,      2457050,      2312517,      2249797,      2198277, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [      3027383,      2036830, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [      3038163,      2045513, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [      3029188,      2037914, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [      3041185,      2047305, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [      3031096,      2039351, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [      3046560,      2051248, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      2485443,      2485709,      3511842,      2485135,      2481912,      1558011, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      2494860,      2494992,      3524029,      2494449,      2491399,      1564770, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      2486869,      2487152,      3513952,      2486565,      2483320,      1558828, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      2497235,      2497401,      3527560,      2496844,      2493742,      1566123, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      2488461,      2488727,      3516008,      2488151,      2484909,      1559970, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      2501713,      2501851,      3533488,      2501304,      2498222,      1569233, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     25057224,     25057180,     25057267,     25057224,     25050415,     25050287, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     25146475,     25146433,     25146517,     25146474,     25139720,     25139594, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     25072299,     25072257,     25072342,     25072299,     25065477,     25065350, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     25171656,     25171615,     25171699,     25171656,     25164880,     25164755, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     25087936,     25087893,     25087979,     25087936,     25081117,     25080991, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     25215950,     25215910,     25215994,     25215950,     25209176,     25209050, ],
  }),
  ("nof_tree_events",                 929529),
  ("nof_db_events",                   2500000),
  ("fsize_local",                     3893814322), # 3.89GB, avg file size 1.30GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_mtop166p5"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       10),
  ("nof_db_files",                    254),
  ("nof_events",                      {
    'Count'                                                                          : [      9767000, ],
    'CountWeighted'                                                                  : [      9687413,      9684323,      9685045, ],
    'CountWeightedLHEWeightScale'                                                    : [     10919512,     10733398,     10616159,      9916203,      9687369,      9509540,      8962606,      8714662,      8511045, ],
    'CountWeightedLHEEnvelope'                                                       : [     11800942,      7934651, ],
    'CountWeightedPSWeight'                                                          : [      9685496,      9686682,     14020142,      9685902,      9665802,      5773865, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     97674399,     97674427,     97674427,     97674400,     97674223,     97674193, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      9710322,      9710341,      9710264, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      9747125,      9747142,      9747076, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      9715853,      9715874,      9715795, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      9756352,      9756387,      9756321, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      9722083,      9722111,      9722035, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      9773855,      9773883,      9773800, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     10948539,     10763333,     10647065,      9939549,      9710025,      9535361,      8981428,      8735057,      8532703, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     10991143,     10806585,     10691093,      9975398,      9746817,      9573008,      9011663,      8766445,      8565029, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     10954750,     10769313,     10652844,      9945392,      9715561,      9540644,      8986861,      8740151,      8537525, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     11001538,     10816525,     10700683,      9985185,      9756062,      9581828,      9020774,      8774969,      8573076, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     10962513,     10777008,     10660513,      9951546,      9721788,      9546931,      8991791,      8745235,      8542735, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     11022726,     10837528,     10721584,     10002620,      9773556,      9599365,      9035270,      8789677,      8587935, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     11828343,      7958910, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     11870611,      7992926, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     11835342,      7963106, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     11882350,      7999869, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     11842837,      7968709, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     11903443,      8015267, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      9710309,      9711081,     14052065,      9710299,      9690852,      5791653, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      9747276,      9747614,     14101622,      9746856,      9727976,      5816598, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      9715837,      9716645,     14060374,      9715850,      9696320,      5794703, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      9756489,      9756920,     14115554,      9756141,      9737100,      5821629, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      9722080,      9722830,     14068737,      9722040,      9702563,      5798913, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      9774035,      9774342,     14139513,      9773551,      9754643,      5833114, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     97896835,     97896864,     97896864,     97896837,     97896665,     97896635, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     98248070,     98248099,     98248099,     98248072,     98247906,     98247877, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     97954980,     97955008,     97955008,     97954981,     97954810,     97954780, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     98345325,     98345354,     98345354,     98345328,     98345159,     98345130, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     98016047,     98016077,     98016077,     98016049,     98015875,     98015847, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     98517951,     98517980,     98517980,     98517953,     98517784,     98517756, ],
  }),
  ("nof_tree_events",                 883914),
  ("nof_db_events",                   9767000),
  ("fsize_local",                     3991641605), # 3.99GB, avg file size 399.16MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTToSemiLeptonic_mtop166p5"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       10),
  ("nof_db_files",                    250),
  ("nof_events",                      {
    'Count'                                                                          : [      9534000, ],
    'CountWeighted'                                                                  : [      9456343,      9452821,      9453493, ],
    'CountWeightedLHEWeightScale'                                                    : [     10658003,     10477492,     10364201,      9678930,      9456343,      9283559,      8748315,      8506953,      8308716, ],
    'CountWeightedLHEEnvelope'                                                       : [     11519502,      7745244, ],
    'CountWeightedPSWeight'                                                          : [      9454624,      9456105,     13975703,      9455032,      9427450,      5379708, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     95329942,     95330026,     95330026,     95329945,     95329779,     95329695, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      9478776,      9478763,      9478723, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      9514637,      9514617,      9514634, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      9484188,      9484166,      9484123, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      9523657,      9523641,      9523652, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      9490239,      9490221,      9490199, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      9540689,      9540667,      9540682, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     10686365,     10506708,     10394337,      9701703,      9478776,      9308681,      8766626,      8526776,      8329770, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     10727997,     10548921,     10437286,      9736661,      9514637,      9345376,      8796076,      8557318,      8361235, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     10692427,     10512533,     10399966,      9707399,      9484188,      9313852,      8771919,      8531748,      8334489, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     10738115,     10558617,     10446642,      9746210,      9523657,      9353968,      8804979,      8565654,      8369100, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     10699989,     10520043,     10407468,      9713368,      9490239,      9319973,      8776714,      8536695,      8339546, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     10758757,     10579099,     10467039,      9763177,      9540689,      9371070,      8819071,      8579954,      8383563, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     11546261,      7768848, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     11587549,      7801965, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     11553092,      7772948, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     11598989,      7808750, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     11560397,      7778407, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     11619546,      7823740, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      9478768,      9479813,     14007864,      9478790,      9452040,      5396165, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      9514794,      9515392,     14057632,      9514432,      9488419,      5419282, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      9484159,      9485256,     14016134,      9484208,      9457383,      5399007, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      9523783,      9524459,     14071488,      9523488,      9497311,      5423989, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      9490234,      9491253,     14024522,      9490230,      9463520,      5402909, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      9540875,      9541398,     14095497,      9540440,      9514536,      5434634, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     95560645,     95560728,     95560728,     95560647,     95560480,     95560399, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     95903055,     95903138,     95903138,     95903058,     95902892,     95902808, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     95617453,     95617536,     95617536,     95617456,     95617289,     95617207, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     95997764,     95997845,     95997845,     95997767,     95997601,     95997518, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     95676753,     95676834,     95676834,     95676755,     95676589,     95676508, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     96165793,     96165879,     96165879,     96165796,     96165637,     96165552, ],
  }),
  ("nof_tree_events",                 115193),
  ("nof_db_events",                   9734000),
  ("fsize_local",                     549757035), # 549.76MB, avg file size 54.98MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTToHadronic_mtop166p5"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       3),
  ("nof_db_files",                    53),
  ("nof_events",                      {
    'Count'                                                                          : [      2490000, ],
    'CountWeighted'                                                                  : [      2469074,      2468788,      2468867, ],
    'CountWeightedLHEWeightScale'                                                    : [      2782949,      2734833,      2704309,      2529088,      2468950,      2423485,      2287277,      2222859,      2169901, ],
    'CountWeightedLHEEnvelope'                                                       : [      3007441,      2023195, ],
    'CountWeightedPSWeight'                                                          : [      2469531,      2470148,      3492236,      2468867,      2465156,      1545009, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     24903108,     24902933,     24903134,     24903108,     24893326,     24893101, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      2473369,      2473404,      2473320, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      2480612,      2480645,      2480580, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      2474935,      2474975,      2474892, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      2483273,      2483304,      2483239, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      2476059,      2476097,      2476008, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      2486775,      2486808,      2486732, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [      2787856,      2740026,      2709777,      2532785,      2473292,      2427905,      2290031,      2226066,      2173482, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [      2796316,      2748686,      2718662,      2539738,      2480538,      2435408,      2295764,      2232146,      2179850, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [      2789623,      2741718,      2711424,      2534440,      2474861,      2429410,      2291560,      2227514,      2174856, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [      2799302,      2751557,      2721434,      2542546,      2483198,      2437955,      2298370,      2234599,      2182170, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [      2791075,      2743166,      2712862,      2535526,      2475983,      2430548,      2292389,      2228382,      2175770, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [      2803623,      2755847,      2725708,      2546018,      2486699,      2441482,      2301188,      2237484,      2185110, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [      3011726,      2027583, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [      3019888,      2034520, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [      3013708,      2028783, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [      3023256,      2036534, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [      3015049,      2029826, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [      3027467,      2039662, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      2473658,      2474179,      3496931,      2472913,      2469293,      1548445, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      2480938,      2481375,      3506135,      2480114,      2476600,      1553834, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      2475226,      2475750,      3499244,      2474483,      2470865,      1549358, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      2483593,      2484044,      3510068,      2482780,      2479253,      1555368, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      2476340,      2476860,      3500659,      2475599,      2471998,      1550191, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      2487094,      2487526,      3514666,      2486268,      2482779,      1557844, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     24935337,     24935165,     24935363,     24935337,     24925656,     24925432, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     25003310,     25003140,     25003336,     25003310,     24993706,     24993485, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     24951845,     24951671,     24951869,     24951845,     24942148,     24941924, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     25031214,     25031042,     25031239,     25031214,     25021583,     25021361, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     24962666,     24962494,     24962690,     24962666,     24952973,     24952752, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     25065516,     25065348,     25065542,     25065516,     25055897,     25055676, ],
  }),
  ("nof_tree_events",                 932589),
  ("nof_db_events",                   2490000),
  ("fsize_local",                     3933042559), # 3.93GB, avg file size 1.31GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_mtop169p5"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       20),
  ("nof_db_files",                    253),
  ("nof_events",                      {
    'Count'                                                                          : [      9550000, ],
    'CountWeighted'                                                                  : [      9471098,      9470970,      9471886, ],
    'CountWeightedLHEWeightScale'                                                    : [     10675723,     10491009,     10373442,      9701162,      9470262,      9295430,      8772934,      8525598,      8322311, ],
    'CountWeightedLHEEnvelope'                                                       : [     11536977,      7759391, ],
    'CountWeightedPSWeight'                                                          : [      9471620,      9470222,     13396012,      9471340,      9460143,      5926147, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     95515139,     95514602,     95515217,     95515139,     95477544,     95476850, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      9487185,      9487240,      9487114, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      9514987,      9515052,      9514913, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      9493230,      9493285,      9493163, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      9525224,      9525290,      9525148, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      9497527,      9497594,      9497463, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      9538681,      9538754,      9538613, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     10694591,     10510915,     10394374,      9715359,      9486890,      9312368,      8783522,      8537908,      8336035, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     10727075,     10544144,     10428448,      9742071,      9514700,      9341156,      8805552,      8561243,      8360464, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     10701392,     10517452,     10400718,      9721718,      9492937,      9318165,      8789422,      8543464,      8341313, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     10738582,     10555192,     10439130,      9752865,      9524935,      9350941,      8815588,      8570681,      8369394, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     10706967,     10522988,     10406234,      9725925,      9497237,      9322539,      8792622,      8546848,      8344830, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     10755194,     10571649,     10455510,      9766229,      9538391,      9364489,      8826461,      8581806,      8380706, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     11553420,      7776251, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     11584760,      7802875, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     11561052,      7780865, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     11597714,      7810637, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     11566211,      7784866, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     11613910,      7822670, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      9487472,      9485644,     13414112,      9486767,      9476168,      5939307, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      9515455,      9513210,     13449503,      9514336,      9504327,      5959976, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      9493501,      9491700,     13422986,      9492835,      9482174,      5942819, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      9525668,      9523481,     13464603,      9524608,      9514486,      5965862, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      9497832,      9495956,     13428450,      9497099,      9486560,      5946031, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      9539184,      9536854,     13482314,      9537999,      9528115,      5975386, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     95635968,     95635432,     95636043,     95635967,     95598727,     95598041, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     95896936,     95896400,     95897010,     95896936,     95859944,     95859260, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     95699289,     95698752,     95699364,     95699288,     95661987,     95661298, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     96004163,     96003623,     96004237,     96004163,     95967066,     95966380, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     95741286,     95740749,     95741361,     95741286,     95704007,     95703319, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     96136722,     96136184,     96136794,     96136721,     96099651,     96098966, ],
  }),
  ("nof_tree_events",                 3575659),
  ("nof_db_events",                   9550000),
  ("fsize_local",                     15093925625), # 15.09GB, avg file size 754.70MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_mtop169p5_ext1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       19),
  ("nof_db_files",                    520),
  ("nof_events",                      {
    'Count'                                                                          : [     18797000, ],
    'CountWeighted'                                                                  : [     18642541,     18642588,     18642631, ],
    'CountWeightedLHEWeightScale'                                                    : [     21011491,     20649172,     20418761,     19093639,     18642541,     18296903,     17267103,     16781002,     16381383, ],
    'CountWeightedLHEEnvelope'                                                       : [     22708347,     15271879, ],
    'CountWeightedPSWeight'                                                          : [     18642229,     18640841,     27002784,     18643029,     18610147,     11101438, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    187965170,    187965262,    187965262,    187965166,    187964746,    187964651, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     18673483,     18673635,     18673310, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     18728260,     18728405,     18728118, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     18685361,     18685498,     18685189, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     18748374,     18748498,     18748211, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     18693797,     18693908,     18693616, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     18774727,     18774872,     18774576, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     21048763,     20688433,     20460035,     19121640,     18673483,     18330264,     17287985,     16805268,     16408409, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     21112764,     20753885,     20527128,     19174252,     18728260,     18386931,     17331319,     16851178,     16456451, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     21062098,     20701270,     20472489,     19134134,     18685361,     18341649,     17299566,     16816188,     16418782, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     21135383,     20775584,     20548106,     19195457,     18748374,     18406154,     17351051,     16869718,     16474001, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     21073014,     20712104,     20483290,     19142328,     18693797,     18350183,     17305791,     16822776,     16425636, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     21167930,     20807843,     20580239,     19221599,     18774727,     18432697,     17372297,     16891493,     16496146, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     22740758,     15305168, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     22802415,     15357641, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     22755731,     15314227, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     22827865,     15372870, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     22765805,     15322056, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     22859583,     15396467, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     18673385,     18671194,     27040285,     18673508,     18641949,     11125802, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     18728444,     18725457,     27112611,     18727856,     18697520,     11164210, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     18685246,     18683119,     27058088,     18685401,     18653715,     11132380, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     18748503,     18745674,     27142864,     18748048,     18717431,     11175257, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     18693705,     18691470,     27069166,     18693752,     18662221,     11138291, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     18774959,     18771942,     27178673,     18774272,     18744036,     11192873, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    188237842,    188237931,    188237931,    188237840,    188237425,    188237333, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    188751533,    188751621,    188751621,    188751531,    188751116,    188751026, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    188362237,    188362329,    188362329,    188362234,    188361817,    188361725, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    188962306,    188962395,    188962395,    188962305,    188961886,    188961796, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    188444222,    188444312,    188444312,    188444218,    188443796,    188443703, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    189221371,    189221459,    189221459,    189221369,    189220949,    189220863, ],
  }),
  ("nof_tree_events",                 1705041),
  ("nof_db_events",                   18896000),
  ("fsize_local",                     7752820228), # 7.75GB, avg file size 408.04MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTToSemiLeptonic_mtop169p5"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       10),
  ("nof_db_files",                    280),
  ("nof_events",                      {
    'Count'                                                                          : [      9108000, ],
    'CountWeighted'                                                                  : [      9033886,      9029454,      9033253, ],
    'CountWeightedLHEWeightScale'                                                    : [     10182335,     10006396,      9894437,      9252367,      9033886,      8865880,      8366978,      8131252,      7937500, ],
    'CountWeightedLHEEnvelope'                                                       : [     11003179,      7401256, ],
    'CountWeightedPSWeight'                                                          : [      9034005,      9034493,     13084289,      9033178,      9015758,      5379624, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     91091894,     91091950,     91091950,     91091894,     91091672,     91091618, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      9048683,      9048689,      9048656, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      9075347,      9075344,      9075338, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      9054441,      9054442,      9054401, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      9085089,      9085073,      9085076, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      9058533,      9058517,      9058516, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      9097909,      9097871,      9097913, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     10200494,     10025519,      9914550,      9266074,      9048683,      8882175,      8377249,      8143166,      7950738, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     10231619,     10057351,      9947159,      9291707,      9075347,      8909758,      8398409,      8165564,      7974151, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     10206975,     10031748,      9920574,      9272123,      9054441,      8887680,      8382858,      8148453,      7955747, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     10242581,     10067868,      9957320,      9301977,      9085089,      8919056,      8407942,      8174526,      7982638, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     10212269,     10037012,      9925815,      9276127,      9058533,      8891836,      8385898,      8151662,      7959085, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     10258399,     10083542,      9972917,      9314696,      9097909,      8931953,      8418302,      8185120,      7993400, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     11019031,      7417468, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     11049052,      7442989, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     11026281,      7421868, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     11061368,      7450373, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     11031170,      7425674, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     11076772,      7461848, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      9049232,      9049410,     13102678,      9048057,      9031249,      5391504, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      9076031,      9075856,     13137898,      9074520,      9058272,      5410200, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      9054979,      9055165,     13111283,      9053811,      9036957,      5394692, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      9085746,      9085624,     13152534,      9084285,      9067933,      5415551, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      9059076,      9059176,     13116636,      9057889,      9041117,      5397590, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      9098602,      9098326,     13169889,      9097051,      9080900,      5424145, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     91211348,     91211399,     91211399,     91211348,     91211127,     91211075, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     91461521,     91461571,     91461571,     91461521,     91461300,     91461251, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     91271605,     91271656,     91271656,     91271605,     91271384,     91271333, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     91563583,     91563631,     91563631,     91563583,     91563360,     91563311, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     91311351,     91311405,     91311405,     91311351,     91311128,     91311076, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     91689630,     91689679,     91689679,     91689629,     91689408,     91689359, ],
  }),
  ("nof_tree_events",                 826706),
  ("nof_db_events",                   9808000),
  ("fsize_local",                     3761267930), # 3.76GB, avg file size 376.13MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTToSemiLeptonic_mtop169p5_ext1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       20),
  ("nof_db_files",                    538),
  ("nof_events",                      {
    'Count'                                                                          : [     19032000, ],
    'CountWeighted'                                                                  : [     18875724,     18874490,     18872710, ],
    'CountWeightedLHEWeightScale'                                                    : [     21274186,     20905632,     20670748,     19332998,     18875667,     18523652,     17483889,     16990484,     16584964, ],
    'CountWeightedLHEEnvelope'                                                       : [     22991341,     15462009, ],
    'CountWeightedPSWeight'                                                          : [     18874034,     18875314,     27911950,     18876191,     18819043,     10727345, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    190276325,    190276402,    190276412,    190276325,    190275748,    190275651, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     18906416,     18906375,     18906377, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     18962036,     18961950,     18962083, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     18918398,     18918384,     18918360, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     18982345,     18982307,     18982368, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     18926905,     18926880,     18926899, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     19009016,     19008957,     19009073, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     21312191,     20945631,     20712755,     19361592,     18905830,     18557589,     17505206,     17015218,     16612442, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     21377241,     21012122,     20780826,     19415059,     18961448,     18615127,     17549283,     17061867,     16661233, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     21325665,     20958601,     20725326,     19374202,     18917827,     18569079,     17516919,     17026256,     16622924, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     21400080,     21034042,     20802054,     19436502,     18981771,     18634530,     17569211,     17080590,     16678952, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     21336692,     20969563,     20736273,     19382487,     18926319,     18577747,     17523222,     17032905,     16629884, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     21433001,     21066686,     20834581,     19462935,     19008433,     18661418,     17590721,     17102639,     16701415, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     23024324,     15495918, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     23086942,     15549256, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     23039452,     15505085, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     23112667,     15564630, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     23049655,     15512992, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     23144753,     15588523, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     18905771,     18906307,     27951577,     18907187,     18851236,     10750721, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     18961706,     18961473,     28027123,     18962385,     18907478,     10787668, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     18917755,     18918328,     27969877,     18919215,     18863140,     10757090, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     18981975,     18981876,     28058226,     18982772,     18927619,     10798358, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     18926288,     18926788,     27981355,     18927666,     18871677,     10762769, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     19008743,     19008467,     28095352,     19009351,     18954376,     10815316, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    190592993,    190593073,    190593083,    190592993,    190592428,    190592326, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    191114596,    191114674,    191114683,    191114596,    191114037,    191113936, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    190718791,    190718870,    190718879,    190718791,    190718221,    190718124, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    191327350,    191327431,    191327441,    191327350,    191326785,    191326688, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    190801785,    190801864,    190801874,    190801785,    190801216,    190801117, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    191590233,    191590315,    191590324,    191590233,    191589673,    191589576, ],
  }),
  ("nof_tree_events",                 230280),
  ("nof_db_events",                   19232000),
  ("fsize_local",                     1105135690), # 1.11GB, avg file size 55.26MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTToHadronic_mtop169p5"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       6),
  ("nof_db_files",                    169),
  ("nof_events",                      {
    'Count'                                                                          : [      5496000, ],
    'CountWeighted'                                                                  : [      5450639,      5451807,      5450527, ],
    'CountWeightedLHEWeightScale'                                                    : [      6143519,      6036897,      5968875,      5584790,      5450548,      5349375,      5052101,      4908288,      4790073, ],
    'CountWeightedLHEEnvelope'                                                       : [      6638903,      4466404, ],
    'CountWeightedPSWeight'                                                          : [      5451593,      5450818,      7713766,      5451616,      5445382,      3408557, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     54955401,     54954967,     54955433,     54955399,     54928173,     54927676, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      5457395,      5457423,      5457352, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      5470282,      5470312,      5470250, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      5461107,      5461129,      5461060, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      5476613,      5476652,      5476588, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      5462880,      5462907,      5462841, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      5482923,      5482963,      5482888, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [      6150783,      6044806,      5977420,      5589661,      5457228,      5355957,      5055198,      4912465,      4795123, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [      6165988,      6060494,      5993617,      5601848,      5470113,      5369457,      5064982,      4923072,      4806428, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [      6154948,      6048841,      5981317,      5593569,      5460940,      5359521,      5058818,      4915884,      4798373, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [      6173095,      6067342,      6000246,      5608517,      5476446,      5375517,      5071166,      4928908,      4811960, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [      6157345,      6051227,      5983716,      5595250,      5462713,      5361344,      5060011,      4917190,      4799783, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [      6181020,      6075220,      6008094,      5614726,      5482753,      5381916,      5076114,      4934024,      4817213, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [      6644371,      4473552, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [      6658539,      4486404, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [      6649046,      4476403, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [      6666543,      4491225, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [      6651151,      4478119, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [      6674113,      4496965, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      5457494,      5456475,      7719594,      5457310,      5451359,      3414134, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      5470461,      5469235,      7735527,      5470085,      5464413,      3424087, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      5461196,      5460199,      7725042,      5461028,      5455050,      3416288, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      5476785,      5475596,      7744870,      5476434,      5470698,      3427738, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      5462972,      5461959,      7727195,      5462801,      5456837,      3417690, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      5483117,      5481876,      7753027,      5482723,      5477055,      3432304, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     55005581,     55005154,     55005614,     55005581,     54978586,     54978094, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     55124273,     55123849,     55124302,     55124272,     55097461,     55096976, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     55044492,     55044063,     55044523,     55044491,     55017447,     55016957, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     55190480,     55190054,     55190510,     55190478,     55163591,     55163102, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     55061509,     55061080,     55061540,     55061507,     55034480,     55033986, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     55252353,     55251930,     55252384,     55252352,     55225486,     55224999, ],
  }),
  ("nof_tree_events",                 2065629),
  ("nof_db_events",                   5896000),
  ("fsize_local",                     8748362921), # 8.75GB, avg file size 1.46GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_mtop171p5"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       50),
  ("nof_db_files",                    622),
  ("nof_events",                      {
    'Count'                                                                          : [     24984000, ],
    'CountWeighted'                                                                  : [     24778580,     24783301,     24777991, ],
    'CountWeightedLHEWeightScale'                                                    : [     27927362,     27440201,     27128077,     25388223,     24778445,     24314574,     22967384,     22312288,     21773679, ],
    'CountWeightedLHEEnvelope'                                                       : [     30180083,     20301659, ],
    'CountWeightedPSWeight'                                                          : [     24781754,     24779573,     35906150,     24780277,     24736581,     14746781, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    249814147,    249814258,    249814258,    249814143,    249813449,    249813332, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     24807420,     24807450,     24807370, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     24866017,     24866060,     24865971, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     24824323,     24824334,     24824253, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     24894817,     24894847,     24894783, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     24832399,     24832423,     24832355, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     24923608,     24923623,     24923572, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     27960265,     27476040,     27166807,     25410402,     24806658,     24344486,     22981535,     22331312,     21796715, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     28029321,     27547281,     27240383,     25465828,     24865257,     24405900,     23026096,     22379643,     21848173, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     27979268,     27494331,     27184549,     25428143,     24823562,     24360676,     22997969,     22346825,     21811463, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     28061725,     27578417,     27270531,     25496179,     24894053,     24433459,     23054257,     22406137,     21873297, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     27990278,     27505283,     27195484,     25435929,     24831639,     24369015,     23003469,     22352838,     21817882, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     28097890,     27614278,     27306253,     25524584,     24922844,     24462543,     23076845,     22429500,     21897242, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     30205105,     20333968, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     30269709,     20392186, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     30226374,     20346903, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     30306087,     20414119, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     30236028,     20354770, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     30340615,     20440311, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     24808553,     24805199,     35934561,     24806126,     24764087,     14770496, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     24867561,     24863132,     36010013,     24864194,     24823773,     14813173, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     24825401,     24822140,     35959831,     24823055,     24780847,     14779880, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     24896304,     24892036,     36053250,     24893076,     24852336,     14829066, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     24833553,     24830144,     35970056,     24831072,     24789092,     14785884, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     24925201,     24920653,     36091825,     24921693,     24881428,     14848706, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    250047469,    250047577,    250047577,    250047466,    250046779,    250046664, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    250586790,    250586897,    250586897,    250586787,    250586112,    250586002, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    250224118,    250224228,    250224228,    250224114,    250223423,    250223311, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    250888129,    250888236,    250888236,    250888125,    250887444,    250887334, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    250302079,    250302189,    250302189,    250302076,    250301393,    250301280, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    251169932,    251170038,    251170038,    251169927,    251169248,    251169137, ],
  }),
  ("nof_tree_events",                 2271667),
  ("nof_db_events",                   24984000),
  ("fsize_local",                     10409814059), # 10.41GB, avg file size 208.20MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTToSemiLeptonic_mtop171p5"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       25),
  ("nof_db_files",                    624),
  ("nof_events",                      {
    'Count'                                                                          : [     24777000, ],
    'CountWeighted'                                                                  : [     24582683,     24578744,     24572924, ],
    'CountWeightedLHEWeightScale'                                                    : [     27694945,     27211894,     26902466,     25179315,     24581787,     24113905,     22779312,     22129409,     21595091, ],
    'CountWeightedLHEEnvelope'                                                       : [     29931812,     20132262, ],
    'CountWeightedPSWeight'                                                          : [     24576647,     24573751,     36358264,     24577431,     24508334,     13956577, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    247745882,    247745997,    247745998,    247745883,    247744937,    247744816, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     24603075,     24602979,     24603018, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     24661326,     24661217,     24661371, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     24619794,     24619724,     24619763, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     24689867,     24689761,     24689917, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     24627828,     24627752,     24627828, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     24718410,     24718312,     24718490, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     27727863,     27247639,     26941007,     25201534,     24602326,     24143656,     22793526,     22148455,     21618019, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     27796576,     27318482,     27014084,     25256682,     24660590,     24204654,     22837865,     22196512,     21669118, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     27746650,     27265753,     26958595,     25219105,     24619055,     24159723,     22809808,     22163840,     21632636, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     27828674,     27349314,     27043947,     25286747,     24689117,     24231973,     22865756,     22222767,     21694023, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     27757585,     27276623,     26969428,     25226822,     24627082,     24167971,     22815247,     22169801,     21638999, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     27864568,     27384911,     27079370,     25314913,     24717652,     24260810,     22888165,     22245928,     21717777, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     29956727,     20164533, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     30020905,     20222502, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     29977789,     20177350, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     30056955,     20244229, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     29987376,     20185170, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     30091189,     20270222, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     24603169,     24599271,     36388674,     24602999,     24536306,     13978661, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     24661819,     24656801,     36466670,     24660712,     24596101,     14018692, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     24619872,     24616059,     36414085,     24619759,     24552852,     13987565, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     24690289,     24685462,     36510176,     24689348,     24624277,     14033782, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     24627940,     24623954,     36424642,     24627737,     24561091,     13993196, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     24718945,     24713713,     36549586,     24717747,     24653283,     14052262, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    247977698,    247977815,    247977817,    247977698,    247976764,    247976648, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    248513659,    248513771,    248513771,    248513657,    248512727,    248512611, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    248152644,    248152761,    248152763,    248152645,    248151701,    248151584, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    248812501,    248812615,    248812616,    248812500,    248811567,    248811450, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    248230001,    248230118,    248230118,    248230004,    248229062,    248228944, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    249092130,    249092246,    249092247,    249092131,    249091191,    249091076, ],
  }),
  ("nof_tree_events",                 299093),
  ("nof_db_events",                   24777000),
  ("fsize_local",                     1442762613), # 1.44GB, avg file size 57.71MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTToHadronic_mtop171p5"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       6),
  ("nof_db_files",                    158),
  ("nof_events",                      {
    'Count'                                                                          : [      5232000, ],
    'CountWeighted'                                                                  : [      5189307,      5189839,      5189893, ],
    'CountWeightedLHEWeightScale'                                                    : [      5847323,      5744403,      5678107,      5318501,      5189281,      5090998,      4813371,      4674579,      4560313, ],
    'CountWeightedLHEEnvelope'                                                       : [      6319399,      4251664, ],
    'CountWeightedPSWeight'                                                          : [      5189525,      5189999,      7346936,      5190491,      5183416,      3241838, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     52324537,     52323849,     52324539,     52324534,     52291077,     52290381, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      5192527,      5192550,      5192494, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      5201939,      5201949,      5201930, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      5196286,      5196317,      5196259, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      5208394,      5208415,      5208392, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      5197377,      5197404,      5197355, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      5213190,      5213195,      5213187, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [      5850885,      5748632,      5682966,      5320112,      5192370,      5094346,      4813581,      4675890,      4562518, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [      5862141,      5760396,      5695235,      5328804,      5201781,      5104385,      4820274,      4683431,      4570775, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [      5855125,      5752704,      5686927,      5324063,      5196121,      5097957,      4817232,      4679333,      4565801, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [      5869417,      5767379,      5702014,      5335601,      5208240,      5110577,      4826570,      4689361,      4576410, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [      5856763,      5754340,      5688540,      5325088,      5197218,      5099101,      4817835,      4680053,      4566612, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [      5875611,      5773522,      5708120,      5340301,      5213031,      5115440,      4830178,      4693145,      4580325, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [      6320980,      4256053, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [      6330983,      4265954, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [      6325715,      4258936, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [      6339134,      4270881, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [      6327011,      4260085, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [      6344869,      4275344, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      5192181,      5192411,      7348287,      5192944,      5186192,      3245311, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      5201684,      5201688,      7359443,      5202241,      5195811,      3253011, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      5195943,      5196180,      7353803,      5196717,      5189934,      3247507, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      5208135,      5208171,      7368931,      5208723,      5202227,      3256756, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      5197047,      5197254,      7355009,      5197793,      5191042,      3248460, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      5212952,      5212928,      7375008,      5213476,      5207069,      3260326, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     52333443,     52332765,     52333445,     52333440,     52300318,     52299631, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     52417488,     52416815,     52417490,     52417486,     52384608,     52383928, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     52372806,     52372124,     52372808,     52372804,     52339624,     52338937, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     52484938,     52484263,     52484940,     52484936,     52451961,     52451280, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     52383036,     52382356,     52383038,     52383034,     52349875,     52349187, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     52531446,     52530771,     52531447,     52531444,     52498511,     52497831, ],
  }),
  ("nof_tree_events",                 1975496),
  ("nof_db_events",                   5732000),
  ("fsize_local",                     8402475305), # 8.40GB, avg file size 1.40GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_mtop173p5"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       48),
  ("nof_db_files",                    590),
  ("nof_events",                      {
    'Count'                                                                          : [     23892000, ],
    'CountWeighted'                                                                  : [     23700254,     23697988,     23699482, ],
    'CountWeightedLHEWeightScale'                                                    : [     26703226,     26232368,     25928705,     24287359,     23699174,     23246880,     21980363,     21345411,     20823192, ],
    'CountWeightedLHEEnvelope'                                                       : [     28859959,     19412689, ],
    'CountWeightedPSWeight'                                                          : [     23699030,     23697405,     34350094,     23699940,     23655069,     14091920, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    238897415,    238897513,    238897520,    238897412,    238896501,    238896386, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     23710424,     23710520,     23710316, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     23752796,     23752921,     23752643, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     23727670,     23727739,     23727538, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     23782380,     23782506,     23782253, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     23732580,     23732648,     23732450, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     23804127,     23804241,     23803975, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     26718747,     26250951,     25950212,     24294015,     23709709,     23261556,     21980700,     21350781,     20832743, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     26769413,     26303943,     26005586,     24333044,     23752086,     23306872,     22010655,     21384698,     20869926, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     26738126,     26269631,     25968351,     24312103,     23726952,     23278097,     21997444,     21366596,     20847786, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     26802683,     26335959,     26036622,     24364160,     23781666,     23335207,     22039503,     21411884,     20895739, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     26745482,     26276953,     25975631,     24316686,     23731858,     23283256,     22000136,     21369816,     20851427, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     26830784,     26363782,     26064311,     24385475,     23803402,     23357270,     22055865,     21429057,     20913529, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     28866320,     19432274, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     28911198,     19477047, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     28887996,     19445497, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     28948510,     19499630, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     28893785,     19450697, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     28974467,     19519937, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     23710386,     23707666,     34357027,     23710350,     23667521,     14106061, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     23753154,     23749375,     34409713,     23752198,     23711249,     14138639, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     23727583,     23724972,     34382726,     23727643,     23684581,     14115678, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     23782677,     23779082,     34453975,     23781869,     23740514,     14155044, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     23732531,     23729818,     34388503,     23732489,     23689649,     14119680, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     23804503,     23800683,     34482648,     23803480,     23762567,     14170277, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    238974820,    238974918,    238974924,    238974819,    238973921,    238973808, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    239352606,    239352701,    239352707,    239352605,    239351714,    239351606, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    239154756,    239154855,    239154860,    239154754,    239153852,    239153740, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    239661540,    239661636,    239661641,    239661538,    239660646,    239660535, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    239201087,    239201186,    239201192,    239201085,    239200186,    239200073, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    239873249,    239873346,    239873352,    239873248,    239872356,    239872244, ],
  }),
  ("nof_tree_events",                 2172864),
  ("nof_db_events",                   23892000),
  ("fsize_local",                     9999424072), # 10.00GB, avg file size 208.32MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTToSemiLeptonic_mtop173p5"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       50),
  ("nof_db_files",                    674),
  ("nof_events",                      {
    'Count'                                                                          : [     24804000, ],
    'CountWeighted'                                                                  : [     24606932,     24608188,     24603273, ],
    'CountWeightedLHEWeightScale'                                                    : [     27723379,     27235352,     26920616,     25215200,     24606932,     24135737,     22819777,     22161096,     21619276, ],
    'CountWeightedLHEEnvelope'                                                       : [     29962037,     20155800, ],
    'CountWeightedPSWeight'                                                          : [     24605389,     24605717,     36408949,     24605151,     24530513,     13963722, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    248030585,    248030713,    248030718,    248030582,    248029237,    248029098, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     24617136,     24617128,     24617085, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     24661580,     24661530,     24661538, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     24634976,     24634983,     24634918, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     24692201,     24692201,     24692133, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     24640105,     24640124,     24640046, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     24714853,     24714845,     24714782, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     27740111,     27255225,     26943466,     25222638,     24617136,     24151416,     22820583,     22167086,     21629564, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     27793278,     27310777,     27001450,     25263649,     24661580,     24198872,     22852111,     22202678,     21668515, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     27760165,     27274568,     26962244,     25241368,     24634976,     24168542,     22837926,     22183462,     21645153, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     27827708,     27343911,     27033576,     25295862,     24692201,     24228219,     22881972,     22230827,     21695252, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     27767815,     27282187,     26969859,     25246143,     24640105,     24173952,     22840745,     22186851,     21648978, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     27856906,     27372864,     27062438,     25318056,     24714853,     24251249,     22899033,     22248753,     21713854, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     29969158,     20176622, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     30016238,     20223552, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     29991612,     20190303, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     30054884,     20246914, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     29997670,     20195721, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     30081954,     20268039, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     24617633,     24617020,     36417345,     24616424,     24543276,     13977712, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     24662490,     24660921,     36474202,     24660323,     24588456,     14009956, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     24635454,     24634902,     36444473,     24634316,     24560985,     13987242, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     24693055,     24691633,     36520921,     24691034,     24618828,     14026213, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     24640637,     24640002,     36450702,     24639372,     24566164,     13991181, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     24715841,     24714198,     36551526,     24713534,     24641571,     14041263, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    248102508,    248102637,    248102640,    248102504,    248101181,    248101041, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    248499729,    248499856,    248499859,    248499725,    248498415,    248498277, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    248288790,    248288920,    248288923,    248288786,    248287459,    248287321, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    248819441,    248819570,    248819573,    248819438,    248818123,    248817983, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    248337254,    248337383,    248337386,    248337250,    248335925,    248335785, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    249040208,    249040337,    249040341,    249040205,    249038893,    249038753, ],
  }),
  ("nof_tree_events",                 300666),
  ("nof_db_events",                   24854000),
  ("fsize_local",                     1471068920), # 1.47GB, avg file size 29.42MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTToHadronic_mtop173p5"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       5),
  ("nof_db_files",                    154),
  ("nof_events",                      {
    'Count'                                                                          : [      4574000, ],
    'CountWeighted'                                                                  : [      4537906,      4537266,      4537771, ],
    'CountWeightedLHEWeightScale'                                                    : [      5111702,      5021044,      4962195,      4651553,      4537893,      4450249,      4211429,      4088468,      3987335, ],
    'CountWeightedLHEEnvelope'                                                       : [      5525110,      3716860, ],
    'CountWeightedPSWeight'                                                          : [      4537801,      4537979,      6426609,      4538020,      4531762,      2832183, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     45734721,     45733918,     45734744,     45734721,     45698609,     45697765, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      4537444,      4537479,      4537392, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      4543103,      4543130,      4543072, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      4540938,      4540973,      4540881, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      4549135,      4549170,      4549100, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      4541376,      4541407,      4541320, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      4552245,      4552286,      4552222, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [      5111841,      5021813,      4963566,      4650215,      4537307,      4450546,      4209088,      4087179,      3986892, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [      5118810,      5029277,      4971515,      4655175,      4542970,      4456817,      4212510,      4091431,      3991825, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [      5115769,      5025603,      4967251,      4653886,      4540800,      4453909,      4212473,      4090385,      3989943, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [      5125586,      5035804,      4977858,      4661512,      4548998,      4462604,      4218392,      4096975,      3997096, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [      5116597,      5026429,      4968083,      4654236,      4541236,      4454398,      4212523,      4090550,      3990194, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [      5129777,      5039968,      4982000,      4664528,      4552107,      4465801,      4220566,      4099335,      3999600, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [      5523167,      3718584, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [      5528732,      3725201, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [      5527567,      3721266, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [      5536324,      3729812, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [      5528051,      3721841, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [      5540027,      3732844, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      4537424,      4537387,      6423971,      4537464,      4531494,      2833554, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      4543168,      4542920,      6430054,      4543020,      4537325,      2838690, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      4540917,      4540894,      6429102,      4540974,      4534976,      2835599, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      4549185,      4548968,      6438918,      4549074,      4543323,      2842193, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      4541351,      4541309,      6429411,      4541388,      4535419,      2836099, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      4552315,      4552056,      6442710,      4552176,      4546480,      2844638, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     45724818,     45724027,     45724840,     45724818,     45689072,     45688238, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     45772467,     45771686,     45772489,     45772468,     45737050,     45736224, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     45761253,     45760459,     45761276,     45761253,     45725452,     45724613, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     45835242,     45834454,     45835264,     45835242,     45799717,     45798886, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     45764990,     45764197,     45765012,     45764990,     45729223,     45728383, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     45865360,     45864575,     45865382,     45865360,     45829901,     45829071, ],
  }),
  ("nof_tree_events",                 1734381),
  ("nof_db_events",                   4958000),
  ("fsize_local",                     7408486119), # 7.41GB, avg file size 1.48GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_mtop175p5"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       10),
  ("nof_db_files",                    283),
  ("nof_events",                      {
    'Count'                                                                          : [      9603000, ],
    'CountWeighted'                                                                  : [      9526486,      9527954,      9526650, ],
    'CountWeightedLHEWeightScale'                                                    : [     10733246,     10542247,     10418091,      9765976,      9526435,      9342288,      8841034,      8582527,      8369891, ],
    'CountWeightedLHEEnvelope'                                                       : [     11599345,      7803857, ],
    'CountWeightedPSWeight'                                                          : [      9526979,      9523922,     13495508,      9526653,      9521156,      5946448, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     96059361,     96057752,     96059429,     96059356,     95982981,     95981229, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      9525647,      9525654,      9525604, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      9537280,      9537281,      9537293, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      9532991,      9533001,      9532953, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      9549974,      9549963,      9549974, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      9533814,      9533825,      9533800, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      9556361,      9556357,      9556389, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     10733183,     10543485,     10420573,      9762933,      9525356,      9342686,      8835989,      8579661,      8368806, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     10747472,     10558796,     10436890,      9773105,      9536982,      9355594,      8843059,      8588455,      8379019, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     10741451,     10551470,     10428326,      9770641,      9532699,      9349742,      8843117,      8586404,      8375236, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     10761757,     10572554,     10450247,      9786444,      9549674,      9367759,      8855394,      8600102,      8390081, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     10743110,     10553135,     10429989,      9771322,      9533524,      9350695,      8843151,      8586671,      8375678, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     10770398,     10581141,     10458789,      9792625,      9556066,      9374337,      8859833,      8604916,      8395187, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     11595024,      7807185, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     11606466,      7820816, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     11604258,      7812845, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     11622439,      7830533, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     11605204,      7813991, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     11630028,      7836769, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      9525921,      9522390,     13489782,      9525308,      9520551,      5949148, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      9537678,      9533707,     13502357,      9536776,      9532744,      5959745, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      9533265,      9529777,     13500540,      9532682,      9527852,      5953451, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      9550353,      9546448,     13520970,      9549492,      9545330,      5967136, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      9534096,      9530563,     13501139,      9533488,      9528752,      5954447, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      9556784,      9552783,     13528847,      9555844,      9551907,      5972139, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     95995657,     95994079,     95995726,     95995652,     95920215,     95918491, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     96093087,     96091530,     96093157,     96093083,     96018299,     96016592, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     96072303,     96070725,     96072375,     96072300,     95996730,     95995002, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     96225338,     96223776,     96225410,     96225334,     96150315,     96148603, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     96079295,     96077718,     96079365,     96079291,     96003782,     96002054, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     96286813,     96285254,     96286885,     96286810,     96211892,     96210184, ],
  }),
  ("nof_tree_events",                 3646124),
  ("nof_db_events",                   9603000),
  ("fsize_local",                     15572209724), # 15.57GB, avg file size 1.56GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_mtop175p5_ext1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       20),
  ("nof_db_files",                    475),
  ("nof_events",                      {
    'Count'                                                                          : [     19625000, ],
    'CountWeighted'                                                                  : [     19472157,     19469323,     19465207, ],
    'CountWeightedLHEWeightScale'                                                    : [     21929717,     21542112,     21291195,     19954671,     19471487,     19093517,     18065789,     17539489,     17106525, ],
    'CountWeightedLHEEnvelope'                                                       : [     23700894,     15948902, ],
    'CountWeightedPSWeight'                                                          : [     19469330,     19469905,     28227352,     19467184,     19428405,     11567283, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    196239732,    196239866,    196239866,    196239733,    196238983,    196238853, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     19466244,     19466249,     19466162, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     19490284,     19490214,     19490343, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     19481240,     19481229,     19481146, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     19516146,     19516100,     19516173, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     19482977,     19482972,     19482937, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     19529352,     19529299,     19529430, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     21929999,     21545038,     21296591,     19948739,     19465649,     19094554,     18055720,     17533852,     17104468, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     21959606,     21576684,     21330254,     19969845,     19489682,     19121149,     18070379,     17551990,     17125500, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     21946844,     21561290,     21312383,     19964467,     19480625,     19108953,     18070264,     17547595,     17117567, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     21988682,     21604698,     21357455,     19997011,     19515558,     19145960,     18095542,     17575750,     17148068, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     21950302,     21564753,     21315864,     19965916,     19482387,     19110932,     18070368,     17548210,     17118541, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     22006499,     21622384,     21375048,     20009796,     19528757,     19159517,     18104745,     17585700,     17158624, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     23692456,     15955921, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     23716182,     15983966, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     23711277,     15967460, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     23748741,     16003784, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     23713273,     15969823, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     23764455,     16016601, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     19467419,     19467251,     28216676,     19464433,     19427237,     11572267, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     19491828,     19490840,     28244219,     19488011,     19452191,     11592607, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     19482373,     19482287,     28239015,     19479466,     19442120,     11580649, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     19517638,     19516776,     28282873,     19513959,     19477838,     11607003, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     19484189,     19483993,     28240462,     19481155,     19443936,     11582545, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     19530933,     19529911,     28299693,     19527030,     19491180,     11616692, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    196181562,    196181693,    196181693,    196181562,    196180822,    196180689, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    196382245,    196382380,    196382380,    196382245,    196381519,    196381386, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    196337845,    196337979,    196337979,    196337846,    196337108,    196336975, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    196652145,    196652278,    196652278,    196652146,    196651419,    196651286, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    196352913,    196353049,    196353049,    196352913,    196352176,    196352044, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    196779238,    196779371,    196779371,    196779238,    196778508,    196778374, ],
  }),
  ("nof_tree_events",                 1786340),
  ("nof_db_events",                   19625000),
  ("fsize_local",                     8233019161), # 8.23GB, avg file size 411.65MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTToSemiLeptonic_mtop175p5"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       20),
  ("nof_db_files",                    254),
  ("nof_events",                      {
    'Count'                                                                          : [      9773000, ],
    'CountWeighted'                                                                  : [      9694384,      9695319,      9693706, ],
    'CountWeightedLHEWeightScale'                                                    : [     10921103,     10726990,     10601000,      9937578,      9694056,      9507111,      8997001,      8734203,      8517971, ],
    'CountWeightedLHEEnvelope'                                                       : [     11802823,      7941597, ],
    'CountWeightedPSWeight'                                                          : [      9695000,      9693205,     14056527,      9694141,      9677202,      5760384, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     97721844,     97721886,     97721886,     97721845,     97721424,     97721381, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      9693073,      9693066,      9693073, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      9704631,      9704666,      9704611, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      9700568,      9700564,      9700574, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      9717596,      9717609,      9717565, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      9701354,      9701353,      9701336, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      9723976,      9724032,      9723927, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     10920775,     10727993,     10603242,      9934193,      9692776,      9507217,      8991594,      8730994,      8516586, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     10935061,     10743307,     10619562,      9944291,      9704333,      9520066,      8998512,      8739663,      8526701, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     10929197,     10736127,     10611148,      9942060,      9700277,      9514424,      8998868,      8737877,      8523139, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     10949610,     10757330,     10633181,      9957885,      9717285,      9532492,      9011110,      8751553,      8538014, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     10930824,     10737752,     10612771,      9942686,      9701056,      9515323,      8998843,      8738094,      8523545, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     10958280,     10765927,     10641736,      9964071,      9723681,      9539053,      9015514,      8756343,      8543092, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     11798059,      7944816, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     11809333,      7958500, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     11807483,      7950577, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     11825641,      7968412, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     11808364,      7951686, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     11833233,      7974646, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      9693660,      9691427,     14050510,      9692435,      9676185,      5762656, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      9705393,      9702726,     14063556,      9703793,      9688196,      5772589, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      9701156,      9698941,     14061698,      9699955,      9683638,      5766855, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      9718317,      9715710,     14082925,      9716773,      9701056,      5779798, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      9701947,      9699682,     14062274,      9700701,      9684485,      5767760, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      9724756,      9722020,     14091019,      9723106,      9707580,      5784541, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     97692084,     97692124,     97692124,     97692084,     97691667,     97691627, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     97788470,     97788509,     97788509,     97788471,     97788058,     97788019, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     97770241,     97770281,     97770281,     97770241,     97769824,     97769783, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     97923463,     97923501,     97923501,     97923463,     97923050,     97923012, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     97776916,     97776956,     97776956,     97776916,     97776499,     97776460, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     97984968,     97985007,     97985007,     97984969,     97984554,     97984516, ],
  }),
  ("nof_tree_events",                 891163),
  ("nof_db_events",                   9773000),
  ("fsize_local",                     4120415072), # 4.12GB, avg file size 206.02MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTToSemiLeptonic_mtop175p5_ext1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       19),
  ("nof_db_files",                    499),
  ("nof_events",                      {
    'Count'                                                                          : [     18080000, ],
    'CountWeighted'                                                                  : [     17936816,     17935809,     17933097, ],
    'CountWeightedLHEWeightScale'                                                    : [     20204489,     19846083,     19613694,     18384745,     17936816,     17589440,     16644426,     16158775,     15759125, ],
    'CountWeightedLHEEnvelope'                                                       : [     21836558,     14692086, ],
    'CountWeightedPSWeight'                                                          : [     17935440,     17939287,     26555208,     17936216,     17883297,     10170170, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    180773883,    180773999,    180774009,    180773878,    180772650,    180772511, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     17933675,     17933640,     17933652, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     17955795,     17955756,     17955780, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     17947480,     17947463,     17947486, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     17979638,     17979604,     17979655, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     17949129,     17949053,     17949135, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     17991808,     17991771,     17991821, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     20204606,     19848722,     19618695,     18379157,     17933675,     17590371,     16635039,     16153492,     15757224, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     20231740,     19877807,     19649715,     18398487,     17955795,     17614875,     16648451,     16170164,     15776586, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     20220143,     19863714,     19633257,     18393660,     17947480,     17603648,     16648448,     16166168,     15769298, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     20258575,     19903658,     19674778,     18423556,     17979638,     17637771,     16671674,     16192062,     15797406, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     20223345,     19866920,     19636470,     18394992,     17949129,     17605493,     16648559,     16166733,     15770217, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     20274991,     19919934,     19691014,     18435322,     17991808,     17650254,     16680129,     16201247,     15807123, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     21828618,     14698580, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     21850324,     14724430, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     21845985,     14709213, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     21880376,     14742700, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     21847843,     14711402, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     21894842,     14754513, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     17933644,     17936760,     26545624,     17933715,     17882129,     10174294, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     17956049,     17958435,     26572041,     17955426,     17905022,     10191948, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     17947449,     17950640,     26566635,     17947563,     17895822,     10181690, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     17979851,     17982372,     26608353,     17979341,     17928637,     10204647, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     17949095,     17952207,     26568101,     17949136,     17897561,     10183328, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     17992102,     17994442,     26624413,     17991403,     17941022,     10213080, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    180736681,    180736791,    180736800,    180736673,    180735461,    180735324, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    180921896,    180922006,    180922015,    180921889,    180920693,    180920560, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    180880897,    180881012,    180881022,    180880893,    180879687,    180879548, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    181170201,    181170312,    181170322,    181170194,    181168996,    181168858, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    180894863,    180894973,    180894983,    180894856,    180893643,    180893503, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    181287850,    181287964,    181287973,    181287845,    181286650,    181286513, ],
  }),
  ("nof_tree_events",                 220664),
  ("nof_db_events",                   18280000),
  ("fsize_local",                     1073850028), # 1.07GB, avg file size 56.52MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTToHadronic_mtop175p5"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       6),
  ("nof_db_files",                    76),
  ("nof_events",                      {
    'Count'                                                                          : [      2416000, ],
    'CountWeighted'                                                                  : [      2396629,      2396709,      2396955, ],
    'CountWeightedLHEWeightScale'                                                    : [      2699606,      2651019,      2619153,      2457780,      2396629,      2349539,      2226128,      2160069,      2105617, ],
    'CountWeightedLHEEnvelope'                                                       : [      2917424,      1963318, ],
    'CountWeightedPSWeight'                                                          : [      2396782,      2396341,      3397659,      2396700,      2395001,      1493824, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     24158209,     24157579,     24158239,     24158208,     24132065,     24131375, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      2394429,      2394499,      2394350, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      2395386,      2395476,      2395296, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      2396431,      2396503,      2396355, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      2398870,      2398957,      2398779, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      2396232,      2396310,      2396150, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      2399649,      2399748,      2399550, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [      2697289,      2649066,      2617536,      2454920,      2394429,      2347625,      2222960,      2157497,      2103546, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [      2698674,      2650737,      2619478,      2455469,      2395386,      2348935,      2222915,      2157934,      2104381, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [      2699545,      2651243,      2619652,      2457018,      2396431,      2349551,      2224899,      2159333,      2105294, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [      2702592,      2654516,      2623148,      2459122,      2398870,      2352280,      2226296,      2161124,      2107418, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [      2699509,      2651207,      2619613,      2456781,      2396232,      2349386,      2224540,      2159038,      2105049, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [      2703839,      2655747,      2624366,      2459847,      2399649,      2353106,      2226664,      2161598,      2107969, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [      2913823,      1962503, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [      2914278,      1964341, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [      2916335,      1964053, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [      2918655,      1967020, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [      2916077,      1964003, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [      2919554,      1967905, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      2394466,      2393936,      3393306,      2394320,      2392760,      1493216, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      2395455,      2394843,      3393672,      2395244,      2393819,      1494637, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      2396469,      2395945,      3396235,      2396328,      2394751,      1494391, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      2398932,      2398337,      3398780,      2398728,      2397282,      1496671, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      2396273,      2395743,      3395827,      2396125,      2394577,      1494378, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      2399719,      2399106,      3399610,      2399507,      2398108,      1497395, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     24128947,     24128324,     24128976,     24128945,     24103085,     24102402, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     24133556,     24132939,     24133584,     24133554,     24107923,     24107247, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     24149820,     24149195,     24149849,     24149818,     24123910,     24123227, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     24169790,     24169172,     24169819,     24169789,     24144074,     24143397, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     24147567,     24146943,     24147596,     24147565,     24121674,     24120991, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     24177075,     24176456,     24177103,     24177073,     24151387,     24150710, ],
  }),
  ("nof_tree_events",                 922007),
  ("nof_db_events",                   2416000),
  ("fsize_local",                     3969258154), # 3.97GB, avg file size 661.54MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_mtop178p5"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       10),
  ("nof_db_files",                    256),
  ("nof_events",                      {
    'Count'                                                                          : [      9762000, ],
    'CountWeighted'                                                                  : [      9685867,      9683141,      9684041, ],
    'CountWeightedLHEWeightScale'                                                    : [     10909569,     10713388,     10584852,      9931823,      9685867,      9494648,      8995459,      8728469,      8508702, ],
    'CountWeightedLHEEnvelope'                                                       : [     11789748,      7933771, ],
    'CountWeightedPSWeight'                                                          : [      9685115,      9684006,     14053885,      9685697,      9670239,      5747816, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     97634674,     97634697,     97634697,     97634675,     97634009,     97633987, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      9675616,      9675632,      9675605, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      9679318,      9679281,      9679379, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      9683731,      9683745,      9683708, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      9693421,      9693378,      9693452, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      9682961,      9682960,      9682950, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      9696612,      9696569,      9696664, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     10899932,     10705296,     10578203,      9919987,      9675616,      9486773,      8982392,      8717884,      8500146, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     10905270,     10711894,     10585955,      9921951,      9679318,      9491948,      8981975,      8719463,      8503383, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     10909052,     10714118,     10586761,      9928476,      9683731,      9494574,      8990250,      8725319,      8507234, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     10921126,     10727172,     10600801,      9936738,      9693421,      9505480,      8995649,      8732394,      8515682, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     10908906,     10713990,     10586655,      9927518,      9682961,      9493938,      8988794,      8724145,      8506283, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     10926157,     10732210,     10605835,      9939658,      9696612,      9508903,      8997138,      8734333,      8517967, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     11774948,      7930296, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     11776572,      7937573, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     11785110,      7936567, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     11794277,      7948418, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     11784087,      7936390, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     11797969,      7952020, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      9675591,      9674011,     14036071,      9675744,      9661164,      5745220, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      9679469,      9677398,     14037788,      9679175,      9665427,      5750455, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      9683682,      9682149,     14048128,      9683866,      9669193,      5749771, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      9693525,      9691553,     14058799,      9693315,      9679363,      5758324, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      9682931,      9681307,     14046507,      9683065,      9668529,      5749721, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      9696765,      9694639,     14062410,      9696450,      9682815,      5761116, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     97499057,     97499077,     97499077,     97499057,     97498405,     97498386, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     97515498,     97515515,     97515515,     97515498,     97514856,     97514840, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     97583372,     97583391,     97583391,     97583372,     97582716,     97582696, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     97662144,     97662161,     97662161,     97662144,     97661501,     97661483, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     97574361,     97574381,     97574381,     97574362,     97573705,     97573686, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     97691778,     97691796,     97691796,     97691778,     97691136,     97691119, ],
  }),
  ("nof_tree_events",                 890456),
  ("nof_db_events",                   9762000),
  ("fsize_local",                     4130588662), # 4.13GB, avg file size 413.06MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTToSemiLeptonic_mtop178p5"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       10),
  ("nof_db_files",                    247),
  ("nof_events",                      {
    'Count'                                                                          : [      9782000, ],
    'CountWeighted'                                                                  : [      9703512,      9705680,      9704809, ],
    'CountWeightedLHEWeightScale'                                                    : [     10930941,     10735060,     10607011,      9952082,      9703512,      9515148,      9014403,      8747233,      8527335, ],
    'CountWeightedLHEEnvelope'                                                       : [     11813835,      7950358, ],
    'CountWeightedPSWeight'                                                          : [      9705681,      9706766,     14371886,      9705521,      9673392,      5498443, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     97834072,     97834145,     97834154,     97834072,     97833193,     97833100, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      9695973,      9695932,      9696015, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      9699718,      9699675,      9699752, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      9704129,      9704079,      9704156, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      9713857,      9713815,      9713890, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      9703362,      9703324,      9703392, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      9717104,      9717088,      9717125, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     10921443,     10727019,     10600291,      9940306,      9695973,      9507208,      9001379,      8736641,      8518716, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     10926933,     10733665,     10608036,      9942395,      9699718,      9512356,      9001023,      8738239,      8521936, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     10930590,     10735869,     10608889,      9948832,      9704129,      9515044,      9009262,      8744104,      8525835, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     10942839,     10749016,     10622929,      9957231,      9713857,      9525945,      9014761,      8751217,      8534278, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     10930468,     10735762,     10608799,      9947888,      9703362,      9514424,      9007831,      8742947,      8524897, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     10947926,     10754079,     10627991,      9960199,      9717104,      9529396,      9016309,      8753200,      8536601, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     11799003,      7946959, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     11800653,      7954331, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     11809226,      7953236, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     11818442,      7965200, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     11808233,      7953069, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     11822204,      7968818, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      9696203,      9696771,     14354064,      9695702,      9664349,      5495832, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      9700073,      9700209,     14356242,      9699227,      9668656,      5500727, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      9704333,      9704939,     14366398,      9703860,      9672400,      5500205, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      9714196,      9714411,     14377698,      9713408,      9682629,      5508287, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      9703587,      9704154,     14364792,      9703074,      9671702,      5500147, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      9717475,      9717595,     14381476,      9716595,      9685977,      5510925, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     97699618,     97699696,     97699704,     97699618,     97698753,     97698662, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     97717059,     97717136,     97717143,     97717059,     97716204,     97716114, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     97784182,     97784258,     97784267,     97784182,     97783314,     97783222, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     97863960,     97864040,     97864048,     97863960,     97863108,     97863015, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     97775322,     97775402,     97775411,     97775322,     97774461,     97774368, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     97894095,     97894174,     97894181,     97894096,     97893244,     97893151, ],
  }),
  ("nof_tree_events",                 118479),
  ("nof_db_events",                   9782000),
  ("fsize_local",                     581028065), # 581.03MB, avg file size 58.10MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTToHadronic_mtop178p5"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       10),
  ("nof_db_files",                    139),
  ("nof_events",                      {
    'Count'                                                                          : [      4776000, ],
    'CountWeighted'                                                                  : [      4737858,      4737710,      4737817, ],
    'CountWeightedLHEWeightScale'                                                    : [      5338885,      5245363,      5185316,      4854301,      4737777,      4647928,      4392015,      4266112,      4162541, ],
    'CountWeightedLHEEnvelope'                                                       : [      5769706,      3880995, ],
    'CountWeightedPSWeight'                                                          : [      4737923,      4737103,      6706450,      4737318,      4732791,      2960039, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     47754904,     47754473,     47754937,     47754905,     47728375,     47727877, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      4741396,      4741322,      4741468, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      4751374,      4751308,      4751430, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      4744714,      4744635,      4744786, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      4757051,      4756977,      4757105, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      4745991,      4745909,      4746069, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      4762005,      4761937,      4762071, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [      5343746,      5250814,      5191333,      4857237,      4741252,      4652404,      4393546,      4268607,      4165829, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [      5355567,      5263074,      5204060,      4866579,      4751228,      4662946,      4400930,      4276744,      4174590, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [      5347473,      5254405,      5194823,      4860721,      4744570,      4655586,      4396771,      4271649,      4168726, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [      5361945,      5269211,      5210006,      4872557,      4756902,      4668380,      4406470,      4281957,      4179545, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [      5349276,      5256202,      5196618,      4861937,      4745846,      4656919,      4397577,      4272561,      4169719, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [      5368242,      5275466,      5216240,      4877431,      4761860,      4673409,      4410287,      4285940,      4183647, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [      5772895,      3886184, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [      5783707,      3896364, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [      5777067,      3888727, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [      5790867,      3900689, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [      5778586,      3890013, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [      5796805,      3905251, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      4741776,      4740714,      6709778,      4740952,      4736824,      2964103, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      4751853,      4750543,      6721952,      4750805,      4747043,      2971994, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      4745087,      4744044,      6714637,      4744276,      4740112,      2966034, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      4757512,      4756241,      6730296,      4756498,      4752668,      2975274, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      4746380,      4745305,      6716141,      4745539,      4741415,      2967084, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      4762507,      4761165,      6736668,      4761420,      4757681,      2978903, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     47787112,     47786683,     47787143,     47787113,     47760825,     47760332, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     47878049,     47877622,     47878080,     47878050,     47851973,     47851485, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     47821784,     47821353,     47821815,     47821785,     47795452,     47794958, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     47937409,     47936979,     47937439,     47937409,     47911253,     47910762, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     47834075,     47833646,     47834107,     47834076,     47807761,     47807267, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     47986053,     47985625,     47986083,     47986054,     47959919,     47959430, ],
  }),
  ("nof_tree_events",                 1801864),
  ("nof_db_events",                   4776000),
  ("fsize_local",                     7655272566), # 7.66GB, avg file size 765.53MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_widthx0p7"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       39),
  ("nof_db_files",                    545),
  ("nof_events",                      {
    'Count'                                                                          : [     19050000, ],
    'CountWeighted'                                                                  : [     18895705,     18894840,     18894776, ],
    'CountWeightedLHEWeightScale'                                                    : [     21289180,     20917892,     20679358,     19359148,     18895705,     18537453,     17516940,     17015038,     16602365, ],
    'CountWeightedLHEEnvelope'                                                       : [     23008498,     15478495, ],
    'CountWeightedPSWeight'                                                          : [     18895294,     18891955,     27382148,     18894092,     18860085,     11238183, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    190513880,    190513933,    190513933,    190513875,    190513271,    190513214, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     18909350,     18909458,     18909237, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     18948874,     18948998,     18948736, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     18922637,     18922738,     18922538, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     18971607,     18971732,     18971461, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     18927757,     18927863,     18927651, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     18991405,     18991533,     18991312, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     21308381,     20939376,     20703070,     19370581,     18909350,     18554968,     17522701,     17024650,     16615146, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     21355340,     20988050,     20753561,     19407582,     18948874,     18596722,     17551871,     17056818,     16649777, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     21323301,     20953766,     20717026,     19384522,     18922637,     18567723,     17535624,     17036850,     16626744, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     21380880,     21012625,     20777380,     19431496,     18971607,     18618489,     17574050,     17077715,     16669619, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     21330519,     20960946,     20724210,     19389405,     18927757,     18573042,     17538864,     17040509,     16630719, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     21406052,     21037585,     20802245,     19450996,     18991405,     18638558,     17589340,     17093628,     16686005, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     23020989,     15498854, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     23063907,     15539141, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     23037699,     15509035, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     23092594,     15556457, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     23043804,     15514166, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     23116326,     15574664, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     18910276,     18906132,     27396109,     18908353,     18875723,     11253019, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     18950101,     18945161,     27446255,     18947477,     18916089,     11282441, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     18923538,     18919460,     27415960,     18921671,     18888914,     11260421, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     18972775,     18967962,     27480340,     18970264,     18938646,     11295013, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     18928699,     18924526,     27422279,     18926738,     18894137,     11264366, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     18992683,     18987646,     27506674,     18989969,     18958649,     11308693, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    190604147,    190604200,    190604200,    190604143,    190603556,    190603499, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    190962548,    190962600,    190962600,    190962544,    190961964,    190961909, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    190742936,    190742989,    190742989,    190742931,    190742340,    190742284, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    191200190,    191200242,    191200242,    191200187,    191199601,    191199544, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    190791905,    190791957,    190791957,    190791901,    190791310,    190791254, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    191393727,    191393779,    191393779,    191393723,    191393137,    191393083, ],
  }),
  ("nof_tree_events",                 1733789),
  ("nof_db_events",                   19500000),
  ("fsize_local",                     7963137399), # 7.96GB, avg file size 204.18MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTToSemiLeptonic_widthx0p7"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       5),
  ("nof_db_files",                    139),
  ("nof_events",                      {
    'Count'                                                                          : [      4790000, ],
    'CountWeighted'                                                                  : [      4750753,      4750875,      4750772, ],
    'CountWeightedLHEWeightScale'                                                    : [      5352792,      5258705,      5198275,      4868065,      4750709,      4660638,      4405302,      4278719,      4174622, ],
    'CountWeightedLHEEnvelope'                                                       : [      5784890,      3892104, ],
    'CountWeightedPSWeight'                                                          : [      4751240,      4751058,      6724736,      4750222,      4745137,      2968300, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     47910975,     47910449,     47911022,     47910975,     47884316,     47883693, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      4754507,      4754516,      4754509, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      4764459,      4764462,      4764486, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      4757849,      4757844,      4757845, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      4770175,      4770174,      4770189, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      4759137,      4759137,      4759144, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      4775163,      4775139,      4775195, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [      5357628,      5264128,      5204274,      4870941,      4754362,      4665060,      4406751,      4281140,      4177845, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [      5369449,      5276397,      5217002,      4880257,      4764313,      4675580,      4414095,      4289232,      4186567, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [      5361376,      5267753,      5207774,      4874457,      4757703,      4668271,      4410008,      4284205,      4180761, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [      5375877,      5282577,      5222981,      4886278,      4770030,      4681044,      4419676,      4294494,      4191553, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [      5363211,      5269564,      5209588,      4875685,      4758995,      4669610,      4410818,      4285124,      4181761, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [      5382217,      5288871,      5229242,      4891187,      4775016,      4686098,      4423513,      4298481,      4195668, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [      5788050,      3897220, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [      5798863,      3907357, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [      5792253,      3899781, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [      5806086,      3911713, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [      5793799,      3901075, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [      5812051,      3916289, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      4755015,      4754642,      6727985,      4753849,      4749087,      2972321, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      4765040,      4764479,      6740130,      4763708,      4759256,      2980186, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      4758347,      4757988,      6732878,      4757191,      4752402,      2974268, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      4770743,      4770215,      6748528,      4769437,      4764922,      2983495, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      4759649,      4759272,      6734406,      4758469,      4753717,      2975321, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      4775739,      4775165,      6754950,      4774385,      4769972,      2987138, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     47926313,     47925794,     47926359,     47926313,     47899967,     47899356, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     48016656,     48016143,     48016702,     48016656,     47990535,     47989930, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     47961200,     47960680,     47961249,     47961200,     47934805,     47934192, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     48076380,     48075867,     48076428,     48076380,     48050175,     48049565, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     47973412,     47972894,     47973461,     47973412,     47947040,     47946426, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     48124902,     48124386,     48124946,     48124902,     48098721,     48098116, ],
  }),
  ("nof_tree_events",                 1808171),
  ("nof_db_events",                   4790000),
  ("fsize_local",                     7675888910), # 7.68GB, avg file size 1.54GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_widthx0p85"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       30),
  ("nof_db_files",                    540),
  ("nof_events",                      {
    'Count'                                                                          : [     14766000, ],
    'CountWeighted'                                                                  : [     14647556,     14647606,     14646476, ],
    'CountWeightedLHEWeightScale'                                                    : [     16503861,     16214465,     16028179,     15007875,     14647556,     14368687,     13579945,     13190052,     12869324, ],
    'CountWeightedLHEEnvelope'                                                       : [     17836624,     11997932, ],
    'CountWeightedPSWeight'                                                          : [     14647479,     14646201,     21224158,     14645694,     14617400,      8711726, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    147677172,    147677257,    147677257,    147677171,    147676739,    147676651, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     14657818,     14657892,     14657743, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     14688229,     14688293,     14688140, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     14668135,     14668201,     14668062, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     14705886,     14705930,     14705791, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     14672058,     14672115,     14671977, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     14721138,     14721176,     14721067, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     16518437,     16230832,     16046258,     15016515,     14657818,     14382032,     13584217,     13197299,     12879032, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     16554551,     16268290,     16085109,     15044972,     14688229,     14414153,     13606638,     13222039,     12905691, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     16530035,     16242005,     16057101,     15027341,     14668135,     14391934,     13594248,     13206769,     12888044, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     16574387,     16287376,     16103610,     15063554,     14705886,     14431064,     13623870,     13238268,     12921102, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     16535578,     16247520,     16062617,     15031072,     14672058,     14396015,     13596716,     13209561,     12891081, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     16593791,     16306614,     16122770,     15078566,     14721138,     14446523,     13635631,     13250512,     12933712, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     17845904,     12013609, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     17878790,     12044733, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     17858895,     12021506, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     17901083,     12058174, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     17863568,     12025446, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     17919374,     12072192, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     14658867,     14656907,     21234659,     14656483,     14629347,      8723083, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     14689544,     14686880,     21273213,     14686551,     14660468,      8745739, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     14669169,     14667255,     21250066,     14666826,     14639578,      8728828, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     14707158,     14704596,     21299671,     14704264,     14677972,      8755509, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     14673131,     14671102,     21254884,     14670707,     14643610,      8731860, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     14722489,     14719687,     21319911,     14719421,     14693445,      8766066, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    147738615,    147738699,    147738699,    147738614,    147738190,    147738102, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    148014955,    148015040,    148015040,    148014955,    148014532,    148014444, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    147846198,    147846282,    147846282,    147846198,    147845772,    147845684, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    148199274,    148199359,    148199359,    148199275,    148198852,    148198764, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    147883727,    147883812,    147883812,    147883726,    147883301,    147883213, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    148348332,    148348416,    148348416,    148348331,    148347914,    148347826, ],
  }),
  ("nof_tree_events",                 1342723),
  ("nof_db_events",                   19800000),
  ("fsize_local",                     6168548125), # 6.17GB, avg file size 205.62MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTToSemiLeptonic_widthx0p85"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("fsize_local",                     935210040), # 935.21MB, avg file size 935.21MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_widthx1p15"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       20),
  ("nof_db_files",                    546),
  ("nof_events",                      {
    'Count'                                                                          : [     19089000, ],
    'CountWeighted'                                                                  : [     18936427,     18935923,     18933015, ],
    'CountWeightedLHEWeightScale'                                                    : [     21336568,     20962845,     20722573,     19401168,     18936427,     18575827,     17554470,     17050733,     16636459, ],
    'CountWeightedLHEEnvelope'                                                       : [     23058727,     15510719, ],
    'CountWeightedPSWeight'                                                          : [     18934715,     18934739,     27442720,     18934574,     18900998,     11261911, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    190861425,    190861509,    190861509,    190861425,    190860817,    190860734, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     18949202,     18949418,     18948880, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     18988619,     18988898,     18988328, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     18962512,     18962728,     18962229, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     19011453,     19011697,     19011145, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     18967616,     18967819,     18967318, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     19031169,     19031439,     19030879, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     21355522,     20984118,     20746088,     19412428,     18949202,     18593213,     17560117,     17060260,     16649130, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     21402341,     21032665,     20796434,     19449338,     18988619,     18634877,     17589211,     17092346,     16683706, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     21370525,     20998560,     20760107,     19426431,     18962512,     18606008,     17573080,     17072497,     16660774, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     21428010,     21057340,     20820352,     19473347,     19011453,     18656712,     17611477,     17113331,     16703613, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     21377700,     21005704,     20767226,     19431280,     18967616,     18611265,     17576281,     17076100,     16664686, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     21453114,     21082208,     20845124,     19492764,     19031169,     18676672,     17626685,     17129140,     16719898, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     23070975,     15530950, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     23113748,     15571167, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     23087749,     15541174, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     23142545,     15588567, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     23093778,     15546271, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     23166147,     15606720, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     18949582,     18948676,     27456495,     18948623,     18916626,     11276649, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     18989353,     18987514,     27506544,     18987609,     18957005,     11306011, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     18962889,     18962065,     27476421,     18961983,     18929815,     11284082, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     19012109,     19010438,     27540707,     19010505,     18979581,     11318624, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     18968027,     18967094,     27482644,     18967000,     18934971,     11287988, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     19031947,     19030035,     27566902,     19030087,     18999462,     11332255, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    190991937,    190992018,    190992018,    190991937,    190991334,    190991253, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    191349407,    191349486,    191349487,    191349407,    191348809,    191348727, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    191131454,    191131539,    191131539,    191131454,    191130855,    191130771, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    191588064,    191588142,    191588143,    191588064,    191587466,    191587386, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    191179682,    191179763,    191179763,    191179682,    191179082,    191179001, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    191780708,    191780788,    191780789,    191780708,    191780110,    191780029, ],
  }),
  ("nof_tree_events",                 1736053),
  ("nof_db_events",                   19137000),
  ("fsize_local",                     7947411118), # 7.95GB, avg file size 397.37MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTToSemiLeptonic_widthx1p15"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       5),
  ("nof_db_files",                    157),
  ("nof_events",                      {
    'Count'                                                                          : [      4296000, ],
    'CountWeighted'                                                                  : [      4260878,      4262527,      4261853, ],
    'CountWeightedLHEWeightScale'                                                    : [      4802690,      4718185,      4663700,      4366934,      4260815,      4180520,      3951106,      3837496,      3744079, ],
    'CountWeightedLHEEnvelope'                                                       : [      5190134,      3490762, ],
    'CountWeightedPSWeight'                                                          : [      4261706,      4260878,      6030700,      4261277,      4256570,      2663440, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [     42958372,     42957983,     42958391,     42958372,     42934596,     42934167, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [      4264923,      4264932,      4264926, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [      4273875,      4273859,      4273890, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [      4267912,      4267922,      4267922, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [      4278985,      4278982,      4278999, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [      4269075,      4269076,      4269083, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [      4283471,      4283454,      4283491, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [      4807018,      4723049,      4669085,      4369529,      4264790,      4184518,      3952442,      3839713,      3747012, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [      4817605,      4734044,      4680511,      4377892,      4273743,      4193980,      3959050,      3847004,      3754872, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [      4810386,      4726290,      4672225,      4372677,      4267782,      4187389,      3955354,      3842458,      3749622, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [      4823370,      4739576,      4685869,      4383285,      4278857,      4198881,      3964049,      3851708,      3759332, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [      4812018,      4727922,      4673856,      4373775,      4268945,      4188607,      3956088,      3843287,      3750525, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [      4829040,      4745218,      4691498,      4387680,      4283341,      4203420,      3967495,      3855305,      3763046, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [      5192972,      3495376, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [      5202675,      3504490, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [      5196744,      3497672, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [      5209142,      3508386, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [      5198124,      3498822, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [      5214508,      3512491, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [      4265165,      4264110,      6033601,      4264534,      4260102,      2667079, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [      4274195,      4272938,      6044444,      4273362,      4269200,      2674168, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [      4268148,      4267111,      6037986,      4267536,      4263074,      2668820, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [      4279294,      4278085,      6051989,      4278507,      4274288,      2677131, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [      4269317,      4268259,      6039330,      4268683,      4264234,      2669775, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [      4283795,      4282540,      6057706,      4282959,      4278763,      2680410, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [     42984020,     42983637,     42984040,     42984020,     42960453,     42960035, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [     43065249,     43064877,     43065269,     43065249,     43041863,     43041449, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [     43015181,     43014798,     43015200,     43015181,     42991578,     42991157, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [     43118642,     43118269,     43118662,     43118642,     43095186,     43094769, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [     43026086,     43025704,     43026106,     43026086,     43002498,     43002077, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [     43162344,     43161968,     43162363,     43162344,     43138913,     43138498, ],
  }),
  ("nof_tree_events",                 1619226),
  ("nof_db_events",                   4796000),
  ("fsize_local",                     6871865603), # 6.87GB, avg file size 1.37GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTTo2L2Nu_widthx1p3"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       20),
  ("nof_db_files",                    549),
  ("nof_events",                      {
    'Count'                                                                          : [     19110000, ],
    'CountWeighted'                                                                  : [     18960031,     18957719,     18955745, ],
    'CountWeightedLHEWeightScale'                                                    : [     21359596,     20986275,     20746592,     19421761,     18960031,     18596772,     17572683,     17069047,     16654914, ],
    'CountWeightedLHEEnvelope'                                                       : [     23083199,     15528590, ],
    'CountWeightedPSWeight'                                                          : [     18955129,     18956119,     27471981,     18956032,     18920715,     11274931, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [    191088557,    191088625,    191088625,    191088556,    191088007,    191087940, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [     18970032,     18969926,     18970071, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [     19009566,     19009492,     19009648, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [     18983355,     18983250,     18983389, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [     19032378,     19032297,     19032447, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [     18988399,     18988282,     18988442, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [     19052047,     19051943,     19052113, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [     21378669,     21007686,     20770282,     19433117,     18970032,     18614283,     17578384,     17078657,     16667685, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [     21425603,     21056375,     20820810,     19470089,     19009566,     18656064,     17607541,     17110849,     16702355, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [     21393658,     21022124,     20784296,     19447113,     18983355,     18627059,     17591357,     17090897,     16679315, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [     21451252,     21081052,     20844711,     19494101,     19032378,     18677904,     17629819,     17131821,     16722262, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [     21400791,     21029213,     20791376,     19451888,     18988399,     18632282,     17594506,     17094469,     16683216, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [     21476244,     21105843,     20869381,     19513438,     19052047,     18697812,     17644959,     17147580,     16738504, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [     23095548,     15548956, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [     23138407,     15589306, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [     23112318,     15559173, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [     23167202,     15606690, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [     23118319,     15564226, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [     23190757,     15624753, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [     18969980,     18970151,     27485880,     18970141,     18936508,     11289797, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [     19009837,     19009090,     27536088,     19009262,     18977105,     11319266, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [     18983272,     18983543,     27505790,     18983504,     18949712,     11297216, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [     19032598,     19032009,     27570272,     19032134,     18999671,     11331882, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [     18988342,     18988501,     27512018,     18988502,     18954905,     11301107, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [     19052336,     19051505,     27596458,     19051692,     19019639,     11345472, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [    191203469,    191203532,    191203532,    191203468,    191202925,    191202862, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [    191562501,    191562562,    191562562,    191562501,    191561967,    191561906, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [    191342617,    191342679,    191342679,    191342616,    191342072,    191342006, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [    191800627,    191800688,    191800688,    191800624,    191800089,    191800024, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [    191390451,    191390513,    191390513,    191390450,    191389908,    191389840, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [    191992439,    191992501,    191992501,    191992437,    191991906,    191991844, ],
  }),
  ("nof_tree_events",                 1736064),
  ("nof_db_events",                   19260000),
  ("fsize_local",                     7947438494), # 7.95GB, avg file size 397.37MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020May23_wPresel_nom_hh_bbww_ttbar/ntuples/TTToSemiLeptonic_widthx1p3"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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

