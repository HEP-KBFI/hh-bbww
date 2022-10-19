from collections import OrderedDict as OD

# file generated at 2021-12-29 23:06:14 with the following command:
# create_dictionary.py -m python/samples/metaDict_2018.py -p python/samples/sampleLocations_2018.txt -N samples_2018 -E 2018 -o python/samples -g hhAnalyzeSamples_2018_hh.py -M

samples_2018 = OD()
samples_2018["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_250_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_250_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99944016e+05, 3.99901719e+05, 3.99946422e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99944016e+05, 3.99944016e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99918412e+06, 3.99918412e+06, 3.99918412e+06, 3.99918412e+06, 3.99918412e+06, 3.99918412e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00054438e+05, 4.00133906e+05, 5.67393078e+05, 3.99875578e+05, 3.99431547e+05, 2.50944070e+05, ],
    'CountWeightedFull'                                                              : [ 3.99877047e+05, 3.99834812e+05, 3.99879172e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99877047e+05, 3.99877047e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99851438e+06, 3.99851438e+06, 3.99851438e+06, 3.99851438e+06, 3.99851438e+06, 3.99851438e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99988672e+05, 4.00066750e+05, 5.67295719e+05, 3.99805328e+05, 3.99363016e+05, 2.50902195e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     2197430781), # 2.20GB, avg file size 1.10GB
  ("fsize_db",                        21769417420), # 21.77GB, avg file size 1.28GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_250_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99899750e+05, 3.99956891e+05, 3.99968969e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.06210953e+05, 3.99890312e+05, 3.91150047e+05, 4.06210953e+05, 3.99890312e+05, 3.91150047e+05, 4.06210953e+05, 3.99890312e+05, 3.91150047e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.06210953e+05, 3.91150047e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.66350825e+06, 2.60514600e+06, 3.40267212e+06, 2.66102050e+06, 2.34407125e+06, 1.67006575e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99954766e+05, 3.99794703e+05, 5.67791031e+05, 3.99942266e+05, 3.99959719e+05, 2.50778391e+05, ],
    'CountWeightedFull'                                                              : [ 3.99832719e+05, 3.99889156e+05, 3.99901219e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.06142188e+05, 3.99823375e+05, 3.91083859e+05, 4.06142188e+05, 3.99823375e+05, 3.91083859e+05, 4.06142188e+05, 3.99823375e+05, 3.91083859e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.06142188e+05, 3.91083859e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.66307075e+06, 2.60470975e+06, 3.40209275e+06, 2.66055500e+06, 2.34367425e+06, 1.66978712e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99888891e+05, 3.99727312e+05, 5.67694438e+05, 3.99872047e+05, 3.99892031e+05, 2.50736594e+05, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     2226052072), # 2.23GB, avg file size 1.11GB
  ("fsize_db",                        20956744775), # 20.96GB, avg file size 1.50GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_260_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99927891e+05, 3.99951359e+05, 3.99969969e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.07473969e+05, 3.99927062e+05, 3.90119828e+05, 4.07473969e+05, 3.99927062e+05, 3.90119828e+05, 4.07473969e+05, 3.99927062e+05, 3.90119828e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.07473969e+05, 3.90119828e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.98437369e+06, 1.97710550e+06, 2.68116200e+06, 1.98309469e+06, 1.85211644e+06, 1.24151975e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00081156e+05, 3.99927250e+05, 5.68395625e+05, 3.99835594e+05, 3.99930203e+05, 2.50312961e+05, ],
    'CountWeightedFull'                                                              : [ 3.99857516e+05, 3.99881453e+05, 3.99899984e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.07402469e+05, 3.99856641e+05, 3.90051375e+05, 4.07402469e+05, 3.99856641e+05, 3.90051375e+05, 4.07402469e+05, 3.99856641e+05, 3.90051375e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.07402469e+05, 3.90051375e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.98404150e+06, 1.97675738e+06, 2.68069162e+06, 1.98274188e+06, 1.85179625e+06, 1.24130844e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 4.00014172e+05, 3.99856828e+05, 5.68296438e+05, 3.99764375e+05, 3.99861469e+05, 2.50270375e+05, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     2260496799), # 2.26GB, avg file size 1.13GB
  ("fsize_db",                        21109891474), # 21.11GB, avg file size 1.24GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_270_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99976109e+05, 3.99945797e+05, 3.99947484e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99976109e+05, 3.99976109e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.70069988e+06, 1.69761944e+06, 2.33382512e+06, 1.69975206e+06, 1.61932481e+06, 1.06392838e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00079453e+05, 3.99817266e+05, 5.68359891e+05, 3.99858547e+05, 3.99816109e+05, 2.50283586e+05, ],
    'CountWeightedFull'                                                              : [ 3.99905656e+05, 3.99876000e+05, 3.99877094e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99905656e+05, 3.99905656e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.70041319e+06, 1.69732338e+06, 2.33340544e+06, 1.69944738e+06, 1.61903362e+06, 1.06374644e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 4.00012125e+05, 3.99747844e+05, 5.68256375e+05, 3.99786891e+05, 3.99742828e+05, 2.50240766e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     2308370718), # 2.31GB, avg file size 1.15GB
  ("fsize_db",                        21992399506), # 21.99GB, avg file size 1.37GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_280_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 2.99966680e+05, 2.99941234e+05, 2.99957605e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.08218430e+05, 2.99966680e+05, 2.90509465e+05, 3.08218430e+05, 2.99966680e+05, 2.90509465e+05, 3.08218430e+05, 2.99966680e+05, 2.90509465e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.08218430e+05, 2.90509465e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.07872716e+06, 1.07861922e+06, 1.49812534e+06, 1.07919705e+06, 1.04202416e+06, 6.74055391e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99912879e+05, 2.99974852e+05, 4.25869844e+05, 3.00048477e+05, 2.98972973e+05, 1.87407316e+05, ],
    'CountWeightedFull'                                                              : [ 2.99914914e+05, 2.99890109e+05, 2.99906301e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.08165656e+05, 2.99914914e+05, 2.90459793e+05, 3.08165656e+05, 2.99914914e+05, 2.90459793e+05, 3.08165656e+05, 2.99914914e+05, 2.90459793e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.08165656e+05, 2.90459793e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.07854603e+06, 1.07843705e+06, 1.49786684e+06, 1.07900697e+06, 1.04184284e+06, 6.73940578e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99862770e+05, 2.99923969e+05, 4.25796336e+05, 2.99995520e+05, 2.98920879e+05, 1.87375277e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1778819270), # 1.78GB, avg file size 889.41MB
  ("fsize_db",                        16130523073), # 16.13GB, avg file size 1.01GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_300_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 2.99943453e+05, 2.99984133e+05, 2.99943273e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.09783438e+05, 2.99943453e+05, 2.89265555e+05, 3.09783438e+05, 2.99943453e+05, 2.89265555e+05, 3.09783438e+05, 2.99943453e+05, 2.89265555e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.09783438e+05, 2.89265547e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.86300703e+05, 9.85538547e+05, 1.37879472e+06, 9.86441672e+05, 9.60543453e+05, 6.14449344e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99939648e+05, 2.99762867e+05, 4.27292266e+05, 2.99981445e+05, 3.00045281e+05, 1.86857789e+05, ],
    'CountWeightedFull'                                                              : [ 2.99888367e+05, 2.99928000e+05, 2.99887750e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.09726258e+05, 2.99888367e+05, 2.89212250e+05, 3.09726258e+05, 2.99888367e+05, 2.89212250e+05, 3.09726258e+05, 2.99888367e+05, 2.89212250e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.09726258e+05, 2.89212242e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.86123938e+05, 9.85357438e+05, 1.37853644e+06, 9.86253625e+05, 9.60364516e+05, 6.14337719e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99886055e+05, 2.99707695e+05, 4.27211820e+05, 2.99924172e+05, 2.99989141e+05, 1.86823949e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1828131213), # 1.83GB, avg file size 914.07MB
  ("fsize_db",                        16290185653), # 16.29GB, avg file size 1.25GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_320_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 2.99972926e+05, 2.99932078e+05, 2.99912266e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.11935551e+05, 2.99972926e+05, 2.87585117e+05, 3.11935551e+05, 2.99972926e+05, 2.87585117e+05, 3.11935551e+05, 2.99972926e+05, 2.87585117e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.11935551e+05, 2.87585117e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.14401794e+06, 1.14295977e+06, 1.58534334e+06, 1.14481558e+06, 1.09909820e+06, 7.11554062e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99834434e+05, 2.99731566e+05, 4.27122125e+05, 3.00043750e+05, 2.99510656e+05, 1.86490236e+05, ],
    'CountWeightedFull'                                                              : [ 2.99916477e+05, 2.99876855e+05, 2.99856762e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.11877742e+05, 2.99916477e+05, 2.87531922e+05, 3.11877742e+05, 2.99916477e+05, 2.87531922e+05, 3.11877742e+05, 2.99916477e+05, 2.87531922e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.11877742e+05, 2.87531922e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.14381683e+06, 1.14274892e+06, 1.58505050e+06, 1.14459961e+06, 1.09889656e+06, 7.11425531e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99781648e+05, 2.99676230e+05, 4.27044055e+05, 2.99987195e+05, 2.99456254e+05, 1.86456564e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1889198670), # 1.89GB, avg file size 944.60MB
  ("fsize_db",                        16256170207), # 16.26GB, avg file size 1.35GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_350_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 2.99957613e+05, 2.99960672e+05, 2.99932742e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.15107703e+05, 2.99950516e+05, 2.85246633e+05, 3.15107703e+05, 2.99950516e+05, 2.85246633e+05, 3.15107703e+05, 2.99950516e+05, 2.85246633e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.15107703e+05, 2.85246633e+05, ],
    'CountWeightedPSWeight'                                                          : [ 6.48843016e+05, 6.49805859e+05, 9.20667281e+05, 6.48971438e+05, 6.40555750e+05, 4.01255680e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99955805e+05, 3.00409000e+05, 4.28266984e+05, 3.00017914e+05, 2.98763133e+05, 1.85496898e+05, ],
    'CountWeightedFull'                                                              : [ 2.99901898e+05, 2.99904977e+05, 2.99878367e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.15049719e+05, 2.99894887e+05, 2.85193859e+05, 3.15049719e+05, 2.99894887e+05, 2.85193859e+05, 3.15049719e+05, 2.99894887e+05, 2.85193859e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.15049719e+05, 2.85193859e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 6.48728156e+05, 6.49686812e+05, 9.20495578e+05, 6.48848891e+05, 6.40436641e+05, 4.01183758e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99902641e+05, 3.00353906e+05, 4.28187016e+05, 2.99961148e+05, 2.98707508e+05, 1.85463625e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1983290415), # 1.98GB, avg file size 991.65MB
  ("fsize_db",                        17394059503), # 17.39GB, avg file size 1.16GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_400_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 2.99936234e+05, 2.99952047e+05, 2.99944594e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.20040125e+05, 2.99936234e+05, 2.81437672e+05, 3.20040125e+05, 2.99936234e+05, 2.81437672e+05, 3.20040125e+05, 2.99936234e+05, 2.81437672e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.20040125e+05, 2.81437672e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.44888547e+05, 8.44404422e+05, 1.19528147e+06, 8.44965016e+05, 8.28049312e+05, 5.18719281e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99969516e+05, 2.99816422e+05, 4.30309984e+05, 2.99996797e+05, 2.99913055e+05, 1.84168973e+05, ],
    'CountWeightedFull'                                                              : [ 2.99880531e+05, 2.99895516e+05, 2.99887922e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.19980141e+05, 2.99880531e+05, 2.81385102e+05, 3.19980141e+05, 2.99880531e+05, 2.81385102e+05, 3.19980141e+05, 2.99880531e+05, 2.81385102e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.19980141e+05, 2.81385102e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 8.44735125e+05, 8.44245469e+05, 1.19505494e+06, 8.44800750e+05, 8.27895375e+05, 5.18623719e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99914984e+05, 2.99760125e+05, 4.30228344e+05, 2.99938578e+05, 2.99857039e+05, 1.84134945e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     2141672673), # 2.14GB, avg file size 1.07GB
  ("fsize_db",                        17471951247), # 17.47GB, avg file size 1.34GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_500_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 2.99920430e+05, 2.99943020e+05, 2.99915848e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.22058230e+05, 2.99917953e+05, 2.79866281e+05, 3.22058230e+05, 2.99917953e+05, 2.79866281e+05, 3.22058230e+05, 2.99917953e+05, 2.79866281e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.22058230e+05, 2.79866281e+05, ],
    'CountWeightedPSWeight'                                                          : [ 6.38353664e+05, 6.38804125e+05, 9.12250297e+05, 6.38733750e+05, 6.32558656e+05, 3.90576812e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99909641e+05, 3.00122215e+05, 4.31303188e+05, 3.00083938e+05, 2.99896309e+05, 1.83499576e+05, ],
    'CountWeightedFull'                                                              : [ 2.99861840e+05, 2.99884113e+05, 2.99857582e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.21994605e+05, 2.99859379e+05, 2.79811395e+05, 3.21994605e+05, 2.99859379e+05, 2.79811395e+05, 3.21994605e+05, 2.99859379e+05, 2.79811395e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.21994605e+05, 2.79811395e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 6.38231633e+05, 6.38680234e+05, 9.12068625e+05, 6.38604055e+05, 6.32432117e+05, 3.90500746e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99852398e+05, 3.00063840e+05, 4.31217203e+05, 3.00022996e+05, 2.99836336e+05, 1.83463891e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     2194774834), # 2.19GB, avg file size 1.10GB
  ("fsize_db",                        18211430509), # 18.21GB, avg file size 2.28GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_550_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1492564507), # 1.49GB, avg file size 1.49GB
  ("fsize_db",                        12311761166), # 12.31GB, avg file size 1.76GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_600_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 1.99931850e+05, 1.99945871e+05, 1.99908004e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.17002898e+05, 1.99927125e+05, 1.84777742e+05, 2.17002898e+05, 1.99927125e+05, 1.84777742e+05, 2.17002898e+05, 1.99927125e+05, 1.84777742e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.17003352e+05, 1.84777289e+05, ],
    'CountWeightedPSWeight'                                                          : [ 4.39739598e+05, 4.39395047e+05, 6.29531125e+05, 4.39483637e+05, 4.35735023e+05, 2.67490227e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99984492e+05, 1.99838504e+05, 2.88552016e+05, 1.99871262e+05, 2.00403889e+05, 1.21645797e+05, ],
    'CountWeightedFull'                                                              : [ 1.99889074e+05, 1.99903119e+05, 1.99865922e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.16956766e+05, 1.99884436e+05, 1.84738293e+05, 2.16956766e+05, 1.99884436e+05, 1.84738293e+05, 2.16956766e+05, 1.99884436e+05, 1.84738293e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.16957219e+05, 1.84737824e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 4.39651645e+05, 4.39302656e+05, 6.29397508e+05, 4.39390629e+05, 4.35642945e+05, 2.67435621e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99944434e+05, 1.99796492e+05, 2.88490727e+05, 1.99828793e+05, 2.00361547e+05, 1.21620963e+05, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     1516198142), # 1.52GB, avg file size 758.10MB
  ("fsize_db",                        12454041911), # 12.45GB, avg file size 1.04GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_650_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 1.99949321e+05, 1.99947220e+05, 1.99955061e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.18015005e+05, 1.99947509e+05, 1.84040576e+05, 2.18015005e+05, 1.99947509e+05, 1.84040576e+05, 2.18015005e+05, 1.99947509e+05, 1.84040576e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.18015099e+05, 1.84040482e+05, ],
    'CountWeightedPSWeight'                                                          : [ 4.51231432e+05, 4.50294463e+05, 6.45076730e+05, 4.50570043e+05, 4.46341385e+05, 2.74148017e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.00118992e+05, 1.99697118e+05, 2.88433808e+05, 1.99820468e+05, 2.00309262e+05, 1.21591378e+05, ],
    'CountWeightedFull'                                                              : [ 1.99907893e+05, 1.99905751e+05, 1.99913732e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.17969958e+05, 1.99906080e+05, 1.84002658e+05, 2.17969958e+05, 1.99906080e+05, 1.84002658e+05, 2.17969958e+05, 1.99906080e+05, 1.84002658e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.17970021e+05, 1.84002564e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 4.51143275e+05, 4.50199758e+05, 6.44941457e+05, 4.50475271e+05, 4.46250314e+05, 2.74093232e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.00079904e+05, 1.99655254e+05, 2.88372912e+05, 1.99778575e+05, 2.00267910e+05, 1.21567065e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1532541361), # 1.53GB, avg file size 766.27MB
  ("fsize_db",                        12555546335), # 12.56GB, avg file size 965.81MB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_700_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 1.99962739e+05, 1.99959387e+05, 1.99972062e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99962739e+05, 1.99962739e+05, ],
    'CountWeightedPSWeight'                                                          : [ 4.64202094e+05, 4.63992941e+05, 6.63881262e+05, 4.64393635e+05, 4.58031107e+05, 2.81488365e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99936171e+05, 1.99852723e+05, 2.88441460e+05, 2.00018615e+05, 1.99776289e+05, 1.21241789e+05, ],
    'CountWeightedFull'                                                              : [ 1.99921127e+05, 1.99917262e+05, 1.99930451e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99921127e+05, 1.99921127e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 4.64110414e+05, 4.63896684e+05, 6.63743584e+05, 4.64295727e+05, 4.57936461e+05, 2.81431149e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99896606e+05, 1.99811287e+05, 2.88381768e+05, 1.99976353e+05, 1.99735039e+05, 1.21217168e+05, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     1554081946), # 1.55GB, avg file size 777.04MB
  ("fsize_db",                        13006707251), # 13.01GB, avg file size 929.05MB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_750_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 1.99958287e+05, 1.99938587e+05, 1.99950391e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99958287e+05, 1.99958287e+05, ],
    'CountWeightedPSWeight'                                                          : [ 4.79319814e+05, 4.79356928e+05, 6.84310580e+05, 4.79288135e+05, 4.70850922e+05, 2.90177993e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99999688e+05, 2.00023009e+05, 2.88293687e+05, 1.99986271e+05, 1.99214335e+05, 1.21075136e+05, ],
    'CountWeightedFull'                                                              : [ 1.99913964e+05, 1.99894550e+05, 1.99906512e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99913964e+05, 1.99913964e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 4.79220584e+05, 4.79253146e+05, 6.84160689e+05, 4.79181570e+05, 4.70746832e+05, 2.90116370e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99958215e+05, 1.99979688e+05, 2.88230325e+05, 1.99941981e+05, 1.99170175e+05, 1.21049467e+05, ],
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     1564121946), # 1.56GB, avg file size 782.06MB
  ("fsize_db",                        13089476147), # 13.09GB, avg file size 934.96MB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_800_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1572778147), # 1.57GB, avg file size 1.57GB
  ("fsize_db",                        13167424036), # 13.17GB, avg file size 1.01GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_850_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 1.99973550e+05, 1.99954398e+05, 1.99955201e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.21322865e+05, 1.99973550e+05, 1.81639109e+05, 2.21322865e+05, 1.99973550e+05, 1.81639109e+05, 2.21322865e+05, 1.99973550e+05, 1.81639109e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.21323068e+05, 1.81638922e+05, ],
    'CountWeightedPSWeight'                                                          : [ 6.88895102e+05, 6.87733266e+05, 9.72151445e+05, 6.89055670e+05, 6.65058572e+05, 4.15440982e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99958036e+05, 1.99697673e+05, 2.89368107e+05, 2.00006032e+05, 2.00155707e+05, 1.20584306e+05, ],
    'CountWeightedFull'                                                              : [ 1.99928558e+05, 1.99909037e+05, 1.99910780e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.21273164e+05, 1.99928558e+05, 1.81598360e+05, 2.21273164e+05, 1.99928558e+05, 1.81598360e+05, 2.21273164e+05, 1.99928558e+05, 1.81598360e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.21273352e+05, 1.81598188e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 6.88749154e+05, 6.87581049e+05, 9.71932262e+05, 6.88898240e+05, 6.64907564e+05, 4.15351020e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99915676e+05, 1.99653441e+05, 2.89302347e+05, 1.99960276e+05, 2.00109702e+05, 1.20558148e+05, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     1578626134), # 1.58GB, avg file size 789.31MB
  ("fsize_db",                        12520224790), # 12.52GB, avg file size 1.04GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_900_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     797684854), # 797.68MB, avg file size 797.68MB
  ("fsize_db",                        6339783437), # 6.34GB, avg file size 704.42MB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_1000_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     814036735), # 814.04MB, avg file size 814.04MB
  ("fsize_db",                        6214334271), # 6.21GB, avg file size 1.04GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_1250_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 9.99488535e+04, 9.99521543e+04, 9.99445684e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.13888332e+05, 9.99482324e+04, 8.85137461e+04, 1.13888332e+05, 9.99482324e+04, 8.85137461e+04, 1.13888332e+05, 9.99482324e+04, 8.85137461e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.13888742e+05, 8.85133359e+04, ],
    'CountWeightedPSWeight'                                                          : [ 6.03263211e+05, 5.92226570e+05, 7.96973906e+05, 6.03341672e+05, 5.31338125e+05, 3.58266570e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99704863e+04, 9.99361680e+04, 1.45730361e+05, 1.00000703e+05, 9.99037441e+04, 5.93737578e+04, ],
    'CountWeightedFull'                                                              : [ 9.99221777e+04, 9.99253516e+04, 9.99182637e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.13857973e+05, 9.99215547e+04, 8.84901113e+04, 1.13857973e+05, 9.99215547e+04, 8.84901113e+04, 1.13857973e+05, 9.99215547e+04, 8.84901113e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.13858381e+05, 8.84897002e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 6.03120023e+05, 5.92068742e+05, 7.96761172e+05, 6.03186016e+05, 5.31197320e+05, 3.58179117e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99467207e+04, 9.99095820e+04, 1.45691654e+05, 9.99748750e+04, 9.98774277e+04, 5.93592480e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     814400142), # 814.40MB, avg file size 407.20MB
  ("fsize_db",                        6217807927), # 6.22GB, avg file size 777.23MB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_1500_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     820468576), # 820.47MB, avg file size 820.47MB
  ("fsize_db",                        6399858338), # 6.40GB, avg file size 711.10MB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_1750_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     821529529), # 821.53MB, avg file size 821.53MB
  ("fsize_db",                        6250048572), # 6.25GB, avg file size 781.26MB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_2000_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     832872433), # 832.87MB, avg file size 832.87MB
  ("fsize_db",                        6648889879), # 6.65GB, avg file size 554.07MB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_2500_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 9.97513184e+04, 9.97542129e+04, 9.97446484e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.97513184e+04, 9.97513184e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.96460859e+05, 9.92294391e+05, 9.97439047e+05, 9.96325953e+05, 9.65275250e+05, 9.60368250e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99962578e+04, 1.00102289e+05, 1.46391395e+05, 9.99936016e+04, 9.95480137e+04, 5.86894551e+04, ],
    'CountWeightedFull'                                                              : [ 9.97194316e+04, 9.97223672e+04, 9.97127227e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.97194316e+04, 9.97194316e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.96151203e+05, 9.91976656e+05, 9.97120078e+05, 9.96016625e+05, 9.64969906e+05, 9.60071031e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99670762e+04, 1.00069615e+05, 1.46343752e+05, 9.99619805e+04, 9.95165020e+04, 5.86715908e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     840264476), # 840.26MB, avg file size 420.13MB
  ("fsize_db",                        6767988851), # 6.77GB, avg file size 676.80MB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_3000_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99958859e+05, 3.99966312e+05, 3.99961359e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.04901516e+05, 3.99958000e+05, 3.92209047e+05, 4.04901516e+05, 3.99958000e+05, 3.92209047e+05, 4.04901516e+05, 3.99958000e+05, 3.92209047e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.04901516e+05, 3.92209047e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99960462e+06, 3.99960462e+06, 3.99960462e+06, 3.99960462e+06, 3.99960462e+06, 3.99960462e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00011297e+05, 4.00158156e+05, 5.67958625e+05, 3.99960812e+05, 3.99028688e+05, 2.50314141e+05, ],
    'CountWeightedFull'                                                              : [ 3.99889688e+05, 3.99897328e+05, 3.99892062e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.04831172e+05, 3.99888656e+05, 3.92140641e+05, 4.04831172e+05, 3.99888656e+05, 3.92140641e+05, 4.04831172e+05, 3.99888656e+05, 3.92140641e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.04831172e+05, 3.92140641e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99891112e+06, 3.99891112e+06, 3.99891112e+06, 3.99891112e+06, 3.99891112e+06, 3.99891112e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99943906e+05, 4.00088906e+05, 5.67858312e+05, 3.99889000e+05, 3.98958141e+05, 2.50271391e+05, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     2230427268), # 2.23GB, avg file size 1.12GB
  ("fsize_db",                        21099457960), # 21.10GB, avg file size 1.76GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_250_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99961266e+05, 3.99976578e+05, 3.99968797e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.06222766e+05, 3.99955078e+05, 3.91162172e+05, 4.06222766e+05, 3.99955078e+05, 3.91162172e+05, 4.06222766e+05, 3.99955078e+05, 3.91162172e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.06222766e+05, 3.91162172e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99981075e+06, 3.99981075e+06, 3.99981075e+06, 3.99981075e+06, 3.99981075e+06, 3.99981075e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99971781e+05, 4.00009484e+05, 5.69266375e+05, 4.00059656e+05, 3.99924672e+05, 2.49805359e+05, ],
    'CountWeightedFull'                                                              : [ 3.99892984e+05, 3.99907891e+05, 3.99899828e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.06153047e+05, 3.99886766e+05, 3.91095250e+05, 4.06153047e+05, 3.99886766e+05, 3.91095250e+05, 4.06153047e+05, 3.99886766e+05, 3.91095250e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.06153047e+05, 3.91095250e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99912550e+06, 3.99912550e+06, 3.99912550e+06, 3.99912550e+06, 3.99912550e+06, 3.99912550e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99905016e+05, 3.99940781e+05, 5.69167656e+05, 3.99989078e+05, 3.99856062e+05, 2.49763055e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     2276965614), # 2.28GB, avg file size 1.14GB
  ("fsize_db",                        21222151277), # 21.22GB, avg file size 1.06GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_260_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99971734e+05, 3.99960000e+05, 3.99953844e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.07472734e+05, 3.99971734e+05, 3.90124266e+05, 4.07472734e+05, 3.99971734e+05, 3.90124266e+05, 4.07472734e+05, 3.99971734e+05, 3.90124266e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.07472734e+05, 3.90124266e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99989888e+06, 3.99989888e+06, 3.99989888e+06, 3.99989888e+06, 3.99989888e+06, 3.99989888e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00093094e+05, 4.00542500e+05, 5.68943281e+05, 3.99869828e+05, 3.98850047e+05, 2.49502078e+05, ],
    'CountWeightedFull'                                                              : [ 3.99900688e+05, 3.99889891e+05, 3.99882500e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.07400750e+05, 3.99900688e+05, 3.90055469e+05, 4.07400750e+05, 3.99900688e+05, 3.90055469e+05, 4.07400750e+05, 3.99900688e+05, 3.90055469e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.07400750e+05, 3.90055469e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99918388e+06, 3.99918388e+06, 3.99918388e+06, 3.99918388e+06, 3.99918388e+06, 3.99918388e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 4.00024438e+05, 4.00472469e+05, 5.68841375e+05, 3.99796875e+05, 3.98778578e+05, 2.49458656e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     2320938564), # 2.32GB, avg file size 1.16GB
  ("fsize_db",                        21635602520), # 21.64GB, avg file size 1.27GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_270_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99933656e+05, 3.99989016e+05, 3.99972297e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.08688906e+05, 3.99929219e+05, 3.89154953e+05, 4.08688906e+05, 3.99929219e+05, 3.89154953e+05, 4.08688906e+05, 3.99929219e+05, 3.89154953e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.08688906e+05, 3.89154953e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99934988e+06, 3.99936012e+06, 3.99936012e+06, 3.99934988e+06, 3.99936012e+06, 3.99934988e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99940016e+05, 3.99749094e+05, 5.68610375e+05, 4.00021234e+05, 3.99200828e+05, 2.49549367e+05, ],
    'CountWeightedFull'                                                              : [ 3.99860297e+05, 3.99915281e+05, 3.99898094e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.08613641e+05, 3.99855859e+05, 3.89083328e+05, 4.08613641e+05, 3.99855859e+05, 3.89083328e+05, 4.08613641e+05, 3.99855859e+05, 3.89083328e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.08613641e+05, 3.89083328e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99862312e+06, 3.99862312e+06, 3.99862312e+06, 3.99862312e+06, 3.99862312e+06, 3.99862312e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99869688e+05, 3.99676016e+05, 5.68505656e+05, 3.99946109e+05, 3.99127438e+05, 2.49504586e+05, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     2365768879), # 2.37GB, avg file size 1.18GB
  ("fsize_db",                        21492020096), # 21.49GB, avg file size 1.79GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_280_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 2.99994586e+05, 3.00011715e+05, 2.99982547e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.08261480e+05, 2.99994586e+05, 2.90533266e+05, 3.08261480e+05, 2.99994586e+05, 2.90533266e+05, 3.08261480e+05, 2.99994586e+05, 2.90533266e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.08261480e+05, 2.90533266e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99976244e+06, 2.99976244e+06, 2.99976244e+06, 2.99976244e+06, 2.99976244e+06, 2.99976244e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.00079312e+05, 3.00055477e+05, 4.27338242e+05, 2.99878145e+05, 2.99645309e+05, 1.86751633e+05, ],
    'CountWeightedFull'                                                              : [ 2.99941953e+05, 2.99958066e+05, 2.99930410e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.08207141e+05, 2.99941953e+05, 2.90481984e+05, 3.08207141e+05, 2.99941953e+05, 2.90481984e+05, 3.08207141e+05, 2.99941953e+05, 2.90481984e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.08207141e+05, 2.90481984e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99923444e+06, 2.99923444e+06, 2.99923444e+06, 2.99923444e+06, 2.99923444e+06, 2.99923444e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.00027793e+05, 3.00002715e+05, 4.27262383e+05, 2.99823352e+05, 2.99592480e+05, 1.86719094e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1834152821), # 1.83GB, avg file size 917.08MB
  ("fsize_db",                        16166482441), # 16.17GB, avg file size 1.15GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_300_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 2.99975875e+05, 2.99997359e+05, 2.99968242e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.09821023e+05, 2.99975875e+05, 2.89287812e+05, 3.09821023e+05, 2.99975875e+05, 2.89287812e+05, 3.09821023e+05, 2.99975875e+05, 2.89287812e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.09821023e+05, 2.89287812e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99973438e+06, 2.99973438e+06, 2.99973438e+06, 2.99973438e+06, 2.99973438e+06, 2.99973438e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.00022383e+05, 2.99848039e+05, 4.27649758e+05, 2.99960797e+05, 2.99798836e+05, 1.86490547e+05, ],
    'CountWeightedFull'                                                              : [ 2.99922164e+05, 2.99942875e+05, 2.99915141e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.09765438e+05, 2.99922164e+05, 2.89235766e+05, 3.09765438e+05, 2.99922164e+05, 2.89235766e+05, 3.09765438e+05, 2.99922164e+05, 2.89235766e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.09765438e+05, 2.89235766e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99919425e+06, 2.99919425e+06, 2.99919425e+06, 2.99919425e+06, 2.99919425e+06, 2.99919425e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99969766e+05, 2.99794562e+05, 4.27572461e+05, 2.99905234e+05, 2.99744438e+05, 1.86457328e+05, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1886991217), # 1.89GB, avg file size 943.50MB
  ("fsize_db",                        16707306428), # 16.71GB, avg file size 1.39GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_320_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 2.99879367e+05, 2.99927699e+05, 2.99908578e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.11915355e+05, 2.99879367e+05, 2.87578680e+05, 3.11915355e+05, 2.99879367e+05, 2.87578680e+05, 3.11915355e+05, 2.99879367e+05, 2.87578680e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.11915355e+05, 2.87578680e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99918038e+06, 2.99918038e+06, 2.99918038e+06, 2.99918038e+06, 2.99918038e+06, 2.99918038e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.00010285e+05, 2.99867426e+05, 4.28501547e+05, 2.99867109e+05, 2.99824410e+05, 1.85646516e+05, ],
    'CountWeightedFull'                                                              : [ 2.99824969e+05, 2.99873125e+05, 2.99853562e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.11858441e+05, 2.99824969e+05, 2.87525992e+05, 3.11858441e+05, 2.99824969e+05, 2.87525992e+05, 3.11858441e+05, 2.99824969e+05, 2.87525992e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.11858441e+05, 2.87525992e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99863369e+06, 2.99863369e+06, 2.99863369e+06, 2.99863369e+06, 2.99863369e+06, 2.99863369e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99957621e+05, 2.99813445e+05, 4.28419688e+05, 2.99811148e+05, 2.99766230e+05, 1.85613363e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1958867092), # 1.96GB, avg file size 979.43MB
  ("fsize_db",                        17008053450), # 17.01GB, avg file size 1.42GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_350_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 2.99970797e+05, 2.99964500e+05, 2.99957547e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.15103828e+05, 2.99970797e+05, 2.85246656e+05, 3.15103828e+05, 2.99970797e+05, 2.85246656e+05, 3.15103828e+05, 2.99970797e+05, 2.85246656e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.15103844e+05, 2.85246578e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99924962e+06, 2.99924962e+06, 2.99924962e+06, 2.99924962e+06, 2.99924962e+06, 2.99924962e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99987797e+05, 2.99918844e+05, 4.29371688e+05, 2.99941289e+05, 2.99954164e+05, 1.85050203e+05, ],
    'CountWeightedFull'                                                              : [ 2.99914961e+05, 2.99908391e+05, 2.99900773e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.15045000e+05, 2.99914961e+05, 2.85193258e+05, 3.15045000e+05, 2.99914961e+05, 2.85193258e+05, 3.15045000e+05, 2.99914961e+05, 2.85193258e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.15045016e+05, 2.85193180e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99869738e+06, 2.99869738e+06, 2.99869738e+06, 2.99869738e+06, 2.99869738e+06, 2.99869738e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99933297e+05, 2.99863266e+05, 4.29290359e+05, 2.99883203e+05, 2.99897203e+05, 1.85015992e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     2066182685), # 2.07GB, avg file size 1.03GB
  ("fsize_db",                        17452430860), # 17.45GB, avg file size 1.16GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_400_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 2.99938836e+05, 2.99893625e+05, 2.99914828e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.17708902e+05, 2.99936672e+05, 2.83189574e+05, 3.17708902e+05, 2.99936672e+05, 2.83189574e+05, 3.17708902e+05, 2.99936672e+05, 2.83189574e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.17708902e+05, 2.83189574e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99870891e+06, 2.99872366e+06, 2.99872366e+06, 2.99870891e+06, 2.99872366e+06, 2.99870891e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99894309e+05, 2.99845750e+05, 4.29900773e+05, 3.00009270e+05, 2.99731086e+05, 1.84386764e+05, ],
    'CountWeightedFull'                                                              : [ 2.99878180e+05, 2.99834898e+05, 2.99854988e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.17645574e+05, 2.99876035e+05, 2.83133148e+05, 3.17645574e+05, 2.99876035e+05, 2.83133148e+05, 3.17645574e+05, 2.99876035e+05, 2.83133148e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.17645574e+05, 2.83133148e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99814181e+06, 2.99814181e+06, 2.99814181e+06, 2.99814181e+06, 2.99814181e+06, 2.99814181e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99838266e+05, 2.99785145e+05, 4.29813828e+05, 2.99949445e+05, 2.99671902e+05, 1.84351572e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     2154569259), # 2.15GB, avg file size 1.08GB
  ("fsize_db",                        18286814735), # 18.29GB, avg file size 2.29GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_450_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 2.99949359e+05, 2.99983438e+05, 2.99957562e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.20056828e+05, 2.99949359e+05, 2.81465867e+05, 3.20056828e+05, 2.99949359e+05, 2.81465867e+05, 3.20056828e+05, 2.99949359e+05, 2.81465867e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.20056828e+05, 2.81465867e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99925025e+06, 2.99925731e+06, 2.99925731e+06, 2.99925025e+06, 2.99925731e+06, 2.99925025e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99889242e+05, 3.00285914e+05, 4.30421031e+05, 3.00097406e+05, 2.99098641e+05, 1.83807855e+05, ],
    'CountWeightedFull'                                                              : [ 2.99889078e+05, 2.99922352e+05, 2.99897141e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.19992516e+05, 2.99889078e+05, 2.81408758e+05, 3.19992516e+05, 2.99889078e+05, 2.81408758e+05, 3.19992516e+05, 2.99889078e+05, 2.81408758e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.19992516e+05, 2.81408758e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99866725e+06, 2.99866725e+06, 2.99866725e+06, 2.99866725e+06, 2.99866725e+06, 2.99866725e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99832031e+05, 3.00226023e+05, 4.30333594e+05, 3.00036031e+05, 2.99037266e+05, 1.83771977e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     2223776940), # 2.22GB, avg file size 1.11GB
  ("fsize_db",                        18029238407), # 18.03GB, avg file size 1.80GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_500_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 2.99932238e+05, 2.99936328e+05, 2.99920215e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.22048535e+05, 2.99932238e+05, 2.79890234e+05, 3.22048535e+05, 2.99932238e+05, 2.79890234e+05, 3.22048535e+05, 2.99932238e+05, 2.79890234e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.22048941e+05, 2.79889844e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99940153e+06, 2.99940153e+06, 2.99940153e+06, 2.99940153e+06, 2.99940153e+06, 2.99940153e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99907688e+05, 3.00079652e+05, 4.31138477e+05, 3.00014465e+05, 2.99295203e+05, 1.83221818e+05, ],
    'CountWeightedFull'                                                              : [ 2.99872914e+05, 2.99877289e+05, 2.99860617e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.21984465e+05, 2.99872914e+05, 2.79833961e+05, 3.21984465e+05, 2.99872914e+05, 2.79833961e+05, 3.21984465e+05, 2.99872914e+05, 2.79833961e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.21984840e+05, 2.79833570e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99880372e+06, 2.99880372e+06, 2.99880372e+06, 2.99880372e+06, 2.99880372e+06, 2.99880372e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99850152e+05, 3.00020359e+05, 4.31052203e+05, 2.99952547e+05, 2.99235355e+05, 1.83185693e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     2276176858), # 2.28GB, avg file size 1.14GB
  ("fsize_db",                        17868443167), # 17.87GB, avg file size 1.62GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_550_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 1.99945719e+05, 1.99972162e+05, 1.99968136e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.15927211e+05, 1.99945719e+05, 1.85645501e+05, 2.15927211e+05, 1.99945719e+05, 1.85645501e+05, 2.15927211e+05, 1.99945719e+05, 1.85645501e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.15928023e+05, 1.85644689e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99954062e+06, 1.99954062e+06, 1.99954062e+06, 1.99954062e+06, 1.99954062e+06, 1.99954062e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99948825e+05, 2.00164134e+05, 2.87634024e+05, 2.00048805e+05, 1.99307863e+05, 1.21826281e+05, ],
    'CountWeightedFull'                                                              : [ 1.99904029e+05, 1.99929697e+05, 1.99925486e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.15881854e+05, 1.99904029e+05, 1.85606285e+05, 2.15881854e+05, 1.99904029e+05, 1.85606285e+05, 2.15881854e+05, 1.99904029e+05, 1.85606285e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.15882667e+05, 1.85605472e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.99911943e+06, 1.99911943e+06, 1.99911943e+06, 1.99911943e+06, 1.99911943e+06, 1.99911943e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99909122e+05, 2.00121927e+05, 2.87573240e+05, 2.00006389e+05, 1.99265888e+05, 1.21801417e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1544846879), # 1.54GB, avg file size 772.42MB
  ("fsize_db",                        12265654789), # 12.27GB, avg file size 1.12GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_600_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1563999470), # 1.56GB, avg file size 1.56GB
  ("fsize_db",                        12362249390), # 12.36GB, avg file size 1.77GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_650_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1573835903), # 1.57GB, avg file size 1.57GB
  ("fsize_db",                        12213272084), # 12.21GB, avg file size 1.22GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_700_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1584045869), # 1.58GB, avg file size 1.58GB
  ("fsize_db",                        12949339827), # 12.95GB, avg file size 1.08GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_750_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1590351418), # 1.59GB, avg file size 1.59GB
  ("fsize_db",                        12584995133), # 12.58GB, avg file size 1.57GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_800_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1579736200), # 1.58GB, avg file size 1.58GB
  ("fsize_db",                        13202094182), # 13.20GB, avg file size 1.89GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_850_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 1.99956062e+05, 1.99944396e+05, 1.99951941e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99956062e+05, 1.99956062e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99936073e+06, 1.99936073e+06, 1.99936073e+06, 1.99936073e+06, 1.99936073e+06, 1.99936073e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99896678e+05, 1.99761475e+05, 2.89789387e+05, 2.00120914e+05, 2.00150086e+05, 1.20421824e+05, ],
    'CountWeightedFull'                                                              : [ 1.99910449e+05, 1.99899211e+05, 1.99906537e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99910449e+05, 1.99910449e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.99891030e+06, 1.99891030e+06, 1.99891030e+06, 1.99891030e+06, 1.99891030e+06, 1.99891030e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99853676e+05, 1.99716176e+05, 2.89724529e+05, 2.00074527e+05, 2.00105414e+05, 1.20395075e+05, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     1611610221), # 1.61GB, avg file size 805.81MB
  ("fsize_db",                        13510236979), # 13.51GB, avg file size 1.23GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_900_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     710345768), # 710.35MB, avg file size 710.35MB
  ("fsize_db",                        5575990858), # 5.58GB, avg file size 2.79GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_1000_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     797413281), # 797.41MB, avg file size 797.41MB
  ("fsize_db",                        6322077799), # 6.32GB, avg file size 1.26GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_1250_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     794949467), # 794.95MB, avg file size 794.95MB
  ("fsize_db",                        6498665132), # 6.50GB, avg file size 649.87MB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_1500_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     796769019), # 796.77MB, avg file size 796.77MB
  ("fsize_db",                        7054399734), # 7.05GB, avg file size 705.44MB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_1750_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     799726581), # 799.73MB, avg file size 799.73MB
  ("fsize_db",                        6472017019), # 6.47GB, avg file size 924.57MB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_2000_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     805607388), # 805.61MB, avg file size 805.61MB
  ("fsize_db",                        6553856520), # 6.55GB, avg file size 936.27MB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_2500_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     812245788), # 812.25MB, avg file size 812.25MB
  ("fsize_db",                        6743129991), # 6.74GB, avg file size 1.12GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_3000_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99990031e+05, 3.99946734e+05, 3.99979250e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99990031e+05, 3.99990031e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99970025e+06, 3.99970025e+06, 3.99970025e+06, 3.99970025e+06, 3.99970025e+06, 3.99970025e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99991109e+05, 3.99826656e+05, 5.57040938e+05, 3.99863031e+05, 3.99800172e+05, 2.56347555e+05, ],
    'CountWeightedFull'                                                              : [ 3.99761547e+05, 3.99719812e+05, 3.99751688e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99761547e+05, 3.99761547e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99741900e+06, 3.99741900e+06, 3.99741900e+06, 3.99741900e+06, 3.99741900e+06, 3.99741900e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99809203e+05, 3.99598359e+05, 5.56714469e+05, 3.99682047e+05, 3.99563328e+05, 2.56231641e+05, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     2623059640), # 2.62GB, avg file size 1.31GB
  ("fsize_db",                        23660265098), # 23.66GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        4.773e-05),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_nonresonant_1_1_1_hh_2b2v_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2498663954), # 2.50GB, avg file size 1.25GB
  ("fsize_db",                        23019095049), # 23.02GB, avg file size 1.21GB
  ("use_it",                          False),
  ("xsection",                        4.773e-05),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_nonresonant_1_1_1_hh_2b2v_dipoleRecoilOn"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.95966305e+05, 3.95939492e+05, 3.95958438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.95966305e+05, 3.95966305e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.95929138e+06, 3.95929912e+06, 3.95929912e+06, 3.95929138e+06, 3.95929912e+06, 3.95929138e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.95769820e+05, 3.95691539e+05, 5.55107109e+05, 3.96028430e+05, 3.95798508e+05, 2.50639008e+05, ],
    'CountWeightedFull'                                                              : [ 3.95709062e+05, 3.95685125e+05, 3.95702609e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.95709062e+05, 3.95709062e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.95676144e+06, 3.95676144e+06, 3.95676144e+06, 3.95676144e+06, 3.95676144e+06, 3.95676144e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.95577094e+05, 3.95435992e+05, 5.54751328e+05, 3.95835070e+05, 3.95543773e+05, 2.50517078e+05, ],
  }),
  ("nof_tree_events",                 395997),
  ("nof_db_events",                   395997),
  ("fsize_local",                     2788187717), # 2.79GB, avg file size 929.40MB
  ("fsize_db",                        24106383775), # 24.11GB, avg file size 1.27GB
  ("use_it",                          True),
  ("xsection",                        3.9346e-05),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_nonresonant_1_1_2_hh_2b2v_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99958500e+05, 3.99992953e+05, 4.00007469e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99958500e+05, 3.99958500e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99971725e+06, 3.99980875e+06, 3.99980875e+06, 3.99971975e+06, 3.99980875e+06, 3.99971600e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99703344e+05, 4.00215000e+05, 5.57968531e+05, 4.00105562e+05, 3.98764406e+05, 2.54887578e+05, ],
    'CountWeightedFull'                                                              : [ 3.99654594e+05, 3.99683719e+05, 3.99700312e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99654594e+05, 3.99654594e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99674550e+06, 3.99674550e+06, 3.99674550e+06, 3.99674550e+06, 3.99674550e+06, 3.99674550e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99503188e+05, 3.99904156e+05, 5.57544375e+05, 3.99905219e+05, 3.98461766e+05, 2.54760102e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     3112784354), # 3.11GB, avg file size 1.56GB
  ("fsize_db",                        26601674546), # 26.60GB, avg file size 1.27GB
  ("use_it",                          True),
  ("xsection",                        0.000393175),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_nonresonant_1_2_1_hh_2b2v_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2984268047), # 2.98GB, avg file size 746.07MB
  ("fsize_db",                        25257880512), # 25.26GB, avg file size 1.15GB
  ("use_it",                          False),
  ("xsection",                        0.000393175),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_nonresonant_1_2_1_hh_2b2v_dipoleRecoilOn"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99937859e+05, 3.99903125e+05, 3.99944234e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99937859e+05, 3.99937859e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99915900e+06, 3.99917175e+06, 3.99917175e+06, 3.99915950e+06, 3.99917175e+06, 3.99915900e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99890828e+05, 4.00035188e+05, 5.55661859e+05, 3.99903406e+05, 3.98894719e+05, 2.57082648e+05, ],
    'CountWeightedFull'                                                              : [ 3.99727094e+05, 3.99692094e+05, 3.99733375e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99727094e+05, 3.99727094e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99704250e+06, 3.99704250e+06, 3.99704250e+06, 3.99704250e+06, 3.99704250e+06, 3.99704250e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99717406e+05, 3.99820141e+05, 5.55366906e+05, 3.99729469e+05, 3.98685359e+05, 2.56971562e+05, ],
  }),
  ("nof_tree_events",                 399999),
  ("nof_db_events",                   399999),
  ("fsize_local",                     2621371599), # 2.62GB, avg file size 1.31GB
  ("fsize_db",                        23615969861), # 23.62GB, avg file size 1.24GB
  ("use_it",                          True),
  ("xsection",                        0.000127452),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_nonresonant_1_1_0_hh_2b2v_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99951250e+05, 3.99970875e+05, 3.99942672e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99951250e+05, 3.99951250e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99970438e+06, 3.99981550e+06, 3.99981550e+06, 3.99970338e+06, 3.99981550e+06, 3.99970262e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99843750e+05, 3.99909781e+05, 5.57366156e+05, 3.99989891e+05, 3.99647266e+05, 2.55996891e+05, ],
    'CountWeightedFull'                                                              : [ 3.99685438e+05, 3.99702641e+05, 3.99680922e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99685438e+05, 3.99685438e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99716512e+06, 3.99716512e+06, 3.99716512e+06, 3.99716512e+06, 3.99716512e+06, 3.99716512e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99657641e+05, 3.99645094e+05, 5.56996656e+05, 3.99803219e+05, 3.99380250e+05, 2.55877328e+05, ],
  }),
  ("nof_tree_events",                 399999),
  ("nof_db_events",                   399999),
  ("fsize_local",                     2854903279), # 2.85GB, avg file size 1.43GB
  ("fsize_db",                        25237710585), # 25.24GB, avg file size 2.52GB
  ("use_it",                          True),
  ("xsection",                        0.001825654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_nonresonant_1p5_1_1_hh_2b2v_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99984453e+05, 3.99943219e+05, 3.99933250e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99984453e+05, 3.99984453e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99967250e+06, 3.99972300e+06, 3.99972300e+06, 3.99967225e+06, 3.99972300e+06, 3.99967225e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99906188e+05, 4.00256984e+05, 5.58233953e+05, 3.99840766e+05, 3.99307656e+05, 2.55096812e+05, ],
    'CountWeightedFull'                                                              : [ 3.99709203e+05, 3.99670266e+05, 3.99655516e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99709203e+05, 3.99709203e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99693888e+06, 3.99693888e+06, 3.99693888e+06, 3.99693888e+06, 3.99693888e+06, 3.99693888e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99712656e+05, 3.99981641e+05, 5.57848344e+05, 3.99647438e+05, 3.99028312e+05, 2.54973117e+05, ],
  }),
  ("nof_tree_events",                 399999),
  ("nof_db_events",                   399999),
  ("fsize_local",                     3037984175), # 3.04GB, avg file size 1.52GB
  ("fsize_db",                        25513228160), # 25.51GB, avg file size 2.55GB
  ("use_it",                          True),
  ("xsection",                        0.000299315),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_nonresonant_0p5_1_1_hh_2b2v_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 4.00002172e+05, 3.99940781e+05, 3.99977641e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.00002172e+05, 4.00002172e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99959775e+06, 3.99961875e+06, 3.99961875e+06, 3.99959775e+06, 3.99961875e+06, 3.99959775e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99947641e+05, 3.99900047e+05, 5.57295969e+05, 3.99921578e+05, 3.99664547e+05, 2.56056273e+05, ],
    'CountWeightedFull'                                                              : [ 3.99758141e+05, 3.99700531e+05, 3.99736359e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99758141e+05, 3.99758141e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99718388e+06, 3.99718388e+06, 3.99718388e+06, 3.99718388e+06, 3.99718388e+06, 3.99718388e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99759578e+05, 3.99659750e+05, 5.56951594e+05, 3.99732844e+05, 3.99408578e+05, 2.55936211e+05, ],
  }),
  ("nof_tree_events",                 399999),
  ("nof_db_events",                   399999),
  ("fsize_local",                     2937223487), # 2.94GB, avg file size 1.47GB
  ("fsize_db",                        25638125950), # 25.64GB, avg file size 2.14GB
  ("use_it",                          True),
  ("xsection",                        0.000748862),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_nonresonant_1_0_1_hh_2b2v_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99943297e+05, 3.99951658e+05, 3.99963725e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.11969602e+05, 4.83222305e+05, 4.56250859e+05, 4.23832705e+05, 3.99942037e+05, 3.77546283e+05, 3.56936500e+05, 3.36753746e+05, 3.17845449e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.11970758e+05, 3.17844449e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99987278e+06, 3.99987278e+06, 3.99987278e+06, 3.99987278e+06, 3.99987278e+06, 3.99987278e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99892088e+05, 3.99445943e+05, 5.73583875e+05, 4.00091596e+05, 4.00283959e+05, 2.45840242e+05, ],
    'CountWeightedFull'                                                              : [ 3.99864160e+05, 3.99873627e+05, 3.99883965e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.11868646e+05, 4.83127215e+05, 4.56160996e+05, 4.23748957e+05, 3.99862885e+05, 3.77471857e+05, 3.56865875e+05, 3.36687361e+05, 3.17782896e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.11869834e+05, 3.17781896e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99907023e+06, 3.99907023e+06, 3.99907023e+06, 3.99907023e+06, 3.99907023e+06, 3.99907023e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99815775e+05, 3.99367686e+05, 5.73467875e+05, 4.00010514e+05, 4.00203100e+05, 2.45792722e+05, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     2780164776), # 2.78GB, avg file size 926.72MB
  ("fsize_db",                        23207192931), # 23.21GB, avg file size 1.55GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_node_sm_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99990406e+05, 3.99971391e+05, 3.99952047e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10101344e+05, 4.84337906e+05, 4.59583828e+05, 4.21287969e+05, 3.99986250e+05, 3.79481172e+05, 3.54086766e+05, 3.36128062e+05, 3.18888812e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10101344e+05, 3.18888812e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99949012e+06, 3.99876625e+06, 3.99950462e+06, 3.99949012e+06, 3.98361688e+06, 3.98286400e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00048531e+05, 4.00023281e+05, 5.72516281e+05, 3.99918766e+05, 3.99374141e+05, 2.46389695e+05, ],
    'CountWeightedFull'                                                              : [ 3.99912750e+05, 3.99893953e+05, 3.99874672e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.10002500e+05, 4.84244234e+05, 4.59494828e+05, 4.21206422e+05, 3.99908625e+05, 3.79407719e+05, 3.54017969e+05, 3.36062812e+05, 3.18826953e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.10002500e+05, 3.18826953e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99873162e+06, 3.99799362e+06, 3.99873162e+06, 3.99873162e+06, 3.98284662e+06, 3.98210850e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99974703e+05, 3.99946125e+05, 5.72404812e+05, 3.99840078e+05, 3.99297094e+05, 2.46343773e+05, ],
  }),
  ("nof_tree_events",                 399999),
  ("nof_db_events",                   399999),
  ("fsize_local",                     2723894020), # 2.72GB, avg file size 1.36GB
  ("fsize_db",                        22964320188), # 22.96GB, avg file size 1.53GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_node_1_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99820344e+05, 3.99854094e+05, 3.99855297e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.19536562e+05, 4.78713156e+05, 4.42843109e+05, 4.34165844e+05, 3.99816109e+05, 3.69701922e+05, 3.68554266e+05, 3.39257703e+05, 3.13568312e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.19537281e+05, 3.13567703e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99819138e+06, 3.99819138e+06, 3.99819138e+06, 3.99819138e+06, 3.99819138e+06, 3.99819138e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99944344e+05, 3.99974062e+05, 5.76102969e+05, 3.99877391e+05, 3.98973734e+05, 2.42956961e+05, ],
    'CountWeightedFull'                                                              : [ 3.99736344e+05, 3.99769141e+05, 3.99770719e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.19427219e+05, 4.78613062e+05, 4.42750984e+05, 4.34074250e+05, 3.99731969e+05, 3.69624859e+05, 3.68476375e+05, 3.39186500e+05, 3.13502656e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.19427938e+05, 3.13502016e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99736150e+06, 3.99736150e+06, 3.99736150e+06, 3.99736150e+06, 3.99736150e+06, 3.99736150e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99863688e+05, 3.99891000e+05, 5.75981875e+05, 3.99791000e+05, 3.98889734e+05, 2.42906555e+05, ],
  }),
  ("nof_tree_events",                 399999),
  ("nof_db_events",                   399999),
  ("fsize_local",                     2977974430), # 2.98GB, avg file size 1.49GB
  ("fsize_db",                        25245646410), # 25.25GB, avg file size 1.49GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_node_2_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeightedLHEWeightScale'                                                    : [ 5.11919750e+05, 4.83126875e+05, 4.56085250e+05, 4.23803578e+05, 3.99913156e+05, 3.77454797e+05, 3.56913828e+05, 3.36728344e+05, 3.17792211e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.11919750e+05, 3.17792211e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99902112e+06, 3.99903112e+06, 3.99903112e+06, 3.99902112e+06, 3.99903112e+06, 3.99902112e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99974781e+05, 3.99663094e+05, 5.73533906e+05, 3.99867500e+05, 4.00032641e+05, 2.45748539e+05, ],
    'CountWeightedFull'                                                              : [ 3.99834016e+05, 3.99794469e+05, 3.99817375e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.11818438e+05, 4.83031188e+05, 4.55995219e+05, 4.23719531e+05, 3.99834016e+05, 3.77380109e+05, 3.56842953e+05, 3.36661547e+05, 3.17729438e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.11818438e+05, 3.17729438e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99823500e+06, 3.99823500e+06, 3.99823500e+06, 3.99823500e+06, 3.99823500e+06, 3.99823500e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99899328e+05, 3.99583016e+05, 5.73419125e+05, 3.99786328e+05, 3.99954688e+05, 2.45701266e+05, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     2793796821), # 2.79GB, avg file size 1.40GB
  ("fsize_db",                        22826714259), # 22.83GB, avg file size 1.43GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_node_3_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99948859e+05, 3.99964969e+05, 3.99962312e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10009344e+05, 4.84373031e+05, 4.59721500e+05, 4.21181297e+05, 3.99948859e+05, 3.79552344e+05, 3.53979891e+05, 3.36098938e+05, 3.18922609e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10009344e+05, 3.18922562e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99932688e+06, 3.99933175e+06, 3.99933175e+06, 3.99932688e+06, 3.99932450e+06, 3.99931962e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99935094e+05, 3.99686391e+05, 5.72423000e+05, 4.00063562e+05, 3.99650891e+05, 2.46529781e+05, ],
    'CountWeightedFull'                                                              : [ 3.99873172e+05, 3.99887922e+05, 3.99886828e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.09912688e+05, 4.84281375e+05, 4.59634422e+05, 4.21101391e+05, 3.99873172e+05, 3.79480531e+05, 3.53912828e+05, 3.36035328e+05, 3.18862312e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.09912719e+05, 3.18862266e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99857938e+06, 3.99857938e+06, 3.99857938e+06, 3.99857938e+06, 3.99857238e+06, 3.99857238e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99862297e+05, 3.99610875e+05, 5.72312594e+05, 3.99985562e+05, 3.99574250e+05, 2.46484203e+05, ],
  }),
  ("nof_tree_events",                 399999),
  ("nof_db_events",                   399999),
  ("fsize_local",                     2720761669), # 2.72GB, avg file size 1.36GB
  ("fsize_db",                        23101309698), # 23.10GB, avg file size 1.36GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_node_4_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99952777e+05, 3.99933848e+05, 3.99913332e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.12952660e+05, 4.82638117e+05, 4.54482996e+05, 4.25157188e+05, 3.99952777e+05, 3.76537363e+05, 3.58408832e+05, 3.37086000e+05, 3.17309680e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.12952660e+05, 3.17309664e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99932206e+06, 3.99932206e+06, 3.99932206e+06, 3.99932206e+06, 3.99932206e+06, 3.99932206e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99988109e+05, 3.99894445e+05, 5.73643207e+05, 4.00019648e+05, 3.99538402e+05, 2.45482895e+05, ],
    'CountWeightedFull'                                                              : [ 3.99870938e+05, 3.99853242e+05, 3.99831996e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.12847992e+05, 4.82539715e+05, 4.54390445e+05, 4.25070176e+05, 3.99870938e+05, 3.76460559e+05, 3.58335527e+05, 3.37017121e+05, 3.17244914e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.12847992e+05, 3.17244914e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99850056e+06, 3.99850056e+06, 3.99850056e+06, 3.99850056e+06, 3.99850056e+06, 3.99850056e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99911297e+05, 3.99814238e+05, 5.73525906e+05, 3.99936887e+05, 3.99455660e+05, 2.45434646e+05, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     2818157863), # 2.82GB, avg file size 939.39MB
  ("fsize_db",                        23707187679), # 23.71GB, avg file size 1.58GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_node_5_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99929703e+05, 3.99970375e+05, 3.99952688e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10262656e+05, 4.84217406e+05, 4.59248047e+05, 4.21508578e+05, 3.99929281e+05, 3.79285547e+05, 3.54332172e+05, 3.36174984e+05, 3.18780891e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10262656e+05, 3.18780859e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99927262e+06, 3.99927262e+06, 3.99927262e+06, 3.99927262e+06, 3.99927262e+06, 3.99927262e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99966422e+05, 4.00355188e+05, 5.72744234e+05, 3.99979312e+05, 3.99087609e+05, 2.46188750e+05, ],
    'CountWeightedFull'                                                              : [ 3.99853750e+05, 3.99893469e+05, 3.99876438e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.10164953e+05, 4.84124688e+05, 4.59160156e+05, 4.21427734e+05, 3.99853250e+05, 3.79212812e+05, 3.54264078e+05, 3.36110703e+05, 3.18719859e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.10164953e+05, 3.18719828e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99851300e+06, 3.99851300e+06, 3.99851300e+06, 3.99851300e+06, 3.99851300e+06, 3.99851300e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99892047e+05, 4.00278688e+05, 5.72633250e+05, 3.99899719e+05, 3.99010391e+05, 2.46142109e+05, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     2729258806), # 2.73GB, avg file size 1.36GB
  ("fsize_db",                        23050645194), # 23.05GB, avg file size 1.36GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_node_6_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99939797e+05, 3.99942203e+05, 3.99942562e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10081469e+05, 4.84309547e+05, 4.59545812e+05, 4.21277094e+05, 3.99938297e+05, 3.79456078e+05, 3.54079750e+05, 3.36117070e+05, 3.18872234e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10081469e+05, 3.18872234e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99936025e+06, 3.99937138e+06, 3.99937188e+06, 3.99936025e+06, 3.99927800e+06, 3.99926575e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99958359e+05, 4.00144703e+05, 5.73081578e+05, 3.99999250e+05, 3.99592031e+05, 2.46252844e+05, ],
    'CountWeightedFull'                                                              : [ 3.99863094e+05, 3.99865219e+05, 3.99864469e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.09982500e+05, 4.84215828e+05, 4.59456797e+05, 4.21195391e+05, 3.99861625e+05, 3.79382781e+05, 3.54011125e+05, 3.36051812e+05, 3.18810609e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.09982500e+05, 3.18810609e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99859325e+06, 3.99859262e+06, 3.99859325e+06, 3.99859325e+06, 3.99849912e+06, 3.99849862e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99884250e+05, 4.00066547e+05, 5.72969359e+05, 3.99920094e+05, 3.99515797e+05, 2.46206672e+05, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     2723703573), # 2.72GB, avg file size 1.36GB
  ("fsize_db",                        23799450196), # 23.80GB, avg file size 1.98GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_node_7_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99992078e+05, 3.99942844e+05, 3.99960031e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.09960594e+05, 4.84407281e+05, 4.59815328e+05, 4.21099984e+05, 3.99992078e+05, 3.79607625e+05, 3.53879047e+05, 3.36071859e+05, 3.18950141e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.09960594e+05, 3.18950141e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.45389888e+06, 1.45402375e+06, 2.02910888e+06, 1.45483306e+06, 1.40005644e+06, 8.96174625e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99861750e+05, 4.00082688e+05, 5.72156688e+05, 4.00118312e+05, 3.98964297e+05, 2.46472656e+05, ],
    'CountWeightedFull'                                                              : [ 3.99913594e+05, 3.99866047e+05, 3.99881891e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.09861578e+05, 4.84313250e+05, 4.59726156e+05, 4.21018062e+05, 3.99913594e+05, 3.79534000e+05, 3.53810062e+05, 3.36006562e+05, 3.18888094e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.09861578e+05, 3.18888094e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.45363312e+06, 1.45374219e+06, 2.02870988e+06, 1.45455044e+06, 1.39978375e+06, 8.96008250e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99788531e+05, 4.00005156e+05, 5.72043188e+05, 4.00040594e+05, 3.98885656e+05, 2.46426828e+05, ],
  }),
  ("nof_tree_events",                 399999),
  ("nof_db_events",                   399999),
  ("fsize_local",                     2718202881), # 2.72GB, avg file size 1.36GB
  ("fsize_db",                        22468004114), # 22.47GB, avg file size 1.32GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_node_8_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99963688e+05, 3.99953656e+05, 3.99956266e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.19457391e+05, 4.78843656e+05, 4.42982188e+05, 4.33988219e+05, 3.99961406e+05, 3.69902562e+05, 3.68280719e+05, 3.39311797e+05, 3.13760211e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.19457609e+05, 3.13760117e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99944725e+06, 3.99944725e+06, 3.99944725e+06, 3.99944725e+06, 3.99944725e+06, 3.99944725e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00045438e+05, 4.00483094e+05, 5.76177922e+05, 3.99920016e+05, 3.98677781e+05, 2.43115211e+05, ],
    'CountWeightedFull'                                                              : [ 3.99879078e+05, 3.99869703e+05, 3.99873438e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.19348641e+05, 4.78743734e+05, 4.42890000e+05, 4.33897422e+05, 3.99876781e+05, 3.69825484e+05, 3.68203484e+05, 3.39240781e+05, 3.13694781e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.19348906e+05, 3.13694688e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99860738e+06, 3.99860738e+06, 3.99860738e+06, 3.99860738e+06, 3.99860738e+06, 3.99860738e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99964891e+05, 4.00400109e+05, 5.76056234e+05, 3.99833531e+05, 3.98593406e+05, 2.43065242e+05, ],
  }),
  ("nof_tree_events",                 399999),
  ("nof_db_events",                   399999),
  ("fsize_local",                     3011489427), # 3.01GB, avg file size 1.51GB
  ("fsize_db",                        25032953842), # 25.03GB, avg file size 1.19GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_node_9_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeightedLHEWeightScale'                                                    : [ 5.10117203e+05, 4.84342078e+05, 4.59575406e+05, 4.21305672e+05, 3.99990406e+05, 3.79477734e+05, 3.54102984e+05, 3.36135031e+05, 3.18887016e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10117234e+05, 3.18886859e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99921188e+06, 3.85714500e+06, 3.99998738e+06, 3.99943262e+06, 3.53810988e+06, 3.39481900e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00015062e+05, 4.00120734e+05, 5.71965938e+05, 3.99940906e+05, 3.98820688e+05, 2.46600172e+05, ],
    'CountWeightedFull'                                                              : [ 3.99913000e+05, 3.99850250e+05, 3.99900625e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.10019250e+05, 4.84249438e+05, 4.59487375e+05, 4.21224766e+05, 3.99913000e+05, 3.79404984e+05, 3.54034938e+05, 3.36070625e+05, 3.18825906e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.10019281e+05, 3.18825750e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99844150e+06, 3.85639988e+06, 3.99921112e+06, 3.99866225e+06, 3.53742625e+06, 3.39417188e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99941266e+05, 4.00044750e+05, 5.71855500e+05, 3.99861938e+05, 3.98743203e+05, 2.46553547e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     2721734218), # 2.72GB, avg file size 1.36GB
  ("fsize_db",                        23040806113), # 23.04GB, avg file size 1.44GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_node_10_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99993844e+05, 3.99981625e+05, 3.99924672e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10454031e+05, 4.84121969e+05, 4.58931312e+05, 4.21765125e+05, 3.99993172e+05, 3.79114156e+05, 3.54615969e+05, 3.36249422e+05, 3.18698758e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10454031e+05, 3.18698758e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99983225e+06, 3.99983225e+06, 3.99983225e+06, 3.99983225e+06, 3.99983225e+06, 3.99983225e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99935938e+05, 3.99876547e+05, 5.73175859e+05, 4.00033906e+05, 3.99991375e+05, 2.46172023e+05, ],
    'CountWeightedFull'                                                              : [ 3.99915156e+05, 3.99902875e+05, 3.99846750e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.10353422e+05, 4.84026906e+05, 4.58841266e+05, 4.21682047e+05, 3.99914453e+05, 3.79039469e+05, 3.54546219e+05, 3.36183375e+05, 3.18636094e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.10353422e+05, 3.18636078e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99904425e+06, 3.99904425e+06, 3.99904425e+06, 3.99904425e+06, 3.99904425e+06, 3.99904425e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99860953e+05, 3.99798500e+05, 5.73061750e+05, 3.99954172e+05, 3.99911547e+05, 2.46125117e+05, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     2736750250), # 2.74GB, avg file size 1.37GB
  ("fsize_db",                        23065514169), # 23.07GB, avg file size 1.36GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_node_11_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99929203e+05, 3.99951250e+05, 3.99898406e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.09915328e+05, 4.84387703e+05, 4.59812469e+05, 4.21063031e+05, 3.99926266e+05, 3.79604484e+05, 3.53846625e+05, 3.36057703e+05, 3.18947219e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.09915328e+05, 3.18947219e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.88564938e+05, 8.88528438e+05, 1.26209622e+06, 8.88320312e+05, 8.77811906e+05, 5.47703234e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00010766e+05, 4.00005766e+05, 5.72053406e+05, 3.99913250e+05, 3.99048172e+05, 2.46563898e+05, ],
    'CountWeightedFull'                                                              : [ 3.99852609e+05, 3.99873844e+05, 3.99822656e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.09818000e+05, 4.84295125e+05, 4.59724703e+05, 4.20982609e+05, 3.99849516e+05, 3.79531891e+05, 3.53778953e+05, 3.35993469e+05, 3.18886406e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.09818000e+05, 3.18886406e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 8.88402625e+05, 8.88360344e+05, 1.26185194e+06, 8.88146812e+05, 8.77641000e+05, 5.47601062e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99937797e+05, 3.99930094e+05, 5.71942859e+05, 3.99834969e+05, 3.98970750e+05, 2.46517938e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     2716021866), # 2.72GB, avg file size 1.36GB
  ("fsize_db",                        23515520244), # 23.52GB, avg file size 1.24GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_node_12_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.60843359e+05, 3.60876156e+05, 3.60866047e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.17606453e+05, 4.10244344e+05, 4.05057609e+05, 3.69126594e+05, 3.60843344e+05, 3.54234719e+05, 3.27247352e+05, 3.18772500e+05, 3.11544438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.32323031e+05, 3.04341438e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.60781625e+05, 3.60493703e+05, 5.14249312e+05, 3.60993625e+05, 3.61367453e+05, 2.23390008e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.45263018e+04, 2.45121182e+04, 3.49904609e+04, 2.45451934e+04, 2.45878965e+04, 1.51834761e+04, ],
    'CountWeightedFull'                                                              : [ 2.30796172e+04, 2.30775479e+04, 2.30823682e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.67079395e+04, 2.62369150e+04, 2.59050205e+04, 2.36076660e+04, 2.30796162e+04, 2.26549082e+04, 2.09288584e+04, 2.03868208e+04, 1.99244858e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.76494355e+04, 1.94638579e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.30736934e+04, 2.30555918e+04, 3.28897168e+04, 2.30873916e+04, 2.31116182e+04, 1.42865103e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.57169067e+03, 1.57074414e+03, 2.24215656e+03, 1.57291125e+03, 1.57556812e+03, 9.73013489e+02, ],
  }),
  ("nof_tree_events",                 383098),
  ("nof_db_events",                   383098),
  ("fsize_local",                     2480025155), # 2.48GB, avg file size 1.24GB
  ("fsize_db",                        19461973427), # 19.46GB, avg file size 846.17MB
  ("use_it",                          True),
  ("xsection",                        0.001928162),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_cHHH0_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.59007578e+05, 3.58995094e+05, 3.59002078e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.08762203e+05, 4.02175938e+05, 3.97835328e+05, 3.67300969e+05, 3.58994062e+05, 3.52450828e+05, 3.29672078e+05, 3.20639406e+05, 3.13074828e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.26300000e+05, 3.03533078e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.59077297e+05, 3.59327641e+05, 5.11664500e+05, 3.58863484e+05, 3.58286000e+05, 2.21655117e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.19700093e+04, 1.19818428e+04, 1.70655024e+04, 1.19693672e+04, 1.19502588e+04, 7.39029956e+03, ],
    'CountWeightedFull'                                                              : [ 1.07200847e+04, 1.07208730e+04, 1.07216057e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.22063940e+04, 1.20095186e+04, 1.18797397e+04, 1.09683691e+04, 1.07193716e+04, 1.05246763e+04, 9.84438916e+03, 9.57454492e+03, 9.34856738e+03, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.27303745e+04, 9.06362573e+03, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.07226987e+04, 1.07301772e+04, 1.52790425e+04, 1.07162549e+04, 1.06988223e+04, 6.61899194e+03, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.58760605e+02, 3.59265213e+02, 5.11119965e+02, 3.58909317e+02, 3.57751999e+02, 2.21555321e+02, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     2666210000), # 2.67GB, avg file size 1.33GB
  ("fsize_db",                        20612880655), # 20.61GB, avg file size 763.44MB
  ("use_it",                          True),
  ("xsection",                        0.000858569),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_cHHH1_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.44776375e+05, 3.44740234e+05, 3.44766062e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.93014000e+05, 3.87587281e+05, 3.84136594e+05, 3.51759656e+05, 3.44763594e+05, 3.39261078e+05, 3.14958484e+05, 3.07209156e+05, 3.00691633e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.14055406e+05, 2.87784484e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.44639477e+05, 3.44724672e+05, 4.92587875e+05, 3.44879562e+05, 3.44774148e+05, 2.12147258e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 5.25140308e+03, 5.25396851e+03, 7.52052051e+03, 5.25546240e+03, 5.26529419e+03, 3.23092188e+03, ],
    'CountWeightedFull'                                                              : [ 4.52072754e+03, 4.52053955e+03, 4.52104492e+03, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.15386902e+03, 5.08260779e+03, 5.03727368e+03, 4.61287402e+03, 4.52063403e+03, 4.44883374e+03, 4.13021558e+03, 4.02854065e+03, 3.94301953e+03, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.42982422e+03, 3.77377393e+03, ],
    'CountWeightedFullPSWeight'                                                      : [ 4.51941479e+03, 4.52061243e+03, 6.45936670e+03, 4.52257178e+03, 4.52096509e+03, 2.78200977e+03, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 6.90009232e+01, 6.90418053e+01, 9.88222160e+01, 6.90554047e+01, 6.91785831e+01, 4.24477749e+01, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     2668997982), # 2.67GB, avg file size 1.33GB
  ("fsize_db",                        20453536548), # 20.45GB, avg file size 1.20GB
  ("use_it",                          True),
  ("xsection",                        0.000362916),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_cHHH2p45_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.93408047e+05, 3.93384812e+05, 3.93375062e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.71152500e+05, 4.62243656e+05, 4.55380406e+05, 4.01255688e+05, 3.93404859e+05, 3.86725688e+05, 3.45566219e+05, 3.38608828e+05, 3.32311984e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.85468109e+05, 3.25618703e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.93493125e+05, 3.92925219e+05, 5.59456125e+05, 3.93285359e+05, 3.93464734e+05, 2.43994227e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.21094727e+04, 3.20603535e+04, 4.56850742e+04, 3.20904795e+04, 3.21461924e+04, 1.99148740e+04, ],
    'CountWeightedFull'                                                              : [ 3.15488691e+04, 3.15502881e+04, 3.15535742e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.77864902e+04, 3.70714629e+04, 3.65205947e+04, 3.21810547e+04, 3.15485635e+04, 3.10149053e+04, 2.77137070e+04, 2.71554502e+04, 2.66501943e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.89351543e+04, 2.61134609e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.15579307e+04, 3.15125547e+04, 4.48678379e+04, 3.15410889e+04, 3.15552607e+04, 1.95680615e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.57806335e+03, 2.57424628e+03, 3.66735559e+03, 2.57680237e+03, 2.58087634e+03, 1.59970984e+03, ],
  }),
  ("nof_tree_events",                 399999),
  ("nof_db_events",                   399999),
  ("fsize_local",                     2429946816), # 2.43GB, avg file size 1.21GB
  ("fsize_db",                        19750514425), # 19.75GB, avg file size 987.53MB
  ("use_it",                          True),
  ("xsection",                        0.002521218),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_cHHH5_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99938609e+05, 3.99975656e+05, 3.99986125e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.11945734e+05, 4.83244797e+05, 4.56304625e+05, 4.23799641e+05, 3.99938188e+05, 3.77581250e+05, 3.56902484e+05, 3.36751156e+05, 3.17867297e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.11945734e+05, 3.17867297e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99980525e+06, 3.99980525e+06, 3.99980525e+06, 3.99980525e+06, 3.99980525e+06, 3.99980525e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00073953e+05, 4.00046500e+05, 5.82914281e+05, 3.99887625e+05, 3.99163766e+05, 2.37470586e+05, ],
    'CountWeightedFull'                                                              : [ 3.99860406e+05, 3.99895922e+05, 3.99906438e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.11844172e+05, 4.83149359e+05, 4.56214672e+05, 4.23715719e+05, 3.99859891e+05, 3.77506812e+05, 3.56831641e+05, 3.36684641e+05, 3.17804516e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.11844172e+05, 3.17804516e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99900550e+06, 3.99900550e+06, 3.99900550e+06, 3.99900550e+06, 3.99900550e+06, 3.99900550e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99997031e+05, 3.99968047e+05, 5.82797656e+05, 3.99805750e+05, 3.99083953e+05, 2.37424242e+05, ],
  }),
  ("nof_tree_events",                 399993),
  ("nof_db_events",                   399993),
  ("fsize_local",                     2924076505), # 2.92GB, avg file size 1.46GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_node_sm_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.96833828e+05, 3.96845781e+05, 3.96802531e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.15618703e+05, 4.75129688e+05, 4.39548453e+05, 4.30880422e+05, 3.96832984e+05, 3.66942797e+05, 3.65757766e+05, 3.36704031e+05, 3.11222125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.15619422e+05, 3.11221500e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.96828388e+06, 3.96828388e+06, 3.96828388e+06, 3.96828388e+06, 3.96828388e+06, 3.96828388e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.96956281e+05, 3.97265844e+05, 5.81352438e+05, 3.96870359e+05, 3.95559391e+05, 2.32825734e+05, ],
    'CountWeightedFull'                                                              : [ 3.96744859e+05, 3.96757438e+05, 3.96713891e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.15502828e+05, 4.75023281e+05, 4.39450453e+05, 4.30783312e+05, 3.96744000e+05, 3.66860828e+05, 3.65675328e+05, 3.36628555e+05, 3.11152562e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.15503547e+05, 3.11151938e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.96739500e+06, 3.96739500e+06, 3.96739500e+06, 3.96739500e+06, 3.96739500e+06, 3.96739500e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.96871375e+05, 3.97178250e+05, 5.81220125e+05, 3.96779828e+05, 3.95468312e+05, 2.32774891e+05, ],
  }),
  ("nof_tree_events",                 396995),
  ("nof_db_events",                   396995),
  ("fsize_local",                     3111253329), # 3.11GB, avg file size 1.56GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_node_2_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.93881797e+05, 3.93892062e+05, 3.93886781e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.04238656e+05, 4.75878953e+05, 4.49243297e+05, 4.17444828e+05, 3.93879703e+05, 3.71792812e+05, 3.51558430e+05, 3.31677336e+05, 3.13026180e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.04238797e+05, 3.13026133e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.93917575e+06, 3.93918525e+06, 3.93918525e+06, 3.93917575e+06, 3.93918525e+06, 3.93917575e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.93872625e+05, 3.93992125e+05, 5.74182188e+05, 3.93932500e+05, 3.93031547e+05, 2.33658016e+05, ],
    'CountWeightedFull'                                                              : [ 3.93799781e+05, 3.93809594e+05, 3.93804188e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.04132531e+05, 4.75778766e+05, 4.49149219e+05, 4.17356953e+05, 3.93797719e+05, 3.71714859e+05, 3.51484273e+05, 3.31607656e+05, 3.12960539e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.04132672e+05, 3.12960484e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.93834962e+06, 3.93834962e+06, 3.93834962e+06, 3.93834962e+06, 3.93834962e+06, 3.93834962e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.93796219e+05, 3.93910953e+05, 5.74061984e+05, 3.93850953e+05, 3.92947812e+05, 2.33611391e+05, ],
  }),
  ("nof_tree_events",                 393994),
  ("nof_db_events",                   393994),
  ("fsize_local",                     2898363224), # 2.90GB, avg file size 1.45GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_node_3_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99930711e+05, 3.99916194e+05, 3.99922588e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.09971629e+05, 4.84350465e+05, 4.59709426e+05, 4.21149912e+05, 3.99929867e+05, 3.79540521e+05, 3.53952820e+05, 3.36081843e+05, 3.18912438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.09971629e+05, 3.18912422e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99897500e+06, 3.99899338e+06, 3.99899338e+06, 3.99897488e+06, 3.99896925e+06, 3.99895075e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00016421e+05, 3.99807897e+05, 5.82078428e+05, 3.99913356e+05, 3.99251747e+05, 2.38065576e+05, ],
    'CountWeightedFull'                                                              : [ 3.99851614e+05, 3.99836734e+05, 3.99842651e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.09869672e+05, 4.84253830e+05, 4.59617871e+05, 4.21065932e+05, 3.99850713e+05, 3.79464966e+05, 3.53881852e+05, 3.36014776e+05, 3.18848829e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.09869672e+05, 3.18848829e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99820372e+06, 3.99820372e+06, 3.99820372e+06, 3.99820372e+06, 3.99817959e+06, 3.99817947e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99940796e+05, 3.99729365e+05, 5.81961727e+05, 3.99832873e+05, 3.99170483e+05, 2.38019543e+05, ],
  }),
  ("nof_tree_events",                 399996),
  ("nof_db_events",                   399996),
  ("fsize_local",                     2856233586), # 2.86GB, avg file size 952.08MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_node_4_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99926234e+05, 3.99914094e+05, 3.99891625e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.12936203e+05, 4.82628859e+05, 4.54481094e+05, 4.25144609e+05, 3.99922156e+05, 3.76535984e+05, 3.58398094e+05, 3.37080875e+05, 3.17308641e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.12936203e+05, 3.17308641e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99952275e+06, 3.99952275e+06, 3.99952275e+06, 3.99952275e+06, 3.99952275e+06, 3.99952275e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99822906e+05, 4.00360531e+05, 5.82996531e+05, 4.00130969e+05, 3.98517469e+05, 2.37035844e+05, ],
    'CountWeightedFull'                                                              : [ 3.99845609e+05, 3.99833781e+05, 3.99810938e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.12831828e+05, 4.82530781e+05, 4.54389031e+05, 4.25058188e+05, 3.99841453e+05, 3.76459547e+05, 3.58325109e+05, 3.37012250e+05, 3.17244375e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.12831828e+05, 3.17244359e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99870900e+06, 3.99870900e+06, 3.99870900e+06, 3.99870900e+06, 3.99870900e+06, 3.99870900e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99744531e+05, 4.00278781e+05, 5.82877438e+05, 4.00047219e+05, 3.98437141e+05, 2.36988656e+05, ],
  }),
  ("nof_tree_events",                 399995),
  ("nof_db_events",                   399995),
  ("fsize_local",                     2968313771), # 2.97GB, avg file size 1.48GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_node_5_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99918080e+05, 3.99890461e+05, 3.99891012e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10153614e+05, 4.84166809e+05, 4.59233831e+05, 4.21408312e+05, 3.99909044e+05, 3.79264322e+05, 3.54239210e+05, 3.36122521e+05, 3.18756083e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10153614e+05, 3.18756759e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99908700e+06, 3.99908838e+06, 3.99908838e+06, 3.99908538e+06, 3.99908838e+06, 3.99908538e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99979949e+05, 4.00002771e+05, 5.82634584e+05, 3.99885635e+05, 3.99282938e+05, 2.37735328e+05, ],
    'CountWeightedFull'                                                              : [ 3.99837272e+05, 3.99810021e+05, 3.99810336e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.10050810e+05, 4.84069119e+05, 4.59141292e+05, 4.21323505e+05, 3.99828375e+05, 3.79187965e+05, 3.54167703e+05, 3.36054601e+05, 3.18691898e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.10050810e+05, 3.18692590e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99827280e+06, 3.99827280e+06, 3.99827280e+06, 3.99827280e+06, 3.99827280e+06, 3.99827280e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99903287e+05, 3.99921934e+05, 5.82517873e+05, 3.99803767e+05, 3.99204087e+05, 2.37688593e+05, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     2871076979), # 2.87GB, avg file size 957.03MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_node_6_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99964062e+05, 3.99977188e+05, 3.99931547e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10086938e+05, 4.84288250e+05, 4.59506672e+05, 4.21290844e+05, 3.99963750e+05, 3.79433969e+05, 3.54097891e+05, 3.36117047e+05, 3.18858719e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10086938e+05, 3.18858688e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99932400e+06, 3.99932400e+06, 3.99932400e+06, 3.99932400e+06, 3.99921738e+06, 3.99921738e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99920062e+05, 3.99759312e+05, 5.82090938e+05, 4.00020516e+05, 3.99390828e+05, 2.38131789e+05, ],
    'CountWeightedFull'                                                              : [ 3.99884234e+05, 3.99897938e+05, 3.99851906e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.09985766e+05, 4.84192266e+05, 4.59415844e+05, 4.21207188e+05, 3.99883844e+05, 3.79358828e+05, 3.54027562e+05, 3.36050312e+05, 3.18795516e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.09985766e+05, 3.18795484e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99853100e+06, 3.99853100e+06, 3.99853100e+06, 3.99853100e+06, 3.99842438e+06, 3.99842438e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99843938e+05, 3.99680141e+05, 5.81972750e+05, 3.99938828e+05, 3.99310234e+05, 2.38085516e+05, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     2861933468), # 2.86GB, avg file size 1.43GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_node_7_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.95951525e+05, 3.95939635e+05, 3.95936742e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.04813404e+05, 4.79557029e+05, 4.55241186e+05, 4.16845357e+05, 3.95951525e+05, 3.75826254e+05, 3.50300224e+05, 3.32700195e+05, 3.15771005e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.04815857e+05, 3.15768849e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.15146810e+06, 1.15146389e+06, 1.64674796e+06, 1.15152989e+06, 1.11994932e+06, 6.85161574e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.95949022e+05, 3.95992288e+05, 5.76283836e+05, 3.95969828e+05, 3.95091949e+05, 2.35603048e+05, ],
    'CountWeightedFull'                                                              : [ 3.95873529e+05, 3.95862129e+05, 3.95859357e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.04714492e+05, 4.79462984e+05, 4.55152010e+05, 4.16763568e+05, 3.95873529e+05, 3.75752745e+05, 3.50231306e+05, 3.32634867e+05, 3.15709198e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.04716898e+05, 3.15707042e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.15125173e+06, 1.15123848e+06, 1.64642545e+06, 1.15129770e+06, 1.11973131e+06, 6.85029736e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.95874699e+05, 3.95914936e+05, 5.76170678e+05, 3.95890123e+05, 3.95014805e+05, 2.35557672e+05, ],
  }),
  ("nof_tree_events",                 395996),
  ("nof_db_events",                   395996),
  ("fsize_local",                     2826897943), # 2.83GB, avg file size 942.30MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_node_8_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99844453e+05, 3.99830938e+05, 3.99829172e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.19289859e+05, 4.78754547e+05, 4.42950719e+05, 4.33824703e+05, 3.99843141e+05, 3.69857375e+05, 3.68125344e+05, 3.39217172e+05, 3.13708469e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.19290031e+05, 3.13708281e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99888962e+06, 3.99888962e+06, 3.99888962e+06, 3.99888962e+06, 3.99888962e+06, 3.99888962e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00121438e+05, 4.00558125e+05, 5.84891375e+05, 3.99647578e+05, 3.97609734e+05, 2.34756578e+05, ],
    'CountWeightedFull'                                                              : [ 3.99757719e+05, 3.99744938e+05, 3.99742953e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.19176469e+05, 4.78650578e+05, 4.42854656e+05, 4.33730047e+05, 3.99756328e+05, 3.69776953e+05, 3.68044953e+05, 3.39143203e+05, 3.13640203e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.19176625e+05, 3.13640000e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99799750e+06, 3.99799750e+06, 3.99799750e+06, 3.99799750e+06, 3.99799750e+06, 3.99799750e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 4.00039312e+05, 4.00470625e+05, 5.84763281e+05, 3.99559938e+05, 3.97523797e+05, 2.34707570e+05, ],
  }),
  ("nof_tree_events",                 399994),
  ("nof_db_events",                   399994),
  ("fsize_local",                     3196129822), # 3.20GB, avg file size 1.60GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_node_9_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99952889e+05, 3.99940167e+05, 3.99948751e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10085731e+05, 4.84286792e+05, 4.59505047e+05, 4.21291924e+05, 3.99952889e+05, 3.79429401e+05, 3.54101363e+05, 3.36117121e+05, 3.18855970e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10086138e+05, 3.18855501e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99842930e+06, 3.83224618e+06, 3.99926070e+06, 3.99876675e+06, 3.47498038e+06, 3.30754088e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99907243e+05, 4.00035741e+05, 5.82087280e+05, 4.00077927e+05, 3.98955785e+05, 2.37930749e+05, ],
    'CountWeightedFull'                                                              : [ 3.99875076e+05, 3.99862383e+05, 3.99871453e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.09986835e+05, 4.84192558e+05, 4.59415820e+05, 4.21210053e+05, 3.99875076e+05, 3.79355773e+05, 3.54032550e+05, 3.36051901e+05, 3.18794124e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.09987272e+05, 3.18793655e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99765412e+06, 3.83150585e+06, 3.99848551e+06, 3.99799131e+06, 3.47430845e+06, 3.30690416e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99832068e+05, 3.99958319e+05, 5.81972666e+05, 3.99997231e+05, 3.98877497e+05, 2.37885052e+05, ],
  }),
  ("nof_tree_events",                 399996),
  ("nof_db_events",                   399996),
  ("fsize_local",                     2863132478), # 2.86GB, avg file size 954.38MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_node_10_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99973469e+05, 3.99967969e+05, 3.99982297e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10435219e+05, 4.84136438e+05, 4.58969469e+05, 4.21741250e+05, 3.99970234e+05, 3.79136938e+05, 3.54588359e+05, 3.36247656e+05, 3.18711359e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10435219e+05, 3.18711359e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99980288e+06, 3.99980288e+06, 3.99980288e+06, 3.99980288e+06, 3.99980288e+06, 3.99980288e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00010141e+05, 3.99898219e+05, 5.82091234e+05, 3.99904609e+05, 3.98976891e+05, 2.37833398e+05, ],
    'CountWeightedFull'                                                              : [ 3.99897516e+05, 3.99890875e+05, 3.99904578e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.10337375e+05, 4.84043719e+05, 4.58881609e+05, 4.21660391e+05, 3.99894203e+05, 3.79064281e+05, 3.54520234e+05, 3.36183188e+05, 3.18650250e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.10337375e+05, 3.18650250e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99903525e+06, 3.99903525e+06, 3.99903525e+06, 3.99903525e+06, 3.99903525e+06, 3.99903525e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99935672e+05, 3.99821344e+05, 5.81977781e+05, 3.99825047e+05, 3.98900109e+05, 2.37788523e+05, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     2877042899), # 2.88GB, avg file size 1.44GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_node_11_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99911625e+05, 3.99965797e+05, 3.99912594e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.09924375e+05, 4.84392328e+05, 4.59812969e+05, 4.21066562e+05, 3.99911625e+05, 3.79603703e+05, 3.53849438e+05, 3.36057445e+05, 3.18945852e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.09924375e+05, 3.18945812e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.48429625e+06, 1.48172375e+06, 2.09167831e+06, 1.48220006e+06, 1.41536281e+06, 8.83198344e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00199703e+05, 3.99808625e+05, 5.82094125e+05, 3.99633062e+05, 3.99442188e+05, 2.38132188e+05, ],
    'CountWeightedFull'                                                              : [ 3.99833469e+05, 3.99886406e+05, 3.99834625e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.09824266e+05, 4.84297453e+05, 4.59723094e+05, 4.20984000e+05, 3.99833469e+05, 3.79529625e+05, 3.53780047e+05, 3.35991578e+05, 3.18883375e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.09824281e+05, 3.18883359e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.48401406e+06, 1.48143475e+06, 2.09126344e+06, 1.48189862e+06, 1.41508275e+06, 8.83027188e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 4.00123734e+05, 3.99730750e+05, 5.81978750e+05, 3.99551766e+05, 3.99363172e+05, 2.38086125e+05, ],
  }),
  ("nof_tree_events",                 399993),
  ("nof_db_events",                   399993),
  ("fsize_local",                     2852875631), # 2.85GB, avg file size 1.43GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_node_12_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.76559453e+05, 3.76507281e+05, 3.76485250e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.35497719e+05, 4.27958625e+05, 4.22674422e+05, 3.85027672e+05, 3.76559438e+05, 3.69694234e+05, 3.41397766e+05, 3.32626539e+05, 3.25147055e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.51050031e+05, 3.17507734e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.76504750e+05, 3.76429938e+05, 5.45265562e+05, 3.76506250e+05, 3.76120922e+05, 2.24959797e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.56196553e+04, 2.56173730e+04, 3.71426641e+04, 2.56197891e+04, 2.56261758e+04, 1.53047515e+04, ],
    'CountWeightedFull'                                                              : [ 2.40798672e+04, 2.40822383e+04, 2.40800762e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.78529902e+04, 2.73704229e+04, 2.70322246e+04, 2.46255479e+04, 2.40798662e+04, 2.36443936e+04, 2.18343984e+04, 2.12733018e+04, 2.07946855e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.88482188e+04, 2.03062256e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.40802021e+04, 2.40759600e+04, 3.48727461e+04, 2.40803174e+04, 2.40540938e+04, 1.43876846e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.64232135e+03, 1.64202112e+03, 2.38085120e+03, 1.64229346e+03, 1.64290552e+03, 9.81234619e+02, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     2729884477), # 2.73GB, avg file size 1.36GB
  ("fsize_db",                        20383479586), # 20.38GB, avg file size 926.52MB
  ("use_it",                          True),
  ("xsection",                        0.0076246),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_cHHH0_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.50875938e+05, 3.50816953e+05, 3.50919320e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.99755828e+05, 3.93300484e+05, 3.89024875e+05, 3.59025359e+05, 3.50866352e+05, 3.44484766e+05, 3.22106766e+05, 3.13275414e+05, 3.05874047e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.16798719e+05, 2.96644164e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.50811703e+05, 3.51004094e+05, 5.09112234e+05, 3.50976281e+05, 3.50461453e+05, 2.08973102e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.17042236e+04, 1.17100161e+04, 1.70052471e+04, 1.17077070e+04, 1.17097070e+04, 6.96811499e+03, ],
    'CountWeightedFull'                                                              : [ 1.04779839e+04, 1.04760762e+04, 1.04794810e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.19372856e+04, 1.17443481e+04, 1.16165220e+04, 1.07211128e+04, 1.04771489e+04, 1.02866431e+04, 9.61831348e+03, 9.35449487e+03, 9.13343555e+03, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.24464170e+04, 8.85787305e+03, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.04757783e+04, 1.04815293e+04, 1.52027520e+04, 1.04805762e+04, 1.04650737e+04, 6.24012183e+03, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.50514946e+02, 3.50688934e+02, 5.08848236e+02, 3.50611145e+02, 3.50139191e+02, 2.08515968e+02, ],
  }),
  ("nof_tree_events",                 391398),
  ("nof_db_events",                   391398),
  ("fsize_local",                     2763744656), # 2.76GB, avg file size 1.38GB
  ("fsize_db",                        20213187246), # 20.21GB, avg file size 962.53MB
  ("use_it",                          True),
  ("xsection",                        0.00339506),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_cHHH1_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.30007742e+05, 3.29942539e+05, 3.29995438e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.76196906e+05, 3.70997867e+05, 3.67679953e+05, 3.36689594e+05, 3.29998461e+05, 3.24737062e+05, 3.01451766e+05, 2.94047648e+05, 2.87810344e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.96198703e+05, 2.75587492e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.30034727e+05, 3.30074398e+05, 4.79314562e+05, 3.29910844e+05, 3.29615172e+05, 1.96028312e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 5.04543286e+03, 5.04635400e+03, 7.32903003e+03, 5.04447559e+03, 5.04580017e+03, 3.00257861e+03, ],
    'CountWeightedFull'                                                              : [ 4.32752124e+03, 4.32708044e+03, 4.32731372e+03, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.93359827e+03, 4.86527820e+03, 4.82166223e+03, 4.41547754e+03, 4.32729309e+03, 4.25853687e+03, 3.95323425e+03, 3.85605151e+03, 3.77420520e+03, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.19594409e+03, 3.61394409e+03, ],
    'CountWeightedFullPSWeight'                                                      : [ 4.32815015e+03, 4.32847058e+03, 6.28574121e+03, 4.32647192e+03, 4.32276575e+03, 2.57079443e+03, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 6.66647530e+01, 6.66768036e+01, 9.66628189e+01, 6.66490021e+01, 6.66374512e+01, 3.97979717e+01, ],
  }),
  ("nof_tree_events",                 383096),
  ("nof_db_events",                   383096),
  ("fsize_local",                     2697747309), # 2.70GB, avg file size 1.35GB
  ("fsize_db",                        19867289750), # 19.87GB, avg file size 794.69MB
  ("use_it",                          True),
  ("xsection",                        0.00143508),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_cHHH2p45_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeightedLHEWeightScale'                                                    : [ 4.60177359e+05, 4.51495516e+05, 4.44802891e+05, 3.91781922e+05, 3.84082406e+05, 3.77623359e+05, 3.37329641e+05, 3.30554414e+05, 3.24421320e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.74108531e+05, 3.17930125e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.84176531e+05, 3.83974359e+05, 5.56259219e+05, 3.84072656e+05, 3.83915250e+05, 2.29597062e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.13190557e+04, 3.13045078e+04, 4.54057080e+04, 3.13111992e+04, 3.13572773e+04, 1.87214277e+04, ],
    'CountWeightedFull'                                                              : [ 3.08044531e+04, 3.08085898e+04, 3.08042441e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.69074365e+04, 3.62104473e+04, 3.56733076e+04, 3.14216689e+04, 3.08038516e+04, 3.02852305e+04, 2.70537900e+04, 2.65099775e+04, 2.60177559e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.80247402e+04, 2.54972432e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.08114492e+04, 3.07949941e+04, 4.46117617e+04, 3.08027100e+04, 3.07895537e+04, 1.84137739e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.51498126e+03, 2.51379108e+03, 3.64501233e+03, 2.51414014e+03, 2.51778973e+03, 1.50410461e+03, ],
  }),
  ("nof_tree_events",                 390197),
  ("nof_db_events",                   390197),
  ("fsize_local",                     2463728102), # 2.46GB, avg file size 1.23GB
  ("fsize_db",                        19251007287), # 19.25GB, avg file size 916.71MB
  ("use_it",                          True),
  ("xsection",                        0.00996974),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_cHHH5_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99928672e+05, 3.99955783e+05, 3.99959559e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99928672e+05, 3.99928672e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99966656e+06, 3.99967606e+06, 3.99967606e+06, 3.99966756e+06, 3.99967606e+06, 3.99966656e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00079863e+05, 4.00088268e+05, 5.77926879e+05, 3.99881098e+05, 3.99623875e+05, 2.42121196e+05, ],
    'CountWeightedFull'                                                              : [ 3.99858684e+05, 3.99885246e+05, 3.99888436e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99858684e+05, 3.99858684e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99896516e+06, 3.99896516e+06, 3.99896516e+06, 3.99896516e+06, 3.99896516e+06, 3.99896516e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 4.00012285e+05, 4.00017576e+05, 5.77823400e+05, 3.99809295e+05, 3.99552682e+05, 2.42079324e+05, ],
  }),
  ("nof_tree_events",                 399995),
  ("nof_db_events",                   399995),
  ("fsize_local",                     2259671189), # 2.26GB, avg file size 753.22MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_250_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99940639e+05, 3.99948718e+05, 3.99878397e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.06192095e+05, 3.99934955e+05, 3.91112567e+05, 4.06192095e+05, 3.99934955e+05, 3.91112567e+05, 4.06192095e+05, 3.99934955e+05, 3.91112567e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.06192095e+05, 3.91112536e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99355916e+06, 1.98457754e+06, 2.71783905e+06, 1.99525878e+06, 1.83700563e+06, 1.20568635e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99796078e+05, 3.99925930e+05, 5.78482928e+05, 4.00148940e+05, 3.99902482e+05, 2.41791845e+05, ],
    'CountWeightedFull'                                                              : [ 3.99868763e+05, 3.99876472e+05, 3.99808031e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.06119696e+05, 3.99863112e+05, 3.91042985e+05, 4.06119696e+05, 3.99863112e+05, 3.91042985e+05, 4.06119696e+05, 3.99863112e+05, 3.91042985e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.06119696e+05, 3.91042970e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.99321493e+06, 1.98422866e+06, 2.71735480e+06, 1.99489277e+06, 1.83667800e+06, 1.20547435e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99726958e+05, 3.99855567e+05, 5.78379144e+05, 4.00075639e+05, 3.99830189e+05, 2.41749283e+05, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     2287813964), # 2.29GB, avg file size 762.60MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_260_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99946391e+05, 3.99931203e+05, 3.99907969e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.07474953e+05, 3.99939734e+05, 3.90118312e+05, 4.07474953e+05, 3.99939734e+05, 3.90118312e+05, 4.07474953e+05, 3.99939734e+05, 3.90118312e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.07474953e+05, 3.90118312e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.48530838e+06, 1.48432019e+06, 2.08407400e+06, 1.48566538e+06, 1.42089956e+06, 8.97351562e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99932094e+05, 3.99857938e+05, 5.78254938e+05, 4.00024094e+05, 3.99501750e+05, 2.41624062e+05, ],
    'CountWeightedFull'                                                              : [ 3.99875172e+05, 3.99859891e+05, 3.99836984e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.07402359e+05, 3.99868609e+05, 3.90048750e+05, 4.07402359e+05, 3.99868609e+05, 3.90048750e+05, 4.07402359e+05, 3.99868609e+05, 3.90048750e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.07402359e+05, 3.90048750e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.48505362e+06, 1.48405925e+06, 2.08369950e+06, 1.48539638e+06, 1.42064119e+06, 8.97194125e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99863500e+05, 3.99787672e+05, 5.78151406e+05, 3.99951578e+05, 3.99429281e+05, 2.41581625e+05, ],
  }),
  ("nof_tree_events",                 399996),
  ("nof_db_events",                   399996),
  ("fsize_local",                     2329514196), # 2.33GB, avg file size 1.16GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_270_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99877188e+05, 3.99881469e+05, 3.99859734e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99877188e+05, 3.99877188e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.70048669e+06, 1.69662694e+06, 2.35921481e+06, 1.69945888e+06, 1.60184138e+06, 1.02638178e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00009359e+05, 3.99743562e+05, 5.78295203e+05, 3.99767453e+05, 3.99494469e+05, 2.41439016e+05, ],
    'CountWeightedFull'                                                              : [ 3.99805344e+05, 3.99810203e+05, 3.99787906e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99805344e+05, 3.99805344e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.70019056e+06, 1.69632112e+06, 2.35879256e+06, 1.69914662e+06, 1.60155825e+06, 1.02619991e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99939703e+05, 3.99671578e+05, 5.78192047e+05, 3.99694234e+05, 3.99424156e+05, 2.41396266e+05, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     2379079673), # 2.38GB, avg file size 1.19GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_280_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 2.99923422e+05, 2.99958008e+05, 2.99922832e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.08224180e+05, 2.99923422e+05, 2.90502363e+05, 3.08224180e+05, 2.99923422e+05, 2.90502363e+05, 3.08224180e+05, 2.99923422e+05, 2.90502363e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.08224258e+05, 2.90502285e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.07898386e+06, 1.07738872e+06, 1.51845966e+06, 1.07911406e+06, 1.03601022e+06, 6.50412219e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99956902e+05, 2.99660410e+05, 4.34084844e+05, 2.99996539e+05, 2.99817328e+05, 1.80816615e+05, ],
    'CountWeightedFull'                                                              : [ 2.99871531e+05, 2.99905480e+05, 2.99870602e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.08170117e+05, 2.99871531e+05, 2.90451352e+05, 3.08170117e+05, 2.99871531e+05, 2.90451352e+05, 3.08170117e+05, 2.99871531e+05, 2.90451352e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.08170180e+05, 2.90451289e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.07879928e+06, 1.07720250e+06, 1.51819341e+06, 1.07891925e+06, 1.03582720e+06, 6.50298336e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99905594e+05, 2.99608555e+05, 4.34008234e+05, 2.99942484e+05, 2.99764125e+05, 1.80784980e+05, ],
  }),
  ("nof_tree_events",                 299997),
  ("nof_db_events",                   299997),
  ("fsize_local",                     1836571826), # 1.84GB, avg file size 918.29MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_300_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 2.99989055e+05, 2.99982285e+05, 2.99957145e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.09815527e+05, 2.99989055e+05, 2.89279805e+05, 3.09815527e+05, 2.99989055e+05, 2.89279805e+05, 3.09815527e+05, 2.99989055e+05, 2.89279805e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.09815527e+05, 2.89279805e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.86885906e+05, 9.86812812e+05, 1.39697555e+06, 9.86256297e+05, 9.52610141e+05, 5.93198586e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.00070043e+05, 3.00117293e+05, 4.34427953e+05, 2.99878555e+05, 2.99246934e+05, 1.80367227e+05, ],
    'CountWeightedFull'                                                              : [ 2.99933172e+05, 2.99926590e+05, 2.99901758e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.09758305e+05, 2.99933172e+05, 2.89226266e+05, 3.09758305e+05, 2.99933172e+05, 2.89226266e+05, 3.09758305e+05, 2.99933172e+05, 2.89226266e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.09758305e+05, 2.89226266e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.86711641e+05, 9.86632797e+05, 1.39671667e+06, 9.86071359e+05, 9.52430531e+05, 5.93091031e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.00016859e+05, 3.00062543e+05, 4.34346938e+05, 2.99822461e+05, 2.99190344e+05, 1.80334467e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1893192488), # 1.89GB, avg file size 946.60MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_320_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 2.99976484e+05, 2.99966328e+05, 2.99999062e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.11970500e+05, 2.99976484e+05, 2.87621922e+05, 3.11970500e+05, 2.99976484e+05, 2.87621922e+05, 3.11970500e+05, 2.99976484e+05, 2.87621922e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.11970500e+05, 2.87621922e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.15455938e+05, 9.16819156e+05, 1.30289600e+06, 9.16267000e+05, 8.87269219e+05, 5.48701109e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99864969e+05, 3.00368594e+05, 4.35115938e+05, 3.00131484e+05, 2.98915391e+05, 1.79731555e+05, ],
    'CountWeightedFull'                                                              : [ 2.99921156e+05, 2.99910562e+05, 2.99943219e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.11913031e+05, 2.99921156e+05, 2.87568656e+05, 3.11913031e+05, 2.99921156e+05, 2.87568656e+05, 3.11913031e+05, 2.99921156e+05, 2.87568656e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.11913031e+05, 2.87568656e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.15292219e+05, 9.16653562e+05, 1.30265388e+06, 9.16094656e+05, 8.87100594e+05, 5.48600953e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99811469e+05, 3.00314328e+05, 4.35034891e+05, 3.00075078e+05, 2.98858531e+05, 1.79698734e+05, ],
  }),
  ("nof_tree_events",                 299997),
  ("nof_db_events",                   299997),
  ("fsize_local",                     1967391802), # 1.97GB, avg file size 983.70MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_350_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 2.99921469e+05, 2.99921219e+05, 2.99955734e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.15093633e+05, 2.99921469e+05, 2.85245562e+05, 3.15093633e+05, 2.99921469e+05, 2.85245562e+05, 3.15093633e+05, 2.99921469e+05, 2.85245562e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.15093695e+05, 2.85245484e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.64873812e+05, 8.64993938e+05, 1.23707481e+06, 8.65575250e+05, 8.43368938e+05, 5.16515047e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99881430e+05, 2.99954070e+05, 4.36823258e+05, 3.00123578e+05, 3.00279914e+05, 1.79093078e+05, ],
    'CountWeightedFull'                                                              : [ 2.99865453e+05, 2.99865273e+05, 2.99899742e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.15034352e+05, 2.99865453e+05, 2.85191922e+05, 3.15034352e+05, 2.99865453e+05, 2.85191922e+05, 3.15034352e+05, 2.99865453e+05, 2.85191922e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.15034414e+05, 2.85191859e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 8.64715781e+05, 8.64831469e+05, 1.23683897e+06, 8.65406375e+05, 8.43208594e+05, 5.16419141e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99826414e+05, 2.99897844e+05, 4.36740016e+05, 3.00064969e+05, 3.00223188e+05, 1.79059816e+05, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     2084977523), # 2.08GB, avg file size 1.04GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_400_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 2.99967172e+05, 2.99955891e+05, 2.99955344e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.17760609e+05, 2.99959328e+05, 2.83223773e+05, 3.17760609e+05, 2.99959328e+05, 2.83223773e+05, 3.17760609e+05, 2.99959328e+05, 2.83223773e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.17760859e+05, 2.83223742e+05, ],
    'CountWeightedPSWeight'                                                          : [ 6.35899031e+05, 6.36036875e+05, 9.19144719e+05, 6.35485953e+05, 6.27810750e+05, 3.78028750e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.00062656e+05, 3.00132055e+05, 4.36967328e+05, 2.99868172e+05, 2.99487859e+05, 1.78379852e+05, ],
    'CountWeightedFull'                                                              : [ 2.99909062e+05, 2.99898195e+05, 2.99897477e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.17699406e+05, 2.99901109e+05, 2.83169344e+05, 3.17699406e+05, 2.99901109e+05, 2.83169344e+05, 3.17699406e+05, 2.99901109e+05, 2.83169344e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.17699664e+05, 2.83169328e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 6.35780969e+05, 6.35915656e+05, 9.18965188e+05, 6.35358844e+05, 6.27687672e+05, 3.77956438e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.00006875e+05, 3.00074922e+05, 4.36881672e+05, 2.99808266e+05, 2.99428898e+05, 1.78345750e+05, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     2187040532), # 2.19GB, avg file size 1.09GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_450_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 2.99942750e+05, 2.99942977e+05, 2.99943172e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.20057953e+05, 2.99942750e+05, 2.81449516e+05, 3.20057953e+05, 2.99942750e+05, 2.81449516e+05, 3.20057953e+05, 2.99942750e+05, 2.81449516e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.20057953e+05, 2.81449484e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.45360375e+05, 8.44158562e+05, 1.21291653e+06, 8.44740000e+05, 8.25556438e+05, 5.01339203e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.00078562e+05, 2.99679953e+05, 4.37883062e+05, 2.99857406e+05, 3.00356484e+05, 1.77962625e+05, ],
    'CountWeightedFull'                                                              : [ 2.99883320e+05, 2.99883672e+05, 2.99883570e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.19994172e+05, 2.99883320e+05, 2.81393320e+05, 3.19994172e+05, 2.99883320e+05, 2.81393320e+05, 3.19994172e+05, 2.99883320e+05, 2.81393320e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.19994172e+05, 2.81393289e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 8.45196781e+05, 8.43991781e+05, 1.21267119e+06, 8.44565656e+05, 8.25389500e+05, 5.01240812e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.00020711e+05, 2.99620641e+05, 4.37794375e+05, 2.99795422e+05, 3.00295523e+05, 1.77927719e+05, ],
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     2273103641), # 2.27GB, avg file size 1.14GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_500_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 2.57974875e+05, 2.57959312e+05, 2.57944613e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.77001141e+05, 2.57974875e+05, 2.40700410e+05, 2.77001141e+05, 2.57974875e+05, 2.40700410e+05, 2.77001141e+05, 2.57974875e+05, 2.40700410e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.77001141e+05, 2.40700410e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.15398172e+05, 9.14911031e+05, 1.29661231e+06, 9.15055469e+05, 8.74786328e+05, 5.41474156e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.58014895e+05, 2.58016098e+05, 3.76410609e+05, 2.57912734e+05, 2.57376352e+05, 1.52620559e+05, ],
    'CountWeightedFull'                                                              : [ 2.57922180e+05, 2.57906672e+05, 2.57892504e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 2.76944711e+05, 2.57922180e+05, 2.40651367e+05, 2.76944711e+05, 2.57922180e+05, 2.40651367e+05, 2.76944711e+05, 2.57922180e+05, 2.40651367e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.76944711e+05, 2.40651367e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.15219531e+05, 9.14725625e+05, 1.29634869e+06, 9.14865297e+05, 8.74608984e+05, 5.41365508e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.57964523e+05, 2.57963695e+05, 3.76334242e+05, 2.57859090e+05, 2.57324531e+05, 1.52589820e+05, ],
  }),
  ("nof_tree_events",                 257999),
  ("nof_db_events",                   257999),
  ("fsize_local",                     2013721215), # 2.01GB, avg file size 1.01GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_550_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1596454843), # 1.60GB, avg file size 1.60GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_600_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1623897343), # 1.62GB, avg file size 1.62GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_650_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1643390544), # 1.64GB, avg file size 1.64GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_700_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 1.99957407e+05, 1.99968683e+05, 1.99953298e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99957407e+05, 1.99957407e+05, ],
    'CountWeightedPSWeight'                                                          : [ 4.64373854e+05, 4.65077951e+05, 6.72841809e+05, 4.64105219e+05, 4.54645729e+05, 2.71854926e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.00044227e+05, 2.00348112e+05, 2.92838164e+05, 1.99921912e+05, 1.98841144e+05, 1.17106026e+05, ],
    'CountWeightedFull'                                                              : [ 1.99913955e+05, 1.99925185e+05, 1.99910382e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99913955e+05, 1.99913955e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 4.64278020e+05, 4.64977695e+05, 6.72695098e+05, 4.64001340e+05, 4.54547838e+05, 2.71797759e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.00002895e+05, 2.00304882e+05, 2.92774166e+05, 1.99877229e+05, 1.98798239e+05, 1.17081326e+05, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     1663604099), # 1.66GB, avg file size 831.80MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_750_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 1.99958164e+05, 1.99960266e+05, 1.99957211e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99958164e+05, 1.99958164e+05, ],
    'CountWeightedPSWeight'                                                          : [ 4.79376359e+05, 4.78975375e+05, 6.95047562e+05, 4.79343531e+05, 4.70363109e+05, 2.80364406e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99991281e+05, 1.99837758e+05, 2.93298875e+05, 1.99982859e+05, 1.99558453e+05, 1.16972406e+05, ],
    'CountWeightedFull'                                                              : [ 1.99914484e+05, 1.99916508e+05, 1.99913609e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99914484e+05, 1.99914484e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 4.79275188e+05, 4.78871047e+05, 6.94894656e+05, 4.79234844e+05, 4.70259969e+05, 2.80303609e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99949062e+05, 1.99794211e+05, 2.93233781e+05, 1.99937453e+05, 1.99514242e+05, 1.16947129e+05, ],
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     1674539393), # 1.67GB, avg file size 837.27MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_800_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 1.99953211e+05, 1.99958127e+05, 1.99975289e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99953211e+05, 1.99953211e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.29473445e+05, 8.29421023e+05, 1.16626071e+06, 8.30219078e+05, 7.75252891e+05, 4.83740980e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99909900e+05, 2.00295980e+05, 2.93511314e+05, 2.00088131e+05, 1.98877145e+05, 1.16584961e+05, ],
    'CountWeightedFull'                                                              : [ 1.99909559e+05, 1.99914346e+05, 1.99931693e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99909559e+05, 1.99909559e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 8.29297328e+05, 8.29238898e+05, 1.16600494e+06, 8.30029773e+05, 7.75084500e+05, 4.83636184e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99867412e+05, 2.00252088e+05, 2.93446740e+05, 2.00042621e+05, 1.98834070e+05, 1.16559679e+05, ],
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     1685393514), # 1.69GB, avg file size 842.70MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_850_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1684478892), # 1.68GB, avg file size 1.68GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_900_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     849380130), # 849.38MB, avg file size 849.38MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_1000_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     857985513), # 857.99MB, avg file size 857.99MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_1250_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     847409525), # 847.41MB, avg file size 847.41MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_1500_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     848325047), # 848.33MB, avg file size 848.33MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_1750_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     843720960), # 843.72MB, avg file size 843.72MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_2000_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     845604220), # 845.60MB, avg file size 845.60MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_2500_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     846676112), # 846.68MB, avg file size 846.68MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_3000_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99924609e+05, 3.99954922e+05, 3.99904984e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.04863922e+05, 3.99921672e+05, 3.92207406e+05, 4.04863922e+05, 3.99921672e+05, 3.92207406e+05, 4.04863922e+05, 3.99921672e+05, 3.92207406e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.04863922e+05, 3.92207406e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99932200e+06, 3.99932200e+06, 3.99932200e+06, 3.99932200e+06, 3.99932200e+06, 3.99932200e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99938328e+05, 4.00280109e+05, 5.77898094e+05, 3.99995141e+05, 3.98517859e+05, 2.41380016e+05, ],
    'CountWeightedFull'                                                              : [ 3.99852125e+05, 3.99882891e+05, 3.99833453e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.04790812e+05, 3.99849234e+05, 3.92136469e+05, 4.04790812e+05, 3.99849234e+05, 3.92136469e+05, 4.04790812e+05, 3.99849234e+05, 3.92136469e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.04790812e+05, 3.92136469e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99860362e+06, 3.99860362e+06, 3.99860362e+06, 3.99860362e+06, 3.99860362e+06, 3.99860362e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99867766e+05, 4.00208062e+05, 5.77792578e+05, 3.99920391e+05, 3.98445234e+05, 2.41336641e+05, ],
  }),
  ("nof_tree_events",                 399995),
  ("nof_db_events",                   399995),
  ("fsize_local",                     2293813185), # 2.29GB, avg file size 1.15GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_250_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99947125e+05, 3.99966188e+05, 3.99918953e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.06203562e+05, 3.99946203e+05, 3.91114438e+05, 4.06203562e+05, 3.99946203e+05, 3.91114438e+05, 4.06203562e+05, 3.99946203e+05, 3.91114438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.06203562e+05, 3.91114438e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99932138e+06, 3.99932138e+06, 3.99932138e+06, 3.99932138e+06, 3.99932138e+06, 3.99932138e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99912359e+05, 3.99981188e+05, 5.78965531e+05, 4.00048750e+05, 3.99622484e+05, 2.41166586e+05, ],
    'CountWeightedFull'                                                              : [ 3.99876500e+05, 3.99894500e+05, 3.99848594e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.06131312e+05, 3.99875500e+05, 3.91044984e+05, 4.06131312e+05, 3.99875500e+05, 3.91044984e+05, 4.06131312e+05, 3.99875500e+05, 3.91044984e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.06131312e+05, 3.91044984e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99860900e+06, 3.99860900e+06, 3.99860900e+06, 3.99860900e+06, 3.99860900e+06, 3.99860900e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99843031e+05, 3.99910812e+05, 5.78861094e+05, 3.99975312e+05, 3.99549844e+05, 2.41124156e+05, ],
  }),
  ("nof_tree_events",                 399996),
  ("nof_db_events",                   399996),
  ("fsize_local",                     2341577308), # 2.34GB, avg file size 1.17GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_260_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99906859e+05, 3.99931859e+05, 3.99932062e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.07489094e+05, 3.99904719e+05, 3.90112656e+05, 4.07489094e+05, 3.99904719e+05, 3.90112656e+05, 4.07489094e+05, 3.99904719e+05, 3.90112656e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.07490797e+05, 3.90110938e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99940088e+06, 3.99940088e+06, 3.99940088e+06, 3.99940088e+06, 3.99940088e+06, 3.99940088e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99832344e+05, 4.00059344e+05, 5.78596156e+05, 4.00132469e+05, 3.98848172e+05, 2.40957406e+05, ],
    'CountWeightedFull'                                                              : [ 3.99835703e+05, 3.99860000e+05, 3.99860062e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.07415922e+05, 3.99833562e+05, 3.90042500e+05, 4.07415922e+05, 3.99833562e+05, 3.90042500e+05, 4.07415922e+05, 3.99833562e+05, 3.90042500e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.07417609e+05, 3.90040797e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99867675e+06, 3.99867675e+06, 3.99867675e+06, 3.99867675e+06, 3.99867675e+06, 3.99867675e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99762047e+05, 3.99987766e+05, 5.78491734e+05, 4.00058406e+05, 3.98776281e+05, 2.40914273e+05, ],
  }),
  ("nof_tree_events",                 399994),
  ("nof_db_events",                   399994),
  ("fsize_local",                     2391516589), # 2.39GB, avg file size 1.20GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_270_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.93995097e+05, 3.93952334e+05, 3.93976511e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.02630425e+05, 3.93989778e+05, 3.83336399e+05, 4.02630425e+05, 3.93989778e+05, 3.83336399e+05, 4.02630425e+05, 3.93989778e+05, 3.83336399e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.02630425e+05, 3.83336399e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.94003448e+06, 3.94003448e+06, 3.94003448e+06, 3.94003448e+06, 3.94003448e+06, 3.94003448e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.94054463e+05, 3.93724054e+05, 5.69904322e+05, 3.93910070e+05, 3.93094191e+05, 2.37247229e+05, ],
    'CountWeightedFull'                                                              : [ 3.93922641e+05, 3.93880384e+05, 3.93904148e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.02555778e+05, 3.93917186e+05, 3.83265408e+05, 4.02555778e+05, 3.93917186e+05, 3.83265408e+05, 4.02555778e+05, 3.93917186e+05, 3.83265408e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.02555778e+05, 3.83265408e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.93930082e+06, 3.93930082e+06, 3.93930082e+06, 3.93930082e+06, 3.93930082e+06, 3.93930082e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.93984137e+05, 3.93652328e+05, 5.69797123e+05, 3.93835425e+05, 3.93019217e+05, 2.37203957e+05, ],
  }),
  ("nof_tree_events",                 393998),
  ("nof_db_events",                   393998),
  ("fsize_local",                     2404291965), # 2.40GB, avg file size 801.43MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_280_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 2.99954211e+05, 2.99931168e+05, 2.99953316e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.08219172e+05, 2.99954211e+05, 2.90500344e+05, 3.08219172e+05, 2.99954211e+05, 2.90500344e+05, 3.08219172e+05, 2.99954211e+05, 2.90500344e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.08219172e+05, 2.90500344e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99954806e+06, 2.99956006e+06, 2.99956006e+06, 2.99954806e+06, 2.99956006e+06, 2.99954806e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99915660e+05, 3.00031203e+05, 4.34319938e+05, 3.00083391e+05, 2.99006852e+05, 1.80206350e+05, ],
    'CountWeightedFull'                                                              : [ 2.99897531e+05, 2.99874785e+05, 2.99896531e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.08161102e+05, 2.99897531e+05, 2.90445656e+05, 3.08161102e+05, 2.99897531e+05, 2.90445656e+05, 3.08161102e+05, 2.99897531e+05, 2.90445656e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.08161102e+05, 2.90445656e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99899722e+06, 2.99899722e+06, 2.99899722e+06, 2.99899722e+06, 2.99899722e+06, 2.99899722e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99861707e+05, 2.99975137e+05, 4.34238039e+05, 3.00025973e+05, 2.98950352e+05, 1.80173525e+05, ],
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     1897471781), # 1.90GB, avg file size 948.74MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_300_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 2.99968930e+05, 2.99968031e+05, 2.99954172e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.09819125e+05, 2.99967906e+05, 2.89275844e+05, 3.09819125e+05, 2.99967906e+05, 2.89275844e+05, 3.09819125e+05, 2.99967906e+05, 2.89275844e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.09819125e+05, 2.89275828e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99988175e+06, 2.99988175e+06, 2.99988175e+06, 2.99988175e+06, 2.99988175e+06, 2.99988175e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.00096844e+05, 3.00125406e+05, 4.35391688e+05, 2.99813836e+05, 2.99487859e+05, 1.79757402e+05, ],
    'CountWeightedFull'                                                              : [ 2.99912438e+05, 2.99911906e+05, 2.99898078e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.09760844e+05, 2.99911242e+05, 2.89221391e+05, 3.09760844e+05, 2.99911242e+05, 2.89221391e+05, 3.09760844e+05, 2.99911242e+05, 2.89221391e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.09760844e+05, 2.89221375e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99931350e+06, 2.99931350e+06, 2.99931350e+06, 2.99931350e+06, 2.99931350e+06, 2.99931350e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.00042102e+05, 3.00068703e+05, 4.35309594e+05, 2.99755391e+05, 2.99432188e+05, 1.79723969e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1960666562), # 1.96GB, avg file size 980.33MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_320_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 2.99946711e+05, 2.99948414e+05, 2.99975797e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.11966891e+05, 2.99946508e+05, 2.87609539e+05, 3.11966891e+05, 2.99946508e+05, 2.87609539e+05, 3.11966891e+05, 2.99946508e+05, 2.87609539e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.11966891e+05, 2.87609539e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99948225e+06, 2.99948225e+06, 2.99948225e+06, 2.99948225e+06, 2.99948225e+06, 2.99948225e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99942266e+05, 2.99891109e+05, 4.36419125e+05, 3.00016906e+05, 3.00226461e+05, 1.79309758e+05, ],
    'CountWeightedFull'                                                              : [ 2.99890141e+05, 2.99892133e+05, 2.99918039e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.11907641e+05, 2.99889883e+05, 2.87554688e+05, 3.11907641e+05, 2.99889883e+05, 2.87554688e+05, 3.11907641e+05, 2.99889883e+05, 2.87554688e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.11907641e+05, 2.87554688e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99891675e+06, 2.99891675e+06, 2.99891675e+06, 2.99891675e+06, 2.99891675e+06, 2.99891675e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99886766e+05, 2.99833672e+05, 4.36335219e+05, 2.99957672e+05, 3.00169461e+05, 1.79276043e+05, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     2050105235), # 2.05GB, avg file size 1.03GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_350_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 2.94930922e+05, 2.94957844e+05, 2.94968344e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.09852141e+05, 2.94930922e+05, 2.80504336e+05, 3.09852141e+05, 2.94930922e+05, 2.80504336e+05, 3.09852141e+05, 2.94930922e+05, 2.80504336e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.09852141e+05, 2.80504336e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.94974462e+06, 2.94974462e+06, 2.94974462e+06, 2.94974462e+06, 2.94974462e+06, 2.94974462e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.94718898e+05, 2.94997805e+05, 4.28711375e+05, 2.95285180e+05, 2.93881219e+05, 1.75786398e+05, ],
    'CountWeightedFull'                                                              : [ 2.94875250e+05, 2.94902109e+05, 2.94911289e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.09792570e+05, 2.94875250e+05, 2.80450664e+05, 3.09792570e+05, 2.94875250e+05, 2.80450664e+05, 3.09792570e+05, 2.94875250e+05, 2.80450664e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.09792570e+05, 2.80450664e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.94917469e+06, 2.94917469e+06, 2.94917469e+06, 2.94917469e+06, 2.94917469e+06, 2.94917469e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.94664047e+05, 2.94941766e+05, 4.28628188e+05, 2.95226492e+05, 2.93824070e+05, 1.75752945e+05, ],
  }),
  ("nof_tree_events",                 294999),
  ("nof_db_events",                   294999),
  ("fsize_local",                     2145216117), # 2.15GB, avg file size 1.07GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_400_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 2.99955391e+05, 2.99965910e+05, 2.99956809e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.17776887e+05, 2.99955391e+05, 2.83229562e+05, 3.17776887e+05, 2.99955391e+05, 2.83229562e+05, 3.17776887e+05, 2.99955391e+05, 2.83229562e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.17776887e+05, 2.83229516e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99950778e+06, 2.99950778e+06, 2.99950778e+06, 2.99950778e+06, 2.99950778e+06, 2.99950778e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.00010988e+05, 3.00198402e+05, 4.36770641e+05, 2.99916023e+05, 2.98853500e+05, 1.78026035e+05, ],
    'CountWeightedFull'                                                              : [ 2.99895926e+05, 2.99906547e+05, 2.99897020e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.17713738e+05, 2.99895926e+05, 2.83173484e+05, 3.17713738e+05, 2.99895926e+05, 2.83173484e+05, 3.17713738e+05, 2.99895926e+05, 2.83173484e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.17713738e+05, 2.83173453e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99891491e+06, 2.99891491e+06, 2.99891491e+06, 2.99891491e+06, 2.99891491e+06, 2.99891491e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99953383e+05, 3.00139352e+05, 4.36681992e+05, 2.99854156e+05, 2.98792637e+05, 1.77991176e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     2290518504), # 2.29GB, avg file size 1.15GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_450_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 2.99983852e+05, 2.99970062e+05, 2.99968648e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.20053609e+05, 2.99983852e+05, 2.81469336e+05, 3.20053609e+05, 2.99983852e+05, 2.81469336e+05, 3.20053609e+05, 2.99983852e+05, 2.81469336e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.20053609e+05, 2.81469336e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99944238e+06, 2.99946488e+06, 2.99946488e+06, 2.99944238e+06, 2.99946488e+06, 2.99944238e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99911516e+05, 2.99961477e+05, 4.37620844e+05, 3.00118562e+05, 2.99237156e+05, 1.77605156e+05, ],
    'CountWeightedFull'                                                              : [ 2.99920586e+05, 2.99907734e+05, 2.99905297e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.19986617e+05, 2.99920586e+05, 2.81410453e+05, 3.19986617e+05, 2.99920586e+05, 2.81410453e+05, 3.19986617e+05, 2.99920586e+05, 2.81410453e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.19986617e+05, 2.81410453e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99883762e+06, 2.99883762e+06, 2.99883762e+06, 2.99883762e+06, 2.99883762e+06, 2.99883762e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99852664e+05, 2.99897375e+05, 4.37527602e+05, 3.00055797e+05, 2.99175469e+05, 1.77569496e+05, ],
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     2377143558), # 2.38GB, avg file size 1.19GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_500_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 2.99861375e+05, 2.99896570e+05, 2.99933480e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.22049027e+05, 2.99861375e+05, 2.79843012e+05, 3.22049027e+05, 2.99861375e+05, 2.79843012e+05, 3.22049027e+05, 2.99861375e+05, 2.79843012e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.22049027e+05, 2.79843012e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99911275e+06, 2.99912450e+06, 2.99912450e+06, 2.99911275e+06, 2.99912450e+06, 2.99911275e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99859891e+05, 3.00057156e+05, 4.37683352e+05, 3.00074055e+05, 2.98604664e+05, 1.77092453e+05, ],
    'CountWeightedFull'                                                              : [ 2.99800266e+05, 2.99834238e+05, 2.99869562e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.21981852e+05, 2.99800266e+05, 2.79784891e+05, 3.21981852e+05, 2.99800266e+05, 2.79784891e+05, 3.21981852e+05, 2.99800266e+05, 2.79784891e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.21981852e+05, 2.79784891e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99849684e+06, 2.99849684e+06, 2.99849684e+06, 2.99849684e+06, 2.99849684e+06, 2.99849684e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99800531e+05, 2.99995613e+05, 4.37591234e+05, 3.00010512e+05, 2.98541234e+05, 1.77056428e+05, ],
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     2444959705), # 2.44GB, avg file size 1.22GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_550_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1664361018), # 1.66GB, avg file size 1.66GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_600_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 1.75957699e+05, 1.75975067e+05, 1.75988167e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.90992063e+05, 1.75956324e+05, 1.62637891e+05, 1.90992063e+05, 1.75956324e+05, 1.62637891e+05, 1.90992063e+05, 1.75956324e+05, 1.62637891e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.90992297e+05, 1.62637657e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.75976989e+06, 1.75976989e+06, 1.75976989e+06, 1.75976989e+06, 1.75976989e+06, 1.75976989e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.76016762e+05, 1.76080407e+05, 2.58460396e+05, 1.75948434e+05, 1.76227463e+05, 1.03283397e+05, ],
    'CountWeightedFull'                                                              : [ 1.75918797e+05, 1.75935915e+05, 1.75948496e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.90949598e+05, 1.75917422e+05, 1.62601603e+05, 1.90949598e+05, 1.75917422e+05, 1.62601603e+05, 1.90949598e+05, 1.75917422e+05, 1.62601603e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.90949848e+05, 1.62601368e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.75937784e+06, 1.75937784e+06, 1.75937784e+06, 1.75937784e+06, 1.75937784e+06, 1.75937784e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.75979808e+05, 1.76041886e+05, 2.58402842e+05, 1.75908670e+05, 1.76187949e+05, 1.03261067e+05, ],
  }),
  ("nof_tree_events",                 175996),
  ("nof_db_events",                   175996),
  ("fsize_local",                     1485385307), # 1.49GB, avg file size 742.69MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_650_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1695947690), # 1.70GB, avg file size 1.70GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_700_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1702809043), # 1.70GB, avg file size 1.70GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_750_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1706265263), # 1.71GB, avg file size 1.71GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_800_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 1.89970567e+05, 1.89959939e+05, 1.89946793e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.89970567e+05, 1.89970567e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.89957838e+06, 1.89957838e+06, 1.89957838e+06, 1.89957838e+06, 1.89957838e+06, 1.89957838e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.89947304e+05, 1.89985757e+05, 2.79469097e+05, 1.90039181e+05, 1.89808687e+05, 1.10711645e+05, ],
    'CountWeightedFull'                                                              : [ 1.89928833e+05, 1.89918543e+05, 1.89905485e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.89928833e+05, 1.89928833e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.89916654e+06, 1.89916654e+06, 1.89916654e+06, 1.89916654e+06, 1.89916654e+06, 1.89916654e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.89907352e+05, 1.89944837e+05, 2.79408011e+05, 1.89996222e+05, 1.89767265e+05, 1.10687655e+05, ],
  }),
  ("nof_tree_events",                 189999),
  ("nof_db_events",                   189999),
  ("fsize_local",                     1631336798), # 1.63GB, avg file size 815.67MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_850_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1718843354), # 1.72GB, avg file size 1.72GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_900_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     859979293), # 859.98MB, avg file size 859.98MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_1000_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     858065538), # 858.07MB, avg file size 858.07MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_1250_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     842781075), # 842.78MB, avg file size 842.78MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_1500_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     835707297), # 835.71MB, avg file size 835.71MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_1750_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     830453044), # 830.45MB, avg file size 830.45MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_2000_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     831576452), # 831.58MB, avg file size 831.58MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_2500_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     833760653), # 833.76MB, avg file size 833.76MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_3000_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99929438e+05, 3.99939266e+05, 3.99938344e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99929438e+05, 3.99929438e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99933725e+06, 3.99937388e+06, 3.99937388e+06, 3.99933812e+06, 3.99937388e+06, 3.99933675e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99943969e+05, 3.99716312e+05, 5.66997969e+05, 3.99858922e+05, 3.99822781e+05, 2.47597672e+05, ],
    'CountWeightedFull'                                                              : [ 3.99699219e+05, 3.99710688e+05, 3.99709391e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99699219e+05, 3.99699219e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99707862e+06, 3.99707862e+06, 3.99707862e+06, 3.99707862e+06, 3.99707862e+06, 3.99707862e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99766094e+05, 3.99485375e+05, 5.66674688e+05, 3.99680781e+05, 3.99593266e+05, 2.47487438e+05, ],
  }),
  ("nof_tree_events",                 399995),
  ("nof_db_events",                   399995),
  ("fsize_local",                     2728659278), # 2.73GB, avg file size 1.36GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_nonresonant_1_1_0_hh_2b2v_sl_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99972484e+05, 3.99987125e+05, 3.99995641e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99972484e+05, 3.99972484e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99965612e+06, 3.99967912e+06, 3.99967912e+06, 3.99965412e+06, 3.99967912e+06, 3.99965212e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00027188e+05, 3.99965625e+05, 5.67300375e+05, 3.99790094e+05, 3.99447922e+05, 2.47149828e+05, ],
    'CountWeightedFull'                                                              : [ 3.99726078e+05, 3.99742172e+05, 3.99748422e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99726078e+05, 3.99726078e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99723275e+06, 3.99723275e+06, 3.99723275e+06, 3.99723275e+06, 3.99723275e+06, 3.99723275e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99844781e+05, 3.99719172e+05, 5.66960766e+05, 3.99606562e+05, 3.99209156e+05, 2.47036414e+05, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     2729333362), # 2.73GB, avg file size 1.36GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_nonresonant_1_1_1_hh_2b2v_sl_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2604784560), # 2.60GB, avg file size 1.30GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_nonresonant_1_1_1_hh_2b2v_sl_dipoleRecoilOn"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99991643e+05, 3.99977556e+05, 3.99984623e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99991643e+05, 3.99991643e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99965153e+06, 3.99966353e+06, 3.99966353e+06, 3.99965091e+06, 3.99966353e+06, 3.99965091e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99909294e+05, 4.00405573e+05, 5.70138562e+05, 3.99920398e+05, 3.98351940e+05, 2.44286953e+05, ],
    'CountWeightedFull'                                                              : [ 3.99735825e+05, 3.99723605e+05, 3.99727292e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99735825e+05, 3.99735825e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99710625e+06, 3.99710625e+06, 3.99710625e+06, 3.99710625e+06, 3.99710625e+06, 3.99710625e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99714586e+05, 4.00153676e+05, 5.69771662e+05, 3.99725224e+05, 3.98088661e+05, 2.44168646e+05, ],
  }),
  ("nof_tree_events",                 399990),
  ("nof_db_events",                   399990),
  ("fsize_local",                     2918169498), # 2.92GB, avg file size 729.54MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_nonresonant_1_1_2_hh_2b2v_sl_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99971250e+05, 3.99967484e+05, 3.99934438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99971250e+05, 3.99971250e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99968338e+06, 3.99976100e+06, 3.99976100e+06, 3.99968188e+06, 3.99976100e+06, 3.99968188e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99753422e+05, 4.00666031e+05, 5.68579750e+05, 3.99981438e+05, 3.98152844e+05, 2.45375312e+05, ],
    'CountWeightedFull'                                                              : [ 3.99654062e+05, 3.99651203e+05, 3.99621625e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99654062e+05, 3.99654062e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99660550e+06, 3.99660550e+06, 3.99660550e+06, 3.99660550e+06, 3.99660550e+06, 3.99660550e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99551422e+05, 4.00346031e+05, 5.68146281e+05, 3.99779969e+05, 3.97851844e+05, 2.45251430e+05, ],
  }),
  ("nof_tree_events",                 399996),
  ("nof_db_events",                   399996),
  ("fsize_local",                     3294456814), # 3.29GB, avg file size 1.65GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_nonresonant_1_2_1_hh_2b2v_sl_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     3165037196), # 3.17GB, avg file size 633.01MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_nonresonant_1_2_1_hh_2b2v_sl_dipoleRecoilOn"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeightedPSWeight'                                                          : [ 3.99974812e+06, 3.99977700e+06, 3.99977700e+06, 3.99974925e+06, 3.99977700e+06, 3.99974738e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99855312e+05, 3.99750109e+05, 5.68531891e+05, 3.99916688e+05, 3.99692469e+05, 2.46074625e+05, ],
    'CountWeightedFull'                                                              : [ 3.99691266e+05, 3.99700469e+05, 3.99641922e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99691266e+05, 3.99691266e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99682525e+06, 3.99682525e+06, 3.99682525e+06, 3.99682525e+06, 3.99682525e+06, 3.99682525e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99655719e+05, 3.99458125e+05, 5.68112297e+05, 3.99716891e+05, 3.99391969e+05, 2.45951219e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     3211010797), # 3.21GB, avg file size 1.61GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_nonresonant_0p5_1_1_hh_2b2v_sl_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 3.99946094e+05, 3.99944977e+05, 3.99951180e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99946094e+05, 3.99946094e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99924262e+06, 3.99929338e+06, 3.99929338e+06, 3.99924325e+06, 3.99929338e+06, 3.99924262e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99850562e+05, 4.00146242e+05, 5.67797078e+05, 3.99853188e+05, 3.99309578e+05, 2.46663805e+05, ],
    'CountWeightedFull'                                                              : [ 3.99690664e+05, 3.99689727e+05, 3.99695234e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99690664e+05, 3.99690664e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99675650e+06, 3.99675650e+06, 3.99675650e+06, 3.99675650e+06, 3.99675650e+06, 3.99675650e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99665203e+05, 3.99893969e+05, 5.67432359e+05, 3.99666742e+05, 3.99048117e+05, 2.46549180e+05, ],
  }),
  ("nof_tree_events",                 399999),
  ("nof_db_events",                   399999),
  ("fsize_local",                     3002189168), # 3.00GB, avg file size 1.00GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_nonresonant_1p5_1_1_hh_2b2v_sl_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 4.00012375e+05, 4.00000547e+05, 3.99960266e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.00012375e+05, 4.00012375e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99992675e+06, 3.99997875e+06, 3.99997875e+06, 3.99992600e+06, 3.99997875e+06, 3.99992575e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99845250e+05, 3.99975500e+05, 5.67785344e+05, 4.00005094e+05, 3.99265688e+05, 2.46483391e+05, ],
    'CountWeightedFull'                                                              : [ 3.99751469e+05, 3.99736922e+05, 3.99705469e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99751469e+05, 3.99751469e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99733512e+06, 3.99733512e+06, 3.99733512e+06, 3.99733512e+06, 3.99733512e+06, 3.99733512e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99655500e+05, 3.99716312e+05, 5.67423438e+05, 3.99814953e+05, 3.99007953e+05, 2.46366344e+05, ],
  }),
  ("nof_tree_events",                 399995),
  ("nof_db_events",                   399995),
  ("fsize_local",                     3086382719), # 3.09GB, avg file size 1.54GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_nonresonant_1_0_1_hh_2b2v_sl_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     3365624474), # 3.37GB, avg file size 3.37GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin0_250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     3416384101), # 3.42GB, avg file size 3.42GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin0_260_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     3326159464), # 3.33GB, avg file size 3.33GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin0_270_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     3315637698), # 3.32GB, avg file size 3.32GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin0_280_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2696913465), # 2.70GB, avg file size 2.70GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin0_300_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2440253655), # 2.44GB, avg file size 2.44GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin0_320_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2828455321), # 2.83GB, avg file size 2.83GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin0_350_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2778484535), # 2.78GB, avg file size 2.78GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin0_400_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     3030538900), # 3.03GB, avg file size 3.03GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin0_450_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     3111176867), # 3.11GB, avg file size 3.11GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin0_500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     3090867829), # 3.09GB, avg file size 3.09GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin0_550_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2155899091), # 2.16GB, avg file size 2.16GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin0_600_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2099522603), # 2.10GB, avg file size 2.10GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin0_650_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2211415136), # 2.21GB, avg file size 2.21GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin0_700_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2144880956), # 2.14GB, avg file size 2.14GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin0_750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2256090788), # 2.26GB, avg file size 2.26GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin0_800_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2277599540), # 2.28GB, avg file size 2.28GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin0_850_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2289318667), # 2.29GB, avg file size 2.29GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin0_900_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1157056790), # 1.16GB, avg file size 1.16GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin0_1000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1177707833), # 1.18GB, avg file size 1.18GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin0_1250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1187863667), # 1.19GB, avg file size 1.19GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin0_1500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1081992129), # 1.08GB, avg file size 1.08GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin0_1750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1000514587), # 1.00GB, avg file size 1.00GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin0_2000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1191868668), # 1.19GB, avg file size 1.19GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin0_3000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     3434965308), # 3.43GB, avg file size 3.43GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin2_250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     3091492938), # 3.09GB, avg file size 3.09GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin2_260_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2968957492), # 2.97GB, avg file size 2.97GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin2_270_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2755538061), # 2.76GB, avg file size 2.76GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin2_280_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2327855848), # 2.33GB, avg file size 2.33GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin2_300_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2332758273), # 2.33GB, avg file size 2.33GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin2_320_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2262996633), # 2.26GB, avg file size 2.26GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin2_350_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2230492252), # 2.23GB, avg file size 2.23GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin2_400_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2334855812), # 2.33GB, avg file size 2.33GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin2_450_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2391370542), # 2.39GB, avg file size 2.39GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin2_500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1551013913), # 1.55GB, avg file size 1.55GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin2_600_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1625614555), # 1.63GB, avg file size 1.63GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin2_650_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1630834097), # 1.63GB, avg file size 1.63GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin2_700_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1637499744), # 1.64GB, avg file size 1.64GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin2_750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1649240428), # 1.65GB, avg file size 1.65GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin2_850_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1654629579), # 1.65GB, avg file size 1.65GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin2_900_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     831564389), # 831.56MB, avg file size 831.56MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin2_1000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     836716224), # 836.72MB, avg file size 836.72MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin2_1200_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     819141840), # 819.14MB, avg file size 819.14MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin2_1750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     814587754), # 814.59MB, avg file size 814.59MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_spin2_2000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2190112234), # 2.19GB, avg file size 2.19GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2136773567), # 2.14GB, avg file size 2.14GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_260_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2265144455), # 2.27GB, avg file size 2.27GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_270_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2277811082), # 2.28GB, avg file size 2.28GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_280_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1673939562), # 1.67GB, avg file size 1.67GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_300_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1830146278), # 1.83GB, avg file size 1.83GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_320_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 2.99971891e+05, 2.99975156e+05, 2.99971445e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.99971891e+05, 2.99971891e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.80919469e+05, 9.80863812e+05, 1.37268494e+06, 9.80391938e+05, 9.54506281e+05, 6.09351156e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.00052109e+05, 3.00092992e+05, 4.27654359e+05, 2.99891781e+05, 2.99680422e+05, 1.86394074e+05, ],
    'CountWeightedFull'                                                              : [ 2.99952266e+05, 2.99955266e+05, 2.99951797e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.99952266e+05, 2.99952266e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.80860438e+05, 9.80799031e+05, 1.37259284e+06, 9.80321906e+05, 9.54443938e+05, 6.09312812e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.00034078e+05, 3.00073164e+05, 4.27625453e+05, 2.99870250e+05, 2.99660672e+05, 1.86382320e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1824270209), # 1.82GB, avg file size 912.14MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_340_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1896063636), # 1.90GB, avg file size 1.90GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_350_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2000924363), # 2.00GB, avg file size 2.00GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_400_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2097882282), # 2.10GB, avg file size 2.10GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_450_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2018679322), # 2.02GB, avg file size 2.02GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2237363077), # 2.24GB, avg file size 2.24GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_550_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1527622634), # 1.53GB, avg file size 1.53GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_600_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1554995721), # 1.55GB, avg file size 1.55GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_650_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1499822814), # 1.50GB, avg file size 1.50GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_700_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1605546754), # 1.61GB, avg file size 1.61GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1620372510), # 1.62GB, avg file size 1.62GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_800_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1634517664), # 1.63GB, avg file size 1.63GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_850_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1641884990), # 1.64GB, avg file size 1.64GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_900_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     833019945), # 833.02MB, avg file size 833.02MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_1000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     852977455), # 852.98MB, avg file size 852.98MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_1250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     845452080), # 845.45MB, avg file size 845.45MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_1500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     846074352), # 846.07MB, avg file size 846.07MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_1750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     842328751), # 842.33MB, avg file size 842.33MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_2000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     634972575), # 634.97MB, avg file size 634.97MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_2500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     847614184), # 847.61MB, avg file size 847.61MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin0_3000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2119854366), # 2.12GB, avg file size 2.12GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2173687512), # 2.17GB, avg file size 2.17GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_260_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2323663891), # 2.32GB, avg file size 2.32GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_270_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2249026887), # 2.25GB, avg file size 2.25GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_280_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1690832196), # 1.69GB, avg file size 1.69GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_300_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1889517959), # 1.89GB, avg file size 1.89GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_320_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 2.99979973e+05, 2.99970750e+05, 2.99956402e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.99979973e+05, 2.99979973e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.00011381e+06, 3.00011381e+06, 3.00011381e+06, 3.00011381e+06, 3.00011381e+06, 3.00011381e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99932195e+05, 3.00139453e+05, 4.28566852e+05, 3.00035270e+05, 2.99884090e+05, 1.85846664e+05, ],
    'CountWeightedFull'                                                              : [ 2.99959559e+05, 2.99950637e+05, 2.99936172e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.99959559e+05, 2.99959559e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99990988e+06, 2.99990988e+06, 2.99990988e+06, 2.99990988e+06, 2.99990988e+06, 2.99990988e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99913469e+05, 3.00119504e+05, 4.28537305e+05, 3.00013133e+05, 2.99863512e+05, 1.85834438e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1895005772), # 1.90GB, avg file size 947.50MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_340_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1970643023), # 1.97GB, avg file size 1.97GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_350_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2091683808), # 2.09GB, avg file size 2.09GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_400_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2186613870), # 2.19GB, avg file size 2.19GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_450_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2267512346), # 2.27GB, avg file size 2.27GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2330808147), # 2.33GB, avg file size 2.33GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_550_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1590529634), # 1.59GB, avg file size 1.59GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_600_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1616827894), # 1.62GB, avg file size 1.62GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_650_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1633595879), # 1.63GB, avg file size 1.63GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_700_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1648331688), # 1.65GB, avg file size 1.65GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1660150415), # 1.66GB, avg file size 1.66GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_800_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1592570604), # 1.59GB, avg file size 1.59GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_850_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     1685656694), # 1.69GB, avg file size 1.69GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_900_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     849536380), # 849.54MB, avg file size 849.54MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_1000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     862524184), # 862.52MB, avg file size 862.52MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_1250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     846499295), # 846.50MB, avg file size 846.50MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_1500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     838553285), # 838.55MB, avg file size 838.55MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_1750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     832735301), # 832.74MB, avg file size 832.74MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_2000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     834310820), # 834.31MB, avg file size 834.31MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_2500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     837737578), # 837.74MB, avg file size 837.74MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_spin2_3000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 9.99965594e+05, 1.00010884e+06, 1.00004773e+06, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99965594e+05, 9.99965594e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.99854925e+06, 9.99863625e+06, 9.99863625e+06, 9.99854825e+06, 9.99863625e+06, 9.99854475e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99832797e+05, 1.00005181e+06, 1.38987069e+06, 9.99847719e+05, 9.97978688e+05, 6.42593094e+05, ],
    'CountWeightedFull'                                                              : [ 9.99498750e+05, 9.99638422e+05, 9.99578297e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99498750e+05, 9.99498750e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99397625e+06, 9.99397625e+06, 9.99397625e+06, 9.99397625e+06, 9.99397625e+06, 9.99397625e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99502969e+05, 9.99578875e+05, 1.38922584e+06, 9.99516781e+05, 9.97519062e+05, 6.42381047e+05, ],
  }),
  ("nof_tree_events",                 1000000),
  ("nof_db_events",                   1000000),
  ("fsize_local",                     6616196867), # 6.62GB, avg file size 1.65GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_nonresonant_1_1_0_hh_2b2t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 1.99996558e+06, 1.99993694e+06, 2.00016364e+06, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99996558e+06, 1.99996558e+06, ],
    'CountWeightedPSWeight'                                                          : [ 1.99985665e+07, 1.99986258e+07, 1.99986258e+07, 1.99985540e+07, 1.99986258e+07, 1.99985510e+07, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99969483e+06, 2.00049094e+06, 2.78500059e+06, 1.99964302e+06, 1.99750756e+06, 1.28197655e+06, ],
    'CountWeightedFull'                                                              : [ 1.99901748e+06, 1.99898784e+06, 1.99919786e+06, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99901748e+06, 1.99901748e+06, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.99891595e+07, 1.99891595e+07, 1.99891595e+07, 1.99891595e+07, 1.99891595e+07, 1.99891595e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99902023e+06, 1.99953812e+06, 2.78369928e+06, 1.99896731e+06, 1.99656931e+06, 1.28154531e+06, ],
  }),
  ("nof_tree_events",                 2000000),
  ("nof_db_events",                   2000000),
  ("fsize_local",                     13247881102), # 13.25GB, avg file size 1.66GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_nonresonant_1_1_1_hh_2b2t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     6304805580), # 6.30GB, avg file size 1.58GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_nonresonant_1_1_1_hh_2b2t_dipoleRecoilOn"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 9.96940641e+05, 9.97036672e+05, 9.96896438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.96940641e+05, 9.96940641e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.96861100e+06, 9.96865875e+06, 9.96865875e+06, 9.96861100e+06, 9.96865875e+06, 9.96860675e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.96982750e+05, 9.96832719e+05, 1.39714312e+06, 9.96636391e+05, 9.96150859e+05, 6.31640328e+05, ],
    'CountWeightedFull'                                                              : [ 9.96422125e+05, 9.96513109e+05, 9.96377141e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.96422125e+05, 9.96422125e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.96347925e+06, 9.96347925e+06, 9.96347925e+06, 9.96347925e+06, 9.96347925e+06, 9.96347925e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.96613688e+05, 9.96309656e+05, 1.39642584e+06, 9.96266656e+05, 9.95636875e+05, 6.31408188e+05, ],
  }),
  ("nof_tree_events",                 997000),
  ("nof_db_events",                   997000),
  ("fsize_local",                     7064819030), # 7.06GB, avg file size 1.77GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_nonresonant_1_1_2_hh_2b2t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 1.99602620e+06, 1.99606347e+06, 1.99576689e+06, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99602620e+06, 1.99602620e+06, ],
    'CountWeightedPSWeight'                                                          : [ 1.99559495e+07, 1.99562902e+07, 1.99562902e+07, 1.99559440e+07, 1.99562902e+07, 1.99559380e+07, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99548872e+06, 1.99602506e+06, 2.78683572e+06, 1.99504528e+06, 1.99329309e+06, 1.27170961e+06, ],
    'CountWeightedFull'                                                              : [ 1.99468427e+06, 1.99472538e+06, 1.99443808e+06, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99468427e+06, 1.99468427e+06, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.99430972e+07, 1.99430972e+07, 1.99430972e+07, 1.99430972e+07, 1.99430972e+07, 1.99430972e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99471186e+06, 1.99469305e+06, 2.78500047e+06, 1.99427027e+06, 1.99196520e+06, 1.27121428e+06, ],
  }),
  ("nof_tree_events",                 1996000),
  ("nof_db_events",                   1996000),
  ("fsize_local",                     16035910239), # 16.04GB, avg file size 2.00GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_nonresonant_1_2_1_hh_2b2t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     7707048289), # 7.71GB, avg file size 1.93GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_nonresonant_1_2_1_hh_2b2t_dipoleRecoilOn"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 1.00012925e+06, 9.99960062e+05, 9.99989094e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.00012925e+06, 1.00012925e+06, ],
    'CountWeightedPSWeight'                                                          : [ 9.99911125e+06, 9.99930125e+06, 9.99930125e+06, 9.99910125e+06, 9.99930125e+06, 9.99909600e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99956000e+05, 9.99923969e+05, 1.39228831e+06, 9.99606891e+05, 9.98511406e+05, 6.40692531e+05, ],
    'CountWeightedFull'                                                              : [ 9.99583047e+05, 9.99426172e+05, 9.99449703e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99583047e+05, 9.99583047e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99400400e+06, 9.99400400e+06, 9.99400400e+06, 9.99400400e+06, 9.99400400e+06, 9.99400400e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99600844e+05, 9.99384422e+05, 1.39154834e+06, 9.99251531e+05, 9.97976266e+05, 6.40464422e+05, ],
  }),
  ("nof_tree_events",                 1000000),
  ("nof_db_events",                   1000000),
  ("fsize_local",                     7285727949), # 7.29GB, avg file size 1.82GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_nonresonant_1p5_1_1_hh_2b2t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 9.91961172e+05, 9.91837781e+05, 9.91953469e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.91961172e+05, 9.91961172e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.92015475e+06, 9.92035750e+06, 9.92035750e+06, 9.92015550e+06, 9.92035750e+06, 9.92014700e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.91653109e+05, 9.91827859e+05, 1.38463259e+06, 9.91739344e+05, 9.91364859e+05, 6.32830406e+05, ],
    'CountWeightedFull'                                                              : [ 9.91352688e+05, 9.91232312e+05, 9.91347859e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.91352688e+05, 9.91352688e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.91420400e+06, 9.91420400e+06, 9.91420400e+06, 9.91420400e+06, 9.91420400e+06, 9.91420400e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.91279938e+05, 9.91217875e+05, 1.38380003e+06, 9.91366984e+05, 9.90760625e+05, 6.32591891e+05, ],
  }),
  ("nof_tree_events",                 992000),
  ("nof_db_events",                   992000),
  ("fsize_local",                     7751965095), # 7.75GB, avg file size 1.94GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_nonresonant_0p5_1_1_hh_2b2t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 1.99704527e+06, 1.99697158e+06, 1.99678088e+06, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99704527e+06, 1.99704527e+06, ],
    'CountWeightedPSWeight'                                                          : [ 1.99713102e+07, 1.99716875e+07, 1.99716875e+07, 1.99712992e+07, 1.99716875e+07, 1.99712970e+07, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99651927e+06, 1.99607614e+06, 2.78212119e+06, 1.99663205e+06, 1.99569725e+06, 1.27852464e+06, ],
    'CountWeightedFull'                                                              : [ 1.99593872e+06, 1.99586245e+06, 1.99568945e+06, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99593872e+06, 1.99593872e+06, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.99605888e+07, 1.99605888e+07, 1.99605888e+07, 1.99605888e+07, 1.99605888e+07, 1.99605888e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99579817e+06, 1.99496998e+06, 2.78058038e+06, 1.99591012e+06, 1.99458083e+06, 1.27806198e+06, ],
  }),
  ("nof_tree_events",                 1997000),
  ("nof_db_events",                   1997000),
  ("fsize_local",                     15034473665), # 15.03GB, avg file size 1.88GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_nonresonant_1_0_1_hh_2b2t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 4.99976328e+05, 4.99998055e+05, 4.99956602e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.99976328e+05, 4.99976328e+05, ],
    'CountWeightedPSWeight'                                                          : [ 4.99983612e+06, 4.99992750e+06, 4.99992750e+06, 4.99983612e+06, 4.99992750e+06, 4.99983562e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.99876254e+05, 5.00031754e+05, 6.96516902e+05, 4.99752770e+05, 4.99222176e+05, 3.19830316e+05, ],
    'CountWeightedFull'                                                              : [ 4.99673070e+05, 4.99692512e+05, 4.99655523e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.99673070e+05, 4.99673070e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 4.99688853e+06, 4.99688853e+06, 4.99688853e+06, 4.99688853e+06, 4.99688853e+06, 4.99688853e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 4.99695277e+05, 4.99734273e+05, 6.96101527e+05, 4.99571723e+05, 4.98914688e+05, 3.19714799e+05, ],
  }),
  ("nof_tree_events",                 500000),
  ("nof_db_events",                   500000),
  ("fsize_local",                     3765650701), # 3.77GB, avg file size 1.26GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_vbf_nonresonant_1_0_1_hh_2b2t_dipoleRecoilOff_ext1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2820937955), # 2.82GB, avg file size 2.82GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_node_sm_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     3053848466), # 3.05GB, avg file size 3.05GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_node_2_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2726026763), # 2.73GB, avg file size 2.73GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_node_3_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2752110065), # 2.75GB, avg file size 2.75GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_node_4_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2857354033), # 2.86GB, avg file size 2.86GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_node_5_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2679743242), # 2.68GB, avg file size 2.68GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_node_6_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2379585582), # 2.38GB, avg file size 2.38GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_node_7_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2748927715), # 2.75GB, avg file size 2.75GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_node_8_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     3053936359), # 3.05GB, avg file size 3.05GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_node_9_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2756702992), # 2.76GB, avg file size 2.76GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_node_10_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2770747517), # 2.77GB, avg file size 2.77GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_node_11_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
  ("fsize_local",                     2748686345), # 2.75GB, avg file size 2.75GB
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
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_node_12_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 9.41259578e+05, 9.41417344e+05, 9.41299016e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.08903019e+06, 1.07015212e+06, 1.05688438e+06, 9.62618016e+05, 9.41259594e+05, 9.24190938e+05, 8.53422859e+05, 8.31498312e+05, 8.12792500e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.12762806e+06, 7.93893422e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.41197328e+05, 9.41436984e+05, 1.34070925e+06, 9.41498141e+05, 9.40353375e+05, 5.82216141e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 6.40846152e+04, 6.40922725e+04, 9.13560273e+04, 6.41015518e+04, 6.41191504e+04, 3.96566484e+04, ],
    'CountWeightedFull'                                                              : [ 6.02110996e+04, 6.02096367e+04, 6.02056162e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 6.96560000e+04, 6.84479121e+04, 6.75988984e+04, 6.15715645e+04, 6.02110986e+04, 5.91128379e+04, 5.45860869e+04, 5.31834795e+04, 5.19866514e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 7.21256875e+04, 5.07779863e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 6.02012607e+04, 6.02161006e+04, 8.57540742e+04, 6.02197822e+04, 6.01469639e+04, 3.72399580e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 4.11330090e+03, 4.11383740e+03, 5.86088513e+03, 4.11429590e+03, 4.11531848e+03, 2.54780432e+03, ],
  }),
  ("nof_tree_events",                 1000000),
  ("nof_db_events",                   1000000),
  ("fsize_local",                     6555911406), # 6.56GB, avg file size 1.64GB
  ("fsize_db",                        49487397386), # 49.49GB, avg file size 1.46GB
  ("use_it",                          True),
  ("xsection",                        0.00509388),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_cHHH0_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 8.95615625e+05, 8.95793766e+05, 8.95671953e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.01973948e+06, 1.00348222e+06, 9.92767453e+05, 9.16317297e+05, 8.95601500e+05, 8.79561797e+05, 8.22488984e+05, 8.00054062e+05, 7.81249125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.06362178e+06, 7.57363219e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.95624906e+05, 8.95827188e+05, 1.27674584e+06, 8.95807750e+05, 8.94804797e+05, 5.53199234e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.98851157e+04, 2.98964692e+04, 4.26494629e+04, 2.98921367e+04, 2.99010498e+04, 1.84592866e+04, ],
    'CountWeightedFull'                                                              : [ 2.67487271e+04, 2.67512671e+04, 2.67503906e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.04534487e+04, 2.99676597e+04, 2.96473818e+04, 2.73653462e+04, 2.67476973e+04, 2.62671802e+04, 2.45623262e+04, 2.38921753e+04, 2.33304741e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.17646416e+04, 2.26171851e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.67472246e+04, 2.67529585e+04, 3.81290166e+04, 2.67526338e+04, 2.67227534e+04, 1.65208823e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 8.93843262e+02, 8.94211563e+02, 1.27524298e+03, 8.94101074e+02, 8.94262543e+02, 5.52432098e+02, ],
  }),
  ("nof_tree_events",                 1000000),
  ("nof_db_events",                   1000000),
  ("fsize_local",                     6768914849), # 6.77GB, avg file size 1.69GB
  ("fsize_db",                        50081318436), # 50.08GB, avg file size 1.47GB
  ("use_it",                          True),
  ("xsection",                        0.00226819),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_cHHH1_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 8.62012328e+05, 8.62175859e+05, 8.61930203e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 9.82854203e+05, 9.69320953e+05, 9.60703703e+05, 8.79599109e+05, 8.61982344e+05, 8.48299453e+05, 7.87431812e+05, 7.68094547e+05, 7.51820312e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.03513475e+06, 7.19873203e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.61948812e+05, 8.61962547e+05, 1.22979019e+06, 8.62135688e+05, 8.60424406e+05, 5.30998797e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.31378369e+04, 1.31370747e+04, 1.87676748e+04, 1.31401401e+04, 1.31402632e+04, 8.09418689e+03, ],
    'CountWeightedFull'                                                              : [ 1.13060481e+04, 1.13071687e+04, 1.13045852e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.28902371e+04, 1.27125051e+04, 1.25993318e+04, 1.15359641e+04, 1.13059009e+04, 1.11252009e+04, 1.03270894e+04, 1.00733491e+04, 9.85981348e+03, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.35758811e+04, 9.44086621e+03, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.13043401e+04, 1.13046606e+04, 1.61284346e+04, 1.13067976e+04, 1.12839709e+04, 6.96386536e+03, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.72814079e+02, 1.72804035e+02, 2.46790760e+02, 1.72842400e+02, 1.72850521e+02, 1.06542303e+02, ],
  }),
  ("nof_tree_events",                 1000000),
  ("nof_db_events",                   1000000),
  ("fsize_local",                     6782525108), # 6.78GB, avg file size 1.70GB
  ("fsize_db",                        50271035315), # 50.27GB, avg file size 1.29GB
  ("use_it",                          True),
  ("xsection",                        0.00095876),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_cHHH2p45_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
    'CountWeighted'                                                                  : [ 9.84270156e+05, 9.84323484e+05, 9.84278312e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.17890166e+06, 1.15664284e+06, 1.13949394e+06, 1.00393428e+06, 9.84261469e+05, 9.67642484e+05, 8.64563031e+05, 8.47196828e+05, 8.31475328e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.21485444e+06, 8.14591891e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.84296484e+05, 9.84223547e+05, 1.39976394e+06, 9.84341969e+05, 9.82914859e+05, 6.10126625e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 8.02211426e+04, 8.02181719e+04, 1.14185186e+05, 8.02269805e+04, 8.02049355e+04, 4.97234082e+04, ],
    'CountWeightedFull'                                                              : [ 7.89411582e+04, 7.89504434e+04, 7.89433242e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 9.45564863e+04, 9.27702129e+04, 9.13936660e+04, 8.05226855e+04, 7.89399688e+04, 7.76104707e+04, 6.93431738e+04, 6.79496992e+04, 6.66881484e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.74408145e+04, 6.53341406e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 7.89471094e+04, 7.89408867e+04, 1.12270895e+05, 7.89502793e+04, 7.88369863e+04, 4.89357109e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 6.43697485e+03, 6.43652954e+03, 9.16197852e+03, 6.43735901e+03, 6.43596313e+03, 3.99015051e+03, ],
  }),
  ("nof_tree_events",                 1000000),
  ("nof_db_events",                   1000000),
  ("fsize_local",                     6115085302), # 6.12GB, avg file size 1.53GB
  ("fsize_db",                        48318284793), # 48.32GB, avg file size 1.38GB
  ("use_it",                          True),
  ("xsection",                        0.00666064),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Feb20_woPresel_nom_all_hh_multilepton/ntuples/signal_ggf_nonresonant_cHHH5_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD/USER"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_450_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_450_hh_2b2v_private"),
  ("nof_files",                       6),
  ("nof_db_files",                    743),
  ("nof_events",                      {
    'Count'                                                                          : [ 297199, ],
    'CountWeighted'                                                                  : [ 2.97180598e+05, 2.97160938e+05, 2.97150020e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.14802074e+05, 2.97180598e+05, 2.80560918e+05, 3.14802074e+05, 2.97180598e+05, 2.80560918e+05, 3.14802074e+05, 2.97180598e+05, 2.80560918e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.14803051e+05, 2.80560918e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.40396846e+04, 8.39880908e+04, 1.20385195e+05, 8.39539697e+04, 8.40772812e+04, 5.17575664e+04, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.97299426e+05, 2.97115836e+05, 4.25522188e+05, 2.96997043e+05, 2.97076367e+05, 1.83095859e+05, ],
    'CountWeightedFull'                                                              : [ 2.97122184e+05, 2.97103059e+05, 2.97091328e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.14740445e+05, 2.97122184e+05, 2.80506012e+05, 3.14740445e+05, 2.97122184e+05, 2.80506012e+05, 3.14740445e+05, 2.97122184e+05, 2.80506012e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.14741430e+05, 2.80506012e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 8.40243936e+04, 8.39717012e+04, 1.20361301e+05, 8.39373916e+04, 8.40606445e+04, 5.17479375e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.97245125e+05, 2.97057988e+05, 4.25437695e+05, 2.96938477e+05, 2.97017504e+05, 1.83061742e+05, ],
  }),
  ("nof_tree_events",                 297199),
  ("nof_db_events",                   297199),
  ("fsize_local",                     2182242785), # 2.18GB, avg file size 363.71MB
  ("fsize_db",                        23548779929), # 23.55GB, avg file size 31.69MB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2018/2021Dec29_woPresel_nom_hh_bbww_hh_multilepton/ntuples/signal_ggf_spin0_450_hh_2b2v_private"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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

