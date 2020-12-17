from collections import OrderedDict as OD

# file generated at 2020-12-17 02:32:50 with the following command:
# create_dictionary.py -m python/samples/metaDict_2018_hh.py -p python/samples/sampleLocations_2018_hh_bbww.txt -N samples_2018 -E 2018 -o python/samples -g hhAnalyzeSamples_2018_hh.py -M -q /hdfs/local/karl/count_final/2020Nov07/count_2018.root

samples_2018 = OD()
samples_2018["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_250_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_250_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99944000e+05, 3.99901719e+05, 3.99946438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99944000e+05, 3.99944000e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99918400e+06, 3.99918400e+06, 3.99918400e+06, 3.99918400e+06, 3.99918400e+06, 3.99918400e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00054438e+05, 4.00133906e+05, 5.67393062e+05, 3.99875562e+05, 3.99431562e+05, 2.50944062e+05, ],
    'CountWeightedFull'                                                              : [ 3.99877062e+05, 3.99834812e+05, 3.99879188e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99877062e+05, 3.99877062e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99851450e+06, 3.99851450e+06, 3.99851450e+06, 3.99851450e+06, 3.99851450e+06, 3.99851450e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99988688e+05, 4.00066750e+05, 5.67295750e+05, 3.99805312e+05, 3.99363000e+05, 2.50902188e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1360510492), # 1.36GB, avg file size 680.26MB
  ("fsize_db",                        21769417420), # 21.77GB, avg file size 1.28GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_250_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_260_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_260_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 399997, ],
    'CountWeighted'                                                                  : [ 3.99899750e+05, 3.99956875e+05, 3.99968969e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.06210938e+05, 3.99890312e+05, 3.91150062e+05, 4.06210938e+05, 3.99890312e+05, 3.91150062e+05, 4.06210938e+05, 3.99890312e+05, 3.91150062e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.06210938e+05, 3.91150062e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.66350825e+06, 2.60514600e+06, 3.40267200e+06, 2.66102050e+06, 2.34407125e+06, 1.67006575e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99954750e+05, 3.99794688e+05, 5.67791000e+05, 3.99942250e+05, 3.99959719e+05, 2.50778391e+05, ],
    'CountWeightedFull'                                                              : [ 3.99832719e+05, 3.99889156e+05, 3.99901219e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.06142188e+05, 3.99823375e+05, 3.91083875e+05, 4.06142188e+05, 3.99823375e+05, 3.91083875e+05, 4.06142188e+05, 3.99823375e+05, 3.91083875e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.06142188e+05, 3.91083875e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.66307075e+06, 2.60470975e+06, 3.40209275e+06, 2.66055500e+06, 2.34367425e+06, 1.66978712e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99888875e+05, 3.99727312e+05, 5.67694438e+05, 3.99872062e+05, 3.99892031e+05, 2.50736594e+05, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     1370578187), # 1.37GB, avg file size 685.29MB
  ("fsize_db",                        20956744775), # 20.96GB, avg file size 1.50GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_260_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_270_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_270_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 399998, ],
    'CountWeighted'                                                                  : [ 3.99927875e+05, 3.99951375e+05, 3.99969969e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.07473969e+05, 3.99927062e+05, 3.90119812e+05, 4.07473969e+05, 3.99927062e+05, 3.90119812e+05, 4.07473969e+05, 3.99927062e+05, 3.90119812e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.07473969e+05, 3.90119812e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.98437375e+06, 1.97710550e+06, 2.68116200e+06, 1.98309475e+06, 1.85211650e+06, 1.24151975e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00081156e+05, 3.99927250e+05, 5.68395625e+05, 3.99835594e+05, 3.99930188e+05, 2.50312969e+05, ],
    'CountWeightedFull'                                                              : [ 3.99857500e+05, 3.99881438e+05, 3.99900000e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.07402469e+05, 3.99856625e+05, 3.90051375e+05, 4.07402469e+05, 3.99856625e+05, 3.90051375e+05, 4.07402469e+05, 3.99856625e+05, 3.90051375e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.07402469e+05, 3.90051375e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.98404150e+06, 1.97675738e+06, 2.68069150e+06, 1.98274188e+06, 1.85179625e+06, 1.24130850e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 4.00014188e+05, 3.99856812e+05, 5.68296438e+05, 3.99764375e+05, 3.99861469e+05, 2.50270375e+05, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     1389494845), # 1.39GB, avg file size 694.75MB
  ("fsize_db",                        21109891474), # 21.11GB, avg file size 1.24GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_270_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_280_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_280_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99976125e+05, 3.99945812e+05, 3.99947500e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99976125e+05, 3.99976125e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.70069988e+06, 1.69761950e+06, 2.33382500e+06, 1.69975200e+06, 1.61932475e+06, 1.06392838e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00079438e+05, 3.99817250e+05, 5.68359875e+05, 3.99858562e+05, 3.99816125e+05, 2.50283594e+05, ],
    'CountWeightedFull'                                                              : [ 3.99905656e+05, 3.99876000e+05, 3.99877094e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99905656e+05, 3.99905656e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.70041325e+06, 1.69732338e+06, 2.33340550e+06, 1.69944738e+06, 1.61903362e+06, 1.06374650e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 4.00012125e+05, 3.99747844e+05, 5.68256375e+05, 3.99786875e+05, 3.99742812e+05, 2.50240766e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1421462586), # 1.42GB, avg file size 710.73MB
  ("fsize_db",                        21992399506), # 21.99GB, avg file size 1.37GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_280_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_300_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_300_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99966688e+05, 2.99941250e+05, 2.99957594e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.08218438e+05, 2.99966688e+05, 2.90509469e+05, 3.08218438e+05, 2.99966688e+05, 2.90509469e+05, 3.08218438e+05, 2.99966688e+05, 2.90509469e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.08218438e+05, 2.90509469e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.07872712e+06, 1.07861925e+06, 1.49812538e+06, 1.07919700e+06, 1.04202412e+06, 6.74055375e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99912875e+05, 2.99974844e+05, 4.25869844e+05, 3.00048469e+05, 2.98972969e+05, 1.87407312e+05, ],
    'CountWeightedFull'                                                              : [ 2.99914906e+05, 2.99890125e+05, 2.99906312e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.08165656e+05, 2.99914906e+05, 2.90459781e+05, 3.08165656e+05, 2.99914906e+05, 2.90459781e+05, 3.08165656e+05, 2.99914906e+05, 2.90459781e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.08165656e+05, 2.90459781e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.07854600e+06, 1.07843700e+06, 1.49786688e+06, 1.07900700e+06, 1.04184288e+06, 6.73940562e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99862781e+05, 2.99923969e+05, 4.25796344e+05, 2.99995531e+05, 2.98920875e+05, 1.87375281e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1088025519), # 1.09GB, avg file size 544.01MB
  ("fsize_db",                        16130523073), # 16.13GB, avg file size 1.01GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_300_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_320_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_320_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99943438e+05, 2.99984125e+05, 2.99943281e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.09783438e+05, 2.99943438e+05, 2.89265562e+05, 3.09783438e+05, 2.99943438e+05, 2.89265562e+05, 3.09783438e+05, 2.99943438e+05, 2.89265562e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.09783438e+05, 2.89265562e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.86300688e+05, 9.85538562e+05, 1.37879475e+06, 9.86441688e+05, 9.60543438e+05, 6.14449375e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99939656e+05, 2.99762875e+05, 4.27292250e+05, 2.99981438e+05, 3.00045281e+05, 1.86857781e+05, ],
    'CountWeightedFull'                                                              : [ 2.99888375e+05, 2.99928000e+05, 2.99887750e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.09726250e+05, 2.99888375e+05, 2.89212250e+05, 3.09726250e+05, 2.99888375e+05, 2.89212250e+05, 3.09726250e+05, 2.99888375e+05, 2.89212250e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.09726250e+05, 2.89212250e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.86123938e+05, 9.85357438e+05, 1.37853650e+06, 9.86253625e+05, 9.60364500e+05, 6.14337750e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99886062e+05, 2.99707688e+05, 4.27211812e+05, 2.99924188e+05, 2.99989125e+05, 1.86823953e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1117029729), # 1.12GB, avg file size 558.51MB
  ("fsize_db",                        16290185653), # 16.29GB, avg file size 1.25GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_320_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_350_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_350_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 299999, ],
    'CountWeighted'                                                                  : [ 2.99972938e+05, 2.99932062e+05, 2.99912250e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.11935562e+05, 2.99972938e+05, 2.87585125e+05, 3.11935562e+05, 2.99972938e+05, 2.87585125e+05, 3.11935562e+05, 2.99972938e+05, 2.87585125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.11935562e+05, 2.87585125e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.14401800e+06, 1.14295975e+06, 1.58534338e+06, 1.14481562e+06, 1.09909825e+06, 7.11554062e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99834438e+05, 2.99731562e+05, 4.27122125e+05, 3.00043750e+05, 2.99510656e+05, 1.86490234e+05, ],
    'CountWeightedFull'                                                              : [ 2.99916469e+05, 2.99876844e+05, 2.99856750e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.11877750e+05, 2.99916469e+05, 2.87531938e+05, 3.11877750e+05, 2.99916469e+05, 2.87531938e+05, 3.11877750e+05, 2.99916469e+05, 2.87531938e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.11877750e+05, 2.87531938e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.14381688e+06, 1.14274888e+06, 1.58505050e+06, 1.14459962e+06, 1.09889650e+06, 7.11425500e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99781656e+05, 2.99676219e+05, 4.27044062e+05, 2.99987188e+05, 2.99456250e+05, 1.86456562e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1153225731), # 1.15GB, avg file size 576.61MB
  ("fsize_db",                        16256170207), # 16.26GB, avg file size 1.35GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_350_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_400_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_400_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99957625e+05, 2.99960688e+05, 2.99932750e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.15107688e+05, 2.99950500e+05, 2.85246625e+05, 3.15107688e+05, 2.99950500e+05, 2.85246625e+05, 3.15107688e+05, 2.99950500e+05, 2.85246625e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.15107688e+05, 2.85246625e+05, ],
    'CountWeightedPSWeight'                                                          : [ 6.48843000e+05, 6.49805875e+05, 9.20667250e+05, 6.48971438e+05, 6.40555750e+05, 4.01255688e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99955812e+05, 3.00409000e+05, 4.28267000e+05, 3.00017906e+05, 2.98763125e+05, 1.85496906e+05, ],
    'CountWeightedFull'                                                              : [ 2.99901906e+05, 2.99904969e+05, 2.99878375e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.15049719e+05, 2.99894875e+05, 2.85193875e+05, 3.15049719e+05, 2.99894875e+05, 2.85193875e+05, 3.15049719e+05, 2.99894875e+05, 2.85193875e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.15049719e+05, 2.85193875e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 6.48728125e+05, 6.49686812e+05, 9.20495562e+05, 6.48848875e+05, 6.40436625e+05, 4.01183750e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99902625e+05, 3.00353906e+05, 4.28187000e+05, 2.99961156e+05, 2.98707500e+05, 1.85463625e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1210147269), # 1.21GB, avg file size 605.07MB
  ("fsize_db",                        17394059503), # 17.39GB, avg file size 1.16GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_400_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_500_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_500_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99936250e+05, 2.99952062e+05, 2.99944594e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.20040125e+05, 2.99936250e+05, 2.81437688e+05, 3.20040125e+05, 2.99936250e+05, 2.81437688e+05, 3.20040125e+05, 2.99936250e+05, 2.81437688e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.20040125e+05, 2.81437688e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.44888562e+05, 8.44404438e+05, 1.19528150e+06, 8.44965000e+05, 8.28049312e+05, 5.18719281e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99969500e+05, 2.99816438e+05, 4.30310000e+05, 2.99996812e+05, 2.99913062e+05, 1.84168969e+05, ],
    'CountWeightedFull'                                                              : [ 2.99880531e+05, 2.99895500e+05, 2.99887938e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.19980125e+05, 2.99880531e+05, 2.81385094e+05, 3.19980125e+05, 2.99880531e+05, 2.81385094e+05, 3.19980125e+05, 2.99880531e+05, 2.81385094e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.19980125e+05, 2.81385094e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 8.44735125e+05, 8.44245500e+05, 1.19505500e+06, 8.44800750e+05, 8.27895375e+05, 5.18623719e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99915000e+05, 2.99760125e+05, 4.30228344e+05, 2.99938562e+05, 2.99857031e+05, 1.84134938e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1298392334), # 1.30GB, avg file size 649.20MB
  ("fsize_db",                        17471951247), # 17.47GB, avg file size 1.34GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_500_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_550_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_550_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99920438e+05, 2.99943031e+05, 2.99915844e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.22058219e+05, 2.99917938e+05, 2.79866281e+05, 3.22058219e+05, 2.99917938e+05, 2.79866281e+05, 3.22058219e+05, 2.99917938e+05, 2.79866281e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.22058219e+05, 2.79866281e+05, ],
    'CountWeightedPSWeight'                                                          : [ 6.38353688e+05, 6.38804125e+05, 9.12250312e+05, 6.38733750e+05, 6.32558625e+05, 3.90576812e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99909625e+05, 3.00122219e+05, 4.31303188e+05, 3.00083938e+05, 2.99896312e+05, 1.83499578e+05, ],
    'CountWeightedFull'                                                              : [ 2.99861844e+05, 2.99884125e+05, 2.99857594e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.21994594e+05, 2.99859375e+05, 2.79811406e+05, 3.21994594e+05, 2.99859375e+05, 2.79811406e+05, 3.21994594e+05, 2.99859375e+05, 2.79811406e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.21994594e+05, 2.79811406e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 6.38231625e+05, 6.38680250e+05, 9.12068625e+05, 6.38604062e+05, 6.32432125e+05, 3.90500750e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99852406e+05, 3.00063844e+05, 4.31217188e+05, 3.00023000e+05, 2.99836344e+05, 1.83463891e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1334937127), # 1.33GB, avg file size 667.47MB
  ("fsize_db",                        18211430509), # 18.21GB, avg file size 2.28GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_550_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_600_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_600_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99946062e+05, 1.99967453e+05, 1.99986422e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.15934125e+05, 1.99945906e+05, 1.85641000e+05, 2.15934125e+05, 1.99945906e+05, 1.85641000e+05, 2.15934125e+05, 1.99945906e+05, 1.85641000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.15934125e+05, 1.85641000e+05, ],
    'CountWeightedPSWeight'                                                          : [ 4.30831062e+05, 4.30606312e+05, 6.15025438e+05, 4.30653844e+05, 4.25869375e+05, 2.62950781e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.00023531e+05, 1.99918922e+05, 2.87538938e+05, 1.99942406e+05, 1.99723812e+05, 1.22084008e+05, ],
    'CountWeightedFull'                                                              : [ 1.99908312e+05, 1.99928906e+05, 1.99947062e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.15892938e+05, 1.99908156e+05, 1.85605609e+05, 2.15892938e+05, 1.99908156e+05, 1.85605609e+05, 2.15892938e+05, 1.99908156e+05, 1.85605609e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.15892938e+05, 1.85605609e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 4.30750969e+05, 4.30523812e+05, 6.14906500e+05, 4.30568312e+05, 4.25787594e+05, 2.62900844e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99986109e+05, 1.99880578e+05, 2.87483500e+05, 1.99902766e+05, 1.99685297e+05, 1.22060836e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     909864852), # 909.86MB, avg file size 909.86MB
  ("fsize_db",                        12311761166), # 12.31GB, avg file size 1.76GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_600_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_650_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_650_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 199999, ],
    'CountWeighted'                                                                  : [ 1.99931844e+05, 1.99945875e+05, 1.99908000e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.17002906e+05, 1.99927125e+05, 1.84777750e+05, 2.17002906e+05, 1.99927125e+05, 1.84777750e+05, 2.17002906e+05, 1.99927125e+05, 1.84777750e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.17003344e+05, 1.84777281e+05, ],
    'CountWeightedPSWeight'                                                          : [ 4.39739594e+05, 4.39395062e+05, 6.29531125e+05, 4.39483625e+05, 4.35735031e+05, 2.67490219e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99984500e+05, 1.99838500e+05, 2.88552000e+05, 1.99871266e+05, 2.00403891e+05, 1.21645797e+05, ],
    'CountWeightedFull'                                                              : [ 1.99889078e+05, 1.99903125e+05, 1.99865922e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.16956766e+05, 1.99884438e+05, 1.84738297e+05, 2.16956766e+05, 1.99884438e+05, 1.84738297e+05, 2.16956766e+05, 1.99884438e+05, 1.84738297e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.16957219e+05, 1.84737828e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 4.39651656e+05, 4.39302656e+05, 6.29397500e+05, 4.39390625e+05, 4.35642938e+05, 2.67435625e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99944438e+05, 1.99796500e+05, 2.88490719e+05, 1.99828797e+05, 2.00361547e+05, 1.21620961e+05, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     926364486), # 926.36MB, avg file size 463.18MB
  ("fsize_db",                        12454041911), # 12.45GB, avg file size 1.04GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_650_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_700_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_700_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99949328e+05, 1.99947219e+05, 1.99955062e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.18015000e+05, 1.99947516e+05, 1.84040578e+05, 2.18015000e+05, 1.99947516e+05, 1.84040578e+05, 2.18015000e+05, 1.99947516e+05, 1.84040578e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.18015094e+05, 1.84040484e+05, ],
    'CountWeightedPSWeight'                                                          : [ 4.51231438e+05, 4.50294469e+05, 6.45076750e+05, 4.50570031e+05, 4.46341375e+05, 2.74148031e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.00119000e+05, 1.99697125e+05, 2.88433812e+05, 1.99820469e+05, 2.00309266e+05, 1.21591375e+05, ],
    'CountWeightedFull'                                                              : [ 1.99907891e+05, 1.99905750e+05, 1.99913734e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.17969953e+05, 1.99906078e+05, 1.84002656e+05, 2.17969953e+05, 1.99906078e+05, 1.84002656e+05, 2.17969953e+05, 1.99906078e+05, 1.84002656e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.17970016e+05, 1.84002562e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 4.51143281e+05, 4.50199750e+05, 6.44941438e+05, 4.50475281e+05, 4.46250312e+05, 2.74093219e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.00079906e+05, 1.99655250e+05, 2.88372906e+05, 1.99778578e+05, 2.00267906e+05, 1.21567062e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     937980492), # 937.98MB, avg file size 468.99MB
  ("fsize_db",                        12555546335), # 12.56GB, avg file size 965.81MB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_700_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_750_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_750_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 199999, ],
    'CountWeighted'                                                                  : [ 1.99962734e+05, 1.99959391e+05, 1.99972062e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99962734e+05, 1.99962734e+05, ],
    'CountWeightedPSWeight'                                                          : [ 4.64202094e+05, 4.63992938e+05, 6.63881250e+05, 4.64393625e+05, 4.58031094e+05, 2.81488375e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99936172e+05, 1.99852719e+05, 2.88441469e+05, 2.00018609e+05, 1.99776281e+05, 1.21241789e+05, ],
    'CountWeightedFull'                                                              : [ 1.99921125e+05, 1.99917266e+05, 1.99930453e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99921125e+05, 1.99921125e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 4.64110406e+05, 4.63896688e+05, 6.63743562e+05, 4.64295719e+05, 4.57936469e+05, 2.81431156e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99896609e+05, 1.99811281e+05, 2.88381781e+05, 1.99976359e+05, 1.99735031e+05, 1.21217172e+05, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     955487639), # 955.49MB, avg file size 477.74MB
  ("fsize_db",                        13006707251), # 13.01GB, avg file size 929.05MB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_750_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_800_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_800_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 199998, ],
    'CountWeighted'                                                                  : [ 1.99958281e+05, 1.99938594e+05, 1.99950391e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99958281e+05, 1.99958281e+05, ],
    'CountWeightedPSWeight'                                                          : [ 4.79319812e+05, 4.79356938e+05, 6.84310562e+05, 4.79288125e+05, 4.70850938e+05, 2.90178000e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99999688e+05, 2.00023016e+05, 2.88293688e+05, 1.99986266e+05, 1.99214328e+05, 1.21075133e+05, ],
    'CountWeightedFull'                                                              : [ 1.99913969e+05, 1.99894547e+05, 1.99906516e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99913969e+05, 1.99913969e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 4.79220594e+05, 4.79253156e+05, 6.84160688e+05, 4.79181562e+05, 4.70746844e+05, 2.90116375e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99958219e+05, 1.99979688e+05, 2.88230312e+05, 1.99941984e+05, 1.99170172e+05, 1.21049469e+05, ],
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     962674473), # 962.67MB, avg file size 481.34MB
  ("fsize_db",                        13089476147), # 13.09GB, avg file size 934.96MB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_800_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_850_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_850_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 199997, ],
    'CountWeighted'                                                                  : [ 1.99935156e+05, 1.99942781e+05, 1.99919203e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99935156e+05, 1.99935156e+05, ],
    'CountWeightedPSWeight'                                                          : [ 4.96242031e+05, 4.95395500e+05, 7.08955438e+05, 4.96130844e+05, 4.88407125e+05, 2.99884750e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99967484e+05, 1.99634688e+05, 2.88522062e+05, 1.99920828e+05, 1.99641844e+05, 1.20846789e+05, ],
    'CountWeightedFull'                                                              : [ 1.99891281e+05, 1.99898797e+05, 1.99875312e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99891281e+05, 1.99891281e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 4.96141000e+05, 4.95287094e+05, 7.08801812e+05, 4.96022344e+05, 4.88301812e+05, 2.99822219e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99926781e+05, 1.99591062e+05, 2.88459438e+05, 1.99877031e+05, 1.99598828e+05, 1.20821758e+05, ],
  }),
  ("nof_tree_events",                 199997),
  ("nof_db_events",                   199997),
  ("fsize_local",                     967947522), # 967.95MB, avg file size 967.95MB
  ("fsize_db",                        13167424036), # 13.17GB, avg file size 1.01GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_850_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_900_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_900_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 199999, ],
    'CountWeighted'                                                                  : [ 1.99973547e+05, 1.99954391e+05, 1.99955203e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.21322859e+05, 1.99973547e+05, 1.81639109e+05, 2.21322859e+05, 1.99973547e+05, 1.81639109e+05, 2.21322859e+05, 1.99973547e+05, 1.81639109e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.21323062e+05, 1.81638922e+05, ],
    'CountWeightedPSWeight'                                                          : [ 6.88895125e+05, 6.87733250e+05, 9.72151438e+05, 6.89055688e+05, 6.65058562e+05, 4.15440969e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99958031e+05, 1.99697672e+05, 2.89368094e+05, 2.00006031e+05, 2.00155703e+05, 1.20584305e+05, ],
    'CountWeightedFull'                                                              : [ 1.99928562e+05, 1.99909031e+05, 1.99910781e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.21273156e+05, 1.99928562e+05, 1.81598359e+05, 2.21273156e+05, 1.99928562e+05, 1.81598359e+05, 2.21273156e+05, 1.99928562e+05, 1.81598359e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.21273344e+05, 1.81598188e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 6.88749125e+05, 6.87581062e+05, 9.71932250e+05, 6.88898250e+05, 6.64907562e+05, 4.15351031e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99915672e+05, 1.99653438e+05, 2.89302344e+05, 1.99960281e+05, 2.00109703e+05, 1.20558148e+05, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     969877658), # 969.88MB, avg file size 484.94MB
  ("fsize_db",                        12520224790), # 12.52GB, avg file size 1.04GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_900_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1000_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_1000_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 9.99407188e+04, 9.99508750e+04, 9.99314688e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.11293977e+05, 9.99407188e+04, 9.02996562e+04, 1.11293977e+05, 9.99407188e+04, 9.02996562e+04, 1.11293977e+05, 9.99407188e+04, 9.02996562e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.11293977e+05, 9.02996562e+04, ],
    'CountWeightedPSWeight'                                                          : [ 3.72879688e+05, 3.72333812e+05, 5.23507125e+05, 3.73115000e+05, 3.56295875e+05, 2.24363844e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99260391e+04, 9.98574062e+04, 1.44713641e+05, 9.99863125e+04, 9.98268125e+04, 6.01255078e+04, ],
    'CountWeightedFull'                                                              : [ 9.99164219e+04, 9.99257812e+04, 9.99075391e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.11266969e+05, 9.99164219e+04, 9.02776953e+04, 1.11266969e+05, 9.99164219e+04, 9.02776953e+04, 1.11266969e+05, 9.99164219e+04, 9.02776953e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.11266969e+05, 9.02776953e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.72801375e+05, 3.72240938e+05, 5.23379750e+05, 3.73030125e+05, 3.56213000e+05, 2.24315125e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99050547e+04, 9.98325000e+04, 1.44678547e+05, 9.99636250e+04, 9.98035391e+04, 6.01124375e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     490957947), # 490.96MB, avg file size 490.96MB
  ("fsize_db",                        6339783437), # 6.34GB, avg file size 704.42MB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_1000_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1250_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_1250_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99413125e+04, 9.99521094e+04, 9.99466875e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99413125e+04, 9.99413125e+04, ],
    'CountWeightedPSWeight'                                                          : [ 5.84966875e+05, 5.77110000e+05, 7.77480500e+05, 5.85215312e+05, 5.18991312e+05, 3.48569250e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99521562e+04, 1.00146797e+05, 1.45731188e+05, 1.00000859e+05, 1.00021547e+05, 5.95604258e+04, ],
    'CountWeightedFull'                                                              : [ 9.99180781e+04, 9.99286719e+04, 9.99235859e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99180781e+04, 9.99180781e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 5.84836000e+05, 5.76978125e+05, 7.77298000e+05, 5.85072312e+05, 5.18867500e+05, 3.48488969e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99297031e+04, 1.00123812e+05, 1.45696375e+05, 9.99763125e+04, 9.99971094e+04, 5.95466641e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     503196327), # 503.20MB, avg file size 503.20MB
  ("fsize_db",                        6214334271), # 6.21GB, avg file size 1.04GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_1250_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1500_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_1500_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99488516e+04, 9.99521562e+04, 9.99445703e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.13888328e+05, 9.99482344e+04, 8.85137500e+04, 1.13888328e+05, 9.99482344e+04, 8.85137500e+04, 1.13888328e+05, 9.99482344e+04, 8.85137500e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.13888742e+05, 8.85133359e+04, ],
    'CountWeightedPSWeight'                                                          : [ 6.03263188e+05, 5.92226562e+05, 7.96973875e+05, 6.03341688e+05, 5.31338125e+05, 3.58266562e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99704844e+04, 9.99361719e+04, 1.45730359e+05, 1.00000703e+05, 9.99037422e+04, 5.93737578e+04, ],
    'CountWeightedFull'                                                              : [ 9.99221797e+04, 9.99253516e+04, 9.99182656e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.13857969e+05, 9.99215547e+04, 8.84901094e+04, 1.13857969e+05, 9.99215547e+04, 8.84901094e+04, 1.13857969e+05, 9.99215547e+04, 8.84901094e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.13858383e+05, 8.84897031e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 6.03120000e+05, 5.92068750e+05, 7.96761188e+05, 6.03186000e+05, 5.31197312e+05, 3.58179125e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99467188e+04, 9.99095781e+04, 1.45691656e+05, 9.99748750e+04, 9.98774297e+04, 5.93592500e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     502454534), # 502.45MB, avg file size 251.23MB
  ("fsize_db",                        6217807927), # 6.22GB, avg file size 777.23MB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_1500_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1750_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_1750_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99183125e+04, 9.99153438e+04, 9.99156094e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99183125e+04, 9.99183125e+04, ],
    'CountWeightedPSWeight'                                                          : [ 7.89202688e+05, 7.38202562e+05, 9.48251125e+05, 7.85840312e+05, 6.40658375e+05, 4.67933625e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99492891e+04, 9.99396562e+04, 1.45492188e+05, 1.00004062e+05, 9.93908516e+04, 5.91293125e+04, ],
    'CountWeightedFull'                                                              : [ 9.98916797e+04, 9.98883594e+04, 9.98895234e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.98916797e+04, 9.98916797e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 7.89009375e+05, 7.38008250e+05, 9.47999500e+05, 7.85633500e+05, 6.40487875e+05, 4.67816438e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99249141e+04, 9.99130938e+04, 1.45452938e+05, 9.99777500e+04, 9.93640625e+04, 5.91144766e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     506845227), # 506.85MB, avg file size 506.85MB
  ("fsize_db",                        6399858338), # 6.40GB, avg file size 711.10MB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_1750_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_2000_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_2000_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 99998, ],
    'CountWeighted'                                                                  : [ 9.99250469e+04, 9.99268125e+04, 9.99234219e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.15690195e+05, 9.99250469e+04, 8.72084453e+04, 1.15690195e+05, 9.99250469e+04, 8.72084453e+04, 1.15690195e+05, 9.99250469e+04, 8.72084453e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.15692641e+05, 8.72060000e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.66006562e+05, 8.66210562e+05, 9.99314000e+05, 9.52066500e+05, 7.52158250e+05, 6.19948562e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00021766e+05, 9.99660234e+04, 1.46550672e+05, 9.99350938e+04, 1.00132336e+05, 5.88673008e+04, ],
    'CountWeightedFull'                                                              : [ 9.98967344e+04, 9.98985625e+04, 9.98952969e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.15657375e+05, 9.98967344e+04, 8.71838438e+04, 1.15657375e+05, 9.98967344e+04, 8.71838438e+04, 1.15657375e+05, 9.98967344e+04, 8.71838438e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.15659820e+05, 8.71814062e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.65757000e+05, 8.65968500e+05, 9.99031750e+05, 9.51813125e+05, 7.51943125e+05, 6.19785750e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99964688e+04, 9.99381719e+04, 1.46508859e+05, 9.99078281e+04, 1.00103016e+05, 5.88518711e+04, ],
  }),
  ("nof_tree_events",                 99998),
  ("nof_db_events",                   99998),
  ("fsize_local",                     505389015), # 505.39MB, avg file size 505.39MB
  ("fsize_db",                        6250048572), # 6.25GB, avg file size 781.26MB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_2000_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_2500_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_2500_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.98775781e+04, 9.98723906e+04, 9.98809453e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.98775781e+04, 9.98775781e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.98728375e+05, 9.82378250e+05, 9.98734125e+05, 9.98718812e+05, 9.22712688e+05, 9.06342375e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99665625e+04, 9.98564375e+04, 1.46542562e+05, 1.00008680e+05, 1.00072562e+05, 5.87847383e+04, ],
    'CountWeightedFull'                                                              : [ 9.98475000e+04, 9.98425859e+04, 9.98506719e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.98475000e+04, 9.98475000e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.98428750e+05, 9.82081250e+05, 9.98431438e+05, 9.98423500e+05, 9.22432625e+05, 9.06074875e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99384531e+04, 9.98266562e+04, 1.46498406e+05, 9.99784844e+04, 1.00041859e+05, 5.87675312e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     513447840), # 513.45MB, avg file size 513.45MB
  ("fsize_db",                        6648889879), # 6.65GB, avg file size 554.07MB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_2500_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_3000_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_3000_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.97513203e+04, 9.97542109e+04, 9.97446484e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.97513203e+04, 9.97513203e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.96460875e+05, 9.92294375e+05, 9.97439062e+05, 9.96325938e+05, 9.65275250e+05, 9.60368250e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99962578e+04, 1.00102289e+05, 1.46391391e+05, 9.99936016e+04, 9.95480156e+04, 5.86894531e+04, ],
    'CountWeightedFull'                                                              : [ 9.97194297e+04, 9.97223672e+04, 9.97127188e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.97194297e+04, 9.97194297e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.96151188e+05, 9.91976625e+05, 9.97120062e+05, 9.96016625e+05, 9.64969875e+05, 9.60071000e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99670781e+04, 1.00069617e+05, 1.46343750e+05, 9.99619844e+04, 9.95165000e+04, 5.86715898e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     517803460), # 517.80MB, avg file size 258.90MB
  ("fsize_db",                        6767988851), # 6.77GB, avg file size 676.80MB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_3000_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_250_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_250_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 399998, ],
    'CountWeighted'                                                                  : [ 3.99958875e+05, 3.99966312e+05, 3.99961375e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.04901500e+05, 3.99958000e+05, 3.92209062e+05, 4.04901500e+05, 3.99958000e+05, 3.92209062e+05, 4.04901500e+05, 3.99958000e+05, 3.92209062e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.04901500e+05, 3.92209062e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99960450e+06, 3.99960450e+06, 3.99960450e+06, 3.99960450e+06, 3.99960450e+06, 3.99960450e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00011312e+05, 4.00158156e+05, 5.67958625e+05, 3.99960812e+05, 3.99028688e+05, 2.50314141e+05, ],
    'CountWeightedFull'                                                              : [ 3.99889688e+05, 3.99897312e+05, 3.99892062e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.04831188e+05, 3.99888656e+05, 3.92140625e+05, 4.04831188e+05, 3.99888656e+05, 3.92140625e+05, 4.04831188e+05, 3.99888656e+05, 3.92140625e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.04831188e+05, 3.92140625e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99891100e+06, 3.99891100e+06, 3.99891100e+06, 3.99891100e+06, 3.99891100e+06, 3.99891100e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99943906e+05, 4.00088906e+05, 5.67858312e+05, 3.99889000e+05, 3.98958125e+05, 2.50271391e+05, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     1375725135), # 1.38GB, avg file size 687.86MB
  ("fsize_db",                        21099457960), # 21.10GB, avg file size 1.76GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_250_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_260_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_260_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99961250e+05, 3.99976562e+05, 3.99968812e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.06222750e+05, 3.99955062e+05, 3.91162188e+05, 4.06222750e+05, 3.99955062e+05, 3.91162188e+05, 4.06222750e+05, 3.99955062e+05, 3.91162188e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.06222750e+05, 3.91162188e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99981075e+06, 3.99981075e+06, 3.99981075e+06, 3.99981075e+06, 3.99981075e+06, 3.99981075e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99971781e+05, 4.00009500e+05, 5.69266375e+05, 4.00059656e+05, 3.99924688e+05, 2.49805359e+05, ],
    'CountWeightedFull'                                                              : [ 3.99893000e+05, 3.99907875e+05, 3.99899812e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.06153062e+05, 3.99886750e+05, 3.91095250e+05, 4.06153062e+05, 3.99886750e+05, 3.91095250e+05, 4.06153062e+05, 3.99886750e+05, 3.91095250e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.06153062e+05, 3.91095250e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99912550e+06, 3.99912550e+06, 3.99912550e+06, 3.99912550e+06, 3.99912550e+06, 3.99912550e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99905000e+05, 3.99940781e+05, 5.69167625e+05, 3.99989062e+05, 3.99856062e+05, 2.49763062e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1401626627), # 1.40GB, avg file size 700.81MB
  ("fsize_db",                        21222151277), # 21.22GB, avg file size 1.06GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_260_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_270_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_270_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99971750e+05, 3.99960000e+05, 3.99953844e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.07472750e+05, 3.99971750e+05, 3.90124250e+05, 4.07472750e+05, 3.99971750e+05, 3.90124250e+05, 4.07472750e+05, 3.99971750e+05, 3.90124250e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.07472750e+05, 3.90124250e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99989900e+06, 3.99989900e+06, 3.99989900e+06, 3.99989900e+06, 3.99989900e+06, 3.99989900e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00093094e+05, 4.00542500e+05, 5.68943250e+05, 3.99869812e+05, 3.98850062e+05, 2.49502078e+05, ],
    'CountWeightedFull'                                                              : [ 3.99900688e+05, 3.99889875e+05, 3.99882500e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.07400750e+05, 3.99900688e+05, 3.90055469e+05, 4.07400750e+05, 3.99900688e+05, 3.90055469e+05, 4.07400750e+05, 3.99900688e+05, 3.90055469e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.07400750e+05, 3.90055469e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99918400e+06, 3.99918400e+06, 3.99918400e+06, 3.99918400e+06, 3.99918400e+06, 3.99918400e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 4.00024438e+05, 4.00472469e+05, 5.68841375e+05, 3.99796875e+05, 3.98778562e+05, 2.49458656e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1424053928), # 1.42GB, avg file size 712.03MB
  ("fsize_db",                        21635602520), # 21.64GB, avg file size 1.27GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_270_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_280_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_280_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 399998, ],
    'CountWeighted'                                                                  : [ 3.99933656e+05, 3.99989000e+05, 3.99972312e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.08688906e+05, 3.99929219e+05, 3.89154938e+05, 4.08688906e+05, 3.99929219e+05, 3.89154938e+05, 4.08688906e+05, 3.99929219e+05, 3.89154938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.08688906e+05, 3.89154938e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99935000e+06, 3.99936000e+06, 3.99936000e+06, 3.99935000e+06, 3.99936000e+06, 3.99935000e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99940000e+05, 3.99749094e+05, 5.68610375e+05, 4.00021250e+05, 3.99200812e+05, 2.49549375e+05, ],
    'CountWeightedFull'                                                              : [ 3.99860312e+05, 3.99915281e+05, 3.99898094e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.08613625e+05, 3.99855875e+05, 3.89083312e+05, 4.08613625e+05, 3.99855875e+05, 3.89083312e+05, 4.08613625e+05, 3.99855875e+05, 3.89083312e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.08613625e+05, 3.89083312e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99862300e+06, 3.99862300e+06, 3.99862300e+06, 3.99862300e+06, 3.99862300e+06, 3.99862300e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99869688e+05, 3.99676000e+05, 5.68505625e+05, 3.99946125e+05, 3.99127438e+05, 2.49504594e+05, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     1448372541), # 1.45GB, avg file size 724.19MB
  ("fsize_db",                        21492020096), # 21.49GB, avg file size 1.79GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_280_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_300_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_300_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 299999, ],
    'CountWeighted'                                                                  : [ 2.99994594e+05, 3.00011719e+05, 2.99982562e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.08261469e+05, 2.99994594e+05, 2.90533250e+05, 3.08261469e+05, 2.99994594e+05, 2.90533250e+05, 3.08261469e+05, 2.99994594e+05, 2.90533250e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.08261469e+05, 2.90533250e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99976250e+06, 2.99976250e+06, 2.99976250e+06, 2.99976250e+06, 2.99976250e+06, 2.99976250e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.00079312e+05, 3.00055469e+05, 4.27338250e+05, 2.99878156e+05, 2.99645312e+05, 1.86751625e+05, ],
    'CountWeightedFull'                                                              : [ 2.99941938e+05, 2.99958062e+05, 2.99930406e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.08207125e+05, 2.99941938e+05, 2.90482000e+05, 3.08207125e+05, 2.99941938e+05, 2.90482000e+05, 3.08207125e+05, 2.99941938e+05, 2.90482000e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.08207125e+05, 2.90482000e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99923450e+06, 2.99923450e+06, 2.99923450e+06, 2.99923450e+06, 2.99923450e+06, 2.99923450e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.00027781e+05, 3.00002719e+05, 4.27262375e+05, 2.99823344e+05, 2.99592469e+05, 1.86719094e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1121271938), # 1.12GB, avg file size 560.64MB
  ("fsize_db",                        16166482441), # 16.17GB, avg file size 1.15GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_300_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_320_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_320_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 299998, ],
    'CountWeighted'                                                                  : [ 2.99975875e+05, 2.99997375e+05, 2.99968250e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.09821031e+05, 2.99975875e+05, 2.89287812e+05, 3.09821031e+05, 2.99975875e+05, 2.89287812e+05, 3.09821031e+05, 2.99975875e+05, 2.89287812e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.09821031e+05, 2.89287812e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99973450e+06, 2.99973450e+06, 2.99973450e+06, 2.99973450e+06, 2.99973450e+06, 2.99973450e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.00022375e+05, 2.99848031e+05, 4.27649750e+05, 2.99960812e+05, 2.99798844e+05, 1.86490547e+05, ],
    'CountWeightedFull'                                                              : [ 2.99922156e+05, 2.99942875e+05, 2.99915125e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.09765438e+05, 2.99922156e+05, 2.89235750e+05, 3.09765438e+05, 2.99922156e+05, 2.89235750e+05, 3.09765438e+05, 2.99922156e+05, 2.89235750e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.09765438e+05, 2.89235750e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99919425e+06, 2.99919425e+06, 2.99919425e+06, 2.99919425e+06, 2.99919425e+06, 2.99919425e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99969750e+05, 2.99794562e+05, 4.27572469e+05, 2.99905250e+05, 2.99744438e+05, 1.86457328e+05, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1152329929), # 1.15GB, avg file size 576.16MB
  ("fsize_db",                        16707306428), # 16.71GB, avg file size 1.39GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_320_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_350_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_350_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99879375e+05, 2.99927688e+05, 2.99908562e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.11915344e+05, 2.99879375e+05, 2.87578688e+05, 3.11915344e+05, 2.99879375e+05, 2.87578688e+05, 3.11915344e+05, 2.99879375e+05, 2.87578688e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.11915344e+05, 2.87578688e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99918050e+06, 2.99918050e+06, 2.99918050e+06, 2.99918050e+06, 2.99918050e+06, 2.99918050e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.00010281e+05, 2.99867438e+05, 4.28501562e+05, 2.99867125e+05, 2.99824406e+05, 1.85646516e+05, ],
    'CountWeightedFull'                                                              : [ 2.99824969e+05, 2.99873125e+05, 2.99853562e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.11858438e+05, 2.99824969e+05, 2.87526000e+05, 3.11858438e+05, 2.99824969e+05, 2.87526000e+05, 3.11858438e+05, 2.99824969e+05, 2.87526000e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.11858438e+05, 2.87526000e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99863375e+06, 2.99863375e+06, 2.99863375e+06, 2.99863375e+06, 2.99863375e+06, 2.99863375e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99957625e+05, 2.99813438e+05, 4.28419688e+05, 2.99811156e+05, 2.99766219e+05, 1.85613359e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1194849422), # 1.19GB, avg file size 597.42MB
  ("fsize_db",                        17008053450), # 17.01GB, avg file size 1.42GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_350_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_400_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_400_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99970812e+05, 2.99964500e+05, 2.99957562e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.15103812e+05, 2.99970812e+05, 2.85246656e+05, 3.15103812e+05, 2.99970812e+05, 2.85246656e+05, 3.15103812e+05, 2.99970812e+05, 2.85246656e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.15103844e+05, 2.85246562e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99924950e+06, 2.99924950e+06, 2.99924950e+06, 2.99924950e+06, 2.99924950e+06, 2.99924950e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99987812e+05, 2.99918844e+05, 4.29371688e+05, 2.99941281e+05, 2.99954156e+05, 1.85050203e+05, ],
    'CountWeightedFull'                                                              : [ 2.99914969e+05, 2.99908375e+05, 2.99900781e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.15045000e+05, 2.99914969e+05, 2.85193250e+05, 3.15045000e+05, 2.99914969e+05, 2.85193250e+05, 3.15045000e+05, 2.99914969e+05, 2.85193250e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.15045000e+05, 2.85193188e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99869750e+06, 2.99869750e+06, 2.99869750e+06, 2.99869750e+06, 2.99869750e+06, 2.99869750e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99933312e+05, 2.99863250e+05, 4.29290375e+05, 2.99883188e+05, 2.99897188e+05, 1.85016000e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1255144343), # 1.26GB, avg file size 627.57MB
  ("fsize_db",                        17452430860), # 17.45GB, avg file size 1.16GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_400_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_450_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_450_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99938844e+05, 2.99893625e+05, 2.99914812e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.17708906e+05, 2.99936688e+05, 2.83189562e+05, 3.17708906e+05, 2.99936688e+05, 2.83189562e+05, 3.17708906e+05, 2.99936688e+05, 2.83189562e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.17708906e+05, 2.83189562e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99870900e+06, 2.99872375e+06, 2.99872375e+06, 2.99870900e+06, 2.99872375e+06, 2.99870900e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99894312e+05, 2.99845750e+05, 4.29900781e+05, 3.00009281e+05, 2.99731094e+05, 1.84386766e+05, ],
    'CountWeightedFull'                                                              : [ 2.99878188e+05, 2.99834906e+05, 2.99855000e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.17645562e+05, 2.99876031e+05, 2.83133156e+05, 3.17645562e+05, 2.99876031e+05, 2.83133156e+05, 3.17645562e+05, 2.99876031e+05, 2.83133156e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.17645562e+05, 2.83133156e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99814175e+06, 2.99814175e+06, 2.99814175e+06, 2.99814175e+06, 2.99814175e+06, 2.99814175e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99838250e+05, 2.99785156e+05, 4.29813812e+05, 2.99949438e+05, 2.99671906e+05, 1.84351578e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1305366619), # 1.31GB, avg file size 652.68MB
  ("fsize_db",                        18286814735), # 18.29GB, avg file size 2.29GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_450_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_500_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_500_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 299999, ],
    'CountWeighted'                                                                  : [ 2.99949375e+05, 2.99983438e+05, 2.99957562e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.20056812e+05, 2.99949375e+05, 2.81465875e+05, 3.20056812e+05, 2.99949375e+05, 2.81465875e+05, 3.20056812e+05, 2.99949375e+05, 2.81465875e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.20056812e+05, 2.81465875e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99925025e+06, 2.99925725e+06, 2.99925725e+06, 2.99925025e+06, 2.99925725e+06, 2.99925025e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99889250e+05, 3.00285906e+05, 4.30421031e+05, 3.00097406e+05, 2.99098625e+05, 1.83807859e+05, ],
    'CountWeightedFull'                                                              : [ 2.99889062e+05, 2.99922344e+05, 2.99897125e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.19992500e+05, 2.99889062e+05, 2.81408750e+05, 3.19992500e+05, 2.99889062e+05, 2.81408750e+05, 3.19992500e+05, 2.99889062e+05, 2.81408750e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.19992500e+05, 2.81408750e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99866725e+06, 2.99866725e+06, 2.99866725e+06, 2.99866725e+06, 2.99866725e+06, 2.99866725e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99832031e+05, 3.00226031e+05, 4.30333594e+05, 3.00036031e+05, 2.99037250e+05, 1.83771969e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1350414375), # 1.35GB, avg file size 675.21MB
  ("fsize_db",                        18029238407), # 18.03GB, avg file size 1.80GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_500_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_550_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_550_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99932250e+05, 2.99936312e+05, 2.99920219e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.22048531e+05, 2.99932250e+05, 2.79890250e+05, 3.22048531e+05, 2.99932250e+05, 2.79890250e+05, 3.22048531e+05, 2.99932250e+05, 2.79890250e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.22048938e+05, 2.79889844e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99940150e+06, 2.99940150e+06, 2.99940150e+06, 2.99940150e+06, 2.99940150e+06, 2.99940150e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99907688e+05, 3.00079656e+05, 4.31138469e+05, 3.00014469e+05, 2.99295188e+05, 1.83221812e+05, ],
    'CountWeightedFull'                                                              : [ 2.99872906e+05, 2.99877281e+05, 2.99860625e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.21984469e+05, 2.99872906e+05, 2.79833969e+05, 3.21984469e+05, 2.99872906e+05, 2.79833969e+05, 3.21984469e+05, 2.99872906e+05, 2.79833969e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.21984844e+05, 2.79833562e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99880375e+06, 2.99880375e+06, 2.99880375e+06, 2.99880375e+06, 2.99880375e+06, 2.99880375e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99850156e+05, 3.00020375e+05, 4.31052188e+05, 2.99952562e+05, 2.99235344e+05, 1.83185688e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1388199462), # 1.39GB, avg file size 694.10MB
  ("fsize_db",                        17868443167), # 17.87GB, avg file size 1.62GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_550_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_600_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_600_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99945719e+05, 1.99972156e+05, 1.99968141e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.15927219e+05, 1.99945719e+05, 1.85645500e+05, 2.15927219e+05, 1.99945719e+05, 1.85645500e+05, 2.15927219e+05, 1.99945719e+05, 1.85645500e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.15928031e+05, 1.85644688e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99954062e+06, 1.99954062e+06, 1.99954062e+06, 1.99954062e+06, 1.99954062e+06, 1.99954062e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99948828e+05, 2.00164141e+05, 2.87634031e+05, 2.00048812e+05, 1.99307859e+05, 1.21826281e+05, ],
    'CountWeightedFull'                                                              : [ 1.99904031e+05, 1.99929703e+05, 1.99925484e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.15881859e+05, 1.99904031e+05, 1.85606281e+05, 2.15881859e+05, 1.99904031e+05, 1.85606281e+05, 2.15881859e+05, 1.99904031e+05, 1.85606281e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.15882672e+05, 1.85605469e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.99911938e+06, 1.99911938e+06, 1.99911938e+06, 1.99911938e+06, 1.99911938e+06, 1.99911938e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99909125e+05, 2.00121922e+05, 2.87573250e+05, 2.00006391e+05, 1.99265891e+05, 1.21801414e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     943635213), # 943.64MB, avg file size 471.82MB
  ("fsize_db",                        12265654789), # 12.27GB, avg file size 1.12GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_600_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_650_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_650_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99953906e+05, 1.99950953e+05, 1.99939703e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.17018953e+05, 1.99953359e+05, 1.84796016e+05, 2.17018953e+05, 1.99953359e+05, 1.84796016e+05, 2.17018953e+05, 1.99953359e+05, 1.84796016e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.17018953e+05, 1.84796016e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99955200e+06, 1.99956175e+06, 1.99956175e+06, 1.99955250e+06, 1.99956175e+06, 1.99955200e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99901250e+05, 1.99543625e+05, 2.88409438e+05, 2.00028156e+05, 2.00446797e+05, 1.21647742e+05, ],
    'CountWeightedFull'                                                              : [ 1.99910641e+05, 1.99907969e+05, 1.99896812e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.16972250e+05, 1.99910109e+05, 1.84756469e+05, 2.16972250e+05, 1.99910109e+05, 1.84756469e+05, 2.16972250e+05, 1.99910109e+05, 1.84756469e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.16972250e+05, 1.84756469e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.99913400e+06, 1.99913400e+06, 1.99913400e+06, 1.99913400e+06, 1.99913400e+06, 1.99913400e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99860688e+05, 1.99501703e+05, 2.88346812e+05, 1.99984781e+05, 2.00402953e+05, 1.21622500e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     956985702), # 956.99MB, avg file size 956.99MB
  ("fsize_db",                        12362249390), # 12.36GB, avg file size 1.77GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_650_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_700_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_700_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99954328e+05, 1.99970750e+05, 1.99971781e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.18034672e+05, 1.99954328e+05, 1.84066781e+05, 2.18034672e+05, 1.99954328e+05, 1.84066781e+05, 2.18034672e+05, 1.99954328e+05, 1.84066781e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.18034672e+05, 1.84066781e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99989100e+06, 1.99989100e+06, 1.99989100e+06, 1.99989100e+06, 1.99989100e+06, 1.99989100e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99984969e+05, 2.00025266e+05, 2.88571625e+05, 1.99996812e+05, 1.99778969e+05, 1.21301844e+05, ],
    'CountWeightedFull'                                                              : [ 1.99911594e+05, 1.99927656e+05, 1.99929422e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.17988109e+05, 1.99911594e+05, 1.84027422e+05, 2.17988109e+05, 1.99911594e+05, 1.84027422e+05, 2.17988109e+05, 1.99911594e+05, 1.84027422e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.17988109e+05, 1.84027422e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.99945725e+06, 1.99945725e+06, 1.99945725e+06, 1.99945725e+06, 1.99945725e+06, 1.99945725e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99945312e+05, 1.99982031e+05, 2.88509281e+05, 1.99954016e+05, 1.99737047e+05, 1.21277211e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     966475228), # 966.48MB, avg file size 966.48MB
  ("fsize_db",                        12213272084), # 12.21GB, avg file size 1.22GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_700_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_750_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_750_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 199999, ],
    'CountWeighted'                                                                  : [ 1.99989781e+05, 1.99952453e+05, 1.99969859e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.18937766e+05, 1.99986953e+05, 1.83373938e+05, 2.18937766e+05, 1.99986953e+05, 1.83373938e+05, 2.18937766e+05, 1.99986953e+05, 1.83373938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.18937828e+05, 1.83373891e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99960162e+06, 1.99960162e+06, 1.99960162e+06, 1.99960162e+06, 1.99960162e+06, 1.99960162e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.00060312e+05, 2.00510609e+05, 2.88398781e+05, 1.99933484e+05, 1.98639969e+05, 1.20928305e+05, ],
    'CountWeightedFull'                                                              : [ 1.99948281e+05, 1.99911781e+05, 1.99929062e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.18892906e+05, 1.99945469e+05, 1.83336125e+05, 2.18892906e+05, 1.99945469e+05, 1.83336125e+05, 2.18892906e+05, 1.99945469e+05, 1.83336125e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.18892969e+05, 1.83336094e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.99918975e+06, 1.99918975e+06, 1.99918975e+06, 1.99918975e+06, 1.99918975e+06, 1.99918975e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.00020516e+05, 2.00469469e+05, 2.88338875e+05, 1.99890578e+05, 1.98598938e+05, 1.20903578e+05, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     973912528), # 973.91MB, avg file size 973.91MB
  ("fsize_db",                        12949339827), # 12.95GB, avg file size 1.08GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_750_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_800_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_800_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 199999, ],
    'CountWeighted'                                                                  : [ 1.99938906e+05, 1.99959797e+05, 1.99969484e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.19788203e+05, 1.99938109e+05, 1.82741938e+05, 2.19788203e+05, 1.99938109e+05, 1.82741938e+05, 2.19788203e+05, 1.99938109e+05, 1.82741938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.19788203e+05, 1.82741938e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99957900e+06, 1.99958175e+06, 1.99958175e+06, 1.99957900e+06, 1.99958175e+06, 1.99957900e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.00040906e+05, 2.00056406e+05, 2.88755094e+05, 1.99871844e+05, 1.99354266e+05, 1.20812922e+05, ],
    'CountWeightedFull'                                                              : [ 1.99892016e+05, 1.99912297e+05, 1.99921812e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.19735797e+05, 1.99891219e+05, 1.82698766e+05, 2.19735797e+05, 1.99891219e+05, 1.82698766e+05, 2.19735797e+05, 1.99891219e+05, 1.82698766e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.19735797e+05, 1.82698766e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.99910812e+06, 1.99910812e+06, 1.99910812e+06, 1.99910812e+06, 1.99910812e+06, 1.99910812e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99997719e+05, 2.00009734e+05, 2.88685656e+05, 1.99825750e+05, 1.99305531e+05, 1.20786117e+05, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     978804178), # 978.80MB, avg file size 978.80MB
  ("fsize_db",                        12584995133), # 12.58GB, avg file size 1.57GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_800_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_850_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_850_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 197000, ],
    'CountWeighted'                                                                  : [ 1.96941750e+05, 1.96955656e+05, 1.96944078e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.96941750e+05, 1.96941750e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.96952200e+06, 1.96952200e+06, 1.96952200e+06, 1.96952200e+06, 1.96952200e+06, 1.96952200e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.97005000e+05, 1.96770000e+05, 2.85029625e+05, 1.96981109e+05, 1.96953688e+05, 1.18765336e+05, ],
    'CountWeightedFull'                                                              : [ 1.96899469e+05, 1.96913219e+05, 1.96901484e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.96899469e+05, 1.96899469e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.96909688e+06, 1.96909688e+06, 1.96909688e+06, 1.96909688e+06, 1.96909688e+06, 1.96909688e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.96964375e+05, 1.96727984e+05, 2.84968344e+05, 1.96937094e+05, 1.96911609e+05, 1.18740234e+05, ],
  }),
  ("nof_tree_events",                 197000),
  ("nof_db_events",                   197000),
  ("fsize_local",                     975775001), # 975.78MB, avg file size 975.78MB
  ("fsize_db",                        13202094182), # 13.20GB, avg file size 1.89GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_850_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_900_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_900_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 199999, ],
    'CountWeighted'                                                                  : [ 1.99956062e+05, 1.99944391e+05, 1.99951938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99956062e+05, 1.99956062e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99936075e+06, 1.99936075e+06, 1.99936075e+06, 1.99936075e+06, 1.99936075e+06, 1.99936075e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99896672e+05, 1.99761469e+05, 2.89789375e+05, 2.00120906e+05, 2.00150094e+05, 1.20421828e+05, ],
    'CountWeightedFull'                                                              : [ 1.99910453e+05, 1.99899219e+05, 1.99906531e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99910453e+05, 1.99910453e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.99891025e+06, 1.99891025e+06, 1.99891025e+06, 1.99891025e+06, 1.99891025e+06, 1.99891025e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99853672e+05, 1.99716172e+05, 2.89724531e+05, 2.00074531e+05, 2.00105406e+05, 1.20395078e+05, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     996288330), # 996.29MB, avg file size 498.14MB
  ("fsize_db",                        13510236979), # 13.51GB, avg file size 1.23GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_900_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1000_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_1000_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                                          : [ 90000, ],
    'CountWeighted'                                                                  : [ 8.99879375e+04, 8.99821875e+04, 8.99780000e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 8.99879375e+04, 8.99879375e+04, ],
    'CountWeightedPSWeight'                                                          : [ 8.99832000e+05, 8.99832000e+05, 8.99832000e+05, 8.99832000e+05, 8.99832000e+05, 8.99832000e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 8.99961719e+04, 8.98183594e+04, 1.30287711e+05, 8.99470938e+04, 8.98635312e+04, 5.40322031e+04, ],
    'CountWeightedFull'                                                              : [ 8.99674688e+04, 8.99617500e+04, 8.99578281e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 8.99674688e+04, 8.99674688e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 8.99626125e+05, 8.99626125e+05, 8.99626125e+05, 8.99626125e+05, 8.99626125e+05, 8.99626125e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 8.99772969e+04, 8.97987109e+04, 1.30258344e+05, 8.99268594e+04, 8.98423750e+04, 5.40204023e+04, ],
  }),
  ("nof_tree_events",                 90000),
  ("nof_db_events",                   90000),
  ("fsize_local",                     432539767), # 432.54MB, avg file size 432.54MB
  ("fsize_db",                        5575990858), # 5.58GB, avg file size 2.79GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_1000_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1250_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_1250_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99932500e+04, 1.00000547e+05, 9.99909688e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99932500e+04, 9.99932500e+04, ],
    'CountWeightedPSWeight'                                                          : [ 1.00000075e+06, 1.00000075e+06, 1.00000075e+06, 1.00000075e+06, 1.00000075e+06, 1.00000075e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99654531e+04, 1.00360609e+05, 1.45034125e+05, 1.00013266e+05, 9.90225938e+04, 5.95691406e+04, ],
    'CountWeightedFull'                                                              : [ 9.99696875e+04, 9.99765859e+04, 9.99676016e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99696875e+04, 9.99696875e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99764500e+05, 9.99764500e+05, 9.99764500e+05, 9.99764500e+05, 9.99764500e+05, 9.99764500e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99426562e+04, 1.00337359e+05, 1.44999656e+05, 9.99889062e+04, 9.89988281e+04, 5.95551016e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     485226864), # 485.23MB, avg file size 485.23MB
  ("fsize_db",                        6322077799), # 6.32GB, avg file size 1.26GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_1250_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1500_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_1500_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99821797e+04, 9.99815078e+04, 9.99755859e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99821797e+04, 9.99821797e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99800188e+05, 9.99800188e+05, 9.99800188e+05, 9.99800188e+05, 9.99800188e+05, 9.99800188e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00017062e+05, 1.00193867e+05, 1.45566438e+05, 9.99056406e+04, 9.94505781e+04, 5.92839375e+04, ],
    'CountWeightedFull'                                                              : [ 9.99563906e+04, 9.99558281e+04, 9.99497031e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99563906e+04, 9.99563906e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99543188e+05, 9.99543188e+05, 9.99543188e+05, 9.99543188e+05, 9.99543188e+05, 9.99543188e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99927734e+04, 1.00167664e+05, 1.45528469e+05, 9.98793984e+04, 9.94252578e+04, 5.92692227e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     482374046), # 482.37MB, avg file size 482.37MB
  ("fsize_db",                        6498665132), # 6.50GB, avg file size 649.87MB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_1500_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1750_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_1750_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99790547e+04, 9.99809219e+04, 9.99776094e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99790547e+04, 9.99790547e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99813125e+05, 9.99813125e+05, 9.99813125e+05, 9.99813125e+05, 9.99813125e+05, 9.99813125e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00018094e+05, 9.98889453e+04, 1.46364062e+05, 9.99297656e+04, 1.00240758e+05, 5.90281953e+04, ],
    'CountWeightedFull'                                                              : [ 9.99518359e+04, 9.99537578e+04, 9.99501641e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99518359e+04, 9.99518359e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99538000e+05, 9.99538000e+05, 9.99538000e+05, 9.99538000e+05, 9.99538000e+05, 9.99538000e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99926250e+04, 9.98620469e+04, 1.46325062e+05, 9.99024375e+04, 1.00213883e+05, 5.90124922e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     482475480), # 482.48MB, avg file size 482.48MB
  ("fsize_db",                        7054399734), # 7.05GB, avg file size 705.44MB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_1750_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_2000_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_2000_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99609922e+04, 9.99680625e+04, 9.99565469e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99609922e+04, 9.99609922e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99584000e+05, 9.99584000e+05, 9.99584000e+05, 9.99584000e+05, 9.99584000e+05, 9.99584000e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99666250e+04, 9.99855781e+04, 1.46224141e+05, 9.99454531e+04, 9.98157656e+04, 5.88879297e+04, ],
    'CountWeightedFull'                                                              : [ 9.99336797e+04, 9.99403203e+04, 9.99294844e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99336797e+04, 9.99336797e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99311750e+05, 9.99311750e+05, 9.99311750e+05, 9.99311750e+05, 9.99311750e+05, 9.99311750e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99411406e+04, 9.99589453e+04, 1.46184219e+05, 9.99179062e+04, 9.97878438e+04, 5.88722148e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     483323918), # 483.32MB, avg file size 483.32MB
  ("fsize_db",                        6472017019), # 6.47GB, avg file size 924.57MB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_2000_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_2500_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_2500_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 9.99876641e+04, 9.99814141e+04, 9.99862656e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99876641e+04, 9.99876641e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99752312e+05, 9.99752312e+05, 9.99752312e+05, 9.99752312e+05, 9.99752312e+05, 9.99752312e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00000914e+05, 9.98327422e+04, 1.46487844e+05, 9.99447344e+04, 9.99861328e+04, 5.87100430e+04, ],
    'CountWeightedFull'                                                              : [ 9.99576562e+04, 9.99515000e+04, 9.99560312e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99576562e+04, 9.99576562e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99454312e+05, 9.99454312e+05, 9.99454312e+05, 9.99454312e+05, 9.99454312e+05, 9.99454312e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99736094e+04, 9.98018203e+04, 1.46443766e+05, 9.99150625e+04, 9.99577188e+04, 5.86933633e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     487100259), # 487.10MB, avg file size 487.10MB
  ("fsize_db",                        6553856520), # 6.55GB, avg file size 936.27MB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_2500_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_3000_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_3000_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99772734e+04, 9.99828438e+04, 9.99768516e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99772734e+04, 9.99772734e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99789250e+05, 9.99789250e+05, 9.99789250e+05, 9.99789250e+05, 9.99789250e+05, 9.99789250e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99315078e+04, 9.99852188e+04, 1.46419266e+05, 1.00031938e+05, 9.97218203e+04, 5.87396719e+04, ],
    'CountWeightedFull'                                                              : [ 9.99445312e+04, 9.99498281e+04, 9.99440859e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99445312e+04, 9.99445312e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99462375e+05, 9.99462375e+05, 9.99462375e+05, 9.99462375e+05, 9.99462375e+05, 9.99462375e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99018750e+04, 9.99513672e+04, 1.46371000e+05, 9.99999375e+04, 9.96905703e+04, 5.87214375e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     491010535), # 491.01MB, avg file size 491.01MB
  ("fsize_db",                        6743129991), # 6.74GB, avg file size 1.12GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Nov03_woPresel_nom_all/ntuples/signal_ggf_spin2_3000_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_1_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_1_hh_2b2v_dipoleRecoilOff"),
  ("nof_files",                       2),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 399998, ],
    'CountWeighted'                                                                  : [ 3.99990031e+05, 3.99946750e+05, 3.99979250e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99990031e+05, 3.99990031e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99970025e+06, 3.99970025e+06, 3.99970025e+06, 3.99970025e+06, 3.99970025e+06, 3.99970025e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99991125e+05, 3.99826656e+05, 5.57040938e+05, 3.99863031e+05, 3.99800188e+05, 2.56347562e+05, ],
    'CountWeightedFull'                                                              : [ 3.99761562e+05, 3.99719812e+05, 3.99751688e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99761562e+05, 3.99761562e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99741900e+06, 3.99741900e+06, 3.99741900e+06, 3.99741900e+06, 3.99741900e+06, 3.99741900e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99809188e+05, 3.99598375e+05, 5.56714500e+05, 3.99682062e+05, 3.99563312e+05, 2.56231641e+05, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     1585656297), # 1.59GB, avg file size 792.83MB
  ("fsize_db",                        23660265098), # 23.66GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        4.7915e-05),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_1_1_hh_2b2v_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_1_dipoleRecoilOn-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_1_hh_dipoleRecoilOn_bbvv"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_1_hh_2b2v_dipoleRecoilOn"),
  ("nof_files",                       2),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 399999, ],
    'CountWeighted'                                                                  : [ 3.99992438e+05, 3.99991125e+05, 3.99972859e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99992438e+05, 3.99992438e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99989938e+06, 3.99993638e+06, 3.99993638e+06, 3.99989425e+06, 3.99993638e+06, 3.99989425e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99932141e+05, 4.00208438e+05, 5.31625531e+05, 3.99963234e+05, 3.99503516e+05, 2.77562000e+05, ],
    'CountWeightedFull'                                                              : [ 3.99750266e+05, 3.99751250e+05, 3.99732062e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99750266e+05, 3.99750266e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99751662e+06, 3.99751662e+06, 3.99751662e+06, 3.99751662e+06, 3.99751662e+06, 3.99751662e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99733656e+05, 3.99966359e+05, 5.31304781e+05, 3.99764594e+05, 3.99261500e+05, 2.77423984e+05, ],
  }),
  ("nof_tree_events",                 399999),
  ("nof_db_events",                   399999),
  ("fsize_local",                     1522429545), # 1.52GB, avg file size 761.21MB
  ("fsize_db",                        23019095049), # 23.02GB, avg file size 1.21GB
  ("use_it",                          False),
  ("xsection",                        4.7915e-05),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Nov22_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_1_1_hh_2b2v_dipoleRecoilOn"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_2_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_2_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_2_hh_2b2v_dipoleRecoilOff"),
  ("nof_files",                       3),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 395997, ],
    'CountWeighted'                                                                  : [ 3.95966312e+05, 3.95939500e+05, 3.95958438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.95966312e+05, 3.95966312e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.95929125e+06, 3.95929900e+06, 3.95929900e+06, 3.95929125e+06, 3.95929900e+06, 3.95929125e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.95769812e+05, 3.95691531e+05, 5.55107125e+05, 3.96028438e+05, 3.95798500e+05, 2.50639000e+05, ],
    'CountWeightedFull'                                                              : [ 3.95709062e+05, 3.95685125e+05, 3.95702625e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.95709062e+05, 3.95709062e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.95676150e+06, 3.95676150e+06, 3.95676150e+06, 3.95676150e+06, 3.95676150e+06, 3.95676150e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.95577094e+05, 3.95436000e+05, 5.54751312e+05, 3.95835062e+05, 3.95543781e+05, 2.50517078e+05, ],
  }),
  ("nof_tree_events",                 395997),
  ("nof_db_events",                   395997),
  ("fsize_local",                     1681406528), # 1.68GB, avg file size 560.47MB
  ("fsize_db",                        24106383775), # 24.11GB, avg file size 1.27GB
  ("use_it",                          True),
  ("xsection",                        3.9498e-05),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_1_2_hh_2b2v_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_2_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_2_1_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_2_1_hh_2b2v_dipoleRecoilOff"),
  ("nof_files",                       2),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99958500e+05, 3.99992938e+05, 4.00007469e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99958500e+05, 3.99958500e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99971725e+06, 3.99980875e+06, 3.99980875e+06, 3.99971975e+06, 3.99980875e+06, 3.99971600e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99703344e+05, 4.00215000e+05, 5.57968500e+05, 4.00105562e+05, 3.98764406e+05, 2.54887578e+05, ],
    'CountWeightedFull'                                                              : [ 3.99654594e+05, 3.99683719e+05, 3.99700312e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99654594e+05, 3.99654594e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99674550e+06, 3.99674550e+06, 3.99674550e+06, 3.99674550e+06, 3.99674550e+06, 3.99674550e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99503188e+05, 3.99904156e+05, 5.57544375e+05, 3.99905219e+05, 3.98461750e+05, 2.54760094e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1892803466), # 1.89GB, avg file size 946.40MB
  ("fsize_db",                        26601674546), # 26.60GB, avg file size 1.27GB
  ("use_it",                          True),
  ("xsection",                        0.000394696),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_2_1_hh_2b2v_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_2_C3_1_dipoleRecoilOn-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_2_1_hh_dipoleRecoilOn_bbvv"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_2_1_hh_2b2v_dipoleRecoilOn"),
  ("nof_files",                       4),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                                          : [ 399997, ],
    'CountWeighted'                                                                  : [ 3.99895094e+05, 3.99944943e+05, 3.99891367e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99895094e+05, 3.99895094e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99898762e+06, 3.99912981e+06, 3.99912981e+06, 3.99898694e+06, 3.99912981e+06, 3.99898512e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99838355e+05, 3.99947629e+05, 5.31319336e+05, 3.99796367e+05, 3.99441742e+05, 2.77472219e+05, ],
    'CountWeightedFull'                                                              : [ 3.99580504e+05, 3.99627531e+05, 3.99579736e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99580504e+05, 3.99580504e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99598694e+06, 3.99598694e+06, 3.99598694e+06, 3.99598694e+06, 3.99598694e+06, 3.99598694e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99621457e+05, 3.99630445e+05, 5.30911047e+05, 3.99580191e+05, 3.99132824e+05, 2.77321684e+05, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     1827839261), # 1.83GB, avg file size 456.96MB
  ("fsize_db",                        25257880512), # 25.26GB, avg file size 1.15GB
  ("use_it",                          False),
  ("xsection",                        0.000394696),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Nov22_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_2_1_hh_2b2v_dipoleRecoilOn"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_0_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_0_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_0_hh_2b2v_dipoleRecoilOff"),
  ("nof_files",                       2),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 399999, ],
    'CountWeighted'                                                                  : [ 3.99937875e+05, 3.99903125e+05, 3.99944250e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99937875e+05, 3.99937875e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99915900e+06, 3.99917175e+06, 3.99917175e+06, 3.99915950e+06, 3.99917175e+06, 3.99915900e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99890812e+05, 4.00035188e+05, 5.55661875e+05, 3.99903406e+05, 3.98894719e+05, 2.57082656e+05, ],
    'CountWeightedFull'                                                              : [ 3.99727094e+05, 3.99692094e+05, 3.99733375e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99727094e+05, 3.99727094e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99704250e+06, 3.99704250e+06, 3.99704250e+06, 3.99704250e+06, 3.99704250e+06, 3.99704250e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99717406e+05, 3.99820125e+05, 5.55366875e+05, 3.99729469e+05, 3.98685375e+05, 2.56971562e+05, ],
  }),
  ("nof_tree_events",                 399999),
  ("nof_db_events",                   399999),
  ("fsize_local",                     1584513014), # 1.58GB, avg file size 792.26MB
  ("fsize_db",                        23615969861), # 23.62GB, avg file size 1.24GB
  ("use_it",                          True),
  ("xsection",                        0.000127945),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_1_0_hh_2b2v_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFHHTo2B2VTo2L2Nu_CV_1_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1p5_1_1_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_nonresonant_1p5_1_1_hh_2b2v_dipoleRecoilOff"),
  ("nof_files",                       2),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 399999, ],
    'CountWeighted'                                                                  : [ 3.99951250e+05, 3.99970875e+05, 3.99942688e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99951250e+05, 3.99951250e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99970450e+06, 3.99981550e+06, 3.99981550e+06, 3.99970350e+06, 3.99981550e+06, 3.99970250e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99843750e+05, 3.99909781e+05, 5.57366125e+05, 3.99989875e+05, 3.99647250e+05, 2.55996891e+05, ],
    'CountWeightedFull'                                                              : [ 3.99685438e+05, 3.99702625e+05, 3.99680938e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99685438e+05, 3.99685438e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99716500e+06, 3.99716500e+06, 3.99716500e+06, 3.99716500e+06, 3.99716500e+06, 3.99716500e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99657625e+05, 3.99645094e+05, 5.56996625e+05, 3.99803219e+05, 3.99380250e+05, 2.55877328e+05, ],
  }),
  ("nof_tree_events",                 399999),
  ("nof_db_events",                   399999),
  ("fsize_local",                     1729592170), # 1.73GB, avg file size 864.80MB
  ("fsize_db",                        25237710585), # 25.24GB, avg file size 2.52GB
  ("use_it",                          True),
  ("xsection",                        0.001832716),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1p5_1_1_hh_2b2v_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFHHTo2B2VTo2L2Nu_CV_0_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_0p5_1_1_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_nonresonant_0p5_1_1_hh_2b2v_dipoleRecoilOff"),
  ("nof_files",                       2),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 399999, ],
    'CountWeighted'                                                                  : [ 3.99984438e+05, 3.99943219e+05, 3.99933250e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99984438e+05, 3.99984438e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99967250e+06, 3.99972300e+06, 3.99972300e+06, 3.99967225e+06, 3.99972300e+06, 3.99967225e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99906188e+05, 4.00257000e+05, 5.58233938e+05, 3.99840750e+05, 3.99307656e+05, 2.55096812e+05, ],
    'CountWeightedFull'                                                              : [ 3.99709188e+05, 3.99670250e+05, 3.99655500e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99709188e+05, 3.99709188e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99693900e+06, 3.99693900e+06, 3.99693900e+06, 3.99693900e+06, 3.99693900e+06, 3.99693900e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99712656e+05, 3.99981625e+05, 5.57848375e+05, 3.99647438e+05, 3.99028312e+05, 2.54973125e+05, ],
  }),
  ("nof_tree_events",                 399999),
  ("nof_db_events",                   399999),
  ("fsize_local",                     1848168249), # 1.85GB, avg file size 924.08MB
  ("fsize_db",                        25513228160), # 25.51GB, avg file size 2.55GB
  ("use_it",                          True),
  ("xsection",                        0.000300473),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_nonresonant_0p5_1_1_hh_2b2v_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_0_1_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_0_1_hh_2b2v_dipoleRecoilOff"),
  ("nof_files",                       2),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 399999, ],
    'CountWeighted'                                                                  : [ 4.00002188e+05, 3.99940781e+05, 3.99977625e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.00002188e+05, 4.00002188e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99959775e+06, 3.99961875e+06, 3.99961875e+06, 3.99959775e+06, 3.99961875e+06, 3.99959775e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99947625e+05, 3.99900062e+05, 5.57296000e+05, 3.99921562e+05, 3.99664562e+05, 2.56056281e+05, ],
    'CountWeightedFull'                                                              : [ 3.99758125e+05, 3.99700531e+05, 3.99736375e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99758125e+05, 3.99758125e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99718400e+06, 3.99718400e+06, 3.99718400e+06, 3.99718400e+06, 3.99718400e+06, 3.99718400e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99759562e+05, 3.99659750e+05, 5.56951625e+05, 3.99732844e+05, 3.99408562e+05, 2.55936219e+05, ],
  }),
  ("nof_tree_events",                 399999),
  ("nof_db_events",                   399999),
  ("fsize_local",                     1779555055), # 1.78GB, avg file size 889.78MB
  ("fsize_db",                        25638125950), # 25.64GB, avg file size 2.14GB
  ("use_it",                          True),
  ("xsection",                        0.000751759),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_0_1_hh_2b2v_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2VTo2L2Nu_node_SM_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_sm_hh_2b2v"),
  ("nof_files",                       3),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 399998, ],
    'CountWeighted'                                                                  : [ 3.99943312e+05, 3.99951656e+05, 3.99963719e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.11969594e+05, 4.83222281e+05, 4.56250875e+05, 4.23832719e+05, 3.99942031e+05, 3.77546281e+05, 3.56936500e+05, 3.36753750e+05, 3.17845469e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.11970750e+05, 3.17844469e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99987275e+06, 3.99987275e+06, 3.99987275e+06, 3.99987275e+06, 3.99987275e+06, 3.99987275e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99892094e+05, 3.99445969e+05, 5.73583875e+05, 4.00091594e+05, 4.00283969e+05, 2.45840250e+05, ],
    'CountWeightedFull'                                                              : [ 3.99864156e+05, 3.99873625e+05, 3.99883969e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.11868656e+05, 4.83127219e+05, 4.56161000e+05, 4.23748969e+05, 3.99862875e+05, 3.77471875e+05, 3.56865875e+05, 3.36687375e+05, 3.17782906e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.11869844e+05, 3.17781906e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99907025e+06, 3.99907025e+06, 3.99907025e+06, 3.99907025e+06, 3.99907025e+06, 3.99907025e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99815781e+05, 3.99367688e+05, 5.73467875e+05, 4.00010500e+05, 4.00203094e+05, 2.45792719e+05, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     1701309574), # 1.70GB, avg file size 567.10MB
  ("fsize_db",                        23207192931), # 23.21GB, avg file size 1.55GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_sm_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2VTo2L2Nu_node_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_1_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 399999, ],
    'CountWeighted'                                                                  : [ 3.99990406e+05, 3.99971375e+05, 3.99952062e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10101344e+05, 4.84337906e+05, 4.59583812e+05, 4.21287969e+05, 3.99986250e+05, 3.79481188e+05, 3.54086750e+05, 3.36128062e+05, 3.18888812e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10101344e+05, 3.18888812e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99949000e+06, 3.99876625e+06, 3.99950450e+06, 3.99949000e+06, 3.98361700e+06, 3.98286400e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00048531e+05, 4.00023281e+05, 5.72516250e+05, 3.99918750e+05, 3.99374125e+05, 2.46389688e+05, ],
    'CountWeightedFull'                                                              : [ 3.99912750e+05, 3.99893938e+05, 3.99874688e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.10002500e+05, 4.84244250e+05, 4.59494812e+05, 4.21206438e+05, 3.99908625e+05, 3.79407719e+05, 3.54017969e+05, 3.36062812e+05, 3.18826938e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.10002500e+05, 3.18826938e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99873150e+06, 3.99799350e+06, 3.99873150e+06, 3.99873150e+06, 3.98284650e+06, 3.98210850e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99974688e+05, 3.99946125e+05, 5.72404812e+05, 3.99840062e+05, 3.99297094e+05, 2.46343781e+05, ],
  }),
  ("nof_tree_events",                 399999),
  ("nof_db_events",                   399999),
  ("fsize_local",                     1664525236), # 1.66GB, avg file size 832.26MB
  ("fsize_db",                        22964320188), # 22.96GB, avg file size 1.53GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_1_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2VTo2L2Nu_node_2_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_2_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 399999, ],
    'CountWeighted'                                                                  : [ 3.99820344e+05, 3.99854094e+05, 3.99855312e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.19536562e+05, 4.78713156e+05, 4.42843125e+05, 4.34165844e+05, 3.99816125e+05, 3.69701938e+05, 3.68554250e+05, 3.39257688e+05, 3.13568312e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.19537281e+05, 3.13567688e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99819150e+06, 3.99819150e+06, 3.99819150e+06, 3.99819150e+06, 3.99819150e+06, 3.99819150e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99944344e+05, 3.99974062e+05, 5.76103000e+05, 3.99877375e+05, 3.98973750e+05, 2.42956969e+05, ],
    'CountWeightedFull'                                                              : [ 3.99736344e+05, 3.99769125e+05, 3.99770719e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.19427219e+05, 4.78613062e+05, 4.42751000e+05, 4.34074250e+05, 3.99731969e+05, 3.69624875e+05, 3.68476375e+05, 3.39186500e+05, 3.13502656e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.19427938e+05, 3.13502000e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99736150e+06, 3.99736150e+06, 3.99736150e+06, 3.99736150e+06, 3.99736150e+06, 3.99736150e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99863688e+05, 3.99891000e+05, 5.75981875e+05, 3.99791000e+05, 3.98889750e+05, 2.42906562e+05, ],
  }),
  ("nof_tree_events",                 399999),
  ("nof_db_events",                   399999),
  ("fsize_local",                     1827190342), # 1.83GB, avg file size 913.60MB
  ("fsize_db",                        25245646410), # 25.25GB, avg file size 1.49GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_2_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2VTo2L2Nu_node_3_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_3_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 399998, ],
    'CountWeighted'                                                                  : [ 3.99913156e+05, 3.99873531e+05, 3.99896219e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.11919750e+05, 4.83126875e+05, 4.56085250e+05, 4.23803562e+05, 3.99913156e+05, 3.77454812e+05, 3.56913812e+05, 3.36728344e+05, 3.17792219e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.11919750e+05, 3.17792219e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99902100e+06, 3.99903100e+06, 3.99903100e+06, 3.99902100e+06, 3.99903100e+06, 3.99902100e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99974781e+05, 3.99663094e+05, 5.73533875e+05, 3.99867500e+05, 4.00032625e+05, 2.45748531e+05, ],
    'CountWeightedFull'                                                              : [ 3.99834000e+05, 3.99794469e+05, 3.99817375e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.11818438e+05, 4.83031188e+05, 4.55995219e+05, 4.23719531e+05, 3.99834000e+05, 3.77380125e+05, 3.56842938e+05, 3.36661562e+05, 3.17729438e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.11818438e+05, 3.17729438e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99823500e+06, 3.99823500e+06, 3.99823500e+06, 3.99823500e+06, 3.99823500e+06, 3.99823500e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99899312e+05, 3.99583000e+05, 5.73419125e+05, 3.99786312e+05, 3.99954688e+05, 2.45701266e+05, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     1705492871), # 1.71GB, avg file size 852.75MB
  ("fsize_db",                        22826714259), # 22.83GB, avg file size 1.43GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_3_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2VTo2L2Nu_node_4_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_4_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 399999, ],
    'CountWeighted'                                                                  : [ 3.99948875e+05, 3.99964969e+05, 3.99962312e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10009344e+05, 4.84373031e+05, 4.59721500e+05, 4.21181312e+05, 3.99948875e+05, 3.79552344e+05, 3.53979875e+05, 3.36098938e+05, 3.18922625e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10009344e+05, 3.18922562e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99932700e+06, 3.99933175e+06, 3.99933175e+06, 3.99932700e+06, 3.99932450e+06, 3.99931950e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99935094e+05, 3.99686375e+05, 5.72423000e+05, 4.00063562e+05, 3.99650875e+05, 2.46529781e+05, ],
    'CountWeightedFull'                                                              : [ 3.99873188e+05, 3.99887938e+05, 3.99886812e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.09912688e+05, 4.84281375e+05, 4.59634438e+05, 4.21101375e+05, 3.99873188e+05, 3.79480531e+05, 3.53912812e+05, 3.36035312e+05, 3.18862312e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.09912719e+05, 3.18862250e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99857950e+06, 3.99857950e+06, 3.99857950e+06, 3.99857950e+06, 3.99857250e+06, 3.99857250e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99862312e+05, 3.99610875e+05, 5.72312625e+05, 3.99985562e+05, 3.99574250e+05, 2.46484203e+05, ],
  }),
  ("nof_tree_events",                 399999),
  ("nof_db_events",                   399999),
  ("fsize_local",                     1663222870), # 1.66GB, avg file size 831.61MB
  ("fsize_db",                        23101309698), # 23.10GB, avg file size 1.36GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_4_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2VTo2L2Nu_node_5_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_5_hh_2b2v"),
  ("nof_files",                       3),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 399997, ],
    'CountWeighted'                                                                  : [ 3.99952781e+05, 3.99933844e+05, 3.99913344e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.12952656e+05, 4.82638125e+05, 4.54482969e+05, 4.25157188e+05, 3.99952781e+05, 3.76537375e+05, 3.58408812e+05, 3.37086000e+05, 3.17309688e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.12952656e+05, 3.17309688e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99932225e+06, 3.99932225e+06, 3.99932225e+06, 3.99932225e+06, 3.99932225e+06, 3.99932225e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99988125e+05, 3.99894438e+05, 5.73643250e+05, 4.00019656e+05, 3.99538406e+05, 2.45482891e+05, ],
    'CountWeightedFull'                                                              : [ 3.99870938e+05, 3.99853250e+05, 3.99831969e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.12848000e+05, 4.82539719e+05, 4.54390469e+05, 4.25070156e+05, 3.99870938e+05, 3.76460562e+05, 3.58335531e+05, 3.37017125e+05, 3.17244906e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.12848000e+05, 3.17244906e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99850050e+06, 3.99850050e+06, 3.99850050e+06, 3.99850050e+06, 3.99850050e+06, 3.99850050e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99911312e+05, 3.99814250e+05, 5.73525875e+05, 3.99936906e+05, 3.99455656e+05, 2.45434641e+05, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     1721420285), # 1.72GB, avg file size 573.81MB
  ("fsize_db",                        23707187679), # 23.71GB, avg file size 1.58GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_5_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2VTo2L2Nu_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_6_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 399998, ],
    'CountWeighted'                                                                  : [ 3.99929688e+05, 3.99970375e+05, 3.99952688e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10262656e+05, 4.84217406e+05, 4.59248062e+05, 4.21508562e+05, 3.99929281e+05, 3.79285562e+05, 3.54332188e+05, 3.36175000e+05, 3.18780875e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10262656e+05, 3.18780875e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99927250e+06, 3.99927250e+06, 3.99927250e+06, 3.99927250e+06, 3.99927250e+06, 3.99927250e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99966438e+05, 4.00355188e+05, 5.72744250e+05, 3.99979312e+05, 3.99087625e+05, 2.46188750e+05, ],
    'CountWeightedFull'                                                              : [ 3.99853750e+05, 3.99893469e+05, 3.99876438e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.10164938e+05, 4.84124688e+05, 4.59160156e+05, 4.21427750e+05, 3.99853250e+05, 3.79212812e+05, 3.54264062e+05, 3.36110688e+05, 3.18719875e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.10164938e+05, 3.18719812e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99851300e+06, 3.99851300e+06, 3.99851300e+06, 3.99851300e+06, 3.99851300e+06, 3.99851300e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99892062e+05, 4.00278688e+05, 5.72633250e+05, 3.99899719e+05, 3.99010375e+05, 2.46142109e+05, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     1666965247), # 1.67GB, avg file size 833.48MB
  ("fsize_db",                        23050645194), # 23.05GB, avg file size 1.36GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_6_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2VTo2L2Nu_node_7_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_7_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 399997, ],
    'CountWeighted'                                                                  : [ 3.99939812e+05, 3.99942188e+05, 3.99942562e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10081469e+05, 4.84309562e+05, 4.59545812e+05, 4.21277094e+05, 3.99938312e+05, 3.79456062e+05, 3.54079750e+05, 3.36117062e+05, 3.18872250e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10081469e+05, 3.18872250e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99936025e+06, 3.99937150e+06, 3.99937200e+06, 3.99936025e+06, 3.99927800e+06, 3.99926575e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99958375e+05, 4.00144688e+05, 5.73081562e+05, 3.99999250e+05, 3.99592031e+05, 2.46252844e+05, ],
    'CountWeightedFull'                                                              : [ 3.99863094e+05, 3.99865219e+05, 3.99864469e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.09982500e+05, 4.84215812e+05, 4.59456812e+05, 4.21195375e+05, 3.99861625e+05, 3.79382781e+05, 3.54011125e+05, 3.36051812e+05, 3.18810625e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.09982500e+05, 3.18810625e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99859325e+06, 3.99859250e+06, 3.99859325e+06, 3.99859325e+06, 3.99849900e+06, 3.99849850e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99884250e+05, 4.00066562e+05, 5.72969375e+05, 3.99920094e+05, 3.99515812e+05, 2.46206672e+05, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     1664403534), # 1.66GB, avg file size 832.20MB
  ("fsize_db",                        23799450196), # 23.80GB, avg file size 1.98GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_7_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2VTo2L2Nu_node_8_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_8_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 399999, ],
    'CountWeighted'                                                                  : [ 3.99992062e+05, 3.99942844e+05, 3.99960031e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.09960594e+05, 4.84407281e+05, 4.59815312e+05, 4.21100000e+05, 3.99992062e+05, 3.79607625e+05, 3.53879062e+05, 3.36071875e+05, 3.18950125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.09960594e+05, 3.18950125e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.45389888e+06, 1.45402375e+06, 2.02910888e+06, 1.45483300e+06, 1.40005650e+06, 8.96174625e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99861750e+05, 4.00082688e+05, 5.72156688e+05, 4.00118312e+05, 3.98964312e+05, 2.46472656e+05, ],
    'CountWeightedFull'                                                              : [ 3.99913594e+05, 3.99866062e+05, 3.99881875e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.09861562e+05, 4.84313250e+05, 4.59726156e+05, 4.21018062e+05, 3.99913594e+05, 3.79534000e+05, 3.53810062e+05, 3.36006562e+05, 3.18888094e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.09861562e+05, 3.18888094e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.45363312e+06, 1.45374225e+06, 2.02870988e+06, 1.45455050e+06, 1.39978375e+06, 8.96008250e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99788531e+05, 4.00005156e+05, 5.72043188e+05, 4.00040594e+05, 3.98885656e+05, 2.46426828e+05, ],
  }),
  ("nof_tree_events",                 399999),
  ("nof_db_events",                   399999),
  ("fsize_local",                     1661121687), # 1.66GB, avg file size 830.56MB
  ("fsize_db",                        22468004114), # 22.47GB, avg file size 1.32GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_8_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2VTo2L2Nu_node_9_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_9_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 399999, ],
    'CountWeighted'                                                                  : [ 3.99963688e+05, 3.99953656e+05, 3.99956250e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.19457375e+05, 4.78843656e+05, 4.42982188e+05, 4.33988219e+05, 3.99961406e+05, 3.69902562e+05, 3.68280719e+05, 3.39311812e+05, 3.13760219e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.19457625e+05, 3.13760125e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99944725e+06, 3.99944725e+06, 3.99944725e+06, 3.99944725e+06, 3.99944725e+06, 3.99944725e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00045438e+05, 4.00483094e+05, 5.76177938e+05, 3.99920000e+05, 3.98677781e+05, 2.43115219e+05, ],
    'CountWeightedFull'                                                              : [ 3.99879062e+05, 3.99869688e+05, 3.99873438e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.19348625e+05, 4.78743750e+05, 4.42890000e+05, 4.33897438e+05, 3.99876781e+05, 3.69825500e+05, 3.68203500e+05, 3.39240781e+05, 3.13694781e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.19348906e+05, 3.13694688e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99860750e+06, 3.99860750e+06, 3.99860750e+06, 3.99860750e+06, 3.99860750e+06, 3.99860750e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99964875e+05, 4.00400125e+05, 5.76056250e+05, 3.99833531e+05, 3.98593406e+05, 2.43065250e+05, ],
  }),
  ("nof_tree_events",                 399999),
  ("nof_db_events",                   399999),
  ("fsize_local",                     1844846242), # 1.84GB, avg file size 922.42MB
  ("fsize_db",                        25032953842), # 25.03GB, avg file size 1.19GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_9_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2VTo2L2Nu_node_10_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_10_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99990406e+05, 3.99925469e+05, 3.99976438e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10117188e+05, 4.84342062e+05, 4.59575406e+05, 4.21305688e+05, 3.99990406e+05, 3.79477750e+05, 3.54103000e+05, 3.36135031e+05, 3.18887000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10117250e+05, 3.18886875e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99921200e+06, 3.85714500e+06, 3.99998750e+06, 3.99943250e+06, 3.53811000e+06, 3.39481900e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00015062e+05, 4.00120750e+05, 5.71965938e+05, 3.99940906e+05, 3.98820688e+05, 2.46600172e+05, ],
    'CountWeightedFull'                                                              : [ 3.99913000e+05, 3.99850250e+05, 3.99900625e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.10019250e+05, 4.84249438e+05, 4.59487375e+05, 4.21224750e+05, 3.99913000e+05, 3.79405000e+05, 3.54034938e+05, 3.36070625e+05, 3.18825906e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.10019281e+05, 3.18825750e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99844150e+06, 3.85640000e+06, 3.99921100e+06, 3.99866225e+06, 3.53742625e+06, 3.39417200e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99941250e+05, 4.00044750e+05, 5.71855500e+05, 3.99861938e+05, 3.98743188e+05, 2.46553547e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1662592586), # 1.66GB, avg file size 831.30MB
  ("fsize_db",                        23040806113), # 23.04GB, avg file size 1.44GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_10_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2VTo2L2Nu_node_11_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_11_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 399998, ],
    'CountWeighted'                                                                  : [ 3.99993844e+05, 3.99981625e+05, 3.99924688e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10454031e+05, 4.84121969e+05, 4.58931312e+05, 4.21765125e+05, 3.99993188e+05, 3.79114156e+05, 3.54615969e+05, 3.36249438e+05, 3.18698750e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10454031e+05, 3.18698750e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99983225e+06, 3.99983225e+06, 3.99983225e+06, 3.99983225e+06, 3.99983225e+06, 3.99983225e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99935938e+05, 3.99876562e+05, 5.73175875e+05, 4.00033906e+05, 3.99991375e+05, 2.46172031e+05, ],
    'CountWeightedFull'                                                              : [ 3.99915156e+05, 3.99902875e+05, 3.99846750e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.10353438e+05, 4.84026906e+05, 4.58841250e+05, 4.21682062e+05, 3.99914438e+05, 3.79039469e+05, 3.54546219e+05, 3.36183375e+05, 3.18636094e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.10353438e+05, 3.18636062e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99904425e+06, 3.99904425e+06, 3.99904425e+06, 3.99904425e+06, 3.99904425e+06, 3.99904425e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99860938e+05, 3.99798500e+05, 5.73061750e+05, 3.99954188e+05, 3.99911562e+05, 2.46125125e+05, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     1671513970), # 1.67GB, avg file size 835.76MB
  ("fsize_db",                        23065514169), # 23.07GB, avg file size 1.36GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_11_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2VTo2L2Nu_node_12_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_12_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99929188e+05, 3.99951250e+05, 3.99898406e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.09915312e+05, 4.84387688e+05, 4.59812469e+05, 4.21063031e+05, 3.99926250e+05, 3.79604500e+05, 3.53846625e+05, 3.36057688e+05, 3.18947219e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.09915312e+05, 3.18947219e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.88564938e+05, 8.88528438e+05, 1.26209625e+06, 8.88320312e+05, 8.77811875e+05, 5.47703250e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00010750e+05, 4.00005750e+05, 5.72053375e+05, 3.99913250e+05, 3.99048188e+05, 2.46563906e+05, ],
    'CountWeightedFull'                                                              : [ 3.99852625e+05, 3.99873844e+05, 3.99822656e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.09818000e+05, 4.84295125e+05, 4.59724688e+05, 4.20982625e+05, 3.99849500e+05, 3.79531875e+05, 3.53778938e+05, 3.35993469e+05, 3.18886406e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.09818000e+05, 3.18886406e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 8.88402625e+05, 8.88360375e+05, 1.26185200e+06, 8.88146812e+05, 8.77641000e+05, 5.47601062e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99937812e+05, 3.99930094e+05, 5.71942875e+05, 3.99834969e+05, 3.98970750e+05, 2.46517938e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1660591261), # 1.66GB, avg file size 830.30MB
  ("fsize_db",                        23515520244), # 23.52GB, avg file size 1.24GB
  ("use_it",                          True),
  ("xsection",                        0.027761),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_12_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2VTo2L2Nu_node_cHHH0_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH0_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH0_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                                          : [ 383098, ],
    'CountWeighted'                                                                  : [ 3.60843375e+05, 3.60876156e+05, 3.60866062e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.17606438e+05, 4.10244344e+05, 4.05057625e+05, 3.69126594e+05, 3.60843344e+05, 3.54234719e+05, 3.27247344e+05, 3.18772500e+05, 3.11544438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.32323031e+05, 3.04341438e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.60781625e+05, 3.60493688e+05, 5.14249312e+05, 3.60993625e+05, 3.61367438e+05, 2.23390000e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.45263008e+04, 2.45121172e+04, 3.49904609e+04, 2.45451934e+04, 2.45878965e+04, 1.51834766e+04, ],
    'CountWeightedFull'                                                              : [ 2.30796172e+04, 2.30775469e+04, 2.30823672e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.67079395e+04, 2.62369141e+04, 2.59050195e+04, 2.36076660e+04, 2.30796172e+04, 2.26549082e+04, 2.09288594e+04, 2.03868203e+04, 1.99244863e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.76494355e+04, 1.94638574e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.30736934e+04, 2.30555918e+04, 3.28897188e+04, 2.30873906e+04, 2.31116172e+04, 1.42865098e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.57169067e+03, 1.57074414e+03, 2.24215649e+03, 1.57291125e+03, 1.57556812e+03, 9.73013489e+02, ],
  }),
  ("nof_tree_events",                 383098),
  ("nof_db_events",                   383098),
  ("fsize_local",                     1519238852), # 1.52GB, avg file size 759.62MB
  ("fsize_db",                        19461973427), # 19.46GB, avg file size 846.17MB
  ("use_it",                          True),
  ("xsection",                        0.00187669),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_cHHH0_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2VTo2L2Nu_node_cHHH1_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH1_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH1_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    27),
  ("nof_events",                      {
    'Count'                                                                          : [ 399998, ],
    'CountWeighted'                                                                  : [ 3.59007562e+05, 3.58995094e+05, 3.59002062e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.08762188e+05, 4.02175938e+05, 3.97835312e+05, 3.67300969e+05, 3.58994062e+05, 3.52450812e+05, 3.29672062e+05, 3.20639406e+05, 3.13074812e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.26300000e+05, 3.03533062e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.59077312e+05, 3.59327625e+05, 5.11664500e+05, 3.58863500e+05, 3.58286000e+05, 2.21655125e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.19700098e+04, 1.19818428e+04, 1.70655020e+04, 1.19693672e+04, 1.19502588e+04, 7.39029980e+03, ],
    'CountWeightedFull'                                                              : [ 1.07200850e+04, 1.07208730e+04, 1.07216055e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.22063945e+04, 1.20095186e+04, 1.18797402e+04, 1.09683691e+04, 1.07193711e+04, 1.05246758e+04, 9.84438867e+03, 9.57454492e+03, 9.34856738e+03, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.27303750e+04, 9.06362598e+03, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.07226992e+04, 1.07301777e+04, 1.52790430e+04, 1.07162549e+04, 1.06988223e+04, 6.61899219e+03, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.58760620e+02, 3.59265198e+02, 5.11119965e+02, 3.58909302e+02, 3.57752014e+02, 2.21555328e+02, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     1629407571), # 1.63GB, avg file size 814.70MB
  ("fsize_db",                        20612880655), # 20.61GB, avg file size 763.44MB
  ("use_it",                          True),
  ("xsection",                        0.00083564),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_cHHH1_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2VTo2L2Nu_node_cHHH2p45_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH2p45_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH2p45_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 399998, ],
    'CountWeighted'                                                                  : [ 3.44776375e+05, 3.44740250e+05, 3.44766062e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.93014000e+05, 3.87587281e+05, 3.84136594e+05, 3.51759656e+05, 3.44763594e+05, 3.39261062e+05, 3.14958500e+05, 3.07209156e+05, 3.00691625e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.14055406e+05, 2.87784500e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.44639469e+05, 3.44724688e+05, 4.92587875e+05, 3.44879562e+05, 3.44774156e+05, 2.12147250e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 5.25140332e+03, 5.25396875e+03, 7.52052051e+03, 5.25546240e+03, 5.26529395e+03, 3.23092188e+03, ],
    'CountWeightedFull'                                                              : [ 4.52072754e+03, 4.52053955e+03, 4.52104492e+03, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.15386914e+03, 5.08260791e+03, 5.03727344e+03, 4.61287402e+03, 4.52063379e+03, 4.44883398e+03, 4.13021582e+03, 4.02854053e+03, 3.94301953e+03, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.42982422e+03, 3.77377393e+03, ],
    'CountWeightedFullPSWeight'                                                      : [ 4.51941504e+03, 4.52061230e+03, 6.45936670e+03, 4.52257178e+03, 4.52096484e+03, 2.78200977e+03, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 6.90009232e+01, 6.90418091e+01, 9.88222198e+01, 6.90554047e+01, 6.91785812e+01, 4.24477768e+01, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     1633375895), # 1.63GB, avg file size 816.69MB
  ("fsize_db",                        20453536548), # 20.45GB, avg file size 1.20GB
  ("use_it",                          True),
  ("xsection",                        0.00035324),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_cHHH2p45_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2VTo2L2Nu_node_cHHH5_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH5_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH5_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 399999, ],
    'CountWeighted'                                                                  : [ 3.93408062e+05, 3.93384812e+05, 3.93375062e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.71152500e+05, 4.62243656e+05, 4.55380406e+05, 4.01255688e+05, 3.93404875e+05, 3.86725688e+05, 3.45566219e+05, 3.38608812e+05, 3.32312000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.85468125e+05, 3.25618688e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.93493125e+05, 3.92925219e+05, 5.59456125e+05, 3.93285375e+05, 3.93464750e+05, 2.43994219e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.21094727e+04, 3.20603535e+04, 4.56850742e+04, 3.20904805e+04, 3.21461914e+04, 1.99148750e+04, ],
    'CountWeightedFull'                                                              : [ 3.15488691e+04, 3.15502891e+04, 3.15535742e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.77864922e+04, 3.70714609e+04, 3.65205938e+04, 3.21810547e+04, 3.15485625e+04, 3.10149062e+04, 2.77137070e+04, 2.71554492e+04, 2.66501953e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.89351562e+04, 2.61134609e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.15579297e+04, 3.15125547e+04, 4.48678359e+04, 3.15410898e+04, 3.15552617e+04, 1.95680625e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.57806348e+03, 2.57424634e+03, 3.66735547e+03, 2.57680225e+03, 2.58087646e+03, 1.59970984e+03, ],
  }),
  ("nof_tree_events",                 399999),
  ("nof_db_events",                   399999),
  ("fsize_local",                     1490452425), # 1.49GB, avg file size 745.23MB
  ("fsize_db",                        19750514425), # 19.75GB, avg file size 987.53MB
  ("use_it",                          True),
  ("xsection",                        0.00245396),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_cHHH5_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2WToLNu2J_node_SM_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_sm_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 399993, ],
    'CountWeighted'                                                                  : [ 3.99938625e+05, 3.99975656e+05, 3.99986125e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.11945750e+05, 4.83244812e+05, 4.56304625e+05, 4.23799625e+05, 3.99938188e+05, 3.77581250e+05, 3.56902500e+05, 3.36751156e+05, 3.17867312e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.11945750e+05, 3.17867312e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99980525e+06, 3.99980525e+06, 3.99980525e+06, 3.99980525e+06, 3.99980525e+06, 3.99980525e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00073938e+05, 4.00046500e+05, 5.82914250e+05, 3.99887625e+05, 3.99163750e+05, 2.37470594e+05, ],
    'CountWeightedFull'                                                              : [ 3.99860406e+05, 3.99895938e+05, 3.99906438e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.11844188e+05, 4.83149375e+05, 4.56214688e+05, 4.23715719e+05, 3.99859875e+05, 3.77506812e+05, 3.56831625e+05, 3.36684625e+05, 3.17804500e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.11844188e+05, 3.17804500e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99900550e+06, 3.99900550e+06, 3.99900550e+06, 3.99900550e+06, 3.99900550e+06, 3.99900550e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99997031e+05, 3.99968062e+05, 5.82797625e+05, 3.99805750e+05, 3.99083938e+05, 2.37424250e+05, ],
  }),
  ("nof_tree_events",                 399993),
  ("nof_db_events",                   399993),
  ("fsize_local",                     1771963101), # 1.77GB, avg file size 885.98MB
  ("fsize_db",                        23965435053), # 23.97GB, avg file size 1.20GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_sm_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2WToLNu2J_node_2_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_2_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                                          : [ 396995, ],
    'CountWeighted'                                                                  : [ 3.96833812e+05, 3.96845781e+05, 3.96802531e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.15618688e+05, 4.75129688e+05, 4.39548438e+05, 4.30880438e+05, 3.96833000e+05, 3.66942812e+05, 3.65757750e+05, 3.36704031e+05, 3.11222125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.15619438e+05, 3.11221500e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.96828400e+06, 3.96828400e+06, 3.96828400e+06, 3.96828400e+06, 3.96828400e+06, 3.96828400e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.96956281e+05, 3.97265844e+05, 5.81352438e+05, 3.96870375e+05, 3.95559375e+05, 2.32825734e+05, ],
    'CountWeightedFull'                                                              : [ 3.96744875e+05, 3.96757438e+05, 3.96713875e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.15502812e+05, 4.75023281e+05, 4.39450438e+05, 4.30783312e+05, 3.96744000e+05, 3.66860812e+05, 3.65675312e+05, 3.36628562e+05, 3.11152562e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.15503562e+05, 3.11151938e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.96739500e+06, 3.96739500e+06, 3.96739500e+06, 3.96739500e+06, 3.96739500e+06, 3.96739500e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.96871375e+05, 3.97178250e+05, 5.81220125e+05, 3.96779812e+05, 3.95468312e+05, 2.32774891e+05, ],
  }),
  ("nof_tree_events",                 396995),
  ("nof_db_events",                   396995),
  ("fsize_local",                     1896568042), # 1.90GB, avg file size 948.28MB
  ("fsize_db",                        25251888315), # 25.25GB, avg file size 1.15GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_2_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2WToLNu2J_node_3_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_3_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                                          : [ 393994, ],
    'CountWeighted'                                                                  : [ 3.93881812e+05, 3.93892062e+05, 3.93886781e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.04238656e+05, 4.75878938e+05, 4.49243312e+05, 4.17444812e+05, 3.93879688e+05, 3.71792812e+05, 3.51558438e+05, 3.31677344e+05, 3.13026188e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.04238812e+05, 3.13026125e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.93917575e+06, 3.93918525e+06, 3.93918525e+06, 3.93917575e+06, 3.93918525e+06, 3.93917575e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.93872625e+05, 3.93992125e+05, 5.74182188e+05, 3.93932500e+05, 3.93031562e+05, 2.33658016e+05, ],
    'CountWeightedFull'                                                              : [ 3.93799781e+05, 3.93809594e+05, 3.93804188e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.04132531e+05, 4.75778750e+05, 4.49149219e+05, 4.17356938e+05, 3.93797719e+05, 3.71714875e+05, 3.51484281e+05, 3.31607656e+05, 3.12960531e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.04132688e+05, 3.12960500e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.93834950e+06, 3.93834950e+06, 3.93834950e+06, 3.93834950e+06, 3.93834950e+06, 3.93834950e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.93796219e+05, 3.93910938e+05, 5.74062000e+05, 3.93850938e+05, 3.92947812e+05, 2.33611391e+05, ],
  }),
  ("nof_tree_events",                 393994),
  ("nof_db_events",                   393994),
  ("fsize_local",                     1755386656), # 1.76GB, avg file size 877.69MB
  ("fsize_db",                        23680187086), # 23.68GB, avg file size 1.03GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_3_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2WToLNu2J_node_4_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_4_hh_2b2v_sl"),
  ("nof_files",                       3),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                                          : [ 399996, ],
    'CountWeighted'                                                                  : [ 3.99930719e+05, 3.99916188e+05, 3.99922594e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.09971625e+05, 4.84350469e+05, 4.59709438e+05, 4.21149906e+05, 3.99929844e+05, 3.79540531e+05, 3.53952812e+05, 3.36081812e+05, 3.18912438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.09971625e+05, 3.18912438e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99897500e+06, 3.99899350e+06, 3.99899350e+06, 3.99897500e+06, 3.99896900e+06, 3.99895050e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00016406e+05, 3.99807906e+05, 5.82078438e+05, 3.99913375e+05, 3.99251719e+05, 2.38065578e+05, ],
    'CountWeightedFull'                                                              : [ 3.99851625e+05, 3.99836750e+05, 3.99842656e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.09869688e+05, 4.84253812e+05, 4.59617875e+05, 4.21065938e+05, 3.99850688e+05, 3.79464969e+05, 3.53881844e+05, 3.36014781e+05, 3.18848844e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.09869688e+05, 3.18848844e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99820375e+06, 3.99820375e+06, 3.99820375e+06, 3.99820375e+06, 3.99817950e+06, 3.99817925e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99940781e+05, 3.99729375e+05, 5.81961750e+05, 3.99832875e+05, 3.99170500e+05, 2.38019547e+05, ],
  }),
  ("nof_tree_events",                 399996),
  ("nof_db_events",                   399996),
  ("fsize_local",                     1730075250), # 1.73GB, avg file size 576.69MB
  ("fsize_db",                        23798532201), # 23.80GB, avg file size 1.03GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_4_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2WToLNu2J_node_5_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_5_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 399995, ],
    'CountWeighted'                                                                  : [ 3.99926250e+05, 3.99914094e+05, 3.99891625e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.12936188e+05, 4.82628875e+05, 4.54481094e+05, 4.25144625e+05, 3.99922156e+05, 3.76536000e+05, 3.58398094e+05, 3.37080875e+05, 3.17308625e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.12936188e+05, 3.17308625e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99952275e+06, 3.99952275e+06, 3.99952275e+06, 3.99952275e+06, 3.99952275e+06, 3.99952275e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99822906e+05, 4.00360531e+05, 5.82996500e+05, 4.00130969e+05, 3.98517469e+05, 2.37035844e+05, ],
    'CountWeightedFull'                                                              : [ 3.99845625e+05, 3.99833781e+05, 3.99810938e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.12831812e+05, 4.82530781e+05, 4.54389031e+05, 4.25058188e+05, 3.99841438e+05, 3.76459562e+05, 3.58325125e+05, 3.37012250e+05, 3.17244375e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.12831812e+05, 3.17244375e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99870900e+06, 3.99870900e+06, 3.99870900e+06, 3.99870900e+06, 3.99870900e+06, 3.99870900e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99744531e+05, 4.00278781e+05, 5.82877438e+05, 4.00047219e+05, 3.98437125e+05, 2.36988656e+05, ],
  }),
  ("nof_tree_events",                 399995),
  ("nof_db_events",                   399995),
  ("fsize_local",                     1797053973), # 1.80GB, avg file size 898.53MB
  ("fsize_db",                        24105158990), # 24.11GB, avg file size 1.27GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_5_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2WToLNu2J_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_6_hh_2b2v_sl"),
  ("nof_files",                       3),
  ("nof_db_files",                    25),
  ("nof_events",                      {
    'Count'                                                                          : [ 399997, ],
    'CountWeighted'                                                                  : [ 3.99918094e+05, 3.99890469e+05, 3.99891000e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10153594e+05, 4.84166812e+05, 4.59233844e+05, 4.21408312e+05, 3.99909031e+05, 3.79264312e+05, 3.54239188e+05, 3.36122531e+05, 3.18756062e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10153594e+05, 3.18756750e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99908700e+06, 3.99908825e+06, 3.99908825e+06, 3.99908525e+06, 3.99908825e+06, 3.99908525e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99979938e+05, 4.00002750e+05, 5.82634562e+05, 3.99885625e+05, 3.99282969e+05, 2.37735328e+05, ],
    'CountWeightedFull'                                                              : [ 3.99837281e+05, 3.99810000e+05, 3.99810344e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.10050812e+05, 4.84069094e+05, 4.59141281e+05, 4.21323500e+05, 3.99828375e+05, 3.79187969e+05, 3.54167688e+05, 3.36054594e+05, 3.18691906e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.10050812e+05, 3.18692594e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99827300e+06, 3.99827300e+06, 3.99827300e+06, 3.99827300e+06, 3.99827300e+06, 3.99827300e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99903312e+05, 3.99921938e+05, 5.82517812e+05, 3.99803781e+05, 3.99204094e+05, 2.37688594e+05, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     1736788369), # 1.74GB, avg file size 578.93MB
  ("fsize_db",                        23790005587), # 23.79GB, avg file size 951.60MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_6_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2WToLNu2J_node_7_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_7_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    26),
  ("nof_events",                      {
    'Count'                                                                          : [ 399997, ],
    'CountWeighted'                                                                  : [ 3.99964062e+05, 3.99977188e+05, 3.99931562e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10086938e+05, 4.84288250e+05, 4.59506688e+05, 4.21290844e+05, 3.99963750e+05, 3.79433969e+05, 3.54097875e+05, 3.36117062e+05, 3.18858719e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10086938e+05, 3.18858688e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99932400e+06, 3.99932400e+06, 3.99932400e+06, 3.99932400e+06, 3.99921750e+06, 3.99921750e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99920062e+05, 3.99759312e+05, 5.82090938e+05, 4.00020500e+05, 3.99390812e+05, 2.38131781e+05, ],
    'CountWeightedFull'                                                              : [ 3.99884250e+05, 3.99897938e+05, 3.99851906e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.09985750e+05, 4.84192250e+05, 4.59415844e+05, 4.21207188e+05, 3.99883844e+05, 3.79358812e+05, 3.54027562e+05, 3.36050312e+05, 3.18795500e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.09985750e+05, 3.18795500e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99853100e+06, 3.99853100e+06, 3.99853100e+06, 3.99853100e+06, 3.99842450e+06, 3.99842450e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99843938e+05, 3.99680125e+05, 5.81972750e+05, 3.99938812e+05, 3.99310250e+05, 2.38085516e+05, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     1731752795), # 1.73GB, avg file size 865.88MB
  ("fsize_db",                        23886773869), # 23.89GB, avg file size 918.72MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_7_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2WToLNu2J_node_8_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_8_hh_2b2v_sl"),
  ("nof_files",                       3),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 395996, ],
    'CountWeighted'                                                                  : [ 3.95951531e+05, 3.95939625e+05, 3.95936750e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.04813406e+05, 4.79557031e+05, 4.55241188e+05, 4.16845344e+05, 3.95951531e+05, 3.75826250e+05, 3.50300219e+05, 3.32700188e+05, 3.15771000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.04815844e+05, 3.15768844e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.15146812e+06, 1.15146388e+06, 1.64674800e+06, 1.15152988e+06, 1.11994925e+06, 6.85161562e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.95949031e+05, 3.95992281e+05, 5.76283875e+05, 3.95969844e+05, 3.95091969e+05, 2.35603062e+05, ],
    'CountWeightedFull'                                                              : [ 3.95873500e+05, 3.95862125e+05, 3.95859344e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.04714469e+05, 4.79463000e+05, 4.55152000e+05, 4.16763562e+05, 3.95873500e+05, 3.75752750e+05, 3.50231312e+05, 3.32634875e+05, 3.15709188e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.04716906e+05, 3.15707062e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.15125175e+06, 1.15123850e+06, 1.64642550e+06, 1.15129762e+06, 1.11973125e+06, 6.85029750e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.95874688e+05, 3.95914938e+05, 5.76170625e+05, 3.95890125e+05, 3.95014812e+05, 2.35557672e+05, ],
  }),
  ("nof_tree_events",                 395996),
  ("nof_db_events",                   395996),
  ("fsize_local",                     1711973687), # 1.71GB, avg file size 570.66MB
  ("fsize_db",                        22673829945), # 22.67GB, avg file size 1.19GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_8_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2WToLNu2J_node_9_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_9_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    24),
  ("nof_events",                      {
    'Count'                                                                          : [ 399994, ],
    'CountWeighted'                                                                  : [ 3.99844438e+05, 3.99830938e+05, 3.99829188e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.19289875e+05, 4.78754562e+05, 4.42950719e+05, 4.33824688e+05, 3.99843125e+05, 3.69857375e+05, 3.68125344e+05, 3.39217188e+05, 3.13708469e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.19290031e+05, 3.13708281e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99888950e+06, 3.99888950e+06, 3.99888950e+06, 3.99888950e+06, 3.99888950e+06, 3.99888950e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00121438e+05, 4.00558125e+05, 5.84891375e+05, 3.99647562e+05, 3.97609750e+05, 2.34756578e+05, ],
    'CountWeightedFull'                                                              : [ 3.99757719e+05, 3.99744938e+05, 3.99742938e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.19176469e+05, 4.78650562e+05, 4.42854656e+05, 4.33730062e+05, 3.99756312e+05, 3.69776938e+05, 3.68044938e+05, 3.39143188e+05, 3.13640188e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.19176625e+05, 3.13640000e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99799750e+06, 3.99799750e+06, 3.99799750e+06, 3.99799750e+06, 3.99799750e+06, 3.99799750e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 4.00039312e+05, 4.00470625e+05, 5.84763250e+05, 3.99559938e+05, 3.97523812e+05, 2.34707562e+05, ],
  }),
  ("nof_tree_events",                 399994),
  ("nof_db_events",                   399994),
  ("fsize_local",                     1943129520), # 1.94GB, avg file size 971.56MB
  ("fsize_db",                        25258622692), # 25.26GB, avg file size 1.05GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_9_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2WToLNu2J_node_10_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_10_hh_2b2v_sl"),
  ("nof_files",                       3),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 399996, ],
    'CountWeighted'                                                                  : [ 3.99952875e+05, 3.99940188e+05, 3.99948750e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10085719e+05, 4.84286781e+05, 4.59505031e+05, 4.21291938e+05, 3.99952875e+05, 3.79429406e+05, 3.54101375e+05, 3.36117125e+05, 3.18855969e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10086125e+05, 3.18855531e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99842950e+06, 3.83224625e+06, 3.99926075e+06, 3.99876675e+06, 3.47498050e+06, 3.30754075e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99907250e+05, 4.00035719e+05, 5.82087250e+05, 4.00077938e+05, 3.98955781e+05, 2.37930750e+05, ],
    'CountWeightedFull'                                                              : [ 3.99875062e+05, 3.99862406e+05, 3.99871438e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.09986812e+05, 4.84192562e+05, 4.59415812e+05, 4.21210062e+05, 3.99875062e+05, 3.79355781e+05, 3.54032562e+05, 3.36051906e+05, 3.18794125e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.09987250e+05, 3.18793656e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99765425e+06, 3.83150600e+06, 3.99848575e+06, 3.99799125e+06, 3.47430850e+06, 3.30690425e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99832062e+05, 3.99958312e+05, 5.81972688e+05, 3.99997250e+05, 3.98877500e+05, 2.37885047e+05, ],
  }),
  ("nof_tree_events",                 399996),
  ("nof_db_events",                   399996),
  ("fsize_local",                     1733244106), # 1.73GB, avg file size 577.75MB
  ("fsize_db",                        23115766015), # 23.12GB, avg file size 1.36GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_10_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2WToLNu2J_node_11_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_11_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 399997, ],
    'CountWeighted'                                                                  : [ 3.99973469e+05, 3.99967969e+05, 3.99982312e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10435219e+05, 4.84136438e+05, 4.58969469e+05, 4.21741250e+05, 3.99970250e+05, 3.79136938e+05, 3.54588375e+05, 3.36247656e+05, 3.18711375e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10435219e+05, 3.18711375e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99980300e+06, 3.99980300e+06, 3.99980300e+06, 3.99980300e+06, 3.99980300e+06, 3.99980300e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00010125e+05, 3.99898219e+05, 5.82091250e+05, 3.99904625e+05, 3.98976875e+05, 2.37833406e+05, ],
    'CountWeightedFull'                                                              : [ 3.99897500e+05, 3.99890875e+05, 3.99904562e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.10337375e+05, 4.84043719e+05, 4.58881625e+05, 4.21660375e+05, 3.99894188e+05, 3.79064281e+05, 3.54520250e+05, 3.36183188e+05, 3.18650250e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.10337375e+05, 3.18650250e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99903525e+06, 3.99903525e+06, 3.99903525e+06, 3.99903525e+06, 3.99903525e+06, 3.99903525e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99935688e+05, 3.99821344e+05, 5.81977750e+05, 3.99825062e+05, 3.98900125e+05, 2.37788531e+05, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     1740384317), # 1.74GB, avg file size 870.19MB
  ("fsize_db",                        23137065319), # 23.14GB, avg file size 1.10GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_11_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2WToLNu2J_node_12_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_12_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 399993, ],
    'CountWeighted'                                                                  : [ 3.99911625e+05, 3.99965812e+05, 3.99912594e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.09924375e+05, 4.84392312e+05, 4.59812969e+05, 4.21066562e+05, 3.99911625e+05, 3.79603688e+05, 3.53849438e+05, 3.36057438e+05, 3.18945844e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.09924375e+05, 3.18945812e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.48429625e+06, 1.48172375e+06, 2.09167825e+06, 1.48220000e+06, 1.41536275e+06, 8.83198375e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00199688e+05, 3.99808625e+05, 5.82094125e+05, 3.99633062e+05, 3.99442188e+05, 2.38132188e+05, ],
    'CountWeightedFull'                                                              : [ 3.99833469e+05, 3.99886406e+05, 3.99834625e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.09824250e+05, 4.84297438e+05, 4.59723094e+05, 4.20984000e+05, 3.99833469e+05, 3.79529625e+05, 3.53780062e+05, 3.35991562e+05, 3.18883375e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.09824281e+05, 3.18883375e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.48401400e+06, 1.48143475e+06, 2.09126350e+06, 1.48189862e+06, 1.41508275e+06, 8.83027188e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 4.00123750e+05, 3.99730750e+05, 5.81978750e+05, 3.99551750e+05, 3.99363188e+05, 2.38086125e+05, ],
  }),
  ("nof_tree_events",                 399993),
  ("nof_db_events",                   399993),
  ("fsize_local",                     1727739152), # 1.73GB, avg file size 863.87MB
  ("fsize_db",                        21463230841), # 21.46GB, avg file size 1.02GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_12_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2VLNu2J_node_cHHH0_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH0_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH0_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                                          : [ 399997, ],
    'CountWeighted'                                                                  : [ 3.76559438e+05, 3.76507281e+05, 3.76485250e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.35497719e+05, 4.27958625e+05, 4.22674438e+05, 3.85027688e+05, 3.76559438e+05, 3.69694250e+05, 3.41397750e+05, 3.32626531e+05, 3.25147062e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.51050031e+05, 3.17507750e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.76504750e+05, 3.76429938e+05, 5.45265562e+05, 3.76506250e+05, 3.76120938e+05, 2.24959797e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.56196562e+04, 2.56173730e+04, 3.71426641e+04, 2.56197891e+04, 2.56261758e+04, 1.53047520e+04, ],
    'CountWeightedFull'                                                              : [ 2.40798672e+04, 2.40822383e+04, 2.40800762e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.78529902e+04, 2.73704219e+04, 2.70322246e+04, 2.46255469e+04, 2.40798672e+04, 2.36443945e+04, 2.18343984e+04, 2.12733008e+04, 2.07946855e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.88482188e+04, 2.03062266e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.40802031e+04, 2.40759609e+04, 3.48727461e+04, 2.40803164e+04, 2.40540938e+04, 1.43876846e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.64232129e+03, 1.64202112e+03, 2.38085107e+03, 1.64229346e+03, 1.64290552e+03, 9.81234619e+02, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     1657118899), # 1.66GB, avg file size 828.56MB
  ("fsize_db",                        20383479586), # 20.38GB, avg file size 926.52MB
  ("use_it",                          True),
  ("xsection",                        0.00739245),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_cHHH0_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2VLNu2J_node_cHHH1_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH1_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH1_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 391398, ],
    'CountWeighted'                                                                  : [ 3.50875938e+05, 3.50816938e+05, 3.50919312e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.99755812e+05, 3.93300500e+05, 3.89024875e+05, 3.59025375e+05, 3.50866344e+05, 3.44484750e+05, 3.22106750e+05, 3.13275406e+05, 3.05874062e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.16798719e+05, 2.96644156e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.50811688e+05, 3.51004094e+05, 5.09112250e+05, 3.50976281e+05, 3.50461438e+05, 2.08973094e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.17042236e+04, 1.17100156e+04, 1.70052461e+04, 1.17077070e+04, 1.17097070e+04, 6.96811523e+03, ],
    'CountWeightedFull'                                                              : [ 1.04779844e+04, 1.04760762e+04, 1.04794805e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.19372852e+04, 1.17443477e+04, 1.16165215e+04, 1.07211133e+04, 1.04771484e+04, 1.02866426e+04, 9.61831348e+03, 9.35449512e+03, 9.13343555e+03, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.24464170e+04, 8.85787305e+03, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.04757783e+04, 1.04815293e+04, 1.52027520e+04, 1.04805762e+04, 1.04650742e+04, 6.24012207e+03, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.50514954e+02, 3.50688934e+02, 5.08848236e+02, 3.50611145e+02, 3.50139191e+02, 2.08515961e+02, ],
  }),
  ("nof_tree_events",                 391398),
  ("nof_db_events",                   391398),
  ("fsize_local",                     1673267758), # 1.67GB, avg file size 836.63MB
  ("fsize_db",                        20213187246), # 20.21GB, avg file size 962.53MB
  ("use_it",                          True),
  ("xsection",                        0.00329167),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_cHHH1_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2VLNu2J_node_cHHH2p45_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH2p45_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH2p45_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    25),
  ("nof_events",                      {
    'Count'                                                                          : [ 383096, ],
    'CountWeighted'                                                                  : [ 3.30007750e+05, 3.29942531e+05, 3.29995438e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.76196906e+05, 3.70997875e+05, 3.67679938e+05, 3.36689594e+05, 3.29998469e+05, 3.24737062e+05, 3.01451750e+05, 2.94047656e+05, 2.87810344e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.96198688e+05, 2.75587500e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.30034719e+05, 3.30074406e+05, 4.79314562e+05, 3.29910844e+05, 3.29615188e+05, 1.96028312e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 5.04543262e+03, 5.04635400e+03, 7.32903027e+03, 5.04447559e+03, 5.04580029e+03, 3.00257861e+03, ],
    'CountWeightedFull'                                                              : [ 4.32752148e+03, 4.32708057e+03, 4.32731348e+03, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.93359814e+03, 4.86527832e+03, 4.82166211e+03, 4.41547754e+03, 4.32729297e+03, 4.25853711e+03, 3.95323438e+03, 3.85605151e+03, 3.77420508e+03, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.19594434e+03, 3.61394409e+03, ],
    'CountWeightedFullPSWeight'                                                      : [ 4.32815039e+03, 4.32847070e+03, 6.28574121e+03, 4.32647168e+03, 4.32276562e+03, 2.57079443e+03, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 6.66647491e+01, 6.66768036e+01, 9.66628189e+01, 6.66490021e+01, 6.66374512e+01, 3.97979736e+01, ],
  }),
  ("nof_tree_events",                 383096),
  ("nof_db_events",                   383096),
  ("fsize_local",                     1634706163), # 1.63GB, avg file size 817.35MB
  ("fsize_db",                        19867289750), # 19.87GB, avg file size 794.69MB
  ("use_it",                          True),
  ("xsection",                        0.00139143),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_cHHH2p45_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2VLNu2J_node_cHHH5_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH5_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH5_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 390197, ],
    'CountWeighted'                                                                  : [ 3.84086688e+05, 3.84107156e+05, 3.84136750e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.60177375e+05, 4.51495500e+05, 4.44802875e+05, 3.91781938e+05, 3.84082406e+05, 3.77623375e+05, 3.37329625e+05, 3.30554406e+05, 3.24421312e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.74108531e+05, 3.17930125e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.84176531e+05, 3.83974375e+05, 5.56259250e+05, 3.84072656e+05, 3.83915250e+05, 2.29597062e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.13190547e+04, 3.13045078e+04, 4.54057070e+04, 3.13111992e+04, 3.13572773e+04, 1.87214277e+04, ],
    'CountWeightedFull'                                                              : [ 3.08044531e+04, 3.08085898e+04, 3.08042441e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.69074375e+04, 3.62104453e+04, 3.56733086e+04, 3.14216680e+04, 3.08038516e+04, 3.02852305e+04, 2.70537891e+04, 2.65099766e+04, 2.60177559e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.80247422e+04, 2.54972422e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.08114492e+04, 3.07949941e+04, 4.46117617e+04, 3.08027109e+04, 3.07895547e+04, 1.84137734e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.51498120e+03, 2.51379102e+03, 3.64501221e+03, 2.51414014e+03, 2.51778979e+03, 1.50410461e+03, ],
  }),
  ("nof_tree_events",                 390197),
  ("nof_db_events",                   390197),
  ("fsize_local",                     1494687077), # 1.49GB, avg file size 747.34MB
  ("fsize_db",                        19251007287), # 19.25GB, avg file size 916.71MB
  ("use_it",                          True),
  ("xsection",                        0.00966639),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_cHHH5_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2WToLNu2J_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_250_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_250_hh_2b2v_sl"),
  ("nof_files",                       3),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                                          : [ 399995, ],
    'CountWeighted'                                                                  : [ 3.99928688e+05, 3.99955781e+05, 3.99959562e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99928688e+05, 3.99928688e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99966675e+06, 3.99967625e+06, 3.99967625e+06, 3.99966775e+06, 3.99967625e+06, 3.99966675e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00079875e+05, 4.00088281e+05, 5.77926875e+05, 3.99881094e+05, 3.99623875e+05, 2.42121203e+05, ],
    'CountWeightedFull'                                                              : [ 3.99858688e+05, 3.99885219e+05, 3.99888438e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99858688e+05, 3.99858688e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99896525e+06, 3.99896525e+06, 3.99896525e+06, 3.99896525e+06, 3.99896525e+06, 3.99896525e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 4.00012281e+05, 4.00017594e+05, 5.77823438e+05, 3.99809281e+05, 3.99552688e+05, 2.42079328e+05, ],
  }),
  ("nof_tree_events",                 399995),
  ("nof_db_events",                   399995),
  ("fsize_local",                     1383718952), # 1.38GB, avg file size 461.24MB
  ("fsize_db",                        22058910739), # 22.06GB, avg file size 1.00GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_250_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2WToLNu2J_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_260_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_260_hh_2b2v_sl"),
  ("nof_files",                       3),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 399998, ],
    'CountWeighted'                                                                  : [ 3.99940625e+05, 3.99948688e+05, 3.99878375e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.06192094e+05, 3.99934969e+05, 3.91112562e+05, 4.06192094e+05, 3.99934969e+05, 3.91112562e+05, 4.06192094e+05, 3.99934969e+05, 3.91112562e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.06192094e+05, 3.91112562e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99355925e+06, 1.98457750e+06, 2.71783925e+06, 1.99525888e+06, 1.83700575e+06, 1.20568638e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99796094e+05, 3.99925938e+05, 5.78482938e+05, 4.00148938e+05, 3.99902469e+05, 2.41791844e+05, ],
    'CountWeightedFull'                                                              : [ 3.99868750e+05, 3.99876469e+05, 3.99808031e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.06119688e+05, 3.99863125e+05, 3.91043000e+05, 4.06119688e+05, 3.99863125e+05, 3.91043000e+05, 4.06119688e+05, 3.99863125e+05, 3.91043000e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.06119688e+05, 3.91042969e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.99321488e+06, 1.98422862e+06, 2.71735500e+06, 1.99489275e+06, 1.83667812e+06, 1.20547438e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99726969e+05, 3.99855562e+05, 5.78379125e+05, 4.00075656e+05, 3.99830188e+05, 2.41749281e+05, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     1393823463), # 1.39GB, avg file size 464.61MB
  ("fsize_db",                        21381399216), # 21.38GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_260_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2WToLNu2J_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_270_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_270_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 399996, ],
    'CountWeighted'                                                                  : [ 3.99946375e+05, 3.99931188e+05, 3.99907969e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.07474938e+05, 3.99939750e+05, 3.90118312e+05, 4.07474938e+05, 3.99939750e+05, 3.90118312e+05, 4.07474938e+05, 3.99939750e+05, 3.90118312e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.07474938e+05, 3.90118312e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.48530838e+06, 1.48432025e+06, 2.08407400e+06, 1.48566538e+06, 1.42089950e+06, 8.97351562e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99932094e+05, 3.99857938e+05, 5.78254938e+05, 4.00024094e+05, 3.99501750e+05, 2.41624062e+05, ],
    'CountWeightedFull'                                                              : [ 3.99875188e+05, 3.99859875e+05, 3.99837000e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.07402375e+05, 3.99868625e+05, 3.90048750e+05, 4.07402375e+05, 3.99868625e+05, 3.90048750e+05, 4.07402375e+05, 3.99868625e+05, 3.90048750e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.07402375e+05, 3.90048750e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.48505362e+06, 1.48405925e+06, 2.08369950e+06, 1.48539638e+06, 1.42064125e+06, 8.97194125e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99863500e+05, 3.99787688e+05, 5.78151375e+05, 3.99951562e+05, 3.99429281e+05, 2.41581625e+05, ],
  }),
  ("nof_tree_events",                 399996),
  ("nof_db_events",                   399996),
  ("fsize_local",                     1416208956), # 1.42GB, avg file size 708.10MB
  ("fsize_db",                        21536125803), # 21.54GB, avg file size 1.13GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_270_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2WToLNu2J_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_280_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_280_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 399997, ],
    'CountWeighted'                                                                  : [ 3.99877188e+05, 3.99881469e+05, 3.99859750e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99877188e+05, 3.99877188e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.70048675e+06, 1.69662700e+06, 2.35921475e+06, 1.69945888e+06, 1.60184138e+06, 1.02638175e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00009375e+05, 3.99743562e+05, 5.78295188e+05, 3.99767438e+05, 3.99494469e+05, 2.41439016e+05, ],
    'CountWeightedFull'                                                              : [ 3.99805344e+05, 3.99810188e+05, 3.99787906e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99805344e+05, 3.99805344e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.70019050e+06, 1.69632112e+06, 2.35879250e+06, 1.69914662e+06, 1.60155825e+06, 1.02619988e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99939688e+05, 3.99671562e+05, 5.78192062e+05, 3.99694250e+05, 3.99424156e+05, 2.41396266e+05, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     1447838289), # 1.45GB, avg file size 723.92MB
  ("fsize_db",                        21876567017), # 21.88GB, avg file size 1.37GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_280_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2WToLNu2J_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_300_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_300_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 299997, ],
    'CountWeighted'                                                                  : [ 2.99923438e+05, 2.99958000e+05, 2.99922844e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.08224188e+05, 2.99923438e+05, 2.90502375e+05, 3.08224188e+05, 2.99923438e+05, 2.90502375e+05, 3.08224188e+05, 2.99923438e+05, 2.90502375e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.08224250e+05, 2.90502281e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.07898388e+06, 1.07738875e+06, 1.51845962e+06, 1.07911400e+06, 1.03601025e+06, 6.50412250e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99956906e+05, 2.99660406e+05, 4.34084844e+05, 2.99996531e+05, 2.99817312e+05, 1.80816609e+05, ],
    'CountWeightedFull'                                                              : [ 2.99871531e+05, 2.99905469e+05, 2.99870594e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.08170125e+05, 2.99871531e+05, 2.90451344e+05, 3.08170125e+05, 2.99871531e+05, 2.90451344e+05, 3.08170125e+05, 2.99871531e+05, 2.90451344e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.08170188e+05, 2.90451281e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.07879925e+06, 1.07720250e+06, 1.51819338e+06, 1.07891925e+06, 1.03582719e+06, 6.50298312e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99905594e+05, 2.99608562e+05, 4.34008250e+05, 2.99942500e+05, 2.99764125e+05, 1.80784984e+05, ],
  }),
  ("nof_tree_events",                 299997),
  ("nof_db_events",                   299997),
  ("fsize_local",                     1111999598), # 1.11GB, avg file size 556.00MB
  ("fsize_db",                        16041315443), # 16.04GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_300_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2WToLNu2J_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_320_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_320_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 299999, ],
    'CountWeighted'                                                                  : [ 2.99989062e+05, 2.99982281e+05, 2.99957156e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.09815531e+05, 2.99989062e+05, 2.89279812e+05, 3.09815531e+05, 2.99989062e+05, 2.89279812e+05, 3.09815531e+05, 2.99989062e+05, 2.89279812e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.09815531e+05, 2.89279812e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.86885875e+05, 9.86812812e+05, 1.39697550e+06, 9.86256312e+05, 9.52610125e+05, 5.93198562e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.00070031e+05, 3.00117281e+05, 4.34427938e+05, 2.99878562e+05, 2.99246938e+05, 1.80367219e+05, ],
    'CountWeightedFull'                                                              : [ 2.99933188e+05, 2.99926594e+05, 2.99901750e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.09758312e+05, 2.99933188e+05, 2.89226250e+05, 3.09758312e+05, 2.99933188e+05, 2.89226250e+05, 3.09758312e+05, 2.99933188e+05, 2.89226250e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.09758312e+05, 2.89226250e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.86711625e+05, 9.86632812e+05, 1.39671662e+06, 9.86071375e+05, 9.52430500e+05, 5.93091000e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.00016875e+05, 3.00062531e+05, 4.34346938e+05, 2.99822469e+05, 2.99190344e+05, 1.80334469e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1146172110), # 1.15GB, avg file size 573.09MB
  ("fsize_db",                        16244875503), # 16.24GB, avg file size 955.58MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_320_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2WToLNu2J_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_350_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_350_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 299997, ],
    'CountWeighted'                                                                  : [ 2.99976500e+05, 2.99966312e+05, 2.99999062e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.11970500e+05, 2.99976500e+05, 2.87621938e+05, 3.11970500e+05, 2.99976500e+05, 2.87621938e+05, 3.11970500e+05, 2.99976500e+05, 2.87621938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.11970500e+05, 2.87621938e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.15455938e+05, 9.16819125e+05, 1.30289600e+06, 9.16267000e+05, 8.87269250e+05, 5.48701125e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99864969e+05, 3.00368594e+05, 4.35115938e+05, 3.00131500e+05, 2.98915375e+05, 1.79731562e+05, ],
    'CountWeightedFull'                                                              : [ 2.99921156e+05, 2.99910562e+05, 2.99943219e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.11913031e+05, 2.99921156e+05, 2.87568656e+05, 3.11913031e+05, 2.99921156e+05, 2.87568656e+05, 3.11913031e+05, 2.99921156e+05, 2.87568656e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.11913031e+05, 2.87568656e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.15292250e+05, 9.16653562e+05, 1.30265388e+06, 9.16094625e+05, 8.87100625e+05, 5.48600938e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99811469e+05, 3.00314312e+05, 4.35034875e+05, 3.00075062e+05, 2.98858531e+05, 1.79698734e+05, ],
  }),
  ("nof_tree_events",                 299997),
  ("nof_db_events",                   299997),
  ("fsize_local",                     1192315498), # 1.19GB, avg file size 596.16MB
  ("fsize_db",                        16512381924), # 16.51GB, avg file size 1.10GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_350_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2WToLNu2J_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_400_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_400_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 299998, ],
    'CountWeighted'                                                                  : [ 2.99921469e+05, 2.99921219e+05, 2.99955750e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.15093625e+05, 2.99921469e+05, 2.85245562e+05, 3.15093625e+05, 2.99921469e+05, 2.85245562e+05, 3.15093625e+05, 2.99921469e+05, 2.85245562e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.15093688e+05, 2.85245500e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.64873812e+05, 8.64993938e+05, 1.23707475e+06, 8.65575250e+05, 8.43368938e+05, 5.16515062e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99881438e+05, 2.99954062e+05, 4.36823250e+05, 3.00123562e+05, 3.00279906e+05, 1.79093078e+05, ],
    'CountWeightedFull'                                                              : [ 2.99865438e+05, 2.99865281e+05, 2.99899750e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.15034344e+05, 2.99865438e+05, 2.85191938e+05, 3.15034344e+05, 2.99865438e+05, 2.85191938e+05, 3.15034344e+05, 2.99865438e+05, 2.85191938e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.15034406e+05, 2.85191875e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 8.64715750e+05, 8.64831500e+05, 1.23683900e+06, 8.65406375e+05, 8.43208625e+05, 5.16419125e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99826406e+05, 2.99897844e+05, 4.36740000e+05, 3.00064969e+05, 3.00223188e+05, 1.79059812e+05, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1259877616), # 1.26GB, avg file size 629.94MB
  ("fsize_db",                        16931027309), # 16.93GB, avg file size 940.61MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_400_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2WToLNu2J_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_450_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_450_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 299998, ],
    'CountWeighted'                                                                  : [ 2.99967188e+05, 2.99955875e+05, 2.99955344e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.17760625e+05, 2.99959312e+05, 2.83223781e+05, 3.17760625e+05, 2.99959312e+05, 2.83223781e+05, 3.17760625e+05, 2.99959312e+05, 2.83223781e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.17760875e+05, 2.83223750e+05, ],
    'CountWeightedPSWeight'                                                          : [ 6.35899000e+05, 6.36036875e+05, 9.19144750e+05, 6.35485938e+05, 6.27810750e+05, 3.78028750e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.00062656e+05, 3.00132062e+05, 4.36967312e+05, 2.99868188e+05, 2.99487875e+05, 1.78379844e+05, ],
    'CountWeightedFull'                                                              : [ 2.99909062e+05, 2.99898188e+05, 2.99897469e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.17699406e+05, 2.99901125e+05, 2.83169344e+05, 3.17699406e+05, 2.99901125e+05, 2.83169344e+05, 3.17699406e+05, 2.99901125e+05, 2.83169344e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.17699656e+05, 2.83169312e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 6.35781000e+05, 6.35915625e+05, 9.18965188e+05, 6.35358875e+05, 6.27687688e+05, 3.77956438e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.00006875e+05, 3.00074938e+05, 4.36881688e+05, 2.99808250e+05, 2.99428906e+05, 1.78345750e+05, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1317064837), # 1.32GB, avg file size 658.53MB
  ("fsize_db",                        17783509618), # 17.78GB, avg file size 987.97MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_450_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2WToLNu2J_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_500_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_500_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 299996, ],
    'CountWeighted'                                                                  : [ 2.99942750e+05, 2.99942969e+05, 2.99943188e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.20057938e+05, 2.99942750e+05, 2.81449500e+05, 3.20057938e+05, 2.99942750e+05, 2.81449500e+05, 3.20057938e+05, 2.99942750e+05, 2.81449500e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.20057938e+05, 2.81449500e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.45360375e+05, 8.44158562e+05, 1.21291650e+06, 8.44740000e+05, 8.25556438e+05, 5.01339188e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.00078562e+05, 2.99679938e+05, 4.37883062e+05, 2.99857406e+05, 3.00356500e+05, 1.77962625e+05, ],
    'CountWeightedFull'                                                              : [ 2.99883312e+05, 2.99883688e+05, 2.99883562e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.19994188e+05, 2.99883312e+05, 2.81393312e+05, 3.19994188e+05, 2.99883312e+05, 2.81393312e+05, 3.19994188e+05, 2.99883312e+05, 2.81393312e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.19994188e+05, 2.81393281e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 8.45196750e+05, 8.43991750e+05, 1.21267125e+06, 8.44565625e+05, 8.25389500e+05, 5.01240812e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.00020719e+05, 2.99620625e+05, 4.37794375e+05, 2.99795438e+05, 3.00295531e+05, 1.77927719e+05, ],
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     1368060503), # 1.37GB, avg file size 684.03MB
  ("fsize_db",                        16531068338), # 16.53GB, avg file size 870.06MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_500_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2WToLNu2J_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_550_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_550_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 257999, ],
    'CountWeighted'                                                                  : [ 2.57974875e+05, 2.57959312e+05, 2.57944609e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.77001125e+05, 2.57974875e+05, 2.40700406e+05, 2.77001125e+05, 2.57974875e+05, 2.40700406e+05, 2.77001125e+05, 2.57974875e+05, 2.40700406e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.77001125e+05, 2.40700406e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.15398188e+05, 9.14911000e+05, 1.29661225e+06, 9.15055500e+05, 8.74786312e+05, 5.41474125e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.58014891e+05, 2.58016094e+05, 3.76410625e+05, 2.57912734e+05, 2.57376344e+05, 1.52620562e+05, ],
    'CountWeightedFull'                                                              : [ 2.57922188e+05, 2.57906672e+05, 2.57892500e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.76944719e+05, 2.57922188e+05, 2.40651375e+05, 2.76944719e+05, 2.57922188e+05, 2.40651375e+05, 2.76944719e+05, 2.57922188e+05, 2.40651375e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.76944719e+05, 2.40651375e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.15219500e+05, 9.14725625e+05, 1.29634875e+06, 9.14865312e+05, 8.74609000e+05, 5.41365500e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.57964531e+05, 2.57963688e+05, 3.76334250e+05, 2.57859094e+05, 2.57324531e+05, 1.52589812e+05, ],
  }),
  ("nof_tree_events",                 257999),
  ("nof_db_events",                   257999),
  ("fsize_local",                     1216105921), # 1.22GB, avg file size 608.05MB
  ("fsize_db",                        14331323976), # 14.33GB, avg file size 1.10GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_550_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2WToLNu2J_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_600_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_600_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 199998, ],
    'CountWeighted'                                                                  : [ 1.99952062e+05, 1.99965328e+05, 1.99969375e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.15938969e+05, 1.99952062e+05, 1.85648453e+05, 2.15938969e+05, 1.99952062e+05, 1.85648453e+05, 2.15938969e+05, 1.99952062e+05, 1.85648453e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.15938969e+05, 1.85648453e+05, ],
    'CountWeightedPSWeight'                                                          : [ 7.20094875e+05, 7.19364188e+05, 1.02245056e+06, 7.20700625e+05, 6.89162688e+05, 4.24243188e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99906312e+05, 1.99838266e+05, 2.92935000e+05, 2.00076391e+05, 2.00277109e+05, 1.17774758e+05, ],
    'CountWeightedFull'                                                              : [ 1.99908000e+05, 1.99921172e+05, 1.99924656e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.15890953e+05, 1.99908000e+05, 1.85607281e+05, 2.15890953e+05, 1.99908000e+05, 1.85607281e+05, 2.15890953e+05, 1.99908000e+05, 1.85607281e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.15890953e+05, 1.85607281e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 7.19946625e+05, 7.19206812e+05, 1.02222225e+06, 7.20541062e+05, 6.89007625e+05, 4.24153625e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99865000e+05, 1.99794594e+05, 2.92869344e+05, 2.00032281e+05, 2.00231953e+05, 1.17749883e+05, ],
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     965540084), # 965.54MB, avg file size 965.54MB
  ("fsize_db",                        11343834815), # 11.34GB, avg file size 810.27MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_600_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2WToLNu2J_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_650_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_650_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 199997, ],
    'CountWeighted'                                                                  : [ 1.99940391e+05, 1.99924484e+05, 1.99918047e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.17017531e+05, 1.99938656e+05, 1.84782328e+05, 2.17017531e+05, 1.99938656e+05, 1.84782328e+05, 2.17017531e+05, 1.99938656e+05, 1.84782328e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.17017531e+05, 1.84782328e+05, ],
    'CountWeightedPSWeight'                                                          : [ 4.39839219e+05, 4.39592969e+05, 6.37912375e+05, 4.39487531e+05, 4.33488625e+05, 2.58744922e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.00029156e+05, 1.99917609e+05, 2.92833312e+05, 1.99870188e+05, 1.99870391e+05, 1.17676164e+05, ],
    'CountWeightedFull'                                                              : [ 1.99899031e+05, 1.99883438e+05, 1.99877172e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.16972547e+05, 1.99897281e+05, 1.84744156e+05, 2.16972547e+05, 1.99897281e+05, 1.84744156e+05, 2.16972547e+05, 1.99897281e+05, 1.84744156e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.16972547e+05, 1.84744156e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 4.39751531e+05, 4.39503219e+05, 6.37780062e+05, 4.39393250e+05, 4.33398281e+05, 2.58691516e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99989312e+05, 1.99876688e+05, 2.92772625e+05, 1.99827250e+05, 1.99828656e+05, 1.17651891e+05, ],
  }),
  ("nof_tree_events",                 199997),
  ("nof_db_events",                   199997),
  ("fsize_local",                     983257939), # 983.26MB, avg file size 983.26MB
  ("fsize_db",                        12597153145), # 12.60GB, avg file size 629.86MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_650_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2WToLNu2J_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_700_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_700_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 199999, ],
    'CountWeighted'                                                                  : [ 1.99955656e+05, 1.99977766e+05, 1.99963859e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.18038984e+05, 1.99955656e+05, 1.84069125e+05, 2.18038984e+05, 1.99955656e+05, 1.84069125e+05, 2.18038984e+05, 1.99955656e+05, 1.84069125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.18039078e+05, 1.84069031e+05, ],
    'CountWeightedPSWeight'                                                          : [ 7.54130438e+05, 7.51968625e+05, 1.06647912e+06, 7.54318375e+05, 7.16916938e+05, 4.43194781e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99972844e+05, 1.99578625e+05, 2.92545812e+05, 2.00024625e+05, 1.99676859e+05, 1.17523203e+05, ],
    'CountWeightedFull'                                                              : [ 1.99912734e+05, 1.99934125e+05, 1.99920781e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.17991828e+05, 1.99912734e+05, 1.84029219e+05, 2.17991828e+05, 1.99912734e+05, 1.84029219e+05, 2.17991828e+05, 1.99912734e+05, 1.84029219e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.17991906e+05, 1.84029141e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 7.53978125e+05, 7.51810188e+05, 1.06624700e+06, 7.54156125e+05, 7.16757062e+05, 4.43104281e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99932734e+05, 1.99536594e+05, 2.92481688e+05, 1.99981609e+05, 1.99632141e+05, 1.17499188e+05, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     997710291), # 997.71MB, avg file size 997.71MB
  ("fsize_db",                        11558773806), # 11.56GB, avg file size 963.23MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_700_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2WToLNu2J_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_750_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_750_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 199999, ],
    'CountWeighted'                                                                  : [ 1.99957406e+05, 1.99968688e+05, 1.99953297e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99957406e+05, 1.99957406e+05, ],
    'CountWeightedPSWeight'                                                          : [ 4.64373844e+05, 4.65077938e+05, 6.72841812e+05, 4.64105219e+05, 4.54645719e+05, 2.71854938e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.00044219e+05, 2.00348109e+05, 2.92838156e+05, 1.99921906e+05, 1.98841141e+05, 1.17106023e+05, ],
    'CountWeightedFull'                                                              : [ 1.99913953e+05, 1.99925188e+05, 1.99910375e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99913953e+05, 1.99913953e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 4.64278031e+05, 4.64977688e+05, 6.72695125e+05, 4.64001344e+05, 4.54547844e+05, 2.71797750e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.00002891e+05, 2.00304875e+05, 2.92774156e+05, 1.99877234e+05, 1.98798234e+05, 1.17081328e+05, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     1015454906), # 1.02GB, avg file size 507.73MB
  ("fsize_db",                        13168839827), # 13.17GB, avg file size 658.44MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_750_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2WToLNu2J_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_800_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_800_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 199998, ],
    'CountWeighted'                                                                  : [ 1.99958156e+05, 1.99960266e+05, 1.99957219e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99958156e+05, 1.99958156e+05, ],
    'CountWeightedPSWeight'                                                          : [ 4.79376375e+05, 4.78975375e+05, 6.95047562e+05, 4.79343531e+05, 4.70363125e+05, 2.80364406e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99991281e+05, 1.99837750e+05, 2.93298875e+05, 1.99982859e+05, 1.99558453e+05, 1.16972406e+05, ],
    'CountWeightedFull'                                                              : [ 1.99914484e+05, 1.99916500e+05, 1.99913609e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99914484e+05, 1.99914484e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 4.79275188e+05, 4.78871062e+05, 6.94894625e+05, 4.79234844e+05, 4.70259969e+05, 2.80303625e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99949062e+05, 1.99794219e+05, 2.93233781e+05, 1.99937453e+05, 1.99514250e+05, 1.16947125e+05, ],
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     1022566363), # 1.02GB, avg file size 511.28MB
  ("fsize_db",                        13271821657), # 13.27GB, avg file size 631.99MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_800_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2WToLNu2J_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_850_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_850_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 199998, ],
    'CountWeighted'                                                                  : [ 1.99953219e+05, 1.99958125e+05, 1.99975281e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99953219e+05, 1.99953219e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.29473438e+05, 8.29421000e+05, 1.16626075e+06, 8.30219062e+05, 7.75252875e+05, 4.83740969e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99909906e+05, 2.00295984e+05, 2.93511312e+05, 2.00088125e+05, 1.98877141e+05, 1.16584961e+05, ],
    'CountWeightedFull'                                                              : [ 1.99909562e+05, 1.99914344e+05, 1.99931688e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99909562e+05, 1.99909562e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 8.29297312e+05, 8.29238875e+05, 1.16600500e+06, 8.30029750e+05, 7.75084500e+05, 4.83636188e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99867406e+05, 2.00252094e+05, 2.93446750e+05, 2.00042625e+05, 1.98834062e+05, 1.16559680e+05, ],
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     1029966370), # 1.03GB, avg file size 514.98MB
  ("fsize_db",                        12193797346), # 12.19GB, avg file size 1.22GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_850_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2WToLNu2J_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_900_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_900_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 199999, ],
    'CountWeighted'                                                                  : [ 1.99961312e+05, 1.99926359e+05, 1.99933406e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.21303891e+05, 1.99960984e+05, 1.81619141e+05, 2.21303891e+05, 1.99960984e+05, 1.81619141e+05, 2.21303891e+05, 1.99960984e+05, 1.81619141e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.21303266e+05, 1.81619203e+05, ],
    'CountWeightedPSWeight'                                                          : [ 5.15235312e+05, 5.14892344e+05, 7.45125188e+05, 5.14735062e+05, 5.02299875e+05, 3.00272031e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.00063812e+05, 1.99942766e+05, 2.93510844e+05, 1.99872156e+05, 1.99212547e+05, 1.16596094e+05, ],
    'CountWeightedFull'                                                              : [ 1.99916641e+05, 1.99881984e+05, 1.99889031e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.21254500e+05, 1.99916281e+05, 1.81578500e+05, 2.21254500e+05, 1.99916281e+05, 1.81578500e+05, 2.21254500e+05, 1.99916281e+05, 1.81578500e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.21253875e+05, 1.81578531e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 5.15124062e+05, 5.14777125e+05, 7.44957062e+05, 5.14615812e+05, 5.02188375e+05, 3.00206375e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.00020516e+05, 1.99897891e+05, 2.93444688e+05, 1.99825781e+05, 1.99168219e+05, 1.16570547e+05, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     1026794094), # 1.03GB, avg file size 1.03GB
  ("fsize_db",                        13081114484), # 13.08GB, avg file size 1.45GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_900_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2WToLNu2J_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1000_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_1000_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99649688e+04, 9.99675000e+04, 9.99693125e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.11331125e+05, 9.99649688e+04, 9.03191250e+04, 1.11331125e+05, 9.99649688e+04, 9.03191250e+04, 1.11331125e+05, 9.99649688e+04, 9.03191250e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.11331125e+05, 9.03191250e+04, ],
    'CountWeightedPSWeight'                                                          : [ 3.73075188e+05, 3.72802375e+05, 5.29989938e+05, 3.73156281e+05, 3.53356812e+05, 2.16635750e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99809766e+04, 1.00001820e+05, 1.47354750e+05, 1.00000734e+05, 9.99248594e+04, 5.80571172e+04, ],
    'CountWeightedFull'                                                              : [ 9.99417344e+04, 9.99444531e+04, 9.99457031e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.11305164e+05, 9.99417344e+04, 9.02981250e+04, 1.11305164e+05, 9.99417344e+04, 9.02981250e+04, 1.11305164e+05, 9.99417344e+04, 9.02981250e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.11305164e+05, 9.02981250e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.72991438e+05, 3.72714812e+05, 5.29865312e+05, 3.73065562e+05, 3.53275125e+05, 2.16586203e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99584453e+04, 9.99783516e+04, 1.47319750e+05, 9.99764453e+04, 9.99014141e+04, 5.80438438e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     519227526), # 519.23MB, avg file size 519.23MB
  ("fsize_db",                        6078455015), # 6.08GB, avg file size 675.38MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_1000_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2WToLNu2J_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1250_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_1250_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 9.99503281e+04, 9.99595781e+04, 9.99466172e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99503281e+04, 9.99503281e+04, ],
    'CountWeightedPSWeight'                                                          : [ 3.48698750e+05, 3.49241312e+05, 4.98420625e+05, 3.49208500e+05, 3.30899000e+05, 2.01314031e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99315938e+04, 1.00151609e+05, 1.47385734e+05, 1.00070266e+05, 9.93200312e+04, 5.76931445e+04, ],
    'CountWeightedFull'                                                              : [ 9.99267812e+04, 9.99359531e+04, 9.99228594e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99267812e+04, 9.99267812e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.48619562e+05, 3.49160188e+05, 4.98302406e+05, 3.49123000e+05, 3.30820125e+05, 2.01267281e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99089062e+04, 1.00128422e+05, 1.47350344e+05, 1.00045828e+05, 9.92960781e+04, 5.76798203e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     525797636), # 525.80MB, avg file size 525.80MB
  ("fsize_db",                        6906320482), # 6.91GB, avg file size 1.38GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_1250_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2WToLNu2J_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1500_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_1500_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 99998, ],
    'CountWeighted'                                                                  : [ 9.99560703e+04, 9.99457734e+04, 9.99621719e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.13891805e+05, 9.99540703e+04, 8.85218750e+04, 1.13891805e+05, 9.99540703e+04, 8.85218750e+04, 1.13891805e+05, 9.99540703e+04, 8.85218750e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.13892188e+05, 8.85214688e+04, ],
    'CountWeightedPSWeight'                                                          : [ 6.03788562e+05, 5.90964188e+05, 8.00000625e+05, 6.02784625e+05, 5.21667688e+05, 3.46217656e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00057812e+05, 1.00192516e+05, 1.48104453e+05, 9.99062188e+04, 9.97115234e+04, 5.73766016e+04, ],
    'CountWeightedFull'                                                              : [ 9.99314688e+04, 9.99212109e+04, 9.99372188e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.13863625e+05, 9.99294062e+04, 8.84999453e+04, 1.13863625e+05, 9.99294062e+04, 8.84999453e+04, 1.13863625e+05, 9.99294062e+04, 8.84999453e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.13864008e+05, 8.84995547e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 6.03645062e+05, 5.90820062e+05, 7.99801250e+05, 6.02629375e+05, 5.21536844e+05, 3.46132812e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.00034008e+05, 1.00167906e+05, 1.48067062e+05, 9.98804141e+04, 9.96863594e+04, 5.73625352e+04, ],
  }),
  ("nof_tree_events",                 99998),
  ("nof_db_events",                   99998),
  ("fsize_local",                     517486598), # 517.49MB, avg file size 517.49MB
  ("fsize_db",                        6245064826), # 6.25GB, avg file size 693.90MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_1500_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2WToLNu2J_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1750_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_1750_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 9.99283750e+04, 9.99317656e+04, 9.99284531e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99283750e+04, 9.99283750e+04, ],
    'CountWeightedPSWeight'                                                          : [ 7.89116312e+05, 7.32078750e+05, 9.48121750e+05, 7.85905062e+05, 6.27855750e+05, 4.52432594e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99432812e+04, 1.00175406e+05, 1.47887562e+05, 1.00014484e+05, 9.92003672e+04, 5.71791523e+04, ],
    'CountWeightedFull'                                                              : [ 9.98993281e+04, 9.99033125e+04, 9.98991016e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.98993281e+04, 9.98993281e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 7.88915500e+05, 7.31873125e+05, 9.47845688e+05, 7.85689312e+05, 6.27670625e+05, 4.52313688e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99178594e+04, 1.00147031e+05, 1.47840875e+05, 9.99868750e+04, 9.91675156e+04, 5.71640664e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     519013169), # 519.01MB, avg file size 519.01MB
  ("fsize_db",                        6519894990), # 6.52GB, avg file size 651.99MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_1750_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2WToLNu2J_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_2000_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_2000_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 9.99170547e+04, 9.99164297e+04, 9.99221719e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.15688633e+05, 9.99170547e+04, 8.71994375e+04, 1.15688633e+05, 9.99170547e+04, 8.71994375e+04, 1.15688633e+05, 9.99170547e+04, 8.71994375e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.15689469e+05, 8.71985859e+04, ],
    'CountWeightedPSWeight'                                                          : [ 5.26353500e+05, 5.20309250e+05, 7.19099375e+05, 5.26073625e+05, 4.69353406e+05, 3.00521688e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00000422e+05, 9.99405781e+04, 1.48000219e+05, 9.99522266e+04, 9.94670469e+04, 5.71020234e+04, ],
    'CountWeightedFull'                                                              : [ 9.98897500e+04, 9.98888672e+04, 9.98941406e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.15656672e+05, 9.98897500e+04, 8.71754531e+04, 1.15656672e+05, 9.98897500e+04, 8.71754531e+04, 1.15656672e+05, 9.98897500e+04, 8.71754531e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.15657500e+05, 8.71746016e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 5.26214875e+05, 5.20168312e+05, 7.18899375e+05, 5.25925875e+05, 4.69220938e+05, 3.00439812e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99740781e+04, 9.99134844e+04, 1.47959031e+05, 9.99241875e+04, 9.94390078e+04, 5.70864844e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     515078174), # 515.08MB, avg file size 515.08MB
  ("fsize_db",                        7295615609), # 7.30GB, avg file size 1.04GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_2000_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2WToLNu2J_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_2500_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_2500_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.98462656e+04, 9.98565781e+04, 9.98363047e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.98462656e+04, 9.98462656e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.93098438e+05, 9.38071375e+05, 9.95104500e+05, 9.92080125e+05, 8.35749562e+05, 7.78415688e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00013141e+05, 1.00001516e+05, 1.48743141e+05, 9.99443906e+04, 9.98173516e+04, 5.68095586e+04, ],
    'CountWeightedFull'                                                              : [ 9.98168906e+04, 9.98274062e+04, 9.98073594e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.98168906e+04, 9.98168906e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.92815438e+05, 9.37796875e+05, 9.94811812e+05, 9.91797125e+05, 8.35506062e+05, 7.78199875e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99858281e+04, 9.99722812e+04, 1.48698938e+05, 9.99147578e+04, 9.97876250e+04, 5.67937617e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     517150661), # 517.15MB, avg file size 517.15MB
  ("fsize_db",                        6648523383), # 6.65GB, avg file size 831.07MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_2500_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2WToLNu2J_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_3000_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_3000_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 99998, ],
    'CountWeighted'                                                                  : [ 9.97671797e+04, 9.97706250e+04, 9.97468359e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.97671797e+04, 9.97671797e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.96653188e+05, 9.91557062e+05, 9.97602562e+05, 9.96572375e+05, 9.58087500e+05, 9.52301375e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99413594e+04, 1.00050141e+05, 1.48393078e+05, 1.00017898e+05, 9.93910547e+04, 5.68321172e+04, ],
    'CountWeightedFull'                                                              : [ 9.97366094e+04, 9.97403828e+04, 9.97161641e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.97366094e+04, 9.97366094e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.96359938e+05, 9.91253500e+05, 9.97297438e+05, 9.96273438e+05, 9.57794812e+05, 9.52021875e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99135391e+04, 1.00018477e+05, 1.48343422e+05, 9.99872969e+04, 9.93563672e+04, 5.68157617e+04, ],
  }),
  ("nof_tree_events",                 99998),
  ("nof_db_events",                   99998),
  ("fsize_local",                     517955139), # 517.96MB, avg file size 517.96MB
  ("fsize_db",                        6813110549), # 6.81GB, avg file size 567.76MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_3000_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_250_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_250_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 399995, ],
    'CountWeighted'                                                                  : [ 3.99924625e+05, 3.99954938e+05, 3.99905000e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.04863938e+05, 3.99921688e+05, 3.92207406e+05, 4.04863938e+05, 3.99921688e+05, 3.92207406e+05, 4.04863938e+05, 3.99921688e+05, 3.92207406e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.04863938e+05, 3.92207406e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99932200e+06, 3.99932200e+06, 3.99932200e+06, 3.99932200e+06, 3.99932200e+06, 3.99932200e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99938312e+05, 4.00280125e+05, 5.77898125e+05, 3.99995125e+05, 3.98517875e+05, 2.41380016e+05, ],
    'CountWeightedFull'                                                              : [ 3.99852125e+05, 3.99882875e+05, 3.99833438e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.04790812e+05, 3.99849250e+05, 3.92136469e+05, 4.04790812e+05, 3.99849250e+05, 3.92136469e+05, 4.04790812e+05, 3.99849250e+05, 3.92136469e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.04790812e+05, 3.92136469e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99860350e+06, 3.99860350e+06, 3.99860350e+06, 3.99860350e+06, 3.99860350e+06, 3.99860350e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99867750e+05, 4.00208062e+05, 5.77792562e+05, 3.99920375e+05, 3.98445250e+05, 2.41336641e+05, ],
  }),
  ("nof_tree_events",                 399995),
  ("nof_db_events",                   399995),
  ("fsize_local",                     1396388926), # 1.40GB, avg file size 698.19MB
  ("fsize_db",                        19971775045), # 19.97GB, avg file size 2.00GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_250_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_260_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_260_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 399996, ],
    'CountWeighted'                                                                  : [ 3.99947125e+05, 3.99966188e+05, 3.99918938e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.06203562e+05, 3.99946188e+05, 3.91114438e+05, 4.06203562e+05, 3.99946188e+05, 3.91114438e+05, 4.06203562e+05, 3.99946188e+05, 3.91114438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.06203562e+05, 3.91114438e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99932150e+06, 3.99932150e+06, 3.99932150e+06, 3.99932150e+06, 3.99932150e+06, 3.99932150e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99912375e+05, 3.99981188e+05, 5.78965500e+05, 4.00048750e+05, 3.99622500e+05, 2.41166594e+05, ],
    'CountWeightedFull'                                                              : [ 3.99876500e+05, 3.99894500e+05, 3.99848594e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.06131312e+05, 3.99875500e+05, 3.91045000e+05, 4.06131312e+05, 3.99875500e+05, 3.91045000e+05, 4.06131312e+05, 3.99875500e+05, 3.91045000e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.06131312e+05, 3.91045000e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99860900e+06, 3.99860900e+06, 3.99860900e+06, 3.99860900e+06, 3.99860900e+06, 3.99860900e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99843031e+05, 3.99910812e+05, 5.78861125e+05, 3.99975312e+05, 3.99549844e+05, 2.41124156e+05, ],
  }),
  ("nof_tree_events",                 399996),
  ("nof_db_events",                   399996),
  ("fsize_local",                     1422975857), # 1.42GB, avg file size 711.49MB
  ("fsize_db",                        20198243316), # 20.20GB, avg file size 1.35GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_260_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_270_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_270_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 399994, ],
    'CountWeighted'                                                                  : [ 3.99906875e+05, 3.99931875e+05, 3.99932062e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.07489094e+05, 3.99904719e+05, 3.90112656e+05, 4.07489094e+05, 3.99904719e+05, 3.90112656e+05, 4.07489094e+05, 3.99904719e+05, 3.90112656e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.07490812e+05, 3.90110938e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99940100e+06, 3.99940100e+06, 3.99940100e+06, 3.99940100e+06, 3.99940100e+06, 3.99940100e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99832344e+05, 4.00059344e+05, 5.78596125e+05, 4.00132469e+05, 3.98848188e+05, 2.40957406e+05, ],
    'CountWeightedFull'                                                              : [ 3.99835688e+05, 3.99860000e+05, 3.99860062e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.07415938e+05, 3.99833562e+05, 3.90042500e+05, 4.07415938e+05, 3.99833562e+05, 3.90042500e+05, 4.07415938e+05, 3.99833562e+05, 3.90042500e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.07417625e+05, 3.90040812e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99867675e+06, 3.99867675e+06, 3.99867675e+06, 3.99867675e+06, 3.99867675e+06, 3.99867675e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99762062e+05, 3.99987750e+05, 5.78491750e+05, 4.00058406e+05, 3.98776281e+05, 2.40914281e+05, ],
  }),
  ("nof_tree_events",                 399994),
  ("nof_db_events",                   399994),
  ("fsize_local",                     1449832821), # 1.45GB, avg file size 724.92MB
  ("fsize_db",                        20152896070), # 20.15GB, avg file size 1.26GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_270_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_280_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_280_hh_2b2v_sl"),
  ("nof_files",                       3),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 393998, ],
    'CountWeighted'                                                                  : [ 3.93995094e+05, 3.93952344e+05, 3.93976500e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.02630438e+05, 3.93989781e+05, 3.83336406e+05, 4.02630438e+05, 3.93989781e+05, 3.83336406e+05, 4.02630438e+05, 3.93989781e+05, 3.83336406e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.02630438e+05, 3.83336406e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.94003450e+06, 3.94003450e+06, 3.94003450e+06, 3.94003450e+06, 3.94003450e+06, 3.94003450e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.94054469e+05, 3.93724031e+05, 5.69904312e+05, 3.93910062e+05, 3.93094188e+05, 2.37247234e+05, ],
    'CountWeightedFull'                                                              : [ 3.93922625e+05, 3.93880375e+05, 3.93904125e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.02555781e+05, 3.93917188e+05, 3.83265406e+05, 4.02555781e+05, 3.93917188e+05, 3.83265406e+05, 4.02555781e+05, 3.93917188e+05, 3.83265406e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.02555781e+05, 3.83265406e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.93930075e+06, 3.93930075e+06, 3.93930075e+06, 3.93930075e+06, 3.93930075e+06, 3.93930075e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.93984125e+05, 3.93652312e+05, 5.69797125e+05, 3.93835438e+05, 3.93019219e+05, 2.37203969e+05, ],
  }),
  ("nof_tree_events",                 393998),
  ("nof_db_events",                   393998),
  ("fsize_local",                     1456781544), # 1.46GB, avg file size 485.59MB
  ("fsize_db",                        20247168170), # 20.25GB, avg file size 1.01GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_280_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_300_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_300_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 299996, ],
    'CountWeighted'                                                                  : [ 2.99954219e+05, 2.99931156e+05, 2.99953312e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.08219188e+05, 2.99954219e+05, 2.90500344e+05, 3.08219188e+05, 2.99954219e+05, 2.90500344e+05, 3.08219188e+05, 2.99954219e+05, 2.90500344e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.08219188e+05, 2.90500344e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99954800e+06, 2.99956000e+06, 2.99956000e+06, 2.99954800e+06, 2.99956000e+06, 2.99954800e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99915656e+05, 3.00031188e+05, 4.34319938e+05, 3.00083375e+05, 2.99006844e+05, 1.80206344e+05, ],
    'CountWeightedFull'                                                              : [ 2.99897531e+05, 2.99874781e+05, 2.99896531e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.08161094e+05, 2.99897531e+05, 2.90445656e+05, 3.08161094e+05, 2.99897531e+05, 2.90445656e+05, 3.08161094e+05, 2.99897531e+05, 2.90445656e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.08161094e+05, 2.90445656e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99899725e+06, 2.99899725e+06, 2.99899725e+06, 2.99899725e+06, 2.99899725e+06, 2.99899725e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99861719e+05, 2.99975125e+05, 4.34238031e+05, 3.00025969e+05, 2.98950344e+05, 1.80173531e+05, ],
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     1149284105), # 1.15GB, avg file size 574.64MB
  ("fsize_db",                        15383217059), # 15.38GB, avg file size 1.10GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_300_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_320_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_320_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 299999, ],
    'CountWeighted'                                                                  : [ 2.99968938e+05, 2.99968031e+05, 2.99954188e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.09819125e+05, 2.99967906e+05, 2.89275844e+05, 3.09819125e+05, 2.99967906e+05, 2.89275844e+05, 3.09819125e+05, 2.99967906e+05, 2.89275844e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.09819125e+05, 2.89275812e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99988175e+06, 2.99988175e+06, 2.99988175e+06, 2.99988175e+06, 2.99988175e+06, 2.99988175e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.00096844e+05, 3.00125406e+05, 4.35391688e+05, 2.99813844e+05, 2.99487875e+05, 1.79757406e+05, ],
    'CountWeightedFull'                                                              : [ 2.99912438e+05, 2.99911906e+05, 2.99898062e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.09760844e+05, 2.99911250e+05, 2.89221375e+05, 3.09760844e+05, 2.99911250e+05, 2.89221375e+05, 3.09760844e+05, 2.99911250e+05, 2.89221375e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.09760844e+05, 2.89221375e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99931350e+06, 2.99931350e+06, 2.99931350e+06, 2.99931350e+06, 2.99931350e+06, 2.99931350e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.00042094e+05, 3.00068688e+05, 4.35309594e+05, 2.99755375e+05, 2.99432188e+05, 1.79723969e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1187312002), # 1.19GB, avg file size 593.66MB
  ("fsize_db",                        15558724573), # 15.56GB, avg file size 1.11GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_320_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_350_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_350_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 299998, ],
    'CountWeighted'                                                                  : [ 2.99946719e+05, 2.99948406e+05, 2.99975812e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.11966875e+05, 2.99946500e+05, 2.87609531e+05, 3.11966875e+05, 2.99946500e+05, 2.87609531e+05, 3.11966875e+05, 2.99946500e+05, 2.87609531e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.11966875e+05, 2.87609531e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99948225e+06, 2.99948225e+06, 2.99948225e+06, 2.99948225e+06, 2.99948225e+06, 2.99948225e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99942250e+05, 2.99891125e+05, 4.36419125e+05, 3.00016906e+05, 3.00226469e+05, 1.79309750e+05, ],
    'CountWeightedFull'                                                              : [ 2.99890125e+05, 2.99892125e+05, 2.99918031e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.11907625e+05, 2.99889875e+05, 2.87554688e+05, 3.11907625e+05, 2.99889875e+05, 2.87554688e+05, 3.11907625e+05, 2.99889875e+05, 2.87554688e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.11907625e+05, 2.87554688e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99891675e+06, 2.99891675e+06, 2.99891675e+06, 2.99891675e+06, 2.99891675e+06, 2.99891675e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99886750e+05, 2.99833688e+05, 4.36335219e+05, 2.99957688e+05, 3.00169469e+05, 1.79276047e+05, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1239321447), # 1.24GB, avg file size 619.66MB
  ("fsize_db",                        15844168810), # 15.84GB, avg file size 1.32GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_350_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_400_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_400_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 294999, ],
    'CountWeighted'                                                                  : [ 2.94930938e+05, 2.94957844e+05, 2.94968344e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.09852125e+05, 2.94930938e+05, 2.80504344e+05, 3.09852125e+05, 2.94930938e+05, 2.80504344e+05, 3.09852125e+05, 2.94930938e+05, 2.80504344e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.09852125e+05, 2.80504344e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.94974450e+06, 2.94974450e+06, 2.94974450e+06, 2.94974450e+06, 2.94974450e+06, 2.94974450e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.94718906e+05, 2.94997812e+05, 4.28711375e+05, 2.95285188e+05, 2.93881219e+05, 1.75786406e+05, ],
    'CountWeightedFull'                                                              : [ 2.94875250e+05, 2.94902125e+05, 2.94911281e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.09792562e+05, 2.94875250e+05, 2.80450656e+05, 3.09792562e+05, 2.94875250e+05, 2.80450656e+05, 3.09792562e+05, 2.94875250e+05, 2.80450656e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.09792562e+05, 2.80450656e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.94917475e+06, 2.94917475e+06, 2.94917475e+06, 2.94917475e+06, 2.94917475e+06, 2.94917475e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.94664062e+05, 2.94941750e+05, 4.28628188e+05, 2.95226500e+05, 2.93824062e+05, 1.75752938e+05, ],
  }),
  ("nof_tree_events",                 294999),
  ("nof_db_events",                   294999),
  ("fsize_local",                     1289877772), # 1.29GB, avg file size 644.94MB
  ("fsize_db",                        16131673901), # 16.13GB, avg file size 1.01GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_400_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_450_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_450_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 299999, ],
    'CountWeighted'                                                                  : [ 2.99955375e+05, 2.99965906e+05, 2.99956812e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.17776875e+05, 2.99955375e+05, 2.83229562e+05, 3.17776875e+05, 2.99955375e+05, 2.83229562e+05, 3.17776875e+05, 2.99955375e+05, 2.83229562e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.17776875e+05, 2.83229500e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99950775e+06, 2.99950775e+06, 2.99950775e+06, 2.99950775e+06, 2.99950775e+06, 2.99950775e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.00011000e+05, 3.00198406e+05, 4.36770625e+05, 2.99916031e+05, 2.98853500e+05, 1.78026031e+05, ],
    'CountWeightedFull'                                                              : [ 2.99895938e+05, 2.99906562e+05, 2.99897031e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.17713750e+05, 2.99895938e+05, 2.83173500e+05, 3.17713750e+05, 2.99895938e+05, 2.83173500e+05, 3.17713750e+05, 2.99895938e+05, 2.83173500e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.17713750e+05, 2.83173438e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99891500e+06, 2.99891500e+06, 2.99891500e+06, 2.99891500e+06, 2.99891500e+06, 2.99891500e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99953375e+05, 3.00139344e+05, 4.36682000e+05, 2.99854156e+05, 2.98792625e+05, 1.77991172e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1375623782), # 1.38GB, avg file size 687.81MB
  ("fsize_db",                        16748440441), # 16.75GB, avg file size 1.05GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_450_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_500_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_500_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 299996, ],
    'CountWeighted'                                                                  : [ 2.99983844e+05, 2.99970062e+05, 2.99968656e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.20053625e+05, 2.99983844e+05, 2.81469344e+05, 3.20053625e+05, 2.99983844e+05, 2.81469344e+05, 3.20053625e+05, 2.99983844e+05, 2.81469344e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.20053625e+05, 2.81469344e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99944250e+06, 2.99946500e+06, 2.99946500e+06, 2.99944250e+06, 2.99946500e+06, 2.99944250e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99911500e+05, 2.99961469e+05, 4.37620844e+05, 3.00118562e+05, 2.99237156e+05, 1.77605156e+05, ],
    'CountWeightedFull'                                                              : [ 2.99920594e+05, 2.99907750e+05, 2.99905312e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.19986625e+05, 2.99920594e+05, 2.81410438e+05, 3.19986625e+05, 2.99920594e+05, 2.81410438e+05, 3.19986625e+05, 2.99920594e+05, 2.81410438e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.19986625e+05, 2.81410438e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99883750e+06, 2.99883750e+06, 2.99883750e+06, 2.99883750e+06, 2.99883750e+06, 2.99883750e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99852656e+05, 2.99897375e+05, 4.37527594e+05, 3.00055812e+05, 2.99175469e+05, 1.77569500e+05, ],
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     1432351712), # 1.43GB, avg file size 716.18MB
  ("fsize_db",                        16947221880), # 16.95GB, avg file size 1.69GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_500_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_550_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_550_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 299996, ],
    'CountWeighted'                                                                  : [ 2.99861375e+05, 2.99896562e+05, 2.99933469e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.22049031e+05, 2.99861375e+05, 2.79843000e+05, 3.22049031e+05, 2.99861375e+05, 2.79843000e+05, 3.22049031e+05, 2.99861375e+05, 2.79843000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.22049031e+05, 2.79843000e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99911275e+06, 2.99912450e+06, 2.99912450e+06, 2.99911275e+06, 2.99912450e+06, 2.99911275e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99859875e+05, 3.00057156e+05, 4.37683344e+05, 3.00074062e+05, 2.98604656e+05, 1.77092453e+05, ],
    'CountWeightedFull'                                                              : [ 2.99800250e+05, 2.99834250e+05, 2.99869562e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.21981844e+05, 2.99800250e+05, 2.79784875e+05, 3.21981844e+05, 2.99800250e+05, 2.79784875e+05, 3.21981844e+05, 2.99800250e+05, 2.79784875e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.21981844e+05, 2.79784875e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99849675e+06, 2.99849675e+06, 2.99849675e+06, 2.99849675e+06, 2.99849675e+06, 2.99849675e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99800531e+05, 2.99995625e+05, 4.37591250e+05, 3.00010500e+05, 2.98541250e+05, 1.77056422e+05, ],
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     1477410586), # 1.48GB, avg file size 738.71MB
  ("fsize_db",                        18422901680), # 18.42GB, avg file size 1.02GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_550_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_600_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_600_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 199999, ],
    'CountWeighted'                                                                  : [ 1.99967750e+05, 1.99969000e+05, 1.99974859e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.15932453e+05, 1.99967750e+05, 1.85657219e+05, 2.15932453e+05, 1.99967750e+05, 1.85657219e+05, 2.15932453e+05, 1.99967750e+05, 1.85657219e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.15932516e+05, 1.85657156e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99971800e+06, 1.99971800e+06, 1.99971800e+06, 1.99971800e+06, 1.99971800e+06, 1.99971800e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.00006188e+05, 1.99949625e+05, 2.92439375e+05, 1.99983469e+05, 1.99574406e+05, 1.17809562e+05, ],
    'CountWeightedFull'                                                              : [ 1.99925828e+05, 1.99927141e+05, 1.99932938e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.15887641e+05, 1.99925828e+05, 1.85618297e+05, 2.15887641e+05, 1.99925828e+05, 1.85618297e+05, 2.15887641e+05, 1.99925828e+05, 1.85618297e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.15887703e+05, 1.85618250e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.99929625e+06, 1.99929625e+06, 1.99929625e+06, 1.99929625e+06, 1.99929625e+06, 1.99929625e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99965656e+05, 1.99908156e+05, 2.92377750e+05, 1.99940281e+05, 1.99532719e+05, 1.17785328e+05, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     1007022957), # 1.01GB, avg file size 1.01GB
  ("fsize_db",                        11639973909), # 11.64GB, avg file size 895.38MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_600_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_650_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_650_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 175996, ],
    'CountWeighted'                                                                  : [ 1.75957703e+05, 1.75975062e+05, 1.75988172e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.90992062e+05, 1.75956328e+05, 1.62637891e+05, 1.90992062e+05, 1.75956328e+05, 1.62637891e+05, 1.90992062e+05, 1.75956328e+05, 1.62637891e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.90992297e+05, 1.62637656e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.75976988e+06, 1.75976988e+06, 1.75976988e+06, 1.75976988e+06, 1.75976988e+06, 1.75976988e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.76016766e+05, 1.76080406e+05, 2.58460391e+05, 1.75948438e+05, 1.76227469e+05, 1.03283398e+05, ],
    'CountWeightedFull'                                                              : [ 1.75918797e+05, 1.75935922e+05, 1.75948500e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.90949594e+05, 1.75917422e+05, 1.62601609e+05, 1.90949594e+05, 1.75917422e+05, 1.62601609e+05, 1.90949594e+05, 1.75917422e+05, 1.62601609e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.90949844e+05, 1.62601375e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.75937788e+06, 1.75937788e+06, 1.75937788e+06, 1.75937788e+06, 1.75937788e+06, 1.75937788e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.75979812e+05, 1.76041891e+05, 2.58402844e+05, 1.75908672e+05, 1.76187953e+05, 1.03261070e+05, ],
  }),
  ("nof_tree_events",                 175996),
  ("nof_db_events",                   175996),
  ("fsize_local",                     900853693), # 900.85MB, avg file size 450.43MB
  ("fsize_db",                        10417424944), # 10.42GB, avg file size 744.10MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_650_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_700_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_700_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99946828e+05, 1.99957344e+05, 1.99932531e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.18018906e+05, 1.99943547e+05, 1.84047375e+05, 2.18018906e+05, 1.99943547e+05, 1.84047375e+05, 2.18018906e+05, 1.99943547e+05, 1.84047375e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.18018906e+05, 1.84047375e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99951912e+06, 1.99953088e+06, 1.99953088e+06, 1.99951912e+06, 1.99953088e+06, 1.99951912e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.00070156e+05, 1.99951156e+05, 2.92930969e+05, 1.99869172e+05, 1.99454500e+05, 1.17205906e+05, ],
    'CountWeightedFull'                                                              : [ 1.99901172e+05, 1.99912391e+05, 1.99886359e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.17969156e+05, 1.99897906e+05, 1.84005547e+05, 2.17969156e+05, 1.99897906e+05, 1.84005547e+05, 2.17969156e+05, 1.99897906e+05, 1.84005547e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.17969156e+05, 1.84005547e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.99907700e+06, 1.99907700e+06, 1.99907700e+06, 1.99907700e+06, 1.99907700e+06, 1.99907700e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.00029000e+05, 1.99906453e+05, 2.92864500e+05, 1.99824719e+05, 1.99408641e+05, 1.17181281e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1031616827), # 1.03GB, avg file size 1.03GB
  ("fsize_db",                        13025859591), # 13.03GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_700_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_750_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_750_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 199995, ],
    'CountWeighted'                                                                  : [ 1.99953281e+05, 1.99940828e+05, 1.99950719e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.18937125e+05, 1.99953281e+05, 1.83354125e+05, 2.18937125e+05, 1.99953281e+05, 1.83354125e+05, 2.18937125e+05, 1.99953281e+05, 1.83354125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.18937125e+05, 1.83354125e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99951575e+06, 1.99951575e+06, 1.99951575e+06, 1.99951575e+06, 1.99951575e+06, 1.99951575e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99911609e+05, 1.99999125e+05, 2.93639000e+05, 2.00088219e+05, 1.99731344e+05, 1.16973953e+05, ],
    'CountWeightedFull'                                                              : [ 1.99909312e+05, 1.99896609e+05, 1.99906812e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.18888781e+05, 1.99909312e+05, 1.83314000e+05, 2.18888781e+05, 1.99909312e+05, 1.83314000e+05, 2.18888781e+05, 1.99909312e+05, 1.83314000e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.18888781e+05, 1.83314000e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.99907550e+06, 1.99907550e+06, 1.99907550e+06, 1.99907550e+06, 1.99907550e+06, 1.99907550e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99869172e+05, 1.99955438e+05, 2.93574500e+05, 2.00042797e+05, 1.99687531e+05, 1.16948281e+05, ],
  }),
  ("nof_tree_events",                 199995),
  ("nof_db_events",                   199995),
  ("fsize_local",                     1038401435), # 1.04GB, avg file size 1.04GB
  ("fsize_db",                        11864616665), # 11.86GB, avg file size 988.72MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_750_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_800_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_800_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 199995, ],
    'CountWeighted'                                                                  : [ 1.99970625e+05, 1.99972844e+05, 1.99930750e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.19801484e+05, 1.99970625e+05, 1.82745844e+05, 2.19801484e+05, 1.99970625e+05, 1.82745844e+05, 2.19801484e+05, 1.99970625e+05, 1.82745844e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.19801500e+05, 1.82745844e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99977825e+06, 1.99978875e+06, 1.99978875e+06, 1.99977825e+06, 1.99978875e+06, 1.99977825e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99976969e+05, 1.99607203e+05, 2.94002812e+05, 1.99999250e+05, 2.00328641e+05, 1.16792594e+05, ],
    'CountWeightedFull'                                                              : [ 1.99923531e+05, 1.99925875e+05, 1.99885031e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.19750297e+05, 1.99923531e+05, 1.82703156e+05, 2.19750297e+05, 1.99923531e+05, 1.82703156e+05, 2.19750297e+05, 1.99923531e+05, 1.82703156e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.19750312e+05, 1.82703156e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.99931662e+06, 1.99931662e+06, 1.99931662e+06, 1.99931662e+06, 1.99931662e+06, 1.99931662e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99935297e+05, 1.99561781e+05, 2.93934719e+05, 1.99954531e+05, 2.00280719e+05, 1.16767633e+05, ],
  }),
  ("nof_tree_events",                 199995),
  ("nof_db_events",                   199995),
  ("fsize_local",                     1042664068), # 1.04GB, avg file size 1.04GB
  ("fsize_db",                        12088855279), # 12.09GB, avg file size 929.91MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_800_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_850_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_850_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 189999, ],
    'CountWeighted'                                                                  : [ 1.89970562e+05, 1.89959938e+05, 1.89946797e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.89970562e+05, 1.89970562e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.89957838e+06, 1.89957838e+06, 1.89957838e+06, 1.89957838e+06, 1.89957838e+06, 1.89957838e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.89947297e+05, 1.89985750e+05, 2.79469094e+05, 1.90039188e+05, 1.89808688e+05, 1.10711648e+05, ],
    'CountWeightedFull'                                                              : [ 1.89928828e+05, 1.89918547e+05, 1.89905484e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.89928828e+05, 1.89928828e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.89916650e+06, 1.89916650e+06, 1.89916650e+06, 1.89916650e+06, 1.89916650e+06, 1.89916650e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.89907344e+05, 1.89944844e+05, 2.79408000e+05, 1.89996219e+05, 1.89767266e+05, 1.10687656e+05, ],
  }),
  ("nof_tree_events",                 189999),
  ("nof_db_events",                   189999),
  ("fsize_local",                     1000432769), # 1.00GB, avg file size 500.22MB
  ("fsize_db",                        11961368588), # 11.96GB, avg file size 920.11MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_850_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_900_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_900_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 199998, ],
    'CountWeighted'                                                                  : [ 1.99934656e+05, 1.99957641e+05, 1.99955672e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99934656e+05, 1.99934656e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99939575e+06, 1.99939575e+06, 1.99939575e+06, 1.99939575e+06, 1.99939575e+06, 1.99939575e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.00011297e+05, 2.00037547e+05, 2.94226812e+05, 1.99945266e+05, 1.99541375e+05, 1.16330344e+05, ],
    'CountWeightedFull'                                                              : [ 1.99890312e+05, 1.99913234e+05, 1.99911562e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99890312e+05, 1.99890312e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.99896050e+06, 1.99896050e+06, 1.99896050e+06, 1.99896050e+06, 1.99896050e+06, 1.99896050e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99968781e+05, 1.99993656e+05, 2.94161219e+05, 1.99899609e+05, 1.99497016e+05, 1.16305070e+05, ],
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     1053777236), # 1.05GB, avg file size 1.05GB
  ("fsize_db",                        13700391957), # 13.70GB, avg file size 1.25GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_900_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1000_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_1000_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99734141e+04, 9.99777891e+04, 9.99781406e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.11340094e+05, 9.99734141e+04, 9.03260625e+04, 1.11340094e+05, 9.99734141e+04, 9.03260625e+04, 1.11340094e+05, 9.99734141e+04, 9.03260625e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.11340094e+05, 9.03260625e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99736188e+05, 9.99746250e+05, 9.99746250e+05, 9.99736250e+05, 9.99746250e+05, 9.99736188e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00014711e+05, 9.97819922e+04, 1.47312750e+05, 9.99509688e+04, 1.00009250e+05, 5.80142852e+04, ],
    'CountWeightedFull'                                                              : [ 9.99485156e+04, 9.99526797e+04, 9.99532578e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.11312469e+05, 9.99485156e+04, 9.03035938e+04, 1.11312469e+05, 9.99485156e+04, 9.03035938e+04, 1.11312469e+05, 9.99485156e+04, 9.03035938e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.11312469e+05, 9.03035938e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99497500e+05, 9.99497500e+05, 9.99497500e+05, 9.99497500e+05, 9.99497500e+05, 9.99497500e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99920234e+04, 9.97574141e+04, 1.47276344e+05, 9.99265156e+04, 9.99847656e+04, 5.80008164e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     526961184), # 526.96MB, avg file size 526.96MB
  ("fsize_db",                        6254656704), # 6.25GB, avg file size 694.96MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_1000_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1250_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_1250_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 99998, ],
    'CountWeighted'                                                                  : [ 9.99478750e+04, 9.99494219e+04, 9.99461172e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99478750e+04, 9.99478750e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99452375e+05, 9.99452375e+05, 9.99452375e+05, 9.99452375e+05, 9.99452375e+05, 9.99452375e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99537578e+04, 1.00185875e+05, 1.47340750e+05, 1.00000094e+05, 9.92008672e+04, 5.76467031e+04, ],
    'CountWeightedFull'                                                              : [ 9.99240781e+04, 9.99253516e+04, 9.99221875e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99240781e+04, 9.99240781e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99216500e+05, 9.99216500e+05, 9.99216500e+05, 9.99216500e+05, 9.99216500e+05, 9.99216500e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99310078e+04, 1.00162312e+05, 1.47303984e+05, 9.99752969e+04, 9.91755547e+04, 5.76330547e+04, ],
  }),
  ("nof_tree_events",                 99998),
  ("nof_db_events",                   99998),
  ("fsize_local",                     526246937), # 526.25MB, avg file size 526.25MB
  ("fsize_db",                        6492023211), # 6.49GB, avg file size 811.50MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_1250_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1500_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_1500_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 9.99579688e+04, 9.99730312e+04, 9.99534375e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99579688e+04, 9.99579688e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99707188e+05, 9.99707188e+05, 9.99707188e+05, 9.99707188e+05, 9.99707188e+05, 9.99707188e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00028969e+05, 9.99716875e+04, 1.48116562e+05, 9.99239141e+04, 9.99466250e+04, 5.73307695e+04, ],
    'CountWeightedFull'                                                              : [ 9.99324297e+04, 9.99471250e+04, 9.99282969e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99324297e+04, 9.99324297e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99452250e+05, 9.99452250e+05, 9.99452250e+05, 9.99452250e+05, 9.99452250e+05, 9.99452250e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.00004453e+05, 9.99463594e+04, 1.48078375e+05, 9.98972969e+04, 9.99210938e+04, 5.73165352e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     516173233), # 516.17MB, avg file size 516.17MB
  ("fsize_db",                        7056320162), # 7.06GB, avg file size 641.48MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_1500_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1750_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_1750_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 9.99335938e+04, 9.99191406e+04, 9.99272188e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99335938e+04, 9.99335938e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99255875e+05, 9.99255875e+05, 9.99255875e+05, 9.99255875e+05, 9.99255875e+05, 9.99255875e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00058164e+05, 9.96850703e+04, 1.48325438e+05, 9.98798438e+04, 1.00197531e+05, 5.72466523e+04, ],
    'CountWeightedFull'                                                              : [ 9.99057500e+04, 9.98919609e+04, 9.98996016e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99057500e+04, 9.99057500e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.98980312e+05, 9.98980312e+05, 9.98980312e+05, 9.98980312e+05, 9.98980312e+05, 9.98980312e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.00032812e+05, 9.96581562e+04, 1.48285312e+05, 9.98525156e+04, 1.00169938e+05, 5.72316484e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     510769401), # 510.77MB, avg file size 510.77MB
  ("fsize_db",                        7084354114), # 7.08GB, avg file size 708.44MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_1750_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_2000_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_2000_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99292734e+04, 9.99280469e+04, 9.99309141e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.15692047e+05, 9.99268359e+04, 8.72101094e+04, 1.15692047e+05, 9.99268359e+04, 8.72101094e+04, 1.15692047e+05, 9.99268359e+04, 8.72101094e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.15693672e+05, 8.72097031e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99290562e+05, 9.99290562e+05, 9.99290562e+05, 9.99290562e+05, 9.99290562e+05, 9.99290562e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99969453e+04, 1.00008695e+05, 1.48555719e+05, 1.00003047e+05, 9.98839375e+04, 5.69892852e+04, ],
    'CountWeightedFull'                                                              : [ 9.99013828e+04, 9.98998281e+04, 9.99032969e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.15659781e+05, 9.98989688e+04, 8.71857812e+04, 1.15659781e+05, 9.98989688e+04, 8.71857812e+04, 1.15659781e+05, 9.98989688e+04, 8.71857812e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.15661406e+05, 8.71853672e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99013438e+05, 9.99013438e+05, 9.99013438e+05, 9.99013438e+05, 9.99013438e+05, 9.99013438e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99702812e+04, 9.99807969e+04, 1.48514719e+05, 9.99743750e+04, 9.98565938e+04, 5.69736133e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     506612117), # 506.61MB, avg file size 506.61MB
  ("fsize_db",                        6452776971), # 6.45GB, avg file size 537.73MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_2000_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_2500_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_2500_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 9.98486875e+04, 9.98571094e+04, 9.98325938e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.17138578e+05, 9.98486875e+04, 8.60844453e+04, 1.17138578e+05, 9.98486875e+04, 8.60844453e+04, 1.17138578e+05, 9.98486875e+04, 8.60844453e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.17141984e+05, 8.60810469e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.98397375e+05, 9.98397375e+05, 9.98397375e+05, 9.98397375e+05, 9.98397375e+05, 9.98397375e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99651562e+04, 1.00183234e+05, 1.48797844e+05, 1.00008898e+05, 9.95904375e+04, 5.67207500e+04, ],
    'CountWeightedFull'                                                              : [ 9.98184375e+04, 9.98264531e+04, 9.98024453e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.17102984e+05, 9.98184375e+04, 8.60583438e+04, 1.17102984e+05, 9.98184375e+04, 8.60583438e+04, 1.17102984e+05, 9.98184375e+04, 8.60583438e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.17106391e+05, 8.60549375e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.98093500e+05, 9.98093500e+05, 9.98093500e+05, 9.98093500e+05, 9.98093500e+05, 9.98093500e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99378750e+04, 1.00153625e+05, 1.48753094e+05, 9.99792891e+04, 9.95597969e+04, 5.67046094e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     507356249), # 507.36MB, avg file size 507.36MB
  ("fsize_db",                        7464949682), # 7.46GB, avg file size 1.24GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_2500_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_3000_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_3000_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 9.97906875e+04, 9.97894531e+04, 9.97952031e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.18494258e+05, 9.97897031e+04, 8.51123906e+04, 1.18494258e+05, 9.97897031e+04, 8.51123906e+04, 1.18494258e+05, 9.97897031e+04, 8.51123906e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.18496352e+05, 8.51103594e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.97941750e+05, 9.97941750e+05, 9.97941750e+05, 9.97941750e+05, 9.97941750e+05, 9.97941750e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99601094e+04, 9.98601484e+04, 1.48523469e+05, 1.00004125e+05, 9.97096484e+04, 5.67764062e+04, ],
    'CountWeightedFull'                                                              : [ 9.97597656e+04, 9.97582656e+04, 9.97640703e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.18457469e+05, 9.97587500e+04, 8.50860938e+04, 1.18457469e+05, 9.97587500e+04, 8.50860938e+04, 1.18457469e+05, 9.97587500e+04, 8.50860938e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.18459562e+05, 8.50840625e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.97632375e+05, 9.97632375e+05, 9.97632375e+05, 9.97632375e+05, 9.97632375e+05, 9.97632375e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99309688e+04, 9.98299375e+04, 1.48476578e+05, 9.99726094e+04, 9.96772031e+04, 5.67590352e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     508755273), # 508.76MB, avg file size 508.76MB
  ("fsize_db",                        6593140153), # 6.59GB, avg file size 659.31MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_3000_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFHHTo2B2WToLNu2J_CV_1_C2V_1_C3_0_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_0_hh_bbvv_sl"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_0_hh_2b2v_sl_dipoleRecoilOff"),
  ("nof_files",                       2),
  ("nof_db_files",                    25),
  ("nof_events",                      {
    'Count'                                                                          : [ 399995, ],
    'CountWeighted'                                                                  : [ 3.99929438e+05, 3.99939250e+05, 3.99938344e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99929438e+05, 3.99929438e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99933725e+06, 3.99937400e+06, 3.99937400e+06, 3.99933800e+06, 3.99937400e+06, 3.99933675e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99943969e+05, 3.99716312e+05, 5.66998000e+05, 3.99858938e+05, 3.99822781e+05, 2.47597672e+05, ],
    'CountWeightedFull'                                                              : [ 3.99699219e+05, 3.99710688e+05, 3.99709375e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99699219e+05, 3.99699219e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99707850e+06, 3.99707850e+06, 3.99707850e+06, 3.99707850e+06, 3.99707850e+06, 3.99707850e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99766094e+05, 3.99485375e+05, 5.66674688e+05, 3.99680781e+05, 3.99593250e+05, 2.47487438e+05, ],
  }),
  ("nof_tree_events",                 399995),
  ("nof_db_events",                   399995),
  ("fsize_local",                     1633989812), # 1.63GB, avg file size 816.99MB
  ("fsize_db",                        24143504881), # 24.14GB, avg file size 965.74MB
  ("use_it",                          True),
  ("xsection",                        0.000503987),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_1_0_hh_2b2v_sl_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFHHTo2B2WToLNu2J_CV_1_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_1_hh_bbvv_sl"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_1_hh_2b2v_sl_dipoleRecoilOff"),
  ("nof_files",                       2),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 399997, ],
    'CountWeighted'                                                                  : [ 3.99972500e+05, 3.99987125e+05, 3.99995625e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99972500e+05, 3.99972500e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99965600e+06, 3.99967900e+06, 3.99967900e+06, 3.99965400e+06, 3.99967900e+06, 3.99965200e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00027188e+05, 3.99965625e+05, 5.67300375e+05, 3.99790094e+05, 3.99447938e+05, 2.47149828e+05, ],
    'CountWeightedFull'                                                              : [ 3.99726062e+05, 3.99742188e+05, 3.99748438e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99726062e+05, 3.99726062e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99723275e+06, 3.99723275e+06, 3.99723275e+06, 3.99723275e+06, 3.99723275e+06, 3.99723275e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99844781e+05, 3.99719188e+05, 5.66960750e+05, 3.99606562e+05, 3.99209156e+05, 2.47036406e+05, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     1634636618), # 1.63GB, avg file size 817.32MB
  ("fsize_db",                        24125629826), # 24.13GB, avg file size 1.15GB
  ("use_it",                          True),
  ("xsection",                        0.000188741),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_1_1_hh_2b2v_sl_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFHHTo2B2WToLNu2J_CV_1_C2V_1_C3_1_dipoleRecoilOn-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_1_hh_dipoleRecoilOn_bbvv_sl"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_1_hh_2b2v_sl_dipoleRecoilOn"),
  ("nof_files",                       2),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 399996, ],
    'CountWeighted'                                                                  : [ 3.99990109e+05, 3.99996953e+05, 3.99990266e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99990109e+05, 3.99990109e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99942638e+06, 3.99949050e+06, 3.99949050e+06, 3.99942562e+06, 3.99949050e+06, 3.99942388e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99872250e+05, 3.99869594e+05, 5.43939328e+05, 3.99976859e+05, 3.99704719e+05, 2.66286344e+05, ],
    'CountWeightedFull'                                                              : [ 3.99727094e+05, 3.99734859e+05, 3.99733484e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99727094e+05, 3.99727094e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99689925e+06, 3.99689925e+06, 3.99689925e+06, 3.99689925e+06, 3.99689925e+06, 3.99689925e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99670859e+05, 3.99608797e+05, 5.43590312e+05, 3.99775203e+05, 3.99448125e+05, 2.66151484e+05, ],
  }),
  ("nof_tree_events",                 399996),
  ("nof_db_events",                   399996),
  ("fsize_local",                     1570263169), # 1.57GB, avg file size 785.13MB
  ("fsize_db",                        23463936206), # 23.46GB, avg file size 1.12GB
  ("use_it",                          False),
  ("xsection",                        0.000188741),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Nov22_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_1_1_hh_2b2v_sl_dipoleRecoilOn"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFHHTo2B2WToLNu2J_CV_1_C2V_1_C3_2_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_2_hh_bbvv_sl"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_2_hh_2b2v_sl_dipoleRecoilOff"),
  ("nof_files",                       4),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 399990, ],
    'CountWeighted'                                                                  : [ 3.99991625e+05, 3.99977531e+05, 3.99984625e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99991625e+05, 3.99991625e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99965150e+06, 3.99966350e+06, 3.99966350e+06, 3.99965100e+06, 3.99966350e+06, 3.99965100e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99909312e+05, 4.00405594e+05, 5.70138625e+05, 3.99920406e+05, 3.98351938e+05, 2.44286969e+05, ],
    'CountWeightedFull'                                                              : [ 3.99735844e+05, 3.99723594e+05, 3.99727281e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99735844e+05, 3.99735844e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99710625e+06, 3.99710625e+06, 3.99710625e+06, 3.99710625e+06, 3.99710625e+06, 3.99710625e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99714594e+05, 4.00153656e+05, 5.69771688e+05, 3.99725219e+05, 3.98088656e+05, 2.44168641e+05, ],
  }),
  ("nof_tree_events",                 399990),
  ("nof_db_events",                   399990),
  ("fsize_local",                     1744485277), # 1.74GB, avg file size 436.12MB
  ("fsize_db",                        24881949087), # 24.88GB, avg file size 1.31GB
  ("use_it",                          True),
  ("xsection",                        0.000155587),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_1_2_hh_2b2v_sl_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFHHTo2B2WToLNu2J_CV_1_C2V_2_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_2_1_hh_bbvv_sl"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_2_1_hh_2b2v_sl_dipoleRecoilOff"),
  ("nof_files",                       2),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                                          : [ 399996, ],
    'CountWeighted'                                                                  : [ 3.99971250e+05, 3.99967500e+05, 3.99934438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99971250e+05, 3.99971250e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99968350e+06, 3.99976100e+06, 3.99976100e+06, 3.99968200e+06, 3.99976100e+06, 3.99968200e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99753438e+05, 4.00666031e+05, 5.68579750e+05, 3.99981438e+05, 3.98152844e+05, 2.45375312e+05, ],
    'CountWeightedFull'                                                              : [ 3.99654062e+05, 3.99651188e+05, 3.99621625e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99654062e+05, 3.99654062e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99660550e+06, 3.99660550e+06, 3.99660550e+06, 3.99660550e+06, 3.99660550e+06, 3.99660550e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99551438e+05, 4.00346031e+05, 5.68146250e+05, 3.99779969e+05, 3.97851844e+05, 2.45251438e+05, ],
  }),
  ("nof_tree_events",                 399996),
  ("nof_db_events",                   399996),
  ("fsize_local",                     1986017385), # 1.99GB, avg file size 993.01MB
  ("fsize_db",                        26833952115), # 26.83GB, avg file size 1.22GB
  ("use_it",                          True),
  ("xsection",                        0.001554746),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_2_1_hh_2b2v_sl_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFHHTo2B2WToLNu2J_CV_1_C2V_2_C3_1_dipoleRecoilOn-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_2_1_hh_dipoleRecoilOn_bbvv_sl"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_2_1_hh_2b2v_sl_dipoleRecoilOn"),
  ("nof_files",                       5),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                                          : [ 399997, ],
    'CountWeighted'                                                                  : [ 3.99964809e+05, 3.99973700e+05, 3.99954422e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99964809e+05, 3.99964809e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99951226e+06, 3.99963776e+06, 3.99963776e+06, 3.99951567e+06, 3.99963776e+06, 3.99951198e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99829277e+05, 3.99890352e+05, 5.44807117e+05, 3.99924531e+05, 4.00285532e+05, 2.65853191e+05, ],
    'CountWeightedFull'                                                              : [ 3.99662437e+05, 3.99670771e+05, 3.99651457e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99662437e+05, 3.99662437e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99661266e+06, 3.99661266e+06, 3.99661266e+06, 3.99661266e+06, 3.99661266e+06, 3.99661266e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99610146e+05, 3.99588038e+05, 5.44401498e+05, 3.99705727e+05, 3.99982405e+05, 2.65706833e+05, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     1924053057), # 1.92GB, avg file size 384.81MB
  ("fsize_db",                        25537439336), # 25.54GB, avg file size 1.11GB
  ("use_it",                          False),
  ("xsection",                        0.001554746),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Nov22_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_2_1_hh_2b2v_sl_dipoleRecoilOn"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFHHTo2B2WToLNu2J_CV_0_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_0p5_1_1_hh_bbvv_sl"),
  ("process_name_specific",           "signal_vbf_nonresonant_0p5_1_1_hh_2b2v_sl_dipoleRecoilOff"),
  ("nof_files",                       2),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99985562e+05, 3.99997156e+05, 3.99932031e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99985562e+05, 3.99985562e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99974800e+06, 3.99977700e+06, 3.99977700e+06, 3.99974925e+06, 3.99977700e+06, 3.99974750e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99855312e+05, 3.99750125e+05, 5.68531875e+05, 3.99916688e+05, 3.99692469e+05, 2.46074625e+05, ],
    'CountWeightedFull'                                                              : [ 3.99691250e+05, 3.99700469e+05, 3.99641938e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99691250e+05, 3.99691250e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99682525e+06, 3.99682525e+06, 3.99682525e+06, 3.99682525e+06, 3.99682525e+06, 3.99682525e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99655719e+05, 3.99458125e+05, 5.68112312e+05, 3.99716875e+05, 3.99391969e+05, 2.45951219e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1933859355), # 1.93GB, avg file size 966.93MB
  ("fsize_db",                        26407229036), # 26.41GB, avg file size 1.32GB
  ("use_it",                          True),
  ("xsection",                        0.00118359),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_nonresonant_0p5_1_1_hh_2b2v_sl_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFHHTo2B2WToLNu2J_CV_1_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1p5_1_1_hh_bbvv_sl"),
  ("process_name_specific",           "signal_vbf_nonresonant_1p5_1_1_hh_2b2v_sl_dipoleRecoilOff"),
  ("nof_files",                       3),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 399999, ],
    'CountWeighted'                                                                  : [ 3.99946062e+05, 3.99944969e+05, 3.99951156e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99946062e+05, 3.99946062e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99924250e+06, 3.99929325e+06, 3.99929325e+06, 3.99924300e+06, 3.99929325e+06, 3.99924250e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99850562e+05, 4.00146250e+05, 5.67797125e+05, 3.99853188e+05, 3.99309562e+05, 2.46663812e+05, ],
    'CountWeightedFull'                                                              : [ 3.99690656e+05, 3.99689719e+05, 3.99695219e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99690656e+05, 3.99690656e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99675650e+06, 3.99675650e+06, 3.99675650e+06, 3.99675650e+06, 3.99675650e+06, 3.99675650e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99665188e+05, 3.99893969e+05, 5.67432375e+05, 3.99666750e+05, 3.99048094e+05, 2.46549188e+05, ],
  }),
  ("nof_tree_events",                 399999),
  ("nof_db_events",                   399999),
  ("fsize_local",                     1804537356), # 1.80GB, avg file size 601.51MB
  ("fsize_db",                        24759957662), # 24.76GB, avg file size 1.30GB
  ("use_it",                          True),
  ("xsection",                        0.007219242),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1p5_1_1_hh_2b2v_sl_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFHHTo2B2WToLNu2J_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_0_1_hh_bbvv_sl"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_0_1_hh_2b2v_sl_dipoleRecoilOff"),
  ("nof_files",                       2),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 399995, ],
    'CountWeighted'                                                                  : [ 4.00012375e+05, 4.00000562e+05, 3.99960250e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.00012375e+05, 4.00012375e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99992675e+06, 3.99997875e+06, 3.99997875e+06, 3.99992600e+06, 3.99997875e+06, 3.99992575e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99845250e+05, 3.99975500e+05, 5.67785375e+05, 4.00005094e+05, 3.99265688e+05, 2.46483391e+05, ],
    'CountWeightedFull'                                                              : [ 3.99751469e+05, 3.99736938e+05, 3.99705469e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99751469e+05, 3.99751469e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99733500e+06, 3.99733500e+06, 3.99733500e+06, 3.99733500e+06, 3.99733500e+06, 3.99733500e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99655500e+05, 3.99716312e+05, 5.67423438e+05, 3.99814938e+05, 3.99007938e+05, 2.46366344e+05, ],
  }),
  ("nof_tree_events",                 399995),
  ("nof_db_events",                   399995),
  ("fsize_local",                     1860110474), # 1.86GB, avg file size 930.06MB
  ("fsize_db",                        25812987479), # 25.81GB, avg file size 1.29GB
  ("use_it",                          True),
  ("xsection",                        0.002961249),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_0_1_hh_2b2v_sl_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToRadionToHHTo2B2Tau_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_250_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_250_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99927375e+05, 3.99956875e+05, 3.99897906e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99927375e+05, 3.99927375e+05, ],
    'CountWeightedFull'                                                              : [ 3.99889906e+05, 3.99919125e+05, 3.99859750e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99889906e+05, 3.99889906e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     2038640056), # 2.04GB, avg file size 2.04GB
  ("fsize_db",                        24201103622), # 24.20GB, avg file size 1.51GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin0_250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToRadionToHHTo2B2Tau_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_260_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_260_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99915000e+05, 4.00012281e+05, 3.99975844e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99915000e+05, 3.99915000e+05, ],
    'CountWeightedFull'                                                              : [ 3.99874969e+05, 3.99970812e+05, 3.99934625e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99874969e+05, 3.99874969e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     2068382597), # 2.07GB, avg file size 2.07GB
  ("fsize_db",                        24429994840), # 24.43GB, avg file size 1.16GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin0_260_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToRadionToHHTo2B2Tau_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_270_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_270_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 384000, ],
    'CountWeighted'                                                                  : [ 3.83914156e+05, 3.83962469e+05, 3.84048000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.83914156e+05, 3.83914156e+05, ],
    'CountWeightedFull'                                                              : [ 3.83874438e+05, 3.83921688e+05, 3.84006812e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.83874438e+05, 3.83874438e+05, ],
  }),
  ("nof_tree_events",                 384000),
  ("nof_db_events",                   384000),
  ("fsize_local",                     2012922249), # 2.01GB, avg file size 2.01GB
  ("fsize_db",                        23560021919), # 23.56GB, avg file size 1.39GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin0_270_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToRadionToHHTo2B2Tau_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_280_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_280_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                                          : [ 378000, ],
    'CountWeighted'                                                                  : [ 3.77940406e+05, 3.78002750e+05, 3.77900031e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.77940406e+05, 3.77940406e+05, ],
    'CountWeightedFull'                                                              : [ 3.77901969e+05, 3.77963500e+05, 3.77862062e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.77901969e+05, 3.77901969e+05, ],
  }),
  ("nof_tree_events",                 378000),
  ("nof_db_events",                   378000),
  ("fsize_local",                     2005279568), # 2.01GB, avg file size 2.01GB
  ("fsize_db",                        23422801619), # 23.42GB, avg file size 1.02GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin0_280_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToRadionToHHTo2B2Tau_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_300_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_300_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99951000e+05, 2.99912906e+05, 2.99920875e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.99951000e+05, 2.99951000e+05, ],
    'CountWeightedFull'                                                              : [ 2.99918531e+05, 2.99880406e+05, 2.99889031e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.99918531e+05, 2.99918531e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1629659367), # 1.63GB, avg file size 1.63GB
  ("fsize_db",                        18779481578), # 18.78GB, avg file size 1.25GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin0_300_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToRadionToHHTo2B2Tau_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_320_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_320_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 268000, ],
    'CountWeighted'                                                                  : [ 2.67981688e+05, 2.67969719e+05, 2.67950125e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.48427500e+05, 3.20557156e+05, 2.95995031e+05, 2.91303375e+05, 2.67981688e+05, 2.47389797e+05, 2.47330078e+05, 2.27476891e+05, 2.09990609e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.48427656e+05, 2.09990500e+05, ],
    'CountWeightedFull'                                                              : [ 2.67951625e+05, 2.67939625e+05, 2.67920031e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.48388188e+05, 3.20521312e+05, 2.95962125e+05, 2.91270438e+05, 2.67951625e+05, 2.47362172e+05, 2.47302156e+05, 2.27451438e+05, 2.09967125e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.48388344e+05, 2.09967000e+05, ],
  }),
  ("nof_tree_events",                 268000),
  ("nof_db_events",                   268000),
  ("fsize_local",                     1466508276), # 1.47GB, avg file size 1.47GB
  ("fsize_db",                        16443985477), # 16.44GB, avg file size 967.29MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin0_320_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToRadionToHHTo2B2Tau_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_350_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_350_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99878812e+05, 2.99896188e+05, 2.99884219e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.99878812e+05, 2.99878812e+05, ],
    'CountWeightedFull'                                                              : [ 2.99845844e+05, 2.99863062e+05, 2.99850906e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.99845844e+05, 2.99845844e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1710029230), # 1.71GB, avg file size 1.71GB
  ("fsize_db",                        19234659018), # 19.23GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin0_350_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToRadionToHHTo2B2Tau_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_400_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_400_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 284000, ],
    'CountWeighted'                                                                  : [ 2.83888000e+05, 2.83918250e+05, 2.83917562e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.83888000e+05, 2.83888000e+05, ],
    'CountWeightedFull'                                                              : [ 2.83854500e+05, 2.83884750e+05, 2.83882938e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.83854500e+05, 2.83854500e+05, ],
  }),
  ("nof_tree_events",                 284000),
  ("nof_db_events",                   284000),
  ("fsize_local",                     1681246733), # 1.68GB, avg file size 1.68GB
  ("fsize_db",                        18538011629), # 18.54GB, avg file size 1.54GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin0_400_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToRadionToHHTo2B2Tau_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_450_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_450_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99941156e+05, 2.99824156e+05, 2.99802375e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.99941156e+05, 2.99941156e+05, ],
    'CountWeightedFull'                                                              : [ 2.99901406e+05, 2.99786938e+05, 2.99764375e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.99901406e+05, 2.99901406e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1833602427), # 1.83GB, avg file size 1.83GB
  ("fsize_db",                        19880260071), # 19.88GB, avg file size 1.42GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin0_450_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToRadionToHHTo2B2Tau_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_500_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_500_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99925719e+05, 2.99977844e+05, 2.99861125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.99925719e+05, 2.99925719e+05, ],
    'CountWeightedFull'                                                              : [ 2.99884938e+05, 2.99936500e+05, 2.99821156e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.99884938e+05, 2.99884938e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1883850283), # 1.88GB, avg file size 1.88GB
  ("fsize_db",                        20164079086), # 20.16GB, avg file size 1.44GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin0_500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToRadionToHHTo2B2Tau_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_550_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_550_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 292000, ],
    'CountWeighted'                                                                  : [ 2.91929812e+05, 2.91936219e+05, 2.91920031e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.91929812e+05, 2.91929812e+05, ],
    'CountWeightedFull'                                                              : [ 2.91890875e+05, 2.91897438e+05, 2.91880375e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.91890875e+05, 2.91890875e+05, ],
  }),
  ("nof_tree_events",                 292000),
  ("nof_db_events",                   292000),
  ("fsize_local",                     1873047006), # 1.87GB, avg file size 1.87GB
  ("fsize_db",                        20001572830), # 20.00GB, avg file size 1.11GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin0_550_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToRadionToHHTo2B2Tau_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_600_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_600_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99931656e+05, 1.99955000e+05, 1.99922703e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99931656e+05, 1.99931656e+05, ],
    'CountWeightedFull'                                                              : [ 1.99901562e+05, 1.99925156e+05, 1.99893531e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99901562e+05, 1.99901562e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1308264886), # 1.31GB, avg file size 1.31GB
  ("fsize_db",                        13832525612), # 13.83GB, avg file size 1.38GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin0_600_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToRadionToHHTo2B2Tau_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_650_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_650_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 192000, ],
    'CountWeighted'                                                                  : [ 1.91889188e+05, 1.91906906e+05, 1.91878844e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.91889188e+05, 1.91889188e+05, ],
    'CountWeightedFull'                                                              : [ 1.91860062e+05, 1.91877656e+05, 1.91850906e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.91860062e+05, 1.91860062e+05, ],
  }),
  ("nof_tree_events",                 192000),
  ("nof_db_events",                   192000),
  ("fsize_local",                     1275177132), # 1.28GB, avg file size 1.28GB
  ("fsize_db",                        13520238121), # 13.52GB, avg file size 901.35MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin0_650_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToRadionToHHTo2B2Tau_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_700_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_700_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99889766e+05, 1.99886969e+05, 1.99878844e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99889766e+05, 1.99889766e+05, ],
    'CountWeightedFull'                                                              : [ 1.99857266e+05, 1.99854688e+05, 1.99846156e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99857266e+05, 1.99857266e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1345374018), # 1.35GB, avg file size 1.35GB
  ("fsize_db",                        14128746298), # 14.13GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin0_700_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToRadionToHHTo2B2Tau_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_750_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_750_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 192000, ],
    'CountWeighted'                                                                  : [ 1.91921625e+05, 1.91902078e+05, 1.91916469e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.91921625e+05, 1.91921625e+05, ],
    'CountWeightedFull'                                                              : [ 1.91890266e+05, 1.91871188e+05, 1.91884766e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.91890266e+05, 1.91890266e+05, ],
  }),
  ("nof_tree_events",                 192000),
  ("nof_db_events",                   192000),
  ("fsize_local",                     1306489263), # 1.31GB, avg file size 1.31GB
  ("fsize_db",                        13657644591), # 13.66GB, avg file size 1.37GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin0_750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToRadionToHHTo2B2Tau_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_800_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_800_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99907719e+05, 1.99879719e+05, 1.99894719e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99907719e+05, 1.99907719e+05, ],
    'CountWeightedFull'                                                              : [ 1.99872938e+05, 1.99845344e+05, 1.99859844e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99872938e+05, 1.99872938e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1376141060), # 1.38GB, avg file size 1.38GB
  ("fsize_db",                        14483792512), # 14.48GB, avg file size 851.99MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin0_800_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToRadionToHHTo2B2Tau_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_850_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_850_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99902625e+05, 1.99879562e+05, 1.99902719e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99902625e+05, 1.99902625e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99884775e+06, 1.99884775e+06, 1.99884775e+06, 1.99884775e+06, 1.99884775e+06, 1.99884775e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.00120609e+05, 1.99812000e+05, 3.11656625e+05, 1.99833750e+05, 1.98715844e+05, 1.01117570e+05, ],
    'CountWeightedFull'                                                              : [ 1.99869828e+05, 1.99846859e+05, 1.99869500e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99869828e+05, 1.99869828e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.99852125e+06, 1.99852125e+06, 1.99852125e+06, 1.99852125e+06, 1.99852125e+06, 1.99852125e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.00089422e+05, 1.99780266e+05, 3.11604656e+05, 1.99798906e+05, 1.98681766e+05, 1.01101250e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1392246402), # 1.39GB, avg file size 1.39GB
  ("fsize_db",                        15269843874), # 15.27GB, avg file size 1.91GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin0_850_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToRadionToHHTo2B2Tau_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_900_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_900_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99880781e+05, 1.99841578e+05, 1.99790125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99880781e+05, 1.99880781e+05, ],
    'CountWeightedFull'                                                              : [ 1.99845406e+05, 1.99806938e+05, 1.99756984e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99845406e+05, 1.99845406e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1398223982), # 1.40GB, avg file size 1.40GB
  ("fsize_db",                        14720486395), # 14.72GB, avg file size 774.76MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin0_900_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToRadionToHHTo2B2Tau_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_1000_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_1000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99381641e+04, 9.99368828e+04, 9.99369609e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99381641e+04, 9.99381641e+04, ],
    'CountWeightedFull'                                                              : [ 9.99213984e+04, 9.99198984e+04, 9.99201328e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99213984e+04, 9.99213984e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     707741108), # 707.74MB, avg file size 707.74MB
  ("fsize_db",                        7497593534), # 7.50GB, avg file size 624.80MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin0_1000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToRadionToHHTo2B2Tau_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_1250_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_1250_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.98748203e+04, 9.98515781e+04, 9.98751094e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.98748203e+04, 9.98748203e+04, ],
    'CountWeightedFull'                                                              : [ 9.98562500e+04, 9.98335938e+04, 9.98566094e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.98562500e+04, 9.98562500e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     717871395), # 717.87MB, avg file size 717.87MB
  ("fsize_db",                        7602021628), # 7.60GB, avg file size 760.20MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin0_1250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToRadionToHHTo2B2Tau_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_1500_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_1500_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.98401250e+04, 9.98451016e+04, 9.98379375e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.98401250e+04, 9.98401250e+04, ],
    'CountWeightedFull'                                                              : [ 9.98179375e+04, 9.98224062e+04, 9.98162656e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.98179375e+04, 9.98179375e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     723275353), # 723.28MB, avg file size 723.28MB
  ("fsize_db",                        7687388828), # 7.69GB, avg file size 854.15MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin0_1500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToRadionToHHTo2B2Tau_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_1750_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_1750_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 91000, ],
    'CountWeighted'                                                                  : [ 9.08024141e+04, 9.08142969e+04, 9.07911094e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.08024141e+04, 9.08024141e+04, ],
    'CountWeightedFull'                                                              : [ 9.07806875e+04, 9.07922031e+04, 9.07693906e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.07806875e+04, 9.07806875e+04, ],
  }),
  ("nof_tree_events",                 91000),
  ("nof_db_events",                   91000),
  ("fsize_local",                     658311651), # 658.31MB, avg file size 658.31MB
  ("fsize_db",                        7052793193), # 7.05GB, avg file size 881.60MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin0_1750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToRadionToHHTo2B2Tau_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_2000_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_2000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 84000, ],
    'CountWeighted'                                                                  : [ 8.36952266e+04, 8.36951641e+04, 8.36963750e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 8.36952266e+04, 8.36952266e+04, ],
    'CountWeightedFull'                                                              : [ 8.36748359e+04, 8.36754062e+04, 8.36755000e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 8.36748359e+04, 8.36748359e+04, ],
  }),
  ("nof_tree_events",                 84000),
  ("nof_db_events",                   84000),
  ("fsize_local",                     607981139), # 607.98MB, avg file size 607.98MB
  ("fsize_db",                        6693361558), # 6.69GB, avg file size 557.78MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin0_2000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToRadionToHHTo2B2Tau_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_3000_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_3000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.88680781e+04, 9.88672500e+04, 9.88706016e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.88680781e+04, 9.88680781e+04, ],
    'CountWeightedFull'                                                              : [ 9.88388750e+04, 9.88385391e+04, 9.88414609e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.88388750e+04, 9.88388750e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     723934552), # 723.93MB, avg file size 723.93MB
  ("fsize_db",                        8103387579), # 8.10GB, avg file size 623.34MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin0_3000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToBulkGravitonToHHTo2B2Tau_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_250_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_250_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.94418688e+05, 3.94387312e+05, 3.94447125e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.33566781e+05, 3.95781938e+05, 3.64336750e+05, 4.32041938e+05, 3.94416062e+05, 3.63103688e+05, 4.30850156e+05, 3.93350031e+05, 3.62141688e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.35378750e+05, 3.60388125e+05, ],
    'CountWeightedFull'                                                              : [ 3.94282000e+05, 3.94258219e+05, 3.94307938e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.33427562e+05, 3.95645094e+05, 3.64205844e+05, 4.31903094e+05, 3.94279500e+05, 3.62972938e+05, 4.30711406e+05, 3.93213562e+05, 3.62011094e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.35236688e+05, 3.60260312e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     2102929416), # 2.10GB, avg file size 2.10GB
  ("fsize_db",                        24231856380), # 24.23GB, avg file size 1.51GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin2_250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToBulkGravitonToHHTo2B2Tau_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_260_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_260_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    25),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.96165812e+05, 3.96169125e+05, 3.96256281e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.25707312e+05, 3.97485312e+05, 3.72997531e+05, 4.24260594e+05, 3.96165812e+05, 3.71788188e+05, 4.23141188e+05, 3.95146312e+05, 3.70853469e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.29960844e+05, 3.66687188e+05, ],
    'CountWeightedFull'                                                              : [ 3.96049000e+05, 3.96050000e+05, 3.96141656e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.25586875e+05, 3.97368344e+05, 3.72884625e+05, 4.24140344e+05, 3.96049000e+05, 3.71675344e+05, 4.23021031e+05, 3.95029594e+05, 3.70740781e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.29838188e+05, 3.66576594e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1898565250), # 1.90GB, avg file size 1.90GB
  ("fsize_db",                        22967054769), # 22.97GB, avg file size 918.68MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin2_260_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToBulkGravitonToHHTo2B2Tau_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_270_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_270_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    25),
  ("nof_events",                      {
    'Count'                                                                          : [ 384000, ],
    'CountWeighted'                                                                  : [ 3.80493344e+05, 3.80366875e+05, 3.80450656e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.09013062e+05, 3.81721750e+05, 3.57944656e+05, 4.07663188e+05, 3.80491219e+05, 3.56817625e+05, 4.06618250e+05, 3.79538750e+05, 3.55946344e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.12938312e+05, 3.52109469e+05, ],
    'CountWeightedFull'                                                              : [ 3.80368125e+05, 3.80248625e+05, 3.80325156e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.08879750e+05, 3.81596312e+05, 3.57823844e+05, 4.07530062e+05, 3.80365969e+05, 3.56696938e+05, 4.06485250e+05, 3.79413625e+05, 3.55825781e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.12800781e+05, 3.51993344e+05, ],
  }),
  ("nof_tree_events",                 384000),
  ("nof_db_events",                   384000),
  ("fsize_local",                     1823092466), # 1.82GB, avg file size 1.82GB
  ("fsize_db",                        21814983036), # 21.81GB, avg file size 872.60MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin2_270_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToBulkGravitonToHHTo2B2Tau_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_280_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_280_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 356000, ],
    'CountWeighted'                                                                  : [ 3.52612375e+05, 3.52583500e+05, 3.52552562e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.79233219e+05, 3.53712750e+05, 3.31507188e+05, 3.78023344e+05, 3.52612375e+05, 3.30501344e+05, 3.77085500e+05, 3.51759875e+05, 3.29722625e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.82760219e+05, 3.26274781e+05, ],
    'CountWeightedFull'                                                              : [ 3.52510750e+05, 3.52487188e+05, 3.52455938e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.79131156e+05, 3.53611000e+05, 3.31412562e+05, 3.77921438e+05, 3.52510750e+05, 3.30406844e+05, 3.76983594e+05, 3.51658438e+05, 3.29628125e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.82656750e+05, 3.26181688e+05, ],
  }),
  ("nof_tree_events",                 356000),
  ("nof_db_events",                   356000),
  ("fsize_local",                     1691690335), # 1.69GB, avg file size 1.69GB
  ("fsize_db",                        20210387059), # 20.21GB, avg file size 1.12GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin2_280_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToBulkGravitonToHHTo2B2Tau_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_300_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_300_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.97178750e+05, 2.97178906e+05, 2.97192906e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.20121781e+05, 2.98036000e+05, 2.78880625e+05, 3.19178219e+05, 2.97178750e+05, 2.78097406e+05, 3.18446906e+05, 2.96514500e+05, 2.77490688e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.22840625e+05, 2.74843719e+05, ],
    'CountWeightedFull'                                                              : [ 2.97108625e+05, 2.97108250e+05, 2.97119781e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.20049594e+05, 2.97965750e+05, 2.78809875e+05, 3.19106125e+05, 2.97108625e+05, 2.78026781e+05, 3.18374875e+05, 2.96444312e+05, 2.77420125e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.22766594e+05, 2.74774938e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1428729097), # 1.43GB, avg file size 1.43GB
  ("fsize_db",                        17244807583), # 17.24GB, avg file size 907.62MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin2_300_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToBulkGravitonToHHTo2B2Tau_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_320_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_320_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.97162406e+05, 2.97168062e+05, 2.97186812e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.20678531e+05, 2.97970844e+05, 2.78353000e+05, 3.19783969e+05, 2.97159875e+05, 2.77613625e+05, 3.19089938e+05, 2.96531000e+05, 2.77040219e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.23206188e+05, 2.74583719e+05, ],
    'CountWeightedFull'                                                              : [ 2.97069562e+05, 2.97076000e+05, 2.97089594e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.20579312e+05, 2.97877719e+05, 2.78263438e+05, 3.19685125e+05, 2.97067031e+05, 2.77524312e+05, 3.18991344e+05, 2.96438375e+05, 2.76951062e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.23105438e+05, 2.74496094e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1430752288), # 1.43GB, avg file size 1.43GB
  ("fsize_db",                        17220173981), # 17.22GB, avg file size 956.68MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin2_320_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToBulkGravitonToHHTo2B2Tau_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_350_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_350_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 290000, ],
    'CountWeighted'                                                                  : [ 2.87416312e+05, 2.87371312e+05, 2.87402062e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.11047250e+05, 2.88135250e+05, 2.68399688e+05, 3.10250562e+05, 2.87416312e+05, 2.67746125e+05, 3.09631062e+05, 2.86856875e+05, 2.67238438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.13222688e+05, 2.65133875e+05, ],
    'CountWeightedFull'                                                              : [ 2.87320312e+05, 2.87277875e+05, 2.87305312e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.10948375e+05, 2.88039219e+05, 2.68307906e+05, 3.10151844e+05, 2.87320312e+05, 2.67654406e+05, 3.09532406e+05, 2.86761062e+05, 2.67146750e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.13119500e+05, 2.65046406e+05, ],
  }),
  ("nof_tree_events",                 290000),
  ("nof_db_events",                   290000),
  ("fsize_local",                     1387243449), # 1.39GB, avg file size 1.39GB
  ("fsize_db",                        16301770062), # 16.30GB, avg file size 857.99MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin2_350_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToBulkGravitonToHHTo2B2Tau_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_400_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_400_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 284000, ],
    'CountWeighted'                                                                  : [ 2.81309625e+05, 2.81267500e+05, 2.81245812e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.05889875e+05, 2.81910219e+05, 2.61372062e+05, 3.05211656e+05, 2.81300938e+05, 2.60820844e+05, 3.04682312e+05, 2.80825062e+05, 2.60390984e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.07635812e+05, 2.58722969e+05, ],
    'CountWeightedFull'                                                              : [ 2.81227875e+05, 2.81187781e+05, 2.81165406e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.05812312e+05, 2.81828656e+05, 2.61293938e+05, 3.05134094e+05, 2.81219438e+05, 2.60742781e+05, 3.04604875e+05, 2.80743688e+05, 2.60312969e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.07555250e+05, 2.58647938e+05, ],
  }),
  ("nof_tree_events",                 284000),
  ("nof_db_events",                   284000),
  ("fsize_local",                     1365897617), # 1.37GB, avg file size 1.37GB
  ("fsize_db",                        16196623550), # 16.20GB, avg file size 1.35GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin2_400_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToBulkGravitonToHHTo2B2Tau_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_450_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_450_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 295000, ],
    'CountWeighted'                                                                  : [ 2.92068250e+05, 2.92030500e+05, 2.91993188e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.19385250e+05, 2.92579281e+05, 2.69887250e+05, 3.18813906e+05, 2.92068250e+05, 2.69426094e+05, 3.18367812e+05, 2.91668188e+05, 2.69066062e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.20876062e+05, 2.67654812e+05, ],
    'CountWeightedFull'                                                              : [ 2.91982938e+05, 2.91947531e+05, 2.91912406e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.19302188e+05, 2.92493875e+05, 2.69805781e+05, 3.18731000e+05, 2.91982938e+05, 2.69344719e+05, 3.18284938e+05, 2.91583000e+05, 2.68984688e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.20789500e+05, 2.67576844e+05, ],
  }),
  ("nof_tree_events",                 295000),
  ("nof_db_events",                   295000),
  ("fsize_local",                     1429380324), # 1.43GB, avg file size 1.43GB
  ("fsize_db",                        16589766784), # 16.59GB, avg file size 829.49MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin2_450_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToBulkGravitonToHHTo2B2Tau_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_500_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_500_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.96841281e+05, 2.96936781e+05, 2.96870531e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.26426969e+05, 2.97285250e+05, 2.73019312e+05, 3.25929312e+05, 2.96841281e+05, 2.72620938e+05, 3.25539625e+05, 2.96494625e+05, 2.72309188e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.27711312e+05, 2.71103219e+05, ],
    'CountWeightedFull'                                                              : [ 2.96754188e+05, 2.96847156e+05, 2.96784281e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.26336031e+05, 2.97198094e+05, 2.72936906e+05, 3.25838375e+05, 2.96754188e+05, 2.72538562e+05, 3.25448719e+05, 2.96407562e+05, 2.72226875e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.27618312e+05, 2.71023000e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1464901539), # 1.46GB, avg file size 1.46GB
  ("fsize_db",                        16882301821), # 16.88GB, avg file size 1.30GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin2_500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToBulkGravitonToHHTo2B2Tau_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_600_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_600_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 192000, ],
    'CountWeighted'                                                                  : [ 1.89876344e+05, 1.89804250e+05, 1.89881719e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.10935469e+05, 1.90076062e+05, 1.72856062e+05, 2.10709750e+05, 1.89876344e+05, 1.72677703e+05, 2.10532500e+05, 1.89719062e+05, 1.72537531e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.11577906e+05, 1.71950750e+05, ],
    'CountWeightedFull'                                                              : [ 1.89813203e+05, 1.89746031e+05, 1.89818156e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.10868578e+05, 1.90012891e+05, 1.72800359e+05, 2.10642906e+05, 1.89813203e+05, 1.72622000e+05, 2.10465656e+05, 1.89655938e+05, 1.72481844e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.11510812e+05, 1.71895266e+05, ],
  }),
  ("nof_tree_events",                 192000),
  ("nof_db_events",                   192000),
  ("fsize_local",                     952229116), # 952.23MB, avg file size 952.23MB
  ("fsize_db",                        11104772663), # 11.10GB, avg file size 854.21MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin2_600_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToBulkGravitonToHHTo2B2Tau_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_650_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_650_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.97556609e+05, 1.97562328e+05, 1.97574172e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.20615250e+05, 1.97729641e+05, 1.79056031e+05, 2.20419266e+05, 1.97556609e+05, 1.78901719e+05, 2.20265078e+05, 1.97420234e+05, 1.78780531e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.21148141e+05, 1.78309438e+05, ],
    'CountWeightedFull'                                                              : [ 1.97496625e+05, 1.97503906e+05, 1.97512266e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.20551312e+05, 1.97669562e+05, 1.79000094e+05, 2.20355406e+05, 1.97496625e+05, 1.78845797e+05, 2.20201219e+05, 1.97360219e+05, 1.78724656e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.21083656e+05, 1.78254188e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     999920417), # 999.92MB, avg file size 999.92MB
  ("fsize_db",                        11488161488), # 11.49GB, avg file size 1.04GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin2_650_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToBulkGravitonToHHTo2B2Tau_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_700_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_700_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.97224812e+05, 1.97186594e+05, 1.97203422e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.21374188e+05, 1.97365625e+05, 1.77891047e+05, 2.21214375e+05, 1.97224812e+05, 1.77765875e+05, 2.21088266e+05, 1.97113672e+05, 1.77667219e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.21853484e+05, 1.77249562e+05, ],
    'CountWeightedFull'                                                              : [ 1.97168547e+05, 1.97131062e+05, 1.97148109e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.21315797e+05, 1.97309359e+05, 1.77838625e+05, 2.21155969e+05, 1.97168547e+05, 1.77713500e+05, 2.21029938e+05, 1.97057469e+05, 1.77614844e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.21792453e+05, 1.77199906e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1005051398), # 1.01GB, avg file size 1.01GB
  ("fsize_db",                        11488642680), # 11.49GB, avg file size 957.39MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin2_700_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToBulkGravitonToHHTo2B2Tau_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_750_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_750_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.97119828e+05, 1.97171406e+05, 1.97176656e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.22372656e+05, 1.97243469e+05, 1.77157969e+05, 2.22231688e+05, 1.97119828e+05, 1.77048594e+05, 2.22120688e+05, 1.97022469e+05, 1.76962234e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.22823000e+05, 1.76575469e+05, ],
    'CountWeightedFull'                                                              : [ 1.97064938e+05, 1.97115719e+05, 1.97120016e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.22315062e+05, 1.97188578e+05, 1.77105516e+05, 2.22174094e+05, 1.97064938e+05, 1.76996172e+05, 2.22063078e+05, 1.96967562e+05, 1.76909781e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.22764406e+05, 1.76523938e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1011012173), # 1.01GB, avg file size 1.01GB
  ("fsize_db",                        11534875410), # 11.53GB, avg file size 823.92MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin2_750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToBulkGravitonToHHTo2B2Tau_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_850_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_850_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.96775656e+05, 1.96811969e+05, 1.96801219e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.24022562e+05, 1.96863125e+05, 1.75383297e+05, 2.23922297e+05, 1.96775656e+05, 1.75306172e+05, 2.23843047e+05, 1.96706500e+05, 1.75245109e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.24370219e+05, 1.74957938e+05, ],
    'CountWeightedFull'                                                              : [ 1.96716422e+05, 1.96750328e+05, 1.96739062e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.23959453e+05, 1.96803891e+05, 1.75325375e+05, 2.23859188e+05, 1.96716422e+05, 1.75248266e+05, 2.23779969e+05, 1.96647281e+05, 1.75187312e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.24301531e+05, 1.74905656e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1019516660), # 1.02GB, avg file size 1.02GB
  ("fsize_db",                        11437184170), # 11.44GB, avg file size 1.14GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin2_850_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToBulkGravitonToHHTo2B2Tau_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_900_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_900_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.96671297e+05, 1.96717016e+05, 1.96644172e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.24826172e+05, 1.96752875e+05, 1.74646469e+05, 2.24732438e+05, 1.96671172e+05, 1.74574484e+05, 2.24658188e+05, 1.96606500e+05, 1.74517625e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.25144938e+05, 1.74267844e+05, ],
    'CountWeightedFull'                                                              : [ 1.96621375e+05, 1.96666578e+05, 1.96595812e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.24775922e+05, 1.96702906e+05, 1.74599125e+05, 2.24682219e+05, 1.96621203e+05, 1.74527188e+05, 2.24608016e+05, 1.96556594e+05, 1.74470297e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.25090531e+05, 1.74224625e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1023430982), # 1.02GB, avg file size 1.02GB
  ("fsize_db",                        11390511587), # 11.39GB, avg file size 1.63GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin2_900_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToBulkGravitonToHHTo2B2Tau_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_1000_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_1000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.81150391e+04, 9.81235938e+04, 9.81276250e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.13121375e+05, 9.81468594e+04, 8.65213203e+04, 1.13083469e+05, 9.81139375e+04, 8.64924922e+04, 1.13053297e+05, 9.80878047e+04, 8.64695938e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.13260195e+05, 8.63665156e+04, ],
    'CountWeightedFull'                                                              : [ 9.80924609e+04, 9.81002578e+04, 9.81044141e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.13096656e+05, 9.81242344e+04, 8.64982578e+04, 1.13058719e+05, 9.80913125e+04, 8.64694141e+04, 1.13028555e+05, 9.80652031e+04, 8.64465391e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.13234375e+05, 8.63445000e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     514894328), # 514.89MB, avg file size 514.89MB
  ("fsize_db",                        5853097024), # 5.85GB, avg file size 650.34MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin2_1000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToBulkGravitonToHHTo2B2Tau_M-1200_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_1200_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_1200_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.76431094e+04, 9.76540469e+04, 9.76301328e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.14311289e+05, 9.76697344e+04, 8.49384688e+04, 1.14280375e+05, 9.76431094e+04, 8.49152812e+04, 1.14255750e+05, 9.76218750e+04, 8.48968359e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.14418086e+05, 8.48290781e+04, ],
    'CountWeightedFull'                                                              : [ 9.76205000e+04, 9.76307031e+04, 9.76082266e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.14288312e+05, 9.76471328e+04, 8.49171172e+04, 1.14257391e+05, 9.76205000e+04, 8.48939219e+04, 1.14232773e+05, 9.75992891e+04, 8.48754609e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.14395086e+05, 8.48077188e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     518866054), # 518.87MB, avg file size 518.87MB
  ("fsize_db",                        5865949865), # 5.87GB, avg file size 1.96GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin2_1200_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToBulkGravitonToHHTo2B2Tau_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_1750_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_1750_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.62268516e+04, 9.62350469e+04, 9.61961562e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.17004086e+05, 9.62375859e+04, 8.10774766e+04, 1.16991398e+05, 9.62268516e+04, 8.10683203e+04, 1.16981258e+05, 9.62182422e+04, 8.10609219e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.17070859e+05, 8.10336562e+04, ],
    'CountWeightedFull'                                                              : [ 9.62128438e+04, 9.62222031e+04, 9.61820234e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.16991797e+05, 9.62235703e+04, 8.10636328e+04, 1.16979102e+05, 9.62128438e+04, 8.10544688e+04, 1.16968961e+05, 9.62042344e+04, 8.10470781e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.17057375e+05, 8.10209609e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     508665371), # 508.67MB, avg file size 508.67MB
  ("fsize_db",                        5885960863), # 5.89GB, avg file size 840.85MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin2_1750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFToBulkGravitonToHHTo2B2Tau_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_2000_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_2000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.51885469e+04, 9.51667344e+04, 9.51816719e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.17551031e+05, 9.51981562e+04, 7.91664531e+04, 1.17539633e+05, 9.51885469e+04, 7.91582500e+04, 1.17530469e+05, 9.51808047e+04, 7.91516641e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.17576312e+05, 7.91631250e+04, ],
    'CountWeightedFull'                                                              : [ 9.51771328e+04, 9.51568672e+04, 9.51696562e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.17545172e+05, 9.51867422e+04, 7.91531641e+04, 1.17533773e+05, 9.51771328e+04, 7.91449844e+04, 1.17524609e+05, 9.51694141e+04, 7.91383984e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.17568070e+05, 7.91522578e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     505645242), # 505.65MB, avg file size 505.65MB
  ("fsize_db",                        6034285592), # 6.03GB, avg file size 670.48MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_spin2_2000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2Tau_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_250_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_250_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99902500e+05, 3.99916812e+05, 3.99971562e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99902500e+05, 3.99902500e+05, ],
    'CountWeightedFull'                                                              : [ 3.99880625e+05, 3.99894250e+05, 3.99949250e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99880625e+05, 3.99880625e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1357028698), # 1.36GB, avg file size 1.36GB
  ("fsize_db",                        20240174056), # 20.24GB, avg file size 1.69GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2Tau_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_260_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_260_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 384000, ],
    'CountWeighted'                                                                  : [ 3.83900500e+05, 3.83973719e+05, 3.83953906e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.89955062e+05, 3.83900500e+05, 3.75506000e+05, 3.89955062e+05, 3.83900500e+05, 3.75506000e+05, 3.89955062e+05, 3.83900500e+05, 3.75506000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.89955062e+05, 3.75506000e+05, ],
    'CountWeightedFull'                                                              : [ 3.83878969e+05, 3.83951344e+05, 3.83931500e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.89932469e+05, 3.83878969e+05, 3.75484344e+05, 3.89932469e+05, 3.83878969e+05, 3.75484344e+05, 3.89932469e+05, 3.83878969e+05, 3.75484344e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.89932469e+05, 3.75484344e+05, ],
  }),
  ("nof_tree_events",                 384000),
  ("nof_db_events",                   384000),
  ("fsize_local",                     1314502865), # 1.31GB, avg file size 1.31GB
  ("fsize_db",                        18565212926), # 18.57GB, avg file size 977.12MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_260_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2Tau_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_270_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_270_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 4.00017375e+05, 3.99935938e+05, 4.00010625e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.07463469e+05, 4.00016812e+05, 3.90129469e+05, 4.07463469e+05, 4.00016812e+05, 3.90129469e+05, 4.07463469e+05, 4.00016812e+05, 3.90129469e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.07463469e+05, 3.90129469e+05, ],
    'CountWeightedFull'                                                              : [ 3.99992469e+05, 3.99911938e+05, 3.99986719e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.07439438e+05, 3.99991875e+05, 3.90106312e+05, 4.07439438e+05, 3.99991875e+05, 3.90106312e+05, 4.07439438e+05, 3.99991875e+05, 3.90106312e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.07439438e+05, 3.90106312e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1389301514), # 1.39GB, avg file size 1.39GB
  ("fsize_db",                        19438730085), # 19.44GB, avg file size 1.02GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_270_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2Tau_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_280_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_280_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 394000, ],
    'CountWeighted'                                                                  : [ 3.93971688e+05, 3.93925312e+05, 3.94012438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.93971688e+05, 3.93971688e+05, ],
    'CountWeightedFull'                                                              : [ 3.93948750e+05, 3.93902500e+05, 3.93989625e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.93948750e+05, 3.93948750e+05, ],
  }),
  ("nof_tree_events",                 394000),
  ("nof_db_events",                   394000),
  ("fsize_local",                     1398210260), # 1.40GB, avg file size 1.40GB
  ("fsize_db",                        20152836915), # 20.15GB, avg file size 1.06GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_280_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2Tau_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_300_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_300_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 282000, ],
    'CountWeighted'                                                                  : [ 2.81948688e+05, 2.81935844e+05, 2.81957844e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.89764750e+05, 2.81939938e+05, 2.73096812e+05, 2.89764750e+05, 2.81939938e+05, 2.73096812e+05, 2.89764750e+05, 2.81939938e+05, 2.73096812e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.89765219e+05, 2.73096312e+05, ],
    'CountWeightedFull'                                                              : [ 2.81931000e+05, 2.81917969e+05, 2.81940000e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.89746188e+05, 2.81922281e+05, 2.73079281e+05, 2.89746188e+05, 2.81922281e+05, 2.73079281e+05, 2.89746188e+05, 2.81922281e+05, 2.73079281e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.89746656e+05, 2.73078781e+05, ],
  }),
  ("nof_tree_events",                 282000),
  ("nof_db_events",                   282000),
  ("fsize_local",                     1022141585), # 1.02GB, avg file size 1.02GB
  ("fsize_db",                        13926261523), # 13.93GB, avg file size 1.27GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_300_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2Tau_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_320_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_320_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99969812e+05, 2.99977375e+05, 2.99955281e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.09800750e+05, 2.99969812e+05, 2.89287844e+05, 3.09800750e+05, 2.99969812e+05, 2.89287844e+05, 3.09800750e+05, 2.99969812e+05, 2.89287844e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.09800750e+05, 2.89287844e+05, ],
    'CountWeightedFull'                                                              : [ 2.99951375e+05, 2.99958281e+05, 2.99936969e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.09781438e+05, 2.99951375e+05, 2.89269812e+05, 3.09781438e+05, 2.99951375e+05, 2.89269812e+05, 3.09781438e+05, 2.99951375e+05, 2.89269812e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.09781438e+05, 2.89269812e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1116886692), # 1.12GB, avg file size 1.12GB
  ("fsize_db",                        15016611273), # 15.02GB, avg file size 938.54MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_320_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2Tau_M-340_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_340_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_340_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99971875e+05, 2.99975156e+05, 2.99971438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.99971875e+05, 2.99971875e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.80919500e+05, 9.80863812e+05, 1.37268500e+06, 9.80391938e+05, 9.54506250e+05, 6.09351125e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.00052125e+05, 3.00093000e+05, 4.27654375e+05, 2.99891781e+05, 2.99680438e+05, 1.86394078e+05, ],
    'CountWeightedFull'                                                              : [ 2.99952250e+05, 2.99955250e+05, 2.99951812e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.99952250e+05, 2.99952250e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.80860438e+05, 9.80799000e+05, 1.37259288e+06, 9.80321875e+05, 9.54443938e+05, 6.09312812e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.00034062e+05, 3.00073156e+05, 4.27625438e+05, 2.99870250e+05, 2.99660688e+05, 1.86382312e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1092939591), # 1.09GB, avg file size 546.47MB
  ("fsize_db",                        16764677713), # 16.76GB, avg file size 1.12GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_340_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2Tau_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_350_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_350_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99949375e+05, 2.99924469e+05, 3.00004000e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.11960688e+05, 2.99946594e+05, 2.87626562e+05, 3.11960688e+05, 2.99946594e+05, 2.87626562e+05, 3.11960688e+05, 2.99946594e+05, 2.87626562e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.11960812e+05, 2.87626438e+05, ],
    'CountWeightedFull'                                                              : [ 2.99929531e+05, 2.99904938e+05, 2.99983500e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.11940344e+05, 2.99926750e+05, 2.87607406e+05, 3.11940344e+05, 2.99926750e+05, 2.87607406e+05, 3.11940344e+05, 2.99926750e+05, 2.87607406e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.11940438e+05, 2.87607281e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1158878770), # 1.16GB, avg file size 1.16GB
  ("fsize_db",                        15183250113), # 15.18GB, avg file size 1.01GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_350_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2Tau_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_400_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_400_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 3.00034781e+05, 2.99945156e+05, 2.99890562e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.15102625e+05, 3.00030594e+05, 2.85209344e+05, 3.15102625e+05, 3.00030594e+05, 2.85209344e+05, 3.15102625e+05, 3.00030594e+05, 2.85209344e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.15102625e+05, 2.85209344e+05, ],
    'CountWeightedFull'                                                              : [ 3.00013031e+05, 2.99924438e+05, 2.99869719e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.15080812e+05, 3.00008844e+05, 2.85189375e+05, 3.15080812e+05, 3.00008844e+05, 2.85189375e+05, 3.15080812e+05, 3.00008844e+05, 2.85189375e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.15080812e+05, 2.85189375e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1217557791), # 1.22GB, avg file size 1.22GB
  ("fsize_db",                        15498531412), # 15.50GB, avg file size 1.03GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_400_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2Tau_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_450_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_450_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99964000e+05, 2.99968656e+05, 2.99961781e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.17768188e+05, 2.99964000e+05, 2.83222000e+05, 3.17768188e+05, 2.99964000e+05, 2.83222000e+05, 3.17768188e+05, 2.99964000e+05, 2.83222000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.17768188e+05, 2.83222000e+05, ],
    'CountWeightedFull'                                                              : [ 2.99941375e+05, 2.99946438e+05, 2.99938719e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.17744406e+05, 2.99941375e+05, 2.83200938e+05, 3.17744406e+05, 2.99941375e+05, 2.83200938e+05, 3.17744406e+05, 2.99941375e+05, 2.83200938e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.17744406e+05, 2.83200938e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1269706654), # 1.27GB, avg file size 1.27GB
  ("fsize_db",                        15806279456), # 15.81GB, avg file size 878.13MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_450_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2Tau_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_500_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_500_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 279000, ],
    'CountWeighted'                                                                  : [ 2.78939250e+05, 2.78919656e+05, 2.78941719e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.97649688e+05, 2.78939250e+05, 2.61750500e+05, 2.97649688e+05, 2.78939250e+05, 2.61750500e+05, 2.97649688e+05, 2.78939250e+05, 2.61750500e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.97649688e+05, 2.61750500e+05, ],
    'CountWeightedFull'                                                              : [ 2.78917312e+05, 2.78897625e+05, 2.78919406e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.97625531e+05, 2.78917312e+05, 2.61729578e+05, 2.97625531e+05, 2.78917312e+05, 2.61729578e+05, 2.97625531e+05, 2.78917312e+05, 2.61729578e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.97625531e+05, 2.61729578e+05, ],
  }),
  ("nof_tree_events",                 279000),
  ("nof_db_events",                   279000),
  ("fsize_local",                     1222852125), # 1.22GB, avg file size 1.22GB
  ("fsize_db",                        14816439731), # 14.82GB, avg file size 1.48GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2Tau_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_550_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_550_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99916312e+05, 2.99941562e+05, 2.99943750e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.22055125e+05, 2.99916094e+05, 2.79855781e+05, 3.22055125e+05, 2.99916094e+05, 2.79855781e+05, 3.22055125e+05, 2.99916094e+05, 2.79855781e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.22055125e+05, 2.79855781e+05, ],
    'CountWeightedFull'                                                              : [ 2.99890844e+05, 2.99916000e+05, 2.99919375e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.22028188e+05, 2.99890656e+05, 2.79832125e+05, 3.22028188e+05, 2.99890656e+05, 2.79832125e+05, 3.22028188e+05, 2.99890656e+05, 2.79832125e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.22028188e+05, 2.79832125e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1356171173), # 1.36GB, avg file size 1.36GB
  ("fsize_db",                        16251104941), # 16.25GB, avg file size 855.32MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_550_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2Tau_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_600_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_600_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99976156e+05, 1.99982719e+05, 1.99970906e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.15959781e+05, 1.99976156e+05, 1.85650172e+05, 2.15959781e+05, 1.99976156e+05, 1.85650172e+05, 2.15959781e+05, 1.99976156e+05, 1.85650172e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.15959781e+05, 1.85650172e+05, ],
    'CountWeightedFull'                                                              : [ 1.99958844e+05, 1.99965219e+05, 1.99953750e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.15940766e+05, 1.99958844e+05, 1.85634047e+05, 2.15940766e+05, 1.99958844e+05, 1.85634047e+05, 2.15940766e+05, 1.99958844e+05, 1.85634047e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.15940766e+05, 1.85634047e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     928210177), # 928.21MB, avg file size 928.21MB
  ("fsize_db",                        11015984538), # 11.02GB, avg file size 734.40MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_600_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2Tau_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_650_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_650_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99968188e+05, 1.99957344e+05, 1.99947906e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.17043594e+05, 1.99968188e+05, 1.84808828e+05, 2.17043594e+05, 1.99968188e+05, 1.84808828e+05, 2.17043594e+05, 1.99968188e+05, 1.84808828e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.17043594e+05, 1.84808828e+05, ],
    'CountWeightedFull'                                                              : [ 1.99950562e+05, 1.99940531e+05, 1.99930562e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.17025000e+05, 1.99950562e+05, 1.84792953e+05, 2.17025000e+05, 1.99950562e+05, 1.84792953e+05, 2.17025000e+05, 1.99950562e+05, 1.84792953e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.17025000e+05, 1.84792953e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     947630556), # 947.63MB, avg file size 947.63MB
  ("fsize_db",                        10969933314), # 10.97GB, avg file size 1.37GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_650_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2Tau_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_700_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_700_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 190000, ],
    'CountWeighted'                                                                  : [ 1.89973969e+05, 1.89975312e+05, 1.89977828e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.07183656e+05, 1.89973969e+05, 1.74874328e+05, 2.07183656e+05, 1.89973969e+05, 1.74874328e+05, 2.07183656e+05, 1.89973969e+05, 1.74874328e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.07183844e+05, 1.74874141e+05, ],
    'CountWeightedFull'                                                              : [ 1.89955750e+05, 1.89956266e+05, 1.89960000e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.07163188e+05, 1.89955750e+05, 1.74857188e+05, 2.07163188e+05, 1.89955750e+05, 1.74857188e+05, 2.07163188e+05, 1.89955750e+05, 1.74857188e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.07163375e+05, 1.74857000e+05, ],
  }),
  ("nof_tree_events",                 190000),
  ("nof_db_events",                   190000),
  ("fsize_local",                     915063773), # 915.06MB, avg file size 915.06MB
  ("fsize_db",                        10693708527), # 10.69GB, avg file size 712.91MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_700_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2Tau_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_750_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_750_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99942594e+05, 1.99988781e+05, 1.99900906e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99942594e+05, 1.99942594e+05, ],
    'CountWeightedFull'                                                              : [ 1.99924734e+05, 1.99970844e+05, 1.99883688e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99924734e+05, 1.99924734e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     983746285), # 983.75MB, avg file size 983.75MB
  ("fsize_db",                        11645634056), # 11.65GB, avg file size 1.16GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2Tau_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_800_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_800_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99979188e+05, 1.99955719e+05, 1.99912062e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99979188e+05, 1.99979188e+05, ],
    'CountWeightedFull'                                                              : [ 1.99958781e+05, 1.99935562e+05, 1.99892312e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99958781e+05, 1.99958781e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     994487326), # 994.49MB, avg file size 994.49MB
  ("fsize_db",                        11769076433), # 11.77GB, avg file size 980.76MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_800_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2Tau_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_850_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_850_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99984531e+05, 1.99932766e+05, 1.99957406e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99984531e+05, 1.99984531e+05, ],
    'CountWeightedFull'                                                              : [ 1.99964000e+05, 1.99913156e+05, 1.99937375e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99964000e+05, 1.99964000e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1004750488), # 1.00GB, avg file size 1.00GB
  ("fsize_db",                        11808552400), # 11.81GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_850_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2Tau_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_900_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_900_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99939359e+05, 1.99976219e+05, 2.00001281e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.21326578e+05, 1.99938156e+05, 1.81633609e+05, 2.21326578e+05, 1.99938156e+05, 1.81633609e+05, 2.21326578e+05, 1.99938156e+05, 1.81633609e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.21326578e+05, 1.81633609e+05, ],
    'CountWeightedFull'                                                              : [ 1.99919750e+05, 1.99956672e+05, 1.99981172e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.21304859e+05, 1.99918500e+05, 1.81616000e+05, 2.21304859e+05, 1.99918500e+05, 1.81616000e+05, 2.21304859e+05, 1.99918500e+05, 1.81616000e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.21304859e+05, 1.81616000e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1007199144), # 1.01GB, avg file size 1.01GB
  ("fsize_db",                        11388868653), # 11.39GB, avg file size 1.63GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_900_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2Tau_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1000_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_1000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99583359e+04, 9.99496016e+04, 9.99516953e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.11312305e+05, 9.99583359e+04, 9.03184141e+04, 1.11312305e+05, 9.99583359e+04, 9.03184141e+04, 1.11312305e+05, 9.99583359e+04, 9.03184141e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.11312570e+05, 9.03181406e+04, ],
    'CountWeightedFull'                                                              : [ 9.99474922e+04, 9.99389922e+04, 9.99405703e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.11300016e+05, 9.99474922e+04, 9.03084766e+04, 1.11300016e+05, 9.99474922e+04, 9.03084766e+04, 1.11300016e+05, 9.99474922e+04, 9.03084766e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.11300281e+05, 9.03081953e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     512533532), # 512.53MB, avg file size 512.53MB
  ("fsize_db",                        5818152628), # 5.82GB, avg file size 969.69MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_1000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2Tau_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1250_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_1250_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99451641e+04, 9.99494844e+04, 9.99439453e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99451641e+04, 9.99451641e+04, ],
    'CountWeightedFull'                                                              : [ 9.99332422e+04, 9.99377422e+04, 9.99318906e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99332422e+04, 9.99332422e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     527021519), # 527.02MB, avg file size 527.02MB
  ("fsize_db",                        6226646883), # 6.23GB, avg file size 622.66MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_1250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2Tau_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1500_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_1500_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99377578e+04, 9.99333438e+04, 9.99185000e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.13882672e+05, 9.99377578e+04, 8.84942656e+04, 1.13882672e+05, 9.99377578e+04, 8.84942656e+04, 1.13882672e+05, 9.99377578e+04, 8.84942656e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.13885898e+05, 8.84910234e+04, ],
    'CountWeightedFull'                                                              : [ 9.99226719e+04, 9.99182734e+04, 9.99040078e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.13865516e+05, 9.99226719e+04, 8.84809766e+04, 1.13865516e+05, 9.99226719e+04, 8.84809766e+04, 1.13865516e+05, 9.99226719e+04, 8.84809766e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.13868742e+05, 8.84777344e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     519962000), # 519.96MB, avg file size 519.96MB
  ("fsize_db",                        5941935179), # 5.94GB, avg file size 1.19GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_1500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2Tau_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1750_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_1750_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99122500e+04, 9.99323359e+04, 9.98937031e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99122500e+04, 9.99122500e+04, ],
    'CountWeightedFull'                                                              : [ 9.98982500e+04, 9.99182188e+04, 9.98801172e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.98982500e+04, 9.98982500e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     520589482), # 520.59MB, avg file size 520.59MB
  ("fsize_db",                        6337929130), # 6.34GB, avg file size 576.18MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_1750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2Tau_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_2000_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_2000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99064141e+04, 9.98929922e+04, 9.99010859e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.15676984e+05, 9.99064141e+04, 8.71945391e+04, 1.15676984e+05, 9.99064141e+04, 8.71945391e+04, 1.15676984e+05, 9.99064141e+04, 8.71945391e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.15678273e+05, 8.71932500e+04, ],
    'CountWeightedFull'                                                              : [ 9.98904531e+04, 9.98775156e+04, 9.98847969e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.15658258e+05, 9.98904531e+04, 8.71805938e+04, 1.15658258e+05, 9.98904531e+04, 8.71805938e+04, 1.15658258e+05, 9.98904531e+04, 8.71805938e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.15659547e+05, 8.71793047e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     516323056), # 516.32MB, avg file size 516.32MB
  ("fsize_db",                        6150409100), # 6.15GB, avg file size 768.80MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_2000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2Tau_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_2500_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_2500_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 75000, ],
    'CountWeighted'                                                                  : [ 7.48853047e+04, 7.49106719e+04, 7.48865625e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 7.48853047e+04, 7.48853047e+04, ],
    'CountWeightedFull'                                                              : [ 7.48679141e+04, 7.48922812e+04, 7.48692734e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 7.48679141e+04, 7.48679141e+04, ],
  }),
  ("nof_tree_events",                 75000),
  ("nof_db_events",                   75000),
  ("fsize_local",                     389855598), # 389.86MB, avg file size 389.86MB
  ("fsize_db",                        4884205812), # 4.88GB, avg file size 610.53MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_2500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToRadionToHHTo2B2Tau_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_3000_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_3000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.97376875e+04, 9.97665938e+04, 9.97184375e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.97376875e+04, 9.97376875e+04, ],
    'CountWeightedFull'                                                              : [ 9.97183281e+04, 9.97467344e+04, 9.96996328e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.97183281e+04, 9.97183281e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     518830693), # 518.83MB, avg file size 518.83MB
  ("fsize_db",                        6520354346), # 6.52GB, avg file size 652.04MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin0_3000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2Tau_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_250_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_250_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 380000, ],
    'CountWeighted'                                                                  : [ 3.79983906e+05, 3.79986375e+05, 3.79994062e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.84654812e+05, 3.79983906e+05, 3.72612250e+05, 3.84654812e+05, 3.79983906e+05, 3.72612250e+05, 3.84654812e+05, 3.79983906e+05, 3.72612250e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.84654812e+05, 3.72612250e+05, ],
    'CountWeightedFull'                                                              : [ 3.79960250e+05, 3.79962188e+05, 3.79970000e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.84630719e+05, 3.79960250e+05, 3.72589031e+05, 3.84630719e+05, 3.79960250e+05, 3.72589031e+05, 3.84630719e+05, 3.79960250e+05, 3.72589031e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.84630719e+05, 3.72589031e+05, ],
  }),
  ("nof_tree_events",                 380000),
  ("nof_db_events",                   380000),
  ("fsize_local",                     1304625748), # 1.30GB, avg file size 1.30GB
  ("fsize_db",                        18890989806), # 18.89GB, avg file size 1.05GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2Tau_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_260_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_260_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 382000, ],
    'CountWeighted'                                                                  : [ 3.82045000e+05, 3.81986156e+05, 3.81968312e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.87971312e+05, 3.82042969e+05, 3.73561750e+05, 3.87971312e+05, 3.82042969e+05, 3.73561750e+05, 3.87971312e+05, 3.82042969e+05, 3.73561750e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.87971312e+05, 3.73561750e+05, ],
    'CountWeightedFull'                                                              : [ 3.82020781e+05, 3.81962156e+05, 3.81944969e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.87947375e+05, 3.82018812e+05, 3.73539031e+05, 3.87947375e+05, 3.82018812e+05, 3.73539031e+05, 3.87947375e+05, 3.82018812e+05, 3.73539031e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.87947375e+05, 3.73539031e+05, ],
  }),
  ("nof_tree_events",                 382000),
  ("nof_db_events",                   382000),
  ("fsize_local",                     1334479898), # 1.33GB, avg file size 1.33GB
  ("fsize_db",                        19066503700), # 19.07GB, avg file size 1.19GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_260_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2Tau_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_270_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_270_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 4.00003344e+05, 4.00043156e+05, 4.00015594e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.07468469e+05, 4.00000625e+05, 3.90150969e+05, 4.07468469e+05, 4.00000625e+05, 3.90150969e+05, 4.07468469e+05, 4.00000625e+05, 3.90150969e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.07468469e+05, 3.90150969e+05, ],
    'CountWeightedFull'                                                              : [ 3.99978344e+05, 4.00018406e+05, 3.99990781e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.07443812e+05, 3.99975531e+05, 3.90127500e+05, 4.07443812e+05, 3.99975531e+05, 3.90127500e+05, 4.07443812e+05, 3.99975531e+05, 3.90127500e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.07443812e+05, 3.90127500e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1422186915), # 1.42GB, avg file size 1.42GB
  ("fsize_db",                        19893232081), # 19.89GB, avg file size 1.24GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_270_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2Tau_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_280_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_280_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 380000, ],
    'CountWeighted'                                                                  : [ 3.79974031e+05, 3.79987156e+05, 3.79961500e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.88286750e+05, 3.79973000e+05, 3.69738406e+05, 3.88286750e+05, 3.79973000e+05, 3.69738406e+05, 3.88286750e+05, 3.79973000e+05, 3.69738406e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.88286750e+05, 3.69738406e+05, ],
    'CountWeightedFull'                                                              : [ 3.79950312e+05, 3.79963469e+05, 3.79937719e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.88262188e+05, 3.79949281e+05, 3.69715000e+05, 3.88262188e+05, 3.79949281e+05, 3.69715000e+05, 3.88262188e+05, 3.79949281e+05, 3.69715000e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.88262188e+05, 3.69715000e+05, ],
  }),
  ("nof_tree_events",                 380000),
  ("nof_db_events",                   380000),
  ("fsize_local",                     1374182564), # 1.37GB, avg file size 1.37GB
  ("fsize_db",                        18844045494), # 18.84GB, avg file size 1.05GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_280_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2Tau_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_300_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_300_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 276000, ],
    'CountWeighted'                                                                  : [ 2.75950500e+05, 2.75966375e+05, 2.75936156e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.83581688e+05, 2.75950500e+05, 2.67263625e+05, 2.83581688e+05, 2.75950500e+05, 2.67263625e+05, 2.83581688e+05, 2.75950500e+05, 2.67263625e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.83581688e+05, 2.67263625e+05, ],
    'CountWeightedFull'                                                              : [ 2.75932656e+05, 2.75948438e+05, 2.75918156e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.83563094e+05, 2.75932656e+05, 2.67246125e+05, 2.83563094e+05, 2.75932656e+05, 2.67246125e+05, 2.83563094e+05, 2.75932656e+05, 2.67246125e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.83563094e+05, 2.67246125e+05, ],
  }),
  ("nof_tree_events",                 276000),
  ("nof_db_events",                   276000),
  ("fsize_local",                     1032195602), # 1.03GB, avg file size 1.03GB
  ("fsize_db",                        14039003672), # 14.04GB, avg file size 779.94MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_300_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2Tau_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_320_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_320_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99925250e+05, 2.99948781e+05, 2.99909031e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.09763969e+05, 2.99925250e+05, 2.89238062e+05, 3.09763969e+05, 2.99925250e+05, 2.89238062e+05, 3.09763969e+05, 2.99925250e+05, 2.89238062e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.09763969e+05, 2.89238062e+05, ],
    'CountWeightedFull'                                                              : [ 2.99905938e+05, 2.99928875e+05, 2.99889312e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.09744031e+05, 2.99905938e+05, 2.89219312e+05, 3.09744031e+05, 2.99905938e+05, 2.89219312e+05, 3.09744031e+05, 2.99905938e+05, 2.89219312e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.09744031e+05, 2.89219312e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1154867743), # 1.15GB, avg file size 1.15GB
  ("fsize_db",                        15463954444), # 15.46GB, avg file size 859.11MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_320_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2Tau_M-340_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_340_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_340_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99979969e+05, 2.99970750e+05, 2.99956406e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.99979969e+05, 2.99979969e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.00011375e+06, 3.00011375e+06, 3.00011375e+06, 3.00011375e+06, 3.00011375e+06, 3.00011375e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99932188e+05, 3.00139438e+05, 4.28566844e+05, 3.00035281e+05, 2.99884094e+05, 1.85846656e+05, ],
    'CountWeightedFull'                                                              : [ 2.99959562e+05, 2.99950625e+05, 2.99936188e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.99959562e+05, 2.99959562e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99991000e+06, 2.99991000e+06, 2.99991000e+06, 2.99991000e+06, 2.99991000e+06, 2.99991000e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99913469e+05, 3.00119500e+05, 4.28537312e+05, 3.00013125e+05, 2.99863500e+05, 1.85834438e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1134236045), # 1.13GB, avg file size 567.12MB
  ("fsize_db",                        17118223925), # 17.12GB, avg file size 1.32GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_340_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2Tau_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_350_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_350_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99944750e+05, 3.00001344e+05, 2.99982625e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.11982875e+05, 2.99944594e+05, 2.87621312e+05, 3.11982875e+05, 2.99944594e+05, 2.87621312e+05, 3.11982875e+05, 2.99944594e+05, 2.87621312e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.11982875e+05, 2.87621312e+05, ],
    'CountWeightedFull'                                                              : [ 2.99921250e+05, 2.99977469e+05, 2.99959250e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.11958156e+05, 2.99921125e+05, 2.87598781e+05, 3.11958156e+05, 2.99921125e+05, 2.87598781e+05, 3.11958156e+05, 2.99921125e+05, 2.87598781e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.11958156e+05, 2.87598781e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1200494219), # 1.20GB, avg file size 1.20GB
  ("fsize_db",                        15655389694), # 15.66GB, avg file size 869.74MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_350_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2Tau_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_400_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_400_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99970344e+05, 2.99982500e+05, 2.99979938e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.15100625e+05, 2.99968281e+05, 2.85241375e+05, 3.15100625e+05, 2.99968281e+05, 2.85241375e+05, 3.15100625e+05, 2.99968281e+05, 2.85241375e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.15100625e+05, 2.85241375e+05, ],
    'CountWeightedFull'                                                              : [ 2.99948000e+05, 2.99960219e+05, 2.99957750e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.15077562e+05, 2.99945906e+05, 2.85220531e+05, 3.15077562e+05, 2.99945906e+05, 2.85220531e+05, 3.15077562e+05, 2.99945906e+05, 2.85220531e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.15077562e+05, 2.85220531e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1264742987), # 1.26GB, avg file size 1.26GB
  ("fsize_db",                        15930702282), # 15.93GB, avg file size 995.67MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_400_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2Tau_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_450_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_450_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99938094e+05, 2.99952125e+05, 2.99995875e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.17768094e+05, 2.99934562e+05, 2.83226469e+05, 3.17768094e+05, 2.99934562e+05, 2.83226469e+05, 3.17768094e+05, 2.99934562e+05, 2.83226469e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.17768094e+05, 2.83226469e+05, ],
    'CountWeightedFull'                                                              : [ 2.99910750e+05, 2.99924688e+05, 2.99967938e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.17738938e+05, 2.99907219e+05, 2.83200812e+05, 3.17738938e+05, 2.99907219e+05, 2.83200812e+05, 3.17738938e+05, 2.99907219e+05, 2.83200812e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.17738938e+05, 2.83200812e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1322195282), # 1.32GB, avg file size 1.32GB
  ("fsize_db",                        16108935179), # 16.11GB, avg file size 1.24GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_450_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2Tau_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_500_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_500_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99931188e+05, 2.99907375e+05, 2.99956625e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.20038750e+05, 2.99931188e+05, 2.81397344e+05, 3.20038750e+05, 2.99931188e+05, 2.81397344e+05, 3.20038750e+05, 2.99931188e+05, 2.81397344e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.20039062e+05, 2.81397031e+05, ],
    'CountWeightedFull'                                                              : [ 2.99905031e+05, 2.99881344e+05, 2.99930000e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.20011000e+05, 2.99905031e+05, 2.81372688e+05, 3.20011000e+05, 2.99905031e+05, 2.81372688e+05, 3.20011000e+05, 2.99905031e+05, 2.81372688e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.20011312e+05, 2.81372344e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1370532564), # 1.37GB, avg file size 1.37GB
  ("fsize_db",                        16548626128), # 16.55GB, avg file size 973.45MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2Tau_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_550_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_550_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99973562e+05, 2.99957062e+05, 2.99908719e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.22100000e+05, 2.99973562e+05, 2.79901812e+05, 3.22100000e+05, 2.99973562e+05, 2.79901812e+05, 3.22100000e+05, 2.99973562e+05, 2.79901812e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.22100000e+05, 2.79901812e+05, ],
    'CountWeightedFull'                                                              : [ 2.99947125e+05, 2.99930812e+05, 2.99884062e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.22072688e+05, 2.99947125e+05, 2.79877594e+05, 3.22072688e+05, 2.99947125e+05, 2.79877594e+05, 3.22072688e+05, 2.99947125e+05, 2.79877594e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.22072688e+05, 2.79877594e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1416319251), # 1.42GB, avg file size 1.42GB
  ("fsize_db",                        16747172547), # 16.75GB, avg file size 837.36MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_550_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2Tau_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_600_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_600_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99897578e+05, 1.99931875e+05, 1.99917000e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.15927500e+05, 1.99896094e+05, 1.85634219e+05, 2.15927500e+05, 1.99896094e+05, 1.85634219e+05, 2.15927500e+05, 1.99896094e+05, 1.85634219e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.15927859e+05, 1.85633875e+05, ],
    'CountWeightedFull'                                                              : [ 1.99880625e+05, 1.99914406e+05, 1.99899734e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.15908438e+05, 1.99879188e+05, 1.85617969e+05, 2.15908438e+05, 1.99879188e+05, 1.85617969e+05, 2.15908438e+05, 1.99879188e+05, 1.85617969e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.15908781e+05, 1.85617625e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     967613563), # 967.61MB, avg file size 967.61MB
  ("fsize_db",                        11160601240), # 11.16GB, avg file size 930.05MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_600_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2Tau_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_650_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_650_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99927984e+05, 1.99945281e+05, 2.00001094e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.17033094e+05, 1.99927984e+05, 1.84798594e+05, 2.17033094e+05, 1.99927984e+05, 1.84798594e+05, 2.17033094e+05, 1.99927984e+05, 1.84798594e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.17033094e+05, 1.84798594e+05, ],
    'CountWeightedFull'                                                              : [ 1.99909891e+05, 1.99927188e+05, 1.99981750e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.17012953e+05, 1.99909891e+05, 1.84781219e+05, 2.17012953e+05, 1.99909891e+05, 1.84781219e+05, 2.17012953e+05, 1.99909891e+05, 1.84781219e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.17012953e+05, 1.84781219e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     985331906), # 985.33MB, avg file size 985.33MB
  ("fsize_db",                        11334272905), # 11.33GB, avg file size 871.87MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_650_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2Tau_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_700_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_700_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99953312e+05, 1.99971875e+05, 1.99979031e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.18050438e+05, 1.99952484e+05, 1.84028500e+05, 2.18050438e+05, 1.99952484e+05, 1.84028500e+05, 2.18050438e+05, 1.99952484e+05, 1.84028500e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.18050438e+05, 1.84028500e+05, ],
    'CountWeightedFull'                                                              : [ 1.99930250e+05, 1.99948781e+05, 1.99955938e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.18025453e+05, 1.99929375e+05, 1.84007938e+05, 2.18025453e+05, 1.99929375e+05, 1.84007938e+05, 2.18025453e+05, 1.99929375e+05, 1.84007938e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.18025453e+05, 1.84007938e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     998293542), # 998.29MB, avg file size 998.29MB
  ("fsize_db",                        11442662705), # 11.44GB, avg file size 715.17MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_700_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2Tau_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_750_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_750_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99979062e+05, 1.99917750e+05, 1.99991875e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.18978688e+05, 1.99979062e+05, 1.83373344e+05, 2.18978688e+05, 1.99979062e+05, 1.83373344e+05, 2.18978688e+05, 1.99979062e+05, 1.83373344e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.18978688e+05, 1.83373344e+05, ],
    'CountWeightedFull'                                                              : [ 1.99959031e+05, 1.99899047e+05, 1.99972188e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.18957344e+05, 1.99959031e+05, 1.83355500e+05, 2.18957344e+05, 1.99959031e+05, 1.83355500e+05, 2.18957344e+05, 1.99959031e+05, 1.83355500e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.18957344e+05, 1.83355500e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1010521480), # 1.01GB, avg file size 1.01GB
  ("fsize_db",                        11419024777), # 11.42GB, avg file size 1.04GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2Tau_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_800_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_800_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99959219e+05, 1.99936438e+05, 1.99939109e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.19776281e+05, 1.99959219e+05, 1.82739469e+05, 2.19776281e+05, 1.99959219e+05, 1.82739469e+05, 2.19776281e+05, 1.99959219e+05, 1.82739469e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.19776281e+05, 1.82739469e+05, ],
    'CountWeightedFull'                                                              : [ 1.99937766e+05, 1.99916125e+05, 1.99918000e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.19753484e+05, 1.99937766e+05, 1.82720438e+05, 2.19753484e+05, 1.99937766e+05, 1.82720438e+05, 2.19753484e+05, 1.99937766e+05, 1.82720438e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.19753484e+05, 1.82720438e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1020429835), # 1.02GB, avg file size 1.02GB
  ("fsize_db",                        11703560456), # 11.70GB, avg file size 835.97MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_800_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2Tau_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_850_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_850_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 190000, ],
    'CountWeighted'                                                                  : [ 1.89931109e+05, 1.89922250e+05, 1.89951625e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.89931109e+05, 1.89931109e+05, ],
    'CountWeightedFull'                                                              : [ 1.89912469e+05, 1.89904219e+05, 1.89932891e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.89912469e+05, 1.89912469e+05, ],
  }),
  ("nof_tree_events",                 190000),
  ("nof_db_events",                   190000),
  ("fsize_local",                     982223531), # 982.22MB, avg file size 982.22MB
  ("fsize_db",                        11594437357), # 11.59GB, avg file size 828.17MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_850_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2Tau_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_900_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_900_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99970125e+05, 1.99956344e+05, 1.99967859e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99970125e+05, 1.99970125e+05, ],
    'CountWeightedFull'                                                              : [ 1.99948656e+05, 1.99935031e+05, 1.99945750e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99948656e+05, 1.99948656e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1040395375), # 1.04GB, avg file size 1.04GB
  ("fsize_db",                        12299683201), # 12.30GB, avg file size 723.51MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_900_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2Tau_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1000_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_1000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99604453e+04, 9.99854609e+04, 9.99458359e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.11334391e+05, 9.99604453e+04, 9.03192734e+04, 1.11334391e+05, 9.99604453e+04, 9.03192734e+04, 1.11334391e+05, 9.99604453e+04, 9.03192734e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.11334391e+05, 9.03192734e+04, ],
    'CountWeightedFull'                                                              : [ 9.99490781e+04, 9.99737266e+04, 9.99345391e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.11321516e+05, 9.99490781e+04, 9.03089219e+04, 1.11321516e+05, 9.99490781e+04, 9.03089219e+04, 1.11321516e+05, 9.99490781e+04, 9.03089219e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.11321516e+05, 9.03089219e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     524692235), # 524.69MB, avg file size 524.69MB
  ("fsize_db",                        5950106308), # 5.95GB, avg file size 991.68MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_1000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2Tau_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1250_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_1250_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99680312e+04, 9.99508594e+04, 9.99810703e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99680312e+04, 9.99680312e+04, ],
    'CountWeightedFull'                                                              : [ 9.99542969e+04, 9.99375859e+04, 9.99673594e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99542969e+04, 9.99542969e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     532840045), # 532.84MB, avg file size 532.84MB
  ("fsize_db",                        6272333626), # 6.27GB, avg file size 784.04MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_1250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2Tau_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1500_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_1500_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99538906e+04, 9.99517656e+04, 9.99340781e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99538906e+04, 9.99538906e+04, ],
    'CountWeightedFull'                                                              : [ 9.99402344e+04, 9.99382188e+04, 9.99208906e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99402344e+04, 9.99402344e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     520520888), # 520.52MB, avg file size 520.52MB
  ("fsize_db",                        6259371847), # 6.26GB, avg file size 1.04GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_1500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2Tau_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1750_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_1750_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99356406e+04, 9.99421250e+04, 9.99604766e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99356406e+04, 9.99356406e+04, ],
    'CountWeightedFull'                                                              : [ 9.99196797e+04, 9.99258281e+04, 9.99440156e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99196797e+04, 9.99196797e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     514835543), # 514.84MB, avg file size 514.84MB
  ("fsize_db",                        6307435165), # 6.31GB, avg file size 901.06MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_1750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2Tau_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_2000_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_2000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.98921797e+04, 9.99119844e+04, 9.99026953e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.15647711e+05, 9.98907656e+04, 8.71793047e+04, 1.15647711e+05, 9.98907656e+04, 8.71793047e+04, 1.15647711e+05, 9.98907656e+04, 8.71793047e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.15648953e+05, 8.71780547e+04, ],
    'CountWeightedFull'                                                              : [ 9.98730312e+04, 9.98927969e+04, 9.98827656e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.15625422e+05, 9.98716328e+04, 8.71621953e+04, 1.15625422e+05, 9.98716328e+04, 8.71621953e+04, 1.15625422e+05, 9.98716328e+04, 8.71621953e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.15626664e+05, 8.71609453e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     509585996), # 509.59MB, avg file size 509.59MB
  ("fsize_db",                        6220782071), # 6.22GB, avg file size 565.53MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_2000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2Tau_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_2500_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_2500_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.98994766e+04, 9.98606797e+04, 9.98832188e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.17194250e+05, 9.98967656e+04, 8.61236094e+04, 1.17194250e+05, 9.98967656e+04, 8.61236094e+04, 1.17194250e+05, 9.98967656e+04, 8.61236094e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.17197578e+05, 8.61202891e+04, ],
    'CountWeightedFull'                                                              : [ 9.98779688e+04, 9.98401016e+04, 9.98614922e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.17169070e+05, 9.98752812e+04, 8.61050312e+04, 1.17169070e+05, 9.98752812e+04, 8.61050312e+04, 1.17169070e+05, 9.98752812e+04, 8.61050312e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.17172383e+05, 8.61017031e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     509240482), # 509.24MB, avg file size 509.24MB
  ("fsize_db",                        6340415904), # 6.34GB, avg file size 634.04MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_2500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToBulkGravitonToHHTo2B2Tau_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_3000_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_3000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.98015312e+04, 9.97896172e+04, 9.97976406e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.18489680e+05, 9.98015312e+04, 8.51010312e+04, 1.18489680e+05, 9.98015312e+04, 8.51010312e+04, 1.18489680e+05, 9.98015312e+04, 8.51010312e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.18496438e+05, 8.50943516e+04, ],
    'CountWeightedFull'                                                              : [ 9.97828906e+04, 9.97713516e+04, 9.97791406e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.18468234e+05, 9.97828906e+04, 8.50855547e+04, 1.18468234e+05, 9.97828906e+04, 8.50855547e+04, 1.18468234e+05, 9.97828906e+04, 8.50855547e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.18475008e+05, 8.50788828e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     510864212), # 510.86MB, avg file size 510.86MB
  ("fsize_db",                        6287076693), # 6.29GB, avg file size 785.88MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_spin2_3000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFHHTo2B2Tau_CV_1_C2V_1_C3_0_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_0_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_0_hh_2b2t_dipoleRecoilOff"),
  ("nof_files",                       4),
  ("nof_db_files",                    26),
  ("nof_events",                      {
    'Count'                                                                          : [ 1000000, ],
    'CountWeighted'                                                                  : [ 9.99965562e+05, 1.00010888e+06, 1.00004775e+06, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99965562e+05, 9.99965562e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.99855000e+06, 9.99863600e+06, 9.99863600e+06, 9.99854800e+06, 9.99863600e+06, 9.99854500e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99832812e+05, 1.00005188e+06, 1.38987062e+06, 9.99847688e+05, 9.97978688e+05, 6.42593062e+05, ],
    'CountWeightedFull'                                                              : [ 9.99498750e+05, 9.99638438e+05, 9.99578312e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99498750e+05, 9.99498750e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99397600e+06, 9.99397600e+06, 9.99397600e+06, 9.99397600e+06, 9.99397600e+06, 9.99397600e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99502938e+05, 9.99578875e+05, 1.38922588e+06, 9.99516812e+05, 9.97519062e+05, 6.42381062e+05, ],
  }),
  ("nof_tree_events",                 1000000),
  ("nof_db_events",                   1000000),
  ("fsize_local",                     4000986478), # 4.00GB, avg file size 1.00GB
  ("fsize_db",                        57894125585), # 57.89GB, avg file size 2.23GB
  ("use_it",                          True),
  ("xsection",                        0.000336706),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_1_0_hh_2b2t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFHHTo2B2Tau_CV_1_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_1_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_1_hh_2b2t_dipoleRecoilOff"),
  ("nof_files",                       8),
  ("nof_db_files",                    48),
  ("nof_events",                      {
    'Count'                                                                          : [ 2000000, ],
    'CountWeighted'                                                                  : [ 1.99996550e+06, 1.99993700e+06, 2.00016362e+06, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99996550e+06, 1.99996550e+06, ],
    'CountWeightedPSWeight'                                                          : [ 1.99985660e+07, 1.99986260e+07, 1.99986260e+07, 1.99985540e+07, 1.99986260e+07, 1.99985520e+07, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99969475e+06, 2.00049088e+06, 2.78500075e+06, 1.99964300e+06, 1.99750750e+06, 1.28197650e+06, ],
    'CountWeightedFull'                                                              : [ 1.99901750e+06, 1.99898775e+06, 1.99919788e+06, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99901750e+06, 1.99901750e+06, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.99891600e+07, 1.99891600e+07, 1.99891600e+07, 1.99891600e+07, 1.99891600e+07, 1.99891600e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99902025e+06, 1.99953800e+06, 2.78369925e+06, 1.99896738e+06, 1.99656938e+06, 1.28154525e+06, ],
  }),
  ("nof_tree_events",                 2000000),
  ("nof_db_events",                   2000000),
  ("fsize_local",                     8015999944), # 8.02GB, avg file size 1.00GB
  ("fsize_db",                        116165471521), # 116.17GB, avg file size 2.42GB
  ("use_it",                          True),
  ("xsection",                        0.00025219),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_1_1_hh_2b2t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFHHTo2B2Tau_CV_1_C2V_1_C3_1_dipoleRecoilOn-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_1_hh_dipoleRecoilOn_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_1_hh_2b2t_dipoleRecoilOn"),
  ("nof_files",                       4),
  ("nof_db_files",                    27),
  ("nof_events",                      {
    'Count'                                                                          : [ 1000000, ],
    'CountWeighted'                                                                  : [ 9.99957547e+05, 9.99904422e+05, 9.99995266e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99957547e+05, 9.99957547e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.99907025e+06, 9.99919975e+06, 9.99919975e+06, 9.99907300e+06, 9.99919975e+06, 9.99906700e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99834328e+05, 9.99876953e+05, 1.32957809e+06, 9.99847984e+05, 1.00000009e+06, 6.93905094e+05, ],
    'CountWeightedFull'                                                              : [ 9.99453500e+05, 9.99405359e+05, 9.99489984e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99453500e+05, 9.99453500e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99417825e+06, 9.99417825e+06, 9.99417825e+06, 9.99417825e+06, 9.99417825e+06, 9.99417825e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99451484e+05, 9.99371875e+05, 1.32891184e+06, 9.99465828e+05, 9.99495562e+05, 6.93639375e+05, ],
  }),
  ("nof_tree_events",                 1000000),
  ("nof_db_events",                   1000000),
  ("fsize_local",                     3847343736), # 3.85GB, avg file size 961.84MB
  ("fsize_db",                        56478823992), # 56.48GB, avg file size 2.09GB
  ("use_it",                          False),
  ("xsection",                        0.00025219),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Nov22_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_1_1_hh_2b2t_dipoleRecoilOn"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFHHTo2B2Tau_CV_1_C2V_1_C3_2_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_2_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_2_hh_2b2t_dipoleRecoilOff"),
  ("nof_files",                       4),
  ("nof_db_files",                    29),
  ("nof_events",                      {
    'Count'                                                                          : [ 997000, ],
    'CountWeighted'                                                                  : [ 9.96940625e+05, 9.97036625e+05, 9.96896438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.96940625e+05, 9.96940625e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.96861100e+06, 9.96865900e+06, 9.96865900e+06, 9.96861100e+06, 9.96865900e+06, 9.96860700e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.96982750e+05, 9.96832750e+05, 1.39714312e+06, 9.96636438e+05, 9.96150875e+05, 6.31640312e+05, ],
    'CountWeightedFull'                                                              : [ 9.96422125e+05, 9.96513125e+05, 9.96377125e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.96422125e+05, 9.96422125e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.96348000e+06, 9.96348000e+06, 9.96348000e+06, 9.96348000e+06, 9.96348000e+06, 9.96348000e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.96613625e+05, 9.96309625e+05, 1.39642588e+06, 9.96266625e+05, 9.95636875e+05, 6.31408188e+05, ],
  }),
  ("nof_tree_events",                 997000),
  ("nof_db_events",                   997000),
  ("fsize_local",                     4266019263), # 4.27GB, avg file size 1.07GB
  ("fsize_db",                        60946852926), # 60.95GB, avg file size 2.10GB
  ("use_it",                          True),
  ("xsection",                        0.000103945),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_1_2_hh_2b2t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFHHTo2B2Tau_CV_1_C2V_2_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_2_1_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_2_1_hh_2b2t_dipoleRecoilOff"),
  ("nof_files",                       8),
  ("nof_db_files",                    56),
  ("nof_events",                      {
    'Count'                                                                          : [ 1996000, ],
    'CountWeighted'                                                                  : [ 1.99602625e+06, 1.99606350e+06, 1.99576675e+06, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99602625e+06, 1.99602625e+06, ],
    'CountWeightedPSWeight'                                                          : [ 1.99559480e+07, 1.99562900e+07, 1.99562900e+07, 1.99559440e+07, 1.99562900e+07, 1.99559380e+07, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99548862e+06, 1.99602500e+06, 2.78683550e+06, 1.99504525e+06, 1.99329312e+06, 1.27170950e+06, ],
    'CountWeightedFull'                                                              : [ 1.99468425e+06, 1.99472525e+06, 1.99443800e+06, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99468425e+06, 1.99468425e+06, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.99430960e+07, 1.99430960e+07, 1.99430960e+07, 1.99430960e+07, 1.99430960e+07, 1.99430960e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99471175e+06, 1.99469325e+06, 2.78500050e+06, 1.99427025e+06, 1.99196525e+06, 1.27121438e+06, ],
  }),
  ("nof_tree_events",                 1996000),
  ("nof_db_events",                   1996000),
  ("fsize_local",                     9753899917), # 9.75GB, avg file size 1.22GB
  ("fsize_db",                        126966878305), # 126.97GB, avg file size 2.27GB
  ("use_it",                          True),
  ("xsection",                        0.001038702),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_2_1_hh_2b2t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFHHTo2B2Tau_CV_1_C2V_2_C3_1_dipoleRecoilOn-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_2_1_hh_dipoleRecoilOn_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_2_1_hh_2b2t_dipoleRecoilOn"),
  ("nof_files",                       4),
  ("nof_db_files",                    29),
  ("nof_events",                      {
    'Count'                                                                          : [ 1000000, ],
    'CountWeighted'                                                                  : [ 9.99957969e+05, 1.00001298e+06, 1.00004680e+06, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99957969e+05, 9.99957969e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.99847675e+06, 9.99884075e+06, 9.99884075e+06, 9.99847075e+06, 9.99884075e+06, 9.99846975e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99829359e+05, 9.99766156e+05, 1.32941325e+06, 9.99623594e+05, 9.99571781e+05, 6.93442266e+05, ],
    'CountWeightedFull'                                                              : [ 9.99302141e+05, 9.99355609e+05, 9.99387078e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99302141e+05, 9.99302141e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99239825e+06, 9.99239825e+06, 9.99239825e+06, 9.99239825e+06, 9.99239825e+06, 9.99239825e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99391281e+05, 9.99105906e+05, 1.32855247e+06, 9.99187453e+05, 9.98921828e+05, 6.93138688e+05, ],
  }),
  ("nof_tree_events",                 1000000),
  ("nof_db_events",                   1000000),
  ("fsize_local",                     4727736407), # 4.73GB, avg file size 1.18GB
  ("fsize_db",                        63322680009), # 63.32GB, avg file size 2.18GB
  ("use_it",                          False),
  ("xsection",                        0.001038702),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Nov22_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_2_1_hh_2b2t_dipoleRecoilOn"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFHHTo2B2Tau_CV_1_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1p5_1_1_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1p5_1_1_hh_2b2t_dipoleRecoilOff"),
  ("nof_files",                       4),
  ("nof_db_files",                    32),
  ("nof_events",                      {
    'Count'                                                                          : [ 1000000, ],
    'CountWeighted'                                                                  : [ 1.00012925e+06, 9.99960062e+05, 9.99989062e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.00012925e+06, 1.00012925e+06, ],
    'CountWeightedPSWeight'                                                          : [ 9.99911200e+06, 9.99930100e+06, 9.99930100e+06, 9.99910200e+06, 9.99930100e+06, 9.99909600e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99956000e+05, 9.99924000e+05, 1.39228825e+06, 9.99606875e+05, 9.98511438e+05, 6.40692562e+05, ],
    'CountWeightedFull'                                                              : [ 9.99583062e+05, 9.99426125e+05, 9.99449625e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99583062e+05, 9.99583062e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99400400e+06, 9.99400400e+06, 9.99400400e+06, 9.99400400e+06, 9.99400400e+06, 9.99400400e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99600875e+05, 9.99384438e+05, 1.39154838e+06, 9.99251500e+05, 9.97976250e+05, 6.40464438e+05, ],
  }),
  ("nof_tree_events",                 1000000),
  ("nof_db_events",                   1000000),
  ("fsize_local",                     4416153866), # 4.42GB, avg file size 1.10GB
  ("fsize_db",                        61833260146), # 61.83GB, avg file size 1.93GB
  ("use_it",                          True),
  ("xsection",                        0.004823067),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1p5_1_1_hh_2b2t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFHHTo2B2Tau_CV_0_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_0p5_1_1_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_0p5_1_1_hh_2b2t_dipoleRecoilOff"),
  ("nof_files",                       4),
  ("nof_db_files",                    29),
  ("nof_events",                      {
    'Count'                                                                          : [ 992000, ],
    'CountWeighted'                                                                  : [ 9.91961188e+05, 9.91837812e+05, 9.91953500e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.91961188e+05, 9.91961188e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.92015400e+06, 9.92035800e+06, 9.92035800e+06, 9.92015500e+06, 9.92035800e+06, 9.92014700e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.91653125e+05, 9.91827812e+05, 1.38463262e+06, 9.91739375e+05, 9.91364875e+05, 6.32830375e+05, ],
    'CountWeightedFull'                                                              : [ 9.91352688e+05, 9.91232375e+05, 9.91347875e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.91352688e+05, 9.91352688e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.91420400e+06, 9.91420400e+06, 9.91420400e+06, 9.91420400e+06, 9.91420400e+06, 9.91420400e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.91279875e+05, 9.91217875e+05, 1.38380000e+06, 9.91367000e+05, 9.90760625e+05, 6.32591875e+05, ],
  }),
  ("nof_tree_events",                 992000),
  ("nof_db_events",                   992000),
  ("fsize_local",                     4709682689), # 4.71GB, avg file size 1.18GB
  ("fsize_db",                        62115882584), # 62.12GB, avg file size 2.14GB
  ("use_it",                          True),
  ("xsection",                        0.000790739),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_nonresonant_0p5_1_1_hh_2b2t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFHHTo2B2Tau_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_0_1_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_0_1_hh_2b2t_dipoleRecoilOff"),
  ("nof_files",                       8),
  ("nof_db_files",                    55),
  ("nof_events",                      {
    'Count'                                                                          : [ 1997000, ],
    'CountWeighted'                                                                  : [ 1.99704525e+06, 1.99697175e+06, 1.99678100e+06, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99704525e+06, 1.99704525e+06, ],
    'CountWeightedPSWeight'                                                          : [ 1.99713100e+07, 1.99716880e+07, 1.99716880e+07, 1.99713000e+07, 1.99716880e+07, 1.99712980e+07, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99651925e+06, 1.99607612e+06, 2.78212100e+06, 1.99663200e+06, 1.99569725e+06, 1.27852462e+06, ],
    'CountWeightedFull'                                                              : [ 1.99593862e+06, 1.99586250e+06, 1.99568950e+06, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99593862e+06, 1.99593862e+06, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.99605900e+07, 1.99605900e+07, 1.99605900e+07, 1.99605900e+07, 1.99605900e+07, 1.99605900e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99579812e+06, 1.99496975e+06, 2.78058050e+06, 1.99591012e+06, 1.99458075e+06, 1.27806212e+06, ],
  }),
  ("nof_tree_events",                 1997000),
  ("nof_db_events",                   1997000),
  ("fsize_local",                     9105316170), # 9.11GB, avg file size 1.14GB
  ("fsize_db",                        125408556263), # 125.41GB, avg file size 2.28GB
  ("use_it",                          True),
  ("xsection",                        0.001978366),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_0_1_hh_2b2t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/VBFHHTo2B2Tau_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_0_1_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_0_1_hh_2b2t_dipoleRecoilOff_ext1"),
  ("nof_files",                       3),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 500000, ],
    'CountWeighted'                                                                  : [ 4.99976344e+05, 4.99998062e+05, 4.99956625e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.99976344e+05, 4.99976344e+05, ],
    'CountWeightedPSWeight'                                                          : [ 4.99983600e+06, 4.99992700e+06, 4.99992700e+06, 4.99983600e+06, 4.99992700e+06, 4.99983550e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.99876250e+05, 5.00031750e+05, 6.96516875e+05, 4.99752781e+05, 4.99222188e+05, 3.19830312e+05, ],
    'CountWeightedFull'                                                              : [ 4.99673062e+05, 4.99692500e+05, 4.99655531e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.99673062e+05, 4.99673062e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 4.99688850e+06, 4.99688850e+06, 4.99688850e+06, 4.99688850e+06, 4.99688850e+06, 4.99688850e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 4.99695281e+05, 4.99734250e+05, 6.96101500e+05, 4.99571719e+05, 4.98914688e+05, 3.19714812e+05, ],
  }),
  ("nof_tree_events",                 500000),
  ("nof_db_events",                   500000),
  ("fsize_local",                     2282319867), # 2.28GB, avg file size 760.77MB
  ("fsize_db",                        31415804608), # 31.42GB, avg file size 2.09GB
  ("use_it",                          True),
  ("xsection",                        0.001978366),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_0_1_hh_2b2t_dipoleRecoilOff_ext1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2Tau_node_SM_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_sm_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99902375e+05, 3.99949875e+05, 3.99919500e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.11999250e+05, 4.83246406e+05, 4.56267125e+05, 4.23857688e+05, 3.99902375e+05, 3.77562469e+05, 3.56956500e+05, 3.36769125e+05, 3.17856031e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.11999250e+05, 3.17856031e+05, ],
    'CountWeightedFull'                                                              : [ 3.99871156e+05, 3.99917406e+05, 3.99888531e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.11957938e+05, 4.83207281e+05, 4.56230750e+05, 4.23823625e+05, 3.99871156e+05, 3.77532125e+05, 3.56927594e+05, 3.36741906e+05, 3.17830719e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.11957938e+05, 3.17830719e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1719154316), # 1.72GB, avg file size 1.72GB
  ("fsize_db",                        21797059213), # 21.80GB, avg file size 990.78MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_sm_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2Tau_node_2_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_2_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    25),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99831938e+05, 3.99872844e+05, 3.99830375e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.19524719e+05, 4.78717625e+05, 4.42863844e+05, 4.34141906e+05, 3.99831938e+05, 3.69708094e+05, 3.68526375e+05, 3.39244750e+05, 3.13565844e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.19524875e+05, 3.13565750e+05, ],
    'CountWeightedFull'                                                              : [ 3.99790562e+05, 3.99832062e+05, 3.99788500e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.19470469e+05, 4.78668500e+05, 4.42818844e+05, 4.34096250e+05, 3.99790562e+05, 3.69670469e+05, 3.68487562e+05, 3.39209688e+05, 3.13533719e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.19470594e+05, 3.13533625e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1874281445), # 1.87GB, avg file size 1.87GB
  ("fsize_db",                        22516257623), # 22.52GB, avg file size 900.65MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_2_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2Tau_node_3_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_3_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 385000, ],
    'CountWeighted'                                                                  : [ 3.85008000e+05, 3.84999375e+05, 3.85002438e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.92816188e+05, 4.65095250e+05, 4.39053031e+05, 4.07993969e+05, 3.85007594e+05, 3.63362188e+05, 3.43601156e+05, 3.24163562e+05, 3.05927688e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.92816188e+05, 3.05927656e+05, ],
    'CountWeightedFull'                                                              : [ 3.84974312e+05, 3.84965781e+05, 3.84968812e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.92773969e+05, 4.65055594e+05, 4.39015625e+05, 4.07958812e+05, 3.84973906e+05, 3.63331219e+05, 3.43571562e+05, 3.24135781e+05, 3.05901688e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.92773969e+05, 3.05901656e+05, ],
  }),
  ("nof_tree_events",                 385000),
  ("nof_db_events",                   385000),
  ("fsize_local",                     1661890648), # 1.66GB, avg file size 1.66GB
  ("fsize_db",                        20832150345), # 20.83GB, avg file size 1.30GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_3_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2Tau_node_4_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_4_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99949219e+05, 3.99991094e+05, 3.99975781e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10041500e+05, 4.84395188e+05, 4.59736031e+05, 4.21205938e+05, 3.99949219e+05, 3.79563156e+05, 3.53998438e+05, 3.36110281e+05, 3.18928375e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10041500e+05, 3.18928375e+05, ],
    'CountWeightedFull'                                                              : [ 3.99918062e+05, 3.99960000e+05, 3.99943625e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.10000750e+05, 4.84356875e+05, 4.59699875e+05, 4.21172375e+05, 3.99918062e+05, 3.79533062e+05, 3.53970250e+05, 3.36083719e+05, 3.18903062e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.10000750e+05, 3.18903062e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1679218326), # 1.68GB, avg file size 1.68GB
  ("fsize_db",                        21196927455), # 21.20GB, avg file size 1.01GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_4_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2Tau_node_5_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_5_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99948625e+05, 3.99946969e+05, 3.99923688e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.12979750e+05, 4.82635250e+05, 4.54454938e+05, 4.25183750e+05, 3.99948312e+05, 3.76515156e+05, 3.58432281e+05, 3.37088188e+05, 3.17291000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.12979812e+05, 3.17291000e+05, ],
    'CountWeightedFull'                                                              : [ 3.99914438e+05, 3.99913125e+05, 3.99890438e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.12936438e+05, 4.82594625e+05, 4.54416750e+05, 4.25147500e+05, 3.99914125e+05, 3.76483344e+05, 3.58401656e+05, 3.37059562e+05, 3.17264312e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.12936438e+05, 3.17264312e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1743071518), # 1.74GB, avg file size 1.74GB
  ("fsize_db",                        21769316911), # 21.77GB, avg file size 1.28GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_5_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2Tau_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_6_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    25),
  ("nof_events",                      {
    'Count'                                                                          : [ 388000, ],
    'CountWeighted'                                                                  : [ 3.87933062e+05, 3.87987625e+05, 3.88052375e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.94929312e+05, 4.69692562e+05, 4.45489188e+05, 4.08838688e+05, 3.87924875e+05, 3.67915344e+05, 3.43676906e+05, 3.26080156e+05, 3.09223188e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.94929312e+05, 3.09223188e+05, ],
    'CountWeightedFull'                                                              : [ 3.87903188e+05, 3.87957375e+05, 3.88022031e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.94892125e+05, 4.69657062e+05, 4.45455719e+05, 4.08807844e+05, 3.87895000e+05, 3.67887625e+05, 3.43650844e+05, 3.26055531e+05, 3.09199812e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.94892125e+05, 3.09199812e+05, ],
  }),
  ("nof_tree_events",                 388000),
  ("nof_db_events",                   388000),
  ("fsize_local",                     1633070401), # 1.63GB, avg file size 1.63GB
  ("fsize_db",                        20580880747), # 20.58GB, avg file size 823.24MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_6_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2Tau_node_7_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_7_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 345000, ],
    'CountWeighted'                                                                  : [ 3.44965750e+05, 3.44921344e+05, 3.44910312e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.39912688e+05, 4.17707594e+05, 3.96363750e+05, 3.63316188e+05, 3.44965750e+05, 3.27278688e+05, 3.05359500e+05, 2.89883781e+05, 2.75022469e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.39912688e+05, 2.75022469e+05, ],
    'CountWeightedFull'                                                              : [ 3.44939281e+05, 3.44894594e+05, 3.44884125e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.39879312e+05, 4.17676000e+05, 3.96333688e+05, 3.63288688e+05, 3.44939281e+05, 3.27253938e+05, 3.05336375e+05, 2.89861781e+05, 2.75001906e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.39879312e+05, 2.75001906e+05, ],
  }),
  ("nof_tree_events",                 345000),
  ("nof_db_events",                   345000),
  ("fsize_local",                     1451009753), # 1.45GB, avg file size 1.45GB
  ("fsize_db",                        18385644793), # 18.39GB, avg file size 919.28MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_7_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2Tau_node_8_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_8_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99914375e+05, 3.99896188e+05, 3.99873406e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.09918781e+05, 4.84409406e+05, 4.59840812e+05, 4.21054438e+05, 3.99913469e+05, 3.79621375e+05, 3.53835625e+05, 3.36063812e+05, 3.18957375e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.09918781e+05, 3.18957375e+05, ],
    'CountWeightedFull'                                                              : [ 3.99885656e+05, 3.99866719e+05, 3.99844938e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.09880875e+05, 4.84373562e+05, 4.59806844e+05, 4.21023062e+05, 3.99884750e+05, 3.79593344e+05, 3.53809188e+05, 3.36039094e+05, 3.18933469e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.09880875e+05, 3.18933469e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1676849826), # 1.68GB, avg file size 1.68GB
  ("fsize_db",                        20868493058), # 20.87GB, avg file size 1.39GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_8_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2Tau_node_9_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_9_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 395000, ],
    'CountWeighted'                                                                  : [ 3.94865688e+05, 3.94872562e+05, 3.94847094e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.12859719e+05, 4.72832844e+05, 4.37485969e+05, 4.28442781e+05, 3.94865688e+05, 3.65283062e+05, 3.63552500e+05, 3.35006812e+05, 3.09822750e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.12861719e+05, 3.09821062e+05, ],
    'CountWeightedFull'                                                              : [ 3.94827375e+05, 3.94835375e+05, 3.94808875e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.12809344e+05, 4.72786875e+05, 4.37443688e+05, 4.28400656e+05, 3.94827375e+05, 3.65247750e+05, 3.63516875e+05, 3.34974219e+05, 3.09792688e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.12811344e+05, 3.09791031e+05, ],
  }),
  ("nof_tree_events",                 395000),
  ("nof_db_events",                   395000),
  ("fsize_local",                     1870080184), # 1.87GB, avg file size 1.87GB
  ("fsize_db",                        22426425741), # 22.43GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_9_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2Tau_node_10_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_10_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99946312e+05, 3.99941906e+05, 3.99963062e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10086594e+05, 4.84293750e+05, 4.59509438e+05, 4.21286750e+05, 3.99938000e+05, 3.79425281e+05, 3.54090969e+05, 3.36106750e+05, 3.18846125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10086625e+05, 3.18846125e+05, ],
    'CountWeightedFull'                                                              : [ 3.99915094e+05, 3.99911125e+05, 3.99931844e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.10047094e+05, 4.84256469e+05, 4.59473812e+05, 4.21254125e+05, 3.99906844e+05, 3.79395812e+05, 3.54063688e+05, 3.36080656e+05, 3.18821500e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.10047125e+05, 3.18821469e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1681240336), # 1.68GB, avg file size 1.68GB
  ("fsize_db",                        21245748310), # 21.25GB, avg file size 923.73MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_10_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2Tau_node_11_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_11_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99916125e+05, 3.99855438e+05, 3.99858000e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10377281e+05, 4.84050031e+05, 4.58870281e+05, 4.21698844e+05, 3.99914562e+05, 3.79061375e+05, 3.54557562e+05, 3.36199969e+05, 3.18651000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10377312e+05, 3.18650938e+05, ],
    'CountWeightedFull'                                                              : [ 3.99884500e+05, 3.99824250e+05, 3.99826031e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.10337062e+05, 4.84011875e+05, 4.58834375e+05, 4.21665656e+05, 3.99882906e+05, 3.79031531e+05, 3.54529281e+05, 3.36173500e+05, 3.18626125e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.10337062e+05, 3.18626094e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1687704199), # 1.69GB, avg file size 1.69GB
  ("fsize_db",                        20943410362), # 20.94GB, avg file size 1.75GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_11_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2Tau_node_12_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_12_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99800844e+05, 3.99849469e+05, 3.99891844e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.09904656e+05, 4.84397438e+05, 4.59832781e+05, 4.21043000e+05, 3.99789469e+05, 3.79612062e+05, 3.53822750e+05, 3.36041844e+05, 3.18945750e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.09904656e+05, 3.18945750e+05, ],
    'CountWeightedFull'                                                              : [ 3.99769812e+05, 3.99819125e+05, 3.99860438e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.09864281e+05, 4.84359094e+05, 4.59796625e+05, 4.21009438e+05, 3.99758500e+05, 3.79582281e+05, 3.53794531e+05, 3.36015219e+05, 3.18920688e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.09864281e+05, 3.18920688e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1676706607), # 1.68GB, avg file size 1.68GB
  ("fsize_db",                        21011506973), # 21.01GB, avg file size 913.54MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_12_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2Tau_node_cHHH0_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH0_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH0_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    34),
  ("nof_events",                      {
    'Count'                                                                          : [ 1000000, ],
    'CountWeighted'                                                                  : [ 9.41259625e+05, 9.41417375e+05, 9.41299000e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.08903025e+06, 1.07015212e+06, 1.05688438e+06, 9.62618000e+05, 9.41259625e+05, 9.24191000e+05, 8.53422875e+05, 8.31498250e+05, 8.12792500e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.12762800e+06, 7.93893438e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.41197375e+05, 9.41437000e+05, 1.34070925e+06, 9.41498125e+05, 9.40353375e+05, 5.82216125e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 6.40846133e+04, 6.40922734e+04, 9.13560234e+04, 6.41015547e+04, 6.41191484e+04, 3.96566484e+04, ],
    'CountWeightedFull'                                                              : [ 6.02110977e+04, 6.02096367e+04, 6.02056172e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 6.96560000e+04, 6.84479141e+04, 6.75988984e+04, 6.15715625e+04, 6.02110977e+04, 5.91128398e+04, 5.45860859e+04, 5.31834766e+04, 5.19866523e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 7.21256875e+04, 5.07779844e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 6.02012617e+04, 6.02161016e+04, 8.57540703e+04, 6.02197812e+04, 6.01469609e+04, 3.72399570e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 4.11330078e+03, 4.11383740e+03, 5.86088525e+03, 4.11429590e+03, 4.11531836e+03, 2.54780420e+03, ],
  }),
  ("nof_tree_events",                 1000000),
  ("nof_db_events",                   1000000),
  ("fsize_local",                     4019272997), # 4.02GB, avg file size 1.00GB
  ("fsize_db",                        49487397386), # 49.49GB, avg file size 1.46GB
  ("use_it",                          True),
  ("xsection",                        0.00493878),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_cHHH0_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2Tau_node_cHHH1_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH1_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH1_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    34),
  ("nof_events",                      {
    'Count'                                                                          : [ 1000000, ],
    'CountWeighted'                                                                  : [ 8.95615625e+05, 8.95793750e+05, 8.95672000e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.01973950e+06, 1.00348225e+06, 9.92767438e+05, 9.16317250e+05, 8.95601500e+05, 8.79561812e+05, 8.22489000e+05, 8.00054062e+05, 7.81249125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.06362175e+06, 7.57363250e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.95624938e+05, 8.95827188e+05, 1.27674575e+06, 8.95807750e+05, 8.94804750e+05, 5.53199250e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.98851172e+04, 2.98964688e+04, 4.26494648e+04, 2.98921367e+04, 2.99010508e+04, 1.84592871e+04, ],
    'CountWeightedFull'                                                              : [ 2.67487266e+04, 2.67512656e+04, 2.67503906e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.04534473e+04, 2.99676602e+04, 2.96473828e+04, 2.73653457e+04, 2.67476953e+04, 2.62671797e+04, 2.45623262e+04, 2.38921758e+04, 2.33304727e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.17646426e+04, 2.26171855e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.67472246e+04, 2.67529590e+04, 3.81290195e+04, 2.67526348e+04, 2.67227539e+04, 1.65208828e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 8.93843262e+02, 8.94211548e+02, 1.27524292e+03, 8.94101074e+02, 8.94262512e+02, 5.52432129e+02, ],
  }),
  ("nof_tree_events",                 1000000),
  ("nof_db_events",                   1000000),
  ("fsize_local",                     4141133401), # 4.14GB, avg file size 1.04GB
  ("fsize_db",                        50081318436), # 50.08GB, avg file size 1.47GB
  ("use_it",                          True),
  ("xsection",                        0.00219911),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_cHHH1_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2Tau_node_cHHH2p45_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH2p45_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH2p45_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    39),
  ("nof_events",                      {
    'Count'                                                                          : [ 1000000, ],
    'CountWeighted'                                                                  : [ 8.62012375e+05, 8.62175875e+05, 8.61930250e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 9.82854250e+05, 9.69321000e+05, 9.60703688e+05, 8.79599125e+05, 8.61982375e+05, 8.48299438e+05, 7.87431812e+05, 7.68094625e+05, 7.51820375e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.03513475e+06, 7.19873250e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.61948875e+05, 8.61962500e+05, 1.22979025e+06, 8.62135625e+05, 8.60424375e+05, 5.30998750e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.31378379e+04, 1.31370742e+04, 1.87676758e+04, 1.31401396e+04, 1.31402627e+04, 8.09418701e+03, ],
    'CountWeightedFull'                                                              : [ 1.13060488e+04, 1.13071689e+04, 1.13045850e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.28902373e+04, 1.27125049e+04, 1.25993320e+04, 1.15359648e+04, 1.13059004e+04, 1.11252012e+04, 1.03270898e+04, 1.00733486e+04, 9.85981348e+03, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.35758809e+04, 9.44086621e+03, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.13043398e+04, 1.13046602e+04, 1.61284346e+04, 1.13067969e+04, 1.12839707e+04, 6.96386572e+03, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.72814087e+02, 1.72804031e+02, 2.46790756e+02, 1.72842392e+02, 1.72850525e+02, 1.06542297e+02, ],
  }),
  ("nof_tree_events",                 1000000),
  ("nof_db_events",                   1000000),
  ("fsize_local",                     4152610579), # 4.15GB, avg file size 1.04GB
  ("fsize_db",                        50271035315), # 50.27GB, avg file size 1.29GB
  ("use_it",                          True),
  ("xsection",                        0.0009296),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_cHHH2p45_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2018["/GluGluToHHTo2B2Tau_node_cHHH5_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH5_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH5_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    35),
  ("nof_events",                      {
    'Count'                                                                          : [ 1000000, ],
    'CountWeighted'                                                                  : [ 9.84270188e+05, 9.84323500e+05, 9.84278312e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.17890175e+06, 1.15664275e+06, 1.13949400e+06, 1.00393425e+06, 9.84261438e+05, 9.67642500e+05, 8.64563062e+05, 8.47196875e+05, 8.31475312e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.21485438e+06, 8.14591875e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.84296500e+05, 9.84223562e+05, 1.39976400e+06, 9.84342000e+05, 9.82914875e+05, 6.10126625e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 8.02211406e+04, 8.02181719e+04, 1.14185188e+05, 8.02269766e+04, 8.02049375e+04, 4.97234062e+04, ],
    'CountWeightedFull'                                                              : [ 7.89411562e+04, 7.89504453e+04, 7.89433281e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 9.45564844e+04, 9.27702188e+04, 9.13936641e+04, 8.05226875e+04, 7.89399688e+04, 7.76104688e+04, 6.93431719e+04, 6.79497031e+04, 6.66881484e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.74408125e+04, 6.53341406e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 7.89471094e+04, 7.89408906e+04, 1.12270898e+05, 7.89502812e+04, 7.88369844e+04, 4.89357109e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 6.43697510e+03, 6.43652979e+03, 9.16197852e+03, 6.43735938e+03, 6.43596289e+03, 3.99015039e+03, ],
  }),
  ("nof_tree_events",                 1000000),
  ("nof_db_events",                   1000000),
  ("fsize_local",                     3755271203), # 3.76GB, avg file size 938.82MB
  ("fsize_db",                        48318284793), # 48.32GB, avg file size 1.38GB
  ("use_it",                          True),
  ("xsection",                        0.00645797),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct26_woPresel_nom_all/ntuples/signal_ggf_nonresonant_cHHH5_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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
  [ 'signal_ggf_nonresonant_node_sm_hh_2b2v',          'signal_ggf_nonresonant_node_1_hh_2b2v',           'signal_ggf_nonresonant_node_2_hh_2b2v',           'signal_ggf_nonresonant_node_3_hh_2b2v',           'signal_ggf_nonresonant_node_4_hh_2b2v',           'signal_ggf_nonresonant_node_5_hh_2b2v',           'signal_ggf_nonresonant_node_6_hh_2b2v',           'signal_ggf_nonresonant_node_7_hh_2b2v',           'signal_ggf_nonresonant_node_8_hh_2b2v',           'signal_ggf_nonresonant_node_9_hh_2b2v',           'signal_ggf_nonresonant_node_10_hh_2b2v',          'signal_ggf_nonresonant_node_11_hh_2b2v',          'signal_ggf_nonresonant_node_12_hh_2b2v',           ],
  [ 'signal_ggf_nonresonant_node_sm_hh_2b2v_sl',       'signal_ggf_nonresonant_node_2_hh_2b2v_sl',        'signal_ggf_nonresonant_node_3_hh_2b2v_sl',        'signal_ggf_nonresonant_node_4_hh_2b2v_sl',        'signal_ggf_nonresonant_node_5_hh_2b2v_sl',        'signal_ggf_nonresonant_node_6_hh_2b2v_sl',        'signal_ggf_nonresonant_node_7_hh_2b2v_sl',        'signal_ggf_nonresonant_node_8_hh_2b2v_sl',        'signal_ggf_nonresonant_node_9_hh_2b2v_sl',        'signal_ggf_nonresonant_node_10_hh_2b2v_sl',       'signal_ggf_nonresonant_node_11_hh_2b2v_sl',       'signal_ggf_nonresonant_node_12_hh_2b2v_sl',        ],
  [ 'signal_ggf_nonresonant_node_sm_hh_2b2t',          'signal_ggf_nonresonant_node_2_hh_2b2t',           'signal_ggf_nonresonant_node_3_hh_2b2t',           'signal_ggf_nonresonant_node_4_hh_2b2t',           'signal_ggf_nonresonant_node_5_hh_2b2t',           'signal_ggf_nonresonant_node_6_hh_2b2t',           'signal_ggf_nonresonant_node_7_hh_2b2t',           'signal_ggf_nonresonant_node_8_hh_2b2t',           'signal_ggf_nonresonant_node_9_hh_2b2t',           'signal_ggf_nonresonant_node_10_hh_2b2t',          'signal_ggf_nonresonant_node_11_hh_2b2t',          'signal_ggf_nonresonant_node_12_hh_2b2t',           ],
  [ 'signal_vbf_nonresonant_1_0_1_hh_2b2t_dipoleRecoilOff', 'signal_vbf_nonresonant_1_0_1_hh_2b2t_dipoleRecoilOff_ext1',  ],
]

