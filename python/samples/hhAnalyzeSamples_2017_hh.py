from collections import OrderedDict as OD

# file generated at 2020-08-24 20:07:44 with the following command:
# create_dictionary.py -m python/samples/metaDict_2017_hh.py -p python/samples/sampleLocations_2017_hh_bbww.txt -N samples_2017 -E 2017 -o python/samples -g hhAnalyzeSamples_2017_hh.py -M

samples_2017 = OD()
samples_2017["/VBFToRadionToHHTo2B2VTo2L2Nu_M-300_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_300_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_spin0_300_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 279999, ],
    'CountWeighted'                                                                  : [ 2.79965500e+05, 2.79957312e+05, 2.79952250e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.79965500e+05, 2.79965500e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.71087500e+05, 2.71074969e+05, 2.71091188e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.71087500e+05, 2.68963062e+05, 2.73162312e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.71087500e+05, 2.71087500e+05, ],
  }),
  ("nof_tree_events",                 279999),
  ("nof_db_events",                   279999),
  ("fsize_local",                     1542355298), # 1.54GB, avg file size 1.54GB
  ("fsize_db",                        18070036516), # 18.07GB, avg file size 1.29GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_300_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToRadionToHHTo2B2VTo2L2Nu_M-350_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_350_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_spin0_350_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 285000, ],
    'CountWeighted'                                                                  : [ 2.84952188e+05, 2.84992656e+05, 2.85007688e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.84952188e+05, 2.84952188e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.75531781e+05, 2.75547812e+05, 2.75569594e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.75531781e+05, 2.73285031e+05, 2.77728719e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.75531781e+05, 2.75531781e+05, ],
  }),
  ("nof_tree_events",                 285000),
  ("nof_db_events",                   285000),
  ("fsize_local",                     1642759596), # 1.64GB, avg file size 1.64GB
  ("fsize_db",                        18927275912), # 18.93GB, avg file size 996.17MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_350_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToRadionToHHTo2B2VTo2L2Nu_M-400_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_400_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_spin0_400_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99870781e+04, 9.99542266e+04, 9.99653984e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99870781e+04, 9.99870781e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.64848047e+04, 9.64607891e+04, 9.64732656e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.64848047e+04, 9.56588438e+04, 9.72928828e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.64848047e+04, 9.64848047e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     597362467), # 597.36MB, avg file size 597.36MB
  ("fsize_db",                        6827583120), # 6.83GB, avg file size 682.76MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_400_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToRadionToHHTo2B2VTo2L2Nu_M-750_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_750_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_spin0_750_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99750000e+04, 9.99893594e+04, 9.99675391e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99750000e+04, 9.99750000e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.59412969e+04, 9.59464844e+04, 9.59394062e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.59412969e+04, 9.50115234e+04, 9.68588594e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.59412969e+04, 9.59412969e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     672658348), # 672.66MB, avg file size 672.66MB
  ("fsize_db",                        7423075893), # 7.42GB, avg file size 571.01MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_750_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_250_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_250_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 399998, ],
    'CountWeighted'                                                                  : [ 3.99935094e+05, 3.99979500e+05, 3.99904500e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99935094e+05, 3.99935094e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.92877031e+05, 3.92882156e+05, 3.92868094e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.92877031e+05, 3.91022406e+05, 3.94641750e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.92877031e+05, 3.92877031e+05, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     1393068280), # 1.39GB, avg file size 1.39GB
  ("fsize_db",                        20842533885), # 20.84GB, avg file size 1.49GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_250_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-260_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_260_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_260_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 4.00019344e+05, 3.99948656e+05, 4.00035469e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.06264625e+05, 3.99993938e+05, 3.91181688e+05, 4.06264625e+05, 3.99993938e+05, 3.91181688e+05, 4.06264625e+05, 3.99993938e+05, 3.91181688e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.06264625e+05, 3.91181688e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.92486625e+05, 3.92430031e+05, 3.92499469e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.92486625e+05, 3.90535906e+05, 3.94349750e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.98574656e+05, 3.92467844e+05, 3.83855594e+05, 3.98574656e+05, 3.92467844e+05, 3.83855594e+05, 3.98574656e+05, 3.92467844e+05, 3.83855594e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.98574656e+05, 3.83855594e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1403651445), # 1.40GB, avg file size 1.40GB
  ("fsize_db",                        20086379241), # 20.09GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_260_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-270_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_270_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_270_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 388000, ],
    'CountWeighted'                                                                  : [ 3.87938344e+05, 3.87980688e+05, 3.88041688e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.95280062e+05, 3.87938344e+05, 3.78436719e+05, 3.95280062e+05, 3.87938344e+05, 3.78436719e+05, 3.95280062e+05, 3.87938344e+05, 3.78436719e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.95280062e+05, 3.78436719e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.80323531e+05, 3.80342812e+05, 3.80399656e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.80323531e+05, 3.78365438e+05, 3.82203562e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.87468250e+05, 3.80323531e+05, 3.71034406e+05, 3.87468250e+05, 3.80323531e+05, 3.71034406e+05, 3.87468250e+05, 3.80323531e+05, 3.71034406e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.87468250e+05, 3.71034406e+05, ],
  }),
  ("nof_tree_events",                 388000),
  ("nof_db_events",                   388000),
  ("fsize_local",                     1383507283), # 1.38GB, avg file size 1.38GB
  ("fsize_db",                        19501546911), # 19.50GB, avg file size 1.03GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_270_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-280_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_280_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_280_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 384000, ],
    'CountWeighted'                                                                  : [ 3.83960906e+05, 3.83999344e+05, 3.84009062e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.83960906e+05, 3.83960906e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.76109719e+05, 3.76120094e+05, 3.76153469e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.76109719e+05, 3.74100906e+05, 3.78035656e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.76109719e+05, 3.76109719e+05, ],
  }),
  ("nof_tree_events",                 384000),
  ("nof_db_events",                   384000),
  ("fsize_local",                     1396375457), # 1.40GB, avg file size 1.40GB
  ("fsize_db",                        20165336883), # 20.17GB, avg file size 1.44GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_280_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-320_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_320_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_320_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 299996, ],
    'CountWeighted'                                                                  : [ 2.99978719e+05, 2.99953188e+05, 3.00000781e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.09821156e+05, 2.99978719e+05, 2.89309156e+05, 3.09821156e+05, 2.99978719e+05, 2.89309156e+05, 3.09821156e+05, 2.99978719e+05, 2.89309156e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.09821156e+05, 2.89309156e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93002969e+05, 2.92966094e+05, 2.93030594e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93002969e+05, 2.91266844e+05, 2.94686875e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.02568062e+05, 2.93002969e+05, 2.82614969e+05, 3.02568062e+05, 2.93002969e+05, 2.82614969e+05, 3.02568062e+05, 2.93002969e+05, 2.82614969e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.02568062e+05, 2.82614969e+05, ],
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     1141656518), # 1.14GB, avg file size 1.14GB
  ("fsize_db",                        15538010606), # 15.54GB, avg file size 776.90MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_320_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-350_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_350_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_350_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99963906e+05, 2.99939562e+05, 2.99937719e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.12013188e+05, 2.99963906e+05, 2.87641375e+05, 3.12013188e+05, 2.99963906e+05, 2.87641375e+05, 3.12013188e+05, 2.99963906e+05, 2.87641375e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.12013188e+05, 2.87641375e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92296875e+05, 2.92276500e+05, 2.92284375e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92296875e+05, 2.90420281e+05, 2.94125812e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.03971906e+05, 2.92296875e+05, 2.80326250e+05, 3.03971906e+05, 2.92296875e+05, 2.80326250e+05, 3.03971906e+05, 2.92296875e+05, 2.80326250e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.03971906e+05, 2.80326250e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1178826708), # 1.18GB, avg file size 1.18GB
  ("fsize_db",                        15654716885), # 15.65GB, avg file size 1.30GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_350_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-400_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_400_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_400_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 292000, ],
    'CountWeighted'                                                                  : [ 2.92012969e+05, 2.91997969e+05, 2.91916281e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.06717531e+05, 2.92012969e+05, 2.77666094e+05, 3.06717531e+05, 2.92012969e+05, 2.77666094e+05, 3.06717531e+05, 2.92012969e+05, 2.77666094e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.06717531e+05, 2.77666094e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.83787938e+05, 2.83771688e+05, 2.83730594e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.83787938e+05, 2.81813438e+05, 2.85718000e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.98033281e+05, 2.83787938e+05, 2.69897219e+05, 2.98033281e+05, 2.83787938e+05, 2.69897219e+05, 2.98033281e+05, 2.83787938e+05, 2.69897219e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.98033281e+05, 2.69897188e+05, ],
  }),
  ("nof_tree_events",                 292000),
  ("nof_db_events",                   292000),
  ("fsize_local",                     1202876535), # 1.20GB, avg file size 1.20GB
  ("fsize_db",                        15536600053), # 15.54GB, avg file size 971.04MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_400_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-450_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_450_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_450_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 299999, ],
    'CountWeighted'                                                                  : [ 2.99934125e+05, 2.99939250e+05, 2.99943438e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.17769562e+05, 2.99934125e+05, 2.83225312e+05, 3.17769562e+05, 2.99934125e+05, 2.83225312e+05, 3.17769562e+05, 2.99934125e+05, 2.83225312e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.17769562e+05, 2.83225312e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.90854625e+05, 2.90842125e+05, 2.90873250e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.90854625e+05, 2.88701844e+05, 2.92966094e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.08073438e+05, 2.90854625e+05, 2.74691656e+05, 3.08073438e+05, 2.90854625e+05, 2.74691656e+05, 3.08073438e+05, 2.90854625e+05, 2.74691656e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.08073438e+05, 2.74691656e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1283200553), # 1.28GB, avg file size 1.28GB
  ("fsize_db",                        16296871303), # 16.30GB, avg file size 814.84MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_450_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_500_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_500_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 2.00008344e+05, 2.00006078e+05, 1.99958984e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.13377781e+05, 2.00008344e+05, 1.87622562e+05, 2.13377781e+05, 2.00008344e+05, 1.87622562e+05, 2.13377781e+05, 2.00008344e+05, 1.87622562e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.13377781e+05, 1.87622531e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.93662781e+05, 1.93646531e+05, 1.93653844e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.93662781e+05, 1.92176625e+05, 1.95127250e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.06579938e+05, 1.93662781e+05, 1.81721297e+05, 2.06579938e+05, 1.93662781e+05, 1.81721297e+05, 2.06579938e+05, 1.93662781e+05, 1.81721297e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.06579938e+05, 1.81721297e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     881837195), # 881.84MB, avg file size 881.84MB
  ("fsize_db",                        10964750047), # 10.96GB, avg file size 913.73MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_500_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-600_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_600_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_600_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 199998, ],
    'CountWeighted'                                                                  : [ 1.99989312e+05, 1.99981062e+05, 1.99980594e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.15942500e+05, 1.99989312e+05, 1.85664875e+05, 2.15942500e+05, 1.99989312e+05, 1.85664875e+05, 2.15942500e+05, 1.99989312e+05, 1.85664875e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.15942500e+05, 1.85664875e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92976859e+05, 1.92970141e+05, 1.92963812e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92976859e+05, 1.91357547e+05, 1.94581062e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.08330703e+05, 1.92976859e+05, 1.79193625e+05, 2.08330703e+05, 1.92976859e+05, 1.79193625e+05, 2.08330703e+05, 1.92976859e+05, 1.79193625e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.08330703e+05, 1.79193625e+05, ],
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     927233398), # 927.23MB, avg file size 927.23MB
  ("fsize_db",                        11169462986), # 11.17GB, avg file size 1.24GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_600_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-650_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_650_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_650_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99939562e+05, 1.99979734e+05, 1.99955062e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.17043281e+05, 1.99939562e+05, 1.84822469e+05, 2.17043281e+05, 1.99939562e+05, 1.84822469e+05, 2.17043281e+05, 1.99939562e+05, 1.84822469e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.17043281e+05, 1.84822469e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92822750e+05, 1.92822297e+05, 1.92862281e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92822750e+05, 1.91177844e+05, 1.94446906e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.09263188e+05, 1.92822750e+05, 1.78266844e+05, 2.09263188e+05, 1.92822750e+05, 1.78266844e+05, 2.09263188e+05, 1.92822750e+05, 1.78266844e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.09263188e+05, 1.78266844e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     942915017), # 942.92MB, avg file size 942.92MB
  ("fsize_db",                        11395262580), # 11.40GB, avg file size 949.61MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_650_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-700_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_700_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_700_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 199998, ],
    'CountWeighted'                                                                  : [ 1.99995562e+05, 1.99963000e+05, 1.99971344e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.18047469e+05, 1.99995406e+05, 1.84041406e+05, 2.18047469e+05, 1.99995406e+05, 1.84041406e+05, 2.18047469e+05, 1.99995406e+05, 1.84041406e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.18047469e+05, 1.84041406e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92656312e+05, 1.92645406e+05, 1.92633688e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92656312e+05, 1.90971281e+05, 1.94319344e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.10006312e+05, 1.92655516e+05, 1.77334688e+05, 2.10006312e+05, 1.92655516e+05, 1.77334688e+05, 2.10006312e+05, 1.92655516e+05, 1.77334688e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.10006312e+05, 1.77334688e+05, ],
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     954533681), # 954.53MB, avg file size 954.53MB
  ("fsize_db",                        11438629863), # 11.44GB, avg file size 1.43GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_700_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_750_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_750_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 2.00016312e+05, 2.00001359e+05, 1.99923000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.00016312e+05, 2.00016312e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92574750e+05, 1.92549656e+05, 1.92533703e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92574750e+05, 1.90871141e+05, 1.94256500e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.92574750e+05, 1.92574750e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     969801833), # 969.80MB, avg file size 969.80MB
  ("fsize_db",                        11931037531), # 11.93GB, avg file size 1.08GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_750_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-800_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_800_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_800_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 197000, ],
    'CountWeighted'                                                                  : [ 1.97019812e+05, 1.96970969e+05, 1.96972938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.97019812e+05, 1.97019812e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.89484609e+05, 1.89441875e+05, 1.89464344e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.89484609e+05, 1.87768828e+05, 1.91179844e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.89484609e+05, 1.89484609e+05, ],
  }),
  ("nof_tree_events",                 197000),
  ("nof_db_events",                   197000),
  ("fsize_local",                     964094143), # 964.09MB, avg file size 964.09MB
  ("fsize_db",                        11877663068), # 11.88GB, avg file size 791.84MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_800_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-850_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_850_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_850_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 199999, ],
    'CountWeighted'                                                                  : [ 1.99945938e+05, 1.99952031e+05, 1.99972406e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99945938e+05, 1.99945938e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92202516e+05, 1.92188938e+05, 1.92235328e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92202516e+05, 1.90440625e+05, 1.93951406e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.92202516e+05, 1.92202516e+05, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     985929109), # 985.93MB, avg file size 985.93MB
  ("fsize_db",                        12127308050), # 12.13GB, avg file size 808.49MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_850_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-900_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_900_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_900_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99779609e+04, 9.99952109e+04, 9.99418828e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.10667148e+05, 9.99779609e+04, 9.08111484e+04, 1.10667148e+05, 9.99779609e+04, 9.08111484e+04, 1.10667148e+05, 9.99779609e+04, 9.08111484e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.10667148e+05, 9.08111484e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.60393047e+04, 9.60472422e+04, 9.60209062e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.60393047e+04, 9.51481328e+04, 9.69225703e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.06280586e+05, 9.60393047e+04, 8.72512109e+04, 1.06280586e+05, 9.60393047e+04, 8.72512109e+04, 1.06280586e+05, 9.60393047e+04, 8.72512109e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.06280586e+05, 8.72512109e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     493482159), # 493.48MB, avg file size 493.48MB
  ("fsize_db",                        5935911198), # 5.94GB, avg file size 539.63MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_900_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-1000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1000_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_1000_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99649453e+04, 9.99692656e+04, 9.99609766e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.11332906e+05, 9.99634766e+04, 9.03303359e+04, 1.11332906e+05, 9.99634766e+04, 9.03303359e+04, 1.11332906e+05, 9.99634766e+04, 9.03303359e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.11333891e+05, 9.03293672e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.59470859e+04, 9.59401484e+04, 9.59563359e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.59470859e+04, 9.50390547e+04, 9.68462812e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.06832422e+05, 9.59457969e+04, 8.67123516e+04, 1.06832422e+05, 9.59457969e+04, 8.67123516e+04, 1.06832422e+05, 9.59457969e+04, 8.67123516e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.06832664e+05, 8.67121016e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     499211970), # 499.21MB, avg file size 499.21MB
  ("fsize_db",                        5930718483), # 5.93GB, avg file size 847.25MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1000_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-1250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1250_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_1250_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99788438e+04, 9.99858594e+04, 9.99620156e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99788438e+04, 9.99788438e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.58526562e+04, 9.58482656e+04, 9.58486953e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.58526562e+04, 9.49302422e+04, 9.67696172e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.58526562e+04, 9.58526562e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     510651963), # 510.65MB, avg file size 510.65MB
  ("fsize_db",                        6224151597), # 6.22GB, avg file size 778.02MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1250_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-1500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1500_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_1500_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 99998, ],
    'CountWeighted'                                                                  : [ 9.99628750e+04, 9.99532734e+04, 9.99488125e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.13887039e+05, 9.99620547e+04, 8.85085312e+04, 1.13887039e+05, 9.99620547e+04, 8.85085312e+04, 1.13887039e+05, 9.99620547e+04, 8.85085312e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.13887391e+05, 8.85081719e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.57350859e+04, 9.57227031e+04, 9.57325234e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.57350859e+04, 9.47964297e+04, 9.66682969e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.09057695e+05, 9.57342578e+04, 8.47827500e+04, 1.09057695e+05, 9.57342578e+04, 8.47827500e+04, 1.09057695e+05, 9.57342578e+04, 8.47827500e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.09058047e+05, 8.47823906e+04, ],
  }),
  ("nof_tree_events",                 99998),
  ("nof_db_events",                   99998),
  ("fsize_local",                     508711053), # 508.71MB, avg file size 508.71MB
  ("fsize_db",                        6171310375), # 6.17GB, avg file size 514.28MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1500_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-1750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1750_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_1750_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99740938e+04, 9.99377188e+04, 9.99650703e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99740938e+04, 9.99740938e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.56086641e+04, 9.55888047e+04, 9.55924453e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.56086641e+04, 9.46437344e+04, 9.65669531e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.56086641e+04, 9.56086641e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     513819685), # 513.82MB, avg file size 513.82MB
  ("fsize_db",                        6356319473), # 6.36GB, avg file size 635.63MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1750_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-2000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_2000_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_2000_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99257969e+04, 9.99186016e+04, 9.99469297e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.15689836e+05, 9.99245391e+04, 8.72035312e+04, 1.15689836e+05, 9.99245391e+04, 8.72035312e+04, 1.15689836e+05, 9.99245391e+04, 8.72035312e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.15698234e+05, 8.71977188e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.55449453e+04, 9.55305625e+04, 9.55616875e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.55449453e+04, 9.45779062e+04, 9.65081719e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.10602719e+05, 9.55436953e+04, 8.33882422e+04, 1.10602719e+05, 9.55436953e+04, 8.33882422e+04, 1.10602719e+05, 9.55436953e+04, 8.33882422e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.10610609e+05, 8.33827734e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     514063142), # 514.06MB, avg file size 514.06MB
  ("fsize_db",                        6172348486), # 6.17GB, avg file size 771.54MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_2000_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-2500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_2500_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_2500_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 97000, ],
    'CountWeighted'                                                                  : [ 9.68743906e+04, 9.68842109e+04, 9.68619141e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.68743906e+04, 9.68743906e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.24944922e+04, 9.24873438e+04, 9.25064453e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.24944922e+04, 9.15366875e+04, 9.34521641e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.24944922e+04, 9.24944922e+04, ],
  }),
  ("nof_tree_events",                 97000),
  ("nof_db_events",                   97000),
  ("fsize_local",                     504894131), # 504.89MB, avg file size 504.89MB
  ("fsize_db",                        6425534542), # 6.43GB, avg file size 494.27MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_2500_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-3000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_3000_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_3000_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 97999, ],
    'CountWeighted'                                                                  : [ 9.77553828e+04, 9.77370625e+04, 9.77472812e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.77553828e+04, 9.77553828e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.33116172e+04, 9.32940234e+04, 9.33152266e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.33116172e+04, 9.23455156e+04, 9.42780781e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.33116172e+04, 9.33116172e+04, ],
  }),
  ("nof_tree_events",                 97999),
  ("nof_db_events",                   97999),
  ("fsize_local",                     513003671), # 513.00MB, avg file size 513.00MB
  ("fsize_db",                        6497731845), # 6.50GB, avg file size 590.70MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_3000_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_250_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_250_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                                          : [ 399997, ],
    'CountWeighted'                                                                  : [ 3.99934625e+05, 4.00016094e+05, 3.99956156e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.04892000e+05, 3.99929000e+05, 3.92225969e+05, 4.04892000e+05, 3.99929000e+05, 3.92225969e+05, 4.04892000e+05, 3.99929000e+05, 3.92225969e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.04892000e+05, 3.92225969e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.92393438e+05, 3.92444156e+05, 3.92422188e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.92393438e+05, 3.90446531e+05, 3.94258875e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.97210156e+05, 3.92388125e+05, 3.84858000e+05, 3.97210156e+05, 3.92388125e+05, 3.84858000e+05, 3.97210156e+05, 3.92388125e+05, 3.84858000e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.97210156e+05, 3.84858000e+05, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     1409967891), # 1.41GB, avg file size 1.41GB
  ("fsize_db",                        20041115926), # 20.04GB, avg file size 871.35MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_250_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-260_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_260_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_260_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 399997, ],
    'CountWeighted'                                                                  : [ 3.99964062e+05, 4.00008719e+05, 4.00035969e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.06237406e+05, 3.99962656e+05, 3.91183125e+05, 4.06237406e+05, 3.99962656e+05, 3.91183125e+05, 4.06237406e+05, 3.99962656e+05, 3.91183125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.06237406e+05, 3.91183094e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.92110688e+05, 3.92118000e+05, 3.92186219e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.92110688e+05, 3.90089281e+05, 3.94044281e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.98209875e+05, 3.92108469e+05, 3.83531219e+05, 3.98209875e+05, 3.92108469e+05, 3.83531219e+05, 3.98209875e+05, 3.92108469e+05, 3.83531219e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.98209875e+05, 3.83531156e+05, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     1433311582), # 1.43GB, avg file size 1.43GB
  ("fsize_db",                        20202072552), # 20.20GB, avg file size 962.00MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_260_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-270_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_270_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_270_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 4.00050812e+05, 3.99949062e+05, 4.00006281e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.07495188e+05, 4.00050812e+05, 3.90160875e+05, 4.07495188e+05, 4.00050812e+05, 3.90160875e+05, 4.07495188e+05, 4.00050812e+05, 3.90160875e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.07495188e+05, 3.90160875e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.91839000e+05, 3.91744812e+05, 3.91839719e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.91839000e+05, 3.89746312e+05, 3.93838625e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.99109312e+05, 3.91839000e+05, 3.82216250e+05, 3.99109312e+05, 3.91839000e+05, 3.82216250e+05, 3.99109312e+05, 3.91839000e+05, 3.82216250e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.99109312e+05, 3.82216250e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1458129105), # 1.46GB, avg file size 1.46GB
  ("fsize_db",                        20268702810), # 20.27GB, avg file size 921.30MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_270_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-280_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_280_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_280_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    31),
  ("nof_events",                      {
    'Count'                                                                          : [ 399995, ],
    'CountWeighted'                                                                  : [ 4.00028781e+05, 3.99941938e+05, 3.99945562e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.08732719e+05, 4.00028344e+05, 3.89179938e+05, 4.08732719e+05, 4.00028344e+05, 3.89179938e+05, 4.08732719e+05, 4.00028344e+05, 3.89179938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.08732719e+05, 3.89179938e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.91534812e+05, 3.91453969e+05, 3.91494094e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.91534812e+05, 3.89393312e+05, 3.93593594e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.00014844e+05, 3.91533312e+05, 3.80976969e+05, 4.00014844e+05, 3.91533312e+05, 3.80976969e+05, 4.00014844e+05, 3.91533312e+05, 3.80976969e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.00014844e+05, 3.80976969e+05, ],
  }),
  ("nof_tree_events",                 399995),
  ("nof_db_events",                   399995),
  ("fsize_local",                     1482716868), # 1.48GB, avg file size 1.48GB
  ("fsize_db",                        20542842010), # 20.54GB, avg file size 662.67MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_280_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-300_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_300_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_300_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    26),
  ("nof_events",                      {
    'Count'                                                                          : [ 399998, ],
    'CountWeighted'                                                                  : [ 4.00013625e+05, 3.99966188e+05, 4.00007031e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.11013219e+05, 4.00013625e+05, 3.87362000e+05, 4.11013219e+05, 4.00013625e+05, 3.87362000e+05, 4.11013219e+05, 4.00013625e+05, 3.87362000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.11013219e+05, 3.87362000e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.90813719e+05, 3.90772531e+05, 3.90821062e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.90813719e+05, 3.88527438e+05, 3.93030875e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.01504188e+05, 3.90813719e+05, 3.78515406e+05, 4.01504188e+05, 3.90813719e+05, 3.78515406e+05, 4.01504188e+05, 3.90813719e+05, 3.78515406e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.01504188e+05, 3.78515406e+05, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     1527627493), # 1.53GB, avg file size 1.53GB
  ("fsize_db",                        20998766588), # 21.00GB, avg file size 807.64MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_300_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-320_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_320_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_320_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 293998, ],
    'CountWeighted'                                                                  : [ 2.93950219e+05, 2.93936656e+05, 2.93988000e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.03633219e+05, 2.93949562e+05, 2.83519500e+05, 3.03633219e+05, 2.93949562e+05, 2.83519500e+05, 3.03633219e+05, 2.93949562e+05, 2.83519500e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.03633219e+05, 2.83519438e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.86900281e+05, 2.86878500e+05, 2.86937062e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.86900281e+05, 2.85170062e+05, 2.88585656e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.96286625e+05, 2.86898875e+05, 2.76749094e+05, 2.96286625e+05, 2.86898875e+05, 2.76749094e+05, 2.96286625e+05, 2.86898875e+05, 2.76749094e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.96286625e+05, 2.76749031e+05, ],
  }),
  ("nof_tree_events",                 293998),
  ("nof_db_events",                   293998),
  ("fsize_local",                     1153759751), # 1.15GB, avg file size 1.15GB
  ("fsize_db",                        15577989269), # 15.58GB, avg file size 916.35MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_320_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-350_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_350_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_350_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 281999, ],
    'CountWeighted'                                                                  : [ 2.81963906e+05, 2.81966500e+05, 2.81960625e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.93259625e+05, 2.81963469e+05, 2.70388812e+05, 2.93259625e+05, 2.81963469e+05, 2.70388812e+05, 2.93259625e+05, 2.81963469e+05, 2.70388812e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.93260000e+05, 2.70388438e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.74728781e+05, 2.74702812e+05, 2.74747688e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.74728781e+05, 2.72980812e+05, 2.76436719e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.85667906e+05, 2.74727500e+05, 2.63486094e+05, 2.85667906e+05, 2.74727500e+05, 2.63486094e+05, 2.85667906e+05, 2.74727500e+05, 2.63486094e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.85668281e+05, 2.63485719e+05, ],
  }),
  ("nof_tree_events",                 281999),
  ("nof_db_events",                   281999),
  ("fsize_local",                     1147413751), # 1.15GB, avg file size 1.15GB
  ("fsize_db",                        15217194365), # 15.22GB, avg file size 845.40MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_350_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-400_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_400_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_400_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 298000, ],
    'CountWeighted'                                                                  : [ 2.97937062e+05, 2.98017094e+05, 2.98002812e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.13029844e+05, 2.97937062e+05, 2.83380000e+05, 3.13029844e+05, 2.97937062e+05, 2.83380000e+05, 3.13029844e+05, 2.97937062e+05, 2.83380000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.13031188e+05, 2.83379938e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.89718219e+05, 2.89765250e+05, 2.89772562e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.89718219e+05, 2.87765500e+05, 2.91640000e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.04311938e+05, 2.89718219e+05, 2.75597125e+05, 3.04311938e+05, 2.89718219e+05, 2.75597125e+05, 3.04311938e+05, 2.89718219e+05, 2.75597125e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.04313281e+05, 2.75597062e+05, ],
  }),
  ("nof_tree_events",                 298000),
  ("nof_db_events",                   298000),
  ("fsize_local",                     1271144466), # 1.27GB, avg file size 1.27GB
  ("fsize_db",                        16133391096), # 16.13GB, avg file size 806.67MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_400_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-450_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_450_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_450_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99910875e+05, 2.99926844e+05, 2.99942094e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.17756844e+05, 2.99910875e+05, 2.83222438e+05, 3.17756844e+05, 2.99910875e+05, 2.83222438e+05, 3.17756844e+05, 2.99910875e+05, 2.83222438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.17756844e+05, 2.83222375e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.91241250e+05, 2.91238719e+05, 2.91278094e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.91241250e+05, 2.89212500e+05, 2.93244562e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.08485094e+05, 2.91241250e+05, 2.75076500e+05, 3.08485094e+05, 2.91241250e+05, 2.75076500e+05, 3.08485094e+05, 2.91241250e+05, 2.75076500e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.08485094e+05, 2.75076438e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1329758066), # 1.33GB, avg file size 1.33GB
  ("fsize_db",                        16485829471), # 16.49GB, avg file size 867.68MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_450_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_500_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_500_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99968344e+05, 1.99967312e+05, 1.99974656e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.13382844e+05, 1.99968344e+05, 1.87657156e+05, 2.13382844e+05, 1.99968344e+05, 1.87657156e+05, 2.13382844e+05, 1.99968344e+05, 1.87657156e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.13382844e+05, 1.87657156e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.94074656e+05, 1.94062219e+05, 1.94084219e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.94074656e+05, 1.92703234e+05, 1.95425719e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.07037688e+05, 1.94074656e+05, 1.82157562e+05, 2.07037688e+05, 1.94074656e+05, 1.82157562e+05, 2.07037688e+05, 1.94074656e+05, 1.82157562e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.07037688e+05, 1.82157562e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     917461285), # 917.46MB, avg file size 917.46MB
  ("fsize_db",                        11497248581), # 11.50GB, avg file size 547.49MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_500_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-550_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_550_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_550_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99970766e+05, 1.99977000e+05, 1.99959719e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.14737984e+05, 1.99970250e+05, 1.86599344e+05, 2.14737984e+05, 1.99970250e+05, 1.86599344e+05, 2.14737984e+05, 1.99970250e+05, 1.86599344e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.14738266e+05, 1.86599062e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.94086828e+05, 1.94091906e+05, 1.94073047e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.94086828e+05, 1.92725109e+05, 1.95427938e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.08363906e+05, 1.94085828e+05, 1.81141172e+05, 2.08363906e+05, 1.94085828e+05, 1.81141172e+05, 2.08363906e+05, 1.94085828e+05, 1.81141172e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.08364000e+05, 1.81141094e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     941303853), # 941.30MB, avg file size 941.30MB
  ("fsize_db",                        11543534297), # 11.54GB, avg file size 679.03MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_550_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-600_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_600_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_600_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 192000, ],
    'CountWeighted'                                                                  : [ 1.91969828e+05, 1.91961531e+05, 1.91941578e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.07286562e+05, 1.91969828e+05, 1.78226031e+05, 2.07286562e+05, 1.91969828e+05, 1.78226031e+05, 2.07286562e+05, 1.91969828e+05, 1.78226031e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.07286562e+05, 1.78226031e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.86268234e+05, 1.86262266e+05, 1.86254141e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.86268234e+05, 1.84954141e+05, 1.87565750e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.01087562e+05, 1.86268234e+05, 1.72965844e+05, 2.01087562e+05, 1.86268234e+05, 1.72965844e+05, 2.01087562e+05, 1.86268234e+05, 1.72965844e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.01087562e+05, 1.72965844e+05, ],
  }),
  ("nof_tree_events",                 192000),
  ("nof_db_events",                   192000),
  ("fsize_local",                     922032674), # 922.03MB, avg file size 922.03MB
  ("fsize_db",                        11191273021), # 11.19GB, avg file size 746.08MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_600_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-650_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_650_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_650_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 2.00017266e+05, 2.00005656e+05, 1.99948906e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.17034609e+05, 2.00017266e+05, 1.84832906e+05, 2.17034609e+05, 2.00017266e+05, 1.84832906e+05, 2.17034609e+05, 2.00017266e+05, 1.84832906e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.17034609e+05, 1.84832906e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.94032656e+05, 1.94005844e+05, 1.94011438e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.94032656e+05, 1.92660047e+05, 1.95385219e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.10511719e+05, 1.94032656e+05, 1.79347000e+05, 2.10511719e+05, 1.94032656e+05, 1.79347000e+05, 2.10511719e+05, 1.94032656e+05, 1.79347000e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.10511719e+05, 1.79347000e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     974105433), # 974.11MB, avg file size 974.11MB
  ("fsize_db",                        11871616225), # 11.87GB, avg file size 539.62MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_650_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-700_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_700_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_700_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 199998, ],
    'CountWeighted'                                                                  : [ 1.99971609e+05, 1.99965469e+05, 1.99953031e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.18036688e+05, 1.99971609e+05, 1.84074531e+05, 2.18036688e+05, 1.99971609e+05, 1.84074531e+05, 2.18036688e+05, 1.99971609e+05, 1.84074531e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.18036688e+05, 1.84074531e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.94057781e+05, 1.94042312e+05, 1.94051625e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.94057781e+05, 1.92703344e+05, 1.95392781e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.11544344e+05, 1.94057781e+05, 1.78659125e+05, 2.11544344e+05, 1.94057781e+05, 1.78659125e+05, 2.11544344e+05, 1.94057781e+05, 1.78659125e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.11544344e+05, 1.78659125e+05, ],
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     982447761), # 982.45MB, avg file size 982.45MB
  ("fsize_db",                        11820942716), # 11.82GB, avg file size 656.72MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_700_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_750_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_750_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 198000, ],
    'CountWeighted'                                                                  : [ 1.97954203e+05, 1.97934281e+05, 1.97956188e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.16759594e+05, 1.97954203e+05, 1.81572250e+05, 2.16759594e+05, 1.97954203e+05, 1.81572250e+05, 2.16759594e+05, 1.97954203e+05, 1.81572250e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.16759594e+05, 1.81572250e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92059891e+05, 1.92034156e+05, 1.92075344e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92059891e+05, 1.90710719e+05, 1.93389422e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.10256422e+05, 1.92059891e+05, 1.76181594e+05, 2.10256422e+05, 1.92059891e+05, 1.76181594e+05, 2.10256422e+05, 1.92059891e+05, 1.76181594e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.10256422e+05, 1.76181594e+05, ],
  }),
  ("nof_tree_events",                 198000),
  ("nof_db_events",                   198000),
  ("fsize_local",                     979880511), # 979.88MB, avg file size 979.88MB
  ("fsize_db",                        11778577981), # 11.78GB, avg file size 785.24MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_750_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-800_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_800_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_800_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99949281e+05, 1.99988812e+05, 1.99985078e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.19796578e+05, 1.99949281e+05, 1.82727125e+05, 2.19796578e+05, 1.99949281e+05, 1.82727125e+05, 2.19796578e+05, 1.99949281e+05, 1.82727125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.19796750e+05, 1.82726969e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.94068531e+05, 1.94076844e+05, 1.94104391e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.94068531e+05, 1.92727438e+05, 1.95395438e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.13289656e+05, 1.94068531e+05, 1.77378609e+05, 2.13289656e+05, 1.94068531e+05, 1.77378609e+05, 2.13289656e+05, 1.94068531e+05, 1.77378609e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.13289688e+05, 1.77378562e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     995548134), # 995.55MB, avg file size 995.55MB
  ("fsize_db",                        11967660431), # 11.97GB, avg file size 598.38MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_800_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-850_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_850_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_850_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99953641e+05, 1.99962438e+05, 1.99948219e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99953641e+05, 1.99953641e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.94009500e+05, 1.94008594e+05, 1.94007844e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.94009500e+05, 1.92654766e+05, 1.95344109e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.94009500e+05, 1.94009500e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1007441071), # 1.01GB, avg file size 1.01GB
  ("fsize_db",                        12348394332), # 12.35GB, avg file size 823.23MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_850_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-900_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_900_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_900_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 9.99968438e+04, 1.00009273e+05, 9.99726875e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.10560906e+05, 9.99968438e+04, 9.09697969e+04, 1.10560906e+05, 9.99968438e+04, 9.09697969e+04, 1.10560906e+05, 9.99968438e+04, 9.09697969e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.10560906e+05, 9.09697969e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.71427422e+04, 9.71461953e+04, 9.71339219e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.71427422e+04, 9.64923047e+04, 9.77847656e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.07386195e+05, 9.71427422e+04, 8.83859922e+04, 1.07386195e+05, 9.71427422e+04, 8.83859922e+04, 1.07386195e+05, 9.71427422e+04, 8.83859922e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.07386195e+05, 8.83859922e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     504379029), # 504.38MB, avg file size 504.38MB
  ("fsize_db",                        6022388849), # 6.02GB, avg file size 669.15MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_900_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1000_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_1000_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 9.99710625e+04, 9.99725859e+04, 9.99791562e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.11340242e+05, 9.99710625e+04, 9.03299844e+04, 1.11340242e+05, 9.99710625e+04, 9.03299844e+04, 1.11340242e+05, 9.99710625e+04, 9.03299844e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.11340320e+05, 9.03298984e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70842969e+04, 9.70857734e+04, 9.70906953e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70842969e+04, 9.64272109e+04, 9.77325312e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.08109578e+05, 9.70842969e+04, 8.77295781e+04, 1.08109578e+05, 9.70842969e+04, 8.77295781e+04, 1.08109578e+05, 9.70842969e+04, 8.77295781e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.08109617e+05, 8.77295312e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     506790427), # 506.79MB, avg file size 506.79MB
  ("fsize_db",                        6101733672), # 6.10GB, avg file size 610.17MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_1000_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1250_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_1250_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99446016e+04, 9.99858594e+04, 9.99806719e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99446016e+04, 9.99446016e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70694844e+04, 9.70988203e+04, 9.70917422e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70694844e+04, 9.64182188e+04, 9.77125703e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.70694844e+04, 9.70694844e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     514808490), # 514.81MB, avg file size 514.81MB
  ("fsize_db",                        6305015701), # 6.31GB, avg file size 900.72MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_1250_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1500_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_1500_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99451094e+04, 9.99329688e+04, 9.99308438e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99451094e+04, 9.99451094e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70620078e+04, 9.70493125e+04, 9.70570312e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70620078e+04, 9.64089922e+04, 9.77069688e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.70620078e+04, 9.70620078e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     511759708), # 511.76MB, avg file size 511.76MB
  ("fsize_db",                        6512057209), # 6.51GB, avg file size 434.14MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_1500_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1750_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_1750_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 9.99394922e+04, 9.99358828e+04, 9.99586484e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99394922e+04, 9.99394922e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70218828e+04, 9.70116094e+04, 9.70422344e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70218828e+04, 9.63592500e+04, 9.76741641e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.70218828e+04, 9.70218828e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     512368023), # 512.37MB, avg file size 512.37MB
  ("fsize_db",                        6489134095), # 6.49GB, avg file size 540.76MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_1750_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-2000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_2000_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_2000_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99045391e+04, 9.99122734e+04, 9.98898125e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.15680008e+05, 9.99045391e+04, 8.71851562e+04, 1.15680008e+05, 9.99045391e+04, 8.71851562e+04, 1.15680008e+05, 9.99045391e+04, 8.71851562e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.15683203e+05, 8.71819531e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.69378828e+04, 9.69265312e+04, 9.69374219e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.69378828e+04, 9.62644531e+04, 9.76001172e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.12242531e+05, 9.69378828e+04, 8.45933438e+04, 1.12242531e+05, 9.69378828e+04, 8.45933438e+04, 1.12242531e+05, 9.69378828e+04, 8.45933438e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.12245711e+05, 8.45901562e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     511499249), # 511.50MB, avg file size 511.50MB
  ("fsize_db",                        6328288934), # 6.33GB, avg file size 575.30MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_2000_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-2500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_2500_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_2500_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 98000, ],
    'CountWeighted'                                                                  : [ 9.78785625e+04, 9.78791875e+04, 9.78734219e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.14844820e+05, 9.78785625e+04, 8.43865000e+04, 1.14844820e+05, 9.78785625e+04, 8.43865000e+04, 1.14844820e+05, 9.78785625e+04, 8.43865000e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.14845414e+05, 8.43858984e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.49392500e+04, 9.49412266e+04, 9.49372812e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.49392500e+04, 9.42715156e+04, 9.55969688e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.11397375e+05, 9.49392500e+04, 8.18523594e+04, 1.11397375e+05, 9.49392500e+04, 8.18523594e+04, 1.11397375e+05, 9.49392500e+04, 8.18523594e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.11397961e+05, 8.18517734e+04, ],
  }),
  ("nof_tree_events",                 98000),
  ("nof_db_events",                   98000),
  ("fsize_local",                     505361623), # 505.36MB, avg file size 505.36MB
  ("fsize_db",                        6377937593), # 6.38GB, avg file size 490.61MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_2500_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-3000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_3000_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_3000_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 9.98155703e+04, 9.97964531e+04, 9.98027266e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.18531211e+05, 9.98134688e+04, 8.51184453e+04, 1.18531211e+05, 9.98134688e+04, 8.51184453e+04, 1.18531211e+05, 9.98134688e+04, 8.51184453e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.18531953e+05, 8.51168359e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.68419766e+04, 9.68287422e+04, 9.68352656e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.68419766e+04, 9.61636797e+04, 9.75101875e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.15007688e+05, 9.68401250e+04, 8.25842422e+04, 1.15007688e+05, 9.68401250e+04, 8.25842422e+04, 1.15007688e+05, 9.68401250e+04, 8.25842422e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.15008219e+05, 8.25828359e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     518743389), # 518.74MB, avg file size 518.74MB
  ("fsize_db",                        6547475897), # 6.55GB, avg file size 545.62MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_3000_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_1_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_1_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_1_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 399996, ],
    'CountWeighted'                                                                  : [ 3.96340312e+05, 3.96381125e+05, 3.96246500e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.96340312e+05, 3.96340312e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.70950000e+05, 3.70919875e+05, 3.70958250e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.70950000e+05, 3.65057812e+05, 3.76794875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.70950000e+05, 3.70950000e+05, ],
  }),
  ("nof_tree_events",                 399996),
  ("nof_db_events",                   399996),
  ("fsize_local",                     1722789667), # 1.72GB, avg file size 1.72GB
  ("fsize_db",                        22186460848), # 22.19GB, avg file size 1.85GB
  ("use_it",                          True),
  ("xsection",                        4.55695e-05),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_1_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToHHTo2B2VTo2L2Nu_node_SM_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_sm_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 388999, ],
    'CountWeighted'                                                                  : [ 3.88917562e+05, 3.88933844e+05, 3.88956062e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.97857125e+05, 4.69962156e+05, 4.43757281e+05, 4.12132719e+05, 3.88916781e+05, 3.67196125e+05, 3.47077469e+05, 3.27484438e+05, 3.09122500e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.97857312e+05, 3.09122406e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.77191688e+05, 3.77195000e+05, 3.77223344e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.77191688e+05, 3.74412125e+05, 3.79920125e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.82706875e+05, 4.55800125e+05, 4.30505125e+05, 3.99570875e+05, 3.77189812e+05, 3.56213125e+05, 3.36485812e+05, 3.17591375e+05, 2.99865719e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.82707031e+05, 2.99865625e+05, ],
  }),
  ("nof_tree_events",                 388999),
  ("nof_db_events",                   388999),
  ("fsize_local",                     1684463228), # 1.68GB, avg file size 1.68GB
  ("fsize_db",                        21257341288), # 21.26GB, avg file size 1.25GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_sm_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToHHTo2B2VTo2L2Nu_node_2_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_2_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99920750e+05, 3.99896188e+05, 3.99913469e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.19619906e+05, 4.78803688e+05, 4.42924188e+05, 4.34230938e+05, 3.99913000e+05, 3.69767250e+05, 3.68607062e+05, 3.39314125e+05, 3.13624344e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.19620469e+05, 3.13623969e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.86217000e+05, 3.86154062e+05, 3.86256906e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.86217000e+05, 3.83055750e+05, 3.89339562e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.01648812e+05, 4.62453188e+05, 4.27971375e+05, 4.19169031e+05, 3.86210844e+05, 3.57247875e+05, 3.55791500e+05, 3.27666188e+05, 3.02977719e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.01649375e+05, 3.02977344e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1863194554), # 1.86GB, avg file size 1.86GB
  ("fsize_db",                        23088598268), # 23.09GB, avg file size 1.36GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_2_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToHHTo2B2VTo2L2Nu_node_3_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_3_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 380000, ],
    'CountWeighted'                                                                  : [ 3.79987094e+05, 3.79938625e+05, 3.79927906e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.86417938e+05, 4.59049188e+05, 4.33324281e+05, 4.02701312e+05, 3.79984219e+05, 3.58622219e+05, 3.39153938e+05, 3.19942969e+05, 3.01944656e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.86417938e+05, 3.01944656e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.68403125e+05, 3.68351812e+05, 3.68386812e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.68403125e+05, 3.65666125e+05, 3.71091062e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.71483312e+05, 4.45078375e+05, 4.20247500e+05, 3.90319281e+05, 3.68400375e+05, 3.47786938e+05, 3.28713062e+05, 3.10190000e+05, 2.92811188e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.71483312e+05, 2.92811188e+05, ],
  }),
  ("nof_tree_events",                 380000),
  ("nof_db_events",                   380000),
  ("fsize_local",                     1652581125), # 1.65GB, avg file size 1.65GB
  ("fsize_db",                        20768532098), # 20.77GB, avg file size 1.22GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_3_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToHHTo2B2VTo2L2Nu_node_7_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_7_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 392999, ],
    'CountWeighted'                                                                  : [ 3.92988188e+05, 3.92955438e+05, 3.92949906e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.01190594e+05, 4.75874094e+05, 4.51525875e+05, 4.13935812e+05, 3.92988188e+05, 3.72834688e+05, 3.47913719e+05, 3.30263406e+05, 3.13307625e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.01190625e+05, 3.13307594e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.81547000e+05, 3.81492188e+05, 3.81551844e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.81547000e+05, 3.78817562e+05, 3.84219688e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.86493125e+05, 4.62037219e+05, 4.38498281e+05, 4.01785500e+05, 3.81547000e+05, 3.62065969e+05, 3.37691219e+05, 3.20642156e+05, 3.04253000e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.86493125e+05, 3.04253000e+05, ],
  }),
  ("nof_tree_events",                 392999),
  ("nof_db_events",                   392999),
  ("fsize_local",                     1670386242), # 1.67GB, avg file size 1.67GB
  ("fsize_db",                        21440735341), # 21.44GB, avg file size 1.13GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_7_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToHHTo2B2VTo2L2Nu_node_9_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_9_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 386999, ],
    'CountWeighted'                                                                  : [ 3.86970719e+05, 3.87034969e+05, 3.86950375e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.02560719e+05, 4.63310750e+05, 4.28627625e+05, 4.19856062e+05, 3.86970719e+05, 3.57904844e+05, 3.56284562e+05, 3.28278688e+05, 3.03580594e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.02580906e+05, 3.03561375e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.73626625e+05, 3.73656219e+05, 3.73629188e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.73626625e+05, 3.70549438e+05, 3.76666031e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.85101062e+05, 4.47362375e+05, 4.13999188e+05, 4.05248875e+05, 3.73626625e+05, 3.45673375e+05, 3.43873469e+05, 3.16952125e+05, 2.93190812e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.85121312e+05, 2.93171562e+05, ],
  }),
  ("nof_tree_events",                 386999),
  ("nof_db_events",                   386999),
  ("fsize_local",                     1819557376), # 1.82GB, avg file size 1.82GB
  ("fsize_db",                        22534822736), # 22.53GB, avg file size 1.19GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_9_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToHHTo2B2VTo2L2Nu_node_12_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_12_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 4.00046312e+05, 4.00023562e+05, 3.99942031e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.09928562e+05, 4.84450031e+05, 4.59890125e+05, 4.21060062e+05, 4.00046312e+05, 3.79661344e+05, 3.53841125e+05, 3.36073094e+05, 3.18990625e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.09928562e+05, 3.18990625e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.88458156e+05, 3.88425969e+05, 3.88424750e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.88458156e+05, 3.85695750e+05, 3.91167562e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.95080750e+05, 4.70464125e+05, 4.46719750e+05, 4.08785469e+05, 3.88458156e+05, 3.68776500e+05, 3.43515438e+05, 3.26354938e+05, 3.09836188e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.95080750e+05, 3.09836188e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1695517111), # 1.70GB, avg file size 1.70GB
  ("fsize_db",                        21561540290), # 21.56GB, avg file size 937.46MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_12_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToHHTo2B2VTo2L2Nu_node_cHHH0_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH0_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH0_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    30),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.76288750e+05, 3.76343906e+05, 3.76284188e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.35347781e+05, 4.27780844e+05, 4.22465859e+05, 3.84834062e+05, 3.76288781e+05, 3.69443703e+05, 3.41171469e+05, 3.32386141e+05, 3.24896109e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.50666969e+05, 3.17445297e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.76388000e+05, 3.76398094e+05, 5.35278031e+05, 3.76166156e+05, 3.75431188e+05, 2.32993953e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.56263574e+04, 2.56260039e+04, 3.64876992e+04, 2.56107188e+04, 2.56025283e+04, 1.58614351e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.67247875e+05, 3.67278734e+05, 3.67248750e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.67247875e+05, 3.65014000e+05, 3.69420484e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.24729750e+05, 4.17443078e+05, 4.12342203e+05, 3.75495125e+05, 3.67247859e+05, 3.60640047e+05, 3.32921172e+05, 3.24428750e+05, 3.17185844e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.39693359e+05, 3.09910391e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.67391219e+05, 3.67249109e+05, 5.22312312e+05, 3.67059156e+05, 3.66543359e+05, 2.27495133e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.50072109e+04, 2.49959551e+04, 3.55955098e+04, 2.49837705e+04, 2.49911562e+04, 1.54826509e+04, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1627768402), # 1.63GB, avg file size 813.88MB
  ("fsize_db",                        20709038606), # 20.71GB, avg file size 690.30MB
  ("use_it",                          True),
  ("xsection",                        0.00176969),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_cHHH0_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToHHTo2B2VTo2L2Nu_node_cHHH1_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH1_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH1_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    28),
  ("nof_events",                      {
    'Count'                                                                          : [ 395000, ],
    'CountWeighted'                                                                  : [ 3.54213125e+05, 3.54124508e+05, 3.54233422e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.03450781e+05, 3.96910062e+05, 3.92571219e+05, 3.62418344e+05, 3.54199469e+05, 3.47707812e+05, 3.25216031e+05, 3.16280477e+05, 3.08791477e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.20724203e+05, 2.99384297e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.54277367e+05, 3.54263438e+05, 5.03994094e+05, 3.54069531e+05, 3.52938875e+05, 2.18786742e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.18016636e+04, 1.18034805e+04, 1.68078340e+04, 1.17972598e+04, 1.17730210e+04, 7.28837109e+03, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.45246625e+05, 3.45158969e+05, 3.45285062e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.45246625e+05, 3.43055688e+05, 3.47382344e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.93098109e+05, 3.86819719e+05, 3.82675953e+05, 3.53164797e+05, 3.45234609e+05, 3.38991797e+05, 3.16940859e+05, 3.08313328e+05, 3.01081500e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.09957562e+05, 2.91899641e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.45372391e+05, 3.45198688e+05, 4.91216203e+05, 3.45049328e+05, 3.44194438e+05, 2.13334109e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.15026519e+04, 1.14992627e+04, 1.63784614e+04, 1.14946641e+04, 1.14788291e+04, 7.10537622e+03, ],
  }),
  ("nof_tree_events",                 395000),
  ("nof_db_events",                   395000),
  ("fsize_local",                     1650983895), # 1.65GB, avg file size 825.49MB
  ("fsize_db",                        20592180227), # 20.59GB, avg file size 735.44MB
  ("use_it",                          True),
  ("xsection",                        0.00078807),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_cHHH1_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToHHTo2B2VTo2L2Nu_node_cHHH2p45_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH2p45_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH2p45_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    36),
  ("nof_events",                      {
    'Count'                                                                          : [ 397398, ],
    'CountWeighted'                                                                  : [ 3.42477109e+05, 3.42574086e+05, 3.42415969e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.90397922e+05, 3.84923094e+05, 3.81417531e+05, 3.49518367e+05, 3.42466070e+05, 3.36939312e+05, 3.12987641e+05, 3.05239781e+05, 2.98716047e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.11362156e+05, 2.85816969e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.42631852e+05, 3.42436562e+05, 4.88491375e+05, 3.42221094e+05, 3.41871867e+05, 2.10976039e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 5.23324561e+03, 5.23117969e+03, 7.46394116e+03, 5.22751978e+03, 5.22800989e+03, 3.22605444e+03, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.33818250e+05, 3.33912016e+05, 3.33752328e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.33818250e+05, 3.31701547e+05, 3.35878336e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.80363812e+05, 3.75134516e+05, 3.71810797e+05, 3.40586031e+05, 3.33808125e+05, 3.28506211e+05, 3.05017281e+05, 2.97554531e+05, 2.91270484e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.00825500e+05, 2.78681398e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.34022172e+05, 3.33679266e+05, 4.76092500e+05, 3.33507172e+05, 3.33414711e+05, 2.05747648e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 5.10076648e+03, 5.09611743e+03, 7.27289697e+03, 5.09327051e+03, 5.09787769e+03, 3.14561035e+03, ],
  }),
  ("nof_tree_events",                 397398),
  ("nof_db_events",                   397398),
  ("fsize_local",                     1663681586), # 1.66GB, avg file size 831.84MB
  ("fsize_db",                        20851244387), # 20.85GB, avg file size 579.20MB
  ("use_it",                          True),
  ("xsection",                        0.00033379),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_cHHH2p45_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToHHTo2B2VTo2L2Nu_node_cHHH5_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH5_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH5_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    31),
  ("nof_events",                      {
    'Count'                                                                          : [ 399999, ],
    'CountWeighted'                                                                  : [ 3.93670203e+05, 3.93695875e+05, 3.93632406e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.71544062e+05, 4.62735609e+05, 4.55960891e+05, 4.01436969e+05, 3.93667297e+05, 3.87064359e+05, 3.45628289e+05, 3.38736938e+05, 3.32499500e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.85902547e+05, 3.25794719e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.93584141e+05, 3.93469000e+05, 5.59683719e+05, 3.93746953e+05, 3.93156281e+05, 2.44049562e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.20949727e+04, 3.20933887e+04, 4.56679043e+04, 3.21089736e+04, 3.20844834e+04, 1.99045435e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.85088844e+05, 3.85100438e+05, 3.85074203e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.85088844e+05, 3.82913500e+05, 3.87188891e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.61052594e+05, 4.52562234e+05, 4.46043141e+05, 3.92586281e+05, 3.85083016e+05, 3.78719656e+05, 3.38061156e+05, 3.31408891e+05, 3.25379703e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.75124328e+05, 3.18809359e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.85066156e+05, 3.84765016e+05, 5.47369812e+05, 3.85096453e+05, 3.84778844e+05, 2.38877031e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.13968535e+04, 3.13801084e+04, 4.46583730e+04, 3.14004082e+04, 3.13975723e+04, 1.94805171e+04, ],
  }),
  ("nof_tree_events",                 399999),
  ("nof_db_events",                   399999),
  ("fsize_local",                     1531570236), # 1.53GB, avg file size 765.79MB
  ("fsize_db",                        20133733845), # 20.13GB, avg file size 649.48MB
  ("use_it",                          True),
  ("xsection",                        0.00232827),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_cHHH5_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToHHTo2B2WToLNu2J_node_SM_TuneCP5_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_sm_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    30),
  ("nof_events",                      {
    'Count'                                                                          : [ 779989, ],
    'CountWeighted'                                                                  : [ 7.79847188e+05, 7.79874469e+05, 7.79932312e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 9.98358094e+05, 9.42384844e+05, 8.89795594e+05, 8.26467750e+05, 7.79847188e+05, 7.36294812e+05, 6.96016078e+05, 6.56689219e+05, 6.19854281e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.98358281e+05, 6.19854094e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 7.56271969e+05, 7.56263844e+05, 7.56337188e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 7.56271969e+05, 7.50652812e+05, 7.61777469e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 9.67858719e+05, 9.13898594e+05, 8.63164125e+05, 8.01173000e+05, 7.56271969e+05, 7.14216828e+05, 6.74680391e+05, 6.36783406e+05, 6.01240344e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.67858906e+05, 6.01240125e+05, ],
  }),
  ("nof_tree_events",                 779989),
  ("nof_db_events",                   779989),
  ("fsize_local",                     3514656195), # 3.51GB, avg file size 1.76GB
  ("fsize_db",                        43860671206), # 43.86GB, avg file size 1.46GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_sm_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToHHTo2B2VLNu2J_node_cHHH0_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH0_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH0_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    38),
  ("nof_events",                      {
    'Count'                                                                          : [ 392598, ],
    'CountWeighted'                                                                  : [ 3.69633812e+05, 3.69565312e+05, 3.69689625e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.27662875e+05, 4.20163875e+05, 4.14877453e+05, 3.78050531e+05, 3.69633828e+05, 3.62850172e+05, 3.35214891e+05, 3.26555734e+05, 3.19164531e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.42923469e+05, 3.11613078e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.69663906e+05, 3.69478000e+05, 5.35366609e+05, 3.69551656e+05, 3.69381109e+05, 2.20768297e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.51464727e+04, 2.51289736e+04, 3.64700322e+04, 2.51355840e+04, 2.51804082e+04, 1.50147832e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.60865336e+05, 3.60783203e+05, 3.60938445e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.60865336e+05, 3.58676453e+05, 3.62980156e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.17355828e+05, 4.10140719e+05, 4.05069281e+05, 3.68990000e+05, 3.60865328e+05, 3.54323094e+05, 3.27209359e+05, 3.18842125e+05, 3.11696453e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.32276938e+05, 3.04312195e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.60943406e+05, 3.60602484e+05, 5.22567984e+05, 3.60724719e+05, 3.60755484e+05, 2.15631492e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.45479092e+04, 2.45197939e+04, 3.55906602e+04, 2.45295176e+04, 2.45872969e+04, 1.46619360e+04, ],
  }),
  ("nof_tree_events",                 392598),
  ("nof_db_events",                   392598),
  ("fsize_local",                     1664223575), # 1.66GB, avg file size 832.11MB
  ("fsize_db",                        20577112946), # 20.58GB, avg file size 541.50MB
  ("use_it",                          True),
  ("xsection",                        0.00732418),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_cHHH0_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToHHTo2B2VLNu2J_node_cHHH1_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH1_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH1_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    28),
  ("nof_events",                      {
    'Count'                                                                          : [ 399994, ],
    'CountWeighted'                                                                  : [ 3.57852594e+05, 3.57917406e+05, 3.57791766e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.07371891e+05, 4.00921875e+05, 3.96687922e+05, 3.66072781e+05, 3.57834109e+05, 3.51425891e+05, 3.28577211e+05, 3.19637148e+05, 3.12150914e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.25003438e+05, 3.02535141e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.57715422e+05, 3.57705547e+05, 5.17772141e+05, 3.58053312e+05, 3.56550219e+05, 2.13472109e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.19581738e+04, 1.19601646e+04, 1.73268379e+04, 1.19628911e+04, 1.19368921e+04, 7.13659814e+03, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.48831555e+05, 3.48865617e+05, 3.48792109e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.48831555e+05, 3.46603625e+05, 3.50994750e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.96963109e+05, 3.90767469e+05, 3.86721641e+05, 3.56754797e+05, 3.48816562e+05, 3.42635742e+05, 3.20232109e+05, 3.11598016e+05, 3.04367781e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.14160344e+05, 2.94993359e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.48739203e+05, 3.48565250e+05, 5.04707453e+05, 3.48967297e+05, 3.47778688e+05, 2.08173797e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.16540186e+04, 1.16508281e+04, 1.68832988e+04, 1.16556094e+04, 1.16383564e+04, 6.95726685e+03, ],
  }),
  ("nof_tree_events",                 399994),
  ("nof_db_events",                   399994),
  ("fsize_local",                     1747307012), # 1.75GB, avg file size 873.65MB
  ("fsize_db",                        21031852916), # 21.03GB, avg file size 751.14MB
  ("use_it",                          True),
  ("xsection",                        0.00326156),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_cHHH1_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToHHTo2B2VLNu2J_node_cHHH2p45_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH2p45_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH2p45_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    55),
  ("nof_events",                      {
    'Count'                                                                          : [ 399996, ],
    'CountWeighted'                                                                  : [ 3.45212250e+05, 3.45175531e+05, 3.45247047e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.93622062e+05, 3.88258328e+05, 3.84868547e+05, 3.52172203e+05, 3.45204227e+05, 3.39752977e+05, 3.15192914e+05, 3.07496977e+05, 3.01025609e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.14538781e+05, 2.88267961e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.45196250e+05, 3.45030859e+05, 5.00197797e+05, 3.45229133e+05, 3.44111703e+05, 2.05407789e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 5.25208862e+03, 5.24794116e+03, 7.62505273e+03, 5.25381836e+03, 5.25221558e+03, 3.12622278e+03, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.36636961e+05, 3.36580469e+05, 3.36681695e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.36636961e+05, 3.34520297e+05, 3.38687203e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.83694547e+05, 3.78573156e+05, 3.75363297e+05, 3.43325547e+05, 3.36628070e+05, 3.31402344e+05, 3.07297258e+05, 2.99885953e+05, 2.93652781e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.04107578e+05, 2.81207969e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.36674109e+05, 3.36359391e+05, 4.87681688e+05, 3.36594281e+05, 3.35709391e+05, 2.00413930e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 5.12065820e+03, 5.11410889e+03, 7.43218359e+03, 5.12067578e+03, 5.12277600e+03, 3.04906921e+03, ],
  }),
  ("nof_tree_events",                 399996),
  ("nof_db_events",                   399996),
  ("fsize_local",                     1743320043), # 1.74GB, avg file size 871.66MB
  ("fsize_db",                        21469157723), # 21.47GB, avg file size 390.35MB
  ("use_it",                          True),
  ("xsection",                        0.00138144),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_cHHH2p45_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToHHTo2B2VLNu2J_node_cHHH5_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH5_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH5_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    44),
  ("nof_events",                      {
    'Count'                                                                          : [ 395996, ],
    'CountWeighted'                                                                  : [ 3.89639312e+05, 3.89667266e+05, 3.89660703e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.66538469e+05, 4.57767453e+05, 4.51023375e+05, 3.97406953e+05, 3.89630938e+05, 3.83080891e+05, 3.42322133e+05, 3.35449047e+05, 3.29231984e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.80859234e+05, 3.22473609e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.89741656e+05, 3.89582281e+05, 5.64375469e+05, 3.89537875e+05, 3.89737938e+05, 2.33066141e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.17732773e+04, 3.17637461e+04, 4.60603711e+04, 3.17594902e+04, 3.18175742e+04, 1.89986855e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.81528969e+05, 3.81544109e+05, 3.81549031e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.81528969e+05, 3.79440922e+05, 3.83522281e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.56601703e+05, 4.48137953e+05, 4.41639109e+05, 3.89025422e+05, 3.81519547e+05, 3.75185516e+05, 3.35156680e+05, 3.28513109e+05, 3.22496656e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.70655562e+05, 3.15865375e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.81676047e+05, 3.81342000e+05, 5.52549781e+05, 3.81354719e+05, 3.81839109e+05, 2.28334938e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.11116270e+04, 3.10877051e+04, 4.50892891e+04, 3.10881035e+04, 3.11687100e+04, 1.86106465e+04, ],
  }),
  ("nof_tree_events",                 395996),
  ("nof_db_events",                   395996),
  ("fsize_local",                     1553998340), # 1.55GB, avg file size 777.00MB
  ("fsize_db",                        20146374153), # 20.15GB, avg file size 457.87MB
  ("use_it",                          True),
  ("xsection",                        0.00963593),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_cHHH5_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2BLNu2J_M-250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_250_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_250_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 399998, ],
    'CountWeighted'                                                                  : [ 3.99962125e+05, 3.99992000e+05, 3.99977766e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99962125e+05, 3.99962125e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.93141266e+05, 3.93141516e+05, 3.93172016e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.93141266e+05, 3.91339875e+05, 3.94838984e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.93141266e+05, 3.93141266e+05, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     1415344702), # 1.42GB, avg file size 707.67MB
  ("fsize_db",                        20824958609), # 20.82GB, avg file size 991.66MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_250_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2BLNu2J_M-260_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_260_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_260_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 399997, ],
    'CountWeighted'                                                                  : [ 3.99970906e+05, 3.99970344e+05, 3.99974766e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.06215375e+05, 3.99970281e+05, 3.91160922e+05, 4.06215375e+05, 3.99970281e+05, 3.91160922e+05, 4.06215375e+05, 3.99970281e+05, 3.91160922e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.06216250e+05, 3.91160031e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.92839688e+05, 3.92815609e+05, 3.92865875e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.92839688e+05, 3.90968656e+05, 3.94607281e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.98934000e+05, 3.92837844e+05, 3.84221000e+05, 3.98934000e+05, 3.92837844e+05, 3.84221000e+05, 3.98934000e+05, 3.92837844e+05, 3.84221000e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.98934750e+05, 3.84220250e+05, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     1426958195), # 1.43GB, avg file size 713.48MB
  ("fsize_db",                        20162954542), # 20.16GB, avg file size 1.26GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_260_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2BLNu2J_M-270_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_270_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_270_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                                          : [ 399997, ],
    'CountWeighted'                                                                  : [ 3.99937875e+05, 3.99938594e+05, 3.99962812e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.07499078e+05, 3.99937875e+05, 3.90141703e+05, 4.07499078e+05, 3.99937875e+05, 3.90141703e+05, 4.07499078e+05, 3.99937875e+05, 3.90141703e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.07499078e+05, 3.90141703e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.92427953e+05, 3.92408688e+05, 3.92462359e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.92427953e+05, 3.90473703e+05, 3.94284141e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.99793844e+05, 3.92427953e+05, 3.82840531e+05, 3.99793844e+05, 3.92427953e+05, 3.82840531e+05, 3.99793844e+05, 3.92427953e+05, 3.82840531e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.99793844e+05, 3.82840531e+05, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     1448620583), # 1.45GB, avg file size 724.31MB
  ("fsize_db",                        20058005605), # 20.06GB, avg file size 911.73MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_270_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2BLNu2J_M-280_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_280_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_280_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                                          : [ 399994, ],
    'CountWeighted'                                                                  : [ 3.99964984e+05, 3.99952172e+05, 3.99954984e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99964984e+05, 3.99964984e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.92105469e+05, 3.92081016e+05, 3.92107547e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.92105469e+05, 3.90078156e+05, 3.94036109e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.92105469e+05, 3.92105469e+05, ],
  }),
  ("nof_tree_events",                 399994),
  ("nof_db_events",                   399994),
  ("fsize_local",                     1483406517), # 1.48GB, avg file size 741.70MB
  ("fsize_db",                        21046001413), # 21.05GB, avg file size 915.04MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_280_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2BLNu2J_M-300_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_300_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_300_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 291995, ],
    'CountWeighted'                                                                  : [ 2.92000512e+05, 2.91958320e+05, 2.91978684e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.00031621e+05, 2.92000512e+05, 2.82781539e+05, 3.00031621e+05, 2.92000512e+05, 2.82781539e+05, 3.00031621e+05, 2.92000512e+05, 2.82781539e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.00031621e+05, 2.82781539e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.85802293e+05, 2.85756957e+05, 2.85802082e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.85802293e+05, 2.84225730e+05, 2.87311457e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.93629336e+05, 2.85802293e+05, 2.76817148e+05, 2.93629336e+05, 2.85802293e+05, 2.76817148e+05, 2.93629336e+05, 2.85802293e+05, 2.76817148e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.93629336e+05, 2.76817148e+05, ],
  }),
  ("nof_tree_events",                 291995),
  ("nof_db_events",                   291995),
  ("fsize_local",                     1108285213), # 1.11GB, avg file size 554.14MB
  ("fsize_db",                        14928343398), # 14.93GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_300_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2BLNu2J_M-320_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_320_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_320_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 299997, ],
    'CountWeighted'                                                                  : [ 2.99980359e+05, 2.99968918e+05, 2.99987453e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.09808297e+05, 2.99980359e+05, 2.89294371e+05, 3.09808297e+05, 2.99980359e+05, 2.89294371e+05, 3.09808297e+05, 2.99980359e+05, 2.89294371e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.09808297e+05, 2.89294371e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93143602e+05, 2.93131715e+05, 2.93144449e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93143602e+05, 2.91426082e+05, 2.94794715e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.02703535e+05, 2.93143602e+05, 2.82739242e+05, 3.02703535e+05, 2.93143602e+05, 2.82739242e+05, 3.02703535e+05, 2.93143602e+05, 2.82739242e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.02703535e+05, 2.82739242e+05, ],
  }),
  ("nof_tree_events",                 299997),
  ("nof_db_events",                   299997),
  ("fsize_local",                     1172978226), # 1.17GB, avg file size 586.49MB
  ("fsize_db",                        15434788839), # 15.43GB, avg file size 1.40GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_320_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2BLNu2J_M-350_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_350_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_350_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 289997, ],
    'CountWeighted'                                                                  : [ 2.89994906e+05, 2.89966801e+05, 2.89976902e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.01577766e+05, 2.89994906e+05, 2.78038848e+05, 3.01577766e+05, 2.89994906e+05, 2.78038848e+05, 3.01577766e+05, 2.89994906e+05, 2.78038848e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.01577766e+05, 2.78038848e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.82802789e+05, 2.82758207e+05, 2.82820168e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.82802789e+05, 2.81024086e+05, 2.84522125e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.94056105e+05, 2.82802789e+05, 2.71186945e+05, 2.94056105e+05, 2.82802789e+05, 2.71186945e+05, 2.94056105e+05, 2.82802789e+05, 2.71186945e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.94056105e+05, 2.71186945e+05, ],
  }),
  ("nof_tree_events",                 289997),
  ("nof_db_events",                   289997),
  ("fsize_local",                     1178179986), # 1.18GB, avg file size 589.09MB
  ("fsize_db",                        15283779028), # 15.28GB, avg file size 849.10MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_350_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2BLNu2J_M-400_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_400_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_400_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 286998, ],
    'CountWeighted'                                                                  : [ 2.86980137e+05, 2.87011305e+05, 2.86981410e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.01460582e+05, 2.86980137e+05, 2.72894684e+05, 3.01460582e+05, 2.86980137e+05, 2.72894684e+05, 3.01460582e+05, 2.86980137e+05, 2.72894684e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.01460582e+05, 2.72894684e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.79114219e+05, 2.79116480e+05, 2.79126156e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.79114219e+05, 2.77201324e+05, 2.80974012e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.93145801e+05, 2.79114219e+05, 2.65462520e+05, 2.93145801e+05, 2.79114219e+05, 2.65462520e+05, 2.93145801e+05, 2.79114219e+05, 2.65462520e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.93145801e+05, 2.65462520e+05, ],
  }),
  ("nof_tree_events",                 286998),
  ("nof_db_events",                   286998),
  ("fsize_local",                     1229424488), # 1.23GB, avg file size 614.71MB
  ("fsize_db",                        15373371640), # 15.37GB, avg file size 1.10GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_400_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2BLNu2J_M-450_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_450_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_450_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 267996, ],
    'CountWeighted'                                                                  : [ 2.67941320e+05, 2.67952941e+05, 2.67970160e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.83864330e+05, 2.67940582e+05, 2.53005387e+05, 2.83864330e+05, 2.67940582e+05, 2.53005387e+05, 2.83864330e+05, 2.67940582e+05, 2.53005387e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.83864330e+05, 2.53005324e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.59934746e+05, 2.59923449e+05, 2.59967277e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.59934746e+05, 2.58017906e+05, 2.61808395e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.75318104e+05, 2.59933375e+05, 2.45487514e+05, 2.75318104e+05, 2.59933375e+05, 2.45487514e+05, 2.75318104e+05, 2.59933375e+05, 2.45487514e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.75318104e+05, 2.45487467e+05, ],
  }),
  ("nof_tree_events",                 267996),
  ("nof_db_events",                   267996),
  ("fsize_local",                     1199905225), # 1.20GB, avg file size 599.95MB
  ("fsize_db",                        14616404259), # 14.62GB, avg file size 913.53MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_450_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2BLNu2J_M-500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_500_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_500_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 195997, ],
    'CountWeighted'                                                                  : [ 1.95988312e+05, 1.95977984e+05, 1.95992781e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.09133250e+05, 1.95988312e+05, 1.83899438e+05, 2.09133250e+05, 1.95988312e+05, 1.83899438e+05, 2.09133250e+05, 1.95988312e+05, 1.83899438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.09133438e+05, 1.83899234e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.89711219e+05, 1.89698344e+05, 1.89717016e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.89711219e+05, 1.88227500e+05, 1.91166750e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.02388609e+05, 1.89711219e+05, 1.78043625e+05, 2.02388609e+05, 1.89711219e+05, 1.78043625e+05, 2.02388609e+05, 1.89711219e+05, 1.78043625e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.02388703e+05, 1.78043500e+05, ],
  }),
  ("nof_tree_events",                 195997),
  ("nof_db_events",                   195997),
  ("fsize_local",                     909412114), # 909.41MB, avg file size 909.41MB
  ("fsize_db",                        10942029158), # 10.94GB, avg file size 683.88MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_500_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2BLNu2J_M-550_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_550_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_550_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 191998, ],
    'CountWeighted'                                                                  : [ 1.91957359e+05, 1.91961328e+05, 1.91966609e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.06135750e+05, 1.91957359e+05, 1.79118094e+05, 2.06135750e+05, 1.91957359e+05, 1.79118094e+05, 2.06135750e+05, 1.91957359e+05, 1.79118094e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.06135750e+05, 1.79118094e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.85552188e+05, 1.85531688e+05, 1.85576625e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.85552188e+05, 1.84049750e+05, 1.87030641e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.99206438e+05, 1.85552188e+05, 1.73175250e+05, 1.99206438e+05, 1.85552188e+05, 1.73175250e+05, 1.99206438e+05, 1.85552188e+05, 1.73175250e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.99206438e+05, 1.73175250e+05, ],
  }),
  ("nof_tree_events",                 191998),
  ("nof_db_events",                   191998),
  ("fsize_local",                     921249507), # 921.25MB, avg file size 921.25MB
  ("fsize_db",                        10846981495), # 10.85GB, avg file size 723.13MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_550_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2BLNu2J_M-600_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_600_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_600_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 199996, ],
    'CountWeighted'                                                                  : [ 1.99966609e+05, 1.99968719e+05, 1.99968234e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.15977156e+05, 1.99966609e+05, 1.85674625e+05, 2.15977156e+05, 1.99966609e+05, 1.85674625e+05, 2.15977156e+05, 1.99966609e+05, 1.85674625e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.15977281e+05, 1.85674516e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92959875e+05, 1.92957875e+05, 1.92962062e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92959875e+05, 1.91328781e+05, 1.94567656e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.08346750e+05, 1.92959875e+05, 1.79198094e+05, 2.08346750e+05, 1.92959875e+05, 1.79198094e+05, 2.08346750e+05, 1.92959875e+05, 1.79198094e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.08346844e+05, 1.79197969e+05, ],
  }),
  ("nof_tree_events",                 199996),
  ("nof_db_events",                   199996),
  ("fsize_local",                     982514203), # 982.51MB, avg file size 982.51MB
  ("fsize_db",                        11423055023), # 11.42GB, avg file size 878.70MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_600_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2BLNu2J_M-650_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_650_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_650_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 195997, ],
    'CountWeighted'                                                                  : [ 1.95961172e+05, 1.95945250e+05, 1.95980484e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.12690094e+05, 1.95961172e+05, 1.81122500e+05, 2.12690094e+05, 1.95961172e+05, 1.81122500e+05, 2.12690094e+05, 1.95961172e+05, 1.81122500e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.12690234e+05, 1.81122359e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.88847453e+05, 1.88827844e+05, 1.88876234e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.88847453e+05, 1.87200797e+05, 1.90471812e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.04917203e+05, 1.88847453e+05, 1.74582156e+05, 2.04917203e+05, 1.88847453e+05, 1.74582156e+05, 2.04917203e+05, 1.88847453e+05, 1.74582156e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.04917234e+05, 1.74582125e+05, ],
  }),
  ("nof_tree_events",                 195997),
  ("nof_db_events",                   195997),
  ("fsize_local",                     981550833), # 981.55MB, avg file size 981.55MB
  ("fsize_db",                        11297009208), # 11.30GB, avg file size 941.42MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_650_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2BLNu2J_M-700_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_700_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_700_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 199998, ],
    'CountWeighted'                                                                  : [ 1.99975094e+05, 1.99976219e+05, 1.99964188e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.18036844e+05, 1.99975094e+05, 1.84068031e+05, 2.18036844e+05, 1.99975094e+05, 1.84068031e+05, 2.18036844e+05, 1.99975094e+05, 1.84068031e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.18036953e+05, 1.84067906e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92498062e+05, 1.92476500e+05, 1.92517250e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92498062e+05, 1.90777828e+05, 1.94196438e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.09834406e+05, 1.92498062e+05, 1.77223406e+05, 2.09834406e+05, 1.92498062e+05, 1.77223406e+05, 2.09834406e+05, 1.92498062e+05, 1.77223406e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.09834422e+05, 1.77223375e+05, ],
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     1014766076), # 1.01GB, avg file size 1.01GB
  ("fsize_db",                        11616106982), # 11.62GB, avg file size 1.16GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_700_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2BLNu2J_M-750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_750_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_750_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 199996, ],
    'CountWeighted'                                                                  : [ 1.99962828e+05, 1.99956156e+05, 1.99966766e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99962828e+05, 1.99962828e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92421750e+05, 1.92408875e+05, 1.92432734e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92421750e+05, 1.90686500e+05, 1.94135031e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.92421750e+05, 1.92421750e+05, ],
  }),
  ("nof_tree_events",                 199996),
  ("nof_db_events",                   199996),
  ("fsize_local",                     1031714322), # 1.03GB, avg file size 1.03GB
  ("fsize_db",                        12183863811), # 12.18GB, avg file size 761.49MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_750_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2BLNu2J_M-800_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_800_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_800_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 199997, ],
    'CountWeighted'                                                                  : [ 1.99981703e+05, 1.99985000e+05, 1.99988766e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99981703e+05, 1.99981703e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92264500e+05, 1.92253000e+05, 1.92279125e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92264500e+05, 1.90498922e+05, 1.94010281e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.92264500e+05, 1.92264500e+05, ],
  }),
  ("nof_tree_events",                 199997),
  ("nof_db_events",                   199997),
  ("fsize_local",                     1039086076), # 1.04GB, avg file size 1.04GB
  ("fsize_db",                        12250384345), # 12.25GB, avg file size 942.34MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_800_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2BLNu2J_M-850_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_850_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_850_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 191998, ],
    'CountWeighted'                                                                  : [ 1.91986312e+05, 1.91980406e+05, 1.91984672e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.91986312e+05, 1.91986312e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.84492062e+05, 1.84470250e+05, 1.84512719e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.84492062e+05, 1.82785359e+05, 1.86181734e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.84492062e+05, 1.84492062e+05, ],
  }),
  ("nof_tree_events",                 191998),
  ("nof_db_events",                   191998),
  ("fsize_local",                     1004090974), # 1.00GB, avg file size 1.00GB
  ("fsize_db",                        11782943840), # 11.78GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_850_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2BLNu2J_M-900_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_900_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_900_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99665547e+04, 9.99720859e+04, 9.99823438e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.10646531e+05, 9.99665547e+04, 9.08051562e+04, 1.10646531e+05, 9.99665547e+04, 9.08051562e+04, 1.10646531e+05, 9.99665547e+04, 9.08051562e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.10646531e+05, 9.08051562e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.60206484e+04, 9.60092344e+04, 9.60413438e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.60206484e+04, 9.51231875e+04, 9.69096328e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.06251156e+05, 9.60206484e+04, 8.72391719e+04, 1.06251156e+05, 9.60206484e+04, 8.72391719e+04, 1.06251156e+05, 9.60206484e+04, 8.72391719e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.06251156e+05, 8.72391719e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     523179941), # 523.18MB, avg file size 523.18MB
  ("fsize_db",                        6068458934), # 6.07GB, avg file size 505.70MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_900_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2BLNu2J_M-1000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1000_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_1000_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99689375e+04, 9.99744062e+04, 9.99827969e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.11344625e+05, 9.99664844e+04, 9.03284688e+04, 1.11344625e+05, 9.99664844e+04, 9.03284688e+04, 1.11344625e+05, 9.99664844e+04, 9.03284688e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.11344625e+05, 9.03284688e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.58593438e+04, 9.58623984e+04, 9.58704531e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.58593438e+04, 9.49316641e+04, 9.67808906e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.06738062e+05, 9.58575781e+04, 8.66305469e+04, 1.06738062e+05, 9.58575781e+04, 8.66305469e+04, 1.06738062e+05, 9.58575781e+04, 8.66305469e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.06738062e+05, 8.66305469e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     527602602), # 527.60MB, avg file size 527.60MB
  ("fsize_db",                        6045424835), # 6.05GB, avg file size 863.63MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1000_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2BLNu2J_M-1250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1250_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_1250_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 9.99793906e+04, 9.99776875e+04, 9.99908359e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99793906e+04, 9.99793906e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.55943359e+04, 9.55943750e+04, 9.56019922e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.55943359e+04, 9.46170156e+04, 9.65666094e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.55943359e+04, 9.55943359e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     533702749), # 533.70MB, avg file size 533.70MB
  ("fsize_db",                        6423289763), # 6.42GB, avg file size 535.27MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1250_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2BLNu2J_M-1500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1500_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_1500_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99625938e+04, 9.99614688e+04, 9.99570156e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.13902133e+05, 9.99618828e+04, 8.85175625e+04, 1.13902133e+05, 9.99618828e+04, 8.85175625e+04, 1.13902133e+05, 9.99618828e+04, 8.85175625e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.13902133e+05, 8.85175547e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.55819688e+04, 9.55715312e+04, 9.55849219e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.55819688e+04, 9.46081016e+04, 9.65502812e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.08890172e+05, 9.55812188e+04, 8.46537266e+04, 1.08890172e+05, 9.55812188e+04, 8.46537266e+04, 1.08890172e+05, 9.55812188e+04, 8.46537266e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.08890172e+05, 8.46537188e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     524921664), # 524.92MB, avg file size 524.92MB
  ("fsize_db",                        6208129873), # 6.21GB, avg file size 689.79MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1500_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2BLNu2J_M-1750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1750_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_1750_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 9.99545625e+04, 9.99404844e+04, 9.99442500e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99545625e+04, 9.99545625e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.54489531e+04, 9.54336875e+04, 9.54440312e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.54489531e+04, 9.44528047e+04, 9.64406406e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.54489531e+04, 9.54489531e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     526857535), # 526.86MB, avg file size 526.86MB
  ("fsize_db",                        6405123519), # 6.41GB, avg file size 800.64MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1750_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2BLNu2J_M-2000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_2000_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_2000_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 9.99312422e+04, 9.99449141e+04, 9.99362969e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.15709969e+05, 9.99312422e+04, 8.72172969e+04, 1.15709969e+05, 9.99312422e+04, 8.72172969e+04, 1.15709969e+05, 9.99312422e+04, 8.72172969e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.15711531e+05, 8.72157188e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.53743828e+04, 9.53773594e+04, 9.53851875e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.53743828e+04, 9.43700000e+04, 9.63747734e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.10413461e+05, 9.53743828e+04, 8.32468125e+04, 1.10413461e+05, 9.53743828e+04, 8.32468125e+04, 1.10413461e+05, 9.53743828e+04, 8.32468125e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.10415016e+05, 8.32452500e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     522581007), # 522.58MB, avg file size 522.58MB
  ("fsize_db",                        6209129498), # 6.21GB, avg file size 1.24GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_2000_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2BLNu2J_M-2500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_2500_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_2500_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 96000, ],
    'CountWeighted'                                                                  : [ 9.58981484e+04, 9.58825938e+04, 9.59009375e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.58981484e+04, 9.58981484e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.13431172e+04, 9.13429062e+04, 9.13375469e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.13431172e+04, 9.03495781e+04, 9.23358438e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.13431172e+04, 9.13431172e+04, ],
  }),
  ("nof_tree_events",                 96000),
  ("nof_db_events",                   96000),
  ("fsize_local",                     503835275), # 503.84MB, avg file size 503.84MB
  ("fsize_db",                        6368497358), # 6.37GB, avg file size 578.95MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_2500_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2BLNu2J_M-3000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_3000_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_3000_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 99997, ],
    'CountWeighted'                                                                  : [ 9.98015312e+04, 9.98119531e+04, 9.97953281e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.98015312e+04, 9.98015312e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.50696094e+04, 9.50639375e+04, 9.50793438e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.50696094e+04, 9.40458672e+04, 9.60954219e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.50696094e+04, 9.50696094e+04, ],
  }),
  ("nof_tree_events",                 99997),
  ("nof_db_events",                   99997),
  ("fsize_local",                     525356351), # 525.36MB, avg file size 525.36MB
  ("fsize_db",                        6731398004), # 6.73GB, avg file size 517.80MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_3000_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2BLNu2J_M-250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_250_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_250_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 399998, ],
    'CountWeighted'                                                                  : [ 3.99991172e+05, 3.99978078e+05, 3.99968062e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.04896359e+05, 3.99987891e+05, 3.92236016e+05, 4.04896359e+05, 3.99987891e+05, 3.92236016e+05, 4.04896359e+05, 3.99987891e+05, 3.92236016e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.04896359e+05, 3.92236016e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.92743594e+05, 3.92726984e+05, 3.92738047e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.92743594e+05, 3.90854109e+05, 3.94528312e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.97527797e+05, 3.92740172e+05, 3.85161312e+05, 3.97527797e+05, 3.92740172e+05, 3.85161312e+05, 3.97527797e+05, 3.92740172e+05, 3.85161312e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.97527797e+05, 3.85161312e+05, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     1430436154), # 1.43GB, avg file size 715.22MB
  ("fsize_db",                        19988532039), # 19.99GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_250_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2BLNu2J_M-260_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_260_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_260_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 376000, ],
    'CountWeighted'                                                                  : [ 3.75997164e+05, 3.76010523e+05, 3.75987695e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.81862484e+05, 3.75997164e+05, 3.67698359e+05, 3.81862484e+05, 3.75997164e+05, 3.67698359e+05, 3.81862484e+05, 3.75997164e+05, 3.67698359e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.81862484e+05, 3.67698359e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.68947469e+05, 3.68945641e+05, 3.68952555e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.68947469e+05, 3.67118414e+05, 3.70683070e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.74668117e+05, 3.68947469e+05, 3.60839469e+05, 3.74668117e+05, 3.68947469e+05, 3.60839469e+05, 3.74668117e+05, 3.68947469e+05, 3.60839469e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.74668117e+05, 3.60839469e+05, ],
  }),
  ("nof_tree_events",                 376000),
  ("nof_db_events",                   376000),
  ("fsize_local",                     1368975545), # 1.37GB, avg file size 684.49MB
  ("fsize_db",                        19062554246), # 19.06GB, avg file size 1.06GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_260_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2BLNu2J_M-270_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_270_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_270_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    27),
  ("nof_events",                      {
    'Count'                                                                          : [ 399999, ],
    'CountWeighted'                                                                  : [ 3.99974969e+05, 3.99981453e+05, 3.99982781e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.07504812e+05, 3.99971781e+05, 3.90157922e+05, 4.07504812e+05, 3.99971781e+05, 3.90157922e+05, 4.07504812e+05, 3.99971781e+05, 3.90157922e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.07504812e+05, 3.90157922e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.92031953e+05, 3.92027922e+05, 3.92049891e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.92031953e+05, 3.89993094e+05, 3.93974344e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.99365094e+05, 3.92028781e+05, 3.82446281e+05, 3.99365094e+05, 3.92028781e+05, 3.82446281e+05, 3.99365094e+05, 3.92028781e+05, 3.82446281e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.99365094e+05, 3.82446281e+05, ],
  }),
  ("nof_tree_events",                 399999),
  ("nof_db_events",                   399999),
  ("fsize_local",                     1483333883), # 1.48GB, avg file size 741.67MB
  ("fsize_db",                        20731646988), # 20.73GB, avg file size 767.84MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_270_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2BLNu2J_M-280_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_280_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_280_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                                          : [ 399997, ],
    'CountWeighted'                                                                  : [ 3.99983031e+05, 3.99989156e+05, 3.99985125e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.08722266e+05, 3.99979844e+05, 3.89177562e+05, 4.08722266e+05, 3.99979844e+05, 3.89177562e+05, 4.08722266e+05, 3.99979844e+05, 3.89177562e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.08722266e+05, 3.89177562e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.91749516e+05, 3.91738984e+05, 3.91763656e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.91749516e+05, 3.89649062e+05, 3.93756109e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.00257875e+05, 3.91746109e+05, 3.81210906e+05, 4.00257875e+05, 3.91746109e+05, 3.81210906e+05, 4.00257875e+05, 3.91746109e+05, 3.81210906e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.00257875e+05, 3.81210906e+05, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     1510533077), # 1.51GB, avg file size 755.27MB
  ("fsize_db",                        20422234109), # 20.42GB, avg file size 887.92MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_280_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2BLNu2J_M-300_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_300_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_300_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 299996, ],
    'CountWeighted'                                                                  : [ 2.99959594e+05, 2.99956242e+05, 2.99964969e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.08224910e+05, 2.99956281e+05, 2.90523887e+05, 3.08224910e+05, 2.99956281e+05, 2.90523887e+05, 3.08224910e+05, 2.99956281e+05, 2.90523887e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.08224910e+05, 2.90523887e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93408148e+05, 2.93382453e+05, 2.93434848e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93408148e+05, 2.91758098e+05, 2.94995602e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.01444777e+05, 2.93405129e+05, 2.84210906e+05, 3.01444777e+05, 2.93405129e+05, 2.84210906e+05, 3.01444777e+05, 2.93405129e+05, 2.84210906e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.01444777e+05, 2.84210906e+05, ],
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     1175764658), # 1.18GB, avg file size 587.88MB
  ("fsize_db",                        15701314107), # 15.70GB, avg file size 981.33MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_300_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2BLNu2J_M-320_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_320_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_320_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99999801e+05, 3.00011953e+05, 2.99992621e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.09807555e+05, 2.99998031e+05, 2.89307738e+05, 3.09807555e+05, 2.99998031e+05, 2.89307738e+05, 3.09807555e+05, 2.99998031e+05, 2.89307738e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.09808023e+05, 2.89307285e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92978500e+05, 2.92972691e+05, 2.92988004e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92978500e+05, 2.91235211e+05, 2.94662395e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.02514406e+05, 2.92976523e+05, 2.82584016e+05, 3.02514406e+05, 2.92976523e+05, 2.82584016e+05, 3.02514406e+05, 2.92976523e+05, 2.82584016e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.02514859e+05, 2.82583578e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1213625039), # 1.21GB, avg file size 606.81MB
  ("fsize_db",                        15961417075), # 15.96GB, avg file size 760.07MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_320_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2BLNu2J_M-350_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_350_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_350_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 299994, ],
    'CountWeighted'                                                                  : [ 2.99961273e+05, 2.99960055e+05, 2.99964586e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.11984762e+05, 2.99961273e+05, 2.87626062e+05, 3.11984762e+05, 2.99961273e+05, 2.87626062e+05, 3.11984762e+05, 2.99961273e+05, 2.87626062e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.11984762e+05, 2.87626062e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92425930e+05, 2.92415305e+05, 2.92441805e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92425930e+05, 2.90583379e+05, 2.94215746e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.04081328e+05, 2.92425930e+05, 2.80443668e+05, 3.04081328e+05, 2.92425930e+05, 2.80443668e+05, 3.04081328e+05, 2.92425930e+05, 2.80443668e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.04081328e+05, 2.80443668e+05, ],
  }),
  ("nof_tree_events",                 299994),
  ("nof_db_events",                   299994),
  ("fsize_local",                     1263897066), # 1.26GB, avg file size 631.95MB
  ("fsize_db",                        16286081884), # 16.29GB, avg file size 775.53MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_350_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2BLNu2J_M-400_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_400_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_400_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 299996, ],
    'CountWeighted'                                                                  : [ 2.99979602e+05, 2.99984836e+05, 2.99961883e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.15123484e+05, 2.99978926e+05, 2.85266121e+05, 3.15123484e+05, 2.99978926e+05, 2.85266121e+05, 3.15123484e+05, 2.99978926e+05, 2.85266121e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.15123781e+05, 2.85265840e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.91852273e+05, 2.91846613e+05, 2.91849008e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.91852273e+05, 2.89903078e+05, 2.93757543e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.06519031e+05, 2.91850656e+05, 2.77592586e+05, 3.06519031e+05, 2.91850656e+05, 2.77592586e+05, 3.06519031e+05, 2.91850656e+05, 2.77592586e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.06519312e+05, 2.77592320e+05, ],
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     1336590428), # 1.34GB, avg file size 668.30MB
  ("fsize_db",                        16786429735), # 16.79GB, avg file size 799.35MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_400_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2BLNu2J_M-450_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_450_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_450_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 299999, ],
    'CountWeighted'                                                                  : [ 2.99984926e+05, 2.99962590e+05, 2.99998004e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.17777395e+05, 2.99984926e+05, 2.83242473e+05, 3.17777395e+05, 2.99984926e+05, 2.83242473e+05, 3.17777395e+05, 2.99984926e+05, 2.83242473e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.17777828e+05, 2.83242023e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.91329523e+05, 2.91301621e+05, 2.91345203e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.91329523e+05, 2.89287125e+05, 2.93334520e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.08541070e+05, 2.91329523e+05, 2.75133742e+05, 3.08541070e+05, 2.91329523e+05, 2.75133742e+05, 3.08541070e+05, 2.91329523e+05, 2.75133742e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.08541469e+05, 2.75133344e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1402762208), # 1.40GB, avg file size 701.38MB
  ("fsize_db",                        16754898877), # 16.75GB, avg file size 881.84MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_450_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2BLNu2J_M-500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_500_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_500_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 299998, ],
    'CountWeighted'                                                                  : [ 2.99954242e+05, 2.99959086e+05, 2.99995426e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.20069027e+05, 2.99953016e+05, 2.81459797e+05, 3.20069027e+05, 2.99953016e+05, 2.81459797e+05, 3.20069027e+05, 2.99953016e+05, 2.81459797e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.20069027e+05, 2.81459797e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.91082906e+05, 2.91078961e+05, 2.91118461e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.91082906e+05, 2.89012008e+05, 2.93122344e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.10521562e+05, 2.91081328e+05, 2.73193812e+05, 3.10521562e+05, 2.91081328e+05, 2.73193812e+05, 3.10521562e+05, 2.91081328e+05, 2.73193812e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.10521562e+05, 2.73193812e+05, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1459151661), # 1.46GB, avg file size 729.58MB
  ("fsize_db",                        17339263289), # 17.34GB, avg file size 825.68MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_500_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2BLNu2J_M-550_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_550_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_550_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 279997, ],
    'CountWeighted'                                                                  : [ 2.79952164e+05, 2.79956504e+05, 2.79953336e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.00623852e+05, 2.79952164e+05, 2.61235945e+05, 3.00623852e+05, 2.79952164e+05, 2.61235945e+05, 3.00623852e+05, 2.79952164e+05, 2.61235945e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.00623852e+05, 2.61235945e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.71504352e+05, 2.71489445e+05, 2.71522094e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.71504352e+05, 2.69548535e+05, 2.73434797e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.91473879e+05, 2.71504352e+05, 2.53401879e+05, 2.91473879e+05, 2.71504352e+05, 2.53401879e+05, 2.91473879e+05, 2.71504352e+05, 2.53401879e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.91473879e+05, 2.53401879e+05, ],
  }),
  ("nof_tree_events",                 279997),
  ("nof_db_events",                   279997),
  ("fsize_local",                     1403767237), # 1.40GB, avg file size 701.88MB
  ("fsize_db",                        16243101578), # 16.24GB, avg file size 1.25GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_550_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2BLNu2J_M-600_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_600_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_600_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 193999, ],
    'CountWeighted'                                                                  : [ 1.93974531e+05, 1.93982781e+05, 1.93980656e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.09478688e+05, 1.93974531e+05, 1.80092625e+05, 2.09478688e+05, 1.93974531e+05, 1.80092625e+05, 2.09478688e+05, 1.93974531e+05, 1.80092625e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.09478688e+05, 1.80092625e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.88097969e+05, 1.88092922e+05, 1.88112562e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.88097969e+05, 1.86739031e+05, 1.89435969e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.03078906e+05, 1.88097969e+05, 1.74672438e+05, 2.03078906e+05, 1.88097969e+05, 1.74672438e+05, 2.03078906e+05, 1.88097969e+05, 1.74672438e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.03078906e+05, 1.74672438e+05, ],
  }),
  ("nof_tree_events",                 193999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     994024785), # 994.02MB, avg file size 994.02MB
  ("fsize_db",                        11943603757), # 11.94GB, avg file size 663.53MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_600_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2BLNu2J_M-650_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_650_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_650_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 185998, ],
    'CountWeighted'                                                                  : [ 1.85973422e+05, 1.85973328e+05, 1.85968344e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.01837922e+05, 1.85973422e+05, 1.71898656e+05, 2.01837922e+05, 1.85973422e+05, 1.71898656e+05, 2.01837922e+05, 1.85973422e+05, 1.71898656e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.01837922e+05, 1.71898656e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.80401844e+05, 1.80394438e+05, 1.80406469e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.80401844e+05, 1.79116609e+05, 1.81667812e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.95747781e+05, 1.80401844e+05, 1.66779516e+05, 1.95747781e+05, 1.80401844e+05, 1.66779516e+05, 1.95747781e+05, 1.80401844e+05, 1.66779516e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.95747781e+05, 1.66779516e+05, ],
  }),
  ("nof_tree_events",                 185998),
  ("nof_db_events",                   185998),
  ("fsize_local",                     966281202), # 966.28MB, avg file size 966.28MB
  ("fsize_db",                        11262492369), # 11.26GB, avg file size 563.12MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_650_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2BLNu2J_M-700_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_700_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_700_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 182000, ],
    'CountWeighted'                                                                  : [ 1.81975156e+05, 1.81953906e+05, 1.81966562e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.98407500e+05, 1.81975156e+05, 1.67484125e+05, 1.98407500e+05, 1.81975156e+05, 1.67484125e+05, 1.98407500e+05, 1.81975156e+05, 1.67484125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.98407672e+05, 1.67483969e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.76431562e+05, 1.76409453e+05, 1.76438344e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.76431562e+05, 1.75161594e+05, 1.77684844e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.92324203e+05, 1.76431562e+05, 1.62418172e+05, 1.92324203e+05, 1.76431562e+05, 1.62418172e+05, 1.92324203e+05, 1.76431562e+05, 1.62418172e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.92324359e+05, 1.62418016e+05, ],
  }),
  ("nof_tree_events",                 182000),
  ("nof_db_events",                   182000),
  ("fsize_local",                     955585529), # 955.59MB, avg file size 955.59MB
  ("fsize_db",                        11031109959), # 11.03GB, avg file size 648.89MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_700_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2BLNu2J_M-750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_750_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_750_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 194000, ],
    'CountWeighted'                                                                  : [ 1.93970531e+05, 1.93983750e+05, 1.93963000e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.12396266e+05, 1.93970531e+05, 1.77874359e+05, 2.12396266e+05, 1.93970531e+05, 1.77874359e+05, 2.12396266e+05, 1.93970531e+05, 1.77874359e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.12396297e+05, 1.77874344e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.88045625e+05, 1.88044406e+05, 1.88044219e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.88045625e+05, 1.86691922e+05, 1.89382047e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.05860406e+05, 1.88045625e+05, 1.72473484e+05, 2.05860406e+05, 1.88045625e+05, 1.72473484e+05, 2.05860406e+05, 1.88045625e+05, 1.72473484e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.05860422e+05, 1.72473469e+05, ],
  }),
  ("nof_tree_events",                 194000),
  ("nof_db_events",                   194000),
  ("fsize_local",                     1024708744), # 1.02GB, avg file size 1.02GB
  ("fsize_db",                        11798319012), # 11.80GB, avg file size 842.74MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_750_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2BLNu2J_M-800_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_800_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_800_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 185999, ],
    'CountWeighted'                                                                  : [ 1.85974734e+05, 1.85954906e+05, 1.85964766e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.04393906e+05, 1.85974734e+05, 1.69949812e+05, 2.04393906e+05, 1.85974734e+05, 1.69949812e+05, 2.04393906e+05, 1.85974734e+05, 1.69949812e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.04393938e+05, 1.69949797e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.80370234e+05, 1.80336406e+05, 1.80380750e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.80370234e+05, 1.79089906e+05, 1.81633844e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.98201422e+05, 1.80370234e+05, 1.64860781e+05, 1.98201422e+05, 1.80370234e+05, 1.64860781e+05, 1.98201422e+05, 1.80370234e+05, 1.64860781e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.98201422e+05, 1.64860766e+05, ],
  }),
  ("nof_tree_events",                 185999),
  ("nof_db_events",                   185999),
  ("fsize_local",                     986005462), # 986.01MB, avg file size 986.01MB
  ("fsize_db",                        11297941565), # 11.30GB, avg file size 941.50MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_800_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2BLNu2J_M-850_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_850_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_850_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 191995, ],
    'CountWeighted'                                                                  : [ 1.91948391e+05, 1.91949672e+05, 1.91958234e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.91948391e+05, 1.91948391e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.86201938e+05, 1.86205875e+05, 1.86206109e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.86201938e+05, 1.84889609e+05, 1.87495469e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.86201938e+05, 1.86201938e+05, ],
  }),
  ("nof_tree_events",                 191995),
  ("nof_db_events",                   191995),
  ("fsize_local",                     1026160445), # 1.03GB, avg file size 1.03GB
  ("fsize_db",                        12148184904), # 12.15GB, avg file size 714.60MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_850_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2BLNu2J_M-900_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_900_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_900_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 98000, ],
    'CountWeighted'                                                                  : [ 9.80004531e+04, 9.79916406e+04, 9.80073438e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.08342906e+05, 9.80004531e+04, 8.91641094e+04, 1.08342906e+05, 9.80004531e+04, 8.91641094e+04, 1.08342906e+05, 9.80004531e+04, 8.91641094e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.08342906e+05, 8.91641094e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.51201094e+04, 9.51080625e+04, 9.51290156e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.51201094e+04, 9.44643828e+04, 9.57664219e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.05138859e+05, 9.51201094e+04, 8.65559688e+04, 1.05138859e+05, 9.51201094e+04, 8.65559688e+04, 1.05138859e+05, 9.51201094e+04, 8.65559688e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.05138859e+05, 8.65559688e+04, ],
  }),
  ("nof_tree_events",                 98000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     524175440), # 524.18MB, avg file size 524.18MB
  ("fsize_db",                        6293415564), # 6.29GB, avg file size 393.34MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_900_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2BLNu2J_M-1000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1000_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_1000_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 85999, ],
    'CountWeighted'                                                                  : [ 8.59697266e+04, 8.59671641e+04, 8.59767656e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 9.57481875e+04, 8.59697266e+04, 7.76800469e+04, 9.57481875e+04, 8.59697266e+04, 7.76800469e+04, 9.57481875e+04, 8.59697266e+04, 7.76800469e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.57481875e+04, 7.76800469e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 8.34668125e+04, 8.34589844e+04, 8.34763125e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 8.34668125e+04, 8.28968438e+04, 8.40292344e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 9.29458125e+04, 8.34668125e+04, 7.54261484e+04, 9.29458125e+04, 8.34668125e+04, 7.54261484e+04, 9.29458125e+04, 8.34668125e+04, 7.54261484e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.29458125e+04, 7.54261484e+04, ],
  }),
  ("nof_tree_events",                 85999),
  ("nof_db_events",                   85999),
  ("fsize_local",                     460731223), # 460.73MB, avg file size 460.73MB
  ("fsize_db",                        5397181263), # 5.40GB, avg file size 539.72MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_1000_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2BLNu2J_M-1250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1250_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_1250_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 9.99548203e+04, 9.99560312e+04, 9.99576094e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99548203e+04, 9.99548203e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70281094e+04, 9.70346328e+04, 9.70260000e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70281094e+04, 9.63642188e+04, 9.76821562e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.70281094e+04, 9.70281094e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     534058195), # 534.06MB, avg file size 534.06MB
  ("fsize_db",                        6545415381), # 6.55GB, avg file size 503.49MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_1250_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2BLNu2J_M-1500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1500_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_1500_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 99998, ],
    'CountWeighted'                                                                  : [ 9.99328750e+04, 9.99383438e+04, 9.99138125e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99328750e+04, 9.99328750e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70415781e+04, 9.70501719e+04, 9.70284062e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70415781e+04, 9.63863438e+04, 9.76870391e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.70415781e+04, 9.70415781e+04, ],
  }),
  ("nof_tree_events",                 99998),
  ("nof_db_events",                   99998),
  ("fsize_local",                     524038948), # 524.04MB, avg file size 524.04MB
  ("fsize_db",                        6563136651), # 6.56GB, avg file size 546.93MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_1500_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2BLNu2J_M-1750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1750_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_1750_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 91997, ],
    'CountWeighted'                                                                  : [ 9.19430625e+04, 9.19372891e+04, 9.19423906e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.19430625e+04, 9.19430625e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 8.92977500e+04, 8.92881719e+04, 8.93021562e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 8.92977500e+04, 8.86976250e+04, 8.98893281e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 8.92977500e+04, 8.92977500e+04, ],
  }),
  ("nof_tree_events",                 91997),
  ("nof_db_events",                   91997),
  ("fsize_local",                     478567290), # 478.57MB, avg file size 478.57MB
  ("fsize_db",                        6187288430), # 6.19GB, avg file size 363.96MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_1750_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2BLNu2J_M-2000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_2000_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_2000_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 98000, ],
    'CountWeighted'                                                                  : [ 9.79393281e+04, 9.79371719e+04, 9.79382578e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.13395477e+05, 9.79393281e+04, 8.54697656e+04, 1.13395477e+05, 9.79393281e+04, 8.54697656e+04, 1.13395477e+05, 9.79393281e+04, 8.54697656e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.13399961e+05, 8.54668359e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.50529141e+04, 9.50447656e+04, 9.50600625e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.50529141e+04, 9.43975625e+04, 9.56983906e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.10053109e+05, 9.50529141e+04, 8.29521016e+04, 1.10053109e+05, 9.50529141e+04, 8.29521016e+04, 1.10053109e+05, 9.50529141e+04, 8.29521016e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.10056844e+05, 8.29494766e+04, ],
  }),
  ("nof_tree_events",                 98000),
  ("nof_db_events",                   98000),
  ("fsize_local",                     504127429), # 504.13MB, avg file size 504.13MB
  ("fsize_db",                        6251658881), # 6.25GB, avg file size 781.46MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_2000_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2BLNu2J_M-2500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_2500_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_2500_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.98551562e+04, 9.98603906e+04, 9.98511875e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.17158125e+05, 9.98551562e+04, 8.60930938e+04, 1.17158125e+05, 9.98551562e+04, 8.60930938e+04, 1.17158125e+05, 9.98551562e+04, 8.60930938e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.17159203e+05, 8.60920234e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.69287656e+04, 9.69338750e+04, 9.69294688e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.69287656e+04, 9.62614375e+04, 9.75848438e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.13726102e+05, 9.69287656e+04, 8.35700156e+04, 1.13726102e+05, 9.69287656e+04, 8.35700156e+04, 1.13726102e+05, 9.69287656e+04, 8.35700156e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.13727164e+05, 8.35689688e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     514147982), # 514.15MB, avg file size 514.15MB
  ("fsize_db",                        6622854002), # 6.62GB, avg file size 441.52MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_2500_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2BLNu2J_M-3000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_3000_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_3000_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 9.97376406e+04, 9.97180469e+04, 9.97429688e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.18437531e+05, 9.97376406e+04, 8.50684688e+04, 1.18437531e+05, 9.97376406e+04, 8.50684688e+04, 1.18437531e+05, 9.97376406e+04, 8.50684688e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.18438078e+05, 8.50673438e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.67692500e+04, 9.67446875e+04, 9.67810078e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.67692500e+04, 9.60917422e+04, 9.74362969e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.14913484e+05, 9.67692500e+04, 8.25366094e+04, 1.14913484e+05, 9.67692500e+04, 8.25366094e+04, 1.14913484e+05, 9.67692500e+04, 8.25366094e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.14913953e+05, 8.25355469e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     515762073), # 515.76MB, avg file size 515.76MB
  ("fsize_db",                        6575117767), # 6.58GB, avg file size 547.93MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_3000_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToRadionToHHTo2B2Tau_M-250_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_250_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_250_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99997531e+05, 3.99993656e+05, 3.99940688e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99997531e+05, 3.99997531e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.88472688e+05, 3.88438312e+05, 3.88469188e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.88472688e+05, 3.85652156e+05, 3.91199469e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.88472688e+05, 3.88472688e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     2078527881), # 2.08GB, avg file size 2.08GB
  ("fsize_db",                        24640211831), # 24.64GB, avg file size 1.07GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToRadionToHHTo2B2Tau_M-260_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_260_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_260_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 388000, ],
    'CountWeighted'                                                                  : [ 3.87904938e+05, 3.87945875e+05, 3.87983188e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.87904938e+05, 3.87904938e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.76422844e+05, 3.76438125e+05, 3.76483219e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.76422844e+05, 3.73628688e+05, 3.79144125e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.76422844e+05, 3.76422844e+05, ],
  }),
  ("nof_tree_events",                 388000),
  ("nof_db_events",                   388000),
  ("fsize_local",                     2044590915), # 2.04GB, avg file size 2.04GB
  ("fsize_db",                        24012313674), # 24.01GB, avg file size 1.33GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_260_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToRadionToHHTo2B2Tau_M-270_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_270_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_270_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 384000, ],
    'CountWeighted'                                                                  : [ 3.83955125e+05, 3.83964500e+05, 3.83898938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.83955125e+05, 3.83955125e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.72436312e+05, 3.72414750e+05, 3.72422875e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.72436312e+05, 3.69639219e+05, 3.75151625e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.72436312e+05, 3.72436312e+05, ],
  }),
  ("nof_tree_events",                 384000),
  ("nof_db_events",                   384000),
  ("fsize_local",                     2052513380), # 2.05GB, avg file size 2.05GB
  ("fsize_db",                        23968184441), # 23.97GB, avg file size 1.41GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_270_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToRadionToHHTo2B2Tau_M-280_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_280_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_280_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99941562e+05, 4.00002781e+05, 3.99967438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99941562e+05, 3.99941562e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.87697094e+05, 3.87701125e+05, 3.87736125e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.87697094e+05, 3.84729438e+05, 3.90579250e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.87697094e+05, 3.87697094e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     2164217288), # 2.16GB, avg file size 2.16GB
  ("fsize_db",                        25138262751), # 25.14GB, avg file size 1.09GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_280_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToRadionToHHTo2B2Tau_M-300_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_300_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_300_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99948625e+05, 2.99971188e+05, 2.99985812e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.99948625e+05, 2.99948625e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.90364625e+05, 2.90362781e+05, 2.90412500e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.90364625e+05, 2.88064219e+05, 2.92612781e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.90364625e+05, 2.90364625e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1659631254), # 1.66GB, avg file size 1.66GB
  ("fsize_db",                        19012035463), # 19.01GB, avg file size 1.27GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_300_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToRadionToHHTo2B2Tau_M-350_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_350_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_350_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99950781e+05, 2.99940562e+05, 2.99973625e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.99950781e+05, 2.99950781e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.89688531e+05, 2.89677062e+05, 2.89702500e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.89688531e+05, 2.87253375e+05, 2.92074250e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.89688531e+05, 2.89688531e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1741988627), # 1.74GB, avg file size 1.74GB
  ("fsize_db",                        19447040410), # 19.45GB, avg file size 1.77GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_350_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToRadionToHHTo2B2Tau_M-400_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_400_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_400_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99754219e+04, 9.99723594e+04, 9.99868516e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99754219e+04, 9.99754219e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.63455938e+04, 9.63423906e+04, 9.63568516e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.63455938e+04, 9.54930078e+04, 9.71847109e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.63455938e+04, 9.63455938e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     603471964), # 603.47MB, avg file size 603.47MB
  ("fsize_db",                        6609409571), # 6.61GB, avg file size 944.20MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_400_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToRadionToHHTo2B2Tau_M-450_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_450_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_450_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99959281e+05, 2.99970254e+05, 2.99950512e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.99959281e+05, 2.99959281e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.88844418e+05, 2.88826473e+05, 2.88859645e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.88844418e+05, 2.86236547e+05, 2.91405805e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.88844418e+05, 2.88844418e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1865009071), # 1.87GB, avg file size 932.50MB
  ("fsize_db",                        20167217854), # 20.17GB, avg file size 1.26GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_450_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToRadionToHHTo2B2Tau_M-500_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_500_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_500_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 290000, ],
    'CountWeighted'                                                                  : [ 2.89987656e+05, 2.89936250e+05, 2.89905719e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.89987656e+05, 2.89987656e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.78902469e+05, 2.78851812e+05, 2.78879312e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.78902469e+05, 2.76315094e+05, 2.81443250e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.78902469e+05, 2.78902469e+05, ],
  }),
  ("nof_tree_events",                 290000),
  ("nof_db_events",                   290000),
  ("fsize_local",                     1848850693), # 1.85GB, avg file size 1.85GB
  ("fsize_db",                        19708690689), # 19.71GB, avg file size 1.79GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToRadionToHHTo2B2Tau_M-550_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_550_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_550_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99930762e+05, 2.99901418e+05, 2.99924680e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.99930762e+05, 2.99930762e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.88216996e+05, 2.88173770e+05, 2.88239633e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.88216996e+05, 2.85489098e+05, 2.90899879e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.88216996e+05, 2.88216996e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1956531477), # 1.96GB, avg file size 978.27MB
  ("fsize_db",                        20644816504), # 20.64GB, avg file size 1.59GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_550_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToRadionToHHTo2B2Tau_M-600_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_600_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_600_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99907688e+05, 1.99904000e+05, 1.99912453e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99907688e+05, 1.99907688e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92023797e+05, 1.92009906e+05, 1.92034906e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92023797e+05, 1.90193250e+05, 1.93827812e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.92023797e+05, 1.92023797e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1327509479), # 1.33GB, avg file size 1.33GB
  ("fsize_db",                        13957904944), # 13.96GB, avg file size 1.16GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_600_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToRadionToHHTo2B2Tau_M-650_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_650_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_650_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99960625e+05, 1.99968094e+05, 1.99906094e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99960625e+05, 1.99960625e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.91776359e+05, 1.91763219e+05, 1.91758094e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.91776359e+05, 1.89883062e+05, 1.93642062e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.91776359e+05, 1.91776359e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1346683997), # 1.35GB, avg file size 1.35GB
  ("fsize_db",                        14016331858), # 14.02GB, avg file size 2.00GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_650_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToRadionToHHTo2B2Tau_M-700_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_700_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_700_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99902922e+05, 1.99931781e+05, 1.99911438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99902922e+05, 1.99902922e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.91637438e+05, 1.91646719e+05, 1.91644844e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.91637438e+05, 1.89725344e+05, 1.93522844e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.91637438e+05, 1.91637438e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1365862947), # 1.37GB, avg file size 1.37GB
  ("fsize_db",                        14253263609), # 14.25GB, avg file size 1.10GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_700_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToRadionToHHTo2B2Tau_M-750_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_750_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_750_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99237500e+04, 9.99622656e+04, 9.99573984e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99237500e+04, 9.99237500e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.57507891e+04, 9.57657812e+04, 9.57739141e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.57507891e+04, 9.47913984e+04, 9.66989062e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.57507891e+04, 9.57507891e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     690762109), # 690.76MB, avg file size 690.76MB
  ("fsize_db",                        7146269195), # 7.15GB, avg file size 1.02GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToRadionToHHTo2B2Tau_M-800_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_800_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_800_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99914578e+05, 1.99922031e+05, 1.99927094e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99914578e+05, 1.99914578e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.91447266e+05, 1.91447453e+05, 1.91458812e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.91447266e+05, 1.89502406e+05, 1.93369344e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.91447266e+05, 1.91447266e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1394335914), # 1.39GB, avg file size 1.39GB
  ("fsize_db",                        14420020815), # 14.42GB, avg file size 1.31GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_800_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToRadionToHHTo2B2Tau_M-850_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_850_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_850_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99872703e+05, 1.99865469e+05, 1.99882375e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99872703e+05, 1.99872703e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.91404484e+05, 1.91393125e+05, 1.91414484e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.91404484e+05, 1.89460531e+05, 1.93325688e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.91404484e+05, 1.91404484e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1405042291), # 1.41GB, avg file size 1.41GB
  ("fsize_db",                        14617490096), # 14.62GB, avg file size 1.04GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_850_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToRadionToHHTo2B2Tau_M-900_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_900_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_900_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99389375e+04, 9.99178203e+04, 9.99277266e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99389375e+04, 9.99389375e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.56674375e+04, 9.56434453e+04, 9.56700625e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.56674375e+04, 9.46887734e+04, 9.66338047e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.56674375e+04, 9.56674375e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     708646544), # 708.65MB, avg file size 708.65MB
  ("fsize_db",                        7382733082), # 7.38GB, avg file size 671.16MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_900_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToRadionToHHTo2B2Tau_M-1000_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_1000_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_1000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99230781e+04, 9.99223594e+04, 9.99194531e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99230781e+04, 9.99230781e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.56239688e+04, 9.56202344e+04, 9.56216406e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.56239688e+04, 9.46381953e+04, 9.65971406e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.56239688e+04, 9.56239688e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     717174638), # 717.17MB, avg file size 717.17MB
  ("fsize_db",                        7364574553), # 7.36GB, avg file size 1.05GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_1000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToRadionToHHTo2B2Tau_M-1250_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_1250_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_1250_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.98962656e+04, 9.98799141e+04, 9.98926094e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.98962656e+04, 9.98962656e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.54015234e+04, 9.53961953e+04, 9.54023281e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.54015234e+04, 9.43801953e+04, 9.64132344e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.54015234e+04, 9.54015234e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     726885015), # 726.89MB, avg file size 726.89MB
  ("fsize_db",                        7497237044), # 7.50GB, avg file size 1.07GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_1250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToRadionToHHTo2B2Tau_M-1500_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_1500_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_1500_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.98298594e+04, 9.98390469e+04, 9.98324375e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.98298594e+04, 9.98298594e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.53223125e+04, 9.53344531e+04, 9.53153281e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.53223125e+04, 9.43006250e+04, 9.63359219e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.53223125e+04, 9.53223125e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     731849421), # 731.85MB, avg file size 731.85MB
  ("fsize_db",                        7582428905), # 7.58GB, avg file size 1.52GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_1500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToRadionToHHTo2B2Tau_M-1750_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_1750_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_1750_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.97185781e+04, 9.97346406e+04, 9.97409297e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.97185781e+04, 9.97185781e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.51394453e+04, 9.51459453e+04, 9.51483906e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.51394453e+04, 9.41047422e+04, 9.61665391e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.51394453e+04, 9.51394453e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     733116360), # 733.12MB, avg file size 733.12MB
  ("fsize_db",                        7802866732), # 7.80GB, avg file size 650.24MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_1750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToRadionToHHTo2B2Tau_M-2000_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_2000_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_2000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.96747266e+04, 9.96807578e+04, 9.96587266e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.96747266e+04, 9.96747266e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.50011094e+04, 9.49986484e+04, 9.50009219e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.50011094e+04, 9.39472891e+04, 9.60459141e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.50011094e+04, 9.50011094e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     732128274), # 732.13MB, avg file size 732.13MB
  ("fsize_db",                        7810715378), # 7.81GB, avg file size 710.07MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_2000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToRadionToHHTo2B2Tau_M-3000_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_3000_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_3000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.87865391e+04, 9.88185469e+04, 9.88096875e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.87865391e+04, 9.87865391e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.40418281e+04, 9.40523672e+04, 9.40658672e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.40418281e+04, 9.29854922e+04, 9.50935938e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.40418281e+04, 9.40418281e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     735274599), # 735.27MB, avg file size 735.27MB
  ("fsize_db",                        7943092984), # 7.94GB, avg file size 992.89MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin0_3000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-250_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_250_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_250_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                                          : [ 386000, ],
    'CountWeighted'                                                                  : [ 3.80710875e+05, 3.80684469e+05, 3.80654281e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.18477469e+05, 3.82050531e+05, 3.51705438e+05, 4.16982688e+05, 3.80710688e+05, 3.50494969e+05, 4.15816156e+05, 3.79664125e+05, 3.49551344e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.20182719e+05, 3.47904688e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.51679719e+05, 3.51624312e+05, 3.51702438e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.51679719e+05, 3.45403250e+05, 3.57976312e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.86172812e+05, 3.52973906e+05, 3.25316438e+05, 3.84727781e+05, 3.51677906e+05, 3.24145844e+05, 3.83600094e+05, 3.50666438e+05, 3.23233000e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.87829625e+05, 3.21630938e+05, ],
  }),
  ("nof_tree_events",                 386000),
  ("nof_db_events",                   386000),
  ("fsize_local",                     2065891738), # 2.07GB, avg file size 2.07GB
  ("fsize_db",                        23569723909), # 23.57GB, avg file size 1.07GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-260_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_260_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_260_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.96138188e+05, 3.96209750e+05, 3.96123781e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.25618375e+05, 3.97454406e+05, 3.72943344e+05, 4.24175000e+05, 3.96138188e+05, 3.71736969e+05, 4.23057969e+05, 3.95120531e+05, 3.70804312e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.29873344e+05, 3.66639000e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.69735812e+05, 3.69732094e+05, 3.69756812e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.69735812e+05, 3.63831469e+05, 3.75626688e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.96677844e+05, 3.71010375e+05, 3.48592562e+05, 3.95280688e+05, 3.69735812e+05, 3.47424094e+05, 3.94199750e+05, 3.68749938e+05, 3.46520938e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.00811938e+05, 3.42472781e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1938316917), # 1.94GB, avg file size 1.94GB
  ("fsize_db",                        22974833125), # 22.97GB, avg file size 1.21GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_260_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-270_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_270_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_270_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.96176375e+05, 3.96169031e+05, 3.96176906e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.25826031e+05, 3.97469000e+05, 3.72790156e+05, 4.24407719e+05, 3.96175438e+05, 3.71605094e+05, 4.23310219e+05, 3.95175625e+05, 3.70688906e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.29939875e+05, 3.66664906e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.69669344e+05, 3.69629625e+05, 3.69701875e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.69669344e+05, 3.63736812e+05, 3.75585719e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.96770250e+05, 3.70919625e+05, 3.48350531e+05, 3.95397688e+05, 3.69667469e+05, 3.47203250e+05, 3.94336344e+05, 3.68699781e+05, 3.46315906e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.00767969e+05, 3.42403000e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1939642017), # 1.94GB, avg file size 1.94GB
  ("fsize_db",                        22808220732), # 22.81GB, avg file size 1.20GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_270_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-280_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_280_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_280_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.96167688e+05, 3.96205125e+05, 3.96164312e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.26095312e+05, 3.97392188e+05, 3.72446375e+05, 4.24750125e+05, 3.96167031e+05, 3.71325188e+05, 4.23708094e+05, 3.95218938e+05, 3.70457688e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.30024812e+05, 3.66622062e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.69680406e+05, 3.69657125e+05, 3.69720781e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.69680406e+05, 3.63745281e+05, 3.75598375e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.97049062e+05, 3.70863938e+05, 3.48027500e+05, 3.95747312e+05, 3.69678312e+05, 3.46942031e+05, 3.94739344e+05, 3.68760875e+05, 3.46102375e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.00874562e+05, 3.42365938e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1941619692), # 1.94GB, avg file size 1.94GB
  ("fsize_db",                        22983626173), # 22.98GB, avg file size 1.21GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_280_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-300_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_300_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_300_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 282000, ],
    'CountWeighted'                                                                  : [ 2.79385094e+05, 2.79306906e+05, 2.79385125e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.00913469e+05, 2.80205375e+05, 2.62164812e+05, 3.00008500e+05, 2.79384062e+05, 2.61414500e+05, 2.99306938e+05, 2.78746312e+05, 2.60832984e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.03536000e+05, 2.58277938e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.60494094e+05, 2.60429797e+05, 2.60526453e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.60494094e+05, 2.56264484e+05, 2.64710062e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.80220469e+05, 2.61288250e+05, 2.44793812e+05, 2.79344406e+05, 2.60492703e+05, 2.44067094e+05, 2.78665500e+05, 2.59875656e+05, 2.43503969e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.82765031e+05, 2.41023062e+05, ],
  }),
  ("nof_tree_events",                 282000),
  ("nof_db_events",                   282000),
  ("fsize_local",                     1370967946), # 1.37GB, avg file size 1.37GB
  ("fsize_db",                        15951259391), # 15.95GB, avg file size 839.54MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_300_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-320_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_320_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_320_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.97162750e+05, 2.97089875e+05, 2.97115875e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.20675531e+05, 2.97965500e+05, 2.78290031e+05, 3.19787188e+05, 2.97161562e+05, 2.77557688e+05, 3.19097469e+05, 2.96536250e+05, 2.76989188e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.23227500e+05, 2.74509094e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.76815688e+05, 2.76758344e+05, 2.76832250e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.76815688e+05, 2.72256438e+05, 2.81358688e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.98343031e+05, 2.77588219e+05, 2.59590609e+05, 2.97488156e+05, 2.76814031e+05, 2.58885219e+05, 2.96824062e+05, 2.76212438e+05, 2.58337719e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.00814375e+05, 2.55933719e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1461878010), # 1.46GB, avg file size 1.46GB
  ("fsize_db",                        17224376684), # 17.22GB, avg file size 1.01GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_320_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-350_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_350_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_350_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.97243844e+05, 2.97241406e+05, 2.97247031e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.21676750e+05, 2.97993438e+05, 2.77648438e+05, 3.20846562e+05, 2.97243250e+05, 2.76967812e+05, 3.20200844e+05, 2.96660812e+05, 2.76438250e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.23926750e+05, 2.74264312e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.76729125e+05, 2.76693781e+05, 2.76755469e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.76729125e+05, 2.72129688e+05, 2.81318250e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.99102312e+05, 2.77448938e+05, 2.58780281e+05, 2.98304594e+05, 2.76727938e+05, 2.58125609e+05, 2.97684188e+05, 2.76168031e+05, 2.57616594e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.01276812e+05, 2.55515594e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1465376565), # 1.47GB, avg file size 1.47GB
  ("fsize_db",                        16911146727), # 16.91GB, avg file size 1.06GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_350_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-400_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_400_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_400_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 292000, ],
    'CountWeighted'                                                                  : [ 2.89082375e+05, 2.89006844e+05, 2.89038031e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.14300938e+05, 2.89647844e+05, 2.68560250e+05, 3.13669344e+05, 2.89080156e+05, 2.68046625e+05, 3.13176969e+05, 2.88637125e+05, 2.67646188e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.16060781e+05, 2.65965219e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.68540875e+05, 2.68475719e+05, 2.68568750e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.68540875e+05, 2.63945625e+05, 2.73125062e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.91657312e+05, 2.69085375e+05, 2.49782344e+05, 2.91049000e+05, 2.68538375e+05, 2.49287250e+05, 2.90574844e+05, 2.68111812e+05, 2.48901469e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.93355938e+05, 2.47276531e+05, ],
  }),
  ("nof_tree_events",                 292000),
  ("nof_db_events",                   292000),
  ("fsize_local",                     1433808838), # 1.43GB, avg file size 1.43GB
  ("fsize_db",                        16538417486), # 16.54GB, avg file size 1.18GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_400_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-450_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_450_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_450_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.97030719e+05, 2.96939875e+05, 2.96860781e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.24809000e+05, 2.97550750e+05, 2.74417875e+05, 3.24223500e+05, 2.97026812e+05, 2.73945125e+05, 3.23766062e+05, 2.96616156e+05, 2.73575750e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.26326625e+05, 2.72143875e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.75420344e+05, 2.75358500e+05, 2.75383688e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.75420344e+05, 2.70595656e+05, 2.80231906e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.00897969e+05, 2.75922156e+05, 2.54769781e+05, 3.00334094e+05, 2.75417656e+05, 2.54314781e+05, 2.99894188e+05, 2.75023094e+05, 2.53959391e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.02358750e+05, 2.52578438e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1483560095), # 1.48GB, avg file size 1.48GB
  ("fsize_db",                        16984173640), # 16.98GB, avg file size 808.77MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_450_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-500_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_500_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_500_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.96816500e+05, 2.96852938e+05, 2.96839719e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.26339625e+05, 2.97262688e+05, 2.72948406e+05, 3.25838625e+05, 2.96816500e+05, 2.72547812e+05, 3.25446438e+05, 2.96467125e+05, 2.72234281e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.27645094e+05, 2.71010906e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.74894250e+05, 2.74871312e+05, 2.74933281e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.74894250e+05, 2.69994344e+05, 2.79784688e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.01933938e+05, 2.75324750e+05, 2.53037469e+05, 3.01450719e+05, 2.74894250e+05, 2.52651219e+05, 3.01072500e+05, 2.74557156e+05, 2.52348562e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.03182094e+05, 2.51177266e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1494669360), # 1.49GB, avg file size 1.49GB
  ("fsize_db",                        16980250583), # 16.98GB, avg file size 1.54GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-600_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_600_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_600_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.97637266e+05, 1.97650031e+05, 1.97618406e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.19587156e+05, 1.97814375e+05, 1.79947641e+05, 2.19387375e+05, 1.97637266e+05, 1.79789703e+05, 2.19230250e+05, 1.97498344e+05, 1.79665672e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.20239406e+05, 1.79072812e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.82291297e+05, 1.82286125e+05, 1.82297312e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.82291297e+05, 1.78871375e+05, 1.85706812e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.02356031e+05, 1.82460062e+05, 1.66104672e+05, 2.02165562e+05, 1.82291297e+05, 1.65954062e+05, 2.02015766e+05, 1.82158812e+05, 1.65835859e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.02975469e+05, 1.65272031e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1011513381), # 1.01GB, avg file size 1.01GB
  ("fsize_db",                        11350421129), # 11.35GB, avg file size 1.03GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_600_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-650_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_650_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_650_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 197000, ],
    'CountWeighted'                                                                  : [ 1.94681281e+05, 1.94620344e+05, 1.94613984e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.17392625e+05, 1.94843891e+05, 1.76393906e+05, 2.17205125e+05, 1.94678656e+05, 1.76246734e+05, 2.17057469e+05, 1.94548031e+05, 1.76130938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.17929969e+05, 1.75655250e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.79001281e+05, 1.78982312e+05, 1.78971188e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.79001281e+05, 1.75525188e+05, 1.82476844e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.99759422e+05, 1.79158438e+05, 1.62336609e+05, 1.99578938e+05, 1.78999438e+05, 1.62195094e+05, 1.99436875e+05, 1.78874109e+05, 1.62083531e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.00269250e+05, 1.61630797e+05, ],
  }),
  ("nof_tree_events",                 197000),
  ("nof_db_events",                   197000),
  ("fsize_local",                     1003378325), # 1.00GB, avg file size 1.00GB
  ("fsize_db",                        11416936121), # 11.42GB, avg file size 1.04GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_650_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-700_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_700_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_700_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.97261266e+05, 1.97245953e+05, 1.97255797e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.21433391e+05, 1.97395531e+05, 1.78002750e+05, 2.21273344e+05, 1.97254531e+05, 1.77877500e+05, 2.21147344e+05, 1.97143562e+05, 1.77778750e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.21909547e+05, 1.77362703e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.81140188e+05, 1.81087766e+05, 1.81186328e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.81140188e+05, 1.77567219e+05, 1.84722031e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.03171781e+05, 1.81270500e+05, 1.63576281e+05, 2.03019125e+05, 1.81135984e+05, 1.63456781e+05, 2.02898922e+05, 1.81030062e+05, 1.63362500e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.03624250e+05, 1.62965562e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1024412252), # 1.02GB, avg file size 1.02GB
  ("fsize_db",                        11593555122), # 11.59GB, avg file size 966.13MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_700_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-750_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_750_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_750_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.97207438e+05, 1.97194188e+05, 1.97247125e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.22483703e+05, 1.97324219e+05, 1.77159281e+05, 2.22350469e+05, 1.97207438e+05, 1.77055922e+05, 2.22245250e+05, 1.97115188e+05, 1.76974250e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.22890969e+05, 1.76626312e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.80670469e+05, 1.80647016e+05, 1.80707656e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.80670469e+05, 1.77017312e+05, 1.84333094e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.03681609e+05, 1.80782625e+05, 1.62412500e+05, 2.03553812e+05, 1.80670469e+05, 1.62313250e+05, 2.03452875e+05, 1.80582031e+05, 1.62234875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.04069391e+05, 1.61903078e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1031260227), # 1.03GB, avg file size 1.03GB
  ("fsize_db",                        11489097788), # 11.49GB, avg file size 2.30GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-850_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_850_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_850_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.96919469e+05, 1.96885250e+05, 1.96894469e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.24088016e+05, 1.97015641e+05, 1.75475281e+05, 2.23977781e+05, 1.96919469e+05, 1.75390562e+05, 2.23890578e+05, 1.96843141e+05, 1.75323562e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.24448219e+05, 1.75029016e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.79908031e+05, 1.79858484e+05, 1.79926469e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.79908031e+05, 1.76163203e+05, 1.83665172e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.04638016e+05, 1.79999906e+05, 1.60431844e+05, 2.04532594e+05, 1.79908031e+05, 1.60350938e+05, 2.04449219e+05, 1.79835094e+05, 1.60286812e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.04982375e+05, 1.60004500e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1039487129), # 1.04GB, avg file size 1.04GB
  ("fsize_db",                        11469515493), # 11.47GB, avg file size 1.43GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_850_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-900_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_900_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_900_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.83468984e+04, 9.83702422e+04, 9.83688359e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.12494477e+05, 9.83887188e+04, 8.73221016e+04, 1.12442414e+05, 9.83434453e+04, 8.72823984e+04, 1.12401164e+05, 9.83076484e+04, 8.72509844e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.12654836e+05, 8.71220469e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 8.97239766e+04, 8.97202031e+04, 8.97400547e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 8.97239766e+04, 8.78275547e+04, 9.16301172e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.02560398e+05, 8.97655312e+04, 7.97080469e+04, 1.02510562e+05, 8.97222422e+04, 7.96700000e+04, 1.02471078e+05, 8.96879688e+04, 7.96399688e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.02711352e+05, 7.95183672e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     521748804), # 521.75MB, avg file size 521.75MB
  ("fsize_db",                        5871346880), # 5.87GB, avg file size 489.28MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_900_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-1000_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_1000_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_1000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.81414062e+04, 9.81382500e+04, 9.81527891e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.13170766e+05, 9.81788906e+04, 8.64981016e+04, 1.13127492e+05, 9.81414062e+04, 8.64652344e+04, 1.13093172e+05, 9.81115312e+04, 8.64391406e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.13320875e+05, 8.63234297e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 8.91172266e+04, 8.90987656e+04, 8.91318203e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 8.91172266e+04, 8.71450234e+04, 9.10982812e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.02712867e+05, 8.91533047e+04, 7.85856406e+04, 1.02671219e+05, 8.91172266e+04, 7.85540312e+04, 1.02638203e+05, 8.90885156e+04, 7.85289375e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.02854281e+05, 7.84197734e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     525090856), # 525.09MB, avg file size 525.09MB
  ("fsize_db",                        5935760871), # 5.94GB, avg file size 494.65MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_1000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-1750_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_1750_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_1750_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.61841562e+04, 9.61812422e+04, 9.61469922e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.16927180e+05, 9.61971641e+04, 8.10300078e+04, 1.16910648e+05, 9.61832188e+04, 8.10180000e+04, 1.16897406e+05, 9.61720156e+04, 8.10084062e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.16945812e+05, 8.10306953e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 8.60772344e+04, 8.60563203e+04, 8.60875000e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 8.60772344e+04, 8.39360391e+04, 8.82495547e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.04631547e+05, 8.60894766e+04, 7.25442734e+04, 1.04616398e+05, 8.60766875e+04, 7.25332734e+04, 1.04604273e+05, 8.60663828e+04, 7.25244453e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.04656492e+05, 7.25353438e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     518489517), # 518.49MB, avg file size 518.49MB
  ("fsize_db",                        5865706342), # 5.87GB, avg file size 651.75MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_1750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-2000_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_2000_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_2000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.51681016e+04, 9.51949844e+04, 9.51735000e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.17498602e+05, 9.51750625e+04, 7.91718438e+04, 1.17490023e+05, 9.51678203e+04, 7.91656953e+04, 1.17483070e+05, 9.51620000e+04, 7.91607266e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.17533961e+05, 7.91697891e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 8.47665469e+04, 8.47761562e+04, 8.47685938e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 8.47665469e+04, 8.25801484e+04, 8.69889453e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.04636727e+05, 8.47723984e+04, 7.05254297e+04, 1.04628828e+05, 8.47657344e+04, 7.05197891e+04, 1.04622453e+05, 8.47603906e+04, 7.05152500e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.04670141e+05, 7.05224219e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     514603495), # 514.60MB, avg file size 514.60MB
  ("fsize_db",                        6015024771), # 6.02GB, avg file size 601.50MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_spin2_2000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_250_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_250_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 390000, ],
    'CountWeighted'                                                                  : [ 3.90069281e+05, 3.89998469e+05, 3.89979531e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.90069281e+05, 3.90069281e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.82745688e+05, 3.82675188e+05, 3.82703625e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.82745688e+05, 3.80831781e+05, 3.84560438e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.82745688e+05, 3.82745688e+05, ],
  }),
  ("nof_tree_events",                 390000),
  ("nof_db_events",                   390000),
  ("fsize_local",                     1362068630), # 1.36GB, avg file size 1.36GB
  ("fsize_db",                        20093492648), # 20.09GB, avg file size 1.18GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-260_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_260_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_260_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 360000, ],
    'CountWeighted'                                                                  : [ 3.59963688e+05, 3.60000250e+05, 3.59998969e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.65609875e+05, 3.59960531e+05, 3.52042938e+05, 3.65609875e+05, 3.59960531e+05, 3.52042938e+05, 3.65609875e+05, 3.59960531e+05, 3.52042938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.65609875e+05, 3.52042938e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.52839344e+05, 3.52857344e+05, 3.52876125e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.52839344e+05, 3.51000125e+05, 3.54603781e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.58325094e+05, 3.52836500e+05, 3.45110125e+05, 3.58325094e+05, 3.52836500e+05, 3.45110125e+05, 3.58325094e+05, 3.52836500e+05, 3.45110125e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.58325094e+05, 3.45110125e+05, ],
  }),
  ("nof_tree_events",                 360000),
  ("nof_db_events",                   360000),
  ("fsize_local",                     1267357939), # 1.27GB, avg file size 1.27GB
  ("fsize_db",                        17758553715), # 17.76GB, avg file size 986.59MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_260_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-270_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_270_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_270_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 392000, ],
    'CountWeighted'                                                                  : [ 3.92035656e+05, 3.91970719e+05, 3.92015562e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.99341844e+05, 3.92021500e+05, 3.82349250e+05, 3.99341844e+05, 3.92021500e+05, 3.82349250e+05, 3.99341844e+05, 3.92021500e+05, 3.82349250e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99341844e+05, 3.82349250e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.83960625e+05, 3.83909312e+05, 3.83958688e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.83960625e+05, 3.81891562e+05, 3.85944344e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.91083906e+05, 3.83950188e+05, 3.74533812e+05, 3.91083906e+05, 3.83950188e+05, 3.74533812e+05, 3.91083906e+05, 3.83950188e+05, 3.74533812e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.91083906e+05, 3.74533812e+05, ],
  }),
  ("nof_tree_events",                 392000),
  ("nof_db_events",                   392000),
  ("fsize_local",                     1399303046), # 1.40GB, avg file size 1.40GB
  ("fsize_db",                        19361033085), # 19.36GB, avg file size 1.21GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_270_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-280_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_280_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_280_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                                          : [ 398000, ],
    'CountWeighted'                                                                  : [ 3.97935469e+05, 3.97980188e+05, 3.97961219e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.97935469e+05, 3.97935469e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.89352312e+05, 3.89367688e+05, 3.89381812e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.89352312e+05, 3.87170781e+05, 3.91452562e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.89352312e+05, 3.89352312e+05, ],
  }),
  ("nof_tree_events",                 398000),
  ("nof_db_events",                   398000),
  ("fsize_local",                     1455365087), # 1.46GB, avg file size 1.46GB
  ("fsize_db",                        20704800616), # 20.70GB, avg file size 900.21MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_280_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-300_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_300_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_300_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 3.00048906e+05, 2.99930000e+05, 2.99959125e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.08236656e+05, 3.00048906e+05, 2.90521781e+05, 3.08236656e+05, 3.00048906e+05, 2.90521781e+05, 3.08236656e+05, 3.00048906e+05, 2.90521781e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.08236656e+05, 2.90521781e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93088938e+05, 2.92993938e+05, 2.93046406e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93088938e+05, 2.91346562e+05, 2.94770094e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.01061594e+05, 2.93088938e+05, 2.83844875e+05, 3.01061594e+05, 2.93088938e+05, 2.83844875e+05, 3.01061594e+05, 2.93088938e+05, 2.83844875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.01061594e+05, 2.83844875e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1117370311), # 1.12GB, avg file size 1.12GB
  ("fsize_db",                        15151937781), # 15.15GB, avg file size 688.72MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_300_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-320_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_320_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_320_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99961750e+05, 2.99953812e+05, 2.99997156e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.09838250e+05, 2.99961750e+05, 2.89297875e+05, 3.09838250e+05, 2.99961750e+05, 2.89297875e+05, 3.09838250e+05, 2.99961750e+05, 2.89297875e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.09838250e+05, 2.89297875e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92504719e+05, 2.92491594e+05, 2.92539094e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92504719e+05, 2.90662375e+05, 2.94301094e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.02075188e+05, 2.92504719e+05, 2.82141000e+05, 3.02075188e+05, 2.92504719e+05, 2.82141000e+05, 3.02075188e+05, 2.92504719e+05, 2.82141000e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.02075188e+05, 2.82141000e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1148798557), # 1.15GB, avg file size 1.15GB
  ("fsize_db",                        15215406969), # 15.22GB, avg file size 1.17GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_320_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-350_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_350_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_350_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99995094e+05, 3.00042500e+05, 2.99940750e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.11981562e+05, 2.99992812e+05, 2.87610875e+05, 3.11981562e+05, 2.99992812e+05, 2.87610875e+05, 3.11981562e+05, 2.99992812e+05, 2.87610875e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.11981562e+05, 2.87610875e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.91872938e+05, 2.91886438e+05, 2.91857031e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.91872938e+05, 2.89896469e+05, 2.93797281e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.03481281e+05, 2.91870250e+05, 2.79881344e+05, 3.03481281e+05, 2.91870250e+05, 2.79881344e+05, 3.03481281e+05, 2.91870250e+05, 2.79881344e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.03481281e+05, 2.79881344e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1189578851), # 1.19GB, avg file size 1.19GB
  ("fsize_db",                        15430234358), # 15.43GB, avg file size 1.10GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_350_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-400_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_400_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_400_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 296000, ],
    'CountWeighted'                                                                  : [ 2.96026938e+05, 2.95914750e+05, 2.95984031e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.10900562e+05, 2.96026938e+05, 2.81468719e+05, 3.10900562e+05, 2.96026938e+05, 2.81468719e+05, 3.10900562e+05, 2.96026938e+05, 2.81468719e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.10900562e+05, 2.81468719e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.87270031e+05, 2.87194875e+05, 2.87248375e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.87270031e+05, 2.85176031e+05, 2.89316219e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.01662688e+05, 2.87270031e+05, 2.73209219e+05, 3.01662688e+05, 2.87270031e+05, 2.73209219e+05, 3.01662688e+05, 2.87270031e+05, 2.73209219e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.01662688e+05, 2.73209219e+05, ],
  }),
  ("nof_tree_events",                 296000),
  ("nof_db_events",                   296000),
  ("fsize_local",                     1232417195), # 1.23GB, avg file size 1.23GB
  ("fsize_db",                        15540706594), # 15.54GB, avg file size 971.29MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_400_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-450_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_450_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_450_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 272000, ],
    'CountWeighted'                                                                  : [ 2.71994844e+05, 2.71937031e+05, 2.71996250e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.88103250e+05, 2.71994844e+05, 2.56803734e+05, 2.88103250e+05, 2.71994844e+05, 2.56803734e+05, 2.88103250e+05, 2.71994844e+05, 2.56803734e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.88103250e+05, 2.56803719e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.63476656e+05, 2.63417562e+05, 2.63506750e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.63476656e+05, 2.61464062e+05, 2.65457625e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.79032469e+05, 2.63476656e+05, 2.48821562e+05, 2.79032469e+05, 2.63476656e+05, 2.48821562e+05, 2.79032469e+05, 2.63476656e+05, 2.48821562e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.79032469e+05, 2.48821547e+05, ],
  }),
  ("nof_tree_events",                 272000),
  ("nof_db_events",                   272000),
  ("fsize_local",                     1179256136), # 1.18GB, avg file size 1.18GB
  ("fsize_db",                        14544281532), # 14.54GB, avg file size 808.02MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_450_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_500_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_500_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 190000, ],
    'CountWeighted'                                                                  : [ 1.89994562e+05, 1.90028500e+05, 1.90020953e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.02728797e+05, 1.89994562e+05, 1.78272016e+05, 2.02728797e+05, 1.89994562e+05, 1.78272016e+05, 2.02728797e+05, 1.89994562e+05, 1.78272016e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.02728797e+05, 1.78272016e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.83623062e+05, 1.83647641e+05, 1.83634156e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.83623062e+05, 1.82135250e+05, 1.85093406e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.95887531e+05, 1.83623062e+05, 1.72330500e+05, 1.95887531e+05, 1.83623062e+05, 1.72330500e+05, 1.95887531e+05, 1.83623062e+05, 1.72330500e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.95887531e+05, 1.72330500e+05, ],
  }),
  ("nof_tree_events",                 190000),
  ("nof_db_events",                   190000),
  ("fsize_local",                     852599591), # 852.60MB, avg file size 852.60MB
  ("fsize_db",                        10300681960), # 10.30GB, avg file size 858.39MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-550_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_550_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_550_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99975156e+05, 1.99950828e+05, 2.00000156e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.14725750e+05, 1.99975156e+05, 1.86581375e+05, 2.14725750e+05, 1.99975156e+05, 1.86581375e+05, 2.14725750e+05, 1.99975156e+05, 1.86581375e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.14725750e+05, 1.86581375e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92936281e+05, 1.92909844e+05, 1.92955578e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92936281e+05, 1.91298609e+05, 1.94550719e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.07116594e+05, 1.92936281e+05, 1.80053016e+05, 2.07116594e+05, 1.92936281e+05, 1.80053016e+05, 2.07116594e+05, 1.92936281e+05, 1.80053016e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.07116594e+05, 1.80053016e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     925203759), # 925.20MB, avg file size 925.20MB
  ("fsize_db",                        10884541416), # 10.88GB, avg file size 989.50MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_550_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-600_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_600_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_600_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99983359e+05, 1.99972266e+05, 1.99940781e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.15954125e+05, 1.99982469e+05, 1.85647234e+05, 2.15954125e+05, 1.99982469e+05, 1.85647234e+05, 2.15954125e+05, 1.99982469e+05, 1.85647234e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.15954125e+05, 1.85647234e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92690625e+05, 1.92676219e+05, 1.92683625e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92690625e+05, 1.91004266e+05, 1.94356875e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.08030391e+05, 1.92689484e+05, 1.78922266e+05, 2.08030391e+05, 1.92689484e+05, 1.78922266e+05, 2.08030391e+05, 1.92689484e+05, 1.78922266e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.08030391e+05, 1.78922266e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     947999667), # 948.00MB, avg file size 948.00MB
  ("fsize_db",                        11044936345), # 11.04GB, avg file size 920.41MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_600_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-650_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_650_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_650_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 188000, ],
    'CountWeighted'                                                                  : [ 1.87979531e+05, 1.87930969e+05, 1.87961391e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.04024594e+05, 1.87979531e+05, 1.73735141e+05, 2.04024594e+05, 1.87979531e+05, 1.73735141e+05, 2.04024594e+05, 1.87979531e+05, 1.73735141e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.04024594e+05, 1.73735141e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.80908781e+05, 1.80857000e+05, 1.80919656e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.80908781e+05, 1.79283453e+05, 1.82514406e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.96304188e+05, 1.80908781e+05, 1.67238750e+05, 1.96304188e+05, 1.80908781e+05, 1.67238750e+05, 1.96304188e+05, 1.80908781e+05, 1.67238750e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.96304188e+05, 1.67238750e+05, ],
  }),
  ("nof_tree_events",                 188000),
  ("nof_db_events",                   188000),
  ("fsize_local",                     910547031), # 910.55MB, avg file size 910.55MB
  ("fsize_db",                        10510514184), # 10.51GB, avg file size 700.70MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_650_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-700_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_700_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_700_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99919094e+05, 2.00015312e+05, 1.99966719e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.18057781e+05, 1.99919094e+05, 1.84084672e+05, 2.18057781e+05, 1.99919094e+05, 1.84084672e+05, 2.18057781e+05, 1.99919094e+05, 1.84084672e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.18057781e+05, 1.84084672e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92225781e+05, 1.92267438e+05, 1.92271719e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92225781e+05, 1.90462250e+05, 1.93971844e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.09587234e+05, 1.92225781e+05, 1.77014312e+05, 2.09587234e+05, 1.92225781e+05, 1.77014312e+05, 2.09587234e+05, 1.92225781e+05, 1.77014312e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.09587234e+05, 1.77014312e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     982972153), # 982.97MB, avg file size 982.97MB
  ("fsize_db",                        11214998225), # 11.21GB, avg file size 1.40GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_700_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_750_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_750_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 196000, ],
    'CountWeighted'                                                                  : [ 1.95944844e+05, 1.95986719e+05, 1.95992078e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.95944844e+05, 1.95944844e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.88193297e+05, 1.88206922e+05, 1.88231125e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.88193297e+05, 1.86425016e+05, 1.89946000e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.88193297e+05, 1.88193297e+05, ],
  }),
  ("nof_tree_events",                 196000),
  ("nof_db_events",                   196000),
  ("fsize_local",                     982820891), # 982.82MB, avg file size 982.82MB
  ("fsize_db",                        11545737081), # 11.55GB, avg file size 962.14MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-800_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_800_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_800_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99954125e+05, 1.99983000e+05, 1.99977516e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99954125e+05, 1.99954125e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.91982969e+05, 1.91996234e+05, 1.92001188e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.91982969e+05, 1.90171062e+05, 1.93781375e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.91982969e+05, 1.91982969e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1014454815), # 1.01GB, avg file size 1.01GB
  ("fsize_db",                        11819983411), # 11.82GB, avg file size 1.18GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_800_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-850_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_850_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_850_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 192000, ],
    'CountWeighted'                                                                  : [ 1.91971062e+05, 1.91958703e+05, 1.91946031e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.91971062e+05, 1.91971062e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.84231688e+05, 1.84201906e+05, 1.84239906e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.84231688e+05, 1.82471781e+05, 1.85973219e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.84231688e+05, 1.84231688e+05, ],
  }),
  ("nof_tree_events",                 192000),
  ("nof_db_events",                   192000),
  ("fsize_local",                     983507593), # 983.51MB, avg file size 983.51MB
  ("fsize_db",                        11490975329), # 11.49GB, avg file size 766.07MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_850_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-900_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_900_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_900_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 95000, ],
    'CountWeighted'                                                                  : [ 9.49802812e+04, 9.49788984e+04, 9.49807031e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.05134172e+05, 9.49802812e+04, 8.62800547e+04, 1.05134172e+05, 9.49802812e+04, 8.62800547e+04, 1.05134172e+05, 9.49802812e+04, 8.62800547e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.05138570e+05, 8.62756484e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.10443672e+04, 9.10408516e+04, 9.10478594e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.10443672e+04, 9.01564453e+04, 9.19272734e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.00747164e+05, 9.10443672e+04, 8.27233203e+04, 1.00747164e+05, 9.10443672e+04, 8.27233203e+04, 1.00747164e+05, 9.10443672e+04, 8.27233203e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.00751578e+05, 8.27189141e+04, ],
  }),
  ("nof_tree_events",                 95000),
  ("nof_db_events",                   95000),
  ("fsize_local",                     488791579), # 488.79MB, avg file size 488.79MB
  ("fsize_db",                        5517036529), # 5.52GB, avg file size 788.15MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_900_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-1000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1000_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_1000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99789922e+04, 9.99916406e+04, 9.99792500e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.11331688e+05, 9.99789688e+04, 9.03264766e+04, 1.11331688e+05, 9.99789688e+04, 9.03264766e+04, 1.11331688e+05, 9.99789688e+04, 9.03264766e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.11331922e+05, 9.03262500e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.57711016e+04, 9.57752812e+04, 9.57761875e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.57711016e+04, 9.48261641e+04, 9.67081016e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.06622094e+05, 9.57708281e+04, 8.65452969e+04, 1.06622094e+05, 9.57708281e+04, 8.65452969e+04, 1.06622094e+05, 9.57708281e+04, 8.65452969e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.06622305e+05, 8.65450781e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     522640478), # 522.64MB, avg file size 522.64MB
  ("fsize_db",                        5887358169), # 5.89GB, avg file size 654.15MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-1250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1250_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_1250_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99701328e+04, 9.99751875e+04, 9.99830938e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99701328e+04, 9.99701328e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.55974375e+04, 9.55993203e+04, 9.56085391e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.55974375e+04, 9.46223125e+04, 9.65677656e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.55974375e+04, 9.55974375e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     536313068), # 536.31MB, avg file size 536.31MB
  ("fsize_db",                        6210975535), # 6.21GB, avg file size 690.11MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-1500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1500_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_1500_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99652578e+04, 9.99667812e+04, 9.99482266e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.13901742e+05, 9.99647031e+04, 8.85185781e+04, 1.13901742e+05, 9.99647031e+04, 8.85185781e+04, 1.13901742e+05, 9.99647031e+04, 8.85185781e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.13902195e+05, 8.85180391e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.54928438e+04, 9.54925078e+04, 9.54822500e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.54928438e+04, 9.45037891e+04, 9.64794453e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.08786188e+05, 9.54922344e+04, 8.45748594e+04, 1.08786188e+05, 9.54922344e+04, 8.45748594e+04, 1.08786188e+05, 9.54922344e+04, 8.45748594e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.08786578e+05, 8.45743828e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     527868184), # 527.87MB, avg file size 527.87MB
  ("fsize_db",                        5949909431), # 5.95GB, avg file size 1.49GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-1750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1750_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_1750_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99403203e+04, 9.99439062e+04, 9.99463359e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99403203e+04, 9.99403203e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.53945078e+04, 9.53858516e+04, 9.54063359e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.53945078e+04, 9.43908125e+04, 9.63941328e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.53945078e+04, 9.53945078e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     528961553), # 528.96MB, avg file size 528.96MB
  ("fsize_db",                        6303523737), # 6.30GB, avg file size 573.05MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-2000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_2000_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_2000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 92000, ],
    'CountWeighted'                                                                  : [ 9.19149766e+04, 9.19114375e+04, 9.19080469e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.06418312e+05, 9.19112656e+04, 8.02110000e+04, 1.06418312e+05, 9.19112656e+04, 8.02110000e+04, 1.06418312e+05, 9.19112656e+04, 8.02110000e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.06418469e+05, 8.02108438e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 8.76738438e+04, 8.76693047e+04, 8.76693359e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 8.76738438e+04, 8.67415234e+04, 8.86031172e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.01496492e+05, 8.76716094e+04, 7.65201328e+04, 1.01496492e+05, 8.76716094e+04, 7.65201328e+04, 1.01496492e+05, 8.76716094e+04, 7.65201328e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.01496609e+05, 7.65200156e+04, ],
  }),
  ("nof_tree_events",                 92000),
  ("nof_db_events",                   92000),
  ("fsize_local",                     483651531), # 483.65MB, avg file size 483.65MB
  ("fsize_db",                        5565938746), # 5.57GB, avg file size 927.66MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_2000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-2500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_2500_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_2500_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.98705312e+04, 9.98876328e+04, 9.98801094e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.98705312e+04, 9.98705312e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.52335078e+04, 9.52346953e+04, 9.52486641e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.52335078e+04, 9.42207969e+04, 9.62471406e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.52335078e+04, 9.52335078e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     527708691), # 527.71MB, avg file size 527.71MB
  ("fsize_db",                        6456631366), # 6.46GB, avg file size 586.97MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_2500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-3000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_3000_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_3000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.97369062e+04, 9.97459219e+04, 9.97438516e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.97369062e+04, 9.97369062e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.50021484e+04, 9.49998359e+04, 9.50218047e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.50021484e+04, 9.39753438e+04, 9.60296016e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.50021484e+04, 9.50021484e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     528249731), # 528.25MB, avg file size 528.25MB
  ("fsize_db",                        6431618251), # 6.43GB, avg file size 803.95MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_3000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2Tau_M-250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_250_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_250_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99947750e+05, 3.99971969e+05, 3.99985719e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.04905125e+05, 3.99947750e+05, 3.92244938e+05, 4.04905125e+05, 3.99947750e+05, 3.92244938e+05, 4.04905125e+05, 3.99947750e+05, 3.92244938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.04905125e+05, 3.92244938e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.92101562e+05, 3.92102125e+05, 3.92143344e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.92101562e+05, 3.90073906e+05, 3.94044250e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.96901125e+05, 3.92101562e+05, 3.84575688e+05, 3.96901125e+05, 3.92101562e+05, 3.84575688e+05, 3.96901125e+05, 3.92101562e+05, 3.84575688e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.96901125e+05, 3.84575688e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1410772370), # 1.41GB, avg file size 1.41GB
  ("fsize_db",                        20195673518), # 20.20GB, avg file size 878.07MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2Tau_M-260_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_260_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_260_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 384000, ],
    'CountWeighted'                                                                  : [ 3.83962531e+05, 3.83923312e+05, 3.83970750e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.90007438e+05, 3.83962531e+05, 3.75522875e+05, 3.90007438e+05, 3.83962531e+05, 3.75522875e+05, 3.90007438e+05, 3.83962531e+05, 3.75522875e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.90007438e+05, 3.75522875e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.76051750e+05, 3.76016438e+05, 3.76062562e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.76051750e+05, 3.74024000e+05, 3.77991312e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.81914812e+05, 3.76051750e+05, 3.67818312e+05, 3.81914812e+05, 3.76051750e+05, 3.67818312e+05, 3.81914812e+05, 3.76051750e+05, 3.67818312e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.81914812e+05, 3.67818312e+05, ],
  }),
  ("nof_tree_events",                 384000),
  ("nof_db_events",                   384000),
  ("fsize_local",                     1380626556), # 1.38GB, avg file size 1.38GB
  ("fsize_db",                        19164112451), # 19.16GB, avg file size 1.13GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_260_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2Tau_M-270_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_270_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_270_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 390000, ],
    'CountWeighted'                                                                  : [ 3.89995062e+05, 3.89981406e+05, 3.89965688e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.97346875e+05, 3.89995062e+05, 3.80395375e+05, 3.97346875e+05, 3.89995062e+05, 3.80395375e+05, 3.97346875e+05, 3.89995062e+05, 3.80395375e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.97346875e+05, 3.80395375e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.81606562e+05, 3.81566812e+05, 3.81608094e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.81606562e+05, 3.79474875e+05, 3.83652312e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.88742531e+05, 3.81606562e+05, 3.72261188e+05, 3.88742531e+05, 3.81606562e+05, 3.72261188e+05, 3.88742531e+05, 3.81606562e+05, 3.72261188e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.88742531e+05, 3.72261188e+05, ],
  }),
  ("nof_tree_events",                 390000),
  ("nof_db_events",                   390000),
  ("fsize_local",                     1427577079), # 1.43GB, avg file size 1.43GB
  ("fsize_db",                        19739699313), # 19.74GB, avg file size 1.10GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_270_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2Tau_M-280_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_280_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_280_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 379000, ],
    'CountWeighted'                                                                  : [ 3.78992500e+05, 3.78961312e+05, 3.78972344e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.87251031e+05, 3.78992500e+05, 3.68744594e+05, 3.87251031e+05, 3.78992500e+05, 3.68744594e+05, 3.87251031e+05, 3.78992500e+05, 3.68744594e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.87251031e+05, 3.68744594e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.70464219e+05, 3.70422344e+05, 3.70469219e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.70464219e+05, 3.68318750e+05, 3.72531062e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.78485562e+05, 3.70464219e+05, 3.60502344e+05, 3.78485562e+05, 3.70464219e+05, 3.60502344e+05, 3.78485562e+05, 3.70464219e+05, 3.60502344e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.78485562e+05, 3.60502344e+05, ],
  }),
  ("nof_tree_events",                 379000),
  ("nof_db_events",                   379000),
  ("fsize_local",                     1411214870), # 1.41GB, avg file size 1.41GB
  ("fsize_db",                        19359006495), # 19.36GB, avg file size 967.95MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_280_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2tau_M-300_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_300_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_300_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    33),
  ("nof_events",                      {
    'Count'                                                                          : [ 40000, ],
    'CountWeighted'                                                                  : [ 3.99952617e+04, 3.99961953e+04, 3.99966211e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.10967500e+04, 3.99952617e+04, 3.87363789e+04, 4.10967500e+04, 3.99952617e+04, 3.87363789e+04, 4.10967500e+04, 3.99952617e+04, 3.87363789e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.10970234e+04, 3.87361055e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.91004766e+04, 3.90999805e+04, 3.91034570e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 3.91004766e+04, 3.88762773e+04, 3.93161562e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.01710234e+04, 3.91004766e+04, 3.78746953e+04, 4.01710234e+04, 3.91004766e+04, 3.78746953e+04, 4.01710234e+04, 3.91004766e+04, 3.78746953e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.01712969e+04, 3.78744180e+04, ],
  }),
  ("nof_tree_events",                 40000),
  ("nof_db_events",                   981549),
  ("fsize_local",                     154915548), # 154.92MB, avg file size 154.92MB
  ("fsize_db",                        50466696906), # 50.47GB, avg file size 1.53GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_300_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2Tau_M-350_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_350_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_350_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 3.00006625e+05, 2.99983688e+05, 3.00003500e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.12005750e+05, 3.00006625e+05, 2.87644750e+05, 3.12005750e+05, 3.00006625e+05, 2.87644750e+05, 3.12005750e+05, 3.00006625e+05, 2.87644750e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.12005750e+05, 2.87644750e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.91984812e+05, 2.91967062e+05, 2.91984125e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.91984812e+05, 2.90052312e+05, 2.93879250e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.03603375e+05, 2.91984812e+05, 2.80010000e+05, 3.03603375e+05, 2.91984812e+05, 2.80010000e+05, 3.03603375e+05, 2.91984812e+05, 2.80010000e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.03603375e+05, 2.80010000e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1230381063), # 1.23GB, avg file size 1.23GB
  ("fsize_db",                        15849336173), # 15.85GB, avg file size 2.26GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_350_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2Tau_M-400_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_400_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_400_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99925625e+05, 2.99960125e+05, 2.99987375e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.15131531e+05, 2.99925625e+05, 2.85253750e+05, 3.15131531e+05, 2.99925625e+05, 2.85253750e+05, 3.15131531e+05, 2.99925625e+05, 2.85253750e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.15131531e+05, 2.85253750e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.91312438e+05, 2.91324062e+05, 2.91357781e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.91312438e+05, 2.89276562e+05, 2.93320156e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.05983344e+05, 2.91312438e+05, 2.77109062e+05, 3.05983344e+05, 2.91312438e+05, 2.77109062e+05, 3.05983344e+05, 2.91312438e+05, 2.77109062e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.05983344e+05, 2.77109062e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1296066271), # 1.30GB, avg file size 1.30GB
  ("fsize_db",                        16220410321), # 16.22GB, avg file size 1.08GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_400_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2Tau_M-450_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_450_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_450_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99992344e+05, 2.99950219e+05, 2.99950406e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.17771531e+05, 2.99992344e+05, 2.83218625e+05, 3.17771531e+05, 2.99992344e+05, 2.83218625e+05, 3.17771531e+05, 2.99992344e+05, 2.83218625e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.17771531e+05, 2.83218625e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.91007875e+05, 2.90958719e+05, 2.90999188e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.91007875e+05, 2.88907062e+05, 2.93076562e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.08184094e+05, 2.91007875e+05, 2.74810094e+05, 3.08184094e+05, 2.91007875e+05, 2.74810094e+05, 3.08184094e+05, 2.91007875e+05, 2.74810094e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.08184094e+05, 2.74810062e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1352970540), # 1.35GB, avg file size 1.35GB
  ("fsize_db",                        16455015197), # 16.46GB, avg file size 1.03GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_450_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2Tau_M-500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_500_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_500_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 2.00001781e+05, 1.99984188e+05, 1.99951469e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.13369062e+05, 2.00001781e+05, 1.87634781e+05, 2.13369062e+05, 2.00001781e+05, 1.87634781e+05, 2.13369062e+05, 2.00001781e+05, 1.87634781e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.13369062e+05, 1.87634781e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.93803641e+05, 1.93788625e+05, 1.93779250e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.93803641e+05, 1.92371750e+05, 1.95216000e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.06712375e+05, 1.93803641e+05, 1.81870594e+05, 2.06712375e+05, 1.93803641e+05, 1.81870594e+05, 2.06712375e+05, 1.93803641e+05, 1.81870594e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.06712375e+05, 1.81870594e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     934915296), # 934.92MB, avg file size 934.92MB
  ("fsize_db",                        11098842678), # 11.10GB, avg file size 1.39GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2Tau_M-550_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_550_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_550_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 192000, ],
    'CountWeighted'                                                                  : [ 1.91978125e+05, 1.91998188e+05, 1.91974875e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.06147531e+05, 1.91978125e+05, 1.79137531e+05, 2.06147531e+05, 1.91978125e+05, 1.79137531e+05, 2.06147531e+05, 1.91978125e+05, 1.79137531e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.06147531e+05, 1.79137531e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.86068594e+05, 1.86073969e+05, 1.86079734e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.86068594e+05, 1.84706906e+05, 1.87412125e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.99748812e+05, 1.86068594e+05, 1.73662078e+05, 1.99748812e+05, 1.86068594e+05, 1.73662078e+05, 1.99748812e+05, 1.86068594e+05, 1.73662078e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.99748812e+05, 1.73662078e+05, ],
  }),
  ("nof_tree_events",                 192000),
  ("nof_db_events",                   192000),
  ("fsize_local",                     926296631), # 926.30MB, avg file size 926.30MB
  ("fsize_db",                        10855478264), # 10.86GB, avg file size 775.39MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_550_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2Tau_M-600_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_600_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_600_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99998141e+05, 1.99998625e+05, 1.99969125e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.15960062e+05, 1.99998141e+05, 1.85682750e+05, 2.15960062e+05, 1.99998141e+05, 1.85682750e+05, 2.15960062e+05, 1.99998141e+05, 1.85682750e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.15960062e+05, 1.85682750e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.93878281e+05, 1.93869281e+05, 1.93874594e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.93878281e+05, 1.92468859e+05, 1.95265547e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.09299547e+05, 1.93878281e+05, 1.80039812e+05, 2.09299547e+05, 1.93878281e+05, 1.80039812e+05, 2.09299547e+05, 1.93878281e+05, 1.80039812e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.09299547e+05, 1.80039812e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     988260453), # 988.26MB, avg file size 988.26MB
  ("fsize_db",                        11487024358), # 11.49GB, avg file size 675.71MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_600_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2Tau_M-650_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_650_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_650_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 188000, ],
    'CountWeighted'                                                                  : [ 1.87974328e+05, 1.87960078e+05, 1.87969875e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.04000641e+05, 1.87973094e+05, 1.73747219e+05, 2.04000641e+05, 1.87973094e+05, 1.73747219e+05, 2.04000641e+05, 1.87973094e+05, 1.73747219e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.04000641e+05, 1.73747219e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.82148750e+05, 1.82129406e+05, 1.82161281e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.82148750e+05, 1.80813766e+05, 1.83466406e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.97631641e+05, 1.82147484e+05, 1.68394719e+05, 1.97631641e+05, 1.82147484e+05, 1.68394719e+05, 1.97631641e+05, 1.82147484e+05, 1.68394719e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.97631641e+05, 1.68394719e+05, ],
  }),
  ("nof_tree_events",                 188000),
  ("nof_db_events",                   188000),
  ("fsize_local",                     945712223), # 945.71MB, avg file size 945.71MB
  ("fsize_db",                        10754684541), # 10.75GB, avg file size 768.19MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_650_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2Tau_M-750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_750_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_750_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99983781e+05, 1.99981375e+05, 1.99951562e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.18959219e+05, 1.99982172e+05, 1.83378766e+05, 2.18959219e+05, 1.99982172e+05, 1.83378766e+05, 2.18959219e+05, 1.99982172e+05, 1.83378766e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.18959188e+05, 1.83378766e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.93809000e+05, 1.93791062e+05, 1.93803859e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.93809000e+05, 1.92399625e+05, 1.95198984e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.12155422e+05, 1.93807469e+05, 1.77751406e+05, 2.12155422e+05, 1.93807469e+05, 1.77751406e+05, 2.12155422e+05, 1.93807469e+05, 1.77751406e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.12155422e+05, 1.77751406e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1030303915), # 1.03GB, avg file size 1.03GB
  ("fsize_db",                        11547164401), # 11.55GB, avg file size 888.24MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToBulkGravitonToHHTo2B2Tau_M-800_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_800_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_800_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 192000, ],
    'CountWeighted'                                                                  : [ 1.91955969e+05, 1.91944703e+05, 1.91972297e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.10982000e+05, 1.91955672e+05, 1.75452156e+05, 2.10982000e+05, 1.91955672e+05, 1.75452156e+05, 2.10982000e+05, 1.91955672e+05, 1.75452156e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.10982000e+05, 1.75452156e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.86175094e+05, 1.86158141e+05, 1.86192250e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.86175094e+05, 1.84856000e+05, 1.87479203e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.04585531e+05, 1.86174562e+05, 1.70192594e+05, 2.04585531e+05, 1.86174562e+05, 1.70192594e+05, 2.04585531e+05, 1.86174562e+05, 1.70192594e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.04585531e+05, 1.70192594e+05, ],
  }),
  ("nof_tree_events",                 192000),
  ("nof_db_events",                   192000),
  ("fsize_local",                     997914058), # 997.91MB, avg file size 997.91MB
  ("fsize_db",                        11179122535), # 11.18GB, avg file size 1.02GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_800_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFHHTo2B2Tau_CV_1_C2V_1_C3_0_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_0_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_0_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    26),
  ("nof_events",                      {
    'Count'                                                                          : [ 369000, ],
    'CountWeighted'                                                                  : [ 3.65800156e+05, 3.65893750e+05, 3.65879875e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.65800156e+05, 3.65800156e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.44775188e+05, 3.44771562e+05, 3.44847719e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.44775188e+05, 3.39838219e+05, 3.49656625e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.44775188e+05, 3.44775188e+05, ],
  }),
  ("nof_tree_events",                 369000),
  ("nof_db_events",                   369000),
  ("fsize_local",                     1596333739), # 1.60GB, avg file size 1.60GB
  ("fsize_db",                        20317409524), # 20.32GB, avg file size 781.44MB
  ("use_it",                          True),
  ("xsection",                        0.0003364547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_0_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFHHTo2B2Tau_CV_1_C2V_1_C3_1_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_1_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_1_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.97138812e+05, 2.97152719e+05, 2.97192250e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.97138812e+05, 2.97138812e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.77515719e+05, 2.77505812e+05, 2.77540438e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.77515719e+05, 2.72963656e+05, 2.82032938e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.77515719e+05, 2.77515719e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1303257918), # 1.30GB, avg file size 1.30GB
  ("fsize_db",                        16551491719), # 16.55GB, avg file size 827.57MB
  ("use_it",                          True),
  ("xsection",                        0.0001260006),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_1_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFHHTo2B2Tau_CV_1_C2V_1_C3_2_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_2_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_2_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.96241531e+05, 3.96299688e+05, 3.96267375e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.96241531e+05, 3.96241531e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.63530500e+05, 3.63512375e+05, 3.63578312e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.63530500e+05, 3.56196969e+05, 3.70858562e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.63530500e+05, 3.63530500e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1849435274), # 1.85GB, avg file size 1.85GB
  ("fsize_db",                        22555887148), # 22.56GB, avg file size 2.51GB
  ("use_it",                          True),
  ("xsection",                        0.0001038674),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_2_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFHHTo2B2Tau_CV_1_C2V_2_C3_1_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_2_1_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_2_1_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    24),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.92904812e+05, 3.92917000e+05, 3.92979938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.92904812e+05, 3.92904812e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.64733500e+05, 3.64694875e+05, 3.64803125e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.64733500e+05, 3.58512562e+05, 3.70965812e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.64733500e+05, 3.64733500e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     2087508594), # 2.09GB, avg file size 2.09GB
  ("fsize_db",                        23834632407), # 23.83GB, avg file size 993.11MB
  ("use_it",                          True),
  ("xsection",                        0.001037918),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_2_1_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/VBFHHTo2B2Tau_CV_1_5_C2V_1_C3_1_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1p5_1_1_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1p5_1_1_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 392000, ],
    'CountWeighted'                                                                  : [ 3.86921812e+05, 3.87033969e+05, 3.86937312e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.86921812e+05, 3.86921812e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.61215938e+05, 3.61241000e+05, 3.61248469e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.61215938e+05, 3.55368719e+05, 3.67040438e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.61215938e+05, 3.61215938e+05, ],
  }),
  ("nof_tree_events",                 392000),
  ("nof_db_events",                   392000),
  ("fsize_local",                     1859105546), # 1.86GB, avg file size 1.86GB
  ("fsize_db",                        22237635973), # 22.24GB, avg file size 1.39GB
  ("use_it",                          True),
  ("xsection",                        0.004819446),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1p5_1_1_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToHHTo2B2Tau_node_SM_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_sm_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 380000, ],
    'CountWeighted'                                                                  : [ 3.80005188e+05, 3.79962062e+05, 3.80038625e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.86390375e+05, 4.59104156e+05, 4.33466844e+05, 4.02655031e+05, 3.80002625e+05, 3.58694781e+05, 3.39105125e+05, 3.19931656e+05, 3.01970531e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.86390375e+05, 3.01970438e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.67951906e+05, 3.67905938e+05, 3.67987031e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.67951906e+05, 3.65108344e+05, 3.70746094e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.70846875e+05, 4.44579062e+05, 4.19883094e+05, 3.89767688e+05, 3.67949438e+05, 3.47435125e+05, 3.28236312e+05, 3.09785500e+05, 2.92481125e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.70846875e+05, 2.92481031e+05, ],
  }),
  ("nof_tree_events",                 380000),
  ("nof_db_events",                   380000),
  ("fsize_local",                     1670447992), # 1.67GB, avg file size 1.67GB
  ("fsize_db",                        20440095707), # 20.44GB, avg file size 1.14GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_sm_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToHHTo2B2Tau_node_2_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_2_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 392000, ],
    'CountWeighted'                                                                  : [ 3.92000250e+05, 3.91922469e+05, 3.91980531e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.09246094e+05, 4.69268594e+05, 4.34112562e+05, 4.25549500e+05, 3.92000250e+05, 3.62403000e+05, 3.61236781e+05, 3.32538156e+05, 3.07370125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.09246312e+05, 3.07369938e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.77803625e+05, 3.77736156e+05, 3.77805062e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.77803625e+05, 3.74541750e+05, 3.81018406e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.90646875e+05, 4.52346875e+05, 4.18638844e+05, 4.09965938e+05, 3.77803625e+05, 3.49449531e+05, 3.47976250e+05, 3.20488312e+05, 2.96356938e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.90647094e+05, 2.96356750e+05, ],
  }),
  ("nof_tree_events",                 392000),
  ("nof_db_events",                   392000),
  ("fsize_local",                     1876509127), # 1.88GB, avg file size 1.88GB
  ("fsize_db",                        22130629455), # 22.13GB, avg file size 1.58GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_2_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToHHTo2B2Tau_node_3_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_3_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                                          : [ 396000, ],
    'CountWeighted'                                                                  : [ 3.96011125e+05, 3.95853500e+05, 3.96019312e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.06923188e+05, 4.78365938e+05, 4.51559969e+05, 4.19680000e+05, 3.96002750e+05, 3.73715562e+05, 3.53457125e+05, 3.33432250e+05, 3.14657219e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.06923250e+05, 3.14657156e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.83324156e+05, 3.83203031e+05, 3.83346906e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.83324156e+05, 3.80330812e+05, 3.86257094e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.90559438e+05, 4.63074688e+05, 4.37247688e+05, 4.06115438e+05, 3.83318000e+05, 3.61858156e+05, 3.42020812e+05, 3.22749625e+05, 3.04661719e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.90559500e+05, 3.04661688e+05, ],
  }),
  ("nof_tree_events",                 396000),
  ("nof_db_events",                   396000),
  ("fsize_local",                     1749084041), # 1.75GB, avg file size 1.75GB
  ("fsize_db",                        21371438091), # 21.37GB, avg file size 971.43MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_3_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToHHTo2B2Tau_node_4_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_4_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99990094e+05, 3.99951500e+05, 3.99973531e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10035938e+05, 4.84401781e+05, 4.59731500e+05, 4.21207625e+05, 3.99990094e+05, 3.79553500e+05, 3.54002156e+05, 3.36103250e+05, 3.18934000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10035938e+05, 3.18934000e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.87769375e+05, 3.87733719e+05, 3.87767312e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.87769375e+05, 3.84858844e+05, 3.90614938e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.94329656e+05, 4.69626906e+05, 4.45825750e+05, 4.08221625e+05, 3.87769375e+05, 3.68062062e+05, 3.43077562e+05, 3.25833500e+05, 3.09266156e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.94329656e+05, 3.09266156e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1719811132), # 1.72GB, avg file size 1.72GB
  ("fsize_db",                        21451946375), # 21.45GB, avg file size 1.02GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_4_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToHHTo2B2Tau_node_7_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_7_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 376000, ],
    'CountWeighted'                                                                  : [ 3.75978500e+05, 3.75920688e+05, 3.76005812e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.79494500e+05, 4.55282875e+05, 4.32002844e+05, 3.96004344e+05, 3.75978500e+05, 3.56709219e+05, 3.32838312e+05, 3.15958562e+05, 2.99750062e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.79494500e+05, 2.99750062e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.64479688e+05, 3.64427938e+05, 3.64508688e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.64479688e+05, 3.61744438e+05, 3.67160688e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.64717750e+05, 4.41380062e+05, 4.18918375e+05, 3.83789750e+05, 3.64479688e+05, 3.45893812e+05, 3.22563531e+05, 3.06293250e+05, 2.90655500e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.64717750e+05, 2.90655500e+05, ],
  }),
  ("nof_tree_events",                 376000),
  ("nof_db_events",                   376000),
  ("fsize_local",                     1618088881), # 1.62GB, avg file size 1.62GB
  ("fsize_db",                        20190349511), # 20.19GB, avg file size 1.26GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_7_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToHHTo2B2Tau_node_9_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_9_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99981406e+05, 3.99864219e+05, 3.99967344e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.19420781e+05, 4.78877469e+05, 4.43038625e+05, 4.33939875e+05, 3.99981406e+05, 3.69934188e+05, 3.68228812e+05, 3.39293906e+05, 3.13778531e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.19420781e+05, 3.13778531e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.85405188e+05, 3.85303781e+05, 3.85421219e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.85405188e+05, 3.82052438e+05, 3.88718531e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.00358281e+05, 4.61460969e+05, 4.27065250e+05, 4.17991094e+05, 3.85405188e+05, 3.56577375e+05, 3.54678188e+05, 3.26927000e+05, 3.02435781e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.00358281e+05, 3.02435781e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1934491450), # 1.93GB, avg file size 1.93GB
  ("fsize_db",                        22924430937), # 22.92GB, avg file size 1.27GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_9_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToHHTo2B2Tau_node_12_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_12_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99989469e+05, 4.00041500e+05, 3.99952000e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.09963125e+05, 4.84459062e+05, 4.59889625e+05, 4.21089906e+05, 3.99988750e+05, 3.79656125e+05, 3.53863594e+05, 3.36081281e+05, 3.18978719e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.09963125e+05, 3.18978719e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.87784531e+05, 3.87792438e+05, 3.87776469e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.87784531e+05, 3.84878938e+05, 3.90625969e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.94284312e+05, 4.69697031e+05, 4.45988000e+05, 4.08130469e+05, 3.87783031e+05, 3.68168938e+05, 3.42963281e+05, 3.25823406e+05, 3.09321750e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.94284312e+05, 3.09321750e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1717419913), # 1.72GB, avg file size 1.72GB
  ("fsize_db",                        21176117597), # 21.18GB, avg file size 2.12GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_12_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToHHTo2B2Tau_node_cHHH0_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH0_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH0_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    57),
  ("nof_events",                      {
    'Count'                                                                          : [ 971000, ],
    'CountWeighted'                                                                  : [ 9.13836141e+05, 9.13942500e+05, 9.13952750e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.05700919e+06, 1.03854241e+06, 1.02556672e+06, 9.34674125e+05, 9.13836172e+05, 8.97202531e+05, 8.28919344e+05, 8.07536297e+05, 7.89292828e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.09459139e+06, 7.70815594e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.13890375e+05, 9.13364734e+05, 1.30104916e+06, 9.13877344e+05, 9.13414609e+05, 5.65749398e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 6.22237607e+04, 6.21922490e+04, 8.86536484e+04, 6.22260049e+04, 6.22657070e+04, 3.85244043e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 8.90456422e+05, 8.90461125e+05, 8.90568547e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 8.90456422e+05, 8.84702391e+05, 8.96050281e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.02956909e+06, 1.01182080e+06, 9.99389047e+05, 9.10513625e+05, 8.90456422e+05, 8.74419906e+05, 8.07557047e+05, 7.86929812e+05, 7.69326344e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.06622527e+06, 7.51307094e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 8.90598328e+05, 8.89757609e+05, 1.26758209e+06, 8.90342250e+05, 8.90379828e+05, 5.51484516e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 6.06188574e+04, 6.05657871e+04, 8.63481914e+04, 6.06041719e+04, 6.06776963e+04, 3.75406143e+04, ],
  }),
  ("nof_tree_events",                 971000),
  ("nof_db_events",                   971000),
  ("fsize_local",                     4001836608), # 4.00GB, avg file size 1.00GB
  ("fsize_db",                        49243258644), # 49.24GB, avg file size 863.92MB
  ("use_it",                          True),
  ("xsection",                        0.00489315),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_cHHH0_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToHHTo2B2Tau_node_cHHH1_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH1_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH1_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    64),
  ("nof_events",                      {
    'Count'                                                                          : [ 973400, ],
    'CountWeighted'                                                                  : [ 8.72441547e+05, 8.72386031e+05, 8.72543719e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 9.93271484e+05, 9.77529641e+05, 9.67159234e+05, 8.92423188e+05, 8.72435031e+05, 8.56705094e+05, 8.00947391e+05, 7.79161188e+05, 7.60897781e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.03614827e+06, 7.37494406e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.72282938e+05, 8.72433281e+05, 1.24285297e+06, 8.72655797e+05, 8.70852172e+05, 5.39005031e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.90874873e+04, 2.90914180e+04, 4.14843779e+04, 2.90964863e+04, 2.90848711e+04, 1.79751489e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 8.49014562e+05, 8.48946547e+05, 8.49115547e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 8.49014562e+05, 8.43322781e+05, 8.54573953e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 9.66266859e+05, 9.51169562e+05, 9.41274625e+05, 8.68265531e+05, 8.49001906e+05, 8.33890578e+05, 7.79323516e+05, 7.58320125e+05, 7.40712047e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.00803711e+06, 7.17913359e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 8.48978016e+05, 8.48754422e+05, 1.20937341e+06, 8.49104109e+05, 8.47890562e+05, 5.24756156e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.83036816e+04, 2.82956553e+04, 4.03591172e+04, 2.83050708e+04, 2.83120762e+04, 1.74955657e+04, ],
  }),
  ("nof_tree_events",                 973400),
  ("nof_db_events",                   973400),
  ("fsize_local",                     4127294194), # 4.13GB, avg file size 1.03GB
  ("fsize_db",                        49904284463), # 49.90GB, avg file size 779.75MB
  ("use_it",                          True),
  ("xsection",                        0.00217899),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_cHHH1_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToHHTo2B2Tau_node_cHHH2p45_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH2p45_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH2p45_hh_2b2t"),
  ("nof_files",                       7),
  ("nof_db_files",                    69),
  ("nof_events",                      {
    'Count'                                                                          : [ 967100, ],
    'CountWeighted'                                                                  : [ 8.34919086e+05, 8.34841891e+05, 8.34961273e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 9.52075922e+05, 9.38822336e+05, 9.30357641e+05, 8.51993445e+05, 8.34903031e+05, 8.21494078e+05, 7.62676516e+05, 7.43882391e+05, 7.28054438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.00326441e+06, 6.96523438e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.34805750e+05, 8.34484227e+05, 1.19114175e+06, 8.35036305e+05, 8.33960602e+05, 5.14483156e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.27268364e+04, 1.27233019e+04, 1.81602736e+04, 1.27264570e+04, 1.27214941e+04, 7.84993109e+03, ],
    'CountWeightedL1PrefireNom'                                                      : [ 8.12460734e+05, 8.12369203e+05, 8.12556875e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 8.12460734e+05, 8.06996711e+05, 8.17782633e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 9.26107930e+05, 9.13475758e+05, 9.05468812e+05, 8.28837219e+05, 8.12442109e+05, 7.99616469e+05, 7.41994383e+05, 7.23937734e+05, 7.08726645e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.75942148e+05, 6.78045855e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 8.12500312e+05, 8.11778117e+05, 1.15883055e+06, 8.12408227e+05, 8.11870406e+05, 5.00933598e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.23841693e+04, 1.23748760e+04, 1.76642202e+04, 1.23791550e+04, 1.23817761e+04, 7.64159766e+03, ],
  }),
  ("nof_tree_events",                 967100),
  ("nof_db_events",                   967100),
  ("fsize_local",                     4117073015), # 4.12GB, avg file size 588.15MB
  ("fsize_db",                        49724444831), # 49.72GB, avg file size 720.64MB
  ("use_it",                          True),
  ("xsection",                        0.00092291),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_cHHH2p45_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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

samples_2017["/GluGluToHHTo2B2Tau_node_cHHH5_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH5_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH5_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    51),
  ("nof_events",                      {
    'Count'                                                                          : [ 974700, ],
    'CountWeighted'                                                                  : [ 9.59183406e+05, 9.59273562e+05, 9.59209016e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.14869138e+06, 1.12718748e+06, 1.11064995e+06, 9.78193859e+05, 9.59162094e+05, 9.43097750e+05, 8.42424312e+05, 8.25605109e+05, 8.10384547e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.18376122e+06, 7.93960172e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.59273719e+05, 9.59182859e+05, 1.36428491e+06, 9.59113797e+05, 9.57922406e+05, 5.94439781e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 7.82816855e+04, 7.82811621e+04, 1.11421484e+05, 7.82705723e+04, 7.82813047e+04, 4.85327041e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.37170688e+05, 9.37210391e+05, 9.37194438e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.37170688e+05, 9.31607312e+05, 9.42539406e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.12176886e+06, 1.10107009e+06, 1.08517586e+06, 9.55475203e+05, 9.37147203e+05, 9.21662750e+05, 8.22993812e+05, 8.06783156e+05, 7.92091438e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.15611075e+06, 7.76001000e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.37421484e+05, 9.36886188e+05, 1.33272688e+06, 9.36877781e+05, 9.36394219e+05, 5.81122297e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 7.64877012e+04, 7.64510137e+04, 1.08829453e+05, 7.64455469e+04, 7.65104902e+04, 4.74377227e+04, ],
  }),
  ("nof_tree_events",                 974700),
  ("nof_db_events",                   974700),
  ("fsize_local",                     3755486117), # 3.76GB, avg file size 938.87MB
  ("fsize_db",                        48118053180), # 48.12GB, avg file size 943.49MB
  ("use_it",                          True),
  ("xsection",                        0.00643758),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_cHHH5_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
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
  [ 'signal_ggf_nonresonant_node_sm_hh_2b2v',          'signal_ggf_nonresonant_node_2_hh_2b2v',           'signal_ggf_nonresonant_node_3_hh_2b2v',           'signal_ggf_nonresonant_node_7_hh_2b2v',           'signal_ggf_nonresonant_node_9_hh_2b2v',           'signal_ggf_nonresonant_node_12_hh_2b2v',           ],
  [ 'signal_ggf_nonresonant_node_sm_hh_2b2t',          'signal_ggf_nonresonant_node_2_hh_2b2t',           'signal_ggf_nonresonant_node_3_hh_2b2t',           'signal_ggf_nonresonant_node_4_hh_2b2t',           'signal_ggf_nonresonant_node_7_hh_2b2t',           'signal_ggf_nonresonant_node_9_hh_2b2t',           'signal_ggf_nonresonant_node_12_hh_2b2t',           ],
]

